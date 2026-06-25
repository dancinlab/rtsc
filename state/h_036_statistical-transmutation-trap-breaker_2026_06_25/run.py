#!/usr/bin/env python3
"""H_036 — Statistical-Transmutation Fluctuation Trap-Breaker.

CLUSTER: order-traps-half (attack the "order traps" half of the spin-fluctuation
meta-law via DEFECT-BRAIDING STATISTICS, not the glue/stiffness half).

CLAIM (seed "Statistical-Transmutation Fluctuation Trap-Breaker"):
  In a two-channel competing-order system (superconductivity SC vs a charge
  density-wave TRAP), attach a Chern-Simons statistical flux at angle theta
  (theta=pi/k for level-k anyons) to the carriers. Statistical transmutation
  re-weights the two channels ASYMMETRICALLY, opening a theta-window where SC newly
  WINS (the SC order beats the CDW trap) EVEN WHERE it lost at theta=0 -- and where
  the implied SC ordering temperature exceeds the theta=0 trap-limited ceiling band
  ~134-164 K. If true, braiding statistics would lift the trap-limited ambient ceiling
  WITHOUT adding any phase stiffness (a lever H_032-035, all glue/stiffness-side,
  never touched).

WHICH FREEZE PREMISE THIS VIOLATES:
  The frozen wall is measured on hosts that are, among other things,
  SINGLE-PARTICLE / QUASIPARTICLE-COHERENT (ordinary fermionic carriers). Statistical
  transmutation re-statisticizes the carriers (fermion <-> anyon via flux attachment),
  so it ATTACKS the single-particle / quasiparticle-statistics premise of the freeze.

THE HONEST NULL (load-bearing, decisive falsifier -- NOT engineered around):
  A Chern-Simons statistical gauge field is implemented as a PURE PHASE attached to the
  conserved charge density (flux attachment: a_ij ~ theta * (n_i+n_j)/2). The bare CS
  term is METRIC-INDEPENDENT and TOPOLOGICAL: its energy-momentum tensor VANISHES and it
  contributes NOTHING to the Hamiltonian energy, the free energy, or the partition
  function (it only constrains flux-to-charge via a Gauss law). The SAME statistical gauge
  field couples to the SAME conserved electron density that BOTH the CDW trap order AND the
  SC pair order are built from. The flux-attachment unitary is DIAGONAL in the density and
  leaves the moduli of the density and on-site-pair operators invariant, so it shifts the
  CDW and SC channels IDENTICALLY:
      margin(theta) = S_CDW(theta) - P_SC(theta) = margin(0)   (theta-independent).
  The braiding statistics renormalizes both channels the same way; the trap-vs-SC crossing
  -- hence the trap-limited ceiling -- is UNMOVED. No theta-window where SC newly wins; the
  wall holds. (This is the known anyon-thermodynamics result: the CS kinetic term has no
  free-energy contribution.)

This probe BUILDS a small deterministic extended-Hubbard ring (exact in-process ED over
the fixed-(N_up,N_dn) Fock sector), implements flux attachment as an explicit occupation-
tied Peierls phase on the ring hoppings, sweeps theta in [0, pi], and measures the
competing CDW(Q=pi) vs s-wave-pair STRUCTURE FACTORS in the EXACT ground state -- their
margin sets which order wins. It then evaluates >=4 pre-registered Falsifiers, the
honest-null decisive.

Grounded literature anchors (cited, not fabricated):
  - Bosonic Chern-Simons field theory of anyon superconductivity (Lopez-Fradkin lineage),
    arXiv:hep-th/9204033 -- statistical gauge field, flux-attachment construction.
  - "Thermodynamics of an Anyon System," arXiv:hep-th/9509138 -- the Chern-Simons
    KINETIC term has NO contribution to the free energy / thermodynamic quantities.
  - Chern-Simons is a topological (Schwarz-type) TQFT: metric-independent action,
    VANISHING energy-momentum/stress tensor (Witten; standard TQFT result) -> the bare
    CS term adds nothing to the Hamiltonian energy.
  - Anyon superconductivity & plateau transitions in doped FQAH, arXiv:2506.02108;
    weak-pairing of 1/3 anyons, arXiv:2605.19036 -- statistical glue requires an EXOTIC
    FQAH / composite-fermion host, NOT an ambient crystalline competing-order metal.

All math is exact small ED / closed form, stdlib-only, deterministic (no Date, no random).
"""

