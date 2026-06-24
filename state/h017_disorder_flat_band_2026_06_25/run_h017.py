#!/usr/bin/env python3
"""run_h_017 — deterministic disorder-as-geometry-lever probe for HYPOTHESES card H_017.

BRAINSTORM SEED O2 (M4 OBSTACLE-as-resource): the geometry lever the whole flat-band
campaign needs is a FLAT, high-DOS band carrying nonzero quantum geometry. Crystalline
flat bands (MATBG, kagome, tMoTe2) are hard to engineer. The O2 question: does DISORDER
give the flat-band lever "for free" — a strongly broadened band whose peak DOS rises as it
flattens — WITHOUT the crystallinity? OR does the SAME disorder that flattens the band also
ANDERSON-LOCALIZE the carriers, destroying the phase coherence superconductivity requires?

A superconducting condensate needs the pairing coherence length xi_0 to fit INSIDE a
delocalized (metallic / extended-or-weakly-localized) region: xi_loc > xi_0. If disorder
localizes states on a scale SHORTER than the Cooper pair size, the pairs cannot phase-lock
into a condensate (the standard Anderson / Finkel'stein picture of disorder-killed SC).

This is a TOY, deterministic two-knob sweep (no fitting, no real-material numbers fitted, no
tune-to-green). It is SELF-CONTAINED: every helper is INLINE (we deliberately do NOT import
the shared tool/rtsc_harness.py, per the campaign idiom, to avoid edit conflicts).

MODEL (deterministic, dimensionless)
------------------------------------
A clean band of width W_band carries a baseline DOS ~ 1/W_band. Disorder of strength W_dis
does two competing things:

  (1) FLATTENS / piles up DOS.  Treat the disorder-broadened band as a (semicircular-ish)
      effective band whose spectral weight gets pushed toward a sharper central peak as the
      lattice loses long-range coherence (precursor of a disorder-induced flat region /
      band-tail pile-up). We model the PEAK-DOS GAIN as
          G_dos(W_dis) = 1 + alpha * (W_dis / W_band)
      a monotone-rising, conservative LINEAR pile-up (alpha = pile-up efficiency). DOS gain
      >= DOS_GAIN_THRESH (default 2x) is the "flat-enough" geometry-lever condition.
      (LIMIT: a real broadened band's peak DOS does NOT rise without bound — Lifshitz tails
      eventually SPREAD weight; this linear form is a generous UPPER bound on the DOS gain,
      which only makes the obstacle-as-resource case EASIER, so a closed-negative here is
      robust.)

  (2) LOCALIZES.  2D scaling theory of localization (Abrahams-Anderson-Licciardello-
      Ramakrishnan 1979, gang of four): in 2D ALL states localize, with a localization
      length that grows EXPONENTIALLY in the dimensionless conductance g = k_F * l / 2
      (Drude sheet conductance in units of e^2/h, weak-disorder regime):
          xi_loc / a  ~  exp( pi * g / 2 ) ,   g = k_F*l/2 ,   l = mean free path.
      Born/Drude disorder scattering gives a mean free path l ~ l0 * (W0 / W_dis)^2
      (scattering rate ~ W_dis^2), i.e. g(W_dis) = g0 * (W0 / W_dis)^2. We use the standard
      2D weak-localization form
          xi_loc(W_dis) / a = exp( BETA / W_dis^2 )
      with BETA absorbing (pi/2)*g0*W0^2 — a defensible weak-disorder 2D scaling form. As
      W_dis grows, xi_loc collapses SUPER-exponentially. (Strong-disorder/3D power-law
      alternatives are listed as honest limits; the 2D exponential is the HARDEST case for
      delocalization and is the regime the flat-band campaign actually lives in — 2D moire
      and 2D kagome sheets.)

The pairing coherence length xi_0 (in units of a) is a FIXED structural constant set by the
clean band: xi_0 ~ hbar v_F / (pi Delta) shrinks as the band flattens, but a flat band's
tiny v_F gives a SMALL xi_0 — we take a fixed, generous (small) xi_0 so the delocalization
test is as EASY as possible. DELOCALIZED <=> xi_loc(W_dis) > xi_0.

GATING QUESTION: sweep W_dis. Is there ANY window where simultaneously
    G_dos(W_dis) >= DOS_GAIN_THRESH  (flat-enough)  AND  xi_loc(W_dis) > xi_0 (delocalized)?
Report the window (lo, hi in W_dis), or that disorder-flatness and delocalization are
MUTUALLY EXCLUSIVE (closed-negative) — the O2 'obstacle-as-resource closes if disorder also
kills coherence' falsifier.

stdout is pasted VERBATIM into the card. Run twice; bytes must be identical.
"""
import json
import math
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
# All dimensionless. W_band sets the energy unit; lengths in units of lattice constant a.
W_BAND          = 1.0     # clean band width (energy unit)
ALPHA_PILEUP    = 1.0     # DOS pile-up efficiency: G_dos = 1 + ALPHA*(W_dis/W_band). GENEROUS.
DOS_GAIN_THRESH = 2.0     # "flat-enough" geometry-lever threshold: peak DOS >= 2x clean.
BETA_LOC        = 0.50    # 2D weak-loc scaling prefactor: xi_loc/a = exp(BETA / W_dis^2).
XI_0            = 3.0     # pairing coherence length in units of a (FIXED, generous/small).
# NOTE on XI_0: a Cooper pair must span MANY lattice sites to be a pair (xi_0 >> a); xi_0=3a
# is already an aggressively SMALL (favorable) choice. Real SC xi_0 ~ 1-100 nm = many a.

