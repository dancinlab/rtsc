---
id: CLEANGLUE
slug: clean-glue-candidates
domain: rtsc
status: pre_registered
pre_register_frozen: true
frozen_at: 2026-06-25
kind: research
---

# Research note — CLEAN bosonic pairing-glue candidates for the +@ trilayer (fixing the Ta2NiSe5 competing-order trap)

**Date:** 2026-06-25
**Lane:** clean-glue-research (CLEANGLUE, research)
**Status:** READ-ONLY cited literature survey — no compute, no rental (web + `sidecar research arxiv` + WebFetch).
**Rule served:** the campaign's "실측전 research" rule + the prior-art pass's load-bearing finding.

**The problem this fixes** (`state/research-plus-at-realization-prior-art-2026-06-25.md`): the campaign's lead
glue, **Ta2NiSe5's exciton**, is a GRAVEYARD on two counts — (1) proximity SC from an excitonic insulator
has NEVER been measured in 50 years, and (2) Ta2NiSe5 superconducts ONLY when its exciton is DESTROYED by
pressure (phonon-mediated, arXiv:2106.04396) — i.e. the boson we called "glue" is the **enemy** of SC there.
Same trap for 1T-TiSe2 (the ~400 meV boson IS its CDW). This note grows the +@ glue registry with a CLEAN
boson, judged on two explicit filters.

**The two CLEAN filters.**
1. **Not a competing-order soft mode** — the pairing boson must NOT be the soft / order-parameter mode of a
   density-wave / excitonic / structural order that suppresses SC when present (the Ta2NiSe5 / 1T-TiSe2 trap).
   Boson and SC must COEXIST, not compete.
2. **Real pairing precedent** — prefer a boson with a MEASURED (or strongly-evidenced) SC-mediation, ideally in
   a proximity / interface / heterostructure geometry (the +@ setting).

**Honesty posture (commons honesty / falsifier-first):** every energy / Tc / citation below is real and cited;
abstract-level confirmations are [VERIFIED WebFetch/WebSearch]; textbook/established values not re-derived this
session are [LIT-ESTABLISHED]. No material is claimed to BE an RTSC. absorbed=false / GATE_OPEN throughout. A
sober "no clean glue reaches the room-T demand" is a valid result — this is NOT tune-to-green.

---

## §0 — The target a CLEAN glue must clear (harness, byte-deterministic)

Inline against `tool/rtsc_harness.py` (NOT edited):

| Quantity | Value |
|---|---|
| `omega_for_stacked_tc(293, three_d=True)` | **349.31 meV** ← glue energy needed for room-T with the 3D lever |
| `stacked_tc(349, True)` | 292.74 K (just clears 293) |
| `stacked_tc(500, True)` | 419.40 K (cuprate BI-magnon scale — clears, IF a sharp usable mode) |
| `stacked_tc(300, True)` | 251.64 K (cuprate SINGLE-magnon zone-boundary ~300 meV → ~252 K; the H_020 wall) |
| `stacked_tc(100, True)` | **83.88 K** (interface-phonon scale, FeSe/STO ~90–100 meV) |
| `stacked_tc(90, True)` | **75.49 K** (SrTiO3 polar phonon ~90 meV) |
| THREED_TC_LEVER | 1.84 |

**The energy verdict is fixed before any cleanliness argument:** a clean glue must deliver a sharp,
q≈0-coupling, **≥349 meV** boson to reach room-T with the campaign's 3D lever. A 90–100 meV interface phonon
— even with the 3D lever — tops out at **~76–84 K**. The single-magnon cuprate scale (~300 meV) lands at
~252 K (the H_020 wall). Only the cuprate bimagnon/multimagnon (~500 meV) crosses 349 meV, and that is a
two-particle continuum, not a sharp single boson. Keep this ceiling in mind for every 🟢/🟠 below.

---

## §1 — Family 1: SPIN-FLUCTUATION / PARAMAGNON glue (the strongest CLEAN family) 🟢

