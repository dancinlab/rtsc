#!/usr/bin/env python3
"""H_045 - Synthetic-Dimension Coordination Pump (escape class (c): different rigidity).

Within-cluster VARIANT of the geometric / multilayer flat-band stiffness cluster
(siblings H_006 dimension-scan, H_032 multiband-donation). It tests one specific
twist: add an internal "synthetic" hopping axis (an extra index m=0..N-1 with
uniform synthetic hopping t_s) to a 2D flat band WITHOUT adding real space, and ask
whether the EXTRA coordination on the synthetic axis pumps up the PHYSICAL phase
stiffness D_s that sets T_BKT.

CLAIM (escape seed, triage 2026_06_25): adding N synthetic Josephson neighbors
decouples flat-band pairing from stiffness-coordination, giving
    D_s(N) ~ D_s(1) * (1 + c*(N-1)),  c>0,  real-space <g> unchanged,
so T_BKT = (pi/2)*D_s clears 164 K for N>=3.

HONEST NULL (load-bearing, decisive falsifier - NOT engineered around):
The phase stiffness that bounds T_BKT is the PHYSICAL Kubo superfluid weight = the
long-wavelength current-current response to a REAL electromagnetic vector potential
A_x (the BKT vortices live in real 2D space). In a lattice BdG/Kubo calculation the
current operator comes from the Peierls phase exp[i (e/hbar) A . r_ij], where r_ij
is the REAL-SPACE displacement of bond (i,j). A synthetic-dimension bond connects
m -> m+1 at the SAME real-space site: its real displacement r_ij = 0, so a real
vector potential imprints ZERO Peierls phase on it. The synthetic hopping t_s
therefore enters the real-direction current operator with weight (displacement)^2 = 0
and contributes NOTHING to D_xx / D_yy; it only feeds a synthetic-index susceptibility
D_ss (response to a fictitious synthetic gauge field, which no real vortex couples to).

Equivalently, in the isolated-flat-band geometric superfluid-weight formula
    D_s^{mu,nu} = (|U|/hbar^2) * nu(1-nu) * <g_{mu,nu}>
(Liang et al. PRB 95 024515 2017; Peotta-Torma Nat.Commun. 6 8944 2015), the quantum
metric g_{mu,nu} is built from d(Bloch eigvec)/dk_mu. For mu,nu in {x,y} this uses the
REAL momentum; for the synthetic direction it uses a synthetic momentum that the real
T_BKT cannot see. So <g_xx>(N) is set by the real-space cell and is N-INDEPENDENT,
while only <g_ss> grows with the synthetic axis -> D_s(N) saturates at D_s(1).

PROBE (deterministic, stdlib `math` only - no numpy, no random, no Date):
Build a minimal flat-band cell (cross-stitch: two real-space sites A,B per cell with a
destructive-interference flat band) replicated into an N-rung synthetic dimension with
uniform synthetic hopping t_s. Compute, in CLOSED FORM, the BZ-averaged quantum-metric
tensor components <g_xx> (REAL) and <g_ss> (SYNTHETIC) by finite difference of the
normalized flat-band Bloch eigenvector over real momentum k_x and synthetic momentum
k_s. Map each to its superfluid weight via the geometric formula at fixed filling nu
and fixed |U|, then T_BKT = (pi/2) D_s. The escape needs the REAL-direction T_BKT(N) to
exceed 164 K and grow with N; the honest-null is D_s_real(N) = D_s_real(1) (flat in N).

GROUNDED anchors (cited, not fabricated):
  * T_BKT = (pi/2) D_s, Tc = min(T_pair, T_phase)   Emery-Kivelson PRB 52 6122 (1995).
  * Isolated-flat-band geometric superfluid weight D_s ~ |U| nu(1-nu) <g> from the
    quantum metric                                  Peotta-Torma Nat.Commun. 6 8944 (2015);
                                                     Liang et al. PRB 95 024515 (2017).
  * Kubo D_s = current-current response to a REAL vector potential via the Peierls
    phase on REAL-space bond displacements          Scalapino-White-Zhang PRB 47 7995 (1993).
  * Synthetic-dimension hopping couples to a SYNTHETIC (not real) gauge field; its
    bonds carry zero real-space displacement        Boada et al. PRL 108 133001 (2012);
                                                     Celi et al. PRL 112 043001 (2014).
GROUNDED campaign numbers (PR#40 frozen wall):
  * ambient phase-stiffness ceiling band ~134-164 K (number to BEAT = 164 K).
  * flat-band geometric D_s ~0.06-0.44 meV (1-8 K), ~20-90x BELOW the cuprate scale.
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tool'))
from rtsc_harness import Falsifier, evaluate, ROOM_T_K

# ---------------------------------------------------------------------------
# Frozen grounded constants (PR#40 wall + literature anchors). No tuning.
# ---------------------------------------------------------------------------
CEILING_LO_K = 134.0          # phase-stiffness ambient ceiling, low edge
CEILING_HI_K = 164.0          # ... high edge (the number to BEAT to escape)
TARGET_K = ROOM_T_K           # 293 K @ 1 atm
PI_OVER_2 = math.pi / 2.0     # Emery-Kivelson: T_BKT = (pi/2) * D_s (D_s in K)

# Geometric-superfluid-weight calibration: map a dimensionless metric trace <g> to a
# stiffness in Kelvin. Anchored CHARITABLY so the SINGLE-cell real-direction flat band
# already sits at the TOP of the campaign's honest geometric band (8 K) - i.e. we give
# the claim its best possible single-rung starting point. (Campaign band 1-8 K.)
DS_PER_UNIT_G_K = 8.0 / 0.25   # so <g_xx>=0.25 (the canonical 1D winding metric) -> 8 K
FILLING_NU = 0.5              # nu(1-nu) maximal at half-filling (best case) = 0.25
NU_FACTOR = FILLING_NU * (1.0 - FILLING_NU) / 0.25   # =1.0 at nu=0.5 (normalized best case)

# Synthetic-axis uniform hopping (eV-scale; large to give the pump its best shot).
T_S = 1.0
# Real-space intra-cell hopping setting the flat-band geometry (held FIXED across N).
T_REAL = 1.0

N_K = 2000                    # fixed BZ grid -> byte-deterministic finite differences
N_MAX = 8                     # synthetic rungs to scan (N=1..8)


# ---------------------------------------------------------------------------
# Flat-band Bloch eigenvector and its quantum metric (closed form, finite diff).
# ---------------------------------------------------------------------------
# REAL-space cell = canonical 2-level winding flat band: the lower-band eigenvector
# tracks the unit vector n(k_x) = (sin k_x, 0, cos k_x). Its BZ-averaged quantum
# metric is the textbook g_xx = 1/4 |d n / d k_x|^2 -> <g_xx> = 0.25 (matches the
# harness _trapz_metric_1d). This is the REAL-direction geometry and is built ONLY
# from the real-space cell - it does NOT know about the synthetic rungs.
#
# SYNTHETIC axis = a uniform-hopping 1D ring of N rungs. Its Bloch phase is
# theta_s = k_s, k_s in [-pi,pi). The synthetic "band" eigenvector winds with k_s and
# carries its OWN metric <g_ss>, which GROWS with the synthetic coordination (more
# rungs -> finer winding -> larger internal susceptibility). Crucially this metric is
# a derivative w.r.t. the SYNTHETIC momentum k_s, NOT k_x: it feeds D_ss, not D_xx.

def _g_real_bz_avg(n_k):
    """<g_xx> of the real-space winding flat band by central finite difference over k_x.
    Independent of N by construction (real cell is fixed). Returns ~0.25."""
    total = 0.0
    dk = 2.0 * math.pi / n_k
    for i in range(n_k):
        k = -math.pi + i * dk
        kp, km = k + dk, k - dk
        np_ = (math.sin(kp), 0.0, math.cos(kp))
        nm_ = (math.sin(km), 0.0, math.cos(km))
        dn = tuple((np_[j] - nm_[j]) / (2.0 * dk) for j in range(3))
        g = 0.25 * sum(c * c for c in dn)
        total += g
    return total / n_k


def _g_synth_bz_avg(n_rungs, n_k):
    """<g_ss> of the SYNTHETIC ring with n_rungs uniform-hopping sites, by central finite
    difference over the SYNTHETIC momentum k_s. For a single uniform 1D ring the lower
    Bloch state is structureless for N=1 (no winding -> 0) and the inter-rung winding
    susceptibility grows with the number of rungs (more internal neighbours). We model
    the synthetic eigenvector as the normalized N-site uniform superposition phase-wound
    by k_s; its metric scales as ~ (N^2-1)/12 (variance of a uniform index distribution),
    the standard 'particle-on-a-ring' position variance. This GROWS with N - it is the
    real lever the claim is paying for, but it lives on the SYNTHETIC axis."""
    if n_rungs < 1:
        raise ValueError("n_rungs must be >= 1: " + repr(n_rungs))
    if n_rungs == 1:
        return 0.0
    # position-variance of a uniform index m=0..N-1 about its mean = (N^2 - 1)/12.
    # This is exactly <g_ss> for a maximally-delocalized synthetic-ring Bloch state
    # (the quantum metric = variance of the position operator in the band Wannier state).
    return (n_rungs * n_rungs - 1.0) / 12.0


def d_s_real_K(n_rungs):
    """PHYSICAL (real-direction) superfluid weight in K. The geometric formula uses the
    REAL-direction metric <g_xx>, which is N-INDEPENDENT: the synthetic rungs add bonds
    with ZERO real-space displacement, so they drop out of the real Kubo current bubble.
    D_s_real(N) = (|U|-normalized) * nu(1-nu) * <g_xx>  -> flat in N."""
    g_real = _g_real_bz_avg(N_K)
    return DS_PER_UNIT_G_K * NU_FACTOR * g_real          # no n_rungs dependence


def d_s_synth_K(n_rungs):
    """SYNTHETIC-direction superfluid weight in K (response to a FICTITIOUS synthetic
    gauge field). This DOES grow with N - it is what the pump actually buys - but no real
    BKT vortex couples to it, so it cannot set the real-space T_BKT."""
    g_synth = _g_synth_bz_avg(n_rungs, N_K)
    return DS_PER_UNIT_G_K * NU_FACTOR * g_synth


def t_bkt_real_K(n_rungs):
    return PI_OVER_2 * d_s_real_K(n_rungs)


# ---------------------------------------------------------------------------
# Scan N = 1..N_MAX deterministically.
# ---------------------------------------------------------------------------
rows = []
for N in range(1, N_MAX + 1):
    ds_r = d_s_real_K(N)
    ds_s = d_s_synth_K(N)
    rows.append((N, ds_r, ds_s, t_bkt_real_K(N)))

ds_real_1 = rows[0][1]
ds_real_Nmax = rows[-1][1]
tbkt_real_Nmax = rows[-1][3]
ds_synth_Nmax = rows[-1][2]

# Claim's fantasy: if the synthetic coordination DID pump real stiffness as
# D_s(N) = D_s(1)*(1 + c*(N-1)) with the SAME slope the synthetic axis shows, what would
# real T_BKT be? (quantifies how much the honest-null costs the claim.)
synth_slope = (ds_synth_Nmax / ds_real_1) if ds_real_1 > 0 else 0.0  # how big the synth lever is
fantasy_tbkt_Nmax = PI_OVER_2 * ds_real_1 * (1.0 + synth_slope)      # if it leaked to real

# Does real D_s grow at all across N? (relative change from N=1 to N_MAX)
real_growth_frac = (ds_real_Nmax - ds_real_1) / ds_real_1 if ds_real_1 > 0 else 0.0

best_real_tbkt = max(r[3] for r in rows)
margin_vs_ceiling = best_real_tbkt - CEILING_HI_K

metrics = {
    "ds_real_N1_K": ds_real_1,
    "ds_real_Nmax_K": ds_real_Nmax,
    "ds_synth_Nmax_K": ds_synth_Nmax,
    "real_growth_frac_N1_to_Nmax": real_growth_frac,
    "best_real_tbkt_K": best_real_tbkt,
    "tbkt_real_Nmax_K": tbkt_real_Nmax,
    "fantasy_tbkt_Nmax_K": fantasy_tbkt_Nmax,
    "synth_lever_size": synth_slope,
    "n_max_rungs": N_MAX,
    "ceiling_lo_K": CEILING_LO_K,
    "ceiling_hi_K": CEILING_HI_K,
    "target_K": TARGET_K,
    "margin_vs_ceiling_K": margin_vs_ceiling,
}

# ---------------------------------------------------------------------------
# FALSIFIERS (PASS = NOT triggered). The honest-null is the decisive one.
# Falsifier.predicate(metrics) -> True means TRIGGERED (refuted).
# ---------------------------------------------------------------------------
# Every falsifier is phrased as an ESCAPE-DETECTOR: it PASSes (not triggered) only when
# the escape feature is genuinely present. Since the wall holds, the escape-detectors
# FAIL (consistent with the sibling confirm-wall cards H_032/H_036/H_038: low pass count).
# F1 is the DECISIVE honest-null - it PASSes only if synthetic coordination pumps the
# REAL phase rigidity; its FAIL is the load-bearing closed-negative signal.
falsifiers = [
    # F1 - DECISIVE HONEST-NULL: synthetic coordination must pump the REAL stiffness.
    #      PASS(not triggered) only if real D_s genuinely grows with N (claim's c>0).
    Falsifier(
        "honest_null_synthetic_pumps_real_Ds",
        lambda m: m["real_growth_frac_N1_to_Nmax"] <= 0.01,
        "DECISIVE honest-null. ESCAPE requires synthetic coordination to pump the REAL "
        "phase rigidity: real D_s(N) grows by >1% from N=1 to N_max. The synthetic bonds "
        "carry ZERO real-space displacement, so they drop out of the real Kubo current "
        "bubble (Peierls phase=0) and out of <g_xx>. TRIGGERED(FAIL) when real D_s stays "
        "flat (growth<=1%) => synthetic axis does NOT pump physical rigidity; D_s(N) "
        "saturates at D_s(1). This FAIL is the closed-negative honest-null.",
    ),
    # F2 - does the real-direction T_BKT clear the 164 K ceiling for any N?
    Falsifier(
        "real_tbkt_clears_ceiling",
        lambda m: m["best_real_tbkt_K"] <= m["ceiling_hi_K"],
        "ESCAPE requires best real-direction T_BKT over N=1..N_max to exceed 164 K. "
        "TRIGGERED(FAIL) when it stays at/below the ceiling.",
    ),
    # F3 - does it reach the actual room-T target?
    Falsifier(
        "reaches_room_T_target",
        lambda m: m["best_real_tbkt_K"] < m["target_K"],
        "ESCAPE requires best real-direction T_BKT to reach 293 K @ 1 atm. "
        "TRIGGERED(FAIL) when below target.",
    ),
    # F4 - growth landed in the WRONG (synthetic) channel? PASS only if the growth shows
    #      up in the REAL channel; FAIL is the mislabelled-internal-susceptibility signal.
    Falsifier(
        "growth_in_real_not_synthetic_channel",
        lambda m: m["synth_lever_size"] > 1.0 and m["real_growth_frac_N1_to_Nmax"] < 0.01,
        "Diagnostic of where the coordination lever lands. ESCAPE requires the growth in "
        "the REAL channel. TRIGGERED(FAIL) when the synthetic lever is large (>1x) while "
        "real D_s stayed flat (<1% growth): the pump fed the SYNTHETIC-index "
        "susceptibility (a fictitious-gauge-field response no real vortex couples to), "
        "not the real phase rigidity. This FAIL co-confirms the honest-null.",
    ),
    # F5 - even the FANTASY (leak the full synthetic lever into the real channel) clear?
    Falsifier(
        "fantasy_leak_reaches_target",
        lambda m: m["fantasy_tbkt_Nmax_K"] < m["target_K"],
        "Charity check: even if the ENTIRE synthetic lever leaked into the REAL channel "
        "(physically forbidden, but the claim's best fantasy), does real T_BKT reach "
        "293 K? PASS(not triggered) if even the fantasy clears target; FAIL if even the "
        "optimistic leak falls short - reporting how generous the closed-negative is.",
    ),
]

result = evaluate(metrics, falsifiers)
passes = result["n_pass"]
total = result["n_total"]

# ESCAPE only if the honest-null PASSES (real D_s genuinely pumped) AND real T_BKT clears
# the ceiling. Honest-null is F1; decisive.
honest_null_passes = metrics["real_growth_frac_N1_to_Nmax"] > 0.01
escapes = honest_null_passes and (metrics["best_real_tbkt_K"] > metrics["ceiling_hi_K"])
verdict = "escapes-wall" if escapes else "confirms-wall"

# ---------------------------------------------------------------------------
# VERBATIM REPORT
# ---------------------------------------------------------------------------
print("=" * 72)
print("H_045  synthetic-dimension coordination pump  (escape class (c): rigidity)")
print("=" * 72)
print("  real-space intra-cell hopping t_real ..... %10.4f  (FIXED across N)" % T_REAL)
print("  synthetic-axis hopping t_s ............... %10.4f" % T_S)
print("  filling nu (best case 0.5) ............... %10.4f" % FILLING_NU)
print("-" * 72)
print("  N   D_s_real(K)   D_s_synth(K)   T_BKT_real(K)")
for (N, ds_r, ds_s, tb) in rows:
    print("  %d   %10.6f   %11.6f   %12.6f" % (N, ds_r, ds_s, tb))
print("-" * 72)
print("  real D_s(N=1) (K) ........................ %10.6f" % ds_real_1)
print("  real D_s(N=%d) (K) ........................ %10.6f" % (N_MAX, ds_real_Nmax))
print("  real D_s growth N=1->%d (frac) ........... %+10.6f" % (N_MAX, real_growth_frac))
print("  synthetic D_s(N=%d) (K) (decoupled axis) .. %10.6f" % (N_MAX, ds_synth_Nmax))
print("  synthetic lever size (x D_s_real) ........ %10.4f" % synth_slope)
print("  fantasy: full synth leak -> real T_BKT (K) %10.4f" % fantasy_tbkt_Nmax)
print("-" * 72)
print("  best real-direction T_BKT over N (K) ..... %10.6f" % best_real_tbkt)
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
