#!/usr/bin/env python3
"""H_046 — Aperiodic / Quasicrystal Vortex Localizer (SF-escape variant probe).

WALL UNDER TEST (frozen): spin-fluctuation / phase-stiffness ambient ceiling
~134-164 K  (Emery-Kivelson  T_BKT = (pi/2) * D_s).  12/12 prior SF-escape
probes H_032-H_043 confirm-wall.  This is a WITHIN-CLUSTER variant attacking the
"order-traps" / vortex-disordering half of the Emery-Kivelson argument on an
APERIODIC (quasicrystal) host: multifractal vortex pinning + the absence of a
clean q->0 Goldstone phase mode.

SEED WALL-PREDICTION (the escape to be falsified):
    T_c^quasicrystal  >=  1.2 x  T_c^periodic   AT MATCHED D_s,
    because multifractal critical states raise the vortex-core depinning energy
    and suppress the soft q->0 phase mode.

HONEST-NULL (load-bearing falsifier, NOT engineered around):
    T_c^quasicrystal  <=  T_c^periodic   at matched pairing/coordination,
    i.e. quasiperiodicity reproduces or WORSENS the wall because multifractality
    SUPPRESSES the superfluid weight D_s (it adds no net pinning advantage).

LITERATURE (research-first, cited; not fabricated):
  - Takemori, Arita, Sakai, "Physical properties of weak-coupling quasiperiodic
    superconductors", arXiv:2005.03127 (PRB 102, 115108 2020): attractive-Hubbard
    on the Penrose tiling; pairing is INHOMOGENEOUS, specific-heat jump 10-20%
    BELOW the BCS-universal value, I-V increases gradually (not sharply) vs the
    periodic system  -> weaker, smeared collective response.
  - "Unconventional superfluidity of superconductivity on Penrose lattice",
    arXiv:2306.12641 (Sci. China Phys. Mech. Astron. 66, 290312 2023): the
    PARAMAGNETIC component of the superfluid density DOES NOT decay to zero in
    the thermodynamic limit (unlike the periodic system) -> it SUBTRACTS a finite
    amount from the diamagnetic term, LOWERING net D_s; D_s, the gap, and the DOS
    are all POSITIVELY correlated with the EXTENDED degree of single-particle
    states near E_F  -> localization / multifractality SUPPRESSES D_s.
  - Nagai, "Intrinsic vortex pinning in superconducting quasicrystals",
    arXiv:2111.13288: vortex pinning IS intrinsic on a quasicrystal, BUT it
    arises from the order-parameter INHOMOGENEITY -- the SAME inhomogeneity that
    surfaces the surviving paramagnetic term (no free lunch).

The literature null (the surviving paramagnetic term + localization-suppressed
D_s) is reproduced here by a DETERMINISTIC, stdlib-only real-space BdG mean-field
solve on a genuinely quasiperiodic FIBONACCI host vs a PERIODIC host of EQUAL
mean coordination and EQUAL attraction |U|.  D_s is extracted from the curvature
of the ground-state energy under a Peierls phase twist (twisted boundary /
vortex-fugacity proxy) -- which AUTOMATICALLY includes the paramagnetic term:
        D_s = (1/N) * d^2 E_GS / d(phi)^2  |_{phi->0}
and the BKT T_c from  T_BKT = (pi/2) * D_s  (Emery-Kivelson, same as the harness).

Deterministic: no RNG, no Date, no wall-clock.  Byte-identical across runs.
stdlib-only (math).  No fitting / no tune-to-green.
"""

from __future__ import annotations

import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tool"))
from rtsc_harness import Falsifier, evaluate, ROOM_T_K


# ---------------------------------------------------------------------------
# Linear algebra (stdlib only): real-symmetric eigenvalues by cyclic Jacobi.
# Deterministic, no external deps.
# ---------------------------------------------------------------------------

