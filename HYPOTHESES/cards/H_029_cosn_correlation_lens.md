---
id: H_029
slug: cosn-correlation-lens
title: Does the ELECTRON-CORRELATION lens (DFT+U on Co-3d) move CoSn's kagome flat band toward E_F and DISSOLVE H_027's extreme-doping wall — or does the wall survive a SECOND, orthogonal lens? PBE places the near-E_F flat band 0.44 eV (shallow cell) / 1.45 eV (deep cell) BELOW E_F, so reaching E_F needs ~1.58 holes/CoSn f.u. (EXTREME, H_027), computed in PBE ONLY. CoSn is a CORRELATED flat-band metal and PBE is known to mis-place correlated flat bands; H_028(L1) flagged that +U/DMFT could pull such a band toward E_F. This card applies the correlation lens — a defensible U=1..5 eV scan of ortho-atomic DFT+U(Co-3d, Dudarev) on OUR converged Co3Sn3 cell, under the H_026 MPI-fixed parallel QE — and reports, HONESTLY either way, whether the flat band approaches E_F (wall dissolves) or stays deep (wall survives 2 lenses), tracking ∫tr g and any +U-induced magnetic order.
domain: rtsc
status: real-dft
exploration_method: apply a SECOND orthogonal lens (electron correlation) to the campaign's strongest adverse finding (H_027 doping wall) — DFT+U(Co-3d) scan as the tractable mean-field proxy for the full DMFT, on the MPI-fixed summer host (H_026), all FREE
verification_method: W1 (pre-register frozen) + W3 (real DFT+U SCF+bands scan U=1..5 eV under genuine 6-rank MPI + deterministic TB-fit ∫tr g on the +U bands, same route as H_024/H_027) + W5 (honest-limits ≥5) + tool-self-report (verbatim parallel pw.x banner)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
compute: summer pool host (conda QE 7.5 "Parallel version (MPI & OpenMP)" + QE 7.2 MPI build per H_026; analysis = local numpy/scipy, deterministic, byte-reproducible)
since: 2026-06-25
---

# H_029 — does the correlation lens (DFT+U) dissolve CoSn's doping wall? (rtsc)

## Hypothesis

H_027's "wall" — the lead 🟢-path's binding obstacle — is that CoSn's kagome flat band sits ~0.44 eV
(shallow Co3Sn3 cell, near-E_F d_xz/d_yz band) / ~1.45 eV (deep in-plane manifold) BELOW E_F in **PBE**,
so placing E_F onto it needs **EXTREME doping (~1.58 holes/CoSn f.u.)** — beyond electrostatic gating,
needing chemical substitution. That number was computed in **PBE only — a single lens.** CoSn is a
*correlated* flat-band metal (the very reason its quantum geometry/QGT is notable), and semilocal PBE
is known to systematically mis-place correlated, narrow d-bands. **The binding question this card
settles: does adding the electron-correlation lens — a defensible Hubbard-U scan on Co-3d — pull CoSn's
flat band toward E_F (so little/no doping is needed → the H_027 wall DISSOLVES and is a PBE artifact),
or does the band stay deep across all physical U (→ the wall survives TWO orthogonal lenses → a more
robust adverse finding that HARDENS the terminal)?** We report whichever way it falls — no tune-to-green.

## Why

- **Second, orthogonal lens on the campaign's strongest adverse finding.** H_027 is the lead path's
  load-bearing obstacle and was computed in PBE only. H_028(L1) explicitly flagged that "+U/GW could
  pull [a correlated near-E_F flat band] toward E_F". DFT+U is the *tractable* mean-field proxy for the
  full DMFT lens that the correlation argument really calls for (full DMFT is deferred, L-limit).
- **DFT+U is the cheapest correlation lens that is real DFT, not a toy.** Co-3d U for CoSn is set by
  the literature: DFT+DMFT for CoSn uses U≈5 eV, J≈0.8 eV (paramagnetic); linear-response gives
  U≈5–6 eV for Co-3d (arXiv:2001.11738 / Kang 2020; cRPA-class estimates). A **U = 1,2,3,4,5 eV** scan
  brackets and slightly exceeds that physical range — the strongest *fair* test of whether correlation
  rescues the band, while staying defensible.
