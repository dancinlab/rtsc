---
id: H_028
slug: ni3in-layer-a
title: Is Ni3In a BETTER layer-A flat-band metal than CoSn for the +@ trio — does its kagome flat band supply the geometry lever (∫tr g ≥ 2) ALREADY at/near E_F, dodging H_027's extreme-doping wall (CoSn needs 1.58 holes/CoSn f.u.)? From OUR converged spin-polarized PBE SCF (Ni6In2, 134 e⁻, MPI per H_026) we measure the flat band's bandwidth W and its offset dE rel E_F, the metric integral ∫tr g, and the native filling ν.
domain: rtsc
status: real-dft
exploration_method: backup-candidate research (state/research-backup-candidates-2026-06-25.md, A-backup-1 Ni3In) named Ni3In as the kagome flat-band metal whose flat band sits ~50 meV NEAR E_F (Ye 2021 arXiv:2106.10824) — a direct dodge of H_027's doping wall. This card tests that dodge with REAL DFT.
verification_method: W1 (pre-register frozen) + W2 (falsifier-7) + W3 (deterministic DFT analysis on OUR converged PBE bands under MPI) + W5 (honest-limits-7) + tool-self-report (verbatim pw.x parallel banner)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
compute: summer pool host (QE 7.2 MPI build per H_026, and conda QE 7.5; analysis = local numpy/scipy, deterministic, byte-reproducible)
since: 2026-06-25
---

# H_028 — Is Ni3In a better layer-A than CoSn (flat band AT E_F, dodging the doping wall)? (rtsc)

## Hypothesis

