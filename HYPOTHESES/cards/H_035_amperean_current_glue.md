---
id: H_035
slug: amperean-current-glue
title: Amperean transverse-gauge current-current glue — a NO-boson, current-current pairing route claimed to escape BOTH the boson-energy cap AND the order-traps law; the honest-null falsifier (the only un-suppressed branch reintroduces a finite-momentum / PDW competing order) is TRIGGERED, and the real-photon branch is killed by the (v_F/c)² ≈ 1.1e-5 relativistic suppression → confirms-wall closed-negative
domain: rtsc
status: closed-negative
exploration_method: closed-form harness — two-branch Amperean scaling (real-photon (v_F/c)² vs emergent-gauge PDW) + 5 falsifiers, honest-null decisive
verification_method: W1 (pre-register frozen) + W2 (falsifier-5, honest-null decisive) + W3 (deterministic, byte-equal x2) + W5 (honest-limits-6)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
compute: closed-form (state/h_035_amperean-current-glue_2026_06_25/run.py + tool/rtsc_harness.py); no DFT
escape_class: grounded (no boson)
---

# H_035 — Amperean transverse-gauge current-current glue (rtsc)

## Hypothesis

A **transverse Amperean current-current interaction** pairs electrons with **NO bosonic glue**
and **NO competing electronic order**: the current of one carrier produces a transverse gauge
("magnetic") field that attracts a co-moving carrier (the two-co-moving-wires force). The claim is
that, because it is mediated by a transverse gauge field rather than an exchanged boson and does not
ride on a particular electronic order, it **escapes BOTH** campaign laws that pin the
~134–164 K spin-fluctuation / phase-stiffness ceiling (PR#40): the **boson-energy cap** and the
**order-traps law** ("the FLUCTUATION glues, the ORDER traps").

## Why

Amperean pairing is a real, published mechanism (P.A. Lee; Lee–Nagaosa–Wen). It is genuinely
"no-boson" in the sense that the glue is a gauge field, and it is a distinct pairing channel from
density-density spin/charge fluctuations — so on its face it is a candidate to sidestep both laws.
The test: does **either** physical realization of it reach a 134–164 K-equivalent pairing scale
from a **uniform** condensate **without** reintroducing a competing order?

## The honest null (load-bearing — NOT engineered around)

Amperean pairing is parametrically **weak** and favors **finite-momentum (competing) pairing**. Two
mutually exclusive branches, and the claim needs one branch to satisfy BOTH promises at once:

- **(A) Real-photon transverse gauge** — the current-current attraction is purely relativistic,
  suppressed by **(v_F/c)² ≈ (10⁶/3×10⁸)² ≈ 1.1×10⁻⁵** (GROUNDED: arXiv:2210.10371, arXiv:1305.3938).
  The pairing scale is microscopic → T_c orders of magnitude below the ceiling. No competing order,
  but no scale either.
- **(B) Emergent-gauge U(1) spin liquid (Lee–Nagaosa)** — the gauge "light speed" ~ v_F removes the
  (v_F/c)² suppression so the coupling can reach the electronic scale, BUT the instability is to
  **finite-momentum (Amperean / pair-density-wave) pairing**: electrons on the *same* side of the
  Fermi surface pair, the Cooper pair carries net momentum, and the condensate is a **PDW — a
  competing density-wave order** (GROUNDED: arXiv:1401.0519 = PRX 4, 031017; arXiv:cond-mat/0607015).
  This is **exactly the order-traps law the claim says it escapes.**

So the route with no competing order is sub-ceiling, and the route that reaches the scale is a
competing order. The joint promise is **unsatisfiable**. Literature-reported Amperean-SC scales are
**1–20 K** (arXiv:2210.10371), >6× below the ceiling. The honest-null falsifier (F1) tests precisely
this and is TRIGGERED by the grounded physics.

## Falsifiers (5 — pre-registered; PASS = NOT triggered)

- **F1_honest_null_competing_order_reintroduced (DECISIVE)**: PASS = the un-suppressed (emergent-gauge)
  branch does NOT reintroduce a competing order. Triggered (FAIL) because that branch is finite-momentum
  PDW. Measurable: ARPES/STM for a pair-density-wave modulation; a net-momentum Cooper pair.
- **F2_real_photon_tc_below_ceiling**: PASS = the real-photon branch T_c ≥ 134 K. Triggered (FAIL):
  (v_F/c)² ≈ 1.1e-5 → T_c → 0. Measurable: transport T_c of any clean real-photon Amperean device.
- **F3_lit_scale_below_ceiling**: PASS = a reported Amperean-SC proposal exceeds 134 K. Triggered
  (FAIL): all reported scales are 1–20 K (arXiv:2210.10371). Measurable: literature census of
  Amperean-SC T_c claims.
- **F4_joint_promise_unsatisfiable**: PASS = some branch is BOTH >ceiling AND competing-order-free.
  Triggered (FAIL): no branch satisfies both. Measurable: a single material with uniform (q=0)
  Amperean condensate above 134 K.
- **F5_suppression_not_microscopic** (guard): PASS = (v_F/c)² < 1e-3 (so branch-A physics holds).
  PASS at 1.1e-5.

## Honest limits (6)

1. **Order-of-magnitude T_c prefactor is speculative.** The BCS-like `exp(-1/λ)` map from coupling
   to T_c is a transparent closed form, NOT a microscopic Eliashberg solve. The verdict does NOT hinge
   on it: branch (A) dies by 5 orders of (v_F/c)², branch (B) dies by the competing-order trap —
   both prefactor-independent.
2. **v_F = 1e6 m/s is a representative value.** A heavy-fermion v_F ~ 1e4 m/s makes (v_F/c)² even
   smaller (worse for the claim); a Dirac v_F ~ c/300 only reaches ~1e-5. No v_F rescues branch (A)
   to the ceiling.
3. **The emergent-gauge "no suppression" is best-case.** Real U(1)-spin-liquid couplings carry their
   own form factors and could be weaker; we GENEROUSLY gave branch (B) the full electronic scale and it
   STILL fails on the competing-order axis. This biases AGAINST the wall, not for it.
4. **PDW-as-competing-order is a physics judgement, not a derived inequality.** It is grounded in the
   Lee/Lee–Nagaosa literature (same-side-of-FS, net-momentum pair), but whether a PDW could in some
   exotic host coexist non-competitively is not excluded in full generality — it is excluded for the
   known Amperean instabilities.
5. **Cavity/Floquet engineering is out of scope here.** arXiv:2210.10371 specifically rules out
   *deep-subwavelength-cavity* induction of the current-current channel; other photonic routes are not
   exhaustively surveyed. This card addresses the intrinsic-mechanism scale, not every engineering knob.
6. **In-silico only.** No material is claimed to BE an Amperean RTSC; `absorbed=false`; the lab gate
   (4-probe transport + Meissner + measured H_c2/T_c) is out of domain. This is a computed closed-negative,
   not a no-go theorem.

## Cross-links

- Frozen wall: PR#40 (spin-fluctuation / phase-stiffness ceiling ~134–164 K; order-traps law).
- Order-traps law precedent: H_031 ("the FLUCTUATION glues, the ORDER traps"; dead Ta2NiSe5 EI trap).
- Boson-energy cap: H_001 two-lever box / `PHONON_CEILING_MEV`; H_002 Allen–Dynes.
- Sibling escape-class probes in the same brainstorm wave (no-boson routes).

## Verdict (VERBATIM run stdout — no LLM self-judge)

```
========================================================================
H_035  Amperean transverse-gauge current-current glue
========================================================================
branch(A) real-photon coupling      = 1.113e-05 eV
  (v_F/c)^2 suppression             = 1.113e-05
  -> T_c(real-photon)               = 0.000e+00 K
branch(B) emergent-gauge pairing    = 1.000 eV (no (v_F/c)^2)
  finite-momentum (PDW) pairing     = True
  reintroduces competing order      = True
  -> T_c(emergent, IF uniform)      = 4.269e+03 K  [not physical: PDW]
literature Amperean-SC scale max    = 20.0 K  (arXiv:2210.10371)
campaign ceiling                    = 134-164 K   (room-T target 293 K)
------------------------------------------------------------------------
  [FAIL] honest_null_competing_order_reintroduced
  [FAIL] real_photon_tc_below_ceiling
  [FAIL] lit_scale_below_ceiling
  [FAIL] joint_promise_unsatisfiable
  [PASS] suppression_not_microscopic
------------------------------------------------------------------------
HONEST-NULL (decisive) status       = FAIL
joint-promise falsifier status      = FAIL
falsifiers_pass                     = 1/5
is_green                            = False
absorbed                            = false
VERDICT: confirms-wall
========================================================================
```

**Result.** `confirms-wall`. The decisive honest-null falsifier is TRIGGERED: the only un-suppressed
Amperean branch (emergent U(1) gauge) pairs at finite momentum (PDW), reintroducing exactly the
competing order the claim said it escaped; the real-photon branch is killed by the (v_F/c)² ≈ 1.1×10⁻⁵
relativistic suppression (T_c → 0). A publishable closed-negative: Amperean current-current glue does
NOT escape the ceiling. `is_green=False`, `absorbed=false`, GATE_OPEN.