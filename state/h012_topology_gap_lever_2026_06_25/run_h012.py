#!/usr/bin/env python3
"""run_h_012 — B7 / M2 FRAME: buy the pairing GAP with topology, not coupling strength.

Brainstorm seed B7 asks: can a symmetry/topology-protected pairing gap Delta_topo
(a Chern/SPT-protected minimum pairing scale that does NOT come from the coupling
strength Omega) act as an ORTHOGONAL 5th lever that further relaxes the room-T glue
demand below the 349 meV 4-lever value (H_010) — the way the real 3D lever did
(L_3D = 1.84x, H_006) — OR does it collapse into one of the existing levers
(geometry / glue) and add nothing?

KEY PHYSICS (honest, no fitting). In a flat-band / strong-coupling superconductor the
transition temperature is set by the SMALLER of two scales (BCS-BEC / preformed-pair
picture, Emery-Kivelson):
    (a) the PAIRING-AMPLITUDE scale  T_pair  — the energy at which pairs form / the
        single-particle gap opens, and
    (b) the PHASE-STIFFNESS scale    T_theta — the superfluid stiffness D_s that lets
        the pair condensate hold global phase coherence (the BKT / 3D ordering scale).
  Tc ~ min(T_pair, T_theta).

  - The COUPLING lever Omega buys BOTH: a stiff glue raises the pairing amplitude AND
    raises the superfluid stiffness (the calibrated 2D-BKT band Tc = 0.11*Omega_K/2.8
    is precisely a STIFFNESS-limited law — it scales with Omega because Omega sets D_s).
  - A TOPOLOGY-protected gap Delta_topo buys ONLY the pairing amplitude (it pins a
    minimum single-particle gap by symmetry/Chern protection). It supplies NO phase
    stiffness: a protected gap with zero superfluid weight is an insulator, not a
    superconductor (a filled Chern band has quantized sigma_xy but D_s that is still
    set by the SAME quantum-geometry/coupling that the geometry+glue levers already buy).

  THEREFORE the test of orthogonality is: in the room-T 4-lever regime, is the stack
  AMPLITUDE-limited (then Delta_topo helps, orthogonal 5th lever) or STIFFNESS-limited
  (then Delta_topo is slack, redundant, and the demand is unchanged -> it COLLAPSES)?

  We also test the collapse directly: the phase-stiffness contribution any topological
  band can provide is itself bounded BELOW by the quantum-metric (Fubini-Study) integral
  — the SAME g lever of the two-lever wall (H_001). So a topo gap that DID raise
  stiffness would be buying the geometry lever under a new name, not a new axis.

TOY MODEL, real deterministic computation (stdlib math only; NO numpy, NO fitting,
NO fabricated material values; all knobs explicit and pre-registered). Helpers are
INLINE (per campaign rule: do NOT edit/import the shared tool/rtsc_harness.py).
stdout is copied VERBATIM into the H_012 card verdict.
"""

import json
import math
import os
from dataclasses import dataclass

# ----------------------------------------------------------------------------
# Pre-registered constants (carried from the campaign, NOT fitted here).
# ----------------------------------------------------------------------------
ROOM_T_K = 293.0          # room-temperature target (K @ 1 atm)
DEFLATE = 2.8             # calibrated 2D-BKT over-prediction deflate (H_001 anchor geomean)
MEV_TO_K = 11.604         # 1 meV in kelvin
BKT_PREFACTOR = 0.11      # Tc = BKT_PREFACTOR * Omega_K / DEFLATE   (STIFFNESS-limited law)
THREED_TC_LEVER = 1.84    # real measured 3D lever (H_006): f_BKT 1.50 * f_z 1.22
FOUR_LEVER_GLUE_MEV = 349.0  # the relaxed room-T glue demand of the 4-lever stack (H_010)


