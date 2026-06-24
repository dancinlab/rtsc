# Research note — constructive candidate enumeration for the +@ trilayer (layer A flat-band metal · layer B bosonic glue)

**Date:** 2026-06-25
**Status:** READ-ONLY constructive materials survey — no compute, no rental. (web + `sidecar research arxiv` + WebFetch.)
**Rule served:** the campaign's "실측전 research" rule — find candidate materials BEFORE anyone synthesizes/measures.
**Relation to the sibling note:** the classification note (`research-excitonic-sc-wall-classification-2026-06-25.md`)
ruled the glue-SC wall **🟠 materials-limited** (no no-go; live theory; no named material). This note is the
**constructive complement**: it enumerates and ranks *concrete, named* candidate materials for layers A and B,
screens the top B candidates for competing order, and proposes one falsifiable A / hBN(n) / B trilayer recipe.

**Honesty posture (commons rule):** materials, energies, and citations below are real and cited; where a number is
a textbook/established value not re-verified from a primary arXiv abstract in this session it is labelled
[LIT-ESTABLISHED]; abstract-level confirmations are [VERIFIED arXiv/WebFetch]. No material is claimed to BE an RTSC.

---

## Architecture recap (what each layer must deliver)

- **Layer A** — a near-flat band of large quantum geometry (∫tr g), metallic/dopable, ideally on a frustrated
  lattice (kagome/triangular/pyrochlore) to suppress nesting (H_016). It supplies the *geometric superfluid weight*
  lever — in a flat band the conventional Drude weight → 0 and the superfluid weight is dominated by the integrated
  quantum metric, so T_c can be finite where a naive m*→∞ would forbid it.
- **Spacer C** — hBN, 1–3 monolayers: electron-opaque (our DFT, H_015) but field-transparent (literature; Coulomb
  field passes with only ~3–4× attenuation). Fixed; not the subject of this note.
- **Layer B** — a sharp ~0.1–0.5 eV (target ~349 meV) **bosonic** mode (exciton or plasmon) that couples *across*
  the spacer via its Coulomb field to pair carriers in A, WITHOUT a competing CDW/SDW pre-empting it.

---

## §1 — Layer A: flat-band metal candidates (ranked)

Ranking axes: **flatness** (bandwidth W) · **isolation** (gap to dispersive bands) · **geometric weight** (⟨tr g⟩
large / measured QGT) · **synthesizability** (bulk-grown & exfoliable > moiré-only) · **frustration** (kagome/
triangular bonus, per H_016).

