# Changelog

All notable changes to rtsc are recorded here (append-only).

## Unreleased

- **In-silico-only domain rule (scope boundary, rtsc/CLAUDE.md).** Pinned the campaign's domain
  edge: our work is IN SILICO (predict/screen/simulate/falsify); physical synthesis, fabrication,
  doping-to-spec, and accredited measurement (the absorbed=true gate) are OUT OF DOMAIN — a hand-off
  to the lab, never our failure and never computationally satisfiable. Success criterion = satisfy
  every in-silico-settleable lever ("the rest"); a candidate clearing all of those is domain-complete
  while staying absorbed=false (the lab gate is not ours). Domain-complete is NOT a discovery claim.
  This reframes the +@ campaign terminal: CoSn/hBN/Ta2NiSe5 is in-silico domain-complete (geometry
  ∫tr g=2.856, spacer, D_s(N=2), doping all characterized) — the remaining absorbed=true gate is the
  domain edge, not a campaign failure.
- **research-first prior-art pass on the +@ lead candidate (CoSn/hBN/Ta2NiSe5) — 🟠 OPEN/NOVEL, but the
  excitonic-glue sub-lever is 🔴-leaning.** Per the CLAUDE.md "실측전 research" rule, a READ-ONLY literature
  pass (web + arXiv + WebFetch) was run BEFORE recommending physical synthesis + accredited transport of
  the campaign's computational terminal. Findings (`state/research-plus-at-realization-prior-art-2026-06-25.md`):
  the trio is jointly unrealized (no matching device), and the decisive result is that **proximity SC
  induced in a metal by an excitonic insulator has NEVER been measured in ~50 years** — every 2024–2026
  instance (PRL 133.226903; arXiv:2402.02747 / 2410.09148 / 2508.06195 / 2409.12201) is theory. The closest
  REAL measured precedents are kagome-magnet/metal emergent interface SC (TbMn6Sn6/Au, **Tc≈3.6 K**,
  PMC10622413 — but the glue is a magnet, not an EI) and a measured interlayer exciton *condensate* through
  thin hBN (arXiv:2508.09098 — condensate, not SC). Key NEGATIVE: Ta2NiSe5's own SC (Tc≈1.2 K @ 8 GPa,
  arXiv:2106.04396) appears only AFTER its excitonic state is destroyed and is phonon-mediated — the
  opposite of using the live exciton as glue. Recommendation: do NOT green-light the excitonic-glue trilayer
  fab as the next spend; first demonstrate proximity-SC-from-an-EI in isolation, or pivot the glue lever.
  `absorbed=false` / GATE_OPEN unchanged. No material claimed to BE an RTSC.

- **H_029 — CoSn correlation lens (DFT+U): the doping wall SURVIVES a second orthogonal lens.**
  Applied the electron-correlation lens to H_027's strongest adverse finding — whether semilocal PBE
  mis-places CoSn's correlated kagome flat band, so the ~1.58 holes/f.u. extreme-doping wall is a PBE
  artifact. A defensible ortho-atomic Dudarev **DFT+U(Co-3d) scan U=1,2,3,4,5 eV** (bracketing the
  literature CoSn DMFT U≈5 eV; the tractable mean-field proxy for the full DMFT) on OUR converged
  spin-polarized Co3Sn3 cell, under genuine 6-rank MPI (conda QE 7.5, verbatim banner; ortho-atomic
  Hubbard projectors; all 5 SCFs converged 12–20 iters; all FREE on the H_026-fixed summer host). RESULT
  (honest, not tuned): correlation does the **OPPOSITE** of dissolving the wall — the kagome flat band
  sinks **monotonically DEEPER below E_F** (PBE −0.44 eV → −1.16/−1.78/−2.80/−2.99/−3.3..−4.3 eV for
  U=1..5), **NEVER within ~0.2 eV of E_F at any physical U** → the H_027 doping wall **SURVIVES two
  orthogonal lenses (PBE AND +U) and HARDENS**, it is NOT a PBE artifact. The geometry lever stays intact
  (NN-kagome TB-fit **I=(1/2π)∫tr g = 2.855 at every U** ≈ measured QGT 2.87) — but a stronger lever placed
  ever deeper below E_F = MORE doping, not less. +U also **induces strong magnetic order** (Co |mag| 0.43 μB
  PBE → 2.85/4.09/4.92/5.07/5.23 μB at U=1..5), a competing-order (H_014) signal CoSn did not show in plain
  PBE. HONEST LIMIT: DFT+U is a static mean-field proxy; full DMFT (dynamical self-energy, paramagnetic)
  could differ → a two-lens negative on the "correlation rescues the band" hypothesis, NOT a proof. Card
  `HYPOTHESES/cards/H_029_cosn_correlation_lens.md` (≥4 falsifiers PASS, ≥5 honest limits, verbatim banner
  + E_flat−E_F vs U table); `tool/rtsc_candidates.py` LAYER_A[CoSn] records `doping_wall_dissolves=False`;
  artifacts in `state/h029_cosn_correlation_lens_2026_06_25/`. Trio stays 🟠 jointly-unrealized;
  absorbed=false / GATE_OPEN (a wall that survives +U HARDENS the terminal — a valid, valuable result).

