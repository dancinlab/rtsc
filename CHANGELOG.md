# Changelog

All notable changes to rtsc are recorded here (append-only).

## Unreleased

- **+@ deepening: real verdicts + 3-combination** (user: "explore 3-combinations too" + "summer pool").
  Three more cards, two backed by REAL computation (not closed-form):
  **H_006 real-3D verdict** — ran `src/fbgeom_3d.py` (mac local numpy) on real 3D flat-band hosts:
  the 3D Tc lever **L_3D=1.84×** (BKT-vortex 1.50 × coordination 1.22) is real but PARTIAL (~21% of
  the ~5× gap); native 3D flat bands (pyrochlore/hyperkagome/3D-Lieb) are gapless band-touchings →
  geometry contaminated, the clean dimension-FRAME bypass is BLOCKED (additive lever, not wall-removal).
  **H_007 combination-order scan** — a 3-lever stack (geometry × electronic glue × real 3D lever)
  reaches room-T by **relaxing the glue demand 642.7→349.3 meV (1.84×)**; Tc by order 10→159→293 K
  (1<2<3 monotone), each lever necessary by ablation (5/5, deterministic). 3-combination beats
  2-combination by *dividing* the deficit, not adding Tc. **H_008 real bipolaron ED** — dispatched
  the decisive sign-free 2e+phonon ED (`src/lane_a_explicit_phonon_bipolaron_ed.py`) to the shared
  **pool host `summer`** (scipy sparse eigsh, dim up to 562500): the retarded explicit-phonon vertex
  makes pair-channel ⟨g⟩_pair **EXCEED** the single-particle Peotta-Törmä value (0.822 vs 0.192,
  **4.27×**) in the anti-adiabatic weak-coupling corner — the static mean-field had *closed* this
  crack; the retarded vertex *reopens* it (corner-confined; strong-coupling ratio collapses to
  0.08–0.78). Added `THREED_TC_LEVER`, `stacked_tc`, `omega_for_stacked_tc` to `tool/rtsc_harness.py`.
  Real verdicts preserved in `state/h006…/fbgeom_3d_real.out` and `state/h008…/lane_a_summer.out`.
  Two more cards from user directives — **H_009 connector spacer** ("use a 3rd material to join the
  2"): the interface becomes a trilayer A/C/B where C is an engineered spacer; a wide-gap/phonon-
  matched spacer (hBN-class) opens a fabricable window [0.44, 1.78 ML] that is both electron-opaque
  (cost ≤ 0.415) AND phonon-transparent (T ≥ 0.70), a non-selective spacer none (4/4) — promotes
  H_003's abstract interface knob to a real material lever. **H_010 top-down lever-count scan**
  ("we're bottom-up; come down top-down on the count, might discover something"): stripping the full
  {geometry, connector, glue, 3D} stack shows the full-4 glue demand (349 meV) is achievable (sub-eV)
  but every removal is not — drop-3D → 643 meV (unachievable), drop-connector → wall (structural).
  Minimal **achievable** count = 4: **more levers is the mechanism for achievability, not redundancy**
  (the deficit is distributed so each lever's demand becomes material-reachable) — inverting the
  "fewer parts is better" intuition (4/4). Added `THREED_TC_LEVER`, `stacked_tc`, `omega_for_stacked_tc`,
  `spacer_window`/`spacer_electron_cost`/`spacer_phonon_transmission` to `tool/rtsc_harness.py`.
  **H_011 the +@ crux** (internal-consistency check) — does the electron-opaque connector block
  the electronic glue too (self-contradiction)? No: a **bosonic** (exciton/plasmon) glue couples
  via its long-range Coulomb field (λ_Coulomb=8 ≫ λ_e=0.5 ML) and penetrates the barrier (window
  [0.44, 2.85 ML], wider than the phonon window; Förster/Coulomb-drag-like), while a **fermionic**
  transfer glue is blocked (4/4). The whole closed-form +@ chain collapses to ONE open materials
  requirement: **a bosonic, field-coupled, ~349 meV glue without competing order**. Registry now
  11 rows (🔴1 🟠1 🟡7 🟢2). Closed-form +@ architecture deepening DEPLETED — the remaining
  frontier is the real DFT/cRPA trilayer verdict (deferred, ING).

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
