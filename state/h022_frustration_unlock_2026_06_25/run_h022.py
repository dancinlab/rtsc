#!/usr/bin/env python3
"""run_h_022 — the 🟢-CONDITIONAL compute for HYPOTHESES card H_022.

THE QUESTION (conditional unlock):
  IF the 1T-TiSe2 CDW is suppressed by frustration (H_016: eta_nest pushed below the critical
  ~0.45) WHILE the host's ~400 meV exciton survives, does the trio CoSn / hBN / 1T-TiSe2

      (a) reach ROOM-T amplitude  (stacked_tc(400, three_d=True) vs 293 K), AND
      (b) become SC-LEADING       (H_016-style Stoner/RPA leading-channel race at the
                                   FRUSTRATED nesting confirms SC leads over CDW/SDW)?

This is a CONFLUENCE check: it pins TWO previously-separate axes onto ONE concrete host.
  - H_020 found the named Ta2NiSe5 trio MISSES room-T (~252 K) because its glue is only ~300 meV;
    the glue gap pointed the search at a higher-energy clean boson. 1T-TiSe2's ~400 meV exciton
    (researchgate 332412936; arXiv:0911.0327) is the ONLY surveyed boson ABOVE the 349 meV room-T
    demand — it CLEARS amplitude (H_020's missing axis).
  - H_016 found the competing-order wall (H_014) is REMOVABLE by frustration: below eta_nest* ~ 0.45
    SC becomes the leading instability. 1T-TiSe2 carries an intrinsic finite-q 2x2x2 CDW — exactly
    the competing order H_016's frustration escape targets.

H_022 does NOT discover a material. It asks the strictly conditional question: IF both unlocks
hold on ONE host, is the trio a room-T-clearing, SC-leading candidate? The ANSWER is a CONDITIONAL
verdict (🟠-with-a-named-unlock), NOT a 🟢 — because the coexistence of (CDW suppression) AND
(surviving 400 meV exciton) in a REAL material is UNVERIFIED. The single remaining unknown is named.

NO tune-to-green. The amplitude uses the campaign-SSOT harness verbatim. The leading-channel race
re-uses H_016's EXACT toy Stoner/RPA bookkeeping and fixed constants (f_glue, N, V/U, etc.), only
EVALUATED at a frustrated nesting (eta below eta*). The 400 meV exciton is a CITED literature value,
not fitted. Run twice; bytes must be byte-identical.
"""
import json
import os
import sys

# ----------------------------------------------------------------------------- shared harness
# Amplitude primitives come from the campaign SSOT (NOT re-implemented, NOT edited). The harness
# lives in repo-root tool/; resolve it relative to this run script and add it to the import path.
_HARNESS_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", "tool"))
if _HARNESS_DIR not in sys.path:
    sys.path.insert(0, _HARNESS_DIR)
from rtsc_harness import (
    stacked_tc,
    geometric_bkt_tc_band,
    omega_for_stacked_tc,
    THREED_TC_LEVER,
    ROOM_T_K,
    PHONON_CEILING_MEV,
)

# ----------------------------------------------------------------------------- inline Falsifier API
class Falsifier:
    """A named predicate(metrics)->bool that is TRUE when TRIGGERED (component refuted).
    PASS = NOT triggered."""
    def __init__(self, name, predicate, desc):
        self.name = name
        self.predicate = predicate
        self.desc = desc

def evaluate(metrics, falsifiers):
    results = []
    for f in falsifiers:
        trig = bool(f.predicate(metrics))
        results.append({"name": f.name, "triggered": trig,
                        "status": "FAIL" if trig else "PASS", "desc": f.desc})
    n_pass = sum(1 for r in results if not r["triggered"])
    return {"metrics": metrics, "falsifiers": results,
            "n_pass": n_pass, "n_total": len(results), "all_pass": n_pass == len(results)}

# ============================================================================= PART (a): AMPLITUDE
# 1T-TiSe2's upper excitonic optical mode ~ 400 meV (CITED literature, not fitted):
#   researchgate 332412936 ("Excitonic and lattice contributions to the CDW in 1T-TiSe2") and
#   arXiv:0911.0327 (exciton-condensate optics). Two modes reported: ~400 meV and ~80 meV; we
#   use the upper mode, the only surveyed electronic boson clearly ABOVE the 349 meV room-T demand.
TISE2_EXCITON_MEV = 400.0

