---
id: H_027
slug: doped-cosn-geometry-survival
title: Does CoSn's kagome flat-band GEOMETRY LEVER (and the D_s∝ν(1−ν) superfluid weight) SURVIVE the DOPING required to bring the flat band onto E_F? From OUR converged spin-polarized PBE bands (now under the H_026 MPI-fixed QE) we measure (1) the rigid-band hole concentration to slide E_F onto the near-E_F flat band = 4.73 e/cell = 1.58 holes/CoSn f.u. (EXTREME, beyond gating), (2) ∫tr g at that doped E_F = 2.855 (≈ measured QGT 2.87 → geometry SURVIVES under rigid-band), (3) the flat-band filling ν = 0.507 → ν(1−ν) = 0.250 = the FAVOURABLE half-filling maximum. Verdict: the geometry + filling are FAVOURABLE *if reachable*, but the doping to reach E_F is EXTREME — the lead 🟢-path is WEAKENED on accessibility, not on geometry. Trio stays 🟠 / absorbed=false.
domain: rtsc
status: real-dft
exploration_method: close the LAST computationally-settleable risk on the lead 🟢-path — does the CoSn geometry lever survive the doping-to-E_F it requires — on the now-MPI-fixed summer host (H_026), all FREE
verification_method: W1 (pre-register frozen) + W2 (falsifier-6) + W3 (deterministic DFT analysis on OUR converged PBE bands + a live MPI doped-SCF cross-check) + W5 (honest-limits-7) + tool-self-report (verbatim pw.x parallel banner)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
compute: summer pool host (QE 7.2 MPI build per H_026, and conda QE 7.5; analysis = local numpy/scipy, deterministic, byte-reproducible)
since: 2026-06-25
---

# H_027 — does CoSn's flat-band geometry lever survive the doping-to-E_F? (rtsc)

## Hypothesis