| Rank | Material (class) | Flat-band W | Isolation / E_F | Geometric weight | Synthesizability | Frustration | Cite |
|---|---|---|---|---|---|---|---|
| **A1** | **CoSn** (kagome metal, CoSn-type) | **W < 0.2 eV; out-of-plane orbital flat band W < 0.02 eV along Γ–M** [VERIFIED WebFetch] | flat band ~−0.2 eV below E_F (dopable toward it); "orbital-selective" so the flat band is the *cleanest* observed kagome flat band | **QGT directly reconstructed in CoSn by spin/polarization-ARPES** (Kang et al., the archetype kagome metal "hosts topological flat bands") [VERIFIED WebFetch] | bulk single-crystal, air-stable, exfoliable; **best-characterized** | kagome ✓ | arXiv:2001.11738 (Liu 2020); arXiv:2412.17809 (Kang 2024) |
| **A2** | **FeSn / Fe-Sn kagome (FeSn, Fe3Sn2)** | flat band ~tens–200 meV, near E_F in Fe3Sn2 | flat band closer to E_F than CoSn but more entangled with magnetism | large (kagome destructive-interference flat band) | bulk crystals, exfoliable | kagome ✓ (but magnetic → SDW risk) | arXiv:2001.11738 cites the kagome family; FeSn/Fe3Sn2 are the magnetic siblings of CoSn [LIT-ESTABLISHED] |
| **A3** | **magic-angle twisted bilayer graphene (MATBG)** | **W ~ 0–10 meV at the magic angle (1.05–1.1°)** [LIT-ESTABLISHED] | isolated by ~tens of meV gaps; tunable to E_F by gating | **superfluid weight is geometry-dominated** — the conventional part →0, geometric part carries T_c | moiré-only: needs precise twist; NOT bulk-grown; fragile | triangular moiré superlattice ✓ | arXiv:1906.07152 (Hu 2019, geometric superfluid weight in TBG); arXiv:2604.05994 (Zhou 2026, band-basis decomposition) |
| **A4** | **Ni3In** (Ni-In kagome-derived, flat-band strange metal) | narrow flat band at E_F, drives non-Fermi-liquid | flat band sits essentially at E_F (intrinsic, no doping needed) | large (flat-band-induced quantum criticality) | bulk crystal; less exfoliation-proven than CoSn | kagome-derived ✓ | Ye et al., *Nat. Phys.* 2024 [LIT-ESTABLISHED — not surfaced in arXiv mirror this session] |
| **A5** | **YMn6Sn6** (kagome, RMn6Sn6 family) | kagome flat band + Dirac; Chern-topological | flat band present but Mn magnetism dominant | sizeable | bulk crystal | kagome ✓ (magnetic) | arXiv:2411.12134 (Bhandari 2024, anomalous Hall in YMn6Sn6) |
| A6 | **CsV3Sb5 / AV3Sb5** (kagome SC, A=K,Rb,Cs) | shallow flat band ~tens meV below E_F | entangled; **has its own 2×2 CDW** | moderate | bulk + exfoliable; already SC at 0.9–2.5 K | kagome ✓ but **CDW present** | arXiv:2311.02289 (Watkins 2023); arXiv:2109.12588 (Zheng 2021) |
| A7 | Lieb / dice lattices (engineered) | exactly flat by construction | tunable | maximal by design | **synthetic only** (cold-atom / photonic / metamaterial) — no bulk solid | bipartite ✓ | [LIT-ESTABLISHED] |

**§1 takeaway.** The strongest *concrete, synthesizable* layer-A is **CoSn** — it has the narrowest cleanly-isolated,
non-magnetic kagome flat band (W<0.2 eV; out-of-plane orbital W<0.02 eV) AND is the one material where the quantum
geometric tensor has been *directly measured* (Kang 2024). It is non-magnetic (no SDW), bulk-grown, and exfoliable.
MATBG (A3) has the flattest band and is the textbook geometric-superfluid-weight system, but it is moiré-only/fragile
and harder to stack against an hBN/B trio in a controlled way. Ni3In (A4) is attractive because its flat band sits
*at* E_F with no doping, but it is less de-risked for thin-film stacking.

---

## §2 — Layer B: bosonic eV-glue candidates (ranked)

Ranking axes: **mode energy in the 0.1–0.5 eV window** (target ~349 meV) · **sharpness / low damping** · **dipole/
Coulomb coupling strength across a spacer** · **absence of a competing order that shorts the mode** (screened in §3).

