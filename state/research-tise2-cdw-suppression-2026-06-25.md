# Research note — Can the 1T-TiSe2 CDW be suppressed WHILE keeping a ~0.3–0.4 eV excitonic mode as pairing glue?

**Date:** 2026-06-25
**Lane:** L-CDW-research (CDW, research)
**Status:** READ-ONLY literature survey — WebSearch + WebFetch + harness compute. No rental, no fabrication.
**Honesty (commons):** every numeric value carries a source (arXiv id / DOI / journal). absorbed=false / GATE_OPEN.
Energies are published material properties, NOT a claim any material IS an RTSC. Computed-only / contested / paywalled
values are labelled. NO tune-to-green: a sober "no clean high-exciton host exists yet" is the honest result.

---

## Decision this note serves

The concrete 🟢-path in the campaign state rests on **1T-TiSe2's ~400 meV excitonic optical mode** — the ONLY surveyed
2D electronic boson that clears the relaxed room-T glue target. With the 3D lever (THREED_TC_LEVER=1.84):

| harness call | value |
|---|---|
| `stacked_tc(400, three_d=True)` | **335.5 K** — CLEARS room-T amplitude (293 K) |
| `omega_for_stacked_tc(293, three_d=True)` | **349.3 meV** — the glue target the 400 meV mode beats |
| `geometric_bkt_tc_band(400)` (2D only) | 182.3 K |

So on **amplitude** the 400 meV mode is sufficient. The blocker is **H_014 (competing order)**: that same mode drives a
finite-q (2×2×2) CDW that pre-empts pairing. H_016 showed a competing CDW/SDW is escapable by frustration (critical
eta_nest* ≈ 0.45). The decisive 🟢 question this note answers: **does a REAL route suppress the TiSe2 CDW while RETAINING
the ~400 meV mode — or does any real high-exciton host carry the CDW inseparably?** Determinism confirmed (byte-equal x2:
`[335.5214, 349.3071, 182.3486]`).

---

## Core finding: in 1T-TiSe2 the ~400 meV mode IS the CDW order parameter — they are NOT separable

The pivotal experiment is Kogar, Rak, Abbamonte et al., *Signatures of exciton condensation in a transition metal
dichalcogenide*, **Science 358, 1314 (2017)** (arXiv:1611.04217). Momentum-resolved EELS (M-EELS) measured a **soft
plasmon / electronic collective mode whose energy falls to ZERO at finite momentum near T_CDW ≈ 190 K** — the dynamical
slowing-down / crystallization of valence electrons into the exciton condensate. [VERIFIED — peer-reviewed.]

Consequence for the campaign: the "~400 meV excitonic optical mode" (the upper mode in the CDW-phase optical spectra,
researchgate 332412936 / arXiv:0911.0327) is **the high-energy face of the very order parameter that condenses into the
finite-q CDW**. The mode and the competing density wave are **two faces of one excitonic instability**, not a clean boson
sitting beside a removable CDW. This is why H_014 is so hard to dodge here specifically: you cannot keep the exciton's
spectral weight at 400 meV and simultaneously erase its q≠0 condensate — the condensate IS the weight.

This is reinforced by *Charge density wave hampers exciton condensation in 1T-TiSe2* (PhysRevResearch 3, 033097 (2021),
OSTI 1802907): the lattice CDW and the excitonic channel **compete for the same electron-hole pairs** — strengthening one
depletes the other. [VERIFIED — peer-reviewed.]

---

## Route 1 — Cu intercalation (Cu_xTiSe2): SC appears, but the EXCITON is screened away

- *Superconductivity in Cu_xTiSe2*, Morosan et al., **Nat. Phys. 2, 544 (2006)** (arXiv:cond-mat/0606529): Cu
  intercalation **continuously suppresses the CDW**; SC emerges near **x ≈ 0.04** and domes at **T_c,max = 4.15 K at
  x = 0.08**. [VERIFIED — peer-reviewed.]