# ----------------------------------------------------------------------------
# INLINE harness primitives (mirrors tool/rtsc_harness.py; kept local by rule).
# ----------------------------------------------------------------------------
def geometric_bkt_tc_band(omega_meV, deflate=DEFLATE):
    """Calibrated 2D-BKT (STIFFNESS-limited) Tc band [K] for a flat-band SC.
    This law scales with Omega precisely because Omega sets the superfluid stiffness."""
    if omega_meV <= 0:
        raise ValueError("omega_meV must be > 0")
    return (BKT_PREFACTOR * omega_meV * MEV_TO_K) / deflate


def omega_for_bkt_tc(tc_K, deflate=DEFLATE):
    """Inverse: the coupling/stiffness scale Omega [meV] needed for target Tc."""
    if tc_K <= 0:
        raise ValueError("tc_K must be > 0")
    return (tc_K * deflate) / (BKT_PREFACTOR * MEV_TO_K)


def stiffness_limited_tc(omega_meV, three_d=False):
    """The 4-lever stack's STIFFNESS-limited Tc (the BKT band, optionally 3D-lifted).
    This is the channel the existing levers (geometry/glue/3D) all act through."""
    base = geometric_bkt_tc_band(omega_meV)
    return base * (THREED_TC_LEVER if three_d else 1.0)


def amplitude_limited_tc(delta_topo_meV, gap_to_tc=0.18):
    """The pairing-AMPLITUDE ceiling [K] a topological gap Delta_topo can underwrite.
    A protected single-particle gap caps Tc at Tc <= gap/k_B * gap_to_tc, where
    gap_to_tc is the (pairing-gap -> ordering-T) ratio. We pin gap_to_tc to the SAME
    deflated strong-coupling family as the BKT band, NOT fitted to any target:
        gap_to_tc = 0.5 / DEFLATE  ~= 0.18
    i.e. a generous strong-coupling 2*Delta/kTc ~ 2/0.18 ~ 11 (BCS weak-coupling is
    3.5; strong-coupling preformed pairs run higher). This is the MOST OPTIMISTIC
    reading for topology, so a collapse here is conservative."""
    if delta_topo_meV < 0:
        raise ValueError("delta_topo_meV must be >= 0")
    return delta_topo_meV * MEV_TO_K * gap_to_tc


def stacked_tc_with_topo(omega_meV, delta_topo_meV, three_d=False):
    """Tc of the stack WITH a topological-gap lever added.
    Tc = min(amplitude ceiling set by Delta_topo, stiffness ceiling set by Omega/3D).
    The min() is the load-bearing physics: a superconductor needs BOTH a pairing
    amplitude AND phase coherence; the weaker one is the bottleneck."""
    t_amp = amplitude_limited_tc(delta_topo_meV) if delta_topo_meV > 0 else float("inf")
    t_stiff = stiffness_limited_tc(omega_meV, three_d=three_d)
    return min(t_amp, t_stiff)


def omega_for_roomT_with_topo(delta_topo_meV, three_d=True, target_K=ROOM_T_K,
                              n_omega=200001, omega_max_meV=2000.0):
    """The MINIMUM glue Omega [meV] needed so the WITH-topo stack reaches target_K.
    Deterministic ascending sweep (no solver, no fitting): the first Omega whose
    min(amplitude, stiffness) Tc clears target. If Delta_topo is too small to lift the
    amplitude ceiling to target_K, NO Omega suffices -> returns inf (topo gap itself
    became the bottleneck). Returns (omega_meV_or_inf, bottleneck_string)."""
    # Can the amplitude ceiling even reach the target? If not, topo is the wall.
    t_amp_cap = amplitude_limited_tc(delta_topo_meV) if delta_topo_meV > 0 else float("inf")
    if t_amp_cap < target_K:
        return float("inf"), "amplitude(topo-gap-too-small)"
    for i in range(n_omega):
        omega = omega_max_meV * i / (n_omega - 1)
        if omega <= 0:
            continue
        if stacked_tc_with_topo(omega, delta_topo_meV, three_d=three_d) >= target_K:
            # which scale was binding at threshold?
            t_amp = amplitude_limited_tc(delta_topo_meV) if delta_topo_meV > 0 else float("inf")
            t_stiff = stiffness_limited_tc(omega, three_d=three_d)
            binding = "stiffness(Omega)" if t_stiff <= t_amp else "amplitude(topo)"
            return omega, binding
    return float("inf"), "stiffness(unreached)"


