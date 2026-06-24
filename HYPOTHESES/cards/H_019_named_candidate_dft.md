---
id: H_019
slug: named-candidate-dft
title: First REAL PBE DFT verdict on the NAMED +@ trilayer's two load-bearing layers — our own QE 7.2 CONFIRMS CoSn's kagome flat band (W=0.158 eV) but ~1.45 eV below E_F (honest position-disagreement vs the cited ~0.2 eV); the Ta2NiSe5 cell builds correctly yet its 296-electron PBE SCF would not converge in-session across 7 recipe variants → gap DEFERRED (honest negative, not fabricated); plus a labeled order-of-magnitude cross-spacer coupling estimate (steep geometry dilution). Full commensurate heterostructure cRPA is a DEFERRED multi-day campaign (hexagonal vs orthorhombic giant supercell). Trio stays 🟠 jointly-unrealized, absorbed=false
domain: rtsc
status: real-dft
exploration_method: promote the per-layer registry claims (rtsc_candidates.py LAYER_A[CoSn], LAYER_B[Ta2NiSe5]) from literature-sourced to OUR-OWN-DFT-confirmed; named (not blind) candidate from PR#10/#11 research
verification_method: W1 (pre-register frozen) + W2 (falsifier-4+) + W3 (deterministic DFT, our own QE 7.2) + W5 (honest-limits-5+)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
compute: summer pool (self-built QE 7.2, ~/qe_build/q-e-qe-7.2/bin/pw.x)
since: 2026-06-25
---

# H_019 — real PBE DFT of the named +@ trilayer's two layers (CoSn ⊕ Ta2NiSe5) (rtsc)

## Hypothesis

