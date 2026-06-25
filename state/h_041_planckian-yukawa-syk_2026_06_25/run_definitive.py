#!/usr/bin/env python3
r"""H_041 DEFINITIVE driver — real Yukawa-SYK Schwinger-Dyson stiffness vs the 164 K ceiling.

Replaces the closed-form PROXY (run.py) with a CONVERGED self-consistent Matsubara
Schwinger-Dyson solve of the Yukawa-SYK superconductor's superfluid stiffness (G, Sigma, Phi,
F, Pi, D iterated to a fixed point with strong damping; per-point convergence residual reported).

PROTOCOL (honest, calibration-controlled):
  COHERENT reference  : weak Yukawa coupling solved at very low T so the BCS-like gap pairs with
                        a sharp residue (Z~O(1)) -> an O(1) anomalous gap Fmax, coherent raw
                        stiffness rho_s^coh = T sum_n F_n^2 (W=1).
  INCOHERENT sweep    : strong coupling from the crossover into the deep NFL (Z->0); full SC SD
                        self-consistency -> converged anomalous F, raw stiffness rho_s^inc.

  ONE generous band scale W (= n/m*) is calibrated so the COHERENT reference D_s = 1.5x the
  164 K requirement (the same generous handicap the proxy used). That SAME W is applied to the
  incoherent sweep. DECISIVE honest-null: does the incoherent converged D_s clear 164 K (escape),
  or collapse orders below it (no quasiparticle -> small superfluid weight -> wall holds)?

  Calibration-FREE cross-check: rho_s^inc/rho_s^coh -- the literature D_s/D_s^bare ~ Z^2 collapse
  (Inkof/Hauck/Schmalian arXiv:2106.12078; arXiv:2406.07608) -- needs no W and cannot be tuned.

CONVERGENCE NOTE: the deep-NFL points have a near-critical boson and converge slowly/stiffly
(reported residual); the per-point absolute D_s there is not pinned to many digits, but the
MONOTONE collapse of Fmax and rho_s with decreasing Z (orders of magnitude) is robust and is what
the verdict rests on. No fitting, no tuning to green.

VERDICT: escapes-wall iff the converged INCOHERENT D_s clears 164 K with a real margin under the
W that lets the COHERENT reference clear it; suppression below = honest-null = confirms-wall.
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tool'))
import numpy as np
from sd_solver import KB_meV_per_K, CEILING_K, D_s_req_meV, solve_sd
from rtsc_harness import Falsifier, evaluate

# Fixed model anchors (no tuning). Energies in meV.
w0    = 50.0      # bare boson (critical-mode) energy
r_syk = 1.0       # SYK ratio M/N
epsF  = 300.0     # flat-band-ish Fermi scale

# Coherent BCS reference: weak coupling, low T -> robustly paired sharp-QP gap.
g2_coh, T_coh, Nf_coh = 6000.0, 0.20, 240
# Incoherent NFL sweep: crossover -> deep NFL, low T, fully self-consistent (strong damping).
T_inc, Nf_inc = 0.80, 200
g2_inc_grid = [30000.0, 70000.0, 150000.0, 300000.0, 700000.0, 1500000.0, 3000000.0]

print("=" * 78)
print("H_041 DEFINITIVE — real Yukawa-SYK Schwinger-Dyson stiffness vs the ceiling")
print("       (replaces the closed-form proxy with a converged Matsubara SD solve)")
print("       freeze premise violated: QUASIPARTICLE-COHERENCE (Z->0, incoherent NFL)")
print("=" * 78)
print(f"ceiling band top                   : {CEILING_K:.1f} K")
print(f"D_s required for (pi/2)D_s=164K     : {D_s_req_meV:.4f} meV")
print(f"boson w0 / Fermi epsF / SYK r       : {w0:.1f} / {epsF:.1f} meV / {r_syk:.1f}")
print(f"solver: damped Matsubara SD (mix=0.2, tol=1e-12), Nf={Nf_inc} (each side)")
print("-" * 78)

t0 = time.time()

# --- COHERENT reference solve ---
sol_coh = solve_sd(T_meV=T_coh, g2=g2_coh, w0=w0, r=r_syk, W=1.0, Nf=Nf_coh, seed_gap=0.30)
rho_coh_raw = sol_coh["Ds_meV"]
print(f"COHERENT reference (g^2={g2_coh:.0f}, T={T_coh:.2f} meV): "
      f"Z={sol_coh['Z']:.4f}  Fmax={sol_coh['Fmax']:.4e}  rho_s^coh(W=1)={rho_coh_raw:.4e}  "
      f"[resid {sol_coh['resid']:.1e}, {sol_coh['n_it']} it]")

target_coh_Ds = 1.5 * D_s_req_meV
W = target_coh_Ds / rho_coh_raw if rho_coh_raw > 0 else 1.0
Ds_coh = W * rho_coh_raw
Tbkt_coh = (np.pi/2.0)*Ds_coh/KB_meV_per_K
print(f"generous W (= n/m* band scale) so coherent D_s=1.5x req ({target_coh_Ds:.3f} meV) -> W={W:.4e}")
print(f"  -> coherent D_s={Ds_coh:.4f} meV, T_BKT^coh={Tbkt_coh:.2f} K (clears ceiling by construction)")
print("-" * 78)

# --- INCOHERENT NFL sweep ---
print("  g^2(meV^2)    Z       Fmax        rho_s^inc(W=1)   D_s(meV)    T_BKT(K)   rho^inc/rho^coh  resid")
records = []
for g2 in g2_inc_grid:
    sol = solve_sd(T_meV=T_inc, g2=g2, w0=w0, r=r_syk, W=1.0, Nf=Nf_inc, seed_gap=0.30)
    Z = sol["Z"]; Fmax = sol["Fmax"]; rho_raw = sol["Ds_meV"]
    Ds = W * rho_raw
    Tbkt = (np.pi/2.0)*Ds/KB_meV_per_K
    ratio = rho_raw / rho_coh_raw if rho_coh_raw > 0 else 0.0
    records.append({"g2": g2, "Z": Z, "Fmax": Fmax, "rho_raw": rho_raw,
                    "Ds_meV": Ds, "Tbkt_K": Tbkt, "ratio": ratio, "resid": sol["resid"]})
    print(f"  {g2:10.0f}  {Z:.4f}  {Fmax:.3e}   {rho_raw:.4e}    {Ds:8.5f}   {Tbkt:8.4f}   "
          f"{ratio:.4e}     {sol['resid']:.1e}")

print("-" * 78)

# --- Observables ---
inc = [r for r in records if r["Z"] < 0.2]
if not inc:
    inc = sorted(records, key=lambda r: r["Z"])[:3]
best_inc_Ds    = max(r["Ds_meV"] for r in inc)
best_inc_Tbkt  = max(r["Tbkt_K"] for r in inc)
best_inc_Fmax  = max(r["Fmax"] for r in inc)
best_inc_ratio = max(r["ratio"] for r in inc)
best_any_Tbkt  = max(r["Tbkt_K"] for r in records)
ref_best       = max(records, key=lambda r: r["Tbkt_K"])

print(f"COHERENT D_s (generous, by construction)     : {Ds_coh:.4f} meV  (T_BKT={Tbkt_coh:.1f} K, clears ceiling)")
print(f"best converged D_s in INCOHERENT (Z<0.2) NFL : {best_inc_Ds:.6f} meV  (req {D_s_req_meV:.3f})")
print(f"best converged Fmax in INCOHERENT NFL        : {best_inc_Fmax:.4e}  (coherent gap Fmax={sol_coh['Fmax']:.3e})")
print(f"best T_BKT in INCOHERENT NFL                 : {best_inc_Tbkt:.4f} K")
print(f"calib-free rho_s^inc/rho_s^coh (= ~Z^2 law)  : {best_inc_ratio:.4e}  (escape needs ~1)")
print(f"best T_BKT over ALL incoherent g             : {best_any_Tbkt:.4f} K  at g^2={ref_best['g2']:.0f} (Z={ref_best['Z']:.4f})")
print("-" * 78)

metrics = {
    "best_incoherent_Ds_meV": best_inc_Ds,
    "best_incoherent_Tbkt_K": best_inc_Tbkt,
    "best_any_Tbkt_K": best_any_Tbkt,
    "inc_to_coh_ratio": best_inc_ratio,
    "D_s_req_meV": D_s_req_meV,
    "ceiling_K": CEILING_K,
}

falsifiers = [
    Falsifier(
        "F1_HONEST_NULL_converged_SYK_stiffness_collapses_in_incoherent_regime",
        lambda m: m["inc_to_coh_ratio"] < 0.5,
        "TRIGGERS if the CONVERGED full-SD D_s in the incoherent (Z<0.2) NFL is <0.5x the coherent "
        "value (calibration-free) -> SYK incoherence suppresses anomalous F; incoherence buys no rigidity.",
    ),
    Falsifier(
        "F2_incoherent_converged_stiffness_clears_ceiling",
        lambda m: m["best_incoherent_Tbkt_K"] <= m["ceiling_K"],
        "TRIGGERS if the best converged T_BKT in the incoherent regime stays <= 164 K under the "
        "generous W -> the non-quasiparticle reservoir cannot lift T_BKT past the wall.",
    ),
    Falsifier(
        "F3_any_incoherent_coupling_clears_ceiling",
        lambda m: m["best_any_Tbkt_K"] <= m["ceiling_K"],
        "TRIGGERS if NO incoherent g gives converged T_BKT > 164 K.",
    ),
    Falsifier(
        "F4_incoherent_Ds_exceeds_required",
        lambda m: m["best_incoherent_Ds_meV"] <= m["D_s_req_meV"],
        "TRIGGERS if the best incoherent converged D_s stays <= the D_s required for 164 K.",
    ),
    Falsifier(
        "F5_incoherent_stiffness_within_factor2_of_coherent",
        lambda m: m["inc_to_coh_ratio"] < 0.5,
        "Calibration-free cross-check of F1 on the raw ratio -> TRIGGERS when incoherence buys "
        "<0.5x the coherent stiffness (the Z^2 collapse the literature reports).",
    ),
]

ledger = evaluate(metrics, falsifiers)
honest_null_pass = (ledger["falsifiers"][0]["status"] == "PASS")
inc_clears = (best_inc_Tbkt > CEILING_K)
escape = inc_clears and honest_null_pass
verdict = "escapes-wall" if escape else "confirms-wall"

for fr in ledger["falsifiers"]:
    tag = "TRIGGER" if fr["triggered"] else "PASS   "
    print(f"  [{tag}] {fr['name']}")
print("-" * 78)
print(f"honest-null (F1) PASS (survives)     : {honest_null_pass}")
print(f"incoherent regime clears 164K margin : {inc_clears}")
print(f"falsifiers_pass                      : {ledger['n_pass']}/{ledger['n_total']}")
print(f"is_green                             : {escape}")
print(f"absorbed                             : False")
print(f"VERDICT                              : {verdict}")
print(f"solver wall-time                     : {time.time()-t0:.1f} s")
print("=" * 78)
