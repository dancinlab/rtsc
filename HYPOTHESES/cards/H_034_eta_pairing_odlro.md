# H_034 — eta-pairing ODLRO / dark-state rigidity

- **id**: H_034
- **slug**: eta-pairing-odlro
- **escape_class**: (c) different rigidity
- **status**: closed-negative (confirms-wall)
- **date**: 2026-06-25
- **is_green**: false
- **absorbed**: false
- **run**: `state/h_034_eta-pairing-odlro_2026_06_25/run.py` (stdlib-only, deterministic, byte-reproducible)

## Hypothesis (frozen pre-register)

Yang eta-pairing gives EXACT off-diagonal long-range order (ODLRO) that is distance-independent: the pair correlator `g(r) -> (N_eta/L)(1 - N_eta/L)` as `|i-j| -> inf`, with NO decay. The condensate rigidity is an algebraic eta-SU(2) property, NOT a phase stiffness — so there is no `rho_s` and therefore no `T_BKT = (pi/2) D_s` quantity to bound `T_c`. If that rigidity persisted at ambient EQUILIBRIUM it would sidestep the frozen ~134-164 K ceiling (PR#40). A Liouvillian / dark-state route is the proposed stabilizer.

## Why (mechanism + grounding)

The charitable premise is physically real: Yang eta-pairing eigenstates carry distance-independent ODLRO (Yang, PRL 63, 2144, 1989); the probe confirms `g(r)` has exact zero r-dependence (F1 PASS) — the (pi/2)D_s bound that walls classes (a)/(b) does not apply to the eta-eigenstate. But the rigidity lives on the wrong states: the eta-tower sits `~|U|` per pair above ground; the eta-eigenstates are exact ETH-violating quantum many-body scars (arXiv:2205.07235); every realization is non-equilibrium — heating-induced dissipation/drive NESS (arXiv:1811.12628, PRL 123 030603), photodoped Hubbard "T_c^eff" up to ~1400 K that is an effective temperature of a pumped NESS (arXiv:2602.17238), single-site Lindblad dark-state pumping (arXiv:2602.00452).

## Probe (closed-form)

Part A confirms `g(r)` r-independence (eta-SU(2) algebra). Part B (decisive null): the equilibrium Boltzmann weight of a macroscopic eta-condensate against the thermal sea is `exp(-n_pairs*|U|/kT)`. With `|U|=3 eV` and `n_pairs=100`, the weight at 293 K underflows to 0.0 (single-pair weight alone = 2.5e-52). The equilibrium temperature for an O(1) weight is `n*|U|/k ~ 3.5e6 K` (a drive temperature). Honest ambient-equilibrium eta `T_c` = 0 K.

## Falsifiers

- F1 algebraic_rigidity_distance_independent — PASS (premise real)
- F2 HONEST_NULL_survives_ambient_equilibrium (decisive) — TRIGGER (weight = 0.0)
- F3 equilibrium_Tc_exceeds_ceiling — TRIGGER (eta T_c = 0 K)
- F4 realizable_without_sustained_external_drive — TRIGGER (needs pump)
- F5 driven_Teff_is_true_ambient_Tc — TRIGGER (NESS effective-temp)

Decisive null F2 TRIGGERED with no margin -> CONFIRMS the wall.

## Honest limits

1. `|U|=3 eV` is representative, not per-material; conclusion is |U|-robust (any extensive condensate underflows at any ambient T), not tuned.
2. Thermodynamic-occupation argument, not a full Lindblad/Floquet sim; it bounds the EQUILIBRIUM phase and concedes the DRIVEN NESS exists.
3. `n_pairs=100` is mesoscopic; the bulk limit is even more decisive — this UNDER-states the null.
4. F1 premise granted in full: the (pi/2)D_s bound truly does not apply; the wall is re-imposed by thermal occupation — a DIFFERENT wall reached independently.
5. Out-of-domain: sustained photodoping / engineered dissipation is lab apparatus, not ambient 1-atm bulk; "T_c^eff ~1400 K" is an effective carrier temperature, not an equilibrium transition.
6. No claim driven eta-SC is impossible/useless — only that it misses the target (293 K @ 1 atm, ambient equilibrium bulk).
7. `1/e` threshold is generous and verdict is threshold-insensitive (weight = 0 to machine precision).

## Cross-links

PR#40 frozen wall; sibling sweep cards H_033 (Z2/Goldstone), H_035 (Amperean current glue); harness `tool/rtsc_harness.py`.

## Verdict (VERBATIM run stdout)

```
==============================================================================
H_034 — eta-pairing ODLRO / dark-state rigidity  (escape class (c))
==============================================================================
eta filling nu_eta                 : 0.5
ODLRO plateau g(inf)=nu(1-nu)      : 0.250000  (distance-independent=True)
Hubbard |U| (eta-tower gap/pair)   : 3.000 eV  (3000.0 meV)
single eta-pair eq. T (kT~U)       : 34813.6 K
Gibbs weight to add 1 pair @ 293 K : 2.501e-52
macro eta-ODLRO eq. weight @ 293 K : 0.000e+00  (n_pairs=100)
macro eta eq. 'T_c' (n*U/k)        : 3.481e+06 K  (drive T, not a transition)
AMBIENT-EQUILIBRIUM eta T_c        : 0.0 K  (no thermal phase @ 1 atm)
frozen wall ceiling band           : 134-164 K
driven-NESS T_c^eff (photodoped)   : up to 1400 K  (EFFECTIVE temp, pumped)
requires sustained external drive  : True  (out-of-domain)
------------------------------------------------------------------------------
  [PASS   ] F1_algebraic_rigidity_distance_independent
  [TRIGGER] F2_HONEST_NULL_survives_ambient_equilibrium
  [TRIGGER] F3_equilibrium_Tc_exceeds_ceiling
  [TRIGGER] F4_realizable_without_sustained_external_drive
  [TRIGGER] F5_driven_Teff_is_true_ambient_Tc
------------------------------------------------------------------------------
honest-null (F2) PASS (survives ambient eq.) : False
equilibrium-escape (F3) PASS                 : False
falsifiers_pass : 1/5
is_green        : False
absorbed        : False
VERDICT         : confirms-wall
==============================================================================
```