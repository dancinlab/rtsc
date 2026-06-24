# Research note — A NEW LENS: does NON-EQUILIBRIUM / DRIVEN suppression re-open the 1T-TiSe2 🟢-path the STATIC research closed?

**Date:** 2026-06-25
**Lane:** L-driven-research (driven/non-equilibrium CDW suppression, research)
**Status:** READ-ONLY literature survey — `sidecar research arxiv` + WebSearch + WebFetch. No rental, no fabrication, no compute.
**Honesty (commons):** every numeric value carries a source (arXiv id / DOI / journal). absorbed=false / GATE_OPEN.
Energies/timescales are published material properties, NOT a claim any material IS an RTSC. NO tune-to-green: if the
driven state is real but only transient/powered, that is 🟠 — a transient powered lab coordinate is NOT the campaign's
equilibrium room-T conductor target, and is not spun into a 🟢.

---

## The new lens (the decision this note serves)

The prior note `state/research-tise2-cdw-suppression-2026-06-25.md` CLOSED the 🟢-path (🔴 for that route) on a
**STATIC-equilibrium** premise: in 1T-TiSe2 the ~400 meV electronic mode and the finite-q (2×2×2) CDW are *two faces of
one excitonic order parameter* (Kogar/Abbamonte, Science 358, 1314 (2017), arXiv:1611.04217 — the mode softens to ZERO
at T_CDW), so every **equilibrium** suppression route (Cu screens the exciton away → 4 K phonon SC; pressure softens the
CDW phonon; monolayer/gating ENHANCES the CDW) destroys the very mode it was meant to preserve.

The user's lens re-opens it: **the WAY you pass current/energy changes the result.** Does NON-EQUILIBRIUM driving —
ultrafast photoexcitation, current-drive, Floquet engineering — suppress the 1T-TiSe2 CDW on a sub-ps timescale *WHILE
retaining* the high-energy excitonic correlation (something static equilibrium cannot do), and/or directly induce an
SC-favorable state? Equilibrium thermodynamics forbids the separation; non-equilibrium dynamics is not bound by it.

---

## Q1 — Photoinduced/driven CDW suppression in 1T-TiSe2 specifically: is the exciton retained while the lattice CDW melts?

**YES — there is a documented transient fluence window where the structural CDW (PLD) is suppressed while the electronic/
excitonic orbital order remains mostly intact.** This is the decisive new result the static survey could not see, because
it is purely a non-equilibrium effect.

- **Burian, Porer, Mardegan, … *Structurally assisted melting of excitonic correlations in 1T-TiSe2*, Phys. Rev.
  Research 3, 013128 (2021) (arXiv:2006.13702).** Femtosecond X-ray + 12-fs optical study. Key finding for the lens:
  **there is a fluence regime in which the periodic lattice deformation (PLD) is strongly suppressed but the CDW-related
  Se 4p orbital order remains MOSTLY INTACT.** Complete CDW melting proceeds 4–5× FASTER than a purely electronic
  charge-screening process would allow → the melt is "structurally assisted." Read in reverse, the same finding gives
  exactly the new-lens regime: **a transient driven state where the lattice CDW is knocked down but the high-energy
  electronic (excitonic/orbital) correlation survives.** [VERIFIED — peer-reviewed.] This is the inverse of the static
  Cu/pressure routes, which kill the electronic mode first.

- **Porer, Leierseder, Ménard, … *Non-thermal separation of electronic and structural orders in a persisting charge
  density wave*, Nat. Mater. 13, 857 (2014) / arXiv:1604.05627.** With 12-fs optical pulses the two CDW components
  respond DISTINCTLY: **"even when the excitonic order of the CDW is quenched, the PLD can persist in a coherently
  excited state."** Direct proof that the electronic and structural orders are *non-thermally separable* in 1T-TiSe2 —
  the equilibrium inseparability (Science 2017) does NOT hold out of equilibrium. (This one demonstrates the OTHER
  separation — lattice persists, exciton quenched — establishing the general decoupling that Burian then exploits in the
  exciton-retaining direction.) [VERIFIED — peer-reviewed.]

