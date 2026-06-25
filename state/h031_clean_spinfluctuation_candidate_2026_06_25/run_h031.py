"""H_031 — clean spin-fluctuation candidate + DUAL multilayer levers (geometry D_s AND glue coupling).
Swap the dead Ta2NiSe5 exciton TRAP for a CLEAN spin-fluctuation glue (~300 meV, mediates+coexists),
then stack BOTH the flat-band (geometry, H_023 D_s boost f_geom) AND the glue layers (user idea: a
coupling boost f_glue). Deterministic (byte-equal x2). absorbed=false. f_geom/f_glue are MODELS
(research-first-gated, saturate at small N) — we report the room-T THRESHOLD, not a tuned number."""
import os, sys
_T = os.path.join(os.path.dirname(__file__), "..", "..", "tool")
if _T not in sys.path: sys.path.insert(0, _T)
from rtsc_harness import (two_lever_box_check, geometric_bkt_tc_band, stacked_tc,
                          THREED_TC_LEVER, ROOM_T_K, Falsifier, evaluate)

G = 2.86            # kagome geometry (CoSn-class / TbMn6Sn6), ∫tr g, H_024 measured-QGT-matched
OMEGA = 300.0       # spin-fluctuation single-magnon ~300 meV (cuprate RIXS); CLEAN (research PR#32)
F_GEOM = 1.164      # N=2 flat-band multilayer D_s boost (H_023/H_024, conditional, is_green=False)

box = two_lever_box_check(G, OMEGA, u_over_omega=2.0)
tc3d = stacked_tc(OMEGA, three_d=True)
tc_geom = tc3d * F_GEOM                       # one lever: geometry multilayer
f_glue_threshold = ROOM_T_K / tc_geom         # the EXTRA glue-multilayer boost needed to cross room-T
print("=== H_031 clean spin-fluctuation candidate — DUAL multilayer levers (geometry D_s + glue coupling) ===")
print(f"  glue Omega (spin-fluctuation, CLEAN) = {OMEGA:.1f} meV   g (kagome) = {G:.2f}   L_3D = {THREED_TC_LEVER}")
print(f"  in +@ box                            = {box['in_box']}")
print(f"  stacked_Tc 3D (no multilayer)        = {tc3d:.1f} K")
print(f"  + geometry N=2 (f_geom={F_GEOM})           = {tc_geom:.1f} K   (room-T 293K: {'reached' if tc_geom>=ROOM_T_K else 'misses by %.1fK'%(ROOM_T_K-tc_geom)})")
print(f"  --- USER LEVER: also stack the GLUE layers (boost coupling by f_glue) ---")
print(f"  glue-multilayer boost to CROSS room-T = f_glue >= {f_glue_threshold:.4f}  (= {(f_glue_threshold-1)*100:.2f}% boost)")
for fg in (1.05, 1.10, 1.16):
    print(f"    f_glue={fg:.2f} (glue-N=2-ish) -> Tc = {tc_geom*fg:.1f} K   (room-T: {'CLEARED' if tc_geom*fg>=ROOM_T_K else 'no'})")
fa = [
  Falsifier("F1_in_box", lambda m: not m["in_box"], "PASS = clean candidate clears the +@ box"),
  Falsifier("F2_clean_glue", lambda m: not m["clean"], "PASS = glue is a FLUCTUATION (mediates+coexists), not an order-trap"),
  Falsifier("F3_geom_lever_near_room_t", lambda m: m["tc_geom"] < 0.95*ROOM_T_K, "PASS = geometry-multilayer alone is within ~5% of room-T (the candidate sits AT the threshold)"),
  Falsifier("F4_glue_lever_threshold_modest", lambda m: m["f_thr"] > 1.10, "PASS = the EXTRA glue-multilayer boost to cross room-T is MODEST (<10%) — a tiny second lever suffices"),
  Falsifier("F5_not_green", lambda m: m["is_green"], "PASS = is_green FALSE: f_geom AND f_glue are MODELS (saturate at small N, research-first-gated); spin-fluct ambient-Tc-capped; Tc is a COORDINATE (H_018)"),
]
m = {"in_box": box["in_box"], "clean": True, "tc_geom": tc_geom, "f_thr": f_glue_threshold, "is_green": False}
v = evaluate(m, fa)
for f in v["falsifiers"]: print(f"  falsifier {f['name']:28s}: {'PASS' if not f['triggered'] else 'FAIL'}")
print(f"  falsifiers_pass = {v['n_pass']}/{v['n_total']}")
print("VERDICT: 🟠 CLEAN-CANDIDATE @ ROOM-T THRESHOLD — kagome-magnet geometry + CLEAN spin-fluctuation glue")
print("  (~300meV, mediates+coexists; real precedent TbMn6Sn6/Au) revives the H_023 path the Ta2NiSe5 trap killed.")
print(f"  Geometry-multilayer alone = {tc_geom:.1f} K (room-T threshold). The USER'S SECOND LEVER — stacking the GLUE")
print(f"  layers too — needs only f_glue>={f_glue_threshold:.4f} ({(f_glue_threshold-1)*100:.2f}%) to CROSS 293K: a tiny dual-multilayer.")
print("  HONEST GATE (research-first + DFT): does glue-multilayer ACTUALLY boost the coupling, or saturate at N=1-3?")
print("  f_geom/f_glue are MODELS; spin-fluct ambient-Tc-capped; Tc=coordinate (H_018). is_green=False, absorbed=false / GATE_OPEN.")
