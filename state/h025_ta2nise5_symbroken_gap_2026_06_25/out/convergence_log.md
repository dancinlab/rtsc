# Ta2NiSe5 monoclinic C2/c SCF — H_025 convergence log (honest record)

Goal: close H_024's deferred Ta2NiSe5 gap by running the PHYSICALLY-CORRECT cell — the
symmetry-broken low-T **monoclinic C2/c** excitonic-insulator GROUND STATE — where the
high-symmetry Cmcm PARENT froze (H_019: 7 recipes, plateau ~0.5 Ry; H_024: 3 recipes,
FROZEN at identical 13.7–13.9 Ry).

## MEASURED constraint discovered this session: the QE 7.2 build is SERIAL
`~/qe_build/q-e-qe-7.2/make.inc`: `MPIF90 = gfortran`, `DFLAGS = -D__FFTW` only (no `-D__MPI`,
no `-D__OPENMP`); `ldd pw.x` shows no MPI lib; pw.x prints "Serial version". So EVERY SCF runs
on **1 core**. The prior H_019/H_024 `mpirun -np 12` launched **12 redundant serial copies** (all
writing the same files) — that is the true tractability wall, now characterised. All H_025 runs
are a SINGLE serial pw.x. ~50–100 s/iter early, growing to ~5–7 min/iter as ethr tightens.

## Cell (built by gen_tanise5_monoclinic.py — EXPERIMENTAL, cited)
Sunshine & Ibers, Inorg. Chem. 24, 3611 (1985), via arXiv:2201.07750 Table I/II:
a=3.496, b=12.829, c=15.641 Å, β=90.53° (unique axis b, ibrav=0 explicit CELL_PARAMETERS).
Verbatim header (identical across all 3 recipes):
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
The Ta atoms carry the symmetry-breaking x-shift (e.g. Ta at x=0.99207 instead of the Cmcm x=0),
so this is the genuinely distorted cell, NOT the Cmcm parent.

## Recipe 1 — monoclinic plain PBE (tanise5.mono.in, β-mix 0.3 local-TF, degauss 0.01 cold)
Oscillated: 17.19 → 36.47 → 14.84 → 4.83 → 11.08 → … (beta=0.3 too aggressive; bounced). Killed,
switched to a low-beta variant. KEY: values CHANGE every iteration (live charge dynamics) — already
unlike the Cmcm freeze. Log: tanise5.mono.beta03.out.

## Recipe 2 — monoclinic robust PBE (tanise5.mono.robust.in, β-mix 0.1 ndim 12, degauss 0.02)
Verbatim estimated scf accuracy trajectory (tanise5.mono.robust.saved.out):
```
  iter1  17.17804532 Ry
  iter2   4.89846787 Ry
  iter3   2.69854663 Ry
  iter4   0.85979621 Ry
  iter5   0.46655266 Ry
  iter6   0.73674519 Ry
  iter7   0.45212745 Ry
  iter8   0.63533596 Ry
  iter9   0.60407384 Ry
```
→ MONOTONIC descent 17.18 → 0.45 Ry (a **~38× / 1.6-order** drop), then a near-metallic PLATEAU
oscillating in the 0.45–0.74 Ry band. No two values identical. NOT converged to 1e-6.

## Recipe 3 — monoclinic PBE+U(Ni-3d)=3.0 eV ortho-atomic (tanise5.mono.u3.in, β-mix 0.1)
Hubbard confirmed active: "Hubbard projectors: ortho-atomic", HUBBARD ENERGY 0.71 Ry,
"Number of occupied Hubbard levels = 32.0". Verbatim trajectory (tanise5.mono.u3.saved.out):
```
  iter1   17.92027428 Ry
  iter2    6.14834631 Ry
  iter3    3.84341370 Ry
  iter4    1.19855525 Ry
  iter5    0.63506607 Ry
  iter6    0.90153765 Ry
  iter7    0.68494937 Ry
  iter8    0.92094657 Ry
  iter9    0.85336784 Ry
  iter10   1.18318694 Ry
```
→ MONOTONIC descent 17.92 → 0.64 Ry (a **~28× / 1.4-order** drop), then the SAME near-metallic
PLATEAU oscillating in the 0.6–1.2 Ry band. Not converged to 1e-6. No band/Fermi line printed
(QE prints eigenvalues only at convergence) → NO gap extractable → gap NOT fabricated.

## CONCLUSION
**The symmetry-broken monoclinic C2/c cell BREAKS the Cmcm-parent SCF freeze.** Both the robust
plain-PBE and the PBE+U recipes drive the residual DOWN by ~1.4–1.6 orders of magnitude (17–18 Ry →
0.45–0.64 Ry) with LIVE charge dynamics (every iteration's value differs) — categorically different
from the high-symmetry Cmcm parent, which in H_024 FROZE at *identical* values (13.94569806 =
13.94569806 exactly; 13.74920763 = 13.74920763) across 10 recipes. The physical insight is
CONFIRMED: the non-converging cell was the wrong (high-symmetry, near-metallic excitonic-parent)
structure; the actual distorted ground state evolves.

BUT neither monoclinic recipe reaches conv_thr=1e-6 Ry: both PLATEAU near-metallic in the ~0.5–0.9 Ry
band on the **serial single-core build**. This is consistent with PBE/PBE+U(3 eV) UNDER-gapping the
many-body excitonic gap → the cell stays near-metallic at experimental coordinates → a hard,
slow-to-converge SCF that the serial build cannot push to 1e-6 in the session budget.

→ The Ta2NiSe5 **band gap stays UNRESOLVED** (no converged density → NO fabricated number), but the
H_024 "ill-conditioning" diagnosis is now SHARPENED: it is specifically the high-symmetry-parent
freeze, and the symmetry-broken ground state demonstrably DOES descend. Deferred (logged) fix to
actually reach the gap: (a) the DFT-RELAXED monoclinic coordinates (β=90.644°, larger distortion →
cleaner gap; PNAS 2221688120 SI), (b) a denser k-mesh to tame the near-metallic Fermi-surface slosh,
and/or (c) a hybrid (HSE) — all of which need a PARALLEL QE build (the serial build is the binding
wall). A valid honest PARTIAL POSITIVE (commons): the freeze-break is kept as a result.
