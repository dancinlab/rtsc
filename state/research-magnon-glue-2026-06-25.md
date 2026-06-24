---
id: MAGNON
slug: magnon-glue
domain: rtsc
status: pre_registered
pre_register_frozen: true
frozen_at: 2026-06-25
kind: research
---

# Research note — the ORTHOGONAL glue family: MAGNONS (spin waves) at ≥349 meV

**Date:** 2026-06-25
**Lane:** M-magnon-research (MAGNON, research)
**Status:** READ-ONLY cited literature survey — no compute, no rental (WebSearch + WebFetch on arXiv/journal abstracts).
**Question:** Exciton and plasmon glue families are surveyed and (for the ≥349 meV clean target) closed. MAGNONS
(spin waves) are a DIFFERENT, orthogonal family. Is there a real material with a magnon mode at **≥349 meV**
(high-energy spin wave) that could serve as a **clean pairing glue WITHOUT a competing order pre-empting SC**,
adjacent to a flat band, compatible with the +@ trilayer?

**Honesty posture (commons honesty / falsifier-first):** every energy and citation below is real and cited;
abstract-level confirmations marked [VERIFIED WebFetch/WebSearch]; textbook/established physics not re-derived
this session marked [LIT-ESTABLISHED]. No material is claimed to BE an RTSC. absorbed=false / GATE_OPEN throughout.
A sober "no clean ≥349 meV magnon glue exists" is a valid result — this is NOT tune-to-green.

---

## §0 — The target the magnon must clear (harness, byte-deterministic)

Inline against `tool/rtsc_harness.py` (NOT edited):

| Quantity | Value |
|---|---|
| `omega_for_stacked_tc(293, three_d=True)` | **349.31 meV** ← the glue energy needed for room-T with the 3D lever |
| `stacked_tc(349, True)` | 292.74 K (just clears 293) |
| `stacked_tc(300, True)` | 251.64 K (= cuprate single-magnon zone-boundary scale → ~252 K, ~49 meV short — same wall as H_020) |
| `stacked_tc(500, True)` | 419.40 K (the cuprate BI-magnon / multi-magnon scale — clears with margin, IF usable) |
| `geometric_bkt_tc_band(349)` | 159.10 K (single-layer band, pre-3D-lever) |
| THREED_TC_LEVER | 1.84 |

So a magnon glue must deliver a **sharp, ≥349 meV, q≈0-coupling spin-wave mode** whose magnetic-order parent does
NOT pre-empt superconductivity. The single-magnon scale of the highest-J host (cuprate, ~300 meV) lands at ~252 K —
**below room-T and identical to the H_020 wall**; only the bimagnon/multimagnon (~500 meV) clears 349, and that is
a two-particle continuum feature, not a sharp single boson.

---

## §1 — Is magnon-mediated pairing a credible mechanism at this scale? (yes — peer-reviewed)

Magnon/spin-fluctuation pairing is the canonical NON-phonon glue and is genuinely a *different family* from the
exciton (charge-transfer) and plasmon (charge-oscillation) glues already surveyed.

