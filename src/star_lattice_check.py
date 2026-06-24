"""
ADVERSARIAL CHECK — star / star-of-David / decorated-honeycomb (6-band) flat-band host.

Independent numpy TB build (Ruegg-Fiete 2010 decorated honeycomb / star lattice).
Same <g> normalization as fbgeom_predictor.py: q_geom = mean over all (k,k') of |<u|u'>|^2,
on the FLATTEST band. Chern via FHS. Goal: is the flat band GAPPED + TOPOLOGICAL,
or gapless-touching (high overlap = artifact)?

Geometry: honeycomb (2 sites A,B) decorated -> each replaced by a triangle =>
6 sublattices per cell. Intra-triangle bond t (the triangles), inter-triangle bond tp
(the honeycomb bonds connecting triangles). SOC = imaginary intra-triangle hopping lam
(intrinsic spin-orbit, like Haldane/kagome), which gaps the band-touchings.
"""
import numpy as np

def q_geom(Uf):
    ov2 = np.abs(Uf.conj() @ Uf.T)**2
    return float(ov2.mean())

def _eig_grid(Hfun, nk, *p):
    bz = 2*np.pi*np.arange(nk)/nk
    nb = Hfun((0.0, 0.0), *p).shape[0]
    E = np.zeros((nk, nk, nb)); V = np.zeros((nk, nk, nb, nb), complex)
    for i, kx in enumerate(bz):
        for j, ky in enumerate(bz):
            w, v = np.linalg.eigh(Hfun((kx, ky), *p)); E[i, j] = w; V[i, j] = v
    return E, V

def flat_band(Hfun, nk, *p):
    E, V = _eig_grid(Hfun, nk, *p)
    widths = E.max(axis=(0,1)) - E.min(axis=(0,1)); b = int(np.argmin(widths))
    Uf = V[:, :, :, b].reshape(-1, E.shape[2])
    # gap of the flat band to nearest other band (min over BZ of energy separation)
    nb = E.shape[2]
    gaps = []
    for o in range(nb):
        if o == b: continue
        # separation could be above or below; use min |E_b - E_o| over BZ
        gaps.append(np.min(np.abs(E[:,:,b] - E[:,:,o])))
    gap = float(min(gaps)) if gaps else float('inf')
    return q_geom(Uf), float(widths[b]), gap, b, E

def chern_flat(Hfun, nk, *p):
    E, V = _eig_grid(Hfun, nk, *p)
    b = int(np.argmin(E.max(axis=(0,1)) - E.min(axis=(0,1))))
    nb = E.shape[2]; F = 0.0
    for i in range(nk):
        for j in range(nk):
            ip, jp = (i+1)%nk, (j+1)%nk
            u1=V[i,j,:,b]; u2=V[ip,j,:,b]; u3=V[ip,jp,:,b]; u4=V[i,jp,:,b]
            U1=np.vdot(u1,u2); U2=np.vdot(u2,u3); U3=np.vdot(u3,u4); U4=np.vdot(u4,u1)
            F += np.angle(U1*U2*U3*U4)
    return F/(2*np.pi)

# ---- star / decorated-honeycomb 6-band Hamiltonian (Ruegg-Fiete 2010) ----
# Honeycomb lattice vectors. Two triangles per cell: triangle A (sites 0,1,2),
# triangle B (sites 3,4,5). Intra-triangle bonds = t (with SOC phase lam).
# Inter-triangle (honeycomb) bonds = tp connecting A-site to B-site of neighbor cells.
def H_star(k, t, tp, lam):
    kx, ky = k
    a1 = np.array([3/2,  np.sqrt(3)/2])   # honeycomb Bravais vectors (decorated)
    a2 = np.array([3/2, -np.sqrt(3)/2])
    H = np.zeros((6,6), complex)
    # intra-triangle A (0,1,2) and B (3,4,5): complex hopping t*exp(i*lam phase) -> chiral
    ph = np.exp(1j*lam)
    for (a,b) in [(0,1),(1,2),(2,0)]:
        H[a,b] += -t*ph; H[b,a] += -t*np.conj(ph)
    for (a,b) in [(3,4),(4,5),(5,3)]:
        H[a,b] += -t*ph; H[b,a] += -t*np.conj(ph)
    # inter-triangle bonds (the honeycomb edges): connect A-triangle corner to B-triangle corner
    # three inter-triangle bonds per cell, one along each honeycomb direction.
    # bond 0: A site0 <-> B site3 (same cell)
    H[0,3] += -tp; H[3,0] += -tp
    # bond 1: A site1 <-> B site4 of cell shifted by a1
    p1 = np.exp(1j*np.dot(k, a1))
    H[1,4] += -tp*p1; H[4,1] += -tp*np.conj(p1)
    # bond 2: A site2 <-> B site5 of cell shifted by a2
    p2 = np.exp(1j*np.dot(k, a2))
    H[2,5] += -tp*p2; H[5,2] += -tp*np.conj(p2)
    return 0.5*(H + H.conj().T)

if __name__ == "__main__":
    nk = 36
    print("="*78)
    print("ADVERSARIAL: star / decorated-honeycomb 6-band flat-band host")
    print("="*78)
    print(f"{'lam':>6}{'<g>':>9}{'width':>10}{'gap':>11}{'Chern':>9}")
    for lam in [0.0, 0.10, 0.20, 0.30, 0.50]:
        # use t=1 (triangles), tp=1 (honeycomb); flat band emerges in this family
        g, w, gap, b, E = flat_band(H_star, nk, 1.0, 1.0, lam)
        C = chern_flat(H_star, nk, 1.0, 1.0, lam)
        print(f"{lam:>6.2f}{g:>9.3f}{w:>10.4f}{gap:>11.5f}{C:>+9.2f}")

    # kagome reference in SAME normalization for the x-kagome ratio claim
    def H_kagome_soc(k, t, lam):
        a1=np.array([1.0,0.0]); a2=np.array([0.5,np.sqrt(3)/2]); a3=a2-a1
        tab=-2*t*np.cos(np.dot(k,a1/2)); tbc=-2*t*np.cos(np.dot(k,a2/2)); tca=-2*t*np.cos(np.dot(k,a3/2))
        s1=2*lam*np.sin(np.dot(k,a1)); s2=2*lam*np.sin(np.dot(k,a2)); s3=2*lam*np.sin(np.dot(k,a3))
        H=np.array([[s1,tab,np.conj(tca)],[np.conj(tab),s2,tbc],[tca,np.conj(tbc),s3]],complex)
        return 0.5*(H+H.conj().T)
    gk, wk, gapk, bk, Ek = flat_band(H_kagome_soc, nk, 0.075, 0.020)
    Ck = chern_flat(H_kagome_soc, nk, 0.075, 0.020)
    print(f"\nkagome(SOC.02) <g>={gk:.3f} width={wk:.4f} gap={gapk:.5f} C={Ck:+.2f}")
    print("\nKEY QUESTIONS:")
    print(" 1. Is the flat band GAPPED from the dispersive bands? (gap>0 needed for isolated stiffness)")
    print(" 2. Is it TOPOLOGICAL (|C|>=1)?  3. Is <g> genuinely > kagome?")
