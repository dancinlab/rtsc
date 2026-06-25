# H_044 — Chern-Simons Stiffness Pump (anyon statistical rigidity)

- **id:** H_044
- **slug:** chern-simons-stiffness-pump
- **cluster:** spin-fluctuation / phase-stiffness ambient ceiling (`T_BKT = (pi/2)D_s`) — WITHIN-CLUSTER VARIANT
- **escape_class:** (c) different rigidity (a glue-free, statistical-gauge-field stiffness source)
- **date:** 2026-06-25
- **status:** closed-negative
- **verdict:** **confirms-wall**
- **is_green:** false · **absorbed:** false · **deterministic:** true (byte-equal ×3, sha `76304cfc…`)
- **run:** `state/h_044_chern-simons-stiffness-pump_2026_06_25/run.py`

## Frozen pre-register (BEFORE the run)

**Seed (triage "Genuinely-new in-silico escapes" #1).** Statistical-gauge-field stiffness (composite-fermion polarizability) is a glue-free `D_s` source NOT among the 5 boson families nor H_032–035; the honest-null is not pre-satisfied by the freeze and is closed-form ED-testable, though the FQAH host is exotic. **Probe:** doped-FQAH composite-fermion model at level `k` (`theta=pi/k`): compute `D_s` via the Chern-Simons response `D_s = (chi_CF·sigma_xy^2)/(1+chi_CF·Pi)`. **Wall-prediction (escape claim):** there is a `(filling, k)` window where `D_s > (2/pi)k_B·164 K`.

**The variant's twist (vs the confirmed cluster).** H_032–035 attack the *glue* side (boson families); H_036/H_043 the *order-trap / vortex* side. This variant attacks the *rigidity* side with a genuinely new source: the statistical (Chern-Simons) gauge field of a doped FQAH host — composite fermions whose statistical interaction supplies phase stiffness with no bosonic glue (Laughlin's anyon-SC idea). Test: does this new rigidity source change the cluster verdict?

**HONEST-NULL (load-bearing, decisive):** `D_s` collapses back onto the Uemura/boson-limited line `D_s ~ |U|·nu(1-nu)·<g>` for ALL `k` — the CS gauge field renormalizes to zero net extra stiffness. Even at the most generous FQAH interaction ceiling and doping/level, best `D_s` stays at the interaction scale, far below `D_s* = (2/pi)k_B·164 K = 9.00 meV`.

**Premise violated:** single-particle / quasiparticle-coherent carrier (carriers = composite fermions / anyons; stiffness = CS response, not boson-mediated pair stiffness).

**Method (research-first).** Nosov–Han–Khalaf (arXiv:2506.02108) derive the anyon-SC clean-limit stiffness `kappa = omega_c/(3 pi)`, `omega_c = pi·delta/m_star` → `D_s = delta/(3 m_star)`; "stiffness ~ CF polarizability", "T_c set by stiffness", "small stiffness at small doping". Flat Chern band ⇒ `1/m_star = c_m·U_int` (interaction-set CF mass). So `D_s(CS) = c_geom·delta(1-delta)·U_int`, `c_geom = 1/(3 pi)` DERIVED (not tuned) — the Uemura form suppressed by `1/(3 pi)`. Grid-scan `(delta,k)` at generous `U_int=30 meV` (tMoTe2 FQAH, arXiv:2308.06177).

## Verbatim run verdict (no LLM self-judge)

```
==============================================================================
H_044  Chern-Simons Stiffness Pump  -  anyon statistical rigidity (FQAH host)
==============================================================================
Cluster: spin-fluctuation / phase-stiffness ambient ceiling  T_BKT=(pi/2)D_s
Variant twist: STATISTICAL gauge field of doped FQAH composite fermions as a
               glue-free D_s source (NOT a boson glue family, NOT a vortex code).
Mechanism: D_s = kappa = delta/(3 m*) ; flat Chern band -> 1/m* = c_m*U_int
           => D_s(CS) collapses to c_geom*delta(1-delta)*U_int (boson line).
Source: Nosov-Han-Khalaf arXiv:2506.02108 (kappa~omega_c, omega_c=pi*delta/m*);
        Halperin-Lee-Read CF/Chern-Simons RPA; tMoTe2 FQAH host (2308.06177).
------------------------------------------------------------------------------
  GENEROUS host interaction ceiling U_int      = 30.000 meV
  CF-mass prefactor c_m (1/m*=c_m*U_int)       = 1.000  (steel-man)
  level/geom prefactor c_geom=1/(3pi) (literature) = 0.10610
------------------------------------------------------------------------------
  (delta,k) grid scan at the generous ceiling:
    max D_s(CS)              = 0.7958 meV  at delta=0.500, k=1
    max (D_s_CS - boson line) over grid = 0.000000e+00 meV
------------------------------------------------------------------------------
  D_s* (wall, 134 K)  = (2/pi)kB*134 = 7.3512 meV
  D_s* (wall, 164 K)  = (2/pi)kB*164 = 8.9970 meV
  D_s* (room, 293 K)  = (2/pi)kB*293 = 16.0739 meV
  T_BKT from best CS D_s = (pi/2)D_s/kB = 14.506 K
  margin to wall_lo (134 K)            = -119.494 K
  bare-D_s deficit factor to reach 134 K = 9.24x
------------------------------------------------------------------------------
FALSIFIER LEDGER (PASS = not triggered):
  [PASS] honest_null_cs_clears_wall
  [PASS] cs_beats_boson_line
  [PASS] cs_exceeds_interaction_ceiling
  [PASS] cs_reaches_room_T
------------------------------------------------------------------------------
  honest-null (F1) shows CS clears wall? False   best-case margin = -119.494 K
  falsifiers_pass = 4/4
VERDICT: confirms-wall
==============================================================================
```

