#!/usr/bin/env python3
"""
H_015 — build graphene / hBN(n) / graphene heterostructure pw.x decks (n=0,1,2,3).

Lattice constants (CITED, NOT fabricated):
  - graphene in-plane a = 2.46 Angstrom  (e.g. Cooper et al., ISRN Cond. Matter 2012;
    standard graphite value 2.461 A)
  - hBN in-plane a = 2.504 Angstrom        (Paszkowicz et al., Appl. Phys. A 75, 431 (2002))
  - vdW interlayer spacing d = 3.35 Angstrom (graphite 3.35 A; G/hBN ~3.3-3.4 A)
  ~1.8% in-plane lattice mismatch between graphene and hBN.
  We adopt a COMMON in-plane a = 2.48 A (midpoint, ~+0.8% on graphene, ~-1% on hBN)
  and record the strain honestly. AA'-type hexagonal stacking, P1 cell (no symmetry assumed).

Geometry (hexagonal 2D cell, single AB-honeycomb basis per layer):
  Layer = 2 atoms per primitive cell at (1/3,2/3) and (2/3,1/3) fractional in-plane.
  Stack along z: bottom graphene, n hBN layers, top graphene, each separated by d=3.35 A.
  Vacuum padding >= 12 A on each side -> total c chosen accordingly.

Observable for electron-opacity: layer-resolved Lowdin charges + PDOS overlap at E_F
(projwfc post-step). Here we emit scf decks; projwfc decks emitted separately.

stdlib only.
"""
import math, os

A_GRAPHENE = 2.461
A_HBN      = 2.504
A_COMMON   = 2.48          # adopted common in-plane lattice constant (Angstrom)
D_INTER    = 3.35          # interlayer vdW spacing (Angstrom)
VACUUM     = 14.0          # vacuum padding each side (>=12 A)

# in-plane lattice vectors for hexagonal cell, |a1|=|a2|=A_COMMON, 120 deg
a1 = (A_COMMON, 0.0)
a2 = (-A_COMMON/2.0, A_COMMON*math.sqrt(3)/2.0)

# honeycomb basis fractional coords (in-plane)
BASIS = [(1.0/3.0, 2.0/3.0), (2.0/3.0, 1.0/3.0)]

PSEUDO = {
    "C": "C.pbe-n-kjpaw_psl.0.1.UPF",
    "B": "B.pbe-n-kjpaw_psl.0.1.UPF",
    "N": "N.pbe-n-kjpaw_psl.0.1.UPF",
}
MASS = {"C": 12.011, "B": 10.811, "N": 14.007}

def frac_to_cart_xy(fa, fb):
    x = fa*a1[0] + fb*a2[0]
    y = fa*a1[1] + fb*a2[1]
    return x, y

def build(n_hbn):
    """Return (species_set, list of (elem, x, y, z)) for graphene/hBN(n)/graphene."""
    layers = []  # each layer: list of (elem, sublattice_index 0/1)
    # bottom graphene
    layers.append([("C", 0), ("C", 1)])
    # n hBN layers: B on sublattice 0, N on sublattice 1 (AA' would alternate; keep B/N fixed,
    # honest hexagonal BN monolayer)
    for _ in range(n_hbn):
        layers.append([("B", 0), ("N", 1)])
    # top graphene
    layers.append([("C", 0), ("C", 1)])

    nlayer = len(layers)
    # z positions: stack with D_INTER, centered, vacuum added
    span = D_INTER*(nlayer-1)
    c = span + 2*VACUUM
    z0 = VACUUM
    atoms = []
    species = set()
    for li, layer in enumerate(layers):
        z = z0 + li*D_INTER
        for (elem, sub) in layer:
            fa, fb = BASIS[sub]
            x, y = frac_to_cart_xy(fa, fb)
            atoms.append((elem, x, y, z))
            species.add(elem)
    return species, atoms, c, nlayer

def write_deck(n_hbn, outdir):
    species, atoms, c, nlayer = build(n_hbn)
    nat = len(atoms)
    ntyp = len(species)
    species = sorted(species)
    prefix = f"ghbn_n{n_hbn}"
    lines = []
    lines.append("&CONTROL")
    lines.append("  calculation = 'scf'")
    lines.append(f"  prefix = '{prefix}'")
    lines.append("  outdir = './tmp'")
    lines.append("  pseudo_dir = '/usr/share/espresso/pseudo'")
    lines.append("  verbosity = 'high'")
    lines.append("  tprnfor = .true.")
    lines.append("/")
    lines.append("&SYSTEM")
    lines.append("  ibrav = 0")
    lines.append(f"  nat = {nat}")
    lines.append(f"  ntyp = {ntyp}")
    lines.append("  ecutwfc = 50.0")
    lines.append("  ecutrho = 400.0")
    lines.append("  occupations = 'smearing'")
    lines.append("  smearing = 'mp'")
    lines.append("  degauss = 0.02")
    lines.append("  vdw_corr = 'grimme-d3'")
    lines.append("/")
    lines.append("&ELECTRONS")
    lines.append("  conv_thr = 1.0d-6")
    lines.append("  mixing_beta = 0.3")
    lines.append("  electron_maxstep = 200")
    lines.append("/")
    lines.append("ATOMIC_SPECIES")
    for s in species:
        lines.append(f"  {s}  {MASS[s]:.3f}  {PSEUDO[s]}")
    lines.append("CELL_PARAMETERS angstrom")
    lines.append(f"  {a1[0]:.8f}  {a1[1]:.8f}  0.00000000")
    lines.append(f"  {a2[0]:.8f}  {a2[1]:.8f}  0.00000000")
    lines.append(f"  0.00000000  0.00000000  {c:.8f}")
    lines.append("ATOMIC_POSITIONS angstrom")
    for (elem, x, y, z) in atoms:
        lines.append(f"  {elem}  {x:.8f}  {y:.8f}  {z:.8f}")
    lines.append("K_POINTS automatic")
    lines.append("  12 12 1 0 0 0")
    lines.append("")
    path = os.path.join(outdir, f"{prefix}.scf.in")
    with open(path, "w") as f:
        f.write("\n".join(lines))
    return path, nat, c, nlayer

if __name__ == "__main__":
    outdir = os.path.dirname(os.path.abspath(__file__)) + "/decks"
    os.makedirs(outdir, exist_ok=True)
    print(f"common a = {A_COMMON} A  (graphene {A_GRAPHENE}, hBN {A_HBN}; mismatch "
          f"{100*(A_HBN-A_GRAPHENE)/A_GRAPHENE:.2f}%)")
    print(f"interlayer d = {D_INTER} A, vacuum {VACUUM} A each side")
    for n in (0, 1, 2, 3):
        p, nat, c, nl = write_deck(n, outdir)
        print(f"n={n}: {nl} layers, nat={nat}, c={c:.3f} A -> {os.path.basename(p)}")
