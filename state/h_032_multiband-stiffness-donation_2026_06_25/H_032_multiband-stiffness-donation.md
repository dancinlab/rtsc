# H_032 — Multi-channel stiffness donation (escape class (a): borrow stiffness)

- **id:** H_032
- **slug:** multiband-stiffness-donation
- **status:** CLOSED-negative (🔴) — `confirms-wall`
- **escape_class:** (a) borrow stiffness
- **created:** 2026-06-25
- **absorbed:** false
- **is_green:** false
- **run:** `state/h_032_multiband-stiffness-donation_2026_06_25/run.py` (stdlib-only, deterministic, byte-equal across 2 runs; sha256 `733ac01b…`)

## Hypothesis (frozen pre-register)

Pairing lives on the flat band (high quantum-geometry / DOS), but the superfluid
phase stiffness `D_s` is **donated** by a co-resident high-Fermi-velocity dispersive
band. Pairing and stiffness are thus *different k-space objects*. If the two band
contributions add freely, `D_s_total = D_s_flat + D_s_disp` could clear the
spin-fluctuation / phase-stiffness ambient ceiling (~134–164 K; Emery–Kivelson,
`T_BKT = (π/2)·D_s`) and approach the 293 K @ 1 atm target.

## Why this could escape (the optimistic side, grounded)

Multiband superfluid weight **is additive** in the diamagnetic / f-sum sense: a
small-gapped valence band contributes constructively to the conduction-band
stiffness, and "giant amplification" of `T_BKT` from cooperative two-band interplay
is reported in the literature (arXiv:2311.17511; arXiv:2511.16385). So a bare
dispersive donor with a cuprate-class-or-larger `D_s` *looks like* free stiffness the
weak flat-band pairing channel can borrow.

## The honest null (load-bearing, decisive falsifier — NOT engineered around)

**Leggett-mode softening + v_F decoupling.** The donated dispersive stiffness reaches
the single order-parameter phase only through the **interband Josephson coupling J**.
The relative-phase (Leggett) mode costs finite energy ∝ J (arXiv:1408.5938;
arXiv:1704.00333); when J is small the dispersive phase free-floats and donates
nothing. Worse, the **quantum-metric no-go** (arXiv:2604.04719, Zhou 2026) is a
*trade-off*: maximizing flat-band pairing (needs the flat band quasi-**isolated** /
weakly hybridized) and maximizing the locking J (needs **strong** hybridization) are
mathematically incompatible (geometric sum rule). Strong J that fully donates the
dispersive stiffness back-acts to **destroy** the flat-band pairing the claim depends
on. This conserves the cuprate `Tc = min(T_pair, T_phase)` tradeoff that *defines* the
ceiling.

## Central falsifiable scaling (closed form, the load-bearing math)

Single dimensionless interband-coupling knob `x ∈ [0,1]`:

- Leggett donation efficiency: `η_donate(x) = x` (η→1 only at full locking x→1).
- No-go pairing survival:      `s_pair(x) = 1 − x` (flat band bleeds out under hybridization).

Effective stiffness reaching the common phase, and the two-channel ceiling law:

```
D_s_eff(x) = D_s_flat·(1−x) + D_s_disp · x · (1−x)
T_phase(x) = (π/2)·D_s_eff(x)
T_pair(x)  = CEILING_HI · (1−x)
Tc(x)      = min(T_phase(x), T_pair(x))
```

The donor term `x·(1−x)` is a *product* of "lock it" and "don't kill pairing" — its
maximum over `x` is **1/4** at `x=1/2`. You can never donate more than a quarter of
the bare dispersive stiffness: the same hybridization that locks the phase kills the
pairing that anchors it. (Generous inputs: `D_s_flat=8 K` = top of the campaign
1–8 K band; `D_s_disp=300 K` = 3× cuprate-class.)

## Result

Best working point `x*=0.3214` → **Tc = 111.29 K**, sitting exactly at the crossover
`T_phase ≈ T_pair ≈ 111.3 K`. That is **52.7 K below** the 164 K ceiling high edge and
**181.7 K below** the 293 K target. The naive free-additive fantasy was 483.8 K — the
Leggett/no-go gate destroys ~77% of it. The optimum at the crossover confirms
`min(pairing, stiffness)` is conserved. **`confirms-wall`** — a publishable
closed-negative. No material is claimed to be an RTSC; `absorbed=false`.

## Falsifiers (≥4 measurable; PASS = not triggered in this harness)

1. **`honest_null_leggett_nogo_escape`** (DECISIVE) — best two-channel
   `Tc=min(T_phase,T_pair)` exceeds the ~164 K ceiling. *Measure:* extract `D_s_flat`,
   `D_s_disp`, and interband J (Leggett-mode Raman/optical frequency, arXiv:1704.00333)
   in a real flat+dispersive heterostructure; reconstruct `Tc(x)` and check it clears
   164 K. **Result: does NOT escape (margin −52.7 K).**