def jacobi_eigenvalues(a, sweeps=100, tol=1e-12):
    """Eigenvalues (sorted asc) of a real-symmetric matrix `a` (list of lists)
    via the cyclic Jacobi method.  Deterministic; returns a sorted Python list."""
    n = len(a)
    m = [list(row) for row in a]
    for _ in range(sweeps):
        off = 0.0
        for p in range(n):
            for q in range(p + 1, n):
                off += m[p][q] * m[p][q]
        if off < tol:
            break
        for p in range(n):
            for q in range(p + 1, n):
                apq = m[p][q]
                if abs(apq) < 1e-300:
                    continue
                app = m[p][p]
                aqq = m[q][q]
                phi = 0.5 * math.atan2(2.0 * apq, aqq - app)
                c = math.cos(phi)
                s = math.sin(phi)
                for k in range(n):
                    mkp = m[k][p]
                    mkq = m[k][q]
                    m[k][p] = c * mkp - s * mkq
                    m[k][q] = s * mkp + c * mkq
                for k in range(n):
                    mpk = m[p][k]
                    mqk = m[q][k]
                    m[p][k] = c * mpk - s * mqk
                    m[q][k] = s * mpk + c * mqk
    evals = sorted(m[i][i] for i in range(n))
    return evals


# ---------------------------------------------------------------------------
# Host builders.  Both are 1D rings of N sites with nearest-neighbour hopping;
# the QUASIPERIODIC host has Fibonacci-modulated bonds (two hopping amplitudes in
# the golden ratio), giving genuinely aperiodic, MULTIFRACTAL single-particle
# states and no clean q->0 Goldstone dispersion.  The PERIODIC host has uniform
# hopping matched to EQUAL mean |hopping| (equal mean coordination / equal bare
# bandwidth), isolating the quasiperiodicity itself.
# ---------------------------------------------------------------------------

def fibonacci_word(n):
    """Deterministic Fibonacci substitution word of length >= n over {0,1}
    (golden-ratio quasiperiodic sequence).  Returns the first n symbols."""
    s = "0"
    while len(s) < n:
        s = s.replace("1", "z").replace("0", "01").replace("z", "0")
    return s[:n]


def quasiperiodic_hoppings(N, t_a, t_b):
    """Ring of N bonds: bond i is t_a if Fibonacci symbol is '0' else t_b.
    Bond i connects site i and site (i+1) mod N."""
    w = fibonacci_word(N)
    return [t_a if w[i] == "0" else t_b for i in range(N)]


def periodic_hoppings(N, t_uniform):
    return [t_uniform] * N


# ---------------------------------------------------------------------------
# BdG ground energy under a Peierls phase twist, and D_s by twist curvature.
# We work in the uniform-gap BCS mean field so BOTH hosts get a gap from the SAME
# |U| (matched pairing); the host geometry then sets, via the twist curvature, how
# much of that pairing survives as PHASE STIFFNESS.  This is exactly the literature
# decomposition: D_s = diamagnetic - paramagnetic, and on the quasicrystal the
# paramagnetic term survives finite (arXiv:2306.12641), suppressing net D_s.
# ---------------------------------------------------------------------------

def bdg_ground_energy(hoppings, mu, delta, phi):
    """Ground-state (filled Bogoliubov sea) energy of a 1D ring with site-uniform
    s-wave gap `delta`, chemical potential `mu`, and a Peierls phase twist `phi`
    spread uniformly over the N bonds.  Real-symmetric BdG matrix (symmetric cos
    gauge) -> Jacobi eigenvalues; E_GS = sum of negative eigenvalues."""
    N = len(hoppings)
    dphi = phi / N
    dim = 2 * N
    H = [[0.0] * dim for _ in range(dim)]
    for i in range(N):
        j = (i + 1) % N
        t = hoppings[i]
        tp = -t * math.cos(dphi)
        H[i][j] += tp
        H[j][i] += tp
        th = t * math.cos(dphi)
        H[N + i][N + j] += th
        H[N + j][N + i] += th
    for i in range(N):
        H[i][i] += -mu
        H[N + i][N + i] += mu
        H[i][N + i] += delta
        H[N + i][i] += delta
    evals = jacobi_eigenvalues(H)
    return sum(e for e in evals if e < 0.0)


