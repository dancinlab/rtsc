"""
FB-GEOM 3D-HOSTS LANE — extend the L24-L38 flat-band law family to 3D flat-band hosts.

Matches the 2D tool's normalization EXACTLY:
  <g> = q_geom = mean over ALL (k,k') of |<u_k|u_k'>|^2   (overlap / Welch-bound metric)
  tc_bkt calibration anchor identical (G_REF=0.672, UOM_REF=1.08, TCOM_REF=0.0977)

3D LANE PHYSICS:
  - 2D BKT caps Tc at (pi/2) D_s (vortex unbinding). A 3D superconductor has NO BKT
    suppression: Tc is set by mean-field pairing, ~ D_s itself (no pi/2 vortex cap), and
    benefits from higher coordination z (pyrochlore z=6 vs kagome z=4).
  - The honest 3D lever vs 2D = (mean-field Tc_3D)/(BKT Tc_2D) for the SAME geometry.
    Mean-field for a flat band: k_B Tc_MF ~ D_s (Peotta-Tormae 3D), where D_s = (a^{D-2}) * (...).
    We report the lever as a multiplicative factor on the SAME calibrated Tc, derived from:
      (i)  removal of the BKT (pi/2) vortex penalty -> not a clean factor, BKT bound is an
           UPPER bound so 2D real Tc < (pi/2)Ds; 3D MF Tc ~ Ds. Conservative lever ~ pi/2 ~ 1.57.
      (ii) coordination boost z_3D/z_2D enters D_s linearly via the bandwidth->stiffness map.
  - HONEST CAVEAT (d6): 3D native flat bands (pyrochlore) are GAPLESS band-TOUCHINGS with a
    dispersive band at the BZ center (quadratic band touching). The flat band is NOT isolated
    -> D_s of the touched flat band is contaminated; geometric stiffness needs the band gapped
    (e.g. by SOC) to be trustworthy, exactly like dice in 2D. We compute width AND the gap to
    the nearest band to flag this.
"""
import numpy as np

meV2K = 11.604
G_REF, UOM_REF, TCOM_REF = 0.672, 1.08, 0.0977

def q_geom(Uf):
    ov2 = np.abs(Uf.conj() @ Uf.T)**2
    return float(ov2.mean())

def flat_band_3d(Hfun, nk, *p):
    """3D BZ grid. Returns (<g>, flat-band width, gap-to-nearest-band, band index)."""
    bz = 2*np.pi*np.arange(nk)/nk
    nb = Hfun((0.0, 0.0, 0.0), *p).shape[0]
    E = np.zeros((nk, nk, nk, nb))
    U = np.zeros((nk, nk, nk, nb, nb), complex)
    for i, kx in enumerate(bz):
        for j, ky in enumerate(bz):
            for l, kz in enumerate(bz):
                w, v = np.linalg.eigh(Hfun((kx, ky, kz), *p))
                E[i, j, l] = w
                U[i, j, l] = v
    widths = E.max(axis=(0, 1, 2)) - E.min(axis=(0, 1, 2))
    b = int(np.argmin(widths))
    Uf = U[:, :, :, :, b].reshape(-1, nb)
    # gap to nearest OTHER band (min over BZ of energy separation to adjacent bands)
    Eb = E[:, :, :, b]
    gap = np.inf
    for ob in range(nb):
        if ob == b:
            continue
        sep = np.abs(E[:, :, :, ob] - Eb)
        gap = min(gap, float(sep.min()))
    return q_geom(Uf), float(widths[b]), gap, b

def chern_slice_3d(Hfun, nk, kz_fixed, band, *p):
    """FHS Chern of the flat band on a fixed-kz 2D slice (3D topology proxy)."""
    bz = 2*np.pi*np.arange(nk)/nk
    nb = Hfun((0.0, 0.0, 0.0), *p).shape[0]
    V = np.empty((nk, nk, nb, nb), complex)
    for i, kx in enumerate(bz):
        for j, ky in enumerate(bz):
            w, v = np.linalg.eigh(Hfun((kx, ky, kz_fixed), *p))
            V[i, j] = v
    F = 0.0
    for i in range(nk):
        for j in range(nk):
            ip, jp = (i+1) % nk, (j+1) % nk
            u1 = V[i, j, :, band]; u2 = V[ip, j, :, band]
            u3 = V[ip, jp, :, band]; u4 = V[i, jp, :, band]
            U1 = np.vdot(u1, u2); U2 = np.vdot(u2, u3)
            U3 = np.vdot(u3, u4); U4 = np.vdot(u4, u1)
            F += np.angle(U1*U2*U3*U4)
    return F/(2*np.pi)