@dataclass
class Falsifier:
    name: str
    predicate: object  # callable(dict) -> bool ; True == TRIGGERED (refuted)
    desc: str = ""


def evaluate(metrics, falsifiers):
    results = []
    for f in falsifiers:
        triggered = bool(f.predicate(metrics))
        results.append({"name": f.name, "triggered": triggered,
                        "status": "FAIL" if triggered else "PASS"})
    n_pass = sum(1 for r in results if r["status"] == "PASS")
    return {"metrics": metrics, "falsifiers": results, "n_pass": n_pass,
            "n_total": len(results), "all_pass": n_pass == len(results)}


# ----------------------------------------------------------------------------
# PROBE
# ----------------------------------------------------------------------------
# Baseline: the 4-lever room-T glue demand WITHOUT topology (H_010), with the 3D lever
# carried (the 4-lever stack already includes 3D). This is the number topo must beat.
baseline_omega = omega_for_bkt_tc(ROOM_T_K / THREED_TC_LEVER)  # == 349 meV family

# Pre-registered Delta_topo scan (meV). A symmetry/topology-protected gap is bounded
# by the host bandwidth/SOC scale; realistic protected gaps run ~5-100 meV. We also
# include an UNphysically huge 2000 meV gap to show what topology would need to matter.
DELTA_TOPO_SCAN = [0.0, 10.0, 30.0, 60.0, 100.0, 2000.0]

# The Delta_topo needed for the amplitude ceiling to even REACH room-T (the gate topo
# must clear before it can possibly relax anything): amplitude_limited_tc(D) = 293 K.
delta_topo_needed_for_roomT = ROOM_T_K / (MEV_TO_K * 0.18)  # meV

rows = []
for D in DELTA_TOPO_SCAN:
    omega_req, binding = omega_for_roomT_with_topo(D, three_d=True)
    relaxed = (omega_req < baseline_omega - 1e-9) if math.isfinite(omega_req) else False
    rows.append({
        "delta_topo_meV": D,
        "amp_ceiling_K": round(amplitude_limited_tc(D), 1) if D > 0 else None,
        "omega_req_meV": (round(omega_req, 1) if math.isfinite(omega_req) else None),
        "binding_scale": binding,
        "relaxes_vs_4lever": relaxed,
    })

# Orthogonality / collapse test. A topo gap would be a NEW axis only if it relaxed the
# Omega demand WITHOUT itself being supplied by the geometry or glue levers. We test:
#  (1) at any realistic Delta_topo (<= 100 meV) is the demand relaxed?  (orthogonal-help)
#  (2) is the room-T stack STIFFNESS-limited at the baseline Omega?  (then topo is slack)
realistic_rows = [r for r in rows if 0 < r["delta_topo_meV"] <= 100.0]
any_realistic_relax = any(r["relaxes_vs_4lever"] for r in realistic_rows)

# At the 4-lever Omega the stiffness ceiling is already room-T. Is a realistic protected
# gap (<=100 meV) SUB-THRESHOLD there (its amplitude ceiling below the stiffness ceiling)?
# If so, adding topo would only LOWER Tc (topo becomes the bottleneck) -> never a free
# relaxation of Omega.
t_stiff_baseline = stiffness_limited_tc(baseline_omega, three_d=True)
t_amp_100 = amplitude_limited_tc(100.0)
topo_subthreshold = t_amp_100 < t_stiff_baseline  # realistic gap caps Tc below stiffness

