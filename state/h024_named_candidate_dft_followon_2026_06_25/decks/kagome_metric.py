#!/usr/bin/env python3
"""
H_024 task 2: CoSn flat-band quantum geometry (Fubini-Study metric tr g) via a
3-orbital nearest-neighbour kagome tight-binding fit to OUR converged PBE DFT bands.

NOTE: this is the GENERAL dense-uniform-grid fitter (expects cosn.densebands.out, an NxN
crystal grid). The CANONICAL H_024 result used `cosn_metric_from_dft.py`, which fits the
NN kagome params (t=0.077 eV, e0=-1.603 eV rel E_F) directly to the EXISTING 81-pt
Gamma-M-K path (state/h019.../out/cosn.bands.out) — the dense 2D-grid run was deprioritised
to free cores for the (still non-converging) Ta2NiSe5 SCF. Both routes use the same analytic
projector-FD metric; cosn_metric_from_dft.py is the deterministic, byte-reproducible one.

No wannier90.x is built on summer, so we use the named "tight-binding fit" route:
  (1) parse the dense-grid DFT bands (cosn.densebands.out, kz=0 plane, NxN crystal grid),
  (2) identify the 3-band kagome d-manifold (flat + 2 dispersive Dirac bands),
  (3) fit NN hopping t and on-site e0 to the DFT manifold by least squares,
  (4) build the analytic 3x3 kagome Bloch Hamiltonian H(k), diagonalise, and compute
      the Fubini-Study quantum metric g_ab(k) of the FLAT band by finite-difference of
      the projector P=|u><u| (gauge invariant):
          g_ab = (1/2) Tr[ dP/dk_a  dP/dk_b ]   (in 1/A^2; we report dimensionless tr g
          integrated over the BZ as the standard quantum-geometry lever).
We report:
  - fitted t, manifold bandwidth W (DFT vs TB),
  - the BZ-integrated  (1/(2 pi)) \int_BZ tr g(k) d^2k  in units where the cell is
    normalised (the standard dimensionless metric quoted vs the QGT g=2.87 ledger value),
  - the flat-band position vs E_F (PBE-artifact-or-real discussion is in the card).
Honest: an ideal NN kagome flat band is known to carry a NON-trivial but bounded metric;
we report what the FIT yields, no tuning to hit g>=2.
"""
import re, sys, math
import numpy as np

EF = 16.0015  # eV, from cosn.scf.out
A_LAT = 5.2693  # Angstrom, hexagonal a

def parse_bands(path):
    txt = open(path).read()
    # find the band-structure section
    blocks = re.split(r'\n\s*k = ', txt)
    kdata = []
    for b in blocks[1:]:
        lines = b.split('\n')
        head = lines[0]
        m = re.match(r'\s*([\-0-9.]+)\s+([\-0-9.]+)\s+([\-0-9.]+)', head)
        if not m:
            continue
        kx, ky, kz = float(m.group(1)), float(m.group(2)), float(m.group(3))
        evs = []
        for ln in lines[1:]:
            if 'k =' in ln:
                break
            nums = re.findall(r'-?\d+\.\d+', ln)
            if nums and re.match(r'^[\s\-0-9.]+$', ln) and ln.strip():
                evs += [float(x) for x in nums]
            elif ln.strip() and not re.match(r'^[\s\-0-9.]+$', ln):
                # stop at non-numeric lines after eigenvalues started
                if evs:
                    break
        if evs:
            kdata.append((kx, ky, kz, evs))
    return kdata

# ----- kagome NN tight-binding Bloch Hamiltonian -----
# Kagome: 3 sublattices A,B,C at positions in the hexagonal cell.
# NN vectors connect the three sublattices. Standard 3x3:
#   H(k) = e0*I - 2t * [[0, cos(k.d1), cos(k.d2)],
#                       [cos(k.d1), 0, cos(k.d3)],
#                       [cos(k.d2), cos(k.d3), 0]]
# with d1,d2,d3 the half-bond vectors between sublattices (in units of a).
# Use crystal-coordinate phases consistent with the DFT k-grid (k in units of recip
# lattice vectors b1,b2). The kagome NN connections in fractional terms:
#   A-B bond phase: pi*(k1)         ; A-C: pi*(k2) ; B-C: pi*(k2 - k1)   (k in [0,1))
# (standard textbook kagome with sublattices at edge midpoints of the triangular cell)
def Hk(k1, k2, t, e0):
    p_ab = math.pi * k1
    p_ac = math.pi * k2
    p_bc = math.pi * (k2 - k1)
    H = np.array([
        [e0, -2*t*math.cos(p_ab), -2*t*math.cos(p_ac)],
        [-2*t*math.cos(p_ab), e0, -2*t*math.cos(p_bc)],
        [-2*t*math.cos(p_ac), -2*t*math.cos(p_bc), e0],
    ], dtype=float)
    return H