**Cleanliness (filter 1): CLEAN — passes, with one caveat.** In the cuprates and Fe-based SCs the spin
fluctuation is the *pairing glue itself*, and SC and AF spin fluctuations **COEXIST** across the doped phase
diagram — SC appears precisely in the doped/fluctuating regime adjacent to (but not inside) the static AF
order. This is structurally different from the exciton/CDW trap: there the boson IS the order parameter whose
*presence kills SC*; here the boson (the fluctuation) is what *causes* SC, and only the *static long-range
order* (the un-fluctuated limit) competes. **Caveat:** the high-energy *paramagnon* still derives from the
same exchange J that drives the AF order (the sibling note `research-magnon-glue-2026-06-25.md` calls the
≥349 meV spin wave "the soft mode of the AF order"). So the family is clean in the *fluctuation* regime
(where real high-Tc SC lives) but the **sharp ≥349 meV mode requires cuprate-scale J = cuprate-scale AF
proximity** — clean enough to give the world's highest ambient Tc, but the highest single-magnon energy
(~300 meV) caps at ~252 K.

**Real pairing precedent (filter 2): the STRONGEST in this survey.**
- **Bulk high-Tc, real & measured:** cuprate Hg-1223 **Tc = 133–134 K at ambient** (three-decade ambient
  record) and **164 K at 31 GPa** [VERIFIED WebSearch], with d-wave pairing widely attributed to AF
  spin fluctuations (review arXiv:1611.07813; numerics Nat. Phys. 18, 1356 (2022) attribute ~half the SC to
  spin-fluctuation glue). Pressure-quenched ambient SC up to 151 K (PNAS 2025) [VERIFIED WebSearch]. The
  spin-fluctuation boson reaches ~300 meV single-magnon / ~500 meV bimagnon (cuprate RIXS; sibling note §2).
- **Proximity / interface SC induced by a magnetic layer's spin fluctuations — REAL & MEASURED (the +@ datum):**
  **TbMn6Sn6 / Au** kagome-magnet/metal heterostructure, **emergent interface Tc ≈ 3.6 K** (Au-capped (001);
  resistance drop at ~3.6 K) [VERIFIED WebSearch, Nat. Commun. 2023 / PMC10622413]. The *non-superconducting*
  kagome MAGNET induces SC in an adjacent *non-superconducting* normal metal — the exact +@ topology (B induces
  SC in A across an interface). SC is quasi-2D, hysteretic, coexists with the ferromagnetism → proposed
  spin-triplet / possibly chiral topological. **This is the ONLY real measured proximity-SC-from-a-boson-layer
  datum in the whole campaign**, and its glue (magnetic-layer spin fluctuations) is in THIS family.
- **Theory corpus (interface magnon → SC), all peer-reviewed:** arXiv:1903.01470 (AF squeezed magnons →
  p-wave triplet at an interface); 1912.07607 (TI surface + AF magnons); 1712.02983 (magnon-induced SC
  COEXISTING with magnetism). These predict only ≳1 K p-wave at the interface — the energy is there but the
  *interface* Tc is low.

**Energy vs the room-T demand.** Single-magnon ~300 meV → ~252 K (sub-293, the H_020 wall). Bimagnon ~500 meV
→ 419 K (clears with margin) **but it is a two-particle continuum, not a sharp single boson** — usable as a
glue only if a sharp ≥349 meV single mode exists, which in cuprates it does not. The measured *interface*
precedent (TbMn6Sn6/Au) is real but **Tc ≈ 3.6 K**, three orders below room-T.

**§1 verdict: 🟢 CLEAN + REAL-PRECEDENT — but ambient-Tc-capped.** The single best CLEAN glue family: it is the
only one with BOTH a real high-Tc bulk precedent (134 K ambient) AND a real measured proximity/interface SC in
the +@ topology (TbMn6Sn6/Au, 3.6 K). It cleanly beats the Ta2NiSe5 exciton on both filters. **But** its sharp
single boson caps at ~300 meV (~252 K) — it does NOT reach the 349 meV room-T demand; the only thing that
crosses is the non-sharp ~500 meV bimagnon continuum.

