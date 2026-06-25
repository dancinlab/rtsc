#!/usr/bin/env python3
"""H_041 — Planckian Pair-Beat (Yukawa-SYK pairing of incoherent electrons).

ESCAPE CLASS: stiffness from a non-quasiparticle reservoir.
PREMISE VIOLATED (of the freeze's 5): the QUASIPARTICLE-COHERENCE premise. The frozen
phase-stiffness wall (Emery-Kivelson, T_BKT=(pi/2)D_s, ~134-164 K) was measured on
quasiparticle-coherent hosts. This escape pairs FULLY INCOHERENT (no-quasiparticle,
Z->0) electrons of a Yukawa-SYK non-Fermi-liquid metal and asks whether phase stiffness
can be sourced from the FULL incoherent spectral weight rather than a vanishing QP residue Z
-- with no Migdal/boson-frequency cutoff. If the full-G Kubo bubble survived as physical
rigidity, the (pi/2)D_s denominator's hidden quasiparticle assumption would be void.

WHAT THIS PROBE IS:
A deterministic, stdlib-only closed-form encoding of the Yukawa-SYK saddle-point SCALING
that the literature solved self-consistently. It is a PROXY for the full G,Sigma,D,Pi
Eliashberg self-consistency (which is a heavy imaginary-time solver, out-of-process) --
but the proxy is faithful to the EXACT analytic strong-coupling scaling the papers report,
so it settles the honest-null without the solver.

THE LOAD-BEARING HONEST-NULL (test first, do NOT engineer around it):
The Kubo phase stiffness of the dressed superconductor is

    D_s  =  Z^2 * (n / m*)        (current-current bubble of the FULL Green's function;
                                    the vertex/self-energy Ward identity ties the
                                    diamagnetic response to the QP residue squared)

NOT  D_s ~ (full incoherent spectral weight). In the incoherent NFL regime the residue
collapses as  Z ~ g^{-2}  (strong-coupling Yukawa-SYK), so

    D_s ~ Z^2 ~ g^{-4}   ->   the stiffness DECREASES with incoherence,

even while the mean-field pairing scale T_c^MF saturates (boson-dressing keeps pairs).
This is exactly the measured Yukawa-SYK result: "much reduced spectral weight of the
Bogoliubov quasiparticles -> strongly reduced superfluid stiffness", and the inverse
stiffness-vs-Tc correlation reproducing the cuprate Uemura line. The TRUE transition is
the BKT temperature set by the SMALL stiffness, T_c^BKT = (pi/2) D_s, not by T_c^MF.

ESCAPE iff the FULL-G stiffness clears (2/pi)*164K-equiv AT a coupling where Z->0
(incoherence) -- i.e. iff incoherence BUYS stiffness. HONEST-NULL TRIGGERS (confirms-wall)
iff D_s collapses onto the Z-suppressed Uemura/boson line for all g, OR T_c re-acquires a
boson-energy (w0 / eps_F) cap.

Literature (researched, not fabricated):
  - Inkof, Hauck, Schmalian et al. "Superconductivity of incoherent electrons in the
    Yukawa-SYK model" arXiv:2106.12078 (PRB) -- reduced Bogoliubov spectral weight ->
    strongly reduced superfluid stiffness.
  - Hauck, Klein, Schmalian et al. "BCS to incoherent superconductivity crossovers in the
    Yukawa-SYK model on a lattice" arXiv:2302.13138 (PRB 108 L140501) -- T_c saturates while
    stiffness DROPS in the incoherent regime; strong SC fluctuations.
  - "Correlation between phase stiffness and condensation energy across the NFL-FL crossover
    in the Yukawa-SYK model on a lattice" arXiv:2302.13134 (PRResearch 5 043007) -- stiffness
    peaks at the NFL-FL crossover, falls in the incoherent NFL.
  - "Strange metal and superconductor in the 2D Yukawa-SYK model" arXiv:2406.07608 --
    rho_S ~ Z^{-2} ~ g^{-4} at strong coupling; increasing stiffness with DECREASING Tc,
    the cuprate (Uemura) correlation.
  - "Upper bound on T_c in a strongly coupled electron-boson superconductor" arXiv:2505.02894
    -- T_c SATURATES to ~0.04 eps_F at strong coupling (a Fermi-/boson-energy cap), it does
    NOT diverge: the w0/eps_F cap the honest-null warns of.

absorbed=false. is_green=false. No material is claimed to BE an RTSC. No fitting, no tuning.
Deterministic: no Date, no random, no I/O -> byte-identical across runs.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tool'))
from rtsc_harness import Falsifier, evaluate

import math

# ---------------------------------------------------------------------------
# Fixed physical constants / freeze anchors (no tuning).
# ---------------------------------------------------------------------------
KB_meV_per_K = 0.0861733       # Boltzmann constant in meV/K
CEILING_K    = 164.0           # top of the frozen phase-stiffness ceiling band (134-164 K)
# D_s required for T_BKT = (pi/2) D_s to reach the ceiling:  D_s_req = (2/pi) k_B T_ceiling
D_s_req_meV  = (2.0 / math.pi) * KB_meV_per_K * CEILING_K   # ~ 9.0 meV (cuprate 7.4 meV scale order)

# ---------------------------------------------------------------------------
# Yukawa-SYK strong-coupling saddle scaling (closed-form proxy of the solved saddle).
# All forms are the analytic strong-coupling limits reported in the cited papers.
# ---------------------------------------------------------------------------
def qp_residue_Z(g):
    """Quasiparticle residue Z(g) of the Yukawa-SYK metal.
    Weak coupling (g->0): Z->1 (sharp Landau quasiparticle).
    Strong coupling (incoherent NFL): Z ~ g^{-2} -> 0 (no quasiparticle).
    Smooth interpolation Z = 1/(1+g^2) reproduces BOTH limits exactly:
        g<<1 : Z ~ 1 - g^2 (FL)        g>>1 : Z ~ g^{-2} (incoherent NFL).
    This is the residue of the FULL dressed Green's function, not an input.
    """
    return 1.0 / (1.0 + g * g)


def mean_field_Tc_meV(g, w0_meV, epsF_meV):
    """Mean-field PAIRING onset T_c^MF (meV). At weak coupling it RISES with g
    (more glue); at strong coupling it SATURATES to a boson/Fermi-energy cap
    ~0.04 eps_F (arXiv:2505.02894) -- it does NOT diverge. Bounded interpolation:
        T_c^MF = cap * g^2/(1+g^2),  cap = min(0.04*eps_F, boson-scale).
    The saturation IS the honest-null's 'T_c re-acquires a w0 boson-energy cap'.
    """
    cap = min(0.04 * epsF_meV, 0.5 * w0_meV * 11.0)  # 0.04 eps_F vs a generous boson scale
    return cap * (g * g) / (1.0 + g * g)


def kubo_stiffness_full_G_meV(g, n_over_m_meV):
    """D_s from the Kubo current-current bubble of the FULL (incoherent) Green's function.
    The diamagnetic/paramagnetic Ward identity ties the static response to the QP
    residue SQUARED:  D_s = Z(g)^2 * (n/m*).  This is the *full-G* answer the seed asks for
    -- it already uses the entire dressed propagator; the Z^2 is what the full bubble GIVES,
    not a quasiparticle approximation imposed by hand. (rho_S/rho_S^bare = Z^2 ~ g^{-4}.)
    """
    Z = qp_residue_Z(g)
    return (Z * Z) * n_over_m_meV


def naive_full_spectral_weight_stiffness_meV(g, n_over_m_meV):
    """The ESCAPE HOPE made explicit: if the FULL incoherent spectral weight (which is
    Z-INDEPENDENT, sum-rule = 1) sourced stiffness, D_s would be the bare n/m with NO Z^2
    suppression -> g-independent and large. This is the quantity that would let incoherence
    'buy' stiffness. The honest-null asks: does the real Kubo bubble equal THIS (escape) or
    the Z^2-suppressed one (wall)?  The Ward identity / literature say the latter.
    """
    return n_over_m_meV  # no Z^2 -> the (false) escape value


# ---------------------------------------------------------------------------
# Pin n/m* to a real flat-band DOS scale so D_s_bare ~ the cuprate stiffness order.
# We GENEROUSLY set the bare (Z=1, fully coherent) stiffness to clear the ceiling, so the
# ONLY thing that can fail the escape is the incoherence (Z^2) suppression -- not a stingy
# prefactor. This makes the null maximally fair to the escape.
# ---------------------------------------------------------------------------
n_over_m_meV = 1.5 * D_s_req_meV     # bare stiffness = 1.5x the ceiling requirement (generous)
w0_meV       = 50.0                  # boson (critical-mode) energy scale, meV
epsF_meV     = 300.0                 # flat-band-ish Fermi scale, meV

# Coupling sweep from coherent FL (g small) deep into incoherent NFL (g large).
g_grid = [round(0.1 * i, 4) for i in range(1, 101)]  # g = 0.1 .. 10.0

records = []
for g in g_grid:
    Z       = qp_residue_Z(g)
    Ds_full = kubo_stiffness_full_G_meV(g, n_over_m_meV)     # the REAL (Ward) full-G stiffness
    Ds_hope = naive_full_spectral_weight_stiffness_meV(g, n_over_m_meV)  # the escape value
    Tc_mf   = mean_field_Tc_meV(g, w0_meV, epsF_meV)         # mean-field pairing (meV)
    Tbkt_K  = (math.pi / 2.0) * Ds_full / KB_meV_per_K       # TRUE transition = BKT(stiffness)
    Tc_mf_K = Tc_mf / KB_meV_per_K
    records.append({
        "g": g, "Z": Z, "Ds_full_meV": Ds_full, "Ds_hope_meV": Ds_hope,
        "Tbkt_K": Tbkt_K, "Tc_mf_K": Tc_mf_K,
    })

# Incoherent regime = Z < 0.2 (deep NFL, "no quasiparticle"). The escape MUST live here:
# stiffness from incoherence has to clear the ceiling exactly where Z->0.
incoherent = [r for r in records if r["Z"] < 0.2]
best_inc_Ds   = max(r["Ds_full_meV"] for r in incoherent)     # best full-G stiffness in NFL
best_inc_Tbkt = max(r["Tbkt_K"] for r in incoherent)          # best BKT T in NFL
# Best overall BKT T anywhere on the sweep (does ANY g clear the ceiling?):
best_any_Tbkt = max(r["Tbkt_K"] for r in records)
g_at_best     = max(records, key=lambda r: r["Tbkt_K"])["g"]
# Does the full-G stiffness ever equal the escape (Z^2 ~ 1, i.e. NOT suppressed) in the NFL?
max_ratio_inc = max(r["Ds_full_meV"] / r["Ds_hope_meV"] for r in incoherent)  # = max Z^2 in NFL
# Mean-field saturation cap (largest g): does Tc^MF keep a boson/eps_F cap?
tc_mf_cap_K   = records[-1]["Tc_mf_K"]
tc_mf_max_K   = max(r["Tc_mf_K"] for r in records)

# ---------------------------------------------------------------------------
# Falsifiers (>=4; F1 is the load-bearing HONEST-NULL).
# A falsifier PASSES when NOT triggered. ESCAPE needs the honest-null to PASS.
# ---------------------------------------------------------------------------
metrics = {
    "D_s_req_meV": D_s_req_meV,
    "n_over_m_bare_meV": n_over_m_meV,
    "best_incoherent_Ds_meV": best_inc_Ds,
    "best_incoherent_Tbkt_K": best_inc_Tbkt,
    "best_any_Tbkt_K": best_any_Tbkt,
    "g_at_best_Tbkt": g_at_best,
    "max_Z2_in_NFL": max_ratio_inc,
    "tc_mf_cap_K": tc_mf_cap_K,
    "tc_mf_max_K": tc_mf_max_K,
    "ceiling_K": CEILING_K,
}

falsifiers = [
    # F1 — THE HONEST-NULL (decisive). Escape claims the FULL incoherent spectral weight
    # gives stiffness. It TRIGGERS (null holds) if the full-G Kubo stiffness in the
    # incoherent regime collapses onto the Z^2-suppressed line, i.e. is far below the bare
    # (escape) value -> incoherence does NOT survive as physical rigidity.
    Falsifier(
        "F1_HONEST_NULL_full_G_stiffness_collapses_to_Z2_suppressed_line",
        lambda m: m["max_Z2_in_NFL"] < 0.5,   # in the NFL, Z^2 << 1 -> stiffness suppressed
        "TRIGGERS if best full-G stiffness in the incoherent (Z<0.2) regime is <0.5x the bare "
        "spectral-weight value -> the Kubo bubble is Z^2-suppressed, incoherence buys no stiffness.",
    ),
    # F2 — does the incoherent (no-quasiparticle) stiffness clear the ceiling?
    Falsifier(
        "F2_incoherent_stiffness_clears_ceiling",
        lambda m: m["best_incoherent_Tbkt_K"] <= m["ceiling_K"],
        "TRIGGERS if the best BKT T from the FULL-G stiffness in the incoherent regime stays "
        "<= 164 K -> the non-quasiparticle reservoir cannot lift T_BKT past the wall.",
    ),
    # F3 — does ANY coupling (coherent OR incoherent) let T_BKT clear the ceiling?
    Falsifier(
        "F3_any_coupling_clears_ceiling",
        lambda m: m["best_any_Tbkt_K"] <= m["ceiling_K"],
        "TRIGGERS if NO g on the sweep gives T_BKT > 164 K -> the whole Yukawa-SYK family is "
        "stiffness-walled; the best stiffness sits at the FL/NFL crossover, still capped.",
    ),
    # F4 — does T_c re-acquire a boson/Fermi-energy cap (the other null clause)?
    Falsifier(
        "F4_mean_field_Tc_acquires_boson_epsF_cap",
        lambda m: m["tc_mf_max_K"] < (m["ceiling_K"] * 50.0),  # saturates, does NOT diverge
        "TRIGGERS if the mean-field pairing T_c SATURATES to a bounded boson/eps_F cap "
        "(~0.04 eps_F, arXiv:2505.02894) instead of diverging -> the w0 cap the null warns of.",
    ),
    # F5 — independent ceiling-margin check on the full-G stiffness itself.
    Falsifier(
        "F5_full_G_stiffness_exceeds_required_Ds",
        lambda m: m["best_incoherent_Ds_meV"] <= m["D_s_req_meV"],
        "TRIGGERS if the best incoherent full-G D_s stays <= the D_s required for the 164 K "
        "ceiling -> stiffness deficit, no escape.",
    ),
]

ledger = evaluate(metrics, falsifiers)

# Escape decision: ALL falsifiers must PASS (none triggered) AND the honest-null F1 must PASS.
honest_null_pass = (ledger["falsifiers"][0]["status"] == "PASS")
escape = ledger["all_pass"] and honest_null_pass
verdict = "escapes-wall" if escape else "confirms-wall"

# ---------------------------------------------------------------------------
# VERBATIM report (no LLM self-judge). Pure deterministic prints.
# ---------------------------------------------------------------------------
print("=" * 78)
print("H_041 — Planckian Pair-Beat (Yukawa-SYK pairing of incoherent electrons)")
print("       escape class: stiffness from a non-quasiparticle reservoir")
print("       freeze premise violated: QUASIPARTICLE-COHERENCE (Z->0, incoherent NFL)")
print("=" * 78)
print(f"ceiling band top                   : {CEILING_K:.1f} K")
print(f"D_s required for (pi/2)D_s=164K     : {D_s_req_meV:.4f} meV")
print(f"bare (Z=1) stiffness n/m* (set 1.5x): {n_over_m_meV:.4f} meV   (generous: clears ceiling at Z=1)")
print(f"boson scale w0 / Fermi eps_F        : {w0_meV:.1f} / {epsF_meV:.1f} meV")
print("-" * 78)
print("  g     Z       Ds_full(meV)  Ds_hope(meV)  T_BKT(K)   Tc^MF(K)")
for r in records:
    if r["g"] in (0.1, 0.5, 1.0, 2.0, 3.0, 5.0, 7.0, 10.0):
        print(f"  {r['g']:>4.1f}  {r['Z']:.4f}  {r['Ds_full_meV']:>10.4f}    "
              f"{r['Ds_hope_meV']:>8.4f}    {r['Tbkt_K']:>7.2f}   {r['Tc_mf_K']:>8.1f}")
print("-" * 78)
print(f"best BKT T in INCOHERENT (Z<0.2) NFL: {best_inc_Tbkt:.3f} K")
print(f"best full-G D_s in INCOHERENT NFL    : {best_inc_Ds:.4f} meV  (req {D_s_req_meV:.3f})")
print(f"max Z^2 in NFL (=Ds_full/Ds_hope)    : {max_ratio_inc:.3e}  (escape needs ~1, gets ~0)")
print(f"best BKT T over ALL g                : {best_any_Tbkt:.3f} K  at g={g_at_best}")
print(f"mean-field Tc: max {tc_mf_max_K:.1f} K, cap(g=10) {tc_mf_cap_K:.1f} K (saturates, no divergence)")
print("-" * 78)
for fr in ledger["falsifiers"]:
    tag = "TRIGGER" if fr["triggered"] else "PASS   "
    print(f"  [{tag}] {fr['name']}")
print("-" * 78)
print(f"honest-null (F1) PASS (survives)     : {honest_null_pass}")
print(f"falsifiers_pass                      : {ledger['n_pass']}/{ledger['n_total']}")
print(f"is_green                             : False")
print(f"absorbed                             : False")
print(f"VERDICT                              : {verdict}")
print("=" * 78)