tc_2d = geometric_bkt_tc_band(TISE2_EXCITON_MEV)          # 2D BKT band, no 3D lever
tc_3d = stacked_tc(TISE2_EXCITON_MEV, three_d=True)       # + real 3D lever L_3D = 1.84
omega_req_roomT_3d = omega_for_stacked_tc(ROOM_T_K, three_d=True)   # glue needed for 293 K w/ 3D
glue_margin_meV = TISE2_EXCITON_MEV - omega_req_roomT_3d  # +ve => exciton OVER-clears the demand
amplitude_clears_roomT = tc_3d >= ROOM_T_K
glue_is_electronic = TISE2_EXCITON_MEV > PHONON_CEILING_MEV   # 400 > 200 -> electronic reservoir

# ============================================================================= PART (b): LEADING CHANNEL
# H_016's EXACT toy Stoner/RPA bookkeeping & fixed constants (NOT re-tuned). The ONLY thing H_022
# does differently is EVALUATE the race at a FRUSTRATED nesting (eta_nest below the critical eta*),
# i.e. the regime H_016 already proved opens an SC-leading window. We confirm it explicitly for
# the 1T-TiSe2-style host: its competing order is a CDW (charge), so we read out U_sc vs U_cdw (and
# U_sdw / U_ps) and require SC to lead EVERY particle-hole channel at the frustrated nesting.
N_DOS            = 1.0      # flat-band DOS at E_F (lever sets the scale -> 1.0)   [H_016]
KAPPA_PS         = 0.55     # phase-separation compressibility curvature (NOT nesting-scaled) [H_016]
U_C_PS           = 1.30     # bare-U PS onset (units of 1/N)                       [H_016]
L_PP             = 1.00     # Cooper-channel log enhancement (toy -> 1)            [H_016]
F_GLUE           = 0.45     # retarded attractive fraction available as glue       [H_016]
V_INTERSITE_FRAC = 0.30     # inter-site V as fraction of U (screens CDW)          [H_016]

# Critical / chosen nesting. H_016 closed form: SC leads SDW  <=>  eta_nest < f_glue/N = 0.45.
ETA_CRIT_CLOSED = F_GLUE / N_DOS                          # 0.45 (boundary)
ETA_PLAUSIBLE_FLOOR = 0.30                                # H_016 pre-registered frustration floor
# Evaluate at a frustration INSIDE the plausible escape band [0.30, 0.45): kagome/triangular lore.
ETA_FRUSTRATED  = 0.35                                    # comfortably below eta* and >= floor

def S_sdw(U, eta): return U * N_DOS * eta
def S_cdw(U, eta):
    V = V_INTERSITE_FRAC * U
    return (U - 2.0 * V) * N_DOS * eta
def S_ps(U, eta):
    return 0.0 if U <= U_C_PS else (U - U_C_PS) * N_DOS * KAPPA_PS
def S_sc(U, eta): return (F_GLUE * U) * (N_DOS * L_PP)   # eta-independent pair channel

CHANNELS = [("SDW", S_sdw), ("CDW", S_cdw), ("PS", S_ps), ("SC", S_sc)]

U_MIN, U_MAX, U_STEP = 0.0, 8.0, 0.001
n_U = int(round((U_MAX - U_MIN) / U_STEP)) + 1
U_GRID = [round(U_MIN + i * U_STEP, 6) for i in range(n_U)]

def threshold_U(S_func, eta):
    """Smallest U at which S_func(U,eta) >= 1 (linear interp between grid nodes)."""
    prev_U, prev_S = None, None
    for U in U_GRID:
        S = S_func(U, eta)
        if S >= 1.0:
            if prev_U is None:
                return U
            frac = (1.0 - prev_S) / (S - prev_S) if S != prev_S else 0.0
            return prev_U + frac * (U - prev_U)
        prev_U, prev_S = U, S
    return None

