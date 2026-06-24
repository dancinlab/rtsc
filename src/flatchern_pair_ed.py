"""
L44 ③ high-Chern 검증 (S3-light 2D 확장·sign-free ED·c2 실측).
QWZ 2-band model H(k)=d.sigma, d=(sin kx, sin ky, m-cos kx-cos ky):
  Chern(lower)=+1 for 0<m<2, =0 for m>2.  We FLATTEN the band (ideal flat band:
keep Bloch eigenvectors |u(k)>, set kinetic energy=0) so single-particle mass=inf
(immobile). Then attractive Hubbard U binds a 2-body (up+down) pair whose ONLY way
to move is via quantum geometry (Peotta-Tormae). Pair effective mass 1/m* vs Chern:
  prescription PASS  <=>  C=1 (g>=|C|/2pi>0) gives MOBILE pair, C=0 can be immobile.
ED has NO sign problem at any flux/Chern -> bypasses the DQMC sign wall (track 3).
Pure numpy. Portable to hexa stdlib/linalg later (QFORGE hexa-native fold).
"""
import numpy as np
from numpy.linalg import eigh

sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)


def dvec(kx, ky, m):
    return np.array([np.sin(kx), np.sin(ky), m - np.cos(kx) - np.cos(ky)])


def lower_band(kx, ky, m):
    d = dvec(kx, ky, m)
    H = d[0] * sx + d[1] * sy + d[2] * sz
    w, v = eigh(H)
    return w[0], v[:, 0]   # lower energy, its eigenvector (2-spinor orbital weights)


def chern_and_metric(m, N=24):
    """FHS Chern + integrated quantum metric <g>=avg tr g over BZ (per k-point)."""
    ks = np.linspace(0, 2 * np.pi, N, endpoint=False)
    U = np.empty((N, N, 2), complex)
    for a, kx in enumerate(ks):
        for b, ky in enumerate(ks):
            _, u = lower_band(kx, ky, m)
            U[a, b] = u
    F = 0.0
    for a in range(N):
        for b in range(N):
            ap, bp = (a + 1) % N, (b + 1) % N
            u1 = np.vdot(U[a, b], U[ap, b]); u2 = np.vdot(U[ap, b], U[ap, bp])
            u3 = np.vdot(U[ap, bp], U[a, bp]); u4 = np.vdot(U[a, bp], U[a, b])
            F += np.angle(u1 * u2 * u3 * u4)
    C = F / (2 * np.pi)
    # quantum metric via overlaps: g ~ 1 - |<u(k)|u(k+dk)>|^2 over dk^2 (both dirs)
    gsum = 0.0
    dk = ks[1] - ks[0]
    for a, kx in enumerate(ks):
        for b, ky in enumerate(ks):
            _, u0 = lower_band(kx, ky, m)
            _, ux = lower_band(kx + dk, ky, m)
            _, uy = lower_band(kx, ky + dk, m)
            gxx = (1 - abs(np.vdot(u0, ux))**2) / dk**2
            gyy = (1 - abs(np.vdot(u0, uy))**2) / dk**2
            gsum += gxx + gyy            # tr g
    return C, gsum / (N * N)


def pair_invmass(m, U, N=10):
    """Flat-band-projected attractive-Hubbard 2-body pair effective inverse mass.
    Band flattened (E=0). Pair total momentum Q sectors; mobility from form factors.
    Orbitals: 2 (A,B sublattice / spinor comps). Hubbard U on each orbital site."""
    ks = [2 * np.pi * i / N for i in range(N)]
    # precompute lower-band spinor u(kx,ky): shape [N,N,2]
    u = np.empty((N, N, 2), complex)
    for a, kx in enumerate(ks):
        for b, ky in enumerate(ks):
            _, u[a, b] = lower_band(kx, ky, m)
    # 2-body in projected flat band, total momentum Q=(0,0) (band minimum of pair).
    # basis |k> = pair (k_up=k, k_dn=-k) ... use standard BCS-pair channel at Q=0:
    # H_pair[k,k'] = (U/Norb/N^2) * sum_orb conj(u[k]_o)u[k']_o * conj(u[-k]_o)u[-k']_o
    # (attractive U scatters pair k->k'; kinetic=0 flat). Lowest eval = pair binding.
    # Mobility: compare Q=0 vs small Q pair energy -> curvature.
    def pairH(Qa, Qb):
        idx = [(a, b) for a in range(N) for b in range(N)]
        M = len(idx)
        H = np.zeros((M, M), complex)
        for I, (a, b) in enumerate(idx):
            ka = ((-a) % N); kb = ((-b) % N)            # partner -k
            qa = ((Qa - a) % N); qb = ((Qb - b) % N)    # partner Q-k
            u1 = u[a, b]; u2 = u[qa, qb]
            for J, (c, d) in enumerate(idx):
                qc = ((Qa - c) % N); qd = ((Qb - d) % N)
                v1 = u[c, d]; v2 = u[qc, qd]
                # on-site U: sum over orbital o of (u1_o* v1_o)(u2_o* v2_o)
                amp = 0j
                for o in range(2):
                    amp += np.conj(u1[o]) * v1[o] * np.conj(u2[o]) * v2[o]
                H[I, J] = (U / (N * N)) * amp
        return np.linalg.eigvalsh(H)[0].real
    E0 = pairH(0, 0)
    E1 = pairH(1, 0)        # small Q step in x
    dQ = ks[1]
    invm = (E1 - E0) / dQ**2
    return E0, invm


print("=" * 70)
print("[L44 ③ high-Chern sign-free ED] QWZ flat-band attractive-Hubbard 2-body")
print("  Chern dialed by m: 0<m<2 -> C=1 ; m>2 -> C=0.  band FLATTENED (kin=0).")
print("  pair 1/m* (mobility) vs Chern/<g>: C=1 mobile = prescription PASS")
print("=" * 70)
print("%5s | %3s | %8s | %10s | %12s" % ("m", "C", "<tr g>", "2pi<g>/|C|", "pair 1/m*(U=-4)"))
for m in [1.0, 1.5, 2.5, 3.0]:
    C, g = chern_and_metric(m)
    E0, invm = pair_invmass(m, -4.0)
    bound = (2 * np.pi * g / abs(C)) if abs(C) > 0.1 else float('nan')
    print("%5.2f | %+.0f | %8.3f | %10s | %12.5f" %
          (m, round(C), g, ("%.2f" % bound if bound == bound else "  -"), invm))
print("-" * 70)
print("[해석] C=1(m=1,1.5): <g> 하한 2pi|C| 만족, pair 1/m*>0=쌍 이동가능(geometric).")
print("  C=0(m=2.5,3): <g> 작아질수 있어 pair 1/m* 작음. C=1 > C=0 이면 ③ PASS 방향.")
print("[d6] 2체(2-body) ED·flat-band projection·작은 k-mesh(유한크기). sign-free(ED).")
print("  many-body(유한밀도)는 다음. QWZ는 single-orbital-pair 근사(2-spinor as orbital).")
