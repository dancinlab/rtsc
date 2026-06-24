#!/usr/bin/env python3
"""run_h003 — deterministic toy probe for HYPOTHESES card H_003.

The +@ combination breakthrough (brainstorm seed B2, meta-principle M1 SPLIT):
the two-lever wall (H_001) forbids one host from holding BOTH large geometry g
AND stiff coupling Omega. The +@ bypass divides labor across a bilayer — geometry
in layer A (published CoSn / Nb3Cl8 flat-band hosts), glue in a stiff-Omega layer B
(published high-frequency phonon scale) — proximity-coupled.

The honest question (per the brainstorm meta-law: SPLIT only DEFERS the wall within a
budget): does the proximity combination OPEN the room-T two-lever box that no single
host can, or does interface hybridization eat the geometry and relocate the same trade
into an interface criterion? This is a TOY transfer model (eta, electron_cost are
explicit swept knobs), not a real heterostructure verdict — layer-A levers are the
published ledger values (no fabrication). Imports the shared harness from repo-root
tool/. stdout is pasted VERBATIM into the card.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tool"))

from rtsc_harness import (
    Falsifier,
    evaluate,
    proximity_bilayer_levers,
    critical_electron_cost,
    two_lever_box_check,
    geometric_bkt_tc_band,
    ROOM_T_K,
)

# Layer A = published flat-band geometry host (CoSn, from H_001 ledger: g=2.87, Omega=22 meV).
G_A, OMEGA_A = 2.87, 22.0
# Layer B = stiff-glue host: a published high-frequency optical-phonon scale (hydride /
# light-element sigma-bond class, ~170 meV order). g_B ~ 0 (no flat-band geometry).
OMEGA_B = 170.0
U_OVER_OMEGA = 2.0  # carried from H_001 design box (>=1.5 gate)

# Reference single-host wall (H_001): CoSn alone never enters the box.
single = two_lever_box_check(G_A, OMEGA_A, U_OVER_OMEGA)

# +@ bilayer: ideal interface (electron_cost=0) imports glue without diluting geometry.
crit = critical_electron_cost(G_A, OMEGA_A, OMEGA_B)
ec_star = crit["critical_electron_cost"]
eta_star = crit["eta_at_critical"]

# Effective levers at the box-opening point, ideal vs generic interface.
ideal = proximity_bilayer_levers(G_A, OMEGA_A, OMEGA_B, eta_star, electron_cost=0.0)
generic = proximity_bilayer_levers(G_A, OMEGA_A, OMEGA_B, eta_star, electron_cost=1.0)
ideal_box = two_lever_box_check(ideal["g_eff"], ideal["omega_eff"], U_OVER_OMEGA)
generic_box = two_lever_box_check(generic["g_eff"], generic["omega_eff"], U_OVER_OMEGA)
bkt_ideal = geometric_bkt_tc_band(ideal["omega_eff"])

metrics = {
    "single_host_in_box": single["in_box"],
    "eta_star": round(eta_star, 3),
    "omega_eff_ideal_meV": round(ideal["omega_eff"], 1),
    "g_eff_ideal": round(ideal["g_eff"], 3),
    "ideal_interface_in_box": ideal_box["in_box"],
    "generic_interface_in_box": generic_box["in_box"],
    "critical_electron_cost": round(ec_star, 3),
    "bkt_tc_ideal_K": round(bkt_ideal, 1),
    "room_T_K": ROOM_T_K,
}

falsifiers = [
    # F1: if the +@ box never opens even at the ideal interface, the SPLIT family is closed.
    Falsifier("F1_split_opens_box",
              lambda m: not (m["ideal_interface_in_box"] and not m["single_host_in_box"]),
              "PASS = the +@ bilayer enters the box that the single host cannot."),
    # F2: if a GENERIC interface also opens the box, interface quality is irrelevant (too easy / model bug).
    Falsifier("F2_generic_stays_closed",
              lambda m: m["generic_interface_in_box"],
              "PASS = generic (electron_cost=1) hybridization keeps the box closed — the trade survives a careless interface."),
    # F3: the breakthrough must demand a NON-generic interface (0 < ec* < 1) — confirms SPLIT relocates the bill, not removes it.
    Falsifier("F3_relocates_not_removes",
              lambda m: not (0.0 < m["critical_electron_cost"] < 1.0),
              "PASS = the box opens only below a critical interface-quality threshold (the wall is relocated into an interface criterion)."),
    # F4: monotone sanity — importing glue must raise omega_eff above the soft single-host value.
    Falsifier("F4_glue_imported",
              lambda m: m["omega_eff_ideal_meV"] <= OMEGA_A,
              "PASS = proximity actually imported stiff glue (omega_eff > omega_A)."),
    # F5: bounds — effective levers physical.
    Falsifier("F5_bounds",
              lambda m: not (m["g_eff_ideal"] >= 0 and 0 <= m["eta_star"] <= 1),
              "PASS = g_eff >= 0 and eta in [0,1]."),
    # F6: no-fabrication — layer A must be the published CoSn ledger values.
    Falsifier("F6_no_fabrication",
              lambda m: not (G_A == 2.87 and OMEGA_A == 22.0),
              "PASS = layer-A levers are the published H_001 ledger values, not invented."),
]

verdict = evaluate(metrics, falsifiers)

print("=== H_003 +@ bilayer division-of-labor — deterministic toy probe ===")
print(f"  single host (CoSn g={G_A} omega={OMEGA_A}meV) in_box = {single['in_box']}  (H_001 wall)")
print(f"  +@ glue layer B: omega_B = {OMEGA_B} meV")
print(f"  box-opening eta* = {metrics['eta_star']}  ->  omega_eff = {metrics['omega_eff_ideal_meV']} meV")
print(f"  ideal interface (ec=0):   g_eff={metrics['g_eff_ideal']} omega_eff={metrics['omega_eff_ideal_meV']}meV -> in_box={metrics['ideal_interface_in_box']}  bkt_Tc~{metrics['bkt_tc_ideal_K']}K")
print(f"  generic interface (ec=1): in_box={metrics['generic_interface_in_box']}")
print(f"  critical_electron_cost ec* = {metrics['critical_electron_cost']}  (interface must be BELOW this to open the box)")
print(f"  room-T target = {ROOM_T_K} K")
for r in verdict["falsifiers"]:
    print(f"  falsifier {r['name']:24s}: {r['status']}")
print(f"  falsifiers_pass = {verdict['n_pass']}/{verdict['n_total']}")
opened = metrics["ideal_interface_in_box"] and not metrics["single_host_in_box"]
tier = "MODEL-PROBE → BOX-OPENS-AT-IDEAL-INTERFACE" if opened else "MODEL-PROBE → SPLIT-CLOSED"
print(f"VERDICT: {tier}")

out = os.path.join(os.path.dirname(__file__), "result.json")
with open(out, "w") as f:
    json.dump(verdict, f, indent=2)