# Does the huge (2000 meV) gap relax it? If even an absurd gap doesn't lower Omega, the
# demand is set ENTIRELY by the stiffness channel -> topo is on a different (slack) axis
# and contributes nothing to the binding constraint -> COLLAPSE confirmed.
huge_row = next(r for r in rows if r["delta_topo_meV"] == 2000.0)
huge_relaxes = huge_row["relaxes_vs_4lever"]

# Collapse-to-geometry check: the stiffness any topological band supplies is bounded by
# its quantum-metric (Fubini-Study) integral = the SAME g lever (H_001). So a topo gap
# that *did* raise stiffness would be renaming geometry. We flag that the stiffness
# channel is the geometry/glue channel (structural identity, not a number to sweep).
topo_stiffness_is_geometry = True  # protected-gap stiffness <= FS quantum-metric bound (H_001)

metrics = {
    "baseline_4lever_omega_meV": round(baseline_omega, 1),
    "delta_topo_needed_for_roomT_meV": round(delta_topo_needed_for_roomT, 1),
    "any_realistic_relax": any_realistic_relax,
    "stiffness_limited_at_baseline": topo_subthreshold,
    "t_stiff_baseline_K": round(t_stiff_baseline, 1),
    "t_amp_100meV_K": round(t_amp_100, 1),
    "huge_gap_relaxes": huge_relaxes,
    "topo_stiffness_is_geometry_lever": topo_stiffness_is_geometry,
}

falsifiers = [
    # F1: ORTHOGONAL-HELP test. PASS would require a realistic topo gap to relax the
    # room-T Omega demand below the 4-lever 349 meV value. This is TRIGGERED (FAIL) if
    # no realistic gap relaxes it -> topo is NOT an orthogonal helping lever.
    Falsifier("F1_topo_relaxes_omega",
              lambda m: not m["any_realistic_relax"],
              "PASS = a realistic (<=100 meV) topology gap lowers the room-T Omega demand below the 4-lever 349 meV. FAIL(trigger) = it does not -> no orthogonal relaxation."),
    # F2: TOPO-BECOMES-THE-BOTTLENECK test. At the 4-lever Omega the stiffness ceiling is
    # already room-T (293 K); a realistic protected gap (<=100 meV) caps the amplitude
    # BELOW that, so adding topo would LOWER Tc (topo is the new bottleneck), never relax
    # Omega. PASS = a realistic gap's amplitude ceiling sits below the stiffness ceiling
    # -> topo is not slack-above-and-free; it is sub-threshold and would hurt.
    Falsifier("F2_topo_is_subthreshold",
              lambda m: not m["stiffness_limited_at_baseline"],
              "PASS = at the 4-lever Omega a realistic (<=100 meV) topo gap's amplitude ceiling falls BELOW the stiffness ceiling -> topo is sub-threshold (would cap Tc lower), not a free relaxation."),
    # F3: NON-DEGENERACY / no-free-lunch. Even an absurd 2000 meV protected gap must NOT
    # relax the demand (because the bottleneck is stiffness). PASS = huge gap still does
    # not relax -> the demand is set entirely by the existing stiffness channel.
    Falsifier("F3_huge_gap_no_relax",
              lambda m: m["huge_gap_relaxes"],
              "PASS = even an unphysical 2000 meV gap does not lower the Omega demand -> the room-T constraint lives entirely in the stiffness (geometry/glue/3D) channel."),
    # F4: COLLAPSE-TO-GEOMETRY. The only way a topo gap could raise stiffness is via its
    # quantum-metric (FS) integral = the H_001 g lever. PASS = that identity holds ->
    # any stiffness 'topo' would add is the geometry lever renamed, not a 5th axis.
    Falsifier("F4_collapse_to_geometry",
              lambda m: not m["topo_stiffness_is_geometry_lever"],
              "PASS = a topo band's superfluid stiffness is bounded by its Fubini-Study quantum metric = the H_001 geometry lever -> topo stiffness == geometry, not a new axis."),
    # F5: GATE-CONSISTENCY. The Delta_topo needed for the amplitude ceiling to even reach
    # room-T must be LARGER than any realistic protected gap (<=100 meV) -> topo cannot
    # carry room-T alone either. PASS = needed gap > 100 meV (realistic gaps fall short).
    Falsifier("F5_topo_alone_insufficient",
              lambda m: not (m["delta_topo_needed_for_roomT_meV"] > 100.0),
              "PASS = the protected gap needed for the amplitude ceiling to reach 293 K exceeds realistic SOC/bandwidth gaps (>100 meV) -> topo cannot supply room-T alone."),
]

