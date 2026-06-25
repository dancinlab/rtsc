# H_060 — O2 Disorder → Flat Band: disorder-induced flat band as a free geometry lever

- **id**: H_060
- **slug**: o2-disorder-flat-band
- **escape_class**: (c) different rigidity — manufacture the geometry lever (tr g) from Anderson / structural disorder "for free from randomness", i.e. a DOS-spike flat band at E_F without crystallinity / destructive-interference design
- **cluster**: spin-fluctuation / phase-stiffness ambient ceiling (T_BKT=(pi/2)D_s) — within-cluster flat-band-ORIGIN variant (disorder-induced, not crystalline)
- **status**: closed-negative (confirms-wall)
- **date**: 2026-06-25
- **is_green**: false
- **absorbed**: false
- **run**: `state/h_060_o2-disorder-flat-band_2026_06_25/run.py` (stdlib-only, deterministic, byte-reproducible — md5 `b8f7cfb4f702571e44895379ff2bd1fa`)

## Which of the freeze's premises this violates

The frozen geometric-stiffness verdict (H_001 / H_006 / H_017 + freeze ~134–164 K) was measured on **crystalline** flat bands whose nonzero superfluid weight comes from quantum-geometric (Bloch-extended) destructive interference. This card deliberately violates the **crystallinity / flat-band-ORIGIN** premise: it tries to get the geometry lever from **on-site Anderson randomness** — a disorder-INDUCED DOS spike at E_F — with no crystalline design. Flagged in the SF grand synthesis as one of two orthogonal bypasses worth a card; its honest-null is NOT pre-satisfied by the freeze (the freeze never measured a disorder-induced flat band).

## Hypothesis (frozen pre-register)

On an attractive-Hubbard lattice with on-site disorder `eps_i ∈ [-W/2, W/2]`, sweeping `W` into the disorder-induced-flat-band regime (DOS spike at `E_F`) yields a Kubo geometric stiffness `D_s(W) = (e²/ħ²)[⟨-k_x⟩ − Π_xx(q→0,ω=0)]`, disorder-averaged, with `T_BKT = (π/2)D_s`.

**Escape claim**: a finite `W*` gives `D_s(W*)` with `T_BKT > 134 K` (toward 293 K) **AND** `xi_loc > vortex-core size` (pairs stay extended) — geometry-for-free from randomness.

## Why (mechanism + literature grounding)

The disorder-induced flat band is real as a DOS phenomenon, but the geometry-for-free claim collides with localization on two fronts (the load-bearing honest-null):

- **In d ≤ 2, any on-site disorder Anderson-localizes ALL single-particle states** (Abrahams, Anderson, Licciardello, Ramakrishnan scaling theory, *PRL* **42**, 673 (1979)). There is no extended-state window; 2D only makes `xi_loc` parametrically larger but still **finite**.
- A disorder-INDUCED DOS pile-up at `E_F` appears precisely when `W ~ bandwidth` — exactly where `xi_loc` collapses toward the lattice spacing.
- The Kubo geometric stiffness of a flat band built from **localized** states is bounded by the spatial extent of those states: a localized insulator has `D_s = 0` (Kohn, *Phys. Rev.* **133**, A171 (1964)). Crystalline flat bands evade this ONLY through Bloch-extended quantum geometry (Peotta–Törmä, *Nat. Commun.* **6**, 8944 (2015); Tovmasyan et al., *PRB* **94**, 245149 (2016)), which on-site RANDOMNESS does not provide. The most recent disorder treatment finds the disorder correction to the flat-band superfluid weight is "a competition between localization functionals, typically **vanishing**" (Kolář–Heikkilä–Törmä, arXiv:2510.05224 (2025); cf. arXiv:2506.07095).

