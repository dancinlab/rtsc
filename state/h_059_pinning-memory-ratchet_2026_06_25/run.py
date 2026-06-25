#!/usr/bin/env python3
"""H_059 — Pinning-Memory Ratchet (Glassy-Phason Non-Equilibrium Stiffness Ballast).

Within-cluster variant of the spin-fluctuation / phase-stiffness ambient ceiling
cluster (T_BKT = (pi/2) rho_s; Emery-Kivelson). Sibling, on the "borrow stiffness
from a non-electronic reservoir" axis, of H_032 (electronic multiband donation),
H_048 (Overhauser nuclear ballast), H_041 (Yukawa-SYK incoherent D_s). Distinct
twist: the donor is a PINNED STRUCTURAL GLASS (overdamped-phason / TLS bath),
added to the phase action as a memory kernel, with NO Leggett mode between the SC
condensate and the glass (so H_032's quantum-metric / Leggett cap does not apply).

Seed escape mechanism (state/sf_seed_full_triage_2026_06_25/triage.md, line ~112):

  Phase action
      S = (1/2) integral d^2r dtau [ rho_s^el (grad theta)^2
                                     + chi_glass(omega) (dtau theta)^2 ]
  with a pinned-phason memory kernel (overdamped-TLS / glassy-phason bath,
  Jiang-Zaccone-Setty-Baggioli, PRB 108, 054203 (2023) = arXiv:2305.05407)
      chi_glass(omega) = sum_i w_i * Gamma_i / (omega^2 + Gamma_i^2).
  ESCAPE CLAIM: the pinned glass donates a finite phase rigidity that lifts the
  effective stiffness rho_s^eff above (2/pi) k_B * 164 K, so
      T_BKT = (pi/2) rho_s^eff  beats the frozen 134-164 K wall.

DECISIVE HONEST-NULL (confirm-wall; load-bearing — NOT engineered around):
  The glass kernel chi_glass multiplies (dtau theta)^2 — it is a TEMPORAL
  (compressibility / phase-inertia) term, NOT the spatial gradient term
  rho_s (grad theta)^2 that the Nelson-Kosterlitz criterion turns into T_BKT.
  Two independent prongs both kill the escape:

   (N1) FREQUENCY-MISMATCH (the seed's own stated null). chi_glass is a sum of
        Lorentzians peaked at the (small) phason damping/pinning scales Gamma_i.
        The SC phase winding that unbinds a vortex lives at the Josephson plasma
        frequency omega_J >> Gamma_i. An adiabatic, slow bath cannot follow the
        fast phase winding, so the kernel the vortex actually feels is
        chi_glass(omega -> omega_J) ~ sum_i w_i Gamma_i / omega_J^2  -> 0.
        Only the zero-frequency (static) limit chi_glass(0) = sum_i w_i / Gamma_i
        is large, but that is the COMPRESSIBILITY, which does not enter T_BKT.

   (N2) WRONG-CHANNEL (structural, even stronger). Even chi_glass(0) feeds the
        (dtau theta)^2 term. Nelson-Kosterlitz: T_BKT = (pi/2) * J with J the
        SPATIAL stiffness only (the temporal term renormalizes the plasma mode /
        compressibility, not the vortex-unbinding stiffness). So d T_BKT /
        d chi_glass = 0 identically, for ANY w_i, Gamma_i. rho_s^eff = rho_s^el.

  No free lunch in the SAME way as every prior null: a reservoir that is rigid
  enough to add static weight (Gamma -> 0) is, by that very slowness, frequency-
  decoupled from the vortex scale AND living in the wrong (temporal) channel.

Real-physics anchor: the Jiang-Zaccone-Setty-Baggioli paper computes a
phason-PAIRING channel (Eliashberg lambda) and finds a NON-MONOTONIC T_c with a
maximum at the underdamped->overdamped crossover — i.e. the glass can dress a
PAIRING vertex, but that is the binding/glue axis (already on the H_032/H_041
manifold), NOT the BKT STIFFNESS axis this card tests. We test the stiffness
claim, which is the seed's actual lever, and which the static/temporal kernel
cannot satisfy.

Deterministic, stdlib-only (math). No Date, no RNG, no fitting. Byte-reproducible.
PASS = falsifier NOT triggered (rtsc_harness convention). escapes-wall ONLY if the
two decisive honest-nulls (N1 frequency-mismatch, N2 wrong-channel) both PASS
(are NOT triggered) with a real margin.
"""

import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tool"))
from rtsc_harness import Falsifier, evaluate, ROOM_T_K

