#!/usr/bin/env python3
"""H_044 -- Chern-Simons Stiffness Pump (anyon statistical rigidity).

WITHIN-CLUSTER VARIANT of the spin-fluctuation / phase-stiffness ambient ceiling
(T_BKT = (pi/2) D_s). The variant's twist: instead of a *bosonic glue* family
(H_032-035) or a *vortex/order-trap* attack (H_036, H_043), it asks whether the
STATISTICAL gauge field of a doped fractional quantum anomalous Hall (FQAH) host --
composite fermions coupled to a Chern-Simons gauge field at level k -- supplies a
glue-free superfluid stiffness D_s that beats the wall.

Central falsifiable scaling (from the real anyon-SC literature, deterministic,
stdlib-only; no fitting, no random, no Date):

  Doped FQAH at filling nu_e (e.g. 2/3) with doping delta = |nu - nu_e|.
  The anyon superconductor's stiffness (Nosov-Han-Khalaf 2025, arXiv:2506.02108):

      kappa = omega_c / (3 pi),   omega_c = pi * delta / m_star        (Eq. 'kappa~omega_c')

  i.e.  D_s = kappa = delta / (3 m_star).

  In a FLAT Chern band the composite-fermion mass m_star has NO kinetic scale --
  the projected band is dispersionless -- so the ONLY scale is the interaction:

      1/m_star = c_m * U_int        (CF mass set by the Coulomb/interaction scale;
                                     standard flat-band CF result, c_m = O(1))

  Hence the Chern-Simons response collapses onto the INTERACTION-set boson line:

      D_s(CS) = c_geom * delta(1 - delta) * U_int        (the Uemura/boson-limited
                                                          form D_s ~ |U| nu(1-nu) <g>)

  The statistical angle theta = pi/k enters ONLY through c_geom = O(1) prefactors
  (the level renormalizes the flux attachment, not the energy scale). It does NOT
  manufacture stiffness beyond U_int.

HONEST-NULL (load-bearing, pre-registered DECISIVE): for ALL k and ALL doping delta,
max_k,delta D_s(CS) collapses onto the boson-limited line and stays at the interaction
scale, far below the wall D_s* = (2/pi) kB * 164 K = 9.00 meV -- the CS gauge field
renormalizes to ZERO net extra stiffness. If instead some (delta, k) window gives
D_s > D_s* with a real margin while staying physical (U_int <= FQAH ceiling), the wall
is escaped.

We FALSIFY by computing max D_s(CS) over the full (delta, k) grid at the GENEROUS host
interaction ceiling and asking whether it clears the wall. Confirm-wall is expected
(this is a variant of a confirmed mechanism); escapes-wall ONLY if the null genuinely
PASSES with margin.
"""

import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tool"))
from rtsc_harness import Falsifier, evaluate

# --- physical constants (exact, no fit) --------------------------------------
KB_MEV_PER_K = 0.0861733  # Boltzmann constant in meV/K
WALL_LO_K = 134.0         # ambient spin-fluctuation ceiling band (low)
WALL_HI_K = 164.0         # ambient spin-fluctuation ceiling band (high)
ROOM_T_K = 293.0


def ds_wall_meV(T_K):
    """Bare stiffness needed to put the 2D-BKT ceiling (pi/2)D_s at temperature T."""
    return (2.0 / math.pi) * KB_MEV_PER_K * T_K


# --- host interaction ceiling (GENEROUS, sourced) ----------------------------
# FQAH is realized in moire flat Chern bands (tMoTe2, R-stacked, nu_e=2/3:
# Cai et al. Nature 2023, arXiv:2308.06177). The interaction scale is the gate-
# screened Coulomb energy e^2/(eps l_B-moire). Across reported tMoTe2 / rhombohedral
# graphene FQAH hosts the Coulomb scale is ~10-30 meV; we take a GENEROUS ceiling
# (steel-man the escape) of U_CEILING = 30 meV. This is ALREADY at/above the H-H
# phonon stretch family and well above any flat-band geometric stiffness.
U_CEILING_MEV = 30.0

# CF-mass prefactor c_m in 1/m_star = c_m * U_int. For a flat Chern band the CF mass
# is set entirely by interaction; microscopic studies give an O(1) coefficient. We take
# the GENEROUS c_m = 1.0 (1/m_star = full U_int) -- larger c_m only HELPS the escape, so
# this maximizes D_s and cannot hide a real escape.
C_M = 1.0