CoSn (the lead 🟢-path's layer A) has its kagome flat band ~0.44 eV (near band) / ~1.45 eV (deep band)
BELOW E_F, so H_027 found that bringing the flat band onto E_F needs EXTREME doping (1.58 holes/CoSn
f.u., chemical substitution — beyond gating). **Ni3In is reported as a flat-band metal whose Ni-3d
kagome flat band sits ~50 meV NEAR E_F (arXiv:2106.10824, Ye 2021).** If real, Ni3In DODGES the doping
wall entirely. **The falsifiable claim: does Ni3In supply the geometry lever (∫tr g ≥ 2) with its flat
band ALREADY within ~0.1–0.2 eV of E_F (no/low doping), at a favourable filling ν — making it a BETTER
layer-A than CoSn on accessibility? Or does it fail (∫tr g < 2, or the flat band is NOT actually at E_F
in OUR DFT, or a competing order intrudes)?** We measure W, dE(rel E_F), ∫tr g, and ν from OUR
converged spin-polarized PBE Ni3In bands on the MPI-fixed host (H_026).

## Why

- **Directly dodges the H_027 wall.** H_027 found CoSn's geometry lever (∫tr g=2.855≈QGT 2.87) and
  filling (ν=0.507) SURVIVE but the doping-to-E_F is EXTREME (1.58 h/f.u.) — the lead path's only
  remaining weakness is ACCESSIBILITY. Ni3In's claimed flat-band-at-E_F (~50 meV) is the natural escape:
  if confirmed, the +@ geometry layer needs no doping at all.
- **Ni3In is a documented correlated kagome metal.** Ye 2021 (arXiv:2106.10824) reports a partially
  filled Ni-3d kagome flat band driving strange-metal transport; DMFT (arXiv:2605.21386) and ARPES
  (arXiv:2503.09704) corroborate. No reported static CDW/SDW at the flat band — relatively H_014-light.
  But its ⟨g⟩ (quantum geometry) was UNVERIFIED (research GAP) — this card computes it.
- **실측전 research + cheapest route.** A converged PBE SCF + the deterministic TB-fit metric route
  (same as H_024/H_027, byte-reproducible) answers the position/geometry/filling questions with one
  SCF + one bands run; no rental beyond the free summer host.

## Predictions

- **H28.1 (flat-band position — the dodge)**: the flattest band near E_F on the Γ-K-M-Γ plane is
  reported with its bandwidth W AND its centre offset dE rel E_F, judged AT/NEAR E_F (|dE|≤0.20 eV,
  dodges the wall), MODERATELY OFF (0.20<|dE|≤0.50), or FAR (|dE|>0.50, no dodge). Compared to CoSn's
  −0.44 eV / −1.45 eV.
- **H28.2 (∫tr g — the geometry lever)**: the metric integral I = (1/2π)∫tr g d²k for the flat band,
  by the same NN-kagome TB-fit + projector-FD route as H_024/H_027, judged ≥2 (lever met) or <2 (not),
  compared to CoSn's 2.855.
- **H28.3 (filling ν at the NATIVE E_F)**: the flat band's filling ν at the real (undoped) E_F is
  reported, ν(1−ν) compared to the 0.25 half-filling max, judged FAVOURABLE/MODERATE/EDGE-SUPPRESSED.
- **H28.4 (honest verdict)**: a stated BETTER-than-CoSn / NOT-BETTER verdict — Ni3In is a better
  layer-A iff (∫tr g≥2) AND (flat band at/near E_F, |dE|≤~0.2 eV, no extreme doping). A negative on
  ANY axis (g<2, or band not at E_F in OUR DFT, or a competing order) is reported plainly, NOT tuned.
  is_green=False preserved; trio stays 🟠 regardless.

## Run Protocol

- **Compute**: summer pool host. QE 7.2 MPI build (H_026), `mpirun -np 6 pw.x -npool 2`, 6 live ranks
  confirmed via pgrep (verbatim parallel banner in the Verdict). Deterministic analysis = local
  numpy/scipy.
- **Structure**: Ni3In hexagonal DO19 (Ni3Sn-type), space group P6₃/mmc, a=5.286 Å, c=4.243 Å
  (celldm(1)=9.9892 a.u., c/a=0.80268), Ni6In2 = 8 atoms/cell = 2 Ni3In f.u.; Ni on 6h, In on 2c
  (Ye 2021 arXiv:2106.10824; consistent with Materials Project Ni3In). Pseudopotentials: Ni
  PBE-spn-kjpaw_psl.1.0.0 (PAW, spin-polarized) + In PBE-dn-rrkjus_psl.1.0.0 (US).
- **SCF**: spin-polarized PBE, ecutwfc 60 / ecutrho 480 Ry, MP smearing degauss 0.02, 8×8×8 k-mesh,
  conv_thr 1e-8, starting_magnetization Ni=0.2. 134 valence e⁻, 80 KS states.
- **(1) position**: Γ-K-M-Γ (kz=0 kagome plane) bands run (nbnd=80) → locate the flattest band near
  E_F, report W and dE.
- **(2) geometry**: NN-kagome 3-orbital TB fit (t,e0) to the flat 3-band manifold of OUR bands →
  I = (1/2π)∫tr g d²k by projector finite-difference on a 60×60 grid (Γ band-touching capped,
  integrable) — same route as H_024/H_027.
- **(3) filling**: smeared occupation of ONLY the flat band at the NATIVE E_F → ν, ν(1−ν).
- **rigid-band cross-check**: the e⁻/cell shift to put E_F at the flat centre (compared to CoSn's
  1.58 h/f.u.), to quantify "how much of a dodge".
- **artifacts**: `state/h028_ni3in_layer_a_2026_06_25/` — decks + `out/h028_geometry.out`.

## Criteria

- **verdict_rule**: tier set by what is ACTUALLY computed. Ni3In is a BETTER layer-A than CoSn iff
  I≥2 (geometry lever) AND |dE|≤~0.2 eV (flat band at/near E_F, dodging the doping wall) AND ν
  favourable. If the flat band is NOT at E_F in OUR DFT (PBE position can disagree with ARPES — H_019
  precedent), or I<2, or a competing order intrudes, Ni3In FAILS as a strict CoSn-beater on that axis
  and the result is reported plainly. The TRIO (Ni3In or CoSn / hBN / Ta2NiSe5) stays 🟠
  jointly-unrealized; absorbed=false; GATE_OPEN — no simulation flips that.

## Falsifiers (≥4 — pre-registered, measurable)

- **F1_position_honest**: PASS = the flat band's W AND dE(rel E_F) are reported from OUR converged
  bands, with an explicit AT-E_F / OFF-E_F / FAR judgement against the stated |dE| thresholds, and an
  honest comparison to the cited ~50 meV (Ye 2021) — including if OUR PBE disagrees. FAIL = no number,
  or a position silently reframed to look at-E_F.
- **F2_geometry_met_or_not**: PASS = I = (1/2π)∫tr g d²k is reported and judged ≥2 (met) or <2 (not),
  via the same non-tuned TB-fit route as H_024/H_027, NN-only caveat named. FAIL = a hand-set I.
- **F3_filling_nu_honest**: PASS = the flat-band filling ν at the NATIVE E_F is reported and ν(1−ν)
  compared to the 0.25 max with a FAVOURABLE/MODERATE/EDGE-SUPPRESSED judgement. FAIL = ν not computed
  or asserted without the occupation integral.
- **F4_verdict_honest**: PASS = a stated BETTER-than-CoSn / NOT-BETTER verdict on Ni3In as layer-A,
  is_green=False preserved, any adverse axis (g<2 / band-off-E_F / competing order) reported plainly.
  FAIL = a claimed is_green=True, or an adverse result suppressed to make Ni3In look like a winner.
- **F5_scf_converged_or_honest**: PASS = the spin-polarized SCF either CONVERGES (E_F, magnetization
  reported verbatim) OR is reported honestly as non-converging/delicate (the equally valid negative);
  the magnetic state is reported as found. FAIL = a fabricated converged E_F / magnetization.
- **F6_preregister**: a post-hoc edit to predictions/criteria/falsifiers → pre-register violation.
- **F7_no_fabrication**: every Verdict number is verbatim pw.x stdout/banner or a labeled deterministic
  analysis output; no value hand-set to clear a falsifier.

## Honest Limits (≥5)

- **L1 (PBE flat-band POSITION is functional-sensitive)**: the load-bearing dodge claim (flat band at
  E_F) rests on OUR PBE E_F vs the band centre. PBE can place a correlated 3d flat band tens-to-hundreds
  of meV off its true (DMFT/ARPES) position; Ni3In is explicitly a CORRELATED strange metal (Ye 2021)
  where DMFT (arXiv:2605.21386) shifts spectral weight. So OUR dE is the PBE position, NOT a guarantee
  the real flat band sits where PBE puts it — reported with the cited ~50 meV for contrast.
- **L2 (∫tr g is a TB-fit, not a Bloch-state QGT)**: no wannier90.x is built, so I is the NN-kagome TB
  fit to OUR PBE bands + the analytic projector metric (H_024 route) — NN-only, omits further-neighbour
  hopping/orbital admixture and the In-p / Ni-s screening; the absolute normalisation carries that
  caveat. There is no directly-measured QGT for Ni3In (unlike CoSn's 2.87) to anchor against.
- **L3 (magnetic PBE Ni3In)**: OUR SCF is spin-polarized; Ni3In's PBE magnetic ground state (moment
  reported as found) may over- or under-estimate the real (possibly paramagnetic correlated) state.
  A flat band can spin-split, and the geometry/filling are reported for the PBE magnetic solution; the
  real correlated metal may differ (L1).
- **L4 (ν at the native E_F is a single-spectrum, path-sampled estimate)**: ν is the smeared occupation
  of the flat band sampled on the Γ-K-M-Γ path at the native E_F, not a full-BZ integral; it is
  indicative, and the flat band's hybridization with neighbouring bands blurs "the" flat-band capacity.
- **L5 (kagome assignment / multiple flat manifolds)**: Ni3In, like CoSn, can host more than one orbital
  flat manifold; the NN-kagome 3-band TB fit picks the contiguous group around the flattest near-E_F
  band, which may mix non-kagome character. The "flat band" identified is the flattest near-E_F band in
  OUR bands, not a symmetry-proven pure kagome flat band.
- **L6 (no glue / no joint realization)**: this card evaluates ONLY layer A. The trio Ni3In/hBN/Ta2NiSe5
  glue scale is still the Ta2NiSe5 many-body literature value (H_026 showed PBE under-gaps it); the
  joint trilayer is unbuilt. Even a perfect Ni3In layer A leaves the trio 🟠 jointly-unrealized.
- **L7 (absorbed=true unaffected)**: nothing here flips the RTSC gate; that still requires accredited
  4-probe transport + Meissner expulsion + measured H_c2 / T_c. No material is claimed to BE an RTSC.

## Cross-Links

- **parent**: H_027 (the CoSn extreme-doping wall this card tries to dodge) · H_024 (the ∫tr g TB-fit
  route reused here) · H_026 (fixed the MPI build used here) · research-backup-candidates-2026-06-25.md
  (named Ni3In as A-backup-1).
- **registry**: `tool/rtsc_candidates.py` LAYER_A — adds Ni3In with the DFT-found g_mean (honest
  verified flag) + flat-band-at-E_F note.
- **literature**: Ni3In flat-band correlated kagome metal Ye arXiv:2106.10824 (2021); DMFT
  arXiv:2605.21386; ARPES origin arXiv:2503.09704; CoSn QGT Kang arXiv:2412.17809; Peotta–Törmä
  arXiv:1506.02815.

## Verdict

**🟡 REAL-DFT — Ni3In is NOT a better layer-A than CoSn: it FAILS the dodge.** In OUR converged
paramagnetic PBE DFT the Ni-kagome flat band sits **−1.57 eV BELOW E_F** (band 56, W=0.255 eV; the
whole narrow-d manifold spans −0.84 to −1.57 eV) — even DEEPER than CoSn's near-E_F band (−0.44 eV,
H_027) and comparable to CoSn's deep band (−1.45 eV, H_024). The cited ~50 meV-near-E_F (Ye 2021) is a
CORRELATED / DMFT / strange-metal position; plain PBE does NOT reproduce it. The geometry lever IS met
(I = (1/2π)∫tr g = **2.854 ≈ CoSn's 2.855 ≈ measured QGT 2.87** — the Ni 6h kagome net is real,
NN=a/2), but the flat band is fully occupied at the native E_F (**ν=1.0 → ν(1−ν)=0, D_s
edge-suppressed**), so without doping it supplies NO superfluid-weight lever. **Worse than CoSn on a
second axis:** the spin-polarized SCF is magnetically UNSTABLE (accuracy oscillates 11–37 Ry, absolute
magnetization swings 11–27 μB/cell across 3 recipes) — a frustrated high-DOS magnetic flat-band metal,
a competing-order (H_014) risk CoSn does not carry. Net: Ni3In **does NOT dodge H_027's doping wall in
PBE** and adds a magnetic instability — it is NOT a better layer-A. The lead A-layer stays CoSn; the
trio CoSn/hBN/Ta2NiSe5 stays **🟠 jointly-unrealized**; absorbed=false / GATE_OPEN. Tier set by what was
ACTUALLY computed: a clean deterministic geometry/position/filling result on OUR converged paramagnetic
PBE bands, plus a reproducible spin-polarized magnetic-instability finding.

