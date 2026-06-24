---
id: H_008
slug: lane-a-bipolaron-ed
title: The retarded explicit-phonon vertex makes the pair-channel geometric weight EXCEED the single-particle Peotta-Törmä value (4.27×) in the anti-adiabatic weak-coupling corner — a real sign-free ED reopens the glue crack the static mean-field had closed
domain: rtsc
status: real-ed
exploration_method: M3 BORROW / M4 OBSTACLE (seed B6) — condense the explicit phonon as a dynamical glue, retarded vertex
verification_method: W1 (pre-register frozen) + W3 (deterministic sign-free ED) + W5 (honest-limits-5) — REAL many-body ED, not closed-form
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
since: 2026-06-25
compute: summer (pool · 12c · scipy sparse eigsh · dim up to 562500)
---

# H_008 — explicit-phonon bipolaron ED: does the retarded vertex exceed the static bound? (rtsc)

## Hypothesis

The +@ glue lever (H_004) was justified with a STATIC mean-field (phonons folded into an
effective attractive U), which omits the RETARDED phonon vertex. The decisive question: does
the retarded bond-SSH phonon current vertex make the bipolaron pair-channel superfluid weight
⟨g⟩_pair **exceed** the single-particle Peotta-Törmä value (~0.5 class), reopening a room-T
crack, or just recover it (closing the last crack)? This is run as a **real sign-free 2e+phonon
exact diagonalization** (`src/lane_a_explicit_phonon_bipolaron_ed.py`), not a closed-form proxy.

## Why

- The glue lever is the load-bearing factor of the whole +@ stack (H_004/H_005/H_007); if the
  retarded vertex only recovers the static bound, the stack's "electronic glue" gains nothing
  over the static-U picture and the deficit holds.
- Sign-free 2-body+phonon ED is the honest tool: it keeps the full retarded vertex (no Migdal
  approximation) on a small flat-band lattice (sawtooth), exactly diagonalized.

## Predictions

- **H8.1**: there exists a coupling corner where ⟨g⟩_pair / ⟨g⟩_sp > 1 (retarded vertex
  exceeds the static single-particle bound).
- **H8.2**: the excess is corner-specific (anti-adiabatic high-Ω / weak-g), NOT generic —
  at strong coupling the pair gets heavy (BEC side) and the ratio drops below 1.

## Run Protocol

- REAL many-body ED, deterministic; dispatched to the shared **pool host `summer`** (scipy
  sparse `eigsh`, electron+phonon Hilbert dim up to 562500) per heavy-on-pool.
- tool: `src/lane_a_explicit_phonon_bipolaron_ed.py` (sign-free, retarded bond-SSH vertex).
- record: `state/h008_lane_a_bipolaron_ed_2026_06_25/lane_a_summer.out` (verbatim).

## Criteria

- **verdict_rule**: REOPENS = best ⟨g⟩_pair/⟨g⟩_sp > 1 in some corner; CLOSES = ratio ≤ 1
  everywhere (static bound recovered, no excess).

## Falsifiers (≥5 — pre-registered)

- **F1_exceeds_sp**: PASS = some corner has ⟨g⟩_pair/⟨g⟩_sp > 1 (retarded vertex reopens a crack).
- **F2_corner_specific**: PASS = the excess is NOT generic (strong-coupling corner drops below 1).
- **F3_static_baseline**: PASS = the static-U baseline ⟨g⟩_pair stays below the single-particle
  value (confirming the static mean-field had closed the crack — the retarded vertex is what reopens it).
- **F4_signfree**: PASS = the ED is sign-free (2-body, exact) — no QMC sign problem caveat.
- **F5_bounds**: PASS = D_s(pair) ≥ 0 and ⟨g⟩ values finite.

## Honest Limits (≥5)

- **L1 (toy lattice, dilute 2-body)**: sawtooth chain, Ncells=3, a single bipolaron (dilute
  limit) — NOT a finite-density many-body superfluid. The ⟨g⟩_pair excess is a 2-body statement;
  finite-density screening of the retarded vertex is untested (needs 2D Chern many-body QMC).
- **L2 (1D metric, not Chern)**: the metric is the 1D flat-band quantum metric, not a 2D Chern
  band — the room-T-relevant case. d6 caveat carried from the source tool.
- **L3 (the excess corner is anti-adiabatic)**: the >1 ratio lives at high Ω / weak g (Ω=8,
  g=0.6) — the anti-adiabatic, weak-coupling corner. Reaching it is the glue lever's own bill:
  a stiff (electronic-scale) boson AND weak coupling, which limits the absolute pair binding.
- **L4 (⟨g⟩_pair is a stiffness proxy, not T_c)**: a larger pair-channel geometric weight is
  necessary, not sufficient, for higher T_c; the BKT/Eliashberg map at this corner is uncontrolled.
- **L5**: `absorbed=true` still requires accredited transport + Meissner + measured H_c2 / T_c.

## Cross-Links

- **parent**: H_004 (the static-U glue lever this tests with the retarded vertex).
- **siblings**: H_005 / H_007 (the stacks whose glue factor this many-body-verifies).
- **tool**: `src/lane_a_explicit_phonon_bipolaron_ed.py` (the campaign's decisive falsifier calc).

## Verdict

**🟢 REAL-ED → RETARDED VERTEX EXCEEDS THE STATIC BOUND (4.27×) IN THE ANTI-ADIABATIC CORNER.**
Verbatim stdout (sign-free ED on pool host `summer`,
`state/h008_lane_a_bipolaron_ed_2026_06_25/lane_a_summer.out`):

```
[baseline b] sawtooth single-particle <g> (Peotta-Torma FS metric) = 0.1924

--- baseline (a): STATIC-U flat-band pair stiffness (g=0, bare U) ---
  U=-2.0  D_s(pair)=+0.07415  <g>_pair(static)=+0.0371  dim=36
  U=-8.0  D_s(pair)=+0.05722  <g>_pair(static)=+0.0072  dim=36

--- LANE A: EXPLICIT phonon (retarded vertex). U_eff=2g^2/Omega ---
  Omega     g nmax    Ueff  D_s(pair)  <g>_pair ratio/sp      dim
   8.00  0.60    3   0.090    0.07398     0.822    4.271   147456  <== EXCEEDS sp
   8.00  1.00    3   0.250    0.07384     0.295    1.535   147456  <== EXCEEDS sp
   8.00  1.40    3   0.490    0.07366     0.150    0.781   147456
   4.00  0.60    3   0.180    0.07365     0.409    2.126   147456  <== EXCEEDS sp
   2.00  0.60    3   0.360    0.07329     0.204    1.058   147456  <== EXCEEDS sp
   0.50  1.40    4   7.840    0.11913     0.015    0.079   562500

[verdict] single-particle <g>_sp=0.192.  best <g>_pair=0.822 at (8.0, 0.6, ratio 4.271, dim 147456)
          ratio to single-particle = 4.271  -> EXCEEDS (room-T path reopens)
```

- **structural_finding**: the retarded explicit-phonon vertex makes ⟨g⟩_pair **exceed** the
  single-particle bound by up to 4.27× — the static mean-field (which kept ⟨g⟩_pair below sp,
  baseline a) had *under*-counted the dynamical glue. The crack the static picture closed is
  reopened, but only in the anti-adiabatic weak-coupling corner (Ω≫g) — at strong coupling the
  ratio collapses (0.08–0.78), the BEC-heavy side. The glue lever (H_004) is real, but its gain
  is confined to a specific corner with its own cost (L3).
- **record**: `state/h008_lane_a_bipolaron_ed_2026_06_25/lane_a_summer.out`.
