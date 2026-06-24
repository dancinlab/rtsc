---
id: H_005
slug: combination-capstone
title: The +@ combination stack (geometry-import × electronic glue × ideal interface) reaches the 293 K box in the toy band — each lever necessary, breakthrough conditional on 2 stacked unsolved sub-problems
domain: rtsc
status: model-probe
exploration_method: M1 SPLIT × M3 BORROW (stack B2 + B3) — the combination capstone
verification_method: W1 (pre-register frozen) + W2 (falsifier-5) + W3 (deterministic) + W5 (honest-limits-6)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
since: 2026-06-25
---

# H_005 — +@ combination capstone: full stack + ablation (rtsc)

## Hypothesis

Stacking the two orthogonal +@ levers the deepening surfaced — (B2) bilayer geometry-import
through a phonon-transparent / electron-opaque interface (H_003), and (B3) an electronic
(eV-class) glue reservoir replacing the phonon ceiling (H_004) — reaches the **293 K**
two-lever box in the toy band, and **each lever is necessary** (ablate one → a wall returns).
This is the rtsc analog of lumen's combination capstone: no single lever wins, but the stack
clears the wall — honestly, conditional on two stacked unsolved materials sub-problems.

## Why

- H_001 closed the single-host path; H_003 showed the +@ SPLIT opens the box (to 59 K);
  H_004 showed room-T needs an electronic glue. The capstone tests the *conjunction*.
- The break-walls discipline demands an ablation: a combination "win" is only real if each
  lever is load-bearing (dropping it re-erects a wall) — otherwise it is over-claimed.

## Predictions

- **H5.1**: the full stack (geometry + electronic glue + ideal interface) enters the box AND
  clears 293 K in the toy band.
- **H5.2**: ablating ANY one lever re-erects a wall (glue→phonon caps ~91 K; geometry→box
  closes; interface→box closes).

## Variables

- **geometry**: layer-A flat band (g=2.87, published)
- **electronic glue**: Ω_e ~700 meV (sub-eV plasmon/exciton order, minimal to clear 293 K)
- **interface**: ideal (electron_cost=0) vs generic (electron_cost=1)

## Run Protocol

- deterministic, stdlib only, $0 mac local
- tools: `tool/rtsc_harness.py` (`proximity_bilayer_levers`, `two_lever_box_check`,
  `geometric_bkt_tc_band`, `PHONON_CEILING_MEV`)
- run: `python3 state/h005_combination_capstone_2026_06_25/run_h005.py`
- record: `state/h005_combination_capstone_2026_06_25/result.json`

## Criteria

- **verdict_rule**: ROOM-T-REACHABLE-IN-TOY-BAND = full stack in box AND ≥293 K AND all
  three ablations re-erect a wall; otherwise the combination is over-claimed or a lever is
  redundant.

## Falsifiers (≥5 — pre-registered)

- **F1_stack_reaches_roomT**: PASS = the full +@ stack enters the box AND clears 293 K.
- **F2_glue_necessary**: PASS = dropping the electronic glue falls below 293 K (phonon-limited).
- **F3_geometry_necessary**: PASS = dropping the flat-band geometry closes the box.
- **F4_interface_necessary**: PASS = a generic interface closes the box.
- **F5_bounds**: PASS = T_c values positive.

## Honest Limits (≥6)

- **L1 (TOY band, not a real material)**: this is the strongest honest limit — the 319 K is a
  calibrated order-of-magnitude band on a separable toy geometry with model interface/glue
  knobs, NOT a synthesized heterostructure. Tier 🟡 MODEL-PROBE. No claim that any material
  is a room-T SC.
- **L2 (the breakthrough is a FACTORIZATION, not a removal)**: the +@ stack does not delete
  the room-T wall — it factorizes it into two real, separately-unsolved sub-problems:
  (a) a phonon-transparent / electron-opaque interface (H_003, electron_cost ≤ 0.415), and
  (b) an electronic glue that pairs without a competing instability (H_004, the M3 deficit).
  The combination is only as real as the harder of the two factors.
- **L3 (Migdal/Eliashberg breakdown at eV glue)**: an electronic glue at 700 meV is outside
  Migdal-Eliashberg validity; the BKT band extrapolation there is uncontrolled.
- **L4 (ablations are model-internal)**: necessity is shown within the toy model; a real
  heterostructure could couple the levers (interface quality ↔ glue ↔ geometry) in ways the
  separable model misses.
- **L5 (no competing-order accounting)**: the capstone does not model CDW/magnetic/structural
  competition that an eV electronic glue invites — the dominant real-world failure mode.
- **L6**: `absorbed=true` still requires accredited 4-probe transport + Meissner expulsion +
  measured H_c2 / T_c — no stacked simulation flips that gate (commons honesty).

## Cross-Links

- **parents**: H_003 (geometry-import / interface lever) + H_004 (electronic-glue lever).
- **grandparent wall**: H_001 (the single-host two-lever wall the stack bypasses).
- **next (real verdict)**: a DFT/DFPT/el-ph heterostructure calc in `src/` on a cloud pod —
  the two factor sub-problems, measured on a real spacer + electronic-glue candidate.

## Verdict

**🟢 MODEL-PROBE → ROOM-T REACHABLE IN TOY BAND, CONDITIONAL ON 2 STACKED UNSOLVED
SUB-PROBLEMS.** Verbatim stdout (`state/h005_combination_capstone_2026_06_25/run_h005.py`):

```
=== H_005 +@ combination capstone — full stack + ablation ===
  FULL stack (geometry + electronic glue 700.0meV + ideal interface):
    g_eff=2.87 omega_eff=700.0meV -> in_box=True  bkt_Tc~319.1K  (room-T 293.0K: CLEARED)
  ablate electronic glue -> phonon ceiling: bkt_Tc~91.2K  (room-T: FAILS)
  ablate geometry layer (g<2):              in_box=False
  ablate interface quality (generic):       in_box=False
  falsifier F1_stack_reaches_roomT  : PASS
  falsifier F2_glue_necessary       : PASS
  falsifier F3_geometry_necessary   : PASS
  falsifier F4_interface_necessary  : PASS
  falsifier F5_bounds               : PASS
  falsifiers_pass = 5/5
VERDICT: ROOM-T REACHABLE IN TOY BAND — CONDITIONAL ON 2 STACKED UNSOLVED SUB-PROBLEMS
```

- **structural_finding**: the +@ combination breaks the room-T *box wall* in the toy band
  (each lever load-bearing), but by *factorizing* it — the wall reappears as the conjunction
  of (a) an electron-opaque/phonon-transparent interface and (b) a competing-order-free
  electronic glue. Honest endpoint: a candidate ARCHITECTURE for room-T, not a claim of one.
- **record**: `state/h005_combination_capstone_2026_06_25/result.json`.