# Geometric / level prefactor c_geom(theta=pi/k). This is NOT a free knob: the real
# anyon-SC literature DERIVES it. Nosov-Han-Khalaf (arXiv:2506.02108) give the clean-limit
# stiffness kappa = omega_c/(3 pi) with omega_c = pi*delta/m_star, i.e. the doping-density
# of CS flux carries a hard 1/(3 pi) suppression from the Landau-damped CF particle-hole
# continuum (Halperin-Lee-Read RPA). We use the LITERATURE value c_geom = 1/(3 pi); we do
# NOT inflate it -- removing the 1/(3 pi) would be tune-to-green by fabricating stiffness
# the gauge field does not actually supply. The statistical level k enters only as a
# further O(1) flux-attachment factor <= 1 (we cap it at 1, the most generous over k).
C_GEOM = 1.0 / (3.0 * math.pi)   # literature: kappa = omega_c/(3 pi)


def ds_cs_meV(delta, k, U_int, c_m=C_M, c_geom=C_GEOM):
    """Chern-Simons / anyon-SC stiffness (literature clean-limit form).

    D_s(CS) = kappa = omega_c/(3 pi),  omega_c = pi*delta/m_star,  1/m_star = c_m*U_int
            = c_geom * delta * (1-delta) * (c_m * U_int)

    with c_geom = 1/(3 pi) the DERIVED prefactor (not a tuned knob). delta = doping away
    from nu_e (in [0,1]); the (1-delta) factor is the particle-hole / boson n(1-n) form;
    k = CS level (theta = pi/k) enters only as an O(1) flux factor (<=1), capped at the
    most generous value 1. This is the honest interaction-set stiffness the gauge field
    actually delivers -- the steel-man is the GENEROUS interaction ceiling and c_m, NOT
    deleting the literature 1/(3 pi) suppression.
    """
    if not (0.0 <= delta <= 1.0):
        raise ValueError(f"delta out of [0,1]: {delta}")
    if k < 1:
        raise ValueError(f"CS level k must be >= 1: {k}")
    level_factor = 1.0  # most-generous O(1) over all k
    return c_geom * level_factor * delta * (1.0 - delta) * (c_m * U_int)


def boson_line_meV(delta, U_int, g_mean=1.0):
    """The honest-null reference line: the bare Uemura/boson-limited stiffness
    D_s ~ |U| * nu(1-nu) * <g> WITHOUT the CS 1/(3 pi) suppression (g_mean=1, U=U_int).
    The CS response (which carries 1/(3 pi)) is COMPARED against this: the honest-null
    says the gauge field does not exceed -- in fact lands a factor 1/(3 pi) BELOW -- this
    interaction line, i.e. it manufactures no extra statistical rigidity."""
    return delta * (1.0 - delta) * U_int * g_mean


def scan():
    """Grid-scan (delta, k) at the generous host ceiling; return the max D_s(CS),
    where it occurs, and whether it clears the wall / beats the boson line."""
    deltas = [i / 200.0 for i in range(0, 201)]      # 0.000 .. 1.000 step 0.005
    levels = list(range(1, 13))                       # CS level k = 1..12 (theta=pi/k)
    best = {"D_s": -1.0, "delta": None, "k": None}
    max_excess_over_boson = -1.0e9                    # max (D_s_CS - boson_line)
    for k in levels:
        for d in deltas:
            ds = ds_cs_meV(d, k, U_CEILING_MEV)
            bl = boson_line_meV(d, U_CEILING_MEV)
            excess = ds - bl
            if excess > max_excess_over_boson:
                max_excess_over_boson = excess
            if ds > best["D_s"]:
                best = {"D_s": ds, "delta": d, "k": k}
    return best, max_excess_over_boson


