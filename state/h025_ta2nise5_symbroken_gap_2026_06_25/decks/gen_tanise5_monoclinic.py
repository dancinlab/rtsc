#!/usr/bin/env python3
# Generate the LOW-T MONOCLINIC C2/c (#15) Ta2NiSe5 cell (the excitonic-insulator
# GROUND STATE) for a Quantum ESPRESSO pw.x SCF.
#
# Physical rationale (H_025): the high-symmetry Cmcm parent SCF does not converge
# (10 recipes, H_019+H_024) because it is the near-metallic excitonic-PARENT at the
# cusp of the gap-opening. The ACTUAL ground state is the symmetry-broken monoclinic
# C2/c phase (beta 90 -> 90.53 deg + small Ta/Se chain-axis shifts), in which the
# valence and conduction bands belong to the same irrep along Gamma-Z and a gap opens
# by hybridization. We build THAT cell and run plain PBE; the broken-symmetry cell is
# expected to converge where the metallic parent oscillates.
#
# EXPERIMENTAL structure: Sunshine & Ibers, Inorg. Chem. 24, 3611 (1985) (room-T,
# below the 328 K transition = monoclinic phase), as tabulated in arXiv:2201.07750
# Table I/II. NO fabricated coordinates.
#
#   a = 3.496, b = 12.829, c = 15.641 Ang ; beta = 90.53 deg (unique axis b)
#   inequivalent sites (C2/c):
#     Ni  0.00000  0.70113  0.25000
#     Ta  0.99207  0.221349 0.110442
#     Se1 0.00530  0.580385 0.137979
#     Se2 0.99487  0.145648 0.950866
#     Se3 0.00000  0.327140 0.25000
#
# C2/c (#15) unique-axis-b, cell-choice-1: centering (0,0,0)+(1/2,1/2,0); 4 point ops:
#   (x,y,z) ; (-x,y,1/2-z) ; (-x,-y,-z) ; (x,-y,1/2+z)
import math

a, b, c = 3.496, 12.829, 15.641
beta_deg = 90.53
beta = math.radians(beta_deg)

# inequivalent sites
sites = {
    'Ni':  [(0.00000, 0.70113,  0.25000)],
    'Ta':  [(0.99207, 0.221349, 0.110442)],
    'Se':  [(0.00530, 0.580385, 0.137979),
            (0.99487, 0.145648, 0.950866),
            (0.00000, 0.327140, 0.25000)],
}

def ops(x, y, z):
    return [
        ( x,  y,        z),
        (-x,  y, 0.5 -  z),
        (-x, -y,       -z),
        ( x, -y, 0.5 +  z),
    ]
cent = [(0.0, 0.0, 0.0), (0.5, 0.5, 0.0)]

def wrap(v):
    return v % 1.0

out = {}
for el, wlist in sites.items():
    pts = set()
    for (x, y, z) in wlist:
        for (xx, yy, zz) in ops(x, y, z):
            for (cx, cy, cz) in cent:
                p = (round(wrap(xx + cx), 6), round(wrap(yy + cy), 6), round(wrap(zz + cz), 6))
                pts.add(p)
    out[el] = sorted(pts)

# Build CELL_PARAMETERS: unique axis b, so b is along y; beta is the a-c angle.
# Standard QE monoclinic (unique axis b) lattice vectors:
#   v1 = a (sin? ) ... use the convention: a along x tilted in x-z plane.
# QE ibrav=-12 (unique axis b): v1=(a,0,0); v2=(0,b,0); v3=(c*cos(beta),0,c*sin(beta)).
v1 = (a, 0.0, 0.0)
v2 = (0.0, b, 0.0)
v3 = (c * math.cos(beta), 0.0, c * math.sin(beta))

nat = sum(len(v) for v in out.values())

lines = []
lines.append("&CONTROL")
lines.append("  calculation = 'scf'")
lines.append("  prefix = 'tanise5m'")
lines.append("  outdir = './out_mono'")
lines.append("  pseudo_dir = './pseudo'")
lines.append("  verbosity = 'high'")
lines.append("  disk_io = 'low'")
lines.append("/")
lines.append("&SYSTEM")
lines.append("  ibrav = 0")
lines.append(f"  nat = {nat}")
lines.append("  ntyp = 3")
lines.append("  ecutwfc = 45.0")
lines.append("  ecutrho = 360.0")
lines.append("  nbnd = 165")
lines.append("  occupations = 'smearing'")
lines.append("  smearing = 'cold'")          # Marzari-Vanderbilt cold smearing
lines.append("  degauss = 0.01")
lines.append("  nspin = 1")
lines.append("/")
lines.append("&ELECTRONS")
lines.append("  conv_thr = 1.0d-6")
lines.append("  mixing_beta = 0.3")
lines.append("  mixing_mode = 'local-TF'")
lines.append("  mixing_ndim = 8")
lines.append("  electron_maxstep = 200")
lines.append("  diagonalization = 'david'")
lines.append("  diago_david_ndim = 4")
lines.append("/")
lines.append("CELL_PARAMETERS {angstrom}")
lines.append(f"  {v1[0]:.8f}  {v1[1]:.8f}  {v1[2]:.8f}")
lines.append(f"  {v2[0]:.8f}  {v2[1]:.8f}  {v2[2]:.8f}")
lines.append(f"  {v3[0]:.8f}  {v3[1]:.8f}  {v3[2]:.8f}")
lines.append("ATOMIC_SPECIES")
lines.append("  Ta 180.948 Ta.pbe-spn-rrkjus_psl.1.0.0.UPF")
lines.append("  Ni  58.693 Ni.pbe-spn-kjpaw_psl.1.0.0.UPF")
lines.append("  Se  78.971 Se.pbe-n-rrkjus_psl.1.0.0.UPF")
lines.append("ATOMIC_POSITIONS {crystal}")
counts = {}
for el in ['Ta', 'Ni', 'Se']:
    counts[el] = len(out[el])
    for p in out[el]:
        lines.append(f"  {el}  {p[0]:.6f}  {p[1]:.6f}  {p[2]:.6f}")
lines.append("K_POINTS {automatic}")
lines.append("  4 1 1 0 0 0")
lines.append("")

deck = "\n".join(lines)
with open("tanise5.mono.in", "w") as f:
    f.write(deck)

print(f"# atom counts: {counts}  (expect Ta8 Ni4 Se20 = 32)")
print(f"# total nat = {nat}")
print(f"# cell volume = {abs(v1[0]*(v2[1]*v3[2]-v2[2]*v3[1])):.4f} Ang^3 (exp mono 701.4)")
print(f"# beta = {beta_deg} deg, v3 = ({v3[0]:.4f}, 0, {v3[2]:.4f})")
print("# wrote tanise5.mono.in")
