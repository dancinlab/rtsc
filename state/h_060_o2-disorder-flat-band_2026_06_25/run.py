#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H_060 — O2 disorder -> flat band (disorder-induced flat band, geometry lever).

WITHIN-CLUSTER VARIANT of the confirmed flat-band / phase-stiffness wall
(H_001 / H_006 / H_017 / freeze ~134-164K). The seed's specific twist:
can a DISORDER-INDUCED flat band (DOS spike at E_F from Anderson on-site
disorder W, with no crystalline destructive-interference geometry) deliver
the geometric phase stiffness D_s "for free from randomness"?

The seed's HONEST-NULL (load-bearing, decisive) reads verbatim:
  "D_s(W) is non-monotone and its maximum stays >=20x below the cuprate
   7.4 meV phase-stiffness scale (T_BKT_max << 134 K), OR disorder that
   flattens the band simultaneously localizes the pairs (xi_loc < lattice
   spacing) so the superfluid response vanishes (D_s -> 0 as IPR -> 1).
   ESCAPE only if a finite W* gives D_s(W*) with T_BKT > 134 K AND
   xi_loc > vortex-core size (pairs stay extended)."

We do NOT engineer around the honest-null. This probe MEASURES the
W-sweep tradeoff with a deterministic, stdlib-only Anderson tight-binding
model and a Kubo/Thouless geometric-stiffness proxy.

PHYSICS (research-grounded, cited in the card):
  - In d<=2, ANY on-site disorder Anderson-localizes ALL single-particle
    states (Abrahams-Anderson-Licciardello-Ramakrishnan scaling theory,
    PRL 42, 673 (1979)). There is no extended-state window in 2D.
  - A disorder-INDUCED DOS spike at E_F (the "flat band" the seed wants)
    appears precisely when W ~ bandwidth, i.e. exactly where the
    localization length xi_loc collapses toward the lattice spacing.
  - The Kubo geometric stiffness of a flat band built from LOCALIZED
    states is bounded by the spatial extent of those states: a localized
    insulator has D_s = 0 (Kohn 1964; localization functional <X^2>_c
    finite -> Drude/superfluid weight -> 0). Crystalline flat bands
    evade this ONLY through quantum-geometric (Bloch-extended) destructive
    interference, which on-site RANDOMNESS does not provide.
    [Tovmasyan et al PRB 94 245149; Peotta-Torma Nat Commun 6 8944;
     Kolar-Heikkila-Torma arXiv:2510.05224 — disorder superfluid weight
     a competition of localization functionals, "typically vanishing".]

Determinism: a fixed-seed (splitmix64) integer PRNG, fixed grid, no Date,
no system RNG. Byte-equal across runs.

Falsifiers (>=4) incl. the HONEST-NULL as the decisive one. PASS = NOT
triggered (falsifier-first honesty; PASS does NOT mean escape).
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tool"))
from rtsc_harness import Falsifier, evaluate, ROOM_T_K

# ---------------------------------------------------------------------------
# deterministic PRNG (splitmix64 -> uniform in [0,1)); NO system RNG, NO Date.
# ---------------------------------------------------------------------------
_MASK = (1 << 64) - 1


def _splitmix64(state):
    state = (state + 0x9E3779B97F4A7C15) & _MASK
    z = state
    z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & _MASK
    z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & _MASK
    z = z ^ (z >> 31)
    return state, z


class Rng:
    def __init__(self, seed):
        self.s = seed & _MASK

    def u01(self):
        self.s, z = _splitmix64(self.s)
        return z / float(1 << 64)


# ---------------------------------------------------------------------------
# physical constants / anchors
# ---------------------------------------------------------------------------
KB_meV_per_K = 0.0861733          # k_B in meV/K
CUPRATE_DS_meV = 7.4              # measured cuprate phase-stiffness scale (seed anchor)
WALL_K = 134.0                    # frozen ambient SF ceiling (lower edge of band)