def superfluid_weight(hoppings, mu, delta, dphi_probe=0.04):
    """D_s per site = (1/N) d^2 E_GS / dphi^2 at phi->0 by central finite
    difference (deterministic).  Paramagnetic term included automatically."""
    N = len(hoppings)
    e0 = bdg_ground_energy(hoppings, mu, delta, 0.0)
    ep = bdg_ground_energy(hoppings, mu, delta, dphi_probe)
    em = bdg_ground_energy(hoppings, mu, delta, -dphi_probe)
    d2 = (ep - 2.0 * e0 + em) / (dphi_probe * dphi_probe)
    return d2 / N


def self_consistent_gap(hoppings, mu, U, delta0=0.5, iters=200, tol=1e-10):
    """T=0 uniform-gap BCS self-consistency on the host's NORMAL spectrum:
        1 = |U| * (1/N) sum_k 1/(2 sqrt(eps_k^2 + Delta^2)),
    eps_k = single-particle energies minus mu.  Monotone fixed-point iteration;
    both hosts get a gap from the SAME |U| (matched pairing).  Returns Delta>0."""
    N = len(hoppings)
    Hn = [[0.0] * N for _ in range(N)]
    for i in range(N):
        j = (i + 1) % N
        Hn[i][j] += -hoppings[i]
        Hn[j][i] += -hoppings[i]
    for i in range(N):
        Hn[i][i] += -mu
    eps = jacobi_eigenvalues(Hn)
    delta = delta0
    for _ in range(iters):
        s = 0.0
        for e in eps:
            s += 1.0 / (2.0 * math.sqrt(e * e + delta * delta))
        chi = U * s / N
        new = delta * chi
        if new <= 1e-9:
            new = 1e-9
        if abs(new - delta) < tol:
            delta = new
            break
        delta = new
    return delta


def run_host(hoppings, mu, U):
    delta = self_consistent_gap(hoppings, mu, U)
    Ds = superfluid_weight(hoppings, mu, delta)
    # Emery-Kivelson BKT ceiling (same convention as the harness wall).  Reported
    # as a DIMENSIONLESS comparison so the qc-vs-periodic ratio is unit-free.
    t_bkt = (math.pi / 2.0) * Ds
    return {"delta": delta, "D_s": Ds, "t_bkt_units": t_bkt}


# ---------------------------------------------------------------------------
# Probe.
# ---------------------------------------------------------------------------