| Rank | Material (class) | Bosonic mode | Energy (window?) | Damping / sharpness | Coupling across spacer | Cite |
|---|---|---|---|---|---|---|
| **B1** | **Ta2NiSe5** (excitonic insulator) | excitonic gap + amplitude (Higgs) mode of the EI order parameter | **gap ~0.16–0.35 eV; T onset ~325–328 K** — *squarely in the 0.1–0.5 eV window and near the 349 meV target* [T~325 K VERIFIED WebFetch; gap value LIT-ESTABLISHED] | sharp EI transition; **but** strong electron–phonon coupling is co-responsible (the mode is exciton+phonon hybrid) | quasi-1D chains, large in-plane dipole; vdW-layered → stackable | arXiv:2007.08212 (Kim 2020, direct excitonic instability); arXiv:2203.06817 (Chen 2022, e-ph role); arXiv:2106.04396 (Matsubayashi 2021, pressure-induced SC) |
| **B2** | **interlayer-exciton TMD bilayer** (MoSe2/WSe2 etc.) | interlayer exciton (spatially indirect, permanent dipole) | **~1.3–1.5 eV bare; but the *relevant* low-energy collective/trion & exciton-DW modes sit ~0.1–0.5 eV**; hBN insertion tunes them | narrow at low T; tunable by field/doping | **permanent out-of-plane dipole → strong cross-spacer Coulomb coupling** (the natural fit to our field-transparent hBN spacer) | arXiv:1904.11434 (Vialla 2019); mechanism: arXiv:2410.09148 (Kumar–Senthil 2024); arXiv:2310.10726 (von Milczewski 2023) |
| **B3** | **1T-TiSe2** (exciton-condensate / CDW) | plasmon strongly tied to the CDW gap; exciton condensate | plasmon response shifts dramatically across the CDW gap (~few hundred meV scale) | **plasmon is sharp but the CDW gap *is* the order** → the glue is entangled with the competing order | layered, exfoliable | arXiv:2210.14635 (Lin 2022, plasmon response to CDW gap in 1T-TiSe2) |
| **B4** | **layered plasmonic metal** (in 't Veld–Rösner platform) | interlayer hybridized plasmon | tunable across the eV scale by dielectric environment | low-loss if engineered; "dynamical Coulomb engineering" | **this IS the cross-spacer plasmon-glue mechanism**, computed to enhance T_c up to an order of magnitude [VERIFIED WebFetch] | arXiv:2508.06195 (in 't Veld 2025); arXiv:2303.06220 (2023, phonon↔plasmon crossover) |
| B5 | graphene / doped-TMD 2D plasmon (mid-IR) | Dirac/2D plasmon | ~0.1–0.6 eV, *gate-tunable* — directly hits the window | low-loss in encapsulated graphene; but a metallic B competes with A for the carrier sheet | strong in-plane; out-of-plane coupling weaker | arXiv:1610.04548 (Low 2016, polaritons in 2D materials) |
| B6 | hyperbolic-phonon-polariton hBN itself | hBN phonon-polariton Reststrahlen bands | ~0.09–0.2 eV (lower edge of window) | very low loss | the spacer *is* the medium (Grankin–Galitski) | arXiv:2201.07731 (Grankin 2022) |

**§2 takeaway.** Two genuinely-in-window, named, synthesizable candidates dominate: **Ta2NiSe5** (B1) — a *bulk,
air-handleable, vdW-layered* excitonic insulator whose order-parameter energy scale (gap ~0.16–0.35 eV, onset ~325 K)
sits right at the ~349 meV target — and the **interlayer-exciton TMD bilayer** (B2), whose *permanent out-of-plane
dipole* is the ideal partner for a field-transparent hBN spacer. The plasmon route (B4) is the cleanest *mechanism*
(in 't Veld–Rösner) but names no turnkey compound.

---

## §3 — Competing-order screen (does a CDW/SDW pre-empt the glue? the H_004 / H_014 risk)

For each top-B candidate: is the bosonic mode the host of, or pre-empted by, a density-wave order?

| Candidate | Competing order present? | Does it short the glue? | Verdict |
|---|---|---|---|
| **B1 Ta2NiSe5** | The EI *is* an electronic order, but it is **NOT a nesting CDW/SDW** — it is a zero-momentum (q=0) excitonic condensate driven by direct-gap e–h binding, hybridized with a phonon. There is no incommensurate density wave; the order is uniform. **Under pressure it gives way to a semimetal that superconducts** (Matsubayashi 2021). | The q=0 character means there is **no nesting instability competing at finite q** — the H_016 frustration goal is partly met *intrinsically* (no SDW/CDW wavevector to pre-empt SC). The e-ph admixture is the main caveat (the mode is not purely excitonic). | **Best competing-order profile of the named candidates** ✓ |
| **B2 TMD interlayer exciton** | In the Kumar–Senthil mechanism the glue **IS the Goldstone mode of an exciton-density-wave order** → the density wave is *built into* the mechanism and is intrinsically adjacent; SC appears only "close to" the EDW. | High risk: the competing order is the mechanism's own host (the sibling note's central caveat). Frustration/incommensurability is *not* guaranteed. | **Competing order intrinsic** ✗/△ |
| **B3 1T-TiSe2** | The CDW gap *is* the order; the plasmon glue tracks it. | The glue is entangled with the CDW — classic short-circuit (H_004). | **Pre-empted** ✗ |
| **B4 layered plasmon metal** | Depends entirely on the chosen carrier compound; in a frustrated/incommensurate host the plasmon can lead. | Avoidable in principle (mechanism is order-agnostic), but no named clean compound. | **Order-agnostic but unnamed** △ |

