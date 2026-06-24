# Research note — classifying the "electronic-glue superconductivity graveyard" wall

**Date:** 2026-06-25
**Status:** READ-ONLY literature survey — no compute, no rental. (web + `sidecar research arxiv` + WebFetch.)
**Decision this note serves:** the prior note (`research-crpa-glue-transparency-2026-06-25.md`, PR #7)
moved the +@ trilayer binding wall UPSTREAM to a MATERIALS question: the field-transparency and
electron-opacity halves of our spacer mechanism are both supported, so the remaining open risk is
whether a real "glue layer B" with a usable bosonic electronic mode actually exists. That question
sits squarely on the historical **excitonic / electronic-glue superconductivity graveyard**
(Allender–Bray–Bardeen 1973 → Miller–Strongin 1976 negative). This note classifies that wall per
the break-walls taxonomy: 🧱 real ceiling · 🟠 materials-limited · 🟢 reopening.

---

## Q1 — Why did the historical excitonic/plasmonic-SC program fail? (a no-go, the materials, or never tested?)

**Verdict: (b)+(c) — the obstacle was the specific materials/geometry of the era plus a never-cleanly-tested
mechanism. There is NO no-go theorem.**

The lineage and its negative verdicts:
- **Little (1964)**, *Phys. Rev.* **134**, A1416 — excitonic high-Tc in a polarizable molecular spine.
  **Ginzburg (1964/1968–70)** — metal/dielectric "sandwich" surface-exciton SC. (Foundational, pre-arXiv.)
- **Allender, Bray & Bardeen (1973)**, *Phys. Rev. B* **7**, 1020, DOI 10.1103/PhysRevB.7.1020 — the
  direct ancestor of our geometry: metal electrons at E_F pair via *virtual excitons* in an adjacent
  semiconductor. **Contested on the dielectric assumption** (Inkson–Anderson: it needs ε with structure at
  small ω over nearly all q, not just q≈0; Comment/Reply *PRB* **8**, 4433, DOI 10.1103/PhysRevB.8.4433).
- **Miller, Strongin, Kammerer & Streetman (1976)**, *Phys. Rev. B* **13**, 4834,
  DOI 10.1103/PhysRevB.13.4834 — "Experimental search for excitonic superconductivity": ultrathin metals
  on semiconductors showed **NO excitonic Tc enhancement.** The cautionary precedent.

**Was it a fundamental ceiling? No — the literature is explicit that it is not forbidden:**
- The historical bound that capped Tc (assuming the static dielectric function stays positive,
  ε_tot(k,0) > 0, which limits e–ph coupling to Tc ≲ 10 K) is itself a **restrictive assumption, not a
  prohibition** — Ginzburg and others argued the exciton mechanism is *not forbidden* by it, and that
  ε_tot < 0 regions are allowed by stability. (Reviewed in "The Prospects of Excitonic Superconductivity,"
  V. L. Ginzburg & D. A. Kirzhnits eds., Springer; springerlink chapter
  10.1007/978-1-4613-0411-1_9. [secondary/textbook — abstract-level only, label UNVERIFIED-FULLTEXT].)
- **Krotov & Suslov (1999)**, arXiv:cond-mat/9912180 — solved the inhomogeneous Eliashberg equations for
  the Ginzburg sandwich exactly in the local limit and explained *why* the 1970s sandwiches showed nothing:
  the excitonic contribution is **diluted to undetectability when the film thickness ≫ interatomic
  spacing.** This is a **geometry/materials** failure (the boson lived too far from the carriers, too few
  carriers saw it), **not a physics ceiling.** [VERIFIED arXiv]

**Q1 bottom line:** the program failed because (b) the specific 1970s metal/semiconductor materials had the
boson too weakly/too-distantly coupled to the carriers (Krotov–Suslov geometry dilution; ABB's fragile
dielectric requirement), and (c) it was never tested in a system engineered to put a strong, near bosonic
mode right against a high-DOS carrier sheet. **No no-go theorem exists.**

---

## Q2 — Modern revival: current state of exciton/plasmon/interlayer-Coulomb-mediated SC

This is an **active, computed frontier** with multiple independent 2023–2026 lines:

- **in 't Veld, Katsnelson, Millis & Rösner (2025)**, arXiv:2508.06195 — "Enhancing Plasmonic
  Superconductivity in Layered Materials via Dynamical Coulomb Engineering": **interlayer hybridized
  plasmon modes** enhance pairing in layered vdW materials by **up to an order of magnitude**, tunable by
  the dielectric environment (dynamical screening). This is essentially the computed analog of our
  cross-spacer bosonic-glue mechanism. (Companion: arXiv:2303.06220 (2023), phonon↔plasmon pairing
  crossover.) [VERIFIED arXiv]
- **Kumar, Patri & Senthil (2024)**, arXiv:2410.09148 — "Unconventional superconductivity mediated by
  exciton density-wave fluctuations" in charge-imbalanced bilayer semiconductors: the **Goldstone mode of
  exciton-density-wave order mediates attractive pairing**, electrically tunable. A modern, credible,
  computed version of exciton-mediated SC. [VERIFIED arXiv]
- **von Milczewski, Chen, Imamoğlu & Schmidt (2023)**, arXiv:2310.10726 — "Superconductivity induced by
  strong electron-exciton coupling in doped atomically thin semiconductor heterostructures": strong-coupling
  (Bose/Fermi-polaron, BCS–BEC crossover) treatment giving **Tc up to ~10% of the Fermi temperature** in TMD
  heterostructures — a high relative Tc claim. Tc set by doping and trion binding energy. [VERIFIED arXiv]
- **Cao & Kavokin (2024)**, arXiv:2409.12201 — "Exciton-Enhanced Superconductivity in Monolayer Films of
  Aluminum": directly revives the ABB/Miller–Strongin metal-on-semiconductor idea, arguing the
  *experimentally observed* Tc rise of Al toward the monolayer limit is consistent with an **exciton-induced**
  enhancement (larger gap / higher Tc than phonons alone). A modern positive re-reading of the very system
  the 1976 search called negative. [VERIFIED arXiv]
- **Nashabeh & Fu (2026)**, arXiv:2601.07729 — SC in mass-asymmetric electron–hole bilayers
  (exciton-condensate / Wigner / SC phase diagram vs interlayer separation). [VERIFIED arXiv]
- **Grankin & Galitski (2022)**, arXiv:2201.07731 — hyperbolic-plasmon / SC interplay in layered conductors
  (hBN is itself a natural hyperbolic medium). [VERIFIED arXiv]
- **Experimental, exciton-condensate platforms:** the doubly-charged-exciton ("quaternion") TMD-bilayer
  program is pursued as a route to a non-BCS condensate carrying supercurrent (Physics World feature,
  2024–25). Still pre-condensation (limited by optical-pump heating + Auger recombination) — **no measured
  Tc yet**. [secondary/news — VERIFIED as reportage, not as a measured SC].

**Q2 bottom line:** exciton/plasmon/interlayer-Coulomb-mediated SC is NOT a dead program — it is a live,
multiply-computed frontier with credible recent proposals (in 't Veld–Rösner plasmon; Kumar–Senthil
exciton-DW; von Milczewski exciton-polaron). **But every credible Tc is model-/material-specific and
relative (a fraction of E_F, an "order-of-magnitude enhancement"), never an experimentally confirmed
absolute Tc, and certainly not a demonstrated 293 K.** No measurement to date shows a meaningful Tc from a
purely bosonic electronic glue.

---

## Q3 — Does a candidate "glue layer B" actually exist? (~0.1–0.5 eV exciton/plasmon, couples across a spacer to a flat band, no competing CDW/SDW)

**The honest answer: NO concrete, named, de-risked material B exists today.** The modern proposals supply
*platform classes*, each carrying an unresolved competing-order or strong-coupling caveat:

- **TMD bilayer / heterostructure excitons** (MoSe₂/WSe₂ etc.) — interlayer excitons sit at ~0.1–0.5 eV
  (the right window), and inserting hBN tunes them (our prior note). BUT: in Kumar–Senthil the pairing glue
  **IS the fluctuation of an exciton-density-wave order** — i.e. the *competing density-wave order is the
  mechanism's host*, and SC appears only "close to" that ordering, so the CDW/EDW is intrinsically adjacent
  and can pre-empt it. (arXiv:2410.09148.)
- **Layered plasmonic metals** (in 't Veld–Rösner) — the plasmon is the glue; this needs a metallic carrier
  sheet whose own plasmon/environment is engineered. No specific compound + spacer + flat-band trio is named
  as a turnkey candidate; it is a tunability principle. (arXiv:2508.06195.)
- **Doped TMD with a separate exciton reservoir** (von Milczewski) — gives high relative Tc, but in the
  strong-coupling regime where the "exciton" and "carrier" are not cleanly separable (Fermi/Bose polarons,
  bipolarons), and Tc is set by trion binding, not a clean 0.3 eV glue across a spacer. (arXiv:2310.10726.)
- **Monolayer Al on a semiconductor** (Cao–Kavokin) — a real, fabricated system with a real Tc bump, but the
  excitonic attribution is a *re-interpretation of existing data*, not an isolated demonstration, and the Tc
  is ~few K, not high. (arXiv:2409.12201.)

Crucially, **the competing-order problem (CDW/SDW/exciton-DW pre-empting SC) is generic** to every flat-band /
strong-long-range-Coulomb proposal, and at least one leading modern proposal (Kumar–Senthil) has the density
wave *built into* the mechanism rather than avoided. **No paper exhibits a B with (i) a 0.1–0.5 eV bosonic
mode, (ii) demonstrated cross-spacer coupling to a neighboring flat band, AND (iii) a shown-clean absence of a
pre-empting density-wave instability.** The trio is individually plausible, jointly unrealized.

---

## Q4 — Classification verdict

### 🟠 MATERIALS-LIMITED

There is **no fundamental no-go theorem** (Q1: the dielectric-stability bound is a restrictive assumption,
not a prohibition; Ginzburg/ABB are not forbidden; Krotov–Suslov pin the historical null on geometry
dilution, not physics). The mechanism is an **active, credibly computed modern frontier** (Q2: in 't
Veld–Rösner, Kumar–Senthil, von Milczewski) — which on its own would read 🟢. **But it is pulled back to 🟠
by Q3:** sixty years on, with the mechanism revived and computed, **no concrete, named, de-risked "glue
layer B" exists** that simultaneously delivers the right bosonic mode energy, demonstrated cross-spacer
coupling to a flat band, and a clean absence of a competing CDW/SDW. And no experiment has ever measured a
meaningful Tc from a purely bosonic electronic glue. The wall is a **60-year graveyard with no tombstone**
(no no-go) **and no birth certificate either** (no material) — i.e. materials-limited, with a genuinely
reopening theory frontier behind it.

**Single most decision-relevant fact per axis:**
- 🧱 (against a real ceiling): Krotov–Suslov (cond-mat/9912180) prove the 1970s null result follows from
  film thickness ≫ interatomic spacing — a *geometry* failure, removable by engineering — not a theorem.
- 🟠 (for materials-limited): no published system exhibits the required (0.1–0.5 eV mode) + (cross-spacer
  flat-band coupling) + (no pre-empting density wave) trio; in Kumar–Senthil the density wave is the
  mechanism's own host, so the competing-order risk is intrinsic, not incidental.
- 🟢 (the live-frontier caveat): in 't Veld–Rösner (2508.06195) compute up to an order-of-magnitude
  plasmonic-pairing enhancement tunable by dielectric environment — the theory side is genuinely open and
  active, so 🟠 here means "no material *yet*," not "abandoned."

**Honesty note:** this is NOT a positive result for the campaign. The most generous reading the literature
supports is: *the mechanism is allowed and is being actively re-derived, but the load-bearing materials
question our +@ stack depends on (a real, CDW-free flat-band + 0.3 eV-glue + spacer trio) remains
unsolved by anyone, and no bosonic-glue Tc has ever been measured — let alone 293 K.* The campaign's
`absorbed=false` / GATE_OPEN posture is unchanged.

---

## Citations (verified — arXiv ids via `sidecar research arxiv`; DOIs via Crossref/journal pages)

**Historical lineage + critiques (Q1):**
- Allender, Bray & Bardeen, *Phys. Rev. B* **7**, 1020 (1973), DOI 10.1103/PhysRevB.7.1020;
  Comment/Reply *PRB* **8**, 4433, DOI 10.1103/PhysRevB.8.4433 — ★ direct ancestor + dielectric critique. [VERIFIED Crossref]
- Miller, Strongin, Kammerer & Streetman, *Phys. Rev. B* **13**, 4834 (1976),
  DOI 10.1103/PhysRevB.13.4834 — experimental search, **negative**. ★ cautionary precedent. [VERIFIED Crossref]
- Krotov & Suslov, arXiv:cond-mat/9912180 (1999) — ★ explains the Ginzburg-sandwich null as
  thickness-dilution geometry, NOT a ceiling. [VERIFIED arXiv]
- "The Prospects of Excitonic Superconductivity" (Ginzburg–Kirzhnits volume), Springer chapter
  10.1007/978-1-4613-0411-1_9 — no-fundamental-prohibition framing. [abstract-level only — UNVERIFIED-FULLTEXT]
- Little, *Phys. Rev.* **134**, A1416 (1964); Ginzburg sandwich (1964/1968–70) — foundational, pre-arXiv. [standard refs]

**Modern revival (Q2) — ★ load-bearing:**
- in 't Veld, Katsnelson, Millis & Rösner, arXiv:2508.06195 (2025) — ★ plasmonic SC, order-of-magnitude
  enhancement via dynamical Coulomb engineering. [VERIFIED arXiv]
- in 't Veld, Katsnelson, Millis & Rösner, arXiv:2303.06220 (2023) — phonon↔plasmon pairing crossover. [VERIFIED arXiv]
- Kumar, Patri & Senthil, arXiv:2410.09148 (2024) — ★ exciton-density-wave-fluctuation-mediated SC. [VERIFIED arXiv]
- von Milczewski, Chen, Imamoğlu & Schmidt, arXiv:2310.10726 (2023) — ★ electron-exciton coupling, Tc up to
  ~10% of T_F in TMD heterostructures. [VERIFIED arXiv]
- Cao & Kavokin, arXiv:2409.12201 (2024) — exciton-enhanced SC in monolayer Al (ABB system, re-read positive). [VERIFIED arXiv]
- Nashabeh & Fu, arXiv:2601.07729 (2026) — SC in mass-asymmetric e–h bilayers. [VERIFIED arXiv]
- Grankin & Galitski, arXiv:2201.07731 (2022) — hyperbolic plasmons & SC. [VERIFIED arXiv]
- Physics World, "Superconductivity's new contender" (2024–25) — TMD "quaternion" exciton-condensate
  platform; pre-condensation, no measured Tc. [secondary/news — VERIFIED reportage]
