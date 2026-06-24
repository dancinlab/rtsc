# Changelog

All notable changes to rtsc are recorded here (append-only).

## Unreleased

- Promote SF-brainstorm seed F2 to a real frozen card: **H_006 FS-bound dimension-invariance**.
  Added a deterministic quantum-metric dimension scan to `tool/rtsc_harness.py`
  (quantum_metric_trace_separable + quantum_metric_trace_2d_dirac, stdlib-only BZ finite-difference
  of the gauge-invariant 2-level FS metric). Ran `state/h006_fs_dimension_scan_2026_06_24/run_h006.py`
  → **MODEL-PROBE: DIMENSION-EXTENSIVE** (⟨tr g⟩ = 0.25·d, growth ratio d3/d1 = 3.0), refuting the
  dimension-invariance hypothesis AT TOY LEVEL → the dimension-FRAME bypass is not closed. Honestly
  scoped: toy 2-level model computing the geometry lever only (Ω not tested); real verdict needs 3D
  flat-band ED (src/, pod). Registry + ARCHITECTURE verification.cards updated.


- Add **HYPOTHESES hypothesis-verification system** (modeled on anima's `UNIVERSE/`, same
  convention as the lumen sibling): `HYPOTHESES/HYPOTHESES.jsonl` registry +
  `HYPOTHESES/cards/H_*.md` (frozen pre-registration + ≥5 measurable falsifiers + honest
  limits + verbatim verdict) + `cards/_TEMPLATE.md`. Shared deterministic stdlib-only
  harness in repo-root **`tool/rtsc_harness.py`** (two_lever_box_check, geometric_bkt_tc_band,
  allen_dynes_tc, Falsifier/evaluate — API-compatible with lumen `tool/lumen_optics.py`);
  heavy compute stays in `src/`. Seeded two real campaign cards: **H_001 flat-band
  two-lever wall** run to verdict (`state/h001_flatband_twolever_2026_06_24/run_h001.py`
  → **CLOSED-NEGATIVE**, 0/2 hosts enter the box, verbatim stdout) and **H_002 ambient
  superhydride stability** (**INCONCLUSIVE**, deferred). Added `verification` node to
  ARCHITECTURE.json + folder guides for `HYPOTHESES/` and `tool/`.


- Scaffold the `rtsc` project as the dedicated home for the room-temperature
  superconductor campaign (same layout as the `lumen` sibling): `src/` + `state/`,
  `ARCHITECTURE.json` (JSON `children` tree) + `architecture.html` viewer + `serve.py`,
  CHANGELOG/CLAUDE docs. Carried existing progress materials over from the demiurge
  repo (copied, non-destructive — demiurge originals preserved):
  - `src/` ← demiurge `tool/rtsc/` (29 predictor / screening / ED-solver tools).
  - `state/RTSC_LEDGER.jsonl` + `RTSC_HARVEST_PARTIAL.jsonl` (campaign ledger SSOT).
  - `state/rtsc.demi` (7-verb pipeline manifest).
  - `state/exports/` ← demiurge `exports/rtsc/` minus the 568 MB `Li2MgH16`
    staging tarball (regenerable compute output, excluded).
  - `state/campaign/` ← demiurge `state/rtsc-*` campaign sub-states.
  - `state/papers/` ← the four RTSC papers (incl. the closed-negative flat-band paper).