### (1)+(2)+(3) — verbatim `out/h028_geometry.out` (deterministic numpy/scipy on OUR bands, NO tuning)

```
========================================================================
H_028 — does Ni3In supply the flat-band GEOMETRY LEVER at/near E_F?
  (dodging CoSn's H_027 extreme-doping wall)
  source: OUR converged NON-SPIN-POL (paramagnetic ref) PBE SCF (8-atom
          Ni6In2, 134 e-, conv 1e-7) -- spin-pol SCF is magnetically
          UNSTABLE (high-DOS flat band at E_F, abs-mag swings 11-27 uB;
          reported separately as competing-order evidence).
          E_F=16.5270 eV, alat=9.9892 a.u. = a=5.2861 A)
========================================================================

--- (1) FLAT BAND on the Gamma-K-M-Gamma plane (flattest near E_F) ---
band  meanE(eV)  W(eV)    dE=mean-EF
  56   14.9600  0.2547  -1.5670
  60   15.6866  0.2734  -0.8404
  59   15.6148  0.3046  -0.9122
  57   15.1692  0.3450  -1.3578
  58   15.2936  0.4288  -1.2334
  53   14.0563  0.4433  -2.4707
=> FLAT BAND = band 56, centre 14.9600 eV (= -1.5670 eV rel E_F), W=0.2547 eV
=> POSITION VERDICT: dE=-1.567 eV -> FAR from E_F (|dE|>0.50 eV) -> heavy doping (no dodge)
   (compare CoSn near band -0.44 eV [H_027], deeper -1.45 eV [H_024])

--- (2) GEOMETRY: NN-kagome TB fit + projector-FD tr g ---
3-band kagome group bands [55, 56, 57], span=0.3758 eV -> t=0.0626 eV, e0=-1.6922 eV (rel E_F)
Gamma band-touching: 30/3600 grid pts capped (integrable singularity)
<tr g>_BZ = 10.9904 A^2 ; I = (1/2pi) int tr g d2k = 2.8536
CoSn (H_027/H_024): I = 2.855 ~= measured QGT 2.87 (arXiv:2412.17809)
=> GEOMETRY VERDICT: I=2.854 -> MET (I>=2, geometry lever supplied)

--- (3) FILLING nu of the flat band at the NATIVE E_F (no doping) ---
flat band (band 56) mean occupation at native E_F=16.5270: nu = 1.000
D_s^geom ~ nu(1-nu) = 0.0000  (maximum 0.25 at nu=0.5)
=> FILLING VERDICT: nu=1.000, nu(1-nu)=0.0000 = 0% of 0.25 max -> EDGE-SUPPRESSED (nu->0 or 1, D_s reduced)

========================================================================
SUMMARY (all from OUR converged PBE DFT; no tuning):
  flat band     : band 56, W=0.255 eV, dE=-1.567 eV rel E_F -> FAR from E_F
  geometry I    : 2.854 -> MET
  flat filling  : nu=1.000, nu(1-nu)=0.000 -> EDGE-SUPPRESSED
========================================================================
```

