---
id: H_022
slug: frustration-unlock
title: Frustration-unlock confluence — IF 1T-TiSe2's CDW is suppressed (H_016, η_nest<0.45) AND its ~400 meV exciton survives, the trio CoSn/hBN/1T-TiSe2 clears room-T amplitude (335.5 K) AND is SC-leading; a 🟠-CONDITIONAL candidate whose single remaining unknown is the coexistence — which the research lanes then CLOSED
domain: rtsc
status: conditional
exploration_method: confluence — pin H_020's missing AMPLITUDE axis and H_016's competing-order ESCAPE onto ONE host (1T-TiSe2)
verification_method: W1 (pre-register frozen) + W2 (falsifier-6 incl. honesty-gate F6) + W3 (deterministic) + W5 (honest-limits-6)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
compute: fleet lane (🟢-conditional confluence)
---

# H_022 — frustration-unlock confluence (rtsc)

## Hypothesis

Two 🟢-blockers lived on separate cards: H_020 (the named Ta2NiSe5 trio MISSES room-T, ~252 K,
glue only ~300 meV) and H_016 (the competing-order wall is REMOVABLE by frustration, η_nest*≈0.45).
1T-TiSe2 is the ONE surveyed host that could close BOTH: a ~400 meV exciton (the only surveyed boson
ABOVE the 349 meV room-T demand) AND an intrinsic CDW (exactly H_016's target). **Hypothesis: IF
the CDW is suppressed by frustration (η<0.45) WHILE the ~400 meV exciton survives, the trio
CoSn/hBN/1T-TiSe2 reaches room-T amplitude AND is SC-leading.** Verdict must stay CONDITIONAL — the
coexistence in a REAL material is the single unverified variable.

## Falsifiers (≥6 — pre-registered)

- **F1_amplitude_clears_roomT**: PASS = stacked_tc(400,3D) ≥ 293 K.
- **F2_glue_margin_positive**: PASS = 400 − 349.3 > 0 (exciton over-clears the demand).
- **F3_sc_leads_when_frustrated**: PASS = at η=0.35, U_sc < min(U_sdw,U_cdw,U_ps).
- **F4_sc_beats_cdw**: PASS = U_sc < U_cdw (SC pre-empts 1T-TiSe2's NAMED competing order).
- **F5_control_sc_subleading_commensurate**: PASS = at η=0.85 SC does NOT lead (unlock is from frustration).
- **F6_honesty_gate_not_green**: PASS = is_green=False (coexistence unverified → 🟠, never 🟢 by construction).

## Honest Limits (≥6)

- **L1**: amplitude uses the calibrated BKT coordinate × the real 3D lever; 335 K is a coordinate (H_018 scatter), not a measured T_c.
- **L2**: the leading-channel race is the H_016 toy Stoner/RPA (linear, single-χ); a full Lindhard/DMFT could move η*.
- **L3**: 1T-TiSe2's ~400 meV is the upper excitonic optical mode; its 1:1 use as the pairing Ω is a modeling assumption.
- **L4 (the binding one)**: the unlock assumes CDW-suppression AND a surviving 400 meV exciton COEXIST — **the research lanes (state/research-tise2-cdw-suppression-2026-06-25.md) then showed they do NOT** in 1T-TiSe2: Cu/pressure/strain all kill the CDW by killing the exciton (the exciton IS the excitonic-CDW). So this confluence is a sharp NEGATIVE hand-off, not a path.
- **L5**: single-channel multiplicative model; the trio is jointly unrealized.
- **L6**: absorbed=false; room-T needs accredited transport + Meissner + measured H_c2/T_c.

## Cross-Links

- H_020 (amplitude axis) · H_016 (competing-order escape) · H_014 (the wall) · the CDW-suppression
  research note (which closed the coexistence) · tool/rtsc_candidates.py.

## Verdict

**🟡 MODEL-PROBE → 🟠 CONDITIONAL (named-unlock), coexistence subsequently CLOSED by research.**
Verbatim stdout (`state/h022_frustration_unlock_2026_06_25/run_h022.py`):

```
PART (a) amplitude: stacked_tc(400 meV, 3D) = 335.5 K >= 293 K (room-T CLEARED, +50.7 meV margin over 349.3)
PART (b) leading channel (H_016 Stoner/RPA):
  eta_nest=0.35 (frustrated): U_sc=2.222 < U_sdw=2.857, U_cdw=7.143, U_ps -> SC LEADS
  eta_nest=0.85 (commensurate control): SDW leads at 1.177 -> SC sub-leading (unlock is from frustration)
  is_green = False  (coexistence unverified)
  F1..F6 : PASS  (6/6)
VERDICT: 🟠 CONDITIONAL — room-T-clearing + SC-leading IF CDW-suppression and the 400 meV exciton coexist
```

- **structural_finding**: a genuine CONFLUENCE — both model blockers (amplitude + competing-order)
  pass at once on 1T-TiSe2, converting "no 🟢" into ONE named, single-variable question (does
  CDW-suppression + surviving 400 meV exciton coexist?). The research lanes then answered NO for
  1T-TiSe2 (the exciton IS the CDW; every suppression route kills it) — so this is the sharp,
  honest pivot that closes the 1T-TiSe2 🟢-path. Not 🟢; absorbed=false; GATE_OPEN.
- **record**: `state/h022_frustration_unlock_2026_06_25/result.json`.