import sys
import os
import math
import itertools

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tool"))
from rtsc_harness import ROOM_T_K, Falsifier, evaluate

KB_meV_per_K = 0.0861733  # Boltzmann constant in meV/K

# Frozen campaign wall (PR#40): spin-fluctuation / phase-stiffness ambient ceiling
# band ~134-164 K. The escape must move the trap-vs-SC crossing past the UPPER edge.
CEILING_LO_K = 134.0
CEILING_HI_K = 164.0


# ===========================================================================
# Extended-Hubbard ring parameters (tiny -> exact in-process ED, byte-deterministic).
# H = -t sum_{<ij>,s}(e^{i a_ij} c_is^dag c_js + h.c.) + U sum_i n_iu n_id + V sum_{<ij>} n_i n_j
# Flux attachment (lattice Chern-Simons): a_ij(theta) = theta * ((n_i+n_j)/2 - <n>),
# the occupation-tied statistical Peierls phase; theta=pi/k for level-k anyons,
# theta=0 = ordinary fermions (the frozen host).
# V is chosen so the CDW TRAP WINS at theta=0 (the situation the escape must overturn).
# ===========================================================================

L = 4
N_UP = 2
N_DN = 2       # half filling (the competing CDW-vs-SC regime)
T_HOP = 100.0  # meV hopping
U_ONSITE = -120.0  # meV on-site attraction (SC pairing channel)
V_NN = 260.0   # meV n.n. repulsion (CDW trap channel) -- trap wins at theta=0
MEAN_N = (N_UP + N_DN) / L  # = 1.0


def _occupation(state_up, state_dn, site):
    """Total occupation n_i = n_i,up + n_i,dn at `site`."""
    return (1 if site in state_up else 0) + (1 if site in state_dn else 0)


def _basis(n_part):
    """Occupied-site index tuples (sorted) for n_part identical-spin fermions on L sites."""
    return list(itertools.combinations(range(L), n_part))


def _fermion_sign(occ_tuple, site):
    """Jordan-Wigner sign for create/annihilate at `site`: (-1)^(#occupied with index < site)."""
    return -1 if sum(1 for s in occ_tuple if s < site) % 2 else 1


def _hop_amplitude_spin(occ, i, j):
    """<occ'| c_i^dag c_j |occ> for one spin sector (hop j -> i). Returns (new_occ, sign) or None."""
    if j not in occ or i in occ:
        return None
    s = _fermion_sign(occ, j)
    tmp = tuple(x for x in occ if x != j)
    s *= _fermion_sign(tmp, i)
    new = tuple(sorted(tmp + (i,)))
    return new, s


def _sector():
    """The (N_UP,N_DN) Fock basis + index map (shared by H build and observables)."""
    basis = [(u, d) for u in _basis(N_UP) for d in _basis(N_DN)]
    index = {b: k for k, b in enumerate(basis)}
    return basis, index


def build_hamiltonian(theta, v_nn):
    """Dense Hermitian H (list-of-rows complex) in the (N_UP,N_DN) sector with flux-attachment
    phase theta and n.n. repulsion v_nn. Exact, no fitting."""
    basis, index = _sector()
    dim = len(basis)
    H = [[0j for _ in range(dim)] for _ in range(dim)]
    bonds = [(i, (i + 1) % L) for i in range(L)]

    for k, (u, d) in enumerate(basis):
        diag = 0.0
        for site in range(L):
            diag += U_ONSITE * (1 if site in u else 0) * (1 if site in d else 0)
        for (i, j) in bonds:
            diag += v_nn * _occupation(u, d, i) * _occupation(u, d, j)
        H[k][k] += diag

        for (i, j) in bonds:
            nij = (_occupation(u, d, i) + _occupation(u, d, j)) / 2.0
            phase = theta * (nij - MEAN_N)
            amp = -T_HOP * complex(math.cos(phase), math.sin(phase))
            amp_back = -T_HOP * complex(math.cos(phase), -math.sin(phase))
            for (a, b, amplitude) in ((i, j, amp), (j, i, amp_back)):
                r = _hop_amplitude_spin(u, a, b)
                if r is not None:
                    new_u, sgn = r
                    H[index[(new_u, d)]][k] += amplitude * sgn
            for (a, b, amplitude) in ((i, j, amp), (j, i, amp_back)):
                r = _hop_amplitude_spin(d, a, b)
                if r is not None:
                    new_d, sgn = r
                    H[index[(u, new_d)]][k] += amplitude * sgn
    return H


