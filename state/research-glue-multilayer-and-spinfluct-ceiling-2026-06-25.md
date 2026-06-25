---
id: GLUEMULTI-SFCEIL
slug: glue-multilayer-and-spinfluct-ceiling
domain: rtsc
status: pre_registered
pre_register_frozen: true
frozen_at: 2026-06-25
kind: research
gates: H_031 (clean spin-fluctuation dual multilayer) — L1 (spin-fluct ambient ceiling) + L3 (f_glue user lever)
---

# Research note — does stacking the GLUE layers boost coupling (the user's f_glue lever), and what is the REAL spin-fluctuation ambient-Tc ceiling?

**Date:** 2026-06-25
**Lane:** glue-multilayer + spin-fluctuation-ceiling research (research-first / 실측전 research)
**Status:** READ-ONLY cited literature survey — no compute, no rental (web + WebFetch; `sidecar research arxiv` available but web sufficed).
**Rule served:** the campaign's "실측전 research" gate on H_031's NEW user lever (f_glue) + its binding honest limit (L1).
**Honesty posture (commons honesty / falsifier-first):** every Tc / energy / ratio below is real and cited; web-confirmed values are [VERIFIED WebSearch]; textbook/established are [LIT-ESTABLISHED]. No material is claimed to BE an RTSC. absorbed=false / GATE_OPEN throughout. A sober "the dual-multilayer crosses only the MODEL threshold, not the real ambient ceiling" is a valid result — this is NOT tune-to-green.

---

## The two questions (from H_031)

1. **Does stacking GLUE layers actually boost the electron-boson coupling / Tc, or saturate? (the user lever f_glue, H_031 limit L3.)** Is the realistic boost at small N (N=2,3) ≥1.0003 (the threshold H_031 needs)? ≥1.05?
2. **What is the REAL spin-fluctuation ambient-Tc ceiling? (the binding cap, H_031 limit L1.)** The harness BKT coordinate maps 300 meV → 252 K, but measured spin-fluctuation SC caps at ~134 K ambient / ~164 K under pressure. Is 252 K (let alone 293 K) physically reachable, or is the real ambient ceiling ~134-164 K? What sets it? Is the harness over-reading by ~2×?

---

## VERDICT (one paragraph — read this first)

**The user's f_glue lever is REAL and LARGE at small N — but it is the SAME lever as the cuprate
multilayer Tc rise, and it carries the SAME hard saturation wall, and that wall sits at ~134 K, NOT
293 K.** The measured analog of "stack the spin-fluctuation glue layers" is exactly the Hg-cuprate
homologous series: stacking pairing/glue planes raises Tc **94 → 128 → 134 K for N = 1 → 2 → 3**
[VERIFIED WebSearch], i.e. a measured boost of **+36% at N=2 and +43% at N=3** over the single layer —
*enormously* more than the f_glue ≥ 1.0003 (0.03%) that H_031 needs, and well past the f_glue ≥ 1.05
(5%) line too. **So on the narrow question "is the small-N boost ≥ the threshold?" the answer is YES,
by two orders of magnitude.** BUT this is a trap for the dual-multilayer claim, because the very same
literature that supplies the boost ALSO supplies its ceiling: the multilayer Tc rise **SATURATES at
N=3 and then DECLINES** (Hg-1234 ~127 K, Hg-1245 ~111 K, falling to ~80 K at n=7) [VERIFIED WebSearch],
killed by the inner/outer-plane **charge imbalance** (doping ratio R = 1.14 / 1.49 / 1.64 for n = 3/4/5)
[VERIFIED WebSearch]. And the peak it saturates AT is **~134 K ambient / ~164 K under pressure** — the
three-decade cuprate record — with a theoretical Tc(J)-from-132-compounds ceiling of only **~155 K**
[VERIFIED WebSearch]. The ceiling is set by **phase stiffness (Emery–Kivelson), the pseudogap, and
competing charge order — NOT by the magnon energy** [VERIFIED WebSearch]. **Therefore the harness BKT
coordinate (300 meV → 252 K) over-reads the real spin-fluctuation ambient ceiling by ~1.5–1.9× (252 K
vs the measured 134–164 K), and H_031's 292.9 K is a MODEL coordinate, not a real one.** The honest
reading: the dual multilayer (f_geom × f_glue) crosses the *harness's* 293 K threshold because BOTH
factors are model knobs that the harness lets run freely — but in the real material BOTH lever and
ceiling are bounded by the same physics: **the f_glue multilayer boost is real and large at N=2-3, the
spin-fluctuation ambient ceiling it saturates at is ~134-164 K, and that ceiling — not the magnon
energy and not 293 K — is the honest binding wall.** absorbed=false / GATE_OPEN unchanged.