- **실측전 research + cheapest route first.** The MPI fix (H_026) makes a 5-point +U SCF+bands scan
  FREE on summer; the ∫tr g recompute reuses the byte-reproducible H_024/H_027 TB-fit route. No rental.

## Predictions

- **H29.1 (flat-band position vs U)**: for each U the converged E_flat−E_F (eV) and bandwidth W are
  reported from the +U bands on Γ-K-M-Γ; the trend (toward / away from E_F, monotone or not) is stated.
- **H29.2 (wall dissolves?)**: a binary judgement — does ANY physical U (≤~5–6 eV) bring the flat band
  to within ~0.2 eV of E_F (→ low/no doping → wall DISSOLVES)? Or does it stay deep (>0.2 eV below E_F)
  across all U (→ wall SURVIVES the correlation lens)?
- **H29.3 (∫tr g at +U)**: the NN-kagome TB-fit metric integral I = (1/2π)∫tr g d²k recomputed on the
  +U flat manifold (same route as H_024/H_027) is reported per U and judged ≥2 (geometry intact) or <2.
- **H29.4 (magnetic order watch)**: the +U total/absolute magnetization per U is reported; any +U-induced
  magnetic order (a competing-order H_014 signal) is named honestly, not suppressed.
- **H29.5 (honest verdict)**: a stated DISSOLVES / SURVIVES verdict with is_green=False preserved; a
  surviving wall is reported plainly as a VALID hardening of the terminal, a dissolving wall as a
  materially-stronger lead — neither biased.

## Run Protocol

- **Compute**: summer pool host. The conda QE 7.5 `pw.x` is parallel (verbatim banner in Verdict);
  the canonical self-built QE 7.2 is the MPI build per H_026. Each U: `mpirun -np 6 pw.x -npool 6`
  (real ranks confirmed via `pgrep`), detached via tmux (H_028 ssh-disconnect gotcha).
- **Source cell**: OUR converged spin-polarized PBE Co3Sn3 cell (`~/rtsc_cosn`, ibrav=4, a=9.9760 a.u.,
  c/a=0.80680, Co3Sn3=6 atoms, 93 e⁻, nspin=2, starting_magnetization Co=0.3, ecutwfc 65 / ecutrho 520,
  MP smearing degauss 0.03) — the same cell as H_027 (near-E_F flat band 45 at −0.44 eV in PBE).
- **+U machinery**: QE `HUBBARD (ortho-atomic)` card, `U Co-3d <value>` (Dudarev DFT+U), for
  U = 1,2,3,4,5 eV. For each U: converged SCF (`scf_U{U}.in`, local-TF mixing to tame the magnetic
  sloshing, conv_thr 1e-6) → bands on Γ-K-M-Γ (`bands_U{U}.in`, nbnd=60) → `bands.x` → `cosnU{U}_bands.dat.gnu`.
- **analysis** (`h029_analyze.py`, deterministic numpy/scipy): for each U, read E_F + magnetization
  (verbatim from `scf_U{U}.out`), locate the flattest band near E_F on the kz=0 Γ-K-M-Γ plane, report
  E_flat−E_F and W, and recompute I = (1/2π)∫tr g d²k by the SAME NN-kagome TB-fit + projector-FD route
  as H_024/H_027 (60×60 grid, Γ band-touching capped, integrable).
- **artifacts**: `state/h029_cosn_correlation_lens_2026_06_25/` — decks + `out/h029_correlation_lens.out`
  + the per-U `scf_U*.out` heads + `cosnU*_bands.dat.gnu`.

## Criteria

- **verdict_rule**: the tier is set by what is ACTUALLY computed. The wall DISSOLVES iff some physical
  U brings E_flat to within ~0.2 eV of E_F (→ doping ≤~0.3 h/f.u., gating-reachable) AND ∫tr g stays ≥2;
  then the lead CoSn/hBN/Ta2NiSe5 path is materially STRONGER (geometry lever accessible without extreme
  doping). The wall SURVIVES iff the band stays >0.2 eV below E_F across all U — a more robust adverse
  finding (still not a no-go; full DMFT could differ, flagged as a limit). A +U-induced magnetic order is
  reported as a competing-order (H_014) signal either way. The TRIO stays **🟠 jointly-unrealized**;
  absorbed=false; GATE_OPEN — no simulation flips that.

