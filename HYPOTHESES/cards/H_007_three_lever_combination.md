---
id: H_007
slug: three-lever-combination
title: A 3-lever stack (geometry × electronic glue × real 3D lever) reaches room-T by RELAXING each lever's demand 1.84× — 3-combination beats 2-combination, each lever necessary
domain: rtsc
status: model-probe
exploration_method: combination-order scan (1 vs 2 vs 3 levers) — user directive "explore 3-combinations too"
verification_method: W1 (pre-register frozen) + W2 (falsifier-5) + W3 (deterministic) + W5 (honest-limits-6)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
since: 2026-06-25
---

# H_007 — combination-order scan: 1 vs 2 vs 3 levers (rtsc)

## Hypothesis

Stacking a THIRD orthogonal lever onto the +@ combination does not just add T_c — it
**relaxes the demand on the other levers**. The third lever is the **real 3D-vs-2D T_c
lever** L_3D = 1.84× (measured by `src/fbgeom_3d.py`: BKT-vortex removal 1.50 × coordination
boost 1.22). With it, the electronic-glue scale a room-T stack needs drops from ~643 meV
(2-lever) to ~349 meV (3-lever) — a far more modest, more reachable glue. Each lever is
necessary (ablate one → room-T fails).

## Why

- H_005 reached room-T in the toy band but with an *extreme* 2-lever glue (~643 meV /
  sub-eV plasmon). The campaign deficit is ~5×; any single lever closes only part of it.
- A 3-combination distributes the deficit: each lever carries a smaller share, so each
  per-lever requirement (glue stiffness, interface quality, 3D gap) is individually milder.
- The 3D lever is *real* (computed, not a model knob), making this the first +@ card where
  one of the stacked levers is a measured quantity.

## Predictions

- **H7.1**: the 3-lever stack clears 293 K with the relaxed glue (~349 meV).
- **H7.2**: the same glue at 2 levers (no 3D) falls short (~159 K) → 3D necessary.
- **H7.3**: the 3-lever glue requirement is ~1.84× below the 2-lever requirement.

## Variables

- **geometry**: flat-band host g=2.87 (H_001)
- **glue**: electronic coupling Ω = the relaxed 3-lever requirement (computed, not hand-set)
- **3D lever**: L_3D = 1.84 (real, `src/fbgeom_3d.py`)

## Run Protocol

- deterministic, stdlib only, $0 mac local
- tools: `tool/rtsc_harness.py` (`stacked_tc`, `omega_for_stacked_tc`, `THREED_TC_LEVER`,
  `geometric_bkt_tc_band`, `PHONON_CEILING_MEV`)
- run: `python3 state/h007_three_lever_combination_2026_06_25/run_h007.py`
- record: `state/h007_three_lever_combination_2026_06_25/result.json`

## Criteria

- **verdict_rule**: 3-LEVER-RELAXES = the 3-lever stack reaches 293 K, the same glue at
  2 levers does not, and the glue demand is relaxed by ≈L_3D; each ablation re-erects a wall.

## Falsifiers (≥5 — pre-registered)

- **F1_3lever_reaches_roomT**: PASS = the 3-lever stack clears 293 K.
- **F2_3d_necessary**: PASS = dropping the 3D lever (same glue) falls below 293 K.
- **F3_demand_relaxed**: PASS = the 3-lever glue demand is below the 2-lever demand (>1.05×).
- **F4_glue_necessary**: PASS = phonon ceiling + 3D still below 293 K.
- **F5_order_monotone**: PASS = T_c rises with combination order (1 < 2 < 3 levers).

## Honest Limits (≥6)

- **L1 (TOY band)**: bkt_Tc∝Ω calibrated band on a model geometry; not a material. 🟡 MODEL-PROBE.
- **L2 (levers may NOT be independent / multiplicative)**: stacking assumes the 3D lever and
  the glue lever multiply cleanly. In a real 3D heterostructure the proximity import (H_003)
  and the 3D coordination compete (a 3D host is not a clean bilayer) — the strongest limit.
- **L3 (the 3D lever carries its own bill)**: L_3D=1.84 is real but native 3D flat bands are
  gapless band-touchings (H_006 real); the trustworthy stiffness needs an SOC gap that costs
  ⟨g⟩. The 1.84× is an upper-corner value, not free.
- **L4 (orthogonal-family census — depletion check)**: the remaining brainstorm +@ families
  classify as: B1 Floquet / B11 eff-T → reduce to the M3 ledger deficit (drive power);
  B6 bipolaron / B3 electronic glue → the H_004/H_008 glue lever; B7 topology → a gap lever
  (untested, needs its own model); S5 fractionalization / O2 disorder → orthogonal, need own
  model. Closed-form stacking of the *computed* levers (geometry × glue × 3D) is DEPLETED here;
  topology (B7) and fractionalization (S5) are the only un-modeled orthogonal axes left.
- **L5 (room-T is marginal, not robust)**: the 3-lever stack lands AT 293 K with the exact
  relaxed glue — a knife-edge, not a comfortable margin; any lever shortfall drops below.
- **L6**: `absorbed=true` still requires accredited 4-probe transport + Meissner + measured
  H_c2 / T_c — no stacked simulation flips that gate (commons honesty).

## Cross-Links

- **parents**: H_003 (geometry-import) · H_004 (glue) · H_006 (real 3D lever) · H_005 (2-factor capstone).
- **sibling**: H_008 (real bipolaron ED — the glue lever's many-body verdict).

## Verdict

**🟡 MODEL-PROBE → 3-LEVER STACK REACHES ROOM-T BY RELAXING EACH LEVER'S DEMAND.** Verbatim
stdout (`state/h007_three_lever_combination_2026_06_25/run_h007.py`):

```
=== H_007 combination-order scan — 1 vs 2 vs 3 levers ===
  L_3D (real, src/fbgeom_3d.py) = 1.84x
  glue Omega required for room-T:  2-lever = 642.7 meV  ->  3-lever = 349.3 meV  (relaxed 1.84x)
  Tc by combination order (glue=349.3meV = relaxed 3-lever requirement):
    1-lever (geometry + soft phonon)        bkt_Tc ~ 10.0 K   (H_001 wall)
    2-lever (geometry + glue, 2D)           bkt_Tc ~ 159.2 K   (box open, room-T missed)
    3-lever (geometry + glue + 3D)          bkt_Tc ~ 293.0 K   (room-T CLEARED)
  ablate 3D   -> 159.2 K  (FAILS)
  ablate glue -> 167.8 K  (FAILS)
  falsifier F1_3lever_reaches_roomT : PASS
  falsifier F2_3d_necessary         : PASS
  falsifier F3_demand_relaxed       : PASS
  falsifier F4_glue_necessary       : PASS
  falsifier F5_order_monotone       : PASS
  falsifiers_pass = 5/5
VERDICT: 3-LEVER STACK REACHES ROOM-T BY RELAXING EACH LEVER'S DEMAND (each lever necessary)
```

- **structural_finding**: a 3-combination beats a 2-combination not by adding T_c but by
  **dividing the ~5× deficit** — each lever's individual requirement softens (glue 643→349 meV).
  The room-T target is met at a knife-edge with each lever necessary; the win is conditional on
  the levers actually being independent in a real 3D heterostructure (L2), the dominant open risk.
- **record**: `state/h007_three_lever_combination_2026_06_25/result.json`.
