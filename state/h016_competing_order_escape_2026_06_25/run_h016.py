#!/usr/bin/env python3
"""run_h_016 — deterministic competing-order ESCAPE sweep for HYPOTHESES card H_016.

CONTINUATION of H_014 (CLOSED-NEGATIVE). H_014 used a STRONG nesting factor eta_nest=0.85,
so the particle-hole SDW channel went unstable (U* = 1/eta_nest) BEFORE the SC pairing channel
(U* = 1/f_glue = 2.222). SDW pre-empted SC: no SC-leading window (0/5, CLOSED-NEGATIVE). H_014
flagged the escape it did NOT test: a FRUSTRATED / INCOMMENSURATE flat band suppresses the
particle-hole nesting susceptibility, which weakens SDW/CDW without touching the pair channel.

H_016 does NOT terminal on one nesting value. It re-runs the SAME toy Stoner/RPA multi-channel
model as H_014, but SWEEPS the frustration knob eta_nest DOWN from 0.85 to ~0.1, and asks:

  Is there a critical eta_nest* below which SC becomes the LEADING instability
  (SC U* < SDW U* and < CDW U*) at the room-T glue mapping? And is that eta_nest* in a
  PHYSICALLY PLAUSIBLE range (not absurdly small)?

CHANNEL FORMULAS — IDENTICAL to H_014's RPA bookkeeping, with eta_nest now multiplying BOTH
particle-hole channels (the frustration knob the lane mandates):
  - SDW (particle-hole, spin):   S_sdw = U * N * eta_nest
  - CDW (particle-hole, charge): S_cdw = (U - 2*V) * N * eta_nest        (V = V/U frac * U)
  - PS  (phase separation):      S_ps  = (U - U_c_ps) * N * kappa  for U > U_c_ps else 0
                                  (PS is a compressibility blow-up; NOT a nesting effect, so
                                   it is deliberately NOT scaled by eta_nest — frustration of
                                   the Fermi-surface nesting does not relieve phase separation.)
  - SC  (particle-particle):     S_sc  = (f_glue * U) * (N * L_pp)       (glue-driven Cooper)

A channel is LEADING when its Stoner product S_c = g_c*chi_c first reaches 1 as U is swept up;
the channel reaching 1 at the SMALLEST U is the leading instability. SC leads iff its threshold
U_sc is strictly below EVERY particle-hole threshold.

NOTHING is tuned to make SC win: f_glue, kappa, U_c_ps, L_pp, N, V/U are the SAME fixed
structural constants as H_014. The ONLY swept quantity is eta_nest (the frustration knob).
A negative (SC stays sub-leading even at weak nesting -> competing order is a robust wall) is a
fully VALID honest result. So is a positive (an SC-leading window opens at plausible frustration).

stdout is pasted VERBATIM into the card. Run twice; bytes must be identical.
"""
import json
import os

# ----------------------------------------------------------------------------- inline harness
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
    n_total = len(results)
    return {"metrics": metrics, "falsifiers": results,
            "n_pass": n_pass, "n_total": n_total, "all_pass": n_pass == n_total}

# ----------------------------------------------------------------------------- fixed constants
# Calibrated 2D-BKT band (campaign SSOT): Tc[K] = 0.11*(Omega[meV]*11.604)/2.8 ; deflate=2.8.
# Inverse: Omega[meV] = Tc*2.8/(0.11*11.604). Room-T target Tc = 293 K.
KB_FACTOR   = 11.604      # meV per K (k_B in meV/K = 0.08617 -> 1/0.08617 ~ 11.604)
DEFLATE     = 2.8
TC_TARGET_K = 293.0
OMEGA_ROOMT_MEV = TC_TARGET_K * DEFLATE / (0.11 * KB_FACTOR)   # ~ 642.7 meV (2D bare)
# H_004/H_011 relaxed room-T glue demand after the verified +@ levers (3D, connector, geometry):
OMEGA_RELAXED_MEV = 349.0

