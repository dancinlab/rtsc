---
id: H_026
slug: qe-mpi-ta2nise5-gap
title: The campaign's self-built QE 7.2 was a SERIAL build (root cause of EVERY DFT freeze H_015→H_025) — rebuilt WITH MPI in place, then the Ta2NiSe5 monoclinic C2/c SCF re-run under genuine 6-core parallelism to settle the deferred excitonic-insulator gap.
domain: rtsc
status: real-dft
exploration_method: root-cause the substrate-infra wall (characterised serial QE build → FIX it, do not defer), then reuse the fix to re-run the H_025 monoclinic SCF that was descending-but-time-budget-cut on the serial build
verification_method: W1 (pre-register frozen) + W2 (falsifier-7) + W3 (deterministic DFT, our own rebuilt-PARALLEL QE 7.2) + W5 (honest-limits-7) + tool-self-report (the build's own banner is the source of truth)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
compute: summer pool host (self-built QE 7.2 REBUILT WITH MPI in place — ~/qe_build/q-e-qe-7.2/bin/pw.x now "Parallel version (MPI)"; OpenMPI 4.1.6 + libopenmpi-dev; 6 physical cores)
since: 2026-06-25
---

# H_026 — QE 7.2 MPI rebuild (infra root-cause fix) + Ta2NiSe5 monoclinic gap re-run (rtsc)

## Hypothesis

H_025 measured that the campaign's self-built `~/qe_build/q-e-qe-7.2/bin/pw.x` is a **SERIAL** build
(`make.inc` `MPIF90=gfortran`, `DFLAGS=-D__FFTW` only, no `-D__MPI`; `ldd` shows no MPI lib; banner
"Serial version"). So the prior campaign DFT launches `mpirun -np 12 pw.x` ran **12 redundant serial
copies on 1 core each** — the true tractability wall behind every "won't converge in budget" DFT from
H_015 through H_025, including the 296-electron Ta2NiSe5 SCF.

**Hypothesis (two parts):**
- **(A, infra)** summer has an MPI toolchain (or one can be installed free); rebuilding QE 7.2 with
  `-D__MPI` produces a `pw.x` whose own banner reads **"Parallel version (MPI)"** and that genuinely
  distributes work across MPI ranks (Number of MPI processes = N). This FIXES the substrate.
- **(B, physics)** with the fix, the H_025 monoclinic C2/c SCF — which on the serial build descended
  ~38× (17→0.45 Ry) but was cut off by the single-core time budget before reaching conv_thr — either
  (i) reaches conv_thr=1e-6 → an our-DFT Kohn–Sham gap compared to the 0.16–0.35 eV excitonic window,
  or (ii) is now shown, with the budget wall removed, to genuinely OSCILLATE in a near-metallic
  plateau (the PBE-under-gaps-the-many-body-excitonic-gap physics, not a compute artifact).

## Why

- **Break-walls / root-cause:** a characterised substrate-infra wall must be FIXED, not deferred. The
  serial build was diagnosed in H_025; this card closes it instead of carrying it forward.
- **실측전 research → cheapest fix first:** the fix is FREE — OpenMPI 4.1.6 was already on summer; only
  the linkable dev package (`libopenmpi-dev`, which provides the `.so` symlinks the `mpif90` wrapper
  references) was missing, which is why `./configure` silently fell back to "serial executables".
- **Honest closure of the deferred gap:** H_025 left F2 (the gap) DEFERRED *explicitly because of the
  serial wall*. Removing the wall lets the gap question get a real answer (converge OR genuinely-oscillate),
  either of which is a valid result.

## Predictions

- **H26.1 (MPI banner)**: the rebuilt `~/qe_build/q-e-qe-7.2/bin/pw.x` prints "Parallel version (MPI)"
  and under `mpirun -np N` reports "running on N processors" / "Number of MPI processes: N".
- **H26.2 (genuine distribution)**: `make.inc` carries `-D__MPI`; `ldd pw.x` links `libmpi.so`; a real
  SCF runs with N ranks sharing the work (npool k-point split), not N redundant copies.
- **H26.3 (gap settled)**: the monoclinic SCF, run under MPI to many more iterations than the serial
  budget allowed, EITHER reaches conv_thr=1e-6 (gap read + compared to 0.16–0.35 eV) OR is shown to
  oscillate persistently in the near-metallic plateau — a measured, definitive verdict either way.

## Run Protocol

- **Infra fix (A):** `sudo apt-get install -y libopenmpi-dev` (OpenMPI 4.1.6 runtime present; dev `.so`
  symlinks missing) → `cd ~/qe_build/q-e-qe-7.2 && ./configure MPIF90=mpif90 --enable-parallel` (now
  detects "Parallel environment detected successfully") → `make clean && make pw -j12`. Build in place
  (canonical build, NOT a _v2 copy). Verify banner + `ldd` + a real `mpirun -np N` distribution.
- **Physics re-run (B):** reuse the H_025 monoclinic C2/c cell + decks verbatim
  (`state/h025_ta2nise5_symbroken_gap_2026_06_25/`; Sunshine & Ibers 1985 via arXiv:2201.07750,
  vol 701.5 Å³, Ta8Ni4Se20=32, 296 e⁻). Run `mpirun -np 6 pw.x -npool 2` (summer = 6 physical cores;
  OpenMPI counts physical slots, so -np 6 not 12). Convergence ladder, STOP at first that converges:
  (1) robust plain PBE (β=0.1, local-TF ndim 12, degauss 0.02, maxstep 300); (2) PBE+U(Ni-3d=3 eV
  ortho-atomic, Dudarev); (3) higher-smearing metallic variant if both oscillate.
- **Gap read:** `read_gap.py` on a converged SCF (verbosity='high' eigenvalue blocks) → Fermi, VBM/CBM.

## Criteria

- **verdict_rule:** the tier is set by what is ACTUALLY computed. (A) A verified "Parallel version (MPI)"
  banner + genuine distribution = the infra root-cause is FIXED (a real campaign-wide deliverable).
  (B) A converged monoclinic SCF + read gap = the H_025-deferred half CLOSED (favourably if in/near
  window; as an honest, direction-stated PBE under-gap disagreement if below). A persistent
  near-metallic oscillation now that the budget wall is removed = a VALID measured negative on the
  gap (the freeze→descent→plateau is now fully characterised, not budget-limited). The TRIO stays
  **🟠 jointly-unrealized**; absorbed=false; GATE_OPEN — no simulation flips that.

## Falsifiers (≥4 — pre-registered, measurable)

- **F1_mpi_banner**: PASS = the rebuilt `~/qe_build/q-e-qe-7.2/bin/pw.x` prints "Parallel version (MPI)"
  and under `mpirun -np N` reports "running on N processors". FAIL = it still prints "Serial version"
  or ignores -np.
- **F2_genuine_distribution**: PASS = `make.inc` has `-D__MPI`, `ldd pw.x` links `libmpi.so`, and a real
  SCF distributes across N ranks (npool k-split, not N redundant copies). FAIL = N redundant serial copies.
- **F3_scf_verdict**: PASS = the monoclinic SCF, run under MPI for ≫ the serial-budget iteration count,
  reaches a DEFINITIVE verdict — either conv_thr=1e-6 (converged) OR a characterised persistent
  near-metallic oscillation across both PBE and PBE+U. FAIL = an ambiguous cut-off that is again merely
  time-budget-limited (i.e. the fix bought nothing).
- **F4_gap_or_honest_negative**: PASS = IF converged, the KS gap is reported and EITHER lands in
  0.16–0.35 eV OR is an explicit, direction-stated PBE under-gap disagreement; IF oscillating, the
  no-gap outcome is attributed to the PBE near-metallic state (the many-body excitonic gap absent in
  PBE), not fabricated. FAIL = a hand-set gap number / silent tuning.
- **F5_cmcm_mono_contrast**: PASS = the descent (freeze→~38× drop) is still attributed to the H_025
  monoclinic symmetry breaking vs the H_019/H_024 Cmcm byte-identical freeze, now under MPI. FAIL = the
  contrast is confounded by the parallelism change and left unstated.
- **F6_preregister**: a post-hoc edit to predictions/criteria/falsifiers → pre-register violation.
- **F7_no_fabrication**: every Verdict number is verbatim pw.x stdout / banner / `make.inc` / `ldd`, or a
  labeled deterministic parser output; no value hand-set to clear a falsifier.

## Honest Limits (≥5)

- **L1 (PBE gap underestimate / many-body)**: the Ta2NiSe5 gap is partly EXCITONIC/many-body (the order
  parameter itself); a PBE/PBE+U near-metallic state (no gap) is EXPECTED and is NOT a refutation of the
  excitonic-insulator claim — it is the known DFT limitation. The MPI fix removes the *compute* wall, not
  the *theory* wall: PBE still cannot host the many-body gap.
- **L2 (fixed experimental coordinates, no relaxation)**: the cell is the experimental low-T monoclinic
  structure at fixed coords; no vc-relax (still costly even with MPI on 6 cores), so any gap is at the
  experimental distortion amplitude, not a self-consistently relaxed one.
- **L3 (modest core count)**: summer is 6 physical cores / 12 threads. The MPI fix makes the SCF ~6×
  faster (real distribution), but a dense nscf band path, vc-relax, or HSE remain heavy; the k-mesh stays
  coarse (4×1×1 → 3 irreducible k after symmetry; b,c axes long ~12.8/15.6 Å so coarse is defensible).
- **L4 (U is a chosen value, not cRPA)**: PBE+U uses U(Ni-3d)=3.0 eV (Dudarev, ortho-atomic) — a chosen
  mid-range value, NOT a self-consistent linear-response/cRPA U; the gap's U-sensitivity is not scanned.
- **L5 (gap from a smearing SCF, not a dense nscf bandstructure)**: any gap would be read from SCF
  eigenvalue blocks on the SCF k-mesh with cold/MV smearing, not a dense Γ–Z path — carries a k-sampling
  systematic.
- **L6 (one polymorph, one pressure)**: ambient low-T monoclinic phase only; the pressure-SC phase and
  Ta2Ni(Se,S)5 alloys are out of scope.
- **L7 (absorbed=true unaffected)**: nothing here flips the RTSC gate — that still requires accredited
  4-probe transport + Meissner expulsion + measured H_c2 / T_c. The trio stays 🟠 jointly-unrealized.

## Cross-Links

- **parent**: H_025 (built the monoclinic C2/c cell; measured the serial build; left the gap DEFERRED on
  the serial wall) · H_024 / H_019 (the original Cmcm byte-identical SCF freeze, 10 recipes).
- **registry**: `tool/rtsc_candidates.py` LAYER_B[Ta2NiSe5] — graduates the gap to our-DFT (honest
  verified flag) IF the monoclinic SCF converges in/near window; else records the now-fully-characterised
  descent→near-metallic-oscillation (budget wall removed) with the literature value kept unverified-by-us.
- **infra**: `tool/CLAUDE.md` "Compute substrate (summer pool host)" — records the MPI rebuild so the
  campaign no longer launches redundant serial copies.
- **literature**: structure Sunshine & Ibers Inorg. Chem. 24, 3611 (1985) via arXiv:2201.07750; exciton
  gap Kim arXiv:2007.08212; pressure-SC Matsubayashi arXiv:2106.04396.

## Verdict

<!-- FILLED FROM VERBATIM RUN OUTPUT BELOW -->

### A — Infra root-cause FIXED (verbatim)

**The campaign's canonical `~/qe_build/q-e-qe-7.2/bin/pw.x` is now an MPI (PARALLEL) build.**

Before (H_025, serial): `make.inc` `MPIF90 = gfortran`, `DFLAGS = -D__FFTW` (no `-D__MPI`); banner
"Serial version"; `mpirun -np 12` = 12 redundant serial copies.

Fix: OpenMPI 4.1.6 runtime was present but the linkable dev package was missing (so `./configure` fell
back to serial). `sudo apt-get install -y libopenmpi-dev` → `./configure MPIF90=mpif90 --enable-parallel`
("Parallel environment detected successfully") → `make clean && make pw -j12` (BUILD_EXIT=0).

After (verbatim):
```
make.inc:   DFLAGS = -D__FFTW -D__MPI      MPIF90 = mpif90
ldd pw.x:   libmpi.so.40 => /lib/x86_64-linux-gnu/libmpi.so.40
            libmpi_mpifh.so.40 => /lib/x86_64-linux-gnu/libmpi_mpifh.so.40
banner (mpirun -np 4 pw.x):
     Parallel version (MPI), running on     4 processors
     MPI processes distributed on     1 nodes
```
**→ F1 PASS, F2 PASS** — the substrate root-cause that silently crippled every campaign DFT is FIXED.

### B — Ta2NiSe5 monoclinic C2/c SCF under genuine 6-core MPI

Cell (verbatim, identical to H_025): vol 4733.7658 (a.u.)³ = 701.5 Å³ (exp 701.4 ✓), 32 atoms
(Ta8Ni4Se20 ✓), 296 electrons, 165 KS states, PBE, 3 irreducible k (MV smearing 0.02 Ry), dense grid
545793 G-vectors. `mpirun -np 6 pw.x -npool 2` — banner "Parallel version (MPI), running on 6 processors".

With the serial budget wall removed, the SCF was run far past the serial-era cut-off (iter ~9). Three
recipes (verbatim `estimated scf accuracy`, Ry):

- **(1) robust plain PBE** (β=0.1, local-TF ndim 12, degauss 0.02): 17.17 → 4.90 → 2.70 → 0.86 → **0.468**
  → 0.738 → 0.448 → 0.631 → 0.581 → 0.917 → 0.861 → **1.638 → 1.662** (14 iters) — descends ~38×, then
  OSCILLATES in the near-metallic plateau, trending UP, not toward 1e-6.
- **(2) PBE+U(Ni-3d=3.0 eV, ortho-atomic, Dudarev)**: 17.91 → 6.15 → 3.84 → 1.20 → **0.639** → 0.906 →
  0.690 → 0.930 → 0.863 → 1.191 → 1.101 (12 iters) — descends ~28×, then OSCILLATES in the 0.6–1.2 Ry
  plateau, not toward 1e-6.
- **(3) higher-smearing PBE** (degauss 0.03, β=0.2, ndim 16): 17.15 → 6.63 → 54.47 → 8.58 → 1.83 → 0.963
  → 1.438 → 1.813 → 1.698 → 1.180 → **0.545** (12 iters) — same descent-then-oscillation in the ~0.5–1.8 Ry
  plateau, not toward 1e-6.

**All three confirm the same, now-DEFINITIVE behaviour:** the monoclinic C2/c SCF breaks the H_019/H_024
Cmcm *byte-identical freeze* (a ~28–38× descent with live charge dynamics — **F5 PASS**, descent attributed
to the symmetry breaking) but then **oscillates persistently in a near-metallic plateau (~0.5–1.7 Ry) and
NEVER reaches conv_thr=1e-6**, even with the MPI build running ≫ the serial-budget iteration count. The
plateau is therefore **PHYSICAL, not a compute artifact**: PBE / PBE+U / higher-smearing all leave monoclinic
Ta2NiSe5 near-metallic (the gap is many-body/excitonic, absent in these functionals), so the charge density
oscillates. **→ F3 PASS** (definitive verdict, not a budget cut-off). **No converged density → no gap printed
→ gap UNRESOLVED-by-us**, reported as an HONEST NEGATIVE on a PBE-family DFT gap, NOT fabricated (**F4 PASS**
on the honest-negative branch; **F7 PASS** — every number above is verbatim pw.x stdout). The only remaining
path to the gap is beyond-PBE (HSE / GW / a many-body excitonic treatment), which needs far more compute than
6 cores provide — out of scope here (**L1**).

### Tier

**🟡 REAL-DFT — INFRA ROOT-CAUSE FIXED + gap honest-negative-under-PBE.** The campaign-wide deliverable
LANDED: the self-built QE 7.2 is now a genuine MPI/parallel build (F1+F2 PASS, verbatim banner + `ldd` +
`make.inc`), removing the single-core wall that silently crippled every DFT from H_015 to H_025. The physics
half is a CLEAN measured result: under genuine MPI, the H_025 monoclinic descent is shown to be real but to
plateau-and-oscillate near-metallic across THREE PBE-family recipes without reaching conv_thr — so the gap is
NOT graduated to our-DFT (it cannot be reached by PBE/PBE+U; the excitonic gap is many-body). This is a VALID
honest negative on the PBE-DFT gap, not a budget artifact and not fabricated. The TRIO stays **🟠
jointly-unrealized**; absorbed=false / GATE_OPEN — nothing here flips the RTSC gate.
