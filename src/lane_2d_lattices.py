"""
LANE 2D-LATTICES — screen topological flat-band lattices vs kagome/Lieb baseline.

SAME normalization as fbgeom_predictor.py:
  q_geom(Uf) = mean over all (k,k') of |<u_k|u_k'>|^2  (overlap metric, ~0.5 for kagome)
  chern_flat = FHS Chern of the FLATTEST band.

Goal: find a GAPPED (isolated) flat band with |C|>=1 that raises <g> meaningfully
above kagome/Lieb (~0.45-0.57). Honest (d6): real computed numbers only; flat-band
width reported so we can see if it is truly isolated (gapped) vs a touching band.
"""
import numpy as np

# ---- shared (copied verbatim convention from fbgeom_predictor.py) ----
def q_geom(Uf):
    ov2 = np.abs(Uf.conj() @ Uf.T)**2
    return float(ov2.mean())

def diag_grid(Hfun, nk, *p):
    bz = 2*np.pi*np.arange(nk)/nk
    nb = Hfun((0.0, 0.0), *p).shape[0]
    E = np.zeros((nk, nk, nb)); V = np.zeros((nk, nk, nb, nb), complex)
    for i, kx in enumerate(bz):
        for j, ky in enumerate(bz):
            w, v = np.linalg.eigh(Hfun((kx, ky), *p)); E[i, j] = w; V[i, j] = v
    return E, V, nb

def flat_index(E):
    widths = E.max(axis=(0, 1)) - E.min(axis=(0, 1))
    return int(np.argmin(widths)), widths

def gap_around(E, b):
    """min energy gap of band b to its neighbors over the BZ (>0 => isolated/gapped)."""
    nb = E.shape[-1]
    Eb = E[:, :, b]
    gaps = []
    if b+1 < nb: gaps.append(float((E[:, :, b+1] - Eb).min()))
    if b-1 >= 0: gaps.append(float((Eb - E[:, :, b-1]).min()))
    return min(gaps) if gaps else float('inf')

def chern_flat(Hfun, nk, *p):
    E, V, nb = diag_grid(Hfun, nk, *p)
    b, _ = flat_index(E)
    F = 0.0
    for i in range(nk):
        for j in range(nk):
            ip, jp = (i+1) % nk, (j+1) % nk
            u1 = V[i, j, :, b]; u2 = V[ip, j, :, b]; u3 = V[ip, jp, :, b]; u4 = V[i, jp, :, b]
            U1 = np.vdot(u1, u2); U2 = np.vdot(u2, u3); U3 = np.vdot(u3, u4); U4 = np.vdot(u4, u1)
            F += np.angle(U1*U2*U3*U4)
    return F/(2*np.pi)

def screen(name, Hfun, nk, *p):
    E, V, nb = diag_grid(Hfun, nk, *p)
    b, widths = flat_index(E)
    Uf = V[:, :, :, b].reshape(-1, nb)
    g = q_geom(Uf)
    w = float(widths[b])
    gap = gap_around(E, b)
    C = chern_flat(Hfun, nk, *p)
    bw_ratio = gap / (w + 1e-12)  # >1 => isolated relative to its own dispersion
    return dict(name=name, nb=nb, band=b, g=g, width=w, gap=gap,
                isolated=gap > 1e-3, bw_ratio=bw_ratio, C=C)

# ============================================================================
# BASELINES (must reproduce tool: kagome~0.50, Lieb~0.57)
# ============================================================================
def H_kagome_soc(k, t, lam):
    a1 = np.array([1.0, 0.0]); a2 = np.array([0.5, np.sqrt(3)/2]); a3 = a2 - a1
    tab = -2*t*np.cos(np.dot(k, a1/2)); tbc = -2*t*np.cos(np.dot(k, a2/2)); tca = -2*t*np.cos(np.dot(k, a3/2))
    s1 = 2*lam*np.sin(np.dot(k, a1)); s2 = 2*lam*np.sin(np.dot(k, a2)); s3 = 2*lam*np.sin(np.dot(k, a3))
    H = np.array([[s1, tab, np.conj(tca)], [np.conj(tab), s2, tbc], [tca, np.conj(tbc), s3]], complex)
    return 0.5*(H + H.conj().T)

def H_lieb(k, t):
    kx, ky = k
    return np.array([[0, -2*t*np.cos(kx/2), -2*t*np.cos(ky/2)],
                     [-2*t*np.cos(kx/2), 0, 0], [-2*t*np.cos(ky/2), 0, 0]], complex)