### Converged SCF + verbatim parallel banner (H_026 MPI build; tool-self-report)

QE 7.2 MPI build, `mpirun -np 6 pw.x -npool 2`, 6 live ranks confirmed via pgrep:
```
     Parallel version (MPI), running on     6 processors
     MPI processes distributed on     1 nodes
     number of atoms/cell      =            8
     number of electrons       =       134.00
     number of Kohn-Sham states=           80
```
Paramagnetic reference SCF (nspin=1, MV smearing degauss 0.025, beta 0.1 ndim 8): converged in 22 iters
to conv_thr 1e-7, **E_F = 16.5270 eV**, total energy −2847.68314186 Ry. Structure: DO19 Ni3Sn-type
(P6₃/mmc) a=5.286 Å c=4.243 Å, Ni 6h kagome net (tau(1)=(0.5,0,0.2007) confirms the kagome edge-midpoint
net, NN=a/2), In 2c. Pseudos: Ni PBE-spn-kjpaw_psl.1.0.0 + In PBE-dn-rrkjus_psl.1.0.0.

### Spin-polarized magnetic instability (verbatim `out/spinpol_instability.txt`) — competing-order evidence

The spin-polarized SCF (the physical magnetic state) does NOT converge — across recipes (beta 0.3; beta
0.1 local-TF; beta 0.05 MV) the accuracy OSCILLATES and the magnetization swings violently:
```
recipe beta=0.05 MV-smearing estimated scf accuracy (Ry):
  1: 33.70  2: 27.86  3: 15.30  4: 30.25  5: 11.33  6: 37.26   (oscillating, no descent to 1e-6)
absolute magnetization (uB/cell): 18.16, 17.29, 11.03, 27.56, 20.47, 26.01  (huge, swinging)
total magnetization (uB/cell):     1.37,  1.48,  2.19,  2.05,  2.13,  2.11  (small net, large local)
```
Large LOCAL moments (abs ~11–27 μB) with small NET moment = a frustrated antiferromagnetic-like Ni
kagome whose near-E_F high DOS drives an SCF instability — Ni3In is a correlated/strange-metal (Ye 2021),
and this is a competing magnetic-order risk (H_014) that CoSn does not carry. (This is also why the
paramagnetic nspin=1 reference was used for the clean band/geometry measurement — L3.)

