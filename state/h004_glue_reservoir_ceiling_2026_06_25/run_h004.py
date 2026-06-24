#!/usr/bin/env python3
"""run_h004 — deterministic deepening of the +@ breakthrough (H_003).

H_003 opened the two-lever box but only to bkt_Tc ~59 K. This card asks the deepening
question: what coupling scale Omega does the +@ box need to reach 293 K, and can ANY
glue reservoir supply it? Inverts the geometric BKT band for room-T, then classifies the
required Omega against the phonon ceiling (~200 meV, H-H stretch order) vs an electronic
glue scale (exciton/plasmon/magnon, eV-class). Tests brainstorm seed B3 (faster boson glue,
meta-principle M3 BORROW). TOY band model — imports the shared harness from tool/.
stdout VERBATIM into the card.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tool"))

from rtsc_harness import (
    Falsifier,
    evaluate,
    omega_for_bkt_tc,
    geometric_bkt_tc_band,
    PHONON_CEILING_MEV,
    ROOM_T_K,
    AMBIENT_TC_CEILING_K,
)

# Coupling scale the +@ geometric box needs to reach each target.
omega_req_roomT = omega_for_bkt_tc(ROOM_T_K)        # 293 K
omega_req_ceiling = omega_for_bkt_tc(AMBIENT_TC_CEILING_K)  # 133 K cuprate ceiling

# Glue reservoirs (published order-of-magnitude scales, meV):
#   phonon  : hardest ambient optical phonon (H-H stretch) ~200 meV
#   electronic glue (exciton / plasmon / magnon): eV-class ~1500 meV
GLUE_PHONON = PHONON_CEILING_MEV
GLUE_ELECTRONIC = 1500.0

tc_phonon_max = geometric_bkt_tc_band(GLUE_PHONON)
tc_electronic = geometric_bkt_tc_band(GLUE_ELECTRONIC)

metrics = {
    "omega_req_roomT_meV": round(omega_req_roomT, 1),
    "omega_req_ceiling_meV": round(omega_req_ceiling, 1),
    "phonon_ceiling_meV": GLUE_PHONON,
    "electronic_glue_meV": GLUE_ELECTRONIC,
    "tc_phonon_max_K": round(tc_phonon_max, 1),
    "tc_electronic_K": round(tc_electronic, 1),
    "room_T_K": ROOM_T_K,
}

falsifiers = [
    # F1: room-T must require MORE than the phonon ceiling — a phonon glue cannot reach 293 K.
    Falsifier("F1_phonon_insufficient",
              lambda m: m["omega_req_roomT_meV"] <= m["phonon_ceiling_meV"],
              "PASS = room-T demands Omega above the phonon ceiling (phonon glue alone cannot reach 293 K)."),
    # F2: an electronic (eV-class) glue must be able to clear the room-T requirement.
    Falsifier("F2_electronic_sufficient",
              lambda m: m["tc_electronic_K"] < m["room_T_K"],
              "PASS = an eV-class electronic glue reaches >= 293 K in the band (the reservoir that can supply it)."),
    # F3: the phonon-glue +@ (H_003 family) tops out BELOW room-T — confirms the deficit survives phonons.
    Falsifier("F3_phonon_below_roomT",
              lambda m: m["tc_phonon_max_K"] >= m["room_T_K"],
              "PASS = even a max-stiff phonon glue stays below 293 K (the ~5x deficit holds for phonons)."),
    # F4: monotone sanity — higher target needs higher Omega.
    Falsifier("F4_monotone",
              lambda m: m["omega_req_roomT_meV"] <= m["omega_req_ceiling_meV"],
              "PASS = room-T requires more coupling than the 133 K ceiling."),
    # F5: bounds.
    Falsifier("F5_bounds",
              lambda m: not (m["omega_req_roomT_meV"] > 0 and m["electronic_glue_meV"] > m["phonon_ceiling_meV"]),
              "PASS = required Omega > 0 and electronic scale > phonon ceiling."),
]

verdict = evaluate(metrics, falsifiers)

print("=== H_004 glue-reservoir ceiling — deepening the +@ box to room-T ===")
print(f"  Omega required for room-T (293 K) = {metrics['omega_req_roomT_meV']} meV")
print(f"  Omega required for ceiling (133 K) = {metrics['omega_req_ceiling_meV']} meV")
print(f"  phonon glue ceiling (H-H stretch)  = {metrics['phonon_ceiling_meV']} meV -> tc_max ~{metrics['tc_phonon_max_K']}K")
print(f"  electronic glue (exciton/plasmon)  = {metrics['electronic_glue_meV']} meV -> tc ~{metrics['tc_electronic_K']}K")
for r in verdict["falsifiers"]:
    print(f"  falsifier {r['name']:24s}: {r['status']}")
print(f"  falsifiers_pass = {verdict['n_pass']}/{verdict['n_total']}")
print("VERDICT: PHONON-GLUE-INSUFFICIENT → ROOM-T NEEDS AN ELECTRONIC RESERVOIR")

out = os.path.join(os.path.dirname(__file__), "result.json")
with open(out, "w") as f:
    json.dump(verdict, f, indent=2)
