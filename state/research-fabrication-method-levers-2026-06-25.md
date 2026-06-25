# Research-first pass — the FABRICATION-METHOD lever: can a PROCESS change unlock the +@ walls without a new material? (2026-06-25)

**Scope.** READ-ONLY literature pass (web + arXiv abstracts via WebFetch; `sidecar research arxiv`
was rate-limited HTTP 429/503 during this pass so arXiv was reached by id via WebFetch instead).
NO compute, NO fab. Triggered by the CLAUDE.md "research-first / 실측전 research" rule and by a
META-LEVER the user raised: **change the FABRICATION/PROCESS, not the material** — the "copper can't
replace gold, but a new making-method succeeded" idea. In superconductivity, process-not-composition
is a REAL, measured lever (FeSe bulk → FeSe/SrTiO3 monolayer; ionic gating; strain). The question:
do the campaign's two MATERIAL walls (CoSn doping; Ta2NiSe5 exciton trap) survive as **method**
walls?

The two walls, as assessed in `state/papers/plus-at-combination-campaign-synthesis.md` §4:
- **CoSn doping wall (H_027/H_029):** "flat band ~1.45 eV below E_F; reaching E_F needs ~1.58
  holes/f.u. = chemical substitution (extreme)." Assessed assuming *conventional* doping.
- **Ta2NiSe5 exciton trap (prior-art note 2026-06-25):** Ta2NiSe5 superconducts (1.2 K, 8 GPa) only
  AFTER its exciton is DESTROYED by pressure; the live exciton COMPETES with SC. Assessed as fatal.

`absorbed=false` / GATE_OPEN unchanged throughout. No material is claimed to BE an RTSC.

---

## VERDICT (one paragraph)

A fabrication-method lever is **real, measured, and large** (FeSe bulk Tc 8 K → monolayer FeSe/SrTiO3
Tc 65–100 K, ~10× — and the interface delivers 20–50 K MORE Tc than identical carrier doping alone, so
it is genuinely a *process* effect, not just doping). It can BOOST Tc and ENABLE doping that chemistry
cannot. But applied honestly to our two walls it is **asymmetric**: (1) **The CoSn "doping wall" is
partly a measurement-vs-DFT artifact, and to the extent it is real it is METHOD-leaning 🟠.** The
*published, measured* CoSn flat d-band sits **~100 meV below E_F** (arXiv:2102.08979 / PRMat 5,
044202), and "a few percent Fe or In" hole substitution brings it to E_F — NOT the "1.45 eV /
1.58 h/f.u." in the synthesis paper, which targets a *different, deeper* flat manifold. A ~100 meV /
few-%-hole target is squarely inside what light chemical doping reaches, and at the margins inside what
**ionic-liquid gating** (≈10^14–10^15 cm^-2) reaches in the **top ~1 unit cell** — and epitaxial
kagome thin films are explicitly proposed as the platform to gate/strain the flat band across E_F
(arXiv:2307.15828). The honest caveat: gating is a *surface/2D* lever (screening length ≈ 1 u.c. at
~7×10^14 cm^-2), so it cannot bulk-dope 1.58 h/f.u.; but for a 2D/monolayer +@ device that is the
regime we want anyway. (2) **The Ta2NiSe5 exciton trap is essentially a MATERIAL/physics wall, not a
method wall 🔴-leaning.** Strain, S-substitution, and dimensionality DO tune the exciton — they trace a
**dome** of EI Tc vs band gap (max near zero-gap, in the BCS–BEC crossover) and uniaxial pressure even
*boosts* excitonic fluctuations — but in EVERY measured case superconductivity appears only where the
exciton is *suppressed/destroyed* (pressure → EI→semimetal → phonon SC). No measured Ta2NiSe5 (or any
EI) state shows the exciton COEXISTING with / cooperating with SC; that remains theory. So: **method
plausibly opens the CoSn doping wall (and is IN-SILICO-testable via gated/strained slab DFT — our
domain); method does NOT, on present evidence, decouple the Ta2NiSe5 exciton from its competition with
SC.** And no method conjures a 293 K @ 1 atm phase that does not exist — `absorbed=true` still needs
accredited transport + Meissner + H_c2/T_c regardless.

