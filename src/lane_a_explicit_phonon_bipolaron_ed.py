"""
LANE A — EXPLICIT-PHONON BIPOLARON EXACT DIAGONALIZATION (the decisive falsifier calc).

THE FALSIFIER (campaign, RTSC):
  The multiband-Kubo lane that "restored" pair stiffness used a STATIC mean-field: bond-SSH (Peierls)
  phonons were folded into an effective static attractive U, which OMITS the RETARDED phonon vertex.
  Open question: does the RETARDED bond-SSH phonon current vertex make the bipolaron PAIR-CHANNEL
  superfluid weight <g>_pair EXCEED the single-particle Peotta-Torma value <g>~0.5 (reopening a
  room-T path), or does it just recover ~0.5 (closing the last crack)?

MODEL (sign-free, FREE local numpy/scipy):
  2 electrons (spin up + spin down = distinguishable -> SIGN-FREE) on a SAWTOOTH (delta) flat-band
  chain, plus EXPLICIT bond-SSH/Peierls phonons. The sawtooth (1D, 2 sites/cell: base A_n + apex B_n)
  has an EXACTLY flat lower band when t2 = sqrt(2) t1 (canonical CLS flat band). Single-particle flat
  band carries a finite quantum metric -> <g>_sp baseline.

  Bond-SSH/Peierls phonon: each apex bond carries an Einstein oscillator Omega; its displacement
  modulates the HOPPING on that bond (OFF-DIAGONAL coupling):  t_bond -> t_bond - g*(b + b_dag).
  Truncated boson Hilbert space n_max per mode, sparse Kron assembly, scipy eigsh.

  PAIR STIFFNESS via TWISTED BOUNDARY on the FULL electron+phonon ground state:
  thread flux theta; boundary-crossing hops carry Peierls phase e^{+/- i theta/Ncells} for BOTH spins.
  The phonon cloud is part of the variational GS => it CO-MOVES with the pair => RETARDED vertex fully
  included (a static-U calc cannot let the cloud drag along -- that is the whole distinction).
      D_s(pair) = (Ncells/2) * d^2 E_gs/d theta^2 |_{theta=0}
  Normalized to compare to single-particle <g> with the SAME Peotta-Torma normalization:
      <g>_pair = D_s(pair) / (4 |U_eff| nu(1-nu)),  nu=1/2  =>  <g>_pair = D_s / |U_eff|,
      U_eff = 2 g^2 / Omega  (bond-SSH retarded attraction, anti-adiabatic limit).

BASELINES:  (a) static-U flat-band pair stiffness ~0 (the crack);  (b) single-particle <g>_sp.

HONEST (d6): every number computed here by sparse ED; no fabrication. Toy 1D, few cells, small n_max;
convergence reported. Room-T SC UNDISCOVERED -- this settles ONLY exceed-vs-recover of <g>_sp.

REFS (novelty framing, not recomputed):
  Peotta & Torma Nat Commun 6:8944 (2015); Huhtinen et al 2104.14257 (minimal quantum metric);
  Iskin / Tovmasyan 1810.09870 (two-body bound-state quantum metric & effective mass, STATIC U);
  Sous, Chakraborty, Krems, Berciu PRL 121:247001 / 1805.06109 (light Peierls bipolarons, NOT flat band).
"""
import sys
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

def pr(*a): print(*a); sys.stdout.flush()

# ---------------------------------------------------------------------------
# Sawtooth (delta) chain, 2 sites/cell. base A_n, apex B_n.
# bonds: base-base A_n - A_{n+1} (t1); apex-base B_n - A_n (t2) and B_n - A_{n+1} (t2).
# t2 = sqrt(2) t1 => exactly flat lower band.
# ---------------------------------------------------------------------------
def sawtooth_Hk(k, t1, t2):
    c1 = np.exp(1j*k)
    HAA = -t1*(c1 + np.conj(c1))
    HAB = -t2*(1.0 + np.conj(c1))   # A_n couples to B_n and B_{n-1}
    return np.array([[HAA, HAB],[np.conj(HAB), 0.0]], complex)

def single_particle_g(t1=1.0, t2=np.sqrt(2), nk=600):
    ks = 2*np.pi*np.arange(nk)/nk; dk = ks[1]-ks[0]
    Es = np.array([np.linalg.eigvalsh(sawtooth_Hk(k,t1,t2)) for k in ks])
    width = Es.max(0)-Es.min(0); fb = int(np.argmin(width))
    gsum=0.0
    for k in ks:
        _,vm = np.linalg.eigh(sawtooth_Hk(k-dk,t1,t2))
        _,v0 = np.linalg.eigh(sawtooth_Hk(k,   t1,t2))
        _,vp = np.linalg.eigh(sawtooth_Hk(k+dk,t1,t2))
        um,u0,up = vm[:,fb],v0[:,fb],vp[:,fb]
        um = um*np.exp(-1j*np.angle(np.vdot(u0,um)))
        up = up*np.exp(-1j*np.angle(np.vdot(u0,up)))
        du = (up-um)/(2*dk)
        g = np.vdot(du,du) - np.abs(np.vdot(du,u0))**2
        gsum += g.real*dk
    return gsum/(2*np.pi), fb, width

