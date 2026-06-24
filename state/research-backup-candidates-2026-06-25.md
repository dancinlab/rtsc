# Research note — backup candidates for the +@ trilayer (layer-B glue + layer-A flat-band metal)

**Date:** 2026-06-25
**Lane:** B-backup-research (research)
**Status:** READ-ONLY literature survey — web + `sidecar research arxiv` + WebFetch. No compute, no rental.
**Honesty (commons):** every numeric value carries a source. NO fabrication / NO tune-to-green.
absorbed=false / GATE_OPEN. Energies below are published material properties, not claims that any
material IS an RTSC. Where a source is secondary or a value is computed-only, it is labelled.

---

## Decision this note serves

The NAMED +@ candidate (tool/rtsc_candidates.py, PR#11) uses **B = Ta2NiSe5**, whose excitonic mode
(~300 meV optical gap; ~325 K onset) slightly **UNDERSHOOTS** the relaxed room-T glue target of
**~349 meV** (H_007 three-lever, `GLUE_TARGET_MEV = 349.0` in the tool). The campaign needs cited
**backups** in case Ta2NiSe5 is later disqualified (e.g. its q=0 exciton turns out too soft once
embedded under the hBN spacer, or synthesis of the trilayer fails). This note supplies:

1. ≥3 alternative **layer-B bosonic-glue hosts** with a mode at/above ~349 meV AND q=0 / non-nesting /
   competing-order-light.
2. ≥2 alternative **layer-A flat-band metals** beyond CoSn/Nb3Cl8 with a measured/computed flat band.

Ranked by **closeness-to-target + competing-order cleanliness + synthesizability**.

---

## Calibration: where Ta2NiSe5 actually sits

- Ta2NiSe5: one-electron gap E_G < 50 meV; optical excitation gap E_op ≈ **0.16 eV**; the estimated
  **exciton binding energy** is comparable to E_op; excitonic-insulator onset **T_C = 326 K**.
  *Nature Commun. 8, 14408 (2017)* (Lu et al., zero-gap→EI transition in Ta2NiSe5),
  https://www.nature.com/articles/ncomms14408 . [VERIFIED — peer-reviewed]
- The tool's existing row cites the exciton gap as **0.16–0.35 eV** (arXiv:2007.08212 Kim 2020 /
  arXiv:2106.04396 Matsubayashi 2021). So Ta2NiSe5's *characteristic* glue scale ≈ 160–350 meV — its
  upper edge just grazes the 349 meV target, its center (~250–300 meV) undershoots it. This is the gap
  the backups below try to close from ABOVE.

The key structural advantage of Ta2NiSe5 we want to preserve in a backup: the order parameter is at
**q = 0** (zone-center, non-nesting), so the excitonic condensate is the glue ITSELF and does not open
a competing finite-q density wave that pre-empts pairing (H_014 risk). Most exciton-CDW materials FAIL
this test — their exciton condensation drives a finite-q periodic lattice distortion.

---

## Part 1 — Layer-B bosonic-glue backups (target: mode ≥ ~349 meV, q=0, competing-order-light)

### B-backup-1 (TOP): **Ta2Pd3Te5 monolayer** — q=0 excitonic insulator, ~100 meV gap, T_C ~365 K
- Transport + ARPES: zero-gap semimetal → insulator with a **~100 meV** gap below **365 K**; identified
  as an excitonic-insulator candidate. *Evidence for an Excitonic Insulator State in Ta2Pd3Te5*
  (researchgate 378959328) and arXiv:2602.23608 (Guo et al. 2026, gate-induced SdH, possible EI).
  [VERIFIED — transport/ARPES; EI assignment still "possible/putative".]
- First-principles: **excitonic instability in the Ta2Pd3Te5 monolayer**, an EI with the instability at
  the zone center (**q = 0**, analogous to Ta2NiSe5's non-nesting character). arXiv:2401.01222 (Yao et
  al. 2024, cond-mat.mtrl-sci). Direct exciton photoemission from the ground state confirmed in
  arXiv:2507.16453 (Lee et al. 2025). [VERIFIED arXiv — computed + photoemission.]