# closed-form SC threshold (eta-independent) for the self-consistency check
U_SC_CLOSED = 1.0 / F_GLUE                                # 2.2222

def race_at(eta):
    th = {name: threshold_U(func, eta) for name, func in CHANNELS}
    ph_names = ["SDW", "CDW", "PS"]
    ph_th = {n: th[n] for n in ph_names if th[n] is not None}
    leading_ph = min(ph_th, key=ph_th.get) if ph_th else None
    leading_ph_U = ph_th[leading_ph] if leading_ph else None
    sc_U = th["SC"]
    sc_leads = (sc_U is not None) and (leading_ph_U is not None) and (sc_U < leading_ph_U)
    return {
        "eta_nest": eta,
        "U_sc": round(sc_U, 4) if sc_U is not None else None,
        "U_sdw": round(th["SDW"], 4) if th["SDW"] is not None else None,
        "U_cdw": round(th["CDW"], 4) if th["CDW"] is not None else None,
        "U_ps": round(th["PS"], 4) if th["PS"] is not None else None,
        "leading_ph": leading_ph,
        "U_leading_ph": round(leading_ph_U, 4) if leading_ph_U is not None else None,
        "sc_leads": sc_leads,
        "window_width": round(leading_ph_U - sc_U, 4) if sc_leads else 0.0,
    }

# Race at three nesting values: the FRUSTRATED host (b), the boundary eta*, and the UNFRUSTRATED
# commensurate host (H_014's CDW-on regime, control: SC must NOT lead there).
row_frustrated   = race_at(ETA_FRUSTRATED)               # 0.35  -> SC should LEAD
row_boundary     = race_at(ETA_CRIT_CLOSED)              # 0.45  -> boundary (SC ties/sub-leads)
row_unfrustrated = race_at(0.85)                         # 0.85  -> SC must NOT lead (control)

sc_leads_frustrated = row_frustrated["sc_leads"]
# For 1T-TiSe2 the named competing order is the CDW. Confirm SC beats the CDW specifically.
sc_beats_cdw = (row_frustrated["U_sc"] is not None
                and row_frustrated["U_cdw"] is not None
                and row_frustrated["U_sc"] < row_frustrated["U_cdw"])

# ============================================================================= CONFLUENCE verdict
# The trio is a 🟢-CONDITIONAL candidate IFF BOTH unlock axes pass at the frustrated host:
#   (a) amplitude clears room-T at 400 meV + 3D lever, AND
#   (b) SC leads the competing order at the frustrated nesting.
both_unlocks_pass = amplitude_clears_roomT and sc_leads_frustrated
# Honest gate: this is CONDITIONAL on an UNVERIFIED coexistence -> still NOT 🟢, it is 🟠.
coexistence_verified = False     # CDW-suppression AND surviving 400 meV exciton in ONE real host
is_green = both_unlocks_pass and coexistence_verified     # must be False (honest)

metrics = {
    "tise2_exciton_meV": TISE2_EXCITON_MEV,
    "L_3D": THREED_TC_LEVER,
    "room_T_K": ROOM_T_K,
    "tc_2d_K": round(tc_2d, 2),
    "tc_3d_K": round(tc_3d, 2),
    "omega_required_roomT_3d_meV": round(omega_req_roomT_3d, 2),
    "glue_margin_meV": round(glue_margin_meV, 2),
    "amplitude_clears_roomT": amplitude_clears_roomT,
    "phonon_ceiling_meV": PHONON_CEILING_MEV,
    "glue_is_electronic": glue_is_electronic,
    "eta_crit_closed": round(ETA_CRIT_CLOSED, 4),
    "eta_plausible_floor": ETA_PLAUSIBLE_FLOOR,
    "eta_frustrated": ETA_FRUSTRATED,
    "U_sc_closed": round(U_SC_CLOSED, 4),
    "row_frustrated": row_frustrated,
    "row_boundary": row_boundary,
    "row_unfrustrated": row_unfrustrated,
    "sc_leads_frustrated": sc_leads_frustrated,
    "sc_beats_cdw_frustrated": sc_beats_cdw,
    "both_unlocks_pass": both_unlocks_pass,
    "coexistence_verified": coexistence_verified,
    "is_green": is_green,
}

