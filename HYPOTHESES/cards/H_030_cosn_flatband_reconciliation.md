---
id: H_030
slug: cosn-flatband-reconciliation
title: Reconcile the CoSn doping wall — does CoSn host BOTH a shallow (~−0.1 to −0.5 eV, measured-ARPES) AND a deep (~−1.45 to −2.0 eV) kagome flat manifold, and which one carries the ∫tr g=2.86 QGT geometry lever? RE-ANALYSIS (no new SCF) of OUR saved CoSn DFT (H_019 non-spin-pol cell + H_027/H_029 spin-pol Co3Sn3 cell) shows BOTH manifolds exist; the ∫tr g≈2.855 lever is a SHAPE property of the NN-kagome geometry and is essentially identical on EITHER manifold (deep band-42 H_024 vs shallow band-45 H_027). The "1.58 h/f.u. EXTREME" doping figure is NOT an artifact of analysing the deep band — H_027 already used the SHALLOW band-45 (−0.44 eV). But it IS sensitive to the TARGET: reaching the PBE flat-band CENTER (−0.44 eV) costs 1.58 h/f.u. EXTREME, while reaching the MEASURED ARPES depth (~−0.10 eV, arXiv:2102.08979) costs only 0.20 h/f.u. PHYSICAL — an 8× swing driven by the flat-band DOS pileup. Verdict = TRADE-OFF (the wall PARTLY dissolves: EXTREME for the strong-geometry band center, MODEST for the measured weak-geometry onset). absorbed=false unchanged.
domain: rtsc
status: closed-supported
exploration_method: RE-ANALYSE existing converged CoSn DFT output (no new SCF) to reconcile the method-lever research (measured flat d-band ~100meV below E_F) against the campaign's "1.45eV / 1.58 h/f.u. EXTREME" doping wall — enumerate ALL narrow manifolds vs E_F, attribute the ∫tr g lever to a specific band, and re-cost the doping to BOTH the measured-ARPES depth and the PBE band center
verification_method: W1 (pre-register frozen) + W2 (falsifier-6) + W3 (deterministic re-analysis of OUR saved pw.x bands — byte-reproducible numpy) + W5 (honest-limits-7)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
compute: NONE new — pure re-parse of saved summer pw.x output (H_019 cosn.bands.out; H_027/H_029 cosn_bands.dat.gnu + scf.out); analysis = local numpy/math, deterministic
since: 2026-06-25
---

# H_030 — CoSn flat-band reconciliation: shallow vs deep manifold + the ∫tr g attribution + re-costed doping (rtsc)

## Hypothesis

The method-lever research (`state/research-fabrication-method-levers-2026-06-25.md`) flagged a
discrepancy: the **MEASURED** CoSn kagome flat d-band sits **~100 meV below E_F**
(arXiv:2102.08979 = PRMat 5, 044202; Kang/Comin ARPES line), reachable by "a few % Fe/In"
(MODEST doping). But the campaign's CoSn doping WALL (H_027/H_029) reports the flat band needs
**~1.58 holes/CoSn f.u. = EXTREME** doping to reach E_F. **The binding question: are these
DIFFERENT bands?** CoSn hosts multiple kagome-derived flat manifolds; if the QGT-relevant one
(∫tr g=2.856, matching the measured QGT 2.87) is the SHALLOW ~100 meV band rather than a deep
~1.45 eV one, the "extreme doping" wall could be a BOOKKEEPING ARTIFACT (analysing the wrong band)
and mostly dissolve. We RE-ANALYSE OUR existing CoSn DFT (no new SCF) to (1) enumerate every narrow
manifold vs E_F, (2) attribute the ∫tr g lever to a specific band, and (3) re-cost the doping to
BOTH the measured-ARPES depth and the PBE band center — reporting whichever way it falls.

## Why

- **Cheapest, highest-value in-silico test named by the method-lever research** (its §"What is
  IN-SILICO-testable next", item 1): pure post-processing of saved H_024/H_027 output; settles a
  *number*, not a measurement. CLAUDE.md 실측전-research: research already located the measured
  ~100 meV band; this card reconciles it against our DFT before any new compute.
- **The doping wall is the campaign's strongest adverse finding** (the lead 🟢-path's binding
  obstacle, H_027/H_029). If it is partly a target-choice artifact it must be corrected honestly;
  if it is real it must stand. Neither direction is privileged (no tune-to-revive-the-candidate).