---

## §2 — Family 2: POLAR-PHONON / FRÖHLICH INTERFACE glue (the cleanest, but low-energy) 🟠

**Cleanliness (filter 1): CLEANEST in the survey.** An interface optical phonon is NOT the soft mode of any
competing order — SrTiO3's polar phonon does not gap the Fermi surface or pre-empt SC; it BOOSTS the adjacent
metal's pairing. No CDW/SDW/EI is destroyed to turn SC on. Passes filter 1 outright.

**Real pairing precedent (filter 2): REAL, MEASURED, and the cleanest interface-glue datum.**
- **FeSe / SrTiO3 (monolayer):** interface Tc enhanced to **~65 K** (some reports 60–100 K) vs ~8 K for bulk
  FeSe [VERIFIED WebSearch]. **Phonon replica bands** in ARPES are interpreted as FeSe electrons coupling to a
  **SrTiO3 optical-oxygen phonon (~90–100 meV)** with strong **forward-scattering (small-q) peak** — the
  small-q character is what makes a modest λ so Tc-effective (Nat. Commun. ncomms14468; New J. Phys. 18,
  022001; arXiv:1607.00843) [VERIFIED WebSearch]. arXiv:2101.08307 explicitly attributes the Tc to a
  COMBINATION: a spin-fluctuation incipient-s± base (Tc ≈ 46.8 K) **further enhanced** by forward-scattering
  phonons [VERIFIED WebFetch — quote in §6]. So FeSe/STO is *both* a clean interface-phonon datum AND a
  spin-fluctuation datum.
- **LaAlO3 / SrTiO3 interface 2DEG SC** (Reyren 2007, Tc ≈ 0.2–0.3 K) — same STO polar-phonon clean-glue
  family, much lower Tc [LIT-ESTABLISHED].
- **FeSe / LaFeO3** interface (Nat. Commun. s41467-021-26201-2) — related high-Tc interface result
  [VERIFIED WebSearch link].

**Energy vs the room-T demand.** The STO polar phonon is ~90–100 meV. With the 3D lever, `stacked_tc(90,True)`
= **75.49 K**, `stacked_tc(100,True)` = **83.88 K** — i.e. even a perfect 100 meV clean interface phonon tops
out at ~84 K. FeSe/STO's measured ~65 K is consistent with this scale. **This family is demonstrably the
cleanest and most real, but it is ~3.5× too low in energy to reach room-T.**

**§2 verdict: 🟠 CLEAN-BUT-LOW-ENERGY.** The most unambiguous clean glue with the most unambiguous real
interface-SC precedent (FeSe/STO, ~65 K) — but the boson is ~90–100 meV (room-T ceiling ~84 K). It is the
honest *floor* of the clean map: real, clean, but energy-capped well below 293 K.

---

## §3 — Family 3: PLASMON / ACOUSTIC-PLASMON glue 🟠 (clean, but no MEASURED SC link)

**Cleanliness (filter 1): CLEAN.** A plasmon is a charge oscillation carrying NO intrinsic CDW/SDW/EI order —
structurally the cleanest *energy-scalable* boson (sibling note `research-engineered-plasmon-glue-2026-06-25.md`).
Passes filter 1.

**Real pairing precedent (filter 2): NONE measured.** This is the family's fatal gap. Plasmon-mediated SC is
an entirely *computed* program — in 't Veld–Katsnelson–Millis–Rösner (arXiv:2508.06195, 2303.06220;
Rösner 1803.04576) enhance plasmon-mediated Tc "by up to an order of magnitude" **in theory**, and
2508.06195 closes by literally calling for *experimental verification that does not yet exist*. No measured
plasmon-mediated SC, in any geometry, was found [VERIFIED §2 sibling note; this session re-confirmed no new
measured datum]. Acoustic graphene plasmons are real and low-loss but **sub-0.2 eV** (lower branch by
construction) and carry no SC measurement.

