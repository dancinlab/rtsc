# Changelog

All notable changes to rtsc are recorded here (append-only).

## Unreleased

- **Research note — classifying the excitonic-SC "electronic-glue graveyard" wall (🟠 MATERIALS-LIMITED)**
  (read-only literature survey, `state/research-excitonic-sc-wall-classification-2026-06-25.md`). The prior
  cRPA note (PR #7) moved the +@ trilayer binding wall upstream to a MATERIALS question — does a real "glue
  layer B" exist? — which sits on the historical excitonic/electronic-glue SC graveyard (Allender–Bray–
  Bardeen 1973 → Miller–Strongin 1976 negative). Per break-walls discipline, classified the wall:
  **🟠 MATERIALS-LIMITED.** (Q1) **No no-go theorem** — the dielectric-stability bound that capped Tc is a
  *restrictive assumption, not a prohibition*; Krotov–Suslov (arXiv:cond-mat/9912180) prove the 1970s
  Ginzburg-sandwich null follows from film-thickness ≫ interatomic-spacing *geometry dilution*, removable by
  engineering. (Q2) **The mechanism is a live, computed modern frontier** — interlayer plasmon SC up to an
  order-of-magnitude enhancement (in 't Veld–Katsnelson–Millis–Rösner arXiv:2508.06195), exciton-density-wave
  -fluctuation SC (Kumar–Patri–Senthil arXiv:2410.09148), electron-exciton-coupling Tc up to ~10% of T_F in
  TMD heterostructures (von Milczewski–Imamoğlu–Schmidt arXiv:2310.10726). (Q3) **But NO concrete, named,
  de-risked "glue layer B" exists today** with the required trio: 0.1–0.5 eV bosonic mode + demonstrated
  cross-spacer coupling to a flat band + clean absence of a pre-empting CDW/SDW — and in Kumar–Senthil the
  density wave *is* the mechanism's host, so the competing-order risk is intrinsic. No experiment has ever
  measured a meaningful Tc from a purely bosonic electronic glue, let alone 293 K. **Verdict: a 60-year
  graveyard with no tombstone (no no-go) and no birth certificate (no material) — materials-limited, with a
  genuinely reopening theory frontier behind it.** Not a positive for the campaign; `absorbed=false` /
  GATE_OPEN unchanged.

- **Research note — cRPA glue-transparency go/no-go (NO-GO on renting GPU)** (read-only literature
  survey, `state/research-crpa-glue-transparency-2026-06-25.md`). Before spending GPU on a
  constrained-RPA calc of H_011's "bosonic glue penetrates the electron-opaque hBN spacer" claim,
  surveyed the real literature (arXiv + Crossref-verified DOIs). **Verdict (a)+(b): NO-GO.** (a) The
  literature already answers the qualitative question — interlayer **Coulomb drag** and **exciton
  condensates** are *measured* to couple two electronic layers across hBN spacers up to **~2.5 nm
  (~8 ML)** by pure Coulomb interaction (Hao–Kim arXiv:2508.09098; Liu–Kim arXiv:1608.03726), while
  single-electron DOS dies by the first ML (our H_015). The pairing version (interlayer
  plasmon/exciton-mediated SC) is already computed (in 't Veld–Rösner arXiv:2508.06195 / 2303.06220;
  Kumar–Senthil arXiv:2410.09148). **Most important number:** out-of-plane static screening of 1–3 ML
  hBN is only **ε⊥ ≈ 3.29→3.6** (Laturia *npj 2D Mater.* 2018, DOI 10.1038/s41699-018-0050-x) — the
  interlayer field is attenuated **~3–4×, not exponentially killed.** (b) A **$0 Keldysh + RPA-W
  proxy on summer** covers what's left. (c) A real cRPA campaign is **not justified now**, and is
  mostly **CPU (RESPACK), not GPU** — GPU (Yambo/BerkeleyGW GW-BSE) only buys the exciton-dipole
  tier, a 2nd-order question behind the still-open upstream "does a real flat-band A + ~349 meV glue
  B without competing order exist?" (H_004/H_011 L2). Honest counterweight: the 1973 Allender–Bray–
  Bardeen exciton-glue proposal (DOI 10.1103/PhysRevB.7.1020) got a **negative 1976 experimental
  verdict** (Miller–Strongin, DOI 10.1103/PhysRevB.13.4834) — the field couples, but a useful Tc is
  exactly where the historical program failed. `absorbed=false`, unaffected.

- **H_015 — first REAL ab-initio DFT verdict for the +@ trilayer (electron-opacity half)**
  (`🟢 REAL-DFT`, summer pool). Promoted the H_009/H_011 closed-form decay-length opacity knob to
  a real finite-cell test: a **graphene / hBN(n) / graphene** heterostructure (the clean lattice-
  matched proxy for metal/spacer/metal), n = 0,1,2,3, built with a stdlib deck generator (ASE not
  on summer). Method: **Quantum ESPRESSO pw.x v7.2**, PBE + **Grimme-D3** vdW, 50/400 Ry,
  **12×12×1** k-mesh, `{C,B,N}.pbe-n-kjpaw_psl.0.1` PAW pseudos; common in-plane **a = 2.48 Å**
  (graphene 2.461 Å, hBN 2.504 Å — **1.75 % mismatch recorded honestly**), d = 3.35 Å, 14 Å vacuum.
  **Toolchain block resolved honestly:** the host's apt `pw.x v6.7MaX` aborts on EVERY input with a
  glibc `__snprintf_chk` *"buffer overflow detected"* (fortify packaging bug, independent of
  input/pseudo/vdW/MPI) — so QE 7.2 was **built from source** on summer (system BLAS/LAPACK/FFTW,
  serial gfortran); the same deck then runs clean (`JOB DONE.`). All 4 SCF converged.
  **Result (`projwfc` Löwdin + pz PDOS):** the hBN spacer suppresses interlayer electronic coupling
  — the **graphene Dirac-point residual pz DOS drops 7.7×** from direct contact (n0 = 0.0472) to one
  hBN layer (n1 = 0.0061), then **plateaus** at the isolated-graphene floor (n2/n3 ≈ 0.0053); the
  **hBN spacer-interior pz DOS at E_F per atom decays monotonically** (0.00249 → 0.00160 → 0.00108);
  the two graphene layers stay charge-symmetric (|imbalance| = 0.0000 e). **4/4 falsifiers.**
  **Scope (L1):** this verifies the +@ **electron-opacity half ONLY** — the glue-transparent /
  bosonic-field cross-spacer coupling (H_011) remains a separate, harder cRPA campaign.
  `absorbed=false`. Artifacts under `state/h015_trilayer_dft_electron_opacity_2026_06_25/`.

- **Fleet — 3 verification lanes** (`/fleet`, via Workflow; each lane wrote+ran a deterministic
  probe, all re-verified by the main loop). **H_016 competing-order ESCAPE** (break-walls vs H_014):
  sweeping the frustration knob eta_nest 0.85->0.10 flips the SDW-vs-SC race at a critical eta*=0.45
  (above the pre-registered plausibility floor 0.30) -> competing order is a REMOVABLE wall (frustrate
  the kagome/triangular host), not robust (5/5) — but the room-T AMPLITUDE axis stays uncleared
  (relaxed room-T U=0.543 < SC threshold 2.22). **H_017 disorder flat-band** (seed O2): the same
  disorder that flattens the band to >=2x DOS Anderson-localizes carriers below the Cooper-pair length
  (xi_loc=0.55*xi_0 at the flat onset) -> flat-and-delocalized window EMPTY, O2 CLOSES (0/5;
  escape = 3D mobility edge / BEC-side pair, untested). **H_018 adversarial predictor check** (the
  campaign's self-audit): geometric_bkt_tc_band vs 8 held-out real SCs (tTLG, RTG, CsV3Sb5, MgB2, Pb,
  YBCO...) -> gets the AVERAGE right (geomean 1.86x, bias +0.27dex, 50% within 3x, monotonic, 4/5 PASS)
  but FAILS per-material SCATTER (1061x spread vs 6.8x in-sample) -> the central Tc estimator is a fair
  order-of-magnitude average, NOT a reliable per-material predictor; every room-T Tc number carries
  ~order-of-magnitude uncertainty (read as coordinates). The wall/closed-negative findings (gates,
  leading-channel races) are NOT affected. Registry 17 rows (H_015 trilayer-DFT lane still in-flight on
  summer). Net: one wall removed (H_016), one mechanism closed (H_017), and the campaign's own predictor
  honestly down-weighted (H_018).

- **Fleet — 3 parallel orthogonal-lever lanes** (`/fleet`, via Workflow; each lane wrote +
  ran a self-contained deterministic probe, all re-verified by the main loop). The remaining
  brainstorm +@ levers are NOT free wins: **H_012 topology gap** (B7) → 🟡 CLOSED-NEGATIVE
  (collapse): a protected gap is a pairing-AMPLITUDE lever, but the room-T stack is phase-
  STIFFNESS-limited, so it never relaxes the 349 meV demand and the only stiffness it adds = the
  FS quantum metric = the H_001 geometry lever — NOT a 5th orthogonal axis (4/5). **H_013
  fractionalization** (S5) → 🟡 BOX-OPENS-BUT-NEW-BILL: sector-split genuinely evades the
  single-electron FS tie but only above an exotic ~800 meV deconfinement gap and only to ~77 K
  (6/6). **H_014 competing-order** (the dominant risk, H_004 L2 / H_011 L3) → 🟡 CLOSED-NEGATIVE:
  under a toy Stoner/RPA multi-channel model the room-T glue drives **SDW (U*=1.0) before SC
  (U*=2.22)** — no SC-leading window; the +@ architecture's biggest assumed risk is realized
  (0/5; conditional on toy nesting η=0.85 → a measured THREAT escapable by suppressing nesting,
  not a terminal ceiling). Net: topology collapses, fractionalization relocates, competing-order
  pre-empts — the closed-form orthogonal-lever search is rigorously DEPLETED (break-walls), and
  the binding open question is now **competing order** + the real DFT verdict. Registry 14 rows.
  Real DFT trilayer lane (cost-gated) dispatched to a rented runpod CPU pod (user `go`).

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
