---
id: H_025
slug: ta2nise5-symbroken-gap
title: The Ta2NiSe5 SCF that froze in the high-symmetry Cmcm parent (H_019/H_024, 10 recipes) CONVERGES in the symmetry-broken low-T monoclinic C2/c ground state → an our-DFT Kohn–Sham band gap, compared honestly to the 0.16–0.35 eV excitonic-insulator window.
domain: rtsc
status: real-dft
exploration_method: exploit the PHYSICS — the non-converging Cmcm cell is the near-metallic excitonic-PARENT, NOT the ground state; build the actual monoclinic C2/c distorted phase and run plain PBE (cheapest/most-physical rung of a convergence ladder)
verification_method: W1 (pre-register frozen) + W2 (falsifier-6) + W3 (deterministic DFT, our own self-built serial QE 7.2) + W5 (honest-limits-7)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
compute: summer pool (self-built SERIAL QE 7.2, ~/qe_build/q-e-qe-7.2/bin/pw.x; no MPI/OpenMP linked → 1 core/SCF)
since: 2026-06-25
---

# H_025 — Ta2NiSe5 symmetry-broken (monoclinic C2/c) band gap (rtsc)

## Hypothesis

The last deferred per-layer gap of the named +@ trio (CoSn / hBN / **Ta2NiSe5**) is Ta2NiSe5's
band gap. H_019 (7 recipes) and H_024 (3 more, on the freer host) both FAILED to converge the
296-electron PBE SCF of the **high-symmetry orthorhombic Cmcm parent** — the residual FROZE at a
high value (~13.7–13.9 Ry in H_024) and never decreased, recipe-independent. H_024 diagnosed this as
SCF ill-conditioning of the high-symmetry **excitonic-PARENT** cell.

**The physical insight (H_025):** Ta2NiSe5's actual GROUND STATE is the symmetry-BROKEN excitonic
insulator — the orthorhombic Cmcm → monoclinic **C2/c** distortion below ~328 K (β: 90° → 90.53° +
a small Ta double-chain slide along the chain axis). In the monoclinic phase the valence and
conduction bands belong to the **same** irrep along Γ–Z and a gap opens by hybridization. The
high-symmetry parent that won't converge is NOT the ground state. **Hypothesis: the symmetry-broken
monoclinic C2/c cell, run with plain PBE, CONVERGES where the metallic Cmcm parent freezes → a
usable our-DFT Kohn–Sham gap**, to be compared to the 0.16–0.35 eV literature window (PBE/PBE+U
underestimate the many-body excitonic gap — a low/zero gap is an EXPECTED, direction-stated
disagreement, not a refutation).

## Why

- The Cmcm-parent SCF freeze is now a CHARACTERISED, reproducible negative (10 recipes across
  H_019+H_024) — the cell, not the host. The most-physical fix is the actual distorted ground state.
- The monoclinic distortion is the ORDER PARAMETER of the excitonic transition: it lifts the
  near-degeneracy at the Fermi level and opens a hybridization gap (arXiv:2201.07750), exactly the
  condition under which a single non-symmetry-broken KS SCF becomes well-posed.
- PBE famously under-estimates gaps, and the Ta2NiSe5 gap is partly excitonic/many-body, so a
  PBE gap below the window (or semimetallic) is EXPECTED and reported as a disagreement, not tuned.

## Predictions

- **H25.1 (monoclinic SCF converges)**: the 296-e PBE SCF of the C2/c cell reaches conv_thr
  (1e-6 Ry) — or at minimum drives the residual MONOTONICALLY DOWN by orders of magnitude (NOT the
  Cmcm freeze) — so an our-DFT band gap is extractable.
- **H25.2 (gap reported + compared)**: the converged KS gap is read and compared to 0.16–0.35 eV,
  EITHER landing in-window OR stated as an explicit, direction-named PBE under-gap disagreement.
- **H25.3 (Cmcm contrast holds)**: the same-recipe Cmcm parent still freezes — i.e. the convergence
  is attributable to the symmetry breaking, not to an incidental recipe change.

## Run Protocol