The lead 🟢-path (H_023 demand-relaxation, leaning on H_001/H_024's CoSn geometry lever) needs
CoSn's narrow kagome flat band to be AT E_F to use it as the superfluid-weight lever
(D_s^geom ∝ ν(1−ν) · ∫tr g). H_024 found the flat band sits BELOW E_F, so E_F must be moved onto it
by DOPING. **The binding question: does the geometry lever (∫tr g) AND the favourable filling
(ν≈1/2, where D_s^geom is maximal) SURVIVE the doping required to bring the flat band to E_F — or is
the required doping so extreme (or does it so distort the band) that the lever is killed or ν pushed
to a D_s-suppressing edge?** D_s^geom ∝ ν(1−ν) vanishes at the band edges (ν→0,1) and is maximal at
half-filling; ∫tr g is the geometric prefactor. We measure all three from OUR converged PBE bands on
the now-MPI-fixed host (H_026), with a live doped SCF as a (non-rigid-band) cross-check.

## Why

- **Last computationally-settleable risk on the 🟢-path.** H_024 confirmed the geometry lever exists
  (∫tr g = 2.86 ≈ measured QGT 2.87) but BELOW E_F, and explicitly deferred the doping question as a
  conditional ("conditional on doping to E_F"). H_026 fixed the MPI infra wall, so a real doped SCF is
  now tractable. This card settles whether that conditional is cheap or expensive.
- **D_s^geom ∝ ν(1−ν) is the physics gate.** Even with a perfect geometry (∫tr g≥2), if the doping
  pushes ν to a band edge the superfluid weight is suppressed; the lever's value depends jointly on
  ∫tr g AND on landing ν near 1/2. Both must be checked.
- **실측전 research + cheapest route first.** The deterministic rigid-band analysis of OUR already-
  converged spectrum answers the doping/ν/geometry questions with no new rental and is byte-
  reproducible; the live doped SCF is the (slower, non-rigid-band) cross-check on top.

## Predictions

- **H27.1 (doping magnitude)**: the rigid-band hole concentration to slide E_F onto the flat-band
  centre is reported in e/cell AND holes/CoSn formula unit, and judged PHYSICAL (≲0.3 h/f.u., gating
  reach), STRETCH (0.3–0.7), or EXTREME (>0.7, needs chemical substitution).
- **H27.2 (∫tr g at the doped E_F)**: the flat-band metric integral I = (1/2π)∫tr g d²k, recomputed
  by the H_024 TB-fit-to-PBE route, is reported and judged ≥2 (lever survives) or <2 (lever killed),
  with the rigid-band-vs-real-doping caveat named.
- **H27.3 (filling ν & D_s∝ν(1−ν))**: the flat-band filling ν when E_F sits on it is reported, and
  ν(1−ν) compared to the favourable 0.25 maximum (FAVOURABLE near ν=0.5, EDGE-SUPPRESSED at ν→0/1).
- **H27.4 (honest verdict)**: a stated SURVIVES / WEAKENED / KILLED verdict on the geometry lever
  under the doping-to-E_F requirement, with is_green=False preserved. If the required doping is
  extreme or distorts the band, that adverse result is reported plainly, NOT tuned away.

## Run Protocol

- **Compute**: summer pool host. The self-built QE 7.2 is now an MPI build (H_026) and a parallel
  QE 7.5 is in the conda env; the live doped SCF uses `mpirun -np 6 pw.x -npool 2` (verbatim banner in
  the Verdict). The deterministic analysis is local numpy/scipy.
- **Source bands**: OUR converged spin-polarized PBE SCF of the full CoSn cell (`~/rtsc_cosn/scf.out`,
  ibrav=4 hexagonal a=9.9760 a.u. c/a=0.80680, Co3Sn3=6 atoms, 93 e⁻, nspin=2,
  starting_magnetization Co=0.3, ecutwfc 65 / ecutrho 520 Ry, MP smearing degauss 0.03, conv_thr
  1e-8 — converged in 25 iters, E_F=14.7132 eV, residual total magnetization 0.43 μ_B/cell) + its
  Γ-K-M-Γ band path (`cosn_bands.dat.gnu`, 60 bands × 161 k).
- **(1) doping**: `h027_doped_geometry.py` integrates the smeared occupation over OUR converged SCF
  eigenvalue spectrum (both spins, k-weighted) and finds Δn = N(E_F) − N(E_flat) = the rigid-band
  holes to put E_F on the flat-band centre; converted to holes/f.u. (3 f.u./cell).
- **(2) geometry**: the same script fits an NN-kagome 3-orbital TB model (t, e0) to the flat 3-band
  manifold of OUR bands and computes I = (1/2π)∫tr g d²k by projector finite-difference on a 60×60
  grid (Γ band-touching capped, integrable — same route as H_024).
- **(3) filling**: the script integrates the smeared occupation of ONLY the flat band at the doped E_F
  to get ν, then ν(1−ν).
- **cross-check (non-rigid-band)**: a live hole-doped SCF (`scf_h4p0.in`, tot_charge=4.0, robust
  recipe β=0.2 degauss=0.04) under genuine MPI, to test whether REAL doping (which can hybridize /
  spin-split the manifold) preserves the rigid-band picture.
- **artifacts**: `state/h027_doped_cosn_geometry_survival_2026_06_25/` — decks + `out/h027_geometry.out`.

## Criteria

- **verdict_rule**: the tier is set by what is ACTUALLY computed. The geometry lever SURVIVES iff
  I≥2 AND ν near 0.5 at the doped E_F; the lead path is then "robust on geometry" — BUT the doping
  MAGNITUDE is a separate accessibility axis (an extreme doping WEAKENS the path even if the geometry
  survives). A geometry-survives-but-doping-extreme outcome is a VALID adverse result and is reported
  as a WEAKENING of the lead path, not tuned to keep it alive. The TRIO stays **🟠 jointly-unrealized**;
  absorbed=false; GATE_OPEN — no simulation flips that.

## Falsifiers (≥4 — pre-registered, measurable)

- **F1_doping_magnitude_honest**: PASS = the rigid-band hole concentration to put E_F on the flat band
  is reported in e/cell AND holes/f.u. with an explicit PHYSICAL/STRETCH/EXTREME judgement against
  stated thresholds. FAIL = no number, or a magnitude silently reframed to look reachable.
- **F2_geometry_survives_or_not**: PASS = I = (1/2π)∫tr g d²k at the flat band is reported and judged
  ≥2 (survives) or <2 (killed), via the same non-tuned TB-fit route as H_024, with the rigid-band-vs-
  real-doping caveat named. FAIL = a hand-set I claimed to clear 2.
- **F3_filling_nu_honest**: PASS = the flat-band filling ν at the doped E_F is reported and ν(1−ν)
  compared to the 0.25 maximum, with a FAVOURABLE/MODERATE/EDGE-SUPPRESSED judgement. FAIL = ν not
  computed, or a favourable ν asserted without the occupation integral.
- **F4_verdict_honest**: PASS = a stated SURVIVES/WEAKENED/KILLED verdict on the geometry lever under
  the doping-to-E_F requirement, is_green=False preserved, an extreme/adverse doping reported plainly.
  FAIL = a claimed is_green=True, or the adverse doping result suppressed to keep the lead path alive.
- **F5_doped_scf_crosscheck_honest**: PASS = the live (non-rigid-band) doped SCF outcome is reported
  honestly — whether it converges and confirms/contradicts the rigid-band picture, OR (the equally
  valid negative) is shown to be hard to stabilize / non-converging (itself evidence the doped flat-
  band metal is delicate). FAIL = a fabricated converged doped E_F / magnetization.
- **F6_preregister**: a post-hoc edit to predictions/criteria/falsifiers → pre-register violation.
- **F7_no_fabrication**: every Verdict number is verbatim pw.x stdout / banner or a labeled
  deterministic analysis output; no value hand-set to clear a falsifier.

## Honest Limits (≥5)

- **L1 (rigid-band is an approximation)**: tasks (1)–(3) slide a FIXED converged spectrum's chemical
  potential; they do NOT self-consistently relax the charge density at the doped filling. Real doping
  can hybridize, spin-split, or shift the flat manifold — so the rigid-band I and ν are the
  geometry-PRESERVED best case; the live doped SCF (F5) is the partial corrective, and it is slow/
  delicate for this high-DOS flat-band metal (itself a caveat).
- **L2 (∫tr g is a TB-fit, not a Bloch-state QGT)**: no wannier90.x is built, so I is the NN-kagome
  TB fit to OUR PBE bands + the analytic projector metric (H_024 route, L3 there) — NN-only, omits
  further-neighbour hopping/orbital admixture; the absolute normalisation vs the measured QGT 2.87
  carries that caveat. The geometry is also formally E_F-shift invariant under rigid-band, so I
  "surviving" means "the band manifold's metric is unchanged IF doping is rigid-band" — not a proof
  it survives a real, hybridizing dopant.
- **L3 (ν≈0.5 at the band CENTRE is partly by construction)**: placing E_F at the flat-band centre
  gives ν≈1/2 almost tautologically (centre of a band = half-filled); the load-bearing finding is not
  "ν is favourable" per se but that the DOPING to reach that centre is extreme. We report ν at the
  centre AND at the band top/bottom so the ν-sensitivity is visible, and flag this construction.
- **L4 (magnetic PBE CoSn)**: OUR SCF is spin-polarized and converges with a small residual moment
  (0.43 μ_B/cell, from starting_magnetization Co=0.3); CoSn's magnetism in PBE is functional- and
  doping-sensitive, and the flat band can spin-split — the rigid-band single-spectrum picture
  averages over this. A doped, possibly-magnetic flat-band metal is exactly where rigid-band is least
  safe (L1).
- **L5 (high DOS → large carrier count is real, not an error)**: the ~4.7 e/cell to move E_F by only
  ~0.44 eV is a DIRECT consequence of the flat band's huge DOS (the rigid-band sweep shows DOS rising
  5→17 states/eV/cell as E_F approaches the flat band) — the dense manifold itself absorbs the
  carriers. This is physically correct, and is precisely WHY the doping is extreme; it is not a
  sampling artifact.