def t_bkt_K(ds_meV):
    # T_BKT = (pi/2) D_s ; with D_s in meV and T in K:
    #   k_B T_BKT = (pi/2) D_s  ->  T_BKT[K] = (pi/2)*D_s[meV]/k_B[meV/K]
    return (math.pi / 2.0) * ds_meV / KB_meV_per_K


# ---------------------------------------------------------------------------
# Anderson tight-binding chain (quasi-1D rep of the d<=2 localized regime).
# In d<=2 ALL states localize for any W>0 (scaling theory): the 1D
# transfer-matrix Lyapunov exponent gives xi_loc EXACTLY and deterministically,
# and the participation ratio / IPR of the states near E_F gives the
# flat-band DOS spike. The verdict (localized -> D_s->0) is dimension-robust
# in d<=2; 2D only makes xi_loc parametrically LARGER but still finite, never
# extended. We additionally report the 2D weak-disorder localization length to
# show the verdict holds in 2D (xi_loc finite -> D_s = 0 either way).
# ---------------------------------------------------------------------------

def lyapunov_xi_loc(W, n_sites, energy, t, seed):
    """1D Anderson localization length xi_loc (lattice units) at given energy
    via the transfer-matrix Lyapunov exponent. on-site eps in [-W/2, W/2].
    Returns xi_loc = 1/gamma. Deterministic for fixed seed."""
    rng = Rng(seed)
    psi0, psi1 = 1.0, 0.0
    logsum = 0.0
    for _ in range(n_sites):
        eps = (rng.u01() - 0.5) * W
        psi2 = ((energy - eps) / t) * psi1 - psi0
        psi0, psi1 = psi1, psi2
        nrm = math.hypot(psi0, psi1)
        if nrm > 1e-12:
            logsum += math.log(nrm)
            psi0 /= nrm
            psi1 /= nrm
    gamma = logsum / n_sites
    if gamma <= 1e-12:
        return float("inf")
    return 1.0 / gamma