- **PBE is known to over-deepen correlated narrow d-bands** (~140 meV ARPES offset already noted in
  H_024); the same shallow band can read deeper in our PBE than in ARPES — a quantifiable systematic.

## Predictions

- **H30.1 (both manifolds exist)**: OUR saved bands show BOTH a shallow narrow (W<0.25 eV) kagome
  flat band at ~−0.1 to −0.6 eV AND a deeper narrow manifold at ~−1.4 to −2.0 eV (or report
  honestly if only one resolves per cell).
- **H30.2 (∫tr g attribution)**: the ∫tr g=2.855–2.856 geometry lever is attributed to a SPECIFIC
  band; stated whether it is a shape-property common to BOTH manifolds or unique to one.
- **H30.3 (re-costed doping)**: the rigid-band hole cost to reach (a) the PBE flat-band CENTER and
  (b) the MEASURED ARPES depth (~−0.10 eV) is reported in h/f.u., each judged PHYSICAL(<0.3) /
  STRETCH(0.3–0.7) / EXTREME(>0.7).
- **H30.4 (verdict)**: a stated ARTIFACT / REAL / TRADE-OFF verdict on the H_027/H_029 doping wall,
  reconciled with the measured QGT 2.87 and the measured ~100 meV ARPES, is_green=False preserved.

## Run Protocol

- **Compute**: NONE new. Re-parse of OUR saved converged pw.x output:
  - `state/h019_named_candidate_dft_2026_06_25/out/cosn.bands.out` (non-spin-pol cell, 52 bands,
    81 k-pts Γ-M-K-Γ, E_F=16.0015 eV) → `decks/enum_manifolds_h019cell.py`.
  - `state/h027_doped_cosn_geometry_survival_2026_06_25/decks/cosn_bands.dat.gnu` (spin-pol Co3Sn3
    cell, 60 bands, 161 k, E_F=14.7132 eV; Γ-K-M-Γ kz=0 plane = first 121 k) +
    `.../decks/scf.out` (k-weighted SCF eigenvalues, both spins) → `decks/enum_manifolds_h027cell.py`
    + `decks/recost_doping.py` (rigid-band gaussian-CDF carrier count, σ=0.10 eV, same engine as the
    H_027 `rigidband.py`).
- **∫tr g attribution**: reuse the H_024/H_027 verbatim outputs (I=2.856 deep band-42; I=2.855
  shallow band-45) — both already computed by the SAME NN-kagome TB-fit + projector-FD route; no
  recompute needed (the metric integral is the same to 3 sig figs on either band).
- **artifacts**: `state/h030_cosn_flatband_reconciliation_2026_06_25/` — decks + `out/{manifolds_h019cell.out,
  manifolds_h027cell.out, recost_doping.out}`.

## Criteria

- **verdict_rule**: tier set by what is ACTUALLY parsed. **ARTIFACT** = the QGT lever lives ONLY on
  a shallow ~−0.1 eV band that costs ≤0.3 h/f.u. and the "1.58 h/f.u." traces to analysing a deeper
  band ⇒ wall dissolves. **REAL** = the QGT lever genuinely requires a band whose accessible E_F
  costs >0.7 h/f.u. across the board ⇒ wall stands. **TRADE-OFF** = shallow band has the (same)
  geometry but reaching its PBE center is EXTREME while reaching the measured onset is MODEST ⇒
  the EXTREME figure is target-sensitive, the wall partly dissolves. The TRIO stays
  **🟠 jointly-unrealized**; absorbed=false; GATE_OPEN — no re-analysis flips that.

## Falsifiers (≥4 — pre-registered, measurable)

- **F1_both_manifolds_enumerated**: PASS = every narrow (W<~0.25 eV) kagome flat band within ±3 eV
  of E_F is tabulated VERBATIM from OUR saved bands with its (E_flat−E_F), stating whether a shallow
  (~−0.1 to −0.6 eV) AND a deep (~−1.4 to −2.0 eV) one exist. FAIL = a band asserted without the
  parsed table, or the multiplicity hand-waved.
