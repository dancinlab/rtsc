---
id: H_014
slug: competing-order-threshold
title: The room-T electronic glue drives a competing order (SDW) BEFORE superconductivity — under a toy Stoner/RPA multi-channel model the +@ architecture fails the competing-order gate (SDW unstable at U*=1.0 vs SC at U*=2.22; no SC-leading window)
domain: rtsc
status: closed-negative
exploration_method: competing-order check — the dominant open risk (H_004 L2 / H_011 L3)
verification_method: W1 (pre-register frozen) + W2 (falsifier-5) + W3 (deterministic) + W5 (honest-limits-6)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
since: 2026-06-25
compute: fleet lane (rtsc-fleet-orthogonal-levers)
---

# H_014 — competing-order threshold (rtsc)

## Hypothesis

The dominant open risk of the whole +@ chain (H_004 L2, H_011 L3): a ~349 meV electronic/bosonic
glue strong enough to pair may instead drive a COMPETING ORDER (SDW / CDW / phase separation)
BEFORE superconductivity. At the coupling room-T SC needs, is the SC channel the leading
instability, or does a particle-hole order diverge first?

## Why

- The same strong interaction that makes the glue feeds particle-hole channels (SDW/CDW). On a
  flat band with high DOS and nesting, the particle-hole susceptibility is large — SDW/CDW often
  pre-empt SC. This is the standard failure mode of flat-band / high-DOS pairing.
- A multi-channel Stoner/RPA threshold (whichever S_c = g_c·χ_c crosses 1 first leads) is the
  honest minimal test.

## Falsifiers (≥5 — pre-registered)

- **F1_sc_window_exists**: PASS = an SC-leading interaction window exists (EXPECTED TO FAIL).
- **F2_sc_leads_competitor**: PASS = SC crosses before the leading particle-hole channel.
- **F3_roomt_relaxed_inside**: PASS = the room-T glue maps inside the SC-leading window.
- **F4_window_has_width**: PASS = the SC-leading window has nonzero width.
- **F5_sdw_not_first_mover**: PASS = SDW is not the first instability.

## Honest Limits (≥6)

- **L1 (TOY Stoner/RPA, fixed constants)**: nesting η=0.85, glue fraction f_glue=0.45, κ_ps=0.55,
  V/U=0.3 are chosen, not computed — the 0/5 verdict is CONDITIONAL on them. Strong nesting (0.85)
  deliberately favors SDW; a poorly-nested flat band would shift U*_SDW up. This is a serious
  WARNING, not a proof.
- **L2 (no momentum structure)**: a single-χ-per-channel model omits the q-dependence that can
  detune nesting (e.g. incommensurate fillings, frustration) — the main escape route untested.
- **L3 (mean-field thresholds)**: Stoner crossing ignores fluctuations that suppress the
  particle-hole order more than SC (or vice versa).
- **L4 (the glue→U map is schematic)**: Ω_eff(U)=f_glue·U links the +@ glue to the Hubbard U by a
  fixed fraction; a different coupling geometry changes the mapping.
- **L5 (negative is a measured threat, not a terminal ceiling)**: per break-walls, this classifies
  the wall as a REAL competing-order risk to be escaped (suppress nesting / frustrate / detune),
  NOT a proof that the +@ architecture is impossible.
- **L6**: `absorbed=true` still requires accredited transport + Meissner + measured H_c2 / T_c.

## Cross-Links

- **gates**: H_004 / H_005 / H_007 / H_011 (the electronic-glue stacks this competing-order check threatens).
- **escape routes (untested)**: poorly-nested / frustrated flat band (L1/L2) — the next probe if pursued.

## Verdict

**🟡 MODEL-PROBE → CLOSED-NEGATIVE (competing order pre-empts SC, under this toy).** Verbatim stdout
(`state/h014_competing_order_threshold_2026_06_25/run_h014.py`):

```
=== H_014 competing-order threshold — does the room-T glue drive CDW/SDW/PS before SC? ===
  --- channel Stoner thresholds (smallest U with S_c >= 1) ---
    SC  (particle-particle, glue) : U* = 2.2222
    SDW (particle-hole, spin)     : U* = 1.0
    CDW (particle-hole, charge)   : U* = 2.9412
    PS  (phase separation)        : U* = 3.1182
  leading particle-hole competitor: SDW at U* = 1.0
  SC leads competitor             : False
  SC-leading window               : [2.2222, 1.0]  width=0.0  exists=False
  room-T glue mapped to U         : bare U=1.0  relaxed U=0.543
  room-T BARE/RELAXED inside window: False / False
  falsifiers_pass = 0/5
VERDICT: competing order PRE-EMPTS SC at the room-T glue demand — the +@ architecture fails the
  competing-order gate under this toy (CLOSED-NEGATIVE on this lever).
```

- **structural_finding**: under a toy Stoner/RPA multi-channel model, SDW goes unstable at U*=1.0
  while SC needs U*=2.22 — the particle-hole (spin) channel diverges FIRST, so there is NO
  SC-leading window and the room-T glue (U≈0.5–1.0) sits at/below the SDW threshold. **The +@
  architecture's biggest assumed risk is realized: the electronic glue drives SDW before SC.**
  This is the dominant open question the whole closed-form chain now points at — escapable only by
  suppressing nesting (L1/L2), which is the next real probe. Honest negative (no tune-to-green).
- **record**: `state/h014_competing_order_threshold_2026_06_25/result.json`.
