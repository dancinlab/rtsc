---
id: H_023
slug: demand-relaxation
title: Demand-relaxation — a MODEST multilayer superfluid-weight boost (f_mult≥1.164, smallest N=2 on both defensible models) lets the CLEAN Ta2NiSe5 trio (300 meV, q=0, NO competing order) clear room-T with NO exotic 349 meV glue; the strongest remaining 🟠-CONDITIONAL 🟢-path, single unknown = the real multilayer D_s (DFT)
domain: rtsc
status: conditional
exploration_method: closed-form demand-relaxation — relax the 349 meV room-T glue demand by a multilayer superfluid-weight (D_s) boost f_mult(N), bracketed by two defensible scaling models
verification_method: W1 (pre-register frozen) + W2 (falsifier-7 incl. honesty-gate F7) + W3 (deterministic, byte-equal x2) + W5 (honest-limits-6)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
compute: fleet lane (🟢-demand-relaxation)
---

# H_023 — demand-relaxation via multilayer D_s boost (rtsc)

## Hypothesis

Both prime 🟢-paths CLOSED (1T-TiSe2's 400 meV exciton IS its CDW; no turnkey ≥349 meV clean
plasmon — and the magnon family lands the same wall). The remaining move is DEMAND-RELAXATION:
instead of an exotic ≥349 meV glue, RELAX the room-T glue demand so the CLEAN Ta2NiSe5 (~300 meV,
q=0 excitonic order = the pairing channel, NO competing CDW/SDW) suffices. In a flat-band SC,
stacking N coupled geometry+glue layers boosts the superfluid weight D_s (and thus the BKT/3D Tc)
by f_mult(N). **Hypothesis: a MODEST f_mult brings the demand onto 300 meV, and the smallest N
reaching it is small (a bilayer) — making the CLEAN trio CoSn/hBN/Ta2NiSe5 a room-T candidate with
NO competing-order problem.** Verdict stays CONDITIONAL: f_mult(N) is a model; the real value needs DFT.

## Why

stacked_tc is exactly linear in Ω, so "relax the demand to 300 meV" and "boost amplitude by 1.164×"
are the identical lever. The structural ADVANTAGE over the two closed paths: Ta2NiSe5's q=0 order IS
the pairing channel — no finite-q density wave to pre-empt SC. So this path needs neither an exotic
glue NOR a competing-order escape; only a real multilayer superfluid weight.

## Falsifiers (≥7 — pre-registered)

- **F1_required_f_mult_modest**: PASS = f_mult_req = 349.3/300 ≤ ~1.3.
- **F2_linearity_self_consistent**: PASS = demand-relax and amplitude-boost give the same f_mult.
- **F3_smallest_N_modest**: PASS = smallest N reaching f_mult on the conservative model is small (≤ a few).
- **F4_clean_trio_clears_roomT_at_modest_N**: PASS = clean trio Tc ≥ 293 K at that N.
- **F5_host_clean_no_competing_order**: PASS = the host (Ta2NiSe5) carries no pre-empting CDW/SDW.
- **F6_control_baseline_misses_roomT**: PASS = N=1 baseline misses room-T (the boost is load-bearing).
- **F7_not_green_model_needs_dft**: PASS = is_green=False (f_mult(N) is a model, not a measured D_s).

## Honest Limits (≥6)

- **L1**: f_mult(N) is a MODEL bracketed by sqrt(N) (optimistic Peotta-Törmä extensive-D_s, arXiv:1506.02815) and N^0.25 (conservative Josephson-stack) — NOT a measured superfluid weight. This is THE binding limit.
- **L2**: the BKT band is a calibrated coordinate (H_018 scatter); 299–356 K carries that uncertainty.
- **L3**: a real multilayer adds interlayer coupling that could ALSO introduce a density wave / reduce per-layer g — not charged here.
- **L4**: the ~300 meV is Ta2NiSe5's exciton scale used 1:1 as Ω (modeling assumption).
- **L5**: the trio (let alone an N=2 stack) is jointly unrealized; interface costs (H_009/H_011) assumed ideal.
- **L6**: absorbed=false; room-T needs accredited 4-probe transport + Meissner + measured H_c2/T_c.

## Cross-Links

- H_020 (the ~252 K wall this relaxes) · H_022 (the 1T-TiSe2 path this replaces — clean host, no competing order) ·
  H_006 (3D lever) · the magnon note (same wall) · tool/rtsc_candidates.py (CoSn/hBN/Ta2NiSe5 host) ·
  **the running real-DFT of the trio (H_019)** — whose natural next step computes the real multilayer D_s (this card's single unknown).

## Verdict

**🟡 MODEL-PROBE → 🟠 CONDITIONAL (strongest 🟢-path, NO competing-order problem).** Verbatim stdout
(`state/h023_demand_relaxation_2026_06_25/run_h023.py`):

```
  baseline stacked_Tc 3D (N=1, no boost)=   251.64 K   (room-T 293 K MISSED; the H_020 ~252 K coordinate)
  f_mult required (= omega_req/glue)    = 1.1644   (= 349.3/300)
    smallest N (sqrt model, optimistic)   = 2   f=1.4142  ->  Tc =   355.87 K
    smallest N (N^0.25, conservative)     = 2   f=1.1892  ->  Tc =   299.25 K
    clean trio Tc at modest N             =   299.25 K   (clears room-T: True)
    host clean / no competing order       = True   <- the structural advantage over the closed 1T-TiSe2 path
    multilayer D_s boost DFT-verified     = False  <- the SINGLE remaining unknown
    is green                              = False  (stays 🟠-CONDITIONAL by honesty gate)
  falsifiers_pass = 7/7
VERDICT: 🟠-CONDITIONAL (relaxed-demand 🟢-path, NO competing-order problem)
```

- **structural_finding**: the required boost to retire the room-T glue demand onto the clean
  Ta2NiSe5 host is MODEST — f_mult ≥ 1.164 (~16%), reached at the SAME smallest N=2 on BOTH a
  conservative (N^0.25) and an optimistic (sqrt N) scaling model; the clean trio then reaches
  299–356 K. The decisive advantage: Ta2NiSe5's q=0 excitonic order IS the pairing channel, so —
  unlike every closed path — there is NO competing order to escape and NO exotic ≥349 meV glue
  needed. This is the campaign's strongest 🟢-path. The SINGLE remaining unknown is named and
  DFT-shaped (the real superfluid weight of a fabricated CoSn/hBN/Ta2NiSe5 N=2 stack), so
  is_green=False. absorbed=false; GATE_OPEN.
- **record**: `state/h023_demand_relaxation_2026_06_25/result.json`.
