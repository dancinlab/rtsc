#!/usr/bin/env python3
"""H_037 DEFINITIVE — real classical XY Monte-Carlo on a {7,3} hyperbolic
tiling vs a square lattice at IDENTICAL bare coupling J.

REPLACES the closed-form proxy in run.py with the real compute the seed demands:

  1. build a verified {7,3} hyperbolic tiling (tiling73.build_73 — combinatorial,
     degree histogram exactly {2:boundary, 3:interior}, faces all heptagons),
     label every vertex BULK vs BOUNDARY by its growth-ring (the outer rings are
     the curvature-inflated O(1) boundary; BULK = vertices several rings inside,
     not adjacent to any degree-2 boundary vertex);
  2. build a periodic square lattice (no boundary) at the SAME bare J;
  3. run a Metropolis XY Monte-Carlo at a temperature sweep on each lattice;
  4. extract T_c on BOTH from the BULK order parameter:
       (a) Binder cumulant  U4 = 1 - <m^4>/(3<m^2>^2)  of the BULK magnetization,
       (b) the half-magnetization crossing of bulk |m|(T),
     measured on BULK SITES ONLY for the hyperbolic graph (boundary excluded).

  Decisive comparison: BULK  T_c^hyp / T_c^square  at matched J.
    honest-null  ratio <= 1.2  (boundary-dominated, no bulk lift -> confirms wall)
    escape       ratio >= 1.7  (geometry genuinely lifts the bulk ceiling)

  No tuning-to-green: T_c read off fixed pre-stated estimators on bulk sites only.

stdlib + numpy. Deterministic seed.
"""
import sys, os, math, time, json, argparse
import numpy as np
from collections import deque
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tiling73 import build_73, bfs_shell, _build as _build73


def build_square(L):
    nV = L * L
    def idx(x, y): return (x % L) * L + (y % L)
    adj = [[idx(x+1, y), idx(x-1, y), idx(x, y+1), idx(x, y-1)]
           for x in range(L) for y in range(L)]
    deg = np.array([4] * nV, dtype=np.int32)
    return nV, adj, deg


def adj_to_csr(adj):
    nbr, ptr = [], [0]
    for a in adj:
        nbr.extend(a); ptr.append(len(nbr))
    return np.array(nbr, dtype=np.int32), np.array(ptr, dtype=np.int32)


def metropolis_xy(nbr, ptr, nV, J, T, n_therm, n_meas, meas_every, rng,
                  bulk_idx):
    """Metropolis XY at coupling J, temperature T. Measures the BULK order
    parameter only (bulk_idx)."""
    beta = 1.0 / T
    theta = rng.uniform(0.0, 2.0 * math.pi, size=nV)
    nB = len(bulk_idx)
    m_abs = m2 = m4 = 0.0
    ncount = 0
    two_pi = 2.0 * math.pi
    total = n_therm + n_meas
    for sweep in range(total):
        # one Metropolis sweep (random new angle proposal)
        prop = theta + rng.uniform(-math.pi, math.pi, size=nV)
        u = rng.random(nV)
        for i in range(nV):
            old = theta[i]; new = prop[i]
            dE = 0.0
            for k in range(ptr[i], ptr[i+1]):
                tj = theta[nbr[k]]
                dE += -J * (math.cos(new - tj) - math.cos(old - tj))
            if dE <= 0.0 or u[i] < math.exp(-beta * dE):
                theta[i] = new % two_pi
        if sweep >= n_therm and (sweep - n_therm) % meas_every == 0:
            c = np.cos(theta[bulk_idx]); s = np.sin(theta[bulk_idx])
            mx = c.sum() / nB; my = s.sum() / nB
            mm = math.hypot(mx, my)
            m_abs += mm; m2 += mm*mm; m4 += mm*mm*mm*mm
            ncount += 1
    inv = 1.0 / ncount
    m_abs *= inv; m2 *= inv; m4 *= inv
    binder = 1.0 - m4 / (3.0 * m2 * m2) if m2 > 0 else 0.0
    return {"T": T, "nbulk": int(nB), "m_abs": m_abs, "m2": m2, "m4": m4,
            "binder": binder}


def run_lattice(name, nbr, ptr, nV, bulk_idx, J, temps, n_therm, n_meas,
                meas_every, seed):
    rows = []
    for ti, T in enumerate(temps):
        rng = np.random.default_rng(seed + 1009 * ti)
        r = metropolis_xy(nbr, ptr, nV, J, T, n_therm, n_meas, meas_every,
                          rng, bulk_idx)
        r["lattice"] = name
        rows.append(r)
        print("  [%s] T=%.3f  |m|_bulk=%.4f  binder=%.4f"
              % (name, T, r["m_abs"], r["binder"]), flush=True)
    return rows


def estimate_Tc(rows):
    Ts = np.array([r["T"] for r in rows])
    U = np.array([r["binder"] for r in rows])
    M = np.array([r["m_abs"] for r in rows])
    o = np.argsort(Ts); Ts, U, M = Ts[o], U[o], M[o]
    dU = np.gradient(U, Ts)
    Tc_binder = float(Ts[np.argmin(dU)])      # steepest Binder drop
    mmid = 0.5 * (M.max() + M.min())
    Tc_half = float(Ts[np.argmin(np.abs(M - mmid))])
    return Tc_binder, Tc_half