# ----------------------------------------------------------------------------- model functions
def G_dos(W_dis):
    """Peak-DOS gain vs clean band (monotone rising, generous linear pile-up)."""
    return 1.0 + ALPHA_PILEUP * (W_dis / W_BAND)

XI_LOC_CAP = 1.0e12   # cap: xi_loc beyond ~1e12 a is "effectively extended" (>> any sample);
                      # also guards math.exp overflow at very weak disorder. Deterministic.
def xi_loc(W_dis):
    """2D weak-localization localization length in units of a (exp in 1/W_dis^2), capped."""
    if W_dis <= 0.0:
        return XI_LOC_CAP
    arg = BETA_LOC / (W_dis * W_dis)
    if arg > math.log(XI_LOC_CAP):
        return XI_LOC_CAP
    return math.exp(arg)

# Closed forms for the two boundaries (deterministic, no root-search drift):
#   flat-enough boundary:  G_dos(W_dis) >= DOS_GAIN_THRESH
#       1 + ALPHA*(W/W_band) >= DOS_GAIN_THRESH  ->  W >= W_band*(DOS_GAIN_THRESH-1)/ALPHA
W_FLAT_MIN = W_BAND * (DOS_GAIN_THRESH - 1.0) / ALPHA_PILEUP   # smallest W_dis that is flat-enough
#   delocalized boundary:  xi_loc(W_dis) > XI_0
#       exp(BETA/W^2) > XI_0  ->  BETA/W^2 > ln(XI_0)  ->  W^2 < BETA/ln(XI_0)  ->  W < sqrt(...)
W_DELOC_MAX = math.sqrt(BETA_LOC / math.log(XI_0))             # largest W_dis still delocalized

# ----------------------------------------------------------------------------- sweep
W_MIN, W_MAX, W_STEP = 0.0, 3.0, 0.0005
n_steps = int(round((W_MAX - W_MIN) / W_STEP)) + 1
W_grid = [round(W_MIN + i * W_STEP, 6) for i in range(n_steps)]

window_points = []
for W in W_grid:
    flat = G_dos(W) >= DOS_GAIN_THRESH
    deloc = xi_loc(W) > XI_0
    if flat and deloc:
        window_points.append(W)

if window_points:
    win_lo = min(window_points)
    win_hi = max(window_points)
    win_width = win_hi - win_lo
    window_exists = True
