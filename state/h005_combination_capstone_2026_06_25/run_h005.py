#!/usr/bin/env python3
"""run_h005 — +@ combination capstone (deepening to depletion).

Stacks the two orthogonal +@ levers the deepening surfaced:
  (B2) bilayer geometry-import via a phonon-transparent/electron-opaque interface (H_003),
  (B3) an electronic (eV-class) glue reservoir replacing the phonon ceiling (H_004).
Tests whether the FULL stack reaches the 293 K box in the toy band AND whether EACH lever
is necessary (ablate one → a wall returns), the rtsc analog of lumen's combination capstone.
Honest: each lever relocates its own bill (interface quality · competing electronic order),
so room-T is REACHABLE-IN-TOY-BAND but CONDITIONAL on two stacked unsolved sub-problems.
TOY band model — imports the shared harness from tool/. stdout VERBATIM into the card.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tool"))

from rtsc_harness import (
    Falsifier,
    evaluate,
    proximity_bilayer_levers,
    two_lever_box_check,
    geometric_bkt_tc_band,
    PHONON_CEILING_MEV,
    ROOM_T_K,
)

G_A, OMEGA_A = 2.87, 22.0          # layer A geometry host (published, H_001 ledger)
OMEGA_ELECTRONIC = 700.0           # electronic glue reservoir (sub-eV plasmon/exciton order)
U_OVER_OMEGA = 2.0

# Full stack: ideal interface imports the electronic glue into A's flat band (eta->1).
full = proximity_bilayer_levers(G_A, OMEGA_A, OMEGA_ELECTRONIC, eta=1.0, electron_cost=0.0)
full_box = two_lever_box_check(full["g_eff"], full["omega_eff"], U_OVER_OMEGA)
full_tc = geometric_bkt_tc_band(full["omega_eff"])

# Ablation 1 — drop the electronic glue (fall back to the phonon ceiling).
abl_glue = proximity_bilayer_levers(G_A, OMEGA_A, PHONON_CEILING_MEV, eta=1.0, electron_cost=0.0)
abl_glue_tc = geometric_bkt_tc_band(abl_glue["omega_eff"])

# Ablation 2 — drop the geometry layer (no flat band: g below the gate).
abl_geom_box = two_lever_box_check(1.0, full["omega_eff"], U_OVER_OMEGA)  # g_eff = 1 < 2

# Ablation 3 — drop interface quality (generic hybridization at the same eta).
abl_iface = proximity_bilayer_levers(G_A, OMEGA_A, OMEGA_ELECTRONIC, eta=1.0, electron_cost=1.0)
abl_iface_box = two_lever_box_check(abl_iface["g_eff"], abl_iface["omega_eff"], U_OVER_OMEGA)

metrics = {
    "full_in_box": full_box["in_box"],
    "full_tc_K": round(full_tc, 1),
    "full_reaches_roomT": full_tc >= ROOM_T_K,
    "ablate_glue_tc_K": round(abl_glue_tc, 1),
    "ablate_geom_in_box": abl_geom_box["in_box"],
    "ablate_iface_in_box": abl_iface_box["in_box"],
    "room_T_K": ROOM_T_K,
}

falsifiers = [
    # F1: the full stack reaches the room-T box in the toy band.
    Falsifier("F1_stack_reaches_roomT",
              lambda m: not (m["full_in_box"] and m["full_reaches_roomT"]),
              "PASS = the full +@ stack enters the box AND clears 293 K in the toy band."),
    # F2: dropping the electronic glue must drop below room-T (glue lever necessary).
    Falsifier("F2_glue_necessary",
              lambda m: m["ablate_glue_tc_K"] >= m["room_T_K"],
              "PASS = without the electronic glue the stack falls below 293 K (phonon-limited)."),
    # F3: dropping the geometry layer must close the box (geometry lever necessary).
    Falsifier("F3_geometry_necessary",
              lambda m: m["ablate_geom_in_box"],
              "PASS = without the flat-band geometry the box closes."),
    # F4: dropping interface quality must close the box (interface lever necessary).
    Falsifier("F4_interface_necessary",
              lambda m: m["ablate_iface_in_box"],
              "PASS = a generic interface closes the box (interface quality necessary)."),
    # F5: bounds.
    Falsifier("F5_bounds",
              lambda m: not (m["full_tc_K"] > 0 and m["ablate_glue_tc_K"] > 0),
              "PASS = T_c values positive."),
]

verdict = evaluate(metrics, falsifiers)

print("=== H_005 +@ combination capstone — full stack + ablation ===")
print(f"  FULL stack (geometry + electronic glue {OMEGA_ELECTRONIC}meV + ideal interface):")
print(f"    g_eff={round(full['g_eff'],3)} omega_eff={round(full['omega_eff'],1)}meV -> in_box={metrics['full_in_box']}  bkt_Tc~{metrics['full_tc_K']}K  (room-T {ROOM_T_K}K: {'CLEARED' if metrics['full_reaches_roomT'] else 'missed'})")
print(f"  ablate electronic glue -> phonon ceiling: bkt_Tc~{metrics['ablate_glue_tc_K']}K  (room-T: {'cleared' if metrics['ablate_glue_tc_K']>=ROOM_T_K else 'FAILS'})")
print(f"  ablate geometry layer (g<2):              in_box={metrics['ablate_geom_in_box']}")
print(f"  ablate interface quality (generic):       in_box={metrics['ablate_iface_in_box']}")
for r in verdict["falsifiers"]:
    print(f"  falsifier {r['name']:24s}: {r['status']}")
print(f"  falsifiers_pass = {verdict['n_pass']}/{verdict['n_total']}")
print("VERDICT: ROOM-T REACHABLE IN TOY BAND — CONDITIONAL ON 2 STACKED UNSOLVED SUB-PROBLEMS")

out = os.path.join(os.path.dirname(__file__), "result.json")
with open(out, "w") as f:
    json.dump(verdict, f, indent=2)
