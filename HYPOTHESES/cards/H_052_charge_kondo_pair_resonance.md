# H_052 — Charge-Kondo / Pair-Resonance Lattice (a negative-U impurity band of preformed pairs)

- **id:** H_052
- **slug:** charge-kondo-pair-resonance
- **cluster:** spin-fluctuation / phase-stiffness ambient ceiling (`T_BKT = (pi/2)D_s`) — WITHIN-CLUSTER VARIANT
- **escape_class:** (c) different rigidity (electronic eV-scale charge-2e pair resonance, claimed glue-free / no quantum-metric ceiling)
- **date:** 2026-06-25
- **status:** closed-negative
- **verdict:** **confirms-wall**
- **is_green:** false · **absorbed:** false · **deterministic:** true (byte-equal ×2, sha `94c587dd…`)
- **run:** `state/h_052_charge-kondo-pair-resonance_2026_06_25/run.py`

## Frozen pre-register (BEFORE the run)

**Seed (triage "Genuinely-new in-silico escapes" #16).** A dense valence-skipper (Tl-O / Bi-O) lattice forms a charge-Kondo pair-resonance band of preformed charge-2e bosons. The escape **CLAIM** is that `T_c` is set by the eV-derived electronic hybridization-coherence width `Gamma` (`T_c ~ Gamma/k_B`, no quantum-metric ceiling), NOT by the 7.4 meV spin-fluctuation stiffness; with binding `>> Gamma` so pairs never break, claiming `Gamma > ~14 meV` (`>164 K`).

**The variant's twist.** Attacks the *rigidity/condensation* side with a different source — an electronic, eV-scale charge-Kondo pair resonance of preformed charge-2e bosons — claimed to set `T_c` at the hybridization width `Gamma` rather than the SF stiffness.

**HONEST-NULL (DECISIVE).** A preformed-pair condensate's `T_c` is the boson superfluid stiffness `k_B T_c = C·n_B^(2/3)·t_B` (Alexandrov bipolaron-BEC, arXiv:2210.14236), with `m_BP* = hbar^2/(2 t_B a^2)` set by `t_B = z·t_imp^2/|U|`. Deep binding `|U|` (pairs preformed/unbreakable) forces `|U| >> z·t_imp` → heavy bipolaron (`t_B` suppressed), AND the dilute formula caps at the quarter-filled charge-order/Mott trap (the seed's own "inter-site charge order before Gamma reaches 14 meV"). So `T_c` collapses onto the phase-stiffness line below the wall.

**Empirical ceiling.** The two real negative-U skipper SCs — Pb₁₋ₓTlₓTe (`T_c ≤ 1.5 K`, PRL 94 157002 / PRL 108 036402) and best-ever K-BaBiO₃ (`T_c ~ 30 K`, Nature 332 814) — are both far below 134 K despite eV binding. Probe calibrates the closed form on BOTH (no free fit).

**Violated premise.** single-particle-coherent / equilibrium carriers (carriers = preformed real-space pairs / bipolarons).

## Verbatim run verdict (no LLM self-judge)

```
[see verbatim_stdout — VERDICT: confirms-wall; falsifiers_pass = 4/5; best_Tc=34.8086 K; margin -99.1914 K]
```

**falsifiers_pass = 4/5.** F1 (decisive honest-null) NOT triggered → confirms-wall. F4 is the one FAIL (steel-man at n_B=0.25 gives 34.8 K, marginally above the 30 K BaBiO₃ record at n_B=0.20) — expected over-reach that only deepens the conclusion (still 3.85× below the wall).

## Falsifiers (≥4; honest-null decisive)

1. **F1 `honest_null_preformed_pair_condensation_clears_wall` (DECISIVE) — NOT triggered (PASS).** Best valid condensation T_c = 34.8 K, −99.2 K below the 134 K wall (3.85× deficit).
2. **F2 `condensation_reaches_gamma_target_14meV` — NOT triggered (PASS).** k_B·T_c(best)=3.0 meV < 14 meV.
3. **F3 `pair_hopping_not_binding_suppressed` (no-free-lunch) — NOT triggered (PASS).** t_B=1.14 meV << |U|=4000 meV (deep binding → heavy bipolaron).
4. **F4 `condensation_exceeds_best_real_skipper_SC` — TRIGGERED (FAIL, expected steel-man overshoot).** 34.8 K marginally > 30 K record; does not affect verdict.
5. **F5 `condensation_reaches_room_T` — NOT triggered (PASS).** 34.8 K << 293 K.

## Honest limits (≥5)

1. Mechanism is REAL (Tl:PbTe, K-BaBiO₃ are genuine negative-U skipper SCs) — fails by no-free-lunch, not inertness.
2. Closed form calibrated, not free-fit, and reality-consistent (reproduces 1.50 K and 30.00 K exactly). An earlier draft mis-used the conduction bandwidth (250 meV) instead of the narrow impurity band (~20 meV), over-predicted Tl:PbTe by ~290× and fabricated a fake escape — caught by the empirical-sanity check and corrected.
3. `C_BEC=6.62` and `m_BP*=hbar²/(2 t_B a²)` are the single-band lattice charged-Bose-gas result; a much lighter intersite bipolaron would reopen — but a light bipolaron is no longer "preformed/unbreakable," breaking the seed's own premise.
4. 2-site ED is a minimal pair-hopping probe; full DMFT would land at-or-below 34.8 K, deepening the deficit.
5. `n_B_max=0.25` (quarter-filled trap) is steel-manned high; a lower trap shrinks T_c further.
6. The Kondo-insulating branch of the null (T_c→0) is not separately computed; it only strengthens the verdict.
7. No fabricated citations; absorbed=false.

## Conclusion

A charge-Kondo / negative-U skipper lattice of preformed charge-2e bosons is a genuinely distinct electronic eV-scale escape, but a preformed-pair condensate's `T_c` is its boson superfluid stiffness, and deep binding makes the bipolaron heavy (`t_B=z t_imp²/|U|`) while the charge-order trap caps density. Calibrated on both real skipper SCs (reproduced exactly), best steel-manned `T_c=34.8 K` lands −99.2 K below the 134 K wall (3.85× deficit); the seed's `Gamma/k_B` claim over-states by 83×. The deepest measured negative-U skipper SC (BaBiO₃, 30 K) IS the empirical confirmation. **Confirms the wall.** is_green=false, absorbed=false.

## Refs

- arXiv:2210.14236 — `T_c≈3.31 ρ^(2/3)/m_BP*`, dilute-validity ceiling
- arXiv:1201.1400 — bipolaron bandwidth `t_B=z t²/|U|`
- PRL 94 157002 (2005); PRL 108 036402 (2012) / arXiv:1109.1824 — Tl:PbTe `T_c≤1.5 K`
- PRB 98 184506 (2018) / arXiv:1808.07213 — mixed-valence Tl negative-U
- Nature 332 814 (1988) — K-BaBiO₃ `T_c~30 K`
- AAPPS Bull. 32 33 (2022) DOI 10.1007/s43673-022-00056-1 — narrow skipper band
- Nature 374 434 (1995) — Emery-Kivelson `T_θ=(π/2)D_s`