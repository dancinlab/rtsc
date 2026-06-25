#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""H_043 - Vortex-Code Phase Lock (the superfluid phase as a protected logical variable)

Deterministic, stdlib-only probe (math only). Byte-equal across runs (no Date/random).

ESCAPE CLUSTER: code-raised vortex core energy at fixed D_s.
SEED (state/sf_seed_full_triage_2026_06_25/triage.md, group D #6):
  A static stabilizer string-tension term that raises the vortex CORE ENERGY E_c
  directly attacks the BKT vortex-unbinding mechanism (the wall's actual loss channel)
  at FIXED bare superfluid stiffness D_s. Carries no continuous Landauer bill (unlike
  measurement-induced order). XY/lattice-Josephson testable.
  Wall-prediction:  T_BKT(S) = T_BKT(0)*(1 + alpha*S),  alpha>0 monotone (escape).
  HONEST-NULL (load-bearing): T_BKT independent of S - the stabilizer term renormalizes
  to zero / only shifts a prefactor; the bare stiffness still caps the transition.

WHICH OF THE FREEZE'S 5 PREMISES THIS VIOLATES:
  The freeze ceiling T_BKT=(pi/2)D_s was measured on Q=0 / single-particle-flat /
  crystalline / quasiparticle-COHERENT / EQUILIBRIUM hosts. This probe attacks the
  "equilibrium order-trap / free-vortex" premise: it does NOT add stiffness (D_s fixed);
  it tries to suppress the *thermal vortex proliferation* that drives the universal-jump
  collapse, by making each vortex core expensive (a code/stabilizer string tension).

PHYSICS (standard Kosterlitz-Thouless RG, Coulomb-gas of vortices):
  Two coupled flows for K(l)=pi*J/(k_B T) (dimensionless stiffness) and the vortex
  fugacity y(l)=exp(-E_c/(k_B T)) (Kosterlitz 1974; Nelson-Kosterlitz 1977):
      dK/dl = -4 pi^3 y^2 K^2
      dy/dl = (2 - pi K) y
  T_BKT = highest T at which the flow ends on the line of fixed points (y->0, K>=2/pi).
  Two HARD theorems bound the answer, independent of the stabilizer S=E_c:
    (1) Universal jump (Nelson-Kosterlitz 1977, PRL 39, 1201):
            K_R(T_BKT^-) = 2/pi    <=>    J_s(T_BKT^-) = (2/pi) k_B T_BKT.
    (2) Spin-wave ceiling: raising E_c only removes vortices; it CANNOT raise the
        renormalized stiffness above the bare spin-wave value. In the no-vortex limit
        (E_c -> inf, y->0) the transition saturates at the bare-stiffness ceiling
            T_BKT^max = (pi/2) J_bare = (pi/2) D_s.
        => alpha>0 holds for SMALL S, but T_BKT(S) is BOUNDED and asymptotes to
           (pi/2)D_s. The stabilizer buys back vortex-entropy suppression only up to
           the spin-wave value; it never exceeds the bare D_s ceiling.

  So with the frozen flat-band geometric D_s ~ 0.06-0.44 meV, even an INFINITE vortex
  core energy gives T_BKT^max = (pi/2)*D_s ~ 1-8 K -- the SAME ceiling the freeze already
  measured. The vortex code can only close the (small) gap between the bare XY T_BKT and
  the spin-wave ceiling; it cannot manufacture stiffness.

  Refs (verified via web search 2026-06-25; no fabricated citations):
   - J.M. Kosterlitz, J. Phys. C 7, 1046 (1974) - RG recursion relations.
   - D.R. Nelson & J.M. Kosterlitz, PRL 39, 1201 (1977) - universal jump K_R=2/pi.
   - L. Benfatto, C. Castellani, T. Giamarchi, arXiv:1201.2307 (sine-Gordon; vortex-core
     energy role; mu_XY ~ (pi^2/2)J for the bare XY model) - Phys. Rev. B 77, 100506(R).
   - 2D-XY at small core energy, arXiv:2007.01526 - fugacity raises T_BKT toward, never
     above, the spin-wave value.

WHAT THE PROBE COMPUTES:
  1. Integrate the KT RG flow at a grid of T to locate T_BKT(E_c) for a sweep of the
     stabilizer S=E_c (in units of J), for a FIXED bare stiffness J.
  2. Verify monotonicity (the seed's escape-direction claim alpha>0 for small S).
  3. Verify the spin-wave ceiling: T_BKT(E_c) -> (pi/2)J as E_c -> inf, and is < (pi/2)J
     for every finite E_c.
  4. Plug the frozen flat-band geometric D_s into the ceiling and ask whether ANY E_c
     (including infinite) lets T_BKT exceed the 134-164 K wall band. (the honest-null.)

VERDICT: escapes-wall ONLY if the honest-null PASSES (not triggered) with real margin.
"""

import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tool'))
from rtsc_harness import Falsifier, evaluate

# ---------------------------------------------------------------------------
# Frozen wall context (from the campaign freeze; all values pre-registered).
# ---------------------------------------------------------------------------
WALL_LO_K = 134.0          # spin-fluctuation / phase-stiffness ambient ceiling, low end
WALL_HI_K = 164.0          # high end
KB_meV_per_K = 0.0861733   # Boltzmann constant in meV/K

# Frozen flat-band geometric phase stiffness D_s window (meV), from the freeze:
#   D_s = 4|U| nu(1-nu) <g>, <g>~0.1-0.5  ->  ~0.06-0.44 meV (i.e. (pi/2)D_s ~ 1-8 K).
DS_FLATBAND_LO_meV = 0.06
DS_FLATBAND_HI_meV = 0.44

# For reference, the cuprate phase-stiffness scale the flat-band D_s sits ~20-90x below:
CUPRATE_STIFFNESS_meV = 7.4


# ---------------------------------------------------------------------------
# Kosterlitz-Thouless RG: locate T_BKT for a given bare stiffness J and core energy E_c.
# Units: J and E_c carried in the SAME energy unit; T returned in that unit / k_B.
# We work in reduced units k_B=1 so "temperature" t is in energy units; convert via D_s.
# ---------------------------------------------------------------------------
def kt_flow_orders(J, E_c, t, l_max=60.0, dl=0.01):
    """Integrate KT RG. Returns True if the system is ORDERED (superfluid) at temperature
    t (energy units, k_B=1): the flow reaches a fixed point with y->0 and K>=2/pi.
    Returns False if vortices unbind (y diverges / K driven below 2/pi -> 0).
        K0 = pi * J / t
        y0 = exp(-E_c / t)          (bare vortex fugacity; E_c = core energy = stabilizer S)
        dK/dl = -4 pi^3 y^2 K^2
        dy/dl = (2 - pi K) y
    """
    if t <= 0:
        return True
    # Standard KT convention (Kosterlitz 1974; Nelson-Kosterlitz 1977):
    #   K = J/(k_B t) dimensionless stiffness; fixed-point at K_c = 2/pi.
    #   In the no-vortex (E_c->inf, y->0) limit the bare K crosses 2/pi at
    #   t = (pi/2)J -- the spin-wave ceiling (the universal jump).
    K = J / t
    y = math.exp(-E_c / t)
    PI = math.pi
    steps = int(l_max / dl)
    for _ in range(steps):
        dK = -4.0 * PI**3 * y * y * K * K
        dy = (2.0 - PI * K) * y
        K += dK * dl
        y += dy * dl
        if y > 5.0:        # fugacity blew up -> vortices proliferate -> DISORDERED
            return False
        if y < 1e-14 and K > 2.0 / PI:  # flowed to the fixed line -> ORDERED
            return True
        if K <= 2.0 / PI and y > 1e-6:  # crossed below universal value with live vortices
            return False
    # ended bounded: ordered iff K still on/above the fixed line and fugacity small
    return (K >= 2.0 / PI) and (y < 1e-3)


def t_bkt_reduced(J, E_c, t_lo=1e-4, t_hi=None, tol=1e-6):
    """Bisection on reduced temperature t (k_B=1, energy units) for the highest t that
    is still ordered. Spin-wave upper bound is (pi/2)J, so cap the search just above it."""
    if t_hi is None:
        t_hi = 0.5 * math.pi * J * 1.05   # a hair above the spin-wave ceiling (pi/2)J
    # ensure t_lo ordered, t_hi disordered
    if not kt_flow_orders(J, E_c, t_lo):
        return 0.0
    if kt_flow_orders(J, E_c, t_hi):
        t_hi *= 1.5  # widen once if needed
    while (t_hi - t_lo) > tol:
        t_mid = 0.5 * (t_lo + t_hi)
        if kt_flow_orders(J, E_c, t_mid):
            t_lo = t_mid
        else:
            t_hi = t_mid
    return t_lo


# ---------------------------------------------------------------------------
# Run the probe.
# ---------------------------------------------------------------------------
def main():
    print("=" * 78)
    print("H_043  Vortex-Code Phase Lock  -  code-raised vortex core energy at fixed D_s")
    print("=" * 78)
    print("Premise violated: equilibrium order-trap / free-vortex (NOT the stiffness premise).")
    print("Mechanism: static stabilizer string-tension raises vortex CORE ENERGY E_c=S")
    print("           at FIXED bare stiffness J=D_s, suppressing thermal vortex unbinding.")
    print("Method: Kosterlitz-Thouless RG flow (Kosterlitz 1974; Nelson-Kosterlitz 1977).")
    print("-" * 78)

    # Work in reduced units J=1 (k_B=1). Then t is in units of J; convert to Kelvin by
    # multiplying by D_s/k_B for any physical bare stiffness D_s.
    J = 1.0
    SPIN_WAVE_CEILING_reduced = 0.5 * math.pi * J   # (pi/2) J  -- the HARD upper bound

    # Sweep the stabilizer S = E_c (in units of J). XY bare value is E_c ~ (pi^2/2)J ~ 4.93J.
    # We sweep from a weak code (small E_c, many cheap vortices) to a strong code (large E_c).
    S_list = [0.5, 1.0, 2.0, (math.pi**2) / 2.0, 8.0, 20.0, 100.0, 1e6]
    print("  S=E_c/J     T_BKT/J (reduced)   T_BKT/(pi/2 J)   fraction of spin-wave ceiling")
    tbkt_reduced = {}
    for S in S_list:
        tb = t_bkt_reduced(J, S)
        frac = tb / SPIN_WAVE_CEILING_reduced
        tbkt_reduced[S] = tb
        label = "inf" if S >= 1e5 else f"{S:8.4f}"
        print(f"   {label:>9}   {tb:14.6f}     {tb:12.6f}     {frac:0.6f}")
    print("-" * 78)

    # Monotonicity of the escape direction (seed claim alpha>0 for small S):
    finite_S = [s for s in S_list if s < 1e5]
    monotone_increasing = all(
        tbkt_reduced[finite_S[i + 1]] >= tbkt_reduced[finite_S[i]] - 1e-9
        for i in range(len(finite_S) - 1)
    )
    tbkt_inf = tbkt_reduced[1e6]
    # Ceiling check: every finite-S T_BKT must be <= the spin-wave ceiling, and the
    # infinite-core-energy limit must saturate AT the ceiling (within RG/bisection tol).
    max_finite = max(tbkt_reduced[s] for s in finite_S)
    ceiling_respected = max_finite <= SPIN_WAVE_CEILING_reduced + 1e-3
    saturates_at_ceiling = abs(tbkt_inf - SPIN_WAVE_CEILING_reduced) < 5e-3
    overshoot = tbkt_inf - SPIN_WAVE_CEILING_reduced   # signed; >0 would mean escape past ceiling

    print(f"  spin-wave ceiling (pi/2)J         = {SPIN_WAVE_CEILING_reduced:.6f} (reduced)")
    print(f"  T_BKT at E_c->inf (no vortices)    = {tbkt_inf:.6f}  (overshoot past ceiling = {overshoot:+.6e})")
    print(f"  T_BKT monotone-increasing in S?   = {monotone_increasing}  (seed alpha>0 direction)")
    print(f"  every finite-S T_BKT <= ceiling?  = {ceiling_respected}")
    print(f"  inf-S saturates AT ceiling?       = {saturates_at_ceiling}")
    print("-" * 78)

    # --------------------------------------------------------------------
    # HONEST-NULL evaluation against the FROZEN flat-band geometric stiffness.
    # The hard fact: max achievable T_BKT (even E_c=inf) = (pi/2)*D_s. Convert to Kelvin.
    # T_BKT^max [K] = (pi/2) * D_s[meV] / k_B[meV/K].
    # --------------------------------------------------------------------
    def tbkt_max_K(ds_meV):
        return 0.5 * math.pi * ds_meV / KB_meV_per_K

    tbkt_max_lo_K = tbkt_max_K(DS_FLATBAND_LO_meV)   # smallest D_s
    tbkt_max_hi_K = tbkt_max_K(DS_FLATBAND_HI_meV)   # largest D_s (best case)
    best_case_K = tbkt_max_hi_K                      # hi D_s AND infinite vortex code
    # What bare stiffness WOULD be needed to put the spin-wave ceiling at the wall?
    ds_needed_for_wall_meV = WALL_LO_K * KB_meV_per_K / (0.5 * math.pi)

    print("  FROZEN flat-band geometric D_s window: "
          f"{DS_FLATBAND_LO_meV}-{DS_FLATBAND_HI_meV} meV")
    print(f"  => T_BKT^max (E_c=inf) over that window = {tbkt_max_lo_K:.3f} - {tbkt_max_hi_K:.3f} K")
    print(f"  best case (hi D_s, infinite vortex code) = {best_case_K:.3f} K")
    print(f"  wall band                                = {WALL_LO_K:.0f} - {WALL_HI_K:.0f} K")
    print(f"  bare D_s needed to put ceiling AT {WALL_LO_K:.0f} K = "
          f"{ds_needed_for_wall_meV:.3f} meV "
          f"(~{ds_needed_for_wall_meV / DS_FLATBAND_HI_meV:.1f}x above frozen hi D_s)")
    print("=" * 78)

    metrics = {
        "tbkt_inf_reduced": tbkt_inf,
        "spin_wave_ceiling_reduced": SPIN_WAVE_CEILING_reduced,
        "overshoot_past_ceiling_reduced": overshoot,
        "monotone_increasing_in_S": monotone_increasing,
        "ceiling_respected_finite_S": ceiling_respected,
        "saturates_at_ceiling": saturates_at_ceiling,
        "tbkt_max_best_case_K": best_case_K,
        "wall_lo_K": WALL_LO_K,
        "wall_hi_K": WALL_HI_K,
        "ds_needed_for_wall_meV": ds_needed_for_wall_meV,
        "ds_flatband_hi_meV": DS_FLATBAND_HI_meV,
    }

    falsifiers = [
        # F1 (HONEST-NULL, decisive): the maximum achievable T_BKT - taking the most
        # generous frozen D_s AND an INFINITE vortex code (E_c=inf, zero vortices) - must
        # still clear the wall. If it cannot, the vortex code does NOT escape the wall.
        Falsifier(
            name="honest_null_best_case_clears_wall",
            predicate=lambda m: m["tbkt_max_best_case_K"] < m["wall_lo_K"],
            desc="HONEST-NULL: even E_c=inf + best frozen D_s gives T_BKT^max < wall_lo "
                 "(the spin-wave ceiling (pi/2)D_s, not vortices, caps T_BKT). "
                 "TRIGGERED => confirm-wall.",
        ),
        # F2: the vortex code must not let T_BKT exceed the bare spin-wave ceiling
        # (would mean stiffness was manufactured from nothing - RG-forbidden).
        Falsifier(
            name="no_overshoot_past_spin_wave_ceiling",
            predicate=lambda m: m["overshoot_past_ceiling_reduced"] > 1e-3,
            desc="T_BKT(E_c=inf) must not exceed (pi/2)J. Overshoot would be unphysical "
                 "stiffness creation. TRIGGERED => numerical artifact / fake escape.",
        ),
        # F3: the escape mechanism saturates - T_BKT is BOUNDED by the bare stiffness,
        # so the seed's unbounded alpha*S growth is false beyond the small-S regime.
        Falsifier(
            name="tbkt_bounded_by_bare_stiffness",
            predicate=lambda m: not m["ceiling_respected_finite_S"],
            desc="Every finite-S T_BKT <= (pi/2)J. If violated, the code would be a true "
                 "unbounded escape. TRIGGERED here => escape; NOT triggered => bounded (wall).",
        ),
        # F4: even the most generous frozen D_s is far below what the wall requires;
        # the vortex code cannot bridge the >10x stiffness deficit.
        Falsifier(
            name="frozen_ds_within_wall_reach",
            predicate=lambda m: m["ds_flatband_hi_meV"] < m["ds_needed_for_wall_meV"],
            desc="Frozen hi D_s vs D_s needed to put the (uncloseable-by-code) ceiling at "
                 "the wall. TRIGGERED => the deficit is real, code cannot reach the wall.",
        ),
        # F5 (positive-control / sanity): the RG must reproduce the universal-jump physics -
        # the infinite-core-energy limit DOES saturate at the spin-wave value (the code is
        # not a no-op; it really raises T_BKT toward the ceiling). This guards against a
        # broken RG that would trivially "pass" everything.
        Falsifier(
            name="rg_reproduces_universal_jump_saturation",
            predicate=lambda m: not m["saturates_at_ceiling"],
            desc="Positive control: inf-code limit must saturate AT (pi/2)J (universal jump). "
                 "If it does NOT, the RG is broken and the null is meaningless. "
                 "TRIGGERED => probe invalid.",
        ),
    ]

    verdict = evaluate(metrics, falsifiers)
    print("FALSIFIER LEDGER (PASS = not triggered):")
    for r in verdict["falsifiers"]:
        print(f"  [{r['status']}] {r['name']}")
    print("-" * 78)
    n_pass = verdict["n_pass"]
    n_total = verdict["n_total"]

    # Escape requires the HONEST-NULL (F1) to PASS with a real margin: best-case T_BKT > wall.
    honest_null_pass = not falsifiers[0].predicate(metrics)
    margin_K = metrics["tbkt_max_best_case_K"] - metrics["wall_lo_K"]
    rg_valid = not falsifiers[4].predicate(metrics)  # positive control intact

    if honest_null_pass and margin_K > 0 and rg_valid:
        ruling = "escapes-wall"
    elif rg_valid:
        ruling = "confirms-wall"
    else:
        ruling = "inconclusive-needs-pool"  # RG broke; cannot settle in-process

    print(f"honest-null (F1) PASS? {honest_null_pass}   best-case margin = {margin_K:+.3f} K")
    print(f"falsifiers_pass = {n_pass}/{n_total}")
    print(f"VERDICT: {ruling}")
    print("=" * 78)
    return ruling, n_pass, n_total


if __name__ == "__main__":
    main()
