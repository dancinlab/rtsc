#!/usr/bin/env python3
"""H_035 — Amperean transverse-gauge current-current glue (escape-class: grounded, no boson).

CLAIM (seed): a transverse Amperean current-current interaction pairs electrons with
NO bosonic glue and NO competing electronic order, so it escapes BOTH the boson-energy
cap and the order-traps law that pin the ~134-164 K spin-fluctuation/phase-stiffness
ceiling (campaign frozen wall, PR#40).

HONEST NULL (the load-bearing falsifier — NOT engineered around):
  Amperean pairing is parametrically WEAK and reintroduces a competing order. Two branches:
   (A) REAL-PHOTON transverse gauge: the current-current attraction is suppressed by
       (v_F/c)^2 ~ 1e-5, so the pairing scale is microscopic — orders below the ceiling.
   (B) EMERGENT-GAUGE (Lee-Nagaosa U(1) spin liquid): replacing c by the gauge "light
       speed" ~ v_F removes the (v_F/c)^2, BUT the instability is to FINITE-MOMENTUM
       (Amperean / pair-density-wave) pairing — a COMPETING order, exactly the order-traps
       law the claim says it escapes. The proposed Amperean-SC scale in the literature is
       1-20 K (cavity-Amperean impossibility paper), NOT a 134-164 K-equivalent.

This probe encodes the CENTRAL falsifiable scaling of BOTH branches as closed-form math
and asks whether EITHER lets T_c exceed the ceiling WITHOUT reintroducing a competing
order. Deterministic, stdlib-only.

GROUNDED literature (cited, not fabricated):
  - P.A. Lee, Amperean pairing & pseudogap, Phys. Rev. X 4, 031017 (2014); arXiv:1401.0519
      -> finite-momentum (PDW) pairing; pairs electrons on the SAME side of the FS.
  - Lee-Nagaosa-Wen U(1) spin liquid Amperean instability; arXiv:cond-mat/0607015
      -> emergent gauge field; finite-momentum competing order.
  - Higher angular momentum pairing from transverse gauge interactions; arXiv:1305.3938.
  - "Amperean superconductivity cannot be induced by deep subwavelength cavities in a 2D
      material", Phys. Rev. B 109, 104513 (2024); arXiv:2210.10371
      -> Amperean-SC proposals are "on the order of 1-20 K"; real cavities induce only
         density-density (NOT current-current) coupling -> the current-current channel
         is hard to realize at scale. The (v_F/c)^2 relativistic suppression is explicit.

SPECULATIVE vs GROUNDED: the (v_F/c)^2 scaling, the finite-momentum/PDW character, and the
1-20 K literature scale are GROUNDED. The exact prefactor mapping coupling -> T_c here is a
TRANSPARENT order-of-magnitude closed form (BCS-like exp), labelled speculative; the verdict
does NOT hinge on its prefactor because branch (A) is killed by 5 orders of (v_F/c)^2 and
branch (B) is killed by the competing-order trap independent of any prefactor.
"""

import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tool'))
from rtsc_harness import Falsifier, evaluate, ROOM_T_K

# --- frozen physical constants (no tuning) -----------------------------------
C_LIGHT = 2.998e8          # m/s, speed of light
V_F = 1.0e6               # m/s, typical metallic Fermi velocity (order 1e6)
KB = 8.617e-5             # eV/K
CEILING_LO_K = 134.0      # campaign frozen spin-fluctuation / phase-stiffness ceiling, low
CEILING_HI_K = 164.0      # ... high
# Bare electronic energy scale available to the current-current channel: the Fermi /
# bandwidth scale ~ 1 eV (generous upper bound for the "no boson" electronic reservoir).
E_ELEC_eV = 1.0
# Literature-reported Amperean-SC scale ceiling (arXiv:2210.10371): 1-20 K.
LIT_AMPEREAN_TC_MAX_K = 20.0

# --- branch (A): REAL-PHOTON transverse-gauge Amperean coupling ---------------
def amperean_real_photon_coupling_eV():
    """Effective attractive pairing scale of the REAL transverse-photon current-current
    interaction = electronic scale suppressed by the relativistic (v_F/c)^2 factor.
    GROUNDED scaling (Lee; cavity-Amperean arXiv:2210.10371)."""
    suppression = (V_F / C_LIGHT) ** 2          # ~1.11e-5
    return E_ELEC_eV * suppression

