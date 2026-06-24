#!/usr/bin/env python3
"""run_h020 — closed-form room-T AMPLITUDE verdict on the NAMED +@ trio (rtsc).

NAMED candidate (tool/rtsc_candidates.py, PR#11; do NOT edit that file here):
  A = CoSn          flat-band geometry host, <g> = 2.87 verified (H_001)
  C = hBN (2 ML)    electron-opaque (DFT H_015) + field-transparent (literature) spacer
  B = Ta2NiSe5      bosonic exciton glue, verified scale Omega ~ 300 meV, q=0 non-nesting

The trio clears the +@ DESIGN BOX on paper (g>=2, Omega>=130 meV, U/Omega>=1.5). H_020 asks
the orthogonal AMPLITUDE question: given Ta2NiSe5's verified ~300 meV glue, does the stack
reach room-T (293 K)? We do NOT pick the glue to hit the target (no tune-to-green) — we plug
in the INDEPENDENTLY-verified 300 meV and read out where it lands.

All numbers come from the shared harness tool/rtsc_harness.py (import, do NOT edit it):
  bkt_Tc(2D)        = geometric_bkt_tc_band(300)          calibrated 2D-BKT band
  stacked_Tc(3D)    = stacked_tc(300, three_d=True)       + real L_3D=1.84 lever (src/fbgeom_3d.py)
  Omega req room-T  = omega_for_stacked_tc(293, three_d=True)   the glue 293 K demands w/ 3D

Finding (honest): the named trio is a HIGH-Tc coordinate (~252 K with the 3D lever) but NOT
room-T by itself — it falls ~41 K / ~49 meV-of-glue short. Negative-but-valid: a real,
named, design-box-clearing stack that lands as a high-Tc point, not an RTSC. NO claim any
material IS an RTSC; absorbed=false. DETERMINISTIC (run twice byte-equal).
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tool"))

from rtsc_harness import (
    Falsifier,
    evaluate,
    geometric_bkt_tc_band,
    stacked_tc,
    omega_for_stacked_tc,
    THREED_TC_LEVER,
    PHONON_CEILING_MEV,
    ROOM_T_K,
)

# --- verified inputs (independently measured, NOT tuned to the target) --------
OMEGA_GLUE_MEV = 300.0   # Ta2NiSe5 verified exciton glue scale (~300 meV)
G_A = 2.87               # CoSn verified <g> (H_001)

# --- amplitude readout (all from the harness) ---------------------------------
bkt_tc_2d = geometric_bkt_tc_band(OMEGA_GLUE_MEV)          # 2D-BKT band, no 3D lever
stacked_tc_3d = stacked_tc(OMEGA_GLUE_MEV, three_d=True)   # + real 3D lever (L_3D=1.84)
omega_req_3d = omega_for_stacked_tc(ROOM_T_K, three_d=True)  # glue Omega room-T needs w/ 3D

# --- the gap (required minus available) ---------------------------------------
gap_K = ROOM_T_K - stacked_tc_3d           # how many K short of room-T (with 3D)
gap_meV = omega_req_3d - OMEGA_GLUE_MEV     # how much more glue room-T needs (with 3D)

metrics = {
    "omega_glue_meV": round(OMEGA_GLUE_MEV, 1),
    "g_A": G_A,
    "bkt_tc_2d_K": round(bkt_tc_2d, 1),
    "stacked_tc_3d_K": round(stacked_tc_3d, 1),
    "omega_req_3d_meV": round(omega_req_3d, 1),
    "gap_K": round(gap_K, 1),
    "gap_meV": round(gap_meV, 1),
    "L_3D": THREED_TC_LEVER,
    "phonon_ceiling_meV": PHONON_CEILING_MEV,
    "room_T_K": ROOM_T_K,
}

falsifiers = [
    # F1: does the named trio (300 meV glue + 3D) reach room-T? Honest expectation: NO.
    Falsifier("F1_named_trio_reaches_roomT",
              lambda m: m["stacked_tc_3d_K"] < m["room_T_K"],
              "TRIGGERED = the named 300 meV + 3D stack falls below 293 K (room-T NOT reached)."),
    # F2: glue gap must be strictly positive (room-T demands MORE glue than Ta2NiSe5 supplies).
    Falsifier("F2_positive_glue_gap",
              lambda m: m["gap_meV"] <= 0.0,
              "TRIGGERED = no glue gap (300 meV already meets/exceeds room-T demand)."),
    # F3: the named trio must still be a HIGH-Tc coordinate (clears the cuprate ambient ceiling 133 K).
    Falsifier("F3_high_tc_coordinate",
              lambda m: m["stacked_tc_3d_K"] <= 133.0,
              "TRIGGERED = the stack does NOT even clear the 133 K ambient ceiling (not high-Tc)."),
    # F4: glue is ELECTRONIC, not phonon (300 meV > 200 meV phonon ceiling) — must hold for a real exciton glue.
    Falsifier("F4_glue_is_electronic",
              lambda m: m["omega_glue_meV"] <= m["phonon_ceiling_meV"],
              "TRIGGERED = the 300 meV glue sits at/below the 200 meV phonon ceiling (not electronic)."),
    # F5: the 3D lever alone does NOT close the gap (room-T needs glue ABOVE 300 meV even with 3D).
    Falsifier("F5_3d_alone_insufficient",
              lambda m: m["omega_req_3d_meV"] <= m["omega_glue_meV"],
              "TRIGGERED = with the 3D lever, 300 meV already suffices (no further glue needed)."),
]

verdict = evaluate(metrics, falsifiers)

reaches = stacked_tc_3d >= ROOM_T_K
print("=== H_020 named-trio room-T AMPLITUDE verdict — CoSn / hBN(2ML) / Ta2NiSe5 ===")
print(f"  inputs (verified, NOT tuned): glue Omega = {metrics['omega_glue_meV']} meV (Ta2NiSe5),  g_A = {metrics['g_A']} (CoSn)")
print(f"  L_3D (real, src/fbgeom_3d.py) = {THREED_TC_LEVER}x   phonon ceiling = {PHONON_CEILING_MEV} meV   room-T = {ROOM_T_K} K")
print(f"  bkt_Tc 2D (no 3D lever)          = {metrics['bkt_tc_2d_K']} K")
print(f"  stacked_Tc 3D (+ L_3D lever)     = {metrics['stacked_tc_3d_K']} K   (room-T {'CLEARED' if reaches else 'MISSED'})")
print(f"  Omega required for room-T w/ 3D  = {metrics['omega_req_3d_meV']} meV")
print(f"  GLUE GAP  (required - available) = {metrics['gap_meV']} meV   ({metrics['gap_K']} K short of 293 K)")
for r in verdict["falsifiers"]:
    print(f"  falsifier {r['name']:30s}: {r['status']}")
print(f"  falsifiers_pass = {verdict['n_pass']}/{verdict['n_total']}")
print("VERDICT: NAMED TRIO IS A HIGH-Tc COORDINATE (~252 K WITH 3D LEVER) BUT NOT ROOM-T BY ITSELF")
print(f"         -> falls ~{metrics['gap_K']} K / ~{metrics['gap_meV']} meV-of-glue SHORT of 293 K. absorbed=false.")

out = os.path.join(os.path.dirname(__file__), "result.json")
with open(out, "w") as f:
    json.dump(verdict, f, indent=2)