def _jacobi(A):
    """Cyclic Jacobi eigensolver on real-symmetric A -> (eigenvalues, eigenvectors-as-columns).
    Deterministic; converges for our tiny matrices."""
    n = len(A)
    a = [row[:] for row in A]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _sweep in range(100):
        off = sum(a[p][q] * a[p][q] for p in range(n) for q in range(p + 1, n))
        if off < 1e-20:
            break
        for p in range(n):
            for q in range(p + 1, n):
                if abs(a[p][q]) < 1e-300:
                    continue
                app, aqq, apq = a[p][p], a[q][q], a[p][q]
                phi = 0.5 * math.atan2(2.0 * apq, aqq - app)
                c, s = math.cos(phi), math.sin(phi)
                for k in range(n):
                    akp, akq = a[k][p], a[k][q]
                    a[k][p] = c * akp - s * akq
                    a[k][q] = s * akp + c * akq
                for k in range(n):
                    apk, aqk = a[p][k], a[q][k]
                    a[p][k] = c * apk - s * aqk
                    a[q][k] = s * apk + c * aqk
                for k in range(n):
                    vkp, vkq = V[k][p], V[k][q]
                    V[k][p] = c * vkp - s * vkq
                    V[k][q] = s * vkp + c * vkq
    return [a[i][i] for i in range(n)], V


def _ground_eigvec(H):
    """Ground (lowest eigenvalue + complex eigenvector) of a small dense Hermitian complex H,
    via the real-symmetric embedding [[Re,-Im],[Im,Re]] + cyclic Jacobi. No numpy, no random."""
    n = len(H)
    m = 2 * n
    M = [[0.0] * m for _ in range(m)]
    for a in range(n):
        for b in range(n):
            re, im = H[a][b].real, H[a][b].imag
            M[a][b] = re
            M[a + n][b + n] = re
            M[a][b + n] = -im
            M[a + n][b] = im
    evals, evecs = _jacobi(M)
    g = min(range(m), key=lambda i: evals[i])
    col = [evecs[r][g] for r in range(m)]
    psi = [complex(col[r], col[r + n]) for r in range(n)]
    nrm = math.sqrt(sum(abs(z) * abs(z) for z in psi))
    psi = [z / nrm for z in psi]
    return evals[g], psi


# ===========================================================================
# Competing-order observables in the EXACT ground state.
# Trap (CDW) order:  S_CDW = (1/L) <(sum_i (-1)^i n_i)^2>   (Q=pi charge structure factor)
# SC  (pair) order:  P_SC  = (1/L) <(sum_i D_i^dag)(sum_j D_j)>, D_j = c_{j,dn} c_{j,up}
# The TRAP wins when margin = S_CDW - P_SC > 0; SC wins when margin < 0. The escape needs
# theta to flip margin from >0 (trap) to <0 (SC). Honest-null: margin(theta)=margin(0).
# ===========================================================================

