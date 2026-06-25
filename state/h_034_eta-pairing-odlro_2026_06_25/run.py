#!/usr/bin/env python3
"""H_034 — eta-pairing ODLRO / dark-state rigidity (escape class (c) different rigidity).

CLAIM (seed): Yang eta-pairing gives EXACT off-diagonal long-range order (ODLRO) that is
DISTANCE-INDEPENDENT. The condensate rigidity is an algebraic eta-SU(2) property
(<c_i^dag c_i^dag c_j c_j> -> n_eta/N as |i-j|->inf, with NO power-law/exponential decay),
NOT a phase stiffness. So there is no rho_s and therefore no T_BKT = (pi/2) D_s quantity
to bound T_c. A Liouvillian / dark-state route can pump the system into a NESS carrying
this ODLRO. If that rigidity survived at ambient EQUILIBRIUM it would sidestep the frozen
~134-164 K spin-fluctuation/phase-stiffness ceiling entirely.

THE HONEST NULL (load-bearing, decisive falsifier — NOT engineered around):
  Yang eta-pairing eigenstates are HIGHLY-EXCITED, NON-THERMAL, fine-tuned Hubbard
  eigenstates (quantum many-body scars / SO(4) tower), OR dissipation-stabilized dark
  states of a Liouvillian. They are NOT thermal-equilibrium phases at 293 K @ 1 atm. The
  eta-tower sits at energy ~ U per added eta-pair ABOVE the ground state, is a
  vanishing-measure set in the spectrum (eigenstate-thermalization-violating scars), and
  the macroscopic ODLRO does NOT survive realistic thermal occupation: at equilibrium the
  Boltzmann weight of the eta-condensate manifold is exp(-Delta E/kT) and the entropy of
  the thermal sea overwhelms it. A NESS requires SUSTAINED pumping (photodoping / engineered
  dissipation) — an out-of-domain external drive, not an ambient bulk SC at 1 atm.

This probe encodes BOTH the algebraic-rigidity claim AND the honest null as closed-form
math and asks: does eta-ODLRO let an AMBIENT-EQUILIBRIUM T_c exceed the ~134-164 K ceiling?

Grounded literature anchors (cited, not fabricated):
  - C.N. Yang, Phys. Rev. Lett. 63, 2144 (1989) — eta-pairing eigenstates, ODLRO,
    eta-pair sits at energy ~|U| above ground state (doublon creation).
  - Kaneko, Shirakawa, Morita, Yunoki, PRL 123, 030603 (2019), arXiv:1811.12628 —
    "Heating-Induced Long-Range eta Pairing": eta-ODLRO is a NON-equilibrium steady state
    (dissipation / periodic drive), spin sector heated to infinite T.
  - Moudgalya et al. / Mark and Motrunich — eta-pairing states as exact quantum many-body
    SCARS: ETH-violating, measure-zero highly-excited eigenstates embedded in a thermal sea.
  - Photodoped Hubbard eta-SC, arXiv:2602.17238 — high "T_c^eff" (>293 K, up to ~1400 K)
    is an EFFECTIVE temperature of a NON-equilibrium photodoped NESS, requires sustained
    photoexcitation; "standard imaginary-time equilibrium approaches are not applicable."
  - Single-site dissipation NESS eta-ODLRO, arXiv:2602.00452 — Lindblad dark-state pumping;
    a DRIVEN steady state, not an equilibrium ambient phase.

All math is closed-form, stdlib-only, deterministic (no Date, no random).
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tool"))
from rtsc_harness import ROOM_T_K, Falsifier, evaluate


# ---------------------------------------------------------------------------
# Physical constants (closed-form, no fitting)
# ---------------------------------------------------------------------------
KB_meV_per_K = 0.0861733  # Boltzmann constant in meV/K

# Frozen campaign wall (PR#40): the spin-fluctuation / phase-stiffness ambient
# ceiling band ~134-164 K. Use the UPPER edge as the bar the escape must clear.
CEILING_LO_K = 134.0
CEILING_HI_K = 164.0


def _exp(x):
    """Underflow-safe exp for very negative x (avoids platform OverflowError; keeps the
    run byte-deterministic). Returns 0.0 when x is far below double underflow."""
    if x < -700.0:
        return 0.0
    return math.exp(x)


# ---------------------------------------------------------------------------
# Part A — the ALGEBRAIC-RIGIDITY claim (taken at face value, charitably).
# ---------------------------------------------------------------------------
# Yang eta-ODLRO: the pair correlator g(r) = <c^dag_{i+r,up} c^dag_{i+r,dn} c_{i,dn} c_{i,up}>
# is distance-INDEPENDENT for an eta-condensate of N_eta pairs on L sites:
#     g(r) -> (N_eta/L)*(1 - N_eta/L)  as r -> inf   (a CONSTANT, no decay).
# This is exact eta-SU(2) algebra, NOT a Goldstone phase stiffness. So there is
# genuinely NO rho_s, hence NO T_BKT=(pi/2)D_s bound *for the eigenstate itself*.

def eta_odlro_plateau(n_eta_density):
    """Distance-independent ODLRO plateau g(inf) for eta filling nu_eta in (0,1)."""
    nu = n_eta_density
    return nu * (1.0 - nu)


def odlro_is_distance_independent(n_eta_density):
    """g(r) for the eta eigenstate has ZERO r-dependence: g(1)==g(10)==g(1e6)."""
    plateau = eta_odlro_plateau(n_eta_density)
    g_at_r = [plateau for _ in (1.0, 10.0, 1.0e6)]  # exact algebraic constant
    return max(g_at_r) - min(g_at_r) == 0.0


# ---------------------------------------------------------------------------
# Part B — the HONEST NULL: does the rigidity survive AMBIENT EQUILIBRIUM?
# ---------------------------------------------------------------------------
# The eta-tower of N_eta pairs sits at energy Delta E = N_eta * |U| ABOVE the
# ground state (each eta^dag adds a doublon costing ~|U|). At thermal equilibrium
# (temperature T, 1 atm) the canonical weight of populating a macroscopic
# eta-condensate against the thermal sea is the Gibbs factor exp(-Delta E / kT).
# For an EXTENSIVE condensate this is e^{-O(N)} -> 0: the eta-ODLRO manifold has
# VANISHING equilibrium occupation. The eta-scars are a measure-zero, ETH-violating
# set; the equilibrium free-energy minimum is the thermal (non-eta) state.

# Hubbard |U| scale for a real correlated host (eV-scale Mott physics): canonical
# |U| ~ 3 eV used for cuprate-like / photodoped Hubbard eta studies. |U| is the
# eta-tower energy gap per pair. (Closed-form; no fitting.)
U_eV_main = 3.0
U_meV_main = U_eV_main * 1000.0


def single_pair_gibbs_factor(U_meV, T_K):
    """exp(-|U|/kT): equilibrium weight to add ONE eta-pair at temperature T."""
    return _exp(-U_meV / (KB_meV_per_K * T_K))


def macroscopic_eta_equilibrium_weight(U_meV, T_K, n_pairs):
    """Gibbs weight of an EXTENSIVE eta-condensate of n_pairs against the sea:
    exp(-n_pairs*|U|/kT). For macroscopic n_pairs this is e^{-O(N)}."""
    return _exp(-n_pairs * U_meV / (KB_meV_per_K * T_K))


def ambient_equilibrium_eta_Tc(U_meV, n_pairs):
    """Equilibrium temperature needed for an O(1) Boltzmann weight on a macroscopic
    (n_pairs) eta-condensate: T = n_pairs*|U|/k. Diverges with system size -> the
    eta-condensate is NOT a thermal-equilibrium phase at any finite ambient T."""
    return n_pairs * U_meV / KB_meV_per_K


# ---------------------------------------------------------------------------
# COMPUTE
# ---------------------------------------------------------------------------
nu_eta = 0.5  # optimal (half) eta filling -> maximal plateau
plateau = eta_odlro_plateau(nu_eta)
r_independent = odlro_is_distance_independent(nu_eta)

# Single eta-pair: equilibrium T for a 1/e weight is kT ~ U => T ~ U/k (~3.5e4 K).
single_pair_Tc_K = U_meV_main / KB_meV_per_K
gibbs_at_293 = single_pair_gibbs_factor(U_meV_main, ROOM_T_K)

# Macroscopic condensate (mesoscopic block n=100 pairs — already far sub-bulk):
N_PAIRS_MACRO = 100.0
macro_weight_293 = macroscopic_eta_equilibrium_weight(U_meV_main, ROOM_T_K, N_PAIRS_MACRO)
macro_eq_Tc_K = ambient_equilibrium_eta_Tc(U_meV_main, N_PAIRS_MACRO)

# Honest equilibrium ambient eta T_c: since the macroscopic weight at ANY ambient T
# is e^{-O(N)}, the equilibrium ambient eta-condensate fraction at 293 K is
# effectively zero -> equilibrium eta T_c is 0 K (no ambient thermal phase). The ONLY
# realization is a sustained, out-of-domain external DRIVE (photodoping / Lindblad).
equilibrium_eta_Tc_ambient_K = 0.0

# Driven NESS "effective" T_c from literature (photodoped Hubbard, arXiv:2602.17238):
# up to ~1400 K, BUT it is an EFFECTIVE temperature of a NON-equilibrium pumped state,
# NOT a thermal-equilibrium T_c at 1 atm — does not satisfy the ambient target.
DRIVEN_NESS_Teff_CEILING_K = 1400.0
driven_requires_sustained_pump = True  # out-of-domain external drive


# ---------------------------------------------------------------------------
# FALSIFIERS  (PASS = NOT triggered = consistent with escaping the wall)
# ---------------------------------------------------------------------------
metrics = {
    "nu_eta": nu_eta,
    "odlro_plateau": plateau,
    "odlro_distance_independent": r_independent,
    "U_meV": U_meV_main,
    "single_pair_eq_Tc_K": single_pair_Tc_K,
    "gibbs_weight_1pair_at_293K": gibbs_at_293,
    "macro_eta_eq_weight_at_293K": macro_weight_293,
    "macro_eta_eq_Tc_K": macro_eq_Tc_K,
    "equilibrium_eta_Tc_ambient_K": equilibrium_eta_Tc_ambient_K,
    "driven_NESS_Teff_ceiling_K": DRIVEN_NESS_Teff_CEILING_K,
    "driven_requires_sustained_pump": driven_requires_sustained_pump,
    "ceiling_hi_K": CEILING_HI_K,
}

falsifiers = [
    # F1 (sanity, charitable): the algebraic rigidity claim is REAL — ODLRO is
    # genuinely distance-independent (no rho_s, no (pi/2)D_s for the eigenstate).
    # PASS = it IS distance-independent (claim's premise holds).
    Falsifier(
        "F1_algebraic_rigidity_distance_independent",
        lambda m: not bool(m["odlro_distance_independent"]),
        "eta-ODLRO pair correlator is distance-independent (exact eta-SU(2) algebra); "
        "no phase stiffness => no (pi/2)D_s bound on the EIGENSTATE. Triggers if the "
        "claimed rigidity is not actually r-independent.",
    ),
    # F2 (DECISIVE honest null): does eta-ODLRO survive AMBIENT EQUILIBRIUM at 293 K
    # @ 1 atm? The macroscopic eta-condensate Gibbs weight must be >= 1/e to be a
    # thermal phase. PASS = it survives; TRIGGER = it collapses thermally (null holds).
    Falsifier(
        "F2_HONEST_NULL_survives_ambient_equilibrium",
        lambda m: m["macro_eta_eq_weight_at_293K"] < 0.3678794,  # 1/e
        "DECISIVE: macroscopic eta-ODLRO must have an O(1) equilibrium Boltzmann weight "
        "at 293 K @ 1 atm to be an ambient thermal SC. eta-tower sits ~|U| per pair above "
        "ground => weight exp(-N*|U|/kT) = e^{-O(N)} -> 0. Triggers (null holds) when the "
        "condensate does NOT survive thermal occupation.",
    ),
    # F3: ambient-EQUILIBRIUM eta T_c must clear the frozen ceiling band upper edge.
    # The honest equilibrium ambient eta T_c is 0 K (no thermal phase). TRIGGER.
    Falsifier(
        "F3_equilibrium_Tc_exceeds_ceiling",
        lambda m: m["equilibrium_eta_Tc_ambient_K"] <= CEILING_HI_K,
        "ambient-EQUILIBRIUM eta T_c must exceed the ~134-164 K wall to escape. Triggers "
        "when equilibrium eta T_c <= 164 K (it is 0 K: no thermal-equilibrium eta phase "
        "at 1 atm).",
    ),
    # F4: realization must be IN-DOMAIN (no out-of-domain sustained drive). eta-ODLRO
    # only appears as a DRIVEN NESS (photodoping / Lindblad pump). TRIGGER.
    Falsifier(
        "F4_realizable_without_sustained_external_drive",
        lambda m: bool(m["driven_requires_sustained_pump"]),
        "macroscopic eta-ODLRO must be realizable as an ambient bulk phase WITHOUT a "
        "sustained out-of-domain external drive. Triggers when it requires continuous "
        "photodoping / engineered Lindblad dissipation (a NESS, not an equilibrium SC).",
    ),
    # F5: the driven-NESS 'high T_c^eff' (up to ~1400 K) must be a genuine ambient
    # EQUILIBRIUM T_c, not merely an EFFECTIVE temperature of a pumped state.
    Falsifier(
        "F5_driven_Teff_is_true_ambient_Tc",
        lambda m: bool(m["driven_requires_sustained_pump"]),
        "the photodoped 'T_c^eff up to ~1400 K' must be a true thermal-equilibrium ambient "
        "T_c, not the EFFECTIVE temperature of a sustained non-equilibrium steady state. "
        "Triggers because the literature T_c^eff is a NESS effective-temperature requiring "
        "continuous pumping (arXiv:2602.17238), not an equilibrium phase at 1 atm.",
    ),
]

ledger = evaluate(metrics, falsifiers)
results = ledger["falsifiers"]

# verdict: escapes-wall ONLY if the DECISIVE honest-null (F2) PASSES (not triggered)
# with a real margin AND the equilibrium T_c (F3) clears the ceiling.
n_falsifiers = ledger["n_total"]
falsifiers_pass = ledger["n_pass"]
honest_null_pass = next((not r["triggered"]) for r in results if r["name"].startswith("F2_HONEST_NULL"))
equilibrium_escape = next((not r["triggered"]) for r in results if r["name"] == "F3_equilibrium_Tc_exceeds_ceiling")
escapes = bool(honest_null_pass and equilibrium_escape)
verdict = "escapes-wall" if escapes else "confirms-wall"

print("=" * 78)
print("H_034 — eta-pairing ODLRO / dark-state rigidity  (escape class (c))")
print("=" * 78)
print("eta filling nu_eta                 : {0}".format(nu_eta))
print("ODLRO plateau g(inf)=nu(1-nu)      : {0:.6f}  (distance-independent={1})".format(plateau, r_independent))
print("Hubbard |U| (eta-tower gap/pair)   : {0:.3f} eV  ({1:.1f} meV)".format(U_eV_main, U_meV_main))
print("single eta-pair eq. T (kT~U)       : {0:.1f} K".format(single_pair_Tc_K))
print("Gibbs weight to add 1 pair @ 293 K : {0:.3e}".format(gibbs_at_293))
print("macro eta-ODLRO eq. weight @ 293 K : {0:.3e}  (n_pairs={1:.0f})".format(macro_weight_293, N_PAIRS_MACRO))
print("macro eta eq. 'T_c' (n*U/k)        : {0:.3e} K  (drive T, not a transition)".format(macro_eq_Tc_K))
print("AMBIENT-EQUILIBRIUM eta T_c        : {0:.1f} K  (no thermal phase @ 1 atm)".format(equilibrium_eta_Tc_ambient_K))
print("frozen wall ceiling band           : {0:.0f}-{1:.0f} K".format(CEILING_LO_K, CEILING_HI_K))
print("driven-NESS T_c^eff (photodoped)   : up to {0:.0f} K  (EFFECTIVE temp, pumped)".format(DRIVEN_NESS_Teff_CEILING_K))
print("requires sustained external drive  : {0}  (out-of-domain)".format(driven_requires_sustained_pump))
print("-" * 78)
for r in results:
    tag = "PASS" if not r["triggered"] else "TRIGGER"
    print("  [{0:7s}] {1}".format(tag, r["name"]))
print("-" * 78)
print("honest-null (F2) PASS (survives ambient eq.) : {0}".format(honest_null_pass))
print("equilibrium-escape (F3) PASS                 : {0}".format(equilibrium_escape))
print("falsifiers_pass : {0}/{1}".format(falsifiers_pass, n_falsifiers))
print("is_green        : False")
print("absorbed        : False")
print("VERDICT         : {0}".format(verdict))
print("=" * 78)
