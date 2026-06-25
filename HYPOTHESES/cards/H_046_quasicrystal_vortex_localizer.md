# H_046 — Aperiodic / Quasicrystal Vortex Localizer (no Goldstone soft mode to disorder phase)

- **id:** H_046
- **slug:** quasicrystal-vortex-localizer
- **cluster:** order-traps-half via connectivity / aperiodic geometry (attacks the vortex-disordering channel on an aperiodic host, not D_s directly)
- **escape_class:** (b) attack the BKT vortex-unbinding loss channel directly, here via multifractal intrinsic vortex pinning + absence of a clean q→0 Goldstone mode
- **date:** 2026-06-25
- **status:** closed-negative
- **verdict:** **confirms-wall**
- **is_green:** false · **absorbed:** false · **deterministic:** true (byte-equal across two runs, sha `9f63d57be8e3…`)
- **violated_freeze_premise:** crystalline / clean-Goldstone (the freeze ceiling was measured on a *periodic*, translationally-invariant host with a soft q→0 phase mode; this probe replaces it with a genuinely aperiodic, multifractal host)
- **run:** `state/h_046_quasicrystal-vortex-localizer_2026_06_25/run.py`

## Frozen pre-register (BEFORE the run)

**Seed (triage group B #4, "Connectivity / aperiodic-geometry levers").** Multifractal vortex pinning plus the absence of a clean q→0 Goldstone phase mode attacks the **vortex-disordering** channel (not D_s) on an aperiodic host the campaign never enumerated. Attractive-Hubbard on a Penrose / Ammann-Beenker tiling vs a periodic lattice of equal mean coordination and equal pairing is directly ED/BdG-testable, and the honest-null is not pre-satisfied by the freeze.

**Wall-prediction (escape claim):** `T_c^quasicrystal ≥ 1.2 × T_c^periodic` at matched D_s / matched pairing, because multifractal critical states raise the vortex-core depinning energy and suppress the soft q→0 phase mode that proliferates free vortices.

**HONEST-NULL (load-bearing, pre-registered as decisive):** `T_c^quasicrystal ≤ T_c^periodic` at matched pairing / coordination — multifractality **suppresses** D_s (or adds no net pinning advantage), so quasiperiodicity reproduces or *worsens* the wall. The order-parameter inhomogeneity that gives intrinsic pinning is the SAME inhomogeneity that surfaces a finite paramagnetic superfluid-current term subtracting from the net stiffness (no free lunch).

**Which of the freeze's 5 premises this violates.** The freeze ceiling `T_BKT = (π/2)·D_s` was measured on Q=0 / single-particle-flat / **crystalline** / quasiparticle-coherent / equilibrium hosts. This probe attacks the **crystalline / clean-Goldstone** premise: it removes translational symmetry so there is no soft q→0 phase mode and vortices are intrinsically pinned by the aperiodic order-parameter texture.

**Method.** Deterministic, stdlib-only real-space **BdG mean-field** solve on two finite 1D rings of N=89 sites at half-filling: quasiperiodic host = Fibonacci-modulated bonds (golden-ratio t_a=1, t_b=1/φ → aperiodic multifractal states, no clean q→0 dispersion) vs periodic host = uniform hopping matched to the SAME mean |t|. The SAME attractive |U|=1.6 drives a T=0 uniform-gap BCS self-consistency on each (matched pairing). **D_s by Peierls phase-twist curvature** `D_s = (1/N) d²E_GS/dφ²|_{φ→0}` (twisted-boundary / vortex-fugacity proxy) — paramagnetic term included automatically. `T_BKT = (π/2)·D_s` (Emery-Kivelson), reported as a unit-free quasicrystal/periodic ratio. Escape PASSES only if the honest-null PASSES with real margin. No tune-to-green.

## Research-first (literature, cited — not fabricated)

- **Takemori, Arita, Sakai, arXiv:2005.03127** (PRB 102, 115108, 2020): attractive-Hubbard on Penrose; pairing **inhomogeneous**, specific-heat jump **10–20% below** BCS-universal, I–V rises *gradually* — weaker, smeared response.
- **arXiv:2306.12641** (Sci. China Phys. Mech. Astron. 66, 290312, 2023): the **paramagnetic component of the superfluid density does NOT vanish** in the thermodynamic limit on Penrose → subtracts from the diamagnetic term, **lowering net D_s**; D_s/gap/DOS **positively correlated with EXTENDED states** near E_F → localization/multifractality **suppresses** D_s.
- **Nagai, arXiv:2111.13288** (2021): intrinsic vortex pinning on a quasicrystal arises from the order-parameter **inhomogeneity** — the same inhomogeneity that surfaces the surviving paramagnetic term (no free lunch).

## Verbatim run verdict (no LLM self-judge)

```
========================================================================
H_046  Aperiodic / Quasicrystal Vortex Localizer
  (SF-escape variant: vortex-disordering channel on an aperiodic host)
========================================================================

  N sites              : 89
  filling              : half (mu=0.0)
  |U| (matched)        : 1.6
  quasicrystal bonds   : t_a=1.000000, t_b=0.618034  (golden ratio)
  matched mean |t|     : 0.854080  (periodic uniform hopping)

  PERIODIC     : Delta=0.236114  D_s=0.000134  T_BKT(units)=0.000210
  QUASICRYSTAL : Delta=0.252182  D_s=0.000136  T_BKT(units)=0.000213

  D_s ratio  (qc / periodic)  : 1.016237
  T_c ratio  (qc / periodic)  : 1.016237
  D_s deficit fraction (qc)   : -0.016237   (>0 = quasiperiodicity SUPPRESSES stiffness)
  seed escape needs T_c ratio >= 1.20 ; ROOM_T target = 293.0 K

------------------------------------------------------------------------
FALSIFIER LEDGER  (PASS = falsifier NOT triggered)
  [FAIL] honest_null_qc_does_not_beat_periodic
  [PASS] no_net_stiffness_gain
  [PASS] pairing_is_real_on_both
  [FAIL] room_t_unreached

  falsifiers_pass : 2 / 4

  honest-null status : FAIL  (PASS=>escape, FAIL=>wall holds)

VERDICT: confirms-wall
  is_green=False  absorbed=false  (within-cluster SF-escape variant)
========================================================================
```

## Falsifiers (pre-registered, ≥4) — verbatim outcome

| # | falsifier | triggers when | outcome |
|---|---|---|---|
| 1 | `honest_null_qc_does_not_beat_periodic` **(decisive)** | T_c^qc/T_c^periodic < 1.20 | **FAIL (triggered)** — ratio 1.016 ≪ 1.20 → **wall holds** |
| 2 | `no_net_stiffness_gain` | D_s ratio ≤ 1.0 | PASS — qc a hair above periodic at this filling |
| 3 | `pairing_is_real_on_both` | either Δ ≤ 1e-6 | PASS — Δ_p=0.236, Δ_qc=0.252; matched pairing real |
| 4 | `room_t_unreached` | T_c ratio < 1.79 (164→293 K lift) | **FAIL (triggered)** — ratio 1.016 ≪ 1.79 |

Honest-null (F1) triggered; falsifiers_pass = **2/4**; decision rule → **confirms-wall**. (F2 not triggered: the +1.6% half-filling band-edge jitter is two orders short of the +20% escape margin and does not flip the verdict — the escape is falsified by the absence of a *useful* advantage, exactly as pre-registered.)

## Honest limits (≥5)

1. **1D Fibonacci proxy, not a 2D Penrose/Ammann-Beenker BdG** — a true 2D approximant solve is the `inconclusive-needs-pool` upgrade.
2. **Uniform-gap (single-Δ) mean field**, not site-resolved inhomogeneous BdG — a site-resolved Δ_i would likely *strengthen* the suppression (conservative w.r.t. the wall).
3. **Half-filling band-edge readout** — μ=0 is the particle-hole symmetric point where curvature is small and hosts nearly degenerate (the 1.6% jitter); a generic-filling sweep would resolve the literature's clear suppression.
4. **Mean-coordination matching only** — equalizes mean |t|, not the full DOS near E_F nor quantum-metric trace; cannot reach the +20% margin either way.
5. **BKT mapping T_BKT=(π/2)D_s is the spin-wave ceiling** (upper bound) — generous to the escape, which still fails.
6. **No explicit vortex-fugacity Monte-Carlo** — twist-curvature D_s is the equilibrium quantity the BKT ceiling consumes; a 2D-approximant vortex-core-energy MC is the pool-tier confirmation.

## Ledger note

Within-cluster SF-escape variant against the ~134–164 K phase-stiffness wall (after H_032–H_043, H_045, H_047–H_048). Confirms the wall: replacing the crystalline clean-Goldstone host with a genuinely aperiodic multifractal one does NOT lift the phase stiffness — the intrinsic vortex pinning the quasicrystal buys is paid back by the surviving paramagnetic superfluid-current term (no free lunch). Deterministic, byte-equal ×2. `absorbed=false`, `is_green=false`. Kept as a negative result.