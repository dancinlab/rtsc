# Research note — the PRESSURE-HYDRIDE axis: is room-T hydride SC pressure-locked, or is there an ambient-retention route?

**Date:** 2026-06-25
**Status:** READ-ONLY literature survey — no compute rented, no DFT/Eliashberg run. `absorbed=false`.
**Domain:** in-silico only (predict / screen / simulate / falsify). Physical synthesis + accredited
4-probe / Meissner measurement remain OUT OF DOMAIN (the lab gate).
**Why this note:** the SF-seed full triage (`state/sf_seed_full_triage_2026_06_25/triage.md`) flagged 7
"pressure-hydride-axis" seeds as a *real-but-different* axis from the now-frozen Emery-Kivelson
phase-stiffness wall (~134-164 K). Those seeds (muonic-hydride inversion, mediator-mass gradient
lattice, internal-negative-pressure cage, anharmonic cage freeze / SSCHA, epitaxial
pressure-equivalence, guest-charge doublet, host-guest sliding-chain boson) all route around the
spin-fluctuation stiffness wall via **conventional (phonon-mediated) hydride pairing on the
chemical-precompression / mediator-mass axis**. This note settles whether that axis is a LIVE
in-silico campaign or is ALSO walled.

**Honesty up front:** no material here is claimed to BE an RTSC. Both prior *near-ambient room-T*
hydride claims (CSH, Lu-N-H) were RETRACTED and are stated as such below. Numbers labelled
"predicted" are DFT+Eliashberg computations, NOT measurements.

---

## The framing: hydrides already reached room-T TEMPERATURE — but only at MEGABAR pressure

| System | Tc | Pressure | Status | Citation |
|---|---|---|---|---|
| H3S (Im-3m) | ~203 K | ~155 GPa | **Measured** | Drozdov et al., *Nature* **525**, 73 (2015), DOI 10.1038/nature14964 |
| LaH10 (Fm-3m) | ~250-260 K | ~170-190 GPa | **Measured** | Drozdov et al., *Nature* **569**, 528 (2019), DOI 10.1038/s41586-019-1201-8; Somayazulu et al., *PRL* **122**, 027001 (2019) |
| (La,Y)H10 | ~253 K | ~183 GPa | **Measured** | Semenok et al., arXiv:2012.04787 (*Mater. Today* 2021) |
| CSH ("carbonaceous sulfur hydride") | ~288 K (15 °C) claim | ~267 GPa | **RETRACTED** | Snider et al., *Nature* **586**, 373 (2020); **Retraction** *Nature* **610**, 804 (2022), DOI 10.1038/s41586-022-05294-9 |
| Lu-N-H ("reddmatter") | ~294 K claim | ~1 GPa | **RETRACTED** | Dasenbrock-Gammon et al., *Nature* **615**, 244 (2023); **Retraction** *Nature* **624**, 460 (2023), DOI 10.1038/s41586-023-06774-2 |

So the verified hydride record is ~250-260 K @ ~170-190 GPa, and **the wall is not phase-stiffness
— it is the PRESSURE wall**: the H sublattice needs megabar pressure to metallize and to supply the
high (~150-200 meV) phonon frequency that sets the conventional Tc. The two claims that broke the
pressure wall to near-ambient (CSH @ 267 GPa room-T, Lu-N-H @ 1 GPa room-T) were **both retracted**
(both from the Dias group; Lu-N-H independently un-reproduced — the Lu-H-N transition was shown to
be a metal-to-poor-conductor transition, not SC: arXiv:2307.00201). There is at present **NO
surviving experimental claim of high-Tc hydride SC at near-ambient pressure.**

---

## Q1 — Is room-T hydride SC intrinsically pressure-locked, or is there a metastable / chemically-precompressed route to ambient?

**Chemical precompression is real and DOES lower the required pressure — but not to ambient at high Tc.**
The idea (Ashcroft 2004) is that alloying H with another element internally "precompresses" the H
sublattice so it metallizes at lower external pressure. The best *computed* low-pressure high-Tc
result is the lanthanum borohydride family:

- **LaBH8** (Fm-3m, sodalite-like, [BH8] cage): predicted **Tc ~126 K @ 50 GPa**, thermodynamically
  stable above ~100 GPa, **dynamically stable down to ~40 GPa** — i.e. once made at ~110 GPa it can
  be *quenched / decompressed and metastably retained down to ~40 GPa* before the lattice goes
  dynamically unstable. Di Cataldo, Heil, von der Linden & Boeri, *PRB* **104**, L020511 (2021),
  arXiv:2102.11227. (Quantum-ionic / anharmonic corrections shift the stability window: Belli &
  Errea, arXiv:2206.07439.)
