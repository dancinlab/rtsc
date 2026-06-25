#!/usr/bin/env python3
"""H_048 — Overhauser-Locked Phase Ballast (nuclear-spin co-condensate).

CLUSTER: "stiffness sourced from a non-quasiparticle / non-electronic reservoir"
(within-cluster VARIANT of the confirmed H_041 Yukawa-SYK incoherent-D_s probe and
the multiband-donation H_032 manifold). This card tests the SPECIFIC twist: can a
coherent Overhauser / nuclear-spin field act as a SECOND phase-rigidity reservoir
adding in PARALLEL to the electronic superfluid weight?

FROZEN WALL (PR#40+; wave-1 H_032-035 + wave-2 H_036-043 all confirm-wall): the
Emery-Kivelson spin-fluctuation / phase-stiffness ambient ceiling band is ~134-164 K,
set by T_BKT = (pi/2) D_s with the relevant rigidity = the electronic Q=0 superfluid
weight. Every donation/borrow escape so far hits "no free lunch": donating stiffness
from another reservoir either (a) couples too weakly to count, or (b) softens the
pairing channel it borrows from (Leggett), or (c) the donor reservoir's own coherence
scale is too low to contribute physical rigidity at ambient T.

CLAIM (seed "Overhauser-Locked Phase Ballast"): treat the nuclear-spin bath as a
co-condensate whose own phase rigidity adds in PARALLEL to the electronic one,
    rho_s = rho_el + lambda^2 * rho_nuc ,                                    (*)
with lambda = A_hf / W the dimensionless electron-nucleus contact-hyperfine coupling
(contact-hyperfine energy A_hf over the electron bandwidth W) and rho_nuc the nuclear
spin-wave stiffness of a high-moment / high-abundance isotope (e.g. 51V, I=7/2). Then
    T_BKT = (pi/2) (rho_el + lambda^2 * rho_nuc) ,
and the parallel nuclear ballast lifts T_BKT above the electronic-only ceiling. A clean
isotope-monotonic falsifier the freeze never tested: Delta-T_BKT between a spin-I and a
spin-0 even-even isotope on the SAME lattice should be POSITIVE and sizeable.

HONEST NULL (the LOAD-BEARING falsifier — NOT engineered around). The parallel ballast
contributes nothing because BOTH multiplicative factors in lambda^2 * rho_nuc are
catastrophically small, by independent grounded physics:

  (N-a) HYPERFINE WEAKNESS. The contact-hyperfine energy in a metal is A_hf ~ 1e-7 ..
        1e-6 eV (Knight-shift / hyperfine fields are MHz..hundreds-of-MHz; 1 MHz ~
        4.1e-9 eV). The electron bandwidth is W ~ 1..10 eV. So
            lambda = A_hf / W ~ 1e-8 .. 1e-6  ->  lambda^2 ~ 1e-16 .. 1e-12.
        For lambda^2 * rho_nuc to MATCH rho_el, rho_nuc would have to EXCEED rho_el by
        ~1e12 .. 1e16. (Grounded: NMR Knight-shift / hyperfine-field magnitudes; Slichter,
        "Principles of Magnetic Resonance"; Knight-shift reviews.)

  (N-b) NUCLEAR ORDERING SCALE. The nuclear spin-wave stiffness rho_nuc is set by the
        nuclear spin ordering scale, which in real metals is nano-to-pico-Kelvin: the
        RKKY-mediated nuclear magnetic ordering temperature is T_nuc ~ 58 nK (Cu),
        ~560 pK (Ag), and at the very best ~milliKelvin in an interaction-enhanced 2D
        electron gas. So rho_nuc expressed as a temperature is ~1e-9 .. 1e-3 K, i.e.
        VASTLY BELOW rho_el ~ O(100 K). (Grounded: A.S. Oja & O.V. Lounasmaa, Rev. Mod.
        Phys. 69, 1 (1997), "Nuclear magnetic ordering in simple metals at positive and
        negative nanokelvin temperatures"; Simon-Loss arXiv:0709.0164, RKKY nuclear
        order pushed only to the mK range in an interacting 2DEG.)

  The two factors COMPOUND: rho_nuc/rho_el ~ (1e-3 K)/(100 K) ~ 1e-5 at the most
  generous (mK-enhanced 2DEG) limit, then multiplied by lambda^2 <= 1e-12. The parallel
  ballast term lambda^2*rho_nuc/rho_el is ~1e-17 or smaller — 16+ orders of magnitude too
  small to move T_BKT. The isotope contrast Delta-T_BKT is then ~zero (sub-femtoKelvin),
  not the sizeable positive shift the escape needs. -> confirm-wall.

NO-FREE-LUNCH (cluster pattern): the nuclear bath is "free" rigidity only if it couples
to the condensate; the coupling that would let it donate (lambda) is the SAME small
contact-hyperfine that makes its donation negligible, and the bath's own coherence
(rho_nuc) orders at nK. Borrowing from a genuinely non-electronic bath repeats the
H_032/H_041 lesson: the donor either decouples (small lambda) or has no rigidity of its
own at ambient T (nK ordering) — here, BOTH.

This probe encodes (*) as a SMALL deterministic computation: it sweeps the contact-
hyperfine coupling lambda across the realistic metal range and the nuclear stiffness
across the entire grounded band (from the bulk-metal nK ordering scale up to the most
generous interaction-enhanced mK 2DEG scale, and even an absurd "what-if" overshoot),
computes T_BKT from the two-stiffness formula, and computes the spin-I vs spin-0 isotope
contrast. Deterministic, stdlib-only (math), no Date/random -> byte-reproducible.

GROUNDED literature (cited, NOT fabricated):
  - A.S. Oja, O.V. Lounasmaa, "Nuclear magnetic ordering in simple metals at positive and
    negative nanokelvin temperatures", Rev. Mod. Phys. 69, 1 (1997).
        -> RKKY-mediated nuclear ordering at nK (Cu ~58 nK) / pK (Ag ~560 pK).
  - P. Simon, D. Loss, "Nuclear spin ferromagnetic phase transition in an interacting 2D
    electron system", arXiv:0709.0164, Phys. Rev. Lett. 98, 156401 (2007).
        -> electron-interaction-enhanced nuclear Curie T pushed only into the mK range.
  - C.P. Slichter, "Principles of Magnetic Resonance" (Springer) — Knight shift / contact
    hyperfine magnitudes (MHz..hundreds-of-MHz -> A_hf ~ 1e-7..1e-6 eV).
  - V. Jaccarino et al. / Knight-shift reviews on 51V hyperfine field (s-d cancellation;
    small net contact term) — high-I (I=7/2) high-abundance isotope, yet small A_hf.

SPECULATIVE vs GROUNDED: the parallel two-stiffness ansatz (*) is the seed's OWN (un-
grounded) construction; we adopt it CHARITABLY (most-favorable form for the escape). The
two suppression factors (N-a) A_hf/W ~ 1e-8..1e-6 and (N-b) nuclear ordering at nK..mK
are GROUNDED in the cited literature. The verdict does NOT hinge on any prefactor: even a
CHARITABLE absurd-overshoot scenario (nuclear stiffness 1e6x the mK enhanced limit AND
the top of the lambda range) is tested and still cannot move T_BKT measurably.
"""