def dos_and_ipr_at_ef(W, n_sites, t, seed):
    """Finite Anderson chain; diagonalize the symmetric tridiagonal H; return:
      rho_ratio : DOS at E_F (E=0) as a ratio to the clean W=0 reference
                  (the 'flat-band spike' enhancement)
      ipr_EF    : mean IPR of the ~2% of states nearest E_F
                  (IPR->1 == single-site localized; IPR->1/N == extended)."""
    rng = Rng(seed)
    diag = [(rng.u01() - 0.5) * W for _ in range(n_sites)]
    off = [t] * (n_sites - 1)
    evals, evecs = _tridiag_eig(diag, off)
    win = 0.10 * 4.0 * t
    cnt = sum(1 for e in evals if abs(e) <= win / 2.0)
    rho = cnt / (win * n_sites)
    order = sorted(range(n_sites), key=lambda i: abs(evals[i]))
    k = max(1, n_sites // 50)
    ipr_vals = []
    for idx in order[:k]:
        v = [evecs[r][idx] for r in range(n_sites)]
        s2 = sum(x * x for x in v)
        if s2 <= 0:
            continue
        ipr = sum((x * x / s2) ** 2 for x in v)
        ipr_vals.append(ipr)
    ipr_EF = sum(ipr_vals) / len(ipr_vals) if ipr_vals else 1.0
    return rho, ipr_EF


# --- stdlib symmetric-tridiagonal eigensolver (QL with implicit shifts) -----
def _tridiag_eig(d, e):
    """Eigenvalues + eigenvectors of a symmetric tridiagonal matrix.
    d: diagonal (len n), e: off-diagonal (len n-1). Returns (evals, Z) with
    Z[r][c] = component r of eigenvector c. Numerical-Recipes tqli; stdlib;
    deterministic."""
    n = len(d)
    d = list(d)
    e = list(e) + [0.0]
    z = [[1.0 if r == c else 0.0 for c in range(n)] for r in range(n)]
    for l in range(n):
        it = 0
        while True:
            m = l
            while m < n - 1:
                dd = abs(d[m]) + abs(d[m + 1])
                if abs(e[m]) <= 1e-15 * dd or abs(e[m]) < 1e-300:
                    break
                m += 1
            if m == l:
                break
            it += 1
            if it > 60:
                break
            g = (d[l + 1] - d[l]) / (2.0 * e[l])
            r = math.hypot(g, 1.0)
            g = d[m] - d[l] + e[l] / (g + (r if g >= 0 else -r))
            s = c = 1.0
            p = 0.0
            broke = False
            for i in range(m - 1, l - 1, -1):
                f = s * e[i]
                b = c * e[i]
                r = math.hypot(f, g)
                e[i + 1] = r
                if r == 0.0:
                    d[i + 1] -= p
                    e[m] = 0.0
                    broke = True
                    break
                s = f / r
                c = g / r
                g = d[i + 1] - p
                r = (d[i] - g) * s + 2.0 * c * b
                p = s * r
                d[i + 1] = g + p
                g = c * r - b
                for kk in range(n):
                    f = z[kk][i + 1]
                    z[kk][i + 1] = s * z[kk][i] + c * f
                    z[kk][i] = c * z[kk][i] - s * f
            if broke:
                continue
            d[l] -= p
            e[l] = g
            e[m] = 0.0
    return d, z


# ---------------------------------------------------------------------------
# Kubo geometric-stiffness proxy for a DISORDER-INDUCED flat band.
#
# CRITICAL HONESTY POINT. The seed's claim is that RANDOMNESS *manufactures* a
# geometric flat band "for free" — an EXCESS pile-up of states at E_F (above the
# clean dispersive baseline) carrying geometric phase stiffness. So the bare
# geometric stiffness this route can claim is set ONLY by the EXCESS DOS that
# disorder creates, NOT by the clean dispersive band that already exists at W=0.
# (The clean W=0 band's stiffness is the ordinary Drude weight; it is NOT a
# disorder-induced flat band and crediting it would be a definitional cheat that
# fakes an escape.)  Hence:
#       excess(W) = max(0, dos_ratio(W) - 1)        # the disorder-MADE flat weight
#       D_s0(W)   = CUPRATE_DS_meV * min(1, excess)  # most generous FS-capped bare
# Then Kohn (1964) / Resta localization: a flat band built from LOCALIZED states
# has its Kubo q->0 stiffness suppressed once xi_loc <= vortex core; the bare
# stiffness is realized only when xi_loc >> 1:
#       D_s(W) = D_s0(W) * f_coh(xi_loc),  f_coh = 1 - exp(-xi_loc / xi_core)
# The honest-null lives in BOTH factors: on-site randomness makes almost no
# excess flat weight (D_s0 ~ 0), and wherever it would (W ~ bandwidth) the states
# localize (f_coh -> 0). Either way D_s collapses.
# ---------------------------------------------------------------------------
XI_CORE = 3.0     # vortex-core size in lattice units (BCS coherence ~ a few a)


def kubo_ds_meV(rho_ratio, xi_loc):
    excess = max(0.0, rho_ratio - 1.0)           # disorder-INDUCED flat weight only
    ds0 = CUPRATE_DS_meV * min(1.0, excess)
    if math.isinf(xi_loc):
        f_coh = 1.0
    else:
        f_coh = 1.0 - math.exp(-xi_loc / XI_CORE)
    return ds0 * f_coh


def xi_loc_2D(W, t):
    # 2D weak-disorder localization length (self-consistent, report-only):
    # xi_2D ~ a * exp(pi k_F l / 2), mean free path l ~ (bandwidth/W)^2.
    if W <= 0:
        return float("inf")
    kf_l = (4.0 * t / W) ** 2
    return math.exp(min(50.0, math.pi * kf_l / 2.0))


# ---------------------------------------------------------------------------
# RUN: W-sweep
# ---------------------------------------------------------------------------
def main():
    t = 1.0
    N = 600
    N_LYAP = 20000
    BASE_SEED = 0xC0FFEE
    Ws = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
    bandwidth = 4.0 * t

    rows = []
    rho0_ref = 1e-9
    for j, W in enumerate(Ws):
        seed = (BASE_SEED * 1000003 + j * 2654435761) & _MASK
        rho_raw, ipr = dos_and_ipr_at_ef(W, N, t, seed)
        if W == 0.0:
            rho0_ref = rho_raw if rho_raw > 0 else 1e-9
        rho_ratio = rho_raw / rho0_ref
        xi = lyapunov_xi_loc(W, N_LYAP, 0.0, t, seed ^ 0xABCDEF)
        xi2d = xi_loc_2D(W, t)
        ds = kubo_ds_meV(rho_ratio, xi)
        tbkt = t_bkt_K(ds)
        rows.append({
            "W_over_t": W,
            "W_over_bandwidth": W / bandwidth,
            "dos_spike_ratio": rho_ratio,
            "ipr_EF": ipr,
            "xi_loc_1D": xi,
            "xi_loc_2D_est": xi2d,
            "Ds_meV": ds,
            "T_BKT_K": tbkt,
        })

    # the disorder-INDUCED flat band: pick among W>0 the row with the largest
    # EXCESS DOS pile-up at E_F (the flat weight randomness actually manufactured).
    disordered = [r for r in rows if r["W_over_t"] > 0.0]
    spike_row = max(disordered, key=lambda r: r["dos_spike_ratio"])
    # best stiffness this ROUTE can claim is also restricted to W>0 (a
    # disorder-induced flat band requires disorder; W=0 is the clean band).
    best_ds_row = max(disordered, key=lambda r: r["Ds_meV"])
    ds_max_meV = best_ds_row["Ds_meV"]
    tbkt_max_K = best_ds_row["T_BKT_K"]
    ds_shortfall_factor = (CUPRATE_DS_meV / ds_max_meV) if ds_max_meV > 0 else float("inf")

    metrics = {
        "n_W_points": len(rows),
        "bandwidth_over_t": bandwidth,
        "spike_W_over_t": spike_row["W_over_t"],
        "spike_dos_ratio": spike_row["dos_spike_ratio"],
        "spike_ipr_EF": spike_row["ipr_EF"],
        "spike_xi_loc_1D": spike_row["xi_loc_1D"],
        "spike_xi_loc_2D_est": spike_row["xi_loc_2D_est"],
        "Ds_at_spike_meV": spike_row["Ds_meV"],
        "T_BKT_at_spike_K": spike_row["T_BKT_K"],
        "Ds_max_meV_anyW": ds_max_meV,
        "T_BKT_max_K_anyW": tbkt_max_K,
        "Ds_max_at_W_over_t": best_ds_row["W_over_t"],
        "cuprate_Ds_meV": CUPRATE_DS_meV,
        "Ds_shortfall_factor_vs_cuprate": ds_shortfall_factor,
        "wall_K": WALL_K,
        "room_T_K": ROOM_T_K,
        "xi_core_lattice": XI_CORE,
    }

    falsifiers = [
        Falsifier(
            name="F_NULL_localized_spike_kills_stiffness",
            predicate=lambda m: (m["spike_xi_loc_1D"] < 1.0) or (m["spike_ipr_EF"] > 0.5)
            or (m["Ds_at_spike_meV"] < CUPRATE_DS_meV / 20.0),
            desc="Honest-null: disorder-induced flat band is built from localized "
                 "states (xi_loc<a OR IPR->1) so D_s at the spike collapses "
                 "(<1/20 cuprate scale). Decisive: confirms the wall.",
        ),
        Falsifier(
            name="F1_Ds_max_below_20x_cuprate",
            predicate=lambda m: m["Ds_shortfall_factor_vs_cuprate"] >= 20.0,
            desc="Max D_s over all W stays >=20x below the 7.4 meV cuprate scale "
                 "(seed honest-null quantitative arm).",
        ),
        Falsifier(
            name="F2_TBKT_max_below_wall",
            predicate=lambda m: m["T_BKT_max_K_anyW"] < m["wall_K"],
            desc="Best disorder-induced T_BKT (any W) stays below the frozen "
                 "~134K SF ceiling.",
        ),
        Falsifier(
            name="F3_no_extended_pairs_in_flatband",
            predicate=lambda m: m["spike_xi_loc_1D"] <= m["xi_core_lattice"],
            desc="In the DOS-spike (flat) regime xi_loc never exceeds the vortex "
                 "core size, so pairs cannot stay phase-coherent.",
        ),
        Falsifier(
            name="F4_room_T_not_reached",
            predicate=lambda m: m["T_BKT_max_K_anyW"] < m["room_T_K"],
            desc="No disorder strength yields T_BKT >= 293 K (target).",
        ),
    ]

    verdict = evaluate(metrics, falsifiers)

    fmap = {r["name"]: r for r in verdict["falsifiers"]}
    null_triggered = fmap["F_NULL_localized_spike_kills_stiffness"]["triggered"]
    wall_triggered = fmap["F2_TBKT_max_below_wall"]["triggered"]
    extended = not fmap["F3_no_extended_pairs_in_flatband"]["triggered"]
    if (not null_triggered) and (not wall_triggered) and extended:
        ruling = "ESCAPES-WALL"
    elif null_triggered and wall_triggered:
        ruling = "CONFIRMS-WALL"
    else:
        ruling = "INCONCLUSIVE"

    print("=" * 72)
    print("H_060  O2 disorder -> flat band (disorder-induced flat band geometry)")
    print("  within-cluster variant of the flat-band / phase-stiffness wall")
    print("=" * 72)
    print("W-sweep (t=1, chain N=%d, Lyapunov N=%d, seed=0x%X):" % (N, N_LYAP, BASE_SEED))
    print("  W/t  W/BW   DOS_spike   IPR_EF    xi_1D      xi_2D_est   "
          "D_s[meV]   T_BKT[K]")
    for r in rows:
        xi1 = ("%.3f" % r["xi_loc_1D"]) if not math.isinf(r["xi_loc_1D"]) else "   inf"
        xi2 = ("%.3e" % r["xi_loc_2D_est"]) if not math.isinf(r["xi_loc_2D_est"]) else "inf"
        print("  %4.1f %5.2f  %9.4f  %7.4f  %8s  %10s  %8.5f  %9.3f" % (
            r["W_over_t"], r["W_over_bandwidth"], r["dos_spike_ratio"],
            r["ipr_EF"], xi1, xi2, r["Ds_meV"], r["T_BKT_K"]))
    print("-" * 72)
    print("flat-band (DOS-spike) regime:  W/t=%.1f  spike_ratio=%.4f" % (
        metrics["spike_W_over_t"], metrics["spike_dos_ratio"]))
    print("   at spike:  IPR_EF=%.4f   xi_loc_1D=%.4f   D_s=%.5f meV   T_BKT=%.3f K" % (
        metrics["spike_ipr_EF"], metrics["spike_xi_loc_1D"],
        metrics["Ds_at_spike_meV"], metrics["T_BKT_at_spike_K"]))
    print("best D_s over ALL W:  %.5f meV  at W/t=%.1f  ->  T_BKT_max=%.3f K" % (
        metrics["Ds_max_meV_anyW"], metrics["Ds_max_at_W_over_t"],
        metrics["T_BKT_max_K_anyW"]))
    print("cuprate scale=%.2f meV ; shortfall factor=%.2fx ; wall=%.0fK ; target=%.0fK" % (
        CUPRATE_DS_meV, metrics["Ds_shortfall_factor_vs_cuprate"],
        WALL_K, ROOM_T_K))
    print("-" * 72)
    print("FALSIFIERS (PASS = not triggered):")
    for r in verdict["falsifiers"]:
        print("  [%s] %s" % (r["status"], r["name"]))
    print("falsifiers_pass: %d / %d" % (verdict["n_pass"], verdict["n_total"]))
    print("=" * 72)
    print("VERDICT: %s" % ruling)
    print("  honest-null F_NULL triggered = %s (True=wall confirmed)" % null_triggered)
    print("  absorbed=false  is_green=false")
    print("=" * 72)


if __name__ == "__main__":
    main()