- **F2_trg_attribution_honest**: PASS = the ∫tr g=2.855–2.856 lever is attributed to a SPECIFIC
  band index, stating plainly whether it is a shape-property common to both manifolds (verbatim H_024
  deep-band I=2.856 AND H_027 shallow-band I=2.855) or unique to one. FAIL = a hand-set attribution.
- **F3_doping_recost_both_targets**: PASS = the rigid-band hole cost to BOTH the PBE flat-band center
  AND the measured ARPES depth (~−0.10 eV) is reported in h/f.u. with the PHYSICAL/STRETCH/EXTREME
  call, via the same gaussian-CDF engine as H_027. FAIL = only one target costed, or a number reframed.
- **F4_verdict_unbiased**: PASS = a stated ARTIFACT / REAL / TRADE-OFF verdict reconciled with the
  measured QGT 2.87 and the measured ~100 meV ARPES, is_green=False preserved, NOT biased toward
  dissolving the wall to revive the candidate. FAIL = a verdict that suppresses an adverse number or
  inflates a favourable one to flip the lead path green.
- **F5_no_new_scf_claimed**: PASS = no fabricated new-SCF result; every number is verbatim from a
  SAVED pw.x file or a labeled deterministic re-parse. FAIL = a new converged band/E_F claimed
  without the run.
- **F6_preregister**: a post-hoc edit to predictions/criteria/falsifiers → pre-register violation.

## Honest Limits (≥7)

- **L1 (PBE flat-band offset)**: the reconciliation rests on PBE over-deepening the shallow band by
  ~0.2–0.3 eV vs ARPES (our shallow-band TOP edge −0.34 eV vs ARPES center ~−0.10 eV). That offset
  is the KNOWN PBE narrow-d systematic (H_024 noted ~140 meV ARPES offset), but its exact size is a
  PBE-vs-experiment comparison, not an our-DFT number — so the "0.20 h/f.u. to the ARPES depth" cost
  is an ARPES-anchored estimate, not a fully self-consistent doped-SCF result.
- **L2 (rigid-band, not self-consistent)**: the re-costed doping slides a FIXED converged spectrum's
  chemical potential (gaussian-CDF, σ=0.10 eV); it does NOT relax the density at the doped filling.
  H_027 already showed the live tot_charge=2/4 doped SCF is delicate (charge/magnetic sloshing,
  MPI_ABORT) — so the rigid-band cost is the geometry-PRESERVED best case, and the real doped state
  is harder (a wall-FAVOURING caveat, kept).
- **L3 (∫tr g is a TB-fit, not a Bloch QGT)**: I=2.855–2.856 is the NN-kagome TB fit to OUR PBE bands
  + the analytic projector metric (H_024 L3 route), NN-only, omits further-neighbour hopping/orbital
  admixture; its closeness to the measured QGT 2.87 on BOTH bands is partly because the NN-kagome
  metric is a SHAPE invariant — so "same I on both manifolds" is partly a property of the model, not
  proof the real Bloch QGT is identical on both.
- **L4 (which orbital)**: the shallow narrow pair (band-45 −0.43 eV / band-44 −0.57 eV) is the
  d_xz/d_yz-derived near-E_F kagome flat band (Kang arXiv:2001.11738); the deep cluster (−1.45 to
  −2.0 eV) is the in-plane-d (d_xy/d_x²−y²) manifold. The TB-fit metric does not resolve orbital
  character; the orbital assignment is from the ARPES/DFT literature, not from a projwfc run (no
  projwfc was re-run — it is the cheap next step if orbital attribution must be OUR-DFT-grounded).
- **L5 (two different cells)**: the H_019 non-spin-pol cell (E_F=16.00 eV) resolves ONLY the deep
  −1.3 to −2.0 eV narrow cluster on its sparse 81-k path; the H_027/H_029 spin-pol Co3Sn3 cell
  (E_F=14.71 eV) resolves BOTH the shallow (−0.43/−0.57 eV) AND deep (−1.95/−2.0 eV) narrow bands.
  The shallow band's appearance is partly a denser-path/spin-polarization effect — both are real CoSn
  flat bands, but the cross-cell comparison carries the cell/functional difference.
