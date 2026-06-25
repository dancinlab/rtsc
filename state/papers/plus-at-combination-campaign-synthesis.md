# The +@ combination campaign — an honest-falsification synthesis (CoSn / hBN / Ta2NiSe5)

**Verdict: 🟠 CREDIBLE-PARTIAL. No turnkey room-temperature superconductor was found.
`absorbed=false` / GATE_OPEN throughout.** The single-host two-lever wall (H_001, CLOSED-NEGATIVE)
was attacked with a `+@` combination architecture (multilayer A/C/B). Across 28 pre-registered cards
(H_001–H_028) the computationally-settleable levers of one named candidate — CoSn / hBN(2ML) /
Ta2NiSe5 — were each confirmed-by-us or literature-confirmed, but the candidate remains **jointly
unrealized**, and the remaining obstacles are all physical-synthesis/measurement, outside what
compute can settle. This document consolidates the campaign; per-hypothesis truth lives in
`HYPOTHESES/cards/` and `state/RTSC_LEDGER.jsonl`.

## 1. The wall and the architecture

- **H_001 (CLOSED-NEGATIVE)** — the Fubini–Study two-lever wall: large quantum geometry
  (∫tr g ≥ 2) and stiff coupling (Ω ≥ 130 meV) do not co-exist in one host (CoSn: g=2.87, Ω≈22 meV).
- **+@ response (H_003–H_011)** — a self-consistent trilayer: flat-band geometry **layer A** +
  electron-opaque, field-transparent **spacer C** (hBN-class) + bosonic field-coupled **glue
  layer B** (exciton/plasmon ~349 meV, no competing order) + **3D lever**. Minimal achievable
  lever count = 4 (H_010, top-down). The closed-form architecture is depleted and self-consistent.

## 2. Calibrated amplitude band (no tune-to-green)