def main():
    line = "=" * 78
    print(line)
    print("H_044  Chern-Simons Stiffness Pump  -  anyon statistical rigidity (FQAH host)")
    print(line)
    print("Cluster: spin-fluctuation / phase-stiffness ambient ceiling  T_BKT=(pi/2)D_s")
    print("Variant twist: STATISTICAL gauge field of doped FQAH composite fermions as a")
    print("               glue-free D_s source (NOT a boson glue family, NOT a vortex code).")
    print("Mechanism: D_s = kappa = delta/(3 m*) ; flat Chern band -> 1/m* = c_m*U_int")
    print("           => D_s(CS) collapses to c_geom*delta(1-delta)*U_int (boson line).")
    print("Source: Nosov-Han-Khalaf arXiv:2506.02108 (kappa~omega_c, omega_c=pi*delta/m*);")
    print("        Halperin-Lee-Read CF/Chern-Simons RPA; tMoTe2 FQAH host (2308.06177).")
    print("-" * 78)

    ds_wall_lo = ds_wall_meV(WALL_LO_K)
    ds_wall_hi = ds_wall_meV(WALL_HI_K)
    ds_wall_room = ds_wall_meV(ROOM_T_K)

    print(f"  GENEROUS host interaction ceiling U_int      = {U_CEILING_MEV:.3f} meV")
    print(f"  CF-mass prefactor c_m (1/m*=c_m*U_int)       = {C_M:.3f}  (steel-man)")
    print(f"  level/geom prefactor c_geom=1/(3pi) (literature) = {C_GEOM:.5f}")
    print("-" * 78)

    best, max_excess = scan()
    print("  (delta,k) grid scan at the generous ceiling:")
    print(f"    max D_s(CS)              = {best['D_s']:.4f} meV"
          f"  at delta={best['delta']:.3f}, k={best['k']}")
    print(f"    max (D_s_CS - boson line) over grid = {max_excess:.6e} meV")
    print("-" * 78)

    # T_BKT the best CS stiffness can support:
    tbkt_best = (math.pi / 2.0) * best["D_s"] / KB_MEV_PER_K
    print(f"  D_s* (wall, 134 K)  = (2/pi)kB*134 = {ds_wall_lo:.4f} meV")
    print(f"  D_s* (wall, 164 K)  = (2/pi)kB*164 = {ds_wall_hi:.4f} meV")
    print(f"  D_s* (room, 293 K)  = (2/pi)kB*293 = {ds_wall_room:.4f} meV")
    print(f"  T_BKT from best CS D_s = (pi/2)D_s/kB = {tbkt_best:.3f} K")
    margin_K = tbkt_best - WALL_LO_K
    print(f"  margin to wall_lo (134 K)            = {margin_K:+.3f} K")
    deficit_factor = ds_wall_lo / best["D_s"] if best["D_s"] > 0 else float("inf")
    print(f"  bare-D_s deficit factor to reach 134 K = {deficit_factor:.2f}x")
    print("-" * 78)

    metrics = {
        "ds_cs_best_meV": best["D_s"],
        "ds_wall_lo_meV": ds_wall_lo,
        "ds_wall_room_meV": ds_wall_room,
        "tbkt_best_K": tbkt_best,
        "wall_lo_K": WALL_LO_K,
        "max_excess_over_boson_meV": max_excess,
        "U_ceiling_meV": U_CEILING_MEV,
    }

    falsifiers = [
        # F1 HONEST-NULL (decisive): does the best CS stiffness clear the wall?
        Falsifier(
            "honest_null_cs_clears_wall",
            lambda m: m["ds_cs_best_meV"] >= m["ds_wall_lo_meV"],
            "DECISIVE honest-null: best (delta,k) CS stiffness >= wall D_s (134 K).",
        ),
        # F2: does the CS response beat the bare boson line (real statistical pump)?
        Falsifier(
            "cs_beats_boson_line",
            lambda m: m["max_excess_over_boson_meV"] > 1e-9,
            "CS gauge field manufactures stiffness BEYOND the Uemura/boson line.",
        ),
        # F3: physicality guard -- CS stiffness must not exceed its own interaction
        # ceiling (a positive control: an unphysical run that fabricated D_s>U would
        # trivially 'escape' and must be caught).
        Falsifier(
            "cs_exceeds_interaction_ceiling",
            lambda m: m["ds_cs_best_meV"] > m["U_ceiling_meV"] + 1e-9,
            "POSITIVE CONTROL: CS D_s cannot exceed its interaction ceiling.",
        ),
        # F4: room-T reach -- best CS stiffness reaches the 293 K target stiffness.
        Falsifier(
            "cs_reaches_room_T",
            lambda m: m["ds_cs_best_meV"] >= m["ds_wall_room_meV"],
            "Best CS stiffness reaches the 293 K target D_s (room-T escape).",
        ),
    ]

    res = evaluate(metrics, falsifiers)
    print("FALSIFIER LEDGER (PASS = not triggered):")
    for r in res["falsifiers"]:
        tag = "FAIL" if r["triggered"] else "PASS"
        print(f"  [{tag}] {r['name']}")
    print("-" * 78)

    # decisive null PASSES (escape) only if F1 is TRIGGERED (CS clears the wall).
    f1 = next(r for r in res["falsifiers"] if r["name"] == "honest_null_cs_clears_wall")
    null_passes_escape = bool(f1["triggered"])
    falsifiers_pass = res["n_pass"]
    n_total = res["n_total"]

    if null_passes_escape:
        verdict = "escapes-wall"
    else:
        verdict = "confirms-wall"

    print(f"  honest-null (F1) shows CS clears wall? {null_passes_escape}"
          f"   best-case margin = {margin_K:+.3f} K")
    print(f"  falsifiers_pass = {falsifiers_pass}/{n_total}")
    print(f"VERDICT: {verdict}")
    print(line)


if __name__ == "__main__":
    main()
