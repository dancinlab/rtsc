#!/usr/bin/env python3
"""run_h001 — deterministic verdict for HYPOTHESES card H_001 (flat-band two-lever wall).

Tests whether any real, published flat-band host enters the honest room-T design box
(g_mean >= 2.0 AND omega >= 130 meV AND U/Omega >= 1.5). Imports the shared harness
from repo-root tool/ (anima-parity). Output stdout is pasted VERBATIM into the card.

Host (g_mean, omega_meV) values are from the campaign records (CoSn g=2.87, Nb3Cl8
g=2.11; soft d-electron phonons omega ~ 15-30 meV). The verdict (box entry 0) is
robust to the exact omega within that documented band.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tool"))

from rtsc_harness import (
    AMBIENT_TC_CEILING_K,
    ROOM_T_K,
    Falsifier,
    evaluate,
    geometric_bkt_tc_band,
    two_lever_box_check,
)

# Real published flat-band hosts with enough quantum geometry (g_mean >= 2).
# omega is a representative value within the documented 15-30 meV soft-phonon band.
HOSTS = [
    {"name": "CoSn", "g_mean": 2.87, "omega_meV": 22.0, "u_over_omega": 2.0},
    {"name": "Nb3Cl8", "g_mean": 2.11, "omega_meV": 20.0, "u_over_omega": 2.0},
]

box_results = []
for h in HOSTS:
    box = two_lever_box_check(h["g_mean"], h["omega_meV"], h["u_over_omega"])
    tc = geometric_bkt_tc_band(h["omega_meV"])
    box_results.append({**h, **box, "bkt_tc_K": round(tc, 2)})

n_in_box = sum(1 for r in box_results if r["in_box"])

metrics = {
    "n_hosts": len(HOSTS),
    "n_in_box": n_in_box,
    "ambient_tc_ceiling_K": AMBIENT_TC_CEILING_K,
    "room_T_K": ROOM_T_K,
    "max_bkt_tc_K": max(r["bkt_tc_K"] for r in box_results),
}

falsifiers = [
    Falsifier("F1_box_entry", lambda m: m["n_in_box"] >= 1,
              "any real host enters the two-lever box -> SUPPORTED"),
    Falsifier("F2_ceiling_broken", lambda m: m["max_bkt_tc_K"] > m["ambient_tc_ceiling_K"],
              "a host clears the ambient cuprate ceiling via geometry"),
    Falsifier("F4_reaches_room_T", lambda m: m["max_bkt_tc_K"] >= m["room_T_K"],
              "estimated T_c reaches 293 K"),
]

verdict = evaluate(metrics, falsifiers)
supported = metrics["n_in_box"] >= 1
verdict_class = "SUPPORTED" if supported else "CLOSED-NEGATIVE"

out = {
    "card": "H_001",
    "verdict_class": verdict_class,
    "hosts": box_results,
    "metrics": metrics,
    "falsifier_ledger": verdict,
}

print("=== H_001 flat-band two-lever wall — deterministic verdict ===")
for r in box_results:
    g = r["gates"]
    print(f"  {r['name']:8s} g={r['g_mean']:.2f}[{'ok' if g['g'] else 'no'}] "
          f"omega={r['omega_meV']:.0f}meV[{'ok' if g['omega'] else 'no'}] "
          f"U/Om={r['u_over_omega']:.1f}[{'ok' if g['u_over_omega'] else 'no'}] "
          f"-> in_box={r['in_box']}  bkt_Tc~{r['bkt_tc_K']}K")
print(f"  hosts_in_box = {metrics['n_in_box']} / {metrics['n_hosts']}")
print(f"  max bkt_Tc = {metrics['max_bkt_tc_K']}K  vs ambient ceiling {AMBIENT_TC_CEILING_K}K  "
      f"vs room-T {ROOM_T_K}K")
for r in verdict["falsifiers"]:
    print(f"  falsifier {r['name']:20s}: {r['status']}")
print(f"  falsifiers_pass = {verdict['n_pass']}/{verdict['n_total']}")
print(f"VERDICT: {verdict_class}")

with open(os.path.join(os.path.dirname(__file__), "result.json"), "w") as fh:
    json.dump(out, fh, indent=2)
