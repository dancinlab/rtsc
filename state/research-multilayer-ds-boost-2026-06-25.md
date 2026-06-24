# Research note — does a ~1.16× multilayer superfluid-weight (D_s) boost at small N hold?

- **date**: 2026-06-25
- **lane**: research-scout (READ-ONLY: web + arxiv + WebFetch; NO compute)
- **tests**: H_023 "demand-relaxation" limit **L1** — the SINGLE binding unknown of the
  campaign's strongest 🟢-path. Card claims f_mult ≥ 1.164 (~16% boost) is reached at the
  smallest N=2 on two bracketed scaling MODELS (optimistic √N Peotta–Törmä extensive-D_s;
  conservative N^0.25 Josephson-stack). The card honestly flags is_green=False because
  f_mult(N) is a MODEL, not a measured D_s. This note bounds the PRIOR on that model.
- **does NOT touch**: tool/rtsc_candidates.py, HYPOTHESES/cards/H_023*.

## Verdict (up front)

**🟠 CONDITIONAL — extensive-D_s is theoretically sound and a ~16–40% Tc/D_s boost at small
N is EMPIRICALLY REAL in several flat-band systems, but the per-layer boost is
system-dependent and is NEITHER monotone-in-N NOR established for the SPECIFIC host
(Ta2NiSe5).** Worse, the only DIRECT data on Ta2NiSe5's layer dependence runs the WRONG
direction: its excitonic order is *layer-confined* and its order-parameter Tc *decreases*
~9% toward the ultrathin limit. So +16% at N=2 is **PLAUSIBLE but UNVERIFIED for this host** —
*not* well-supported (would be 🟢), *not* impossible (would be 🔴). The H_023 L1 assumption
survives as a prior but does not harden. **The real DFT of the CoSn/hBN/Ta2NiSe5 N=2 stack
(H_019 follow-on) remains the decisive test.** The lead path stays 🟠-CONDITIONAL.

---

## Q1 — Flat-band D_s extensivity (Peotta–Törmä and the corrected bound)

**The bound is real but it is a RATIO, not an extensive-in-stacked-layers law.**