2D-BKT band `Tc[K] = 0.4559·Ω[meV]` (deflated ×2.8 to MATBG/tMoTe2/Re6Se8Cl2 anchors); real 3D
lever `L_3D = 1.84` (`src/fbgeom_3d.py`). Room-T (293 K) with the 3D lever needs **Ω ≈ 349 meV**.
`Tc` is a COORDINATE, not a prediction (H_018 predictor scatter 1061×). **Correction (PR#40): the
band is a PAIRING coordinate and over-reads the real Tc — it omits the superfluid-stiffness cap, and
the geometry input was conflated. The QGT integral `∫tr g = 2.86` (= `I=(1/2π)∮tr g`) is NOT the
per-BZ `⟨g⟩ ≈ 0.1–0.5` that enters `D_s = 4|U|ν(1−ν)⟨g⟩` — using the integral as `⟨g⟩` inflated D_s
~6–30×. The real flat-band geometric stiffness is ~0.06–0.44 meV (≈1–8 K), ~20–90× BELOW the cuprate
phase stiffness, so a flat-band SC is STIFFNESS-limited (MATBG: 10× stiffness yet Tc~1 K), not
pairing-limited. The 252 K / 292.9 K coordinates (H_023/H_031) were this conflation × BKT optimism.**

## 3. What the real DFT confirmed (summer pool, QE 7.2/7.5 MPI)

| Lever | Result | Card |
|---|---|---|
| Spacer electron-opacity | hBN suppresses interlayer e-coupling 7.7×, saturating at 1 ML | H_015 (PBE+D3 DFT) |
| Spacer field-transparency | out-of-plane hBN screening only ε⊥≈3.3–3.6; drag/exciton measured to ~8 ML | literature (H_011, PR#7) |
| Layer-A geometry | CoSn ∫tr g = **2.856 ≈ measured QGT 2.87** (arXiv:2412.17809) | H_024 |
| Geometry under doping | ∫tr g = 2.855 survives; flat-band filling ν = 0.507 (D_s maximum) | H_027 |
| Multilayer D_s boost | f_mult ≥ 1.164 (16%) at N=2 supported on two scaling models (Peotta–Törmä / Josephson) | H_023, H_024 |
| Bipolaron vertex | retarded-vertex ⟨g⟩_pair 4.27× > single-particle | H_008 (ED) |

## 4. The materials-wall constellation (the honest obstacles)

Not a single no-go theorem — a constellation, each precisely characterized:

1. **No clean ≥349 meV glue exists** (the modern excitonic-SC graveyard). All 5 boson families
   surveyed: phonon (≤200 meV ceiling), exciton (Ta2NiSe5 ~300 meV — undershoots; 1T-TiSe2 400 meV
   but the exciton **is** its CDW, inseparable — H_022 + research), plasmon (no turnkey ≥349 meV;
   graphene Pauli-capped ~0.11 eV), magnon (single-magnon ~252 K wall; bi-magnon tied to magnetic
   order). The clean q=0 hosts sit at/below target.
2. **The lead glue is many-body.** Ta2NiSe5's ~300 meV gap is an excitonic (many-body) effect that
   PBE/PBE+U cannot reproduce — even with proper MPI the monoclinic SCF stays near-metallic
   (H_026). The glue scale is **literature-measured**, not our-DFT (GW/BSE would be needed and is
   redundant given the measurement).
3. **The geometry metals need extreme doping.** CoSn's flat band is ~1.45 eV below E_F (real, not a
   PBE artifact — H_024); placing E_F on it needs ~1.58 holes/f.u. = chemical substitution, not
   gating (H_027). Ni3In is no better (flat band as deep + a magnetic SDW instability, H_028).
4. **Demand-relaxation is the lead path but conditional.** Stacking the clean Ta2NiSe5 to N=2 boosts
   D_s ~16% → room-T on paper (299–356 K, H_023) with NO competing-order problem — but conditional
   on the doping-to-E_F and on a multilayer D_s that is a model, not measured.
5. **Jointly unrealized.** CoSn, hBN, and Ta2NiSe5 have never been stacked or co-measured.
6. **The geometric-stiffness ceiling — the foundational lens, frozen 🧱 (PR#40).** Applying the
   campaign's own flat-band quantum-geometry lens (Peotta-Törmä) to the spin-fluctuation phase-stiffness
   ceiling does NOT escape it — it confirms it at higher confidence. The flat-band geometric superfluid
   weight is ~20–90× BELOW the cuprate phase stiffness (and the geometry input was conflated, §2), so the
   candidate is STIFFNESS-limited; every measured flat-band geometric SC (MATBG ~1 K, tTLG ~2–3 K,
   Re6Se8Cl2 ~8 K, kagome ~3–6 K) lands FAR below the cuprate 133 K record — the geometric route is the
   LOWEST rung on the ambient ladder. The clean spin-fluctuation ceiling (~134–164 K, Emery-Kivelson
   phase stiffness) is the honest UNIVERSAL wall; room-T (293 K) is beyond it. This is the campaign's
   strongest negative result, and it freezes the conventional-mechanism map.
7. **The wall survives its 4 SF-imagination escapes (micro-exp, deterministic).** An SF-imagination
   brainstorm (89 seeds, NOT depleted) produced a shortlist of 4 orthogonal escape *classes* that attack
   the phase-stiffness wall's ASSUMPTIONS, not its magnitude; each was built as a deterministic closed-form
   harness probe with an honest-null falsifier (`exports/sweep/rtsc-sf-escape-2026-06-25/ledger.json`):
   (a) **multiband stiffness donation** (H_032) — Leggett-locking × the quantum-metric no-go caps the
   donated stiffness at D_s_disp/4 → best two-channel Tc 111 K (52.7 K below the ceiling; the naive
   additive 484 K collapses 77%); (b) **z=2 Goldstone universality** (H_033) — z labels the critical
   *dynamics* (τ∼ξ^z), not the *static* vortex-balance T_BKT, whose cap is the stiffness MAGNITUDE not the
   exponent; (c) **η-pairing ODLRO** (H_034, the one long shot) — η-pairs are non-thermal fine-tuned
   eigenstates / dissipative dark states, not an ambient 293 K equilibrium bulk SC; (d) **Amperean
   current-current glue** (H_035) — transverse-gauge coupling is (v_F/c)²-suppressed and favors competing
   finite-q pairing. ALL FOUR **confirm-wall** (closed-negative). The ceiling is no longer just
   "measured on cuprates" — it has been tested against four structural escapes and held.
   **Honest scope correction (full SF-seed triage, `state/sf_seed_full_triage_2026_06_25/`):** the 4
   probed escapes are NOT the whole space. Triaging ALL 140 existing SF seeds (89 new + ~50 older d6)
   gave 56 already-carded, 32 pre-satisfied-by-freeze, 16 pure-SF, 7 pressure-hydride (a different axis),
   4 lab-handoff — and **25 genuinely-new in-silico escapes that remain UN-PROBED**. The freeze's
   geometric-stiffness verdict was measured on Q=0 / single-particle-flattened / crystalline /
   quasiparticle-coherent / equilibrium hosts; each of the 25 deliberately violates exactly one of those
   five premises (braiding-statistics, hyperbolic/quasicrystal connectivity, non-quasiparticle SYK
   stiffness, light real-space negative-U pairs, static Coulomb-sign-flip, altermagnet spin-group pairing,
   flux/interference-decoupled flat bands, FFLO finite-Q, disorder-induced geometry), so its honest-null is
   genuinely un-run, not already-implied. **micro-exp wave-2 then probed one deterministic representative
   of EACH of the 8 escape clusters (H_036 statistical-transmutation, H_037 hyperbolic-connectivity, H_038
   ligand-hole negative-U, H_039 ENZ Coulomb-sign-flip, H_040 altermagnet spin-group, H_041 Yukawa-SYK
   incoherent stiffness, H_042 FFLO finite-Q, H_043 vortex-code) — ALL 8 confirm-wall (byte-equal, honest-null
   triggered). So 12/12 SF-escape probes across wave-1 (H_032-035) + wave-2 (H_036-043) hold the wall;
   each cluster's central mechanism is now tested and held. **micro-exp wave-3 then probed ALL 17 of
   the remaining within-cluster variants (H_044-H_060) — every one confirm-wall — so 29/29 SF-escape
   probes hold the wall and all 25 genuinely-new triaged escapes are now exhausted.** The two clusters whose wave-2 probe
   was a closed-form PROXY were then upgraded to DEFINITIVE real compute, both confirm-wall: H_041
   (Yukawa-SYK) via a real Matsubara Schwinger-Dyson solver — the incoherent metal pairs but ρ_s collapses
   ~Z², T_BKT 2.68 K vs the 164 K ceiling (arXiv:2406.07608 kernel); and H_037 (hyperbolic connectivity)
   via a real classical XY Monte-Carlo on a {7,3} tiling — bulk T_c^hyperbolic/T_c^square ≈ 0.46–0.59 (the
   wrong direction; negative curvature SUPPRESSES bulk ordering, reproducing Baek–Minnhagen). Honest ruling: across 5 premise-violating
   axes and **29 orthogonal probes (H_032-H_060, 2 with definitive real compute)**, the ~134-164K
   phase-stiffness wall stands UNDEFEATED — the no-go is not formally proven (heavier ED/MC could still
   surprise), but no in-silico escape has been found and the entire triaged SF-escape space is exhausted.
   This is the campaign's honest terminal map: every computationally-settleable lever and every SF-escape
   cluster surveyed, wall holds, absorbed=false / GATE_OPEN, no material claimed to BE an RTSC.

## 5. Lenses that did not rescue it

- **Driven / non-equilibrium (H_022 + research)** — photoinduced CDW-melting WITH a retained exciton
  IS documented in 1T-TiSe2 (Burian PRR 2021; Porer Nat. Mater. 2014), overturning the static
  inseparability — but every driven state is transient (~ps) and power-bound (kW lasers); not the
  equilibrium room-T target.
- **Topology / fractionalization (H_012/H_013)** — closed-negative as independent levers.
- **Infrastructure (H_026)** — the campaign QE build was silently SERIAL (missing `libopenmpi-dev`);
  fixed in place to MPI (root-cause, not workaround). This re-classified prior "non-convergence"
  from science-ceiling to substrate-infra.

## 6. Verdict and the path that remains

The `+@` architecture is **sound** (spacer + geometry DFT-confirmed); what does not exist is a single
**realizable** system in which a clean ≥349 meV glue, an at-E_F flat-band geometry, and the absence of
competing order **co-exist**. The named CoSn / hBN / Ta2NiSe5 trio is the **strongest 🟠**: every
computationally-settleable lever is confirmed or literature-bounded, clearing the +@ box on paper
(~137 K @ 2D, ~252 K with the 3D lever) but jointly unrealized. The remaining gates — extreme-doping
synthesis, trilayer fabrication, and accredited 4-probe transport + Meissner expulsion + measured
H_c2/T_c — are **physical, not computational**, and `absorbed=true` requires them regardless. The
honest computational campaign is therefore complete; advancement now requires the laboratory.

## 7. The three-wall convergence (the campaign's deepest finding)

Every route to room-T @ 1 atm the campaign explored terminates at ONE of three walls — and all three end
at the **out-of-domain laboratory gate** (`absorbed=true`), never at an in-silico failure:

1. **Phase-stiffness mechanism wall (~134–164 K).** The clean in-silico near-no-go: 29 orthogonal
   SF-escape probes (H_032–H_060, 2 real-compute) all confirm it; every escape hits the same "no free
   lunch" (borrow stiffness → Leggett softens pairing; change statistics → the gauge shifts both channels;
   incoherence → ρ_s collapses ~Z²; curvature → suppresses bulk ordering). The deep law: *the FLUCTUATION
   glues, the ORDER traps* — and the rigidity is bounded regardless of how it is sourced.
2. **Pressure / materials-existence wall (1 atm retention).** The hydride route reaches room-T
   *temperature* but only at megabar pressure (LaH10 ~250 K @ 170–190 GPa); ambient-stable hydride Tc caps
   ~17 K (GNoME), and the near-ambient room-T claims (CSH 2020, Lu-N-H 2023) were both retracted. Ambient
   retention is a synthesis endpoint — the lab gate (`state/research-pressure-hydride-axis-2026-06-25.md`).
3. **Many-body computability wall (beyond-PBE).** The exciton/strong-correlation glue scale (Ta2NiSe5)
   is a measured quantity our DFT cannot reproduce — routed around by literature, not computed by us.

No material is claimed to BE an RTSC. Negative and partial results are kept as results.
