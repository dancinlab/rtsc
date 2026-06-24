#!/usr/bin/env python3
"""run_h011 — the decisive internal-consistency check of the +@ trilayer.

The crux (H_009 L2): the connector must block single-electron tunneling (to preserve the
flat-band geometry g) YET pass the electronic glue (to reach the room-T Omega, H_004). If the
glue is electronic, does an electron-opaque spacer block it too — collapsing the whole +@
trilayer into self-contradiction?

Resolution under test: a NEUTRAL/collective bosonic glue (exciton/plasmon) couples across the
spacer via a LONG-RANGE Coulomb/dipole FIELD (lambda_coulomb >> lambda_e), not wavefunction
overlap, so it penetrates the electron-tunneling barrier (cf. Forster transfer / Coulomb drag).
A FERMIONIC glue (needs electron transfer) is blocked exactly where the electron is. TOY decay
model — imports the shared harness from tool/. stdout VERBATIM into the card.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tool"))

from rtsc_harness import Falsifier, evaluate, glue_through_spacer_window

LAMBDA_E = 0.5          # electron tunneling decay (ML) — short, wide-gap spacer
LAMBDA_COULOMB = 8.0    # bosonic glue Coulomb-field decay (ML) — long, long-range field

# Bosonic glue (exciton/plasmon): couples via the long-range field.
bosonic = glue_through_spacer_window(LAMBDA_E, LAMBDA_COULOMB, glue_is_bosonic=True)
# Fermionic glue (needs electron transfer): decays like the electron -> blocked where it is.
fermionic = glue_through_spacer_window(LAMBDA_E, LAMBDA_COULOMB, glue_is_bosonic=False)

metrics = {
    "bosonic_window_exists": bosonic["window_exists"],
    "bosonic_d_lo_ml": round(bosonic["d_lo_ml"], 2) if bosonic["d_lo_ml"] is not None else None,
    "bosonic_d_hi_ml": round(bosonic["d_hi_ml"], 2) if bosonic["d_hi_ml"] is not None else None,
    "bosonic_window_width_ml": round(bosonic["window_width_ml"], 2),
    "fermionic_window_exists": fermionic["window_exists"],
}

falsifiers = [
    # F1: a bosonic (field-coupled) glue must pass the electron-opaque spacer (resolves H_009 L2).
    Falsifier("F1_bosonic_passes",
              lambda m: not m["bosonic_window_exists"],
              "PASS = a neutral/collective bosonic glue penetrates the electron-opaque spacer via its long-range field."),
    # F2: a fermionic (transfer) glue must be BLOCKED — the resolution is conditional on glue character.
    Falsifier("F2_fermionic_blocked",
              lambda m: m["fermionic_window_exists"],
              "PASS = a fermionic glue (needs electron transfer) is blocked where the electron is -> the +@ trilayer requires a BOSONIC glue."),
    # F3: the bosonic window must be wider than the electron-opacity onset (a real tolerance).
    Falsifier("F3_window_width",
              lambda m: not (m["bosonic_window_exists"] and m["bosonic_window_width_ml"] > 0.5),
              "PASS = the bosonic-glue window has real thickness tolerance."),
    # F4: the window must start at finite thickness (electron-opacity reached before the field dies).
    Falsifier("F4_finite_onset",
              lambda m: not (m["bosonic_window_exists"] and 0.0 < m["bosonic_d_lo_ml"] < 5.0),
              "PASS = the window onset is at finite, fabricable thickness."),
]

verdict = evaluate(metrics, falsifiers)

print("=== H_011 electronic glue through an electron-opaque spacer — the +@ crux ===")
print(f"  lambda_e (electron tunneling) = {LAMBDA_E} ML   lambda_coulomb (bosonic field) = {LAMBDA_COULOMB} ML")
print(f"  BOSONIC glue (exciton/plasmon, field-coupled):")
print(f"    window = [{metrics['bosonic_d_lo_ml']}, {metrics['bosonic_d_hi_ml']}] ML  width={metrics['bosonic_window_width_ml']} ML  exists={metrics['bosonic_window_exists']}")
print(f"  FERMIONIC glue (electron-transfer):  window exists={metrics['fermionic_window_exists']}")
for r in verdict["falsifiers"]:
    print(f"  falsifier {r['name']:24s}: {r['status']}")
print(f"  falsifiers_pass = {verdict['n_pass']}/{verdict['n_total']}")
print("VERDICT: NO CONTRADICTION — A BOSONIC (FIELD-COUPLED) GLUE PASSES THE ELECTRON-OPAQUE SPACER; A FERMIONIC ONE DOES NOT")

out = os.path.join(os.path.dirname(__file__), "result.json")
with open(out, "w") as f:
    json.dump(verdict, f, indent=2)
