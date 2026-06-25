# H_037 — Bethe-Ceiling Lattice (negative-curvature stiffness ladder)

- **id**: H_037
- **slug**: bethe-ceiling-hyperbolic-lattice
- **escape_class**: connectivity-geometry universality (Mermin-Wagner fails)
- **status**: closed-negative (confirms-wall)
- **date**: 2026-06-25
- **is_green**: false
- **absorbed**: false
- **run**: `state/h_037_bethe-ceiling-hyperbolic-lattice_2026_06_25/run.py` (stdlib-only, deterministic, byte-reproducible)

## Hypothesis (frozen pre-register)

The frozen phase-stiffness wall (~134-164 K; `T_BKT=(pi/2)D_s`) was MEASURED on
CRYSTALLINE (flat / Euclidean) hosts. This card violates exactly the **crystalline**
premise of the freeze: replace the square-lattice Cooper-pair phase field with a
**negative-curvature hyperbolic tiling** ({7,3} heptagonal or {5,4}). On a hyperbolic
graph the volume grows exponentially with radius (the graph is "effectively
infinite-dimensional"), so the Mermin-Wagner / BKT log-suppression of order is claimed
to be replaced by a **mean-field crossing** at fixed bare stiffness `J`: vortex entropy
can no longer compensate vortex energy on an exponentially-growing graph.

**Wall-prediction (escape):** `T_c^hyperbolic / T_c^square >= 1.7` at matched bare `J`,
lifting the ambient ceiling past 164 K purely by connectivity geometry — no new glue,
no new boson family (distinct from H_032-035), and a different universality change than
H_033's z=2 dynamical-critical lever.

**Honest-null (load-bearing, from the triage probe_sketch — NOT engineered):**
`T_c^hyperbolic <= 1.2 x T_c^square` — the negative curvature does NOT lift the bulk
ordering temperature; the apparent "mean-field" lift is a boundary-dominated
finite-size artifact and BKT-like physics (or worse) survives at matched `D_s`.

## Why (mechanism + literature grounding, research-first)

The literature is genuinely **split**, and the split IS the answer:

- **DISCRETE clock models** on the {7,3} hyperbolic lattice DO cross **mean-field**
  (corner-transfer-matrix RG; Krcmar, Gendiar et al., arXiv:0801.0836). The
  "effectively infinite-dimensional" exponential volume growth makes the discrete
  q-state transition mean-field. This is the optimistic estimate the escape rests on:
  plane-rotor Weiss mean-field gives `kT_c^MF=(z/2)J`, so for {7,3} (z=3) the naive
  ratio vs square BKT (`T_BKT/J=0.893`, Tobochnik-Chester PRB 20 3761 1979) is
  `(3/2)/0.893 = 1.68` — tantalizingly right at the 1.7 escape threshold.

- **The CONTINUOUS XY model** (the actual U(1) Cooper-pair phase) on a hyperbolic
  surface does the OPPOSITE: **curvature-induced frustration drives a zero-temperature
  glass with NO finite-T order** (Baek, Minnhagen, Shima, Kim, *Phys. Rev. E* **80**,
  011133, 2009; PubMed 19658458). A constant ferromagnetic coupling on the curved
  surface "exhibits glasslike behavior without possessing any disorder" — the curvature
  itself replaces random disorder. Independently, heptagonal-XY open-boundary MC reports
  **absence of any transition including BKT**.

The superconducting order parameter is a **continuous U(1) phase**, not a discrete clock
state — so the continuous-XY result governs. This is the no-free-lunch the freeze
predicts: the geometry that would defeat vortex entropy (the escape) simultaneously
injects curvature frustration that destroys continuous-phase order (the null). The
{p,q} shell growth ratio quantifies the mechanism: `mu_{7,3}=phi^2=2.618`, boundary
fraction `f_bd=(mu-1)/mu=1/phi=0.618` — an **O(1) fraction of vertices is on the
boundary at every tractable size**, so a "bulk mean-field" lift is never actually
reached; what looks like order is the boundary, exactly the honest-null's wording.

## Probe (closed-form proxy + the in-process compute it CAN do)

Deterministic, stdlib-only. The honest settlement of the continuous-XY case at the
required scale needs a large open-boundary hyperbolic XY Monte-Carlo with careful
bulk extrapolation, which does NOT fit byte-deterministically in-process in seconds.
So the probe is the best closed-form PROXY, and it settles BECAUSE the continuous-XY
honest-null is already a MEASURED literature result:

- **(A)** computes the optimistic discrete-clock mean-field ratio (`{7,3}=1.68`,
  `{5,4}=2.24`) — granted as real (F1 PASS).
- **(B)** computes the {p,q} shell growth `mu` (closed form) and boundary fraction
  `f_bd` exactly: `{7,3} -> 0.618`, `{5,4} -> 0.732` (all-boundary graph).
- **(C)** the decisive honest-null: the realized **continuous** U(1) ordering ratio is
  `0.0` (no finite-T order; zero-T glass), `<= 1.2` by a wide margin -> escape fails.

## Falsifiers (>=4 measurable; F2 decisive honest-null)

| # | name | PASS criterion | result |
|---|------|----------------|--------|
| F1 | `discrete_clock_meanfield_estimate_is_real` | discrete {7,3} clock model crosses ~mean-field (~1.68x) | **PASS** (premise granted) |
| F2 | `HONEST_NULL_continuous_phase_lifts_bulk_Tc` | realized continuous-XY `T_c^hyp/T_c^sq > 1.2` (lifts bulk) | **TRIGGER** (ratio = 0.0) |
| F3 | `escape_ratio_ge_1p7_realized` | realized `T_c^hyp/T_c^sq >= 1.7` at matched J | **TRIGGER** (ratio = 0.0) |
| F4 | `tc_exceeds_wall_band` | hyperbolic `T_c > 164 K` (clears ceiling band) | **TRIGGER** (T_c = 0 K) |
| F5 | `lift_is_bulk_not_boundary_artifact` | boundary fraction `< 1/2` so a bulk lift is well-defined | **TRIGGER** (f_bd = 0.618) |

Decisive null F2 is **TRIGGERED** with a wide margin (realized continuous-phase ratio
0.0 vs 1.2 threshold) — the hypothesis CONFIRMS the wall. Measurable in principle: a
real hyperbolic XY-MC ordering temperature on a {7,3}/{5,4} tiling vs a square lattice
at matched bare `J` (open-boundary, bulk-extrapolated); the spin-stiffness helicity
modulus; and whether the low-T state is a frozen glass (Edwards-Anderson `q_EA>0`,
zero net magnetization) vs a uniform phase-ordered superfluid.

## Honest limits (>=5)

1. **Closed-form PROXY, not an in-process hyperbolic XY-MC.** A byte-deterministic
   large open-boundary hyperbolic XY Monte-Carlo with bulk extrapolation does not fit
   in-process in seconds; the verdict leans on the MEASURED continuous-XY literature
   result rather than re-deriving it here. A summer-pool XY-MC on a {7,3}/{5,4} tiling
   (~10^4-10^5 sites, parallel-tempering, helicity-modulus bulk extrapolation) would be
   the decisive own-compute confirmation. (This is the residual pool item.)
2. **The discrete-clock mean-field crossing (F1) is granted in full** — it is a real,
   independently-published result (arXiv:0801.0836). The null is re-imposed not by
   denying the mean-field crossing but by the order parameter being a CONTINUOUS U(1)
   phase, for which curvature frustration applies; this is a different wall than
   H_032-035, reached independently.
2b. **`realized_ratio = 0.0` is the bulk continuous-XY glass result, not a tuned knob.**
   The honest-null is set by the literature (no finite-T order), not chosen to make F2
   trigger; any value `<= 1.2` gives the same verdict, so it is threshold-insensitive.
3. **`T_BKT/J = 0.893` is the standard square-XY value** (Tobochnik-Chester 1979), used
   only as the matched-J denominator; the verdict does not depend on its precise value.
4. **Boundary fraction (F5) alone is NOT the decisive killer.** With the naive boundary
   coordination correction, {5,4} (z=4) still gives a corrected ratio ~1.83 > 1.7 — so
   the all-boundary argument by itself does not close every tiling. The genuinely
   decisive null is the continuous-XY curvature-frustration result (C), not (B); (B) is
   the mechanism/finite-size caveat, honestly NOT over-claimed as sufficient.
5. **Curvature frustration is itself the bill.** Even granting the optimistic
   mean-field reading, the same negative curvature that would beat vortex entropy
   injects geometric frustration that glassifies the continuous phase — a no-free-lunch
   exactly parallel to the prior nulls (pinning-that-helps suppresses pairing;
   donation-that-adds-D_s softens via Leggett).
6. **No claim hyperbolic SC is impossible or uninteresting** — only that connectivity
   geometry does NOT lift the ambient continuous-phase ceiling past 164 K at matched
   `D_s`; a real hyperbolic host (circuit-QED hyperbolic lattices, certain MOFs) remains
   a fine platform for OTHER physics. Target unmet: 293 K @ 1 atm, equilibrium bulk.
7. **{7,3} and {5,4} are representative**; the exponential-growth / O(1)-boundary
   property and curvature frustration hold for ALL hyperbolic {p,q} with
   `(p-2)(q-2)>4`, so the conclusion is tiling-robust, not specific to these two.

## Cross-links

- Frozen wall: PR#40 (spin-fluctuation / phase-stiffness ~134-164 K ceiling; `T_BKT=(pi/2)D_s`).
- Sibling escape-class cards (same 2026-06-25 sweep / wave-1): H_032 (multiband donation),
  H_033 (Z2/Goldstone universality, z=2 dynamics), H_034 (eta-pairing ODLRO),
  H_035 (Amperean current glue) — all confirm-wall. This card attacks the **"order traps"**
  half of the meta-law via connectivity-geometry (a lever none of H_032-035 touched) and
  also confirms.
- Harness: `tool/rtsc_harness.py` (`Falsifier`, `evaluate`).
- Triage source: `state/sf_seed_full_triage_2026_06_25/triage.md` ("Genuinely-new
  in-silico escapes" -> "Bethe-Ceiling Lattice").

## Verdict (VERBATIM run stdout — no LLM self-judge)

```
==============================================================================
H_037 — Bethe-Ceiling Lattice (negative-curvature stiffness ladder)
cluster: connectivity-geometry universality (Mermin-Wagner fails)
premise violated: CRYSTALLINE (flat/Euclidean host) -> hyperbolic {p,q}
==============================================================================
square XY  T_BKT/J (Tobochnik-Chester)   : 0.893
square BKT T_c at the wall band          : 134-164 K
------------------------------------------------------------------------------
(A) OPTIMISTIC discrete-clock mean-field estimate  kT_c^MF=(z/2)J :
   {7,3} z=3 : MF/BKT ratio = 1.680   (naive escape number)
   {5,4} z=4 : MF/BKT ratio = 2.240
   -> the DISCRETE clock variable does cross mean-field (arXiv:0801.0836)
------------------------------------------------------------------------------
(B) shell growth mu and boundary fraction f_bd=(mu-1)/mu :
   {7,3} mu = 2.618034 (= phi^2)   f_bd = 0.618034 (= 1/phi)
   {5,4} mu = 3.732051        f_bd = 0.732051
   -> O(1) of all vertices are on the boundary at EVERY tractable size;
      a hyperbolic graph is all-boundary, so a 'bulk mean-field' lift is
      never actually reached -> boundary-dominated finite-size effects.
------------------------------------------------------------------------------
(C) DECISIVE honest-null — CONTINUOUS U(1) Cooper-pair phase (the real OP):
   continuous-XY finite-T order on hyperbolic surface : False
   (Baek-Minnhagen PRE 80 011133 2009: curvature frustration -> zero-T glass;
    heptagonal-XY open-boundary MC: absence of any transition incl. BKT)
   realized T_c^hyperbolic / T_c^square (continuous OP): 0.000
   honest-null threshold (escape FAILS if ratio<=1.2)  : 1.2
------------------------------------------------------------------------------
  [PASS   ] F1_discrete_clock_meanfield_estimate_is_real
  [TRIGGER] F2_HONEST_NULL_continuous_phase_lifts_bulk_Tc
  [TRIGGER] F3_escape_ratio_ge_1p7_realized
  [TRIGGER] F4_tc_exceeds_wall_band
  [TRIGGER] F5_lift_is_bulk_not_boundary_artifact
------------------------------------------------------------------------------
honest-null (F2) PASS (continuous phase lifts bulk T_c) : False
escape (F3) PASS (ratio >= 1.7 realized)                : False
falsifiers_pass : 1/5
is_green        : False
absorbed        : False
VERDICT         : confirms-wall
==============================================================================
```