# Structural (geometry/host) constants — fixed up front, NOT fitted, NOT tuned to green.
# IDENTICAL to H_014 except eta_nest, which is now the SWEPT frustration knob (not a constant).
N_DOS        = 1.0        # dimensionless flat-band DOS at E_F (the lever sets the scale -> 1.0)
KAPPA_PS     = 0.55       # phase-separation compressibility-curvature factor (NOT nesting-scaled)
U_C_PS       = 1.30       # bare-U onset (in units of 1/N) below which PS does not activate
L_PP         = 1.00       # Cooper-channel log enhancement (TOY: no BCS log divergence kept -> 1)
F_GLUE       = 0.45       # retarded attractive fraction of the bare interaction available as glue
V_INTERSITE_FRAC = 0.30   # inter-site V as a fraction of U (screens the CDW charge channel)

# Frustration sweep range. eta_nest in (0,1]; 1.0 = perfect commensurate nesting (worst case for
# SC), small = strong frustration / incommensuration. We start at H_014's value (0.85) and sweep
# DOWN to 0.10 (deep frustration). The sweep grid is FIXED and deterministic.
ETA_HI, ETA_LO, ETA_STEP = 0.85, 0.10, 0.01
n_eta = int(round((ETA_HI - ETA_LO) / ETA_STEP)) + 1
ETA_GRID = [round(ETA_HI - i * ETA_STEP, 4) for i in range(n_eta)]   # 0.85 -> 0.10 descending

# "Physically plausible" frustration floor: below this, the suppression is regarded as an
# unphysically perfect cancellation of nesting (a triangular/kagome geometric-frustration host
# realistically reaches eta_nest ~ 0.3-0.5, not ~0). Pre-registered, NOT tuned to outcome.
ETA_PLAUSIBLE_FLOOR = 0.30

# meV-per-dimensionless-unit tie (same as H_014): Omega_eff(U=1)=F_GLUE maps to OMEGA_ROOMT_MEV.
MEV_PER_UNIT = OMEGA_ROOMT_MEV / F_GLUE
def U_for_omega(omega_meV):
    """Dimensionless bare interaction U whose retarded glue remainder = omega_meV."""
    return omega_meV / OMEGA_ROOMT_MEV

# ----------------------------------------------------------------------------- channel Stoner products
def S_sdw(U, eta):
    return U * N_DOS * eta                                       # particle-hole, nesting-scaled

def S_cdw(U, eta):
    V = V_INTERSITE_FRAC * U
    return (U - 2.0 * V) * N_DOS * eta                           # charge channel, nesting-scaled

def S_ps(U, eta):
    if U <= U_C_PS:
        return 0.0
    return (U - U_C_PS) * N_DOS * KAPPA_PS                       # compressibility — NOT nesting-scaled

def S_sc(U, eta):
    omega_eff = F_GLUE * U                                       # retarded attractive remainder
    chi_pp = N_DOS * L_PP
    return omega_eff * chi_pp                                    # eta-independent (pair channel)

CHANNELS = [("SDW", S_sdw), ("CDW", S_cdw), ("PS", S_ps), ("SC", S_sc)]

# ----------------------------------------------------------------------------- U-sweep threshold finder
U_MIN, U_MAX, U_STEP = 0.0, 8.0, 0.001
n_U = int(round((U_MAX - U_MIN) / U_STEP)) + 1
U_GRID = [round(U_MIN + i * U_STEP, 6) for i in range(n_U)]

def threshold_U(S_func, eta):
    """Smallest U on the grid at which S_func(U,eta) >= 1 (linear interp between nodes)."""
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

# ----------------------------------------------------------------------------- eta sweep
ph_names = ["SDW", "CDW", "PS"]
sweep_rows = []
eta_first_sc_leads = None      # the LARGEST eta (least frustration) at which SC already leads
eta_critical = None            # the boundary eta*: largest eta where SC leads (= eta_first_sc_leads)

