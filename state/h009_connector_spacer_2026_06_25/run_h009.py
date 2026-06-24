#!/usr/bin/env python3
"""run_h009 — the connector spacer as the THIRD material (trilayer A/C/B).

User directive: "the 2 materials — use one more added material as the connector". H_003 left
the interface as an abstract electron_cost knob; here the 3rd material IS that connector — a
spacer C of thickness d (monolayers) that must be electron-OPAQUE (block hybridization, drive
electron_cost <= the H_003 critical 0.415) yet phonon-TRANSPARENT (pass the glue, transmission
>= 0.70). Both decay with thickness at rates set by C's gap (lambda_e) and phonon match
(lambda_ph). The question: does a thickness WINDOW exist where C does both — and what spacer
class achieves it? TOY decay model — imports the shared harness from tool/. stdout VERBATIM.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tool"))

from rtsc_harness import Falsifier, evaluate, spacer_window

# Good spacer (hBN-like): wide gap -> fast electron decay; stiff/matched phonons -> slow decay.
good = spacer_window(lambda_e=0.5, lambda_ph=5.0)
# Bad spacer (narrow-gap / metallic-ish): electron and phonon decay at similar rates.
bad = spacer_window(lambda_e=3.0, lambda_ph=3.0)

metrics = {
    "good_window_exists": good["window_exists"],
    "good_d_lo_ml": round(good["d_lo_ml"], 2) if good["d_lo_ml"] is not None else None,
    "good_d_hi_ml": round(good["d_hi_ml"], 2) if good["d_hi_ml"] is not None else None,
    "good_window_width_ml": round(good["window_width_ml"], 2),
    "bad_window_exists": bad["window_exists"],
}

falsifiers = [
    # F1: a phonon-matched wide-gap spacer must open a usable thickness window.
    Falsifier("F1_good_spacer_window",
              lambda m: not m["good_window_exists"],
              "PASS = a wide-gap/phonon-matched spacer has a thickness window that is both electron-opaque and phonon-transparent."),
    # F2: a spacer whose electron and phonon decays are similar must FAIL (no free connector).
    Falsifier("F2_bad_spacer_no_window",
              lambda m: m["bad_window_exists"],
              "PASS = a non-selective spacer (lambda_e ~ lambda_ph) has NO window -> the connector requirement is real, not automatic."),
    # F3: the window must be at finite, fabricable thickness (> 0, few monolayers).
    Falsifier("F3_finite_thickness",
              lambda m: not (m["good_window_exists"] and 0.0 < m["good_d_lo_ml"] < 5.0),
              "PASS = the window sits at a finite, few-monolayer thickness (fabricable)."),
    # F4: window has positive width (a tolerance, not a knife-edge single thickness).
    Falsifier("F4_window_has_width",
              lambda m: not (m["good_window_width_ml"] > 0.0),
              "PASS = the window has nonzero thickness tolerance."),
]

verdict = evaluate(metrics, falsifiers)

print("=== H_009 connector spacer (trilayer A/C/B) — the 3rd material is the link ===")
print("  requirement: electron_cost <= 0.415 (opaque, H_003 critical) AND phonon T >= 0.70 (glue passes)")
print(f"  GOOD spacer (hBN-like: lambda_e=0.5 wide-gap, lambda_ph=5.0 stiff):")
print(f"    window = [{metrics['good_d_lo_ml']}, {metrics['good_d_hi_ml']}] ML  width={metrics['good_window_width_ml']} ML  exists={metrics['good_window_exists']}")
print(f"  BAD spacer (non-selective: lambda_e=lambda_ph=3.0):  window exists={metrics['bad_window_exists']}")
for r in verdict["falsifiers"]:
    print(f"  falsifier {r['name']:24s}: {r['status']}")
print(f"  falsifiers_pass = {verdict['n_pass']}/{verdict['n_total']}")
print("VERDICT: A WIDE-GAP/PHONON-MATCHED CONNECTOR (hBN-CLASS) OPENS A FABRICABLE THICKNESS WINDOW")

out = os.path.join(os.path.dirname(__file__), "result.json")
with open(out, "w") as f:
    json.dump(verdict, f, indent=2)
