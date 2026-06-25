# H_058 — PDW Commensurate Lock: pair-density-wave pinned to the lattice

- **id**: H_058
- **slug**: pdw-commensurate-lock
- **escape_class**: (b) order-traps clause — commensurate phase pinning (violates the Q=0 premise from momentum space)
- **cluster**: finite-Q / order-traps (sibling of H_042 FFLO, H_043 vortex-code)
- **status**: closed-negative (confirms-wall)
- **date**: 2026-06-25
- **is_green**: false
- **absorbed**: false
- **run**: `state/h_058_pdw-commensurate-lock_2026_06_25/run.py` (stdlib-only, deterministic, byte-reproducible)

## Which of the freeze's 5 premises this violates

The frozen geometric-stiffness verdict was measured on **Q=0** / single-particle-flat / crystalline / quasiparticle-coherent / equilibrium hosts. This card violates ONE: the **Q=0 premise** — but from a different angle than its FFLO sibling H_042. Instead of claiming the finite-Q *sliding stiffness* is large, it attacks the **"order-traps" clause**: a commensurate (Q=G/n) PDW whose soft sliding Goldstone (the PDW phason) is **gapped** by a lattice-commensurate Umklapp `V_p·cos(n·theta)`, so free vortices/phase-slips cost `Delta_phason` instead of `(pi/2)D_s`. Untouched by H_032–035 and by the finite-Q siblings H_042 (stiffness magnitude) / H_043 (code-space phase lock).

## Hypothesis (frozen pre-register)

Commensurate PDW `Delta(r) ~ Delta_0 cos(Q·r)`, `Q=G/n`, sliding phason gapped by `V_p·cos(n·theta)`: `Delta_phason ~ sqrt(V_p·rho_s)`, so `T_melt ~ max[(pi/2)D_s, Delta_phason]`. Escape claim: at accessible `V_p`, `Delta_phason > 164 K` while the finite-Q pairing eigenvalue is unchanged → BKT no longer caps `T_c`.

## Why (mechanism + literature grounding)

Commensurate pinning is real (commensurability energy ∝ cos(n·theta) → finite phason gap): Lee-Rice-Anderson Solid State Commun. 14, 703 (1974); McMillan PRB 12, 1187 (1975) / Nakanishi-Shiba; arXiv:1706.07231; arXiv:2409.02236. Load-bearing honest-null: (i) the lock-in energy is a **high-order Umklapp** `V_p(n)~W·(Delta_0/W)^n`, `(Delta_0/W)<<1`, so `Delta_phason` is the geometric mean of a tiny commensurability energy and the already-capped dilute Q=0 superfluid weight — it cannot out-run the wall; (ii) the same Umklapp mixes `+Q/−Q` and depairs the finite-Q channel for the small `n` where `V_p` is largest. Big gap and intact pairing are mutually exclusive: no free lunch.

## Probe

Same host as H_042 (`t=0.3 eV`, `W=8t=2.4 eV`, `Delta_0=20 meV`). Sweep `n=2..6`: `V_p(n)=W·(Delta_0/W)^n`; `Delta_phason(n)=sqrt(V_p·rho_s)/k_B` with `rho_s` charitably anchored to 164 K; `lambda_pair(n)/lambda_0=1−(Delta_0/W)^{n-1}`; `T_melt=max[(pi/2)D_s, Delta_phason·survive]`. Escapes-wall ONLY if decisive honest-nulls F1, F2 AND joint F3 all PASS (not triggered). No LLM self-judge.

## Verbatim run verdict

