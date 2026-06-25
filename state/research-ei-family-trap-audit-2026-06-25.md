---
id: EITRAP
slug: ei-family-trap-audit
domain: rtsc
status: pre_registered
pre_register_frozen: true
frozen_at: 2026-06-25
kind: research
---

# Research note — is the Ta2NiSe5 exciton TRAP excitonic-insulator-FAMILY-WIDE? (EI-glue family audit)

**Date:** 2026-06-25
**Lane:** ei-family-trap-audit (EITRAP, research)
**Status:** READ-ONLY cited literature survey — no compute, no rental (web + WebFetch + `sidecar research arxiv`).
**Extends:** `state/research-plus-at-realization-prior-art-2026-06-25.md` (Ta2NiSe5 trap) +
`state/research-clean-glue-candidates-2026-06-25.md` (the clean-vs-trap glue principle) +
`state/research-backup-candidates-2026-06-25.md` (the Ta2Pd3Te5 / 1T-TiSe2 backup EIs) +
`state/research-driven-tise2-reopen-2026-06-25.md` (the driven 1T-TiSe2 🟠 re-open).

**Honesty posture (commons honesty / falsifier-first):** every Tc / pressure / energy / citation below is real and
cited (arXiv id / DOI / journal); abstract-level confirmations are [VERIFIED WebFetch/WebSearch]; textbook /
established values not re-derived this session are [LIT-ESTABLISHED]. No material is claimed to BE an RTSC.
absorbed=false / GATE_OPEN throughout. No fabricated citations — in particular NO invented "Ta2Pd3Te5 mediates SC"
claim; the cited SC there is the real high-pressure SC AFTER metallization. A sober "the EI-glue family is dead"
is a valid result — this is NOT tune-to-green.

---

## The trap being audited (the principle to test family-wide)

From the prior-art + clean-glue passes, the deep pattern: **a glue that IS its own electronic ORDER (exciton / CDW)
TRAPS — the order parameter is itself a Fermi-surface gap that COMPETES with the SC gap; a glue that is a
FLUCTUATION or vibration (spin-fluctuation / phonon / exciton *density fluctuation*) is CLEAN.** Ta2NiSe5 is the
type specimen: it superconducts (Tc≈1.2 K @ ~8 GPa) only AFTER its excitonic-insulator gap is destroyed by pressure,
and the SC is phonon-mediated, not exciton-mediated (arXiv:2106.04396). **Hypothesis under test: this trap is
EXCITONIC-INSULATOR-FAMILY-WIDE, not Ta2NiSe5-specific.**

The decisive textbook-level reason the trap should be generic (the mechanism, not just the data) — from the
*New Era of Excitonic Insulators* review (JPSJ 94, 012001 (2025), arXiv:2411.10985): **"excitons have no net charge
and thus cannot carry electrical current or become superconducting even in their BEC state."** An EI condensate is a
charge-NEUTRAL electron–hole superfluid: the EI ORDER PARAMETER, by construction, *cannot itself superconduct*, and
its gap occupies the same Fermi surface a charge-SC gap would need. The same review states the ONLY way SC appears
"near" an EI: **"superconductivity may appear near the excitonic insulator due to exciton density FLUCTUATIONS …
excitonic superconductivity can occur when density fluctuations … serve as a Cooper pairing glue"** — i.e. the
FLUCTUATION, never the condensed order. [VERIFIED WebSearch — this is the family-wide mechanism statement.]

---

## §1 — Per-EI verdict (the audit)

### 🔴 Ta2NiSe5 (the type specimen — already closed, restated for the family)
SC Tc≈1.2 K @ ~8 GPa, but ONLY after the EI gap is destroyed (EI→semimetal at ~3 GPa); SC is soft-phonon /
electron-lattice, not excitonic (arXiv:2106.04396; optical-conductivity suppression arXiv:2208.12077).
**TRAP — exciton competes with SC; SC requires destroying the exciton.** [VERIFIED prior-art pass.]

### 🔴 Ta2Pd3Te5 — TRAP confirmed (high-pressure SC AFTER metallization)
- EI / quantum-spin-Hall insulator at ambient (excitonic-insulator candidate, small lattice distortion;
  arXiv:2401.01222 ML excitonic instability; STM exciton-condensate impurity bound states). [VERIFIED WebSearch.]