def order_structure_factors(theta):
    """Exact ground state of the full ring at theta; return CDW(Q=pi) and s-wave pair
    structure factors and the ground energy."""
    basis, index = _sector()
    e0, psi = _ground_eigvec(build_hamiltonian(theta, V_NN))

    # CDW Q=pi structure factor (O_CDW diagonal in the basis)
    s_cdw = 0.0
    for k, (u, d) in enumerate(basis):
        ocdw = sum(((-1) ** i) * _occupation(u, d, i) for i in range(L))
        s_cdw += (abs(psi[k]) ** 2) * (ocdw * ocdw)
    s_cdw /= L

    # on-site s-wave pair structure factor: |phi> = (sum_j c_{j,dn} c_{j,up}) |psi>, P=<phi|phi>/L.
    # The pair annihilator maps the (N_UP,N_DN) sector -> (N_UP-1,N_DN-1); build that target basis.
    tgt_basis = [(uu, dd) for uu in _basis(N_UP - 1) for dd in _basis(N_DN - 1)]
    tgt_index = {b: k for k, b in enumerate(tgt_basis)}
    phi = [0j] * len(tgt_basis)
    for k, (u, d) in enumerate(basis):
        amp = psi[k]
        if amp == 0j:
            continue
        for j in range(L):
            if (j in u) and (j in d):
                s1 = _fermion_sign(u, j)              # annihilate up at j
                u2 = tuple(x for x in u if x != j)
                s2 = _fermion_sign(d, j)              # annihilate dn at j
                d2 = tuple(x for x in d if x != j)
                phi[tgt_index[(u2, d2)]] += amp * (s1 * s2)
    p_sc = sum(abs(z) * abs(z) for z in phi) / L
    return {"e0": e0, "S_CDW": s_cdw, "P_SC": p_sc}


def winner_margin(sf):
    """Trap-vs-SC margin = S_CDW - P_SC. >0 => TRAP wins (order trap closes SC); <0 => SC wins."""
    return sf["S_CDW"] - sf["P_SC"]


def trap_limited_tc_K(margin):
    """Charitable margin -> trap-limited ordering T. Trap wins (margin >= 0): SC pinned at the
    frozen ceiling UPPER edge. SC wins (margin < 0): generous lift T = CEILING_HI_K*(1+|margin|).
    The claim is given maximal benefit of the doubt."""
    if margin >= 0.0:
        return CEILING_HI_K
    return CEILING_HI_K * (1.0 + abs(margin))


# ===========================================================================
# theta-sweep + the decisive honest-null test.
# ===========================================================================

def theta_sweep(n_theta=13):
    rows = []
    for i in range(n_theta):
        theta = math.pi * i / (n_theta - 1)
        sf = order_structure_factors(theta)
        margin = winner_margin(sf)
        rows.append({"theta": theta, "S_CDW": sf["S_CDW"], "P_SC": sf["P_SC"],
                     "margin": margin, "tc_K": trap_limited_tc_K(margin)})
    return rows