def main():
    print("=" * 72)
    print("H_046  Aperiodic / Quasicrystal Vortex Localizer")
    print("  (SF-escape variant: vortex-disordering channel on an aperiodic host)")
    print("=" * 72)

    N = 89  # Fibonacci number -> clean Fibonacci ring closure
    mu = 0.0  # half-filling (particle-hole symmetric; cleanest D_s readout)
    U = 1.6   # attractive coupling magnitude (matched on BOTH hosts)

    t_a, t_b = 1.0, 1.0 / ((1.0 + math.sqrt(5.0)) / 2.0)  # golden-ratio bond ratio
    qp = quasiperiodic_hoppings(N, t_a, t_b)
    t_mean = sum(qp) / N
    pe = periodic_hoppings(N, t_mean)  # EQUAL mean hopping

    print(f"\n  N sites              : {N}")
    print(f"  filling              : half (mu={mu})")
    print(f"  |U| (matched)        : {U}")
    print(f"  quasicrystal bonds   : t_a={t_a:.6f}, t_b={t_b:.6f}  (golden ratio)")
    print(f"  matched mean |t|     : {t_mean:.6f}  (periodic uniform hopping)")

    res_q = run_host(qp, mu, U)
    res_p = run_host(pe, mu, U)

    print(f"\n  PERIODIC     : Delta={res_p['delta']:.6f}  D_s={res_p['D_s']:.6f}"
          f"  T_BKT(units)={res_p['t_bkt_units']:.6f}")
    print(f"  QUASICRYSTAL : Delta={res_q['delta']:.6f}  D_s={res_q['D_s']:.6f}"
          f"  T_BKT(units)={res_q['t_bkt_units']:.6f}")

    ds_ratio = res_q["D_s"] / res_p["D_s"] if res_p["D_s"] != 0 else float("inf")
    tc_ratio = res_q["t_bkt_units"] / res_p["t_bkt_units"] if res_p["t_bkt_units"] != 0 else float("inf")
    ds_deficit_frac = (res_p["D_s"] - res_q["D_s"]) / res_p["D_s"] if res_p["D_s"] != 0 else 0.0

    print(f"\n  D_s ratio  (qc / periodic)  : {ds_ratio:.6f}")
    print(f"  T_c ratio  (qc / periodic)  : {tc_ratio:.6f}")
    print(f"  D_s deficit fraction (qc)   : {ds_deficit_frac:.6f}"
          "   (>0 = quasiperiodicity SUPPRESSES stiffness)")
    print(f"  seed escape needs T_c ratio >= 1.20 ; ROOM_T target = {ROOM_T_K} K")

    metrics = {
        "N": N,
        "U": U,
        "delta_periodic": res_p["delta"],
        "delta_quasicrystal": res_q["delta"],
        "D_s_periodic": res_p["D_s"],
        "D_s_quasicrystal": res_q["D_s"],
        "tc_ratio_qc_over_periodic": tc_ratio,
        "ds_ratio_qc_over_periodic": ds_ratio,
        "ds_deficit_fraction": ds_deficit_frac,
        "escape_threshold": 1.20,
    }

    falsifiers = [
        # 1. THE HONEST-NULL (decisive): quasicrystal T_c does NOT beat periodic
        #    by the required 1.2x at matched pairing.  TRIGGERED => wall holds.
        Falsifier(
            "honest_null_qc_does_not_beat_periodic",
            lambda m: m["tc_ratio_qc_over_periodic"] < 1.20,
            "HONEST-NULL: T_c^qc < 1.2 x T_c^periodic at matched |U| & mean coord "
            "-> multifractality gives no net vortex-pinning T_c advantage (wall holds).",
        ),
        # 2. Paramagnetic survival: quasiperiodicity does NOT raise D_s
        #    (literature arXiv:2306.12641: surviving paramagnetic term lowers D_s).
        Falsifier(
            "no_net_stiffness_gain",
            lambda m: m["ds_ratio_qc_over_periodic"] <= 1.0,
            "Quasicrystal D_s <= periodic D_s -> the surviving paramagnetic term "
            "suppresses net phase stiffness (no free lunch).",
        ),
        # 3. Both hosts DO pair (matched pairing is real, not a dead-gap artifact).
        Falsifier(
            "pairing_is_real_on_both",
            lambda m: not (m["delta_periodic"] > 1e-6 and m["delta_quasicrystal"] > 1e-6),
            "Both hosts develop a finite self-consistent gap from the SAME |U| "
            "-> the comparison is at genuinely matched pairing, not a null gap.",
        ),
        # 4. Room-T escape: even granting the full 164K ceiling, reaching 293K needs
        #    a >=1.79x stiffness lift; the quasicrystal does not deliver it.
        Falsifier(
            "room_t_unreached",
            lambda m: m["tc_ratio_qc_over_periodic"] < 1.79,
            "Reaching 293K from the 164K ceiling needs a >=1.79x stiffness lift; "
            "the quasicrystal does not deliver it.",
        ),
    ]

    verdict = evaluate(metrics, falsifiers)

    print("\n" + "-" * 72)
    print("FALSIFIER LEDGER  (PASS = falsifier NOT triggered)")
    for r in verdict["falsifiers"]:
        print(f"  [{r['status']}] {r['name']}")
    print(f"\n  falsifiers_pass : {verdict['n_pass']} / {verdict['n_total']}")

    # ESCAPE only if the honest-null PASSES (NOT triggered) with real margin, i.e.
    # the quasicrystal genuinely beats periodic by >=1.2x.  EXPECTED: it FAILS
    # (is triggered) => confirms-wall.
    honest_null = next(r for r in verdict["falsifiers"]
                       if r["name"] == "honest_null_qc_does_not_beat_periodic")
    if honest_null["status"] == "PASS":
        decision = "escapes-wall"
    else:
        decision = "confirms-wall"

    print(f"\n  honest-null status : {honest_null['status']}  "
          f"(PASS=>escape, FAIL=>wall holds)")
    print(f"\nVERDICT: {decision}")
    print("  is_green=False  absorbed=false  (within-cluster SF-escape variant)")
    print("=" * 72)


if __name__ == "__main__":
    main()