- **L6 (different cell from H_019/H_024)**: this card uses the fuller spin-polarized Co3Sn3 hexagonal
  cell (`~/rtsc_cosn`, near-E_F flat band at −0.44 eV) rather than the H_019/H_024 cell (which
  reported the DEEPER in-plane manifold at −1.45 eV). Both are real CoSn flat bands (CoSn hosts
  multiple orbital kagome flat bands; H_024 Records); this card targets the SHALLOWER, near-E_F
  d_xz/d_yz band that H_024 named as the realistic doping target — the relevant one for the lever.
- **L7 (absorbed=true unaffected)**: nothing here flips the RTSC gate; that still requires accredited
  4-probe transport + Meissner expulsion + measured H_c2 / T_c. The trio stays 🟠 jointly-unrealized.

## Cross-Links

- **parent**: H_024 (confirmed the geometry lever ∫tr g=2.86 below E_F and DEFERRED the doping
  conditional this card settles) · H_023 (the lead 🟢-path whose D_s∝ν(1−ν) lever this tests under
  real doping) · H_026 (fixed the MPI infra wall that makes the live doped SCF tractable).
- **registry**: `tool/rtsc_candidates.py` LAYER_A[CoSn] — records the doping-to-E_F magnitude + the
  geometry/ν survival flags.
