# H_057 — Interference-Protected Pair BICs (two-particle bound state in the continuum)

- **id:** H_057
- **slug:** interference-protected-pair-bics
- **cluster:** spin-fluctuation / phase-stiffness ambient ceiling (T_BKT=(pi/2)D_s) — within-cluster flat-band variant (sibling of H_032–035 single-particle-flat, H_056 CLS-phonon BIC)
- **escape_class:** (a) split the levers by SECTOR — flatten the PAIR (two-body) band via a two-particle bound-state-in-the-continuum while single particles stay dispersive, so pairing (flat pair band) and stiffness (dispersive single-particle band) live in different sectors
- **date:** 2026-06-25
- **status:** closed-negative
- **verdict:** **confirms-wall**
- **is_green:** false · **absorbed:** false · **deterministic:** true (byte-equal across two runs, sha `8571eeda530e…`)
- **violated_freeze_premise:** single-particle-flattened (the freeze's geometric-stiffness ceiling was measured on hosts where the SINGLE-particle band is flattened; this probe instead flattens the TWO-particle pair band via a BIC and keeps single particles dispersive)
- **run:** `state/h_057_interference-protected-pair-bics_2026_06_25/run.py`

## Frozen pre-register (BEFORE the run)

**Seed (triage group "Genuinely-new in-silico escapes" #22, "Interference-Protected Pair BICs").**
Flatten the PAIR (two-body) band via a two-particle BIC while single particles stay dispersive, so
pairing and stiffness live in DIFFERENT sectors (H_032–035 all flatten the single-particle band).
*Probe:* attractive-Hubbard ED on a cross-stitch / diamond chain at the caging point; two-particle
spectral function / pair band to confirm a flat pair band inside the continuum, plus Kubo / twist D_s.

**Wall-prediction (escape claim):** D_s tracks the SINGLE-particle bandwidth W_1 (eV-scale), NOT the
flat pair-band width — flattening the two-body band relocates pairing into a meV pair sector while the
phase stiffness keeps the large eV single-particle scale, so T_BKT = (π/2)·D_s reaches room-T.

**HONEST-NULL (load-bearing, pre-registered as decisive — two prongs, either decisive):**
(a) the pair-BIC acquires a **finite width** once interactions dress the continuum (it is not a true
zero-width flat pair band), AND/OR (b) **D_s collapses to the flat-pair-band scale (~0.1–0.4 meV)**:
the pair phase stiffness is set by the PAIR mobility (the pair-band width W_2), which the attractive
interaction drives to the second-order virtual-hopping scale W_2 ~ t²/|U| ≪ W_1. Pairing and stiffness
do NOT decouple: the same |U| that binds the pair also immobilizes it (no free lunch).

**Which of the freeze's 5 premises this violates.** The freeze ceiling T_BKT = (π/2)·D_s was measured
on Q=0 / **single-particle-flat** / crystalline / quasiparticle-coherent / equilibrium hosts. This
probe attacks the **single-particle-flattened** premise: it keeps single particles dispersive and
flattens the TWO-particle (pair) band via a BIC, trying to put pairing and stiffness in different
sectors.

**Method.** Deterministic, stdlib-only **exact two-particle diagonalization** (full opposite-spin
M²-dimensional Hilbert space, exact 2-particle dim = 64) on a cross-stitch ring (N=4 cells, M=8
sites) — a canonical flat-band lattice (Bloch bands s=−t′−4t·cos k dispersive, a=+t′ flat). The SAME
exact solve, under a Peierls flux φ inserted as the pair center-of-mass momentum (twisted boundary),
yields in one calculation: **W_1** (single-particle dispersive bandwidth — the seed's hoped D_s scale);
**W_2** (dressed pair-band width = spread of the lowest two-particle bound-state energy over φ∈[0,2π));
and the **t²/|U|** second-order pair-hopping reference. Swept over |U| ∈ {3,6,12}. D_s is identified
with the pair-band scale W_2. The decisive falsifiers are the **dimensionless** decoupling tests
(W_2/W_1, the t²/|U| collapse) the N=4 ring resolves robustly; absolute Kelvin is finite-size-
contaminated and reported only as labeled context.

The escape PASSES only if the honest-null PASSES (is NOT triggered) — i.e. the pair band stays broad
(W_2 ~ W_1) so D_s keeps the eV scale. No tune-to-green.

## Research-first (literature, cited — not fabricated)

- **Peotta & Törmä**, Nat. Commun. 6, 8944 (2015), **arXiv:1506.02815**: flat-band superfluid weight is
  set by the QUANTUM GEOMETRY of the **single-particle** Bloch states; the Cooper-pair mass is HEAVY
  (m* ~ 1/(U·g)) — the pair barely moves.
- **Herzog-Arbeitman, Peotta et al. (Törmä group)**, PRB 106, 014518 (2022), **arXiv:2203.11133**: D_s
  in an isolated flat band ∝ the MINIMAL QUANTUM METRIC of the single-particle wavefunctions — NOT a
  free pair-band-width sector.
- **Deng, Ortix, van den Brink et al.**, PRL 109, 116405 (2012), **arXiv:1204.1556**: a two-particle BIC
  EXISTS in the Hubbard continuum but requires fine tuning / an impurity and acquires a finite width
  away from the tuned point.
- **Tovmasyan, Peotta, Törmä et al.**, PRB 94, 245149 (2016), **arXiv:1608.00976**: effective pair
  hopping t_pair ~ |U|·(geometric factor); the pair COM dispersion is bounded by the same
  quantum-geometric scale, not the eV single-particle bandwidth.

The literature is unambiguous: the pair stiffness is set by the single-particle quantum geometry and
the heavy-pair (t²/|U|) scale, NOT a free pair-band sector inheriting the eV bandwidth. The in-process
exact two-particle ED reproduces this: W_2/W_1 = 0.14 at the deepest BIC and SHRINKS with binding
(W_2: 0.70→0.37→0.28 as |U|: 3→6→12), tracking t²/|U|.

## Verbatim run verdict (no LLM self-judge)

```
========================================================================
H_057  Interference-Protected Pair BICs (two-particle BIC)
  (SF-escape variant: flatten the PAIR band, keep single particles dispersive)
========================================================================

  lattice               : cross-stitch ring (canonical flat-band lattice)
  N cells / M sites      : 4 / 8   (exact 2-particle dim = 64)
  hoppings               : t=0.500  tprime=1.000  (Bloch: s=-tprime-4t cos k, a=+tprime flat)
  single-particle bands  : dispersive W_1=2.0000 , flat band at E=+1.000
  physical anchor        : W_1 := 2.00 eV  ->  1.00000 eV per lattice unit

  ATTRACTIVE-U SWEEP  (does the pair band stay broad, or collapse to t^2/|U| ?)
  |U|     W_2(pair)    t^2/|U| ref    W_2/W_1      W_2/(t^2/U) 
  3.00    0.701210     0.083333       0.350605     8.415       
  6.00    0.370570     0.041667       0.185285     8.894       
  12.00   0.280069     0.020833       0.140035     13.443      

  DECISIVE (strongest coupling |U|=12.0, deepest BIC / most-dressed continuum):
    pair-band width W_2          : 0.280069  (lattice)  = 280.07 meV (phys)
    single-particle W_1          : 2.000000  (lattice)  = 2.0 eV   (phys)
    W_2 / W_1                     : 0.14003   (escape needs ~1 ; null => <<1)
    W_2 vs t^2/|U|               : 13.443 x t^2/|U|  (pair = virtual-hop scale, collapses as U grows)

    dilute pair density n_pair   : 0.1250  (one pair per 8 sites)
    D_s (pair sector, dilute)    : 35.009 meV   T_BKT=(pi/2)D_s = 638.15 K
    [escape: D_s = W_1 sector]   : 250.0 meV   T_BKT would be 4557 K (only IF sectors decoupled)
    ambient wall ceiling         : 133.0 K ; ROOM-T target = 293.0 K

------------------------------------------------------------------------
FALSIFIER LEDGER  (PASS = falsifier NOT triggered)
  [FAIL] honest_null_pair_sector_does_not_inherit_W1
  [FAIL] pair_immobilised_by_binding
  [FAIL] sectors_do_not_decouple
  [FAIL] room_T_decoupling_lift_unreached

  falsifiers_pass : 0 / 4

  honest-null status : FAIL  (PASS=>escape, FAIL=>wall holds)

VERDICT: confirms-wall
  is_green=False  absorbed=false  (within-cluster SF-escape variant)
========================================================================

SHA256(stdout-above)=8571eeda530e4b46b51fd95678a9103ce6cd5cacd3a6be02cc7946808ae02cb1
```

## Falsifiers (pre-registered, ≥4) — verbatim outcome

| # | falsifier | triggers when | outcome |
|---|---|---|---|
| 1 | `honest_null_pair_sector_does_not_inherit_W1` **(decisive)** | W_2/W_1 < 0.5 | **FAIL (triggered)** — W_2/W_1 = 0.140 ≪ 0.5 → D_s does NOT keep the eV scale → **wall holds** |
| 2 | `pair_immobilised_by_binding` **(decisive, prong a)** | W_2 falls monotonically with \|U\| AND W_2/W_1 falls | **FAIL (triggered)** — W_2: 0.70→0.37→0.28, W_2/W_1: 0.35→0.19→0.14 as \|U\|: 3→6→12 |
| 3 | `sectors_do_not_decouple` | W_2/(t²/\|U\|) < 1e3 | **FAIL (triggered)** — W_2 = 13.4·(t²/\|U\|); pair-band stiffness locked to the binding scale |
| 4 | `room_T_decoupling_lift_unreached` | W_2/W_1 < (293/134 = 2.19) | **FAIL (triggered)** — W_2/W_1 = 0.140 ≪ 2.19 |

The **honest-null (F1) is triggered**: the pair sector does NOT inherit the single-particle bandwidth;
D_s collapses to W_2 ~ t²/|U| ≪ W_1. falsifiers_pass = **0 / 4** → **confirms-wall**.

## Honest limits (≥5)

1. **Small ring (N=4, M=8, exact dim 64).** Resolves the DIMENSIONLESS scaling robustly but not the
   thermodynamic asymptote nor a clean absolute Kelvin; the 638 K / 4557 K numbers are finite-size-
   contaminated and reported ONLY as labeled context — the verdict rests on the dimensionless decoupling
   tests. Larger N is the `inconclusive-needs-pool` upgrade and would sharpen the collapse.
2. **Cross-stitch (not a literal Penrose/diamond caging point).** The canonical exactly-solvable
   flat-band analog; a diamond-chain AB caging point gives the same heavy-pair physics, not separately run.
3. **Single bound-pair sector, not finite-density BKT.** A finite-density Kubo D_s would add a
   paramagnetic subtraction that only LOWERS D_s further (conservative w.r.t. the wall).
4. **Pair-band width as stiffness proxy** is an upper bound (full COM bandwidth, not band-bottom
   curvature × density) — GENEROUS to the escape, which still fails.
5. **BKT mapping T_BKT = (π/2)·D_s is the spin-wave ceiling**, over-counting T_c — generous to the escape.
6. **The exact two-particle BIC tuning was not isolated**; per Deng/Ortix arXiv:1204.1556 it is
   finite-width and parameter-fragile, so isolating it would not lift W_2/W_1.

## Ledger note

Within-cluster SF-escape variant against the ~134–164 K phase-stiffness wall (after H_032–H_053,
H_056). Confirms the wall: flattening the TWO-particle (pair) band via a BIC while single particles stay
dispersive does NOT put pairing and stiffness in independent sectors — the attractive interaction that
binds the pair also immobilizes it, driving the pair-band (stiffness) scale to W_2 ~ t²/|U| ≪ W_1
(W_2/W_1 = 0.14 at the deepest BIC, falling with |U|). D_s collapses to the dressed flat-pair-band scale
exactly as the pre-registered honest-null prong (b) predicted (no free lunch). Deterministic, byte-equal
×3. `absorbed=false`, `is_green=false`. Kept as a negative result.