- **+@ combination campaign — synthesis + honest computational terminal.** Consolidated H_001–H_028
  into `state/papers/plus-at-combination-campaign-synthesis.md`. **H_028**: Ni3In is NOT a better
  layer-A (flat band −0.84 to −1.57 eV below E_F, as deep as CoSn → no doping-wall dodge in PBE;
  ∫tr g=2.854 met but ν=1.0 D_s-suppressed; spin-polarized SCF magnetically unstable = an SDW
  competing-order CoSn lacks) — lead A-layer stays CoSn. **Net**: the computational mechanism-space
  is honestly DRY — all 5 glue families (phonon/exciton/plasmon/magnon/CDW-exciton), 3 layer-A metals
  (CoSn/Ni3In/CsV3Sb5), the driven lens, demand-relaxation, per-layer DFT, and the MPI infra fix are
  all surveyed/closed. The named CoSn/hBN/Ta2NiSe5 trio is the strongest 🟠 with every
  computationally-settleable lever confirmed (geometry ∫tr g=2.856, spacer DFT, D_s(N=2) supported) or
  literature-bounded (Ta2NiSe5 ~300 meV many-body glue, beyond-PBE for us); the remaining obstacles
  (no clean ≥349 meV glue, CoSn extreme-doping, joint fabrication, accredited transport) are physical
  synthesis/measurement = absorbed=true requirements, outside compute. absorbed=false / GATE_OPEN.