- **literature**: CoSn flat band Liu arXiv:2001.11738; CoSn QGT Kang arXiv:2412.17809; Peotta–Törmä
  arXiv:1506.02815; Huhtinen 2022 arXiv:2203.11133.

## Verdict

**🟡 REAL-DFT — the GEOMETRY LEVER and the FAVOURABLE FILLING SURVIVE the doping (rigid-band), but the
DOPING REQUIRED to reach E_F is EXTREME (~1.58 holes/CoSn f.u.) → the lead 🟢-path is WEAKENED on
ACCESSIBILITY, not on geometry.** Specifically, from OUR converged spin-polarized PBE bands: (1) the
near-E_F kagome flat band (band 45, W=0.167 eV, −0.44 eV below E_F) needs Δn = 4.73 e⁻/cell =
**1.58 holes per CoSn formula unit** of rigid-band hole doping to bring E_F onto it — **EXTREME**,
beyond electrostatic gating, requiring full chemical substitution; (2) at that doped E_F the flat-band
metric integral **I = 2.855 ≈ measured QGT 2.87** → geometry **SURVIVES** (I≥2) under the rigid-band
assumption; (3) at E_F-on-flat-band the filling **ν = 0.507 → ν(1−ν) = 0.250 = the FAVOURABLE
half-filling maximum** (D_s^geom strongest). So the geometry and ν are the best case *if E_F could be
placed there* — but the carrier count to place it is unphysical for gating. Tier set by what was
ACTUALLY computed: a clean deterministic rigid-band result on OUR converged bands (geometry+ν favourable,
doping extreme); the live doped SCF cross-check is delicate (high-DOS flat-band metal, slow under MPI;
the prior tot_charge=2 run MPI_ABORTed) — itself evidence the doped state is hard to stabilize. The
TRIO stays **🟠 jointly-unrealized**; absorbed=false / GATE_OPEN — no simulation flips that.

### (1)+(2)+(3) — verbatim `out/h027_geometry.out` (deterministic numpy/scipy, NO tuning)