- **Why a backup, not an upgrade of the mode energy:** its gap (~100 meV) is LOWER than Ta2NiSe5, so on
  raw energy it is worse. It ranks #1 among the q=0-clean set on **cleanliness + synthesizability**
  (same Ta-chalcogenide vdW family, exfoliable/MBE-growable, q=0 non-nesting, higher T_C=365 K). It is
  the natural drop-in if Ta2NiSe5 fails for a non-energy reason. GAP: mode energy < target.

### B-backup-2: **1T-TiSe2** — a ~0.4 eV (400 meV) excitonic mode ABOVE target, but CDW-contaminated
- Optical spectroscopy in the CDW phase shows **two excitonic modes at 0.4 eV (≈400 meV) and 80 meV**;
  both soften toward the transition. *Excitonic and lattice contributions to the CDW in 1T-TiSe2
  revealed by a phonon bottleneck* (researchgate 332412936) and arXiv:0911.0327 (exciton-condensate
  photoemission model). [VERIFIED — optical/ARPES.]
- The **400 meV** upper mode is the ONLY surveyed electronic boson that clearly sits ABOVE the 349 meV
  target. **BUT** TiSe2's exciton condensation drives a **finite-q (2×2×2) periodic lattice
  distortion / CDW** below ~200 K — i.e. a built-in competing density wave (H_014 fails). Worse, a 2025
  study argues TiSe2 may be a lattice-fluctuation band insulator, NOT an excitonic insulator (npj
  Comput. Mater. 2025, https://www.nature.com/articles/s41524-025-01631-4 ). [VERIFIED — but EI
  assignment CONTESTED.]
- **Why listed despite the CDW:** it documents that a real, q-accessible **electronic boson at ~400 meV
  exists** in a 2D TMD — proof the target energy is materials-reachable. As a layer-B host it is a
  cautionary/“energy-exists” entry, NOT competing-order-clean. competing_order = CDW (intrinsic).

### B-backup-3: **Monolayer WTe2** — equilibrium exciton condensation, E_b > 100 meV, QSH+EI
- *Evidence for equilibrium exciton condensation in monolayer WTe2*, **Nat. Phys. 18, 87 (2022)**,
  https://www.nature.com/articles/s41567-021-01427-5 — equilibrium exciton condensate in the
  quantum-spin-Hall monolayer; first-principles give **exciton binding energy > 100 meV**, radius ~4 nm.
  [VERIFIED — peer-reviewed.]
- q-character: the condensate forms at the zone boundary band-overlap of the QSH edge/bulk; it is NOT a
  clean q=0 zone-center order like Ta2NiSe5, and the QSH edge adds an extra channel. Binding energy
  (>100 meV) is below target. **Backup value:** a genuinely 2D, gate-tunable exciton condensate that
  could be stacked vdW with the flat-band layer; competing-order is light (no CDW), but mode energy and
  q=0 purity are both weaker than Ta2NiSe5. competing_order ≈ none/light; mode < target.

