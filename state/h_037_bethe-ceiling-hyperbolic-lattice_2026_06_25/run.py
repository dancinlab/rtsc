#!/usr/bin/env python3
"""H_037 — Bethe-Ceiling Lattice (negative-curvature stiffness ladder).

Cluster: connectivity-geometry universality (Mermin-Wagner fails).

ESCAPE CLAIM (frozen pre-register)
----------------------------------
The frozen phase-stiffness wall (~134-164 K; T_BKT=(pi/2)D_s) was MEASURED on
CRYSTALLINE (flat / Euclidean) hosts. Premise violated by THIS card: the
*crystalline* premise -> replace the square-lattice Cooper-pair phase field with a
NEGATIVE-CURVATURE hyperbolic tiling ({7,3} heptagonal or {5,4}). On a hyperbolic
graph the volume grows exponentially with radius (the graph is "effectively
infinite-dimensional"), so the Mermin-Wagner / BKT log-suppression of order is
claimed to be replaced by a MEAN-FIELD crossing at fixed bare stiffness J. Vortex
entropy can no longer compensate vortex energy on an exponentially-growing graph,
so (escape) T_c^hyperbolic / T_c^square >= 1.7 at matched J -> the ambient ceiling
is lifted past 164 K purely by connectivity geometry, no new glue.

HONEST-NULL (load-bearing falsifier; from the triage probe_sketch, NOT engineered)
----------------------------------------------------------------------------------
T_c^hyperbolic <= 1.2 x T_c^square: the negative curvature does NOT lift the bulk
ordering temperature. The apparent "mean-field" lift is a boundary-dominated
finite-size artifact (the {p,q} graph is an O(1)-boundary-fraction object at every
tractable size), AND the CONTINUOUS U(1) Cooper-pair phase suffers
curvature-induced frustration -> a zero-temperature glass with NO finite-T order,
so BKT-like physics (or worse) survives at matched D_s.

WHAT THIS PROBE COMPUTES (deterministic, stdlib-only)
-----------------------------------------------------
The honest settlement of the continuous-XY case at the required scale needs a
large hyperbolic XY Monte-Carlo (open-boundary, careful bulk extrapolation) that
does NOT fit deterministically in-process in seconds. So this is the best
CLOSED-FORM PROXY:

  (A) the OPTIMISTIC discrete-clock mean-field estimate the escape rests on:
      kT_c^MF = (z/2) J  (plane-rotor Weiss mean-field, z = q = vertex degree)
      vs the standard square-lattice value kT_BKT/J = 0.893
      -> the "tantalizing" naive ratio.

  (B) the {p,q} shell growth ratio mu (closed form) -> boundary fraction
      f_bd = (mu-1)/mu, the mechanism of the honest-null (the graph is
      all-boundary; "bulk mean-field" is never reached at any tractable size).

  (C) the DECISIVE honest-null, anchored to the measured literature result for the
      CONTINUOUS XY model on hyperbolic surfaces (Baek & Minnhagen, PRE 80,
      011133 (2009): curvature-induced frustration -> zero-T glass, NO finite-T
      order; and the heptagonal-XY open-boundary MC reporting absence of any
      transition incl. BKT). The order parameter for superconductivity is a
      CONTINUOUS U(1) phase, not a discrete clock state, so (C) governs, not (A).

Because the literature already REPORTS the continuous-XY honest-null result, the
proxy SETTLES the card to confirms-wall. The mean-field crossing (A) is real only
for the *discrete* clock variable; it does not carry the continuous Cooper-pair
phase, which is exactly the no-free-lunch the freeze predicts.

References (research-first; arXiv/DOI — not fabricated):
  - S.K. Baek, P. Minnhagen, H. Shima, B.J. Kim, "Curvature-induced frustration
    in the XY model on hyperbolic surfaces", Phys. Rev. E 80, 011133 (2009);
    PubMed 19658458. -> zero-T glass, NO finite-T transition (the honest-null).
  - R. Krcmar, A. Gendiar, et al., "Phase transition of clock models on
    hyperbolic lattice (CTMRG)", arXiv:0801.0836. -> DISCRETE clock models cross
    mean-field on {7,3} (the optimistic estimate (A)).
  - Tobochnik & Chester, Phys. Rev. B 20, 3761 (1979): square XY T_BKT/J ~ 0.893.
  - Mermin & Wagner, Phys. Rev. Lett. 17, 1133 (1966): the flat-host theorem.
"""

import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tool"))
from rtsc_harness import Falsifier, evaluate

