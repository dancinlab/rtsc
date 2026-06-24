"""
LANE 2D-LATTICES v2 — properly GAPPED topological flat bands via complex-phase NN SOC
(Ohgushi-Murakami-Nagaosa / Guo-Franz convention), reporting the gap-vs-flatness tradeoff.

Same overlap normalization as fbgeom_predictor.py: q_geom = mean|<u|u'>|^2 (kagome~0.50, Lieb~0.57).
Reports for the flattest band: <g>, width, gap-to-neighbor, isolation, FHS Chern.
Honest (d6): all numbers computed and printed.
"""
import numpy as np

def q_geom(Uf):
    return float((np.abs(Uf.conj() @ Uf.T)**2).mean())

def diag_grid(Hfun, nk, *p):
    bz = 2*np.pi*np.arange(nk)/nk
    nb = Hfun((0.0, 0.0), *p).shape[0]
    E = np.zeros((nk, nk, nb)); V = np.zeros((nk, nk, nb, nb), complex)
    for i, kx in enumerate(bz):
        for j, ky in enumerate(bz):
            w, v = np.linalg.eigh(Hfun((kx, ky), *p)); E[i, j] = w; V[i, j] = v
    return E, V, nb

def chern_band(V, b, nk):
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
    widths = E.max((0, 1)) - E.min((0, 1))
    b = int(np.argmin(widths))
    Uf = V[:, :, :, b].reshape(-1, nb)
    g = q_geom(Uf); w = float(widths[b])
    Eb = E[:, :, b]; gaps = []
    if b+1 < nb: gaps.append(float((E[:, :, b+1]-Eb).min()))
    if b-1 >= 0: gaps.append(float((Eb-E[:, :, b-1]).min()))
    gap = min(gaps) if gaps else float('inf')
    C = chern_band(V, b, nk)
    return dict(name=name, nb=nb, g=g, w=w, gap=gap, iso=gap > 1e-3, C=C)

# ---- kagome, complex-phase NN SOC (gaps the flat band) ----
def H_kagome_phase(k, t, lam):
    a1 = np.array([1., 0.]); a2 = np.array([0.5, np.sqrt(3)/2]); a3 = a2-a1
    ph = np.exp(1j*lam)
    hab = -2*t*ph*np.cos(np.dot(k, a1/2))
    hbc = -2*t*ph*np.cos(np.dot(k, a2/2))
    hca = -2*t*ph*np.cos(np.dot(k, a3/2))
    H = np.array([[0, hab, np.conj(hca)], [np.conj(hab), 0, hbc], [hca, np.conj(hbc), 0]], complex)
    return 0.5*(H + H.conj().T)

# ---- Lieb, complex-phase edge hop (gaps the central flat band -> Chern) ----
def H_lieb_phase(k, t, lam):
    kx, ky = k
    ph = np.exp(1j*lam)
    ab = -2*t*ph*np.cos(kx/2)
    ac = -2*t*np.conj(ph)*np.cos(ky/2)
    H = np.array([[0, ab, ac], [np.conj(ab), 0, 0], [np.conj(ac), 0, 0]], complex)
    return 0.5*(H + H.conj().T)

# ---- star / star-of-David (decorated honeycomb), complex SOC on triangle bonds ----
def H_star(k, t, tp, lam):
    a1 = np.array([1., 0.]); a2 = np.array([0.5, np.sqrt(3)/2])
    H = np.zeros((6, 6), complex)
    so = np.exp(1j*lam)
    for (a, b) in [(0, 1), (1, 2), (2, 0)]:
        H[a, b] = -t*so; H[b, a] = -t*np.conj(so)
    for (a, b) in [(3, 4), (4, 5), (5, 3)]:
        H[a, b] = -t*np.conj(so); H[b, a] = -t*so
    p1 = np.exp(1j*np.dot(k, a1)); p2 = np.exp(1j*np.dot(k, a2))
    H[0, 3] += -tp;        H[3, 0] += -tp
    H[1, 4] += -tp*p1;     H[4, 1] += -tp*np.conj(p1)
    H[2, 5] += -tp*p2;     H[5, 2] += -tp*np.conj(p2)
    return 0.5*(H + H.conj().T)

