---
id: H_010
slug: topdown-lever-count
title: TOP-DOWN lever-count scan — stripping levers from the full stack reveals that MORE levers means ACHIEVABILITY, not redundancy; 4 is the minimal achievable count (the 3D lever crosses the achievable-glue line, the connector is structural)
domain: rtsc
status: model-probe
exploration_method: top-down count scan (the user's pivot: "we're going bottom-up; come down top-down on the count, we might discover something")
verification_method: W1 (pre-register frozen) + W2 (falsifier-4) + W3 (deterministic) + W5 (honest-limits-5)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
since: 2026-06-25
---

# H_010 — top-down lever-count scan (rtsc)

## Hypothesis

H_007 built the stack BOTTOM-UP (1→2→3 levers). Going TOP-DOWN — starting from the full stack
and REMOVING levers — reveals a different structure: each removal RAISES the per-lever demand,
so the question is not "what's the minimal set" but "what's the minimal **achievable** count".
The claim: the full 4-lever stack {geometry, connector, glue, 3D} is the *minimal achievable*
count — every removal pushes the glue demand over a sub-eV achievability ceiling or collapses
the import. **More levers is the mechanism for achievability, not redundancy.**

## Why

- Bottom-up shows T_c rising with count; it does NOT show whether a lever is removable. Top-down
  does — strip each and test whether room-T survives *achievably*.
- The deficit is ~5×; distributing it over more levers lowers each lever's individual demand
  below what a real material can supply. This inverts the usual "fewer parts is better" intuition.

## Predictions

- **H10.1**: the full 4-lever stack's glue demand (~349 meV) is under the achievable ceiling (~500 meV).
- **H10.2**: dropping the 3D lever pushes the demand over the ceiling (~643 meV) — 3D crosses the line.
- **H10.3**: dropping the connector collapses the import (wall) — connector is structural.

## Variables

- **lever set**: {geometry, connector, glue, 3D} and its sub-stacks
- **achievable glue ceiling**: 500 meV (sub-eV electronic glue plausible; eV+ exotic)

## Run Protocol

- deterministic, stdlib only, $0 mac local
- tools: `tool/rtsc_harness.py` (`omega_for_stacked_tc`, `THREED_TC_LEVER`)
- run: `python3 state/h010_topdown_lever_count_2026_06_25/run_h010.py`
- record: `state/h010_topdown_lever_count_2026_06_25/result.json`

## Criteria

- **verdict_rule**: MORE-LEVERS-IS-ACHIEVABILITY = the full count is achievable, every single
  removal is not, and the minimal achievable count equals the full count.

## Falsifiers (≥4 — pre-registered)

- **F1_full_achievable**: PASS = the 4-lever stack's glue demand is under the ceiling.
- **F2_3d_crosses_line**: PASS = without 3D the demand exceeds the ceiling (3D is load-bearing, not padding).
- **F3_connector_structural**: PASS = without the connector the import collapses (unachievable).
- **F4_frontier_at_full**: PASS = the minimal achievable count is the full 4.

## Honest Limits (≥5)

- **L1 (achievable ceiling is a chosen line)**: 500 meV is a defensible "sub-eV electronic glue"
  order, but the exact achievability boundary is itself uncertain (L2 of H_004) — moving it
  shifts which count crosses. The *structure* (more levers → lower demand) is robust; the exact
  crossing count is ceiling-dependent.
- **L2 (levers assumed multiplicative & independent)**: same as H_007 L2 — a real 3D
  heterostructure couples 3D coordination, connector, and glue; the clean per-lever demand split
  may not hold.
- **L3 (only 4 levers enumerated)**: topology (B7) and fractionalization (S5) are un-modeled
  orthogonal levers; adding them would lower the demand further (more achievability), not less —
  consistent with the finding but untested.
- **L4 (achievability ≠ realization)**: "achievable glue demand" means a material *could*
  supply it, NOT that a synthesized stack does. Each lever still carries its own bill (interface
  L2, competing order H_004 L2, band-touching H_006).
- **L5**: `absorbed=true` still requires accredited transport + Meissner + measured H_c2 / T_c.

## Cross-Links

- **complement**: H_007 (bottom-up count scan — same levers, opposite direction).
- **levers**: H_003/H_009 (connector) · H_004/H_008 (glue) · H_006 (3D).

## Verdict

**🟡 MODEL-PROBE → TOP-DOWN DISCOVERY: MORE LEVERS = ACHIEVABILITY, NOT REDUNDANCY.** Verbatim
stdout (`state/h010_topdown_lever_count_2026_06_25/run_h010.py`):

```
=== H_010 TOP-DOWN lever-count scan — strip from the full stack ===
  achievable glue ceiling = 500.0 meV (sub-eV electronic glue)
  3D lever (real) = 1.84x
  count  lever set                       glue demand   achievable?
    4    geo+connector+glue+3D              349.3 meV   YES
    3    geo+connector+glue (drop 3D)       642.7 meV   no
    3    geo+glue+3D (drop connector)      inf (wall)   no
    2    geo+glue (drop connector+3D)      inf (wall)   no
  minimal ACHIEVABLE count = 4
  falsifier F1_full_achievable      : PASS
  falsifier F2_3d_crosses_line      : PASS
  falsifier F3_connector_structural : PASS
  falsifier F4_frontier_at_full     : PASS
  falsifiers_pass = 4/4
VERDICT: TOP-DOWN DISCOVERY — MORE LEVERS = ACHIEVABILITY, NOT REDUNDANCY (4 is the minimal achievable count)
```

- **structural_finding**: top-down inverts the intuition — you cannot strip any lever and stay
  achievable. The 3D lever is what carries the glue demand from an exotic 643 meV under the
  sub-eV achievability line (349 meV); the connector is structurally load-bearing (without it the
  +@ division-of-labor collapses to the H_001 single-host wall). The deficit is paid by
  *distributing* it across more levers, so each lever's individual requirement becomes
  material-achievable. The discovery the user predicted: count is not overhead — it is the
  achievability mechanism.
- **record**: `state/h010_topdown_lever_count_2026_06_25/result.json`.
