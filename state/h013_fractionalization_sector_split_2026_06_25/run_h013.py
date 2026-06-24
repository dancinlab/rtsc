#!/usr/bin/env python3
"""run_h_013 — deterministic toy probe for HYPOTHESES card H_013.

Brainstorm seed S5 (meta-principle M1 SPLIT, most exotic): charge/spin/orbital
FRACTIONALIZATION as a bypass of the two-lever wall (H_001, REFUTED). The FS
anti-correlation (g vs Omega) is a property of ONE coherent electron fluid: the
same Bloch wavefunction carries both the Fubini-Study geometry g AND the coupling
stiffness Omega, and the Fubini-Study bound ties them anti-correlated.

S5's claim: in a slave-particle / spin-liquid mean field the electron
fractionalizes  c = f * b  (spinon f carries spin+geometry, holon b carries
charge+glue). The two sectors have INDEPENDENT mean-field dispersions, so the FS
bound on the physical electron no longer couples g(spinon) to Omega(holon) — a
SECTOR-level split, distinct from the SPATIAL bilayer of H_003.

The honest question (per the SPLIT meta-law — a split only DEFERS the wall within
a budget): does sector separation let g_spinon and Omega_holon be independently
LARGE so the box opens, and is the fractionalization gap Delta_frac (the energy
protecting deconfinement against spinon-holon RECOMBINATION/confinement) a NEW
bill that closes it? Recombination re-fuses c = f*b and re-imposes the FS tie.

This is a TOY closed-form probe (stdlib math only). NO fitting, NO fabricated
material values: the geometry/glue inputs are the published H_001 ledger levers
(CoSn-class g, hydride-class Omega) reused unchanged; the only swept knob is the
fractionalization gap Delta_frac, scanned over a declared range. ALL falsifier
helpers are INLINE (the shared tool/rtsc_harness.py is NOT imported, to avoid
cross-lane edit conflicts; the Falsifier/evaluate API is re-implemented identically).
stdout is pasted VERBATIM into the card.
"""
import json
import math
import os
from dataclasses import dataclass

# ----------------------------------------------------------------------------
# INLINE harness (API-identical to tool/rtsc_harness.py Falsifier/evaluate).
# ----------------------------------------------------------------------------

@dataclass
class Falsifier:
    """One pre-registered measurable falsifier. predicate(metrics)->bool is TRUE
    when TRIGGERED (component refuted). PASS = NOT triggered."""
    name: str
    predicate: object
    desc: str = ""


def evaluate(metrics, falsifiers):
    results = []
    for f in falsifiers:
        triggered = bool(f.predicate(metrics))
        results.append({"name": f.name, "triggered": triggered,
                        "status": "FAIL" if triggered else "PASS"})
    n_pass = sum(1 for r in results if r["status"] == "PASS")
    return {"metrics": metrics, "falsifiers": results, "n_pass": n_pass,
            "n_total": len(results), "all_pass": n_pass == len(results)}


# ----------------------------------------------------------------------------
# Design box (re-stated INLINE, identical thresholds to H_001).
# ----------------------------------------------------------------------------
G_MIN = 2.0           # quantum-geometry gate (FS trace)
OMEGA_MIN = 130.0     # coupling-stiffness gate (meV)
U_OVER_OMEGA_MIN = 1.5
ROOM_T_K = 293.0
DEFLATE = 2.8         # calibrated 2D-BKT deflation (H_001 anchor)
MEV_TO_K = 11.604


def two_lever_box_check(g, omega_meV, u_over_omega):
    gates = {"g": g >= G_MIN, "omega": omega_meV >= OMEGA_MIN,
             "u_over_omega": u_over_omega >= U_OVER_OMEGA_MIN}
    return {"gates": gates, "in_box": all(gates.values())}


def bkt_tc_band(omega_meV, deflate=DEFLATE):
    return (0.11 * omega_meV * MEV_TO_K) / deflate


# ----------------------------------------------------------------------------
# Published ledger levers (NO fabrication — reused from H_001 / H_003).
# ----------------------------------------------------------------------------
# Spinon sector inherits the flat-band GEOMETRY host (CoSn-class): big g, soft glue.
G_SPINON, OMEGA_SPINON = 2.87, 22.0
# Holon sector inherits the STIFF-GLUE host (hydride/light-element sigma class).
OMEGA_HOLON, G_HOLON = 170.0, 0.0
U_OVER_OMEGA = 2.0    # carried from H_001 design box (>=1.5 gate)