---

## Q1 — Does stacking GLUE layers boost the coupling / Tc, or saturate? (f_glue, the user lever, L3)

**The measured analog is the cuprate multilayer homologous series.** Stacking CuO2 (= pairing/glue)
planes within one unit cell IS the physical realization of "stack the spin-fluctuation-glue layers."
The data is unambiguous and quantitative.

### Q1a — the small-N boost (N=1→2→3) is REAL and LARGE

Hg-12(n-1)n homologous series, optimally-doped, ambient pressure [VERIFIED WebSearch]:

| n (CuO2 layers) | Material | Tc (ambient) | Boost vs n=1 | f_glue analog |
|---|---|---|---|---|
| 1 | Hg-1201 | **94–97 K** | — | 1.00 |
| 2 | Hg-1212 | **128 K** | **+36%** | **≈1.36** |
| 3 | Hg-1223 | **134–135 K** | **+43%** | **≈1.43** (PEAK) |
| 4 | Hg-1234 | ~127 K | +35% | ≈1.35 (declining) |
| 5 | Hg-1245 | ~111 K | +18% | ≈1.18 (declining) |
| 7 | Hg-12(6)7 | ~80 K | −15% | ≈0.85 (well below n=1) |

**Answer to the threshold question:** the realistic f_glue boost at N=2 is **≈1.36 (+36%)** and at N=3
is **≈1.43 (+43%)** — *vastly* above the **f_glue ≥ 1.0003 (0.03%)** that H_031 needs to cross 293 K,
and far above the **f_glue ≥ 1.05 (5%)** line. So **the user's lever clears its own threshold with
enormous margin** at small N. The interlayer mechanism is measured: the denser charge fluid of the
outer plane enhances quasiparticle weight on the strongly-correlated inner plane, and the stronger
pairing of the inner plane is shared with the outer plane — both pairing strength AND phase coherence
are optimized when interfacing planes with distinct hole concentrations [VERIFIED WebSearch,
PRL p4c3-t34b / arXiv:2506.01448 / 2506.08763]. This is a genuine cooperative *coupling/coherence*
boost, not mere additive layer counting.

### Q1b — but it SATURATES at N=3 and DECLINES — the same wall H_031's L3 anticipated

This is the load-bearing caveat. The multilayer boost is **not monotonic**: Tc **increases with n,
saturates at n=3, then DECREASES for n>3** [VERIFIED WebSearch, multiple]. The mechanism is the
inner/outer-plane **charge imbalance**: inner planes are farther from the charge-reservoir layer, so
they stay underdoped while outer planes are more strongly doped; the imbalance grows with n
(doping-ratio R = **1.14 (n=3) / 1.49 (n=4) / 1.64 (n=5)** [VERIFIED WebSearch, arXiv:cond-mat/0511249])
and suppresses Tc for n≥4. So:

- **For a stacked spin-fluctuation glue the realistic boost is ≥1.05 (indeed ≈1.3-1.4) at N=2-3 — clears
  H_031's threshold — BUT it is NOT a free knob that keeps climbing.** It is a *cooperative-coupling*
  boost that peaks at trilayer and then reverses. H_031's limit L3 ("saturation at N=1–3 likely") is
  CONFIRMED: saturation at N=3 is measured, and the user's lever cannot be pushed past trilayer to buy
  more Tc — beyond N=3 it COSTS Tc.