- BUT the exciton does NOT survive the doping. M-EELS on Cu_xTiSe2 (Kogar et al., nanoHUB 30624 "Suppression of Exciton
  Condensation in Copper-Doped TiSe2"; consistent with PRR 3, 033097 (2021)): **Cu rapidly DESTROYS the exciton
  condensate by added-carrier screening**, while only a conventional **Peierls-phase CDW persists for x ≳ 0.01**. So Cu
  trades the excitonic mode for (a) a tiny phonon-mediated SC dome and (b) a residual lattice CDW. [VERIFIED.]
- *Observation of a CDW Incommensuration Near the Superconducting Dome in Cu_xTiSe2* (OSTI 1352597; PRL 110, 196404
  via Nat. Phys. nphys2935): the CDW **does NOT terminate inside the SC dome** — it persists (as incommensurate /
  domain-wall order) to higher x than the SC onset. [VERIFIED.]
- **Verdict for the glue question:** Cu suppression is the WRONG trade. The ~400 meV exciton is screened out (mode
  LOST), what remains is a 4 K phonon SC + a residual Peierls CDW. `omega_for_stacked_tc(4.15, 3D)` ≈ **5 meV** — the Cu
  SC is energetically trivial vs the 349 meV target. **Exciton retained? NO.**

## Route 2 — Hydrostatic pressure: a 2nd SC dome, also driven by phonon softening of the CDW

- Kusmartseva, Sipos, Forró et al., *Pressure Induced Superconductivity in Pristine 1T-TiSe2*, **PRL 103, 236401
  (2009)**: pressure suppresses the CDW and induces an SC dome (T_c up to ~1.8 K, ~2–4 GPa). [VERIFIED.]
- *Effect of Cu intercalation and pressure on excitonic interaction in 1T-TiSe2* (arXiv:1902.02046): the **excitonic
  interaction matters in the P–T phase diagram but NOT in the x–T diagram** — i.e. pressure and doping suppress the order
  by DIFFERENT mechanisms (pressure softens the CDW phonon; Cu screens the exciton). Theory (arXiv:1104.0492) attributes
  the pressure SC dome to **softening of the CDW-related phonon mode**. [VERIFIED — arXiv/theory.]
- **Verdict:** pressure still works by collapsing the same excitonic-CDW order. There is no pressure window that leaves a
  strong, sharp ~400 meV exciton standing while removing its q≠0 condensate; the mode softens AS the order dies.
  **Exciton retained at 349–400 meV? NO** — it softens to zero at the transition (the M-EELS soft-mode picture).

## Route 3 — Monolayer / reduced dimensionality / gating: makes the CDW STRONGER (wrong direction)

- *Charge density wave transition in single-layer titanium diselenide*, Chen et al., **Nat. Commun. 6, 8943 (2015)** and
  *Unconventional CDW Transition in Monolayer 1T-TiSe2* (ACS Nano 2016): monolayer T_CDW = **232 ± 5 K > bulk 200 K**, and
  the ARPES gap GROWS — *"enhancement of electron–hole coupling upon reducing dimensionality."* [VERIFIED.]
- *Strong-coupling charge density wave in monolayer TiSe2* (2D Mater. 7, abafec (2020)) and *Fluctuation-driven multi-step
  CDW in monolayer TiSe2* (arXiv:2604.20355) reinforce a robust/strengthened monolayer CDW. [VERIFIED.]
- **Verdict:** dimensional reduction ENHANCES the excitonic CDW. Gating/monolayering keeps (even grows) the exciton, but
  AT THE COST of a stronger competing order — the opposite of what we need. **CDW suppressed? NO (enhanced).**

## Route 4 — Topological / strain suppression of the CDW (Sn, twist, topological band engineering)

- *Topological suppression of the charge-density-wave transition in TiSe2* (researchgate 321879751) and *CDW suppression
  in 1T-TiSe2 through Sn intercalation* (Nano Res., 10.1007/s12274-021-3859-0): the CDW T can be lowered by these levers.
  [VERIFIED — but these works report CDW suppression, not retention of a sharp 349–400 meV electronic mode.]
- **Verdict:** these are CDW-suppression demonstrations; NONE reports a surviving high-energy (≥349 meV) exciton after
  suppression. They confirm the general pattern: suppress the order ⇒ lose the mode.

---

## Sibling materials — is there a q=0 / CDW-free host with a ≥349 meV electronic mode?

| Sibling | Mode / gap | q-character | Competing order | Net vs target |
|---|---|---|---|---|
| **Ta2NiSe5** (incumbent) | E_op ≈ 0.16 eV (range 0.16–0.35); T_C 326 K | **q=0** zone-center, non-nesting | none (q=0 EI) | grazes target; clean but undershoots |
| **Ta2Pd3Te5** monolayer | ~100 meV many-body gap; T_C 365 K | **q=0** (computed) | none | cleanest drop-in; energy too LOW |
| **1T-TiSe2** | **~400 meV** upper mode (+80 meV lower) | **finite-q** (2×2×2) | **CDW (intrinsic)** | only host ABOVE target, but CDW IS the mode |
| monolayer WTe2 | E_b > 100 meV | zone-boundary (not pure q=0) | light (QSH edge) | clean-ish, sub-target |
| topological EI, **tunable momentum order** | (paywalled; not extracted) | **TUNABLE q → possibly 0** | EI | INTRIGUING but unverified energy |

- *Zero-gap → EI in Ta2NiSe5*, Lu et al., **Nat. Commun. 8, 14408 (2017)**: E_op ≈ 0.16 eV, T_C 326 K, q=0. [VERIFIED.]
- *Evidence for an Excitonic Insulator State in Ta2Pd3Te5*, **PRX 14, 011046 (2024)** + arXiv:2312.14456 / arXiv:2401.01222:
  q=0 EI, ~100 meV gap. [VERIFIED — but sub-target energy.]
- *A New Era of Excitonic Insulators*, review, **J. Phys. Soc. Jpn. 94, 012001 (2025)**: the candidate field (Ta2NiSe5,
  Ta2Pd3Te5, TiSe2, WTe2…) — none reported with BOTH a ≥349 meV mode AND q=0 cleanliness. [VERIFIED — review.]
- *Topological excitonic insulator with tunable momentum order*, **Nat. Phys. (2025), s41567-025-02917-6**: title/abstract
  report an EI whose ordering **momentum is tunable** — in principle toward q=0. Body PAYWALLED (auth redirect); **mode
  energy NOT extracted — treat as a LEAD, not a verified high-energy clean host.** [UNVERIFIED energy — flagged.]
- **No surveyed sibling has BOTH ≥349 meV AND q=0/CDW-free.** The energy axis (TiSe2's 400 meV) and the cleanliness axis
  (Ta2NiSe5 / Ta2Pd3Te5 q=0) are realized in DIFFERENT materials, never jointly. The campaign's own **engineered 2D
  plasmon** (in 't Veld, arXiv:2508.06195) remains the one route where energy is a tunable design parameter with a
  competing-order-free profile by construction — but its energy is engineered, not a fixed material constant.

---

## Proposed registry rows (for the main loop — DO NOT add to tool/rtsc_candidates.py here)

Format mirrors existing `Candidate(...)` rows: (value, source, verified). exciton_retained encodes the decisive trade.

| name | role | key property = value | competing_order | exciton_retained_after_suppression | citation | verified |
|---|---|---|---|---|---|---|
| CuxTiSe2 | B (suppression test) | tc_sc_K = 4.15 (x=0.08); CDW suppressed | CDW (Peierls) persists past SC onset | **NO — exciton screened away** | Nat.Phys.2,544(2006) arXiv:cond-mat/0606529; OSTI 1352597; nanoHUB 30624 | tc True; exciton-loss True |
| TiSe2-pressure | B (suppression test) | tc_sc_K ~1.8 (2–4 GPa); 2nd dome | CDW (phonon-softened) | **NO — mode softens to zero at transition** | PRL 103,236401(2009); arXiv:1902.02046; arXiv:1104.0492 | tc True; soft-mode True |
| TiSe2-monolayer | B (suppression test) | T_CDW = 232 K (>bulk 200); gap GROWS | CDW **enhanced** | exciton kept but CDW STRONGER (wrong way) | Nat.Commun.6,8943(2015); ACS Nano 2016; 2D Mater.7 abafec(2020) | True |
| 1T-TiSe2 (exciton=CDW) | B (energy-exists) | boson_meV = 400; soft mode → 0 at T_CDW | CDW (mode IS the order param) | inseparable | Science 358,1314(2017) arXiv:1611.04217; PRR 3,033097(2021) | mode True; inseparability True |
| Ta2Pd3Te5 | B (clean q=0) | boson_meV = 100; T_C 365 K | none (q=0) | n/a (no CDW to suppress) | PRX 14,011046(2024); arXiv:2401.01222 | True; energy<target |
| topo-EI-tunable-q | B (LEAD) | boson_meV = UNKNOWN; **q tunable → 0** | EI (tunable momentum) | n/a | Nat.Phys. s41567-025-02917-6 (2025) | q-tunable True (title); energy False/paywalled |

**Integration note:** the three TiSe2 suppression rows all carry the same verdict — *suppression of the CDW costs the
~400 meV exciton* (screened, softened, or only available where the CDW is even stronger). The `topo-EI-tunable-q` row is
the single genuinely-new LEAD worth a follow-up fetch (its mode energy must be obtained from the paper body before any
promotion). It does NOT change today's verdict because its energy is unverified.

---

## Verdict: 🟠 — suppression trades AWAY the exciton; no real CDW-free ≥349 meV host found

> **🟠 MATERIALS-LIMITED.** In 1T-TiSe2 the ~400 meV mode and the finite-q CDW are **two faces of one excitonic order
> parameter** (Kogar/Abbamonte, Science 2017: the mode softens to zero AT the CDW transition). Every real suppression
> route therefore destroys the mode it was supposed to preserve: **Cu intercalation** screens the exciton away (leaving a
> 4 K phonon SC + a residual Peierls CDW that outlasts the SC dome), **pressure** softens the CDW phonon (the mode goes
> soft, not retained), and **monolayering/gating ENHANCES** the CDW (T_CDW 232 K > bulk 200 K — wrong direction). On the
> sibling axis, the energy (TiSe2's 400 meV) and the cleanliness (Ta2NiSe5 / Ta2Pd3Te5 q=0, ≤~160 meV) are realized in
> **different** materials, never jointly: **no surveyed real material has BOTH a ≥349 meV mode AND a q=0/CDW-free
> profile.** The only genuinely-clean ≥349 meV route remains an *engineered* 2D plasmon (arXiv:2508.06195), whose energy
> is a design parameter, not a fixed material constant. One real LEAD — a topological EI with *tunable* ordering momentum
> (Nat. Phys. 2025) — could in principle reach q→0, but its mode energy is paywalled/unverified and cannot support 🟢
> today. absorbed=false / GATE_OPEN.

**Promote to 🟢 only if** a future round verifies a single real host with BOTH (i) a measured/computed electronic mode
≥349 meV AND (ii) q=0 (or tunable-to-q=0) with no pre-empting density wave AND (iii) a 2D/vdW growth route — e.g. by
extracting the tunable-momentum topological-EI mode energy, or by realizing the engineered-plasmon energy on a flat-band
host. **NOT** 🔴: the energy is materials-reachable (400 meV exists) and a clean q=0 family exists — they are just not yet
in the same crystal.

---

### Sources (markdown)
- [Kogar, Abbamonte et al., Science 358, 1314 (2017) — exciton condensation soft mode in TiSe2](https://www.science.org/doi/10.1126/science.aam6432) ([arXiv:1611.04217](https://arxiv.org/abs/1611.04217))
- [Morosan et al., Nat. Phys. 2, 544 (2006) — Superconductivity in CuxTiSe2](https://www.nature.com/articles/nphys360) ([arXiv:cond-mat/0606529](https://arxiv.org/pdf/cond-mat/0606529))
- [CDW Incommensuration Near the SC Dome in CuxTiSe2 — OSTI 1352597](https://www.osti.gov/pages/biblio/1352597)
- [nanoHUB 30624 — Suppression of Exciton Condensation in Copper-Doped TiSe2](https://nanohub.org/resources/30624)
- [Charge density wave hampers exciton condensation in 1T-TiSe2 — PRR 3, 033097 (2021), OSTI 1802907](https://www.osti.gov/pages/biblio/1802907)
- [Kusmartseva et al., PRL 103, 236401 (2009) — Pressure-induced SC in pristine 1T-TiSe2](https://www.semanticscholar.org/paper/3c30f8140a97b29158de6e6e4dd93ec8a1ed27ce)
- [Effect of Cu intercalation and pressure on excitonic interaction in 1T-TiSe2 — arXiv:1902.02046](https://arxiv.org/abs/1902.02046)
- [CDW and SC dome in TiSe2 from electron-phonon interaction — arXiv:1104.0492](https://ar5iv.labs.arxiv.org/html/1104.0492)
- [Chen et al., Nat. Commun. 6, 8943 (2015) — CDW transition in single-layer TiSe2](https://www.nature.com/articles/ncomms9943)
- [Unconventional CDW Transition in Monolayer 1T-TiSe2 — ACS Nano (2016)](https://pubs.acs.org/doi/10.1021/acsnano.5b06727)
- [CDW suppression in 1T-TiSe2 through Sn intercalation — Nano Res. (2021)](https://link.springer.com/article/10.1007/s12274-021-3859-0)
- [Lu et al., Nat. Commun. 8, 14408 (2017) — Ta2NiSe5 EI transition](https://www.nature.com/articles/ncomms14408)
- [Evidence for an Excitonic Insulator State in Ta2Pd3Te5 — PRX 14, 011046 (2024)](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.14.011046)
- [A New Era of Excitonic Insulators — J. Phys. Soc. Jpn. 94, 012001 (2025)](https://journals.jps.jp/doi/10.7566/JPSJ.94.012001)
- [Topological excitonic insulator with tunable momentum order — Nat. Phys. (2025)](https://www.nature.com/articles/s41567-025-02917-6) (body paywalled; energy unverified)
- [in 't Veld et al., arXiv:2508.06195 — engineered plasmonic SC (clean, tunable energy)](https://arxiv.org/abs/2508.06195)
