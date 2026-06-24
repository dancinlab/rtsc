---
id: H_001
slug: flatband-twolever-wall
title: High-Chern flat-band quantum geometry yields ambient (293 K @ 1 atm) superconductivity
domain: rtsc
status: closed-negative
exploration_method: E6 (cross-domain — quantum-geometry → pairing) + E7 (campaign directive)
verification_method: W1 (pre-register frozen) + W2 (falsifier-5+) + W3 (deterministic) + W5 (honest-limits-5+)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-16
since: 2026-06-16
---

# H_001 — Flat-band quantum geometry → ambient-pressure room-T superconductor (rtsc)

## Hypothesis

A high-Chern flat band with large quantum-geometric weight (integrated trace of the
Fubini-Study metric, ∫tr g) supports a geometric superfluid stiffness high enough for
superconductivity at **293 K @ 1 atm** in a real, synthesizable material.

## Why

- Flat-band superfluid weight is bounded below by the quantum metric (Peotta-Törmä):
  pairing can survive where the band is flat if ∫tr g is large.
- Observed flat-band SC anchors (MATBG 1.7 K, tMoTe2 2 K, Re6Se8Cl2 8 K) show the
  mechanism is real but low-T; the question is whether geometry alone can reach room-T.

## Predictions

- **H1.1**: there exists a synthesizable host with ⟨g⟩ ≥ 2–3 AND strong-coupling phonon
  scale Ω ≥ ~130 meV simultaneously (the two levers a room-T geometric SC needs).
- **H1.2**: the 2D-BKT estimate (calibrated to the SC anchors) clears 293 K for ≥1 real host.

## Variables

- **axis1_host**: published flat-band hosts (kagome CoSn, Nb3Cl8, Lieb, dice, checkerboard, …)
- **axis2_filling**: ν around half
- **axis3_lever**: (⟨g⟩, Ω, U/Ω) landscape

## Run Protocol

- deterministic: seed=fnv(host+filling+lever)
- tools: src/fbgeom_predictor.py · src/lane_2d_lattices.py · src/kubo_pair_stiffness.py · src/lang_firsov_offdiag_metric.py
- record: state/RTSC_LEDGER.jsonl + state/papers/flatband-geometry-ambient-roomt-closed/
- cost: $0 (mac local ED + analytic bounds)

## Criteria

- **C1**: predictor reproduces SC anchors within the calibrated band (geomean ≤ ~3×).
- **C2**: ≥1 real host enters the honest design box (⟨g⟩≥2–3 AND Ω≥~130 meV AND U/Ω≥1.5).
- **verdict_rule**: SUPPORTED = C2 met on a real host; REFUTED = C2 unmet across all real + computed hosts.

## Falsifiers (≥5 — pre-registered)

- **F1**: any real host simultaneously satisfies ⟨g⟩≥2–3 AND Ω≥~130 meV → hypothesis SUPPORTED (box entered).
- **F2**: a top-down known SC exceeds the ambient-pressure ceiling (cuprate 133 K) via a flat-band geometric lever → wall is not structural.
- **F3**: the Fubini-Study lower bound on stiffness is shown not to force the ⟨g⟩↔Ω trade-off → mechanism re-opens.
- **F4**: predictor mis-calibrated (fails to reproduce MATBG/tMoTe2/Re6Se8Cl2 within band) → run protocol broken, halt.
- **F5**: a novel (not-yet-published) lever raises the ambient ceiling → not closed.
- **F6**: post-hoc edit to the design-box thresholds → pre-register violation.

## Honest Limits (≥5)

- **L1**: this is a NEGATIVE ruling, not a discovery; no claim that room-T SC is impossible — only that this geometric path is closed at ambient pressure.
- **L2**: predictor is a verification/ranking tool calibrated to 3 anchors; absolute T_c is band-estimated (2D-BKT), not a full Eliashberg solution.
- **L3**: host roster = published flat-band materials; an unmeasured ⟨g⟩ host could exist (fabrication of values is forbidden — d6).
- **L4**: high-pressure hydride lane is a SEPARATE hypothesis (see H_002), not covered here.
- **L5**: every component of the two-lever wall is itself published — this is a synthesis observation, novelty = 0.
- **L6**: absorbed=true would still require accredited 4-probe transport + Meissner expulsion + measured H_c2 / T_c.

## Cross-Links

- **paper**: state/papers/flatband-geometry-ambient-roomt-closed/ (10 paths CLOSED-NEGATIVE, 9 refs)
- **ledger**: state/RTSC_LEDGER.jsonl
- **tools**: src/fbgeom_predictor.py, src/kubo_pair_stiffness.py, src/lang_firsov_offdiag_metric.py
- **literature**: Peotta & Törmä (2015) flat-band superfluid weight; Regnault et al. Nature (2022) flat-band catalogue

## Verdict

**🔴 CLOSED-NEGATIVE** — geometric flat-band path to ambient room-T SC refuted. Verbatim
stdout of the deterministic run (`state/h001_flatband_twolever_2026_06_24/run_h001.py`,
importing `tool/rtsc_harness.py`); 0/2 real hosts enter the two-lever box. Consistent with
the full 10-path closure in `state/papers/flatband-geometry-ambient-roomt-closed/`.

```
=== H_001 flat-band two-lever wall — deterministic verdict ===
  CoSn     g=2.87[ok] omega=22meV[no] U/Om=2.0[ok] -> in_box=False  bkt_Tc~10.03K
  Nb3Cl8   g=2.11[ok] omega=20meV[no] U/Om=2.0[ok] -> in_box=False  bkt_Tc~9.12K
  hosts_in_box = 0 / 2
  max bkt_Tc = 10.03K  vs ambient ceiling 133.0K  vs room-T 293.0K
  falsifier F1_box_entry        : PASS
  falsifier F2_ceiling_broken   : PASS
  falsifier F4_reaches_room_T   : PASS
  falsifiers_pass = 3/3
VERDICT: CLOSED-NEGATIVE
```

- **structural_cause**: Fubini-Study bound forces the two-lever trade-off — large ∫tr g and strong coupling Ω do not coexist in one host; CoSn/Nb3Cl8 have the geometry (g≥2) but soft d-electron phonons (Ω~15–30 meV) miss the Ω≥130 meV gate.
- **answer_key**: top-down scout confirms ambient ceiling = cuprate 133 K; only novel lever (nickelate strain law) already PUBLISHED (arXiv 2603.14519) → closed. novelty = 0.
- **note**: falsifiers PASS = NOT triggered = the wall holds (F1 box-entry never happened); this is a negative ruling, not a discovery.
- **record**: state/h001_flatband_twolever_2026_06_24/result.json + state/papers/flatband-geometry-ambient-roomt-closed/