---

## Q1 — "Method-not-material" SC precedents (proof the lever is real)

The lever is real and quantified. Ranked by how far the METHOD reaches beyond conventional chemical
doping:

| Method | System | Effect (measured) | Reaches what chemistry can't | Cite |
|---|---|---|---|---|
| **Interface / epitaxy** | FeSe bulk → **monolayer FeSe/SrTiO3** | Tc **8 K → 65–100 K** (~10×); gap vanishes ~65 K; reports to >100 K | Interface gives **20–50 K MORE than identical carrier doping** — a process effect beyond doping (charge transfer + interfacial phonon) | s41467-019-08560-z (Nat. Commun. 2019); PMID 25419814 (>100 K); sciadv.aay4517 |
| **Ionic-liquid / EDL gating** | SrTiO3, **ZrNCl (Tc 15.2 K)**, MoS2, KTaO3, FeSe | Field-INDUCES SC in band insulators; **n_2D ≈ 10^14–10^15 cm^-2** | Reaches carrier densities **~1–2 orders above conventional FET dielectrics**; SC where chemistry gave none | nmat2587 (ZrNCl, liquid-gated film); IOP 10.1088/2515-7639/ab8270 (review); sciadv.abn4273 (KTaO3) |
| **Pressure** | Ta2NiSe5, H3S/LaH10 class | Induces/raises SC | Accesses metastable/high-density phases unreachable at 1 atm — but NOT a 1-atm device | arXiv:2106.04396 (Ta2NiSe5 1.2 K @ 8 GPa) |
| **Epitaxial strain** | kagome thin films (proposed), cuprate films | Tunes bands / Tc | Continuous lattice tuning beyond discrete substitution | arXiv:2307.15828 (epitaxial kagome platform) |
| **Metastable / non-equilibrium synthesis** | metal hydrides, high-entropy nanomaterials | New crystal structures impossible at equilibrium (Hume–Rothery bypass) | Quench-trapped phases outside the equilibrium phase diagram | PMC12931243 (non-equilibrium synthesis review) |

- **Strongest precedent = FeSe/SrTiO3 monolayer:** Tc **8 K → up to ~100 K**, the canonical
  "method-not-material" win. Crucially the interface adds **20–50 K beyond what the same electron
  count gives** in doped bulk FeSe — so it is not reducible to "just doping."
- **The user's "copper-can't-replace-gold-but-a-new-method-succeeded" anecdote**: I found **no exact
  documented metallurgy quote** matching it; treat it as an **analogy, not a citation**. The faithful
  *physics* analog is FeSe/STO (same material, new making-method → 10× the property) and
  non-equilibrium/metastable synthesis (PMC12931243), where a *process* (ultrafast quench) makes
  phases that *composition rules alone forbid* (Hume–Rothery). Labeled honestly: the anecdote is an
  analogy; FeSe/STO is its real measured counterpart.

## Q2 — CoSn doping wall: method wall or material wall?

**Partly a DFT-vs-measurement discrepancy; to the extent real, it is METHOD-leaning 🟠.**

- **The number to flag (honesty):** the synthesis paper's "flat band 1.45 eV below E_F, needs
  1.58 holes/f.u." does NOT match the **published, ARPES/measured** CoSn flat band. arXiv:2102.08979
  (PRMat 5, 044202, "Tuning the flat bands of the kagome metal CoSn with Fe, In, or Ni doping") states
  CoSn has "relatively flat d-bands centered **~100 meV below E_F**," and within rigid-band, **"hole
  doping with a few percent of Fe or In moves the flat bands closer to E_F."** So the *relevant* flat
  band is ~100 meV / a-few-%-holes away — the campaign's 1.45 eV / 1.58 h/f.u. targets a *deeper*
  manifold (likely a different/lower flat band, or a PBE+U-deepened one — H_029). **Which flat band the
  +@ geometry needs should be reconciled before the wall is called "extreme."**