```
==========================================================================
H_058  PDW Commensurate Lock — pair-density-wave pinned to the lattice
==========================================================================
cluster: finite-Q / order-traps (violates the Q=0 premise of the freeze)
host band: t=0.300 eV, W=8t=2.400 eV, Delta0=20.0 meV
dilute Q=0 rigidity (pi/2)D_s^Q0 anchor = 164.0 K (TOP of frozen band, charitable)
rho_s = 14.1324 meV ;  (Delta0/W) = 0.00833
commensurability energy V_p(n) ~ W*(Delta0/W)^n  (LRA / McMillan-Nakanishi-Shiba)
phason gap Delta_phason(n) ~ sqrt(V_p*rho_s) ;  finite-Q pairing mixing ~ (Delta0/W)^(n-1)
--------------------------------------------------------------------------
  n        Vp(meV)     Dphason(K)   lambda/lam0   T_melt(K)
  2   1.666667e-01     1.7810e+01      0.991667      164.00
  3   1.388889e-03     1.6258e+00      0.999931      164.00
  4   1.157407e-05     1.4842e-01      0.999999      164.00
  5   9.645062e-08     1.3548e-02      1.000000      164.00
  6   8.037551e-10     1.2368e-03      1.000000      164.00
--------------------------------------------------------------------------
best phason gap over n-sweep    = 1.7810e+01 K  (at n=2)
  vs ceiling top                = 164.0 K
n=2 (strongest pinning) gap     = 1.7810e+01 K, lambda/lam0 = 0.991667
best T_melt = max[(pi/2)Ds, Dph]= 164.00 K
campaign ceiling                = 134-164 K (room-T target 293 K)
--------------------------------------------------------------------------
  [FAIL] honest_null_N1_phason_gap_stays_below_ceiling
  [FAIL] honest_null_N2_strong_pinning_depairs_finiteQ
  [FAIL] honest_null_N3_no_joint_gap_and_pairing
  [FAIL] t_melt_below_room_target
  [PASS] commensurability_energy_high_order_guard
--------------------------------------------------------------------------
HONEST-NULL N1 escape-PASS (gap beats ceiling) = False
HONEST-NULL N2 escape-PASS (pairing fully intact) = False
HONEST-NULL N3 escape-PASS (joint gap+pairing) = False
falsifiers_pass = 1/5
is_green = False
absorbed = false
VERDICT: confirms-wall
==========================================================================
```

## Falsifiers (≥4; F1 & F2 decisive honest-nulls)

| # | name | escape-PASS criterion | result |
|---|------|------------------------|--------|
| F1 | `honest_null_N1_phason_gap_stays_below_ceiling` | DECISIVE: best `Delta_phason` > 164 K | **FAIL** (max gap 17.81 K ≤ 164 K) |
| F2 | `honest_null_N2_strong_pinning_depairs_finiteQ` | DECISIVE: at n=2 pairing fully intact (`lambda_ratio≥1`) | **FAIL** (lambda/lam0=0.9917<1) |
| F3 | `honest_null_N3_no_joint_gap_and_pairing` | some n clears 164 K gap AND keeps `lambda_ratio≥0.95` | **FAIL** (mutually exclusive) |
| F4 | `t_melt_below_room_target` | max `T_melt` ≥ 293 K | **FAIL** (T_melt=164 K < 293 K) |
| F5 | `commensurability_energy_high_order_guard` | small-ratio expansion valid (`0<Delta_0<W`) | **PASS** (guard holds) |

`falsifiers_pass = 1/5`. Verdict: **confirms-wall**.

## Honest limits (≥5)

1. Toy high-order-Umklapp kernel `V_p=W·(Delta_0/W)^n`, not a self-consistent BdG `Delta(r)` solve; verdict structural, not prefactor-dependent.
2. Charitable `rho_s` anchored to 164 K (band top); real flat-band `D_s` is 1–8 K, so true gap is even smaller — null safer than printed.
3. `(Delta_0/W)` is the single small parameter; `Delta_0→W` exits the controlled flat-band regime; even `Delta_0/W=0.1` gives only tens of K, not hundreds.
4. Linearized `±Q` depairing `1−(Delta_0/W)^{n-1}` is a first-pass; true depairing could be larger but never helps — no-free-lunch direction robust.
5. Single commensurate channel; a real PDW host also has a competing commensurate CDW/SDW sharing the lock-in, further suppressing SC — tightens null.
6. `T_melt` uses `max[]`, not a full anisotropic 2D-XY/BKT flow; since `Delta_phason`<<`(pi/2)D_s`, a full flow can only lower melting `T`.
7. Commensurability order `n` is set by host filling/lattice, not freely dialable; the most favorable `n=2` already fails; realistic dilute-band `n` is larger (gap exponentially smaller).

## Verdict

**confirms-wall.** Pinning a commensurate PDW phason to the lattice does NOT supply a fluctuation-proof rigidity beating the dilute Q=0 superfluid weight: the lock-in energy is a high-order Umklapp `~W·(Delta_0/W)^n`, so even at `n=2` with a charitable 164 K `rho_s` the gap is only 17.8 K (an order of magnitude below the ceiling, ~16× below 293 K) and the same strong pinning depairs the finite-Q channel (`lambda/lam0=0.9917<1`). Big gap and intact finite-Q pairing are mutually exclusive: no free lunch. Both decisive honest-null prongs triggered; grounded in Lee-Rice-Anderson 1974, McMillan PRB 12 1187 1975 / Nakanishi-Shiba, arXiv:1706.07231, arXiv:2409.02236. `is_green=false`, `absorbed=false`; no material is claimed to BE an RTSC.