def bcs_like_tc_K(coupling_eV, prefactor_eV=E_ELEC_eV, dimensionless_lambda=0.3):
    """TRANSPARENT order-of-magnitude T_c (K) from a pairing scale.
    T_c ~ (prefactor/kB) * exp(-1/lambda_eff), lambda_eff = coupling/prefactor.
    Labelled speculative; used only to show branch (A) is microscopic. Monotone in coupling."""
    lam = max(coupling_eV / prefactor_eV, 1e-12)
    return (prefactor_eV / KB) * math.exp(-1.0 / lam)

# --- branch (B): EMERGENT-GAUGE (spin-liquid) Amperean instability ------------
def amperean_emergent_gauge():
    """Lee-Nagaosa U(1) spin-liquid Amperean instability. The gauge 'light speed' ~ v_F,
    so the (v_F/c)^2 suppression is REMOVED -> coupling can reach the electronic scale.
    BUT the instability is to FINITE-MOMENTUM (Amperean/PDW) pairing: a competing density-wave
    order, NOT a uniform zero-momentum condensate. GROUNDED (arXiv:1401.0519, cond-mat/0607015).
    Returns the (best-case) pairing scale AND the competing-order flag."""
    return {
        "pairing_scale_eV": E_ELEC_eV,        # best case: no relativistic suppression
        "finite_momentum_pairing": True,      # pairs on SAME side of FS -> net momentum
        "reintroduces_competing_order": True, # PDW = a competing density-wave order
    }

# === compute =================================================================
g_A_eV = amperean_real_photon_coupling_eV()
tc_A_K = bcs_like_tc_K(g_A_eV)
suppression_AB = (V_F / C_LIGHT) ** 2

emergent = amperean_emergent_gauge()
# Branch (B) best-case T_c IF it were a uniform condensate (it is NOT — flagged):
tc_B_K_if_uniform = bcs_like_tc_K(emergent["pairing_scale_eV"])

# The claim's two simultaneous promises:
#   (i)  escape boson-energy cap  -> needs T_c > ceiling from a real (uniform) condensate
#   (ii) escape order-traps law   -> needs NO competing order reintroduced
escapes_boson_cap = (tc_A_K > CEILING_LO_K)              # branch (A), the no-suppression-free route
no_competing_order = (not emergent["reintroduces_competing_order"])
ceiling_mid_K = 0.5 * (CEILING_LO_K + CEILING_HI_K)

metrics = {
    "real_photon_coupling_eV": g_A_eV,
    "vF_over_c_sq_suppression": suppression_AB,
    "tc_real_photon_K": tc_A_K,
    "tc_emergent_if_uniform_K": tc_B_K_if_uniform,
    "emergent_finite_momentum_pairing": emergent["finite_momentum_pairing"],
    "emergent_reintroduces_competing_order": emergent["reintroduces_competing_order"],
    "ceiling_lo_K": CEILING_LO_K,
    "ceiling_hi_K": CEILING_HI_K,
    "ceiling_mid_K": ceiling_mid_K,
    "lit_amperean_tc_max_K": LIT_AMPEREAN_TC_MAX_K,
    "room_t_K": ROOM_T_K,
}