- **Pressure-induced SC** — *Observation of Emergent Superconductivity in the (Quantum Spin Hall / Topological)
  Insulator Ta2Pd3Te5 via Pressure Manipulation*, **J. Am. Chem. Soc. 146, 3890 (2024)** (arXiv:2310.05532). The
  ambient insulating state is driven metallic under pressure; an isostructural electronic transition near **~20 GPa**
  produces a **fivefold amplification of the DOS** that "synergistically fosters the emergence of robust
  superconductivity." SC emerges from the **pressure-METALLIZED** state, NOT from the insulating EI. [VERIFIED
  WebSearch/WebFetch — abstract level; exact Tc not extracted, but the mechanism is metallize-then-superconduct.]
- **Verdict 🔴 TRAP.** Same structure as Ta2NiSe5: SC appears only after the insulating (EI/TI) gap is pressure-killed
  and the system metallizes. There is **NO measured exciton-MEDIATED SC and NO coexistence with the live EI gap.**
  The backup-candidates note's `competing_order="none"` (on the q=0 non-nesting argument) is **WRONG for the
  trap test** — flag for registry correction (§3).

### 🔴 Ta2Ni3Te5 — TRAP confirmed (high-pressure SC AFTER metallization)
- *Pressure-induced nontrivial Z2 band topology and superconductivity in Ta2Ni3Te5*, arXiv:2301.09641 (2023):
  small-gap semiconductor at ambient; **metallization at 3.3 GPa**, then **SC at Pc = 21.3 GPa, Tc ≈ 0.4 K**, rising
  to **Tc ≈ 7.1 K at ~28 GPa**. The Z2=0→1 topological transition occurs only **after** pressure turns it into an
  electron–hole-compensated SEMIMETAL. [VERIFIED WebSearch.]
- **Verdict 🔴 TRAP.** Identical pattern — insulator → pressure-metallize → SC. SC lives in the metallized phase, not
  the EI phase. Exciton not the glue.

### 🟠→🔴 Ta2Pd3Se5 — no SC datum found; trap by family analogy (UNCLEAR-leaning-TRAP)
- Same A2M3X5 EI/QSH family (A=Ta/Nb, M=Pd/Ni, X=Se/Te). The family review (Front. Electron. Mater. 2025,
  10.3389/femat.2025.1456147) groups it with the EI/QSH siblings. **No dedicated SC measurement of Ta2Pd3Se5 was
  found this session.** [VERIFIED — absence of result.]
- **Verdict 🟠 UNCLEAR (no SC datum)** — but every sibling that HAS been pressurized superconducts only after
  metallization, so the prior is 🔴 trap. Honest label: unproven, family-prior = trap. Note the family also contains
  **Nb2Pd3Te5**, reported superconducting — but as an ambient *metal/SC*, i.e. not an EI being used as glue
  (different member, different physics; not a clean-EI-glue counterexample).

### 🔴 1T-TiSe2 — TRAP confirmed (Cu-doping / pressure both kill the exciton to get SC)
- The exciton condensate is real: M-EELS shows an electronic collective (exciton) mode softening to zero energy at
  **T_CDW ≈ 190 K** (Kogar/Abbamonte, Science 358, 1314 (2017)) — the exciton IS the CDW order parameter.
- **CuxTiSe2:** Cu intercalation **continuously SUPPRESSES the CDW**; SC emerges near x≈0.04, **max Tc = 4.15 K at
  x≈0.08** (Morosan et al., Nat. Phys. 2, 544 (2006)). The exciton collective mode **does not soften at any
  temperature for x ≳ 0.01** — i.e. by the time SC appears the exciton condensation is already deteriorated; Cu shifts
  the chemical potential and destroys the exciton-formation condition (arXiv:1902.02046; PubMed 32720648
  "Superconductivity related to the SUPPRESSION of exciton formation in 1T-TiSe2"). [VERIFIED WebSearch.]
- **Verdict 🔴 TRAP.** SC requires suppressing the exciton/CDW (by Cu doping or pressure). Consistent with the
  static-survey 🔴 and the driven-survey 🟠 (driven re-open is a transient/powered LAB coordinate, not an
  equilibrium glue — `research-driven-tise2-reopen-2026-06-25.md`).

