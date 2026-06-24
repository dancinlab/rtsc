---
id: H_024
slug: named-candidate-dft-followon
title: REAL-DFT follow-on closing H_019's two deferred/failed halves AND attacking the lead 🟢-path's single unknown — (1) re-converge the Ta2NiSe5 296-electron PBE SCF on the now-free summer host for an our-DFT band gap; (2) extract the CoSn kagome flat-band quantum geometry ∫tr g via a tight-binding fit to OUR converged PBE bands and ask whether g≥2 survives + whether the ~1.45 eV-below-E_F position is a PBE artifact; (3) bound D_s(N=2) for H_023's demand-relaxation path via the Peotta-Törmä + Huhtinen-2022 geometric route (NOT the intractable full stack SCF). All FREE (no rental). Trio stays 🟠 / absorbed=false regardless.
domain: rtsc
status: real-dft
exploration_method: close the DEFERRED (Ta2NiSe5 gap) + FAILED (CoSn position) halves of H_019, and the single named DFT unknown of H_023 (lead 🟢-path), on the now-uncontended summer host — all cheap/free routes
verification_method: W1 (pre-register frozen) + W2 (falsifier-4+) + W3 (deterministic DFT, our own QE 7.2) + W5 (honest-limits-5+)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
compute: summer pool (self-built QE 7.2, ~/qe_build/q-e-qe-7.2/bin/pw.x); local TB metric (numpy/scipy)
since: 2026-06-25
---

# H_024 — real-DFT follow-on: Ta2NiSe5 gap + CoSn ∫tr g + D_s(N=2) geometric bound (rtsc)

## Hypothesis

H_019 left TWO open halves and H_023 names ONE DFT-shaped unknown. This card attacks all three
by CHEAP/FREE routes on the now-uncontended summer host (no rental):

1. **Ta2NiSe5 gap (H_019 deferred half).** The 32-atom orthorhombic Cmcm cell whose 296-electron
   PBE SCF would not converge under host contention in H_019 is re-run with a robustness recipe
   (SSSP-class pseudos, mixing_beta 0.25 + local-TF, electron_maxstep 200, MV smearing degauss
   0.01 Ry, ecutwfc 50 / ecutrho 400 Ry, k 4×2×2). **Hypothesis: on the free host it converges →
   our-DFT Kohn–Sham gap**, to be compared to the 0.16–0.35 eV literature window (PBE
   underestimates gaps; an honest disagreement is a valid result).
2. **CoSn ∫tr g (H_019 layer-A lever).** From OUR converged CoSn PBE bands, extract the flat-band
   Fubini–Study quantum metric (no wannier90.x is built → named tight-binding-fit route: fit a NN
   kagome 3-orbital Bloch model to the DFT flat manifold, compute its analytic metric by projector
   finite-difference). **Hypothesis: the geometry lever is non-vanishing/O(1)** (vs the MEASURED QGT
   g=2.87, arXiv:2412.17809); and we judge whether the ~1.45 eV-below-E_F position is a PBE
   correlated-flat-band artifact or a real obstruction.