```
========================================================================
H_027 — does CoSn's flat-band geometry lever SURVIVE doping-to-E_F?
  source: OUR converged spin-polarized PBE SCF (6-atom Co3Sn3, 93 e-,
          E_F=14.7132 eV, alat=9.9760 a.u. = a=5.2791 A)
========================================================================

--- (1a) FLAT BAND on the Gamma-K-M-Gamma plane (flattest near E_F) ---
band  meanE(eV)  W(eV)    dE=mean-EF
  45   14.2697  0.1668  -0.4435
  44   14.1586  0.1770  -0.5546
  39   12.7677  0.1889  -1.9455
  38   12.6690  0.1925  -2.0442
=> FLAT BAND = band 45, centre 14.2697 eV (= -0.4435 eV rel E_F), W=0.1668 eV

--- (1b) RIGID-BAND hole doping to slide E_F onto the flat band ---
sanity: N(E_F=14.7132)=93.039 (should be ~93.0)
N(E_F'=14.2697 flat centre)=88.314 -> hole doping Delta_n = 4.726 e-/cell
   = 1.575 holes / CoSn formula unit (cell has 3 f.u.)
   = 5.1% of the cell's valence electrons removed
=> DOPING VERDICT: 1.58 holes/f.u. -> EXTREME (>0.7 h/f.u.; beyond gating, needs full chemical replacement)

--- (2) GEOMETRY at the flat band: NN-kagome TB fit + projector-FD tr g ---
3-band kagome group bands [44, 45, 46], span=0.8594 eV -> t=0.1432 eV, e0=-0.7300 eV (rel E_F)
Gamma band-touching: 30/3600 grid pts capped (integrable singularity)
<tr g>_BZ = 10.9658 A^2 ; I = (1/2pi) int tr g d2k = 2.8548
MEASURED QGT (arXiv:2412.17809) g = 2.87 ; H_024 (deeper band) I = 2.856
=> GEOMETRY VERDICT (rigid-band): I=2.855 -> SURVIVES (I>=2, lever intact under rigid-band doping)
   CAVEAT: rigid-band keeps the projector fixed; REAL doping (live SCF)
   can hybridize/spin-split the manifold -> checked against the doped SCF.

--- (3) FILLING nu of the flat band at the doped E_F & D_s ∝ nu(1-nu) ---
flat band (band 45) mean occupation at E_F'=14.2697 (path-sampled): nu = 0.507
D_s^geom ∝ nu(1-nu) = 0.2500  (maximum 0.25 at nu=0.5)
=> FILLING VERDICT: nu=0.507, nu(1-nu)=0.2500 = 100% of the 0.25 max -> FAVOURABLE (near half-filling, D_s strong)

========================================================================
SUMMARY (all from OUR converged PBE DFT; no tuning):
  doping-to-E_F : 4.73 e-/cell = 1.58 holes/CoSn f.u. -> EXTREME
  geometry I    : 2.855 (rigid-band) -> SURVIVES
  flat filling  : nu=0.507, nu(1-nu)=0.250 -> FAVOURABLE
========================================================================
```

ν-sensitivity (same script, reported for honesty, L3): if E_F lands at the flat-band TOP ν=0.819 →
ν(1−ν)=0.148; at the BOTTOM ν=0.287 → ν(1−ν)=0.205; at the CENTRE ν=0.507 → 0.250. So the favourable
ν is a ~0.17 eV-wide window around the band centre — landing in it needs doping control to ~0.1 eV in
E_F, i.e. to ~±0.5 e/cell precision, on top of the ~4.7 e/cell extreme baseline.

### Live doped-SCF cross-check (non-rigid-band) — verbatim pw.x parallel banner + status

