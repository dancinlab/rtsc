---
id: H_031
slug: clean-spinfluctuation-dual-multilayer
title: Clean spin-fluctuation candidate + DUAL multilayer — swapping the dead Ta2NiSe5 exciton TRAP for a clean spin-fluctuation glue revives the H_023 demand-relaxation path; geometry-multilayer alone reaches the room-T threshold (292.9 K), and stacking the GLUE layers too (user lever) needs only a ~0.03% extra boost to cross 293 K
domain: rtsc
status: model-probe
exploration_method: closed-form harness — clean-glue swap + dual (geometry D_s × glue coupling) multilayer levers
verification_method: W1 (pre-register frozen) + W2 (falsifier-5) + W3 (deterministic, byte-equal x2) + W5 (honest-limits-7)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
compute: closed-form (tool/rtsc_harness.py); no DFT
---

# H_031 — clean spin-fluctuation candidate + dual multilayer (rtsc)

## Hypothesis

The research round killed the Ta2NiSe5 exciton glue (a TRAP — the EI order competes with SC; the
whole EI family is dead, PR#30/#32/#36) and crystallized the law **the FLUCTUATION glues, the ORDER
traps**. The clean spin-fluctuation glue (~300 meV, MEDIATES + COEXISTS with SC; real precedent
TbMn6Sn6/Au interface SC 3.6 K) has the SAME energy as the dead exciton but no trap. **Swapping it
into the H_023 demand-relaxation path revives it.** And the user's lever — just as we stacked the
flat-band (geometry) layers for a D_s boost (f_geom), also stack the GLUE layers for a coupling boost
(f_glue) — adds a SECOND multilayer factor. Test: does the clean candidate reach the room-T
coordinate, and how small a glue-multilayer boost crosses 293 K?

## Why

A kagome MAGNET supplies BOTH the flat-band geometry (∫tr g≈2.86) AND a clean spin-fluctuation glue
in one layer — cleaner than metal+EI. stacked_tc is linear in the boosts, so f_geom and f_glue
multiply: Tc = stacked_tc(Ω,3D) × f_geom × f_glue.

## Falsifiers (≥5 — pre-registered)

- **F1_in_box**: PASS = clean candidate clears the +@ box (g≥2, Ω in band).
- **F2_clean_glue**: PASS = glue is a FLUCTUATION (mediates+coexists), not an order-trap.
- **F3_geom_lever_near_room_t**: PASS = geometry-multilayer alone is within ~5% of room-T.
- **F4_glue_lever_threshold_modest**: PASS = the extra glue-multilayer boost to cross 293 K is <10%.
- **F5_not_green**: PASS = is_green FALSE (f_geom/f_glue are models; spin-fluct ambient-Tc-capped; Tc=coordinate).

## Honest Limits (≥7)

- **L1 (the binding one)**: the BKT band (300 meV → 252 K) is OPTIMISTIC vs reality — measured spin-fluctuation SC (cuprates) caps at ~134 K AMBIENT / ~164 K under pressure, NOT 252 K. The harness coordinate over-reads the clean glue's real ambient ceiling.
- **L2**: f_geom (multilayer D_s) is a MODEL (Peotta-Törmä/Huhtinen, conditional, H_024) that SATURATES at N=1–3 (clean-glue research) — not a free knob.
- **L3**: f_glue (glue-multilayer coupling boost, the user lever) is a MODEL — whether stacking glue layers boosts λ vs saturates is UNVERIFIED (research-first gate; saturation at N=1–3 likely).
- **L4**: Tc is a COORDINATE, not a prediction (H_018 predictor scatter 1061×); ~293 K carries order-of-magnitude uncertainty.
- **L5**: the candidate (kagome magnet + multilayer glue + 3D) is JOINTLY UNREALIZED; the only real datum is TbMn6Sn6/Au at 3.6 K.
- **L6**: a kagome magnet brings its own magnetic order — a competing-order risk (H_014) the closed-form does not subtract here.
- **L7**: absorbed=false; room-T needs accredited 4-probe transport + Meissner + measured H_c2/T_c.

## Cross-Links

- H_023 (the demand-relaxation path this revives) · the clean-glue research (PR#32, spin-fluctuation 🟢) ·
  the EI-family-trap audit (PR#36, why the exciton glue is dead) · H_024 (∫tr g, f_geom bound) · H_018 (Tc scatter).

## Verdict

**🟡 MODEL-PROBE → 🟠 CLEAN-CANDIDATE @ ROOM-T THRESHOLD.** Verbatim stdout
(`state/h031_clean_spinfluctuation_candidate_2026_06_25/run_h031.py`):

```
  stacked_Tc 3D (no multilayer)        = 251.6 K
  + geometry N=2 (f_geom=1.164)        = 292.9 K   (room-T 293K: misses by 0.1K)
  glue-multilayer boost to CROSS room-T = f_glue >= 1.0003  (= 0.03% boost)
    f_glue=1.05 -> Tc = 307.6 K   (room-T: CLEARED)
  falsifiers_pass = 5/5
VERDICT: 🟠 CLEAN-CANDIDATE @ ROOM-T THRESHOLD — kagome-magnet geometry + CLEAN spin-fluctuation glue
  revives the H_023 path the Ta2NiSe5 trap killed; geometry-multilayer alone = 292.9 K; the user's
  SECOND lever (stack the GLUE layers) needs only f_glue>=1.0003 to cross 293K. absorbed=false.
```

- **structural_finding**: the campaign's path SURVIVES the EI-glue death — swapping the clean
  spin-fluctuation glue into H_023 lands at 292.9 K (the room-T threshold) with the geometry-multilayer
  alone, and the user's dual lever (also stacking the glue layers) crosses 293 K with a ~0.03% boost.
  This is the cleanest 🟠 coordinate the campaign has produced. BUT it stands on THREE model assumptions
  (BKT-optimistic-vs-ambient-cap L1, f_geom L2, f_glue L3) and a coordinate-not-prediction caveat (L4).
  The honest gate is now research-first + DFT: **does glue-multilayer actually boost the coupling, or
  saturate?** is_green=False; absorbed=false / GATE_OPEN; no material claimed to BE an RTSC.
- **record**: `state/h031_clean_spinfluctuation_candidate_2026_06_25/result.txt`.