- **L6 (DOS pileup makes the cost target-sensitive, not the band-choice)**: the 8× swing (0.20 →
  1.58 h/f.u.) between the ARPES onset and the PBE band center is the flat-band DOS pileup — most of
  the band's spectral weight sits in the −0.34..−0.51 eV slab, so the LAST 0.34 eV of the slide is
  cheap but the slide INTO the dense slab is expensive. The "wall partly dissolves" claim therefore
  depends on whether the lever needs E_F at the band ONSET (weak D_s^geom∝ν(1−ν) at the edge) or at
  the CENTER (strong D_s at ν≈0.5) — a genuine physics trade-off (H_027 L3), not removable by re-labeling.
- **L7 (+U deepens it — H_029)**: the correlation lens (DFT+U, H_029) sinks the flat band MONOTONICALLY
  DEEPER (−0.44 → −3.3..−4.3 eV at U=5) and induces magnetic order; this reconciliation is a PBE-level
  statement. If the true CoSn correlation pushes the band deeper than PBE, the ARPES-anchored MODEST
  cost is optimistic; if (as full paramagnetic DMFT might) it pulls the band toward the measured
  ~100 meV, the MODEST cost holds. The +U-vs-DMFT direction is unresolved (H_029 L1).
- **L8 (absorbed=true unaffected)**: nothing here flips the RTSC gate; that still requires accredited
  4-probe transport + Meissner expulsion + measured H_c2 / T_c. The trio stays 🟠 jointly-unrealized.

## Cross-Links

- **parent**: H_027 (the PBE doping wall this card reconciles) · H_029 (the +U lens that deepened it)
  · H_024 (the deep-band ∫tr g=2.856) · H_019 (the original deep-band extraction) ·
  `state/research-fabrication-method-levers-2026-06-25.md` (the method-lever research that raised the
  100 meV-vs-1.45 eV discrepancy this card settles).
- **registry**: `tool/rtsc_candidates.py` LAYER_A[CoSn] — records the reconciliation (both manifolds;
  the ∫tr g shape-attribution; the corrected target-sensitive doping cost: MODEST to the measured
  onset, EXTREME to the PBE center).
- **literature**: measured QGT g=2.87 Kang arXiv:2412.17809; measured ~100 meV flat d-band + few-%
  Fe/In doping arXiv:2102.08979 (PRMat 5, 044202); CoSn flat band / d_xz-d_yz near-E_F + in-plane-d
  deeper Kang arXiv:2001.11738 (Nat. Commun. 11, 4004); Peotta–Törmä arXiv:1506.02815.

## Verdict

**🟡 RE-ANALYSIS (closed-supported) — the H_027/H_029 doping wall is a TRADE-OFF (PARTLY DISSOLVES),
NOT a clean bookkeeping artifact and NOT a band-choice error.** Three findings from OUR saved bands
(no new SCF): (1) CoSn hosts BOTH a shallow narrow kagome flat-band pair (band-45 −0.43 eV, band-44
−0.57 eV, W≈0.17 eV) AND a deep narrow manifold (bands 38/39 ≈−2.0 eV; the H_019/H_024 −1.45 eV
band-42 is in the same deep family) — confirmed in the spin-pol Co3Sn3 cell; the H_019 cell resolved
only the deep cluster. (2) The ∫tr g geometry lever is a SHAPE property of the NN-kagome destructive-
interference geometry and is essentially IDENTICAL on both: I=2.856 on the DEEP band (H_024) and
I=2.855 on the SHALLOW band (H_027), both ≈ the measured QGT 2.87 — so the lever does NOT live
uniquely on one manifold, and H_027/H_029 ALREADY attributed it to the shallow near-E_F band, not the
deep one. (3) Therefore the "1.58 h/f.u. EXTREME" is NOT an artifact of analysing the wrong (deep)
band — H_027 used the shallow band-45. It IS strongly TARGET-sensitive: reaching the PBE flat-band
CENTER (−0.44 eV) costs **1.58 h/f.u. = EXTREME**, but reaching the **MEASURED ARPES depth
(~−0.10 eV, arXiv:2102.08979)** costs only **0.20 h/f.u. = PHYSICAL** (gating/few-%-substitution
reach) — an 8× swing driven by the flat-band DOS pileup (L6). Reconciliation: the measured ~100 meV
band and our shallow −0.44 eV band are the SAME d_xz/d_yz kagome flat band, with PBE over-deepening it
~0.2–0.3 eV (L1); E_F reaches its measured ONSET cheaply (MODEST) but reaching its CENTER — where
D_s^geom∝ν(1−ν) is maximal — is EXTREME. **So the wall PARTLY DISSOLVES on accessibility (the lead
path is re-opened for a weak-geometry, gating-reachable onset device) but STANDS for the strong-
geometry half-filled center** — a genuine geometry-vs-accessibility trade-off (H_027 L3), not a
re-labelable artifact. is_green=False; the TRIO stays **🟠 jointly-unrealized**; absorbed=false /
GATE_OPEN — no re-analysis flips that.