The H_026 fix is confirmed live this session — both builds are genuinely parallel (tool-self-report,
verbatim banners):
```
QE 7.2 (~/qe_build, H_026): mpirun -np 6 pw.x ->
     Parallel version (MPI), running on     6 processors
     MPI processes distributed on     1 nodes
QE 7.5 (conda ~/miniforge3/envs/qe): mpirun -np 6 pw.x ->
     Parallel version (MPI & OpenMP), running on      12 processor cores
     Number of MPI processes:                 6
     Threads/MPI process:                     2
```
A hole-doped SCF (`scf_h4p0.in`, tot_charge=4.0 → 89 e⁻, robust β=0.2 degauss=0.04 recipe) was launched
under genuine 6-rank MPI (`mpirun -np 6 pw.x -npool 2`; 6 live pw.x ranks confirmed via `pgrep`). For
this high-DOS flat-band metal the doped SCF is DELICATE: iteration 1 alone runs many minutes (Davidson
struggling against the dense doped manifold), the SCF accuracy sloshes (iter1 ~29.1 Ry → iter2 ~3.36 Ry)
and — tellingly — the **total magnetization swings violently (0.68 → 8.23 μ_B/cell between iters 1–2)**,
and the earlier session's tot_charge=2.0 run terminated with `MPI_ABORT` (charge-sloshing instability).
This slowness/magnetic-instability is itself an honest signal that the doped flat-band metal is hard to
stabilize self-consistently (the high doped DOS drives a magnetic instability, exactly where rigid-band
is least safe — L1/L4) — consistent with L1 (rigid-band
is the geometry-preserved best case; the real doped state is the harder, less benign object). **No
converged doped E_F or magnetization is reported (none was reached) — NOT fabricated** (F5 PASS on the
honest "doped state is delicate / non-converging" branch). The deterministic rigid-band result above
is therefore the load-bearing answer; the live SCF corroborates only that the doped state is non-trivial.

### Falsifiers

- **F1_doping_magnitude_honest**: **PASS** — Δn=4.73 e⁻/cell = 1.58 holes/CoSn f.u. = 5.1% of valence,
  judged EXTREME (>0.7 h/f.u.) against the stated thresholds.
- **F2_geometry_survives_or_not**: **PASS** — I=2.855 (TB-fit route, same as H_024) ≥ 2 → SURVIVES;
  the rigid-band-vs-real-doping caveat is named (L1/L2).
- **F3_filling_nu_honest**: **PASS** — ν=0.507, ν(1−ν)=0.250 = the 0.25 maximum → FAVOURABLE; the
  band-top/bottom ν-sensitivity is reported.
- **F4_verdict_honest**: **PASS** — SURVIVES-on-geometry-but-WEAKENED-on-accessibility verdict stated;
  is_green=False preserved; the EXTREME doping reported plainly, not tuned away.
- **F5_doped_scf_crosscheck_honest**: **PASS** — the live doped SCF is reported honestly as delicate/
  slow/non-converging (prior tot_charge=2 MPI_ABORTed); no fabricated converged doped E_F.
- **F6_preregister**: not triggered (criteria frozen before runs).
- **F7_no_fabrication**: **PASS** — every number is verbatim pw.x stdout/banner or labeled
  deterministic analysis output; the un-converged doped SCF is reported as such, not invented.

### Structural finding

The CoSn geometry lever is ROBUST where it can be evaluated: the kagome flat-band quantum metric
integral I=2.855 ≈ the measured QGT 2.87 at the near-E_F flat band, and the filling at E_F-on-band is
ν≈0.5 — the FAVOURABLE half-filling that maximises D_s^geom ∝ ν(1−ν). The lead 🟢-path is therefore NOT
weakened on the geometry/filling physics. The NEW adverse result is on ACCESSIBILITY: bringing E_F onto
the flat band requires ~4.7 holes/cell = ~1.58 holes per CoSn formula unit, an EXTREME carrier density
(direct consequence of the flat band's huge DOS, L5) that exceeds electrostatic gating and demands full
chemical substitution — and the live doped SCF shows the doped flat-band metal is delicate to stabilize
(L1/L4). Net: the H_023/H_024 D_s lever's geometry survives, but its doping-to-E_F precondition is
expensive — the lead path stays viable in principle yet is materially harder than the undoped geometry
suggested. The trio remains **🟠 jointly-unrealized**; `absorbed=false` / GATE_OPEN — no simulation
flips that.

### Records

`state/h027_doped_cosn_geometry_survival_2026_06_25/` — `decks/{h027_doped_geometry.py, scf.in,
scf.out, bands.in, cosn_bands.dat.gnu, flat.py, rigidband.py, dope.py, nscf.in}`,
`out/{h027_geometry.out, doped_scf_h4p0.head.out}`.