- **The deeper point: the boost and the ceiling are the SAME object.** The +43% trilayer boost lands
  the cuprate AT its ~134 K record — the boost is *how cuprates reach their ceiling*, not a way past it.
  You cannot use f_geom to reach 252 K and THEN add f_glue's +43% on top, because the +43% is already
  spent getting any spin-fluctuation system to its ~134 K ceiling. Treating f_geom and f_glue as
  *independent multiplicative* knobs (Tc = stacked_tc × f_geom × f_glue, H_031 "Why") is the model's
  optimism: in the real material the glue-multilayer boost is not orthogonal to the binding ceiling — it
  is the mechanism that defines that ceiling.

**Q1 verdict:** the user lever is **REAL and ≥1.05 (≈1.36-1.43) at N=2-3 — it clears the 0.03% AND the
5% thresholds** — but it **SATURATES hard at N=3 (then declines)** via charge imbalance, and it is the
same lever that pins any spin-fluctuation glue at its ~134 K ceiling, so it is NOT a free multiplicative
factor on top of the ceiling.

---

## Q2 — The REAL spin-fluctuation ambient-Tc ceiling (L1, the binding limit)

**The measured ambient ceiling is ~134 K; the theoretical spin-fluctuation ceiling is ~155 K; it is set
by phase stiffness / pseudogap / competing order, NOT by magnon energy.**

### Q2a — the measured numbers

- **Ambient record: Hg-1223 Tc = 133–135 K** [VERIFIED WebSearch] — the three-decade ambient
  spin-fluctuation-SC record, unbeaten at 1 atm.
- **Under pressure: ~164–166 K @ ~31 GPa** [VERIFIED WebSearch]. (Pressure-quench ambient up to 151 K,
  PNAS 2025 — still <164 K, still <<293 K.)
- **Theoretical Tc(J) ceiling: ~155 K.** Because Tc ∝ J (in-plane exchange) in cuprates, the
  Tc(J) correlation across 132 compounds gives a *maximal attainable* Tc of **~155 K (J = 6.15)**;
  "it is not possible to significantly increase Tc in superconductors based on the CuO2 plane"
  [VERIFIED WebSearch]. An "intrinsic temperature scale of order 100 K" / record ~135 K is argued to
  be the inherent potential of the CuO2-plane mechanism [VERIFIED WebSearch, arXiv:cond-mat/0604026].

### Q2b — what sets the ceiling (it is NOT the magnon energy)

The harness BKT map assumes the boson energy (300 meV) sets Tc (300 meV → 252 K). **The real ceiling is
set by other factors, all of which the harness omits:**

1. **Phase stiffness (Emery–Kivelson, Nature 374, 434 (1995)).** In 2D, strong-coupling SCs with small
   superfluid density have Tc set by the **phase stiffness, not the pairing magnitude** — the phase is
   soft enough that fluctuations destroy SC *before* the pairing gap closes [VERIFIED WebSearch]. This
   is the dominant cap and it is *independent of how energetic the glue boson is*. A 300 meV magnon does
   not buy 252 K if the superfluid stiffness can only sustain ~134 K of phase coherence.
2. **Pseudogap.** The large gap persists well above Tc as a pseudogap — strong pairing energy in the
   inner layer that does NOT convert to higher Tc because phase coherence (not pairing) is the
   bottleneck [VERIFIED WebSearch, npj Quantum Materials s41535-025-00735-w].
3. **Competing charge order / AF order.** Charge order and the pseudogap compete with SC at optimal
   doping; in the trilayer, AF + charge order coexist deep in the SC phase [VERIFIED WebSearch,
   PMC8943046]. (This is the same "the fluctuation glues, the ORDER traps" law from the clean-glue note —
   the static side of the very spin order that supplies the glue competes with SC.)