### (1) Both manifolds — verbatim `out/manifolds_h027cell.out` (spin-pol Co3Sn3 cell, deterministic numpy)

```
nbands=60 nk=161  E_F=14.7132 eV (H_027/H_029 SPIN-POL Co3Sn3 cell)

=== ALL narrow bands (W<0.30 eV) within +/-3 eV of E_F, by position ===
band   W(eV)   mid-EF   min-EF   max-EF
  38   0.193   -1.998   -2.094   -1.902
  39   0.189   -1.951   -2.045   -1.856
  44   0.177   -0.567   -0.655   -0.478
  45   0.167   -0.425   -0.508   -0.341

=== bands within +/-1.0 eV of E_F (any width) ===
band  42  W=0.487  mid=-0.832  range[-1.075,-0.588]
band  43  W=0.492  mid=-0.805  range[-1.051,-0.559]
band  44  W=0.177  mid=-0.567  range[-0.655,-0.478]
band  45  W=0.167  mid=-0.425  range[-0.508,-0.341]
band  46  W=1.441  mid=+0.255  range[-0.466,+0.975]
band  47  W=0.856  mid=+0.830  range[+0.402,+1.258]
```

And the H_019 non-spin-pol cell (resolves ONLY the deep cluster), verbatim `out/manifolds_h019cell.out`:

```
81 k-points parsed, 52 bands, E_F=16.0015 eV (H_019 non-spin-pol cell)

=== ALL narrow bands (W<0.30 eV) within +/-3 eV of E_F, by position ===
band   W(eV)   mid-EF   min-EF   max-EF
  38   0.254   -1.921   -2.048   -1.794
  39   0.210   -1.877   -1.981   -1.772
  40   0.183   -1.738   -1.829   -1.646
  41   0.220   -1.578   -1.688   -1.468
  42   0.158   -1.446   -1.525   -1.367   <- the H_024 deep band
  43   0.237   -1.299   -1.418   -1.180
```