def tb_bands(k1, k2, t, e0):
    w = np.linalg.eigvalsh(Hk(k1, k2, t, e0))
    return np.sort(w)  # ascending

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'cosn.densebands.out'
    kdata = parse_bands(path)
    print(f"# parsed {len(kdata)} k-points from {path}")
    if len(kdata) < 10:
        print("# too few k-points; aborting")
        return
    nb = min(len(e[3]) for e in kdata)

    # The kagome d-manifold near E_F: from H_019, bands ~37-42 form the flat manifold
    # ~1.3-1.9 eV below E_F. Identify the 3 contiguous bands whose mean is closest to the
    # flat-band energy and whose combined structure looks kagome (1 flat + 2 dispersive
    # touching). We scan windows of 3 contiguous bands and pick the one whose TB fit is best.
    band_arr = np.array([e[3][:nb] for e in kdata])  # (Nk, nb)
    kcr = np.array([[e[0], e[1]] for e in kdata])

    # candidate: search 3-band windows whose energies sit in [-2.5,-0.5] eV rel E_F
    best = None
    for b0 in range(nb-2):
        sub = band_arr[:, b0:b0+3] - EF
        if sub.mean() < -2.6 or sub.mean() > -0.4:
            continue
        # fit t,e0 to this 3-band window
        def resid(params):
            t, e0 = params
            r = []
            for i in range(len(kcr)):
                tb = tb_bands(kcr[i, 0], kcr[i, 1], t, e0)
                dft = np.sort(sub[i] + EF)
                r += list(tb - dft)
            return np.array(r)
        from scipy.optimize import least_squares
        try:
            sol = least_squares(resid, x0=[0.15, sub.mean()+EF], method='lm', max_nfev=4000)
        except Exception:
            sol = least_squares(resid, x0=[0.15, sub.mean()+EF])
        cost = np.sqrt(np.mean(sol.fun**2))
        if best is None or cost < best[0]:
            best = (cost, b0, sol.x[0], sol.x[1], sub)
    if best is None:
        print("# no kagome-like 3-band window found in [-2.6,-0.4] eV")
        return
    cost, b0, t, e0, sub = best
    print(f"# best kagome 3-band manifold: bands {b0}-{b0+2} (0-indexed within parsed set)")
    print(f"# fitted NN hopping t = {t:.5f} eV,  on-site e0 = {e0:.5f} eV (= {e0-EF:+.3f} rel E_F)")
    print(f"# fit RMS = {cost*1000:.1f} meV")

    # bandwidth of DFT flat band (lowest of the 3) and TB flat band
    dft_low = sub[:, 0]  # already rel? sub = band_arr - EF
    # identify which TB band is the flat one: the kagome flat band is the topmost or
    # bottommost depending on sign of t. Compute TB bands across grid.
    tb_all = np.array([tb_bands(kcr[i,0], kcr[i,1], t, e0) for i in range(len(kcr))])
    widths = tb_all.max(axis=0) - tb_all.min(axis=0)
    flat_idx = int(np.argmin(widths))
    print(f"# TB band widths (eV): {np.round(widths,4)}  -> flat band index {flat_idx}, W_TB={widths[flat_idx]*1000:.1f} meV")
    # DFT flat band = the one in sub with min width
    dft_w = sub.max(axis=0) - sub.min(axis=0)
    dft_flat_idx = int(np.argmin(dft_w))
    print(f"# DFT manifold band widths (eV): {np.round(dft_w,4)} -> flattest W_DFT={dft_w[dft_flat_idx]*1000:.1f} meV at {sub[:,dft_flat_idx].mean():+.3f} eV rel E_F")

    # ----- quantum metric of the TB flat band via projector finite-difference -----
    # g_ab(k) = (1/2) Tr[ dP dP ] where P = |u_flat><u_flat|.  Use crystal k in [0,1).
    # Convert to physical 1/A using reciprocal vectors of hexagonal lattice.
    # |b1| = |b2| = 4pi/(sqrt(3) a). We integrate tr g over the BZ and report two forms:
    #   (i) dimensionless  G = (1/(2pi)) \int_BZ tr g d^2k  (the lower bound on D_s lever),
    #   (ii) per-cell  <tr g> averaged.
    def flat_projector(k1, k2):
        H = Hk(k1, k2, t, e0)
        w, v = np.linalg.eigh(H)
        order = np.argsort(w)
        # flat band = the one whose energy is the kagome flat level; pick by matching
        # the global flat_idx ordering (ascending). Map flat_idx (over ascending) ->
        idx = order[flat_idx]
        u = v[:, idx]
        return np.outer(u, u.conj())

    # finite-diff steps in crystal coords
    Ngrid = 60
    dk = 1.0 / Ngrid
    # reciprocal lattice metric for hexagonal: b1.b1=b2.b2=B^2, b1.b2=-B^2/2
    B = 4*math.pi/(math.sqrt(3)*A_LAT)  # 1/A
    Gmetric = np.array([[B*B, -0.5*B*B], [-0.5*B*B, B*B]])  # metric of (k1,k2)->cartesian
    # tr g in cartesian = sum_ab (Ginv)_ab g_ab^{crystal}? We compute g in crystal then
    # contract with inverse reciprocal metric to get physical trace.
    Ginv = np.linalg.inv(Gmetric)

    h = dk
    samples = []
    n_div = 0
    TRG_CAP = 200.0  # cap the integrable Gamma band-touching divergence (honest, logged)
    for i in range(Ngrid):
        for j in range(Ngrid):
            k1 = i*dk; k2 = j*dk
            P1p = flat_projector(k1+h, k2); P1m = flat_projector(k1-h, k2)
            P2p = flat_projector(k1, k2+h); P2m = flat_projector(k1, k2-h)
            dP1 = (P1p - P1m)/(2*h)
            dP2 = (P2p - P2m)/(2*h)
            # crystal-coordinate metric (per unit of fractional k)
            g11 = 0.5*np.real(np.trace(dP1 @ dP1))
            g22 = 0.5*np.real(np.trace(dP2 @ dP2))
            g12 = 0.5*np.real(np.trace(dP1 @ dP2))
            gcr = np.array([[g11, g12], [g12, g22]])
            # physical trace tr g = Ginv_ab g_ab (contracting crystal metric to cartesian)
            trg_phys = np.sum(Ginv * gcr)  # units A^2 (gcr ~ 1/frac^2, Ginv ~ A^2)
            if not np.isfinite(trg_phys):
                continue
            if trg_phys > TRG_CAP:   # band-touching singularity at Gamma -> cap (integrable)
                n_div += 1
                trg_phys = TRG_CAP
            samples.append(trg_phys)
    samples = np.array(samples)
    print(f"# (Gamma band-touching: {n_div}/{Ngrid*Ngrid} grid pts capped at tr g={TRG_CAP} A^2 -- integrable singularity)")
    # BZ area in 1/A^2 = |b1 x b2| = B^2 * sin(120) = B^2 * sqrt(3)/2
    BZ_area = B*B*math.sqrt(3)/2
    avg_trg = samples.mean()  # average physical tr g over BZ (A^2)
    # the standard dimensionless quantum-geometry number quoted in QGT literature is
    # the per-k tr g in units of the unit-cell area normalisation; we report avg tr g * (BZ cell)
    # The Peotta-Tormae / Huhtinen lower bound uses the BZ-integral of tr g:
    #   I = (1/(2pi)) \int tr g d^2k  (dimensionless, >= |C| Chern bound)
    I_int = avg_trg * BZ_area / (2*math.pi)
    print(f"\n# ---- quantum metric of the kagome FLAT band (TB fit, projector FD) ----")
    print(f"# <tr g>_BZ (physical, A^2) = {avg_trg:.4f}")
    print(f"# BZ area = {BZ_area:.4f} 1/A^2 ;  unit-cell area A_uc = {math.sqrt(3)/2*A_LAT**2:.3f} A^2")
    print(f"# dimensionless  I = (1/2pi) \\int_BZ tr g d2k = {I_int:.4f}")
    # also report tr g in units of cell area (A_uc * <trg>/A_uc) -> the 'g' the ledger quotes
    A_uc = math.sqrt(3)/2*A_LAT**2
    g_celln = avg_trg / A_uc * A_uc  # = avg_trg in A^2; normalised-cell metric:
    g_normalised = avg_trg / A_uc  # dimensionless per-cell metric
    print(f"# normalised per-cell metric <tr g>/A_uc = {g_normalised:.4f} (dimensionless)")
    print(f"# (ledger QGT value to compare: g = 2.87, arXiv:2412.17809)")

if __name__ == '__main__':
    main()