- **Duan, Xia, Huang, … *Ultrafast Switching from the Charge Density Wave Phase to a Metastable Metallic State in
  1T-TiSe2*, arXiv:2306.00311 (2023).** High-resolution trARPES: photoexcitation drives an **ultrafast electronic phase
  transition within 100 fs**, producing a **metastable METALLIC state**; its lifetime is **prolonged to picoseconds at
  the highest pump fluence.** So driving does reach a transient metal (the SC-favorable precondition — kill the gap/CDW,
  get a metal). [VERIFIED — arXiv preprint.]

- **Suo, Liu, Wang, … *Photoinduced charge density wave transition like a puppet on a string* (1T-TiSe2),
  arXiv:2112.12289 (2021).** ab-initio non-adiabatic MD: photoexcitation modulates Ti–Se bond charge → a
  fluence-dependent interatomic-repulsive force that mechanically suppresses the PLD/CDW. A hybrid-but-lattice-driven
  melt mechanism; supports that fluence is the control knob and the suppression is dynamical, not thermal. [VERIFIED —
  arXiv/theory.]

- Supporting: **Heinrich, Chang, Zayko, … Rossnagel, Ropers**, XUV transient-absorption at the Ti M2,3 edge
  (arXiv:2211.03562, 2022) and **Fragkos et al.**, trXUV momentum microscopy (arXiv:2507.12430, 2025) both confirm
  ultrafast, electronically-driven CDW dynamics and high-T CDW fluctuations — the CDW order parameter responds to light
  on the fs scale and is electronically tunable.

**Q1 answer: documented.** A transient, fluence-tuned non-equilibrium regime in 1T-TiSe2 melts the structural CDW while
the high-energy electronic/excitonic correlation is retained (Burian, PRR 3, 013128 (2021)), and a metastable METALLIC
(gap-collapsed, SC-favorable) state is reached within 100 fs and lives for picoseconds (Duan, arXiv:2306.00311). This is
PRECISELY what static equilibrium suppression could not deliver — the static graveyard does not apply to the driven axis.

---

## Q2 — Driven/light-induced SC precedent: does the mechanism exist at all (and is it contested)?

Driven/non-equilibrium SC is a **real, reproducible phenomenon in some systems, but its SC interpretation is contested in
others** — it is not a settled turnkey effect.

- **K3C60 — the strongest case.** Mitrano, Cantaluppi, … Cavalleri, *Possible light-induced superconductivity in K3C60 at
  high temperature*, **Nature 530, 461 (2016)** (arXiv:1505.04529): mid-IR resonant excitation of intramolecular
  vibrations induces transient SC-like optical conductivity at temperatures FAR above the equilibrium **Tc ≈ 20 K** (up
  to ~5× Tc, ~100 K). Initially **ps lifetime** (drive-limited). **Budden, … Cavalleri, *Evidence for metastable
  photo-induced superconductivity in K3C60*, Nat. Phys. 17, 611 (2021)** (arXiv:2002.12835): with tunable 1 ps–1 ns mid-IR
  drive, the SC-like state becomes **metastable with lifetime > 10 ns** (≥4 orders of magnitude longer) — vanishing
  resistance measured electrically at ~5× equilibrium Tc. **Resonant enhancement** confirmed (Nat. Phys. 19, 1821 (2023),
  s41567-023-02235-9). This is the most reproducible driven-SC case. [VERIFIED.]

- **Cuprates — contested.** YBCO/LSCO driven above Tc by mid-IR (Hu/Kaiser/Cavalleri era) was long cited as
  light-induced SC by melting competing stripe order. BUT **Zhang et al., *Light-Induced Melting of Competing Stripe
  Orders without Introducing Superconductivity in La2-xBaxCuO4*, arXiv:2306.07869 (2023)** finds the opposite:
  **"transient three-dimensional superconductivity cannot be induced by melting the competing stripe orders"** — in-plane
  probes show ENHANCED quasiparticle scattering, incompatible with SC condensation; the THz "Josephson-like" response is
  reinterpreted. The authors state plainly that **"photoinduced superconductivity remains a topic of controversy."**
  [VERIFIED — peer-reviewed counter-evidence.]