# ============================================================================
# NEW CANDIDATES
# ============================================================================
def H_lieb_flux(k, t, phi):
    """Lieb lattice with a magnetic pi-type flux on the square plaquette via complex
    edge phases -> gaps the central flat band and gives it a Chern number.
    Edge phase phi distributed so plaquette flux = 4*phi."""
    kx, ky = k
    e = np.exp(1j*phi)
    ab = -t*(1 + np.exp(1j*kx))*e          # corner A to edge B (x)
    ac = -t*(1 + np.exp(1j*ky))*np.conj(e) # corner A to edge C (y)
    H = np.array([[0, ab, ac],
                  [np.conj(ab), 0, 0],
                  [np.conj(ac), 0, 0]], complex)
    return H

def H_breathing_kagome(k, t1, t2, lam):
    """Breathing kagome: alternating up/down triangle hoppings t1,t2 + intrinsic SOC lam.
    The t1!=t2 breathing opens gaps; SOC topologizes the flat band."""
    a1 = np.array([1.0, 0.0]); a2 = np.array([0.5, np.sqrt(3)/2]); a3 = a2 - a1
    # up-triangle NN (t1) within cell, down-triangle (t2) with phase to neighbor cell
    p1 = np.exp(1j*np.dot(k, a1)); p2 = np.exp(1j*np.dot(k, a2)); p3 = np.exp(1j*np.dot(k, a3))
    hab = -t1 - t2*p1
    hbc = -t1 - t2*p2
    hca = -t1 - t2*p3
    s1 = 2*lam*np.sin(np.dot(k, a1)); s2 = 2*lam*np.sin(np.dot(k, a2)); s3 = 2*lam*np.sin(np.dot(k, a3))
    H = np.array([[s1, hab, np.conj(hca)],
                  [np.conj(hab), s2, hbc],
                  [hca, np.conj(hbc), s3]], complex)
    return 0.5*(H + H.conj().T)

def H_kagome_rashba(k, t, lam_i, lam_r):
    """Kagome with intrinsic SOC (lam_i) + Rashba SOC (lam_r), spinful 6-band.
    Rashba mixes spin; intrinsic SOC gaps. Flattest band among the 6."""
    # spinless kagome NN
    a1 = np.array([1.0, 0.0]); a2 = np.array([0.5, np.sqrt(3)/2]); a3 = a2 - a1
    tab = -2*t*np.cos(np.dot(k, a1/2)); tbc = -2*t*np.cos(np.dot(k, a2/2)); tca = -2*t*np.cos(np.dot(k, a3/2))
    H0 = np.array([[0, tab, np.conj(tca)], [np.conj(tab), 0, tbc], [tca, np.conj(tbc), 0]], complex)
    H0 = 0.5*(H0 + H0.conj().T)
    # intrinsic SOC (sigma_z, opposite sign for the two spins)
    s1 = 2*lam_i*np.sin(np.dot(k, a1)); s2 = 2*lam_i*np.sin(np.dot(k, a2)); s3 = 2*lam_i*np.sin(np.dot(k, a3))
    Hso = np.diag([s1, s2, s3]).astype(complex)
    I3 = np.eye(3, dtype=complex)
    # Rashba: spin-flip hop with i*lam_r between sublattices (schematic, off-diag in spin)
    R = 1j*lam_r*np.array([[0, np.cos(np.dot(k,a1/2)), -np.cos(np.dot(k,a3/2))],
                           [-np.cos(np.dot(k,a1/2)), 0, np.cos(np.dot(k,a2/2))],
                           [np.cos(np.dot(k,a3/2)), -np.cos(np.dot(k,a2/2)), 0]], complex)
    up = H0 + Hso
    dn = H0 - Hso
    H = np.block([[up, R],
                  [R.conj().T, dn]])
    return 0.5*(H + H.conj().T)

def H_star_lattice(k, t, tp, lam):
    """Star (triangle-honeycomb / star-of-David / 'star') lattice: 6 sites/cell.
    Honeycomb backbone (tp inter-triangle) + triangle bonds (t intra) + intrinsic SOC lam.
    Known to host topological flat bands when SOC opens the touching point."""
    a1 = np.array([1.0, 0.0]); a2 = np.array([0.5, np.sqrt(3)/2])
    # 6 sites: two triangles (A1A2A3) and (B1B2B3) forming a star
    H = np.zeros((6, 6), complex)
    # intra-triangle bonds (t) within each triangle, with SOC phase
    so = np.exp(1j*lam)
    for (a, b) in [(0,1),(1,2),(2,0)]:
        H[a, b] = -t*so; H[b, a] = -t*np.conj(so)
    for (a, b) in [(3,4),(4,5),(5,3)]:
        H[a, b] = -t*np.conj(so); H[b, a] = -t*so
    # inter-triangle bonds (tp) connecting the two triangles across cells
    p1 = np.exp(1j*np.dot(k, a1)); p2 = np.exp(1j*np.dot(k, a2))
    H[0, 3] += -tp;          H[3, 0] += -tp
    H[1, 4] += -tp*p1;       H[4, 1] += -tp*np.conj(p1)
    H[2, 5] += -tp*p2;       H[5, 2] += -tp*np.conj(p2)
    return 0.5*(H + H.conj().T)

