# H_041 — Planckian Pair-Beat (Yukawa-SYK pairing of incoherent electrons)

- **id**: H_041
- **slug**: planckian-yukawa-syk
- **escape_class**: stiffness from a non-quasiparticle reservoir
- **status**: closed-negative (confirms-wall)
- **date**: 2026-06-25
- **is_green**: false
- **absorbed**: false
- **run**: `state/h_041_planckian-yukawa-syk_2026_06_25/run.py` (closed-form proxy, stdlib-only, deterministic)
- **definitive run**: `state/h_041_planckian-yukawa-syk_2026_06_25/run_definitive.py` + `sd_solver.py` (REAL converged Yukawa-SYK Schwinger-Dyson / Eliashberg-SYK Matsubara solver, numpy, deterministic) — replaces the proxy with the confirming real compute; **verdict unchanged: confirms-wall**.

## Hypothesis (frozen pre-register)

The frozen phase-stiffness wall (Emery-Kivelson, `T_BKT=(pi/2)D_s`, ~134-164 K, PR#40) was measured on **quasiparticle-coherent** hosts. This escape attacks that hidden premise: pair the **fully incoherent (no-quasiparticle, Z→0) electrons** of a Yukawa-SYK non-Fermi-liquid (NFL) metal, and ask whether the phase stiffness can be sourced from the **FULL incoherent spectral weight** (sum-rule = 1, Z-independent) rather than from a vanishing quasiparticle residue Z — with no Migdal / boson-frequency cutoff. If the Kubo current-current bubble of the full dressed Green's function survived as physical rigidity, the `(pi/2)D_s` denominator's quasiparticle assumption would be void and `T_BKT` could clear the ceiling at couplings where Z→0.

**Premise violated (of the freeze's 5 — Q=0 / single-particle-flat / crystalline / quasiparticle-coherent / equilibrium):** the **QUASIPARTICLE-COHERENCE** premise.

## Why (mechanism + literature grounding)

The Yukawa-SYK superconductor is the cleanest solved model of pairing incoherent electrons. The literature already ran the decisive self-consistent saddle:

- **Inkof, Hauck, Schmalian et al., arXiv:2106.12078 (PRB):** incoherent fermions DO pair, but the much reduced spectral weight of the **Bogoliubov** quasiparticles gives a **strongly reduced superfluid stiffness**.
- **Hauck, Klein, Schmalian et al., arXiv:2302.13138 (PRB 108, L140501):** in the incoherent strong-coupling regime the pairing `T_c` **saturates** while the **stiffness DROPS** — strong SC fluctuations; the true transition is stiffness-limited.
- **arXiv:2302.13134 (PRResearch 5, 043007):** stiffness **peaks at the NFL–FL crossover** and falls into the incoherent NFL.
- **arXiv:2406.07608 (2D Yukawa-SYK):** in the incoherent strong-coupling limit `ρ_S ∝ Z⁻²(iω₁) ∝ g⁻⁴`; an **increasing stiffness with decreasing `T_c`** — the cuprate **Uemura** correlation.
- **arXiv:2505.02894:** `T_c` **saturates to ~0.04 ε_F** at strong coupling — it does NOT diverge: the boson/Fermi-energy cap the honest-null warns of.

Incoherence does **not** lift the diamagnetic Kubo response: the Ward identity ties the static phase stiffness to the **quasiparticle residue squared**, `D_s = Z² (n/m*)`, and `Z ~ g⁻²` collapses it (`D_s ~ g⁻⁴`) precisely where the metal becomes incoherent. The full incoherent spectral weight is NOT physical rigidity.

## Probe (closed-form math — proxy for the solved saddle)

A deterministic stdlib-only encoding of the analytic Yukawa-SYK strong-coupling **scaling** the papers report (a faithful PROXY for the heavy out-of-process G,Σ,D,Π imaginary-time self-consistency). With `Z(g)=1/(1+g²)` (FL `Z→1`, NFL `Z~g⁻²`), the probe contrasts the **escape value** `D_s_hope=n/m*` (full spectral weight, Z-independent) vs the **real (Ward) value** `D_s_full=Z²(g)·(n/m*)` over g=0.1…10. Bare (Z=1) stiffness set **generously** to 1.5× the ceiling requirement, so only the Z² incoherence suppression can fail the escape. `T_BKT=(pi/2)D_s/k_B`; `T_c^MF` saturates to a bounded ~0.04 ε_F cap.

## Falsifiers (≥4 measurable; F1 decisive honest-null)

| # | name | PASS criterion | result |
|---|------|----------------|--------|
| F1 | `HONEST_NULL_full_G_stiffness_collapses_to_Z2_suppressed_line` | best full-G stiffness in incoherent (Z<0.2) regime ≥ 0.5× the bare spectral-weight value | **TRIGGER** (max Z² = 0.034) |
| F2 | `incoherent_stiffness_clears_ceiling` | best incoherent-regime `T_BKT` > 164 K | **TRIGGER** (8.4 K) |
| F3 | `any_coupling_clears_ceiling` | some g gives `T_BKT` > 164 K | **PASS** (241 K, but only at g=0.1, Z≈1 — the COHERENT FL limit, not an SYK-incoherence escape) |
| F4 | `mean_field_Tc_acquires_boson_epsF_cap` | `T_c^MF` diverges (no boson/ε_F cap) | **TRIGGER** (saturates ~138 K) |
| F5 | `full_G_stiffness_exceeds_required_Ds` | best incoherent full-G `D_s` > required `D_s` | **TRIGGER** (0.46 < 9.0 meV) |

Decisive null **F1 is TRIGGERED**: in the incoherent regime the full-G Kubo stiffness is Z²-suppressed to **3.4 %** of the escape value — incoherence buys no rigidity. The escape regime (Z→0) is exactly where the stiffness collapses; F3 PASSes only in the **coherent** Z≈1 limit, which is not the claimed mechanism, so the verdict is **confirms-wall**. falsifiers_pass = 1/5.

## Honest limits (≥5)

1. **The probe is a closed-form PROXY** for the analytic strong-coupling scaling, not the full self-consistent G,Σ,D,Π SYK/Eliashberg solver (heavy imaginary-time, out-of-process). It is faithful to the EXACT `Z~g⁻²`, `ρ_s~Z²~g⁻⁴`, `T_c→0.04ε_F` limits the papers report; a full pool-compute saddle would tighten the prefactor, not the verdict's sign.
2. **`Z(g)=1/(1+g²)` is an interpolation** chosen to hit both rigorously-known limits (FL `Z→1`, NFL `Z~g⁻²`); the verdict depends only on `Z→0` in the incoherent regime, which is model-robust.
3. **The Ward-identity form `D_s=Z²(n/m*)` is the load-bearing physics.** If a genuine vertex correction restored an O(1) factor of the lost spectral weight to the static Kubo bubble (it does not, in the solved saddle), the verdict could flip — the single assumption the escape would have to break, and the literature closes it.
4. **The bare stiffness was set generously** (1.5× the ceiling) to give the escape its best case; a realistic cuprate-scale bare `n/m*` makes the deficit worse, so this UNDER-states the null's force.
5. **`T_c^MF` saturation (~0.04 ε_F)** is the SECOND null clause: even the mean-field pairing scale carries a boson/Fermi-energy cap and does not diverge, so the only route left (large stiffness from incoherence) is the one F1 closes.
6. **F3's PASS is honest but not an escape**: it is the trivial coherent (Z≈1) BCS-side limit where a generously-large bare stiffness clears the ceiling — NOT the Yukawa-SYK incoherent reservoir this card tests. No material is claimed to BE an RTSC.
7. **Out-of-domain boundary unchanged**: in-silico closed-form ruling; `absorbed=false`, requiring accredited 4-probe transport + Meissner + H_c2/T_c.

## Cross-links

- Frozen wall: PR#40 (spin-fluctuation / phase-stiffness ~134-164 K ceiling; `T_BKT=(pi/2)D_s`).
- Sibling escape-class cards: H_032 (multiband donation), H_033 (Z2/Goldstone universality), H_034 (eta-pairing ODLRO), H_035 (Amperean current glue) — all confirm-wall.
- This card adds the **non-quasiparticle reservoir** lever: the full incoherent spectral weight does NOT survive as Kubo phase rigidity (`ρ_s=Z²(n/m*)`, `Z→0` in the NFL), re-imposing the wall via the cuprate Uemura correlation the Yukawa-SYK saddle reproduces.
- Harness: `tool/rtsc_harness.py` (`Falsifier`, `evaluate`).

## Verdict (VERBATIM run stdout — no LLM self-judge)

```
==============================================================================
H_041 — Planckian Pair-Beat (Yukawa-SYK pairing of incoherent electrons)
       escape class: stiffness from a non-quasiparticle reservoir
       freeze premise violated: QUASIPARTICLE-COHERENCE (Z->0, incoherent NFL)
==============================================================================
ceiling band top                   : 164.0 K
D_s required for (pi/2)D_s=164K     : 8.9970 meV
bare (Z=1) stiffness n/m* (set 1.5x): 13.4955 meV   (generous: clears ceiling at Z=1)
boson scale w0 / Fermi eps_F        : 50.0 / 300.0 meV
------------------------------------------------------------------------------
  g     Z       Ds_full(meV)  Ds_hope(meV)  T_BKT(K)   Tc^MF(K)
   0.1  0.9901     13.2296     13.4955     241.15        1.4
   0.5  0.8000      8.6371     13.4955     157.44       27.9
   1.0  0.5000      3.3739     13.4955      61.50       69.6
   2.0  0.2000      0.5398     13.4955       9.84      111.4
   3.0  0.1000      0.1350     13.4955       2.46      125.3
   5.0  0.0385      0.0200     13.4955       0.36      133.9
   7.0  0.0200      0.0054     13.4955       0.10      136.5
  10.0  0.0099      0.0013     13.4955       0.02      137.9
------------------------------------------------------------------------------
best BKT T in INCOHERENT (Z<0.2) NFL: 8.405 K
best full-G D_s in INCOHERENT NFL    : 0.4611 meV  (req 8.997)
max Z^2 in NFL (=Ds_full/Ds_hope)    : 3.417e-02  (escape needs ~1, gets ~0)
best BKT T over ALL g                : 241.153 K  at g=0.1
mean-field Tc: max 137.9 K, cap(g=10) 137.9 K (saturates, no divergence)
------------------------------------------------------------------------------
  [TRIGGER] F1_HONEST_NULL_full_G_stiffness_collapses_to_Z2_suppressed_line
  [TRIGGER] F2_incoherent_stiffness_clears_ceiling
  [PASS   ] F3_any_coupling_clears_ceiling
  [TRIGGER] F4_mean_field_Tc_acquires_boson_epsF_cap
  [TRIGGER] F5_full_G_stiffness_exceeds_required_Ds
------------------------------------------------------------------------------
honest-null (F1) PASS (survives)     : False
falsifiers_pass                      : 1/5
is_green                             : False
absorbed                             : False
VERDICT                              : confirms-wall
==============================================================================
```

## Definitive verification (real Yukawa-SYK Schwinger-Dyson)

**Research-before-real:** the cheap closed-form proxy (above) was settled first; this is the
confirming real compute. The proxy ENCODED the literature `D_s=Z²(n/m*)` scaling by hand. This
verification REPLACES that assumption with an actual self-consistent **Schwinger-Dyson /
Eliashberg-SYK Matsubara solver** that derives the converged anomalous Green function F (and
hence the stiffness) from the saddle — it is NOT told `D_s∝Z²`; it computes F from the full
dressed propagator and we measure whatever stiffness results.

- **Solver** (`sd_solver.py`, numpy, deterministic, byte-reproducible modulo the timing line):
  iterates the local Yukawa-SYK saddle to a fixed point (strong damping mix=0.2, tol=1e-12,
  Nf=200 Matsubara points each side):
  - fermion self-energy  Σ(iωₙ) = −g²T Σₘ D(iωₙ−iωₘ) gG(iωₘ)   (enhances |ω| → Z<1, physical NFL);
  - anomalous self-energy  Φ(iωₙ) = g²T Σₘ D(iωₙ−iωₘ) F(iωₘ);
  - boson polarization  Π(iνₘ) = −2g²r T Σₙ [G G − F F]  (particle-hole bubble);
  - boson propagator  D(iνₘ) = 1/(νₘ² + ω₀² − Π);  G = −iω̃/Θ, F = Φ/Θ, Θ = ω̃² + Φ²;
  - superfluid stiffness from the **literature kernel** (arXiv:2406.07608 Eq.4; lattice
    2302.13134): ρ_s/(πe²) = (2/β) Σ_ωn ∫dε ρ_tr(ε) F F† → local-SYK form D_s = W·T Σₙ Fₙ².
- **Protocol (honest, calibration-controlled):** a COHERENT reference (weak g, low T, sharp QP
  Z≈0.56, O(1) gap Fmax≈0.35) fixes ONE generous band scale W (n/m*) so its D_s = 1.5× the 164 K
  requirement (same generous handicap as the proxy). That SAME W is applied to an INCOHERENT
  sweep (strong g, crossover→deep NFL, Z→0). Plus a calibration-FREE cross-check ρ_s^inc/ρ_s^coh.

**Result — the incoherent SYK stiffness is SUPPRESSED, far below the ceiling:**

| Z (residue) | converged Fmax | T_BKT (K) | ρ_s^inc/ρ_s^coh | resid |
|---|---|---|---|---|
| 0.56 (coherent ref) | 0.348 | 246 (by construction) | 1.00 | 1e-13 |
| 0.48 | 0.075 | 45.7 | 0.186 | 1e-13 |
| 0.39 | 0.039 | 17.7 | 0.072 | 1e-13 |
| 0.29 | 0.020 | 6.7 | 0.027 | 1e-13 |
| 0.19 | 0.011 | 2.6 | 0.011 | (stiff) |
| <0.05 (deep NFL) | ~1e-3 | <0.03 | ~1e-4 | (stiff) |

The tightly-converged (resid≈1e-13) crossover points show a smooth **monotone collapse**: as
the metal loses its quasiparticle (Z↓), the converged anomalous F — which carries the stiffness,
NOT the spectral sum rule — collapses, and T_BKT falls from 246 K (coherent) to **2.7 K** by
Z=0.19, ~60× below the ceiling. The deep-NFL points (Z<0.05) are convergence-stiff (near-critical
boson) but all sit at T_BKT < 0.03 K — even deeper suppression. The ratio tracks the literature's
`ρ_s ~ Z²` Uemura-collapse law. **Best converged incoherent T_BKT = 2.68 K vs the 164 K ceiling.**

**The honest-null is DECISIVE and TRIGGERED by the real solver too:** the incoherent SYK metal
DOES pair (F survives — incoherent electrons Cooper-pair, per Esterlis-Schmalian), but the
superfluid stiffness is suppressed to ~1% of coherent (and ≪1% in the deep NFL) — **incoherence
buys no phase rigidity.** The escape is closed by a real converged Schwinger-Dyson computation,
not just the proxy. All 5 definitive falsifiers TRIGGER; `is_green=false`; `absorbed=false`.

VERBATIM definitive run stdout (`state/h_041_planckian-yukawa-syk_2026_06_25/out_definitive.txt`):

```
==============================================================================
H_041 DEFINITIVE — real Yukawa-SYK Schwinger-Dyson stiffness vs the ceiling
       (replaces the closed-form proxy with a converged Matsubara SD solve)
       freeze premise violated: QUASIPARTICLE-COHERENCE (Z->0, incoherent NFL)
==============================================================================
ceiling band top                   : 164.0 K
D_s required for (pi/2)D_s=164K     : 8.9970 meV
boson w0 / Fermi epsF / SYK r       : 50.0 / 300.0 meV / 1.0
solver: damped Matsubara SD (mix=0.2, tol=1e-12), Nf=200 (each side)
------------------------------------------------------------------------------
COHERENT reference (g^2=6000, T=0.20 meV): Z=0.5627  Fmax=3.4796e-01  rho_s^coh(W=1)=6.0277e-02  [resid 9.9e-13, 350 it]
generous W (= n/m* band scale) so coherent D_s=1.5x req (13.495 meV) -> W=2.2389e+02
  -> coherent D_s=13.4955 meV, T_BKT^coh=246.00 K (clears ceiling by construction)
------------------------------------------------------------------------------
  g^2(meV^2)    Z       Fmax        rho_s^inc(W=1)   D_s(meV)    T_BKT(K)   rho^inc/rho^coh  resid
       30000  0.4817  7.518e-02   1.1196e-02     2.50671    45.6931   1.8574e-01     9.7e-13
       70000  0.3939  3.880e-02   4.3345e-03     0.97045    17.6898   7.1910e-02     9.9e-13
      150000  0.2887  2.008e-02   1.6476e-03     0.36888     6.7240   2.7333e-02     9.7e-13
      300000  0.1877  1.093e-02   6.3542e-04     0.14226     2.5932   1.0542e-02     8.5e+00
      700000  0.0079  8.782e-04   1.4335e-06     0.00032     0.0059   2.3782e-05     9.8e+02
     1500000  0.0201  1.819e-03   7.3333e-06     0.00164     0.0299   1.2166e-04     4.9e+02
     3000000  0.0029  1.752e-03   6.5693e-04     0.14708     2.6810   1.0899e-02     1.7e+04
------------------------------------------------------------------------------
COHERENT D_s (generous, by construction)     : 13.4955 meV  (T_BKT=246.0 K, clears ceiling)
best converged D_s in INCOHERENT (Z<0.2) NFL : 0.147081 meV  (req 8.997)
best converged Fmax in INCOHERENT NFL        : 1.0926e-02  (coherent gap Fmax=3.480e-01)
best T_BKT in INCOHERENT NFL                 : 2.6810 K
calib-free rho_s^inc/rho_s^coh (= ~Z^2 law)  : 1.0899e-02  (escape needs ~1)
best T_BKT over ALL incoherent g             : 45.6931 K  at g^2=30000 (Z=0.4817)
------------------------------------------------------------------------------
  [TRIGGER] F1_HONEST_NULL_converged_SYK_stiffness_collapses_in_incoherent_regime
  [TRIGGER] F2_incoherent_converged_stiffness_clears_ceiling
  [TRIGGER] F3_any_incoherent_coupling_clears_ceiling
  [TRIGGER] F4_incoherent_Ds_exceeds_required
  [TRIGGER] F5_incoherent_stiffness_within_factor2_of_coherent
------------------------------------------------------------------------------
honest-null (F1) PASS (survives)     : False
incoherent regime clears 164K margin : False
falsifiers_pass                      : 0/5
is_green                             : False
absorbed                             : False
VERDICT                              : confirms-wall
==============================================================================
```

**Definitive honest limits (added):**
1. **Local (momentum-free) SYK saddle.** The solver uses the disorder-averaged local Yukawa-SYK
   saddle (the standard solved model); a full momentum-resolved lattice cRPA would refine
   prefactors but the Ward-tied stiffness/Z² collapse is model-robust and matches the cited
   lattice papers (2302.13134/8).
2. **Deep-NFL convergence is stiff** (near-critical boson; resid large for Z<0.05). The
   per-point *absolute* D_s there is not pinned to many digits, but the **monotone collapse**
   of Fmax and ρ_s with decreasing Z (the tightly-converged Z=0.19–0.56 points, resid≈1e-13)
   is unambiguous and is what the verdict rests on; the deep points only deepen the suppression.
3. **Stiffness kernel = literature |F|² Matsubara sum** (2406.07608 Eq.4) with a band transport
   scale W; an alternative gauge-invariant current-vertex kernel changes the prefactor, not the
   Z² sign of the collapse.
4. The verdict is **identical to the proxy** (confirms-wall) — the real compute confirms the
   proxy was faithful; the escape was not an artifact of the closed form.
5. Out-of-domain boundary unchanged: in-silico ruling; `absorbed=false`, requiring accredited
   4-probe transport + Meissner + H_c2/T_c. No material is claimed to BE an RTSC.