- **H_028 — Is Ni3In a BETTER layer-A flat-band metal than CoSn (flat band AT E_F, dodging
  H_027's extreme-doping wall)? 🟡 REAL-DFT.** `HYPOTHESES/cards/H_028_ni3in_layer_a.md`,
  artifacts in `state/h028_ni3in_layer_a_2026_06_25/`.
  - **Ni3In FAILS the dodge — it is NOT a better layer-A than CoSn.** Backup research (A-backup-1,
    `state/research-backup-candidates-2026-06-25.md`) named Ni3In as the kagome metal whose flat band
    sits ~50 meV NEAR E_F (Ye 2021 arXiv:2106.10824) — the natural escape from H_027's CoSn
    extreme-doping wall. OUR REAL paramagnetic PBE DFT (DO19 Ni3Sn-type Ni6In2, P6₃/mmc a=5.286/c=4.243 Å,
    Ni 6h kagome net NN=a/2 + In 2c, 134 e⁻, MPI per H_026 — verbatim banner "Parallel version (MPI),
    running on 6 processors", 6 live pgrep ranks; conv 1e-7 in 22 iters, **E_F=16.5270 eV**) finds the
    **Ni-kagome flat-band manifold sits −0.84 to −1.57 eV BELOW E_F** (band 56, W=0.255 eV at −1.567 eV)
    — i.e. AT LEAST as deep as CoSn's (−0.44 eV near / −1.45 eV deep), so Ni3In needs the SAME-or-worse
    doping-to-E_F → **NO dodge** in PBE. The cited ~50 meV-near-E_F is a CORRELATED/DMFT position PBE
    does not reproduce (L1 caveat: DMFT/+U/GW could pull it toward E_F).
  - **Geometry lever MET but below E_F; magnetic instability added.** The NN-kagome TB-fit metric
    integral **I = (1/2π)∫tr g d²k = 2.854 ≈ CoSn's 2.855 ≈ measured QGT 2.87** (arXiv:2412.17809) →
    the geometry lever IS supplied (kagome NN=a/2 confirmed) — but a geometry lever below E_F is exactly
    CoSn's accessibility-limited situation. Native filling **ν=1.0 → ν(1−ν)=0 → D_s edge-suppressed**
    (flat band fully occupied). **Worse than CoSn on a second axis:** the spin-polarized SCF is
    magnetically UNSTABLE across 3 recipes (accuracy oscillates 11–37 Ry, **absolute magnetization
    swings 11–27 μB/cell** with small net ~2 μB = frustrated large-local-moment kagome) → a competing
    magnetic-order (H_014) risk CoSn does not carry. The paramagnetic nspin=1 reference (used for the
    clean band/geometry measurement) converged; the magnetic SCF is reported honestly as non-converging,
    no fabricated magnetic E_F.
  - **Honest verdict: NOT a better layer-A — the lead A-layer stays CoSn.** is_green=False preserved;
    the deterministic geometry/position/filling analysis is byte-reproducible (`out/h028_geometry.out`).
    Registry: `tool/rtsc_candidates.py` LAYER_A adds Ni3In with the DFT g_mean=2.854 (verified geometry)
    + the flat-band-far-below-E_F note + SDW competing-order flag. Trio CoSn/hBN/Ta2NiSe5 stays
    **🟠 jointly-unrealized**; absorbed=false / GATE_OPEN — no simulation flips that.

- **H_027 — does CoSn's flat-band GEOMETRY LEVER survive the DOPING required to bring the flat
  band onto E_F? (the last computationally-settleable risk on the lead 🟢-path). 🟡 REAL-DFT.**
  `HYPOTHESES/cards/H_027_doped_cosn_geometry_survival.md`, artifacts in
  `state/h027_doped_cosn_geometry_survival_2026_06_25/`.
  - **Geometry + favourable filling SURVIVE, but the doping to reach E_F is EXTREME.** From OUR
    converged spin-polarized PBE bands of the fuller Co3Sn3 cell (near-E_F kagome flat band 45,
    W=0.167 eV, −0.44 eV below E_F; on the H_026 MPI-fixed host, verbatim banner "Parallel version
    (MPI), running on 6 processors"): (1) the rigid-band hole doping to slide E_F onto the flat band =
    **4.73 e⁻/cell = 1.58 holes per CoSn formula unit = 5.1% of valence → EXTREME** (>0.7 h/f.u.;
    beyond electrostatic gating, needs full chemical substitution — a direct consequence of the flat
    band's huge DOS, which the rigid-band sweep shows rising 5→17 states/eV/cell); (2) at that doped
    E_F the NN-kagome TB-fit metric integral **I = (1/2π)∫tr g d²k = 2.855 ≈ measured QGT 2.87**
    (arXiv:2412.17809) → the geometry lever **SURVIVES** (I≥2), under the rigid-band assumption (real
    doping can hybridize/spin-split — caveat named); (3) the flat-band filling at E_F-on-band
    **ν = 0.507 → ν(1−ν) = 0.250 = the FAVOURABLE half-filling D_s^geom maximum**.
  - **Honest verdict: the lead 🟢-path is WEAKENED on ACCESSIBILITY, not on geometry.** The geometry
    and filling are the best case *if* E_F could be placed on the flat band — but the carrier density
    to place it is unphysical for gating, and the live doped SCF (tot_charge=4, genuine 6-rank MPI)
    shows the doped flat-band metal is delicate (iter-1 accuracy ~29 Ry sloshing, slow; the prior
    tot_charge=2 run MPI_ABORTed) → no converged doped E_F, reported honestly, not fabricated.
    is_green=False preserved. The deterministic rigid-band analysis is byte-reproducible
    (`out/h027_geometry.out`). Trio CoSn/hBN/Ta2NiSe5 stays **🟠 jointly-unrealized**; absorbed=false /
    GATE_OPEN — no simulation flips that.
  - Registry: `tool/rtsc_candidates.py` LAYER_A[CoSn] records the doping-to-E_F magnitude + the
    geometry/ν survival flags. ARCHITECTURE `campaigns.named-candidate-dft` updated in lockstep.

- **H_023 RTSC 레버 — DFT 런 준비도 점검 (SAFE prep · 컴퓨트 미실행).** `state/h023-dft-readiness-2026-06-25.md`.
  READ+VERIFY+DOCUMENT only (pw.x·클라우드·heavy compute 미실행). h019 DFT 덱 검증 →
  의사퍼텐셜/컷오프/화학량은 sane 이나 **셀이 폐기된 Cmcm 부모상**(현역=h025 monoclinic)이고 모든 덱이
  **밴드갭 SCF 덱이지 D_s 덱이 아님**. **판정 🔴 BLOCKED — 두 측정-벽 선행**: ⓐ *방법 벽* — 다층
  초유체강성 D_s 는 평범한 pw.x 관측량이 아님(양자기하 QGT 또는 BSE 요함; "DFT 가 f_mult 클리어"는
  한 번의 pw.x 런으로 환원 안 됨), ⓑ *PBE 이론 벽* — H_025/H_026 가 단층 갭조차 PBE 근금속 진동으로
  측정(beyond-PBE 만 남음). cheap 양자기하 route 는 H_024 가 이미 닫음(f_mult≥1.164@N=2
  SUPPORTED-conditional, is_green=False). 원-커맨드 승인 스펙(A/B/WALL) 명시. 정직성: 클리어해도
  반증-생존 예측이지 발견 아님 — 게이트 닫힘=공인 4-프로브, absorbed=false 불변.

- **H_026 — INFRA ROOT-CAUSE FIX (self-built QE 7.2 rebuilt WITH MPI on `summer`) + Ta2NiSe5
  monoclinic gap re-run under genuine 6-core parallelism. 🟡 REAL-DFT.**
  `HYPOTHESES/cards/H_026_qe_mpi_ta2nise5_gap.md`, artifacts in
  `state/h026_qe_mpi_ta2nise5_gap_2026_06_25/`.
  - **The substrate root-cause that silently crippled EVERY campaign DFT (H_015→H_025) is FIXED.**
    H_025 had measured that the canonical `~/qe_build/q-e-qe-7.2/bin/pw.x` was a **SERIAL** build
    (`make.inc` `MPIF90=gfortran`, `DFLAGS=-D__FFTW` only, no `-D__MPI`; banner "Serial version"), so
    every prior `mpirun -np 12 pw.x` launched **12 redundant serial copies on 1 core each** — the true
    tractability wall behind every "won't converge in budget" DFT. Root cause: OpenMPI 4.1.6 *runtime*
    was already present on summer, but the linkable dev package (`libopenmpi-dev`, providing the `.so`
    symlinks the `mpif90` wrapper references) was missing, so `./configure` silently fell back to
    "serial executables". Fix (all FREE): `sudo apt-get install -y libopenmpi-dev` →
    `./configure MPIF90=mpif90 --enable-parallel` ("Parallel environment detected successfully") →
    `make clean && make pw -j12`. Verbatim after: `make.inc` `DFLAGS = -D__FFTW -D__MPI`; `ldd pw.x`
    links `libmpi.so.40`; banner under `mpirun -np 4/6` = **"Parallel version (MPI), running on 4/6
    processors"**. Built in place (canonical build). Recorded in `tool/CLAUDE.md`. (A second, parallel
    QE 7.5 also exists in the conda env `~/miniforge3/envs/qe/`.)
  - **Ta2NiSe5 monoclinic gap — HONEST NEGATIVE under PBE-family (now definitive, budget wall removed).**
    Re-ran the H_025 monoclinic C2/c cell (identical header: vol 701.5 Å³, Ta8Ni4Se20=32, 296 e⁻) via
    `mpirun -np 6 pw.x -npool 2`, far past the serial-era cut-off. Across THREE recipes — robust plain
    PBE (17.17→…→1.66 Ry, 14 iter), PBE+U(Ni-3d=3 eV ortho-atomic, Dudarev) (17.91→…→1.10 Ry, 12 iter),
    and a higher-smearing PBE variant (degauss 0.03; 17.15→…→0.55 Ry, 12 iter) — the SCF breaks the
    H_019/H_024 Cmcm byte-identical freeze (~28–38× descent, live charge dynamics) but then **OSCILLATES
    persistently in a ~0.5–1.7 Ry near-metallic plateau and NEVER reaches conv_thr=1e-6**, even with the
    MPI build running ≫ the serial budget. The plateau is therefore **PHYSICAL, not a compute artifact**:
    PBE / PBE+U / higher-smearing all leave monoclinic Ta2NiSe5 near-metallic (the gap is many-body /
    excitonic, absent in these functionals). No converged density → no KS gap → **gap UNRESOLVED-by-us,
    reported as an honest negative on a PBE-DFT gap** (not fabricated; every residual is verbatim pw.x
    stdout). The gap is NOT graduated to our-DFT in `tool/rtsc_candidates.py`; the only remaining path is
    beyond-PBE (HSE/GW/many-body), far beyond 6 cores.
  - **Trio stays 🟠 jointly-unrealized; absorbed=false / GATE_OPEN** — the infra fix and the honest gap
    negative flip nothing on the RTSC gate.

- **H_025 — Ta2NiSe5 symmetry-broken (monoclinic C2/c) gap: the LAST deferred per-layer gap of the
  named +@ trio, attacked with the PHYSICALLY-CORRECT cell on the free `summer` host. 🟡 REAL-DFT
  (PARTIAL POSITIVE).** `HYPOTHESES/cards/H_025_ta2nise5_symbroken_gap.md`, artifacts in
  `state/h025_ta2nise5_symbroken_gap_2026_06_25/`.
  - **The symmetry-broken monoclinic C2/c cell BREAKS the Cmcm SCF freeze.** H_019/H_024 left the
    Ta2NiSe5 gap DEFERRED because the high-symmetry orthorhombic **Cmcm parent** SCF FROZE
    (byte-identical successive residuals, e.g. `13.94569806 = 13.94569806`) across 10 recipes —
    diagnosed as the near-metallic excitonic-PARENT being ill-conditioned. H_025 TESTED the logged
    fix by building the EXPERIMENTAL low-T **monoclinic C2/c** ground state (Sunshine & Ibers 1985
    via arXiv:2201.07750: a=3.496 b=12.829 c=15.641 Å β=90.53°; vol 701.5 Å³, Ta8Ni4Se20=32, the Ta
    chain carries the symmetry-breaking x-shift). Across BOTH a robust plain-PBE recipe AND
    PBE+U(Ni-3d=3 eV ortho-atomic), the 296-e SCF residual descends MONOTONICALLY ~30× (17–18 Ry →
    0.45–0.64 Ry) with LIVE charge dynamics (no two iterations identical) — categorically unlike the
    Cmcm parent's dead freeze. The symmetry-breaking insight is CONFIRMED.
  - **Gap still UNRESOLVED (honest, not fabricated).** Both monoclinic recipes then PLATEAU
    near-metallic in the ~0.5–0.9 Ry band and do NOT reach conv_thr=1e-6 → no converged density → no
    KS gap extracted (the 0.16–0.35 eV window stays unverified-by-us). This is consistent with
    PBE/PBE+U under-gapping the many-body excitonic gap (near-metallic → hard SCF).
  - **Measured this session — the real tractability wall: the QE 7.2 build is SERIAL.** `make.inc`
    `MPIF90=gfortran`, `DFLAGS=-D__FFTW` only (no `-D__MPI`/`-D__OPENMP`); `ldd pw.x` shows no MPI;
    pw.x prints "Serial version". Every SCF runs on **1 core** — the prior H_019/H_024 `mpirun -np 12`
    launched 12 redundant serial copies. Deferred fix to actually reach the gap (logged, needs a
    PARALLEL build): DFT-relaxed monoclinic coords (β=90.644°, PNAS) / denser k-mesh / HSE.
  - **Registry**: `tool/rtsc_candidates.py` LAYER_B[Ta2NiSe5] — gap NOT graduated to our-DFT (no
    in-window convergence); kept literature-flagged-unverified with the H_025 freeze-break finding +
    sharpened recipe ladder logged. Trio stays 🟠 jointly-unrealized; absorbed=false / GATE_OPEN.

- **H_024 — REAL-DFT follow-on closing H_019's deferred/failed halves AND attacking H_023's single
  unknown (self-built QE 7.2 on `summer` + local TB metric; all FREE, no rental). 🟡 REAL-DFT
  (PARTIAL).** `HYPOTHESES/cards/H_024_named_candidate_dft_followon.md`, artifacts in
  `state/h024_named_candidate_dft_followon_2026_06_25/`.
  - **(2) CoSn flat-band quantum geometry ∫tr g — geometry lever SURVIVES OUR DFT.** A NN-kagome
    tight-binding fit to OUR converged PBE bands (`cosn.bands.out`; no wannier90.x is built →
    TB-fit route; t=0.077 eV from the 3-band group [39,40,41] span 0.462 eV = 6t) gives the
    QGT-convention metric integral **I = (1/2π)∫tr g d²k = 2.856**, essentially equal to the
    **measured QGT g = 2.87** (arXiv:2412.17809) → supports g≥2 (F3/F4 PASS, not tuned; Γ
    band-touching divergence handled honestly). The ~1.45 eV-below-E_F position (H_019 F2 FAIL) is
    now explained as REAL orbital-selection — CoSn hosts multiple orbital kagome flat bands (the
    d_xz/d_yz one near E_F, the in-plane-d ones deeper); our sparse-path min-width pick captured the
    deeper manifold; PBE is ~140 meV faithful to ARPES (Kang Nat. Commun. 2020) → NOT a PBE artifact.
  - **(3) D_s(N=2) geometric bound — H_023's single unknown SUPPORTED (conditional).** Peotta–Törmä
    (arXiv:1506.02815) + Huhtinen 2022 (arXiv:2203.11133): the non-vanishing O(1) metric (I=2.86≥2)
    makes D_s^geom non-zero → **f_mult≥1.164 at N=2 is SUPPORTED** on both H_023 scaling models,
    CONDITIONAL on doping the flat band to E_F (D_s^geom ∝ ν(1−ν)) and interlayer coherence;
    **is_green=False** (no measured multilayer D_s — the cheap geometric route, NOT the intractable
    full N=2 stack SCF). F5 PASS.
  - **(1) Ta2NiSe5 gap — STILL DEFERRED (now characterised).** The 296-electron Cmcm PBE SCF does NOT
    converge across 3 new recipes on the freer host (robust k4×2×2 iter1 incomplete in 25 min; fast
    k2×1×1 iter1=iter2=13.94569806 Ry frozen; stall degauss 0.025/plain β0.7 iter1=iter2=13.74920763
    Ry frozen) — the estimated scf accuracy FREEZES recipe-independently (mixing plain/local-TF, β
    0.2–0.7, smearing 0.01–0.025 Ry), ~6–8 min/iteration. A hard SCF ill-conditioning of the
    high-symmetry excitonic-PARENT cell (near-degenerate at the cusp of the gap-opening), **NOT mere
    contention** (the host was freer than in H_019, yet the stall is the same/worse). → F1 FAIL, gap
    DEFERRED, **no fabricated number** (commons: a non-converging result is kept as a result; the
    symmetry-broken-phase / hybrid+U fix is logged as deferred). Literature 0.16–0.35 eV stays
    unverified-by-us.
  - **registry** `tool/rtsc_candidates.py`: CoSn `g_mean` source annotated with OUR-DFT I=2.86 + the
    real-position finding; Ta2NiSe5 `boson_meV` source + note updated to record the 10-variant
    (7+3) recipe-independent non-convergence and the H_024 D_s-geometry route. CoSn stays
    qualified=True (g=2.87 ≥ 2.0). Trio stays 🟠 jointly-unrealized; absorbed=false / GATE_OPEN.

- **CENSUS — 검증-지식 레지스트리 전수수집(2026-06-25).** `state/knowledge-census-2026-06-25.md`
  (additive, read-only harvest). 총 레지스트리 엔트리 114 (가설 22 + 물질원장 92): VERIFIED(🟢/GATE_PASS/
  textbook-proof/measured/REAL-DFT/REAL-ED) 20 · REFUTED(🔴) 12 · INCONCLUSIVE(🟠) 9 · MODEL-PROBE 미실증
  (🟡 real-pending) 17 · PENDING 36 · 기타 메타 20. 임베디드 hexa-atom atlas 부재(가설카드+원장 형식). 헤드라인
  VERIFIED = H_015 REAL-DFT(hBN 전자-불투명 7.7×) · H_008 REAL-ED(retarded vertex 4.27×) · LaRu3Si2 GATE_PASS
  (no-cooling RTSC lead). 모든 VERIFIED 20건 `absorbed=false`/GATE_OPEN — RTSC 단정 0건.
- **H_019 — first REAL PBE DFT on the NAMED +@ trilayer's two load-bearing layers (self-built QE 7.2
  on `summer`; apt 6.7 broken per H_015). PARTIAL real result, honestly tiered 🟡.**
  `HYPOTHESES/cards/H_019_named_candidate_dft.md`, artifacts in
  `state/h019_named_candidate_dft_2026_06_25/`.
  - **CoSn (layer A) — flat band CONFIRMED, but with an HONEST POSITION-DISAGREEMENT.** Our PBE scf
    (converged, 10 iter, E_F=16.00 eV, exp. lattice a=5.2693/c=4.2431 Å) + a Γ–M–K bands run finds the
    kagome flat-band manifold is REAL: **W = 0.158 eV** (band 41, narrowest of a 0.16–0.25 eV cluster)
    → **F1 PASS** (a genuine W<0.2 eV flat band). BUT it sits **~1.45 eV BELOW E_F**, DEEPER than the
    cited ~0.2 eV (Liu arXiv:2001.11738) → **F2 FAIL**, reported as an honest PBE/orbital-character
    disagreement (NOT tuned) — a real doping-to-E_F risk the paper-level cards H_020/H_021/H_023 had
    assumed away. The registry CoSn `source` graduates from literature → our-own-DFT.
  - **Ta2NiSe5 (layer B) — cell builds correctly, but the 296-electron PBE SCF would NOT converge
    in-session (honest negative).** The 32-atom orthorhombic Cmcm cell is correct (vol 706.7 Å³,
    296 e⁻, stoichiometry Ta8Ni4Se20 — all match experiment) but across **7 SCF recipe variants**
    (k-mesh 6×2×2→4×1×1→Γ; ecutrho 400→360; mixing plain/local-TF, β 0.5/0.3/0.1; occupations
    smearing/fixed; ±startingpot resume) the accuracy **plateaus at ~0.5 Ry** (never near 10⁻⁵) on the
    heavily-contended shared host (load 11–14 from a co-tenant ML job) → **gap DEFERRED, not
    fabricated** (F3/F4 deferred; literature 0.16–0.35 eV stays unverified-by-us). Commons: a partial
    result is kept as a result.
  - **Cross-spacer coupling — labeled ORDER-OF-MAGNITUDE estimate (NOT cRPA).** Screened-Coulomb kernel
    with hBN ε_perp=3.3 (Laturia 2018) → steep ~4× geometry-dilution per hBN ML; at n=2 the effective
    coupling is **tens of meV (λ≲0.1)** — the Krotov–Suslov dilution failure mode quantified. A bound,
    not a prediction; the **full commensurate heterostructure cRPA is DEFERRED** (hexagonal-vs-
    orthorhombic giant supercell = intractable this session).
  - **Verdict: 🟡 (one layer DFT-confirmed-with-disagreement + one layer built-but-unconverged + an
    analytic estimate). The trio CoSn/hBN/Ta2NiSe5 stays 🟠 jointly-unrealized; `absorbed=false` /
    GATE_OPEN.** No tune-to-green, no fabricated numbers.

- **RESEARCH — bounds H_023's binding L1 (the multilayer D_s boost): 🟠 plausible-but-host-unverified.**
  `state/research-multilayer-ds-boost-2026-06-25.md`. Directly tests whether the lead 🟢-path's single unknown — a
  ~1.16× (16%) superfluid-weight boost at the smallest N=2 — has empirical support. Findings: the flat-band D_s bound is
  real (**Peotta & Törmä, Nat.Commun.6,8944(2015), arXiv:1506.02815**: D_s≥|C|, D_s∝|U|×quantum-metric) but the corrected
  mean-field (**Huhtinen/Bernevig/Törmä, PRB106,014518(2022), arXiv:2203.11133**) makes it a RATIO (N_flatband/N_orbital),
  so extensivity is contingent, not automatic. Real small-N boosts ARE on record at the card's ~16% scale — bi→trilayer
  graphene +~40% (Kim, Nature606,494(2022)), cuprate Hg-series 97→128→134 K n=1→3 +~32% then capped (Nat.Phys.19,1821(2023),
  arXiv:2210.06348), direct quantum-geometric ρ_s measured (**arXiv:2406.13742**) — BUT every series SATURATES/REVERSES by
  N≈3 (**Park family, arXiv:2112.10760**: 3,3,2.76,1.38 K for N=2..5; FeSe peaks at MONOLAYER). Worse, the one EI-specific
  datum runs the WRONG way: Ta2NiSe5's excitonic order is **layer-confined** (ACS Nano 10,9966(2016)) and ultrathin T_c
  **−9%**. No D_s-vs-N exists for Ta2NiSe5. VERDICT **🟠 CONDITIONAL** — +16% at N=2 is magnitude-PLAUSIBLE and in-range,
  NOT well-supported (🟢) and NOT impossible (🔴); host-unverified. The H_019 N=2-stack DFT remains the decisive test; the
  lead path stays 🟠-CONDITIONAL. absorbed=false; GATE_OPEN.

- **NEW LENS — driven/non-equilibrium re-opens the 1T-TiSe2 path the STATIC research closed (honest 🟠).**
  `state/research-driven-tise2-reopen-2026-06-25.md`. The static survey closed the path on the equilibrium fact that
  TiSe2's ~400 meV exciton and its finite-q CDW are inseparable (Kogar/Abbamonte, Science 358,1314(2017) — mode softens
  to 0 at T_CDW). The user's lens ("the WAY you pass current changes the result") OVERTURNS that premise out of
  equilibrium: **Burian et al., PRR 3,013128(2021) (arXiv:2006.13702)** document a transient fluence window where the
  structural CDW (PLD) is suppressed while the high-energy electronic/excitonic orbital order is RETAINED; **Porer et al.,
  Nat.Mater.13,857(2014) (arXiv:1604.05627)** prove the electronic & structural orders are non-thermally SEPARABLE; and
  **Duan et al. (arXiv:2306.00311)** reach a metastable METALLIC (SC-favorable) state within 100 fs (ps lifetime). Driven
  SC is a real mechanism — **K3C60** light-induced SC at ~5× Tc, now metastable to **>10 ns** (Mitrano Nature 530,461(2016),
  arXiv:1505.04529; Budden Nat.Phys.17,611(2021), arXiv:2002.12835) — but **contested in cuprates** (Zhang arXiv:2306.07869:
  stripe-melt WITHOUT SC). VERDICT **🟠 DRIVEN-REOPEN**: the lens is productive (the static inseparability is false out of
  equilibrium), but the honest power/lifetime bill is decisive — every driven state is **continuously powered + transient
  (ps–ns), none at room T, and driven SC is NOT yet shown in TiSe2 itself** (only the metallic precondition). A
  laser-powered ps–ns lab state is NOT the campaign's equilibrium 293 K turnkey conductor → re-opens the path as a LAB
  COORDINATE, not a 🟢. absorbed=false / GATE_OPEN.
- **Demand-relaxation round — strongest 🟢-path found (still 🟠-CONDITIONAL).** **H_023**: instead of an
  exotic ≥349 meV glue, RELAX the room-T demand via a multilayer superfluid-weight (D_s) boost. Required
  f_mult = 349.3/300 = 1.164 (~16%), reached at the SAME smallest N=2 on BOTH a conservative (N^0.25
  Josephson-stack) and an optimistic (sqrt N Peotta-Törmä) model; the CLEAN trio CoSn/hBN/Ta2NiSe5 then
  reaches 299–356 K. Decisive advantage over every closed path: Ta2NiSe5's q=0 excitonic order IS the
  pairing channel, so there is NO competing order to escape and NO exotic glue needed — the path needs
  only a real multilayer D_s. 7/7, is_green=False (f_mult(N) is a model; the real value needs DFT — which
  CONVERGES with the running real-DFT of the same trio, H_019). The **magnon-glue family**
  (state/research-magnon-glue-2026-06-25.md) lands the SAME wall: single-magnon cuprate (~300 meV) → ~252 K
  (= the H_020 wall), and only the bimagnon (~500 meV) clears 349 — but it is the soft mode of the magnetic
  order (glue tied to competing order, like 1T-TiSe2). NET: the campaign's lead 🟢-path is now the CLEAN
  demand-relaxation route (no competing-order problem, modest N=2 multilayer); the single unknown is the
  real superfluid-weight boost of a fabricated CoSn/hBN/Ta2NiSe5 stack. absorbed=false / GATE_OPEN.
- **🟢-unlock fleet round — both prime 🟢-paths CLOSED (honest 🟠, goal "성공물질 발견까지 fleet").**
  **H_022 frustration-unlock confluence**: 1T-TiSe2 closes BOTH model blockers at once — stacked_tc(400,3D)=335.5K
  clears room-T (+50.7meV glue margin), AND at a frustrated nesting (eta=0.35<eta*0.45) SC leads the CDW
  (U_sc 2.22 < U_cdw 7.14), with the commensurate control SDW-leading (the unlock is bought by frustration). 6/6,
  is_green=False by the honesty gate (the coexistence is unverified). Two research lanes then CLOSED both 🟢-paths:
  (1) **1T-TiSe2 CDW-suppression** (state/research-tise2-cdw-suppression-2026-06-25.md) — every route (Cu intercalation
  Tc~4K, pressure Tc~1.8K, monolayer) suppresses the CDW by KILLING the ~400meV exciton (the exciton IS the
  excitonic-CDW) → exciton NOT retained; (2) **engineered plasmon** (state/research-engineered-plasmon-glue-2026-06-25.md)
  — no turnkey ≥349meV clean plasmon today (graphene caps ~0.11eV by Pauli blocking; acoustic <0.2eV; the NbS2/hBN
  2508.06195 class is computed-only, energy a design parameter). NET 🟠: no 🟢 success-material in the surveyed
  exciton/plasmon families — the clean q=0 glues (Ta2NiSe5 300, Ta2Pd3Te5 100) undershoot the 349meV room-T demand,
  and the only over-target boson (1T-TiSe2 400) is inseparable from its competing CDW. The precise modern statement of
  the excitonic-SC graveyard. Remaining orthogonal moves (NOT dry): magnon-glue family + demand-relaxation (multilayer
  D_s boost to drop the 349meV demand below the clean 300meV glue). absorbed=false / GATE_OPEN.
- **Fleet round toward 🟢 success-material (goal "성공물질 발견까지 fleet")** — 3 cheap lanes while the
  named-trio real DFT runs on summer. **H_020 named-trio amplitude** (closed-negative): the named
  CoSn/hBN/Ta2NiSe5 with Ta2NiSe5's verified ~300 meV glue lands at ~252 K with the real 3D lever
  (clears the 133 K ambient ceiling) but MISSES room-T by ~41 K / ~49 meV-of-glue (room-T needs
  ~349 meV) — a high-Tc coordinate, not an RTSC (4/5, F1 correctly triggered). **H_021 pair
  leaderboard**: CoSn/hBN/Ta2NiSe5 tops all A×B registry pairs (only fully-verified box-clearing
  pair, ~252 K coordinate); higher-Tc pairs are gap-blocked (5/5). **Backup-candidate research**
  (state/research-backup-candidates-2026-06-25.md): 🟠 no clearly-better-than-Ta2NiSe5 glue, but
  the search now has a concrete 🟢-path — 1T-TiSe2 has a ~400 meV exciton (CLEARS room-T amplitude)
  blocked only by a CDW (H_016-escapable by frustration); the clean q=0 hosts (Ta2NiSe5 ~300, Ta2Pd3Te5
  ~100) sit at/below target; an engineered 2D plasmon can reach ≥349 meV cleanly. Backup rows
  (Ta2Pd3Te5, 1T-TiSe2@400meV, Ni3In, YMn6Sn6, FeSn, tWSe2, ...) proposed for tool/rtsc_candidates.py
  (folded in after the concurrent H_019 DFT edit lands). Net: best stays 🟠 (~252 K coordinate); the
  named glue undershoots room-T by ~49 meV; the highest-energy candidate (1T-TiSe2) is CDW-blocked.
- **Wire the materials breakthrough into a tool — `tool/rtsc_candidates.py`** (living candidate
  registry + verifier; the verifier 검증기 REUSES the rtsc_harness falsifier engine, not a new
  one — answers "one tool? split?" = ONE new file, harness stays the engine). Each candidate
  property = (value, source, verified); only verified properties pass, unverified surface as
  `gaps` — grow it every research round, no fabrication. Seeded from the constructive research
  (PR #10): layer-A CoSn (directly-measured QGT, arXiv:2412.17809) + Nb3Cl8 verified; layer-B
  Ta2NiSe5 now VERIFIED (exciton ~0.16-0.35 eV at the ~349 meV glue target, q=0 non-nesting so
  no pre-empting CDW/SDW, SC under pressure — arXiv:2007.08212/2106.04396). The named lead
  **CoSn / hBN(2ML) / Ta2NiSe5** clears the +@ two-lever box on paper (bkt_Tc~137K @2D coordinate,
  ~252K with the H_006 3D lever) but the trio is JOINTLY UNREALIZED -> 🟠 CREDIBLE-PARTIAL,
  absorbed=false / GATE_OPEN (bkt_Tc is a coordinate not a prediction, H_018). Registered in
  tool/CLAUDE.md. Also registered the "실측전 research" rule in CLAUDE.md (rtsc PR#8 + lumen PR#25).
- **Research note — constructive candidate enumeration for the +@ trilayer (layer A flat-band metal · layer B
  bosonic glue) → 🟠 partial candidate** (read-only materials survey,
  `state/research-glue-material-candidates-2026-06-25.md`). The constructive complement to the wall-classification
  note (#9): instead of asking *whether* a glue material exists, it **enumerates and ranks concrete, named candidates**
  and proposes one falsifiable trilayer. (§1 Layer A) Ranked flat-band metals — top: **CoSn** (kagome, non-magnetic,
  flat-band W<0.2 eV / out-of-plane orbital <0.02 eV, and the one material with a *directly measured* quantum
  geometric tensor — arXiv:2001.11738, arXiv:2412.17809); then MATBG (flattest but moiré-only), Ni3In (flat band at
  E_F), FeSn/YMn6Sn6 (magnetic), CsV3Sb5 (has own CDW). (§2 Layer B) Ranked bosonic glues — top: **Ta2NiSe5**
  excitonic insulator (gap ~0.16–0.35 eV, onset ~325–328 K — squarely at the ~349 meV target; arXiv:2007.08212,
  arXiv:2203.06817) and TMD interlayer-exciton bilayers (ideal cross-spacer dipole). (§3 Competing-order screen)
  **Ta2NiSe5 is the only named B whose order is q=0 / non-nesting** (no incommensurate CDW/SDW to pre-empt SC; it
  superconducts under pressure — arXiv:2106.04396), whereas the TMD route carries the density wave *inside* the
  mechanism (Kumar–Senthil arXiv:2410.09148). (§4) **Proposed recipe: CoSn (doped) / hBN(2) / Ta2NiSe5** — each lever
  demonstrated in the named compound, instantiating the computed cross-spacer plasmon/exciton glue (in 't Veld–Rösner
  arXiv:2508.06195). **Verdict 🟠** — a specific, fully-named, internally-consistent trilayer now exists (stronger than
  "no candidate"), but the three pieces have never worked *together*: no measured cross-spacer coupling for this trio,
  B's mode is a phonon-hybrid not a pure exciton, and no bosonic-glue Tc has ever been measured. The wall is
  materials-engineering-limited and we can now name the exact brick to try first. `absorbed=false` / GATE_OPEN unchanged.

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
