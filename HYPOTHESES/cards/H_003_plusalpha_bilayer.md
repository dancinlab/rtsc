---
id: H_003
slug: plusalpha-bilayer
title: The +@ combination (bilayer division-of-labor) enters the room-T two-lever box that no single host can — geometry in layer A, stiff glue proximity-imported from layer B
domain: rtsc
status: model-probe
exploration_method: M1 SPLIT (brainstorm seed B2) — divide the two levers across two proximity-coupled subsystems
verification_method: W1 (pre-register frozen) + W2 (falsifier-6) + W3 (deterministic) + W5 (honest-limits-6)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
since: 2026-06-25
---

# H_003 — +@ combination: bilayer division-of-labor bypass of the two-lever wall (rtsc)

## Hypothesis

The Fubini-Study two-lever wall (H_001) forbids ONE host from holding both large quantum
geometry (⟨g⟩≥2) AND stiff coupling (Ω≥130 meV). The **+@ combination** (meta-principle
M1 SPLIT, brainstorm seed B2) divides labor: layer **A** supplies the flat-band geometry
(a published host, CoSn ⟨g⟩=2.87 but soft Ω_A=22 meV), layer **B** supplies stiff glue
(a published high-frequency phonon scale Ω_B~170 meV, no flat-band geometry), and proximity
coupling imports B's glue into A's flat band. The claim: the bilayer enters the room-T design
box that neither single host can.

## Why

- H_001 closed the SINGLE-host geometric path: CoSn/Nb3Cl8 have the geometry but soft
  d-electron phonons (Ω~15–30 meV) miss the 130 meV gate. The wall is a *simultaneity*
  constraint on one material — exactly what SPLIT targets.
- The brainstorm meta-law warns SPLIT only **defers/relocates** a frame-invariant wall
  within a budget; this card tests *whether* the relocation opens a reachable corner or
  just re-bills the same deficit at the interface.

## Predictions

- **H3.1**: at a proximity weight η that lifts Ω_eff to ≥130 meV, an *ideal* interface
  (electron-opaque) keeps g_eff≥2 → the box opens (which the single host cannot).
- **H3.2**: a *generic* interface (electron hybridization ∝ glue transfer) dilutes g_eff
  below 2 at that same η → the box stays closed; the breakthrough demands a non-generic
  (phonon-transparent / electron-opaque) interface with electron_cost below a critical value.

## Variables

- **g_A, Ω_A**: published layer-A flat-band host levers (CoSn 2.87 / 22 meV, H_001 ledger)
- **Ω_B**: published stiff-glue phonon scale (~170 meV, light-element σ-bond class)
- **η** ∈ [0,1]: proximity transfer weight (interface transparency to the glue)
- **electron_cost** ∈ [0,1]: generic electron-hybridization penalty of the same interface

## Run Protocol

- deterministic: closed-form transfer model, stdlib only, $0 mac local
- tools: `tool/rtsc_harness.py` (`proximity_bilayer_levers`, `critical_electron_cost`,
  `two_lever_box_check`, `geometric_bkt_tc_band`)
- run: `python3 state/h003_plusalpha_bilayer_2026_06_25/run_h003.py`
- record: `state/h003_plusalpha_bilayer_2026_06_25/result.json`

## Criteria

- **C1**: layer-A levers are the published H_001 ledger values (no fabrication).
- **C2**: the ideal-interface bilayer enters the box (g_eff≥2 AND Ω_eff≥130 AND U/Ω≥1.5)
  while the single host does not.
- **verdict_rule**: BOX-OPENS-AT-IDEAL-INTERFACE = C2 met AND the box demands a
  non-generic interface (0 < critical_electron_cost < 1); SPLIT-CLOSED = box never opens
  even at the ideal interface.

## Falsifiers (≥5 — pre-registered)

- **F1_split_opens_box**: PASS = the +@ bilayer enters the box the single host cannot.
- **F2_generic_stays_closed**: PASS = a generic (electron_cost=1) interface keeps the box
  closed — a careless interface does not get the breakthrough for free.
- **F3_relocates_not_removes**: PASS = the box opens only below a critical interface-quality
  threshold (0<ec*<1) — confirming SPLIT **relocates** the wall into an interface criterion
  rather than removing it (the brainstorm meta-law, made measurable).
