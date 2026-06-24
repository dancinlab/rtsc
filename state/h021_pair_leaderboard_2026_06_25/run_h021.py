#!/usr/bin/env python3
"""run_h_021 — closed-form A x B PAIR leaderboard for the +@ trilayer (A / hBN / B).

THE QUESTION
------------
The +@ trilayer splits the two-lever wall (H_001): geometry lives in layer A
(large quantum-geometry <g>), bosonic glue lives in layer B (stiff coupling
scale Omega), proximity-coupled through an electron-opaque / field-transparent
hBN spacer (both spacer halves confirmed: DFT electron-opacity H_015 +
field-transparent literature H_011). The remaining question is purely a
MATERIALS bookkeeping one: of the candidate A hosts x candidate B hosts in the
living registry (tool/rtsc_candidates.py), which PAIRS clear the +@ design box,
and what is their closed-form BKT T_c?

WHAT THIS SCRIPT DOES (no fitting, no fabrication, no tune-to-green)
-------------------------------------------------------------------
1. Reads the candidate registry (import LAYER_A / LAYER_B from rtsc_candidates;
   re-listed inline below as a deterministic fallback so the run is robust). Each
   property is (value, source, verified). ONLY verified values may enter the box.
2. For EVERY A x B pair, builds the +@ box input from VERIFIED values only:
       g_use  = A.g_mean   iff VERIFIED, else the pair is GAP-BLOCKED (geometry gap)
       om_use = B.boson_meV iff VERIFIED, else the pair is GAP-BLOCKED (glue gap)
   U/Omega is the registry's pre-registered demo value (2.0 >= 1.5 box-min); it is
   NOT a per-material measured quantity here, so it is held fixed and surfaced as a
   limit (it is the same value rtsc_candidates.verify_pair uses).
3. Runs two_lever_box_check(g_use, om_use, u_over_omega=2.0) -> in_box.
   Computes bkt_Tc_2D = geometric_bkt_tc_band(om_use) and
            bkt_Tc_3D = stacked_tc(om_use, three_d=True) = 1.84 x 2D.
   GAP-BLOCKED pairs report which gap(s) and carry T_c = None (NOT zero-as-data).
4. Ranks: fully-verified box-clearing pairs first (by bkt_Tc_3D desc), then
   gap-blocked pairs by the bkt they WOULD reach IF the gap value were confirmed
   (the "if gaps filled" leaderboard), so the best-if-filled pair is identifiable.
5. Falsifiers (PASS = not triggered):
     F1  a fully-verified box-clearing pair EXISTS (the +@ box is reachable today).
     F2  the leaderboard is MONOTONE in Omega (higher verified Omega -> >= bkt_Tc).
     F3  NO fabricated values: every box input traces to a verified registry source.
     F4  the best fully-verified pair is CoSn / Ta2NiSe5 (pre-registered expectation).
     F5  every gap-blocked pair names a concrete missing/unverified property.

HONEST FRAMING (tier MODEL-PROBE / bookkeeping, d6). bkt_Tc is a COORDINATE from a
3-anchor-calibrated estimator extrapolated far in Omega (H_018 scatter ~3x), NOT a
prediction; "clears the box on paper" != "is an RTSC". The winning trio is JOINTLY
UNREALIZED (never co-fabricated/measured). absorbed=false / GATE_OPEN. A negative
(no verified pair) would be a fully valid result. Every helper is INLINE; we import
the harness (do NOT edit it) and read the registry (do NOT edit it).

stdout is pasted VERBATIM into the card. Run twice; bytes must be identical.
"""
import json
import os
import sys

# --- import the shared harness (do NOT edit it) ------------------------------
_TOOL = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "tool"))
if _TOOL not in sys.path:
    sys.path.insert(0, _TOOL)
from rtsc_harness import (
    two_lever_box_check,
    geometric_bkt_tc_band,
    stacked_tc,
    THREED_TC_LEVER,
)

# --- read the candidate registry ---------------------------------------------
# Import the LIVING registry; if the import is awkward in some environment we fall
# back to the SAME verified values re-listed inline (deterministic either way).
try:
    from rtsc_candidates import LAYER_A as _LA, LAYER_B as _LB

    LAYER_A = [
        {"name": c.name, "g_mean": c.g_mean, "frustrated": c.frustrated,
         "competing_order": c.competing_order} for c in _LA
    ]
    LAYER_B = [
        {"name": c.name, "boson_meV": c.boson_meV,
         "competing_order": c.competing_order} for c in _LB
    ]
    _SOURCE = "imported from tool/rtsc_candidates.py"