4. **Charge imbalance (the multilayer-specific cap from Q1b)** — caps the multilayer route at trilayer.

**None of these is the magnon energy.** So raising the boson to 300 meV (or even 500 meV bimagnon) does
NOT lift the ceiling, because the ceiling is a phase-stiffness/competing-order ceiling, not an
energy-scale ceiling.

### Q2c — is the harness over-reading?

**Yes, by ~1.5–1.9×.** The harness BKT coordinate: 300 meV → **252 K**. The real ambient ceiling:
**134 K** (252/134 ≈ **1.88×** over-read), or **164 K** under 31 GPa pressure (252/164 ≈ **1.54×**
over-read even granting pressure the campaign cannot apply at 1 atm). The harness reads the *boson
energy* as if it sets Tc; the real material is stiffness/order-limited at roughly *half* the BKT value.
**252 K is NOT physically reachable for a spin-fluctuation glue at ambient — the measured ceiling is
~134-164 K — and 293 K is even further out of reach.**

**Q2 verdict:** the REAL spin-fluctuation ambient ceiling is **~134 K (record) / ~155 K (theoretical
Tc(J) max) / ~164 K (under 31 GPa pressure)** — set by **phase stiffness + pseudogap + competing
order**, not magnon energy. The harness BKT coordinate (252 K) **over-reads it by ~1.5-1.9×**.

---

## Synthesis — does H_031's dual-multilayer REALLY cross room-T?

**No — it crosses only the MODEL threshold, not the real ambient ceiling.** Walking the H_031 numbers
against the literature:

- H_031: `stacked_Tc 3D (no multilayer) = 251.6 K` — this is already the BKT over-read (Q2c): the real
  spin-fluctuation value at this 300 meV boson is **~134-164 K**, not 252 K. The 251.6 K starting point
  is ~1.5-1.9× too high before any multilayer lever is applied.
- H_031: `+ geometry N=2 (f_geom=1.164) = 292.9 K` — f_geom is the H_024 flat-band D_s model (L2,
  separately model-bound); applied to an already-inflated 252 K base.
