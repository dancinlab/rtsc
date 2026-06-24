# Research note — does a bosonic glue survive the hBN spacer? (cRPA go/no-go on renting GPU)

**Date:** 2026-06-25
**Status:** READ-ONLY literature survey — no compute rented, no DFT run.
**Decision this note serves:** whether to rent vast.ai GPU for a constrained-RPA (cRPA)
calculation of the H_011 "bosonic glue penetrates the electron-opaque hBN spacer" claim.
**Cards in scope:** H_003 (`plusalpha-bilayer`), H_009 (`connector-spacer`), H_011
(`glue-through-spacer`), H_015 (`trilayer-dft-electron-opacity`, the real-DFT card that
already CONFIRMED the electron-opacity half: hBN drops interlayer single-electron DOS 7.7×,
saturating at 1 ML).

## The exact open question

H_011's load-bearing, un-verified claim: a **neutral/collective bosonic** glue (exciton or
plasmon, Ω ~ 0.3 eV / ~349 meV per H_007) couples **across** a 1–3 ML hBN spacer via its
**long-range Coulomb/dipole field** strongly enough to mediate pairing in layer A — even
though single-electron tunneling is blocked (H_015). The closed-form card modeled this with a
decay-length proxy (λ_Coulomb = 8 ML vs λ_e = 0.5 ML → window 0.44–2.85 ML). We were about
to spend GPU to replace that proxy with a real cross-spacer screened-interaction W.

---

## Q1 — Coulomb / dielectric screening through hBN (does the field actually pass?)