# ----------------------------------------------------------------------------- falsifiers (>=4)
falsifiers = [
    # F1: amplitude — 400 meV + 3D lever must CLEAR room-T (293 K). EXPECTED PASS (the unlock-a).
    Falsifier("F1_amplitude_clears_roomT",
              lambda m: not m["amplitude_clears_roomT"],
              "PASS = stacked_tc(400 meV, 3D) >= 293 K — the ~400 meV exciton + L_3D lever clears "
              "room-T amplitude (the axis H_020's 300 meV trio MISSED). FAIL = under 293 K."),
    # F2: the exciton over-clears the room-T glue DEMAND (positive margin over the 349 meV need).
    Falsifier("F2_glue_over_clears_demand",
              lambda m: m["glue_margin_meV"] <= 0.0,
              "PASS = 400 meV exceeds the omega required for room-T with the 3D lever (~349 meV) "
              "-> positive margin. FAIL = the exciton does not even meet the relaxed room-T demand."),
    # F3: leading-channel — at the FRUSTRATED nesting (eta=0.35 < eta*=0.45) SC must LEAD every
    #     particle-hole channel (the H_016 escape, evaluated for this host). EXPECTED PASS (unlock-b).
    Falsifier("F3_sc_leads_when_frustrated",
              lambda m: not m["sc_leads_frustrated"],
              "PASS = at eta_nest=0.35 (below the critical 0.45) SC is the leading instability "
              "over SDW/CDW/PS — frustration unlocks SC-leading. FAIL = competing order still leads."),
    # F4: SC must specifically beat the CDW (1T-TiSe2's NAMED competing order) at the frustrated nesting.
    Falsifier("F4_sc_beats_cdw",
              lambda m: not m["sc_beats_cdw_frustrated"],
              "PASS = U_sc < U_cdw at the frustrated nesting — SC pre-empts 1T-TiSe2's intrinsic "
              "CDW specifically. FAIL = the CDW channel still goes unstable before SC."),
    # F5: CONTROL — at the UNFRUSTRATED commensurate nesting (eta=0.85, H_014's CDW-on regime) SC
    #     must NOT lead; the unlock must be a genuine CHANGE from frustration, not a free win.
    Falsifier("F5_control_unfrustrated_sc_subleads",
              lambda m: m["row_unfrustrated"]["sc_leads"],
              "PASS = at eta_nest=0.85 (commensurate, CDW-on) SC is NOT leading — the SC-leading "
              "result is bought BY frustration, not by construction. FAIL = SC leads even unfrustrated."),
    # F6: HONESTY GATE — this must remain a CONDITIONAL (NOT 🟢). The coexistence of CDW-suppression
    #     AND a surviving 400 meV exciton in ONE real material is UNVERIFIED -> is_green must be False.
    Falsifier("F6_not_green_conditional_only",
              lambda m: m["is_green"],
              "PASS = is_green is False — the verdict stays 🟠-CONDITIONAL because the coexistence "
              "(CDW suppression + surviving 400 meV exciton in a real host) is UNVERIFIED. "
              "FAIL = the run claims 🟢 without that coexistence proven (tune-to-green / over-claim)."),
]

verdict = evaluate(metrics, falsifiers)

# ----------------------------------------------------------------------------- verbatim stdout
def fmt(x): return f"{x:8.3f}" if isinstance(x, (int, float)) else "    None"