# ---------------------------------------------------------------------------
# Constants / host (all explicit; no fitting).
# ---------------------------------------------------------------------------
KB_MEV_PER_K = 0.0861733          # k_B in meV/K
HBAR_MEV_PS = 0.6582119569        # hbar in meV*ps  (so omega[meV] = hbar*omega[1/ps])
ROOM_K = ROOM_T_K                 # 293.0 K target
CEILING_TOP_K = 164.0             # charitable TOP of the frozen 134-164 K band
CEILING_BOT_K = 134.0

# Electronic (real, glue-limited) spatial stiffness of the host, expressed as a
# rigidity in Kelvin. CHARITY: anchor (pi/2) rho_s^el to the TOP of the frozen
# band (164 K) — the most favorable choice for the escape (real flat-band D_s is
# 1-8 K). This is the only thing T_BKT is allowed to depend on.
RIGIDITY_EL_K = CEILING_TOP_K                 # (pi/2) rho_s^el, charitable anchor
RHO_S_EL_MEV = RIGIDITY_EL_K * KB_MEV_PER_K   # rho_s^el as an energy scale (meV)

# Josephson plasma frequency: the scale at which the SC phase winds when a vortex
# unbinds. Conservative/low estimate. For 2D SC films omega_J ~ tens of meV; we
# take a deliberately SMALL omega_J = 10 meV (favorable to the slow bath — a
# larger omega_J only makes the frequency mismatch worse for the escape).
OMEGA_J_MEV = 10.0

# ---------------------------------------------------------------------------
# Glassy-phason memory kernel (overdamped-TLS bath, arXiv:2305.05407).
#   chi_glass(omega) = sum_i w_i * Gamma_i / (omega^2 + Gamma_i^2)
# Each TLS/phason mode i: spectral weight w_i (meV, sets a stiffness scale) and a
# damping/pinning rate Gamma_i (meV). A *glass* is SLOW: Gamma_i << omega_J.
# We build a bath whose STATIC weight is HUGE (deliberately stacked in the
# escape's favor) to show that even a maximally-rigid static glass cannot help.
# ---------------------------------------------------------------------------

def chi_glass(omega_meV, modes):
    """Overdamped-phason memory kernel chi_glass(omega) in meV.
    modes = list of (w_i [meV^2 dimension as weight*Gamma], Gamma_i [meV]).
    Lorentzian sum: each term = w_i * Gamma_i / (omega^2 + Gamma_i^2)."""
    total = 0.0
    for w_i, gamma_i in modes:
        total += w_i * gamma_i / (omega_meV * omega_meV + gamma_i * gamma_i)
    return total


# Build a deliberately STRONG glass bath: large weights, slow rates (glass).
# Gamma_i chosen << omega_J so the bath is genuinely slow/pinned (the only regime
# in which it carries large static weight). Weights w_i chosen so the *static*
# chi_glass(0) is enormous (>> rho_s^el) — maximally charitable to the escape.
#   chi_glass(0) = sum_i w_i / Gamma_i.
# Pick three slow modes spanning the glassy range (ueV..meV).
GLASS_MODES = [
    # (w_i [meV], Gamma_i [meV])   Gamma_i << omega_J = 10 meV (slow glass)
    (5.0e1, 1.0e-3),   # very slow pinned phason  (Gamma ~ 1 ueV)
    (5.0e1, 1.0e-2),   # slow                     (Gamma ~ 10 ueV)
    (5.0e1, 1.0e-1),   # fastest glass mode still << omega_J (Gamma ~ 0.1 meV)
]


def static_chi():
    """chi_glass(omega->0) = sum_i w_i / Gamma_i (the compressibility-channel weight)."""
    return chi_glass(0.0, GLASS_MODES)


def chi_at_omega_J():
    """chi_glass evaluated at the Josephson plasma frequency (what a winding vortex
    actually feels). Slow bath: omega_J >> Gamma_i => kernel ~ sum w_i Gamma_i/omega_J^2."""
    return chi_glass(OMEGA_J_MEV, GLASS_MODES)


# ---------------------------------------------------------------------------
# Effective stiffness and T_BKT under the two competing interpretations.
# ---------------------------------------------------------------------------
# ESCAPE (naive) reading: pretend the static glass weight ADDS to the spatial
# stiffness:  rho_s^escape = rho_s^el + chi_glass(0).  T_BKT^escape = (pi/2)rho_s^escape.
# This is the reading the seed needs to beat the wall — we compute it to show how
# absurd (and physically wrong) it is.
def rho_s_escape_meV():
    return RHO_S_EL_MEV + static_chi()


def tbkt_escape_K():
    return rho_s_escape_meV() / KB_MEV_PER_K   # (pi/2) folded into RIGIDITY anchor