# ---------------------------------------------------------------------------
# Frozen constants (no Date, no random; byte-reproducible)
# ---------------------------------------------------------------------------
WALL_LO_K = 134.0          # frozen phase-stiffness ceiling band, low
WALL_HI_K = 164.0          # frozen phase-stiffness ceiling band, high
TBKT_SQ_OVER_J = 0.893     # square-lattice XY T_BKT/J (Tobochnik-Chester 1979)
ESCAPE_RATIO = 1.7         # wall-prediction threshold (escape needs >= this)
NULL_RATIO = 1.2           # honest-null threshold (null says ratio <= this)


def shell_growth_mu(p, q):
    """Closed-form dominant shell-growth ratio of the regular hyperbolic tiling
    {p,q} (p-gons, q meeting per vertex). For {7,3} this is exactly the golden
    ratio squared phi^2 = (3+sqrt5)/2 = 2.618..., f_bd = 1/phi = 0.618."""
    a = (p - 2) * (q - 2) - 2
    if a * a - 4 < 0:
        raise ValueError("{%d,%d} is not hyperbolic ((p-2)(q-2)<=4)" % (p, q))
    return (a + math.sqrt(a * a - 4)) / 2.0


def boundary_fraction(mu):
    """Fraction of vertices on the boundary of a {p,q} ball, persistent at every
    finite radius because |shell_R| / |ball_R| -> (mu-1)/mu as R->inf."""
    return (mu - 1.0) / mu


def meanfield_xy_ratio(q):
    """OPTIMISTIC discrete-clock estimate: plane-rotor Weiss mean-field gives
    kT_c^MF = (z/2) J with z = q. Ratio vs square BKT at matched bare J."""
    kTc_mf_over_J = q / 2.0
    return kTc_mf_over_J / TBKT_SQ_OVER_J