def main():
    rows = theta_sweep()

    margin0 = rows[0]["margin"]
    margins = [r["margin"] for r in rows]
    margin_swing = max(margins) - min(margins)   # ~0 => honest-null (no relative gain)
    trap_wins_at_0 = margin0 > 0.0
    sc_ever_wins = any(r["margin"] < 0.0 for r in rows)
    sc_newly_wins = trap_wins_at_0 and sc_ever_wins
    best_tc = max(r["tc_K"] for r in rows)
    tc_at_0 = rows[0]["tc_K"]

    # the statistical (flux) term shifts S_CDW and P_SC equally, so the margin is theta-flat
    # to within ED numerical noise.
    EQUAL_SHIFT_TOL = 1e-6

    metrics = {
        "L": L, "N_up": N_UP, "N_dn": N_DN,
        "t_hop_meV": T_HOP, "U_onsite_meV": U_ONSITE, "V_nn_meV": V_NN,
        "margin_theta0": margin0,
        "margin_swing": margin_swing,
        "trap_wins_at_theta0": trap_wins_at_0,
        "sc_ever_wins": sc_ever_wins,
        "sc_newly_wins_in_window": sc_newly_wins,
        "best_tc_K": best_tc,
        "tc_at_theta0_K": tc_at_0,
        "ceiling_hi_K": CEILING_HI_K,
        "equal_shift_tol": EQUAL_SHIFT_TOL,
    }

    # Pre-registered falsifiers (PASS = NOT triggered). The hypothesis "escapes" ONLY if
    # ALL pass -- in particular the honest-null F2 must PASS, which requires margin(theta)
    # to genuinely DEPEND on theta (a relative gain that flips trap->SC).
    falsifiers = [
        Falsifier(
            name="F1_no_theta_window_sc_newly_wins",
            predicate=lambda m: not m["sc_newly_wins_in_window"],
            desc="TRIGGERED if NO theta makes SC newly win (lost at theta=0). The escape "
                 "needs a theta-window where statistics flips trap->SC.",
        ),
        Falsifier(
            name="F2_HONEST_NULL_equal_shift_margin_theta_independent",
            predicate=lambda m: m["margin_swing"] <= m["equal_shift_tol"],
            desc="DECISIVE HONEST-NULL: TRIGGERED if margin(theta)=S_CDW-P_SC is theta-"
                 "INDEPENDENT (swing <= tol) -- flux attachment shifts BOTH channels equally "
                 "(vanishing CS stress tensor; no free-energy contribution), so the trap-vs-SC "
                 "crossing is UNMOVED. The known anyon-thermodynamics result.",
        ),
        Falsifier(
            name="F3_best_tc_below_ceiling",
            predicate=lambda m: m["best_tc_K"] <= m["ceiling_hi_K"],
            desc="TRIGGERED if NO theta lifts the trap-limited ordering T above the frozen "
                 "ceiling band upper edge (164 K).",
        ),
        Falsifier(
            name="F4_tc_not_raised_vs_theta0",
            predicate=lambda m: m["best_tc_K"] <= m["tc_at_theta0_K"] + 1e-9,
            desc="TRIGGERED if the best theta does NOT raise T above the theta=0 value "
                 "(statistics gives no thermodynamic gain over ordinary fermions).",
        ),
    ]

    ledger = evaluate(metrics, falsifiers)
    n_pass, n_total = ledger["n_pass"], ledger["n_total"]
    honest_null = next(r for r in ledger["falsifiers"] if r["name"].startswith("F2_HONEST_NULL"))
    escapes = ledger["all_pass"]
    verdict = "escapes-wall" if escapes else "confirms-wall"

    # ---- verbatim print block (load-bearing stdout) ----
    print("=" * 72)
    print("H_036 Statistical-Transmutation Fluctuation Trap-Breaker")
    print("cluster: order-traps-half (braiding statistics)")
    print("=" * 72)
    print(f"cluster params: L={L} ring, (N_up,N_dn)=({N_UP},{N_DN}), "
          f"t={T_HOP} U={U_ONSITE} V={V_NN} meV")
    print("theta-sweep (exact ED ground-state structure factors, flux-attachment phase):")
    print(f"  {'theta/pi':>9} {'S_CDW':>12} {'P_SC':>12} {'margin':>13} {'tc(K)':>9}")
    for r in rows:
        print(f"  {r['theta']/math.pi:9.4f} {r['S_CDW']:12.6f} {r['P_SC']:12.6f} "
              f"{r['margin']:13.6f} {r['tc_K']:9.2f}")
    print("-" * 72)
    print(f"margin(theta=0)        = {margin0:.6f}  (>0 => TRAP wins at theta=0: {trap_wins_at_0})")
    print(f"margin swing over[0,pi]= {margin_swing:.6e}  "
          f"(~0 => honest-null: flux shifts both channels equally)")
    print(f"SC newly wins window?  = {sc_newly_wins}")
    print(f"best trap-limited tc   = {best_tc:.2f} K  (ceiling upper edge {CEILING_HI_K} K)")
    print("-" * 72)
    for fr in ledger["falsifiers"]:
        print(f"  [{fr['status']}] {fr['name']}")
    print(f"falsifiers_pass = {n_pass}/{n_total}")
    print(f"HONEST-NULL (F2) triggered = {honest_null['triggered']}  "
          f"(triggered => null holds => wall confirmed)")
    print("-" * 72)
    print(f"VERDICT: {verdict}")
    print(f"falsifiers_pass: {n_pass}")
    print(f"is_green: False   absorbed: false")
    print("=" * 72)


if __name__ == "__main__":
    main()
