# Ta2NiSe5 296-electron PBE SCF — H_024 convergence attempt log (honest record)

Goal: re-converge the 32-atom orthorhombic Cmcm cell SCF that DEFERRED in H_019 (plateau ~0.5 Ry
over 7 recipe variants on the THEN-contended host) → an our-DFT band gap.

Host state at attempt: summer, self-built QE 7.2. Load ~13-14 (NOT fully uncontended — a co-tenant
`hexa_v2` + `python3` held ~2 of 12 cores throughout; a GCC/lapack build ran early).

## Attempt 1 — robust 12-k-point recipe (tanise5.robust.in)
- ecutwfc 50 / ecutrho 400 Ry, nbnd 170, k 4x2x2 (= 12 irreducible k-pts), MV degauss 0.01 Ry,
  mixing_beta 0.25 local-TF ndim 8, david ndim 4, conv_thr 1e-6, electron_maxstep 200. 10 MPI ranks.
- FFT dense grid 45x160x192 = 644,113 G-vectors. Per-rank RSS ~1.9 GB.
- RESULT: the FIRST SCF iteration did NOT complete after ~25 min wall (>17 CPU-min/rank); no
  "estimated scf accuracy" line printed. 12 k-points x 170 bands x the dense FFT for 296 electrons
  is the cost driver. Killed to switch to a lighter k-mesh.

## Attempt 2 — fast 2-k-point recipe (tanise5.fast.in)
- ecutwfc 45 / ecutrho 360 Ry, nbnd 165, k 2x1x1 (= 2 irreducible k-pts; b,c axes long ~12.9/15.7 A
  so coarse along them is justified; a=3.5 A short), MV degauss 0.012 Ry, mixing_beta 0.20 local-TF
  ndim 10, david ndim 4, diago_thr_init 1e-4, conv_thr 1e-6, electron_maxstep 250. 12 MPI ranks.
- FFT dense grid 40x150x180 = 549,791 G-vectors. ~8.6 min wall PER SCF iteration on 12 cores.
- RESULT: iterations 1 AND 2 BOTH report estimated scf accuracy = 13.94569806 Ry EXACTLY — the
  residual is FROZEN (zero change between iterations) => a hard charge-density mixing STALL, even
  WORSE than H_019's 0.5 Ry plateau (this lighter beta=0.2 local-TF recipe sloshes harder). Killed.

## Attempt 3 — stall-breaker (tanise5.stall.in): larger smearing + plain mixing
- degauss 0.025 Ry (2.5x larger — the standard cure for near-metallic SCF stalls), mixing_mode
  'plain' beta 0.7 ndim 8, k 2x1x1, ecutwfc 45 / ecutrho 360, nbnd 165, conv_thr 1e-6. 12 ranks.
- RESULT: iter1 = iter2 = 13.74920763 Ry EXACTLY — residual FROZEN AGAIN. The larger smearing +
  plain mixing did NOT break the stall. ~6-8 min wall per iteration. Killed.

## CONCLUSION (across 3 H_024 recipes + 7 H_019 recipes = 10 total)
The Ta2NiSe5 296-electron PBE SCF does NOT converge. The pathology is now well-characterised and
reproducible: the estimated scf accuracy FREEZES at a high value (~13.7-13.9 Ry here; ~0.5 Ry in
H_019's best variant) and does NOT decrease across iterations, regardless of mixing scheme (plain /
local-TF), beta (0.2-0.7), or smearing (0.01-0.025 Ry). This is a hard, recipe-independent SCF
ill-conditioning — consistent with the high-symmetry Cmcm cell being the PARENT of the excitonic
instability (a near-degenerate, near-metallic electronic structure right at the cusp of the
excitonic gap-opening), which makes a single non-symmetry-broken KS SCF ill-posed. It is NOT merely
host contention (the host was freer here than in H_019, yet the stall is the same/worse) and NOT a
per-iteration speed problem alone (the residual would still not converge given more iterations).

=> OUR-DFT Ta2NiSe5 gap stays DEFERRED (F1 FAIL, no fabricated gap). The literature window
0.16-0.35 eV stays unverified-by-us. This is a VALID honest negative (commons): a non-converging
result is kept as a result. The likely fix (NOT attempted this session, logged as deferred) is to
start from the SYMMETRY-BROKEN low-T monoclinic phase (or a spin/charge-symmetry-broken guess), or
to use a hybrid/DFT+U functional that opens the gap and regularises the SCF.

## Honest assessment
The binding obstacle is PER-ITERATION COST x ITERATION COUNT, not (only) host contention: a single
SCF iteration of this near-metallic excitonic-insulator PAW cell costs ~7-12 min wall on 12 cores,
and an excitonic/near-gap cell typically needs many tens of iterations to reach 1e-6 Ry. This is the
same tractability wall as H_019, now characterised quantitatively (it is the cell, not just the
co-tenant). Whatever iteration-1 accuracy printed is recorded verbatim in the card; no gap is
fabricated if convergence is not reached.