# ---------- 3D lattices ----------
def H_pyrochlore(k, t):
    """Pyrochlore: 4-site FCC basis, corner-sharing tetrahedra. NN hopping -t.
    Sublattice positions (fcc tetrahedron): standard pyrochlore basis.
    Gives 2 flat bands (top) + 2 dispersive (bottom), flat bands touch at Gamma."""
    kx, ky, kz = k
    # 4 sublattice positions of the up-tetrahedron (units of conventional cell)
    r = np.array([[0, 0, 0],
                  [0.25, 0.25, 0.0],
                  [0.25, 0.0, 0.25],
                  [0.0, 0.25, 0.25]])
    H = np.zeros((4, 4), complex)
    kv = np.array([kx, ky, kz])
    for a in range(4):
        for b in range(a+1, 4):
            d = r[a] - r[b]
            # NN within tetrahedron + image bonds (corner sharing): use cos of phase
            phase = 2*np.cos(np.dot(kv, d))  # symmetric NN combination
            H[a, b] = -t*phase
            H[b, a] = -t*phase
    return H

def H_pyrochlore_soc(k, t, lam):
    """Pyrochlore + complex (SOC-like) inter-sublattice phase to GAP the flat-band touching.
    Adds imaginary NN hopping (different phase per bond, breaking the destructive-interference
    that pins the flat band to the dispersive one) -> attempt to isolate the flat band."""
    kx, ky, kz = k
    r = np.array([[0, 0, 0],
                  [0.25, 0.25, 0.0],
                  [0.25, 0.0, 0.25],
                  [0.0, 0.25, 0.25]])
    kv = np.array([kx, ky, kz])
    H = np.zeros((4, 4), complex)
    for a in range(4):
        for b in range(a+1, 4):
            d = r[a] - r[b]
            # real NN + complex SOC term with a bond-dependent sign (chiral)
            sign = 1.0 if (a+b) % 2 == 0 else -1.0
            hop = -t*2*np.cos(np.dot(kv, d)) - 1j*sign*lam*2*np.sin(np.dot(kv, d))
            H[a, b] = hop
            H[b, a] = np.conj(hop)
    return H  # already Hermitian (H[b,a]=conj(H[a,b]))

def H_hyperkagome(k, t):
    """Hyperkagome (3D corner-sharing triangles, e.g. Na4Ir3O8): 12-site cubic basis is heavy.
    Use a reduced 6-site effective model capturing the 3D corner-sharing-triangle flat band:
    two interpenetrating kagome-like layers coupled along z."""
    kx, ky, kz = k
    # layer A kagome in xy
    a1 = np.array([1.0, 0.0]); a2 = np.array([0.5, np.sqrt(3)/2]); a3 = a2 - a1
    kxy = np.array([kx, ky])
    def kag():
        tab = -2*t*np.cos(np.dot(kxy, a1/2))
        tbc = -2*t*np.cos(np.dot(kxy, a2/2))
        tca = -2*t*np.cos(np.dot(kxy, a3/2))
        return np.array([[0, tab, np.conj(tca)],
                         [np.conj(tab), 0, tbc],
                         [tca, np.conj(tbc), 0]], complex)
    K = kag()
    H = np.zeros((6, 6), complex)
    H[:3, :3] = K
    H[3:, 3:] = K
    cz = -t*np.cos(kz/2)  # interlayer corner-sharing coupling
    for s in range(3):
        H[s, s+3] = cz
        H[s+3, s] = np.conj(cz)
    return 0.5*(H + H.conj().T)

def H_perovskite_3dlieb(k, t):
    """3D Lieb (perovskite ABO3 B-O network): cubic with 3 edge-center O sites + corner B.
    4-site cubic basis. Native 3D flat bands from the O sublattice (lines)."""
    kx, ky, kz = k
    # corner (0) coupled to 3 edge centers (x,y,z)
    fx = -2*t*np.cos(kx/2)
    fy = -2*t*np.cos(ky/2)
    fz = -2*t*np.cos(kz/2)
    H = np.array([[0, fx, fy, fz],
                  [fx, 0, 0, 0],
                  [fy, 0, 0, 0],
                  [fz, 0, 0, 0]], complex)
    return H

# ---------- law relations (IDENTICAL to 2D tool) ----------
def tc_bkt(g, Omega_meV, UOm, nu=0.5):
    TcOm = TCOM_REF * (g/G_REF) * (UOm/UOM_REF) * (4*nu*(1-nu))
    return TcOm * Omega_meV * meV2K

# 3D lever: mean-field (no BKT pi/2 vortex cap) + coordination boost.
# BKT bound Tc_2D <= (pi/2)Ds; real 2D Tc is BELOW this. 3D MF Tc ~ Ds (Peotta 2018, 3D).
# Honest lever = remove the BKT discount that the 2D anchor implicitly carries, NOT a free pi/2.
# The 2D calibration was fit to real 2D-BKT SC (MATBG etc.), which already ARE BKT-limited.
# Moving the SAME geometry to 3D removes vortex unbinding -> Tc_3D ~ Tc_2D * L3D.
def lever_3d(z_3d=6.0, z_2d=4.0):
    """Conservative 3D-vs-2D Tc multiplier.
    Two contributions, both honestly bounded:
      f_BKT  : 2D real Tc is suppressed below MF by vortex fluctuations; 3D restores ~ MF.
               For a flat band the BKT/MF ratio is geometry-dependent; literature flat-band
               QMC (2D) gives Tc_BKT ~ 0.5 Tc_MF -> f_BKT ~ 2.0 at most. Use 1.5 (conservative).
      f_z    : stiffness scales ~ coordination -> z_3d/z_2d (pyrochlore 6 / kagome 4 = 1.5).
    Total conservative lever ~ f_BKT * sqrt(f_z) (sublinear z to stay honest)."""
    f_bkt = 1.5
    f_z = np.sqrt(z_3d/z_2d)
    return f_bkt*f_z, f_bkt, f_z