def hyper_bulk_idx(n_rings, bulk_ring_cut):
    """Build {7,3}, return (nV, adj, deg, bulk_idx, info). BULK = vertices whose
    growth-ring <= bulk_ring_cut AND not adjacent to any degree-2 boundary
    vertex (curvature boundary excluded)."""
    nV, adj, deg, ring_idx, faces = _build73(7, 3, n_rings)
    deg2 = (deg == 2)
    is_bulk = np.zeros(nV, dtype=bool)
    for v in range(nV):
        if deg[v] == 3 and ring_idx[v] <= bulk_ring_cut:
            if not any(deg2[w] for w in adj[v]):
                is_bulk[v] = True
    bulk_idx = np.where(is_bulk)[0]
    info = {"nV": nV, "nbulk": int(bulk_idx.size),
            "f_bd": 1.0 - bulk_idx.size / nV, "max_ring": int(ring_idx.max()),
            "deg_hist": {int(k): int(v) for k, v in
                         zip(*np.unique(deg, return_counts=True))}}
    return nV, adj, deg, bulk_idx, info


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rings", type=int, default=5)
    ap.add_argument("--bulk-ring-cut", type=int, default=-1,
                    help="max growth-ring counted as bulk; -1 => rings-2")
    ap.add_argument("--Lsq", type=int, default=20)
    ap.add_argument("--J", type=float, default=1.0)
    ap.add_argument("--ntemp", type=int, default=21)
    ap.add_argument("--tlo", type=float, default=0.2)
    ap.add_argument("--thi", type=float, default=2.4)
    ap.add_argument("--therm", type=int, default=400)
    ap.add_argument("--meas", type=int, default=1200)
    ap.add_argument("--meas-every", type=int, default=2)
    ap.add_argument("--seed", type=int, default=20260625)
    ap.add_argument("--out", type=str, default="mc_out.json")
    args = ap.parse_args()

    t0 = time.time()
    print("=" * 78)
    print("H_037 DEFINITIVE — hyperbolic {7,3} XY-MC vs square XY-MC at matched J")
    print("=" * 78)

    cut = args.bulk_ring_cut if args.bulk_ring_cut >= 0 else args.rings - 2
    nV_h, adj_h, deg_h, bulk_h, info = hyper_bulk_idx(args.rings, cut)
    print("hyperbolic {7,3}: rings=%d  nV=%d  deg_hist=%s"
          % (args.rings, nV_h, info["deg_hist"]))
    print("  bulk-ring-cut=%d  BULK vertices=%d  (f_bd=%.3f)"
          % (cut, info["nbulk"], info["f_bd"]))
    if info["nbulk"] < 8:
        print("  !! too few bulk sites; increase --rings");

    nV_s, adj_s, deg_s = build_square(args.Lsq)
    bulk_s = np.arange(nV_s)   # periodic: all sites bulk
    print("square (periodic): L=%d  nV=%d  (all bulk)" % (args.Lsq, nV_s))

    nbr_h, ptr_h = adj_to_csr(adj_h)
    nbr_s, ptr_s = adj_to_csr(adj_s)
    temps = np.linspace(args.tlo, args.thi, args.ntemp)
    print("temps:", " ".join("%.2f" % t for t in temps))
    print("therm=%d meas=%d meas_every=%d J=%.3f"
          % (args.therm, args.meas, args.meas_every, args.J))
    print("-" * 78)

    print("SQUARE lattice MC (matched bare J):")
    rows_s = run_lattice("square", nbr_s, ptr_s, nV_s, bulk_s, args.J,
                         temps, args.therm, args.meas, args.meas_every, args.seed)
    print("HYPERBOLIC {7,3} MC (BULK-only estimators, boundary excluded):")
    rows_h = run_lattice("hyp73", nbr_h, ptr_h, nV_h, bulk_h, args.J,
                         temps, args.therm, args.meas, args.meas_every,
                         args.seed + 777)

    Tcb_s, Tch_s = estimate_Tc(rows_s)
    Tcb_h, Tch_h = estimate_Tc(rows_h)
    print("-" * 78)
    print("SQUARE     T_c(binder)=%.3f  T_c(half-m)=%.3f" % (Tcb_s, Tch_s))
    print("HYP {7,3}  T_c(binder)=%.3f  T_c(half-m)=%.3f   [BULK only]" % (Tcb_h, Tch_h))
    r_b = Tcb_h / Tcb_s if Tcb_s else float('nan')
    r_h = Tch_h / Tch_s if Tch_s else float('nan')
    print("-" * 78)
    print("BULK  T_c^hyperbolic / T_c^square  at matched J :")
    print("   via Binder steepest-drop : %.3f" % r_b)
    print("   via half-magnetization   : %.3f" % r_h)
    print("   escape threshold >= 1.7  ;  honest-null <= 1.2")
    ratio_dec = max(r_b, r_h)   # most charitable to the escape
    if ratio_dec >= 1.7:
        verdict = "escapes-wall"
    elif ratio_dec <= 1.2:
        verdict = "confirms-wall"
    else:
        verdict = "inconclusive-band"
    print("   VERDICT (real MC, bulk)  : %s" % verdict)
    print("=" * 78)
    print("wall-clock: %.1f s" % (time.time() - t0))

    out = {"params": vars(args), "hyp": info, "square": {"nV": nV_s, "L": args.Lsq},
           "rows_square": rows_s, "rows_hyp": rows_h,
           "Tc_square_binder": Tcb_s, "Tc_square_half": Tch_s,
           "Tc_hyp_binder": Tcb_h, "Tc_hyp_half": Tch_h,
           "ratio_binder": r_b, "ratio_half": r_h, "verdict": verdict}
    with open(args.out, "w") as f:
        json.dump(out, f, indent=2)
    print("wrote", args.out)


if __name__ == "__main__":
    main()