for eta in ETA_GRID:
    th = {name: threshold_U(func, eta) for name, func in CHANNELS}
    sc_U = th["SC"]
    ph_th = {n: th[n] for n in ph_names if th[n] is not None}
    leading_ph = min(ph_th, key=ph_th.get) if ph_th else None
    leading_ph_U = ph_th[leading_ph] if leading_ph else None
    sc_leads = (sc_U is not None) and (leading_ph_U is not None) and (sc_U < leading_ph_U)
    # window width = how far above SC-onset before the first particle-hole channel triggers
    if sc_leads:
        window_width = leading_ph_U - sc_U
    else:
        window_width = 0.0
    sweep_rows.append({
        "eta_nest": eta,
        "U_sc": round(sc_U, 4) if sc_U is not None else None,
        "U_sdw": round(th["SDW"], 4) if th["SDW"] is not None else None,
        "U_cdw": round(th["CDW"], 4) if th["CDW"] is not None else None,
        "U_ps": round(th["PS"], 4) if th["PS"] is not None else None,
        "leading_ph": leading_ph,
        "U_leading_ph": round(leading_ph_U, 4) if leading_ph_U is not None else None,
        "sc_leads": sc_leads,
        "window_width": round(window_width, 4),
    })
    if sc_leads and eta_first_sc_leads is None:
        # first time (descending eta) SC leads -> this is the upper boundary of the escape regime
        eta_first_sc_leads = eta
        eta_critical = eta

# Closed-form cross-check of the critical eta (independent of the grid):
#   SC threshold  U_sc = 1 / F_GLUE              (eta-independent)
#   SDW threshold U_sdw = 1 / (N_DOS * eta)
#   SC leads SDW  <=>  U_sc < U_sdw  <=>  1/F_GLUE < 1/(N*eta)  <=>  eta < F_GLUE/N
# CDW threshold (with V=V/U*U): S_cdw = (U-2V)*N*eta = U*(1-2*V/U_frac)*N*eta
#   U_cdw = 1 / ((1-2*V_INTERSITE_FRAC)*N*eta) ; (1-0.6)=0.4 -> U_cdw = 1/(0.4*N*eta) > U_sdw,
#   so SDW is always the leading particle-hole competitor here -> SDW sets eta*.
ETA_CRIT_CLOSED = F_GLUE / N_DOS                      # = 0.45 (eta below this -> SC leads)
U_SC_CLOSED = 1.0 / F_GLUE                            # = 2.2222 (eta-independent)

# room-T glue demand mapped to U (same tie as H_014)
U_roomt_bare    = U_for_omega(OMEGA_ROOMT_MEV)        # = 1.0 by construction
U_roomt_relaxed = U_for_omega(OMEGA_RELAXED_MEV)      # < 1.0

# At the relaxed room-T demand, what eta is needed for the relaxed-U glue to also be SC-leading?
# Note U_roomt_relaxed (0.543) is BELOW U_sc(=2.222): the relaxed glue mapped to U does not even
# reach SC threshold on its own. The room-T mapping is a SEPARATE axis from the leading-channel
# race. We report the leading-channel race (the competing-order wall) as the primary result, and
# also flag whether the room-T-relaxed U lands in any SC-leading window.
escape_exists = eta_critical is not None
eta_plausible = escape_exists and (eta_critical >= ETA_PLAUSIBLE_FLOOR)

# does the relaxed room-T U sit inside the SC-leading window at the critical eta?
roomt_relaxed_inside = False
if escape_exists:
    crit_row = next(r for r in sweep_rows if r["eta_nest"] == eta_critical)
    if crit_row["sc_leads"] and crit_row["U_sc"] is not None and crit_row["U_leading_ph"] is not None:
        roomt_relaxed_inside = (crit_row["U_sc"] <= U_roomt_relaxed <= crit_row["U_leading_ph"])