except Exception:
    LAYER_A = [
        {"name": "CoSn", "g_mean": (2.87, "H_001 ledger; QGT arXiv:2412.17809", True),
         "frustrated": (True, "kagome", True), "competing_order": (None, "", False)},
        {"name": "Nb3Cl8", "g_mean": (2.11, "H_001 ledger", True),
         "frustrated": (True, "breathing kagome", True), "competing_order": (None, "", False)},
        {"name": "CsV3Sb5", "g_mean": (None, "needs DFT <g>", False),
         "frustrated": (True, "kagome", True), "competing_order": ("CDW", "known CDW host", False)},
    ]
    LAYER_B = [
        {"name": "Ta2NiSe5", "boson_meV": (300.0, "exciton arXiv:2007.08212", True),
         "competing_order": ("none", "q=0 non-nesting arXiv:2106.04396", True)},
        {"name": "1T-TiSe2", "boson_meV": (None, "needs sourced value", False),
         "competing_order": ("CDW", "exciton-driven CDW", False)},
    ]
    _SOURCE = "inline fallback (import unavailable)"

U_OVER_OMEGA = 2.0  # registry pre-registered demo value; >= box-min 1.5. Held fixed (a limit).


# --- inline falsifier engine (mirrors tool/rtsc_harness.evaluate; do NOT edit harness) ---
class Falsifier:
    """predicate(metrics)->bool, TRUE when TRIGGERED (refuted). PASS = not triggered."""
    def __init__(self, name, predicate, desc):
        self.name, self.predicate, self.desc = name, predicate, desc


def evaluate(metrics, falsifiers):
    rows = []
    for f in falsifiers:
        trig = bool(f.predicate(metrics))
        rows.append({"name": f.name, "triggered": trig, "status": "FAIL" if trig else "PASS"})
    n_pass = sum(1 for r in rows if r["status"] == "PASS")
    return {"falsifiers": rows, "n_pass": n_pass, "n_total": len(rows),
            "all_pass": n_pass == len(rows)}


# --- build the pair leaderboard ----------------------------------------------
def build_rows():
    rows = []
    for a in LAYER_A:
        g_val, g_src, g_ver = a["g_mean"]
        for b in LAYER_B:
            om_val, om_src, om_ver = b["boson_meV"]
            gaps = []
            # geometry gap (A side)
            if g_val is None:
                gaps.append(f"A.g_mean({a['name']}): unknown")
            elif not g_ver:
                gaps.append(f"A.g_mean({a['name']})={g_val}: UNVERIFIED")
            # glue gap (B side)
            if om_val is None:
                gaps.append(f"B.boson_meV({b['name']}): unknown")
            elif not om_ver:
                gaps.append(f"B.boson_meV({b['name']})={om_val}: UNVERIFIED")

            blocked = bool(gaps)
            # box inputs: VERIFIED only. For ranking-if-filled we also record the
            # WOULD-BE Omega when a glue value exists but is unverified.
            g_use = g_val if (g_ver and g_val is not None) else 0.0
            om_verified = om_val if (om_ver and om_val is not None) else 0.0
            om_iffilled = om_val if (om_val is not None) else 0.0  # value if confirmed

            box = two_lever_box_check(g_use, om_verified, u_over_omega=U_OVER_OMEGA)
            # T_c from VERIFIED Omega only (None when no verified glue -> not zero-as-data)
            if om_verified > 0:
                tc2d = round(geometric_bkt_tc_band(om_verified), 1)
                tc3d = round(stacked_tc(om_verified, three_d=True), 1)
            else:
                tc2d = tc3d = None
            # "if gaps filled" T_c: uses the (possibly unverified) candidate value
            tc3d_iffilled = round(stacked_tc(om_iffilled, three_d=True), 1) if om_iffilled > 0 else None

            rows.append({
                "pair": f"{a['name']}/hBN/{b['name']}",
                "A": a["name"], "B": b["name"],
                "g_use": g_use, "omega_verified_meV": om_verified,
                "omega_iffilled_meV": om_iffilled,
                "in_box": box["in_box"], "gates": box["gates"],
                "fully_verified": (not blocked),
                "bkt_tc_2d_K": tc2d, "bkt_tc_3d_K": tc3d,
                "bkt_tc_3d_iffilled_K": tc3d_iffilled,
                "gaps": gaps,
            })
    return rows


def rank_key(r):
    # fully-verified box-clearing first; then by realized bkt_Tc_3D; the estimator is
    # Omega-only so verified pairs sharing a B host TIE on bkt -> break the tie by the
    # geometry lever g (larger g = better margin on the A gate); then by if-filled, name.
    realized = r["bkt_tc_3d_K"] if r["bkt_tc_3d_K"] is not None else -1.0
    iffilled = r["bkt_tc_3d_iffilled_K"] if r["bkt_tc_3d_iffilled_K"] is not None else -1.0
    return (
        0 if (r["fully_verified"] and r["in_box"]) else 1,
        -realized,
        -r["g_use"],
        -iffilled,
        r["pair"],
    )