So: the deep −1.3 to −2.0 eV narrow cluster is in BOTH cells; the shallow −0.43/−0.57 eV narrow pair
is resolved in the spin-pol cell (H_027's band-45 is the −0.43 eV one). The original "1.45 eV" was the
H_019/H_024 deep band-42; H_027/H_029 already moved to the shallow band-45.

### (2) ∫tr g attribution — verbatim from H_024 (deep) and H_027 (shallow) prior runs

```
H_024 (deep band-42, mid −1.449 eV):  I = (1/2pi) int tr g d2k = 2.8564
H_027 (shallow band-45, mid −0.444 eV): I = (1/2pi) int tr g d2k = 2.8548
measured QGT (arXiv:2412.17809):        g = 2.87
```
The metric integral is the same to 3 sig figs (2.855 vs 2.856) on BOTH manifolds — the NN-kagome
geometry lever is a SHAPE invariant, present on the shallow near-E_F band (the lever-relevant one) and
on the deep one alike. The lever is NOT confined to either band ⇒ no bookkeeping artifact in the
geometry attribution.

### (3) Re-costed doping (both targets) — verbatim `out/recost_doping.out` (rigid-band gaussian-CDF, σ=0.10 eV, OUR scf.out)

```
N(E_F=14.7132)=93.039  (should be ~93)

 target E_F dE-rel-EF  hole e-/cell  holes/f.u.  %valence  class
     14.270    -0.444         4.725       1.575      5.1%  EXTREME(>0.7)
     14.613    -0.100         0.605       0.202      0.7%  PHYSICAL(<0.3)
     14.513    -0.200         1.410       0.470      1.5%  STRETCH(0.3-0.7)
     14.146    -0.567         6.707       2.236      7.2%  EXTREME(>0.7)
     13.263    -1.450        13.680       4.560     14.7%  EXTREME(>0.7)
     12.713    -2.000        19.753       6.584     21.2%  EXTREME(>0.7)
```
- **Measured ARPES depth (~−0.10 eV): 0.20 h/f.u. → PHYSICAL** (light Fe/In or gating reach — matches
  the method-lever research's "few % Fe/In").
- **PBE flat-band CENTER (−0.44 eV): 1.58 h/f.u. → EXTREME** (the H_027 wall figure — confirmed).
- The 8× swing is the flat-band DOS pileup (L6): the band edge is cheap, the dense center is expensive.

### Falsifiers

- **F1_both_manifolds_enumerated**: **PASS** — verbatim narrow-band tables for BOTH cells; shallow
  (−0.43/−0.57 eV) AND deep (−1.3 to −2.0 eV) manifolds tabulated.
- **F2_trg_attribution_honest**: **PASS** — ∫tr g attributed to specific bands: I=2.856 deep band-42
  (H_024) AND I=2.855 shallow band-45 (H_027); stated as a shared NN-kagome shape invariant.
- **F3_doping_recost_both_targets**: **PASS** — both targets costed via the H_027 gaussian-CDF engine:
  ARPES −0.10 eV → 0.20 h/f.u. PHYSICAL; PBE center −0.44 eV → 1.58 h/f.u. EXTREME.
- **F4_verdict_unbiased**: **PASS** — TRADE-OFF verdict stated (wall PARTLY dissolves for the
  weak-geometry onset, STANDS for the strong-geometry center); is_green=False; not biased to revive
  the candidate (the EXTREME center-doping is kept, the live-SCF delicacy L2 and +U-deepening L7 kept).
- **F5_no_new_scf_claimed**: **PASS** — no new SCF; every number is verbatim from saved pw.x output or
  a labeled deterministic re-parse.
- **F6_preregister**: held — predictions/criteria/falsifiers frozen 2026-06-25 before the re-parse.

### Structural finding

The CoSn doping wall is best stated as a **geometry-vs-accessibility TRADE-OFF**, not a binary wall.
The kagome ∫tr g≈2.855 lever (≈ measured QGT 2.87) is real and present on the SHALLOW near-E_F flat
band that H_027/H_029 already used — so the "wrong-band" dissolution hypothesis is FALSE (the campaign
did not analyse the wrong band). But the EXTREME 1.58 h/f.u. figure is the cost to reach the PBE
band CENTER (maximal D_s^geom); reaching the MEASURED ~100 meV ARPES onset costs only ~0.2 h/f.u.
(PHYSICAL, gating/few-%-Fe-In reach). The honest reconciliation: **a gating/light-doping device can
put E_F on the flat band's ONSET cheaply, but lands at a band-edge filling where D_s^geom∝ν(1−ν) is
weak; landing at the strong half-filled center is EXTREME.** The lead path is re-opened for a
2D/onset-gated geometry device (the method-lever research's regime) while the strong-D_s center stays
expensive — a partial dissolution, reported without bias. The trio remains **🟠 jointly-unrealized**;
`absorbed=false` / GATE_OPEN.

### Records

`state/h030_cosn_flatband_reconciliation_2026_06_25/` — `decks/{enum_manifolds_h019cell.py,
enum_manifolds_h027cell.py, recost_doping.py}`, `out/{manifolds_h019cell.out, manifolds_h027cell.out,
recost_doping.out}`. No new compute (re-parse of saved H_019/H_027/H_029 pw.x output).
