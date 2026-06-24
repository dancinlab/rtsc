---
id: H_016
slug: competing-order-escape
title: Frustrating the nesting (η_nest sweep) lifts H_014's competing-order wall — below a critical η*≈0.45 (plausible for kagome/triangular hosts) SC becomes the leading instability, but the room-T amplitude axis stays uncleared
domain: rtsc
status: model-probe
exploration_method: break-walls continuation of H_014 (do not terminal on one nesting value) — frustration knob sweep
verification_method: W1 (pre-register frozen) + W2 (falsifier-5) + W3 (deterministic) + W5 (honest-limits-5)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
compute: fleet lane (verification)
---

# H_016 — competing-order escape: does frustrating the nesting let SC lead? (rtsc)

## Hypothesis

H_014 ruled competing order a wall using ONE strong nesting value (η_nest=0.85): the
particle-hole SDW channel (U*=1/(N·η_nest)) goes unstable before the SC pair channel
(U*=1/f_glue=2.22). break-walls forbids terminating on one axis value. **Hypothesis: a
frustrated / incommensurate flat band suppresses the nesting susceptibility (low η_nest), and
below a critical η_nest* SC becomes the LEADING instability** — without touching the
η-independent pair channel.

## Why

- Pairing (particle-particle) and density-wave (particle-hole) share the same interaction; the
  leading instability is whichever susceptibility diverges first. Frustration (triangular/kagome)
  lowers the particle-hole nesting peak, raising the SDW threshold while SC's stays put.

## Falsifiers (≥5 — pre-registered)

- **F1_escape_exists**: PASS = an SC-leading window opens somewhere on the η sweep.
- **F2_eta_critical_plausible**: PASS = η* sits above the pre-registered plausible-frustration floor (0.30).
- **F3_grid_matches_closed_form**: PASS = grid η* agrees with the closed form f_glue/N.
- **F4_reproduces_h014_at_strong_nesting**: PASS = at η=0.85 SDW still pre-empts (reproduces H_014).
- **F5_monotone_escape_boundary**: PASS = the escape boundary is monotone in η.

## Honest Limits (≥5)

- **L1 (toy Stoner/RPA, linear bookkeeping)**: η* from a single-χ-per-channel model; a full
  FS-resolved Lindhard / DMFT treatment could move η*.
- **L2 (the room-T AMPLITUDE axis is NOT cleared)**: this resolves only the leading-CHANNEL race
  (SC vs particle-hole). The relaxed room-T glue maps to U=0.543, BELOW the SC threshold 2.22 —
  so "room-T U inside SC window = False". The escape opens an SC-leading regime, NOT a
  room-T-magnitude pair. The strongest honest caveat.
- **L3 (η* is a model knob, not a measured nesting)**: 0.45 is a toy susceptibility ratio; a real
  frustrated host's effective nesting needs DFT/RPA computation.
- **L4 (plausibility floor 0.30 is pre-registered, not derived)**: kagome/triangular reach
  η~0.3–0.5 by lore; the exact value is host-specific.
- **L5**: `absorbed=true` still requires accredited transport + Meissner + measured H_c2 / T_c.

## Cross-Links

- **lifts the wall of**: H_014 (competing-order, η=0.85 CLOSED-NEGATIVE).
- **hands to**: a frustrated flat-band host (kagome/triangular) as a testable coordinate.

## Verdict

**🟡 MODEL-PROBE → HONEST-POSITIVE (escape lever).** Verbatim stdout
(`state/h016_competing_order_escape_2026_06_25/run_h016.py`):

```
  eta_nest  U_sc    U_sdw   ...  SC_leads  win_width
    0.85    2.222   1.177        False     0.000   (reproduces H_014)
    0.45    2.222   2.222        False     0.000
    0.44    2.222   2.273        True      0.051
    0.30    2.222   3.333        True      0.896
    critical eta* (grid) = 0.44 · (closed form f_glue/N) = 0.45
    plausible-frustration floor = 0.30 · eta* plausible = True
    relaxed room-T U inside SC window = False
  falsifiers_pass = 5/5
VERDICT: an SC-LEADING ESCAPE OPENS for frustration eta_nest < 0.45 (>= floor 0.3) —
  frustrating the nesting LIFTS H_014's competing-order wall in this toy.
```

- **structural_finding**: H_014's CLOSED-NEGATIVE was NOT terminal — sweeping the frustration
  knob flips the SDW-vs-SC race at η*≈0.45, above the plausibility floor 0.30. Competing order is
  a **removable** wall (frustrate the host), not a robust one. BUT the room-T amplitude axis stays
  uncleared (U=0.543 < 2.22) — the escape buys SC-leading, not room-T magnitude. A testable
  coordinate (frustrated flat-band host), not a discovery; absorbed=false, GATE_OPEN.
- **record**: `state/h016_competing_order_escape_2026_06_25/result.json`.