- **Peotta & Törmä, *Nat. Commun.* 6, 8944 (2015) / arXiv:1506.02815** establishes that a
  dispersionless flat band can still carry finite superfluid weight, with the lower bound
  **D_s ≥ |C|** (Chern number) and, more generally, D_s set by the Brillouin-zone integral of
  the **quantum metric**. Crucially the mean-field flat-band result is **D_s ∝ |U|** (linear in
  the pairing interaction) × the (minimal) quantum metric — *not* a free-running enhancement.
  (arXiv:1506.02815, confirmed id; abstract quote: "The integral over the Brillouin zone of the
  quantum metric gives the superfluid weight in a flat band, with the bound D_s ≥ |C|.")

- **Huhtinen, Herzog-Arbeitman, Chew, Bernevig & Törmä, *Phys. Rev. B* 106, 014518 (2022) /
  arXiv:2203.11133** ("Revisiting flat band superconductivity") CORRECTS the earlier mean-field
  derivation and is the load-bearing caveat here: for an isolated flat band the superfluid weight
  is proportional to the **minimal** quantum metric AND to the **ratio (number of degenerate flat
  bands) / (number of orbitals on which the flat-band states reside)**. That ratio is the trap:
  **naively stacking N copies of a host adds orbitals to the denominator as fast as flat bands to
  the numerator** unless the interlayer coupling is engineered to keep the per-layer flat band
  isolated and uniformly paired. So "extensive D_s ∝ √N" (the card's OPTIMISTIC model) is the
  *best case*, contingent on uniform pairing + flat-band isolation being preserved layer-to-layer;
  the generic case can be flat or DILUTING. (arXiv:2203.11133, confirmed id.)

**Realistic per-added-layer boost at N=2:** +16% is INSIDE the theoretically allowed window
(D_s can grow with the coupled-flat-band count) but is NOT guaranteed — it requires the stack to
preserve flat-band isolation and uniform pairing. Verdict on Q1: **plausible-optimistic, not
automatic.** The √N model is an upper bracket, not a measured law.

## Q2 — Measured multilayer Tc / D_s enhancement at small N (the empirical anchor)

Real systems DO show ~16–40% boosts at small N — but the sign and magnitude are
system-specific, and in the best-characterized "family" series the boost does NOT persist past
N=3:

| system | boost vs N | quantified |
|---|---|---|
| **Twisted bi→trilayer graphene (MATBG→MATTG)** | **N=2→3: +~40%** | T_c 1.7 K (bilayer) → 2.3–2.9 K (trilayer); "~40% higher than similarly prepared bilayer", stronger-coupling SC. Kim *et al.* Nature 606, 494 (2022); Park *et al.* / Hao *et al.* Science 371, 1133 (2021). **This is the strongest small-N boost datapoint and it is right at the card's ~16% scale (in fact larger).** |
| **Alternating-twist magic-angle family (Park, arXiv:2112.10760 / Nat. Mater. 21, 877 (2022))** | **N=2→5: flat then DOWN** | T_c,50% ≈ 3 K (N=2), ≈3 K (N=3), 2.76 K (N=4), 1.38 K (N=5). The boost does NOT compound — it saturates by trilayer and then declines. |
| **Cuprate Hg-series HgBa2Ca_{n-1}Cu_nO_{2n+2}** | **n=1→3: +~38% total**, then DOWN | T_c 97 K (n=1) → 128 K (n=2) → **134 K (n=3, ambient-pressure record)** → declines for n>3. Per-step boost n=1→2 ≈ +32%, n=2→3 ≈ +5%. Maximum at the TRILAYER; coupling of layers by quantum tunneling cited as the mechanism (npj Quantum Mater. 2025; Nat. Phys. 19, 1821 (2023), arXiv:2210.06348). **A real ~16–32% small-N boost — but capped at n=3.** |
| **FeSe thin films** | **monolayer BEST; multilayer WORSE** | Monolayer FeSe/SrTiO3 T_c ≈ 65 K vs bulk ≈ 8 K, but enhancement is interface-driven (interfacial e-ph + charge transfer), NOT a stacking effect — bilayer develops competing nematic/smectic order that SUPPRESSES SC. PNAS 116 (2019); npj Quantum Mater. 6 (2021). **Counter-example: more layers HURT.** |
| **Twisted trilayer superfluid stiffness (direct ρ_s measurement)** | quantum-geometric ρ_s confirmed | Banerjee, Hao, *et al.* arXiv:2406.13742 / Nature (2025): measured ρ_s of twisted multilayer graphene has a large **quantum-geometric** (flat-band) contribution beyond the conventional bound — DIRECT evidence that flat-band D_s is real and sizeable, supporting the *mechanism* the card invokes (but measured in graphene, not an EI). |

**Net Q2:** the +16%-at-N=2 magnitude is empirically REAL and even conservative compared to the
~40% bi→trilayer graphene jump and the +32% cuprate n=1→2 jump. BUT every quantified series shows
the boost **saturating or reversing by N≈3–4** (graphene family down past N=3; cuprates peak at
n=3; FeSe peaks at the MONOLAYER). The card only needs N=2, which is the most favorable case — so
the empirical prior is supportive at exactly N=2 and cautionary about extrapolating further.

## Q3 — Excitonic-insulator multilayers specifically (Ta2NiSe5) — the worrying datum

This is where the prior turns cautionary for THIS host.

- **Layer-Confined Excitonic Insulating Phase in Ultrathin Ta2NiSe5 (ACS Nano 10, 9966 (2016))**:
  the EI phase persists to the monolayer limit, BUT the out-of-plane correlation length of the EI
  order is **~one monolayer** — the order is "highly layer-confined." Interlayer coupling does NOT
  strongly bind the excitonic condensate across layers.
- Ultrathin Ta2NiSe5 shows **ΔT_c/T_c,bulk ≈ −9%** (transition temperature DECREASES toward the
  thin limit), explicitly contrasted in the literature with 1T-TiSe2 (which *increases* +30%).
  (substrate-tuning / atomically-thin Ta2NiSe5 studies, 2025: arXiv:2512.12439, arXiv:2512.09751 /
  Nat. Commun. 2025 — flagged as recent, ids confirmed via arxiv search but findings unverified by
  full-text read.)
- The Ta2NiSe5 **monolayer** is computed to be a *trivial narrow-gap semiconductor* with NO
  spontaneous exciton condensate (arXiv:2412.14582, first-principles) — the EI order is a
  bulk/few-layer collective effect, not monolayer-intrinsic.

**Implication:** the H_023 lever boosts the *superfluid weight D_s* of the paired state, which is a
DIFFERENT quantity from the *excitonic order-parameter T_c* that the layer-confinement data speaks
to — so the −9% datum is not a direct refutation. BUT it removes the comfortable assumption that
"stacking strengthens everything about Ta2NiSe5": the one EI-specific layer-dependence on record
runs the wrong way for the order parameter and shows the condensate is layer-confined. There is
**no measurement of D_s (or any SC-favorable property) vs N for Ta2NiSe5 or any sibling EI.** This
is a genuine gap, and it is exactly the gap the H_019 DFT must close.

## Q4 — Verdict on the f_mult ≥ 1.164-at-N=2 assumption

**🟠 CONDITIONAL.** Decomposing:

- **Is +16% at N=2 well-supported (🟢)?** No. It is *magnitude-plausible* — real systems hit
  +32% (cuprate n=1→2) and +40% (graphene bi→trilayer) at exactly this small-N scale — and the
  quantum-geometric D_s mechanism is directly measured (arXiv:2406.13742). But "well-supported"
  would require it for THIS host/coupling, which no measurement provides.
- **Is it impossible (🔴)?** No. The corrected flat-band bound (arXiv:2203.11133) permits D_s to
  grow with coupled-flat-band count, and multiple real systems realize boosts ≥16% at N=2.
- **Therefore 🟠:** extensive-D_s is theoretically sound; a ~16% boost at N=2 is *empirically in
  range*; but the per-layer boost is **system-dependent, non-monotone in N (saturates/reverses by
  N≈3), and unmeasured for Ta2NiSe5** — whose only EI layer-dependence datum is unfavorable
  (−9%, layer-confined condensate). The assumption is a **plausible but unverified prior**, not a
  hardened result.

**What the real boost-vs-N looks like (synthesis):** monotone-rising only over a SHORT window
(N=1→3), with a system-dependent peak at the bilayer or trilayer, then flat/declining. The card's
choice of the SMALLEST N=2 sits in the favorable part of every observed curve — which is the
right call — but the card's √N optimistic model would over-predict if extrapolated, and the
conservative N^0.25 model is the safer bracket. Per-step boosts of +5% to +40% are all on the
record at N=2→3; +16% is comfortably inside that spread but cannot be assigned to Ta2NiSe5 a priori.

**Decisive test (unchanged):** a real DFT of the fabricated CoSn/hBN/Ta2NiSe5 N=2 stack
(the converging H_019 follow-on) computing the actual multilayer D_s. This research lane bounds the
prior to "plausible, in-range, host-unverified"; only the DFT flips L1.

## Strongest citations (arXiv ids / DOIs confirmed)

1. **Peotta & Törmä, Nat. Commun. 6, 8944 (2015) — arXiv:1506.02815** (confirmed). Flat-band D_s
   ≥ |C|, D_s ∝ |U| × quantum metric. The card's optimistic-bracket source.
2. **Huhtinen, Herzog-Arbeitman, Chew, Bernevig & Törmä, PRB 106, 014518 (2022) —
   arXiv:2203.11133** (confirmed). Corrected mean-field: D_s ∝ minimal quantum metric ×
   (N_flatband/N_orbital) — the RATIO caveat that makes extensivity contingent, not automatic.
3. **Park et al., Nat. Mater. 21, 877 (2022) — arXiv:2112.10760** (confirmed). Magic-angle
   family T_c,50%: 3 K (N=2), 3 K (N=3), 2.76 K (N=4), 1.38 K (N=5) — boost saturates/reverses
   past trilayer.
4. **Cuprate Hg-series — Nat. Phys. 19, 1821 (2023) / arXiv:2210.06348** (confirmed) + npj
   Quantum Mater. (2025). T_c 97→128→134 K (n=1→2→3), peak at trilayer — a real +16–32%
   small-N boost, capped at n=3.
5. **Banerjee, Hao et al. — arXiv:2406.13742 / Nature (2025)** (confirmed). Direct measurement
   of a large quantum-geometric (flat-band) superfluid stiffness in twisted multilayer graphene —
   the mechanism the card invokes, measured.

Supporting (EI-specific, host-cautionary): ACS Nano 10, 9966 (2016) (layer-confined EI in ultrathin
Ta2NiSe5); arXiv:2412.14582 (trivial Ta2NiSe5 monolayer, first-principles); arXiv:2512.12439 /
arXiv:2512.09751 (atomically-thin Ta2NiSe5, ~−9% T_c, **flagged recent — abstract-level only, full
text unread**). Kim et al. Nature 606, 494 (2022) & Science 371, 1133 (2021) (MATTG +~40% vs MATBG).

## Honest limits of THIS note

- No full-text read of the paywalled Nature/Science/ACS articles — magnitudes are from abstracts,
  arxiv search snippets, and reputable secondary summaries; the **arXiv ids are id-confirmed**, the
  DOIs/journal page numbers are from search metadata and may carry minor citation errors.
- The D_s-vs-N for Ta2NiSe5 specifically is **unmeasured** — the −9% datum is the EI
  *order-parameter* T_c, a related-but-distinct quantity from the SC D_s the card boosts.
- This lane bounds a PRIOR; it does not measure the trio's stack. absorbed=false; GATE_OPEN.