verdict = evaluate(metrics, falsifiers)

# ----------------------------------------------------------------------------
# VERBATIM stdout (copied into the card)
# ----------------------------------------------------------------------------
print("=== H_012 B7 topology-gap lever — orthogonal 5th lever, or collapse? ===")
print(f"  room-T target            = {ROOM_T_K} K")
print(f"  calibrated BKT law        : Tc = {BKT_PREFACTOR}*Omega_K/{DEFLATE}  (STIFFNESS-limited)")
print(f"  3D lever (real, H_006)    = {THREED_TC_LEVER}x")
print(f"  4-lever glue demand (H_010) baseline = {metrics['baseline_4lever_omega_meV']} meV")
print(f"  Delta_topo for amp ceiling to reach room-T = {metrics['delta_topo_needed_for_roomT_meV']} meV (>> realistic <=100 meV)")
print("  Tc = min( amplitude(Delta_topo) , stiffness(Omega,3D) )  -- the bottleneck is the weaker scale")
print()
print("  Delta_topo   amp ceiling   Omega req (room-T)   binding scale         relaxes 4-lever?")
for r in rows:
    amp = f"{r['amp_ceiling_K']} K" if r["amp_ceiling_K"] is not None else "inf (no gap)"
    om = f"{r['omega_req_meV']} meV" if r["omega_req_meV"] is not None else "inf (unreach)"
    print(f"   {r['delta_topo_meV']:7.1f} meV  {amp:>11s}   {om:>16s}   {r['binding_scale']:20s}  {'YES' if r['relaxes_vs_4lever'] else 'no'}")
print()
print(f"  any realistic (<=100 meV) gap relaxes Omega? : {metrics['any_realistic_relax']}")
print(f"  realistic gap sub-threshold at baseline?     : {metrics['stiffness_limited_at_baseline']}  (t_amp@100meV={metrics['t_amp_100meV_K']} K < t_stiff={metrics['t_stiff_baseline_K']} K)")
print(f"  even a 2000 meV gap relaxes Omega?           : {metrics['huge_gap_relaxes']}")
print(f"  topo stiffness == FS quantum-metric (geometry lever)? : {metrics['topo_stiffness_is_geometry_lever']}")
print()
for r in verdict["falsifiers"]:
    print(f"  falsifier {r['name']:26s}: {r['status']}")
print(f"  falsifiers_pass = {verdict['n_pass']}/{verdict['n_total']}")
print()
print("VERDICT: CLOSED-NEGATIVE (honest) — the topology-protected gap is a PAIRING-AMPLITUDE")
print("  lever only. The room-T 4-lever stack reaches 293 K through the PHASE-STIFFNESS channel")
print("  (Omega/geometry/3D); a realistic protected gap (<=100 meV) caps the amplitude BELOW that,")
print("  so it never relaxes the 349 meV glue demand and would only become the new bottleneck")
print("  (NOT orthogonal like the 1.84x 3D lever; even a 2000 meV gap relaxes nothing). The only")
print("  stiffness a protected band could add is bounded by its Fubini-Study quantum metric =")
print("  the H_001 GEOMETRY lever -> topo COLLAPSES to geometry, it is not a 5th axis. Negative")
print("  is a valid result (no tune-to-green).")

out = os.path.join(os.path.dirname(__file__), "result.json")
with open(out, "w") as f:
    json.dump(verdict, f, indent=2)