- **Hidden/metastable non-equilibrium states are real (TaS2).** Stojchevska, … Mihailovic, *Ultrafast switching to a
  stable hidden topologically protected quantum state* in 1T-TaS2, **Science 344, 177 (2014)** (arXiv:1401.6786): a single
  fs pulse switches 1T-TaS2 into a **non-volatile hidden metallic state** (electrically switchable, cryogenic flash
  memory; Burri et al. arXiv:2411.04830, 2024). Proves driven states CAN be metastable/non-volatile — but at cryogenic
  temperatures. [VERIFIED.]

**Q2 answer: the mechanism exists** (K3C60 is real and reproducible, now metastable to >10 ns), but it is **not
universal and is actively contested** (LBCO/cuprate driven-SC is disputed). No driven-SC case is at room temperature, and
none is an equilibrium (un-powered) state.

---

## Q3 — The honest ledger (M3 BORROW): the power / lifetime bill

This is where the lens must pay its debt. Driven SC is non-equilibrium: **it must be continuously (or repetitively)
powered, and outside the drive the state decays.**

| coordinate | best driven number (cited) | the campaign target |
|---|---|---|
| Operating temperature | K3C60 SC-like to ~100 K (~5× Tc 20 K); TiSe2 metal transient | **293 K equilibrium** |
| State lifetime | TiSe2 metastable metal: **~ps** (arXiv:2306.00311); K3C60: ps → **>10 ns** under sustained drive (Budden 2021) | **∞ (a material you plug in)** |
| Power source | continuous/repetitive mid-IR or optical pumping; fluences ~0.1–few mJ/cm² (TiSe2 CDW-melt threshold ~0.12 mJ/cm²); large laser/THz infrastructure | **none — an equilibrium conductor** |
| Reproducibility | K3C60 robust; cuprate SC **contested** (arXiv:2306.07869) | settled |
| In TiSe2 specifically | exciton-retaining CDW-melt window is **fs–ps, transient** (Burian PRR 3,013128); SC itself NOT yet observed in driven TiSe2 — only a metallic precondition | a sustained SC |

**Honest verdict on the bill:** even in the best case (K3C60, the metastable >10 ns state) the SC exists ONLY while
energy is being pumped in and decays when the drive stops — it is a **continuously-powered, transient lab state, not a
sustained room-T conductor you can plug in.** For 1T-TiSe2 the situation is one step earlier still: the exciton-retaining
CDW-melt is a **picosecond** window, and **driven SC has NOT been demonstrated in TiSe2 at all** — only the SC-favorable
metallic precondition. The "material you plug in" target (an equilibrium 293 K conductor) is categorically NOT met by any
driven route surveyed. The power/lifetime bill is: **kW-class pulsed laser/THz infrastructure, ps–ns lifetime, cryogenic
or transient operating point** — orders of magnitude away from a turnkey room-T conductor.

---

## Q4 — Verdict: 🟠 — the driven lens RE-OPENS the path as a LAB coordinate, not as a turnkey conductor

> **🟠 DRIVEN-REOPEN (transient / power-bound).** The new lens is genuinely productive and OVERTURNS the static premise:
> in 1T-TiSe2 the equilibrium inseparability of the ~400 meV exciton and the finite-q CDW does NOT hold out of
> equilibrium. There is a **documented transient fluence window where the structural CDW (PLD) is suppressed while the
> high-energy electronic/excitonic orbital order is RETAINED** (Burian et al., PRR 3, 013128 (2021), arXiv:2006.13702 —
> the inverse-favorable regime), the orders are proven **non-thermally separable** (Porer, Nat. Mater. 13, 857 (2014),
> arXiv:1604.05627), and photoexcitation reaches a **metastable METALLIC, SC-favorable state within 100 fs** (Duan,
> arXiv:2306.00311). Driven SC is a real mechanism in at least one clean system — **K3C60**, now metastable to **>10 ns**
> (Budden, Nat. Phys. 17, 611 (2021), arXiv:2002.12835) — though it remains **contested in cuprates** (Zhang,
> arXiv:2306.07869: stripe-melt WITHOUT SC). **BUT** the honest power/lifetime bill is decisive: every driven state is
> **continuously powered and transient (ps–ns)**, none is at room temperature, and **driven SC has not been demonstrated
> in TiSe2 itself** (only the metallic precondition). A transient, kW-laser-powered, ps-lived state is **NOT** the
> campaign's equilibrium 293 K @ 1 atm conductor — it is a non-equilibrium LAB coordinate. So the lens does NOT restore a
> 🟢: it converts the static 🔴 into a **🟠 — the driven path is real and worth a coordinate, but it cannot, as surveyed,
> yield a sustained turnkey room-T conductor.** absorbed=false / GATE_OPEN.

