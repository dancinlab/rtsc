# H_054 — ANISOTROPY-LOCKED GLUE: crystal-symmetry-protected pairing immune to order melting

- **id**: H_054
- **slug**: anisotropy-locked-glue
- **escape_class**: (b) different glue — spin-group-symmetry vertex claimed to degrade with moment amplitude SLOWER than a Goldstone magnon (thermal-robustness axis)
- **cluster**: spin-group-symmetry pairing decoupled from ORDER AMPLITUDE (thermal-axis within-cluster VARIANT of H_040 nodal-spin-splitter; H_033/H_034 magnon closures)
- **status**: closed-negative (confirms-wall)
- **date**: 2026-06-25
- **is_green**: false
- **absorbed**: false
- **run**: `state/h_054_anisotropy-locked-glue_2026_06_25/run.py` (stdlib-only, deterministic, byte-reproducible)

## Within-cluster variant — what twist is being tested

H_040 already closed the **T=0 stiffness-sweep** axis of the altermagnet glue (does `lambda_pair` stay finite as `rho_s -> 0` at fixed t_AM? — no, it tracks the Stoner factor). This card tests the **orthogonal THERMAL axis** the seed names: even granting a finite T=0 vertex, does the spin-group-symmetry lock make `lambda_pair(T)` degrade with the moment amplitude `<S>(T)` **SLOWER** than a Goldstone-magnon control as T rises toward `T_N`? Seed CLAIM: `lambda_AM(T)` retains **>50% out to 0.7 T_N** while an AFM-magnon control on the SAME lattice falls below 50% by **0.3 T_N**.

## Which freeze premise this attacks

The **'order-traps' half** of the meta-law: glue borrowed from a magnetic order thermally dies WITH the order (`lambda ~ <S>^2`), so the usable-glue window closes at the same reduced T the order melts. This variant posits symmetry protection **partially decouples `lambda_pair(T)` from `<S>(T)`**.

## Hypothesis (frozen pre-register)

On one square lattice (`T_N = z·J`), run TWO SF pairing vertices differing ONLY in FS form factor (the symmetry lock): an altermagnet d-wave (B1g) vertex and an AFM-magnon control. Seed CLAIMS normalized `lambda_AM(T)/lambda_AM(0)` retains >50% to `T/T_N=0.7` while `lambda_AFM(T)/lambda_AFM(0)` drops below 50% by `T/T_N=0.3` → margin `T50_AM − T50_AFM >= 0.30`.

## Why (mechanism + literature)

Altermagnet SF vertex = standard RPA kernel `V ~ U^2·chi(q,T)`, amplitude set by local-moment / short-range correlation magnitude, NOT a T-independent crystal constant. The spin-group symmetry fixes the d-wave NODE STRUCTURE (which q-channel), not the AMPLITUDE.
- **arXiv:2505.12342**: anisotropy suppresses long-range AFM order while enhancing d-wave pairing via **short-range spin fluctuations** — pairing still rides `chi(q)`.
- **arXiv:2509.09959 / 2510.19083**: `V ~ U^2·chi` RPA; lambda strongest at the magnetic instability, collapses away.
- **Dahm et al. Nat.Phys. 5, 217 (2009)** (arXiv:0812.3217); **cond-mat/0408564**: SF pairing T-dependence follows `chi(T)`; amplitude tracks `<S·S>(T) ~ <S>^2(T)` plus a short-range tail.

**Key identity:** C4-paired spin-group symmetry is a SELECTION RULE on the MOMENTUM structure of `chi`; the OVERALL SCALE is the static local susceptibility `~ <S^2>`, a Curie/Brillouin amplitude collapsing on the SAME Weiss/Brillouin reduced-T scale as any AFM order. Short-range correlations give BOTH the same OZ tail above T_N. Symmetry buys a different ANGULAR pattern, not a slower amplitude decay.

## The probe (deterministic, stdlib-only, L=24×24, <1 s)

`m(T)` self-consistent Weiss/Brillouin (`m = tanh(z·J·m/T)`, `T_N=1.0` t-units); shared `Camp(T) = max(m(T)^2, min(1, c_tail·T_N/T))`; `lambda_AM = g0·<g_dwave^2>·Camp`, `lambda_AFM = g0·<g_magnon^2>·Camp`; normalize each to T=0; `T50` = reduced T where ratio drops below 0.50; charge `D_s` capped at 7.4 meV, `T_BKT=(pi/2)D_s`. `g0=4, c_tail=0.15, t_AM=0.40` fixed — **not tuned to green** (they cancel in the normalized curve; the load-bearing test is whether the symmetry makes the normalized decay slower — it cannot, both share `Camp(T)`).

