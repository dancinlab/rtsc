---
id: H_020
slug: named-candidate-amplitude
title: Named-trio room-T amplitude verdict — CoSn/hBN(2ML)/Ta2NiSe5 with Ta2NiSe5's verified ~300 meV glue is a HIGH-Tc coordinate (~252 K with the 3D lever) but NOT room-T by itself, falling ~41 K / ~49 meV-of-glue short
domain: rtsc
status: closed-negative
exploration_method: pin H_007's placeholder glue to the named material's verified value
verification_method: W1 (pre-register frozen) + W2 (falsifier-5) + W3 (deterministic) + W5 (honest-limits-6)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
compute: fleet lane (named-candidate deepen)
---

# H_020 — named-trio room-T amplitude verdict (rtsc)

## Hypothesis

The named +@ trio (A=CoSn ⟨g⟩=2.87, C=hBN(2ML), B=Ta2NiSe5 exciton glue Ω≈300 meV verified)
clears the +@ design box on paper. Plugging in Ta2NiSe5's INDEPENDENTLY-verified ~300 meV glue
(no tune-to-green), does the stack reach room-T (293 K) with the real 3D lever (L_3D=1.84)? This
separates "clears the box" (membership, already true) from "reaches the target amplitude" (magnitude).

## Why

H_007's 3-lever room-T point used the relaxed *requirement* (349 meV) as a placeholder glue. H_020
replaces it with a REAL named material's value and reads out where it actually lands.

## Falsifiers (≥5 — pre-registered)

- **F1_named_trio_reaches_roomT**: PASS = stacked_Tc(3D) ≥ 293 K (EXPECTED FAIL — the honest finding).
- **F2_positive_glue_gap**: PASS = required Ω − 300 > 0 (the glue undershoots).
- **F3_high_tc_coordinate**: PASS = stacked_Tc(3D) > 133 K ambient ceiling.
- **F4_glue_is_electronic**: PASS = 300 meV > 200 meV phonon ceiling.
- **F5_3d_alone_insufficient**: PASS = required Ω(3D) > 300 meV.

## Honest Limits (≥6)

- **L1**: BKT band is an order-of-magnitude estimate (deflated ~2.8× to 3 anchors); 252 K is a coordinate, not a measured T_c (H_018 scatter).
- **L2**: L_3D=1.84 is real but partial; native 3D flat bands are gapless band-touchings (cost not charged).
- **L3**: the ~300 meV is Ta2NiSe5's exciton BINDING energy, not a directly-measured pairing Ω; 1:1 use is a modeling assumption.
- **L4**: the trio is JOINTLY UNREALIZED — interface electron_cost / glue-transmission (H_009/H_011) assumed ideal here, not measured for this trio.
- **L5**: single-channel multiplicative model; competing orders (Ta2NiSe5's own excitonic order, H_014/H_016) not subtracted.
- **L6**: `absorbed=false`; room-T needs accredited 4-probe transport + Meissner + measured H_c2/T_c.

## Cross-Links

- H_007 (combination-order scan — this pins its placeholder glue to a real material) · H_016
  (the room-T amplitude axis it flagged uncleared) · tool/rtsc_candidates.py (the named trio).

## Verdict

**🟡 MODEL-PROBE → CLOSED-NEGATIVE (high-Tc coordinate, not room-T).** Verbatim stdout
(`state/h020_named_candidate_amplitude_2026_06_25/run_h020.py`):

```
=== H_020 named-trio room-T AMPLITUDE verdict — CoSn / hBN(2ML) / Ta2NiSe5 ===
  inputs (verified, NOT tuned): glue Omega = 300.0 meV (Ta2NiSe5),  g_A = 2.87 (CoSn)
  L_3D (real) = 1.84x   phonon ceiling = 200.0 meV   room-T = 293.0 K
  bkt_Tc 2D (no 3D lever)          = 136.8 K
  stacked_Tc 3D (+ L_3D lever)     = 251.6 K   (room-T MISSED)
  Omega required for room-T w/ 3D  = 349.3 meV
  GLUE GAP  (required - available) = 49.3 meV   (41.4 K short of 293 K)
  falsifier F1_named_trio_reaches_roomT   : FAIL
  falsifier F2_positive_glue_gap          : PASS
  falsifier F3_high_tc_coordinate         : PASS
  falsifier F4_glue_is_electronic         : PASS
  falsifier F5_3d_alone_insufficient      : PASS
  falsifiers_pass = 4/5
```

- **structural_finding**: the named trio with Ta2NiSe5's verified ~300 meV glue lands at ~252 K
  (clears the 133 K ambient ceiling) but misses 293 K by ~41 K / ~49 meV-of-glue. A real,
  named, box-clearing stack that is a HIGH-Tc coordinate, NOT an RTSC. The remaining gap is the
  glue scale (300 vs 349 meV) → points the search at a higher-energy clean glue (see the backup
  research: 1T-TiSe2 has 400 meV but a CDW; the q=0 clean hosts are at/below target). absorbed=false.
- **record**: `state/h020_named_candidate_amplitude_2026_06_25/result.json`.
