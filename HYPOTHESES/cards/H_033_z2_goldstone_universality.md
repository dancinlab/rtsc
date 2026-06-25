---
id: H_033
slug: z2-goldstone-universality
title: z=2 Goldstone universality-class change — does a quadratic phase-mode dispersion make k_B·T_BKT=(π/2)·D_s the WRONG formula and lift the ~134–164 K phase-stiffness ceiling? (escape class (b) wrong-formula)
domain: rtsc
status: closed-negative
exploration_method: closed-form harness — static vortex free-energy balance with a GENERAL Goldstone dynamical exponent z; honest-null = z drops out of the static balance
verification_method: W1 (pre-register frozen) + W2 (falsifier-5, honest-null decisive) + W3 (deterministic, byte-equal ×2) + W5 (honest-limits-7)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
compute: closed-form (tool/rtsc_harness.py); no DFT
---

# H_033 — z=2 Goldstone universality-class change (rtsc)

## Hypothesis

The campaign frozen wall (PR#40) caps the spin-fluctuation / phase-stiffness ambient T_c via the
Berezinskii / KT-Nelson relation **k_B·T_BKT = (π/2)·D_s** (Emery-Kivelson; T_BKT=(π/2)D_s). The
**escape class (b)** seed asserts this is the **WRONG formula**: a dynamical-exponent **z=2 Goldstone**
mode (a *quadratic* phase-mode dispersion ω_q ~ q², vs the z=1 *linear* ω_q ~ c·q) **changes the
universality class**, so the true phase-ordering temperature is a different, *higher* functional of the
stiffness — lifting the ~134–164 K ceiling.

## Why (the test)

If the universality class genuinely changed the *formula* (not just the prefactor), then re-deriving the
transition temperature from first principles for a general z should yield a z-dependent multiplier in
front of D_s. We encode the **central falsifiable scaling** — the static single-vortex free-energy
balance F = E − T·S with E = π·D_s·ln(L/a), S = 2·k_B·ln(L/a) — for a *general* Goldstone dispersion z,
and read off the prefactor in k_B·T = (prefactor)·(π/2)·D_s as a function of z. We then hand the seed its
**best case** (z=2 + a generous 1.5× O(1) prefactor uplift + the harness 3D lever 1.84×) and test whether
*any* z-driven uplift carries the flat-band geometric stiffness (D_s ≤ 0.44 meV) past the ceiling.

## The honest null (load-bearing — NOT engineered around)

A z=2 phase mode reproduces **essentially the same Berezinskii bound up to an O(1) prefactor**: the
stiffness still sets the scale. The 2D BKT transition is a **STATIC** (equilibrium) phenomenon — E and S
are **equal-time** quantities depending only on the spatial phase winding, which exists for *any*
dispersion. The dynamical exponent z multiplies the **frequency** axis (ω ~ q^z) — the *critical
dynamics* (relaxation τ ~ ξ^z, flux noise, critical slowing down) — an integration the static free-energy
balance never performs. **z drops out of the static balance**; the (π/2) is z-independent. Changing z
shifts logarithms and dynamic scaling, **not** the ~k_B·164 K magnitude. **The cap is the stiffness
MAGNITUDE D_s, not the exponent.** (Encoded as math: `z_static_prefactor(z) ≡ 1.0` for all z; the
measured prefactor spread over z∈[1,3] is exactly 0.)

## Grounding (cited, not fabricated)

- KT-Nelson static criterion k_B·T_BKT=(π/2)·J_s and the universal-jump 2/π: **Nelson & Kosterlitz,
  PRL 39, 1201 (1977)**; observed universal jump in a 2D Bose gas **arXiv:1305.1423** (Desbuquois et al.,
  Nat. Phys. 8, 645 (2012)).
- z=2 is the standard dynamical exponent for the 2D superfluid/SC BKT transition (relaxational dynamics /
  flux-noise): **arXiv:cond-mat/0003447** (Lidmar et al.); **arXiv:2210.01838** (BKT dynamics in a spin
  fluid). z governs *dynamics*; the static transition T is set by the equilibrium stiffness.
- Static/dynamic separation is textbook **Hohenberg-Halperin, RMP 49, 435 (1977)**: the static
  universality class (2D XY) and its critical T are independent of the dynamical class (which z labels).

## Falsifiers (≥4 — pre-registered; PASS = NOT triggered)

- **F1_null_z_changes_static_T** *(DECISIVE NULL)*: PASS iff changing z (1→2→3) does NOT move the static
  BKT T(D_s) — i.e. prefactor spread ≤ 1e-6 AND |T(z=2)−T(z=1)| ≤ 1e-6. Triggered (FAIL) would mean z
  genuinely moves the transition T → the seed escapes.
- **F2_seed_best_clears_ceiling**: PASS iff even the z=2 + 1.5×-uplift + 3D-lever best case FAILS to reach
  the 134 K ceiling lower edge. Triggered = the uplifted case crosses the ceiling → escape.
- **F3_magnitude_is_the_cap**: PASS iff the flat-band stiffness (0.44 meV) sits FAR below the cuprate
  stiffness (~9 meV) so its z=2 T_phase is far below the ceiling → the cap is the MAGNITUDE D_s.
- **F4_room_t_unreached**: PASS iff the best uplifted z=2 case stays below 293 K. Triggered would be a
  room-T claim from a dynamical-exponent relabel (extraordinary).
- **F5_honest_not_green**: PASS by construction — is_green=False, absorbed=false, no material claimed to
  BE an RTSC; T_phase is a closed-form coordinate, not a measurement.

## Honest Limits (≥5)

- **L1 (the binding one)**: the probe encodes the *static* universality argument as a flat-in-z prefactor;
  it does NOT carry out a full RG of a z=2 quantum-critical XY action. A z=2 mode at a *quantum* (T→0)
  transition has its own (d+z)-dimensional scaling — but the finite-T phase-ordering transition that
  caps T_c is the *thermal* 2D XY/BKT one, where z is irrelevant by Hohenberg-Halperin. This is the honest
  scope of the claim being tested.
- **L2**: the 1.5× "best-case O(1) uplift" is a deliberately generous stand-in for any prefactor a
  different dynamical class might shift; the real universal-jump physics restores 2/π and gives uplift→1.
  Even at 1.5× the case stays at ~22 K, so the conclusion is robust to this knob.
- **L3**: D_s ≤ 0.44 meV is the OPTIMISTIC top of the flat-band geometric band (PR#40); most hosts sit
  20–90× below cuprate stiffness, so the real margin below the ceiling is *larger* than the 111.9 K shown.
- **L4**: T_phase here is a COORDINATE, not a prediction (H_018 predictor scatter); the ceiling band
  134–164 K itself carries Emery-Kivelson model uncertainty.
- **L5**: the harness `geometric_bkt_tc_band` deflation (2.8×) and 3D lever (1.84×) are calibrated
  order-of-magnitude factors, not first-principles for this candidate.
- **L6**: a genuine z-change requires a *physical* mechanism (e.g. a Galilean-vs-relativistic phase
  action, a particle-hole-symmetric point); this probe does not construct or screen such a host — it only
  tests the *formula-change* claim.
- **L7**: absorbed=false; room-T needs accredited 4-probe transport + Meissner expulsion + measured
  H_c2/T_c — out of the in-silico domain.

## Cross-Links

- PR#40 frozen wall (the ~134–164 K phase-stiffness ceiling this seed attacks) · H_001 (two-lever box) ·
  H_006/H_024 (∫tr g geometry lever, D_s magnitude) · H_018 (Tc=coordinate scatter) · H_031 (the
  spin-fluctuation glue path that the same ceiling caps).

## Verdict

**CLOSED-NEGATIVE — confirms-wall.** The honest-null falsifier (F1) **PASSes with a real margin**: the
static vortex free-energy prefactor is *exactly* z-independent (spread = 0.000000e+00; T(z=2)−T(z=1) =
0 K), so k_B·T_BKT=(π/2)·D_s is the RIGHT formula — changing the Goldstone dynamical exponent does NOT
change the static transition temperature. Even the seed's best case (z=2 + 1.5× O(1) uplift + 3D 1.84×
lever) reaches only **22.14 K**, staying **111.86 K below** the 134 K ceiling lower edge. 5/5 falsifiers
PASS. This is a publishable closed-negative: the universality-class-change escape (class (b)) is a
*wrong-formula* claim that the static/dynamic separation refutes — the cap is the stiffness MAGNITUDE,
not the exponent. is_green=False; absorbed=false; GATE_OPEN; target 293 K @ 1 atm unreached.

### Verbatim run verdict (state/h_033_z2-goldstone-universality_2026_06_25/run.py — byte-equal ×2)

```
==============================================================================
H_033  z=2 Goldstone universality-class change  (escape class (b) wrong-formula)
==============================================================================
CLAIM: a quadratic (z=2) phase-mode dispersion changes the universality class
       so k_B*T_BKT=(pi/2)*D_s is the WRONG formula -> a HIGHER T_phase(D_s),
       lifting the ~134-164 K spin-fluctuation/phase-stiffness ceiling.
NULL : T_BKT is fixed by the STATIC vortex free-energy balance (no time, no z);
       z labels the CRITICAL DYNAMICS (tau~xi^z), not the static transition T.
       The cap is the stiffness MAGNITUDE D_s, not the exponent z.
------------------------------------------------------------------------------
[1] STATIC vortex-balance prefactor vs z (honest physics):
    z = 1.0   static prefactor = 1.000000   (pi/2 multiplier)
    z = 1.5   static prefactor = 1.000000   (pi/2 multiplier)
    z = 2.0   static prefactor = 1.000000   (pi/2 multiplier)
    z = 3.0   static prefactor = 1.000000   (pi/2 multiplier)
    -> prefactor spread over z in [1,3] = 0.000000e+00
    -> the (pi/2) is z-INDEPENDENT: changing z does NOT change T_BKT(D_s).
------------------------------------------------------------------------------
[2] T_phase at the OPTIMISTIC flat-band stiffness D_s = 0.44 meV:
    z=1 (linear)    T_phase =   8.0205 K
    z=2 (quadratic) T_phase =   8.0205 K   (delta = +0.0000e+00 K)
    cuprate-scale D_s =  8.997 meV -> 164.0 K  (the real ceiling: it is the MAGNITUDE)
------------------------------------------------------------------------------
[3] SEED BEST CASE: z=2 + a generous 1.5x O(1) prefactor uplift:
    T_phase (uplifted)             =  12.0307 K
    T_phase (uplifted + 3D 1.84x)  =  22.1351 K
    ceiling band                   = 134-164 K
------------------------------------------------------------------------------
[4] FALSIFIER LEDGER (PASS = NOT triggered):
    [PASS] F1_null_z_changes_static_T
    [PASS] F2_seed_best_clears_ceiling
    [PASS] F3_magnitude_is_the_cap
    [PASS] F4_room_t_unreached
    [PASS] F5_honest_not_green
------------------------------------------------------------------------------
VERDICT: confirms-wall   falsifiers_pass=5/5
         null_holds=True  seed_best_stacked_Tc=22.1351K  ceiling_lo=134K  margin_below_ceiling=111.8649K
         is_green=False  absorbed=false  target=293K  (GATE_OPEN)
==============================================================================
```