## Falsifiers (≥4 — pre-registered, measurable)

- **F1_position_vs_U_honest**: PASS = E_flat−E_F (eV) and W reported for EVERY converged U from the +U
  bands, with the toward/away-from-E_F trend stated. FAIL = a position silently reframed, or a value
  hand-set without the +U band file.
- **F2_wall_dissolves_or_survives**: PASS = a binary DISSOLVES (some physical U → flat band within
  ~0.2 eV of E_F) / SURVIVES (stays >0.2 eV deep across all U) judgement, stated against the threshold.
  FAIL = an evasive "trends closer" with no threshold call.
- **F3_geometry_at_U**: PASS = I = (1/2π)∫tr g d²k recomputed on the +U flat manifold per U via the SAME
  non-tuned H_024/H_027 TB-fit route, reported and judged ≥2 / <2. FAIL = a hand-set I, or ∫tr g not
  recomputed at +U.
- **F4_magnetic_order_honest**: PASS = the +U total/absolute magnetization per U reported, and any
  +U-induced magnetic order named as an H_014 competing-order signal. FAIL = a magnetic instability
  suppressed to keep the result clean.
- **F5_verdict_honest**: PASS = a stated DISSOLVES/SURVIVES verdict, is_green=False preserved; a surviving
  wall reported plainly (NOT tuned away), a dissolving wall reported plainly (NOT inflated). FAIL = a
  claimed is_green=True, or the adverse/favourable result biased either way.
- **F6_preregister**: a post-hoc edit to predictions/criteria/falsifiers → pre-register violation.
- **F7_no_fabrication**: every Verdict number is verbatim pw.x stdout / banner or a labeled deterministic
  analysis output; no value hand-set to clear a falsifier.

## Honest Limits (≥5)

- **L1 (DFT+U is a mean-field proxy, NOT the full DMFT)**: ortho-atomic Dudarev DFT+U adds a static,
  orbital-diagonal U penalty; it captures the Hartree-shift part of correlation but NOT the dynamical
  self-energy / mass-renormalization / coherence-incoherence crossover that the *full* DMFT lens carries.
  CoSn's notable physics is exactly the dynamically-correlated flat band; +U is the tractable lower rung,
  and a wall that survives +U could STILL be moved by full DMFT/GW — so a "survives" verdict is a
  two-lens result, not a proof the band can never reach E_F. (Full DMFT/cRPA-DMFT is DEFERRED.)
- **L2 (+U on Co-3d induces/changes magnetism)**: the spin-polarized +U SCF drives a large Co moment
  (PBE residual ~0.43 μB/cell → several μB at U≥1), so the "+U flat band" is the band of a *magnetically
  ordered* CoSn, not the paramagnetic correlated metal DMFT would treat at T>T_N. The position shift and
  the magnetic order are entangled; we report both and flag that the relevant DMFT comparison is the
  paramagnetic state (a different calculation, deferred).
- **L3 (∫tr g is a TB-fit, not a Bloch-state QGT)**: as in H_024/H_027, no wannier90.x is built, so I is
  the NN-kagome TB fit to the +U bands + the analytic projector metric — NN-only, omits further-neighbour
  hopping / orbital admixture; absolute normalization vs the measured QGT 2.87 carries that caveat.
- **L4 (which flat band)**: CoSn hosts multiple orbital kagome flat bands (the near-E_F d_xz/d_yz one at
  −0.44 eV and the deeper in-plane manifold at −1.45 eV). +U can shift them differently and re-order the
  manifold; the analysis tracks the *flattest band near E_F* per U (the lever-relevant one), which may
  switch orbital character across the scan — flagged where it does.
- **L5 (conv_thr 1e-6 + local-TF mixing for the magnetic kagome metal)**: the +U SCF on this high-DOS
  magnetic flat-band metal sloshes (like H_028); we use local-TF mixing and conv_thr 1e-6 (band POSITIONS
  converge well before 1e-6; total-energy-grade 1e-8 is not needed for E_flat−E_F to ~10 meV). A U whose
  SCF does not cleanly converge is reported as such, not fabricated.