- H_031: `glue-multilayer f_glue ≥ 1.0003 crosses 293 K; f_glue=1.05 → 307.6 K` — the f_glue lever is
  REAL and ≥1.05 at N=2-3 (Q1a, the user's lever genuinely clears its threshold) — BUT (i) it is the
  SAME cuprate multilayer boost that *defines* the ~134 K ceiling rather than adding on top of it (Q1b),
  and (ii) it saturates at N=3.

So the dual multilayer crosses 293 K **only because the harness multiplies two model knobs (f_geom ×
f_glue) onto a BKT base that is itself ~1.5-1.9× over the real spin-fluctuation ceiling.** Strip the
BKT over-read and the same architecture lands at roughly **(134-164 K) × f_geom × f_glue**, where
f_glue is *already spent* reaching the 134-164 K — i.e. **the honest coordinate is ~134-200 K, not 293 K.**

### The honest binding wall

**The spin-fluctuation ambient-Tc ceiling, ~134-164 K, set by phase stiffness + pseudogap + competing
charge/AF order (NOT magnon energy).** H_031's 292.9 K is **BKT-optimistic**: the dual-multilayer
crosses the harness's 293 K threshold but NOT the real ambient ceiling, which is ~half that. The user's
f_glue lever is real and large (it clears its 0.03% and 5% thresholds with margin), but it is the same
trilayer cooperative-coupling boost that *gets cuprates to 134 K in the first place* — it does not
stack on top of the ceiling, and it saturates at N=3. is_green=False; absorbed=false / GATE_OPEN; no
material is claimed to BE an RTSC.

---

## Citations (load-bearing; web-confirmed this session unless marked LIT-ESTABLISHED)

- **Hg homologous series Tc(n):** Hg-1201 **94-97 K** / Hg-1212 **128 K** / Hg-1223 **134-135 K**
  (peak at n=3) / Hg-1234 **~127 K** / Hg-1245 **~111 K** / down to ~80 K at n=7; under pressure
  118/154/166 K. [VERIFIED WebSearch — multiple, incl. npj QM s41535-025-00735-w; ScienceDirect
  S0038109825003965 (uniaxial-pressure-derivative model); arXiv:cond-mat/0604026.]
- **Tc peaks at n=3, decreases for n>3 via inner/outer charge imbalance:** doping ratio R =
  **1.14 (n=3) / 1.49 (n=4) / 1.64 (n=5)**; charge imbalance suppresses Tc for n≥4.
  [VERIFIED WebSearch — arXiv:cond-mat/0511249 "Charge Imbalance Effects on Interlayer Hopping…";
  PMC8943046 (trilayer AF + charge order).]
- **Trilayer interlayer cooperative-coupling mechanism (boost is coupling+coherence, not additive):**
  enhanced OP gap; OP charge fluid raises IP quasiparticle weight, IP pairing shared with OP; both
  pairing and phase coherence optimized at distinct-doping interface. [VERIFIED WebSearch —
  PRL 10.1103/p4c3-t34b; arXiv:2506.01448; arXiv:2506.08763.]
- **Ambient record 134 K / 164 K @ 31 GPa / 151 K pressure-quench (PNAS 2025):** [VERIFIED WebSearch —
  carried + reconfirmed from clean-glue note.]
- **Tc ∝ J; theoretical max ~155 K (J=6.15) from 132 compounds; intrinsic scale ~100-135 K; "cannot
  significantly increase Tc on the CuO2 plane":** [VERIFIED WebSearch — Tc(J) correlation;
  arXiv:cond-mat/0604026 "What Tc can teach about superconductivity"; arXiv:2010.00572 "Universal
  limiting transition temperature".]
- **Phase stiffness limits Tc (Emery–Kivelson):** Nature **374, 434 (1995)** "Importance of phase
  fluctuations in superconductors with small superfluid density"; Tc set by phase stiffness, not pairing
  magnitude, in low-superfluid-density 2D SCs. [VERIFIED WebSearch.]
- **Heuristic bounds on Tc (Fermi-T, superfluid stiffness, Debye freq) — none a fundamental bound, but
  all cap real cuprates well below room-T:** npj Quantum Materials **s41535-022-00491-1** "Heuristic
  bounds on superconductivity and how to exceed them." [VERIFIED WebSearch.]
- **Pseudogap / large gap above Tc / competing charge order at optimal doping:** [VERIFIED WebSearch —
  npj QM s41535-025-00735-w; Pseudogap (Wikipedia/Science 1248221); PMC8943046.]
- **Moriya–Ueda spin-fluctuation theory / SCR / AF-QCP pairing:** Moriya & Ueda, "Antiferromagnetic
  spin fluctuation and superconductivity." [LIT-ESTABLISHED / VERIFIED WebSearch.]
- Carried from `state/research-clean-glue-candidates-2026-06-25.md`: spin-fluctuation single-magnon
  ~300 meV / bimagnon ~500 meV; TbMn6Sn6/Au interface SC 3.6 K (the only real +@ proximity datum);
  review arXiv:1611.07813; Nat. Phys. 18, 1356 (2022) (~half doped-Hubbard SC = spin-fluctuation glue).

**Honesty note.** No fabricated citations. All Tc / J / R / energy numbers are as reported by the cited
works via web/WebFetch (not re-derived). The "f_glue is real-and-large-but-saturates-at-N=3-and-is-the-
same-lever-as-the-ceiling" and "BKT over-reads the ambient ceiling by ~1.5-1.9×" readings are the honest
conclusions, not a tune-to-green. The user's lever genuinely clears its numeric threshold (≥1.05 at
N=2-3) — that is reported truthfully — but the binding wall is the spin-fluctuation ambient ceiling
(~134-164 K), which the harness over-reads. absorbed=false / GATE_OPEN throughout; no material is
claimed to BE an RTSC.
