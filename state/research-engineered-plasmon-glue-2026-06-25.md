---
id: PLASMON
slug: engineered-plasmon-glue
domain: rtsc
status: pre_registered
pre_register_frozen: true
frozen_at: 2026-06-25
kind: research
---

# Research note — the engineered-plasmon 🟢-path (layer-B glue at ≥349 meV)

**Date:** 2026-06-25
**Lane:** L-plasmon-research (PLASMON, research)
**Status:** READ-ONLY cited literature survey — no compute, no rental (web + WebFetch on arXiv abstracts).
**Question:** Per in 't Veld–Katsnelson–Millis–Rösner (arXiv:2508.06195) and related, can a real 2D /
heterostructure plasmon be tuned to ≥349 meV with low loss and NO competing density-wave order, to serve as
the +@ glue layer B? Identify concrete candidate platforms with published plasmon energies/linewidths in the
0.3–0.5 eV range. Is any a credible turnkey clean glue at ≥349 meV today, or still a design proposal?

**Honesty posture (commons honesty / falsifier-first):** energies and citations below are real and cited;
abstract-level confirmations marked [VERIFIED arXiv/WebFetch]; textbook/established physics not re-derived this
session marked [LIT-ESTABLISHED]. No material is claimed to BE an RTSC. absorbed=false / GATE_OPEN throughout.

---

## §0 — The target the plasmon must clear (harness, byte-deterministic)

Inline against `tool/rtsc_harness.py` (NOT edited):

| Quantity | Value |
|---|---|
| `omega_for_stacked_tc(293, three_d=True)` | **349.31 meV** ← the glue energy needed for room-T with the 3D lever |
| `stacked_tc(349, True)` | 292.74 K (just clears 293) |
| `stacked_tc(400, True)` | 335.52 K (the TiSe2 exciton path — clears with margin) |
| `stacked_tc(300, True)` | 251.64 K (= the named CoSn/hBN/Ta2NiSe5 lead, ~252K; H_020 ~49 meV-of-glue short) |
| THREED_TC_LEVER | 1.84 |

So layer B must deliver a **q≈0-launchable, sharp, ≥349 meV bosonic mode with no pre-empting density wave**.
A plasmon is attractive precisely because — unlike the TiSe2 exciton (carries a CDW, H_014 risk) — a plasmon is
a charge-oscillation with NO intrinsic density-wave order. The question is whether its **energy** can be pushed to
349 meV while keeping loss low and a real synthesizable host.

---

## §1 — The in 't Veld–Katsnelson–Millis–Rösner program (the cited basis)