import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tool'))
from rtsc_harness import Falsifier, evaluate, ROOM_T_K

# --- frozen campaign context (no tuning) -------------------------------------
CEILING_LO_K = 134.0      # spin-fluctuation / phase-stiffness ceiling band, low
CEILING_HI_K = 164.0      # ... high
CEILING_MID_K = 0.5 * (CEILING_LO_K + CEILING_HI_K)
KB = 8.617333262e-5       # eV/K

# Electronic Q=0 superfluid-weight scale of the SAME host the freeze measured, expressed
# as the (pi/2)*rho_el Kelvin scale. We anchor the electronic-only ceiling to the TOP of
# the frozen band (164 K) so the nuclear ballast only has to beat the host's OWN best
# number (a charitable anchor for the claim). rho_el (Kelvin) = (2/pi)*ceiling.
RHO_EL_K = (2.0 / math.pi) * CEILING_HI_K       # electronic phase stiffness as a Kelvin scale
# sanity: (pi/2)*RHO_EL_K == CEILING_HI_K

# --- grounded magnitudes (NOT tuned; from the cited literature) ---------------
# (N-a) contact-hyperfine coupling lambda = A_hf / W:
#   A_hf ~ 1e-7..1e-6 eV (MHz..hundreds-of-MHz hyperfine fields); W ~ 1..10 eV.
A_HF_LO_EV = 1.0e-7        # ~24 MHz contact-hyperfine (lower realistic)
A_HF_HI_EV = 1.0e-6        # ~240 MHz contact-hyperfine (generous upper, e.g. heavy-nucleus)
W_BAND_EV  = 2.0          # eV electron bandwidth (representative metal)
LAMBDA_LO = A_HF_LO_EV / W_BAND_EV     # ~5e-8
LAMBDA_HI = A_HF_HI_EV / W_BAND_EV     # ~5e-7