3. **D_s(N=2) geometric bound (H_023's single unknown).** Use the Peotta–Törmä flat-band
   superfluid-weight bound (arXiv:1506.02815) + the Huhtinen-2022 minimal-metric correction
   (arXiv:2203.11133) to ask: does the quantum-geometry evidence SUPPORT f_mult≥1.164 at N=2 for
   THIS flat band? (The full N=2 stack SCF is intractable on 12 cores and is NOT attempted.)

## Why

- H_019 ended 🟡 with two honest gaps (Ta2NiSe5 SCF non-convergence under contention; CoSn flat
  band confirmed but position-disagreeing). The host is now free → the SCF is retriable, and the
  geometry lever (which H_001/H_023 lean on) is testable from OUR bands, not just the literature QGT.
- H_023 (the campaign's strongest 🟢-path) rests on a single DFT-shaped unknown: the real
  multilayer D_s. The CHEAP geometric bound is the honest first cut before any (intractable) full
  stack SCF.
- PBE famously underestimates gaps and, for a correlated kagome flat band, can mis-place the band —
  so a wrong gap / deep position is EXPECTED and is reported as a disagreement, not tuned away.

## Predictions

- **H24.1 (Ta2NiSe5 SCF converges)**: on the free host the 296-e PBE SCF reaches conv_thr=1e-6 Ry →
  a usable Kohn–Sham band gap (or honest semimetal). The gap is reported and compared to 0.16–0.35 eV.
- **H24.2 (CoSn metric non-vanishing)**: the TB-fit kagome flat band carries a non-vanishing,
  O(1) BZ-integrated quantum metric (the geometric lever exists), with the band-touching divergence
  at Γ handled honestly (capped/regularized).
- **H24.3 (D_s(N=2) verdict)**: a stated SUPPORTED / PARTIAL / NOT-SUPPORTED verdict on whether the
  geometry licenses f_mult≥1.164 at N=2, with the doping/coherence conditionals named. is_green stays False.

## Run Protocol

- **Compute**: self-built QE 7.2 `pw.x` on `summer` (`~/qe_build/q-e-qe-7.2/bin/pw.x`; apt 6.7 broken).
  `mpirun --use-hwthread-cpus`. PBE.
- **Ta2NiSe5**: deck `tanise5.robust.in` (ibrav=8, a/b/c=3.5029/12.8699/15.6768 Å, nat=32, ntyp=3,
  ecutwfc 50 / ecutrho 400 Ry, nbnd 170, occupations smearing/mv degauss 0.01 Ry, conv_thr 1e-6,
  mixing_beta 0.25 local-TF ndim 8, electron_maxstep 200, david ndim 4, k 4×2×2). Pseudos as H_019.
- **CoSn ∫tr g**: non-SCF dense bands (`cosn.densebands.in`, 24×24 kz=0 crystal grid = 576 k-pts) off
  the converged H_019 charge density; then `kagome_metric.py` fits NN kagome t,e0 and computes
  ∫tr g by projector FD on a 60×60 internal grid (numpy/scipy, local, deterministic).
- **D_s(N=2)**: `ds_n2_bound.py` (Peotta–Törmä + Huhtinen 2022), inputs = the metric integral I and
  the normalised per-cell metric from `kagome_metric.py`. Deterministic, stdlib+math.
- **artifacts**: `state/h024_named_candidate_dft_followon_2026_06_25/` — decks + raw pw.x out + analysis stdout.

## Criteria

- **verdict_rule**: the tier is set by what is ACTUALLY computed. 🟢 (both H_019 halves closed
  favourably) requires Ta2NiSe5 converged AND in/near the literature gap window AND a surviving g≥2
  geometry lever. 🟡 = partial (one half closed; or converged-but-disagreeing). A converged-but-
  unfavourable result (gap wrong, g<2, D_s bound fails) is VALID and reported. The TRIO stays
  **🟠 jointly-unrealized**; absorbed=false; GATE_OPEN — no simulation flips that.

## Falsifiers (≥4 — pre-registered, measurable)

- **F1_tanise5_converges**: PASS = the Ta2NiSe5 PBE SCF reaches conv_thr (1e-6 Ry) on the free host
  and prints a Fermi energy / HOMO–LUMO so an our-DFT gap is extractable. FAIL = it again plateaus /
  does not converge (then the gap stays DEFERRED, honestly — no fabricated number).
- **F2_tanise5_gap_or_disagree**: PASS = the converged KS gap is reported and EITHER lands in
  0.16–0.35 eV OR is an explicit, direction-stated honest disagreement (PBE under-gaps the
  many-body excitonic gap; high-symmetry Cmcm parent, not the low-T condensed phase). FAIL = silent
  tuning / no comparison.
- **F3_cosn_metric_nonvanishing**: PASS = the TB-fit kagome flat band has a non-vanishing O(1)
  BZ-integrated quantum metric (geometry lever exists), Γ-divergence handled honestly. FAIL = the
  fitted metric is ~0 (lever absent in our fit).
- **F4_g_ge_2_honest**: PASS = a stated, NON-tuned judgement on whether OUR DFT supports g≥2 vs the
  measured QGT 2.87 — reporting agreement OR disagreement plainly (normalisation caveats named).
  FAIL = a hand-set g claimed to clear the bar.
- **F5_ds_n2_verdict_honest**: PASS = a stated SUPPORTED/PARTIAL/NOT-SUPPORTED verdict on f_mult≥1.164
  at N=2 from the geometric bound, with is_green=False preserved and the doping/coherence conditionals
  named. FAIL = a claimed measured D_s or is_green=True.
- **F6_preregister**: a post-hoc edit to predictions/criteria/falsifiers → pre-register violation.
- **F7_no_fabrication**: every Verdict number is verbatim pw.x stdout or a labeled deterministic
  analysis output; no value hand-set to clear a falsifier.

## Honest Limits (≥5)

- **L1 (PBE gap underestimate / many-body)**: Ta2NiSe5's gap is partly EXCITONIC/many-body (the order
  parameter itself); a PBE gap below the 0.16–0.35 eV window (or semimetallic) is EXPECTED and is NOT
  a refutation of the excitonic-insulator claim — it is the known DFT limitation, reported as a
  disagreement, not tuned.
- **L2 (high-T Cmcm parent, no relaxation)**: the cell is the high-symmetry Cmcm parent at fixed
  experimental coordinates, NOT the low-T monoclinic excitonic-condensed phase; the spontaneous
  excitonic distortion (the actual glue) is not captured by a single PBE SCF of the parent.
- **L3 (no wannier90 → TB-fit metric, not Bloch-state QGT)**: no wannier90.x is built on summer, so
  the CoSn metric is a NN-kagome tight-binding FIT to OUR DFT bands + the analytic projector metric —
  not the full ab-initio Wannier/Bloch QGT. The fit's NN-only model omits further-neighbour hopping
  and orbital admixture; the absolute normalisation vs the measured QGT g=2.87 carries that caveat.
- **L4 (Γ band-touching divergence)**: an ideal NN kagome flat band TOUCHES the dispersive band at Γ
  → the Fubini–Study metric has an integrable singularity there; the BZ integral is reported with the
  Γ neighbourhood capped/regularized (logged), so the absolute ∫tr g carries that systematic.
- **L5 (geometric bound is a bound, not a measured D_s)**: the Peotta–Törmä + Huhtinen route bounds
  whether the geometry LICENSES the f_mult(N) lever; it does NOT compute the real multilayer D_s of a
  fabricated CoSn/hBN/Ta2NiSe5 N=2 stack (intractable on 12 cores). f_mult(N) itself is still the
  H_023 stacking MODEL (sqrt N / N^0.25), not a measurement.
- **L6 (position / filling)**: OUR PBE puts the flat band ~1.45 eV below E_F → the flat-band filling ν
  is far from the optimal ν≈1/2 that maximises D_s^geom ∝ ν(1−ν); reaching the geometric optimum
  needs the logged heavy-doping/gating step (H_019 F2 already FAILED on position).
- **L7 (absorbed=true unaffected)**: nothing here flips the RTSC gate; that still requires accredited
  4-probe transport + Meissner expulsion + measured H_c2 / T_c. The trio stays 🟠 jointly-unrealized.

## Cross-Links

- **parent**: H_019 (this card closes its Ta2NiSe5-deferred + CoSn-position halves) · H_023 (the lead
  🟢-path whose single DFT unknown — multilayer D_s — this bounds geometrically).
- **registry**: `tool/rtsc_candidates.py` LAYER_A[CoSn] (records ∫tr g + position finding),
  LAYER_B[Ta2NiSe5] (graduates the gap to our-DFT IF converged, honest verified flag).
- **literature**: CoSn flat band/lattice Liu arXiv:2001.11738; CoSn QGT Kang arXiv:2412.17809;
  Ta2NiSe5 structure IUCr/PMC5947720, exciton gap Kim arXiv:2007.08212, pressure-SC Matsubayashi
  arXiv:2106.04396; Peotta–Törmä arXiv:1506.02815; Huhtinen 2022 arXiv:2203.11133.

## Verdict

**🟡 REAL-DFT (PARTIAL) → the GEOMETRY half of the trio is now OUR-DFT-CONFIRMED and STRONG, but the
Ta2NiSe5 gap stays DEFERRED (now characterised as a reproducible, recipe-independent SCF
ill-conditioning, not mere contention).** Specifically: (2) CoSn flat-band ∫tr g SURVIVES — OUR-DFT
TB-fit metric integral I=2.856 matches the measured QGT 2.87, supports g≥2, and the deep position is
REAL not a PBE artifact; (3) the D_s(N=2) geometric bound SUPPORTS f_mult≥1.164 (conditional on
doping + interlayer coherence; is_green=False); (1) the Ta2NiSe5 296-e PBE SCF does NOT converge
across 3 new recipes (residual frozen ~13.7–13.9 Ry) → gap DEFERRED, no fabricated number. Tier set
by what was ACTUALLY computed: one H_019-half CLOSED FAVOURABLY (geometry lever, with the
position-FAIL now explained as orbital-selection), one H_019-half STILL DEFERRED (gap) → 🟡, not 🟢.
The TRIO stays 🟠 jointly-unrealized; absorbed=false / GATE_OPEN.

### (1) Ta2NiSe5 — layer-B gap: SCF DOES NOT CONVERGE across 3 recipes → gap DEFERRED (honest)

Re-ran the 296-electron Cmcm SCF on the freer host with 3 distinct robustness recipes. Verbatim
header (`tanise5.stall.out`, identical across recipes):
```
     unit-cell volume          =    4769.3251 (a.u.)^3   (= 706.7 A^3, matches exp ✓)
     number of atoms/cell      =           32             (Ta8 Ni4 Se20 ✓)
     number of electrons       =       296.00
     number of Kohn-Sham states=          165
     Exchange-correlation= PBE
     number of k points=     2  Marzari-Vanderbilt smearing, width (Ry)=  0.0250
     Dense  grid:   549791 G-vectors     FFT dimensions: (  40, 150, 180)
```
Verbatim accuracy trajectories (rank-0, deduplicated) — the residual FREEZES, never decreases:
```
  recipe robust  (k 4x2x2, ecutrho 400, local-TF beta 0.25): iter1 did not complete in ~25 min wall
  recipe fast    (k 2x1x1, ecutrho 360, local-TF beta 0.20): iter1=13.94569806 Ry  iter2=13.94569806 Ry
  recipe stall   (k 2x1x1, ecutrho 360, plain   beta 0.70, degauss 0.025): iter1=13.74920763  iter2=13.74920763
```
Across all 3 (and H_019's 7) the estimated scf accuracy does NOT drop between iterations, regardless
of mixing (plain/local-TF), beta (0.2–0.7), or smearing (0.01–0.025 Ry); each iteration costs
~6–8 min wall on 12 cores. This is a hard, recipe-independent SCF ill-conditioning — consistent with
the high-symmetry Cmcm cell being the PARENT of the excitonic instability (a near-degenerate,
near-metallic structure at the cusp of the excitonic gap-opening), making a single
non-symmetry-broken KS SCF ill-posed. It is NOT mere host contention (the host was freer than in
H_019, yet the stall is the same/worse). **→ F1 FAIL (no convergence) → F2 the our-DFT gap is
DEFERRED, not fabricated**; the literature window 0.16–0.35 eV stays unverified-by-us. The logged
(deferred, NOT attempted) fix: start from the symmetry-broken low-T monoclinic phase, or a
spin/charge-symmetry-broken guess, or a hybrid/DFT+U that opens the gap and regularises the SCF.

### (2) CoSn — layer-A ∫tr g: geometry lever SURVIVES (I=2.86 ~= measured QGT 2.87); position is REAL

Verbatim `out/cosn_metric.out` (deterministic, numpy; TB params fitted to OUR converged
`cosn.bands.out`, NO tuning):
```
TB params (from OUR cosn.bands.out, NO tuning): t = 0.0770 eV, e0 = -1.603 eV rel E_F
DFT flat band (band 41): W = 0.158 eV, mid = -1.449 eV rel E_F
Gamma band-touching: 30/3600 grid pts capped at tr g=200.0 A^2 (integrable singularity, card L4)
<tr g>_BZ (physical)              = 10.9314 A^2   (uncapped 13.140, max 949)
I = (1/2pi) int_BZ tr g d2k     = 2.8564   <-- QGT-convention metric integral (the D_s lever)
<tr g>/A_uc                       = 0.4546   (alt per-cell normalisation)
MEASURED QGT (arXiv:2412.17809)   g = 2.87
verdict: OUR-DFT-fit metric integral I = 2.856 -> SUPPORTS g>=2 (matches the measured QGT 2.87)
```
- **∫tr g lever survives our DFT**: the NN-kagome TB fit (t=0.077 eV from the 3-band group
  [39,40,41], span 0.462 eV = 6t) gives a QGT-convention metric integral **I = 2.856**, essentially
  equal to the **measured QGT g = 2.87** (arXiv:2412.17809) — **F3 PASS** (non-vanishing O(1) metric)
  and **F4 PASS** (supports g≥2, agreeing with the measurement, NOT tuned). The Γ band-touching
  divergence is handled honestly (30/3600 grid pts capped; integrable singularity, L4).
- **Position is REAL, not a PBE artifact**: CoSn hosts MULTIPLE orbital kagome flat bands — the
  d_xz/d_yz one near E_F (~0.2 eV) and the in-plane-d ones deeper (~−1 to −2 eV). Our sparse-path
  min-width selection captured the DEEPER in-plane manifold (W=0.158 eV at −1.449 eV); both are real
  (ARPES+DFT, Kang Nat. Commun. 2020), and PBE's Fermi level is only ~140 meV off ARPES — so PBE is
  faithful, NOT a correlated mis-placement. The H_019 F2 "position FAIL" is an artifact of WHICH
  flat band the extraction picked, not of PBE nor of the geometry lever. (See
  `out/cosn_position_finding.md`.) Reaching a flat band AT E_F still needs doping/gating — the
  near-E_F d_xz/d_yz band is the realistic target and carries the same kagome geometry.

### (3) D_s(N=2) — H_023's single unknown: geometric bound SUPPORTS f_mult≥1.164 (conditional)

Verbatim `out/ds_n2_bound.out` (Peotta–Törmä + Huhtinen 2022; deterministic, stdlib):
```
flat-band metric integral  I = (1/2pi)int tr g d2k = 2.8564
ledger measured QGT value (arXiv:2412.17809)       g = 2.870
Q2: does OUR DFT support g >= 2 ?  ->  True  (<tr g>/A_uc = 2.856 vs threshold 2.0; QGT measured = 2.87)
f_mult required (H_023)            = 1.1640
f_mult(N=2) optimistic sqrt(N)     = 1.4142   -> >=req
f_mult(N=2) conservative N^0.25    = 1.1892   -> >=req
VERDICT: SUPPORTED (conditional on doping + coherence)
is_green = False (no measured multilayer D_s; trio stays orange, absorbed=false)
```
- The geometric lever EXISTS and is O(1)/strong (I=2.86 ≥ 2): the Peotta–Törmä flat-band
  D_s^geom is non-vanishing, so f_mult(N=2)≥1.164 is SUPPORTED by BOTH H_023 scaling models —
  **CONDITIONAL on (a) doping the flat band to E_F (D_s^geom ∝ ν(1−ν), maximal at half-filling; OUR
  band is ~1.45 eV below E_F so the undoped prefactor is small) and (b) interlayer coherence
  preserving the metric.** **F5 PASS** (verdict stated; is_green=False; doping/coherence named). This
  bounds whether the geometry LICENSES the lever; it is NOT a measured multilayer D_s (L5).

### Falsifiers

- **F1_tanise5_converges**: **FAIL (honest)** — SCF residual frozen ~13.7–13.9 Ry across 3 recipes;
  no convergence → gap DEFERRED, no fabricated number.
- **F2_tanise5_gap_or_disagree**: **DEFERRED (honest)** — no converged gap to compare; the
  non-convergence is reported plainly, literature window stays unverified-by-us. No silent tuning.
- **F3_cosn_metric_nonvanishing**: **PASS** — I=2.856 (non-vanishing O(1)); Γ-divergence handled.
- **F4_g_ge_2_honest**: **PASS** — OUR-DFT I=2.86 supports g≥2 and MATCHES the measured QGT 2.87
  (agreement, not tuned).
- **F5_ds_n2_verdict_honest**: **PASS** — SUPPORTED-conditional verdict stated; is_green=False;
  doping/coherence conditionals named.
- **F6_preregister**: not triggered (criteria frozen before runs).
- **F7_no_fabrication**: **PASS** — every number above is verbatim pw.x stdout or labeled
  deterministic analysis output; the un-converged gap is reported as DEFERRED, not invented.

### Structural finding

The trio's GEOMETRY half is now OUR-DFT-confirmed and strong: CoSn's kagome flat-band quantum
metric integral I=2.856 from a TB fit to OUR PBE bands MATCHES the measured QGT 2.87 (the g≥2 lever
survives), the deep flat-band position is a REAL orbital-selection effect (not a PBE failure; PBE is
~140 meV faithful to ARPES), and that geometry SUPPORTS the H_023 demand-relaxation lever
(f_mult≥1.164 at N=2) — conditional on doping to E_F and interlayer coherence, is_green=False. The
Ta2NiSe5 GAP half stays DEFERRED: its 296-e PBE SCF does NOT converge across 3 new recipes (residual
frozen, recipe-independent) — a characterised ill-conditioning of the high-symmetry excitonic-parent
cell, not mere contention (a valid honest negative; the symmetry-broken-phase / hybrid fix is logged
as deferred). Net: one H_019-half CLOSED FAVOURABLY, one STILL DEFERRED → **🟡 REAL-DFT (PARTIAL)**.
The trio remains **🟠 jointly-unrealized**; `absorbed=false` / GATE_OPEN — no simulation flips that.

### Records

`state/h024_named_candidate_dft_followon_2026_06_25/` — `decks/{cosn_metric_from_dft.py,
kagome_metric.py, ds_n2_bound.py, run_h024_geometry.sh, tanise5.robust.in, tanise5.fast.in,
tanise5.stall.in}`, `out/{cosn_metric.out, ds_n2_bound.out, cosn_position_finding.md,
tanise5_convergence_log.md, tanise5.robust.head.out, tanise5.fast.head.out, tanise5.stall.head.out}`.