- **LaBeH8**: predicted dynamically stable down to ~20 GPa, Tc predicted ~185 K; **experimentally
  synthesized** with measured **Tc ~110 K @ 80 GPa** (Song et al., *PRL* 2023) — the first
  *crystallized* ternary-hydride SC template and the lowest-pressure *measured* high-Tc hydride to date.
- Metal-borohydride doping route (e.g. K-doped Ca(BH4)2, ~0.03 holes/f.u.): proposed as an
  *ambient-pressure* high-Tc (~110 K predicted) hydride. Di Cataldo & Boeri, arXiv:2207.05593 — but
  this is an **un-synthesized DFT prediction**; the ambient-pressure stability + doping is exactly
  the un-verified, hard step.

**The decisive ambient-pressure datum (the honest one):** a 2026 search of the GNoME
crystal-structure database for *thermodynamically stable* (on-convex-hull, conventionally
synthesizable-at-ambient) superconducting hydrides found the **highest Tc among truly
ambient-stable hydrides is only ~17 K (LiZrH6Ru)**, with the whole stable set in the **4-17 K**
range — and concluded that **"high-Tc values of the order of 100 K appear to be systematically
linked to some degree of thermodynamical instability."** (Cerqueira et al. / GNoME hydride search,
*Commun. Phys.* (2026), DOI 10.1038/s42005-026-02552-4.) The complementary "maximum Tc of
conventional superconductors at ambient pressure" analysis (*Nat. Commun.* **16** (2025), DOI
10.1038/s41467-025-63702-w) likewise places the *ambient* conventional-SC ceiling far below the
megabar hydride record.

**Answer Q1:** Decompression does NOT automatically destroy the SC H-sublattice — some computed
ternaries (LaBH8) are *metastably retainable* well below their synthesis pressure (down to ~40 GPa),
and chemical precompression genuinely buys ~100-150 GPa. **But there is a robust
stability-vs-Tc trade-off:** every hydride that is *thermodynamically stable at 1 atm* has low Tc
(≤~17 K computed, GNoME), and every high-Tc (~100-250 K) hydride is *metastable/unstable* and needs
tens-to-hundreds of GPa either to form or to avoid dynamical/decomposition instability. So room-T
hydride SC is **effectively pressure-locked at the ambient (1 atm) endpoint**: the ambient-retention
of high Tc is a *materials-existence / metastable-recovery* question that no one has yet demonstrated
(the only two near-ambient room-T claims, CSH and Lu-N-H, were retracted).

---

## Q2 — Lowest pressure at which any hydride keeps Tc ≥ 250 K? Is the trend bending toward ambient?

- **Lowest-pressure Tc ≥ 250 K datum (measured):** ~250-253 K at **~170-190 GPa** — LaH10 (Drozdov
  2019 / Somayazulu 2019) and (La,Y)H10 ~253 K @ ~183 GPa (Semenok, arXiv:2012.04787). No measured
  hydride keeps Tc ≥ 250 K below ~170 GPa.
- **The pressure trend for Tc ≥ 250 K is SATURATING near ~150-200 GPa, not bending to ambient.**
  Ternaries bend the curve for *moderate* Tc: the lowest-pressure *measured* high-Tc point is LaBeH8
  at ~110 K @ 80 GPa, and the best *computed* low-pressure point is LaBH8 ~126 K @ 50 GPa (stable to
  ~40 GPa). But the ≥250 K class has NOT moved below ~150 GPa in any measurement; the National
  Science Review ternary review (Du et al., *Natl. Sci. Rev.* **11**, nwae003 (2024), DOI
  10.1093/nsr/nwae003) describes the experimentally-confirmed pressure reduction as **plateauing
  around ~80-110 GPa for ~100-180 K**, with closing the gap to ambient still an "ultimate goal."
- Net: there are TWO frontiers, and they are anti-correlated — you can have **(a) ≥250 K but only at
  ≥150 GPa**, or **(b) lower pressure (40-80 GPa) but only ~110-185 K**. Nobody has both. The
  hydride record is room-T *temperature* (250-260 K) but never at room-T-relevant (ambient) pressure.

---

## Q3 — Is this axis IN-SILICO-tractable for us, and is it redundant with published databases?