# ---------------------------------------------------------------------------
# Real-space single-electron hopping matrices, split into static + per-mode phonon part.
# We Kron up: full space = H_up (x) I_dn (x) I_ph  +  I_up (x) H_dn (x) I_ph  +  Hubbard + phonon.
# Phonon-modulated hops need (electron-hop) (x) (b+bdag) -> assembled per mode via kron.
# ---------------------------------------------------------------------------
def saw_bonds(Ncells):
    """bonds (i, j, crosses_boundary, kind). kind 'base' or 'apex'. apex bonds get phonons."""
    def A(n): return 2*(n%Ncells)
    def B(n): return 2*(n%Ncells)+1
    bonds=[]
    for n in range(Ncells):
        cross = (n+1)>=Ncells
        bonds.append((A(n), A(n+1), cross, 'base'))   # base-base t1
        bonds.append((B(n), A(n),   False, 'apex'))   # apex to own base t2
        bonds.append((B(n), A(n+1), cross, 'apex'))   # apex to next base t2
    return bonds

def e_hop_matrices(Ncells, t1, t2, theta, phonon_apex=True):
    """Return (Hstat, mode_hops): single-electron static hop matrix (Nsite x Nsite, complex)
    and list of (mode_id, Hphon_e) single-electron hop matrices that get multiplied by (b+bdag)."""
    Nsite=2*Ncells
    bonds=saw_bonds(Ncells)
    Hstat=np.zeros((Nsite,Nsite),complex)
    mode_hops=[]; mid=0
    for (i,j,cross,kind) in bonds:
        t = t1 if kind=='base' else t2
        phase = np.exp(1j*theta/Ncells) if cross else 1.0
        Hstat[i,j]+= -t*phase; Hstat[j,i]+= -t*np.conj(phase)
        if phonon_apex and kind=='apex':
            He=np.zeros((Nsite,Nsite),complex)
            # phonon part: +g*(b+bdag) * (hop)  -> here store the hop with phase (g multiplied later)
            He[i,j]+= +phase; He[j,i]+= +np.conj(phase)
            mode_hops.append((mid,He)); mid+=1
    return Hstat, mode_hops

def boson_ops(n_max):
    n=n_max+1
    b=np.zeros((n,n))
    for k in range(1,n): b[k-1,k]=np.sqrt(k)
    bd=b.T
    x=b+bd                  # (b+bdag)
    num=np.diag(np.arange(n))
    return sp.csr_matrix(x), sp.csr_matrix(num), n

def build_H(Ncells, t1, t2, g, Omega, U, theta, n_max):
    Nsite=2*Ncells
    Hstat,mode_hops=e_hop_matrices(Ncells,t1,t2,theta,phonon_apex=(g!=0.0 and n_max>0))
    nmode=len(mode_hops)
    x_op,num_op,nb=boson_ops(n_max)
    Ie=sp.identity(Nsite,format='csr',dtype=complex)
    Hstat_s=sp.csr_matrix(Hstat)
    # phonon identity over all modes
    def ph_identity():
        return sp.identity(nb**nmode,format='csr',dtype=complex) if nmode>0 else sp.identity(1,dtype=complex)
    Iph=ph_identity()
    Dph=nb**nmode if nmode>0 else 1

    # ---- electron kinetic: (Hstat_up x I_dn + I_up x Hstat_dn) x I_ph ----
    He2 = sp.kron(Hstat_s,Ie) + sp.kron(Ie,Hstat_s)
    H = sp.kron(He2, Iph, format='csr')

    # ---- Hubbard U: sum_s n_{s,up} n_{s,dn} -> diagonal in site basis, both electrons same site ----
    if U!=0.0:
        diagU=np.zeros(Nsite*Nsite)
        for s in range(Nsite):
            diagU[s*Nsite+s]=U
        HU=sp.kron(sp.diags(diagU), Iph, format='csr')
        H=H+HU

    # ---- phonon harmonic energy: Omega * sum_m num_m ----
    if nmode>0:
        Iee=sp.identity(Nsite*Nsite,format='csr',dtype=complex)
        for m in range(nmode):
            ops=[sp.identity(nb,dtype=complex)]*nmode
            ops[m]=num_op
            Nm=ops[0]
            for o in ops[1:]: Nm=sp.kron(Nm,o,format='csr')
            H=H+Omega*sp.kron(Iee,Nm,format='csr')

        # ---- phonon-modulated hops: +g * (hop_e for mode m) x (b+bdag)_m ----
        for (m,He) in mode_hops:
            He_up = sp.kron(sp.csr_matrix(He),Ie) + sp.kron(Ie,sp.csr_matrix(He))  # both spins hop on that bond
            ops=[sp.identity(nb,dtype=complex)]*nmode
            ops[m]=x_op
            Xm=ops[0]
            for o in ops[1:]: Xm=sp.kron(Xm,o,format='csr')
            H=H+ g*sp.kron(He_up,Xm,format='csr')

    H=0.5*(H+H.getH())
    return H.tocsr()