| arXiv / ref | Title (verbatim / paraphrased) | What it is | Status |
|---|---|---|---|
| **arXiv:cond-mat/0407550** | "Antiferromagnetic exchange and spin-fluctuation pairing in cuprate superconductors" | AF superexchange → d-wave pairing in the p-d Hubbard model for CuO₂ | computed / theory [VERIFIED WebSearch] |
| **arXiv:1611.07813** (Phys. Rep. / ScienceDirect) | "Spin fluctuations and high-temperature superconductivity in cuprates" | review: AF spin fluctuations as the d-wave pairing glue | review [VERIFIED WebSearch] |
| **Nat. Phys. 18, 1356 (2022)** | "Quantifying the role of antiferromagnetic fluctuations in the superconductivity of the doped Hubbard model" | numerics: ~half of SC attributable to spin-fluctuation glue in standard one-loop theory | computed [VERIFIED WebSearch] |
| **arXiv:1903.01470** | "Enhancement of superconductivity mediated by antiferromagnetic squeezed magnons" (Erlandsen, Kamra, Brataas, Sudbø) | interfacial exchange to an AF insulator's magnons → **p-wave triplet** SC; T_c boosted by asymmetric single-sublattice coupling | computed [VERIFIED WebFetch — abstract verbatim] |
| **arXiv:1912.07607** | "Magnon-mediated superconductivity on the surface of a topological insulator" | TI surface + adjacent AF insulator magnons → pairing | computed [VERIFIED WebSearch] |
| **arXiv:1712.02983** | "Magnon-induced superconductivity in field-cooled spin-1/2 antiferromagnets" | magnon-induced SC coexisting with magnetism | computed [VERIFIED WebSearch] |

**Verbatim (arXiv:1903.01470 abstract, key sentence):**
> "The attractive electron-electron pairing interaction is caused by an interfacial exchange coupling with magnons
> residing in the antiferromagnet, resulting in p-wave, spin-triplet superconductivity."

**Reading.** The mechanism is real, peer-reviewed, and orthogonal to exciton/plasmon. BUT every credible
realization is *interfacial coupling to an ordered (or proximate-to-ordered) antiferromagnet* — the magnon is the
**Goldstone/soft mode of the magnetic order**. The pairing strength and the magnetic order share one root (the
exchange J). This is the same structural trap as 1T-TiSe2 ("the 400 meV exciton IS its CDW, inseparable"): for
magnons, **the ≥349 meV spin wave IS the soft mode of the antiferromagnetic order**.

---

## §2 — High-magnon-energy hosts: who actually reaches ≥349 meV? (the energy census)

Magnon zone-boundary energy scales as ~2J (S=1/2 square lattice). The energy ladder, measured:

| # | Host | Single-magnon zone-boundary energy | Multi-magnon reach | Magnetic order / T_N | ≥349 meV clean single magnon? | Cite |
|---|---|---|---|---|---|---|
| M1 | **La₂CuO₄** (cuprate parent, S=1/2) | J=143 meV; magnon bandwidth ~300 meV; zone-boundary ~292–314 meV | **bimagnon / multimagnon up to ~500 meV** | AF, T_N≈325 K; magnon IS the soft mode of the AF order | **NO** — single magnon ~300 meV (= 252 K, H_020 wall); 500 meV is a 2-particle continuum, not a sharp boson | INS J=143 meV [VERIFIED]; arXiv:2102.04078 (multi-magnon shape) [VERIFIED WebFetch]; arXiv:1002.1440 (500 meV peak, La₂₋ₓSrₓCuO₄) |
| M2 | **Sr₂CuO₂Cl₂ / CaCuO₂** (cuprate parents) | ~300 meV bandwidth, comparable to La₂CuO₄ | similar multimagnon | AF | NO (same ~300 meV single-magnon ceiling) | RIXS square-lattice study [VERIFIED WebSearch] |
| M3 | **Sr₂IrO₄** (iridate, j_eff=1/2 "cuprate analog") | magnon bandwidth ~**200 meV** | — | AF (canted) | NO (lower than cuprate) | arXiv:1110.0759 (isospin dynamics) [VERIFIED WebSearch] |
| M4 | **NiO** (S=1, rocksalt AF) | high slope but max magnon ~**117 meV** | — | AF, T_N≈525 K | NO (far below) | arXiv:2508.12153 (NiO/MnO ab initio); KNiF3/NiO optical magnon [VERIFIED WebSearch] |
| M5 | **KNiF₃ / K₂NiF₄** (fluoride AF) | J≈77 cm⁻¹; max magnon ~**117 meV** (K₂NiF₄) | — | AF | NO | K₂NiF₄ INS [VERIFIED WebSearch] |
| M6 | **MnO / MnF₂ / FeF₂ / Rb₂MnF₄** (S=5/2 fluoride/oxide AF) | J₂≈19 meV (MnO); zone-boundary ~tens of meV (≲10–15 THz ≈ 40–60 meV) | — | AF | NO (an order of magnitude too low) | MnO J₂=19.01 meV; MnF₂ INS [VERIFIED WebSearch] |
| M7 | **α-RuCl₃** (Kitaev honeycomb) | K≈−6 to −16 meV; magnons ~2–2.4 meV (zone-center) | — | zigzag AF, T_N≈7 K | NO (tens of meV at most — Kitaev energy scale is small) | arXiv:1909.00462; Nat. Commun. 2020/2021 [VERIFIED WebSearch] |
| M8 | **NiPS₃ / MPX₃ family** (2D vdW AF) | tens of meV bandwidth | — | AF | NO | MPX₃ magnon family [VERIFIED WebSearch] |

