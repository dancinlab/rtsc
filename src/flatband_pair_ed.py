"""
L44 검증 트랙 S3(가벼운 버전·실측 c2): flat band에서 Cooper 쌍이 움직이는가(geometric pair mass).
diamond(rhombus) chain은 E=mu의 평탄밴드(CLS=(B-C)/√2) 보유. 단일입자는 평탄밴드서 immobile(mass=∞)이나,
attractive-U로 묶인 2체(↑+↓) 쌍은 quantum-metric 덕에 ★finite mass로 움직일 수 있다(Peotta-Törmä 2체판).
2체 total-momentum Q 분해로 pair dispersion E_pair(Q) → 유효질량. 평탄밴드 vs 디튠(평탄 깨짐) 대조.
"""
import numpy as np
from numpy.linalg import eigh

def build_H1(N, t=1.0, mu=-4.0, detune=0.0):
    S=3*N
    def idx(n,a): return 3*(n%N)+a   # a: 0=A,1=B,2=C
    H=np.zeros((S,S))
    for n in range(N):
        A,B,C,An=idx(n,0),idx(n,1),idx(n,2),idx(n+1,0)
        for i,j in [(A,B),(A,C),(B,An),(C,An)]:
            H[i,j]-=t; H[j,i]-=t
        H[B,B]+=mu+detune; H[C,C]+=mu-detune   # detune≠0 → 평탄밴드 깨짐(dispersive 대조)
    return H

def pair_dispersion(N, U, mu=-4.0, detune=0.0, t=1.0):
    S=3*N
    H1=build_H1(N,t,mu,detune)
    ev1=np.sort(np.linalg.eigvalsh(H1))
    # 2체 (↑⊗↓, distinguishable): dim S^2
    I=np.eye(S)
    H2=np.kron(H1,I)+np.kron(I,H1)
    for s in range(S):              # attractive Hubbard U<0, 같은 site
        H2[s*S+s, s*S+s]+=U
    # translation T2 = P⊗P (cell +1)
    P=np.zeros((S,S))
    for n in range(N):
        for a in range(3):
            P[3*((n+1)%N)+a, 3*n+a]=1.0
    Pm=[np.linalg.matrix_power(P,m) for m in range(N)]
    T2m=[np.kron(Pm[m],Pm[m]) for m in range(N)]
    def lowestE(q):
        Q=2*np.pi*q/N
        Pr=sum(np.exp(-1j*Q*m)*T2m[m] for m in range(N))/N   # Q-sector projector
        wp,vp=eigh(Pr)
        cols=vp[:, wp.real>0.5]                               # range(Pr) 기저
        Hq=cols.conj().T@H2@cols
        return float(np.linalg.eigvalsh(Hq)[0])
    E0=lowestE(0); E1=lowestE(1)
    Eb=E0-2*ev1[0]   # pair binding (vs 비상호작용 2입자 최저)
    dQ=2*np.pi/N
    inv_mass=(E1-E0)/(dQ**2) if E1 is not None else float('nan')  # ~1/(2m*) 곡률
    return Eb, E0, E1, inv_mass, ev1

N=8
Us=[-1.0,-2.0,-4.0,-8.0,-16.0,-32.0]
print("=== flat-band Cooper 쌍 mobility + BEC-side 완화 (diamond chain N=8, 2체 ED) ===")
print(f"{'U':>5}{'flat 1/m*':>11}{'disp 1/m*':>11}{'flat/disp 비율':>14}")
for U in Us:
    _,_,_,imf,_=pair_dispersion(N,U,detune=0.0)
    _,_,_,imd,_=pair_dispersion(N,U,detune=1.0)
    ratio = imf/imd if abs(imd)>1e-9 else float('nan')
    print(f"{U:>5.0f}{imf:>11.5f}{imd:>11.5f}{ratio:>14.2f}")
print()
print("[검증] 절대 1/m*는 강결합서 둘 다 →0(쌍 무거워짐·BEC). 핵심=flat/disp ★비율 — 강결합서도 비율 유지/증가면")
print("  flat band가 dispersive보다 항상 덜 죽음(geometric stiffness가 BEC-side서도 상대 우위) = 처방 S3 정합.")
print("[d6] toy diamond·2체(dilute)·1D metric(Chern 아님). 절대 BEC-side 면역은 2D Chern many-body QMC(S3-full)가 확정.")