**Tractable — yes, in principle, and importantly it is NOT the beyond-PBE glue problem** that walled
the excitonic/EI (electron-opacity) campaign. Hydride Tc is **conventional electron-phonon**, computed
by the well-established **DFT (DFPT) + Migdal-Eliashberg / Allen-Dynes** stack (QE → EPW for the
Eliashberg spectral function α²F(ω), then isotropic/anisotropic ME or McMillan-Allen-Dynes for Tc).
This is a *standard, validated* pipeline for hydrides (e.g. EPW anisotropic ME applied to superhydrides,
arXiv:2310.00056). Our summer QE + an Eliashberg solver could in principle compute a candidate ternary
hydride's Tc-vs-pressure curve.

**Three honest caveats that bound the tractability:**
1. **Anharmonicity / quantum nuclei are load-bearing, not optional.** Light H + flat anharmonic wells
   mean harmonic DFPT phonons are quantitatively wrong (and often spuriously stable/unstable). The
   field standard is **SSCHA** (stochastic self-consistent harmonic approximation) for the
   quantum-anharmonic phonons + dynamical-stability pressure, then ME on the SSCHA-renormalized α²F.
   Examples: LuH3 (Lucrezi et al., *Nat. Commun.* **15**, 441 (2024), DOI 10.1038/s41467-023-44326-4);
   LaBH8 quantum-ionic stability (arXiv:2206.07439). SSCHA adds a sizeable but feasible compute cost
   on top of plain DFPT — it is the part that would actually need a GPU/cluster budget, and per the
   `실측전 research` rule it should be gated on a literature check that the specific candidate isn't
   already done.
2. **The crux is dynamical-stability at low pressure, NOT Tc.** For known cages the Tc is already
   roughly known; the *open* in-silico question is the **metastable-retention window** — the lowest
   pressure at which a given ternary cage stays dynamically stable (no imaginary phonons) and on/near
   the convex hull. That is an SSCHA-phonon + convex-hull (formation-enthalpy) calculation, which is
   squarely in-silico-settleable.
3. **Redundancy risk is HIGH.** The published high-throughput hydride landscape is already dense:
   JARVIS-DFT hydride screen (arXiv:2312.12694, *Mater. Futures* 2024), the GNoME ambient-pressure
   search (DOI 10.1038/s42005-026-02552-4), curated 2059-record binary+ternary datasets
   (arXiv:2512.20228), and dedicated ternary-borohydride / La-X-H sweeps (npj Comput. Mater. 2022,
   DOI 10.1038/s41524-022-00801-y; DOI 10.1038/s41524-021-00691-6). A naive Tc-vs-P scan of a known
   cage would mostly **reproduce** these. A *non-redundant* in-silico contribution would have to target
   a gap they leave: specifically a **carded, honest SSCHA-based metastable-retention (decompression)
   window** for a *named* ternary cage, framed as a falsifiable prediction — which is precisely the
   kind of single-question micro-experiment our framework is built for, but it is a *narrow* opening,
   not a wide-open field.

**Answer Q3:** In-silico-tractable (conventional el-ph, not the EI beyond-PBE wall), but the
*scientifically honest* compute is SSCHA+ME on the **retention/stability window**, not a Tc scan —
and a Tc scan would be largely redundant with the published databases. The non-redundant slice is
small and is a *materials-stability* question, not a *new-pairing-mechanism* question.

---

## Honest verdict — is the pressure-hydride axis a LIVE in-silico campaign or ALSO walled?

