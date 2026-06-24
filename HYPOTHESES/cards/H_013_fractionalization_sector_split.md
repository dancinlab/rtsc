---
id: H_013
slug: fractionalization-sector-split
title: Charge/spin/orbital fractionalization evades the FS two-lever tie at the SECTOR level (geometry in the spinon, glue in the holon) — but only above an exotic ~800 meV fractionalization gap, and only to ~77 K (box opens, new bill, no room-T)
domain: rtsc
status: model-probe
exploration_method: M1 SPLIT (brainstorm seed S5, most exotic) — split the two levers across fractionalized sectors
verification_method: W1 (pre-register frozen) + W2 (falsifier-6) + W3 (deterministic) + W5 (honest-limits-5)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
since: 2026-06-25
compute: fleet lane (rtsc-fleet-orthogonal-levers)
---

# H_013 — fractionalization sector-split (S5) (rtsc)

## Hypothesis

Brainstorm seed **S5 (M1 SPLIT, most exotic)**: charge/spin/orbital fractionalization
(spinon/holon separation) puts the geometry lever in ONE sector (spinon) and the glue in
ANOTHER (holon), evading the Fubini-Study anti-correlation at the **sector** level — a different
bypass than the spatial bilayer (H_003). Does sector-separation open the box a single fused
electron cannot, and what is the cost?

## Why

- The FS tie binds g and Ω **on one electron**; if the electron fractionalizes, the tie is on a
  composite that no longer needs both levers in the same sector.
- But fractionalization requires a deconfinement gap; below it the sectors recombine and the tie
  returns — the relocated bill.

## Falsifiers (≥5 — pre-registered)

- **F1_sector_split_opens_box**: PASS = a finite fractionalization gap opens the box (g_eff≥2, Ω_eff≥130).
- **F2_evades_fs_tie**: PASS = the split evades the single-electron FS cap.
- **F3_fractionalization_gap_is_the_bill**: PASS = the box stays open only above a critical Δ_frac.
- **F4_no_free_room_t**: PASS = the ideal split alone does NOT reach room-T.
- **F5_monotone_in_gap**: PASS = Ω_eff rises monotonically with Δ_frac.
- **F6_no_fabrication**: PASS = sector levers are the published host values.

## Honest Limits (≥5)

- **L1 (toy deconfinement model)**: Δ_frac is a schematic deconfinement scale, not a computed
  spin-liquid gap; a real verdict needs a parton/gauge-theory or DMRG treatment.
- **L2 (the ~800 meV gap is exotic)**: the box opens only above Δ_frac ~800 meV (critical 459 meV
  to hold against recombination) — far above known spin-liquid gaps; this is the relocated bill.
- **L3 (only ~77 K even ideal)**: the ideal deconfined split reaches bkt_Tc ~77 K, not room-T —
  sector-split alone is not a room-T mechanism.
- **L4 (sectors assumed cleanly separable)**: real spinon/holon coupling, gauge fluctuations, and
  confinement transitions are omitted.
- **L5**: `absorbed=true` still requires accredited transport + Meissner + measured H_c2 / T_c.

## Cross-Links

- **sibling bypass**: H_003 (spatial bilayer SPLIT — the same labor-division, different axis).
- **contrast**: H_012 (topology collapses) · H_006 (3D — a real orthogonal lever).

## Verdict

**🟡 MODEL-PROBE → BOX-OPENS-BUT-NEW-BILL.** Verbatim stdout
(`state/h013_fractionalization_sector_split_2026_06_25/run_h013.py`):

```
=== H_013 fractionalization sector-split (S5, M1 SPLIT) — deterministic toy probe ===
  FS wall on ONE fused electron at g=2.87: omega_cap = 22.0 meV  -> fused in_box = False
  ideal deconfined split (Delta_frac -> inf): g_eff=2.87  omega_eff=170.0 meV -> in_box=True  bkt_Tc~77.5K
  critical fractionalization gap Delta_frac* = 459.0 meV  (must EXCEED to keep the box open)
    Delta_frac=  400.0 meV  s_deconf=0.702  omega_eff= 125.9 meV  in_box=False  bkt_Tc~57.4K
    Delta_frac=  800.0 meV  s_deconf=0.825  omega_eff= 144.1 meV  in_box=True   bkt_Tc~65.7K
  any finite Delta_frac opens box = True  (min opening Delta_frac = 800.0 meV)
  room-T reached by ideal split alone = False  (room-T target = 293.0 K)
  falsifiers_pass = 6/6
VERDICT: MODEL-PROBE -> BOX-OPENS-BUT-NEW-BILL (fractionalization gap relocates the wall)
```

- **structural_finding**: fractionalization genuinely evades the FS tie at the sector level (a
  real orthogonal bypass), but only above an **exotic ~800 meV deconfinement gap** and only to
  ~77 K — the wall is relocated to the fractionalization-gap requirement, not removed. A real but
  expensive and sub-room-T lever.
- **record**: `state/h013_fractionalization_sector_split_2026_06_25/result.json`.