**hBN dielectric constants (first-principles, the canonical reference):** Laturia, Van de Put
& Vandenberghe, *npj 2D Mater. Appl.* **2**, 6 (2018), DOI 10.1038/s41699-018-0050-x
(open-access mirror: https://utd-ir.tdl.org/items/315c3c21-a6f8-4552-a882-420dfb5136fb):

- **Out-of-plane** (c-axis, the relevant direction for a vertical stack): ε⊥ = **3.29
  (monolayer) → 3.76 (bulk)** — increases only ~14% from 1 ML to bulk.
- **In-plane:** ε∥ = **6.82 → 6.93** — essentially **layer-independent**.
- Classic bulk IR values (Geick 1966, via secondary sources): ε⊥,0 ≈ 5.09, ε∥,0 ≈ 7.04
  (static) — same order; the relevant out-of-plane static screening is **ε ≈ 3–5**, i.e.
  WEAK. hBN is a poor dielectric screener compared to a metal or a high-κ oxide.

**Direct empirical answer — the Coulomb field DOES pass thin hBN, measured:**

The whole field of **interlayer Coulomb drag** and **exciton condensation through an hBN
spacer** is exactly the experiment H_011 needs, and the answer is *yes, the field couples
across*:

- Hao, Zimmerman, Watanabe, Taniguchi & Kim (2025), arXiv:2508.09098 — quantized Coulomb-drag
  and **interlayer exciton condensate** between two bilayer-graphene sheets separated by a
  **2.5 nm (~7–8 ML) hBN spacer**. Pure Coulomb coupling (no tunneling) condenses
  electron–hole pairs across **far thicker hBN than our 1–3 ML target.**
- Liu, Watanabe, Taniguchi, Halperin & Kim (2016), arXiv:1608.03726 — quantum-Hall exciton
  superfluid / drag in graphene double layers separated by **few-layer hBN**; interlayer
  Coulomb attraction binds e–h pairs across the insulator.
- Liu, Wang, Fong et al. (2016), arXiv:1612.08308 — frictional magneto-Coulomb drag through
  few-layer-hBN graphene double layers; drag is a direct probe of interlayer e–e Coulomb
  scattering surviving the spacer.
- Wang, Xue, Watanabe, Taniguchi & Ki (2024), arXiv:2405.20393 — Coulomb drag in
  graphene/hBN/graphene moiré stacks.
- TMD/hBN/TMD interlayer excitons: Yoon, Zhang, Qi et al. (2022), arXiv:2209.14521
  (MoSe₂/hBN/WSe₂) — interlayer excitons and their Coulomb properties tuned by inserting hBN;
  Erkensten, Brem, Perea-Causin & Malic (2022), arXiv:2207.03942 — microscopic theory of the
  dipole–dipole / Coulomb-driven interlayer-exciton transport across vdW spacers.

**Crucial nuance — two different things decay differently through hBN:**

1. **Single-electron / charge-transfer coupling** (wavefunction overlap) is *strongly*
   suppressed — exponential, few-nm decay length, often gone by ~4 ML / 2 nm (this is exactly
   our H_015 result: 7.7× drop, saturating at 1 ML; and matches reported plasmon/charge-
   transfer-mode decay "of only a few nm … gone at ~2 nm" in TMD/spacer/TMD stacks).
2. **The long-range Coulomb / dipole field** (density–density, drag, exciton binding) is only
   *dielectrically attenuated* — by the **static ε⊥ ≈ 3–4** of the hBN slab, with the
   Keldysh/Rytova non-local form softening it further — and demonstrably **survives 1–8 ML**.

This is precisely H_011's λ_Coulomb ≫ λ_e premise, and the literature supports it
qualitatively and with hard device data.

**Screening framework (the cheap-proxy tool):** the Keldysh/Rytova non-local 2D potential and
its environmental-screening generalization (Noori, Cheng, Xuan & Quek 2020, arXiv:2005.14374,
"Dielectric Screening by 2D Substrates"; Adeniran & Liu 2022, arXiv:2212.01676, hBN:TMD
dielectric embedding GW; Li, Santos, Cappelluti, Roldán et al. 2015, arXiv:1503.00380,
dielectric screening in atomically thin BN) gives a closed-form, *runnable-on-summer*
estimate of how much a 1–3 ML hBN slab attenuates the interlayer Coulomb kernel.

> **THE SINGLE MOST IMPORTANT NUMBER:** out-of-plane static screening of 1–3 ML hBN is only
> **ε⊥ ≈ 3.29 → ~3.6** (Laturia 2018). The interlayer Coulomb field is therefore attenuated by
> a factor of order **~3–4× (one slab's dielectric constant), NOT exponentially killed**, and
> it is *measured* to survive Coulomb-drag/exciton-condensate coupling across hBN spacers up to
> ~2.5 nm (~8 ML) — far thicker than our 1–3 ML target. The "field penetrates" half of H_011 is
> empirically supported; the field passes, screened by a factor of a few, not blocked.

---

## Q2 — Exciton/plasmon-mediated SC (prior art — has anyone done cross-spacer boson glue?)

**The classic excitonic lineage and its verdicts:**

- **Little (1964)** — excitonic high-Tc in a polarizable spine; **Ginzburg (1964/1968–70)** —
  sandwich/surface excitonic SC, the "exciton mechanism" program (foundational, pre-arXiv).
- **Allender, Bray & Bardeen (1973)**, *Phys. Rev. B* **7**, 1020, DOI
  10.1103/PhysRevB.7.1020 (Comment/Reply: *PRB* **8**, 4433) — **the direct ancestor of H_011**:
  metal-layer electrons at E_F tunnel into an adjacent semiconductor's gap and pair via virtual
  **excitons** in the semiconductor. This is essentially our A/glue geometry. **Verdict:
  contested + experimentally negative** — Inkson & Anderson critiqued the dielectric assumption
  (needs ε with peaks at small ω for nearly all q, not just q≈0); and **Miller, Strongin,
  Kammerer & Streetman (1976)**, *Phys. Rev. B* **13**, 4834, DOI 10.1103/PhysRevB.13.4834 —
  "Experimental search for excitonic superconductivity" — deposited ultrathin metals on
  semiconductors and saw **NO excitonic Tc enhancement.** *This is the cautionary precedent:
  the exact "exciton in adjacent layer glues the metal" idea was tried and did not deliver.*

**Modern interlayer/bilayer boson-mediated pairing (the live frontier — directly on point):**

- **Kumar, Patri & Senthil (2024)**, arXiv:2410.09148 — "Unconventional superconductivity
  mediated by **exciton density-wave fluctuations**" in charge-imbalanced bilayer
  semiconductors. Electrically tunable **exciton-mediated SC** — a modern, credible version of
  the H_011 mechanism, computed.
- **Nashabeh & Fu (2026)**, arXiv:2601.07729 — predicted SC in mass-asymmetric electron–hole
  bilayers (exciton condensate / Wigner / SC phase diagram vs interlayer separation).
- **in 't Veld, Katsnelson, Millis & Rösner (2023)**, arXiv:2303.06220 — "Screening-induced
  crossover between phonon- and **plasmon-mediated pairing** in layered superconductors"
  (RPA-dynamical-screening; plasmons as the bosonic glue).
- **in 't Veld, Katsnelson, Millis & Rösner (2025)**, arXiv:2508.06195 — "Enhancing Plasmonic
  Superconductivity in Layered Materials via **Dynamical Coulomb Engineering**." **This is
  essentially the published, computed version of H_011's mechanism:** interlayer **hybridized
  plasmon modes** enhance pairing in layered vdW materials by up to an order of magnitude,
  tuned by the (dielectric) environment. The bosonic glue coupling **across** a layered stack
  via the dynamically-screened Coulomb interaction W is exactly what we wanted to compute.
- Grankin & Galitski (2022), arXiv:2201.07731 — hyperbolic-plasmon / SC interplay in layered
  conductors (hBN is itself a natural hyperbolic medium).
- Wang, Fan, Dai & Zaletel (2024), arXiv:2409.19059; Hao et al. 2025 (above) — exciton-
  condensate Josephson / drag platforms confirm the interlayer-boson physics is real and
  device-accessible.

**Bottom line for Q2:** cross-spacer / insulator-separated boson-mediated pairing is **NOT
novel** — it is a 60-year lineage (Little/Ginzburg/ABB) with a *negative 1976 experimental
verdict for the metal-on-semiconductor exciton version*, now reincarnated as a **live,
actively-computed** frontier (Kumar–Senthil exciton-DW SC; in 't Veld–Rösner plasmon SC). The
modern works already use RPA-class dynamical-screening machinery and already conclude that
interlayer plasmon/exciton modes **can** mediate/enhance pairing — but with Tc and coupling
strength that are model- and material-specific, not a free 293 K.

---

## Q3 — Method + tool selection (what would the GPU rental actually run?)

What we need is the **cross-spacer screened interaction W(q,ω)** and whether a bosonic mode in
it gives net attraction in layer A. Three tiers:

| Tool | What it outputs | Convergence | Hardware / wall-time (4–10-atom hetero-cell) |
|---|---|---|---|
| **RPA dielectric / Lindhard χ⁰, W=ε⁻¹v** (own code or QE/`epsilon.x`/`turboEELS`, or the Keldysh closed form) | ε(q,ω), W(q,ω), plasmon dispersion, interlayer Coulomb attenuation | modest: bands to ~2–3× E_F window, q-grid for the in-plane dispersion | **CPU, hours on summer** — no rental |
| **cRPA (RESPACK, pairs with QE via wan2respack)** | *constrained* (partially-screened) effective U/W between target Wannier orbitals — the actual cross-spacer effective interaction parameter | Wannierization of target manifold + RPA polarization (empty-state sum, q-grid) | **CPU, MPI+OpenMP, "a few hundred atoms" feasible**; a 4–10-atom cell is small → **~hours–1 day on a multicore node**, GPU NOT required (RESPACK has no GPU port). Refs: Nakamura et al., *Comput. Phys. Commun.* **261**, 107781 (2021), arXiv:2001.02351; wan2respack, arXiv:2302.13531 |
| **GW/BSE (Yambo, BerkeleyGW — GPU-capable)** | quasiparticle gaps + **bound exciton** energies/wavefunctions/dipoles (BSE) — needed only if we must prove the *exciton* exists at Ω~0.3 eV and get its interlayer dipole | heavy: dense empty-state sums, dielectric-matrix cutoff, k-grid; the expensive tier | **GPU pays off here.** BerkeleyGW & Yambo are GPU-ported (BerkeleyGW ran 2700-atom GW at full Summit scale, arXiv → JCTC 2022; Yambo/BerkeleyGW GPU-BSE arXiv:2409.15116). For a 4–10-atom cell: **a few GPU-hours**, but setup/convergence is the real cost. |

**Key tooling fact:** the natural cRPA tool (RESPACK) is **CPU/MPI, not GPU** — so "rent a GPU
for cRPA" is partly a category error. GPU only buys us speed in the **GW/BSE** tier, which we
need only if proving the exciton's existence/dipole is the goal. The screened-W / plasmon
question is an **RPA dielectric** calculation that runs on summer.

---

## Q4 — BOTTOM LINE (a / b / c) for the rental decision

**Verdict: (a) + (b) — NO-GO on renting GPU now.**

**(a) The literature substantially answers the qualitative question.** "Does the long-range
Coulomb/dipole field of an interlayer boson penetrate 1–3 ML hBN even when single-electron
tunneling is blocked?" — **Yes, and it is measured:** Coulomb drag and interlayer exciton
condensates couple two electronic layers across hBN spacers up to ~8 ML (2.5 nm) by pure
Coulomb interaction, dielectrically attenuated by only ε⊥ ≈ 3–4 per slab, while single-electron
DOS dies by the first ML (our own H_015 + the drag/exciton-condensate corpus). And the
*pairing* version — interlayer plasmon/exciton modes mediating/enhancing SC — is already
computed in the modern literature (in 't Veld–Rösner 2023/2025; Kumar–Senthil 2024). **H_011's
"the field penetrates, the glue can be bosonic" premise is corroborated; it is not the open
risk.** The 1976 Miller–Strongin negative result is the honest counterweight: the *quantitative*
payoff (a useful Tc, let alone 293 K) is exactly where the historical exciton program failed.

**(b) A cheap proxy fully covers what's left, runnable on summer with $0:**

1. **Keldysh/Rytova non-local screened-Coulomb estimate** with ε⊥ = 3.29–3.76 (Laturia) for
   1/2/3 ML hBN → a defensible number for the interlayer Coulomb-kernel attenuation, replacing
   the ad-hoc λ_Coulomb = 8 ML proxy in H_011's harness with a literature-grounded one.
2. **RPA dielectric / Lindhard W(q,ω)** on the existing summer-built QE 7.2 (the H_015
   toolchain) — interlayer plasmon dispersion + cross-spacer W, CPU-only, hours. This already
   delivers the "does a bosonic mode in W give attraction in A" signal at proxy level.

**(c) A genuine cRPA/GW campaign is NOT justified at the current stage**, and even if pursued
later it is mostly **CPU (RESPACK cRPA), not GPU** — GPU rental would only be warranted for the
**GW/BSE exciton-existence/dipole** tier (Yambo/BerkeleyGW), which is a *second-order* question
behind a still-unanswered first-order materials question: **does a real flat-band metal A with
the required ~349 meV bosonic glue and no competing CDW order actually exist?** (H_004 L2 /
H_011 L2). Renting GPU to compute a cross-spacer exciton dipole before we have a concrete
candidate A/B pair would be computing a detail of an architecture whose load-bearing materials
question is upstream and unsolved. **Spending money here does not de-risk the campaign; the
upstream candidate-existence question does.**

### Recommendation
1. **Do NOT rent GPU now.** (Saves the rental.)
2. On summer ($0): add a Keldysh-screening + RPA-W proxy card (call it H_019) that replaces
   H_011's hand-set λ_Coulomb with the Laturia ε⊥ and the measured drag/exciton-condensate
   thickness reach — cite this note.
3. Keep the cRPA/GW campaign **deferred**, and re-scope it: if ever run, it is **RESPACK cRPA on
   CPU** for W/U, and **GW/BSE on GPU only** if the exciton dipole at Ω~0.3 eV must be proven —
   and only **after** a concrete flat-band A + glue B candidate exists. Estimated cost if/when
   triggered: GW/BSE on a 4–10-atom cell ≈ a few GPU-hours of compute, but dominated by
   convergence setup; a single on-demand vast.ai GPU-day (~$10–30) would suffice for a scoping
   run — *not* warranted until the upstream candidate question is answered.

### Honesty / caveats
- The drag/exciton-condensate evidence is in the **quantum-Hall / strong-B and TMD-exciton**
  regimes; it proves the **Coulomb field couples across hBN**, which is the H_011 premise, but
  it does **not** prove a 293 K, zero-field, phonon-free pairing glue. The leap from "field
  couples" to "mediates room-T pairing in a flat band" is unproven and is where the 1976
  Miller–Strongin negative and the model-specific Tc of the modern papers should keep us
  conservative.
- ε⊥ values are first-principles (Laturia) and broadly consistent with IR data; the per-ML
  Keldysh attenuation is a model estimate, label **MODEL-PROBE** in any card that uses it.
- `absorbed=true` is unaffected — still needs accredited 4-probe transport + Meissner +
  measured H_c2 / T_c.

---

## Citations (verified — arXiv ids retrieved via `sidecar research arxiv`; DOIs via Crossref)

**Dielectric screening through hBN (Q1):**
- Laturia, Van de Put & Vandenberghe, *npj 2D Mater. Appl.* **2**, 6 (2018), DOI
  10.1038/s41699-018-0050-x — hBN ε⊥ = 3.29→3.76, ε∥ = 6.82→6.93 (1 ML → bulk). [VERIFIED via
  Crossref/UTD repository] ★ load-bearing number.
- Noori, Cheng, Xuan & Quek, arXiv:2005.14374 (2020) — dielectric screening by 2D substrates
  (non-local). [VERIFIED arXiv]
- Adeniran & Liu, arXiv:2212.01676 (2022) — TMD:hBN dielectric screening, ML-to-bulk. [VERIFIED]
- Li, Santos, Cappelluti, Roldán et al., arXiv:1503.00380 (2015) — dielectric screening in
  atomically thin BN. [VERIFIED]

**Coulomb field passes hBN — measured (Q1):** ★ load-bearing
- Hao, Zimmerman, Watanabe, Taniguchi & Kim, arXiv:2508.09098 (2025) — exciton condensate /
  quantized drag across **2.5 nm (~7–8 ML) hBN**. [VERIFIED arXiv]
- Liu, Watanabe, Taniguchi, Halperin & Kim, arXiv:1608.03726 (2016) — QH exciton superfluid,
  few-layer hBN. [VERIFIED]
- Liu, Wang, Fong et al., arXiv:1612.08308 (2016) — magneto-Coulomb drag, few-layer hBN. [VERIFIED]
- Wang, Xue, Watanabe, Taniguchi & Ki, arXiv:2405.20393 (2024) — drag in graphene/hBN/graphene.
  [VERIFIED]
- Yoon, Zhang, Qi et al., arXiv:2209.14521 (2022) — MoSe₂/hBN/WSe₂ interlayer excitons. [VERIFIED]
- Erkensten, Brem, Perea-Causin & Malic, arXiv:2207.03942 (2022) — interlayer-exciton Coulomb
  transport theory. [VERIFIED]

**Exciton/plasmon-mediated SC lineage + modern (Q2):**
- Allender, Bray & Bardeen, *Phys. Rev. B* **7**, 1020 (1973), DOI 10.1103/PhysRevB.7.1020;
  Comment/Reply *PRB* **8**, 4433. [VERIFIED via Crossref] ★ direct ancestor.
- Miller, Strongin, Kammerer & Streetman, *Phys. Rev. B* **13**, 4834 (1976), DOI
  10.1103/PhysRevB.13.4834 — experimental search, **negative**. [VERIFIED via Crossref] ★
  cautionary precedent.
- Kumar, Patri & Senthil, arXiv:2410.09148 (2024) — exciton-density-wave-mediated SC. [VERIFIED] ★
- in 't Veld, Katsnelson, Millis & Rösner, arXiv:2508.06195 (2025) — plasmonic SC via dynamical
  Coulomb engineering (the computed analog of H_011). [VERIFIED] ★
- in 't Veld, Katsnelson, Millis & Rösner, arXiv:2303.06220 (2023) — phonon↔plasmon pairing
  crossover. [VERIFIED]
- Nashabeh & Fu, arXiv:2601.07729 (2026) — SC in mass-asymmetric e–h bilayers. [VERIFIED]
- Grankin & Galitski, arXiv:2201.07731 (2022) — hyperbolic plasmons & SC. [VERIFIED]
- Wang, Fan, Dai & Zaletel, arXiv:2409.19059 (2024) — exciton-condensate Josephson. [VERIFIED]
- Little (1964), *Phys. Rev.* **134**, A1416; Ginzburg (1964/1970), exciton-mechanism program —
  foundational, pre-arXiv. [classic refs, not independently re-fetched — label as standard
  textbook citations]

**Method / tools (Q3):**
- RESPACK cRPA: Nakamura et al., *Comput. Phys. Commun.* **261**, 107781 (2021), arXiv:2001.02351;
  wan2respack, arXiv:2302.13531 — CPU/MPI, ~few-hundred atoms. [VERIFIED arXiv]
- GPU GW/BSE: BerkeleyGW (Summit-scale GW, JCTC 2022); Yambo/BerkeleyGW GPU-BSE, arXiv:2409.15116
  (2024). [VERIFIED arXiv / BerkeleyGW docs]