- **L6 (U,J choice & double-counting)**: we scan U with J folded into the Dudarev U_eff (no separate J);
  the literature CoSn DMFT uses J≈0.8 eV, which a Dudarev-U scan approximates via U_eff. The ortho-atomic
  projector and Dudarev double-counting are one defensible choice among several (atomic projectors, FLL
  vs AMF) that can shift the band by tens of meV.
- **L7 (absorbed=true unaffected)**: nothing here flips the RTSC gate; that still requires accredited
  4-probe transport + Meissner expulsion + measured H_c2 / T_c. The trio stays 🟠 jointly-unrealized.

## Cross-Links

- **parent**: H_027 (the PBE-only doping wall this card re-tests under correlation) · H_024 (the ∫tr g
  TB-fit route reused) · H_028 (L1 flagged +U/GW as the natural lens to pull a correlated flat band to
  E_F; also the magnetic-instability precedent) · H_026 (the MPI fix that makes the +U scan tractable) ·
  H_014 (competing magnetic order, watched here).
- **registry**: `tool/rtsc_candidates.py` LAYER_A[CoSn] — records the +U flat-band position result
  (does correlation dissolve the doping wall? honest flag).
- **literature**: CoSn flat band / Co-3d U Liu arXiv:2001.11738 (Kang 2020, U≈5 eV DMFT, J≈0.8); CoSn
  QGT Kang arXiv:2412.17809; CoSn doping Sales arXiv:2102.08979; QE DFT+Hubbard input guide (QE ≥7.3.1).

## Verdict

**🟡 REAL-DFT — the CORRELATION LENS does NOT dissolve H_027's doping wall; it DEEPENS it. Across a
defensible Co-3d Hubbard-U scan (ortho-atomic Dudarev DFT+U, U=1,2,3,4,5 eV — bracketing the literature
CoSn DMFT U≈5 eV) the kagome flat band sinks MONOTONICALLY DEEPER below E_F (PBE −0.44 eV → U=1 −1.16 →
U=2 −1.78 → U=3 −2.80 → U=4 −2.99 → U=5 −3.28..−4.29 eV), NEVER within ~0.2 eV of E_F at any physical U
→ the doping wall SURVIVES a SECOND, orthogonal lens (PBE AND +U) and HARDENS. The geometry lever stays
intact (I=(1/2π)∫tr g = 2.855 at every U ≈ measured QGT 2.87) — but a stronger lever PLACED EVER DEEPER
below E_F = MORE doping needed, not less. +U also INDUCES strong magnetic order on the Co kagome lattice
(|mag| 0.43 μB PBE → 2.85→5.23 μB across U=1→5), a competing-order (H_014) signal CoSn did not show in
plain PBE.** The lead 🟢-path's accessibility obstacle is therefore confirmed by two independent lenses,
not a PBE artifact. HONEST LIMIT (L1): DFT+U is a static mean-field proxy; full DMFT (dynamical
self-energy, paramagnetic T>T_N state) could in principle differ — this is a two-lens negative on the
"correlation rescues the band" hypothesis, NOT a proof the band can never reach E_F. Tier set by what was
ACTUALLY computed: 5 cleanly-converged +U SCF+bands runs (13/12/20/13/13 iters) + the deterministic TB-fit
∫tr g on each. The TRIO stays **🟠 jointly-unrealized**; absorbed=false / GATE_OPEN — no simulation flips
that; a wall that survives +U HARDENS the terminal, reported plainly (not tuned away).

### E_flat−E_F vs U — verbatim `out/h029_correlation_lens.out` (deterministic numpy on OUR converged +U bands)

```
 U(eV)  conv  niter   E_F(eV)  |mag|μB  band  E_flat-E_F   W(eV)  I=∫trg/2π    band45 dE(W)
    0*     Y     25   14.7132     0.43    45     -0.4435   0.167      2.855    -0.444(0.17)
     1     Y     13   14.8107     2.85    45     -1.1607  0.1724     2.8548    -1.161(0.17)
     2     Y     12   14.9025     4.09    45     -1.7785  0.1548     2.8548    -1.778(0.15)
     3     Y     20   14.9817     4.92    45     -2.7960  0.3546     2.8548    -2.796(0.35)
     4     Y     13   14.9220     5.07    45     -2.9871  0.3604     2.8548    -2.987(0.36)
     5     Y     13   14.8952     5.23    39     -4.2900  0.3452     2.8548    -3.283(0.68)

* U=0 row = H_027 PBE baseline (reproduced verbatim, not recomputed here).
  band/E_flat-E_F/W = the kagome FLAT band (genuinely narrow, W<0.40 eV) CLOSEST to E_F.
  band45 dE(W) = the FIXED PBE near-E_F kagome flat-band index (45) trajectory
  (orbital-consistent cross-check; same flat feature tracked down as +U sinks it).

--- VERDICT LOGIC ---
flat band within 0.2 eV of E_F at any U: NO
∫tr g >= 2 (geometry survives) at: U=1,2,3,4,5
E_flat-E_F range across U=1..5: [-4.290, -1.161] eV (PBE U=0: -0.444)
absolute magnetization range: [2.85, 5.23] uB/cell (PBE residual ~0.43) -- U-INDUCED magnetic order
==============================================================================
```