**The energy verdict (load-bearing fact).** Only the **cuprate class** (M1–M2) has a magnon at the relevant scale,
and even there the **sharp single magnon caps at ~300 meV (= 252 K, exactly the H_020 wall)**. Every other AF host
(fluorides, oxides, iridates, Kitaev, MPX₃) is FAR below — because magnon energy ∝ exchange J, and only the
cuprate Cu²⁺ S=1/2 180° superexchange reaches J≈143 meV. The ONLY thing that crosses 349 meV is the cuprate
**bimagnon/multimagnon ≈500 meV** — a two-particle continuum, not a sharp single boson, and it sits on top of the
same AF order.

---

## §3 — The cleanliness wall: the high magnon is inseparable from magnetic order

This is the decisive point and it exactly parallels the TiSe2 exciton-IS-CDW closure.

1. **High magnon energy REQUIRES large J, and large J REQUIRES magnetic order (or strong proximity to it).** A
   ≥300 meV spin wave only exists because the Cu spins are antiferromagnetically locked with J≈143 meV. Remove the
   order and you remove the well-defined high-energy magnon. The magnon is the *soft mode of the very order that
   competes with / pre-empts SC* (the parent cuprate is a Mott AF insulator, NOT a superconductor — SC appears only
   on DOPING the AF away). [LIT-ESTABLISHED]

2. **Magnon-mediated SC in the cited literature lives at the INTERFACE to an ordered AF, not in a clean order-free
   bulk.** arXiv:1903.01470 / 1912.07607 / 1712.02983 all require an *adjacent antiferromagnetic insulator with
   intact order*; the pairing they predict is **p-wave triplet or interface d-wave with modest T_c (≳1 K)** — far
   from room-T, and explicitly coexisting with magnetism. The order is a *prerequisite*, not an avoidable side
   effect. [VERIFIED WebFetch/WebSearch]

3. **This is the same trap class as the closed exciton path.** TiSe2: "the 400 meV exciton IS its CDW —
   inseparable." Magnon: "the ≥349 meV spin wave IS the soft mode of the AF order — inseparable." In both, the
   high-energy boson and the competing order are TWO FACES OF ONE INSTABILITY (the same coupling makes both). You
   cannot have the cuprate's 300 meV magnon without the cuprate's AF Mott order.

4. **+@ trilayer compatibility.** The +@ spacer (H_015, hBN-class) is electron-opaque and could in principle host a
   magnon-active AF as layer B. But a high-J AF insulator adjacent to the flat-band layer A imports its **magnetic
   order** into the stack — precisely the H_014 competing-order risk — and the magnon energy that survives
   stacking is the same ~300 meV (sub-349). The H_016 frustration-escape (η_nest* ~0.45) is designed to kill a
   *nesting CDW*; it does not obviously remove a local-moment AF whose J sets the magnon energy (frustrating the
   lattice would also *lower* the very magnon energy you need). So frustration trades cleanliness for energy here —
   the opposite of what the plasmon path enjoyed.