**Mostly walled at the ambient (1 atm) endpoint — but walled differently from the EI graveyard, and
with one narrow live in-silico slice.** Unlike the now-frozen Emery-Kivelson phase-stiffness wall
(a *mechanism* ceiling on cuprate-class spin-fluctuation pairing) and unlike the excitonic/EI glue
wall (a *beyond-PBE computability* wall on whether the glue even exists), the hydride wall is a
**pressure / materials-existence wall**: the pairing mechanism is uncontested (conventional
electron-phonon, computable to good accuracy), the room-T *temperature* is genuinely reached (~250-260
K), and the *only* missing thing is keeping that H-sublattice metallic and dynamically stable at 1
atm. The literature is consistent and honest that this has NOT been achieved: the highest
*ambient-stable* hydride Tc is ~17 K (GNoME), high-Tc is "systematically linked to thermodynamical
instability," the Tc ≥ 250 K class has not dropped below ~170 GPa, and the two near-ambient room-T
claims (CSH, Lu-N-H) were both retracted. **So the ambient-retention of high-Tc hydride SC is, today,
a materials-existence wall analogous in *spirit* to the EI graveyard — the candidate that satisfies it
may simply not exist as a 1-atm-stable solid, and that endpoint (synthesis + measurement) is
OUT OF DOMAIN (the lab gate), never our failure.** What IS in-domain and live: a *single*, carded,
SSCHA+Eliashberg **metastable-decompression-window** prediction for a named ternary cage (LaBH8-class /
metal-borohydride-class) — a falsifiable "lowest pressure at which this cage stays dynamically stable
with Tc ≥ X" computation that the databases leave as a gap. That is a real but *narrow* in-silico
lever (one card, not a campaign), and it is partly redundant with published high-throughput sweeps.
**Recommendation:** open it only as a *single pre-registered card* (per the no-orphan-hypotheses rule)
with the honest-null built in — null = "the dynamical-stability window of every accessible
chemically-precompressed cage closes above the pressure where Tc stays high (stability and Tc are
anti-correlated), reproducing the published trade-off" — and gate any SSCHA GPU spend on a fresh
`실측전 research` check that the specific cage+pressure point isn't already published. **No material is
claimed to BE an RTSC; `absorbed=false` stands.**

---

## Sources (all confirmed via web search / publisher pages; arXiv ids and DOIs as cited)

- Drozdov et al., *Nature* **525**, 73 (2015) — H3S ~203 K @ ~155 GPa. DOI 10.1038/nature14964
- Drozdov et al., *Nature* **569**, 528 (2019); Somayazulu et al., *PRL* **122**, 027001 (2019) — LaH10 ~250-260 K @ ~170-190 GPa
- Semenok et al., arXiv:2012.04787 — (La,Y)H10 ~253 K @ ~183 GPa
- Snider et al., *Nature* **586**, 373 (2020) — CSH claim; **RETRACTED** *Nature* **610**, 804 (2022), DOI 10.1038/s41586-022-05294-9
- Dasenbrock-Gammon et al., *Nature* **615**, 244 (2023) — Lu-N-H near-ambient claim; **RETRACTED** *Nature* **624**, 460 (2023), DOI 10.1038/s41586-023-06774-2; un-reproduction arXiv:2307.00201
- Di Cataldo, Heil, von der Linden & Boeri, *PRB* **104**, L020511 (2021), arXiv:2102.11227 — LaBH8 ~126 K @ 50 GPa, dyn-stable to ~40 GPa
- Belli & Errea, arXiv:2206.07439 — quantum-ionic effects on LaBH8 stability
- Song et al., *PRL* (2023) — LaBeH8 measured Tc ~110 K @ 80 GPa (lowest-pressure measured high-Tc hydride)
- Di Cataldo & Boeri, arXiv:2207.05593 — K-doped Ca(BH4)2 borohydride, predicted ambient-pressure ~110 K (un-synthesized)
- Cerqueira et al. (GNoME ambient-pressure hydride search), *Commun. Phys.* (2026), DOI 10.1038/s42005-026-02552-4 — ambient-stable max Tc ~17 K (LiZrH6Ru); high-Tc ↔ thermodynamic instability
- *Nat. Commun.* **16** (2025), DOI 10.1038/s41467-025-63702-w — maximum Tc of conventional SC at ambient pressure
- Du et al., *Natl. Sci. Rev.* **11**, nwae003 (2024), DOI 10.1093/nsr/nwae003 — ternary superhydrides for high-Tc at low pressure (trend plateau ~80-110 GPa)
- Boeri et al., "2021 room-temperature superconductivity roadmap," *J. Phys.: Condens. Matter* (2022), PMID 34544070
- Choudhary & Garrity, arXiv:2312.12694, *Mater. Futures* (2024) — JARVIS-DFT high-throughput hydride screen
- npj Comput. Mater. **8** (2022), DOI 10.1038/s41524-022-00801-y — in-silico synthesis of lowest-pressure high-Tc ternary superhydrides
- Lucrezi et al., *Nat. Commun.* **15**, 441 (2024), DOI 10.1038/s41467-023-44326-4 — SSCHA quantum-anharmonic LuH3 (method precedent)
- EPW anisotropic Migdal-Eliashberg for superhydrides — arXiv:2310.00056

*(In-silico-only domain; physical synthesis + accredited transport/Meissner are OUT OF DOMAIN, the lab gate. No fabricated citations; retracted claims labelled as retracted.)*
