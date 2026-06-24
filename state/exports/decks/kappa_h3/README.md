# κ-H₃(Cat-EDT-TTF)₂ — RTSC H-SSH terminal-DFT deck pack (RESUME RECIPE)

> RTSC FLEET ambient lane (`state/fb-geom-lambda/ambient/kappa_h3_dft.md`). The reopened
> H-corner's terminal off-diagonal H-SSH host. Full from-scratch crystal QE relax+DFPT is
> **PENDING** (hard org-crystal DFT, ~220 atoms/cell — too big for one shared-free-box run).
> This pack is the honest **resume recipe**: the staged decks + the exact `hexa cloud exec summer`
> commands to compute the real-host O-H-O Ω + ∂t/∂u + t when a sized box (or shards) is available.
> The TB-grade real-host number (the verdict driver) is in `../../../state/fb-geom-lambda/ambient/kappa_h3_dft.md`.

## ⚠ hexa deck gap (d_deck_always — guard filed)
`hexa deck rtsc` has **no molecular-cluster / organic-crystal prototype** (all current prototypes
are parametric crystalline hydride lattices). So these decks are NOT `hexa deck`-built — the gap is
filed to the hexa-lang handoff registry (`sidecar handoff ls hexa-lang`, id `b6346955`) requesting a
`molecular_cluster` prototype with (1) XYZ/CIF input, (2) a frozen-phonon proton-displacement scan
template, (3) projwfc/wannier90 t-extraction. Until that lands, molecular-crystal RTSC targets are
hand-staged here with the d-rules enforced manually (correct masses, ecut, k-grid, SCF aids).

## Real structure (sourced; arXiv:1408.3162 = PRB 92,035102; Shimozawa Nat Commun arXiv:1703.00324)
- space group **C2/c**, a=29.43, b=8.36, c=11.13 Å, β=100.92° (50 K), Z=4, ~220 atoms/cell.
- f.u. **C₂₄H₁₅O₄S₁₂** (55 atoms); two Cat-EDT-TTF π-units + the bridging [O···H···O]⁻ protons.
- O···O = **2.45 Å**, O–H = 1.23/1.22 Å (H-side **centered single-well**, proton delocalized).
- inter-dimer transfers (DFT four-band): b1=241 (intra), **b2=75, p=40 meV (inter-dimer = the SSH t)**,
  bandwidth W=312 meV, t′/t≈1.25, J≈80–100 K. **Deep dimer-Mott insulator** at ambient.
- ⚠ EMPIRICAL HEADWIND: under hydrostatic pressure → **charge-ordered INSULATOR**, never metal/SC.

## TRACTABILITY (d11 sizing — why the full crystal is PENDING)
~220 atoms/cell, 12 S (Z=12, needs ≥40 Ry wfc / 320 Ry rho with USPP, or NC ≥60/480), molecular
solid (vdW/dispersion needed: vdw_corr='grimme-d3'). A full crystal vc-relax + ph.x DFPT on the
O-H-O mode = **days on a single CPU box**, OOM-risk on a 64 GB shard. → NOT a one-run free-box job.
The tractable substitute (done TB-grade in the lane) is the published-geometry t(proton) frozen-phonon
on the dimer pair. The full-crystal decks below are the resume recipe for a sized GPU/HPC pod.

## Decks (staged; run order)
1. `relax.in`        — C2/c cell vc-relax (cell+ions), D3 dispersion, SCF aids (d15) — confirm geometry.
2. `scf.in`          — converged SCF on the relaxed cell (shared out/ for all downstream).
3. `nscf_bands.in`   — band structure (verbosity='high', #k≥100) — confirm Mott gap / band near E_F.
4. `frozen_phonon/`  — proton-displacement scan: 7 scf decks displacing the bridge H along O···O by
                       u = -0.15 … +0.15 Å; ∂t/∂u from the change in the inter-π Wannier transfer.
5. `ph_oho.in`       — ph.x DFPT pinned to the O-H-O stretch Γ mode → Ω(O-H-O) (cross-check the
                       frozen-phonon Ω). d6 dynamical-stability precheck (no imaginary O-H-O mode).
6. `w90/`            — wannier90 downfold (inter-dimer π Wannier) → t(u) → ∂t/∂u → g = ∂t/∂u·u0 → g/t.

## Resume commands (summer FREE; -np ≤ 6; serial SCF; pgrep -c pw.x before relaunch)
```bash
# pool-qe-detached-fire-recipe: taskset + serial, NO billing pod
hexa cloud exec summer 'pgrep -c pw.x && echo BUSY && exit 0
  cd /tmp/kappa_h3 && QE=/home/summer/miniforge3/envs/qe/bin
  $QE/pw.x -nk 1 -nd 1 < relax.in > relax.out 2>&1'        # step 1 (long; check vc-relax converged)
hexa cloud exec summer 'cd /tmp/kappa_h3 && QE=/home/summer/miniforge3/envs/qe/bin
  $QE/pw.x < scf.in > scf.out 2>&1'                         # step 2
# step 4 scan (7 decks): loop u in -0.15..0.15, pw.x scf, projwfc -> t(u)
# step 6: pw2wannier90 + wannier90.x -> inter-dimer t Wannier -> dt/du
```
Pseudopotentials: SSSP-efficiency (PBEsol) C/H/O/S — `hexa cloud exec summer` grep the pseudo dir for
all four elements (d13 coverage check) before firing. dft = PBE + vdw_corr='grimme-d3' (molecular solid).

## What the lane already settled WITHOUT this run (TB-grade)
- g/t (off-diagonal SSH) from the published t=40 meV + O-H-O exponential-overlap ∂t/∂u ≈ **0.26–0.44**
  (reaches the QMC dome onset g*/t=0.38) → **coupling axis = candidate PASS**, Tc-ceiling 278–446 K.
- **carrier axis CLOSES (empirical)**: pressure → CO insulator, the Mott→metal lever fails on record.
- the from-scratch crystal ∂t/∂u + Ω **PENDING** — would sharpen g/t but cannot flip the carrier gate.