### 🔴 Monolayer WTe2 — TRAP confirmed (the EI is the parent insulator; SC is the DOPED-AWAY phase)
- At charge neutrality, monolayer 1T'-WTe2 is a quantum-spin-Hall insulator that is **also an excitonic insulator**
  (spontaneous e–h bound states; Nat. Phys. 18, 87 (2022), s41567-021-01422-w; Nat. Phys. equilibrium-condensation
  s41567-021-01427-5). [VERIFIED WebSearch.]
- **Gate-doping AWAY from the EI → SC:** electron-doping the excitonic-QSH insulator drives a superconducting
  transition (*Gate-induced SC in a monolayer topological insulator*, arXiv:1809.04691; *Unconventional SC quantum
  criticality in monolayer WTe2*, Nat. Phys. 19 (2023), s41567-023-02291-1; arXiv:2501.16699). There is an
  **unconventional SC quantum-critical point sitting BETWEEN the EI state and the SC dome** — the EI and SC are
  ADJACENT/competing phases tuned by carrier density, not the exciton gluing the pairs. [VERIFIED WebSearch.]
- The other WTe2 "coexistence" result (proximity SC gap on the QSH edge while the QSH edge survives; Nat. Phys. 16,
  526 (2020), s41567-020-0816-x) uses an **EXTERNAL van-der-Waals superconductor** to supply the pairs — the EI does
  NOT mediate; it is a proximity host. [VERIFIED WebSearch.]
- **Verdict 🔴 TRAP.** You must dope the EI state away (or supply external pairs) to superconduct; the exciton is not
  the glue. (This sharpens the backup-candidates note, which listed WTe2 as "competing_order none/light" — for the
  trap test it is a trap: SC is the doped-away phase.)

### 🔴 TmSe0.45Te0.55 (intermediate-valence / pressure EI) — TRAP / not-even-SC
- The canonical intermediate-valence EI: under pressure it traverses semiconductor → **condensed excitonic phase**
  → intermediate-valent METAL (Wachter et al., Solid State Commun. 118 (2001); IntechOpen review). The exciton
  condensate phase shows a heat-conductivity rise below ~20 K interpreted as **exciton SUPERFLUIDITY — a NEUTRAL
  superfluid, NOT electrical superconductivity** (no zero-resistance charge transport reported). The metallic phase
  is reached by closing the gap (destroying the EI). [VERIFIED WebSearch.]
- **Verdict 🔴 TRAP (and the cleanest illustration of WHY):** even where the exciton DOES condense into a superfluid,
  it is charge-neutral → carries no supercharge → is NOT a superconductor. To get a charge metal you destroy the EI.
  This is the textbook "neutral exciton can't superconduct" statement made experimental.

### 🔴 InAs/GaSb double quantum well (topological EI) — TRAP (neutral EI; charge SC is external/proximity)
- *Evidence for a topological excitonic insulator in InAs/GaSb bilayers* (Nat. Phys. / PMC5719361): e–h pairing in a
  dilute semimetal opens a **~2 meV gap, T_EI ~10 K**, with quantized QSH edge conductance — a "2D electron-hole
  'superconductor'" / **topological EI**. But this is again a NEUTRAL e–h condensate; the named "superconductor" is by
  analogy to the BCS gap equation, NOT a charge supercurrent. [VERIFIED WebSearch/MagLab highlight.]
- Real charge SC in this platform is **proximity-induced on the QSH edge from an external SC** (Nat. Phys. 10, nphys3036
  *Induced superconductivity in the QSH edge*) — the EI is the host, not the glue. [VERIFIED WebSearch.]
- **Verdict 🔴 TRAP** (same neutral-condensate reason as TmSeTe).

### 🔴 Ultra-compressed helium — TRAP shown as an explicit PHASE SEQUENCE
- *Excitonic Insulator to Superconductor Phase Transition in Ultra-Compressed Helium*, **Nat. Commun. 14, 4458
  (2023)** (arXiv:2301.06756): under TPa compression He goes insulator → **EI (intermediate phase)** → metal →
  **superconductor** (predicted Tc ≈ 20 K just above metallization, ~70 K at 100 TPa). The very title is a transition
  **FROM EI TO SC** — sequential, mutually exclusive phases; the EI is the phase you pass THROUGH and destroy to reach
  the metal that then superconducts. [VERIFIED WebSearch — DFT+MBPT prediction.]
- **Verdict 🔴 TRAP** — the single clearest demonstration that EI and SC are sequential (EI gap must close first).