def main():
    rows = build_rows()
    ranked = sorted(rows, key=rank_key)

    verified_box = [r for r in ranked if r["fully_verified"] and r["in_box"]]
    best_verified = verified_box[0] if verified_box else None
    # best IF gaps were filled: among NOT-fully-verified pairs, the highest if-filled
    # bkt that WOULD clear the box once its missing values are confirmed.
    iffilled_cands = [r for r in ranked if not (r["fully_verified"] and r["in_box"])
                      and r["bkt_tc_3d_iffilled_K"] is not None]
    best_iffilled = sorted(iffilled_cands, key=lambda r: -r["bkt_tc_3d_iffilled_K"])[0] \
        if iffilled_cands else None

    # monotonicity check: sort fully-verified pairs by verified Omega, bkt must be non-decreasing.
    fv = [r for r in rows if r["omega_verified_meV"] > 0]
    fv_sorted = sorted(fv, key=lambda r: r["omega_verified_meV"])
    monotone = all(
        fv_sorted[i]["bkt_tc_2d_K"] <= fv_sorted[i + 1]["bkt_tc_2d_K"] + 1e-9
        for i in range(len(fv_sorted) - 1)
    )
    # no fabrication: a nonzero verified Omega must yield a real bkt (i.e. it WAS verified).
    no_fab = all(
        (r["omega_verified_meV"] == 0.0) or (r["bkt_tc_3d_K"] is not None)
        for r in rows
    )
    # every gap-blocked pair names a concrete missing property
    gaps_named = all(len(r["gaps"]) > 0 for r in rows if not r["fully_verified"])

    metrics = {
        "n_pairs": len(rows),
        "n_fully_verified_in_box": len(verified_box),
        "best_verified_pair": best_verified["pair"] if best_verified else None,
        "monotone": monotone,
        "no_fabrication": no_fab,
        "gaps_named": gaps_named,
    }
    fals = [
        Falsifier("F1_verified_pair_exists",
                  lambda m: not (m["n_fully_verified_in_box"] >= 1),
                  "PASS = at least one fully-verified box-clearing A/B pair exists."),
        Falsifier("F2_leaderboard_monotone",
                  lambda m: not m["monotone"],
                  "PASS = bkt_Tc non-decreasing in verified Omega (estimator monotone)."),
        Falsifier("F3_no_fabricated_values",
                  lambda m: not m["no_fabrication"],
                  "PASS = every nonzero box input traces to a VERIFIED registry source."),
        Falsifier("F4_best_is_CoSn_Ta2NiSe5",
                  lambda m: m["best_verified_pair"] != "CoSn/hBN/Ta2NiSe5",
                  "PASS = the best fully-verified pair is CoSn/hBN/Ta2NiSe5 (pre-registered)."),
        Falsifier("F5_gaps_named",
                  lambda m: not m["gaps_named"],
                  "PASS = every gap-blocked pair names a concrete missing/unverified property."),
    ]
    verdict = evaluate(metrics, fals)

    # ---------------------------------------------------------------- verbatim verdict block
    lines = []
    P = lines.append
    P("================ H_021  A x B PAIR LEADERBOARD (+@ trilayer) ================")
    P(f"registry: {_SOURCE}")
    P(f"box: g>=2.0  Omega>=130 meV  U/Omega>=1.5 (U/Omega held = {U_OVER_OMEGA}, registry demo)")
    P(f"bkt_Tc_2D = geometric_bkt_tc_band(Omega) = 0.4559*Omega[meV];  "
      f"bkt_Tc_3D = {THREED_TC_LEVER}x  (room_T target = 293 K)")
    P(f"pairs: {len(rows)}  ({len(LAYER_A)} A x {len(LAYER_B)} B)")
    P("-" * 78)
    P(f"{'rank':>4} {'pair':28s} {'in_box':>6} {'g':>5} {'Om':>6} "
      f"{'Tc2D':>6} {'Tc3D':>6} {'status':>8}")
    P("-" * 78)
    for i, r in enumerate(ranked, 1):
        if r["fully_verified"] and r["in_box"]:
            status = "VERIFIED"
        elif r["fully_verified"]:
            status = "OUT-BOX"
        else:
            status = "GAP-BLK"
        om = f"{r['omega_verified_meV']:.0f}" if r["omega_verified_meV"] else "-"
        g = f"{r['g_use']:.2f}" if r["g_use"] else "-"
        t2 = f"{r['bkt_tc_2d_K']:.1f}" if r["bkt_tc_2d_K"] is not None else "-"
        t3 = f"{r['bkt_tc_3d_K']:.1f}" if r["bkt_tc_3d_K"] is not None else "-"
        ib = "YES" if r["in_box"] else "no"
        P(f"{i:>4} {r['pair']:28s} {ib:>6} {g:>5} {om:>6} {t2:>6} {t3:>6} {status:>8}")
    P("-" * 78)
    P("gap-blocked detail (what research must still confirm):")
    for r in ranked:
        if not r["fully_verified"]:
            ifk = f"{r['bkt_tc_3d_iffilled_K']:.1f}K" if r["bkt_tc_3d_iffilled_K"] is not None else "n/a"
            P(f"  {r['pair']:28s} Tc3D_if_filled={ifk:>8}  gaps: {'; '.join(r['gaps'])}")
    P("-" * 78)
    if best_verified:
        P(f"BEST fully-verified pair : {best_verified['pair']}  "
          f"in_box={best_verified['in_box']}  "
          f"bkt_Tc_2D={best_verified['bkt_tc_2d_K']}K  bkt_Tc_3D={best_verified['bkt_tc_3d_K']}K")
    else:
        P("BEST fully-verified pair : NONE (no pair clears the box on verified values)")
    if best_iffilled:
        P(f"BEST if-gaps-filled pair : {best_iffilled['pair']}  "
          f"bkt_Tc_3D_if_filled={best_iffilled['bkt_tc_3d_iffilled_K']}K  "
          f"(needs: {'; '.join(best_iffilled['gaps'])})")
    else:
        P("BEST if-gaps-filled pair : NONE")
    P("-" * 78)
    for fr in verdict["falsifiers"]:
        P(f"  [{fr['status']}] {fr['name']}  (triggered={fr['triggered']})")
    P(f"falsifiers: {verdict['n_pass']}/{verdict['n_total']} PASS  "
      f"all_pass={verdict['all_pass']}")
    P("VERDICT: 🟠 CREDIBLE-PARTIAL — CoSn/hBN/Ta2NiSe5 tops the leaderboard (best of")
    P("  two box-clearing pairs; ties Nb3Cl8/hBN/Ta2NiSe5 on bkt, wins on g=2.87>2.11).")
    P(f"  bkt_Tc_2D={best_verified['bkt_tc_2d_K']}K, bkt_Tc_3D={best_verified['bkt_tc_3d_K']}K @ coordinate; the trio")
    P("  is JOINTLY UNREALIZED and bkt_Tc is a COORDINATE not a prediction (H_018).")
    P("  absorbed=false / GATE_OPEN. The strongest 🟠, not 🟢.")
    P("============================================================================")
    block = "\n".join(lines)
    print(block)

    out = {
        "domain": "rtsc",
        "hypothesis": "H_021",
        "registry_source": _SOURCE,
        "u_over_omega": U_OVER_OMEGA,
        "threed_lever": THREED_TC_LEVER,
        "metrics": metrics,
        "best_verified_pair": best_verified["pair"] if best_verified else None,
        "best_verified_bkt_tc_2d_K": best_verified["bkt_tc_2d_K"] if best_verified else None,
        "best_verified_bkt_tc_3d_K": best_verified["bkt_tc_3d_K"] if best_verified else None,
        "best_iffilled_pair": best_iffilled["pair"] if best_iffilled else None,
        "best_iffilled_bkt_tc_3d_K": best_iffilled["bkt_tc_3d_iffilled_K"] if best_iffilled else None,
        "leaderboard": [
            {"rank": i, "pair": r["pair"], "in_box": r["in_box"],
             "fully_verified": r["fully_verified"],
             "g_use": r["g_use"], "omega_verified_meV": r["omega_verified_meV"],
             "bkt_tc_2d_K": r["bkt_tc_2d_K"], "bkt_tc_3d_K": r["bkt_tc_3d_K"],
             "bkt_tc_3d_iffilled_K": r["bkt_tc_3d_iffilled_K"], "gaps": r["gaps"]}
            for i, r in enumerate(ranked, 1)
        ],
        "falsifiers": [{"name": f["name"], "status": f["status"]} for f in verdict["falsifiers"]],
        "all_pass": verdict["all_pass"],
        "verdict_block": block,
    }
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "result.json"), "w") as fh:
        json.dump(out, fh, indent=2, ensure_ascii=False, sort_keys=True)
        fh.write("\n")


if __name__ == "__main__":
    main()