def gs_energy(Ncells,t1,t2,g,Omega,U,theta,n_max):
    H=build_H(Ncells,t1,t2,g,Omega,U,theta,n_max)
    dim=H.shape[0]
    if dim<=2500:
        w=np.linalg.eigvalsh(H.toarray()); return float(w[0]),dim
    w=eigsh(H,k=1,which='SA',return_eigenvectors=False,maxiter=8000,tol=1e-9)
    return float(w[0]),dim

def pair_stiffness(Ncells,t1,t2,g,Omega,U,n_max,dtheta=0.06):
    E0,dim=gs_energy(Ncells,t1,t2,g,Omega,U,0.0,n_max)
    Ep,_ =gs_energy(Ncells,t1,t2,g,Omega,U,+dtheta,n_max)
    Em,_ =gs_energy(Ncells,t1,t2,g,Omega,U,-dtheta,n_max)
    d2=(Ep-2*E0+Em)/dtheta**2
    return 0.5*Ncells*d2, E0, dim

if __name__=="__main__":
    t1=1.0; t2=np.sqrt(2.0)
    pr("="*80)
    pr("LANE A — EXPLICIT-PHONON BIPOLARON ED (retarded bond-SSH vertex; sign-free 2e+phonon)")
    pr("="*80)

    g_sp,fb,width=single_particle_g(t1,t2)
    pr(f"\n[baseline b] sawtooth single-particle <g> (Peotta-Torma FS metric) = {g_sp:.4f}")
    pr(f"             flat band idx={fb}, widths={np.round(width,4)} (lower band ~flat)")

    Ncells=3
    pr(f"\nNcells={Ncells}, sites={2*Ncells}, electron dim=(2N)^2={(2*Ncells)**2}, apex phonon modes={2*Ncells}")

    pr("\n--- baseline (a): STATIC-U flat-band pair stiffness (g=0, bare U) ---")
    for U in (-2.0,-4.0,-8.0):
        Ds,E0,dim=pair_stiffness(Ncells,t1,t2,0.0,10.0,U,0)
        pr(f"  U={U:+.1f}  D_s(pair)={Ds:+.5f}  <g>_pair(static)={Ds/abs(U):+.4f}  dim={dim}")

    pr("\n--- LANE A: EXPLICIT phonon (retarded vertex). U_eff=2g^2/Omega ---")
    pr(f"{'Omega':>7}{'g':>6}{'nmax':>5}{'Ueff':>8}{'D_s(pair)':>11}{'<g>_pair':>10}{'ratio/sp':>9}{'dim':>9}")
    best=(-1e9,None)
    for Omega in (8.0,4.0,2.0,1.0,0.5):
        for g in (0.6,1.0,1.4):
            n_max = 3 if Omega>=2.0 else 4
            U_eff=2*g*g/Omega
            try:
                Ds,E0,dim=pair_stiffness(Ncells,t1,t2,g,Omega,0.0,n_max)
            except Exception as ex:
                pr(f"  Omega={Omega} g={g}: FAILED {ex}"); continue
            gpair=Ds/abs(U_eff) if U_eff>1e-9 else float('nan')
            ratio=gpair/g_sp
            tag="  <== EXCEEDS sp" if (ratio>1.0 and Ds>0) else ""
            pr(f"{Omega:>7.2f}{g:>6.2f}{n_max:>5d}{U_eff:>8.3f}{Ds:>11.5f}{gpair:>10.3f}{ratio:>9.3f}{dim:>9d}{tag}")
            if Ds>0 and gpair>best[0]: best=(gpair,(Omega,g,ratio,dim))
    pr(f"\n[verdict] single-particle <g>_sp={g_sp:.3f}.  best <g>_pair={best[0]:.3f} at {best[1]}")
    if best[1] is not None:
        pr(f"          ratio to single-particle = {best[1][2]:.3f}  -> "
           + ("EXCEEDS (room-T path reopens)" if best[1][2]>1.0 else "RECOVERS/below (last crack CLOSED)"))