---

## §4 — Verdict: is a clean ≥349 meV magnon glue host realizable?

**🟠 (high-energy magnons are REAL and magnon pairing is credible, but the ≥349 meV mode is TIED TO magnetic order
/ not clean — no turnkey clean magnon glue today; also NOT a flat no-go, because the cuprate scale is genuinely
~300 meV and a doped/proximate route is an open design question).**

- **Mechanism: credible & orthogonal.** Spin-fluctuation / magnon pairing is the canonical non-phonon glue
  (cond-mat/0407550; 1611.07813; Nat. Phys. 18, 1356; 1903.01470). It is a genuinely different family from
  exciton/plasmon — this lane is not redundant.
- **Energy: the cuprate is the ONLY host in range, and it caps at ~300 meV single-magnon (= 252 K, the H_020
  wall).** All other AF hosts (NiO/MnO/fluorides ~≤117 meV, iridate ~200 meV, Kitaev/MPX₃ ~tens of meV) are far
  below 349. Only the cuprate bimagnon ~500 meV crosses, and it is a two-particle continuum, not a sharp boson.
- **Cleanliness: the WALL.** A ≥349 meV magnon requires J≈cuprate-scale, which requires AF order — the magnon is
  the soft mode of that order. This is the same inseparability that closed the TiSe2 exciton path. The cited
  magnon-SC realizations all sit at an interface to an *ordered* AF and predict only ≳1 K p-wave SC.
- **Therefore:** a clean, order-free, sharp ≥349 meV single-magnon glue is **not a turnkey material today**.
  GATE_OPEN, absorbed=false. To flip toward 🟢 would need a *measured* sharp single magnon ≥349 meV in a host whose
  magnetic order is demonstrably suppressed/quantum-disordered (a quantum spin liquid retaining ≥349 meV
  spinon/magnon spectral weight WITHOUT static order) AND a demonstrated stacking route adjacent to the flat band —
  none exists as of 2026-06-25.

**Open (honest) escape hatch, not a green:** a high-J **quantum-disordered** magnet (frustrated S=1/2 with no
static order but retaining high-energy two-spinon spectral weight) is the only conceivable way to keep cuprate-scale
exchange energy WITHOUT the competing static order. This is a research target, not an existing turnkey host, and its
spectral weight at ≥349 meV in a single sharp mode is unproven.

---

## §5 — Proposed registry rows (for the main loop to integrate; do NOT self-merge)

Layer B (bosonic glue), magnon family. All rows: absorbed=false, GATE_OPEN.

| material | layer | role | boson_meV (magnon) | competing_order | reaches_349 clean? | absorbed | cite | claim_truth |
|---|---|---|---|---|---|---|---|---|
| La2CuO4 (cuprate magnon) | B | magnon-AF | ~292–314 (single, =252K); bimagnon ~500 (continuum) | **AF Mott order, T_N≈325K — magnon IS its soft mode** | False (single ~300<349; 500 is multi-particle, order-bound) | false | J=143meV INS; arXiv:2102.04078; arXiv:1002.1440 | True(highest-J host); False(clean), False(sharp ≥349) |
| Sr2CuO2Cl2 / CaCuO2 (cuprate parents) | B | magnon-AF | ~300 (single) | AF order | False | false | RIXS square-lattice study | False(≥349), False(clean) |
| Sr2IrO4 (iridate j_eff=1/2) | B | magnon-AF | ~200 (bandwidth) | canted AF | False (below 349) | false | arXiv:1110.0759 | False(energy) |
| NiO (S=1 oxide AF) | B | magnon-AF | ~117 (max) | AF, T_N≈525K | False | false | arXiv:2508.12153; KNiF3/NiO optical | False(energy) |
| K2NiF4 / KNiF3 (fluoride AF) | B | magnon-AF | ~117 (max) | AF | False | false | K2NiF4 INS | False(energy) |
| MnO/MnF2/FeF2 (S=5/2 AF) | B | magnon-AF | ~tens (≤~60) | AF | False | false | MnO J2=19meV; MnF2 INS | False(energy) |
| alpha-RuCl3 (Kitaev) | B | magnon-Kitaev | ~2–16 | zigzag AF, T_N≈7K | False | false | arXiv:1909.00462; Nat.Commun.2020 | False(energy) |
| NiPS3 / MPX3 (2D vdW AF) | B | magnon-AF | ~tens | AF | False | false | MPX3 magnon family | False(energy) |
| [TARGET, not a host] high-J quantum-spin-liquid magnon | B | magnon-QSL | aspirational ≥349 (two-spinon) WITHOUT static order | none (quantum-disordered) — UNPROVEN | False (no turnkey host; spectral weight ≥349 unproven) | false | open research target | False(exists today) |