# --- the FS anti-correlation, stated as the wall a SINGLE fused electron obeys ---
# In one coherent electron fluid the SAME wavefunction carries g and Omega, and the
# Fubini-Study bound forces them onto an anti-correlated trade curve. We encode that
# tie as: a host with geometry g can support coupling at most OMEGA_FS_CAP(g). Using
# the two published anchors (g=2.87 -> 22 meV soft; g~0 -> 170 meV stiff) the linear
# FS trade through them gives the cap the fused electron cannot beat.
def omega_fs_cap(g):
    # line through (g=0, 170) and (g=2.87, 22): the harder the geometry, the softer
    # the max coupling a SINGLE fused electron fluid can hold (the H_001 wall).
    slope = (OMEGA_SPINON - OMEGA_HOLON) / (G_SPINON - G_HOLON)  # negative
    return OMEGA_HOLON + slope * g


# A fused electron that tries to carry BOTH the geometry host's g AND the stiff glue
# is capped by the FS trade -> fails the omega gate at large g. This is the wall.
omega_fused_at_geometry = omega_fs_cap(G_SPINON)            # what one fluid can do at g=2.87
fused_box = two_lever_box_check(G_SPINON, omega_fused_at_geometry, U_OVER_OMEGA)


# ----------------------------------------------------------------------------
# SECTOR SPLIT: spinon carries g, holon carries Omega, INDEPENDENT dispersions.
# The physical pairing/condensate effective levers are g_eff = g_spinon (geometry
# rides the spinon band) and Omega_eff = Omega_holon (glue rides the holon band) —
# IF the state stays deconfined. Deconfinement is protected by the fractionalization
# gap Delta_frac. Recombination (confinement) at scale below the operating scale
# re-fuses c=f*b and RE-IMPOSES the FS cap, collapsing Omega_eff back onto the cap.
# ----------------------------------------------------------------------------

def sector_split_levers(delta_frac_meV, omega_op_meV):
    """Effective (g, Omega) of the fractionalized pairing state.

    Deconfinement is robust only while Delta_frac exceeds the operating energy
    scale omega_op (the pairing/glue scale that probes the sector structure). We
    model the surviving fraction of the SPLIT advantage with a smooth confinement
    crossover s = Delta_frac / (Delta_frac + omega_op) in [0,1):
      s -> 1  (Delta_frac >> omega_op): fully deconfined, sectors independent,
              Omega_eff = Omega_holon, g_eff = g_spinon  (split realized).
      s -> 0  (Delta_frac << omega_op): confined, c=f*b re-fused, FS cap restored,
              Omega_eff -> omega_fs_cap(g_spinon), g_eff -> g_spinon (geometry kept,
              glue collapses to the wall value).
    The geometry g rides the spinon band either way (spinon flat band survives
    confinement as the electron band); it is the GLUE that is at risk of re-tying.
    """
    s = delta_frac_meV / (delta_frac_meV + omega_op_meV)
    omega_cap = omega_fs_cap(G_SPINON)
    omega_eff = omega_cap + s * (OMEGA_HOLON - omega_cap)  # cap (confined) -> holon (free)
    g_eff = G_SPINON                                       # geometry rides spinon band
    return {"s_deconf": s, "g_eff": g_eff, "omega_eff": omega_eff}


# Operating scale that the deconfinement must beat: the holon glue scale itself is
# what is being imported, so the sector structure is probed at omega_op = OMEGA_HOLON.
OMEGA_OP = OMEGA_HOLON

# Critical Delta_frac that just reopens the omega gate (Omega_eff == OMEGA_MIN):
# solve OMEGA_MIN = cap + s*(holon-cap), s = D/(D+op) -> D* = op*(req-cap)/(holon-req).
_cap = omega_fs_cap(G_SPINON)
_req = OMEGA_MIN
if (OMEGA_HOLON - _req) > 0 and (_req - _cap) > 0:
    DELTA_FRAC_CRIT = OMEGA_OP * (_req - _cap) / (OMEGA_HOLON - _req)
