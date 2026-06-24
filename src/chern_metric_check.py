"""
L44 검증 트랙 S1-2 (실측·c2): Chern flat-band의 quantum-metric 위상 하한 확인.
처방 핵심 = "위상수 C가 superfluid stiffness(D_s ∝ ∫tr g)를 떠받친다".
수학적 사실: tr g(k) >= |Omega(k)| pointwise → ∫tr g >= ∫|Omega| >= |∫Omega| = 2*pi*|C|.
즉 ∫tr g/(2*pi) >= |C| (위상 하한). ideal(Kähler) flat band면 등호.
2-band QWZ model H(k)=d(k).sigma 로 ∫tr g, ∫|Omega|, 2*pi*|C| 수치 비교.
"""
import numpy as np

def run(M, N=240, label=""):
    ks = np.linspace(-np.pi, np.pi, N, endpoint=False)
    dk = (2*np.pi)/N
    KX, KY = np.meshgrid(ks, ks, indexing="ij")
    # d-vector (QWZ): C=1 for 0<M<2, C=-1 for -2<M<0, C=0 otherwise
    dx, dy, dz = np.sin(KX), np.sin(KY), M - np.cos(KX) - np.cos(KY)
    dn = np.sqrt(dx**2 + dy**2 + dz**2)
    nx, ny, nz = dx/dn, dy/dn, dz/dn
    # gradients (periodic): ∂kx, ∂ky of unit vector n̂
    def grad(f):
        return np.gradient(f, dk, axis=0), np.gradient(f, dk, axis=1)
    nxx, nxy = grad(nx); nyx, nyy = grad(ny); nzx, nzy = grad(nz)
    # quantum metric: tr g = (1/4)(|∂x n̂|^2 + |∂y n̂|^2)
    trg = 0.25*((nxx**2+nyx**2+nzx**2) + (nxy**2+nyy**2+nzy**2))
    # Berry curvature: Omega = (1/2) n̂ . (∂x n̂ × ∂y n̂)
    cross_x = nyx*nzy - nzx*nyy
    cross_y = nzx*nxy - nxx*nzy
    cross_z = nxx*nyy - nyx*nxy
    Omega = 0.5*(nx*cross_x + ny*cross_y + nz*cross_z)
    intΩ   = np.sum(Omega)*dk*dk
    C      = intΩ/(2*np.pi)
    int_trg = np.sum(trg)*dk*dk
    int_absΩ = np.sum(np.abs(Omega))*dk*dk
    bound = 2*np.pi*abs(round(C))
    print(f"[{label} M={M:+.1f}]  C={C:+.3f}  ∫trg={int_trg:7.3f}  2π|C|={bound:7.3f}  "
          f"∫trg/(2π|C|)={ (int_trg/bound if bound>1e-6 else float('nan')):.3f}  "
          f"(하한 {'OK' if int_trg>=bound-1e-2 or bound<1e-6 else 'VIOLATED'})")
    return C, int_trg, bound

print("=== Chern flat-band quantum-metric 위상 하한 검증 (∫trg >= 2π|C|) ===")
run(1.0, label="C=1 phase")   # topological, C=+1
run(1.5, label="C=1 phase")   # topological, C=+1 (덜 평탄)
run(0.5, label="C=1 phase")   # topological, C=+1 (더 평탄 쪽)
run(2.5, label="trivial  ")   # trivial, C=0
run(-1.0, label="C=-1 phase") # topological, C=-1
print()
print("[해석] ∫trg/(2π|C|) >= 1 이면 위상 하한 성립 → stiffness D_s ∝ ∫trg가 |C|에 의해 바닥받침됨(처방 핵심).")
print("  값이 1에 가까울수록 ideal(Kähler) flat band(등호)·클수록 여유. C=0(trivial)은 하한 없음(stiffness 위상보호 X).")
print("[d6] 2-band toy QWZ·single band·연속극한 이산화. higher-C(|C|>=2)는 2π|C|로 하한 스케일↑(처방의 C↑→stiffness↑ 정합).")
