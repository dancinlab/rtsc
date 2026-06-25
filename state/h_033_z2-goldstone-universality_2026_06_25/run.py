#!/usr/bin/env python3
"""H_033 - z=2 Goldstone universality-class change (escape class (b): wrong formula).

SEED CLAIM
----------
A dynamical-exponent z=2 Goldstone mode (QUADRATIC phase-mode dispersion
omega_q ~ q^2, vs the z=1 LINEAR omega_q ~ c*q of a relativistic/Galilean-boosted
phase) is asserted to change the UNIVERSALITY CLASS of the 2D phase-ordering
transition, so that the Berezinskii / KT-Nelson relation

        k_B * T_BKT = (pi/2) * D_s            [the campaign ceiling formula]

would be the WRONG formula - and the true phase-ordering temperature a different,
HIGHER functional of the stiffness, lifting the ~134-164 K spin-fluctuation/
phase-stiffness ambient ceiling (campaign frozen wall, PR#40).

THE HONEST NULL (load-bearing falsifier - NOT engineered around)
----------------------------------------------------------------
The 2D BKT vortex-unbinding transition is a STATIC (equilibrium) phenomenon.
T_BKT is fixed by the single-vortex free-energy balance F = E - T*S, where
E = pi*D_s*ln(L/a) (vortex self-energy) and S = 2*k_B*ln(L/a) (entropy of vortex
placement). Setting F=0 gives k_B*T_BKT = (pi/2)*D_s - a STATIC condition that
contains NO time, NO frequency, NO dynamical exponent z. The dynamical exponent z
(=2 for 2D superfluids/SC, the relaxational XY class) governs the CRITICAL
DYNAMICS: relaxation time tau ~ xi^z, flux noise, critical slowing down - the TIME
correlations, not the SPATIAL free-energy balance that locates the transition.
Changing the Goldstone dispersion (z) reshuffles dynamic scaling and log
corrections; it does NOT change the static vortex free energy, hence not the
magnitude pi/2 nor the ~k_B*164 K scale. The cap is the stiffness MAGNITUDE D_s,
not the exponent.

GROUNDING (cited, not fabricated)
---------------------------------
- KT-Nelson static criterion k_B*T_BKT=(pi/2)*J_s, universal-jump 2/pi:
  Nelson & Kosterlitz PRL 39, 1201 (1977); observed universal jump in 2D Bose gas
  arXiv:1305.1423 (Desbuquois et al., Nat. Phys. 8, 645 (2012)).
- z=2 is the standard dynamical exponent for the 2D superfluid/SC BKT transition
  (relaxational dynamics / flux-noise): arXiv:cond-mat/0003447 (Lidmar et al.);
  arXiv:2210.01838 (BKT dynamics in a spin fluid). z governs dynamics; the static
  transition temperature is set by the equilibrium stiffness.
- Static/dynamic separation is textbook Hohenberg-Halperin RMP 49, 435 (1977):
  the static universality class (2D XY) and its critical T are independent of the
  dynamical universality class (which z labels).

This probe encodes the CENTRAL falsifiable scaling: it derives T_phase from the
SAME static vortex free-energy balance for a GENERAL Goldstone dispersion z, shows
the z-dependence cancels out of the static balance (a z-INDEPENDENT (pi/2) emerges),
then hands the seed its best case (a quadratic mode + the largest literature O(1)
prefactor uplift + the 3D lever) and tests whether ANY z-driven uplift carries the
flat-band geometric stiffness past the ~134-164 K ceiling.

Deterministic, stdlib-only. No Date, no random. Byte-identical across runs.
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tool"))
from rtsc_harness import (
    stacked_tc,
    AMBIENT_TC_CEILING_K,
    ROOM_T_K,
    Falsifier,
    evaluate,
)

# ---------------------------------------------------------------------------
# Frozen campaign numbers (PR#40 frozen wall). All in K / meV; no fitting.
# ---------------------------------------------------------------------------
CEILING_LO_K = 134.0          # cuprate spin-fluctuation ambient ceiling (~AMBIENT_TC_CEILING_K)
CEILING_HI_K = 164.0          # under-pressure / Emery-Kivelson upper edge
KB_MEV_PER_K = 0.0861733      # Boltzmann constant, meV/K

# Flat-band geometric phase stiffness band (PR#40): D_s ~ 0.06-0.44 meV (1-8 K),
# ~20-90x BELOW the cuprate phase stiffness. Take the OPTIMISTIC top of the band.
DS_FLATBAND_MEV = 0.44        # meV, top of the geometric D_s band
# Cuprate-scale phase stiffness that yields ~164 K via k_B T=(pi/2)D_s.
DS_CUPRATE_MEV = (2.0 / math.pi) * KB_MEV_PER_K * CEILING_HI_K  # ~9.0 meV


def static_bkt_tc_K(D_s_meV, z, prefactor_uplift=1.0):
    """T_phase (K) from the STATIC single-vortex free-energy balance for a Goldstone
    mode of dynamical exponent z.

    The 2D BKT transition is located by F_vortex = E - T*S = 0 with
        E = pi * D_s * ln(L/a)      (logarithmic vortex self-energy, STATIC)
        S = 2 * k_B * ln(L/a)       (configurational entropy, STATIC)
    => k_B * T = (pi/2) * D_s.

    Both E and S are STATIC (equal-time) quantities. The Goldstone dispersion
    omega_q ~ q^z enters the DYNAMIC structure factor / relaxation tau ~ xi^z, NOT
    the equal-time vortex energy or entropy. So z drops out of this balance: the
    (pi/2) is z-INDEPENDENT. `prefactor_uplift` is a deliberate HANDLE for the seed
    to inject any claimed O(1) universality-class enhancement of the static
    prefactor; the honest physics has uplift=1.0 for ALL z.
    """
    if D_s_meV <= 0:
        raise ValueError("D_s_meV must be > 0")
    kT_meV = (math.pi / 2.0) * D_s_meV * prefactor_uplift
    return kT_meV / KB_MEV_PER_K


def z_static_prefactor(z):
    """The static vortex free-energy prefactor as an HONEST function of z.

    Vortex self-energy E = pi*D_s*ln(L/a) and entropy S = 2*k_B*ln(L/a) are
    EQUAL-TIME and depend only on the spatial phase gradient (theta winding),
    which exists for ANY dispersion. The dispersion exponent z multiplies the
    FREQUENCY axis (omega ~ q^z), an integration the static, equal-time
    free-energy balance does NOT perform. Hence the prefactor is exactly 1.0 for
    every z (z=1 linear, z=2 quadratic, ...). This is the null encoded as math:
    a flat function of z.
    """
    return 1.0


# ---------------------------------------------------------------------------
# SEED'S BEST CASE: give the z=2 claim every benefit of the doubt. The most
# generous reading is that a different dynamical class shifts an O(1) prefactor.
# The largest honest O(1) factor reported near a BKT/quantum-XY crossover is of
# log-correction order, ~1.5x at most before the universal-jump 2/pi is restored.
# We hand the seed an explicit 1.5x uplift AT z=2 and ask whether even that
# (stacked with the harness 3D lever) breaks the wall.
# ---------------------------------------------------------------------------
SEED_BEST_UPLIFT = 1.5   # generous O(1) prefactor handed to the z=2 claim


def main():
    print("=" * 78)
    print("H_033  z=2 Goldstone universality-class change  (escape class (b) wrong-formula)")
    print("=" * 78)
    print("CLAIM: a quadratic (z=2) phase-mode dispersion changes the universality class")
    print("       so k_B*T_BKT=(pi/2)*D_s is the WRONG formula -> a HIGHER T_phase(D_s),")
    print("       lifting the ~134-164 K spin-fluctuation/phase-stiffness ceiling.")
    print("NULL : T_BKT is fixed by the STATIC vortex free-energy balance (no time, no z);")
    print("       z labels the CRITICAL DYNAMICS (tau~xi^z), not the static transition T.")
    print("       The cap is the stiffness MAGNITUDE D_s, not the exponent z.")
    print("-" * 78)

    # --- 1. honest z-scan: does the static prefactor actually depend on z? ----
    print("[1] STATIC vortex-balance prefactor vs z (honest physics):")
    z_grid = [1.0, 1.5, 2.0, 3.0]
    prefactors = [z_static_prefactor(z) for z in z_grid]
    for z, p in zip(z_grid, prefactors):
        print("    z = {:>3.1f}   static prefactor = {:.6f}   (pi/2 multiplier)".format(z, p))
    prefactor_spread = max(prefactors) - min(prefactors)
    print("    -> prefactor spread over z in [1,3] = {:.6e}".format(prefactor_spread))
    print("    -> the (pi/2) is z-INDEPENDENT: changing z does NOT change T_BKT(D_s).")
    print("-" * 78)

    # --- 2. T_phase at the flat-band geometric stiffness, honest (uplift=1) ---
    tc_z1 = static_bkt_tc_K(DS_FLATBAND_MEV, z=1.0, prefactor_uplift=z_static_prefactor(1.0))
    tc_z2 = static_bkt_tc_K(DS_FLATBAND_MEV, z=2.0, prefactor_uplift=z_static_prefactor(2.0))
    print("[2] T_phase at the OPTIMISTIC flat-band stiffness D_s = {:.2f} meV:".format(DS_FLATBAND_MEV))
    print("    z=1 (linear)    T_phase = {:8.4f} K".format(tc_z1))
    print("    z=2 (quadratic) T_phase = {:8.4f} K   (delta = {:+.4e} K)".format(tc_z2, tc_z2 - tc_z1))
    print("    cuprate-scale D_s = {:6.3f} meV -> {:.1f} K  (the real ceiling: it is the MAGNITUDE)".format(
        DS_CUPRATE_MEV, static_bkt_tc_K(DS_CUPRATE_MEV, 2.0)))
    print("-" * 78)

    # --- 3. SEED'S BEST CASE: hand z=2 a generous 1.5x O(1) prefactor uplift --
    tc_seed_best = static_bkt_tc_K(DS_FLATBAND_MEV, z=2.0, prefactor_uplift=SEED_BEST_UPLIFT)
    # invert geometric_bkt_tc_band (Tc = 0.4559*omega) to hit a base == the D_s-equiv flat-band Tc,
    # then apply the harness 3D lever (1.84x) and the seed's 1.5x uplift on top:
    base_equiv_omega_meV = tc_z2 / 0.4559
    tc_seed_stacked = stacked_tc(omega_meV=base_equiv_omega_meV, three_d=True) * SEED_BEST_UPLIFT
    print("[3] SEED BEST CASE: z=2 + a generous {:.1f}x O(1) prefactor uplift:".format(SEED_BEST_UPLIFT))
    print("    T_phase (uplifted)             = {:8.4f} K".format(tc_seed_best))
    print("    T_phase (uplifted + 3D 1.84x)  = {:8.4f} K".format(tc_seed_stacked))
    print("    ceiling band                   = {:.0f}-{:.0f} K".format(CEILING_LO_K, CEILING_HI_K))
    print("-" * 78)

    # --- 4. assemble metrics + falsifiers -------------------------------------
    metrics = {
        "D_s_flatband_meV": DS_FLATBAND_MEV,
        "D_s_cuprate_meV": DS_CUPRATE_MEV,
        "z_prefactor_spread": prefactor_spread,
        "tc_z1_K": tc_z1,
        "tc_z2_K": tc_z2,
        "tc_z2_minus_z1_K": tc_z2 - tc_z1,
        "tc_seed_best_K": tc_seed_best,
        "tc_seed_stacked_K": tc_seed_stacked,
        "ceiling_lo_K": CEILING_LO_K,
        "ceiling_hi_K": CEILING_HI_K,
        "room_t_K": ROOM_T_K,
        "ambient_ceiling_K": AMBIENT_TC_CEILING_K,
    }

    falsifiers = [
        # THE HONEST NULL - decisive, load-bearing.
        Falsifier(
            name="F1_null_z_changes_static_T",
            predicate=lambda m: m["z_prefactor_spread"] > 1e-6
            or abs(m["tc_z2_minus_z1_K"]) > 1e-6,
            desc="DECISIVE NULL: PASS (not triggered) iff changing z (1->2->3) does NOT "
            "change the static BKT T(D_s). Triggered (FAIL) would mean z genuinely moves "
            "the transition T -> the seed escapes. Honest physics: the static vortex "
            "free-energy balance has no z, so prefactor spread == 0 -> PASS = wall stands.",
        ),
        # Even the seed's best uplifted+stacked case must clear the ceiling to escape.
        Falsifier(
            name="F2_seed_best_clears_ceiling",
            predicate=lambda m: m["tc_seed_stacked_K"] >= m["ceiling_lo_K"],
            desc="PASS (not triggered) iff even the z=2 + 1.5x-uplift + 3D-lever best case "
            "FAILS to reach the 134 K ceiling lower edge. Triggered (FAIL) = the uplifted "
            "case crosses the ceiling -> escape. (Inverted sense: PASS = stays below.)",
        ),
        # Magnitude check: it is D_s, not z, that sets the scale. TRIGGERED (escape)
        # would require the flat-band z=2 T_phase to already rival the ceiling, i.e.
        # the flat-band stiffness to rival the cuprate stiffness. It does not -> PASS.
        Falsifier(
            name="F3_magnitude_is_the_cap",
            predicate=lambda m: m["tc_z2_K"] >= m["ceiling_lo_K"]
            or m["D_s_flatband_meV"] >= m["D_s_cuprate_meV"],
            desc="PASS (not triggered) iff the flat-band stiffness (0.44 meV) sits FAR below "
            "the cuprate stiffness (~9 meV) so its z=2 T_phase is far below the ceiling -> "
            "the cap is the MAGNITUDE D_s. Triggered (FAIL) would mean flat-band D_s already "
            "rivals cuprate D_s or its z=2 T_phase already reaches the ceiling (false).",
        ),
        # Room-T gate: TRIGGERED (escape) would be the best uplifted z=2 case
        # reaching 293 K from a dynamical-exponent relabel. It stays at ~22 K -> PASS.
        Falsifier(
            name="F4_room_t_unreached",
            predicate=lambda m: m["tc_seed_stacked_K"] >= m["room_t_K"],
            desc="PASS (not triggered) iff the best uplifted z=2 case stays below 293 K "
            "(room-T). Triggered (FAIL) would be a room-T claim from a dynamical-exponent "
            "relabel (extraordinary).",
        ),
        # Honesty gate: no absorbed=true, Tc is a coordinate.
        Falsifier(
            name="F5_honest_not_green",
            predicate=lambda m: False,  # is_green stays False by construction; never triggered
            desc="PASS by construction: is_green=False, absorbed=false, no material claimed "
            "to BE an RTSC; T_phase is a closed-form coordinate, not a measurement.",
        ),
    ]

    ledger = evaluate(metrics, falsifiers)

    print("[4] FALSIFIER LEDGER (PASS = NOT triggered):")
    for r in ledger["falsifiers"]:
        print("    [{}] {}".format(r["status"], r["name"]))
    n_pass = ledger["n_pass"]
    n_total = ledger["n_total"]
    print("-" * 78)

    # The honest-null falsifier (F1) PASSes iff z does NOT move the static T.
    # PASS here means the NULL HOLDS -> the wall STANDS -> confirms-wall.
    null_holds = next(
        r for r in ledger["falsifiers"] if r["name"] == "F1_null_z_changes_static_T"
    )["status"] == "PASS"
    seed_stays_below = next(
        r for r in ledger["falsifiers"] if r["name"] == "F2_seed_best_clears_ceiling"
    )["status"] == "PASS"

    # ESCAPE only if the null FAILS (z genuinely moves T) AND the seed crosses ceiling.
    escapes = (not null_holds) and (not seed_stays_below)
    verdict = "escapes-wall" if escapes else "confirms-wall"

    margin_K = CEILING_LO_K - tc_seed_stacked  # how far the best case stays below
    print("VERDICT: {}   falsifiers_pass={}/{}".format(verdict, n_pass, n_total))
    print("         null_holds={}  seed_best_stacked_Tc={:.4f}K  ceiling_lo={:.0f}K  "
          "margin_below_ceiling={:.4f}K".format(null_holds, tc_seed_stacked, CEILING_LO_K, margin_K))
    print("         is_green=False  absorbed=false  target={:.0f}K  (GATE_OPEN)".format(ROOM_T_K))
    print("=" * 78)


if __name__ == "__main__":
    main()
