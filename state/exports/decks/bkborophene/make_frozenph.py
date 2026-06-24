#!/usr/bin/env python3
"""
Frozen-phonon B-B bond-stretch for BK-borophene: real-DFT Omega + d eps/du (Holstein)
+ band-shift -> d t/du (SSH) for the kagome bond.

Mode probed: A1g breathing of one kagome triangle (lower layer B1,B2,B3 displaced radially
outward from triangle centroid). This stretches all 3 NN bonds of the triangle symmetrically
= the SSH-active bond-stretch mode. Symmetric => on-site 1st-order shift small (Holstein 2nd
order), hopping modulation 1st order (SSH).

Emits scf inputs at displacements u = -du,..,+du (Ang along bond) -> finite-diff:
  - E(u) curve -> harmonic Omega of the breathing mode (reduced-mass corrected)
  - band-edge shift of the kagome manifold -> d(bandwidth)/du proxy for d t/du
"""
import numpy as np

a_bohr = 6.474450
bohr = 0.529177
A1 = np.array([a_bohr,0,0]); A2 = np.array([-a_bohr/2, a_bohr*np.sqrt(3)/2,0])
c_bohr = 6.474450*5.838710  # celldm1*celldm3

# lower-layer triangle sites (fractional in-plane), z = 0.4487791773
tri = [(0.5,0.0),(0.0,0.5),(0.5,0.5)]
z_lo = 0.4487791773
z_hi = 0.5512208227

# centroid of the triangle (cartesian, using the NN images so the triangle is compact)
# B1(0.5,0)->(3.237,0); B2 image (0,0.5)+(0,-1)*A2 ; B3 image (0.5,0.5)+(0,-1)*A2
c1 = 0.5*A1 + 0.0*A2
c2 = 0.0*A1 + 0.5*A2 + (-1)*A2     # (0, -0.5)
c3 = 0.5*A1 + 0.5*A2 + (-1)*A2     # (0.5, -0.5)
cart = [c1,c2,c3]
centroid = sum(cart)/3.0
print("triangle cart (bohr):", [f"({c[0]:.3f},{c[1]:.3f})" for c in cart])
print("centroid:", centroid[:2])
# bond length check
for i in range(3):
    for j in range(i+1,3):
        print(f"  B{i+1}-B{j+1} = {np.linalg.norm(cart[i]-cart[j])*bohr:.4f} A")

# radial unit vectors (outward from centroid)
rad = [ (c-centroid)/np.linalg.norm(c-centroid) for c in cart ]
# For an equilateral triangle, moving each vertex radially out by dr changes each
# NN bond length by: d(bond) = sqrt(3)*dr  (geometry of equilateral triangle).
# So to stretch each bond by u, set dr = u/sqrt(3).

def frac_of_cart(p):
    # invert in-plane (x,y) to fractional f1,f2 on A1,A2
    M = np.array([[A1[0],A2[0]],[A1[1],A2[1]]])
    f = np.linalg.solve(M, p[:2])
    return f

du_list = [-0.06,-0.03,0.0,0.03,0.06]  # bond stretch u in Angstrom
for u in du_list:
    dr_bohr = (u/bohr)/np.sqrt(3)   # radial displacement per atom (bohr)
    newcart = [ cart[i] + dr_bohr*rad[i] for i in range(3) ]
    # map back to fractional, keep original z
    fracs=[]
    for i,p in enumerate(newcart):
        f = frac_of_cart(p)
        fracs.append((f[0],f[1]))
    tag = f"{u:+.2f}".replace("+","p").replace("-","m").replace(".","")
    fn = f"scf_u{tag}.in"
    # NOTE: B2,B3 were taken in a -A2 image; the actual fractional in the home cell:
    # we must add back the image (0,+1) to return to home-cell fractional for QE.
    # B1: image (0,0); B2: we used (0,-1) -> add (0,+1); B3: used (0,-1) -> add (0,+1)
    img_add = [(0,0),(0,1),(0,1)]
    home_fracs = [ (fracs[i][0]+img_add[i][0], fracs[i][1]+img_add[i][1]) for i in range(3) ]
    with open(fn,"w") as fo:
        fo.write(f"""&control
  calculation = 'scf'
  prefix = 'bk_u{tag}'
  outdir = './out_fp'
  pseudo_dir = './pseudo'
  verbosity = 'high'
/
&system
  ibrav = 4
  celldm(1) = 6.474450
  celldm(3) = 5.838710
  nat = 6
  ntyp = 1
  ecutwfc = 50
  ecutrho = 400
  assume_isolated = '2D'
  nbnd = 24
  occupations = 'smearing'
  smearing = 'mp'
  degauss = 0.02
/
&electrons
  conv_thr = 1.0d-9
  mixing_beta = 0.3
  mixing_mode = 'local-TF'
  electron_maxstep = 400
/
ATOMIC_SPECIES
  B 10.811 B.pbe-n-rrkjus_psl.1.0.0.UPF
ATOMIC_POSITIONS crystal
  B {home_fracs[0][0]:.8f} {home_fracs[0][1]:.8f} {z_lo:.8f}
  B {home_fracs[1][0]:.8f} {home_fracs[1][1]:.8f} {z_lo:.8f}
  B {home_fracs[2][0]:.8f} {home_fracs[2][1]:.8f} {z_lo:.8f}
  B 0.50000000 0.00000000 {z_hi:.8f}
  B 0.00000000 0.50000000 {z_hi:.8f}
  B 0.50000000 0.50000000 {z_hi:.8f}
K_POINTS automatic
  18 18 1 0 0 0
""")
    print(f"wrote {fn}  (u={u:+.3f}A, dr={dr_bohr*bohr:.4f}A/atom)")
