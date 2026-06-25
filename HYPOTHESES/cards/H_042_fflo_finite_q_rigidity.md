# H_042 — FFLO Stiffness Bypass: finite-Q phase rigidity from the depairing tensor

- **id**: H_042
- **slug**: fflo-finite-q-rigidity
- **escape_class**: (c) different rigidity — finite-Q (violates the Q=0 premise)
- **cluster**: finite-Q rigidity (violates Q=0 premise)
- **status**: closed-negative (confirms-wall)
- **date**: 2026-06-25
- **is_green**: false
- **absorbed**: false
- **run**: `state/h_042_fflo-finite-q-rigidity_2026_06_25/run.py` (stdlib-only, deterministic, byte-reproducible)

## Which of the freeze's 5 premises this violates

The frozen geometric-stiffness verdict (PR#40) was measured on **Q=0** / single-particle-flat / crystalline / quasiparticle-coherent / equilibrium hosts. This card deliberately violates exactly ONE: the **Q=0 premise** — it asks whether a *finite-Q* FFLO/LO condensate carries a phase rigidity that escapes the dilute Q=0 superfluid-weight ceiling. None of the wave-1 escapes (H_032-035) are finite-Q.

## Hypothesis (frozen pre-register)

A finite-Q FFLO/LO condensate has `Delta(r) ~ cos(Q.r)`, `Q ~ 2*delta_kF` set by FS mismatch `delta`. Its GL phase-stiffness is a TENSOR. The seed claims the modulation-direction component `D_s^||` (from `d^2F/d(grad theta)^2` about the LO saddle) is set by FS-mismatch/bandwidth `~ delta*(bandwidth)`, GROWS with `delta`, and can exceed `(pi/2)*D_s^{Q=0}`, so melting is governed by the large sliding stiffness and `T_c` clears 134-164 K.

## Why (mechanism + literature grounding)

The escape premise is the magnitude claim; grounded LO Goldstone literature contradicts it: at T=0 the LO longitudinal stiffness has the SAME FORM as a uniform SC superfluid density, not enhanced (Samokhin arXiv:1003.2194). The TRANSVERSE stiffness is the soft (smectic) one and vanishes in the FF limit; the anisotropy diverges because `D_perp->0`, not because `D_par` blows up (Radzihovsky-Vishwanath arXiv:1102.4903). FFLO nucleates only below `0.56*T_c^{BCS}` (Larkin-Ovchinnikov 1964; Fulde-Ferrell 1964), and `T_c` is itself Pauli-suppressed (Clogston/Chandrasekhar) — the `delta` that opens the window caps the pairing.

## Probe (small deterministic computation)

`run.py`: clean tight-binding host (`e(k)=-2t(cos kx+cos ky)`, `W=8t=2.4 eV`, `Delta0=20 meV`); GL stiffness tensor about the LO saddle via the microscopic gradient kernel — `D_s^||=D_s0*R_par`, `R_par=sqrt(1-(delta/delta_c)^2)` (gapped FS fraction, Clogston `delta_c=Delta0/sqrt(2)`); `D_s^perp=D_s0*R_par^2` (smectic-soft); FFLO onset cap `T_LO=0.56*T_c^{BCS}(delta)` Pauli-suppressed. Q=0 rigidity anchored CHARITABLY to 164 K (top of frozen band). Sweep delta over the whole window. escapes-wall ONLY if F1 AND F2 (honest-nulls) PASS with margin AND F4 PASS — no LLM self-judge.

## Verbatim run verdict

```
H_042  FFLO Stiffness Bypass — finite-Q phase rigidity from the depairing tensor
max R_par over window               = 1.0000  (at delta=0.000 meV)
best D_s^|| (modulation direction)  = 164.00 K   [vs Q=0 anchor 164.0 K]
max FFLO onset T = 0.56*Tc_BCS      = 73.85 K
  [FAIL] honest_null_N1_Ds_par_not_above_Q0
  [FAIL] honest_null_N2_onset_T_below_ceiling
  [FAIL] transverse_softens_not_long_hardens
  [FAIL] joint_escape_unsatisfiable
  [PASS] window_bounded_guard
falsifiers_pass                        = 1/5
VERDICT: confirms-wall
```

## Falsifiers (F1 & F2 decisive honest-nulls)

| # | name | PASS criterion | result |
|---|------|----------------|--------|
| F1 | `honest_null_N1_Ds_par_not_above_Q0` | DECISIVE: `D_s^||` exceeds `D_s^{Q=0}` somewhere | **FAIL** (triggered: max R_par=1 at delta=0; null holds) |
| F2 | `honest_null_N2_onset_T_below_ceiling` | DECISIVE: FFLO onset T reaches 134 K | **FAIL** (triggered: max onset T=73.85 K; null holds) |
| F3 | `transverse_softens_not_long_hardens` | transverse stiffness NOT the soft one | **FAIL** (triggered: D_s^perp<=D_s^||) |
| F4 | `joint_escape_unsatisfiable` | both D_s^||>Q0 AND melting T>134 K | **FAIL** (triggered: neither holds) |
| F5 | `window_bounded_guard` | LO window bounded, R_par<=1 | **PASS** (kernel physical) |

## Honest limits

1. Toy gradient kernel, not a self-consistent material BdG `Delta(r)` solve; verdict does not hinge on prefactor (nulls cap structurally).
2. Single-band Clogston Pauli model for the window; orbital/multiband/strong-coupling not included (do not flip sign of R_par-1 or lift 0.56 cap).
3. The 0.56 onset factor is the clean-limit tricritical value; disorder/dimensionality shift the number but always to a fraction <1 of T_c^{BCS}.
4. Anchor charity: host Q=0 rigidity anchored to 164 K (top of band); real geometric flat-band D_s^{Q=0} is 1-8 K, so the true margin is far larger and the null even safer.
5. Probe uses the LO (largest-longitudinal) branch; FF branch has an identically vanishing transverse stiffness and no advantage — charitable choice.
6. Not a full finite-T anisotropic BKT flow; since D_s^|| is bounded by D_s^{Q=0} and one Goldstone is smectic-soft, a BKT flow can only reduce the melting T.
7. delta treated as a free knob; in a real host it is bounded by orbital depairing and normal-state instabilities — additional constraints that only tighten the null.

## Verdict

**confirms-wall.** The finite-Q FFLO/LO condensate does NOT beat the dilute Q=0 superfluid weight: `D_s^||` has the same form as the uniform superfluid density and only decreases with mismatch (max R_par=1 at delta=0), the anisotropy is the transverse smectic stiffness collapsing, and FFLO nucleates only below `0.56*T_c^{BCS}` (max 73.85 K, far below 134-164 K). Both honest-null prongs triggered by grounded physics (Samokhin arXiv:1003.2194; Radzihovsky-Vishwanath arXiv:1102.4903; Larkin-Ovchinnikov 1964). A valuable closed-negative: the Q=0-premise violation is settled in-silico and the wall holds. `is_green=false`, `absorbed=false`; no material claimed to BE an RTSC.