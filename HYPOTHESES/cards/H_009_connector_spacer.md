---
id: H_009
slug: connector-spacer
title: The third material is the connector — a wide-gap/phonon-matched spacer C (hBN-class) opens a fabricable thickness window [0.44, 1.78 ML] that is both electron-opaque and phonon-transparent, turning H_003's abstract interface knob into a real material lever
domain: rtsc
status: model-probe
exploration_method: M1 SPLIT extension — promote the interface (H_003 electron_cost knob) to a third material C (trilayer A/C/B)
verification_method: W1 (pre-register frozen) + W2 (falsifier-4) + W3 (deterministic) + W5 (honest-limits-5)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
since: 2026-06-25
---

# H_009 — connector spacer as the third material (trilayer A/C/B) (rtsc)

## Hypothesis

H_003's +@ bilayer left the interface as an abstract `electron_cost` knob (box opens iff
electron_cost ≤ 0.415). The user's refinement: make the **third material** the connector — a
spacer **C** of thickness d (monolayers) inserted between geometry layer A and glue layer B.
C must be **electron-opaque** (block hybridization → drive electron_cost ≤ 0.415) yet
**phonon-transparent** (pass the glue → transmission ≥ 0.70). The claim: a wide-gap,
phonon-matched spacer (hBN-class) has a fabricable thickness **window** where it does both,
turning H_003's relocated "interface bill" into a concrete material + thickness requirement.

## Why

- H_003's L3 named the interface as the relocated bill; this card pays it with a real material.
- Electron tunneling decays fast through a wide gap (short λ_e); stiff/matched phonons decay
  slowly (long λ_ph). When λ_e ≪ λ_ph there is a thickness band that is opaque-yet-transparent.
- hBN is the archetype: ~6 eV gap (fast electron decay) + stiff B–N phonons (good transmission)
  — already the canonical 2D-heterostructure spacer.

## Predictions

- **H9.1**: a wide-gap/phonon-matched spacer (λ_e=0.5, λ_ph=5.0 ML) opens a finite window.
- **H9.2**: a non-selective spacer (λ_e ≈ λ_ph) opens NO window — the connector is not automatic.

## Variables

- **λ_e**: electron tunneling decay length (ML) — short for a wide-gap spacer
- **λ_ph**: phonon transmission decay length (ML) — long for a stiff/matched spacer
- **d**: spacer thickness (ML), swept

## Run Protocol

- deterministic, stdlib only, $0 mac local
- tools: `tool/rtsc_harness.py` (`spacer_window`, `spacer_electron_cost`, `spacer_phonon_transmission`)
- run: `python3 state/h009_connector_spacer_2026_06_25/run_h009.py`
- record: `state/h009_connector_spacer_2026_06_25/result.json`

## Criteria

- **verdict_rule**: CONNECTOR-WINDOW-EXISTS = a wide-gap/matched spacer has a finite,
  few-monolayer window where electron_cost ≤ 0.415 AND phonon transmission ≥ 0.70, while a
  non-selective spacer does not.

## Falsifiers (≥4 — pre-registered)

- **F1_good_spacer_window**: PASS = the wide-gap/matched spacer opens a window.
- **F2_bad_spacer_no_window**: PASS = a non-selective spacer (λ_e ≈ λ_ph) has NO window.
- **F3_finite_thickness**: PASS = the window is at finite, few-ML (fabricable) thickness.
- **F4_window_has_width**: PASS = the window has nonzero thickness tolerance.

## Honest Limits (≥5)

- **L1 (decay-length model, not a DFT interface)**: λ_e and λ_ph are decay-length proxies for
  a real spacer's electron tunneling and phonon transmission — a DFT/DFPT interface calc (src/,
  pod) on an actual A/hBN/B trilayer is the real verdict. 🟡 MODEL-PROBE.
- **L2 (electron-opaque vs phonon-transparent may not decouple for a real glue)**: an electronic
  (eV-scale, H_004) glue is itself electronic — a spacer that blocks electrons may also block an
  *electronic* glue. The clean λ_e ≪ λ_ph separation assumes a phonon-like glue; an electronic
  glue (H_008's regime) reintroduces the coupling. Strongest limit.
- **L3 (lattice/strain matching ignored)**: a real trilayer needs lattice-matched A/C/B; strain,
  moiré, and interface reconstruction are not modeled.
- **L4 (window width is a model tolerance)**: 1.34 ML is the model window; real fabrication
  tolerance depends on growth control not captured here.
- **L5**: `absorbed=true` still requires accredited transport + Meissner + measured H_c2 / T_c.

## Cross-Links

- **parent**: H_003 (the interface knob this promotes to a material).
- **siblings**: H_007 (3-lever combination) · H_010 (top-down: connector is structurally essential).

## Verdict

**🟡 MODEL-PROBE → A WIDE-GAP/PHONON-MATCHED CONNECTOR OPENS A FABRICABLE WINDOW.** Verbatim
stdout (`state/h009_connector_spacer_2026_06_25/run_h009.py`):

```
=== H_009 connector spacer (trilayer A/C/B) — the 3rd material is the link ===
  requirement: electron_cost <= 0.415 (opaque, H_003 critical) AND phonon T >= 0.70 (glue passes)
  GOOD spacer (hBN-like: lambda_e=0.5 wide-gap, lambda_ph=5.0 stiff):
    window = [0.44, 1.78] ML  width=1.34 ML  exists=True
  BAD spacer (non-selective: lambda_e=lambda_ph=3.0):  window exists=False
  falsifier F1_good_spacer_window   : PASS
  falsifier F2_bad_spacer_no_window : PASS
  falsifier F3_finite_thickness     : PASS
  falsifier F4_window_has_width     : PASS
  falsifiers_pass = 4/4
VERDICT: A WIDE-GAP/PHONON-MATCHED CONNECTOR (hBN-CLASS) OPENS A FABRICABLE THICKNESS WINDOW
```

- **structural_finding**: the +@ "2 materials joined" becomes a **trilayer A/C/B** where C is an
  engineered spacer; H_003's abstract interface bill is paid by a concrete material class
  (wide-gap, phonon-matched, e.g. hBN) at a few-monolayer thickness. The connector is a real
  third lever, not a free assumption — a non-selective spacer fails (F2). The dominant risk is L2
  (an electronic glue may not pass an electron-opaque spacer).
- **record**: `state/h009_connector_spacer_2026_06_25/result.json`.