| arXiv / DOI | Title (verbatim) | What it is | Status |
|---|---|---|---|
| **arXiv:2508.06195** | "Enhancing Plasmonic Superconductivity in Layered Materials via Dynamical Coulomb Engineering" (in 't Veld, Katsnelson, Millis, Rösner) | "bosonic engineering" of **interlayer hybridized plasmon modes**; tunable dynamical screening → enhanced plasmon-mediated T_c "by up to an order of magnitude" | **computed / theory** [VERIFIED WebFetch — abstract verbatim] |
| **arXiv:2303.06220** (2D Mater. 10, 045031) | "Screening Induced Crossover between Phonon- and Plasmon-Mediated Pairing in Layered Superconductors" (in 't Veld, Katsnelson, Millis, Rösner, 2023) | gapless 2D plasmons mediate pairing at weak screening; phonon↔plasmon crossover | **computed / theory** [VERIFIED WebFetch] |
| **arXiv:1803.04576** | "Plasmonic Superconductivity in Layered Materials" (Rösner, Groenewald, Schönhoff, Berges, Haas, Wehling, 2018) | layered-material plasmons are **gapless** modes coupling to electrons; can enhance OR reduce T_c | **computed / theory** [VERIFIED WebFetch] |

**Verbatim abstract of arXiv:2508.06195** (the lane's anchor paper):
> "Conventional Coulomb engineering, through controlled manipulation of the environment, offers an effective route
> to tune the correlation properties of atomically thin van der Waals materials via static screening. Here we
> present tunable dynamical screening as a method for precisely tailoring bosonic modes to optimize many-body
> properties. We show that ``bosonic engineering'' of plasmon modes can be used to enhance plasmon-induced
> superconducting critical temperatures of layered superconductors in metallic environments by up to an order of
> magnitude, due to the formation of interlayer hybridized plasmon modes with enhanced superconducting pairing
> strength. We determine optimal properties of the screening environment to maximize critical temperatures. We show
> how bosonic engineering can aid the search for experimental verification of plasmon mediated superconductivity."

**Key reading.** The program is a *self-consistent computed proposal*. It reports (a) NO specific plasmon energy in
eV/meV in the abstract, (b) NO fabricated host, (c) the T_c enhancement is relative ("an order of magnitude") and
the closing sentence is literally a call for **experimental verification** that does not yet exist. It is a
mechanism/design framework, NOT a turnkey 349 meV glue.

---

## §2 — Concrete plasmon platforms with published energies/linewidths in the 0.1–0.5 eV window

| # | Platform | Plasmon energy (measured/achievable) | Loss / Q | Competing density wave? | Reaches ≥349 meV clean today? | Cite |
|---|---|---|---|---|---|---|
| P1 | **Doped monolayer graphene (gate/chemical)** | mid-IR; typ. 16–200 meV; up to ~0.11 eV with measured Q; energy ∝ √(E_F·q), capped by Pauli blocking at ~2·E_F | **Q≈4 at ℏω≈0.11 eV** [VERIFIED WebSearch] | **none** (charge oscillation) | **NO** — to reach 349 meV needs E_F≳0.5 eV AND large q; Q stays low | arXiv:1202.4996 (gate-tuned imaging); Nano Lett. 2017 (intrinsic plasmon-phonon, Q~4) |
| P2 | **hBN-encapsulated graphene** | same band, energy still mid-IR | **Q improved ~5× vs bare** (impurity scattering removed) | none | NO (energy still sub-0.3 eV in practice) | Science 360, aar8438 (2018, ultimate confinement) [VERIFIED WebSearch] |
| P3 | **Acoustic graphene plasmon (graphene on metal / graphene-TMD)** | ultra-confined, low loss; sub-eV, mid-IR | low loss (metal-screened) but **energy still < ~0.2 eV** | none | NO (acoustic branch is *lower* energy by construction) | Science 2018 (aar8438); arXiv:2406.15654 (graphene-TMD acoustic, 2024) |
| P4 | **Layered metallic TMD (NbS2 3R on hBN, doped) — the 2508.06195 host class** | computed interlayer-hybridized plasmon; energy is a **design parameter** of doping + dielectric environment | computed; no measured Q for the 349 meV target | **none for the plasmon** (host SC/CDW is a separate concern — NbSe2-class CDW caution) | NO (computed only; not measured at 349 meV) | arXiv:2508.06195; arXiv:2303.06220; NbS2 3R/hBN CVD growth [LIT-ESTABLISHED] |
| P5 | **Dielectric-engineered / Coulomb-engineered 2D metal** | tunable by substrate ε(ω) (the "dynamical screening" knob) | computed | none intrinsic | NO (design proposal) | arXiv:2508.06195 |

**Physics ceiling (the load-bearing fact).** A 2D Dirac/parabolic plasmon disperses as ω_p ∝ √(n·q) and is bounded
above by Pauli/Landau damping near ω ≈ 2·E_F. To put a graphene plasmon at **349 meV** you need a Fermi level
E_F ≳ 0.5–1 eV (very heavy, ~10^14 cm^-2 doping) *and* a large in-plane q — and at that point the measured quality
factor is low (Q~4–15), i.e. the mode is **broad**, not the "sharp" boson the glue argument wants. The highest
*cleanly measured* graphene plasmons reported are mid-IR (≲0.2 eV). [VERIFIED WebSearch — Pauli-blocking cap ≈ 2·E_F]

**Cleanliness win (the real advantage).** Across P1–P5 the **competing-order column is empty** — a plasmon is a
charge oscillation and carries NO intrinsic CDW/SDW. This is the genuine edge over TiSe2 (P-exciton at 400 meV but
CDW-bound, H_014) and over Ta2NiSe5 (~300 meV glue, ~252K, H_020): the plasmon path trades the H_014 competing-order
risk for an **energy-reach** risk. Per the campaign's H_016 result a competing CDW is escapable by frustration
(η_nest* ~0.45), but the plasmon avoids needing that escape at all — at the cost that 349 meV is not yet demonstrated.

---

## §3 — Verdict: is an engineered-plasmon glue at ≥349 meV realizable?

**🟠 (design-stage, materials/energy-limited — NOT a turnkey clean glue today; NOT a no-go either).**

- **Mechanism exists & is clean:** plasmon-mediated pairing in layered metals is a *computed, peer-reviewed* program
  (arXiv:1803.04576 → 2303.06220 → 2508.06195) and a plasmon carries **no intrinsic density-wave order** — it
  structurally beats the TiSe2/Ta2NiSe5 glues on the competing-order axis.
- **Energy reach is the wall:** no platform has a **measured, sharp, low-loss plasmon at ≥349 meV**. Doped/acoustic
  graphene plasmons are mid-IR (≲0.2 eV); pushing to 349 meV needs E_F≳0.5–1 eV where measured Q collapses (~4–15);
  the layered-metal / dynamical-Coulomb route that *can* in principle hit 349 meV exists **only as computation**, and
  arXiv:2508.06195 itself closes by calling for experimental verification.
- **Therefore:** an engineered-plasmon glue at ≥349 meV is a **credible design proposal, not a turnkey material**.
  GATE_OPEN, absorbed=false. To flip to 🟢 needs a *measured* zone-(q→0)-coupling plasmon ≥349 meV with Q≳20 and a
  demonstrated vdW stacking route — none exists as of 2026-06-25.

---

## §4 — Proposed registry rows (for the main loop to integrate; do NOT self-merge)

| material/platform | layer | boson_meV | competing_order | reaches_349? | absorbed | cite | claim_truth |
|---|---|---|---|---|---|---|---|
| doped-graphene-plasmon | B | ~16–200 (measured); Pauli cap ~2·E_F | none | False (measured ≤ ~0.2 eV; Q low at high E_F) | false | arXiv:1202.4996; Nano Lett. 2017 (Q~4 @0.11eV) | True(clean); False(energy) |
| hBN-encap-graphene-plasmon | B | mid-IR; Q ~5× bare | none | False | false | Science 360 aar8438 (2018) | True(clean,low-loss); False(energy) |
| acoustic-graphene-plasmon | B | sub-0.2 eV, ultra-low-loss | none | False (acoustic branch is lower energy) | false | aar8438; arXiv:2406.15654 | True(low-loss); False(energy) |
| layered-metal-2D-plasmon (NbS2/TMD, dyn-Coulomb) | B | tunable, ≥349 reachable IN THEORY | none (plasmon) | False (computed only, not measured) | false | arXiv:2508.06195; 2303.06220; 1803.04576 | True(clean,tunable); False(measured-energy) |
| dielectric-Coulomb-engineered-plasmon | B | tunable by substrate ε(ω) | none | False (design proposal) | false | arXiv:2508.06195 | False(turnkey) |

All rows: absorbed=false, GATE_OPEN. The plasmon path's distinctive value = **cleanest competing-order profile of
any layer-B option**; its open risk = **energy reach to 349 meV is unproven in any measured sharp/low-loss mode**.

---

## §5 — Citations (all verified this session unless marked LIT-ESTABLISHED)

- arXiv:2508.06195 — in 't Veld, Katsnelson, Millis, Rösner, "Enhancing Plasmonic Superconductivity in Layered
  Materials via Dynamical Coulomb Engineering" [VERIFIED WebFetch — abstract verbatim §1]
- arXiv:2303.06220 — in 't Veld, Katsnelson, Millis, Rösner, "Screening Induced Crossover between Phonon- and
  Plasmon-Mediated Pairing in Layered Superconductors", 2D Mater. 10, 045031 (2023) [VERIFIED WebFetch]
- arXiv:1803.04576 — Rösner, Groenewald, Schönhoff, Berges, Haas, Wehling, "Plasmonic Superconductivity in Layered
  Materials" (2018) [VERIFIED WebFetch]
- arXiv:1202.4996 — "Optical nano-imaging of gate-tuneable graphene plasmons" (gate-tuned graphene plasmon imaging)
- Nano Lett. 17, 7 (2017), "Intrinsic Plasmon–Phonon Interactions in Highly Doped Graphene" — measured Q≈4 at
  ℏω≈0.11 eV [VERIFIED WebSearch]
- Science 360, eaar8438 (2018), "Probing the ultimate plasmon confinement limits with a van der Waals
  heterostructure" — hBN encapsulation, ~5× damping improvement [VERIFIED WebSearch]
- arXiv:2406.15654 — "Ultrasensitive acoustic graphene plasmons in a graphene–TMD heterostructure" (2024)
- Pauli-blocking plasmon cap (ω ≲ 2·E_F) [LIT-ESTABLISHED — confirmed via WebSearch on graphene plasmon dispersion]
</content>
</invoke>