# (N-b) nuclear spin-wave stiffness rho_nuc as a Kelvin scale = the nuclear spin
# ORDERING temperature (RKKY-set). Grounded band:
RHO_NUC_BULK_K = 58.0e-9   # ~58 nK  (Cu nuclear Neel; Oja-Lounasmaa RMP 69, 1)
RHO_NUC_2DEG_K = 1.0e-3    # ~1 mK   (most generous: interaction-enhanced 2DEG; Simon-Loss)
# CHARITABLE absurd overshoot the escape would NEED to even be discussed:
RHO_NUC_ABSURD_K = 1.0e3   # 1000 K  (a fantasy nuclear stiffness 1e6x the enhanced limit)

# --- two-stiffness BKT formula -----------------------------------------------
def t_bkt_two_stiffness_K(rho_el_K, lam, rho_nuc_K):
    """T_BKT (K) from the parallel two-stiffness ansatz (*):
        rho_s = rho_el + lambda^2 * rho_nuc  (all stiffnesses as Kelvin scales)
        T_BKT = (pi/2) * rho_s
    Charitable to the escape: lambda^2*rho_nuc is ADDED, never subtracted."""
    rho_s_K = rho_el_K + (lam * lam) * rho_nuc_K
    return (math.pi / 2.0) * rho_s_K

def nuclear_ballast_term_K(lam, rho_nuc_K):
    """The PARALLEL nuclear contribution lambda^2 * rho_nuc as a Kelvin scale (the only
    thing that can move T_BKT above the electronic ceiling)."""
    return (lam * lam) * rho_nuc_K

# --- electronic-only ceiling (the wall) --------------------------------------
T_BKT_EL_ONLY_K = (math.pi / 2.0) * RHO_EL_K     # == CEILING_HI_K by construction

# --- sweep lambda x rho_nuc over the grounded band (+ absurd overshoot) -------
LAMBDAS = [
    ("realistic_lo", LAMBDA_LO),
    ("realistic_hi", LAMBDA_HI),
]
RHO_NUCS = [
    ("bulk_metal_nK", RHO_NUC_BULK_K),
    ("enhanced_2DEG_mK", RHO_NUC_2DEG_K),
    ("absurd_overshoot_1000K", RHO_NUC_ABSURD_K),
]

sweep = []          # (lam_name, rho_name, lam, rho_nuc_K, ballast_K, t_bkt_K, dT_vs_ceiling_K)
max_ballast_K = 0.0
max_t_bkt_K = 0.0
for lam_name, lam in LAMBDAS:
    for rho_name, rho_nuc_K in RHO_NUCS:
        ballast_K = nuclear_ballast_term_K(lam, rho_nuc_K)
        t_bkt = t_bkt_two_stiffness_K(RHO_EL_K, lam, rho_nuc_K)
        dT = t_bkt - T_BKT_EL_ONLY_K          # lift of T_BKT above the electronic ceiling
        sweep.append((lam_name, rho_name, lam, rho_nuc_K, ballast_K, t_bkt, dT))
        if ballast_K > max_ballast_K:
            max_ballast_K = ballast_K
        if t_bkt > max_t_bkt_K:
            max_t_bkt_K = t_bkt