# === falsifiers (PASS = NOT triggered) =======================================
# Each predicate returns True when the CLAIM is refuted (falsifier triggered -> FAIL).
falsifiers = [
    # 1) HONEST NULL — the decisive, load-bearing falsifier.
    #    The claim escapes the order-traps law ONLY if the realizable (un-suppressed) branch
    #    does NOT reintroduce a competing order. The emergent-gauge branch is finite-momentum
    #    PDW -> competing order. This is TRIGGERED by the grounded physics.
    Falsifier(
        "honest_null_competing_order_reintroduced",
        lambda m: m["emergent_reintroduces_competing_order"] is True,
        "DECISIVE/HONEST-NULL: the only un-suppressed Amperean branch (emergent U(1) gauge) "
        "pairs at FINITE momentum (PDW) -> reintroduces exactly the competing order the claim "
        "says it escapes. Grounded: arXiv:1401.0519, cond-mat/0607015.",
    ),
    # 2) Real-photon branch is parametrically weak: (v_F/c)^2 suppression -> sub-ceiling T_c.
    Falsifier(
        "real_photon_tc_below_ceiling",
        lambda m: m["tc_real_photon_K"] < m["ceiling_lo_K"],
        "Real transverse-photon current-current coupling is suppressed by (v_F/c)^2 ~ 1e-5, "
        "so its T_c is microscopic, far below the 134-164 K ceiling.",
    ),
    # 3) Literature scale: every reported Amperean-SC proposal is 1-20 K, not >134 K.
    Falsifier(
        "lit_scale_below_ceiling",
        lambda m: m["lit_amperean_tc_max_K"] < m["ceiling_lo_K"],
        "Reported Amperean-SC scales are 1-20 K (arXiv:2210.10371), >6x below the ceiling.",
    ),
    # 4) Does NOT reach room-T even in the (non-physical) best uniform-condensate case AND
    #    that best case still requires the competing-order branch -> the claim's joint promise
    #    (uniform AND no competing order AND >ceiling) is unsatisfiable.
    Falsifier(
        "joint_promise_unsatisfiable",
        lambda m: not ( (m["tc_real_photon_K"] > m["ceiling_lo_K"]) and
                        (not m["emergent_reintroduces_competing_order"]) ),
        "Joint promise unsatisfiable: the route with no competing order (real-photon) is sub-"
        "ceiling, and the route that reaches the scale (emergent gauge) is a competing PDW.",
    ),
    # 5) Sanity: suppression factor is genuinely ~1e-5 (guards the branch-A physics).
    Falsifier(
        "suppression_not_microscopic",
        lambda m: m["vF_over_c_sq_suppression"] > 1e-3,
        "Guard: (v_F/c)^2 must be microscopic (<1e-3) for the real-photon argument to hold.",
    ),
]

ledger = evaluate(metrics, falsifiers)

# Honest-null is falsifier index 0. "escapes-wall" requires the HONEST NULL to PASS
# (NOT triggered) with a real margin AND the joint-promise falsifier to PASS.
honest_null = ledger["falsifiers"][0]
joint = ledger["falsifiers"][3]
honest_null_passes = (honest_null["status"] == "PASS")
joint_passes = (joint["status"] == "PASS")
escapes = honest_null_passes and joint_passes

verdict = "escapes-wall" if escapes else "confirms-wall"
n_pass = ledger["n_pass"]
n_total = ledger["n_total"]

print("=" * 72)
print("H_035  Amperean transverse-gauge current-current glue")
print("=" * 72)
print(f"branch(A) real-photon coupling      = {g_A_eV:.3e} eV")
print(f"  (v_F/c)^2 suppression             = {suppression_AB:.3e}")
print(f"  -> T_c(real-photon)               = {tc_A_K:.3e} K")
print(f"branch(B) emergent-gauge pairing    = {emergent['pairing_scale_eV']:.3f} eV (no (v_F/c)^2)")
print(f"  finite-momentum (PDW) pairing     = {emergent['finite_momentum_pairing']}")
print(f"  reintroduces competing order      = {emergent['reintroduces_competing_order']}")
print(f"  -> T_c(emergent, IF uniform)      = {tc_B_K_if_uniform:.3e} K  [not physical: PDW]")
print(f"literature Amperean-SC scale max    = {LIT_AMPEREAN_TC_MAX_K:.1f} K  (arXiv:2210.10371)")
print(f"campaign ceiling                    = {CEILING_LO_K:.0f}-{CEILING_HI_K:.0f} K   (room-T target {ROOM_T_K:.0f} K)")
print("-" * 72)
for r in ledger["falsifiers"]:
    print(f"  [{r['status']}] {r['name']}")
print("-" * 72)
print(f"HONEST-NULL (decisive) status       = {honest_null['status']}")
print(f"joint-promise falsifier status      = {joint['status']}")
print(f"falsifiers_pass                     = {n_pass}/{n_total}")
print(f"is_green                            = False")
print(f"absorbed                            = false")
print(f"VERDICT: {verdict}")
print("=" * 72)