def H_ruby(k, t1, t2, lam):
    """Ruby lattice: 6 sites/cell (trihexagonal-related), hosts a topological flat band
    with intrinsic SOC. t1 triangle bonds, t2 connecting bonds, lam SOC phase."""
    a1 = np.array([1.0, 0.0]); a2 = np.array([0.5, np.sqrt(3)/2])
    H = np.zeros((6, 6), complex)
    so = np.exp(1j*lam)
    # two triangles per cell with intra bonds t1
    for (a, b) in [(0,1),(1,2),(2,0)]:
        H[a, b] = -t1*so; H[b, a] = -t1*np.conj(so)
    for (a, b) in [(3,4),(4,5),(5,3)]:
        H[a, b] = -t1*np.conj(so); H[b, a] = -t1*so
    # rectangle/connecting bonds t2 between triangles (intra + across cells)
    p1 = np.exp(1j*np.dot(k, a1)); p2 = np.exp(1j*np.dot(k, a2)); p3 = np.exp(1j*np.dot(k, (a2-a1)))
    pairs = [(0,3,1.0),(1,4,p1),(2,5,p2),(0,4,p3),(1,5,1.0),(2,3,np.conj(p1))]
    for a, b, ph in pairs:
        H[a, b] += -t2*ph; H[b, a] += -t2*np.conj(ph)
    return 0.5*(H + H.conj().T)

def H_decorated_honeycomb(k, t, tp, lam):
    """Decorated honeycomb (star-of-David / triangular kagome): honeycomb where each
    site is replaced by a triangle. 6 sites/cell + intrinsic SOC. (Same family as star.)"""
    return H_star_lattice(k, t, tp, lam)

# ============================================================================
if __name__ == "__main__":
    nk = 30
    print("="*92)
    print("LANE 2D-LATTICES — topological flat-band screen (overlap <g>, FHS Chern, isolation)")
    print("="*92)
    print("baseline ref: kagome~0.50, Lieb~0.57 (tool normalization)\n")

    runs = [
        ("kagome(SOC).02",   H_kagome_soc,        (0.075, 0.020)),
        ("kagome(SOC).10",   H_kagome_soc,        (0.075, 0.100)),
        ("Lieb",             H_lieb,              (1.0,)),
        ("Lieb+flux(.5)",    H_lieb_flux,         (1.0, 0.5)),
        ("Lieb+flux(.785)",  H_lieb_flux,         (1.0, np.pi/4)),
        ("breathing-kag",    H_breathing_kagome,  (1.0, 0.6, 0.12)),
        ("breathing-kag.hi", H_breathing_kagome,  (1.0, 0.3, 0.15)),
        ("kagome+Rashba",    H_kagome_rashba,     (1.0, 0.10, 0.15)),
        ("star/SoD",         H_star_lattice,      (1.0, 0.5, 0.30)),
        ("star/SoD.hiSOC",   H_star_lattice,      (1.0, 0.5, 0.60)),
        ("ruby",             H_ruby,              (1.0, 0.7, 0.30)),
        ("ruby.hiSOC",       H_ruby,              (1.0, 0.7, 0.60)),
    ]
    res = []
    for nm, Hf, pp in runs:
        r = screen(nm, Hf, nk, *pp)
        res.append(r)

    print(f"  {'host':<18}{'nb':>3}{'<g>':>7}{'width':>8}{'gap':>8}{'iso':>5}{'Chern':>8}  status")
    for r in res:
        iso = "Y" if r['isolated'] else "n"
        topo = abs(r['C']) >= 0.5
        gapped_topo = r['isolated'] and topo
        tag = "GAPPED-TOPO" if gapped_topo else ("topo-touch" if topo else ("gapped-trivial" if r['isolated'] else "trivial/touch"))
        print(f"  {r['name']:<18}{r['nb']:>3}{r['g']:>7.3f}{r['width']:>8.4f}{r['gap']:>8.4f}{iso:>5}{r['C']:>+8.2f}  {tag}")

    print("\n--- GAPPED + |C|>=1 hosts, ranked by <g> (vs kagome 0.50 / Lieb 0.57) ---")
    winners = [r for r in res if r['isolated'] and abs(r['C']) >= 0.5]
    winners.sort(key=lambda r: -r['g'])
    if not winners:
        print("  (none cleared gapped+topological gate at these params)")
    for r in winners:
        adv = r['g']/0.50
        print(f"  {r['name']:<18} <g>={r['g']:.3f}  |C|={abs(r['C']):.0f}  gap={r['gap']:.3f}  "
              f"-> {adv:.2f}x kagome <g>  (need ~5x for room-T)")
