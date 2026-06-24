# Changelog

All notable changes to rtsc are recorded here (append-only).

## Unreleased

- **+@ combination wall-breakthrough + deepening to depletion** (goal: "+@ 조합 벽돌파 및 돌파
  후 심화 고갈까지"). Three frozen MODEL-PROBE cards stack the brainstorm SPLIT/BORROW seeds to
  bypass the single-host two-lever wall (H_001):
  **H_003 +@ bilayer division-of-labor** (M1 SPLIT / seed B2) — geometry in layer A (CoSn g=2.87),
  stiff glue proximity-imported from layer B → the bilayer enters the box no single host can
  (η*=0.73, Ω_eff=130 meV) but only via a phonon-transparent/electron-opaque interface
  (critical electron_cost=0.415) and only to bkt_Tc~59 K → **the SPLIT relocates the wall into an
  interface criterion, does not remove it** (6/6 falsifiers PASS). **H_004 glue-reservoir ceiling**
  (M3 BORROW / seed B3) — room-T via the box needs Ω~643 meV, above the phonon ceiling (200 meV →
  91 K); only an electronic eV-class reservoir can supply it (5/5 PASS). **H_005 combination capstone**
  — the full stack (geometry × electronic glue × ideal interface) reaches **bkt_Tc~319 K (room-T
  CLEARED in the toy band)** with **each lever necessary** (ablate glue→91 K, ablate geometry→box
  closes, ablate interface→box closes; 5/5 PASS). Honest endpoint: the breakthrough is a
  **FACTORIZATION** — the room-T wall becomes the conjunction of (a) an electron-opaque interface +
  (b) a competing-order-free electronic glue, two stacked *real, unsolved* materials sub-problems;
  closed-form deepening is **DEPLETED**, the real verdict needs a DFT/DFPT/el-ph heterostructure calc
  (`src/` + cloud pod). Added `proximity_bilayer_levers`, `critical_electron_cost`, `omega_for_bkt_tc`,
  `PHONON_CEILING_MEV` to `tool/rtsc_harness.py`; all runs deterministic (byte-equal). Registry +
  ARCHITECTURE verification node updated.

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