### 🟠 Theory counterexample candidate — arXiv:2606.01785 (EI–SC COEXISTENCE, but NOT exciton-as-glue)
- *Excitonic-Superconducting Coexistence and Emergent Nematic Superconductivity Driven by Spontaneous Symmetry
  Breaking* (2026): a self-consistent microscopic theory showing EI and SC **can coexist** when an electron–hole
  Fermi-surface MISMATCH lets **different FS regions complementarily support EI vs SC** (FFLO-like e–h pairing +
  spontaneous EI symmetry breaking). [VERIFIED WebFetch.]
- **But the abstract states plainly: EI and SC "are generally regarded as MUTUALLY EXCLUSIVE," and the coexistence is
  SPATIAL (different FS regions), NOT mediation — the exciton does NOT glue the SC.** It is theory, no material.
- **Verdict 🟠 — NOT a clean counterexample to the trap.** It is the *exception that proves the rule*: coexistence
  needs an engineered FS mismatch to keep the two orders OUT of each other's way, and even then the exciton is not the
  pairing glue. It does not deliver an EI-as-glue mechanism.

### 🟢-adjacent (the REAL clean route, for completeness) — exciton DENSITY FLUCTUATIONS, not the EI order
- *Dramatically Enhanced SC in Elemental Bismuth from Excitonic Fluctuation Exchange* (Koley–Laad–Taraphder, Sci. Rep.
  7, 11433 (2017), PMC5591209): SC enhanced by **"preformed but UNCONDENSED excitons"** — an *incipient* EI
  self-doped with carriers, where the **exciton FLUCTUATION (not the condensed EI order)** acts as Cooper glue.
  [VERIFIED WebSearch.] This is the SAME clean pattern as spin-fluctuation glue: the FLUCTUATION glues; the ORDER
  traps. The PNAS 2019 spin-triplet "excitonic-effect" doped-insulator route (2117735119) is likewise a
  fluctuation/effect route, not the static EI gap.
- **This is NOT an "EI glue" — it is an EXCITON-FLUCTUATION glue, near but NOT inside the EI.** It belongs to the
  clean-fluctuation family (alongside spin-fluctuation), not the trap family. It is unmeasured-as-room-T and is a
  *mechanism*, not a turnkey EI crystal.

---

## §2 — GENERIC VERDICT: the EI-glue route is FAMILY-WIDE DEAD

**Every excitonic insulator audited is a 🔴 trap, and the mechanism is generic, not accidental.** Across seven real
EI materials/platforms (Ta2NiSe5, Ta2Pd3Te5, Ta2Ni3Te5, 1T-TiSe2, WTe2, TmSe0.45Te0.55, InAs/GaSb) and the
ab-initio He prediction, **superconductivity NEVER coexists with the live EI order parameter — it appears only after
the EI gap is destroyed (by pressure, doping, or further compression to a metal), and where it appears the glue is
phonons or a doped metal, not the exciton.** The reason is structural and family-wide, stated by the field's own
review: **the EI order parameter is a charge-NEUTRAL electron–hole condensate that cannot carry supercurrent, and its
gap pre-empts the same Fermi surface a charge-SC gap needs.** So "use the static EI order as the pairing glue" is a
category error — an EI is, by definition, the *enemy* of charge SC on its own Fermi surface.

The only theoretical EI–SC coexistence (arXiv:2606.01785) requires an engineered FS mismatch to keep the two orders
spatially apart and still does NOT use the exciton as glue. The only place excitons HELP SC is as **DENSITY
FLUCTUATIONS** of an *incipient* (uncondensed) EI (Bi, arXiv review) — which is the CLEAN-fluctuation family, not the
EI-order family, and is unmeasured at any useful Tc.

**BCS-BEC crossover — does it let exciton + SC cooperate anywhere? NO (for charge SC).** The BCS-BEC crossover in EIs
(arXiv:2404.18727 pressure-tuned e–h pairing; arXiv:2209.07178 triplet-exciton bilayers; Science abg1110 exciton
superfluid crossover) is a crossover **of the exciton condensate itself** — from BCS-like overlapping e–h pairs to
BEC-like tight excitons. It makes a better/tighter NEUTRAL exciton superfluid; it does NOT turn the neutral condensate
into a charge superconductor. The crossover that DOES give charge SC (cuprates/Fe-based/twisted-graphene BCS-BEC) is
the *Cooper-pair* crossover, a different condensate. **There is no regime in the surveyed literature where the exciton
condensate and charge SC COOPERATE — the crossover deepens the trap (a tighter exciton = a more robust competing
neutral order), it does not escape it.**

