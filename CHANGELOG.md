# Changelog

All notable changes to rtsc are recorded here (append-only).

## Unreleased

- Add **UNIVERSE hypothesis-verification system** (modeled on anima's `UNIVERSE/`, same
  convention as the lumen sibling): `UNIVERSE/HYPOTHESES.jsonl` registry +
  `UNIVERSE/cards/H_*.md` (frozen pre-registration + ≥5 measurable falsifiers + honest
  limits + verbatim verdict) + `cards/_TEMPLATE.md`. Shared deterministic stdlib-only
  harness in repo-root **`tool/rtsc_harness.py`** (two_lever_box_check, geometric_bkt_tc_band,
  allen_dynes_tc, Falsifier/evaluate — API-compatible with lumen `tool/lumen_optics.py`);
  heavy compute stays in `src/`. Seeded two real campaign cards: **H_001 flat-band
  two-lever wall** run to verdict (`state/h001_flatband_twolever_2026_06_24/run_h001.py`
  → **CLOSED-NEGATIVE**, 0/2 hosts enter the box, verbatim stdout) and **H_002 ambient
  superhydride stability** (**INCONCLUSIVE**, deferred). Added `verification` node to
  ARCHITECTURE.json + folder guides for `UNIVERSE/` and `tool/`.


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