**§3 takeaway.** **Ta2NiSe5 is the only named B candidate whose competing order is q=0 and non-nesting**, i.e. it does
NOT carry an incommensurate CDW/SDW wavevector that could pre-empt SC at finite q — it most cleanly satisfies the
H_016 "escape competing order by frustration/incommensurability" goal (here by *commensurate-zero-q* uniformity, plus
the empirical fact that the system *does* superconduct once the gap is suppressed under pressure). The TMD-exciton
route (B2), despite its ideal dipole geometry, carries the competing order *inside* the mechanism (Kumar–Senthil).

---

## §4 — Proposed recipe + verdict

### Proposed single falsifiable trilayer

> **A = CoSn (kagome, hole/gate-doped to bring the orbital-selective flat band to E_F)**
> **/ C = hBN, n = 2 monolayers (electron-opaque per H_015, field-transparent)**
> **/ B = Ta2NiSe5 (excitonic insulator, near its ~325–328 K excitonic onset, gap ~0.16–0.35 eV ≈ the ~349 meV target)**

A single, fully-named, vdW-stackable A/hBN(2)/B target. All three are real, bulk-grown or exfoliable materials.

**3 biggest reasons it MIGHT work**
1. **Energy match + measured geometry.** B's order-parameter scale (~0.16–0.35 eV, onset ~325 K) sits right at the
   ~349 meV glue target, and A is the one flat-band metal with a *directly measured* quantum geometric tensor and the
   cleanest isolated non-magnetic kagome flat band (W<0.2 eV) — the two levers our architecture needs are each
   independently demonstrated in these specific compounds (arXiv:2412.17809; arXiv:2001.11738).
2. **Best competing-order profile.** B's excitonic order is **q=0 / non-nesting** and the system *superconducts* once
   its gap is suppressed (arXiv:2106.04396) — uniquely among named B candidates it does not bring an incommensurate
   CDW/SDW to pre-empt SC (§3), partially meeting the H_016 frustration goal intrinsically.
