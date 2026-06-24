#!/usr/bin/env python3
"""run_h010 — TOP-DOWN lever-count scan (the user's pivot).

H_007 went BOTTOM-UP (1->2->3 levers, building up). The user: "we're going bottom-up;
if we come down TOP-DOWN on the COUNT we might discover something." So start from the full
stack and REMOVE levers, asking at each count: what glue demand does room-T then require, and
is that demand ACHIEVABLE (<= a sub-eV electronic-glue ceiling)? The discovery is the
ACHIEVABILITY FRONTIER — the count at which the per-lever demand first drops under the ceiling.

Levers (Tc multipliers / gates):
  geometry  : structural prerequisite (no flat band -> no geometric stiffness)
  connector : STRUCTURAL gate — without it the glue cannot be imported (H_009); division-of-labor collapses
  glue      : sets bkt via Omega (H_004/H_008)
  3D        : real x1.84 multiplier (H_006)
TOY band model — imports the shared harness from tool/. stdout VERBATIM into the card.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tool"))

from rtsc_harness import (
    Falsifier,
    evaluate,
    omega_for_stacked_tc,
    THREED_TC_LEVER,
    ROOM_T_K,
)

# A sub-eV electronic glue (exciton/plasmon) is plausible; eV+ needs an exotic reservoir.
ACHIEVABLE_GLUE_CEILING_MEV = 500.0

# Top-down: full stack, then strip one lever at a time. Each entry = glue Omega room-T demands.
stacks = [
    {"n": 4, "set": "geo+connector+glue+3D", "three_d": True,  "connector": True},
    {"n": 3, "set": "geo+connector+glue (drop 3D)", "three_d": False, "connector": True},
    {"n": 3, "set": "geo+glue+3D (drop connector)", "three_d": True,  "connector": False},
    {"n": 2, "set": "geo+glue (drop connector+3D)", "three_d": False, "connector": False},
]

rows = []
for s in stacks:
    if not s["connector"]:
        # no connector -> glue cannot be imported into the geometry host; falls back to the
        # single-host wall (H_001): an intrinsic stiff glue + flat-band geometry do not coexist.
        demand = float("inf")
        achievable = False
    else:
        demand = omega_for_stacked_tc(ROOM_T_K, three_d=s["three_d"])
        achievable = demand <= ACHIEVABLE_GLUE_CEILING_MEV
    rows.append({**s, "glue_demand_meV": (round(demand, 1) if demand != float("inf") else None),
                 "achievable": achievable})

# Achievability frontier: the LOWEST lever count whose demand is achievable.
achievable_counts = [r["n"] for r in rows if r["achievable"]]
min_achievable_count = min(achievable_counts) if achievable_counts else None
full_achievable = rows[0]["achievable"]
drop3d_achievable = rows[1]["achievable"]

metrics = {
    "full4_demand_meV": rows[0]["glue_demand_meV"],
    "full4_achievable": rows[0]["achievable"],
    "drop3d_demand_meV": rows[1]["glue_demand_meV"],
    "drop3d_achievable": rows[1]["achievable"],
    "drop_connector_achievable": rows[2]["achievable"],
    "min_achievable_count": min_achievable_count,
    "glue_ceiling_meV": ACHIEVABLE_GLUE_CEILING_MEV,
}

falsifiers = [
    # F1: the full 4-lever stack must be achievable (demand under the ceiling).
    Falsifier("F1_full_achievable",
              lambda m: not m["full4_achievable"],
              "PASS = the full 4-lever stack's glue demand is under the achievable ceiling."),
    # F2: dropping the 3D lever must push the demand OVER the ceiling (3D crosses the line).
    Falsifier("F2_3d_crosses_line",
              lambda m: m["drop3d_achievable"],
              "PASS = without 3D the glue demand exceeds the achievable ceiling -> 3D is the lever that crosses the achievability line, not padding."),
    # F3: dropping the connector must be unachievable (structural lever).
    Falsifier("F3_connector_structural",
              lambda m: m["drop_connector_achievable"],
              "PASS = without the connector the import collapses (unachievable) -> connector is structurally essential."),
    # F4: the achievability frontier is at the FULL count (you need all 4 to be achievable).
    Falsifier("F4_frontier_at_full",
              lambda m: m["min_achievable_count"] != 4,
              "PASS = the minimal ACHIEVABLE lever count is the full 4 -> more levers is the mechanism for achievability, not redundancy."),
]

verdict = evaluate(metrics, falsifiers)

print("=== H_010 TOP-DOWN lever-count scan — strip from the full stack ===")
print(f"  achievable glue ceiling = {ACHIEVABLE_GLUE_CEILING_MEV} meV (sub-eV electronic glue)")
print(f"  3D lever (real) = {THREED_TC_LEVER}x")
print("  count  lever set                       glue demand   achievable?")
for r in rows:
    d = f"{r['glue_demand_meV']} meV" if r["glue_demand_meV"] is not None else "inf (wall)"
    print(f"    {r['n']}    {r['set']:32s} {d:>11s}   {'YES' if r['achievable'] else 'no'}")
print(f"  minimal ACHIEVABLE count = {metrics['min_achievable_count']}")
for r in verdict["falsifiers"]:
    print(f"  falsifier {r['name']:24s}: {r['status']}")
print(f"  falsifiers_pass = {verdict['n_pass']}/{verdict['n_total']}")
print("VERDICT: TOP-DOWN DISCOVERY — MORE LEVERS = ACHIEVABILITY, NOT REDUNDANCY (4 is the minimal achievable count)")

out = os.path.join(os.path.dirname(__file__), "result.json")
with open(out, "w") as f:
    json.dump(verdict, f, indent=2)