metrics = {
    "eta_sweep_hi": ETA_HI, "eta_sweep_lo": ETA_LO, "eta_sweep_step": ETA_STEP, "n_eta": n_eta,
    "U_sc_closed": round(U_SC_CLOSED, 4),
    "eta_critical_grid": eta_critical,
    "eta_critical_closed": round(ETA_CRIT_CLOSED, 4),
    "escape_exists": escape_exists,
    "eta_plausible_floor": ETA_PLAUSIBLE_FLOOR,
    "eta_plausible": eta_plausible,
    "leading_ph_competitor_at_h014": "SDW",
    "U_roomt_bare": round(U_roomt_bare, 4),
    "U_roomt_relaxed": round(U_roomt_relaxed, 4),
    "roomt_relaxed_inside_window": roomt_relaxed_inside,
    # representative rows for the verdict
    "row_eta085_sc_leads": next(r["sc_leads"] for r in sweep_rows if r["eta_nest"] == 0.85),
    "row_eta050_sc_leads": next(r["sc_leads"] for r in sweep_rows if r["eta_nest"] == 0.50),
    "row_eta045_sc_leads": next(r["sc_leads"] for r in sweep_rows if r["eta_nest"] == 0.45),
    "row_eta044_sc_leads": next(r["sc_leads"] for r in sweep_rows if r["eta_nest"] == 0.44),
    "row_eta030_sc_leads": next(r["sc_leads"] for r in sweep_rows if r["eta_nest"] == 0.30),
    "row_eta010_sc_leads": next(r["sc_leads"] for r in sweep_rows if r["eta_nest"] == 0.10),
}

# ----------------------------------------------------------------------------- falsifiers (>=4)
# A Falsifier is TRUE when TRIGGERED (component refuted). PASS = NOT triggered.
falsifiers = [
    # F1: an SC-leading escape must EXIST somewhere on the (0.10, 0.85] frustration sweep.
    Falsifier("F1_escape_exists",
              lambda m: not m["escape_exists"],
              "PASS = there is some eta_nest on the swept frustration range at which SC becomes "
              "the leading instability. FAIL = competing order leads for EVERY swept eta -> wall."),
    # F2: the critical eta_nest* must be PHYSICALLY PLAUSIBLE (>= the pre-registered floor 0.30):
    #     a frustrated/incommensurate flat-band host can realistically reach this nesting
    #     suppression. FAIL = SC only leads at an absurdly small (unphysical) nesting.
    Falsifier("F2_eta_critical_plausible",
              lambda m: not m["eta_plausible"],
              "PASS = the critical eta_nest* (below which SC leads) is >= the pre-registered "
              "plausible-frustration floor (0.30). FAIL = SC only leads at unphysical eta<0.30."),
    # F3: the grid-found eta* must AGREE with the closed-form eta* = f_glue/N (= 0.45) within one
    #     sweep step (a self-consistency / no-bug check that the toy is doing what we claim).
    Falsifier("F3_grid_matches_closed_form",
              lambda m: (m["eta_critical_grid"] is None
                         or abs(m["eta_critical_grid"] - m["eta_critical_closed"]) > (m["eta_sweep_step"] + 1e-9)),
              "PASS = grid-determined eta_critical matches the closed-form f_glue/N within one "
              "sweep step. FAIL = grid and analytic boundary disagree (model/implementation bug)."),
    # F4: at H_014's original strong nesting (eta_nest=0.85), SC must STILL be sub-leading — i.e.
    #     the escape is a genuine CHANGE from H_014, not a re-derivation accident.
    Falsifier("F4_reproduces_h014_at_strong_nesting",
              lambda m: m["row_eta085_sc_leads"],
              "PASS = at eta_nest=0.85 (H_014's value) SC is NOT leading (reproduces H_014's "
              "CLOSED-NEGATIVE). FAIL = the toy no longer reproduces H_014 -> not a valid continuation."),
    # F5: monotonic ordering sanity — at strong nesting (0.50) SC sub-leads, at weak nesting
    #     (0.30) SC leads; the escape boundary must lie strictly between, never inverted.
    Falsifier("F5_monotone_escape_boundary",
              lambda m: not ((not m["row_eta050_sc_leads"]) and m["row_eta030_sc_leads"]),
              "PASS = SC sub-leads at eta=0.50 and leads at eta=0.30 (the frustration knob works "
              "monotonically). FAIL = the escape is non-monotone / inverted -> model pathology."),
]

verdict = evaluate(metrics, falsifiers)