else:
    win_lo = win_hi = None
    win_width = 0.0
    window_exists = False

# Analytic window check (independent of grid): a window exists iff W_FLAT_MIN < W_DELOC_MAX.
analytic_window_exists = W_FLAT_MIN < W_DELOC_MAX
analytic_win_width = max(0.0, W_DELOC_MAX - W_FLAT_MIN)

# Diagnostics at the two boundaries:
xi_at_flatmin = xi_loc(W_FLAT_MIN)          # localization length right where the band turns flat-enough
gdos_at_delocmax = G_dos(W_DELOC_MAX)       # DOS gain right where it is about to localize the pair
# The crux number: at the disorder needed to reach 2x DOS, how localized are we vs the pair?
xi_over_xi0_at_flatmin = xi_at_flatmin / XI_0

metrics = {
    "W_band":                 W_BAND,
    "alpha_pileup":           ALPHA_PILEUP,
    "dos_gain_thresh":        DOS_GAIN_THRESH,
    "beta_loc":               BETA_LOC,
    "xi_0":                   XI_0,
    "W_flat_min":             round(W_FLAT_MIN, 6),
    "W_deloc_max":            round(W_DELOC_MAX, 6),
    "window_exists":          window_exists,
    "window_lo":              round(win_lo, 6) if win_lo is not None else None,
    "window_hi":              round(win_hi, 6) if win_hi is not None else None,
    "window_width":           round(win_width, 6),
    "analytic_window_exists": analytic_window_exists,
    "analytic_window_width":  round(analytic_win_width, 6),
    "xi_loc_at_W_flat_min":   round(xi_at_flatmin, 6),
    "xi_over_xi0_at_flat_min": round(xi_over_xi0_at_flatmin, 6),
    "gdos_at_W_deloc_max":    round(gdos_at_delocmax, 6),
}

# ----------------------------------------------------------------------------- falsifiers (>=4)
# A Falsifier is TRUE when TRIGGERED (component refuted). PASS = NOT triggered.
falsifiers = [
    # F1: a flat-AND-delocalized window must EXIST at all (grid sweep).
    Falsifier("F1_window_exists",
              lambda m: not m["window_exists"],
              "PASS = a finite W_dis window exists where the band is flat-enough (DOS gain >= "
              "2x) AND still delocalized (xi_loc > xi_0). FAIL = disorder-flatness and "
              "delocalization are mutually exclusive -> obstacle-as-resource CLOSES (O2 dead)."),
    # F2: the analytic boundary check must agree (W_flat_min < W_deloc_max) — guards the grid.
    Falsifier("F2_analytic_window_exists",
              lambda m: not m["analytic_window_exists"],
              "PASS = the closed-form boundaries overlap (W_flat_min < W_deloc_max), confirming "
              "the window is real and not a grid artifact. FAIL = no overlap -> closed-negative."),
    # F3: at the disorder needed to reach 2x DOS, the system must still be delocralized on the
    #     pair scale (xi_loc(W_flat_min) > xi_0).
    Falsifier("F3_flat_point_delocalized",
              lambda m: not (m["xi_loc_at_W_flat_min"] > m["xi_0"]),
              "PASS = at the disorder that first makes the band flat-enough, xi_loc still exceeds "
              "the pair size xi_0. FAIL = reaching 2x DOS already localizes carriers below the "
              "Cooper-pair length -> the flatness you bought has no coherent carriers."),
    # F4: the window must have real WIDTH (a finite tolerance), not a measure-zero touch.
    Falsifier("F4_window_has_width",
              lambda m: not (m["window_exists"] and m["window_width"] > 0.02),
              "PASS = the flat-and-delocalized window has finite W_dis tolerance (>0.02), not a "
              "fragile knife-edge. FAIL = the window is measure-zero / nonexistent."),
    # F5: the localization length where the band turns flat-enough must beat the pair size by a
    #     real margin (xi_loc/xi_0 > 1.5) — a robustness cushion, not a marginal touch.
    Falsifier("F5_margin_above_pair",
              lambda m: not (m["xi_over_xi0_at_flat_min"] > 1.5),
              "PASS = at flat-onset, xi_loc/xi_0 > 1.5 (comfortable delocalization margin). "
              "FAIL = even if a sliver of window exists, the pair barely fits -> fragile."),
]

