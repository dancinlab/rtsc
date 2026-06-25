# H_043 — Vortex-Code Phase Lock (the superfluid phase as a protected logical variable)

- **id:** H_043 · **slug:** vortex-code-phase-lock · **date:** 2026-06-25
- **cluster:** code-raised vortex core energy at fixed D_s (violates equilibrium order-trap / free-vortex premise)
- **escape_class:** (b) attack the BKT vortex-unbinding loss channel directly (not the stiffness)
- **status:** closed-negative · **verdict:** confirms-wall
- **is_green:** false · **absorbed:** false · **deterministic:** true (byte-equal across two runs, sha 0cbe0b51…)
- **run:** state/h_043_vortex-code-phase-lock_2026_06_25/run.py · **card:** state/HYPOTHESES/cards/H_043_vortex-code-phase-lock.md

## Frozen pre-register
Seed (triage group D #6): a static stabilizer string-tension raising vortex CORE ENERGY E_c attacks the BKT vortex-unbinding loss channel at FIXED bare stiffness D_s; no continuous Landauer bill. Wall-prediction (escape): T_BKT(S)=T_BKT(0)(1+alpha·S), alpha>0 monotone & unbounded. HONEST-NULL (decisive): T_BKT is independent of S beyond a prefactor — the bare stiffness still caps it; even E_c→∞ caps T_BKT at the spin-wave ceiling (pi/2)·D_s. Premise violated: equilibrium order-trap / free-vortex (D_s held fixed; only the thermal vortex proliferation is suppressed). Method: standard Kosterlitz-Thouless RG for the 2D vortex Coulomb gas — K=J/(k_B t), y=exp(-E_c/t), dK/dl=-4pi^3 y^2 K^2, dy/dl=(2-pi K)y; universal jump K_R(T_BKT^-)=2/pi; convert T_BKT^max[K]=(pi/2)·D_s[meV]/k_B with frozen D_s=0.06–0.44 meV.

## Verbatim verdict
falsifiers_pass = 3/5; VERDICT: confirms-wall. inf-core-energy limit saturates EXACTLY at (pi/2)J (overshoot −4.4e−7); best-case T_BKT^max=8.02 K (hi D_s + infinite code) is −125.98 K short of the 134 K wall; bare D_s needed = 7.351 meV (~16.7× above frozen hi D_s).

## Falsifiers (honest-null decisive)
1. F1 honest_null_best_case_clears_wall (HONEST-NULL, decisive) — TRIGGERED (FAIL): even E_c=∞ + best frozen D_s=0.44 meV gives T_BKT^max=(pi/2)D_s=8.02 K < 134 K (margin −125.98 K). The spin-wave ceiling, not vortices, caps T_BKT.
2. F2 no_overshoot_past_spin_wave_ceiling — PASS: T_BKT(E_c=∞) does not exceed (pi/2)J (no fabricated stiffness).
3. F3 tbkt_bounded_by_bare_stiffness — PASS: every finite-S T_BKT ≤ (pi/2)J; the seed's unbounded alpha·S growth is false — the lever saturates.
4. F4 frozen_ds_within_wall_reach — TRIGGERED (FAIL): D_s needed for ceiling@134 K = 7.351 meV, ~16.7× above frozen hi D_s — a real code-irreducible deficit.
5. F5 rg_reproduces_universal_jump_saturation (positive control) — PASS: E_c→∞ limit saturates exactly at (pi/2)J → RG valid, null meaningful.

## Honest limits
1. The mechanism is REAL, not a no-op — T_BKT does rise monotonically with the code (0.31J→1.57J); it fails only because the rise is BOUNDED by the bare stiffness (confirm-wall by saturation).
2. Classical KT-RG / single-vortex Coulomb-gas approximation: a true statistics-changing (non-Abelian) stabilizer that altered the dy/dl scaling dimension itself — not just the bare fugacity y0 — is outside this flow and is a separate un-run hypothesis. The seed framed a core-ENERGY term, which only renormalizes y0, so the bound holds for the carded mechanism.
3. Strictly-2D BKT framing; a 3D Josephson coupling raises mean-field T_c but is the SAME (stiffness-limited) 3D lever already in the freeze ledger.
4. Frozen D_s=0.06–0.44 meV taken as given; a cuprate-scale D_s~7.4 meV would put the ceiling at 134 K, but then the win is the stiffness (the wall the freeze already states), not the vortex code.
5. Discrete RG (dl=0.01, l_max=60, bisection tol 1e-6): saturation 1.570796 vs exact pi/2=1.5707963 (−4.4e−7); >100 K verdict margin is insensitive to discretization.
6. The "no continuous Landauer bill" advantage (static stabilizer) is genuine but moot: the static term cannot beat the equilibrium spin-wave ceiling, so the thermodynamic-cost edge never matters.
7. No fabricated citations — all refs verified via web search 2026-06-25; universal jump + mu_XY~(pi^2/2)J are textbook KT.

## Conclusion
A static vortex-code stabilizer raises the BKT transition by suppressing thermal vortex unbinding (alpha>0 direction correct), but the rise is hard-bounded by the bare spin-wave ceiling T_BKT^max=(pi/2)·D_s (Nelson-Kosterlitz universal jump). With the frozen flat-band D_s, even infinite core energy caps T_BKT at 1.1–8.0 K — ~126 K and ~16.7× short of the 134–164 K wall. The code removes vortices; it cannot manufacture stiffness. Confirms the wall via the order-trap channel, tightening the no-go: suppressing the loss channel is not enough when the bare rigidity is the binding constraint. absorbed=false.

## Refs
- J.M. Kosterlitz, J. Phys. C 7, 1046 (1974) — RG recursion relations.
- D.R. Nelson & J.M. Kosterlitz, PRL 39, 1201 (1977) — universal jump K_R=2/pi.
- L. Benfatto, C. Castellani, T. Giamarchi, arXiv:1201.2307 (PRB 77, 100506(R)) — sine-Gordon vortex-core energy, mu_XY~(pi^2/2)J.
- 2D-XY at small vortex-core energy, arXiv:2007.01526 — fugacity raises T_BKT toward, never above, the spin-wave value.