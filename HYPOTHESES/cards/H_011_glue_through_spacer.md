---
id: H_011
slug: glue-through-spacer
title: The +@ trilayer is self-consistent ONLY for a bosonic (field-coupled) glue — a neutral/collective exciton/plasmon penetrates the electron-opaque connector via its long-range Coulomb field [window 0.44–2.85 ML], a fermionic electron-transfer glue is blocked
domain: rtsc
status: model-probe
exploration_method: internal-consistency check — resolve the H_009 L2 crux (electron-opaque vs electronic glue)
verification_method: W1 (pre-register frozen) + W2 (falsifier-4) + W3 (deterministic) + W5 (honest-limits-5)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
since: 2026-06-25
---

# H_011 — does the electronic glue pass an electron-opaque spacer? (the +@ crux) (rtsc)

## Hypothesis

The dominant risk of the whole +@ trilayer (H_009 L2): the connector C must block single-electron
tunneling (to preserve the flat-band geometry g of layer A) **yet** pass the electronic glue (to
reach the room-T Ω, H_004). If the glue is electronic, an electron-opaque spacer seems to block it
too — a self-contradiction that would collapse the architecture. The resolution under test: a
**neutral/collective bosonic** glue (exciton / plasmon) couples across the spacer via its
**long-range Coulomb/dipole field** (λ_Coulomb ≫ λ_e), not wavefunction overlap, so it penetrates
the electron-tunneling barrier — whereas a **fermionic** (electron-transfer) glue is blocked exactly
where the electron is. The +@ trilayer is consistent **iff the glue is bosonic**.

## Why

- Single-electron tunneling needs wavefunction overlap (decays over λ_e, short for a wide gap);
  a bosonic collective mode couples via the Coulomb/dipole field, which is long-range and
  penetrates thin insulators — exactly the physics of Förster energy transfer and Coulomb drag
  between layers separated by an insulating barrier.
- This converts H_009's relocated bill into a sharp, falsifiable *glue-character* requirement.

## Predictions

- **H11.1**: a bosonic (field-coupled, λ_Coulomb≫λ_e) glue has a thickness window that is both
  electron-opaque and glue-coupled.
- **H11.2**: a fermionic (electron-transfer, decays like the electron) glue has NO window.

## Variables

- **λ_e**: electron tunneling decay length (ML) — short, wide-gap spacer
- **λ_Coulomb**: bosonic-glue field decay length (ML) — long, long-range field
- **glue character**: bosonic (field-coupled) vs fermionic (transfer)

## Run Protocol

- deterministic, stdlib only, $0 mac local
- tools: `tool/rtsc_harness.py` (`glue_through_spacer_window`, `coulomb_glue_coupling`)
- run: `python3 state/h011_glue_through_spacer_2026_06_25/run_h011.py`
- record: `state/h011_glue_through_spacer_2026_06_25/result.json`

## Criteria

- **verdict_rule**: NO-CONTRADICTION = a bosonic glue opens a window through the electron-opaque
  spacer AND a fermionic glue does not (the consistency is conditional on glue character).

## Falsifiers (≥4 — pre-registered)

- **F1_bosonic_passes**: PASS = a bosonic glue penetrates the electron-opaque spacer.
- **F2_fermionic_blocked**: PASS = a fermionic glue is blocked (no window) — consistency is conditional.
- **F3_window_width**: PASS = the bosonic window has real thickness tolerance (>0.5 ML).
- **F4_finite_onset**: PASS = the window onset is at finite, fabricable thickness.

## Honest Limits (≥5)

- **L1 (decay-length model, not a DFT/cRPA interface)**: λ_e and λ_Coulomb are decay-length
  proxies; a real verdict is a DFT + constrained-RPA calc of cross-spacer exciton/plasmon coupling
  vs electron tunneling on an actual A/hBN/B trilayer (src/, pod). 🟡 MODEL-PROBE.
- **L2 (the resolution narrows the glue to bosonic + field-coupled)**: this is a real constraint,
  not a free pass — it excludes fermionic/transfer pairing glues. Whether a bosonic exciton/plasmon
  glue at the required Ω (~349 meV, H_007) AND without competing order (H_004 L2) exists is the
  next open question.
- **L3 (Coulomb coupling also reaches competing channels)**: a long-range field that couples the
  glue also couples density-density (CDW) and dielectric screening — the same penetration that
  helps pairing can seed the competing order H_004 warned of.
- **L4 (geometry-preservation assumes only single-electron hybridization matters)**: a strong
  Coulomb field across the spacer could still perturb layer A's band (Stark / image-charge),
  partially diluting g by a channel this model omits.
- **L5**: `absorbed=true` still requires accredited transport + Meissner + measured H_c2 / T_c.

## Cross-Links

- **parent**: H_009 (the connector whose L2 crux this resolves) · H_004/H_008 (the glue it constrains).
- **architecture**: completes the self-consistent +@ trilayer — flat-band geometry layer A,
  hBN-class electron-opaque connector C, bosonic (exciton/plasmon) field-coupled glue layer B, 3D.

## Verdict

**🟡 MODEL-PROBE → NO CONTRADICTION (CONDITIONAL ON A BOSONIC GLUE).** Verbatim stdout
(`state/h011_glue_through_spacer_2026_06_25/run_h011.py`):

```
=== H_011 electronic glue through an electron-opaque spacer — the +@ crux ===
  lambda_e (electron tunneling) = 0.5 ML   lambda_coulomb (bosonic field) = 8.0 ML
  BOSONIC glue (exciton/plasmon, field-coupled):
    window = [0.44, 2.85] ML  width=2.41 ML  exists=True
  FERMIONIC glue (electron-transfer):  window exists=False
  falsifier F1_bosonic_passes       : PASS
  falsifier F2_fermionic_blocked    : PASS
  falsifier F3_window_width         : PASS
  falsifier F4_finite_onset         : PASS
  falsifiers_pass = 4/4
VERDICT: NO CONTRADICTION — A BOSONIC (FIELD-COUPLED) GLUE PASSES THE ELECTRON-OPAQUE SPACER; A FERMIONIC ONE DOES NOT
```

- **structural_finding**: the +@ trilayer has no internal contradiction — but only because the
  glue is a NEUTRAL/COLLECTIVE BOSONIC mode (exciton/plasmon) coupling via its long-range Coulomb
  field, which penetrates the electron-tunneling barrier (window 0.44–2.85 ML, wider than the
  phonon window). A fermionic transfer glue is blocked. The architecture's relocated bills now
  collapse to one sharp requirement: **a bosonic, field-coupled, ~349 meV glue without competing
  order** — the single open materials question the whole closed-form +@ chain points to.
- **record**: `state/h011_glue_through_spacer_2026_06_25/result.json`.
