"""
L44 ③ robustness sweep (sign-free ED·c2): does D_s(C=1) > D_s(C=0) survive across
filling (density) and U? QWZ flat-band-projected attractive-Hubbard, twist-D_s.
3x3 k-mesh (9 orbitals) so higher fillings stay tractable. Same mesh both C → the
relative C=1 vs C=0 comparison is fair even if 3x3 <g> is coarse.
filling nup=ndn=1,2,3 (density 1/9,2/9,3/9) × U=-2,-4 × C=1(m=1)/C=0(m=3).
PASS = D_s(C=1)>D_s(C=0) across the board; flip at some density = real window finding.
"""
import numpy as np
from numpy.linalg import eigh
from itertools import combinations
import bisect

sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]],complex); sz=np.array([[1,0],[0,-1]],complex)

def ucell(kx,ky,m):
    d=np.array([np.sin(kx),np.sin(ky),m-np.cos(kx)-np.cos(ky)])
    w,v=eigh(d[0]*sx+d[1]*sy+d[2]*sz); return v[:,0]

def fermi_sign(occ,kremove,kadd):
    occl=sorted(occ); i=occl.index(kremove); s=(-1)**i; occl.pop(i)
    j=bisect.bisect_left(occl,kadd); return s*((-1)**j)

def gs_energy(m,U,N,nup,ndn,theta):
    ks=[(2*np.pi*ix/N,2*np.pi*iy/N) for ix in range(N) for iy in range(N)]
    Nk=len(ks); kmom=[(ix,iy) for ix in range(N) for iy in range(N)]
    uU=np.array([ucell(kx+theta/N,ky,m) for (kx,ky) in ks])
    uD=np.array([ucell(kx,ky,m) for (kx,ky) in ks])
    ups=list(combinations(range(Nk),nup)); dns=list(combinations(range(Nk),ndn))
    nU=len(ups); nD=len(dns); dim=nU*nD
    upi={s:i for i,s in enumerate(ups)}; dni={s:i for i,s in enumerate(dns)}
    H=np.zeros((dim,dim),complex); Uamp=U/Nk
    for iu,us in enumerate(ups):
        uvec=set(us)
        for idn,ds in enumerate(dns):
            dvec=set(ds); col=iu*nD+idn
            for k4 in us:
                for k1 in range(Nk):
                    if k1!=k4 and k1 in uvec: continue
                    for k3 in ds:
                        for k2 in range(Nk):
                            if k2!=k3 and k2 in dvec: continue
                            m1,m2,m3,m4=kmom[k1],kmom[k2],kmom[k3],kmom[k4]
                            if (m1[0]+m2[0]-m3[0]-m4[0])%N or (m1[1]+m2[1]-m3[1]-m4[1])%N: continue
                            amp=sum(np.conj(uU[k1][o])*uU[k4][o]*np.conj(uD[k2][o])*uD[k3][o] for o in range(2))
                            if amp==0: continue
                            if k1!=k4:
                                nu=sorted(list(us)+[k1]); nu.remove(k4); nu=tuple(nu); s1=fermi_sign(us,k4,k1)
                            else: nu=us; s1=1
                            if k2!=k3:
                                nd=sorted(list(ds)+[k2]); nd.remove(k3); nd=tuple(nd); s2=fermi_sign(ds,k3,k2)
                            else: nd=ds; s2=1
                            if nu not in upi or nd not in dni: continue
                            H[upi[nu]*nD+dni[nd],col]+=Uamp*amp*s1*s2
    return np.linalg.eigvalsh((H+H.conj().T)/2)[0].real

def Ds(m,U,N,n,th=0.3):
    return 2*(gs_energy(m,U,N,n,n,th)-gs_energy(m,U,N,n,n,0.0))/th**2

N=3
print("="*64)
print("[L44 ③ robustness] QWZ flat-Chern attractive-U D_s, 3x3 k, sign-free ED")
print("  filling n_pair × U × Chern. PASS = D_s(C=1)>D_s(C=0) 전구간")
print("="*64)
print("%6s %5s | %10s %10s | %s" % ("npair","U","D_s(C=1)","D_s(C=0)","ratio C1/C0"))
allpass=True
for U in [-2.0,-4.0]:
    for n in [1,2,3]:
        d1=Ds(1.0,U,N,n); d0=Ds(3.0,U,N,n)
        r=d1/d0 if abs(d0)>1e-9 else float('nan')
        flag="" if d1>d0 else "  <-- FLIP!"
        if d1<=d0: allpass=False
        print("%6d %5.1f | %10.4f %10.4f | %.2f%s" % (n,U,d1,d0,r,flag))
print("-"*64)
print("[VERDICT] %s" % ("ALL PASS: C=1>C=0 전 밀도·U → ③ 강건" if allpass else "일부 FLIP: 위상이점 밀도/U 의존(window)"))
print("[d6] 3x3 k 유한크기·이상화 QWZ·flatband proj. 무부호(ED). 절대값아닌 C1 vs C0 상대.")