- **Can a METHOD reach it?**
  - *Chemical (light):* a few % Fe/In already does it (measured) — this is barely "extreme" for the
    100 meV band.
  - *Ionic-liquid gating:* reaches n_2D ≈ 10^14–10^15 cm^-2. At ~7×10^14 cm^-2 the screening length
    ≈ **one unit cell** (sciadv.abn4273 / KTaO3-class), i.e. gating dopes the **top ~1 u.c.** ≈ order
    ~1 carrier per surface f.u. — enough to shift E_F by a few hundred meV in a 2D/monolayer layer, but
    NOT enough to bulk-dope 1.58 h/f.u. through a thick crystal. **For a 2D/monolayer +@ device this is
    the correct regime** (the +@ architecture is a thin-stack anyway).
  - *Epitaxial strain / thin film:* arXiv:2307.15828 ("Epitaxial Kagome Thin Films as a Platform for
    Topological Flat Bands") explicitly names **electrostatic gating OR strain to tune flat bands across
    E_F** as the "key next step." FeSn thin-film ARPES shows sharper flat bands than bulk. So the kagome
    community already treats gate/strain-to-flat-band as the realistic method.
- **Precedent for gating a kagome flat-band metal onto its flat band:** **proposed, not yet measured**
  (arXiv:2307.15828 names it as the goal; no transport paper achieving it was found). So: method is the
  *intended* route, demonstration is pending.
- **Verdict:** the CoSn doping wall is **NOT a hard material wall**. It is (a) partly a band-bookkeeping
  discrepancy to reconcile, and (b) a 🟠 **method wall** — light chemical doping reaches the measured
  ~100 meV band; gating/strain reach E_F in a 2D layer (which is the +@ regime); only *bulk* 1.58 h/f.u.
  is out of reach for gating.

## Q3 — Ta2NiSe5 exciton trap: method wall or material wall?

**Method TUNES the exciton (dome, BCS–BEC crossover) but does NOT make it cooperate with SC →
essentially a MATERIAL/physics wall 🔴-leaning.**

- **Strain/S-sub/pressure DO tune the EI:** Ta2Ni(Se,S)5 and physical pressure trace a **dome of EI
  Tc vs band gap**, peaked near **zero gap**, where the system is in the **BCS–BEC crossover /
  strong-coupling (BEC) regime** (s41467-023-43365-1; ncomms14408; JPSJ 94, 012001 (2025) review).
  Uniaxial compressive strain *reduces* monoclinic distortion and **enhances excitonic fluctuations**
  (MPI-FKF 2025; PRL 10.1103/jysr-2dk1). So the exciton is highly method-tunable — the lever is real.
- **But the SC payoff never coexists with the live exciton:** in every *measured* case, Ta2NiSe5
  superconducts (**Tc ≈ 1.2 K, ~8 GPa**) only **after** the EI is destroyed (EI→semimetal ~3 GPa),
  and the SC is **soft-phonon / electron-lattice**, not excitonic (arXiv:2106.04396; 2208.12077).
  Tuning toward the zero-gap crossover *raises the EI Tc*, not a SC Tc. **Exciton-cooperating-with-SC
  is theory only** (the prior-art note's Q2/Q4: PRL 133.226903; arXiv:2402.02747 — all proposals).
- **Dimensionality:** thin-flake Ta2NiSe5 has its EI transition *reduced* ~9% (interband Coulomb
  dominates), and a conducting (Au) substrate *suppresses* the transition by >100 K (arXiv:2512.12439).
  So dimensionality/interface push the exciton DOWN or AWAY here — they do not open an exciton+SC window.
- **Verdict:** the exciton trap is a **physics/material wall**. No measured method makes the exciton and
  SC cooperate; the only measured Ta2NiSe5 SC requires killing the exciton. Method can move the system
  along the dome but does not deliver the competing-order-free, live-exciton-glued SC the +@ premise
  needs. (Not a *no-go theorem* — the cooperative crossover is an open theory frontier — but zero
  measured support.)

## Q4 — The general map: METHOD-fixable vs MATERIAL-fixable

| Wall | Method lever | Real measured precedent (Tc) | In-silico-testable? | Verdict |
|---|---|---|---|---|
| **CoSn flat band not at E_F** | epitaxial-strain + electrostatic/ionic gating of a kagome thin film; light Fe/In hole-doping | gating-induced SC in band insulators (ZrNCl 15.2 K, SrTiO3, KTaO3); FeSe/STO interface doping; few-% Fe/In **measured** to move CoSn flat band toward E_F | **YES** — gated/strained slab DFT (E_F shift vs field/strain), our exact domain (cf. H_015 hBN DFT, H_024/H_027 ∫tr g) | 🟠 **METHOD-leaning** (reconcile the 100 meV-vs-1.45 eV band first) |
| **Glue scale ≥349 meV** | interface phonon enhancement (FeSe/STO-style); strain-stiffened phonons | FeSe/STO interfacial mode + charge transfer → 10× Tc | partly (interface-phonon DFT) — but no clean ≥349 meV q=0 glue exists (synthesis §4.1) | 🟠/🔴 — method boosts a glue but cannot create a ≥349 meV one |
| **Ta2NiSe5 exciton COMPETES with SC** | strain / S-sub / dimensionality / BCS-BEC-crossover tuning | dome of EI Tc (s41467-023-43365-1); pressure-SC only when EI destroyed (1.2 K) | partly (strained-slab DFT of gap/distortion) — but the SC-coexistence is a many-body GW/BSE question PBE can't settle | 🔴-leaning **MATERIAL/physics wall** |
| **Excitonic proximity-SC never measured (50 yr)** | (any) device demonstration | none (prior-art note Q2) | no — needs a real device | 🔴 (material/measurement, not method) |
| **No realizable system with all three co-existing** | metastable / non-equilibrium synthesis | metastable hydrides, high-entropy phases (Hume–Rothery bypass) | partly (formation-energy / metastable-phase DFT) | 🟠 — method widens phase space but can't conjure a 293 K phase |

**Honest summary of the map:** the **geometry/doping** half of the campaign (place E_F on a flat band)
is the most METHOD-fixable and the most IN-SILICO-testable — strain + gating of a kagome thin film is
the kagome community's own stated route, and a gated/strained-slab DFT E_F-vs-field/strain scan is
squarely our domain. The **glue** half (a clean ≥349 meV q=0 boson, and the Ta2NiSe5 exciton's
competition with SC) is MATERIAL/physics-bound: method can *tune* the exciton along a dome but does not
*decouple* it from its competition with SC, and no method invents a ≥349 meV glue that doesn't exist.

---

## What is IN-SILICO-testable next (our domain — no fab/rent needed)

1. **Reconcile CoSn's flat-band bookkeeping (cheapest, highest-value).** Re-extract, from our existing
   CoSn DFT, the energy of EACH flat manifold vs E_F and identify WHICH one the +@ geometry (∫tr g)
   actually uses. If it is the measured ~100 meV band, the "1.58 h/f.u. / 1.45 eV" wall is mostly an
   artifact and the doping wall downgrades to "light doping / gating." Pure post-processing of H_024/
   H_027 output. (Settles a number, not a measurement.)
2. **Gated / strained CoSn-slab DFT E_F scan.** Compute ΔE_F vs surface charge (jellium/dipole
   field, ~10^14–10^15 cm^-2) and vs biaxial strain (±2–3%), for a few-layer CoSn slab — does the flat
   band reach E_F in the TOP layer? This is the exact in-silico test of "can gating put a 2D/monolayer
   CoSn layer's flat band at E_F." Standard slab+field DFT (same QE-MPI stack as H_015).
3. **Strained-Ta2NiSe5-slab gap/distortion DFT.** Map monoclinic-distortion / one-electron gap vs
   uniaxial strain (to locate the zero-gap / crossover point). NOTE the honest limit: PBE/PBE+U cannot
   reproduce the *excitonic* gap (synthesis §4.2, H_026) — this DFT locates the *lattice/one-electron*
   crossover only; the exciton-vs-SC cooperation question needs GW/BSE or measurement, NOT settleable by
   our PBE stack. So test the lattice lever in-silico, but do NOT claim it settles the exciton trap.
4. **(Do NOT spend on)**: real gated-transport fab, GPU cRPA for the glue (the glue scale is
   literature-measured already, synthesis §4), or building the trilayer — all blocked behind the
   physics walls and the research-first rule.

---

## Citations (load-bearing; via web + arXiv-by-id WebFetch; labels honest)

- **s41467-019-08560-z** (Nat. Commun. 2019) + **PMID 25419814** (Nature 2014, >100 K) +
  **sciadv.aay4517** — FeSe **bulk 8 K → monolayer/STO 65–100 K**; interface adds **20–50 K beyond
  identical doping** (cooperative interface-phonon + charge transfer). [STRONGEST method-not-material
  precedent, MEASURED.]
- **arXiv:2102.08979** = **PhysRevMaterials 5, 044202** — CoSn flat d-band **~100 meV below E_F**;
  "few % Fe or In" hole doping moves it toward E_F. [KEY: contradicts the campaign's 1.45 eV/1.58 h/f.u.
  for the relevant band — reconcile.]
- **arXiv:2307.15828** = **Nano Lett. (acs.nanolett.3c01961)** — "Epitaxial Kagome Thin Films …";
  names **electrostatic gating OR strain to tune flat bands across E_F** as the key next step. [Method
  route for the CoSn wall, PROPOSED.]
- **nmat2587** (Nat. Mater.) — liquid-gated **ZrNCl Tc 15.2 K**, field-induced SC. **IOP
  10.1088/2515-7639/ab8270** (EDL-transistor review) — gating reaches **n_2D 10^14–10^15 cm^-2**.
  **sciadv.abn4273** (KTaO3) — screening length **≈ 1 unit cell at ~7×10^14 cm^-2** (gating = top-~1-u.c.
  lever). [Quantifies the gating ceiling and its 2D/surface nature.]
- **s41467-023-43365-1** (Nat. Commun. 2023, Ta2Ni(Se,S)5) + **ncomms14408** (zero-gap→EI) +
  **JPSJ 94, 012001 (2025)** review — **dome of EI Tc vs band gap**, peak near zero-gap, **BCS–BEC
  crossover / BEC regime**. [Exciton IS method-tunable along a dome.]
- **arXiv:2106.04396** + **arXiv:2208.12077** — Ta2NiSe5 SC **Tc ≈ 1.2 K @ ~8 GPa, only after EI
  destroyed, phonon-mediated**. [KEY NEGATIVE: SC ≠ live exciton.]
- **arXiv:2512.12439** — thin-flake Ta2NiSe5; conducting (Au) substrate **suppresses the EI transition
  by >100 K**; insulating Al2O3 keeps ~326 K. [Dimensionality/interface push the exciton AWAY here.]
- **arXiv:2404.18727** (BCS–BEC crossover of e-h pairing in graphite under field/pressure) — crossover
  IS pressure-tunable but "summit locked"; NO SC coexistence reported. [Crossover-tunable ≠ SC.]
- **PMC12931243** (non-equilibrium / metastable synthesis review) — process (ultrafast quench)
  accesses phases **forbidden by Hume–Rothery composition rules**. [Physics analog of the user's
  copper/gold anecdote — labeled ANALOGY.]
- Carried from prior-art note: **PMC10622413** (kagome-magnet/metal interface SC, TbMn6Sn6/Au,
  Tc≈3.6 K — closest real metal-interface precedent, but glue is a magnet, not an EI);
  **PRL 133, 226903 (2024)** + **arXiv:2402.02747** (exciton-SC cooperation — THEORY only).

**Honesty note.** No fabricated citations. The copper/gold anecdote is treated as an ANALOGY (its real
measured counterpart = FeSe/STO + metastable synthesis), not quoted as a source. All Tc / carrier-
density / band-position numbers are as reported by the cited works (not re-derived here). The CoSn
100 meV-vs-1.45 eV discrepancy is flagged as an open bookkeeping item, not silently adopted.
`absorbed=false` / GATE_OPEN unchanged; no material is claimed to BE an RTSC; no method is claimed to
conjure a 293 K @ 1 atm phase that does not exist.