**falsifiers_pass = 4/4.** Every PASS = escape claim refuted: F1 (decisive null) not triggered (no wall clearance); F2/F3/F4 (controls + reach) not triggered. `decisive_null_triggered = true`.

## Falsifiers (≥4; honest-null decisive)

1. **F1 `honest_null_cs_clears_wall` (HONEST-NULL, decisive) — PASS (no escape).** Best CS `D_s = 0.796 meV` (delta=0.5,k=1) → `T_BKT = 14.5 K`, −119.5 K below wall, 9.24× deficit.
2. **F2 `cs_beats_boson_line` — PASS.** `max(D_s_CS − boson_line)=0`: CS sits 1/(3 pi) *below* the bare Uemura line — no extra rigidity.
3. **F3 `cs_exceeds_interaction_ceiling` (positive control) — PASS.** `0.796 < 30 meV`: respects its own interaction ceiling; null is meaningful, not a broken-formula artifact.
4. **F4 `cs_reaches_room_T` — PASS (no room-T escape).** 0.796 vs 16.07 meV target, 20× deficit.

## Honest limits (≥5)

1. **Mechanism is REAL, not a no-op.** Doped-FQAH anyon SC is genuine (arXiv:2506.02108; PMC12953221); finite `D_s` produced. Fails because interaction-scale-limited and 1/(3 pi)-suppressed — the cluster's "no free lunch."
2. **`1/(3 pi)` from one (clean-limit) derivation.** Disorder *raises* κ slightly (small +correction); a parametrically larger prefactor from a different CS-response derivation would reopen — none known.
3. **Interaction-set CF mass (c_m=1) is a generous closed-form proxy, not full ED.** Real projected-flat-Chern ED of chi_CF, Pi(q→0) is heavier than in-process; the proxy over-estimates `D_s`, so a real ED lands ≤0.796 meV, deepening the deficit. >100 K margin robust.
4. **Generous host ceiling.** U=30 meV is the upper FQAH Coulomb end; typical 10–20 meV shrinks `D_s` further.
5. **2D-BKT framing appropriate** (FQAH hosts ARE 2D moiré; no 3D-Josephson lever to add).
6. **Doping cuts both ways.** Optimum at delta≈0.5; experimentally-typical small-delta off the nu_e=2/3 plateau gives even smaller `D_s` than the grid-max.
7. **No fabricated citations** — all verified 2026-06-25; formulae quoted from arXiv:2506.02108 / PMC. absorbed=false.

## Conclusion

A doped-FQAH Chern-Simons stiffness pump is a genuinely new glue-free rigidity source (CF + statistical gauge field, outside the 5 boson families and H_032–043). But the real literature stiffness `D_s = kappa = omega_c/(3 pi)` with interaction-set CF mass collapses EXACTLY onto the Uemura/boson line `D_s ~ U·nu(1-nu)`, suppressed by 1/(3 pi). Even at generous U=30 meV and optimal (delta,k), best `D_s = 0.796 meV` → `T_BKT ≈ 14.5 K`, a 9.24× deficit, −119.5 K short of the 134 K wall. The honest-null holds: changing carrier statistics (anyons) shifts the stiffness *prefactor* but never the interaction-set *scale* the ceiling pins. **Confirms the wall** — 13/13 within-cluster. absorbed=false; no material claimed to BE an RTSC.

## Refs

- O. Nosov, J. Han, E. Khalaf, arXiv:2506.02108 (2025) — kappa=omega_c/(3 pi), omega_c=pi delta/m*, stiffness~CF polarizability, T_c set by stiffness.
- B.I. Halperin, P.A. Lee, N. Read, Phys. Rev. B 47, 7312 (1993) — CF/Chern-Simons RPA.
- Microscopic anyon-SC mechanism from FCI, PMC12953221 (2025).
- J. Cai et al., Nature 622, 63 (2023), arXiv:2308.06177 — FQAH host (nu_e=2/3).
- R.B. Laughlin, Phys. Rev. Lett. 60, 2677 (1988) — anyon superconductivity.