- **F4_glue_imported**: PASS = proximity actually raised Ω_eff above the soft Ω_A.
- **F5_bounds**: PASS = g_eff≥0 and η∈[0,1].
- **F6_no_fabrication**: PASS = layer-A levers are the published ledger values.

## Honest Limits (≥5)

- **L1 (toy transfer model, not a heterostructure verdict)**: η and electron_cost are
  explicit model knobs, not measured interface properties. The real verdict needs a
  DFT/DFPT/el-ph heterostructure calc (`src/`, cloud pod) of an actual spacer system →
  tier is 🟡 MODEL-PROBE (real-pending), not a discovery.
- **L2 (box-entry is necessary, NOT sufficient for room-T)**: the ideal-interface bilayer
  reaches only bkt_Tc ~59 K — it clears the *design box* but is still ~5× short of 293 K.
  The +@ breaks the **box wall**, not yet the **room-T wall** (deepening: H_004+).
- **L3 (the breakthrough relocates to a hard interface)**: electron_cost ≤ ~0.415 demands a
  phonon-transparent / electron-opaque interface — a real, unsolved materials problem, not a
  guaranteed win. This is the relocated bill (per the brainstorm's ledger-deficit meta-law).
- **L4 (Ω_B is an order-of-magnitude published scale)**: 170 meV is a light-element σ-bond
  phonon order, not a specific synthesized glue layer; a softer real B layer raises η* (and
  tightens ec*).
- **L5 (proximity model is first-order)**: a linear glue-import + linear geometry-dilution
  ignores band-structure detail, detuning, and Tc-vs-coupling nonlinearity (Allen-Dynes/BKT).
- **L6**: `absorbed=true` would still require accredited 4-probe transport + Meissner
  expulsion + measured H_c2 / T_c — no simulation flips that gate (commons honesty).

## Cross-Links

- **parent wall**: H_001 (single-host two-lever wall — the constraint this SPLITs).
- **sibling FRAME-test**: H_006 (is the FS bound dimension-invariant? — the orthogonal bypass).
- **seed**: `state/sf-abstract-brainstorm.md` B2 (bilayer division-of-labor, M1 SPLIT).
- **harness**: `tool/rtsc_harness.py`.

## Verdict

**🟡 MODEL-PROBE → BOX-OPENS-AT-IDEAL-INTERFACE** — the +@ bilayer enters the two-lever box
the single host cannot, but only via a non-generic interface, and only to bkt_Tc ~59 K (box
cleared, room-T not). Verbatim stdout of the deterministic run
(`state/h003_plusalpha_bilayer_2026_06_25/run_h003.py`, importing `tool/rtsc_harness.py`):

```
=== H_003 +@ bilayer division-of-labor — deterministic toy probe ===
  single host (CoSn g=2.87 omega=22.0meV) in_box = False  (H_001 wall)
  +@ glue layer B: omega_B = 170.0 meV
  box-opening eta* = 0.73  ->  omega_eff = 130.0 meV
  ideal interface (ec=0):   g_eff=2.87 omega_eff=130.0meV -> in_box=True  bkt_Tc~59.3K
  generic interface (ec=1): in_box=False
  critical_electron_cost ec* = 0.415  (interface must be BELOW this to open the box)
  room-T target = 293.0 K
  falsifier F1_split_opens_box      : PASS
  falsifier F2_generic_stays_closed : PASS
  falsifier F3_relocates_not_removes: PASS
  falsifier F4_glue_imported        : PASS
  falsifier F5_bounds               : PASS
  falsifier F6_no_fabrication       : PASS
  falsifiers_pass = 6/6
VERDICT: MODEL-PROBE → BOX-OPENS-AT-IDEAL-INTERFACE
```

- **structural_finding**: the +@ SPLIT does not *remove* the two-lever wall — it *relocates*
  it from "(g, Ω) in one host" (impossible) into "a phonon-transparent / electron-opaque
  interface (electron_cost ≤ 0.415)" (a different, possibly-reachable materials problem).
- **honest_caveat**: box-entry ≠ room-T. The bilayer clears the design box but bkt_Tc ~59 K
  is still ~5× short of 293 K — the room-T deficit (the campaign's measured ~5× thermodynamic
  deficit) survives the combination. The +@ buys the box, not the target.
- **record**: `state/h003_plusalpha_bilayer_2026_06_25/result.json`.