verdict = evaluate(metrics, falsifiers)

# ----------------------------------------------------------------------------- verbatim stdout
print("=== H_017 disorder-as-geometry-lever — does disorder give a flat high-DOS band 'for free' "
      "without killing coherence? ===")
print("  TOY deterministic two-knob sweep (self-contained, no fit, no tune-to-green).")
print("  SEED O2 (M4 obstacle-as-resource): disorder flattens DOS but Anderson-localizes carriers.")
print(f"  fixed constants: W_band={W_BAND}  alpha_pileup={ALPHA_PILEUP}  dos_gain_thresh={DOS_GAIN_THRESH}  "
      f"beta_loc={BETA_LOC}  xi_0={XI_0} (units of a)")
print("  models: G_dos(W) = 1 + alpha*(W/W_band) [generous linear DOS pile-up];  "
      "xi_loc(W)/a = exp(beta/W^2) [2D weak-localization scaling]")
print(f"  W_dis sweep: [{W_MIN}, {W_MAX}] step {W_STEP}  ({n_steps} nodes)")
print("  --- boundaries (closed form) ---")
print(f"    flat-enough onset    : W_dis >= {metrics['W_flat_min']}  (DOS gain reaches {DOS_GAIN_THRESH}x)")
print(f"    delocalized limit    : W_dis <  {metrics['W_deloc_max']}  (xi_loc drops to xi_0={XI_0})")
print(f"  --- overlap test: does the band turn flat BEFORE it localizes the pair? ---")
print(f"    W_flat_min < W_deloc_max ? : {metrics['analytic_window_exists']}  "
      f"(flat_min={metrics['W_flat_min']}  deloc_max={metrics['W_deloc_max']})")
print(f"    flat-and-delocalized window: [{metrics['window_lo']}, {metrics['window_hi']}]  "
      f"width={metrics['window_width']}  exists={metrics['window_exists']}")
print("  --- crux diagnostics ---")
print(f"    xi_loc at flat-onset (W={metrics['W_flat_min']}) : {metrics['xi_loc_at_W_flat_min']} a   "
      f"(xi_0={XI_0} a  ->  xi_loc/xi_0 = {metrics['xi_over_xi0_at_flat_min']})")
print(f"    DOS gain at deloc-limit (W={metrics['W_deloc_max']}) : {metrics['gdos_at_W_deloc_max']}x   "
      f"(need {DOS_GAIN_THRESH}x)")
print("  --- falsifiers (PASS = not triggered) ---")
for r in verdict["falsifiers"]:
    print(f"  falsifier {r['name']:26s}: {r['status']}")
print(f"  falsifiers_pass = {verdict['n_pass']}/{verdict['n_total']}")
if verdict["all_pass"]:
    print("VERDICT: a FLAT-AND-DELOCALIZED window EXISTS — disorder can buy a >=2x DOS pile-up "
          "while xi_loc still exceeds the pair size xi_0; obstacle-as-resource (O2) SURVIVES this "
          "toy gate. (Still MODEL-PROBE; no claim any material IS an RTSC.)")
else:
    print("VERDICT: disorder-flatness and pair-scale delocalization are MUTUALLY EXCLUSIVE under "
          "this toy — the same disorder that flattens the band to >=2x DOS localizes carriers "
          "below the Cooper-pair length xi_0. Obstacle-as-resource (O2) CLOSES (CLOSED-NEGATIVE).")

out = os.path.join(os.path.dirname(__file__), "result.json")
with open(out, "w") as f:
    json.dump(verdict, f, indent=2)
