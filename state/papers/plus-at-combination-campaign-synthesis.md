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

No material is claimed to BE an RTSC. Negative and partial results are kept as results.