3. **Geometry fits the spacer.** Both A (kagome sheet) and B (vdW-layered chains) are 2D-stackable against hBN, and
   the cross-spacer Coulomb-glue mechanism is exactly the one computed to enhance pairing up to an order of magnitude
   (in 't Veld–Rösner, arXiv:2508.06195) — our trio is a named instantiation of a published, computed mechanism.

**3 biggest reasons it might NOT work**
1. **B's mode is exciton+phonon hybrid, not pure exciton** (arXiv:2203.06817) — the e-ph admixture may cap the usable
   bosonic coupling at the same Tc≲10 K ceiling the dielectric-stability argument historically imposed.
2. **No demonstrated cross-spacer coupling for THIS trio.** Field-transparency (~3–4× attenuation) is shown for hBN
   generally, not for a CoSn↔Ta2NiSe5 pair; the glue may be too diluted across n=2 hBN (the Krotov–Suslov geometry-
   dilution failure mode, cond-mat/9912180, recast at the monolayer scale).
3. **Doping CoSn's flat band to E_F without killing the flat-band character** (or inducing its own order) is unproven;
   the flat band sits ~0.2 eV from E_F and aggressive gating/intercalation may disperse it.

### Verdict

# 🟠 — only a credible *partial* candidate exists today

There is now a **specific, fully-named, internally-consistent A/hBN/B trilayer** (CoSn / hBN(2) / Ta2NiSe5) in which
**each individual lever is demonstrated in the named compound** — measured quantum geometry + isolated flat band in
CoSn, an in-window q=0 non-nesting bosonic order in Ta2NiSe5, and a published cross-spacer plasmon/exciton-glue
mechanism. That is materially stronger than "no candidate." **But** it remains 🟠, not 🟢, because the three pieces
have **never been demonstrated working *together***: no measured cross-spacer coupling for this trio, B's mode is a
phonon-hybrid rather than a pure 0.349 eV exciton, and no bosonic-glue Tc — let alone a high one — has ever been
measured in any system. A sober reading: **the wall is materials-engineering-limited, and we can now name the exact
brick to try first** — which is a real, useful narrowing, but not a solved material. `absorbed=false` / GATE_OPEN
unchanged.

---

## Citations (load-bearing ★; arXiv ids via `sidecar research arxiv`, abstracts via WebFetch)

**Layer A:**
- ★ Liu et al., arXiv:2001.11738 (2020) — CoSn orbital-selective Dirac fermions + **flat band W<0.2 eV** (out-of-plane orbital <0.02 eV along Γ–M). [VERIFIED WebFetch]
- ★ Kang et al., arXiv:2412.17809 (2024) — **direct measurement of the quantum geometric tensor in CoSn** (archetype kagome flat-band metal). [VERIFIED WebFetch]
- Hu, Hyart, Pikulin & Rossi, arXiv:1906.07152 (2019) — geometric vs conventional superfluid weight in TBG. [VERIFIED arXiv]
- Zhou, arXiv:2604.05994 (2026) — band-basis decomposition of TBG superfluid weight (geometric contribution). [VERIFIED arXiv]
- Bhandari et al., arXiv:2411.12134 (2024) — YMn6Sn6 kagome (anomalous Hall). [VERIFIED arXiv]
- Watkins et al., arXiv:2311.02289 (2023); Zheng et al., arXiv:2109.12588 (2021) — CsV3Sb5 kagome SC + interlayer structure. [VERIFIED arXiv]
- Ye et al., *Nat. Phys.* (2024) — Ni3In flat-band quantum criticality. [LIT-ESTABLISHED — not surfaced in arXiv mirror this session]

**Layer B + competing-order screen:**
- ★ Kim et al., arXiv:2007.08212 (2020) — direct observation of the **excitonic instability in Ta2NiSe5**. [VERIFIED arXiv]
- ★ Chen et al., arXiv:2203.06817 (2022) — role of **electron-phonon coupling** in Ta2NiSe5 (mode is exciton+phonon hybrid). [VERIFIED arXiv]
- ★ Matsubayashi et al., arXiv:2106.04396 (2021) — **pressure-induced superconductivity** in semimetallic Ta2NiSe5 (gap suppression → SC; T_S~325 K confirmed). [VERIFIED WebFetch]
- Chen et al., arXiv:2309.07111 (2023) — band-gap-tuned Ta2Ni(Se,S)5 excitonic phase diagram. [VERIFIED arXiv]
- Lin et al., arXiv:2210.14635 (2022) — plasmon response to CDW gap in **1T-TiSe2** (glue entangled with CDW). [VERIFIED arXiv]
- Vialla et al., arXiv:1904.11434 (2019) — interlayer complexes in a vdW heterobilayer (TMD exciton). [VERIFIED arXiv]
- Low et al., arXiv:1610.04548 (2016) — polaritons / plasmons in 2D materials. [VERIFIED arXiv]

**Mechanism (cross-spacer glue):**
- ★ in 't Veld, Katsnelson, Millis & Rösner, arXiv:2508.06195 (2025) — **plasmonic SC enhanced up to an order of magnitude via dynamical Coulomb engineering**; the computed analog of our cross-spacer glue. [VERIFIED WebFetch]
- in 't Veld et al., arXiv:2303.06220 (2023) — phonon↔plasmon pairing crossover. [VERIFIED arXiv]
- Kumar, Patri & Senthil, arXiv:2410.09148 (2024) — exciton-density-wave-fluctuation-mediated SC (competing order is the host — disqualifies the pure TMD route on §3). [VERIFIED arXiv]
- von Milczewski, Chen, Imamoğlu & Schmidt, arXiv:2310.10726 (2023) — electron-exciton coupling SC in TMD heterostructures. [VERIFIED arXiv]
- Grankin & Galitski, arXiv:2201.07731 (2022) — hyperbolic plasmons & SC (hBN as medium). [VERIFIED arXiv]
- Krotov & Suslov, arXiv:cond-mat/9912180 (1999) — geometry-dilution failure mode (the "too diluted across the spacer" risk). [VERIFIED arXiv]