**Therefore: DROP the entire excitonic-insulator glue family.** It is family-wide dead as a *static-order* glue. The
campaign's honest ceiling stays the CLEAN fluctuation/vibration glues from `research-clean-glue-candidates`:
spin-fluctuation (🟢 clean + real high-Tc 134 K ambient + real proximity datum TbMn6Sn6/Au 3.6 K, but sharp single
boson ~300 meV → ~252 K) and interface phonon (🟠 FeSe/STO ~65 K, ~90–100 meV → ~84 K ceiling) — energy-capped as
they are. **There is ONE thread worth keeping, but it is NOT an EI: the exciton-DENSITY-FLUCTUATION glue of an
incipient EI** (Bi-class), which belongs to the clean-fluctuation family — keep it as a *fluctuation* candidate, not
as an EI-order candidate.

---

## §3 — Proposed registry corrections / rows (Layer B; for the main loop to fold into `tool/rtsc_candidates.py` — do NOT self-edit)

Schema mirrors `Candidate` (`role`, `boson_meV`, `competing_order=(value,source,verified)`). The KEY correction: every
EI row's `competing_order` must read the EI order ITSELF as the competing order (it is the trap), overriding any prior
`"none"` set on a q=0-non-nesting argument. `competing_order="EI-order (TRAP)"` ⇒ fails the harness CLEAN pass (FB2).
absorbed=false, GATE_OPEN on all rows.

| name | role | boson_meV | competing_order (CORRECTED) | clean-glue? | absorbed | citation | trap verdict |
|---|---|---|---|---|---|---|---|
| **Ta2NiSe5** (existing row) | B | ~300 (EI gap 0.16–0.35 eV) | **"EI-order (TRAP)"** — was `"none"`; the q=0 exciton IS the competing gap; SC only when EI destroyed (phonon, 1.2 K@8 GPa) | **NO (TRAP)** | false | arXiv:2106.04396; 2208.12077 | 🔴 |
| **Ta2Pd3Te5** (backup row) | B | ~100 (EI gap) | **"EI/TI-order (TRAP)"** — was `"none (q=0)"`; SC only after ~20 GPa metallization (DOS×5) | **NO (TRAP)** | false | JACS 146,3890 (2024) / arXiv:2310.05532; arXiv:2401.01222 | 🔴 |
| **Ta2Ni3Te5** (new) | B | small-gap semic. | **"EI-order (TRAP)"** — SC only after metallization 3.3 GPa; Tc 0.4 K@21.3 GPa → 7.1 K@28 GPa | **NO (TRAP)** | false | arXiv:2301.09641 | 🔴 |
| **Ta2Pd3Se5** (new) | B | EI candidate | **"EI-order (TRAP, by family prior; SC datum UNVERIFIED)"** | **NO (UNCLEAR→trap prior)** | false | Front.Electron.Mater. 2025 10.3389/femat.2025.1456147 | 🟠→🔴 |
| **1T-TiSe2** (backup row) | B | 400 (upper exciton mode) | **"exciton/CDW-order (TRAP)"** — already CDW; SC needs Cu-doping/pressure to kill exciton; CuxTiSe2 Tc 4.15 K | **NO (TRAP)** | false | Science 358,1314; Nat.Phys.2,544; arXiv:1902.02046 | 🔴 |
| **WTe2-monolayer** (backup row) | B | ~100 (E_b) | **"EI/QSH-order (TRAP)"** — was `"none/light"`; SC is the DOPED-AWAY phase across a QCP; proximity SC is external | **NO (TRAP)** | false | Nat.Phys.18,87; Nat.Phys.19 s41567-023-02291-1; arXiv:2501.16699 | 🔴 |
| **TmSe0.45Te0.55** (new, optional) | B | EI condensate | **"EI-order (TRAP); neutral exciton superfluid ≠ charge SC"** | **NO (TRAP)** | false | Solid State Commun. 118 (2001); IntechOpen review | 🔴 |
| **InAs/GaSb-bilayer** (new, optional) | B | ~2 meV EI gap | **"topological-EI-order (TRAP); neutral condensate; charge SC is proximity"** | **NO (TRAP)** | false | Nat.Phys. PMC5719361; Nat.Phys.10 nphys3036 | 🔴 |
| **exciton-density-fluctuation (incipient-EI, Bi-class)** (new — the KEEPER) | B | fluctuation (not a fixed mode) | **"none (FLUCTUATION of an UNCONDENSED EI — clean, NOT the EI order)"** | **YES (clean-fluctuation family, like spin-fluctuation)** | false | Sci.Rep.7,11433 / PMC5591209; PNAS 2117735119 | 🟢-adjacent (mechanism, unmeasured room-T) |