# ---- ruby lattice, complex SOC on triangle bonds ----
def H_ruby(k, t1, t2, lam):
    a1 = np.array([1., 0.]); a2 = np.array([0.5, np.sqrt(3)/2])
    H = np.zeros((6, 6), complex)
    so = np.exp(1j*lam)
    for (a, b) in [(0, 1), (1, 2), (2, 0)]:
        H[a, b] = -t1*so; H[b, a] = -t1*np.conj(so)
    for (a, b) in [(3, 4), (4, 5), (5, 3)]:
        H[a, b] = -t1*np.conj(so); H[b, a] = -t1*so
    p1 = np.exp(1j*np.dot(k, a1)); p2 = np.exp(1j*np.dot(k, a2))
    pairs = [(0, 3, 1.0), (1, 4, p1), (2, 5, p2), (0, 4, np.exp(1j*np.dot(k, a2-a1))),
             (1, 5, 1.0), (2, 3, np.conj(p1))]
    for a, b, ph in pairs:
        H[a, b] += -t2*ph; H[b, a] += -t2*np.conj(ph)
    return 0.5*(H + H.conj().T)

if __name__ == "__main__":
    nk = 30
    print("="*96)
    print("LANE 2D-LATTICES v2 — GAPPED topological flat bands (complex-phase SOC)")
    print("="*96)
    print("ref: kagome~0.50, Lieb~0.57.  Sweep SOC phase lam to find gap-vs-flatness sweet spot.\n")

    runs = []
    for lam in [0.05, 0.10, 0.15, 0.20, 0.30]:
        runs.append((f"kagome-ph lam={lam}", H_kagome_phase, (1.0, lam)))
    for lam in [0.10, 0.30, 0.50, np.pi/4]:
        runs.append((f"Lieb-ph lam={lam:.2f}", H_lieb_phase, (1.0, lam)))
    for lam in [0.10, 0.20, 0.30, 0.50]:
        runs.append((f"star lam={lam:.2f}", H_star, (1.0, 0.5, lam)))
    for lam in [0.10, 0.20, 0.30, 0.50]:
        runs.append((f"ruby lam={lam:.2f}", H_ruby, (1.0, 0.7, lam)))

    res = [screen(nm, Hf, nk, *pp) for nm, Hf, pp in runs]
    print(f"  {'host':<20}{'<g>':>7}{'width':>8}{'gap':>8}{'iso':>5}{'Chern':>8}  status")
    for r in res:
        iso = "Y" if r['iso'] else "n"
        topo = abs(r['C']) >= 0.5
        tag = "GAPPED-TOPO" if (r['iso'] and topo) else ("topo-touch" if topo else ("gapped-triv" if r['iso'] else "touch"))
        print(f"  {r['name']:<20}{r['g']:>7.3f}{r['w']:>8.4f}{r['gap']:>8.4f}{iso:>5}{r['C']:>+8.2f}  {tag}")

    print("\n--- GAPPED + |C|>=1, ranked by <g> (advantage = <g>/0.50 vs kagome) ---")
    win = [r for r in res if r['iso'] and abs(r['C']) >= 0.5]
    win.sort(key=lambda r: -r['g'])
    if not win:
        print("  (none)")
    for r in win:
        print(f"  {r['name']:<20} <g>={r['g']:.3f}  |C|={abs(r['C']):.0f}  gap={r['gap']:.3f}  width={r['w']:.3f}"
              f"  -> {r['g']/0.50:.2f}x kagome <g>")
    print("\n[d6] flat-band SC stiffness needs BOTH high <g> AND small width (isolated+flat).")
    print("     SOC opens gap but broadens band: report the tradeoff honestly, no single-number cherry-pick.")
