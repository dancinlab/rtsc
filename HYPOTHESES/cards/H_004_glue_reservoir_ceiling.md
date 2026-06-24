---
id: H_004
slug: glue-reservoir-ceiling
title: The +@ box reaches room-T only with an electronic (eV-class) glue — a phonon glue tops out ~91 K (the ~5× deficit holds for phonons)
domain: rtsc
status: model-probe
exploration_method: M3 BORROW (brainstorm seed B3) — draw glue from a faster/denser (electronic) reservoir
verification_method: W1 (pre-register frozen) + W2 (falsifier-5) + W3 (deterministic) + W5 (honest-limits-5)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
since: 2026-06-25
---

# H_004 — glue-reservoir ceiling: what coupling reaches room-T (rtsc)

## Hypothesis

H_003's +@ bilayer opened the two-lever box but only to bkt_Tc ~59 K. Inverting the geometric
BKT band for 293 K, the box needs Ω ~ 643 meV — far above the hardest ambient phonon
(~200 meV, H–H stretch). Therefore room-T via the +@ geometric box requires a **non-phonon,
electronic glue** (exciton / plasmon / magnon, eV-class), not a stiffer phonon.

## Why

- bkt_Tc ∝ Ω in the calibrated band; room-T is a coupling-scale demand, and the phonon
  reservoir is bounded (~200 meV) → a phonon glue caps the +@ box at ~91 K.
- Brainstorm seed B3 (M3 BORROW): draw the glue from a denser/faster reservoir — an
  electronic mode lives at the eV scale and can, in principle, supply Ω ~ 643 meV.

## Predictions

- **H4.1**: Ω required for 293 K exceeds the phonon ceiling (phonon glue insufficient).
- **H4.2**: an eV-class electronic glue clears the room-T coupling demand in the band.

## Variables

- **target T_c**: 293 K (room-T) vs 133 K (cuprate ambient ceiling)
- **glue reservoirs**: phonon (200 meV ceiling) vs electronic (eV-class ~1500 meV order)

## Run Protocol

- deterministic, stdlib only, $0 mac local
- tools: `tool/rtsc_harness.py` (`omega_for_bkt_tc`, `geometric_bkt_tc_band`,
  `PHONON_CEILING_MEV`)
- run: `python3 state/h004_glue_reservoir_ceiling_2026_06_25/run_h004.py`
- record: `state/h004_glue_reservoir_ceiling_2026_06_25/result.json`

## Criteria

- **verdict_rule**: PHONON-GLUE-INSUFFICIENT = room-T Ω demand exceeds the phonon ceiling
  AND an electronic reservoir clears it; otherwise re-open.

## Falsifiers (≥5 — pre-registered)

- **F1_phonon_insufficient**: PASS = room-T demands Ω above the phonon ceiling.
- **F2_electronic_sufficient**: PASS = an eV-class electronic glue reaches ≥293 K in the band.
- **F3_phonon_below_roomT**: PASS = a max-stiff phonon glue stays below 293 K (deficit holds).
- **F4_monotone**: PASS = room-T requires more coupling than the 133 K ceiling.
- **F5_bounds**: PASS = required Ω > 0 and electronic scale > phonon ceiling.

## Honest Limits (≥5)

- **L1 (band model, not Eliashberg)**: bkt_Tc∝Ω is the calibrated order-of-magnitude band
  (deflated to 3 anchors), not a full Eliashberg/Migdal solution at eV coupling — where
  Migdal's theorem itself breaks down (the very regime an electronic glue lives in).
- **L2 (the electronic glue carries the M3 ledger deficit)**: an eV-scale electronic mode
  strong enough to pair also drives competing order (CDW / magnetism / phase separation).
  BORROW relocates the bill into "pair without a competing instability" (unsolved).
- **L3 (Ω scales are published orders, not a synthesized glue)**: 200 meV / 1500 meV are
  reservoir orders, not a specific material's measured coupling.
- **L4 (U/Ω gate at eV)**: the U/Ω≥1.5 box gate assumed from H_001 is a phonon-regime gate;
  at electronic coupling U and Ω are both eV and the gate's calibration is uncertain.
- **L5**: no claim of an existing electronic-glue room-T SC — this classifies WHICH reservoir
  could supply the coupling, not that one is realized. `absorbed=true` still needs accredited
  transport + Meissner + measured H_c2 / T_c.

## Cross-Links

- **parent**: H_003 (+@ bilayer that opened the box to 59 K — the deficit this deepens).
- **child**: H_005 (combination capstone stacking this electronic glue with the bilayer).
- **seed**: `state/sf-abstract-brainstorm.md` B3 (faster boson glue, M3 BORROW).

## Verdict

**🟡 MODEL-PROBE → PHONON-GLUE-INSUFFICIENT, ROOM-T NEEDS AN ELECTRONIC RESERVOIR.**
Verbatim stdout (`state/h004_glue_reservoir_ceiling_2026_06_25/run_h004.py`):

```
=== H_004 glue-reservoir ceiling — deepening the +@ box to room-T ===
  Omega required for room-T (293 K) = 642.7 meV
  Omega required for ceiling (133 K) = 291.7 meV
  phonon glue ceiling (H-H stretch)  = 200.0 meV -> tc_max ~91.2K
  electronic glue (exciton/plasmon)  = 1500.0 meV -> tc ~683.8K
  falsifier F1_phonon_insufficient  : PASS
  falsifier F2_electronic_sufficient: PASS
  falsifier F3_phonon_below_roomT   : PASS
  falsifier F4_monotone             : PASS
  falsifier F5_bounds               : PASS
  falsifiers_pass = 5/5
VERDICT: PHONON-GLUE-INSUFFICIENT → ROOM-T NEEDS AN ELECTRONIC RESERVOIR
```

- **structural_finding**: room-T via the +@ geometric box is a 643 meV coupling demand —
  a phonon glue (≤200 meV) caps at ~91 K; only an electronic (eV) reservoir can supply it,
  relocating the wall from "stiffer phonon" (impossible) to "pair on an electronic glue
  without a competing instability" (the M3 ledger deficit, unsolved).
- **record**: `state/h004_glue_reservoir_ceiling_2026_06_25/result.json`.