**Why NOT 🟢:** the deliverable target is a real material you plug in (equilibrium, un-powered, sustained). No driven route
delivers that; all are transient + powered. Spinning "K3C60 SC-like at 100 K for 10 ns under a laser" into a room-T
success-material would be tune-to-green dishonesty.

**Why NOT 🔴:** the static survey's core blocker (exciton ⇔ CDW inseparable) is FALSE out of equilibrium — Burian/Porer
prove the orders separate, and a transient exciton-retaining metallic state is real. The lens is a legitimate re-opening;
the path is alive as a non-equilibrium research coordinate, just not as a turnkey conductor.

**Promote toward 🟢 only if** a future result shows (i) driven/Floquet SC observed *in 1T-TiSe2 or a sibling* (not just a
metallic precondition), AND (ii) a route to a *self-sustaining / steady-state* (e.g. CW-driven or genuinely non-volatile
hidden-state) SC near room T with a tractable power budget — i.e. the lifetime axis pushed from ns to ∞ and the
temperature axis from ~100 K to 293 K. Both are currently open.

---

### Load-bearing citations (markdown)
- [Burian et al., Phys. Rev. Research 3, 013128 (2021) — Structurally assisted melting of excitonic correlations in 1T-TiSe2 (exciton-RETAINING CDW-melt window)](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.3.013128) ([arXiv:2006.13702](https://arxiv.org/abs/2006.13702))
- [Porer et al., Nat. Mater. 13, 857 (2014) — Non-thermal separation of electronic and structural orders in a persisting CDW](https://www.nature.com/articles/nmat4042) ([arXiv:1604.05627](https://arxiv.org/abs/1604.05627))
- [Duan et al., arXiv:2306.00311 (2023) — Ultrafast switching to a metastable metallic state in 1T-TiSe2 (100 fs; ps lifetime)](https://arxiv.org/abs/2306.00311)
- [Mitrano et al., Nature 530, 461 (2016) — Possible light-induced superconductivity in K3C60](https://www.nature.com/articles/nature16522) ([arXiv:1505.04529](https://arxiv.org/abs/1505.04529))
- [Budden et al., Nat. Phys. 17, 611 (2021) — Evidence for metastable photo-induced superconductivity in K3C60 (>10 ns)](https://www.nature.com/articles/s41567-020-01148-1) ([arXiv:2002.12835](https://arxiv.org/abs/2002.12835))
- [Zhang et al., arXiv:2306.07869 (2023) — Light-induced melting of stripe order WITHOUT superconductivity in La2-xBaxCuO4 (driven-SC contested)](https://arxiv.org/abs/2306.07869)
- [Suo et al., arXiv:2112.12289 (2021) — Photoinduced CDW transition "puppet on a string" in 1T-TiSe2](https://arxiv.org/abs/2112.12289)
- [Stojchevska et al., Science 344, 177 (2014) — Ultrafast switching to a stable hidden state in 1T-TaS2](https://www.science.org/doi/10.1126/science.1241591) ([arXiv:1401.6786](https://arxiv.org/abs/1401.6786))
- [Kogar, Abbamonte et al., Science 358, 1314 (2017) — exciton condensation soft mode in TiSe2 (the equilibrium inseparability the lens overturns)](https://www.science.org/doi/10.1126/science.aam6432) ([arXiv:1611.04217](https://arxiv.org/abs/1611.04217))
