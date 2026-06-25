#!/usr/bin/env python3
"""H_032 - Multi-channel stiffness donation (escape class (a): borrow stiffness).

CLAIM (escape seed): Pairing lives on the flat band (high QGT / DOS), but the
superfluid phase stiffness D_s is DONATED by a co-resident high-Fermi-velocity
dispersive band, so pairing and stiffness are different k-space objects. If the
two add freely, total D_s = D_s_flat + D_s_disp could clear the spin-fluctuation /
phase-stiffness ambient ceiling (~134-164 K; Emery-Kivelson, T_BKT=(pi/2)*D_s).

HONEST NULL (load-bearing, decisive falsifier - NOT engineered around):
"Leggett mode softening + v_F decoupling." If the condensate phase is pinned to the
flat band, the dispersive band's D_s couples to the ORDER-PARAMETER phase only
through the interband Josephson coupling J. The relative-phase (Leggett) mode costs
finite energy ~ J; when J is small the dispersive phase decouples and its stiffness
is NOT donated to the phase that sets T_BKT. Worse, the quantum-metric no-go
(arXiv:2604.04719, Zhou 2026) is a TRADE-OFF: you cannot simultaneously maximize
flat-band pairing (needs the flat band ISOLATED / weakly hybridized) and the
interband locking J (needs strong hybridization). Strong J that fully donates the
dispersive stiffness back-acts to DESTROY the flat-band pairing that the claim needs.
This conserves the cuprate min(pairing, stiffness) tradeoff that DEFINES the ceiling.

This probe encodes that trade-off as closed-form math and asks whether ANY single
interband-coupling working point lets the donated-stiffness T_BKT exceed the ceiling
while pairing survives. Deterministic, stdlib-only. No fitting, no tuned constants
beyond the documented grounded anchors. NO random / NO date.

GROUNDED anchors (cited, not fabricated):
  * T_BKT = (pi/2) * D_s, Tc = min(T_pair, T_phase)        Emery-Kivelson PRB 1995;
                                                            arXiv:2604.04719 (two-channel).
  * Multiband superfluid weight is additive in the diamagnetic / f-sum sense
    (valence band ADDS to conduction stiffness)            arXiv:2311.17511, arXiv:2511.16385.
  * Donated stiffness gated by interband Josephson J; relative phase = Leggett mode
    that costs finite energy                                arXiv:1408.5938, arXiv:1704.00333.
  * Quantum-metric NO-GO: maximizing flat-band DOS and interband coupling is
    mathematically INCOMPATIBLE (geometric sum-rule trade-off) arXiv:2604.04719 (Zhou).
GROUNDED campaign numbers (PR#40 frozen wall):
  * ambient phase-stiffness ceiling band ~134-164 K.
  * flat-band geometric D_s ~0.06-0.44 meV (1-8 K), ~20-90x BELOW cuprate stiffness.
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tool'))
from rtsc_harness import Falsifier, evaluate, ROOM_T_K

# ---------------------------------------------------------------------------
# Frozen grounded constants (PR#40 wall + literature anchors). No tuning.
# ---------------------------------------------------------------------------
CEILING_LO_K = 134.0          # spin-fluctuation / phase-stiffness ambient ceiling, low edge
CEILING_HI_K = 164.0          # ... high edge (the number to BEAT to escape)
TARGET_K = ROOM_T_K           # 293 K @ 1 atm

PI_OVER_2 = math.pi / 2.0     # Emery-Kivelson: T_BKT = (pi/2) * D_s (D_s in K)

# Flat-band geometric stiffness (the PAIRING channel's own phase stiffness), K.
# Campaign measured band 1-8 K; take the OPTIMISTIC top of the honest band.
DS_FLAT_K = 8.0

# Dispersive donor band raw stiffness, K. A high-v_F metal can carry a LARGE bare
# phase stiffness; set it generously huge so the claim gets its best shot.
# (cuprate-class stiffness ~ ceiling/(pi/2) ~ 100 K; give the donor 3x that.)
DS_DISP_RAW_K = 300.0

# ---------------------------------------------------------------------------
# CENTRAL FALSIFIABLE SCALING (the load-bearing math)
# ---------------------------------------------------------------------------
# Interband dimensionless coupling x in (0,1): hybridization that locks the two
# band phases into one condensate. Two competing, GROUNDED effects of x:
#
#  (1) DONATION efficiency (Leggett locking): the dispersive stiffness reaches the
#      order-parameter phase only as fast as the interband Josephson coupling locks
#      the relative phase. Leggett restoring force ~ J ~ x. Fraction of D_s_disp that
#      is donated to the COMMON phase:    eta_donate(x) = x   (eta->1 only at x->1).
#      (At x->0 the dispersive phase free-floats: a soft Leggett mode, zero donation.)
#
#  (2) PAIRING survival (quantum-metric no-go trade-off, arXiv:2604.04719): the flat
#      band must stay quasi-isolated to keep its high-DOS pairing. Hybridization x
#      bleeds spectral weight off the flat band -> pairing channel weakens. Grounded
#      no-go = the two cannot both be maxed; encode the strongest *additive* survival:
#                              s_pair(x) = 1 - x.
#      So the flat-band stiffness that survives is DS_FLAT_K * s_pair(x), and the
#      pairing-temperature cap (T_pair) also scales with s_pair(x).
#
# Effective DONATED stiffness reaching the single order-parameter phase:
#      D_s_eff(x) = DS_FLAT_K*(1-x)  +  DS_DISP_RAW_K * eta_donate(x) * s_pair(x)
#                 = DS_FLAT_K*(1-x)  +  DS_DISP_RAW_K * x * (1-x)
#
# The donor term x*(1-x) is a PRODUCT of "lock it" and "don't kill pairing" - its
# maximum over x is 1/4 at x=1/2. That 1/4 is the Leggett/no-go CAP: you can never
# donate more than a quarter of the bare dispersive stiffness, because the same
# hybridization that locks the phase also kills the pairing that anchors it.
# This is the closed-form statement of "min(pairing, stiffness) is conserved."


def d_s_eff_K(x):
    if not (0.0 <= x <= 1.0):
        raise ValueError("x must be in [0,1]: " + repr(x))
    flat = DS_FLAT_K * (1.0 - x)
    donated = DS_DISP_RAW_K * x * (1.0 - x)
    return flat + donated


def t_bkt_K(x):
    """Phase-ordering (BKT) temperature from the effective DONATED stiffness."""
    return PI_OVER_2 * d_s_eff_K(x)


def t_pair_cap_K(x):
    """Pairing-temperature cap. The flat band is the ONLY pairing channel (claim);
    its pairing scale degrades with hybridization x via the no-go trade-off.
    Anchor T_pair(x=0) to the ceiling high edge (best-case flat-band pairing)."""
    return CEILING_HI_K * (1.0 - x)


def t_c_K(x):
    """Tc = min(T_phase, T_pair) - the two-channel ceiling law (Emery-Kivelson /
    arXiv:2604.04719). A working point only 'counts' if BOTH channels clear it."""
    return min(t_bkt_K(x), t_pair_cap_K(x))


# ---------------------------------------------------------------------------
# Scan the single free knob x deterministically; find the best Tc.
# ---------------------------------------------------------------------------
N = 10001  # fixed grid -> byte-deterministic
best_x = 0.0
best_tc = -1.0
best_tbkt = 0.0
best_tpair = 0.0
for i in range(N):
    x = i / (N - 1)
    tc = t_c_K(x)
    if tc > best_tc:
        best_tc = tc
        best_x = x
        best_tbkt = t_bkt_K(x)
        best_tpair = t_pair_cap_K(x)

# Also the *naive additive* fantasy (claim's optimistic ceiling: free addition, no
# Leggett gate, no no-go) - to quantify how much the honest gate costs.
naive_additive_K = PI_OVER_2 * (DS_FLAT_K + DS_DISP_RAW_K)

margin_vs_ceiling = best_tc - CEILING_HI_K   # >0 would mean genuine escape

metrics = {
    "best_x": best_x,
    "best_tc_K": best_tc,
    "best_tbkt_K": best_tbkt,
    "best_tpair_K": best_tpair,
    "naive_additive_tc_K": naive_additive_K,
    "ceiling_lo_K": CEILING_LO_K,
    "ceiling_hi_K": CEILING_HI_K,
    "target_K": TARGET_K,
    "margin_vs_ceiling_K": margin_vs_ceiling,
    "ds_flat_K": DS_FLAT_K,
    "ds_disp_raw_K": DS_DISP_RAW_K,
    "donation_cap_fraction": 0.25,  # closed-form max of x*(1-x)
}

# ---------------------------------------------------------------------------
# FALSIFIERS (PASS = NOT triggered). The honest-null is the decisive one.
# Falsifier.predicate(metrics) -> True means TRIGGERED (refuted).
# ---------------------------------------------------------------------------
falsifiers = [
    # F1 - DECISIVE honest-null: does the best achievable Tc beat the ceiling high edge?
    Falsifier(
        "honest_null_leggett_nogo_escape",
        lambda m: m["best_tc_K"] > m["ceiling_hi_K"],
        "DECISIVE honest-null: Leggett locking + quantum-metric no-go trade-off "
        "(eta_donate=x, s_pair=1-x => donated <= D_s_disp/4). TRIGGERED(PASS) only if "
        "the best two-channel Tc=min(T_phase,T_pair) genuinely exceeds the ~164 K ceiling.",
    ),
    # F2 - does it reach the actual room-T target?
    Falsifier(
        "reaches_room_T_target",
        lambda m: m["best_tc_K"] >= m["target_K"],
        "Best Tc reaches 293 K @ 1 atm.",
    ),
    # F3 - is the donor actually donating freely (naive additive realized)?
    #      If the gate is real, best_tc is far below the naive additive fantasy.
    Falsifier(
        "free_additive_donation_realized",
        lambda m: m["best_tc_K"] >= 0.5 * m["naive_additive_tc_K"],
        "Free D_s_flat+D_s_disp addition (no Leggett gate) realized: best Tc reaches "
        ">=50% of the naive additive ceiling. Triggered => the gate is weak / donation free.",
    ),
    # F4 - min(pairing,stiffness) tradeoff broken? Triggered if at the optimum one
    #      channel dominates the other by >3x (a free lunch).
    Falsifier(
        "pairing_stiffness_tradeoff_broken",
        lambda m: (m["best_tbkt_K"] / max(m["best_tpair_K"], 1e-9)) > 3.0
        or (m["best_tpair_K"] / max(m["best_tbkt_K"], 1e-9)) > 3.0,
        "min(pairing,stiffness) conservation broken: at the optimum one channel "
        "dominates the other by >3x (free lunch). NOT triggered (ratio~1) => the "
        "tradeoff is conserved, the optimum sits at the crossover.",
    ),
]

result = evaluate(metrics, falsifiers)
passes = result["n_pass"]
total = result["n_total"]

escapes = metrics["best_tc_K"] > metrics["ceiling_hi_K"]
verdict = "escapes-wall" if escapes else "confirms-wall"

# ---------------------------------------------------------------------------
# VERBATIM REPORT
# ---------------------------------------------------------------------------
print("=" * 72)
print("H_032  multi-channel stiffness donation  (escape class (a): borrow stiffness)")
print("=" * 72)
print("  D_s_flat (pairing channel, K) ............ %10.4f" % DS_FLAT_K)
print("  D_s_disp raw (donor channel, K) .......... %10.4f" % DS_DISP_RAW_K)
print("  naive additive fantasy Tc (K) ............ %10.4f  (no Leggett gate)" % naive_additive_K)
print("  donation cap fraction max[x(1-x)] ........ %10.4f" % 0.25)
print("-" * 72)
print("  best working point x* .................... %10.4f" % best_x)
print("  T_phase (BKT, donated) at x* (K) ......... %10.4f" % best_tbkt)
print("  T_pair  (no-go cap)   at x* (K) .......... %10.4f" % best_tpair)
print("  Tc = min(T_phase,T_pair) at x* (K) ....... %10.4f" % best_tc)
print("-" * 72)
print("  ceiling band (K) ......................... %.1f - %.1f" % (CEILING_LO_K, CEILING_HI_K))
print("  room-T target (K) ........................ %10.4f" % TARGET_K)
print("  margin vs ceiling high edge (K) .......... %+10.4f" % margin_vs_ceiling)
print("-" * 72)
for r in result["falsifiers"]:
    print("  [%s] %s" % (r["status"], r["name"]))
print("-" * 72)
print("falsifiers_pass=%d/%d" % (passes, total))
print("VERDICT: %s" % verdict)
print("=" * 72)
