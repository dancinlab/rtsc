"""
L44 ③ many-body 확장 (유한밀도·sign-free ED·c2). 2체→4체(2up+2dn) 유한밀도.
QWZ flat-band-projected attractive-Hubbard, twist theta로 superfluid weight D_s 직접:
  D_s = d^2 E_GS / d theta^2  (twist-energy 곡률; flat band라 kinetic=0, 순수 geometric).
C=1(m=1) vs C=0(m=3) 비교. 쌍 밀도 올려도 D_s(C=1)>D_s(C=0) 유지면 ③ many-body PASS.
projected interaction: H=-|U| sum_{R,alpha} n_{R,a,up} n_{R,a,dn}, 밴드투영.
Fock basis = (up k-occ, dn k-occ). 작은 k-mesh로 유한크기(d6). 무부호(ED).
"""
import numpy as np
from itertools import combinations

sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]],complex); sz=np.array([[1,0],[0,-1]],complex)

def ucell(kx,ky,m):
    d=np.array([np.sin(kx),np.sin(ky),m-np.cos(kx)-np.cos(ky)])
    H=d[0]*sx+d[1]*sy+d[2]*sz
    w,v=np.linalg.eigh(H); return v[:,0]   # lower band spinor (2 orbitals A,B)

def run(m, U=-3.0, Nx=4, Ny=4, nup=2, ndn=2, theta=0.0):
    # k-mesh with twist theta in x for up-spin (probe superfluid stiffness)
    ks=[(2*np.pi*ix/Nx, 2*np.pi*iy/Ny) for ix in range(Nx) for iy in range(Ny)]
    Nk=len(ks)
    # band spinors per k (twist shifts up-spin k by theta/Nx in x)
    def uarr(shift):
        return np.array([ucell(kx+shift, ky, m) for (kx,ky) in ks])  # [Nk,2]
    uU=uarr(theta/Nx); uD=uarr(0.0)
    # projected on-site density form factors: for orbital a, rho_a(k,k') = u_a(k)^* u_a(k')
    # interaction H=-|U| sum_a sum_{k1k2k3k4 : k1-k2+k3-k4=0 (mom cons)} ...
    # Build many-body in Fock basis of occupied k-modes (spinless per spin, band index fixed)
    up_states=list(combinations(range(Nk),nup)); dn_states=list(combinations(range(Nk),ndn))
    nU=len(up_states); nD=len(dn_states); dim=nU*nD
    upi={s:i for i,s in enumerate(up_states)}; dni={s:i for i,s in enumerate(dn_states)}
    # momentum index of each k
    kmom=[(ix,iy) for ix in range(Nx) for iy in range(Ny)]
    def occ_to_vec(occ,Nk):
        v=np.zeros(Nk,bool)
        for o in occ: v[o]=True
        return v
    # interaction matrix element: -|U|/Nk * sum_a u_a(k1)^* u_a(k4) u_a(k2)^* u_a(k3)
    #   scatters up: k4->k1, dn: k3->k2, with momentum cons k1+k2=k3+k4 (mod mesh).
    # We build H as dense (dim small).
    H=np.zeros((dim,dim),complex)
    Uamp=U/Nk
    # precompute orbital form factor f_a[k,k'] = conj(u_a[k])*u_a[k'] for up and dn
    def ff(uarr_):
        return np.array([[ [np.conj(uarr_[k][a])*uarr_[kp][a] for a in range(2)] for kp in range(Nk)] for k in range(Nk)])
    ffU=ff(uU); ffD=ff(uD)
    def kmomidx(k): return kmom[k]
    def addmom(a,b): return ((a[0]+b[0]), (a[1]+b[1]))
    # iterate basis
    import numpy as _np
    for iu,us in enumerate(up_states):
        for idn,ds in enumerate(dn_states):
            col=iu*nD+idn
            uvec=occ_to_vec(us,Nk); dvec=occ_to_vec(ds,Nk)
            # up scatter k4(occ)->k1(empty); dn scatter k3(occ)->k2(empty)
            for k4 in us:
                for k1 in range(Nk):
                    if k1!=k4 and uvec[k1]: continue
                    for k3 in ds:
                        for k2 in range(Nk):
                            if k2!=k3 and dvec[k2]: continue
                            # momentum conservation k1+k2 == k3+k4 (mod mesh)
                            m1=kmom[k1]; m2=kmom[k2]; m3=kmom[k3]; m4=kmom[k4]
                            if ((m1[0]+m2[0]-m3[0]-m4[0])%Nx!=0) or ((m1[1]+m2[1]-m3[1]-m4[1])%Ny!=0):
                                continue
                            amp=0j
                            for a in range(2):
                                amp+=ffU[k1][k4][a]*ffD[k2][k3][a]
                            if amp==0: continue
                            # new up occ: remove k4 add k1
                            nu=list(us)
                            if k1!=k4:
                                nu.remove(k4); nu.append(k1)
                                nu_sorted=tuple(sorted(nu))
                                # fermion sign
                                s1=fermi_sign(us,k4,k1)
                            else:
                                nu_sorted=us; s1=1
                            nd=list(ds)
                            if k2!=k3:
                                nd.remove(k3); nd.append(k2)
                                nd_sorted=tuple(sorted(nd)); s2=fermi_sign(ds,k3,k2)
                            else:
                                nd_sorted=ds; s2=1
                            if nu_sorted not in upi or nd_sorted not in dni: continue
                            row=upi[nu_sorted]*nD+dni[nd_sorted]
                            H[row,col]+=Uamp*amp*s1*s2
    w=np.linalg.eigvalsh((H+H.conj().T)/2)
    return float(w[0])

def fermi_sign(occ, kremove, kadd):
    # sign for c†_kadd c_kremove on sorted occ
    occl=sorted(occ)
    i=occl.index(kremove)
    s=(-1)**i
    occl.pop(i)
    import bisect
    j=bisect.bisect_left(occl,kadd)
    s*=(-1)**j
    return s

print("="*64)
print("[L44 ③ many-body] QWZ flat-band attractive-U twist-D_s (2up+2dn, 4x4 k)")
print("  D_s = (E(theta)-E(0))*2/theta^2 (twist 곡률). C=1 vs C=0.")
print("="*64)
th=0.3
for m,lab in [(1.0,"C=1"),(3.0,"C=0")]:
    E0=run(m,theta=0.0); Eth=run(m,theta=th)
    Ds=2*(Eth-E0)/th**2
    print("m=%.1f (%s): E0=%.4f  E(th)=%.4f  D_s=%.4f" % (m,lab,E0,Eth,Ds))
print("-"*64)
print("[해석] D_s(C=1) > D_s(C=0) 이면 ③ many-body PASS(유한밀도서도 위상이 강성↑).")
print("[d6] 2up2dn 유한밀도·4x4 k(유한크기)·flat-band projection·QWZ 2-orbital. 무부호(ED).")