## Falsifiers (PASS = NOT triggered)

1. **F1_honest_null_tracks_S_squared** (DECISIVE) — TRIGGERS when `T50_AM − T50_AFM < 0.30`: the symmetry gives zero thermal robustness.
2. **F2_AM_fails_0p7TN_retention** — TRIGGERS when `T50_AM < 0.7`.
3. **F3_curves_identical** — TRIGGERS when `max|lambda_AM/0 − lambda_AFM/0| < 1e-6` (same curve).
4. **F4_surviving_tbkt_below_wall** — TRIGGERS when best surviving (≥50%) AM `T_BKT ≤ 164 K`.
5. **F5_no_dwave_projection** — TRIGGERS when `<g_dwave^2> ≤ 0.01` (degenerate guard).

ESCAPE requires ALL five PASS **including** F1.

## Verbatim run verdict (no LLM self-judge)

```
FS form factor <g^2>  AM (d-wave) = 0.277617
FS form factor <g^2>  AFM (magnon)= 0.014916
T50 (reduced) AM  (need >= 0.7)   = 0.8080
T50 (reduced) AFM (need <= 0.3)   = 0.8080
thermal-robustness margin T50_AM - T50_AFM = +0.0000  (need >= 0.3 to escape)
max |lam_AM/0 - lam_AFM/0| over T          = 2.220446e-16
AM charge T_BKT at 0.7 T_N                 = 160.49 K
best surviving (>=50%) AM charge T_BKT     = 210.49 K  (wall 134-164 K)
  [FAIL] F1_honest_null_tracks_S_squared
  [PASS] F2_AM_fails_0p7TN_retention
  [FAIL] F3_curves_identical
  [PASS] F4_surviving_tbkt_below_wall
  [PASS] F5_no_dwave_projection
honest_null (F1) PASS = False
falsifiers_pass = 3/5
VERDICT: confirms-wall
```

The honest-null **F1 FAILS**: normalized `lambda_AM(T)` and `lambda_AFM(T)` curves are identical to machine precision (max diff 2.2e-16), so both have `T50 = 0.808` and the margin is `+0.0000` vs the required +0.30. F3 also fails. The spin-group symmetry changes only the angular form factor `<g^2>` (AM 0.278 vs AFM 0.015 — a large which-channel difference) but NOT the amplitude T-law; both ride the same `Camp(T)`. F2/F4 PASS vacuously — the AM vertex survives to 0.7 T_N but the AFM control does exactly the same, so there is no DIFFERENTIAL thermal robustness ("no free lunch").

## Honest limits

1. **Mean-field Weiss/Brillouin order amplitude, not QMC/DMFT** — but AM and AFM amplitudes obey the SAME self-consistent equation (same spin/coordination/J), which makes the normalized curves identical exactly in this model.
2. **Scalar shared-amplitude proxy** — vertices differ only in `<g^2>`; a full q-resolved matrix kernel factorizes angular × amplitude identically, so the conclusion is robust.
3. **OZ tail `c_tail=0.15` fixed and SHARED** — cancels in `T50_AM − T50_AFM`; moves both T50's together, cannot open a margin.
4. **Single half-filling FS weight** — doping rescales both `<g^2>` but not the shared amplitude law.
5. **Charge-D_s 7.4 meV cap encodes the freeze's doped-Mott scarcity**, not a recomputed Kubo weight; the F1 failure is upstream of and independent of the cap (a statement about the normalized curves).
6. **In-silico only**; absorbed=false. A closed-negative on the *thermal-decoupling mechanism*, not a claim altermagnets cannot superconduct (they can, at low Tc, coupled to `<S>`).

## Verdict

**confirms-wall.** A crystal-symmetry / spin-group lock does NOT make the altermagnet SF pairing vertex thermally more robust than a Goldstone magnon: the normalized `lambda(T)` curves are identical to machine precision because both ride the same order-amplitude `Camp(T) ~ <S>^2`; symmetry picks the *angular channel*, not the *amplitude T-law*. Margin exactly zero (need ≥0.30). Thermal-axis within-cluster variant of H_040; re-confirms the magnon-family closure (H_033/H_034) and the frozen ~134-164 K phase-stiffness ceiling. is_green=false, absorbed=false.