# Best (largest) nuclear ballast over the REALISTIC band (exclude the absurd row). We rank
# by the BALLAST term (column 4), NOT by dT: with grounded magnitudes the lift dT underflows
# to exactly 0.0 in double precision for every realistic row (164 + 1e-16 == 164), so ranking
# by dT would be ill-defined. The ballast term itself is the honest, non-underflowed measure
# of the parallel nuclear contribution; dT is then computed from that same charitable best row.
realistic = [r for r in sweep if r[1] != "absurd_overshoot_1000K"]
best_real = max(realistic, key=lambda r: r[4])   # max BALLAST over realistic sweep
best_real_ballast_K = best_real[4]
best_real_dT_K = best_real[6]                     # double-precision lift (underflows to 0.0)

# The absurd-overshoot row (charitable upper bound): even THIS cannot move T_BKT?
absurd = max((r for r in sweep if r[1] == "absurd_overshoot_1000K"), key=lambda r: r[6])
absurd_dT_K = absurd[6]
absurd_ballast_K = absurd[4]

# --- isotope contrast: spin-I (51V, I=7/2) vs spin-0 even-even isotope --------
# A spin-0 nucleus has rho_nuc = 0 (no nuclear moment -> no ballast). The isotope
# contrast Delta-T_BKT = T_BKT(spin-I) - T_BKT(spin-0) = (pi/2)*lambda^2*rho_nuc, i.e.
# exactly the ballast term. Evaluate at the most generous realistic point.
best_lam = LAMBDA_HI
best_rho_nuc_realistic_K = RHO_NUC_2DEG_K       # most generous realistic nuclear stiffness
isotope_contrast_K = (math.pi / 2.0) * nuclear_ballast_term_K(best_lam, best_rho_nuc_realistic_K)
# what the escape NEEDS: a sizeable positive shift, say >= 1 K (to matter against a 134 K wall)
ISOTOPE_CONTRAST_NEEDED_K = 1.0

# How many orders of magnitude short is the realistic ballast vs the electronic stiffness?
ballast_to_el_ratio = best_real_ballast_K / RHO_EL_K if RHO_EL_K > 0 else 0.0

metrics = {
    "rho_el_K": RHO_EL_K,
    "t_bkt_el_only_K": T_BKT_EL_ONLY_K,
    "A_hf_lo_eV": A_HF_LO_EV,
    "A_hf_hi_eV": A_HF_HI_EV,
    "W_band_eV": W_BAND_EV,
    "lambda_lo": LAMBDA_LO,
    "lambda_hi": LAMBDA_HI,
    "lambda_sq_hi": LAMBDA_HI * LAMBDA_HI,
    "rho_nuc_bulk_K": RHO_NUC_BULK_K,
    "rho_nuc_2deg_K": RHO_NUC_2DEG_K,
    "rho_nuc_absurd_K": RHO_NUC_ABSURD_K,
    "best_real_ballast_K": best_real_ballast_K,
    "best_real_dT_K": best_real_dT_K,
    "absurd_ballast_K": absurd_ballast_K,
    "absurd_dT_K": absurd_dT_K,
    "max_t_bkt_K": max_t_bkt_K,
    "isotope_contrast_K": isotope_contrast_K,
    "isotope_contrast_needed_K": ISOTOPE_CONTRAST_NEEDED_K,
    "ballast_to_el_ratio": ballast_to_el_ratio,
    "ceiling_lo_K": CEILING_LO_K,
    "ceiling_hi_K": CEILING_HI_K,
    "ceiling_mid_K": CEILING_MID_K,
    "room_t_K": ROOM_T_K,
}