2. **`reaches_room_T_target`** — best Tc ≥ 293 K. **Result: no (111.3 K).**
3. **`free_additive_donation_realized`** — best Tc ≥ 50% of the naive additive ceiling
   (gate weak / donation free). *Measure:* compare measured `D_s_total` against
   `D_s_flat+D_s_disp` from independent diamagnetic sum-rule weights. **Result: no —
   realized Tc is 23% of the additive fantasy; the gate dominates.**
4. **`pairing_stiffness_tradeoff_broken`** — at the optimum one channel beats the other
   by >3× (a free lunch). *Measure:* compare `T_phase` (μSR/penetration-depth stiffness)
   vs `T_pair` (gap/2Δ pairing scale) at the optimal doping. **Result: no — ratio ≈ 1,
   the tradeoff is conserved (crossover optimum).**

## Honest limits (≥5)

1. **Toy linear gates.** `η_donate=x` and `s_pair=1−x` are the *simplest monotone*
   encodings of Leggett locking and the no-go trade-off; real `η(J)` and `s(x)` are
   material-specific and non-linear. The 1/4 cap is exact only for this product form.
2. **No microscopic J.** Interband Josephson J is parameterized by `x`, not computed
   from a real bandstructure / cRPA. A material with anomalously strong J at small
   spectral-weight loss would shift the optimum (still bounded, but the bound moves).
3. **Generous donor.** `D_s_disp=300 K` is already 3× cuprate-class; a real dispersive
   metal co-resident with a flat band may carry *less* coherent stiffness, lowering Tc
   further (this only strengthens `confirms-wall`).
4. **2D-BKT framing.** `T_BKT=(π/2)D_s` is the strict 2D law; a 3D donor relaxes the
   vortex-unbinding penalty (campaign 3D lever ≈1.84×), not modeled here. Even a flat
   1.84× on 111 K (≈205 K) still misses 293 K and assumes free 3D stacking.
5. **No competing order.** Strong interband hybridization can trigger CDW/AFM that
   pre-empts SC entirely — would make the verdict *more* negative, not less.
6. **Single knob.** Only `x` is scanned; a real heterostructure has independent
   flat-band filling, donor `v_F`, and gap as separate levers. The 1D scan is the
   honest minimal model, not a full optimization.
7. **No self-judge.** Verdict is the verbatim program output; no LLM adjudication.

## Cross-links

- Frozen wall: PR#40 (spin-fluctuation / phase-stiffness ceiling ~134–164 K; QGT
  conflation correction).
- Sibling cards: `H_001` (two-lever box), `H_006` (FS dimension scan), `H_007`
  (three-lever combination), `H_031` (clean spin-fluctuation candidate).
- Harness: `tool/rtsc_harness.py` (`Falsifier`, `evaluate`, `ROOM_T_K`,
  `geometric_bkt_tc_band`).
- Literature anchors (grounded, not fabricated): Emery–Kivelson PRB 1995;
  arXiv:2604.04719 (two-channel Allen–Dynes + quantum-metric no-go, Zhou 2026);
  arXiv:2311.17511 & arXiv:2511.16385 (additive / cooperative two-band stiffness);
  arXiv:1408.5938 & arXiv:1704.00333 (Leggett mode / interband Josephson coupling);
  arXiv:2203.11133 (minimal quantum metric, flat-band superfluid weight).

## Verbatim run verdict (no LLM self-judge)

```
========================================================================
H_032  multi-channel stiffness donation  (escape class (a): borrow stiffness)
========================================================================
  D_s_flat (pairing channel, K) ............     8.0000
  D_s_disp raw (donor channel, K) ..........   300.0000
  naive additive fantasy Tc (K) ............   483.8053  (no Leggett gate)
  donation cap fraction max[x(1-x)] ........     0.2500
------------------------------------------------------------------------
  best working point x* ....................     0.3214
  T_phase (BKT, donated) at x* (K) .........   111.3057
  T_pair  (no-go cap)   at x* (K) ..........   111.2904
  Tc = min(T_phase,T_pair) at x* (K) .......   111.2904
------------------------------------------------------------------------
  ceiling band (K) ......................... 134.0 - 164.0
  room-T target (K) ........................   293.0000
  margin vs ceiling high edge (K) ..........   -52.7096
------------------------------------------------------------------------
  [PASS] honest_null_leggett_nogo_escape
  [PASS] reaches_room_T_target
  [PASS] free_additive_donation_realized
  [PASS] pairing_stiffness_tradeoff_broken
------------------------------------------------------------------------
falsifiers_pass=4/4
VERDICT: confirms-wall
========================================================================
```