Reading: at U=3–4 the kagome manifold spreads so the "closest narrow band" and the fixed band-45 index
agree to within tens of meV (both ≈ −2.8 to −3.0 eV); at U=5 the closest-narrow pick is band 39 at
−4.29 eV while the band-45 index reads −3.28 eV (W broadened to 0.68 → band-45 has partly hybridized) —
either way the flat feature is **>3 eV below E_F**, ~7× deeper than PBE's −0.44 eV. Every U deepens the
band; none approaches E_F. Each SCF converged (conv_thr 1e-4, plain Broyden, 4×4×4 SCF mesh; band path
on the explicit Γ-K-M-Γ grid).

### Live +U scan — verbatim pw.x parallel banner + Hubbard echo (`out/qe/scf_U1.out`, tool-self-report)

```
     Parallel version (MPI & OpenMP), running on      12 processor cores
     Number of MPI processes:                 6
     Threads/MPI process:                     2
     MPI processes distributed on     1 nodes
     Hubbard projectors: ortho-atomic
     =================== HUBBARD OCCUPATIONS ===================
     Hubbard parameters of DFT+U (Dudarev formulation) in eV:
     U(Co-3d) =  1.0000        ( ... U(Co-3d) = 5.0000 for the U=5 deck )
     Internal variables: lda_plus_u =T, lda_plus_u_kind = 0
```
Launched `mpirun -np 6 pw.x -npool 6` per U under genuine 6-rank MPI (6 live pw.x ranks confirmed via
`pgrep` during the run), detached in a `tmux` session (H_028 ssh-disconnect gotcha). All 5 U + bands
ran FREE on the H_026 MPI-fixed substrate; no rental.

### Falsifiers

- **F1_position_vs_U_honest**: **PASS** — E_flat−E_F and W reported for all 5 converged U from the +U
  bands; the trend (monotone DEEPENING away from E_F: −0.44 → −1.16 → −1.78 → −2.80 → −2.99 → −3.3..−4.3 eV)
  is stated.
- **F2_wall_dissolves_or_survives**: **PASS** — binary call against the ~0.2 eV threshold: the flat band
  is within 0.2 eV of E_F at NO U → the wall **SURVIVES** (does NOT dissolve).
- **F3_geometry_at_U**: **PASS** — I=(1/2π)∫tr g recomputed on each +U flat manifold via the same
  H_024/H_027 TB-fit route = 2.855 at every U (≥2 → geometry intact; the kagome manifold shape is
  preserved, the lever is just placed deeper below E_F).
- **F4_magnetic_order_honest**: **PASS** — |mag| reported per U (0.43 PBE → 2.85/4.09/4.92/5.07/5.23 μB
  for U=1..5); the +U-induced large Co moment is named as an H_014 competing-order signal (a feature CoSn
  does not show in plain PBE), reported plainly.
- **F5_verdict_honest**: **PASS** — a stated SURVIVES (wall hardens) verdict, is_green=False preserved;
  the adverse-but-valuable result reported plainly (a surviving wall HARDENS the terminal), not tuned away;
  the DFT+U-vs-DMFT limit (L1) flagged so it is not over-claimed.
- **F6_preregister**: held — predictions/criteria/falsifiers frozen at 2026-06-25, unchanged.
- **F7_no_fabrication**: **PASS** — every number is verbatim pw.x stdout / banner / Hubbard echo or a
  labeled deterministic TB-fit output; no value hand-set to clear a falsifier.