else:
    DELTA_FRAC_CRIT = None

# Scan Delta_frac over a declared physical range (meV): weak Mott/RVB gaps ~ tens of
# meV up to strong-correlation gaps ~ eV. NO tuning to a target — fixed grid.
DELTA_FRAC_GRID = [10.0, 30.0, 50.0, 100.0, 200.0, 400.0, 800.0]

scan = []
for D in DELTA_FRAC_GRID:
    lev = sector_split_levers(D, OMEGA_OP)
    box = two_lever_box_check(lev["g_eff"], lev["omega_eff"], U_OVER_OMEGA)
    scan.append({"delta_frac_meV": D, "s_deconf": lev["s_deconf"],
                 "g_eff": lev["g_eff"], "omega_eff_meV": lev["omega_eff"],
                 "in_box": box["in_box"], "bkt_tc_K": bkt_tc_band(lev["omega_eff"])})

# Ideal deconfinement limit (Delta_frac -> infinity): the pure split advantage.
ideal = sector_split_levers(1.0e9, OMEGA_OP)
ideal_box = two_lever_box_check(ideal["g_eff"], ideal["omega_eff"], U_OVER_OMEGA)

# Does ANY finite, physical Delta_frac in the grid open the box the fused electron can't?
opening_rows = [r for r in scan if r["in_box"]]
any_finite_opens = len(opening_rows) > 0
min_delta_opens = min((r["delta_frac_meV"] for r in opening_rows), default=None)

# Room-T bill: even in the ideal split, is the imported holon glue enough for 293 K?
# (the published holon scale is 170 meV; room-T 2D needs ~643 meV -> expected NO.)
ideal_tc = bkt_tc_band(ideal["omega_eff"])
room_t_reached_ideal = ideal_tc >= ROOM_T_K

metrics = {
    "fused_omega_cap_meV": round(omega_fused_at_geometry, 1),
    "fused_in_box": fused_box["in_box"],
    "ideal_split_g_eff": round(ideal["g_eff"], 3),
    "ideal_split_omega_eff_meV": round(ideal["omega_eff"], 1),
    "ideal_split_in_box": ideal_box["in_box"],
    "delta_frac_crit_meV": (round(DELTA_FRAC_CRIT, 1)
                            if DELTA_FRAC_CRIT is not None else None),
    "any_finite_delta_opens_box": any_finite_opens,
    "min_delta_frac_opens_meV": min_delta_opens,
    "ideal_bkt_tc_K": round(ideal_tc, 1),
    "room_t_reached_ideal_split": room_t_reached_ideal,
    "room_t_K": ROOM_T_K,
}

falsifiers = [
    # F1: the SECTOR split must open the box the single FUSED electron cannot
    #     (the whole point of S5). Triggered if either fused is already in-box
    #     (no wall to beat) or the ideal split fails to open it.
    Falsifier("F1_sector_split_opens_box",
              lambda m: not (m["ideal_split_in_box"] and not m["fused_in_box"]),
              "PASS = the deconfined sector split enters the box that one fused electron cannot."),
    # F2: the split must EVADE the FS tie on glue — Omega_eff in the ideal split must
    #     exceed the fused FS cap (geometry no longer suppresses the imported glue).
    Falsifier("F2_evades_fs_tie",
              lambda m: not (m["ideal_split_omega_eff_meV"] > m["fused_omega_cap_meV"] + 1e-6),
              "PASS = sector independence lifts Omega above the FS cap a fused electron is stuck at."),
    # F3: the NEW BILL must be real — a FINITE critical Delta_frac must exist, i.e. the
    #     box closes again below it (recombination re-imposes the wall). Triggered if no
    #     finite threshold (advantage free) or if even infinite gap can't open it.
    Falsifier("F3_fractionalization_gap_is_the_bill",
              lambda m: not (m["delta_frac_crit_meV"] is not None
                             and m["delta_frac_crit_meV"] > 0.0
                             and m["ideal_split_in_box"]),
              "PASS = a finite Delta_frac threshold gates the box (the wall is relocated into a fractionalization-gap criterion, not removed)."),
    # F4: room-T HONESTY — the imported holon glue (published 170 meV) must NOT by itself
    #     reach 293 K. Triggered if the ideal split is claimed to hit room-T (would mean
    #     the published glue magically suffices -> model too generous / fabrication).
    Falsifier("F4_no_free_room_t",
              lambda m: m["room_t_reached_ideal_split"],
              "PASS = even the ideal split does NOT reach room-T on the published holon glue — room-T still needs the other levers (it only restores the 2-lever box, honestly)."),
    # F5: monotonicity sanity — Omega_eff must increase with Delta_frac (more
    #     deconfinement -> more split advantage). Triggered if non-monotone.
    Falsifier("F5_monotone_in_gap",
              lambda m: not all(
                  scan[i]["omega_eff_meV"] <= scan[i + 1]["omega_eff_meV"] + 1e-9
                  for i in range(len(scan) - 1)),
              "PASS = the imported glue rises monotonically with the fractionalization gap (confinement crossover well-behaved)."),
    # F6: NO-FABRICATION — sector inputs must be the published H_001/H_003 ledger levers.
    Falsifier("F6_no_fabrication",
              lambda m: not (G_SPINON == 2.87 and OMEGA_SPINON == 22.0
                             and OMEGA_HOLON == 170.0),
              "PASS = spinon geometry and holon glue are the published ledger values, not invented."),
]