print("=== H_022 frustration-unlock — IF 1T-TiSe2's CDW is suppressed AND its 400 meV exciton survives, is the trio room-T + SC-leading? ===")
print("  CONDITIONAL confluence: pins H_020's missing AMPLITUDE axis + H_016's competing-order ESCAPE onto ONE host (CoSn / hBN / 1T-TiSe2).")
print("  NO tune-to-green: amplitude via campaign-SSOT harness; leading-channel via H_016's exact toy Stoner/RPA constants, evaluated at a frustrated nesting.")
print("  --- PART (a): room-T AMPLITUDE (1T-TiSe2 ~400 meV exciton; cited researchgate 332412936 / arXiv:0911.0327) ---")
print(f"    exciton Omega                         = {TISE2_EXCITON_MEV:.1f} meV   (> phonon ceiling {PHONON_CEILING_MEV:.0f} meV -> electronic: {glue_is_electronic})")
print(f"    bkt_Tc 2D (no 3D lever)               = {tc_2d:8.2f} K")
print(f"    stacked_Tc 3D (+ L_3D={THREED_TC_LEVER})           = {tc_3d:8.2f} K   (room-T {ROOM_T_K:.0f} K {'CLEARED' if amplitude_clears_roomT else 'MISSED'})")
print(f"    Omega required for room-T w/ 3D       = {omega_req_roomT_3d:8.2f} meV")
print(f"    glue margin (400 - required)          = {glue_margin_meV:+8.2f} meV   (positive => over-clears)")
print("  --- PART (b): LEADING-CHANNEL race (H_016 toy Stoner/RPA; SC leads when U_sc < every particle-hole U*) ---")
print(f"    fixed constants: N={N_DOS} kappa_ps={KAPPA_PS} U_c_ps={U_C_PS} L_pp={L_PP} f_glue={F_GLUE} V/U={V_INTERSITE_FRAC}")
print(f"    critical eta* (closed form f_glue/N)  = {ETA_CRIT_CLOSED:.4f}   plausible floor = {ETA_PLAUSIBLE_FLOOR}")
print(f"    SC threshold (eta-independent)        = U_sc = {U_SC_CLOSED:.4f}")
print("      regime          eta_nest  U_sc    U_sdw   U_cdw   U_ps    lead_ph  U_lead  SC_leads")
for label, r in (("frustrated(b)", row_frustrated), ("boundary eta*", row_boundary), ("unfrustrated(ctrl)", row_unfrustrated)):
    print(f"      {label:18s} {r['eta_nest']:.2f}  {fmt(r['U_sc'])} {fmt(r['U_sdw'])} {fmt(r['U_cdw'])} {fmt(r['U_ps'])}  {str(r['leading_ph']):>5s}  {fmt(r['U_leading_ph'])}  {str(r['sc_leads'])}")
print(f"    SC leads at frustrated nesting (0.35) : {sc_leads_frustrated}")
print(f"    SC beats CDW specifically (frustrated): {sc_beats_cdw}")
print("  --- CONFLUENCE verdict ---")
print(f"    (a) amplitude clears room-T           : {amplitude_clears_roomT}")
print(f"    (b) SC leads when frustrated          : {sc_leads_frustrated}")
print(f"    BOTH unlocks pass                     : {both_unlocks_pass}")
print(f"    coexistence (CDW-suppr + 400meV) verified : {coexistence_verified}   <- the SINGLE remaining unknown")
print(f"    is green                              : {is_green}   (stays 🟠-CONDITIONAL by honesty gate)")
print("  --- falsifiers (PASS = not triggered) ---")
for r in verdict["falsifiers"]:
    print(f"  falsifier {r['name']:36s}: {r['status']}")
print(f"  falsifiers_pass = {verdict['n_pass']}/{verdict['n_total']}")
if verdict["all_pass"]:
    print("VERDICT: 🟠-CONDITIONAL (named-unlock). IF the 1T-TiSe2 CDW is suppressed by frustration (eta_nest<0.45, H_016) AND")
    print("  the ~400 meV exciton survives, the trio CoSn/hBN/1T-TiSe2 (a) CLEARS room-T amplitude (stacked_tc(400,3D)=335.5 K > 293 K)")
    print("  AND (b) is SC-LEADING over the CDW at the frustrated nesting. This is a room-T-clearing, SC-leading CANDIDATE — but the")
    print("  SINGLE remaining unknown is whether CDW-suppression and the high exciton COEXIST in a real material. UNVERIFIED -> still")
    print("  NOT green; it is 🟠-with-a-named-unlock. absorbed=false, GATE_OPEN.")
else:
    print("VERDICT: an unlock axis FAILS or the honesty gate trips -> the confluence does NOT hold as stated (re-examine).")

out = os.path.join(os.path.dirname(__file__), "result.json")
with open(out, "w") as f:
    json.dump({"verdict": verdict}, f, indent=2)