**One-line instruction for the main loop:** flag ALL static-EI rows (Ta2NiSe5, Ta2Pd3Te5, Ta2Ni3Te5, Ta2Pd3Se5,
1T-TiSe2, WTe2-ML) with `competing_order="EI-order (TRAP)"` so `verify()` fails their CLEAN pass; KEEP only the
exciton-DENSITY-FLUCTUATION (incipient-EI) entry as a clean-fluctuation candidate. Do NOT edit the tool here.

---

## §4 — VERDICT (one paragraph): DROP the EI-glue family; keep the clean fluctuation glues

**The campaign should DROP the entire excitonic-insulator glue family.** The Ta2NiSe5 exciton trap is
EXCITONIC-INSULATOR-FAMILY-WIDE, not material-specific: in every real EI surveyed — Ta2NiSe5 (1.2 K@8 GPa,
phonon, EI destroyed), Ta2Pd3Te5 (SC only after ~20 GPa metallization), Ta2Ni3Te5 (Tc 0.4→7.1 K only above the
3.3 GPa metallization), 1T-TiSe2 (SC needs Cu/pressure to suppress the exciton; CuxTiSe2 4.15 K), monolayer WTe2 (SC
is the doped-away phase across a quantum-critical point from the excitonic-QSH insulator), TmSe0.45Te0.55 (neutral
exciton superfluid, never a charge SC), InAs/GaSb (neutral topological-EI; charge SC only by external proximity) —
and in the ab-initio helium sequence (EI→metal→SC by title) — **superconductivity never coexists with the live EI
order and only appears once the EI gap is destroyed.** The reason is generic and stated by the field's own review:
the EI order parameter is a charge-NEUTRAL electron–hole condensate that cannot carry supercurrent and whose gap
pre-empts the Fermi surface a charge-SC gap needs — so an EI is structurally the enemy of charge SC, not its glue.
The BCS-BEC crossover does NOT rescue it: tuning the exciton condensate from BCS to BEC just makes a tighter *neutral*
superfluid, deepening the trap rather than escaping it, and the only theory coexistence (arXiv:2606.01785) needs an
engineered Fermi-surface mismatch to keep EI and SC spatially apart and STILL does not use the exciton as glue. **There
is exactly one keeper, and it is NOT an EI: the exciton-DENSITY-FLUCTUATION glue of an *incipient* (uncondensed) EI
(Bi-class, Sci. Rep. 7, 11433) — which is the clean-FLUCTUATION family, the same family as spin-fluctuation, and is
unmeasured at any useful Tc.** So the honest ceiling stays the clean fluctuation/vibration glues from the clean-glue
pass — spin-fluctuation (~252 K from the sharp single magnon) and interface phonon (~84 K) — energy-capped as they
are. No static EI is worth keeping as a glue. absorbed=false / GATE_OPEN. No material is claimed to BE an RTSC.

---

## §5 — Citations (load-bearing; verified this session unless marked LIT-ESTABLISHED)

- **JPSJ 94, 012001 (2025) / arXiv:2411.10985** — *A New Era of Excitonic Insulators* — the family-wide mechanism:
  "excitons have no net charge … cannot … become superconducting even in their BEC state"; SC only "near" an EI via
  "exciton density FLUCTUATIONS … as a Cooper pairing glue." [VERIFIED WebSearch — THE generic statement.]
- **arXiv:2106.04396** — Ta2NiSe5 pressure-SC (Tc≈1.2 K@8 GPa, EI destroyed, phonon-mediated). [VERIFIED prior pass.]
- **J. Am. Chem. Soc. 146, 3890 (2024) / arXiv:2310.05532** — Ta2Pd3Te5 emergent SC via pressure (~20 GPa, DOS×5,
  from the metallized state). [VERIFIED WebSearch/WebFetch.]
