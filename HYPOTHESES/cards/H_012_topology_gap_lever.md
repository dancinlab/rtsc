---
id: H_012
slug: topology-gap-lever
title: A topology/symmetry-protected pairing gap is NOT an orthogonal 5th room-T lever — it buys only pairing amplitude, the room-T stack is phase-stiffness-limited, so it collapses into the H_001 geometry lever
domain: rtsc
status: closed-negative
exploration_method: M2 FRAME (brainstorm seed B7) — buy the gap with topology instead of coupling strength
verification_method: W1 (pre-register frozen) + W2 (falsifier-5) + W3 (deterministic) + W5 (honest-limits-5)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
since: 2026-06-25
compute: fleet lane (rtsc-fleet-orthogonal-levers)
---

# H_012 — topology-protected gap as an orthogonal lever? (rtsc)

## Hypothesis

Brainstorm seed **B7 (M2 FRAME)**: buy the pairing gap with a symmetry/topology-protected
`Δ_topo` (a minimum pairing scale independent of coupling Ω) instead of with glue. Does it act
as an **orthogonal 5th lever** that relaxes the room-T glue demand below the 349 meV 4-lever
value (the way the real 3D lever did, ×1.84), or does it **collapse** into an existing lever?

## Why

- Flat-band SC is `Tc ~ min(T_amplitude, T_stiffness)`. The calibrated BKT band
  (Tc = 0.11·Ω_K/2.8) is a **stiffness** law; a protected gap pins only the **amplitude** (a
  gapped band with zero superfluid weight is an insulator, not a superconductor).
- The only stiffness a protected band can add is bounded by its Fubini-Study quantum metric —
  which IS the H_001 geometry lever.

## Predictions / Falsifiers (≥5 — pre-registered)

- **F1_topo_relaxes_omega**: PASS = a realistic gap lowers the room-T Ω demand (EXPECTED TO FAIL).
- **F2_topo_is_subthreshold**: PASS = a realistic (≤100 meV) gap caps amplitude below the stiffness ceiling.
- **F3_huge_gap_no_relax**: PASS = even a 2000 meV gap relaxes the Ω demand by nothing.
- **F4_collapse_to_geometry**: PASS = the added stiffness equals the FS quantum-metric (geometry lever).
- **F5_topo_alone_insufficient**: PASS = topology cannot carry room-T alone (needs ~140 meV gap > realistic).

## Honest Limits (≥5)

- **L1 (toy min(amplitude, stiffness) model)**: a generous strong-coupling gap→Tc ratio (2Δ/kTc≈11,
  most optimistic for topology) is used, so the collapse verdict is conservative. Not an Eliashberg solution.
- **L2 (amplitude/stiffness separation is schematic)**: a real flat band couples them; the clean split is a model.
- **L3 (assumes the room-T regime is stiffness-limited)**: true for the calibrated band; a different
  regime (very strong coupling, BEC) could re-weight — untested.
- **L4 (negative is a ruling, not impossibility)**: topology may help via a channel this toy omits (e.g.
  protecting the flat band against disorder, raising effective g).
- **L5**: `absorbed=true` still requires accredited transport + Meissner + measured H_c2 / T_c.

## Cross-Links

- **collapses into**: H_001 (geometry lever). **contrast**: H_006 (real 3D lever — a GENUINE orthogonal axis).

## Verdict

**🟡 MODEL-PROBE → CLOSED-NEGATIVE (collapse).** Verbatim stdout
(`state/h012_topology_gap_lever_2026_06_25/run_h012.py`):

```
=== H_012 B7 topology-gap lever — orthogonal 5th lever, or collapse? ===
  4-lever glue demand (H_010) baseline = 349.3 meV
  Delta_topo   amp ceiling   Omega req (room-T)   binding scale         relaxes 4-lever?
       0.0 meV  inf (no gap)          349.3 meV   stiffness(Omega)      no
     100.0 meV      208.9 K      inf (unreach)   amplitude(topo-gap-too-small)  no
    2000.0 meV     4177.4 K          349.3 meV   stiffness(Omega)      no
  any realistic (<=100 meV) gap relaxes Omega? : False
  topo stiffness == FS quantum-metric (geometry lever)? : True
  falsifier F1_topo_relaxes_omega     : FAIL
  falsifier F2_topo_is_subthreshold   : PASS
  falsifier F3_huge_gap_no_relax      : PASS
  falsifier F4_collapse_to_geometry   : PASS
  falsifier F5_topo_alone_insufficient: PASS
  falsifiers_pass = 4/5
VERDICT: CLOSED-NEGATIVE (honest) — the topology-protected gap is a PAIRING-AMPLITUDE lever only.
```

- **structural_finding**: topology is a pairing-amplitude lever; the room-T stack is
  phase-stiffness-limited, so a protected gap never relaxes the 349 meV demand and would only
  become the new bottleneck — and the only stiffness it could add is the FS quantum metric = the
  H_001 geometry lever. **Topology is NOT an orthogonal 5th axis; it collapses into geometry.**
  (F1 FAIL is the intended "does not relax" result — an honest closed-negative, not tune-to-green.)
- **record**: `state/h012_topology_gap_lever_2026_06_25/result.json`.