# ----------------------------------------------------------------------------- verbatim stdout
print("=== H_016 competing-order ESCAPE — does frustrating the nesting let SC lead? (sweep eta_nest) ===")
print("  TOY Stoner/RPA multi-channel model (self-contained, same formulas as H_014, no fit, no tune-to-green).")
print(f"  fixed constants: N_DOS={N_DOS}  kappa_ps={KAPPA_PS}  U_c_ps={U_C_PS}  "
      f"L_pp={L_PP}  f_glue={F_GLUE}  V/U={V_INTERSITE_FRAC}")
print(f"  SWEPT knob: eta_nest from {ETA_HI} down to {ETA_LO} step {ETA_STEP}  ({n_eta} values)")
print(f"  room-T glue demand: 2D-bare Omega={round(OMEGA_ROOMT_MEV,1)} meV  relaxed(+@) Omega={OMEGA_RELAXED_MEV} meV")
print(f"  U sweep: [{U_MIN}, {U_MAX}] step {U_STEP}  ({n_U} nodes)")
print("  --- eta_nest sweep (U* per channel; SC leads when U_sc < every particle-hole U*) ---")
print("    eta_nest  U_sc    U_sdw   U_cdw   U_ps     lead_ph  U_lead_ph  SC_leads  win_width")
for r in sweep_rows:
    if (round(r["eta_nest"] * 100) % 5 == 0) or (r["eta_nest"] in (0.46, 0.44)):
        def fmt(x): return f"{x:7.3f}" if x is not None else "   None"
        print(f"    {r['eta_nest']:.2f}    {fmt(r['U_sc'])} {fmt(r['U_sdw'])} {fmt(r['U_cdw'])} "
              f"{fmt(r['U_ps'])}  {str(r['leading_ph']):>5s}   {fmt(r['U_leading_ph'])}   "
              f"{str(r['sc_leads']):>5s}    {r['window_width']:.3f}")
print("  --- escape summary ---")
print(f"    SC threshold (eta-independent)     : U_sc = {metrics['U_sc_closed']}")
print(f"    leading particle-hole competitor    : {metrics['leading_ph_competitor_at_h014']} (sets eta*)")
print(f"    critical eta* (grid)                : {metrics['eta_critical_grid']}")
print(f"    critical eta* (closed form f_glue/N): {metrics['eta_critical_closed']}")
print(f"    SC-leading escape exists on sweep   : {metrics['escape_exists']}")
print(f"    plausible-frustration floor          : {metrics['eta_plausible_floor']}")
print(f"    eta* is physically plausible        : {metrics['eta_plausible']}")
print(f"    room-T glue mapped to U (bare/relax) : {metrics['U_roomt_bare']} / {metrics['U_roomt_relaxed']}")
print(f"    relaxed room-T U inside SC window    : {metrics['roomt_relaxed_inside_window']}")
print("  --- falsifiers (PASS = not triggered) ---")
for r in verdict["falsifiers"]:
    print(f"  falsifier {r['name']:34s}: {r['status']}")
print(f"  falsifiers_pass = {verdict['n_pass']}/{verdict['n_total']}")
if verdict["all_pass"]:
    print(f"VERDICT: an SC-LEADING ESCAPE OPENS for frustration eta_nest < {metrics['eta_critical_closed']} "
          f"(>= plausible floor {ETA_PLAUSIBLE_FLOOR}) — frustrating the nesting LIFTS H_014's competing-order "
          "wall in this toy. The escape is a TESTABLE coordinate (frustrated host), NOT a discovery; "
          "absorbed=false, GATE_OPEN. (HONEST POSITIVE on the escape lever.)")
else:
    print("VERDICT: SC stays SUB-LEADING across the swept frustration range / the escape is implausible "
          "or inconsistent — competing order is a ROBUST wall under this toy (CLOSED-NEGATIVE on this lever).")

out = os.path.join(os.path.dirname(__file__), "result.json")
with open(out, "w") as f:
    json.dump({"verdict": verdict, "sweep_rows": sweep_rows}, f, indent=2)