**No free lunch (this card's instance)**: the same randomness that would flatten the band into a DOS spike is the randomness that localizes the carriers — so the manufactured flat weight carries zero phase coherence (`D_s → 0`).

## Probe (deterministic, stdlib-only)

`run.py` is a fixed-seed (splitmix64), stdlib-only Anderson tight-binding probe (no numpy, no Date, no system RNG):

1. **DOS spike + IPR at E_F** — a length-`N=600` Anderson chain, exact symmetric-tridiagonal diagonalization (Numerical-Recipes `tqli`, QL with implicit shifts, stdlib), measuring the DOS pile-up ratio at `E_F=0` and the IPR of the ~2% of states nearest `E_F`.
2. **Localization length** — `xi_loc` at `E_F` from the transfer-matrix Lyapunov exponent on a long `N=20000` chain (exact in 1D); plus a 2D weak-disorder `xi_2D ~ exp(π k_F ℓ/2)` estimate.
3. **Kubo geometric-stiffness proxy** — `D_s(W) = D_s0(W)·f_coh(xi_loc)`, with the bare flat stiffness tied ONLY to the EXCESS DOS disorder manufactures above the clean baseline (`excess = max(0, DOS_ratio−1)`; `D_s0 = 7.4 meV · min(1, excess)`, the most generous FS-capped estimate — the clean `W=0` dispersive band is NOT credited), and `f_coh = 1 − exp(−xi_loc/xi_core)` (Kohn/Resta coherence suppression, `xi_core=3a`).

`W` is swept `0 … 8t` (clean → 2× bandwidth, deep into the localized regime). The honest-null is load-bearing; nothing is tuned toward green.

## Falsifiers (pre-registered; PASS = NOT triggered)

1. **F_NULL_localized_spike_kills_stiffness** *(decisive honest-null)* — in the disorder-induced flat-band regime the states are localized (`xi_loc < a` OR `IPR → 1`) OR the stiffness there is `< 1/20` of 7.4 meV. **Triggered ⇒ wall confirmed.**
2. **F1_Ds_max_below_20x_cuprate** — the best `D_s` over the sweep stays ≥ 20× below 7.4 meV.
3. **F2_TBKT_max_below_wall** — the best disorder-induced `T_BKT` (any `W`) stays below ~134 K.
4. **F3_no_extended_pairs_in_flatband** — in the DOS-spike regime `xi_loc` never exceeds the vortex-core size. *(Positive-control arm: PASSes only because the only `W` with excess DOS is not yet a real flat band.)*
5. **F4_room_T_not_reached** — no disorder strength yields `T_BKT ≥ 293 K`.

**Escape would require** F_NULL **and** F2 to both NOT trigger. They both trigger.

## Verbatim run verdict (no LLM self-judge)

```
========================================================================
H_060  O2 disorder -> flat band (disorder-induced flat band geometry)
  within-cluster variant of the flat-band / phase-stiffness wall
========================================================================
W-sweep (t=1, chain N=600, Lyapunov N=20000, seed=0xC0FFEE):
  W/t  W/BW   DOS_spike   IPR_EF    xi_1D      xi_2D_est   D_s[meV]   T_BKT[K]
   0.0  0.00     1.0000   0.0025       inf         inf   0.00000      0.000
   1.0  0.25     1.0263   0.0131   103.394   8.223e+10   0.19474      3.550
   2.0  0.50     1.0263   0.0438    26.091   5.355e+02   0.19470      3.549
   3.0  0.75     1.0263   0.0935    11.283   1.632e+01   0.19021      3.467
   4.0  1.00     1.0000   0.1353     6.505   4.810e+00   0.00000      0.000
   5.0  1.25     0.9211   0.2059     4.098   2.733e+00   0.00000      0.000
   6.0  1.50     0.7895   0.2099     3.005   2.010e+00   0.00000      0.000
   7.0  1.75     0.6842   0.2606     2.289   1.670e+00   0.00000      0.000
   8.0  2.00     0.6842   0.3201     1.910   1.481e+00   0.00000      0.000
------------------------------------------------------------------------
flat-band (DOS-spike) regime:  W/t=1.0  spike_ratio=1.0263
   at spike:  IPR_EF=0.0131   xi_loc_1D=103.3943   D_s=0.19474 meV   T_BKT=3.550 K
best D_s over ALL W:  0.19474 meV  at W/t=1.0  ->  T_BKT_max=3.550 K
cuprate scale=7.40 meV ; shortfall factor=38.00x ; wall=134K ; target=293K
------------------------------------------------------------------------
FALSIFIERS (PASS = not triggered):
  [FAIL] F_NULL_localized_spike_kills_stiffness
  [FAIL] F1_Ds_max_below_20x_cuprate
  [FAIL] F2_TBKT_max_below_wall
  [PASS] F3_no_extended_pairs_in_flatband
  [FAIL] F4_room_T_not_reached
falsifiers_pass: 1 / 5
========================================================================
VERDICT: CONFIRMS-WALL
  honest-null F_NULL triggered = True (True=wall confirmed)
  absorbed=false  is_green=false
========================================================================
```

**Reading**: on-site Anderson disorder manufactures essentially NO excess flat-band weight (DOS spike ratio peaks at only 1.026 — it broadens the band, it does not pile a degenerate flat band at `E_F`), so the most-generous bare stiffness is `D_s ≈ 0.19 meV` (`T_BKT = 3.55 K`, **38× below** the cuprate scale). And the only `W` where even that tiny excess survives (`W/t ≈ 1`) is the weak-disorder regime where there is no real flat band; pushing `W` to where DOS would concentrate (`W/t ≳ 4`) instead drives `xi_loc → a` and IPR up (localization), so the coherence factor kills `D_s → 0`. The decisive honest-null **triggers**. No `W*` gives `T_BKT > 134 K` with extended pairs. The wall holds.

## Honest limits (≥5)

1. **1D core model.** Exact `xi_loc` and DOS/IPR are 1D. The localized→`D_s=0` conclusion is dimension-robust in `d ≤ 2` (scaling theory), the 2D `xi_2D` estimate is reported, but a full 2D self-consistent BdG was not run in-process (deferred to pool). The 1D model can only make localization STRONGER, not weaker.
2. **Box on-site disorder only.** Off-diagonal (random-hopping) disorder or randomly-decorated Lieb/kagome lattices could build a more genuine flat band; those are different mechanisms needing their own cards. On-site box disorder is the seed's stated probe and does NOT manufacture a geometric flat band.
3. **Kubo proxy, not a full bubble.** `D_s` uses a coherence-suppressed bare-stiffness proxy calibrated to the Kohn/Resta localization bound; deliberately generous to the escape. A real bubble would only suppress more.
4. **Excess-DOS definition is a modeling choice.** Crediting only `max(0, DOS_ratio−1)` is the honest reading of "geometry for FREE from randomness". Crediting absolute DOS would falsely hand the clean dispersive band's trivial Drude weight to the disorder route (caught and corrected in-build; the uncorrected version produced a spurious escape artifact).
5. **`xi_core = 3a` and the 7.4 meV / 134 K anchors are fixed inputs**, not derived here. Shifting them within a factor of a few does not change the verdict (38× shortfall, exponential localization).
6. **No quantum-metric flat band claimed.** This card does NOT test crystalline geometric flat bands (that is the freeze itself); it tests only the disorder-INDUCED route and finds it does not deliver the lever.

## Outcome

`confirms-wall`. The disorder-induced-flat-band route is a within-cluster variant of the flat-band / phase-stiffness ceiling: on-site randomness either fails to manufacture a real flat band (weak `W`) or localizes the carriers it would pile up (strong `W`) — manufactured geometry carries no superfluid coherence. Same no-free-lunch signature as the prior 12/12 SF-escape probes. `is_green=false`, `absorbed=false`. The lab gate is untouched (in-silico domain).