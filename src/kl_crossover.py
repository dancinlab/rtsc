"""
geometry-KL frontier 정량 (L43·c14 (d) compute census, pool-run).
geometry-KL은 non-phonon glue라 phonon Omega 천장(L22 ~155meV)을 우회한다. 그러나
flat-band SC 공통 BKT-stiffness 천장(L25: k_B Tc <= (pi/2) D_s, D_s=4|U|nu(1-nu)<g>)과
L30 BCS-BEC crossover(|U| 키우면 Tc peak 후 falls)는 공유하는가? — |U|_KL 스윕으로 max Tc cap을 본다.
HONEST(d6): crossover |U|_opt~bandwidth W·form-factor는 거친 추정; 정확은 strong-coupling QMC(TERMINAL).
"""
import math

kB = 0.0862   # meV/K
defl = 2.8    # raw 2D-BKT over-predicts (fbgeom_predictor tc_band)
g = 0.494     # kagome <g> = integral tr(g) (fbgeom_predictor 출력)
Wflat = 50.0  # kagome dispersive bandwidth scale (meV)

print("=== geometry-KL |U|_KL sweep: BKT Tc vs L30 crossover cap (kagome <g>=0.494) ===")
print(f"{'|U|_KL(meV)':>11}  {'BKT_Tc(K)':>9}  note")
for U in [30, 60, 90, 120, 150, 200, 300, 500]:
    Ds = U * g                       # nu=1/2 -> D_s = |U|<g>
    Tc = (math.pi / 2) * Ds / defl / kB
    if U > 2 * Wflat:
        note = "BEC side: Tc satur/falls ~ t^2/U (L30) -> BKT overpredicts"
    elif U > Wflat:
        note = "crossover (L30 peak 부근)"
    else:
        note = "weak-U linear (BCS, KL native regime)"
    print(f"  {U:>9}  {Tc:>9.0f}  {note}")

print()
print("[L30 crossover cap] flat-band W~50meV -> |U|_opt~W(50-100meV)서 Tc peak; |U|>2W면 BEC(Tc~t^2/U falls).")
print("=> geometry-KL은 phonon 천장 우회하나 max Tc는 crossover서 |U|_opt~W*<g>에 cap.")
print("   kagome |U|_opt~50-100meV -> BKT Tc ~ 95-190K = 293K 미달(marginal sub-room).")
print("[HONEST d6] |U|_opt~W·form-factor projection은 거친 추정(실재 호스트 의존); 정확은 strong-coupling QMC=TERMINAL compute.")