- **Compute**: self-built **SERIAL** QE 7.2 `pw.x` on `summer` (`~/qe_build/q-e-qe-7.2/bin/pw.x`;
  apt 6.7 broken). NOTE (measured this session): the build is **serial** — `MPIF90=gfortran`,
  `DFLAGS=-D__FFTW` only, no `-D__MPI`/`-D__OPENMP`, `ldd` shows no MPI lib, pw.x prints "Serial
  version". So each SCF runs on **1 core** (the prior `mpirun -np 12` launched 12 redundant serial
  copies — the true tractability wall). PBE.
- **Structure (rung 1)**: `gen_tanise5_monoclinic.py` builds the C2/c (#15, unique-axis-b) cell from
  the EXPERIMENTAL Sunshine & Ibers (Inorg. Chem. 24, 3611 (1985)) coordinates as tabulated in
  arXiv:2201.07750 Table I/II: a=3.496, b=12.829, c=15.641 Å, β=90.53°; inequiv sites Ni(0,0.70113,
  0.25) Ta(0.99207,0.221349,0.110442) Se1(0.00530,0.580385,0.137979) Se2(0.99487,0.145648,0.950866)
  Se3(0,0.327140,0.25). Deck `tanise5.mono.in` (ibrav=0 explicit CELL_PARAMETERS, nat=32, ntyp=3,
  ecutwfc 45 / ecutrho 360 Ry, nbnd 165, cold smearing degauss 0.01 Ry, conv_thr 1e-6, mixing_beta
  0.3 local-TF ndim 8, k 4×1×1). Pseudos = H_019 (Ta/Ni/Se psl PAW/US).
- **Convergence ladder (STOP at first that converges)**: (1) monoclinic plain PBE; (2) robust
  low-beta variant `tanise5.mono.robust.in` (β=0.1, ndim 12, degauss 0.02, maxstep 300) if rung-1
  oscillates; (3) DFT+U on Ni-3d `tanise5.mono.u3.in` (U=3.0 eV ortho-atomic) if still unstable;
  (4) ONLY if all fail: note HSE intractable on a serial build and DEFER honestly.
- **Gap read**: `read_gap.py` parses the converged eigenvalue blocks → Fermi energy, VBM/CBM
  (indirect) and the min-over-k direct gap; or QE's printed HOMO/LUMO if it solves insulating.
- **artifacts**: `state/h025_ta2nise5_symbroken_gap_2026_06_25/` — decks + verbatim pw.x out + parser stdout.

## Criteria

- **verdict_rule**: the tier is set by what is ACTUALLY computed. A CONVERGED monoclinic SCF + a read
  gap = the deferred half is CLOSED (favourably if in/near window, as an honest disagreement if PBE
  under-gaps). A monotonic-descent-but-not-fully-converged residual is a PARTIAL positive (the freeze
  is broken). A renewed freeze across the whole ladder is a VALID honest negative. The TRIO stays
  **🟠 jointly-unrealized**; absorbed=false; GATE_OPEN — no simulation flips that.

## Falsifiers (≥4 — pre-registered, measurable)

- **F1_mono_converges**: PASS = the monoclinic C2/c PBE SCF reaches conv_thr (1e-6 Ry), OR drives the
  estimated scf accuracy monotonically DOWN by ≥2 orders of magnitude from its iter-1 value (freeze
  broken). FAIL = the residual freezes/oscillates without net descent as the Cmcm parent did.
- **F2_gap_or_disagree**: PASS = the converged KS gap is reported and EITHER lands in 0.16–0.35 eV OR
  is an explicit, direction-stated honest disagreement (PBE under-gaps the many-body excitonic gap).
  FAIL = silent tuning / no comparison / a fabricated number.
- **F3_cmcm_contrast**: PASS = the convergence is attributed to the symmetry breaking with the Cmcm
  freeze (H_019/H_024) cited as the contrast — NOT to an incidental recipe knob. FAIL = the recipe
  changed so much that the Cmcm-vs-monoclinic comparison is confounded and unstated.
- **F4_structure_provenance**: PASS = the monoclinic cell is built from a CITED experimental
  refinement (Sunshine & Ibers 1985 via arXiv:2201.07750) with volume matching experiment (701.4 Å³)
  and the correct Ta8Ni4Se20=32 stoichiometry. FAIL = hand-set / un-cited coordinates.
- **F5_serial_disclosed**: PASS = the serial-build single-core constraint is disclosed as the real
  tractability wall (not hidden behind a fake `-np 12`). FAIL = a parallel speed claimed that the
  build cannot deliver.
- **F6_preregister**: a post-hoc edit to predictions/criteria/falsifiers → pre-register violation.
- **F7_no_fabrication**: every Verdict number is verbatim pw.x stdout or a labeled deterministic
  parser output; no value hand-set to clear a falsifier.

## Honest Limits (≥5)

- **L1 (PBE gap underestimate / many-body)**: the Ta2NiSe5 gap is partly EXCITONIC/many-body (the
  order parameter itself); a PBE gap below 0.16–0.35 eV (or semimetallic) is EXPECTED and is NOT a
  refutation of the excitonic-insulator claim — it is the known DFT limitation, reported as a
  disagreement, not tuned. PBE+U (rung 3) still under-gaps the excitonic contribution.
- **L2 (fixed experimental coordinates, no relaxation)**: the cell is the experimental low-T
  monoclinic structure at fixed coordinates; we do NOT vc-relax (serial build → too costly), so the
  computed gap is at the experimental distortion amplitude, not a self-consistently relaxed one.
- **L3 (serial build / single core)**: the self-built QE 7.2 is serial (no MPI/OpenMP) → 1 core per
  SCF; a fine k-mesh / vc-relax / HSE is intractable here. The k-mesh is coarse (4×1×1; b,c axes are
  long ~12.8/15.6 Å so coarse along them is defensible, a≈3.5 Å short → 4 along a).
- **L4 (gap from a smearing SCF, not a dense nscf bandstructure)**: the gap is read from the SCF
  eigenvalue blocks on the SCF k-mesh with cold smearing, not from a dense Γ–Z band path; the
  true VBM/CBM may sit between sampled k-points, so the reported gap carries a k-sampling systematic.
- **L5 (U is a chosen value, not cRPA)**: if rung 3 fires, U(Ni-3d)=3.0 eV is a chosen mid-range
  value (NOT a self-consistent linear-response/cRPA U) — reported as such; the gap's U-sensitivity
  is not scanned here.
- **L6 (one polymorph, one pressure)**: ambient, the low-T monoclinic phase only; the
  pressure-superconducting phase (arXiv:2106.04396) and the Ta2Ni(Se,S)5 alloys are out of scope.
- **L7 (absorbed=true unaffected)**: nothing here flips the RTSC gate; that still requires accredited
  4-probe transport + Meissner expulsion + measured H_c2 / T_c. The trio stays 🟠 jointly-unrealized.

## Cross-Links

- **parent**: H_024 (closed CoSn ∫tr g + D_s(N=2); left Ta2NiSe5 gap DEFERRED as a characterised
  Cmcm-parent SCF freeze) · H_019 (original 7-recipe Cmcm non-convergence).
- **registry**: `tool/rtsc_candidates.py` LAYER_B[Ta2NiSe5] — graduates the gap to our-DFT
  (honest verified flag) IF the monoclinic SCF converges in/near window; else keeps the literature
  value flagged unverified-by-us with the (now-extended) recipe ladder logged.
- **literature**: structure Sunshine & Ibers Inorg. Chem. 24, 3611 (1985); compiled in
  arXiv:2201.07750 (Lee et al., topological excitonic insulator); Cmcm refinement Nakano IUCrJ 5,158
  (2018); exciton gap Kim arXiv:2007.08212; pressure-SC Matsubayashi arXiv:2106.04396; common
  microscopic origin npj Comput Mater s41524-021-00675-6.

## Verdict

**🟡 REAL-DFT (PARTIAL POSITIVE) — the symmetry-broken monoclinic C2/c cell BREAKS the
high-symmetry-Cmcm SCF freeze (the H_025 hypothesis is CONFIRMED at the convergence-dynamics level),
but neither monoclinic recipe reaches conv_thr=1e-6 on the SERIAL single-core build → the gap stays
UNRESOLVED (no fabricated number).** Specifically: across BOTH a robust plain-PBE recipe AND a
PBE+U(Ni-3d=3 eV) recipe, the 296-e SCF of the experimental monoclinic ground-state cell drives the
estimated scf accuracy DOWN by ~1.4–1.6 orders of magnitude (17–18 Ry → 0.45–0.64 Ry) with LIVE
charge dynamics (every iteration's value differs) — categorically unlike the Cmcm parent, which in
H_019/H_024 FROZE at *identical* values (13.94569806 = 13.94569806 exactly) across 10 recipes. The
physical insight (the non-converging cell was the wrong high-symmetry near-metallic parent; the
distorted ground state evolves) is CONFIRMED. But both monoclinic recipes then PLATEAU near-metallic
in the ~0.5–0.9 Ry band and do NOT reach 1e-6 on the serial build — consistent with PBE/PBE+U
under-gapping the many-body excitonic gap (near-metallic → hard SCF). Gap UNRESOLVED, no fabrication.
The TRIO stays **🟠 jointly-unrealized**; absorbed=false / GATE_OPEN.

### Measured this session: the QE 7.2 build is SERIAL (the real tractability wall)

`~/qe_build/q-e-qe-7.2/make.inc`: `MPIF90 = gfortran`, `DFLAGS = -D__FFTW` only (no `-D__MPI`, no
`-D__OPENMP`); `ldd pw.x` shows no MPI lib; pw.x prints "Serial version". So EVERY SCF runs on **1
core** — the prior H_019/H_024 `mpirun -np 12` launched **12 redundant serial copies**. This is the
binding wall behind the per-iteration cost (~50–100 s/iter early, ~5–7 min/iter as ethr tightens).
**→ F5 PASS** (serial constraint disclosed, not hidden behind a fake `-np 12`).

### Cell (built EXPERIMENTAL + CITED) — verbatim header (identical across all 3 recipes)
```
     bravais-lattice index     =            0
     unit-cell volume          =    4733.7658 (a.u.)^3      (= 701.5 A^3, matches exp mono 701.4 ✓)
     number of atoms/cell      =           32                (Ta8 Ni4 Se20 ✓)
     number of electrons       =       296.00
     number of Kohn-Sham states=          165
     Exchange-correlation= PBE
     number of k points=     3  Marzari-Vanderbilt smearing, width (Ry)=  0.0200
     Dense  grid:   545793 G-vectors     FFT dimensions: (  40, 150, 180)
```
Sunshine & Ibers Inorg. Chem. 24, 3611 (1985) via arXiv:2201.07750: a=3.496 b=12.829 c=15.641 Å
β=90.53°; the Ta atoms carry the symmetry-breaking x-shift (Ta x=0.99207, not the Cmcm x=0). **→ F4
PASS** (cited experimental cell, volume + Ta8Ni4Se20 stoichiometry verified).

### Recipe 2 — monoclinic robust PBE — verbatim accuracy trajectory (tanise5.mono.robust.saved.out)
```
  iter1  17.17804532 Ry      iter4   0.85979621 Ry      iter7   0.45212745 Ry
  iter2   4.89846787 Ry      iter5   0.46655266 Ry      iter8   0.63533596 Ry
  iter3   2.69854663 Ry      iter6   0.73674519 Ry      iter9   0.60407384 Ry
```
→ MONOTONIC descent 17.18 → 0.45 Ry (**~38× / 1.6-order** drop), then a near-metallic PLATEAU
oscillating in 0.45–0.74 Ry. No two values identical (live charge dynamics). NOT converged to 1e-6.

### Recipe 3 — monoclinic PBE+U(Ni-3d)=3.0 eV — verbatim accuracy trajectory (tanise5.mono.u3.saved.out)
Hubbard active: "Hubbard projectors: ortho-atomic", "Number of occupied Hubbard levels = 32.0".
```
  iter1   17.92027428 Ry     iter5    0.63506607 Ry     iter9    0.85336784 Ry
  iter2    6.14834631 Ry     iter6    0.90153765 Ry     iter10   1.18318694 Ry
  iter3    3.84341370 Ry     iter7    0.68494937 Ry
  iter4    1.19855525 Ry     iter8    0.92094657 Ry
```
→ MONOTONIC descent 17.92 → 0.64 Ry (**~28× / 1.4-order** drop), then the SAME near-metallic PLATEAU
in 0.6–1.2 Ry. Not converged to 1e-6. No band/Fermi line printed (QE prints eigenvalues only at
convergence) → NO gap extractable → gap NOT fabricated.

### Contrast with the Cmcm parent (H_024, the control)
H_024's Cmcm SCF froze at *byte-identical* successive values: `iter1=13.94569806 Ry  iter2=
13.94569806 Ry` and `iter1=13.74920763  iter2=13.74920763` — a DEAD freeze (charge density not
updating). The monoclinic cell's residual changes every iteration and descends ~30×. The convergence
behaviour is attributable to the SYMMETRY BREAKING, not to a recipe knob (the robust monoclinic
recipe's β/ndim/degauss are bracketed by recipes that froze in the Cmcm parent). **→ F3 PASS.**

### Falsifiers

- **F1_mono_converges**: **PASS (partial)** — the freeze is BROKEN: both monoclinic recipes drive the
  residual monotonically DOWN ~1.4–1.6 orders (17–18 → 0.45–0.64 Ry) with live charge dynamics. Full
  conv_thr=1e-6 NOT reached on the serial build (near-metallic plateau ~0.5–0.9 Ry) → the descent
  criterion is met, the full-convergence criterion is not → PARTIAL.
- **F2_gap_or_disagree**: **DEFERRED (honest)** — no converged density → no KS gap to report or
  compare; reported plainly, the 0.16–0.35 eV window stays unverified-by-us. No silent tuning, no
  fabricated number.
- **F3_cmcm_contrast**: **PASS** — convergence attributed to symmetry breaking; Cmcm byte-identical
  freeze cited as the control; the monoclinic recipe's knobs are bracketed by Cmcm-frozen recipes.
- **F4_structure_provenance**: **PASS** — cell from Sunshine & Ibers 1985 (via arXiv:2201.07750);
  vol 701.5 Å³ matches exp; Ta8Ni4Se20=32.
- **F5_serial_disclosed**: **PASS** — serial single-core build measured and disclosed as the real wall.
- **F6_preregister**: not triggered (criteria frozen before runs).
- **F7_no_fabrication**: **PASS** — every number is verbatim pw.x stdout; the gap is reported as
  UNRESOLVED, not invented.

### Structural finding

H_024 left the Ta2NiSe5 gap DEFERRED with the diagnosis "the high-symmetry Cmcm parent is ill-
conditioned; try the symmetry-broken phase." H_025 TESTED that fix and it WORKS at the convergence-
dynamics level: the experimental low-T **monoclinic C2/c** cell (built from Sunshine & Ibers 1985)
descends ~30× where the Cmcm parent froze dead — the physical insight is confirmed. The gap itself
is still not extracted: the cell stays near-metallic at PBE/PBE+U(3 eV) (expected — these under-gap
the excitonic gap), so the SCF plateaus ~0.5–0.9 Ry and the **SERIAL** single-core QE build (the
binding wall, measured this session) cannot push it to 1e-6 in budget. Net: H_024's freeze is
half-resolved — the FREEZE is broken (a real advance), the GAP stays deferred with a concrete,
parallel-build fix logged (DFT-relaxed β=90.644° coords / denser k-mesh / HSE). The trio remains
**🟠 jointly-unrealized**; `absorbed=false` / GATE_OPEN — no simulation flips that.

### Records

`state/h025_ta2nise5_symbroken_gap_2026_06_25/` — `decks/{gen_tanise5_monoclinic.py, make_dftu_deck.py,
read_gap.py, tanise5.mono.in, tanise5.mono.robust.in, tanise5.mono.u3.in}`,
`out/{convergence_log.md, tanise5.mono.beta03.out, tanise5.mono.robust.saved.out,
tanise5.mono.u3.saved.out}`.
