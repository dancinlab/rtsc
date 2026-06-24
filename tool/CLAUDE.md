# tool — shared HYPOTHESES harness (rtsc)

Anima-parity: the shared, deterministic execution skeleton for HYPOTHESES hypothesis
cards lives here in repo-root `tool/`. Heavy compute (DFT / DFPT / el-ph predictors,
ED solvers) stays in `src/`; `tool/` holds only the closed-form / threshold logic a
card's falsifiers are evaluated against.

## Key files

- `rtsc_harness.py` — stdlib-only (math) primitives + falsifier ENGINE:
  - `two_lever_box_check` (H_001 room-T design box), `geometric_bkt_tc_band`,
    `allen_dynes_tc` (H_002), `AMBIENT_TC_CEILING_K`, `ROOM_T_K`, +@ chain helpers
    (`proximity_bilayer_levers`, `stacked_tc`, `spacer_window`, `erl_rep_rate_ceiling`, …).
  - `Falsifier` dataclass + `evaluate(metrics, falsifiers)` → JSON-safe verdict ledger.
    API-compatible with the sibling lumen `tool/lumen_optics.py`.
- `rtsc_candidates.py` — LIVING candidate-materials registry + verifier (검증기) for the +@
  trilayer. Holds layer-A flat-band hosts + layer-B bosonic-glue hosts, each property =
  `(value, source, verified)`; `verify()` / `verify_pair()` REUSE the rtsc_harness engine (no
  new verifier) to run pre-registered falsifiers — only VERIFIED properties pass, unverified
  ones surface as `gaps`. GROW IT every research round (fill gaps with sourced values; never
  fabricate / tune-to-green). Current lead (🟠): CoSn / hBN(2ML) / Ta2NiSe5, box-clearing on
  paper but jointly unrealized (absorbed=false).

## Rules

- Dependency-free (stdlib only) and deterministic — a card run must reproduce byte-for-byte.
- No fitting / no hidden constants beyond documented defaults; all inputs explicit.
- Per-hypothesis run scripts under `state/<hX>/` import from here via a relative path.

## Compute substrate (summer pool host)

- **QE 7.2 is now an MPI (PARALLEL) build** (fixed in H_026, 2026-06-25). The canonical
  `~/qe_build/q-e-qe-7.2/bin/pw.x` was a **SERIAL** build through H_025 (`make.inc`
  `MPIF90=gfortran`, `DFLAGS=-D__FFTW` only, no `-D__MPI`; `ldd` showed no MPI lib; banner
  "Serial version") — so the prior `mpirun -np 12` launched 12 *redundant* serial copies on
  1 core each. THAT was the true tractability wall behind every H_015/H_019/H_024/H_025 DFT.
  Root-cause fix (H_026): `sudo apt-get install libopenmpi-dev` (OpenMPI 4.1.6 runtime was
  present but the linkable dev `.so` symlinks were missing → `configure` fell back to serial),
  then `cd ~/qe_build/q-e-qe-7.2 && ./configure MPIF90=mpif90 --enable-parallel && make pw -j12`.
  Source of truth = the build's own banner: `mpirun -np N pw.x` now prints **"Parallel version
  (MPI), running on N processors"** and `make.inc` has `DFLAGS = -D__FFTW -D__MPI`, `ldd` links
  `libmpi.so.40`. summer = 6 physical cores / 12 threads → use `mpirun -np 6` (not 12; OpenMPI
  counts physical slots) with a sensible `-npool` for k-point parallelism.
- A second, independent **parallel QE 7.5** lives in the conda env `~/miniforge3/envs/qe/bin/pw.x`
  (OpenMPI 5.0.10) — banner "Parallel version (MPI & OpenMP)". Either works; the self-built one
  is canonical.