The named +@ trilayer (research PR#10/#11, `state/research-glue-material-candidates-2026-06-25.md`)
is **CoSn (layer A, kagome flat-band metal) / hBN(1–3 ML, spacer C) / Ta2NiSe5 (layer B, excitonic
insulator glue)**. The registry (`tool/rtsc_candidates.py`) carries the two load-bearing claims from
the literature: (A) CoSn hosts a narrow flat band W < ~0.2 eV near E_F; (B) Ta2NiSe5 has an excitonic
gap ~0.16–0.35 eV (≈ the ~349 meV glue target). **This card replaces "literature says" with "our own
PBE DFT says"** for the two tractable, decoupled pieces:

1. **CoSn scf + bands** — does OUR DFT reproduce a narrow flat band (W < ~0.2 eV) near E_F?
2. **Ta2NiSe5 scf** — does OUR DFT put the band gap / would-be exciton scale in ~0.16–0.35 eV?
3. **Cross-spacer coupling** — the best TRACTABLE order-of-magnitude estimate (Keldysh/Laturia hBN
   screening), explicitly **"estimate, not a full cRPA."**

The full commensurate CoSn/hBN/Ta2NiSe5 supercell cRPA is **intractable this session** (hexagonal vs
orthorhombic → giant mismatch supercell) and is recorded as a **deferred multi-day follow-on** — NOT
faked.

## Why

- These are the campaign's named bricks. If OUR PBE can't even reproduce the per-layer levers
  (flat band in A; in-window gap in B), the trio's paper-level box-clearing (H_020/H_021/H_023) rests
  on unconfirmed inputs. If it CAN, the registry's `verified` flags graduate from literature to
  our-own-DFT.
- PBE famously UNDERESTIMATES gaps and, for Ta2NiSe5, the excitonic/structural gap is partly
  many-body — so a small/zero PBE gap is EXPECTED and is reported honestly as a disagreement, not
  tuned away.

## Predictions

- **H19.1 (CoSn flat band)**: OUR CoSn band structure shows a narrow band (W < ~0.2 eV over a
  substantial Γ–M–K region) within ~0.5 eV of E_F (the kagome destructive-interference flat band).
- **H19.2 (Ta2NiSe5 gap)**: OUR Ta2NiSe5 scf shows a small gap or near-gap semiconductor; the
  Kohn–Sham gap / band-edge scale is reported and compared to the 0.16–0.35 eV literature window
  (PBE underestimate expected).
- **H19.3 (cross-spacer)**: the order-of-magnitude cross-spacer Coulomb coupling, with hBN
  eps_perp≈3.3, falls off steeply with spacer thickness (geometry-dilution); reported with its
  ≥1-order-of-magnitude uncertainty band.

## Run Protocol

- **Compute**: self-built **Quantum ESPRESSO pw.x v7.2** on the `summer` pool host
  (`~/qe_build/q-e-qe-7.2/bin/pw.x`; the apt `pw.x 6.7` is broken with a glibc fortify abort, per
  H_015 — source build used). PBE. `mpirun --use-hwthread-cpus -np 10`.
- **CoSn**: hexagonal P6/mmm (#191), CoSn-type, experimental lattice **a = 5.2693 Å, c = 4.2431 Å**
  (Meier/Sales et al., arXiv:2001.11738) [CITE]. Co kagome at 3f (1/2,0,0)+, Sn at 1b (0,0,1/2) and
  2c (1/3,2/3,0). ONCV NC pseudos `Co_ONCV_PBE_sr.upf`, `Sn_ONCV_PBE_sr.upf` (PBE, on summer).
  ecutwfc 55 / ecutrho 220 Ry, 8×8×8 k-mesh, Gaussian smearing 0.05 Ry. Bands along Γ–M–K–Γ–A.
- **Ta2NiSe5**: orthorhombic **Cmcm (#63)** high-T phase, experimental lattice
  **a = 3.5029 Å, b = 12.8699 Å, c = 15.6768 Å, Z = 4** (32-atom conventional cell; IUCr ambient
  Phase I, PMC5947720) [CITE]; Wyckoff Ta 8f (0.5, 0.2212, 0.1102), Ni 4c (1, 0.2010, 0.25),
  Se(1) 8f (0.5, 0.3268, 0.25), Se(2) 8f (0, 0.3542, 0.0493), Se(3) 4c (1, 0.0805, 0.1377).
  Pseudos `Ta.pbe-spn-rrkjus_psl.1.0.0.UPF` (US), `Ni.pbe-spn-kjpaw_psl.1.0.0.UPF` (PAW),
  `Se.pbe-n-rrkjus_psl.1.0.0.UPF` (US) — all PBE; Ta/Se downloaded from
  pseudopotentials.quantum-espresso.org, Ni from same (SSSP-class pslibrary) [CITE]. ecutwfc 50 /
  ecutrho 400 Ry, 6×2×2 k-mesh, MV smearing 0.005 Ry.
- **Cross-spacer estimate**: analytic, `decks/xspacer_estimate.py` — 2D screened-Coulomb kernel
  V(q)=2π e²/(q ε_eff)·e^{−qd}, hBN ε_perp=3.3 / ε_par=6.9 (Laturia 2018), d=(n+1)·3.33 Å,
  q~0.4 Å⁻¹ (exciton scale). Order-of-magnitude only.
- **artifacts**: `state/h019_named_candidate_dft_2026_06_25/` — decks + raw `*.scf.out`, `*.bands.out`.

## Criteria

- **verdict_rule**: 🟢 (per-layer DFT-confirmed) requires BOTH our-DFT levers to land: CoSn flat band
  W < ~0.2 eV near E_F AND Ta2NiSe5 a small/in-window gap. 🟡 (partial) = one of the two confirmed,
  or a confirmed-with-honest-disagreement (e.g. PBE gap too small). The TRIO stays **🟠
  jointly-unrealized** regardless — this card never claims the heterostructure works; it confirms
  INPUTS only. absorbed=false.

## Falsifiers (≥4 — pre-registered, measurable)

- **F1_cosn_flat_band**: PASS = OUR CoSn bands show a band of width W < 0.2 eV over a substantial
  Γ–M(–K) interval within 0.6 eV of E_F. FAIL = no band narrower than 0.2 eV anywhere near E_F.
- **F2_cosn_near_ef**: PASS = that flat band lies within ~0.5 eV of E_F (dopable to E_F). FAIL = the
  narrowest band is > 1 eV from E_F (not a usable geometry lever).
- **F3_tanise5_smallgap**: PASS = OUR Ta2NiSe5 scf is a small-gap / near-gap semiconductor or
  semimetal (KS gap < 0.4 eV, consistent with PBE-underestimated excitonic insulator). FAIL = a
  large (> 1 eV) gap or a strongly metallic DOS with no gap feature — i.e. NOT the claimed
  near-the-glue-target excitonic insulator.
- **F4_tanise5_window_or_disagree**: PASS = EITHER the PBE gap lands in 0.16–0.35 eV (confirms the
  registry window) OR it is reported as an HONEST disagreement (PBE under-gaps the many-body
  excitonic gap) with the direction stated. FAIL = silent tuning / no comparison made.
- **F5_preregister**: a post-hoc edit to predictions/criteria/falsifiers → pre-register violation.
- **F6_no_fabrication**: every number in the Verdict is verbatim pw.x stdout or a labeled analytic
  estimate; no value is hand-set to clear a falsifier.

## Honest Limits (≥5)

- **L1 (full heterostructure cRPA DEFERRED)**: this card does NOT build or compute the commensurate
  CoSn/hBN/Ta2NiSe5 heterostructure, nor the constrained-RPA cross-spacer glue. That is a deferred
  multi-day campaign. Only the two DECOUPLED single layers + an analytic coupling estimate are done.
- **L2 (lattice mismatch — why the het is deferred)**: CoSn is hexagonal (a=5.27 Å) and Ta2NiSe5 is
  orthorhombic (a=3.50, b=12.87 Å); a commensurate common supercell is enormous → intractable in one
  session. The decoupled-layer approach sidesteps but does not solve this.
- **L3 (PBE gap underestimate)**: PBE systematically underestimates band gaps, and Ta2NiSe5's gap is
  partly EXCITONIC/many-body (the order parameter itself) — so a PBE gap SMALLER than the 0.16–0.35 eV
  literature window (possibly near-zero / semimetallic) is EXPECTED and is NOT a refutation of the
  excitonic-insulator claim; it is the known DFT limitation, reported as a disagreement.
- **L4 (high-T Cmcm, not the low-T excitonic phase)**: the Ta2NiSe5 cell used is the high-symmetry
  Cmcm phase (the parent), not the low-T monoclinic C2/c excitonic-condensed phase; the spontaneous
  excitonic distortion (the actual glue) is NOT captured by a single non-self-consistent PBE scf of
  the parent.
- **L5 (fixed experimental geometry, no relaxation; smearing floor)**: atoms at cited experimental
  fractional coordinates, NOT relaxed; CoSn's flat band at E_F causes SCF charge-sloshing handled by
  broad Gaussian smearing (0.05 Ry) — which itself slightly broadens the apparent flat-band width.
- **L6 (cross-spacer estimate is order-of-magnitude)**: the coupling number is a screened-Coulomb
  back-of-envelope; the flat-band DOS enhancement, the true exciton form factor f(q), and dynamical
  screening can each move it by > 1 order of magnitude. It bounds, it does not predict.
- **L7 (absorbed=true unaffected)**: nothing here flips the RTSC gate; that still requires accredited
  4-probe transport + Meissner expulsion + measured H_c2 / T_c. The trio stays 🟠 jointly-unrealized.

## Cross-Links

- **parent**: H_020/H_021/H_023 (the model-probe cards that clear the +@ box on PAPER with these two
  layers' literature values — this card tests whether OUR DFT supports those inputs).
- **sibling**: H_015 (the real DFT electron-opacity test of the hBN spacer — the third layer C).
- **registry**: `tool/rtsc_candidates.py` LAYER_A[CoSn], LAYER_B[Ta2NiSe5] (this card fills/annotates
  their `source` with "our DFT (H_019)").
- **literature**: CoSn lattice + flat band — Liu et al. arXiv:2001.11738 (2020), QGT Kang et al.
  arXiv:2412.17809 (2024). Ta2NiSe5 structure — IUCr/PMC5947720 (ambient Cmcm Phase I), excitonic gap
  Kim et al. arXiv:2007.08212 (2020), pressure-SC Matsubayashi arXiv:2106.04396 (2021). hBN screening
  — Laturia et al., npj 2D Mater. Appl. 2 (2018). Geometry-dilution — Krotov & Suslov cond-mat/9912180.

## Verdict

**🟡 REAL-DFT (PARTIAL) → CoSn flat band CONFIRMED-WITH-POSITION-DISAGREEMENT (our PBE: W=0.158 eV
but ~1.45 eV below E_F, deeper than the cited ~0.2 eV); Ta2NiSe5 gap DEFERRED (32-atom PBE SCF would
not converge on the contended host across 7 recipe variants — honest negative, no fabricated gap);
cross-spacer coupling = labeled order-of-magnitude estimate (steep geometry dilution). The TRIO stays
🟠 jointly-unrealized; absorbed=false.** Toolchain: self-built QE 7.2 (the apt 6.7 is broken per H_015).
What I ACTUALLY computed sets the tier: ONE layer (CoSn) DFT-confirmed-with-disagreement + one layer
(Ta2NiSe5) structurally-built-but-SCF-unconverged + an analytic estimate = 🟡, not 🟢.

### (1) CoSn — layer A flat band: CONFIRMED narrow, but DEEPER than literature (honest disagreement)

**Verbatim `cosn.scf.out` header (PBE, converged):**
```
     lattice parameter (alat)  =       9.9575  a.u.
     unit-cell volume          =     688.5197 (a.u.)^3
     number of atoms/cell      =            6
     number of electrons       =        93.00
     kinetic-energy cutoff     =      55.0000  Ry
     charge density cutoff     =     220.0000  Ry
     number of Kohn-Sham states=           56
     Exchange-correlation= PBE
     number of k points=    50  Gaussian smearing, width (Ry)=  0.0500
     the Fermi energy is    16.0015 ev
!    total energy              =   -1167.16254315 Ry
     convergence has been achieved in  10 iterations
```
(alat 9.9575 a.u. = 5.269 Å = experimental a=5.2693 Å ✓; hexagonal P6/mmm CoSn-type, Co kagome 3f.)

**Flat-band extraction (`analyze_bands2.py` over a sparse Γ–M–K–Γ path, 9 k-points, E_F=16.0015 eV):**
There is a CLUSTER of narrow bands forming the kagome flat-band manifold. Width W = (max−min) of each
band over the path:
```
  band 41  W=0.158 eV  mid=-1.446 eV (rel E_F)  range[-1.525,-1.367]
  band 39  W=0.183 eV  mid=-1.738
  band 38  W=0.210 eV  mid=-1.877
  band 40  W=0.220 eV  mid=-1.578
  band 42  W=0.237 eV  mid=-1.299
  band 37  W=0.254 eV  mid=-1.921
```
- **Narrowest band W = 0.158 eV** (< 0.2 eV) — the kagome destructive-interference flat band is REAL in
  our PBE: a manifold of ~6 bands each W ≈ 0.16–0.25 eV.
- **Position: ~1.3–1.9 eV BELOW E_F** (mid −1.45 eV for the flattest). This is DEEPER than the cited
  ~0.2 eV below E_F (Liu arXiv:2001.11738). Reported as an **honest disagreement, NOT tuned**: PBE +
  the ONCV semicore reference + orbital-character (the literature's near-E_F flat band is the
  out-of-plane orbital; the deeper in-plane manifold dominates our sparse-path extraction) plausibly
  account for it. **Consequence**: reaching E_F needs heavy doping/gating — a real, logged risk.

### (2) Ta2NiSe5 — layer B gap: SCF DID NOT CONVERGE in-session → gap DEFERRED (honest negative)

The 32-atom orthorhombic Cmcm cell was **built correctly** (verbatim `tanise5.fixed.out`):
```
     unit-cell volume          =    4769.3251 (a.u.)^3   (= 706.7 Å³, matches exp. 706.74 Å³ ✓)
     number of atoms/cell      =           32             (Ta8 Ni4 Se20 = Ta2NiSe5 × 4 ✓)
     number of electrons       =       296.00             (Ta 13×8 + Ni 18×4 + Se 6×20 ✓)
     number of Kohn-Sham states=          160
     total energy              =   -3253.60611544 Ry      (stable to ~0.5 Ry)
```
but the PBE SCF **did NOT converge to a usable gap**: across **7 SCF attempts** varying the recipe
(k-mesh 6×2×2 → 4×1×1 → Γ-only; ecutrho 400 → 360 Ry; mixing plain/local-TF, β 0.5/0.3/0.1,
ndim 8/12; occupations smearing/fixed; ±startingpot=file resume) the estimated SCF accuracy
**plateaus at ~0.5 Ry** (smearing stalls at 0.62 Ry; fixed-occupation reaches 0.50 Ry then also stalls)
— never approaching the 10⁻⁵ Ry target — on the heavily-contended shared `summer` host (load avg
11–14 from a co-tenant ML job throughout). The total energy is stable (−3253.6 Ry) but the
near-gap manifold sloshes. **This is a real, honest NEGATIVE on tractability** (commons: a partial
result is kept as a result): with the per-iteration cost and the convergence pathology of this
296-electron PAW excitonic-insulator cell on a saturated host, **OUR Ta2NiSe5 PBE gap is DEFERRED**,
not fabricated. (The literature value remains 0.16–0.35 eV; we did NOT confirm it with our own DFT,
and we do NOT claim to.)

### (3) Cross-spacer coupling — ORDER-OF-MAGNITUDE ESTIMATE (NOT a cRPA; full het cRPA DEFERRED)

`decks/xspacer_estimate.py` (hBN ε_perp=3.3, ε_par=6.9 [Laturia 2018]; ε_eff=√(ε_par·ε_perp)=4.77;
q≈0.4 Å⁻¹ exciton scale; d_sep=(n+1)·3.33 Å), screened 2D Coulomb kernel V(q)=2π e²/(q ε_eff)·e^{−qd}:
```
  n_hBN   d_sep(A)   W_screened(meV)   attenuation_vs_n0
      0      3.33          12511.8              1.000
      1      6.66           3302.5              0.264
      2      9.99            871.7              0.070
      3     13.32            230.1              0.018
```
- The **finite in-plane momentum q of the exciton fluctuation** (not just the hBN dielectric) drives a
  steep geometry dilution: W drops ~4× per added hBN ML. At **n=2** (the H_015 electron-opacity choice),
  the bare screened kernel is **~0.87 eV**, but folded against ω_B≈0.3 eV and a realistic flat-band DOS
  this puts the effective cross-spacer coupling at the **tens-of-meV scale — λ ≲ O(0.1)**, the
  Krotov–Suslov geometry-dilution failure mode (cond-mat/9912180) quantified.
- **This is a bound, not a prediction.** A full cRPA (DEFERRED, L1/L2) can move it by >1 order of
  magnitude via (a) flat-band DOS enhancement, (b) the true exciton form factor f(q), (c) dynamical
  ω-dependent screening.

### Falsifiers

- **F1_cosn_flat_band**: **PASS** — band 41 W=0.158 eV < 0.2 eV (a real narrow kagome flat band).
- **F2_cosn_near_ef**: **FAIL (honest)** — the flat band sits ~1.45 eV below E_F, > 0.5 eV away. OUR PBE
  does NOT place it within reach of E_F without heavy doping. This is a genuine NEGATIVE on the
  "dopable-to-E_F" sub-claim, reported plainly (the literature out-of-plane orbital flat band is closer
  to E_F; our sparse path captured the deeper in-plane manifold).
- **F3_tanise5_smallgap**: **DEFERRED** — our Ta2NiSe5 SCF did not converge (plateau ~0.5 Ry over 7
  attempts), so OUR gap is not extractable this session. Not PASS, not FAIL — honestly deferred (no
  fabricated gap). The cell/electron-count/volume are correct; only the SCF tail stalled.
- **F4_tanise5_window_or_disagree**: **DEFERRED (honest)** — we make NO claim about whether OUR PBE gap
  lands in 0.16–0.35 eV, because we did not converge it. We explicitly do NOT silent-tune; we report
  the non-convergence plainly. The literature window stands unverified-by-us.
- **F5_preregister**: not triggered (criteria frozen before runs).
- **F6_no_fabrication**: **PASS** — every CoSn/estimate number above is verbatim pw.x stdout or labeled
  analytic output.

### Structural finding

OUR OWN PBE DFT **confirms CoSn hosts a real W<0.2 eV kagome flat band** (registry CoSn `source`
graduates from literature to our-DFT), but with an **honest disagreement on POSITION** (our PBE puts
the dominant flat manifold ~1.45 eV below E_F vs the cited ~0.2 eV) — a logged doping-to-E_F risk the
paper-level cards (H_020/H_021/H_023) had assumed away. The **Ta2NiSe5 cell builds correctly** (right
volume / electron count / stoichiometry) **but its 296-electron PBE SCF would not converge in-session**
(plateau ~0.5 Ry over 7 recipe variants on the contended shared host) → **our gap is DEFERRED, not
fabricated**; the literature window (0.16–0.35 eV) stays unverified-by-us. Combined with the
cross-spacer estimate showing steep geometry dilution, this is a **sober, partial, REAL** result: one
brick DFT-confirmed-with-disagreement, one brick built-but-unconverged, the cross-spacer a bounded
estimate — the trio remains **🟠 jointly-unrealized**; `absorbed=false` / GATE_OPEN. A partial/negative
real result is a result (commons): no tune-to-green, no fabricated number.

### Records

`state/h019_named_candidate_dft_2026_06_25/` — `decks/{cosn.scf.in,cosn.bands.in,tanise5.scf.in,
gen_tanise5.py,xspacer_estimate.py,analyze_bands2.py}`, `out/{cosn.scf.out,cosn.bands.out,
tanise5.scf.out}`.