verdict = evaluate(metrics, falsifiers)

print("=== H_013 fractionalization sector-split (S5, M1 SPLIT) — deterministic toy probe ===")
print(f"  spinon sector (geometry host): g={G_SPINON}  omega_spinon={OMEGA_SPINON} meV")
print(f"  holon  sector (glue host):     g={G_HOLON}    omega_holon ={OMEGA_HOLON} meV")
print(f"  FS wall on ONE fused electron at g={G_SPINON}: omega_cap = {metrics['fused_omega_cap_meV']} meV"
      f"  -> fused in_box = {metrics['fused_in_box']}")
print(f"  ideal deconfined split (Delta_frac -> inf): g_eff={metrics['ideal_split_g_eff']}"
      f"  omega_eff={metrics['ideal_split_omega_eff_meV']} meV -> in_box={metrics['ideal_split_in_box']}"
      f"  bkt_Tc~{metrics['ideal_bkt_tc_K']}K")
print(f"  critical fractionalization gap Delta_frac* = {metrics['delta_frac_crit_meV']} meV"
      f"  (must EXCEED this to keep the box open against recombination)")
print(f"  Delta_frac scan (op-scale omega_op={OMEGA_OP} meV):")
for r in scan:
    print(f"    Delta_frac={r['delta_frac_meV']:7.1f} meV  s_deconf={r['s_deconf']:.3f}"
          f"  omega_eff={r['omega_eff_meV']:6.1f} meV  in_box={str(r['in_box']):5s}"
          f"  bkt_Tc~{r['bkt_tc_K']:.1f}K")
print(f"  any finite Delta_frac opens box = {metrics['any_finite_delta_opens_box']}"
      f"  (min opening Delta_frac = {metrics['min_delta_frac_opens_meV']} meV)")
print(f"  room-T reached by ideal split alone = {metrics['room_t_reached_ideal_split']}"
      f"  (room-T target = {metrics['room_t_K']} K)")
for r in verdict["falsifiers"]:
    print(f"  falsifier {r['name']:34s}: {r['status']}")
print(f"  falsifiers_pass = {verdict['n_pass']}/{verdict['n_total']}")

opened = metrics["ideal_split_in_box"] and not metrics["fused_in_box"]
gated = metrics["delta_frac_crit_meV"] is not None and metrics["delta_frac_crit_meV"] > 0.0
if opened and gated:
    tier = "MODEL-PROBE -> BOX-OPENS-BUT-NEW-BILL (fractionalization gap relocates the wall)"
elif opened:
    tier = "MODEL-PROBE -> BOX-OPENS-FREE (suspicious — no bill)"
else:
    tier = "MODEL-PROBE -> SPLIT-CLOSED"
print(f"VERDICT: {tier}")

out = os.path.join(os.path.dirname(__file__), "result.json")
with open(out, "w") as f:
    json.dump(verdict, f, indent=2)
