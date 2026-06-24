#!/usr/bin/env python3
"""run_h006 — deterministic toy probe for HYPOTHESES card H_006.

F2 from the SF brainstorm, promoted to a falsifiable card: "is the quantum-geometry
lever (integrated trace of the Fubini-Study metric) DIMENSION-INVARIANT (capped at 2D)?"
If invariant, going to 3D / synthetic dimension does NOT relax the two-lever wall (H_001).

This is a TOY tight-binding computation (canonical 2-level winding band), not a real-material
verdict — it computes the quantum metric by finite difference, no fitting. Imports the shared
harness from repo-root tool/ (anima-parity). stdout is pasted VERBATIM into the card.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tool"))

from rtsc_harness import (
    Falsifier,
    evaluate,
    quantum_metric_trace_2d_dirac,
    quantum_metric_trace_separable,
)

dims = [1, 2, 3, 4]
sep = {d: quantum_metric_trace_separable(d) for d in dims}
dirac2d = quantum_metric_trace_2d_dirac()
closed_form_dev = max(abs(sep[d] - 0.25 * d) for d in dims)  # vs 0.25*d expectation
growth_ratio = sep[3] / sep[1]

metrics = {
    "sep_tr_g": {str(d): round(sep[d], 4) for d in dims},
    "dirac2d_tr_g": round(dirac2d, 4),
    "closed_form_deviation": round(closed_form_dev, 4),
    "growth_ratio_d3_over_d1": round(growth_ratio, 3),
}

falsifiers = [
    Falsifier("F1_dimension_invariant",
              lambda m: m["growth_ratio_d3_over_d1"] < 1.1,
              "geometry lever flat across dim → dimension-invariant (hypothesis SUPPORTED)"),
    Falsifier("F3_numerics_broken",
              lambda m: m["closed_form_deviation"] > 0.05,
              "separable scan deviates from 0.25*d by >5% → numerics broken, halt"),
    Falsifier("F4_metric_ill_defined",
              lambda m: m["dirac2d_tr_g"] <= 0.0,
              "non-separable 2D metric non-positive → metric ill-defined"),
]

verdict = evaluate(metrics, falsifiers)
# hypothesis = "dimension-invariant"; it is REFUTED if the lever grows with dim.
dimension_invariant = growth_ratio < 1.1
verdict_class = "DIMENSION-INVARIANT (real ceiling)" if dimension_invariant \
    else "DIMENSION-EXTENSIVE (toy: geometry lever grows with dim)"

out = {"card": "H_006", "verdict_class": verdict_class, "metrics": metrics,
       "falsifier_ledger": verdict}

print("=== H_006 FS two-lever bound — dimension scan (TOY model, real computation) ===")
for d in dims:
    print(f"  separable d={d}:  <tr g> = {sep[d]:.4f}   (closed-form 0.25*d = {0.25*d:.4f})")
print(f"  non-separable 2D Dirac:  <tr g> = {dirac2d:.4f}")
print(f"  growth ratio <tr g>(d=3)/(d=1) = {growth_ratio:.3f}")
print(f"  closed-form deviation = {closed_form_dev:.4f}")
for r in verdict["falsifiers"]:
    print(f"  falsifier {r['name']:24s}: {r['status']}")
print(f"VERDICT: {verdict_class}")
print("NOTE: toy 2-level model only — computes the GEOMETRY lever, not coupling Omega;")
print("      real verdict needs 3D flat-band ED with the actual quantum metric (src/, pod).")

with open(os.path.join(os.path.dirname(__file__), "result.json"), "w") as fh:
    json.dump(out, fh, indent=2)