**Energy vs the room-T demand.** In principle the layered-metal / dynamical-Coulomb plasmon is *tunable* to
≥349 meV — but only on paper, and a measured sharp ≥349 meV low-loss plasmon does not exist (graphene
plasmons cap at ~0.2 eV before Q collapses; sibling note §2).

**§3 verdict: 🟠 CLEAN-BUT-INDIRECT (no measured SC).** Passes filter 1 and is the only clean boson that is
*energy-scalable in principle*, but it FAILS filter 2 outright — zero measured SC precedent. It is a design
proposal, not a real glue.

---

## §4 — Family 4: OTHER clean high-energy bosons (hydride optical phonons, bipolaron/Fröhlich) 🟠/🔴

**Hydride optical phonons — the only REAL >200 K class, but high-pressure & not a +@ interface glue.**
- LaH10 **Tc ≈ 250–260 K @ ~170 GPa**; H3S ~203 K @ ~155 GPa; the boson is the **H optical phonon at
  ~100–200 meV** with enormous λ [LIT-ESTABLISHED, the campaign's `state/exports/.../Li2MgH16` lineage].
- **Cleanliness (filter 1): CLEAN** — the H-phonon is the pairing glue and is not a competing-order soft mode
  (the structural instabilities are stabilized *by* the pressure that enables SC; the phonon does not gap the
  FS). Passes filter 1.
- **Real precedent (filter 2): REAL and the highest measured Tc anywhere** — BUT it is a *bulk pressure*
  mechanism, not a proximity/interface glue, and it requires ~150–200 GPa. It does not transplant into the
  +@ trilayer geometry: you cannot proximity-couple a 170 GPa hydride phonon across an hBN spacer to a
  flat-band metal at 1 atm. **Off-geometry, not off-mechanism.**
- **§4a verdict: 🟠** — clean + real + high-Tc, but high-pressure & geometrically incompatible with +@.

**Bipolaron / Fröhlich (strong-coupling polaron) — clean mechanism, no high-Tc real precedent.**
- Strong electron–phonon (Fröhlich) coupling → real-space bipolarons → BEC-like SC (Alexandrov–Mott program)
  [LIT-ESTABLISHED]. Clean (a polaron is not a competing-order soft mode). But no *measured* high-Tc bipolaron
  SC at the room-T scale; the real bipolaronic candidates (e.g. some oxides) are low-Tc.
- **§4b verdict: 🔴-leaning** (clean mechanism, but no real high-Tc precedent; energy not demonstrably ≥349 meV
  in a usable mode).

**The two TRAP families (for contrast, 🔴):**
- **Excitonic-insulator exciton (Ta2NiSe5)** — the lead the campaign must replace: **🔴 TRAP** — the exciton is
  the q=0 EI order parameter; Ta2NiSe5 superconducts only once it is DESTROYED (arXiv:2106.04396), and 50 years
  of proximity-EI-SC are unmeasured (prior-art pass).
- **1T-TiSe2 exciton/CDW** — **🔴 TRAP** — the ~400 meV boson IS the CDW order parameter (sibling note;
  arXiv:2210.14635); the glue is entangled with the order that suppresses SC.

---

## §5 — Ranked CLEAN-glue table (cleanliness × real-SC-precedent × boson energy)

Ranked by (filter-1 cleanliness) × (filter-2 real SC precedent, with Tc) × (boson energy reach toward 349 meV).

| Rank | Family / material | Boson | Boson energy | Competing-order soft mode? (filter 1) | Real SC precedent? (filter 2, Tc) | +@ interface geometry? | Reaches 349 meV (room-T)? | Verdict |
|---|---|---|---|---|---|---|---|---|
| **1** | **Spin-fluctuation / paramagnon (cuprate-class)** | AF spin fluctuation / paramagnon | single ~300 meV; bimagnon ~500 meV (continuum) | **NO** — fluctuation CAUSES SC, coexists; only static order competes (clean caveat: high-E mode tied to J) | **YES, strongest:** cuprate 134 K ambient / 164 K @31GPa; **+@ interface TbMn6Sn6/Au 3.6 K (measured)** | **YES** (TbMn6Sn6/Au is the +@ topology) | **NO** (sharp single ~300 meV→252 K; only non-sharp 500 meV crosses) | **🟢** |
| **2** | **Polar-phonon / Fröhlich interface (FeSe/STO)** | SrTiO3 optical phonon (forward-scattering) | ~90–100 meV | **NO** — phonon boosts, no order destroyed | **YES, measured:** FeSe/STO ~65 K (from ~8 K bulk); LAO/STO ~0.3 K | **YES** (interface glue by definition) | **NO** (90–100 meV → 76–84 K ceiling) | **🟠** |
| 3 | **Plasmon / acoustic-plasmon** | charge-density plasmon | sub-0.2 eV measured; ≥349 meV theory-only | **NO** — no intrinsic density wave | **NO measured SC** (theory only, 2508.06195 calls for verification) | tunable (theory) | only in theory | **🟠** |
| 4a | **Hydride optical phonon (LaH10/H3S)** | H optical phonon | ~100–200 meV | **NO** — clean glue | **YES, highest Tc:** LaH10 ~250–260 K @170 GPa | **NO** — bulk high-pressure, not transplantable to +@ | n/a (room-T only at ~170 GPa) | **🟠** (off-geometry) |
| 4b | Bipolaron / Fröhlich (strong-coupling) | polaron/bipolaron | mode-dependent | NO — clean | **NO high-Tc measured** | maybe | unproven | 🔴-leaning |
| — | Ta2NiSe5 exciton (LEAD TO REPLACE) | EI exciton/Higgs | ~300 meV (gap 0.16–0.35 eV) | **YES — IS the q=0 EI order parameter; SC only when DESTROYED** | **NO** (50 yr unmeasured; pressure-SC is phonon, EI gone) | proposed | n/a | **🔴 TRAP** |
| — | 1T-TiSe2 exciton/CDW | exciton-CDW | ~400 meV | **YES — IS the CDW order parameter** | NO (glue entangled with CDW) | proposed | n/a | **🔴 TRAP** |

**Per-family 🟢/🟠/🔴:** Spin-fluctuation 🟢 · Polar-phonon interface 🟠 · Plasmon 🟠 · Hydride-phonon 🟠
(off-geometry) · Bipolaron 🔴-leaning · [traps: exciton-EI 🔴, exciton-CDW 🔴].

---

## §6 — Proposed registry rows (Layer B; for the main loop to fold into `tool/rtsc_candidates.py` — do NOT self-merge)

Schema mirrors `Candidate` (`role`, `boson_meV`, `competing_order=(value,source,verified)`). All rows:
absorbed=false, GATE_OPEN. `competing_order="none"` is the harness's CLEAN pass condition (FB2). Energies are
VERIFIED where a primary abstract was confirmed this session; LIT-ESTABLISHED textbook values flagged unverified.

| name | role | boson_meV | competing_order | reaches_349_clean? | absorbed | citation | verified | claim_truth |
|---|---|---|---|---|---|---|---|---|
| cuprate-spin-fluctuation (La2CuO4/Hg1223-class) | B | 300 (single magnon; bimagnon ~500 continuum) | "none" (fluctuation CAUSES SC, coexists; static AF order competes only in un-fluctuated limit) | False (sharp single ~300→252K=H_020 wall; 500meV not a sharp boson) | false | Hg1223 134K ambient/164K@31GPa [VERIFIED WebSearch]; review arXiv:1611.07813; Nat.Phys.18,1356(2022) | True(clean-glue+real-high-Tc); False(sharp≥349) | CLEAN ✓, real precedent ✓, energy ✗ |
| TbMn6Sn6/Au (kagome-magnet/metal interface SC) | B | spin-fluctuation (interface) | "none" (magnetic-fluctuation glue; SC coexists w/ FM, quasi-2D, spin-triplet) | False (real Tc≈3.6K, far below room-T) | false | Nat.Commun.2023 / PMC10622413 [VERIFIED WebSearch] | True(CLEAN + only REAL +@-geometry proximity-SC datum) | THE +@ datum: clean ✓, measured proximity-SC ✓, Tc low |
| FeSe/SrTiO3 (polar-phonon interface glue) | B | 100 (STO forward-scattering optical phonon ~90–100meV) | "none" (phonon boosts Tc; no competing order destroyed) | False (90–100meV → 76–84K ceiling) | false | ncomms14468; NJP18,022001; arXiv:2101.08307 (spin-fluc 46.8K + fwd phonon→~65K) [VERIFIED WebFetch/WebSearch] | True(CLEAN + measured interface SC ~65K); False(energy) | cleanest+real, but low-energy |
| layered-metal plasmon (dyn-Coulomb, NbS2/TMD) | B | 349 (reachable IN THEORY; measured ≤~200) | "none" (charge oscillation, no density wave) | False (computed only; no measured SC) | false | arXiv:2508.06195; 2303.06220; 1803.04576 [VERIFIED sibling note] | True(clean,tunable-in-theory); False(measured-SC, measured-energy) | clean but no measured SC |
| LaH10 (hydride H-optical-phonon) | B | 150 (H optical phonon ~100–200meV) | "none" (clean glue; structural instab. stabilized by pressure) | False (off-geometry: 170GPa bulk, not +@-transplantable) | false | LaH10 ~250–260K@170GPa [LIT-ESTABLISHED] | False(verified-for-+@); True(clean-mechanism, real-bulk-Tc) | clean+real+highTc but off-geometry/high-pressure |

(For contrast, the existing seed `Ta2NiSe5` row in `rtsc_candidates.py` currently carries
`competing_order=("none", …)` on the *q=0-non-nesting* argument — but the prior-art pass shows it is a
🔴 TRAP because the exciton, though q=0, is the order parameter whose *presence kills SC*; flagged here for the
main loop's attention, NOT edited.)

---

## §7 — VERDICT (one paragraph)

**Is there a CLEAN glue that beats Ta2NiSe5's exciton? YES — the SPIN-FLUCTUATION / paramagnon family.** It is
the single best clean-glue family: it is the ONLY family that passes BOTH filters with REAL measured data —
cleanliness (the spin fluctuation *causes* SC and coexists with it across the cuprate/Fe-based phase diagram,
unlike the exciton which *kills* SC when present) AND a real SC precedent that is simultaneously the world's
highest ambient Tc (cuprate Hg-1223, **134 K @ 1 atm**, 164 K @ 31 GPa) and the campaign's ONLY real
*proximity/interface* SC datum in the +@ topology (**TbMn6Sn6/Au kagome-magnet/metal, Tc ≈ 3.6 K**, where a
non-SC magnet induces SC in a non-SC metal across an interface). This decisively beats Ta2NiSe5's exciton,
which is a 🔴 trap on both filters (50-yr-unmeasured proximity-EI-SC + SC only once the exciton is destroyed).
**BUT — and this is the honest map — NO clean glue reaches the ~349 meV room-T demand.** The spin fluctuation's
sharp single boson caps at ~300 meV (→ ~252 K, the H_020 wall); only its non-sharp ~500 meV bimagnon continuum
crosses 349 meV, and a two-particle continuum is not the sharp single boson the glue argument needs. The polar-
phonon interface glue (FeSe/STO) is even cleaner and demonstrably real (~65 K) but is ~90–100 meV → a ~84 K
ceiling. The energy-scalable plasmon has NO measured SC, and the only real >200 K boson (hydride H-phonon,
~250–260 K) is a 170 GPa *bulk* mechanism that does not transplant into the +@ interface geometry. **Cost to
the +@ trio of swapping in the best clean glue (spin-fluctuation, e.g. a high-J magnetic layer B):** you trade
Ta2NiSe5's fatal competing-order trap for a glue that is genuinely clean and has a real measured proximity-SC
precedent — but you accept a sharp-boson energy ceiling of ~300 meV (~252 K), i.e. **a clean glue buys
honesty and a real mechanism, not room temperature.** Every clean glue is LOW-energy relative to the 349 meV
demand: spin-fluctuation ~300 meV (ambient-Tc-capped), interface-phonon ~90–100 meV. `absorbed=false` /
GATE_OPEN unchanged. No material is claimed to BE an RTSC.

---

## §8 — Citations (load-bearing; verified this session unless marked LIT-ESTABLISHED)

- **PMC10622413 / Nat. Commun. (2023)** — "Emergent superconductivity in topological-kagome-magnet/metal
  heterostructures" — TbMn6Sn6/Au, **measured interface Tc ≈ 3.6 K**, quasi-2D, coexists w/ FM, spin-triplet.
  [VERIFIED WebSearch — THE only real +@-geometry proximity-SC datum.]
- **arXiv:2101.08307** — "Enhanced superconductivity in FeSe/SrTiO3 from the combination of forward scattering
  phonons and spin fluctuations" — spin-fluctuation base Tc ≈ 46.8 K + forward-scattering phonon enhancement.
  [VERIFIED WebFetch — abstract quote.]
- **Nat. Commun. ncomms14468** — "Ubiquitous strong electron–phonon coupling at the interface of FeSe/SrTiO3"
  — replica bands ← STO optical phonon, forward-scattering. [VERIFIED WebSearch.]
- **New J. Phys. 18, 022001 (2016) / arXiv:1607.00843** — forward-scattering e-ph peak dominant in FeSe/STO
  high-Tc. [VERIFIED WebSearch.]
- **Nat. Commun. s41467-021-26201-2** — "High temperature superconductivity at FeSe/LaFeO3 interface."
  [VERIFIED WebSearch link.]
- **Cuprate Tc records:** Hg-1223 **134 K ambient** (three-decade record), **164 K @ 31 GPa**; pressure-quench
  ambient 151 K (PNAS 2025). [VERIFIED WebSearch.]
- **arXiv:1611.07813** — "Spin fluctuations and high-temperature superconductivity in cuprates" (Phys. Rep.
  review — AF spin fluctuations as d-wave glue). [VERIFIED prior sibling note WebSearch.]
- **Nat. Phys. 18, 1356 (2022)** — ~half of doped-Hubbard SC attributable to spin-fluctuation glue. [sibling note.]
- **arXiv:1903.01470 / 1912.07607 / 1712.02983** — interface AF-magnon → SC theory (p-wave triplet, coexists
  w/ magnetism). [VERIFIED sibling magnon note.]
- **arXiv:2106.04396** — Ta2NiSe5 pressure-SC (Tc≈1.2K@8GPa, EI destroyed, phonon-mediated). [KEY NEGATIVE for
  the exciton lead; VERIFIED prior-art pass.]
- **arXiv:2210.14635** — 1T-TiSe2 plasmon tied to CDW gap (exciton-IS-CDW trap). [VERIFIED sibling note.]
- **arXiv:2508.06195 / 2303.06220 / 1803.04576** — plasmonic SC (THEORY; calls for experimental verification).
  [VERIFIED sibling plasmon note.]
- **LaH10 / H3S** — Tc ≈ 250–260 K @ ~170 GPa / 203 K @ 155 GPa, H optical-phonon glue. [LIT-ESTABLISHED.]

**Honesty note.** No fabricated citations. Tc / energy / pressure numbers are as reported by the cited works via
web/WebFetch (not re-derived). The 🟢-for-spin-fluctuation-but-energy-capped verdict is the honest reading: a
clean glue with a real measured proximity-SC precedent EXISTS and beats the Ta2NiSe5 exciton trap, but NO clean
glue reaches the 349 meV room-T demand. absorbed=false / GATE_OPEN throughout.
