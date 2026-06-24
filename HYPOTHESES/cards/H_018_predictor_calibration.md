---
id: H_018
slug: predictor-calibration
title: Adversarial held-out check of the campaign's central Tc estimator — it gets the AVERAGE right (geomean 1.86×, within band) but FAILS on per-material SCATTER (1061× spread on 8 held-out anchors), so individual Tc predictions (incl. the 293 K room-T extrapolation) carry order-of-magnitude uncertainty
domain: rtsc
status: closed-negative
exploration_method: adversarial verify-done — held-out validation of geometric_bkt_tc_band
verification_method: W1 (pre-register frozen) + W2 (falsifier-5) + W3 (deterministic) + W5 (honest-limits-5)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
compute: fleet lane (verification)
---

# H_018 — adversarial held-out calibration of the central Tc estimator (rtsc)

## Hypothesis

The campaign's central tool `geometric_bkt_tc_band` (Tc = 0.4559·Ω[meV], depends on Ω ALONE)
is calibrated to 3 anchors (MATBG, tMoTe2, Re6Se8Cl2). **Adversarial claim to falsify: it
generalizes to HELD-OUT real superconductors within its calibrated ~3× band.** If it fails on
held-out data, the whole campaign Tc map — and every room-T (293 K) extrapolation built on it —
is undermined.

## Why

- Every +@ / combination card's Tc number flows through this one estimator. A held-out test is the
  honest verify-done check of the campaign's foundation (no LLM self-judge; real published anchors).
- Held-out anchors (published Tc + a citable coupling scale Ω): tTLG, RTG bilayer graphene,
  CsV3Sb5, MgB2, Pb, YBCO, … (8 total, cited in the run).

## Falsifiers (≥5 — pre-registered)

- **F1_geomean_within_3x**: PASS = held-out geomean pred/meas in [1/3, 3].
- **F2_no_systematic_bias**: PASS = |bias| < 0.477 dex (no systematic >3× over/under-prediction).
- **F3_majority_within_3x**: PASS = ≥ half of held-out anchors individually within ±3×.
- **F4_scatter_not_blown_open**: PASS = held-out scatter spread < 100× (estimator not effectively random).
- **F5_monotonic_in_Omega**: PASS = predicted Tc monotonic in Ω.

## Honest Limits (≥5)

- **L1 (Ω-kind heterogeneity)**: held-out Ω mixes flat-band/coupling scales, Debye phonon scales,
  and magnetic boson scales — the estimator was calibrated on flat-band anchors, so phonon/magnetic
  anchors stress it unfairly. The scatter is partly this apples-to-oranges Ω definition (honest, but
  it is also exactly why a single-Ω law is fragile).
- **L2 (8 anchors, small N)**: held-out statistics on 8 points are noisy; the geomean (passes) is
  more robust than the spread (fails).
- **L3 (the law dropped g and U/Ω)**: the SSOT form depends on Ω alone — the two-lever wall's other
  axes are not in the predictor, which is plausibly why per-material scatter is huge.
- **L4 (this does NOT falsify the campaign's NEGATIVE rulings)**: H_001's CLOSED-NEGATIVE used the
  design-box gates, not absolute Tc; the scatter undermines POSITIVE Tc extrapolations (room-T
  reach), not the wall findings.
- **L5**: `absorbed=true` still requires accredited transport + Meissner + measured H_c2 / T_c.

## Cross-Links

- **down-weights**: every Tc number in H_005/H_007/H_016 (the room-T extrapolations) — read them as
  order-of-magnitude, not per-material predictions.
- **does NOT undermine**: H_001/H_012/H_014/H_017 (the wall/closed-negative findings use gates/races, not absolute Tc).

## Verdict

**🟡 MODEL-PROBE → CLOSED-NEGATIVE (predictor fails held-out scatter).** Verbatim stdout excerpt
(`state/h018_predictor_calibration_2026_06_25/run_h018.py`):

```
[2] HELD-OUT anchors (real published SCs, NOT used in calibration)
    RTG bilayer graphene   Om=12.0  pred=5.47  meas=0.026   ratio=210.40
    MgB2                   Om=67.0  pred=30.54 meas=39.000  ratio=0.78
    Pb (lead)              Om=4.4   pred=2.01  meas=7.200   ratio=0.28
    YBCO (cuprate)         Om=40.0  pred=18.23 meas=92.000  ratio=0.20
[3] HELD-OUT statistics
    held-out geomean ratio = 1.862    bias = +0.270 dex    within +-3x = 4/8 (50%)
    held-out scatter spread = 1061.5x  (in-sample spread = 6.8x)
  [PASS] F1_geomean_within_3x   [PASS] F2_no_systematic_bias   [PASS] F3_majority_within_3x
  [FAIL] F4_scatter_not_blown_open   [PASS] F5_monotonic_in_Omega
  falsifiers_pass = 4/5
VERDICT: the central estimator FAILS the held-out adversarial check on >=1 axis -> the campaign
  Tc map and its room-T extrapolation are UNDERMINED; the estimator should be re-banded /
  down-weighted. VALID honest negative.
```

- **structural_finding**: the estimator gets the CENTRAL TENDENCY right (geomean 1.86×, bias +0.27
  dex, 50% within 3×, monotonic — 4/5 axes PASS) but its per-material SCATTER is enormous (0.2×–210×,
  spread 1061× vs 6.8× in-sample). So it is a fair order-of-magnitude AVERAGE but NOT a reliable
  per-material predictor — every room-T Tc number in the campaign carries ~order-of-magnitude
  uncertainty. The honest consequence: read the +@/combination Tc reaches as coordinates, not
  predictions; the negative/wall findings (gates, leading-channel races) are NOT affected.
- **record**: `state/h018_predictor_calibration_2026_06_25/result.json`.