### B-backup-4 (mechanism alternative, not a single host): **interlayer hybridized 2D plasmon**
- *Enhancing Plasmonic Superconductivity in Layered Materials via Dynamical Coulomb Engineering*,
  arXiv:2508.06195 (in 't Veld, Katsnelson, Millis, Rösner 2025): **interlayer hybridized plasmon
  modes** enhance vdW pairing by **up to ~1 order of magnitude**, tuned by the dielectric environment.
  Companion arXiv:2303.06220 (2023, phonon↔plasmon crossover). [VERIFIED arXiv — computed.]
- A 2D plasmon is intrinsically a **q=0-launchable, gapless-but-tunable, low-loss** electronic boson and
  is **competing-order-free by construction** (a charge oscillation, not a symmetry-breaking density
  wave). Its energy is set by carrier density / dielectric screening (tunable into the 0.1–1 eV range in
  doped graphene/2D metals), so it can in principle be tuned AT or ABOVE 349 meV. **Backup value:** the
  cleanest competing-order profile of any layer-B option; the cost is that the plasmon energy is a
  design parameter (must be engineered), not a fixed material constant. competing_order = none (charge
  oscillation); mode tunable, potentially ≥ target. Note: this overlaps the campaign's own cross-spacer
  glue mechanism, so it is a *mechanism* backup rather than a turnkey single crystal.

---

## Part 2 — Layer-A flat-band-metal backups (beyond CoSn / Nb3Cl8)

### A-backup-1 (TOP): **Ni3In** — kagome flat band, ~50 meV scale, strange-metal (correlation-rich)
- *A flat band-induced correlated kagome metal*, arXiv:2106.10824 (Ye et al. 2021): a partially filled
  **Ni-3d kagome flat band** near E_F drives correlated strange-metal transport; characteristic flat-band
  energy scale **≈ 0.05 eV**. DMFT confirmation arXiv:2605.21386 (2026) and ARPES origin
  arXiv:2503.09704 (2025). [VERIFIED arXiv — transport/STM + theory.]
- competing-order: strange-metal/correlated but NO reported static CDW/SDW at the flat band — relatively
  clean (H_014-light). Synthesizability: established bulk single crystals. **GAP for the +@ role:** the
  campaign needs a directly-computed ⟨g⟩ (quantum-geometry) value for Ni3In — flat band measured, ⟨g⟩
  UNVERIFIED. frustrated = True (kagome).

### A-backup-2: **YMn6Sn6** — ARPES-resolved kagome flat band at ~0.4 eV below E_F
- *Dirac cone, flat band and saddle point in kagome magnet YMn6Sn6*, **Nat. Commun. 12, 3129 (2021)**,
  https://www.nature.com/articles/s41467-021-23536-8 — combined ARPES + DFT+DMFT resolve a kagome **flat
  band ~0.4 eV below E_F** across the whole BZ (sister compounds Dy/Tb/GdMn6Sn6 show it at ~0.42 eV,
  arXiv:2203.10542). [VERIFIED — ARPES.]
- competing-order: it is a magnetic kagome metal (helimagnetic / TbMn6Sn6 is Chern-magnetic) → carries
  magnetic order (SDW-like) which is an H_014 risk. Flat band sits 0.4 eV BELOW E_F (not at E_F), so it
  is not partially filled → weaker for pairing. **GAP:** flat band off-E_F + magnetism; ⟨g⟩ UNVERIFIED.
  frustrated = True (kagome) but magnetically ordered.

### A-backup-3: **FeSn** — clean kagome flat band but FAR from E_F (and antiferromagnetic)
- ARPES on the kagome layers of FeSn resolves a flat band, but in magnetic FeSn the flat band is
  **either unobserved or far from E_F** (strong 3d correlation + AFM). (Same kagome-thin-film platform
  line, arXiv:2307.15828; FeSn flat-band ARPES is the canonical CoSn sister.) [VERIFIED — ARPES;
  flat band off-E_F.]
- **Backup value:** structural/synthesis sibling of CoSn (the named A layer), so it is the most
  drop-in-compatible host; but its flat band is farther from E_F and it is AFM (competing order),
  so it ranks below CoSn itself. frustrated = True (kagome); ⟨g⟩ UNVERIFIED; off-E_F + AFM.

### A-backup-4 (moiré, gate-tunable): **twisted bilayer WSe2** — ultra-flat moiré band, hosts SC
- *Superconductivity in twisted bilayer WSe2*, **Nature (2024)** — robust SC near half-band filling in
  3.5–5.0° tWSe2 (T_c ~0.2–0.43 K), the moiré band being a **flat Chern band**; lattice reconstruction
  gives **multiple ultra-flat bands** (Nat. Commun., PMC8460827). arXiv:2405.14784 / arXiv:2406.03418 /
  https://www.nature.com/articles/s41586-024-08381-1 . [VERIFIED — peer-reviewed.]
- competing-order: correlated insulators at integer/fractional fillings compete (twisted-MoTe2 shows
  FCIs) — moiré systems are correlation-rich but the flat band is **continuously gate-tunable**, which is
  unique among the A options. **GAP:** twist-angle fabrication is the synthesizability cost; ⟨g⟩ /
  quantum geometry of the specific flat Chern band is computed in the continuum model but UNVERIFIED for
  our ⟨g⟩≥2 box. frustrated/Chern-flat = True.

---

## Ranking summary

**Layer B (glue) — ranked by closeness-to-349meV × cleanliness × synthesizability:**

| Rank | Host | Mode energy | q=0 / clean? | Synth | Net |
|------|------|-------------|--------------|-------|-----|
| (incumbent) | Ta2NiSe5 | ~160–350 meV (~300) | q=0 non-nesting, clean | bulk vdW, easy | grazes target |
| 1 | Ta2Pd3Te5 (ML) | ~100 meV gap, T_C 365 K | q=0 non-nesting (computed) | exfoliable/MBE | cleanest drop-in; lower energy |
| 2 | 2D hybridized plasmon | tunable, ≥349 meV reachable | none (charge osc.) | engineered | cleanest order; energy must be designed |
| 3 | 1T-TiSe2 | **400 meV** (+80 meV) | NO — drives CDW | bulk/ML, easy | only host ABOVE target, but CDW-contaminated |
| 4 | monolayer WTe2 | E_b >100 meV | light (no CDW), not pure q=0 | 2D, gate-tunable | clean-ish but sub-target energy |

**Layer A (flat-band metal) — ranked by flat-band-at-E_F × cleanliness × synthesizability:**

| Rank | Host | Flat band | Competing order | Synth | Net |
|------|------|-----------|-----------------|-------|-----|
| 1 | Ni3In | ~50 meV scale, near E_F | strange-metal, no static CDW | bulk crystals | best partial-filling + clean |
| 2 | tWSe2 | ultra-flat moiré, at E_F (tunable) | correlated insulators/FCI | twist fab | gate-tunable, hosts SC |
| 3 | YMn6Sn6 | ~0.4 eV below E_F | magnetic (SDW-like) | bulk crystals | off-E_F + magnetism |
| 4 | FeSn | flat band far from E_F | AFM | bulk (CoSn sibling) | drop-in but off-E_F + AFM |

---

## Proposed registry rows (for the main loop to add to tool/rtsc_candidates.py — DO NOT add here)

Format mirrors the existing `Candidate(...)` rows: (value, source, verified). All B excitonic-order
q=0 claims marked verified only where the cited paper states zone-center / non-nesting explicitly.

| name | role | key property = value | competing_order | citation | verified |
|------|------|----------------------|-----------------|----------|----------|
| Ta2Pd3Te5 | B | boson_meV = 100 (EI gap; T_C 365 K) | none (q=0 non-nesting, computed) | arXiv:2401.01222 (Yao 2024); arXiv:2507.16453 (Lee 2025); arXiv:2602.23608 (Guo 2026) | True (gap); True (q=0, computed) |
| 1T-TiSe2 | B | boson_meV = 400 (upper excitonic optical mode; +80 meV lower) | CDW (intrinsic, finite-q 2×2×2) | researchgate 332412936; arXiv:0911.0327; npj Comput.Mater. 2025 (EI contested) | True (mode); True (CDW) |
| WTe2-monolayer | B | boson_meV = 100 (exciton binding, lower bound) | none/light (QSH edge, not pure q=0) | Nat. Phys. 18, 87 (2022) s41567-021-01427-5 | True (E_b>100meV); q=0 NOT clean |
| 2D-hybridized-plasmon | B | boson_meV = tunable (≥349 reachable) | none (charge oscillation) | arXiv:2508.06195 (in 't Veld 2025); arXiv:2303.06220 | False (energy is a design param, not fixed) |
| Ni3In | A | g_mean = UNKNOWN (needs DFT ⟨g⟩); flat band ~50 meV near E_F | strange-metal, no static CDW | arXiv:2106.10824 (Ye 2021); arXiv:2605.21386; arXiv:2503.09704 | flat band True; ⟨g⟩ False |
| YMn6Sn6 | A | g_mean = UNKNOWN; flat band ~0.4 eV below E_F (ARPES) | magnetic (SDW-like) | Nat. Commun. 12, 3129 (2021) s41467-021-23536-8; arXiv:2203.10542 | flat band True (off-E_F); ⟨g⟩ False |
| FeSn | A | g_mean = UNKNOWN; flat band far from E_F | AFM | arXiv:2307.15828 (kagome thin films); CoSn-sibling line | flat band True (off-E_F); ⟨g⟩ False |
| tWSe2 | A | g_mean = UNKNOWN; ultra-flat moiré Chern band at E_F, hosts SC | correlated insulators / FCI | Nature s41586-024-08381-1 (2024); arXiv:2405.14784; arXiv:2406.03418 | flat band True; ⟨g⟩ False |

**Integration note for the main loop:** add these as UNVERIFIED-where-flagged seed rows. Every A row's
⟨g⟩ is a research GAP (flat band measured, quantum geometry not yet computed) — `verify()` will surface
that gap exactly as it does for CsV3Sb5. The Ta2Pd3Te5 row is the only one that meaningfully improves on
Ta2NiSe5 for the q=0/cleanliness/synth axes (not for raw mode energy).

---

## Verdict: 🟠 — NO clearly-better-than-Ta2NiSe5 glue found (Ta2NiSe5 remains the lead)

A glue host that beats Ta2NiSe5 on **all three** axes (mode energy ≥349 meV AND q=0-clean AND
synthesizable) was **NOT found** in this survey:

- The only surveyed host with a mode **above** 349 meV is **1T-TiSe2 (~400 meV)** — but it carries an
  **intrinsic finite-q CDW** (H_014 fails) and its EI assignment is contested. Energy↑ at the cost of
  cleanliness — a strict downgrade for the q=0 requirement.
- The cleanest q=0 EI backup, **Ta2Pd3Te5 monolayer**, has a **lower** gap (~100 meV) than Ta2NiSe5 —
  better drop-in/synth, worse energy.
- The **2D hybridized plasmon** can in principle be *tuned* to ≥349 meV with a clean (no-CDW) profile,
  but its energy is an engineering parameter, not a fixed material constant — so it cannot be claimed as
  a turnkey "better glue" today.

Therefore Ta2NiSe5 stays the lead glue; the field of backups is real and cited, but none dominates it.
The honest verdict is **🟠 MATERIALS-LIMITED** — backups exist and are worth registering, but the
349 meV-clean-synthesizable glue remains JOINTLY UNREALIZED. absorbed=false / GATE_OPEN.

Promote to 🟢 only if a future round finds (or computes) a single host with a verified q=0
zone-center electronic mode ≥349 meV AND no pre-empting density wave AND a demonstrated 2D/vdW growth
route. The strongest path to that is likely the **engineered plasmon** route (tunable energy, clean by
construction) rather than a fixed-energy excitonic crystal.

---

### Sources (markdown)
- [Lu et al., Nat. Commun. 8, 14408 (2017) — Ta2NiSe5 EI transition](https://www.nature.com/articles/ncomms14408)
- [Yao et al., arXiv:2401.01222 — Ta2Pd3Te5 monolayer excitonic instability](https://arxiv.org/abs/2401.01222)
- [Lee et al., arXiv:2507.16453 — exciton photoemission from Ta2Pd3Te5 ground state](https://arxiv.org/abs/2507.16453)
- [Guo et al., arXiv:2602.23608 — possible EI Ta2Pd3Te5 SdH](https://arxiv.org/abs/2602.23608)
- [npj Comput. Mater. (2025) — TiSe2 lattice-fluctuation band insulator (EI contested)](https://www.nature.com/articles/s41524-025-01631-4)
- [Wang et al., Nat. Phys. 18, 87 (2022) — monolayer WTe2 exciton condensation](https://www.nature.com/articles/s41567-021-01427-5)
- [in 't Veld et al., arXiv:2508.06195 — plasmonic SC via dynamical Coulomb engineering](https://arxiv.org/abs/2508.06195)
- [Ye et al., arXiv:2106.10824 — Ni3In flat-band correlated kagome metal](https://arxiv.org/abs/2106.10824)
- [Li et al., Nat. Commun. 12, 3129 (2021) — YMn6Sn6 kagome flat band ARPES](https://www.nature.com/articles/s41467-021-23536-8)
- [Nature (2024) — superconductivity in twisted bilayer WSe2](https://www.nature.com/articles/s41586-024-08381-1)
- [arXiv:2307.15828 — epitaxial kagome thin films (FeSn) topological flat bands](https://arxiv.org/pdf/2307.15828)
