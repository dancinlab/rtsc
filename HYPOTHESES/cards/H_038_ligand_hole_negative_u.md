# H_038 — Ligand-Hole Negative-U: the pair lives on oxygen, not the cation

- **id**: H_038
- **slug**: ligand-hole-negative-u
- **escape_class**: (c) different rigidity (real-space pair, not single-particle quasiparticle)
- **cluster**: light real-space pairs decouple eV binding from stiffness
- **status**: closed-negative (confirms-wall)
- **date**: 2026-06-25
- **is_green**: false
- **absorbed**: false
- **run**: `state/h_038_ligand-hole-negative-u_2026_06_25/run.py` (stdlib-only, deterministic, byte-reproducible)
- **violated_premise**: single-particle / quasiparticle-coherent (carrier = composite real-space boson)

## Hypothesis (frozen pre-register)

A BaBiO3-class **delocalized-ligand negative-U** gives a LIGHT real-space pair — a preformed *intersite bipolaron* on the symmetric O6 molecular orbital (bond disproportionation: the hole pair lives on the contracted oxygen octahedron, not on the Bi cation). NOT a flat-band quantum-metric pair (H_001/H_006), NOT a phonon-Holstein bipolaron (H_008), NOT a k-space Leggett object (H_032). Its stiffness is a Bose-gas response: D_s = hbar^2 n_pair/(2 m*), T_BKT=(pi/2)D_s. Frozen claim: as ligand bandwidth W grows, m* drops below ~3 m_e at fixed eV-scale |U_eff|, so the pair Bose gas condenses above the 134–164 K ceiling.

## Which freeze premise this violates
The **single-particle / quasiparticle-coherent** premise: the carrier is a composite real-space boson, not a BCS quasiparticle; the operative bound is hbar^2 n/(2m*), not D_s=4|U|nu(1-nu)<g>.

## Decisive probe
run.py parametrizes binding↔mass by the SINGLE coupling g=|U_eff|/W: E_bind(g)=|U|g/(1+g) (eV-scale only at strong g) and m*(g)/m0=1+a g^2, with a=2.0 ANCHORED (not tuned) to QMC m*~50 m0 at g~5 (arXiv:2507.17398). Generous inputs: U=0.75 eV, n=0.30 pairs/a^2, lightest channel.

## Falsifiers (PASS=not triggered)
1. honest_null_self_trapping_lock (DECISIVE) — TRIGGERED: lightest eV-bound mass 12.18 m_e > 10 m_e; eV binding does NOT decouple from stiffness.
2. tbkt_below_freeze_floor — TRIGGERED: best eV-bound T_BKT 90.38 K < 134 K.
3. ds_below_cuprate_scale — TRIGGERED: D_s 4.96 meV < 7.4 meV.
4. lit_superlight_below_ceiling — TRIGGERED: ~120 K (cond-mat/0701412) < 164 K.
5. tbkt_below_room_T — TRIGGERED: 90.38 K < 293 K.

## Honest limits
1. Toy closed-form (single-coupling parametrization), not lattice ED/QMC — direction robust, numbers order-of-magnitude. 2. Mass anchor is one QMC point; triangular vs FCC shifts prefactor but optimum still ~120 K. 3. n_pair generous (0.30/a^2); real bismuthates diluter → wall harder. 4. 2D-BKT form; 3D Alexandrov BEC formula gives same ~90–120 K. 5. BaBiO3 itself is an undoped insulator (doped Ba1-xKxBiO3 Tc≤34 K measured) — probe models idealized doped limit. 6. eV-bound floor E_bind≥0.50 eV; relaxing it admits marginal Cooper-like pairs that abandon the seed's own "decouple eV binding" premise.

## Verdict
confirms-wall. Real-space-pair escape is genuine in KIND (violates single-particle premise; superlight intersite bipolaron is real) but fails in MAGNITUDE: binding↔mass lock forces eV-bound m*≳12 m_e → T_BKT≈90 K, in the published 90–120 K superlight-bipolaron BEC band, below the 134–164 K ceiling. Decisive honest-null TRIGGERED. A valuable closed-negative. is_green=false; absorbed=false; no material claimed to BE an RTSC.

## References
arXiv:1807.07168; cond-mat/0606036; cond-mat/0701412; arXiv:2507.17398; arXiv:0907.4572; cond-mat/9809025