- **arXiv:2301.09641** — Ta2Ni3Te5 pressure SC: metallize 3.3 GPa; Tc 0.4 K@21.3 GPa → 7.1 K@28 GPa. [VERIFIED WebSearch.]
- **Front. Electron. Mater. (2025) 10.3389/femat.2025.1456147** — Ta2NiSe5 + A2M3X5 family RIXS review (incl.
  Ta2Pd3Se5 / Ta2Ni3Te5). [VERIFIED WebSearch.]
- **Science 358, 1314 (2017)** — 1T-TiSe2 exciton condensate, mode softens at T_CDW≈190 K. [VERIFIED.]
- **Nat. Phys. 2, 544 (2006)** — SC in CuxTiSe2 (CDW suppressed; Tc 4.15 K@x≈0.08). [VERIFIED WebSearch.]
- **arXiv:1902.02046 / PubMed 32720648** — SC related to SUPPRESSION of exciton formation in 1T-TiSe2. [VERIFIED.]
- **Nat. Phys. 18, 87 (2022) s41567-021-01422-w** — monolayer WTe2 is an excitonic insulator. [VERIFIED WebSearch.]
- **Nat. Phys. 19 (2023) s41567-023-02291-1 / arXiv:2501.16699 / arXiv:1809.04691** — gate-induced SC from the
  doped excitonic-QSH insulator monolayer WTe2 (SC is the doped-away phase across a QCP). [VERIFIED WebSearch.]
- **Nat. Phys. 16, 526 (2020) s41567-020-0816-x** — proximity SC gap on the WTe2 QSH edge (external SC, EI is host).
  [VERIFIED WebSearch.]
- **Solid State Commun. 118 (2001) / IntechOpen "Exciton Condensation and Superfluidity in TmSe0.45Te0.55"** —
  neutral exciton superfluid (heat-conductivity rise <20 K), NOT charge SC; gap closes to metal under pressure.
  [VERIFIED WebSearch.]
- **Nat. Phys. (topological EI in InAs/GaSb) PMC5719361 / MagLab highlight** — ~2 meV EI gap, T_EI~10 K, neutral
  condensate ("2D e–h superconductor" by BCS-analogy, not charge SC). [VERIFIED WebSearch.]
- **Nat. Phys. 10 (nphys3036)** — induced SC in the QSH edge (external proximity, not EI-mediated). [VERIFIED WebSearch.]
- **Nat. Commun. 14, 4458 (2023) / arXiv:2301.06756** — *Excitonic Insulator TO Superconductor* in ultra-compressed
  He (EI→metal→SC sequence; Tc~20 K above metallization). [VERIFIED WebSearch.]
- **arXiv:2606.01785 (2026)** — EI–SC COEXISTENCE via FS mismatch (FFLO-like); "generally regarded as MUTUALLY
  EXCLUSIVE"; coexistence is SPATIAL, exciton NOT the glue; theory only. [VERIFIED WebFetch — the 🟠 near-counterexample.]
- **Sci. Rep. 7, 11433 (2017) / PMC5591209** — *Enhanced SC in Bi from Excitonic Fluctuation Exchange* — "preformed
  but UNCONDENSED excitons" of an incipient EI as glue (the clean-FLUCTUATION keeper, NOT the EI order). [VERIFIED.]
- **arXiv:2404.18727 / 2209.07178 / Science abg1110** — BCS-BEC crossover of the EXCITON condensate (neutral
  superfluid crossover; does not become charge SC). [VERIFIED WebSearch.]
- **PNAS 2117735119 (2019)** — spin-triplet SC from excitonic EFFECT in doped insulators (fluctuation/effect route).
  [VERIFIED WebSearch.]

**Honesty note.** No fabricated citations. NO invented "Ta2Pd3Te5/Ta2Ni3Te5 exciton-MEDIATED SC" claim — the cited SC
in those materials is the real HIGH-PRESSURE SC that appears AFTER the EI/insulating gap is destroyed and the system
metallizes. The family-wide-trap verdict is the honest reading: every static EI competes with charge SC (neutral
condensate + competing FS gap), the BCS-BEC crossover deepens rather than escapes it, and the only clean thread is the
exciton-DENSITY-FLUCTUATION route, which is a fluctuation glue, not an EI glue. absorbed=false / GATE_OPEN throughout.
