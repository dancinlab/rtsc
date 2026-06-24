import numpy as np
# Harrison scaling (same as model)
tperp_0=0.635; k_ap=0.55; N_AP=4.0; A0=3.84; U_HUB=3.0
def tperp(eps): return tperp_0*(1+k_ap*eps)**(-N_AP)
def eps_of(a): return a/A0-1
SUBS=[("LaAlO3 (LAO)",3.79),("SrLaAlO4 (SLAO)",3.756),("LSAT",3.868),
      ("SrTiO3 (STO)",3.905),("NdGaO3 (NGO)",3.86),("YAlO3 (YAO)",3.71),
      ("(stronger comp)",3.74)]
# Sign-correct proxy: Tc linear in interlayer super-exchange J_perp=4 t_perp^2/U.
# Calibrate so LAO (eps=-1.30%) -> 48 K. Then predict others (pure t_perp^2 trend).
def Jperp(eps): return 4*tperp(eps)**2/U_HUB
eps_LAO=eps_of(3.79)
cal = 48.0/Jperp(eps_LAO)        # K per (eV of J_perp)
print("=== SIGN-CORRECT design-law: Tc = cal * J_perp,  J_perp=4 t_perp^2/U, LAO->48K ===")
print(f"calibration: cal={cal:.2f} K/eV ; J_perp(LAO)={Jperp(eps_LAO):.4f} eV")
print(f"{'eps%':>7}{'t_perp':>9}{'Jperp':>9}{'Tc_K':>8}")
for e in np.linspace(-0.04,0.02,13):
    print(f"{e*100:7.2f}{tperp(e):9.4f}{Jperp(e):9.4f}{cal*Jperp(e):8.1f}")
print("\n=== SUBSTRATE RANKING (sign-correct) ===")
rows=[(n,a,eps_of(a),tperp(eps_of(a)),cal*Jperp(eps_of(a))) for n,a in SUBS]
for n,a,e,tp,tc in sorted(rows,key=lambda r:-r[4]):
    print(f"{n:<18} a={a:.3f}  eps={e*100:+.2f}%  t_perp={tp:.4f}  Tc={tc:.1f}K")
# design-law closed form
print(f"\n[LAW] Tc(eps) = {cal:.1f} * 4/{U_HUB} * [{tperp_0}*(1+{k_ap}*eps)^-{N_AP}]^2")
print(f"[LAW] d ln Tc/d eps = -2*N_AP*k_ap/(1+k_ap*eps) ~ {-2*N_AP*k_ap:.2f} per unit strain "
      f"(={-2*N_AP*k_ap*0.01*100:.1f}% Tc per 1% compression)")
# practical ceiling: extrapolate to apical bond straightening limit (~ -4% before structural instab)
print(f"[ceiling] at eps=-4% (apical 180-limit): Tc_proxy = {cal*Jperp(-0.04):.1f} K")