if __name__ == "__main__":
    print("="*88)
    print("FB-GEOM 3D-HOSTS LANE  (pyrochlore / hyperkagome / 3D-Lieb perovskite)")
    print("  <g> normalization = mean|<u_k|u_k'>|^2 over 3D BZ (SAME as 2D tool, kagome~0.5)")
    print("="*88)
    nk = 12  # 12^3 = 1728 k-points (3D is expensive; enough for <g> + width + gap)

    hosts = [
        ("pyrochlore",     H_pyrochlore,        (1.0,)),
        ("pyrochlore+SOC", H_pyrochlore_soc,    (1.0, 0.30)),
        ("hyperkagome",    H_hyperkagome,       (1.0,)),
        ("3D-Lieb/perov",  H_perovskite_3dlieb, (1.0,)),
    ]

    print(f"\n[COMPUTE 3D] <g>, flat-band width, gap-to-nearest-band  (nk={nk}^3)")
    print(f"  {'host':<16}{'<g>':>7}{'width':>9}{'gap':>9}   isolated?")
    results = []
    for nm, Hf, pp in hosts:
        g, w, gap, b = flat_band_3d(Hf, nk, *pp)
        iso = "YES (gapped)" if gap > 1e-3 else "NO (touching)"
        results.append((nm, Hf, pp, g, w, gap, b))
        print(f"  {nm:<16}{g:>7.3f}{w:>9.4f}{gap:>9.4f}   {iso}")

    # Chern on a kz slice for the gapped host(s)
    print(f"\n[TOPOLOGY] FHS Chern of flat band on kz=0 and kz=pi slices (gapped hosts)")
    for nm, Hf, pp, g, w, gap, b in results:
        if gap > 1e-3:
            c0 = chern_slice_3d(Hf, nk, 0.0, b, *pp)
            cp = chern_slice_3d(Hf, nk, np.pi, b, *pp)
            print(f"  {nm:<16} C(kz=0)={c0:+.2f}  C(kz=pi)={cp:+.2f}")
        else:
            print(f"  {nm:<16} (band touching -> Chern ill-defined for flat band)")

    # 3D lever + Tc prediction
    L, f_bkt, f_z = lever_3d(6.0, 4.0)
    Om, UOm = 150.0, 1.5
    print(f"\n[3D LEVER] mean-field (no BKT cap) + coordination boost")
    print(f"  f_BKT (vortex-restored) = {f_bkt:.2f}   f_z (sqrt z3d/z2d=6/4) = {f_z:.2f}")
    print(f"  total 3D-vs-2D Tc lever  L_3D = {L:.2f}x")

    print(f"\n[PREDICT 3D] Tc = L_3D * calibrated-BKT  (Omega={Om:.0f} meV, U/Om={UOm}, nu=1/2)")
    print(f"  {'host':<16}{'<g>':>7}{'Tc_2D(K)':>10}{'Tc_3D(K)':>10}{'x to 293K':>11}  isolated?")
    for nm, Hf, pp, g, w, gap, b in results:
        tc2 = tc_bkt(g, Om, UOm)
        tc3 = tc2*L
        need = 293.15/tc3 if tc3 > 0 else float('inf')
        iso = "iso" if gap > 1e-3 else "TOUCH(spurious)"
        print(f"  {nm:<16}{g:>7.3f}{tc2:>10.0f}{tc3:>10.0f}{need:>11.1f}  {iso}")

    # the 5x question
    print(f"\n[5x QUESTION] does 3D give the ~5x needed for room-T?")
    print(f"  2D kagome/Lieb fell x4.7-5.6 SHORT. The 3D lever above is L_3D={L:.2f}x.")
    print(f"  => 3D ALONE provides ~{L:.1f}x, NOT the full ~5x. Closes ~{(L-1)/(5-1)*100:.0f}% of the gap.")
    print(f"  Combined with a higher-<g> isolated 3D flat band it could approach it, BUT:")
    print(f"  HONEST WALL (d6): pyrochlore native flat band is GAPLESS (touching, see gap col)")
    print(f"  -> its D_s is contaminated; only the SOC-gapped variant has trustworthy stiffness,")
    print(f"  and gapping costs <g>. No free 5x. Report L_3D as a real but partial lever.")
