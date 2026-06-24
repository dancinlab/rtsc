#!/usr/bin/env python3
"""
BK-borophene (Bilayer Kagome Borophene) QE deck builder — d_deck_always discipline baked in.

Structure (from state/fb-geom-lambda/sc-channel/light_kagome_design.md):
  bilayer kagome boron, ~P6/mmm hexagonal, a ~= 2.9-3.0 A, 6 B/cell (2 kagome sublayers x 3),
  vacuum >= 15 A out-of-plane (2D slab). Refs arXiv:2307.07137 / 2406.18165.

Disciplines baked (d_deck_always / d13 / d15 / bands):
  - B mass = 10.811 amu  (correct)
  - B pseudo = B.pbe-n-rrkjus_psl.1.0.0.UPF  (PSlibrary 1.0.0, PBE USPP, verified on summer; matches family)
  - ecutwfc=50 / ecutrho=400  (UPF suggests 43/325; padded for USPP)
  - d15 metallic SCF aids: smearing mp degauss 0.02, mixing_beta 0.3, local-TF, electron_maxstep 400
  - bands: verbosity='high' (needed for >100 kpts band parsing)
  - 2D: assume_isolated='2D' for the slab (correct vacuum electrostatics), dipole-free in-plane metal

Emits: vc-relax.in, scf.in, nscf.in (wannier mesh), bands.in + KPATH, ph.in (gamma B-B stretch probe).
"""
import os, math

HERE = os.path.dirname(os.path.abspath(__file__))

# --- geometry ---
A_ANG   = 2.95          # kagome boron lattice const (vc-relax will refine)
C_ANG   = 20.0          # out-of-plane (interlayer ~2.0 + vacuum ~18)
INTER_A = 2.00          # interlayer spacing (bilayer gap), to be relaxed
BOHR    = 1.8897259886
A_BOHR  = A_ANG * BOHR
COVERA  = C_ANG / A_ANG

# kagome sites (fractional, in-plane): edge midpoints of the hex cell
KAGOME_XY = [(0.5, 0.0), (0.0, 0.5), (0.5, 0.5)]

# bilayer: two layers centered in the cell, separated by INTER_A along z
z_mid = 0.5
dz = (INTER_A / C_ANG)
z_lo = z_mid - dz/2
z_hi = z_mid + dz/2

# AA-stacked bilayer kagome (per light_kagome_design.md: "two AA-stacked boron kagome layers")
POSITIONS = []
for (x,y) in KAGOME_XY:
    POSITIONS.append(("B", x, y, z_lo))
for (x,y) in KAGOME_XY:
    POSITIONS.append(("B", x, y, z_hi))

NAT = len(POSITIONS)   # 6
PREFIX = "bkboro"
PSEUDO = "B.pbe-n-rrkjus_psl.1.0.0.UPF"   # downloaded -> renamed B.UPF on summer; use real name
B_MASS = 10.811

def cell_block():
    # hexagonal: ibrav=4, celldm(1)=a(bohr), celldm(3)=c/a
    return (f"  ibrav = 4\n"
            f"  celldm(1) = {A_BOHR:.6f}\n"
            f"  celldm(3) = {COVERA:.6f}\n")

def species_block():
    return f"ATOMIC_SPECIES\n  B {B_MASS} {PSEUDO}\n"

def positions_block():
    s = "ATOMIC_POSITIONS crystal\n"
    for (sym,x,y,z) in POSITIONS:
        s += f"  {sym} {x:.6f} {y:.6f} {z:.6f}\n"
    return s

SYSTEM_COMMON = (
    "  ! BK-borophene: bilayer AA-stacked kagome boron, hexagonal ibrav=4.\n"
    "  ! 6 B/cell (2 kagome sublayers x 3 edge-midpoint sites). a~2.95A, vacuum~18A.\n"
    "  ! refs arXiv:2307.07137 / 2406.18165. light-element line-graph kagome flat band.\n"
    + cell_block() +
    f"  nat = {NAT}\n"
    "  ntyp = 1\n"
    "  ecutwfc = 50\n"
    "  ecutrho = 400\n"
    "  assume_isolated = '2D'\n"          # 2D slab electrostatics
    "  occupations = 'smearing'\n"
    "  smearing = 'mp'\n"
    "  degauss = 0.02\n"                  # d15 metallic SCF aid
)