# HONEST (N2 wrong-channel) reading: chi_glass multiplies (dtau theta)^2, a
# TEMPORAL term. Nelson-Kosterlitz: T_BKT depends on the SPATIAL stiffness only.
# So the glass contributes ZERO to T_BKT, regardless of its static weight.
def rho_s_eff_honest_meV():
    return RHO_S_EL_MEV            # temporal kernel does NOT enter spatial stiffness


def tbkt_honest_K():
    return rho_s_eff_honest_meV() / KB_MEV_PER_K


# N1 frequency-mismatch: the fraction of the static glass weight that actually
# survives at the vortex (Josephson) scale. If the bath could somehow feed the
# spatial channel, only the high-frequency tail would reach the vortex.
def surviving_weight_fraction():
    c0 = static_chi()
    cJ = chi_at_omega_J()
    return cJ / c0 if c0 > 0 else 0.0


# Even in the (physically wrong) world where the SURVIVING high-frequency weight
# could feed the spatial stiffness, what T_BKT would it give?
def tbkt_surviving_K():
    rho_eff = RHO_S_EL_MEV + chi_at_omega_J()
    return rho_eff / KB_MEV_PER_K


# ---------------------------------------------------------------------------
# Compute metrics.
# ---------------------------------------------------------------------------
c0 = static_chi()
cJ = chi_at_omega_J()
frac = surviving_weight_fraction()

metrics = {
    "rho_s_el_meV": RHO_S_EL_MEV,
    "rigidity_el_K": RIGIDITY_EL_K,
    "omega_J_meV": OMEGA_J_MEV,
    "min_gamma_meV": min(g for _, g in GLASS_MODES),
    "max_gamma_meV": max(g for _, g in GLASS_MODES),
    "static_chi_meV": c0,
    "chi_at_omegaJ_meV": cJ,
    "surviving_fraction": frac,
    "tbkt_honest_K": tbkt_honest_K(),        # the real answer (N2): unchanged
    "tbkt_escape_K": tbkt_escape_K(),        # naive static-add (what seed needs)
    "tbkt_surviving_K": tbkt_surviving_K(),  # frequency-cut spatial-add (N1 charity)
    "ceiling_top_K": CEILING_TOP_K,
    "room_K": ROOM_K,
}

# ---------------------------------------------------------------------------
# Falsifiers (PASS = NOT triggered). N1 & N2 are the DECISIVE honest-nulls.
# Convention: predicate(m) -> True means TRIGGERED (FAIL) = the null/wall-
# confirming condition HOLDS. An escape needs the decisive nulls to PASS.
# ---------------------------------------------------------------------------
falsifiers = [
    Falsifier(
        name="honest_null_N1_glass_decoupled_at_vortex_scale",
        predicate=lambda m: m["surviving_fraction"] < 1e-3,
        desc=("DECISIVE honest-null (frequency-mismatch, the seed's own stated null). "
              "TRIGGERED (FAIL) when the fraction of static glass weight surviving at "
              "the Josephson/vortex frequency omega_J is < 1e-3 -> the slow pinned "
              "glass (Gamma_i << omega_J) is frequency-decoupled from the fast phase "
              "winding that unbinds a vortex; chi_glass(omega_J)->0. PASS (escape) "
              "needs the bath to follow the vortex scale (surviving_fraction ~ 1)."),
    ),
    Falsifier(
        name="honest_null_N2_temporal_kernel_does_not_enter_TBKT",
        predicate=lambda m: abs(m["tbkt_honest_K"] - m["rigidity_el_K"]) < 1e-9,
        desc=("DECISIVE honest-null (wrong-channel, structural). TRIGGERED (FAIL) when "
              "the honest T_BKT equals the electronic-only rigidity to machine "
              "precision -> the glass kernel chi_glass*(dtau theta)^2 is a TEMPORAL "
              "(compressibility) term and does NOT enter the Nelson-Kosterlitz "
              "spatial-stiffness T_BKT=(pi/2)rho_s^el. d T_BKT/d chi_glass = 0 for ALL "
              "w_i,Gamma_i. PASS (escape) needs T_BKT to actually shift with the bath."),
    ),
    Falsifier(
        name="honest_TBKT_below_room_target",
        predicate=lambda m: m["tbkt_honest_K"] < m["room_K"],
        desc=("TRIGGERED (FAIL) when the honest (real-channel) T_BKT stays below the "
              "293 K room target. PASS (escape) would need T_BKT >= 293 K from the "
              "glass ballast."),
    ),
    Falsifier(
        name="frequency_cut_TBKT_below_ceiling",
        predicate=lambda m: m["tbkt_surviving_K"] <= m["ceiling_top_K"] + 1e-6,
        desc=("TRIGGERED (FAIL) when even the maximally-charitable 'surviving high-"
              "frequency weight feeds the spatial stiffness' reading stays at/below "
              "the 164 K ceiling top -> after the omega_J frequency cut, the glass adds "
              "negligible stiffness. PASS (escape) would need the frequency-cut "
              "contribution to push T_BKT past 164 K."),
    ),
    Falsifier(
        name="glass_is_slow_guard",
        predicate=lambda m: not (m["max_gamma_meV"] < m["omega_J_meV"]
                                 and m["min_gamma_meV"] > 0.0
                                 and m["static_chi_meV"] > m["rho_s_el_meV"]),
        desc=("Physical guard / charity witness. TRIGGERED (FAIL) iff the bath is NOT a "
              "genuine strong slow glass; PASS means every Gamma_i < omega_J (slow, "
              "pinned) AND chi_glass(0) > rho_s^el (the static weight is huge, stacked "
              "in the escape's favor) -> the null is tested against the most favorable "
              "glass, not a weak strawman."),
    ),
]