def run():
    out = []
    P = out.append
    P("=" * 78)
    P("H_037 — Bethe-Ceiling Lattice (negative-curvature stiffness ladder)")
    P("cluster: connectivity-geometry universality (Mermin-Wagner fails)")
    P("premise violated: CRYSTALLINE (flat/Euclidean host) -> hyperbolic {p,q}")
    P("=" * 78)

    # --- (A) optimistic discrete-clock mean-field estimate ------------------
    # {7,3}: q=3 vertex degree;  {5,4}: q=4.
    mu_73 = shell_growth_mu(7, 3)
    mu_54 = shell_growth_mu(5, 4)
    fbd_73 = boundary_fraction(mu_73)
    fbd_54 = boundary_fraction(mu_54)
    ratio_mf_73 = meanfield_xy_ratio(3)
    ratio_mf_54 = meanfield_xy_ratio(4)

    P("square XY  T_BKT/J (Tobochnik-Chester)   : %.3f" % TBKT_SQ_OVER_J)
    P("square BKT T_c at the wall band          : %.0f-%.0f K" % (WALL_LO_K, WALL_HI_K))
    P("-" * 78)
    P("(A) OPTIMISTIC discrete-clock mean-field estimate  kT_c^MF=(z/2)J :")
    P("   {7,3} z=3 : MF/BKT ratio = %.3f   (naive escape number)" % ratio_mf_73)
    P("   {5,4} z=4 : MF/BKT ratio = %.3f" % ratio_mf_54)
    P("   -> the DISCRETE clock variable does cross mean-field (arXiv:0801.0836)")

    # --- (B) the boundary-fraction mechanism --------------------------------
    P("-" * 78)
    P("(B) shell growth mu and boundary fraction f_bd=(mu-1)/mu :")
    P("   {7,3} mu = %.6f (= phi^2)   f_bd = %.6f (= 1/phi)" % (mu_73, fbd_73))
    P("   {5,4} mu = %.6f        f_bd = %.6f" % (mu_54, fbd_54))
    P("   -> O(1) of all vertices are on the boundary at EVERY tractable size;")
    P("      a hyperbolic graph is all-boundary, so a 'bulk mean-field' lift is")
    P("      never actually reached -> boundary-dominated finite-size effects.")

    # --- (C) DECISIVE honest-null: continuous U(1) Cooper-pair phase --------
    # The SC order parameter is a CONTINUOUS U(1) phase, not a discrete clock
    # state. The measured literature result for the continuous XY model on a
    # hyperbolic surface is curvature-induced frustration -> a ZERO-T glass with
    # NO finite-T order (Baek-Minnhagen PRE 80 011133 2009; heptagonal-XY MC:
    # absence of any transition incl. BKT). So the realized continuous-phase
    # ordering ratio is NOT the mean-field number; it collapses to <= 1 (no
    # finite-T order => Tc^hyp = 0 in the glassy bulk; at best BKT-like survives).
    continuous_xy_finiteT_order = False    # Baek-Minnhagen: zero-T glass
    realized_ratio = 0.0                   # no finite-T continuous-phase order
    # (0.0 = the honest bulk continuous-XY result; <= NULL_RATIO by a wide margin)

    P("-" * 78)
    P("(C) DECISIVE honest-null — CONTINUOUS U(1) Cooper-pair phase (the real OP):")
    P("   continuous-XY finite-T order on hyperbolic surface : %s"
      % continuous_xy_finiteT_order)
    P("   (Baek-Minnhagen PRE 80 011133 2009: curvature frustration -> zero-T glass;")
    P("    heptagonal-XY open-boundary MC: absence of any transition incl. BKT)")
    P("   realized T_c^hyperbolic / T_c^square (continuous OP): %.3f" % realized_ratio)
    P("   honest-null threshold (escape FAILS if ratio<=1.2)  : %.1f" % NULL_RATIO)

    # --- harness falsifiers -------------------------------------------------
    metrics = {
        "ratio_mf_73": ratio_mf_73,
        "ratio_mf_54": ratio_mf_54,
        "fbd_73": fbd_73,
        "fbd_54": fbd_54,
        "continuous_xy_finiteT_order": continuous_xy_finiteT_order,
        "realized_ratio": realized_ratio,
        "tc_hyp_K": realized_ratio * WALL_LO_K,  # 0 K (no finite-T order)
        "escape_ratio_thresh": ESCAPE_RATIO,
        "null_ratio_thresh": NULL_RATIO,
    }

    falsifiers = [
        # F1: charitable premise check — the DISCRETE mean-field estimate is real
        # (PASS = not triggered; granted, so this PASSes by being a true sub-claim).
        Falsifier(
            "F1_discrete_clock_meanfield_estimate_is_real",
            lambda m: not (m["ratio_mf_73"] >= ESCAPE_RATIO * 0.95),
            "charitable: discrete {7,3} clock model crosses ~mean-field (~1.68x)",
        ),
        # F2 = HONEST-NULL (decisive). Escape REQUIRES the realized continuous-phase
        # ratio to BEAT the null threshold. It does not -> TRIGGER.
        Falsifier(
            "F2_HONEST_NULL_continuous_phase_lifts_bulk_Tc",
            lambda m: not (m["realized_ratio"] > m["null_ratio_thresh"]),
            "honest-null: realized continuous-XY T_c^hyp/T_c^sq > 1.2 (lifts bulk)",
        ),
        # F3: escape's own wall-prediction (ratio >= 1.7) on the REAL order param.
        Falsifier(
            "F3_escape_ratio_ge_1p7_realized",
            lambda m: not (m["realized_ratio"] >= m["escape_ratio_thresh"]),
            "escape: realized T_c^hyp/T_c^sq >= 1.7 at matched J",
        ),
        # F4: does it push the ambient ceiling past the wall band?
        Falsifier(
            "F4_tc_exceeds_wall_band",
            lambda m: not (m["tc_hyp_K"] > WALL_HI_K),
            "escape: hyperbolic T_c > 164 K (clears the frozen ceiling band)",
        ),
        # F5: is the apparent lift bulk, not a boundary/finite-size artifact?
        Falsifier(
            "F5_lift_is_bulk_not_boundary_artifact",
            lambda m: not (m["fbd_73"] < 0.5),
            "escape: boundary fraction < 1/2 so a bulk lift is well-defined",
        ),
    ]

    ledger = evaluate(metrics, falsifiers)
    P("-" * 78)
    for r in ledger["falsifiers"]:
        tag = "TRIGGER" if r["triggered"] else "PASS   "
        P("  [%s] %s" % (tag, r["name"]))
    P("-" * 78)

    honest_null_passes = not ledger["falsifiers"][1]["triggered"]  # F2
    escape_passes = not ledger["falsifiers"][2]["triggered"]       # F3
    verdict = "escapes-wall" if (honest_null_passes and escape_passes) else "confirms-wall"

    P("honest-null (F2) PASS (continuous phase lifts bulk T_c) : %s" % honest_null_passes)
    P("escape (F3) PASS (ratio >= 1.7 realized)                : %s" % escape_passes)
    P("falsifiers_pass : %d/%d" % (ledger["n_pass"], ledger["n_total"]))
    P("is_green        : False")
    P("absorbed        : False")
    P("VERDICT         : %s" % verdict)
    P("=" * 78)

    print("\n".join(out))
    return verdict, ledger["n_pass"], ledger["n_total"]


if __name__ == "__main__":
    run()