ELECTRONS_COMMON = (
    "&electrons\n"
    "  conv_thr = 1.0d-8\n"
    "  mixing_beta = 0.3\n"              # d15
    "  mixing_mode = 'local-TF'\n"       # d15 small-gap aid
    "  electron_maxstep = 400\n"         # d15
    "  diagonalization = 'david'\n"
    "/\n"
)

def write(fn, content):
    with open(os.path.join(HERE, fn), "w") as f:
        f.write(content)
    print("wrote", fn)

# ---------- vc-relax (tight, @1atm) ----------
vc = (
    "&control\n"
    "  calculation = 'vc-relax'\n"
    f"  prefix = '{PREFIX}'\n"
    "  outdir = './out'\n"
    "  pseudo_dir = './pseudo'\n"
    "  tprnfor = .true.\n"
    "  tstress = .true.\n"
    "  verbosity = 'high'\n"
    "  forc_conv_thr = 1.0d-4\n"
    "  etot_conv_thr = 1.0d-5\n"
    "  nstep = 200\n"
    "/\n"
    "&system\n"
    + SYSTEM_COMMON +
    "/\n"
    + ELECTRONS_COMMON +
    "&ions\n  ion_dynamics = 'bfgs'\n/\n"
    "&cell\n"
    "  cell_dynamics = 'bfgs'\n"
    "  press = 0.0\n"                    # 1 atm ~ 0 GPa (ambient)
    "  press_conv_thr = 0.1\n"
    "  cell_dofree = '2Dxy'\n"           # relax only in-plane lattice (keep vacuum fixed) -> ambient 2D
    "/\n"
    + species_block()
    + positions_block() +
    "K_POINTS automatic\n  12 12 1 0 0 0\n"
)
write("vc-relax.in", vc)

# ---------- scf ----------
scf = (
    "&control\n"
    "  calculation = 'scf'\n"
    f"  prefix = '{PREFIX}'\n"
    "  outdir = './out'\n"
    "  pseudo_dir = './pseudo'\n"
    "  tprnfor = .true.\n"
    "  tstress = .true.\n"
    "  verbosity = 'high'\n"
    "/\n"
    "&system\n"
    + SYSTEM_COMMON +
    "/\n"
    + ELECTRONS_COMMON
    + species_block()
    + positions_block() +
    "K_POINTS automatic\n  16 16 1 0 0 0\n"
)
write("scf.in", scf)

# ---------- nscf (uniform mesh for wannier) ----------
nscf = (
    "&control\n"
    "  calculation = 'nscf'\n"
    f"  prefix = '{PREFIX}'\n"
    "  outdir = './out'\n"
    "  pseudo_dir = './pseudo'\n"
    "  verbosity = 'high'\n"
    "/\n"
    "&system\n"
    + SYSTEM_COMMON +
    "  nbnd = 24\n"                      # enough to capture kagome FB manifold + dispersive
    "/\n"
    + ELECTRONS_COMMON
    + species_block()
    + positions_block() +
    "K_POINTS crystal\n"                 # placeholder; wannier90 -pp writes the real list
    "  __NSCF_KPTS__\n"
)
write("nscf.in", nscf)

# ---------- bands ----------
# hex 2D path: Gamma -> M -> K -> Gamma
bands = (
    "&control\n"
    "  calculation = 'bands'\n"
    f"  prefix = '{PREFIX}'\n"
    "  outdir = './out'\n"
    "  pseudo_dir = './pseudo'\n"
    "  verbosity = 'high'\n"            # >100 kpts band parse
    "/\n"
    "&system\n"
    + SYSTEM_COMMON +
    "  nbnd = 24\n"
    "/\n"
    + ELECTRONS_COMMON
    + species_block()
    + positions_block() +
    "K_POINTS crystal_b\n"
    "  4\n"
    "  0.000000 0.000000 0.000000 40  ! Gamma\n"
    "  0.500000 0.000000 0.000000 40  ! M\n"
    "  0.333333 0.333333 0.000000 40  ! K\n"
    "  0.000000 0.000000 0.000000 1   ! Gamma\n"
)
write("bands.in", bands)

print(f"\nNAT={NAT} ntyp=1 a={A_ANG}A c={C_ANG}A interlayer={INTER_A}A")
print("layers z_lo=%.4f z_hi=%.4f" % (z_lo, z_hi))
print("pseudo:", PSEUDO, " mass:", B_MASS)
