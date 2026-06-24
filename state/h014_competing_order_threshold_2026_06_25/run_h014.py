#!/usr/bin/env python3
"""run_h_014 — deterministic competing-order threshold probe for HYPOTHESES card H_014.

THE DOMINANT OPEN RISK of the whole +@ chain (H_004 L2 electronic glue / H_011 L3 bosonic
glue): the ~349 meV glue we need for a room-T SC pair amplitude is STRONG. A coupling that
strong, sitting on a flat band with an enormous density of states, may instead drive a
COMPETING ORDER — charge-density-wave (CDW), spin-density-wave (SDW), or phase separation
(PS) — BEFORE superconductivity ever condenses. Pairing and these particle-hole orders share
the SAME interaction; the leading instability is whichever susceptibility diverges FIRST as
the interaction is turned up.

This is a TOY Stoner/RPA-style multi-channel threshold model (no fitting, no real-material
numbers, no tune-to-green). It is SELF-CONTAINED: every helper is INLINE (we deliberately do
NOT import the shared tool/rtsc_harness.py, per the campaign idiom, to avoid conflicts).

MODEL (deterministic, dimensionless RPA bookkeeping)
----------------------------------------------------
A flat-band host has a large dimensionless density of states at the Fermi level, N (states
per unit interaction scale). Four channels, each with an RPA denominator 1 - g_c * chi_c(U).
A channel goes UNSTABLE (leading) when its Stoner-like product S_c = g_c * chi_c crosses 1;
the channel that reaches 1 at the SMALLEST interaction U is the LEADING instability.

  - SDW (particle-hole, spin):   S_sdw = U * N            (on-site Hubbard repulsion, full DOS)
  - CDW (particle-hole, charge): S_cdw = (U - 2*V) * N * eta_nest
                                  (intra-site charge channel = U screened by inter-site V;
                                   eta_nest in (0,1] is the flat-band nesting/geometry factor)
  - PS  (phase separation):      S_ps  = (U - U_c_ps) * N * kappa     for U > U_c_ps else 0
                                  (compressibility blow-up; kappa = curvature factor)
  - SC  (particle-particle):     S_sc  = (Omega_eff) * chi_pp
                                  Omega_eff = the bosonic/electronic GLUE attraction in the
                                  pair channel (set by the room-T Omega demand, H_004/H_011);
                                  chi_pp = N * L_pp, L_pp the Cooper logarithm enhancement.

The interaction U is swept. For SC, the glue attraction Omega_eff is tied to the SAME bare
interaction scale by a fixed retarded-overscreening fraction f_glue (the glue is the
attractive, retarded REMAINDER of the same interaction after the instantaneous repulsion is
subtracted): Omega_eff(U) = f_glue * U. NOTHING here is tuned to make SC win — f_glue,
eta_nest, kappa, L_pp, N are fixed structural constants stated up front.

We then ask the GATING QUESTION: at the interaction U* where SC first reaches threshold,
is SC the LEADING channel (no particle-hole channel reached threshold at a smaller U)? And
does the room-T glue demand (Omega ~ 349 meV, mapped to U via f_glue) sit INSIDE or OUTSIDE
that SC-leading window?

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
OMEGA_ROOMT_MEV = TC_TARGET_K * DEFLATE / (0.11 * KB_FACTOR)   # ~ 642.6 meV (2D bare)
# H_004/H_011 relaxed room-T glue demand after the verified +@ levers (3D, connector, geometry):
OMEGA_RELAXED_MEV = 349.0

# Structural (geometry/host) constants — fixed up front, NOT fitted, NOT tuned to green.
N_DOS        = 1.0        # dimensionless flat-band DOS at E_F (the lever sets the scale -> 1.0)
ETA_NEST     = 0.85       # flat-band CDW nesting/geometry factor in (0,1]; flat bands nest well
KAPPA_PS     = 0.55       # phase-separation compressibility-curvature factor
U_C_PS       = 1.30       # bare-U onset (in units of 1/N) below which PS does not activate
L_PP         = 1.00       # Cooper-channel log enhancement (TOY: no BCS log divergence kept -> 1)
F_GLUE       = 0.45       # retarded attractive fraction of the bare interaction available as glue
V_INTERSITE_FRAC = 0.30   # inter-site V as a fraction of U (screens the CDW charge channel)

# Map a glue Omega (meV) onto the dimensionless bare interaction U via the same f_glue tie:
#   Omega_eff(U) = F_GLUE * U  (dimensionless) ; and the meV<->dimensionless scale is set so
#   that U = 1.0 corresponds to the bare interaction whose retarded remainder = OMEGA_ROOMT_MEV.
# i.e. Omega_eff(U=1) = F_GLUE*1 maps to OMEGA_ROOMT_MEV  -> meV_per_unit = OMEGA_ROOMT_MEV/F_GLUE.
MEV_PER_UNIT = OMEGA_ROOMT_MEV / F_GLUE      # meV of bare interaction per dimensionless unit U

def U_for_omega(omega_meV):
    """The dimensionless bare interaction U whose retarded glue remainder = omega_meV."""
    # Omega_eff = F_GLUE*U  (dimensionless) ; Omega(meV) = Omega_eff * MEV_PER_UNIT
    #   -> omega_meV = F_GLUE*U*MEV_PER_UNIT = U*OMEGA_ROOMT_MEV ; so U = omega_meV/OMEGA_ROOMT_MEV
    return omega_meV / OMEGA_ROOMT_MEV

# ----------------------------------------------------------------------------- channel Stoner products
def S_sdw(U):
    return U * N_DOS

def S_cdw(U):
    V = V_INTERSITE_FRAC * U
    return (U - 2.0 * V) * N_DOS * ETA_NEST          # charge channel screened by inter-site V

def S_ps(U):
    if U <= U_C_PS:
        return 0.0
    return (U - U_C_PS) * N_DOS * KAPPA_PS

def S_sc(U):
    omega_eff = F_GLUE * U                            # retarded attractive remainder
    chi_pp = N_DOS * L_PP
    return omega_eff * chi_pp

CHANNELS = [("SDW", S_sdw), ("CDW", S_cdw), ("PS", S_ps), ("SC", S_sc)]

def threshold_U(S_func, U_grid):
    """Smallest U on the grid at which S_func(U) >= 1 (linear interpolation between nodes)."""
    prev_U, prev_S = None, None
    for U in U_grid:
        S = S_func(U)
        if S >= 1.0:
            if prev_U is None:
                return U
            # linear interp for a smoother, deterministic crossing
            frac = (1.0 - prev_S) / (S - prev_S) if S != prev_S else 0.0
            return prev_U + frac * (U - prev_U)
        prev_U, prev_S = U, S
    return None  # never crosses on the grid

# ----------------------------------------------------------------------------- sweep
U_MIN, U_MAX, U_STEP = 0.0, 6.0, 0.001
n_steps = int(round((U_MAX - U_MIN) / U_STEP)) + 1
U_grid = [round(U_MIN + i * U_STEP, 6) for i in range(n_steps)]

thresholds = {name: threshold_U(func, U_grid) for name, func in CHANNELS}

# Leading particle-hole competitor threshold (the SC killer = whichever of SDW/CDW/PS is first):
ph_names = ["SDW", "CDW", "PS"]
ph_thresholds = {n: thresholds[n] for n in ph_names if thresholds[n] is not None}
leading_ph_name = min(ph_thresholds, key=ph_thresholds.get) if ph_thresholds else None
leading_ph_U = ph_thresholds[leading_ph_name] if leading_ph_name else None
sc_U = thresholds["SC"]

# SC-leading window = interactions where SC has crossed but no particle-hole channel has.
# SC crosses at sc_U; the first particle-hole channel crosses at leading_ph_U.
# SC is the LEADING instability iff sc_U < leading_ph_U.
sc_leads = (sc_U is not None) and (leading_ph_U is not None) and (sc_U < leading_ph_U)
if sc_U is not None and leading_ph_U is not None:
    window_lo = sc_U
    window_hi = leading_ph_U
    window_width = max(0.0, window_hi - window_lo)
    window_exists = window_width > 0.0
else:
    window_lo = window_hi = None
    window_width = 0.0
    window_exists = False

# Where does the room-T glue demand sit?  Map both the 2D-bare and the relaxed demand to U.
U_roomt_bare    = U_for_omega(OMEGA_ROOMT_MEV)     # = 1.0 by construction
U_roomt_relaxed = U_for_omega(OMEGA_RELAXED_MEV)   # < 1.0 (relaxed by the +@ levers)

def inside_window(U):
    if not window_exists or U is None:
        return False
    return window_lo <= U <= window_hi

roomt_bare_inside    = inside_window(U_roomt_bare)
roomt_relaxed_inside = inside_window(U_roomt_relaxed)

metrics = {
    "omega_roomt_2d_meV":   round(OMEGA_ROOMT_MEV, 1),
    "omega_relaxed_meV":    round(OMEGA_RELAXED_MEV, 1),
    "U_sc_threshold":       round(sc_U, 4) if sc_U is not None else None,
    "U_sdw_threshold":      round(thresholds["SDW"], 4) if thresholds["SDW"] is not None else None,
    "U_cdw_threshold":      round(thresholds["CDW"], 4) if thresholds["CDW"] is not None else None,
    "U_ps_threshold":       round(thresholds["PS"], 4) if thresholds["PS"] is not None else None,
    "leading_ph_competitor": leading_ph_name,
    "U_leading_ph":         round(leading_ph_U, 4) if leading_ph_U is not None else None,
    "sc_leads":             sc_leads,
    "sc_leading_window_lo": round(window_lo, 4) if window_lo is not None else None,
    "sc_leading_window_hi": round(window_hi, 4) if window_hi is not None else None,
    "sc_leading_window_width": round(window_width, 4),
    "window_exists":        window_exists,
    "U_roomt_bare":         round(U_roomt_bare, 4),
    "U_roomt_relaxed":      round(U_roomt_relaxed, 4),
    "roomt_bare_inside_window":    roomt_bare_inside,
    "roomt_relaxed_inside_window": roomt_relaxed_inside,
}

# ----------------------------------------------------------------------------- falsifiers (>=4)
# A Falsifier is TRUE when TRIGGERED (component refuted). PASS = NOT triggered.
falsifiers = [
    # F1: an SC-leading window must EXIST at all. If SDW/CDW/PS always pre-empt SC for every U,
    #     the +@ glue can never condense as SC -> the whole architecture is refuted.
    Falsifier("F1_sc_window_exists",
              lambda m: not m["window_exists"],
              "PASS = a finite interaction window exists where SC is the LEADING instability "
              "(no particle-hole order pre-empts it). FAIL = competing order always wins -> +@ dead."),
    # F2: SC must reach threshold at a SMALLER interaction than the leading particle-hole order.
    Falsifier("F2_sc_leads_competitor",
              lambda m: not m["sc_leads"],
              "PASS = SC crosses its Stoner threshold BEFORE the leading CDW/SDW/PS competitor. "
              "FAIL = a density-wave / phase-separation order is the first instability."),
    # F3: the ROOM-T (relaxed, +@-levered) glue demand must sit INSIDE the SC-leading window.
    Falsifier("F3_roomt_relaxed_inside",
              lambda m: not m["roomt_relaxed_inside_window"],
              "PASS = the relaxed room-T glue demand (349 meV mapped to U) lands inside the "
              "SC-leading window. FAIL = the coupling we NEED for room-T SC drives competing order."),
    # F4: the window must have real WIDTH (a tolerance), not a measure-zero touch point.
    Falsifier("F4_window_has_width",
              lambda m: not (m["window_exists"] and m["sc_leading_window_width"] > 0.05),
              "PASS = the SC-leading window has finite interaction tolerance (>0.05 in U units), "
              "not a fragile knife-edge. FAIL = the window is a measure-zero coincidence."),
    # F5: the on-site SDW Stoner instability must NOT be the universal first mover at U->0+.
    #     (flat-band magnetism is the canonical killer; this checks it is held off past SC onset.)
    Falsifier("F5_sdw_not_first_mover",
              lambda m: (m["U_sdw_threshold"] is not None and m["U_sc_threshold"] is not None
                         and m["U_sdw_threshold"] < m["U_sc_threshold"]),
              "PASS = bare on-site SDW does not pre-empt SC. FAIL = flat-band magnetism (SDW) "
              "triggers first -> the canonical competing-order killer wins."),
]

verdict = evaluate(metrics, falsifiers)

# ----------------------------------------------------------------------------- verbatim stdout
print("=== H_014 competing-order threshold — does the room-T glue drive CDW/SDW/PS before SC? ===")
print("  TOY Stoner/RPA multi-channel model (self-contained, no fit, no tune-to-green).")
print(f"  fixed constants: N_DOS={N_DOS}  eta_nest={ETA_NEST}  kappa_ps={KAPPA_PS}  "
      f"U_c_ps={U_C_PS}  L_pp={L_PP}  f_glue={F_GLUE}  V/U={V_INTERSITE_FRAC}")
print(f"  room-T glue demand: 2D-bare Omega={metrics['omega_roomt_2d_meV']} meV  "
      f"relaxed(+@) Omega={metrics['omega_relaxed_meV']} meV")
print(f"  U sweep: [{U_MIN}, {U_MAX}] step {U_STEP}  ({n_steps} nodes)")
print("  --- channel Stoner thresholds (smallest U with S_c >= 1) ---")
print(f"    SC  (particle-particle, glue) : U* = {metrics['U_sc_threshold']}")
print(f"    SDW (particle-hole, spin)     : U* = {metrics['U_sdw_threshold']}")
print(f"    CDW (particle-hole, charge)   : U* = {metrics['U_cdw_threshold']}")
print(f"    PS  (phase separation)        : U* = {metrics['U_ps_threshold']}")
print(f"  leading particle-hole competitor: {metrics['leading_ph_competitor']} at U* = {metrics['U_leading_ph']}")
print(f"  SC leads competitor             : {metrics['sc_leads']}")
print(f"  SC-leading window               : "
      f"[{metrics['sc_leading_window_lo']}, {metrics['sc_leading_window_hi']}]  "
      f"width={metrics['sc_leading_window_width']}  exists={metrics['window_exists']}")
print(f"  room-T glue mapped to U         : bare U={metrics['U_roomt_bare']}  relaxed U={metrics['U_roomt_relaxed']}")
print(f"  room-T BARE    inside window    : {metrics['roomt_bare_inside_window']}")
print(f"  room-T RELAXED inside window    : {metrics['roomt_relaxed_inside_window']}")
print("  --- falsifiers (PASS = not triggered) ---")
for r in verdict["falsifiers"]:
    print(f"  falsifier {r['name']:24s}: {r['status']}")
print(f"  falsifiers_pass = {verdict['n_pass']}/{verdict['n_total']}")
if verdict["all_pass"]:
    print("VERDICT: an SC-LEADING WINDOW EXISTS and the RELAXED room-T glue sits INSIDE it — "
          "competing order does NOT pre-empt SC under this toy; the +@ architecture survives this gate.")
else:
    print("VERDICT: competing order PRE-EMPTS SC at the room-T glue demand — the +@ architecture "
          "fails the competing-order gate under this toy (CLOSED-NEGATIVE on this lever).")

out = os.path.join(os.path.dirname(__file__), "result.json")
with open(out, "w") as f:
    json.dump(verdict, f, indent=2)
