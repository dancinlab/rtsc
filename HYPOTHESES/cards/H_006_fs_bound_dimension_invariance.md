---
id: H_006
slug: fs-bound-dimension-invariance
title: The quantum-geometry lever (∫tr g) is dimension-invariant — going to 3D/synthetic dimension does NOT relax the two-lever wall
domain: rtsc
status: model-probe
exploration_method: E6 (SF abstract brainstorm F2 — the FRAME lens; see state/sf-abstract-brainstorm.md)
verification_method: W1 (pre-register frozen) + W2 (falsifier-5+) + W3 (deterministic) + W5 (honest-limits-5+)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-24
since: 2026-06-24
---

# H_006 — Is the FS two-lever geometry lever dimension-invariant? (rtsc)

## Hypothesis

The quantum-geometry lever of the two-lever wall (H_001) — the integrated trace of the
Fubini-Study metric, ∫tr g — is **dimension-invariant** (capped, independent of spatial
dimension). If true, moving the flat band to 3D or a synthetic dimension does NOT add
geometry, so the dimension-FRAME bypass (brainstorm F2 / B5) is closed and the wall is a
real (frame-invariant) ceiling.

## Why

- The SF brainstorm's grand synthesis says a wall is a REAL ceiling iff it is frame-invariant;
  the single most testable frame is dimension. This card runs that test at toy level.
- The trace of the metric sums diagonal components; whether it stays capped or grows with the
  number of geometric directions is the crux.

## Predictions

- **H6.1**: ⟨tr g⟩ is flat across dimension (ratio ⟨tr g⟩(d=3)/⟨tr g⟩(d=1) ≈ 1) → invariant.
- **H6.2 (the alternative)**: ⟨tr g⟩ grows with dimension → extensive → bypass NOT closed.

## Variables

- **axis1_dim**: [1, 2, 3, 4] (separable winding directions)
- **axis2_model**: separable 2-level winding · non-separable 2D Dirac (m=1.0)

## Run Protocol

- deterministic: BZ finite-difference of the gauge-invariant 2-level FS metric g = ¼ ∂n̂·∂n̂.
- tool: tool/rtsc_harness.py (quantum_metric_trace_separable, quantum_metric_trace_2d_dirac).
- record: state/h006_fs_dimension_scan_2026_06_24/run_h006.py + result.json.
- cost: $0 (mac local, stdlib only).

## Criteria

- **C1**: separable scan matches the closed form 0.25·d within 5% (numerics valid).
- **C2**: non-separable 2D metric is finite and positive (metric well-defined).
- **verdict_rule**: DIMENSION-INVARIANT (hypothesis SUPPORTED) if growth ratio < 1.1;
  DIMENSION-EXTENSIVE (hypothesis REFUTED, at toy level) if it grows.

## Falsifiers (≥5 — pre-registered)

- **F1**: ⟨tr g⟩ flat across dim (ratio < 1.1) → dimension-invariance SUPPORTED (wall is a real ceiling).
- **F2**: ⟨tr g⟩(d=3)/(d=1) ≥ 1.5 → invariance REFUTED, geometry lever is dimension-extensive.
- **F3**: separable scan deviates from 0.25·d by > 5% → numerics broken, halt (no claim).
- **F4**: non-separable 2D metric ≤ 0 → metric ill-defined, halt.
- **F5**: a real 3D flat-band ED (deferred) contradicts the toy trend → toy is unrepresentative, reopen.
- **F6**: post-hoc edit to the verdict_rule threshold → pre-register violation.

## Honest Limits (≥5)

- **L1**: TOY model — a canonical 2-level winding band, NOT a real material. This is a structural
  seed, not a physics discovery.
- **L2**: computes the GEOMETRY lever (∫tr g) ONLY — it does NOT compute the coupling scale Ω, so the
  full two-lever trade-off (geometry vs Ω) is NOT tested here. Ω may co-scale with dimension.
- **L3**: the separable construction is d independent winding directions; a real 3D flat band is not
  literally separable.
- **L4**: the real verdict requires 3D / synthetic-dimension flat-band exact diagonalization with the
  actual quantum metric (src/ ED tools on a pod) — deferred.
- **L5**: this does not flip H_001's closed-negative ruling; it only tests one bypass axis (dimension).
- **L6**: absorbed=true still requires accredited 4-probe transport + Meissner + measured H_c2 / T_c.

## Cross-Links

- **brainstorm**: state/sf-abstract-brainstorm.md (F2 + grand synthesis; orthogonal seeds S5, O2).
- **parent wall**: cards/H_001_flatband_twolever_wall.md (the two-lever wall this probes).
- **tool**: tool/rtsc_harness.py · run: state/h006_fs_dimension_scan_2026_06_24/run_h006.py

## Verdict

**🟡 MODEL-PROBE → DIMENSION-EXTENSIVE (toy)** — in this toy, the geometry lever GROWS linearly
with dimension (⟨tr g⟩ = 0.25·d), so the dimension-invariance hypothesis is REFUTED at toy level
and the dimension-FRAME bypass is NOT closed. This is a structural signal, not a real-material result.

```
=== H_006 FS two-lever bound — dimension scan (TOY model, real computation) ===
  separable d=1:  <tr g> = 0.2500   (closed-form 0.25*d = 0.2500)
  separable d=2:  <tr g> = 0.5000   (closed-form 0.25*d = 0.5000)
  separable d=3:  <tr g> = 0.7499   (closed-form 0.25*d = 0.7500)
  separable d=4:  <tr g> = 0.9999   (closed-form 0.25*d = 1.0000)
  non-separable 2D Dirac:  <tr g> = 0.2268
  growth ratio <tr g>(d=3)/(d=1) = 3.000
  closed-form deviation = 0.0001
  falsifier F1_dimension_invariant  : PASS
  falsifier F3_numerics_broken      : PASS
  falsifier F4_metric_ill_defined   : PASS
VERDICT: DIMENSION-EXTENSIVE (toy: geometry lever grows with dim)
NOTE: toy 2-level model only — computes the GEOMETRY lever, not coupling Omega;
      real verdict needs 3D flat-band ED with the actual quantum metric (src/, pod).
```

- **reading**: F1_dimension_invariant PASS = the falsifier did NOT fire (growth=3.0, not <1.1) =
  invariance is REJECTED; the lever is extensive. F3/F4 PASS = numerics valid + metric well-defined.
- **so what**: the geometry lever is NOT 2D-capped in the toy → the dimension bypass survives, worth a
  real 3D flat-band ED. It does NOT prove the two-lever WALL breaks (Ω not tested — L2).
- **follow-on**: real 3D ED (src/ + pod) to compute geometry AND Ω vs dimension together.