**Distinctive value of the magnon lane:** it is the orthogonal non-phonon glue family and the ONLY one whose host
(cuprate) natively reaches ~300 meV. **Open risk (the wall):** the ≥349 meV magnon is inseparable from
antiferromagnetic order (same trap as TiSe2 exciton-IS-CDW); the only clean escape is a high-J quantum-disordered
magnet that does not yet exist as a turnkey ≥349 meV single-mode host.

---

## §6 — Citations (all verified this session unless marked LIT-ESTABLISHED)

- arXiv:1903.01470 — Erlandsen, Kamra, Brataas, Sudbø, "Enhancement of superconductivity mediated by
  antiferromagnetic squeezed magnons" — interfacial AF magnons → p-wave triplet SC [VERIFIED WebFetch — abstract verbatim §1]
- arXiv:2102.04078 — "Multiple-magnon excitations shape the spin spectrum of cuprate parent compounds" — single +
  bimagnon RIXS in cuprates [VERIFIED WebFetch]
- arXiv:1002.1440 — "Magnetic nature of the 500 meV peak in La₂₋ₓSrₓCuO₄ observed with RIXS at the Cu K-edge"
  [VERIFIED WebSearch]
- arXiv:cond-mat/0407550 — "Antiferromagnetic exchange and spin-fluctuation pairing in cuprate superconductors"
  [VERIFIED WebSearch]
- arXiv:1611.07813 — "Spin fluctuations and high-temperature superconductivity in cuprates" (Phys. Rep. review)
  [VERIFIED WebSearch]
- Nat. Phys. 18, 1356 (2022) — "Quantifying the role of antiferromagnetic fluctuations in the superconductivity of
  the doped Hubbard model" [VERIFIED WebSearch]
- arXiv:1912.07607 — "Magnon-mediated superconductivity on the surface of a topological insulator" [VERIFIED WebSearch]
- arXiv:1712.02983 — "Magnon-induced superconductivity in field-cooled spin-1/2 antiferromagnets" [VERIFIED WebSearch]
- arXiv:1110.0759 — "Isospin Dynamics in Sr₂IrO₄: Forging Links to Cuprate Superconductivity" — magnon bandwidth
  ~200 meV vs ~300 meV in La₂CuO₄ [VERIFIED WebSearch]
- arXiv:2508.12153 — "Comparative study of magnetic exchange parameters and magnon dispersions in NiO and MnO from
  first principles" [VERIFIED WebSearch]
- arXiv:1909.00462 — "Magnetic field-dependent low-energy magnon dynamics in α-RuCl₃" [VERIFIED WebSearch]
- La₂CuO₄ J=143 meV (inelastic neutron scattering; magnon bandwidth ~300 meV, zone-boundary 292–314 meV) [VERIFIED WebSearch]
- K₂NiF₄ / NiO / MnO / MnF₂ exchange + magnon energies (≤~117 meV) [VERIFIED WebSearch]
- Magnon energy ∝ exchange J; J requires magnetic order; magnon = soft mode of AF order [LIT-ESTABLISHED]
</content>