# === falsifiers (PASS = NOT triggered) =======================================
# A predicate returns True when the CLAIM is REFUTED (falsifier TRIGGERED -> FAIL).
falsifiers = [
    # F1 — HONEST NULL (DECISIVE, load-bearing): the realistic nuclear ballast cannot lift
    #      T_BKT to the room-T target. The escape REQUIRES T_BKT(with ballast) to reach 293 K;
    #      the two-stiffness formula with grounded lambda^2 and rho_nuc lifts it by <<1 K.
    Falsifier(
        "honest_null_ballast_cannot_reach_room_T",
        lambda m: m["t_bkt_el_only_K"] + m["best_real_dT_K"] < m["room_t_K"],
        "DECISIVE/HONEST-NULL: with grounded lambda=A_hf/W (~1e-8..1e-6) and rho_nuc at the "
        "nuclear ordering scale (nK..mK), the parallel ballast lambda^2*rho_nuc lifts T_BKT by "
        "<<1 K, nowhere near 293 K. Grounded: Oja-Lounasmaa RMP 69,1 (nK ordering); Simon-Loss "
        "arXiv:0709.0164 (mK enhanced limit); Slichter (A_hf MHz-scale).",
    ),
    # F2 — HONEST NULL prong (decisive): the ballast term is parametrically negligible vs the
    #      electronic stiffness — many orders of magnitude too small to matter at all.
    Falsifier(
        "honest_null_ballast_negligible_vs_electronic",
        lambda m: m["best_real_ballast_K"] < 1e-3 * m["rho_el_K"],
        "DECISIVE/HONEST-NULL: realistic lambda^2*rho_nuc / rho_el ~ 1e-17 or smaller (compounded "
        "lambda^2<=1e-12 and rho_nuc/rho_el<=1e-5), so the parallel nuclear channel adds <0.1%% of "
        "the electronic stiffness — it cannot move T_BKT.",
    ),
    # F3 — the isotope-monotonic falsifier the escape itself proposes FAILS: the spin-I vs
    #      spin-0 contrast Delta-T_BKT = (pi/2)*lambda^2*rho_nuc is sub-femtoKelvin, not the
    #      sizeable (>= 1 K) positive shift the escape needs.
    Falsifier(
        "isotope_contrast_unmeasurable",
        lambda m: m["isotope_contrast_K"] < m["isotope_contrast_needed_K"],
        "The escape's own isotope-monotonic falsifier fails: Delta-T_BKT(spin-I vs spin-0) "
        "= (pi/2)lambda^2 rho_nuc is sub-femtoKelvin, not a sizeable positive shift — no "
        "measurable nuclear-ballast signature on T_BKT.",
    ),
    # F4 — CHARITABLE absurd-overshoot guard: even a fantasy nuclear stiffness 1e6x the enhanced
    #      mK limit (1000 K) STILL cannot lift T_BKT to room-T, because lambda^2 alone kills it.
    #      This shows the verdict does NOT hinge on the nuclear-stiffness prefactor.
    Falsifier(
        "absurd_overshoot_still_below_room_T",
        lambda m: m["t_bkt_el_only_K"] + m["absurd_dT_K"] < m["room_t_K"],
        "Charitable absurd-overshoot guard: even rho_nuc = 1000 K (a fantasy 1e6x the enhanced "
        "2DEG limit) lifts T_BKT by < (pi/2)*lambda^2*1000 K ~ sub-mK because lambda^2<=1e-12 "
        "alone caps the ballast. The hyperfine weakness (N-a) is decisive independent of rho_nuc.",
    ),
    # F5 — net escape unsatisfiable: no realistic (lambda, rho_nuc) gives a T_BKT clearing even
    #      the LOW edge of the ceiling beyond the electronic-only value.
    Falsifier(
        "joint_escape_unsatisfiable",
        lambda m: not (m["best_real_dT_K"] > (m["ceiling_lo_K"] - m["t_bkt_el_only_K"]) and
                       m["best_real_dT_K"] > 1.0),
        "Joint escape unsatisfiable: no realistic (lambda, rho_nuc) lifts T_BKT by >1 K; the "
        "relevant rigidity remains the electronic Q=0 superfluid weight. Nuclear ballast adds "
        "nothing measurable.",
    ),
    # F6 — sanity guard: the two-stiffness formula reproduces the electronic ceiling exactly when
    #      the nuclear ballast is zeroed (no hidden tuning of rho_el).
    Falsifier(
        "electronic_anchor_consistency_guard",
        lambda m: abs(m["t_bkt_el_only_K"] - m["ceiling_hi_K"]) > 1e-6,
        "Guard: (pi/2)*rho_el reproduces the 164 K electronic ceiling exactly (rho_el anchored, "
        "not tuned); if this failed the anchor would be inconsistent and the comparison invalid.",
    ),
]