### Falsifiers

- **F1_position_honest**: **PASS** — band 56 W=0.255 eV at dE=−1.567 eV (whole narrow manifold −0.84 to
  −1.57 eV), judged FAR from E_F (>0.5 eV) → NO dodge; the disagreement with the cited ~50 meV (Ye 2021,
  a correlated/DMFT position) is stated plainly, not reframed.
- **F2_geometry_met_or_not**: **PASS** — I=2.854 (TB-fit route, same as H_024/H_027) ≥2 → MET; NN-only
  caveat named (L2). Not hand-set (matches CoSn's 2.855 by the band-manifold geometry).
- **F3_filling_nu_honest**: **PASS** — ν=1.0 at the native E_F (flat band fully occupied, far below E_F)
  → ν(1−ν)=0 → EDGE-SUPPRESSED, computed from the occupation integral, reported plainly.
- **F4_verdict_honest**: **PASS** — NOT-BETTER-than-CoSn verdict stated (fails the dodge + adds a magnetic
  instability); is_green=False preserved; the adverse position + instability reported, not tuned.
- **F5_scf_converged_or_honest**: **PASS** — the paramagnetic SCF CONVERGED (E_F, energy verbatim); the
  spin-polarized SCF is reported honestly as magnetically unstable/non-converging (the equally valid
  negative), magnetization swings reported verbatim — no fabricated converged magnetic E_F.
- **F6_preregister**: not triggered (criteria frozen before runs).
- **F7_no_fabrication**: **PASS** — every number is verbatim pw.x stdout/banner or labeled deterministic
  analysis output; the unstable spin-pol SCF is reported as such.

### Structural finding

The backup-candidate research (A-backup-1) named Ni3In as the kagome flat-band metal whose flat band sits
~50 meV NEAR E_F (Ye 2021) — the natural escape from H_027's CoSn extreme-doping wall. OUR real PBE DFT
does NOT confirm that escape: the Ni-kagome flat-band manifold sits ~0.84–1.57 eV BELOW E_F (paramagnetic
PBE), i.e. AT LEAST as deep as CoSn's, so Ni3In needs the SAME (or worse) doping-to-E_F and does NOT dodge
the wall. The geometry lever is genuinely present and strong (I=2.854 ≈ CoSn's QGT 2.87), but a geometry
lever below E_F is exactly the CoSn situation H_027 already characterised as accessibility-limited. On top
of that, Ni3In's spin-polarized SCF is magnetically unstable (frustrated large-local-moment kagome),
adding a competing-order risk CoSn lacks. Net: Ni3In is NOT a better layer-A than CoSn — the lead A-layer
stays CoSn. (Caveat L1: the ~50 meV near-E_F flat band is a CORRELATED feature; a DMFT/+U/GW treatment
could pull it toward E_F — PBE under-correlation is a real limit, so this is a PBE-level negative on the
dodge, not a proof Ni3In can never host a near-E_F flat band.) The trio stays **🟠 jointly-unrealized**;
absorbed=false / GATE_OPEN — no simulation flips that.

### Records

`state/h028_ni3in_layer_a_2026_06_25/` — `decks/{scf_nm.in, scf_spinpol.in, bands.in,
h028_ni3in_geometry.py}`, `out/{h028_geometry.out, spinpol_instability.txt, scf_nm_converged.out,
bands.out}`.