verdict_ledger = evaluate(metrics, falsifiers)
falsifiers_pass = verdict_ledger["n_pass"]
n_total = verdict_ledger["n_total"]

# Decisive honest-null logic (NO LLM self-judge): escapes-wall ONLY if BOTH
# decisive honest-null prongs (N1 frequency-mismatch, N2 wrong-channel) PASS
# (are NOT triggered) — i.e. the glass genuinely follows the vortex scale AND the
# kernel genuinely enters the spatial stiffness. Expected closed-negative: both
# TRIGGERED (FAIL).
n1_pass = not verdict_ledger["falsifiers"][0]["triggered"]
n2_pass = not verdict_ledger["falsifiers"][1]["triggered"]
escapes = n1_pass and n2_pass
verdict = "escapes-wall" if escapes else "confirms-wall"

# ---------------------------------------------------------------------------
# Verbatim report.
# ---------------------------------------------------------------------------
L = "=" * 74
print(L)
print("H_059  Pinning-Memory Ratchet — glassy-phason non-equilibrium stiffness ballast")
print(L)
print("cluster: SF / phase-stiffness ceiling (borrow stiffness from a non-electronic glass)")
print("kernel : chi_glass(w)=sum_i w_i*G_i/(w^2+G_i^2)  (overdamped-phason / TLS bath)")
print("         Jiang-Zaccone-Setty-Baggioli, PRB 108 054203 (2023) = arXiv:2305.05407")
print("-" * 74)
print("electronic spatial stiffness  (pi/2)rho_s^el = {:.2f} K  (= {:.4f} meV, charity=band top)".format(
    RIGIDITY_EL_K, RHO_S_EL_MEV))
print("Josephson plasma (vortex) freq  omega_J       = {:.2f} meV".format(OMEGA_J_MEV))
print("glass modes (w_i meV, Gamma_i meV):")
for w_i, g_i in GLASS_MODES:
    print("    w={:>8.3e}  Gamma={:>8.3e}  (Gamma/omega_J={:.2e})".format(
        w_i, g_i, g_i / OMEGA_J_MEV))
print("-" * 74)
print("static kernel   chi_glass(0)        = {:.4e} meV   (>> rho_s^el: charity)".format(c0))
print("kernel at vortex chi_glass(omega_J) = {:.4e} meV".format(cJ))
print("surviving weight fraction cJ/c0     = {:.4e}   (N1: ~0 => slow bath decoupled)".format(frac))
print("-" * 74)
print("T_BKT readings:")
print("  HONEST   (N2 spatial-only)         = {:.2f} K   <- real answer (kernel is temporal)".format(
    metrics["tbkt_honest_K"]))
print("  naive    (static-add to spatial)   = {:.4e} K  <- what the seed claim NEEDS".format(
    metrics["tbkt_escape_K"]))
print("  charity  (freq-cut weight to spat) = {:.4f} K   <- even N1-surviving weight".format(
    metrics["tbkt_surviving_K"]))
print("campaign ceiling = {:.0f}-{:.0f} K ; room-T target = {:.0f} K".format(
    CEILING_BOT_K, CEILING_TOP_K, ROOM_K))
print("-" * 74)
for r in verdict_ledger["falsifiers"]:
    tag = "FAIL" if r["triggered"] else "PASS"
    print("  [{}] {}".format(tag, r["name"]))
print("-" * 74)
print("HONEST-NULL N1 escape-PASS (glass follows vortex scale) = {}".format(n1_pass))
print("HONEST-NULL N2 escape-PASS (kernel enters spatial T_BKT) = {}".format(n2_pass))
print("falsifiers_pass = {}/{}".format(falsifiers_pass, n_total))
print("is_green = False")
print("absorbed = false")
print("VERDICT: {}".format(verdict))
print(L)