ledger = evaluate(metrics, falsifiers)

# "escapes-wall" requires the load-bearing honest-null (F1) AND F2 to PASS (NOT triggered)
# with a real margin AND the joint-escape falsifier (F5) to PASS. Otherwise confirm-wall.
n_hn1 = ledger["falsifiers"][0]
n_hn2 = ledger["falsifiers"][1]
joint = ledger["falsifiers"][4]
hn1_passes = (n_hn1["status"] == "PASS")
hn2_passes = (n_hn2["status"] == "PASS")
joint_passes = (joint["status"] == "PASS")
escapes = hn1_passes and hn2_passes and joint_passes

verdict = "escapes-wall" if escapes else "confirms-wall"
n_pass = ledger["n_pass"]
n_total = ledger["n_total"]

print("=" * 78)
print("H_048  Overhauser-Locked Phase Ballast — nuclear-spin co-condensate (parallel D_s)")
print("=" * 78)
print("cluster: non-electronic-reservoir stiffness donation (variant of H_041/H_032)")
print(f"electronic-only rho_el (Kelvin scale)    = {RHO_EL_K:.3f} K")
print(f"electronic-only T_BKT = (pi/2)rho_el     = {T_BKT_EL_ONLY_K:.2f} K  (== ceiling top)")
print(f"contact-hyperfine A_hf range             = {A_HF_LO_EV:.1e}..{A_HF_HI_EV:.1e} eV")
print(f"electron bandwidth W                     = {W_BAND_EV:.2f} eV")
print(f"lambda = A_hf/W range                    = {LAMBDA_LO:.2e}..{LAMBDA_HI:.2e}")
print(f"  -> lambda^2 (hi)                       = {LAMBDA_HI*LAMBDA_HI:.2e}")
print(f"nuclear ordering rho_nuc band            = {RHO_NUC_BULK_K:.1e} K (nK bulk).."
      f"{RHO_NUC_2DEG_K:.1e} K (mK 2DEG)")
print("-" * 78)
print("  lambda          rho_nuc            ballast=lam^2*rho_nuc(K)   T_BKT(K)   dT_vs_ceiling(K)")
for (ln, rn, lam, rho, ball, tb, dT) in sweep:
    print(f"  {ln:13s} {rn:22s} {ball:.3e}        {tb:10.4f}   {dT:.3e}")
print("-" * 78)
print(f"best realistic nuclear ballast           = {best_real_ballast_K:.3e} K")
print(f"best realistic T_BKT lift dT             = {best_real_dT_K:.3e} K")
print(f"ballast / rho_el                         = {ballast_to_el_ratio:.3e}")
print(f"isotope contrast Delta-T_BKT (I vs 0)    = {isotope_contrast_K:.3e} K  "
      f"(need >= {ISOTOPE_CONTRAST_NEEDED_K:.1f} K)")
print(f"absurd-overshoot (rho_nuc=1000K) T_BKT   = {(T_BKT_EL_ONLY_K+absurd_dT_K):.4f} K  "
      f"(lift {absurd_dT_K:.3e} K)")
print(f"campaign ceiling                         = {CEILING_LO_K:.0f}-{CEILING_HI_K:.0f} K  "
      f"(room-T target {ROOM_T_K:.0f} K)")
print("-" * 78)
for r in ledger["falsifiers"]:
    print(f"  [{r['status']}] {r['name']}")
print("-" * 78)
print(f"HONEST-NULL F1 (ballast cant reach room-T) status = {n_hn1['status']}")
print(f"HONEST-NULL F2 (ballast negligible vs el)         = {n_hn2['status']}")
print(f"joint-escape falsifier status                     = {joint['status']}")
print(f"falsifiers_pass                                   = {n_pass}/{n_total}")
print(f"is_green                                           = False")
print(f"absorbed                                           = false")
print(f"VERDICT: {verdict}")
print("=" * 78)
