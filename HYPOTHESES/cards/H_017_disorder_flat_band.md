---
id: H_017
slug: disorder-flat-band
title: Disorder does NOT give the geometry lever for free — the same disorder that flattens the band to ≥2× DOS Anderson-localizes carriers below the Cooper-pair length; flat-and-delocalized window is empty (O2 closes)
domain: rtsc
status: closed-negative
exploration_method: M4 OBSTACLE-as-resource (brainstorm seed O2) — disorder-induced flat band
verification_method: W1 (pre-register frozen) + W2 (falsifier-5) + W3 (deterministic) + W5 (honest-limits-5)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
compute: fleet lane (verification)
---

# H_017 — disorder as the geometry lever? (O2) (rtsc)

## Hypothesis

Brainstorm seed **O2 (M4 OBSTACLE-as-resource)**: disorder broadens a dispersive band into an
effective FLAT, high-DOS band — giving the geometry lever "for free" without crystallinity. The
obstacle (disorder) becomes the resource. **But** the same disorder Anderson-localizes carriers.
Tested claim: is there a window where the band is flat-enough (DOS gain ≥2×) AND still
delocalized (localization length ξ_loc > the Cooper-pair length ξ_0), or are the two mutually
exclusive (O2 closes)?

## Why

- Disorder flattens (DOS pile-up) and localizes (ξ_loc shrinks) at the SAME knob W_dis. SC needs
  both a flat high-DOS band AND delocalized pairs. If the flatness onset W_flat exceeds the
  delocalization limit W_deloc, no host satisfies both.

## Falsifiers (≥5 — pre-registered)

- **F1_window_exists** / **F2_analytic_window_exists**: PASS = a flat-AND-delocalized W window exists.
- **F3_flat_point_delocalized**: PASS = at the flatness onset the carriers are still delocalized.
- **F4_window_has_width**: PASS = the window has nonzero width.
- **F5_margin_above_pair**: PASS = ξ_loc exceeds ξ_0 at the flat point.

## Honest Limits (≥5)

- **L1 (toy two-knob model)**: linear DOS pile-up G(W)=1+W/W_band and 2D weak-localization
  ξ_loc/a=exp(β/W²) are schematic scalings, not a real disordered-band computation (needs KPM /
  transfer-matrix / kernel-polynomial DOS + localization).
- **L2 (2D weak-localization assumed)**: 3D has a mobility edge (Anderson transition) — a 3D host
  could delocalize states above the edge while keeping a flat region; untested (the main escape).
- **L3 (generous DOS pile-up)**: the linear pile-up is generous to O2, so the closure is conservative.
- **L4 (ξ_0=3a fixed)**: the Cooper-pair length is a fixed proxy; a very short-coherence (BEC-side)
  pair would tolerate more localization — untested.
- **L5**: `absorbed=true` still requires accredited transport + Meissner + measured H_c2 / T_c.

## Cross-Links

- **contrast**: H_001/H_006 (crystalline geometry lever) — O2 tried to get it from randomness instead.
- **possible escape (untested)**: a 3D mobility edge (L2) or a BEC-side short pair (L4).

## Verdict

**🟡 MODEL-PROBE → CLOSED-NEGATIVE (O2 closes).** Verbatim stdout
(`state/h017_disorder_flat_band_2026_06_25/run_h017.py`):

```
  flat-enough onset    : W_dis >= 1.0  (DOS gain reaches 2.0x)
  delocalized limit    : W_dis <  0.674626  (xi_loc drops to xi_0=3.0)
  W_flat_min < W_deloc_max ? : False  (flat_min=1.0  deloc_max=0.674626)
  flat-and-delocalized window: [None, None]  width=0.0  exists=False
  xi_loc at flat-onset (W=1.0) : 1.648721 a   (xi_0=3.0 a -> xi_loc/xi_0 = 0.55)
  falsifiers_pass = 0/5
VERDICT: disorder-flatness and pair-scale delocalization are MUTUALLY EXCLUSIVE under this toy
  — the same disorder that flattens the band to >=2x DOS localizes carriers below the
  Cooper-pair length xi_0. Obstacle-as-resource (O2) CLOSES (CLOSED-NEGATIVE).
```

- **structural_finding**: disorder cannot supply the geometry lever for free — flattening to ≥2×
  DOS requires W_dis≥1.0, but delocalization fails already at W_dis>0.67, so the flat band's
  carriers are localized (ξ_loc=0.55·ξ_0) before SC can use them. O2 closes under 2D
  weak-localization; the only honest escape is a 3D mobility edge (L2) or a BEC-side short pair (L4).
- **record**: `state/h017_disorder_flat_band_2026_06_25/result.json`.
