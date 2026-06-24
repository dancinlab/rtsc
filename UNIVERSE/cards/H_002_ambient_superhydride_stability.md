---
id: H_002
slug: ambient-superhydride-stability
title: A light-element superhydride is dynamically stable AND superconducting at 293 K @ 1 atm
domain: rtsc
status: inconclusive
exploration_method: E2 (hydride-class screen) + E6 (QFORGE from-scratch el-ph)
verification_method: W1 (pre-register frozen) + W2 (falsifier-5+) + W3 (deterministic) + W5 (honest-limits-5+)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-16
since: 2026-06-15
---

# H_002 — Ambient-pressure superhydride: dynamically stable + superconducting (rtsc)

## Hypothesis

There exists a light-element superhydride that is **dynamically stable at 1 atm**
(no soft/imaginary phonon modes) AND superconducting near **293 K**, removing the
megabar-pressure requirement of H3S/LaH10-class hydrides.

## Why

- High-pressure hydrides reach high T_c (H3S ~200 GPa, LaH10) via strong H-network
  el-ph coupling; the open question is whether any composition keeps that coupling
  while staying dynamically stable at ambient pressure.
- Candidates from the screen: Li2CuH6, Mg2IrH6, AcBeH8, B–C clathrates.

## Predictions

- **H2.1**: ≥1 candidate has all-real phonons at 1 atm (vc-relax converged, no imaginary modes).
- **H2.2**: that candidate's Allen-Dynes / Eliashberg T_c (μ*=0.10–0.13) ≥ 273 K at 1 atm.

## Variables

- **axis1_material**: [Li2CuH6, Mg2IrH6, AcBeH8, LaB3C3, CaB3C3, …]
- **axis2_pressure_GPa**: [0–1 atm regime]

## Run Protocol

- deterministic: per-material QE/QFORGE chain (vc-relax → scf → ph → el-ph → Tc)
- tools: src/build_deck.py + QFORGE engine (SCF→DFPT→el-ph→Tc)
- record: state/exports/<material>/*_ambient_stability_verdict.json + state/RTSC_LEDGER.jsonl
- cost: cloud pods (per-material, deprioritized after flat-band pivot)

## Criteria

- **C1**: vc-relax converges at 1 atm.
- **C2**: phonon spectrum all-real (dynamic stability).
- **C3**: T_c(μ*) ≥ 273 K.
- **verdict_rule**: SUPPORTED = C1+C2+C3; INCONCLUSIVE = C1 unmet (non-converged); REFUTED = C2 fails (imaginary modes) for all.

## Falsifiers (≥5 — pre-registered)

- **F1**: every candidate shows imaginary phonon modes at 1 atm → ambient superhydride REFUTED for this set.
- **F2**: vc-relax fails to converge for all → INCONCLUSIVE (infrastructure, not physics) — keep, do not delete.
- **F3**: stable candidate has T_c(μ*) < 273 K → H2.2 FALSIFIED (stable but not room-T).
- **F4**: el-ph engine fails Al/Nb/Pb cross-validation → run protocol broken, halt.
- **F5**: any candidate already published as ambient RTSC → novelty 0, defer to literature.
- **F6**: post-hoc edit to stability/T_c thresholds → pre-register violation.

## Honest Limits (≥5)

- **L1**: 2×2×2 coarse-q can hide soft modes — 4×4×4 needed before a stability claim is firm.
- **L2**: Li2CuH6 / Mg2IrH6 already read ambient-dynamically-unstable; AcBeH8 / B–C clathrates still inconclusive (vc-relax non-converged, pods down, deferred).
- **L3**: synthesis (DAC, crystal growth) is outside this map — a computed stable structure is not a made one.
- **L4**: μ* range {0.10, 0.13} is the usual Allen-Dynes window; a wider μ* shifts T_c.
- **L5**: deferred runs are kept in the ledger (d_defer_no_delete), not deleted.
- **L6**: absorbed=true would still require accredited 4-probe transport + Meissner + measured H_c2 / T_c.

## Cross-Links

- **ledger**: state/RTSC_LEDGER.jsonl (H3S, LaH10, CaH6, Li2CuH6, Mg2IrH6, AcBeH8 rows)
- **verdicts**: state/exports/li2cuh6_ambient_stability_verdict.json, mg2irh6_…, AcBeH8_…, LaB3C3_…, CaB3C3_…
- **tools**: src/build_deck.py
- **literature**: Drozdov et al. (2015) H3S; Snider et al. / LaH10 hydride SC line

## Verdict

**🟠 INCONCLUSIVE** — no candidate has cleared all three criteria at 1 atm; the lane is deferred (not refuted, not supported).

```
verdict_class: INCONCLUSIVE
criteria:
  - C1 (vc-relax converge @1atm): PARTIAL — Li2CuH6/Mg2IrH6 ran; AcBeH8 / B–C clathrates non-converged (pods down)
  - C2 (all-real phonons):        FAIL for Li2CuH6, Mg2IrH6 (ambient-dynamically-unstable); UNKNOWN for AcBeH8 / clathrates
  - C3 (T_c ≥ 273 K @1atm):        not reached (no ambient-stable candidate to evaluate)
falsifiers_triggered: F1 partial (2/5 candidates show instability), F2 partial (clathrate vc-relax non-converged)
status: deferred per d_defer_no_delete — high-pressure hydrides deprioritized after the flat-band pivot
record: state/RTSC_LEDGER.jsonl
```
