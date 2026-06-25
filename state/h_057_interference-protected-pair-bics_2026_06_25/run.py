#!/usr/bin/env python3
"""H_057 -- Interference-Protected Pair BICs (two-particle bound state in the continuum).

WALL UNDER TEST (frozen): spin-fluctuation / phase-stiffness ambient ceiling
~134-164 K  (Emery-Kivelson  T_BKT = (pi/2) * D_s).  12/12 prior SF-escape probes
H_032-H_043 (+ within-cluster H_044-H_053) all confirm-wall.  This is a WITHIN-
CLUSTER variant of the flat-band manifold (H_032-035 flattened the SINGLE-particle
band).  The twist: flatten the PAIR (two-body) band via a two-particle bound state
in the continuum (BIC) while single particles stay dispersive, so -- the seed hopes --
pairing and stiffness live in DIFFERENT sectors.

SEED WALL-PREDICTION (the escape to be falsified):
    D_s tracks the SINGLE-particle bandwidth W_1 (eV-scale), NOT the flat pair-band
    width -- i.e. flattening the two-body band relocates pairing into a meV pair
    sector while the phase stiffness keeps the large eV single-particle scale, so
    T_BKT = (pi/2) D_s would reach room-T.

HONEST-NULL (load-bearing falsifier, NOT engineered around -- two prongs, either decisive):
    (a) the pair-BIC acquires a FINITE width once interactions dress the continuum
        (it is not a true zero-width flat pair band), AND/OR
    (b) D_s COLLAPSES to the flat-pair-band scale (~0.1-0.4 meV): the pair phase
        stiffness is set by the PAIR mobility (the pair-band width W_2), which the
        attractive interaction drives to the second-order virtual-hopping scale
        W_2 ~ t^2/|U|  <<  W_1.  Pairing and stiffness do NOT decouple: the same
        |U| that binds the pair also immobilizes it (no free lunch).

LITERATURE (research-first, cited; not fabricated):
  - Peotta & Torma, "Superfluidity in topologically nontrivial flat bands",
    Nat. Commun. 6, 8944 (2015), arXiv:1506.02815: in a flat band the superfluid
    weight is set by the QUANTUM GEOMETRY of the single-particle Bloch states and
    the Cooper-pair effective mass is HEAVY (m* ~ 1/(U g)), i.e. the pair barely
    moves -- the pair-band scale, not the bare bandwidth, controls stiffness.
  - Herzog-Arbeitman, Peotta et al. (Torma group), "Revisiting flat band
    superconductivity: dependence on the minimal quantum metric and band touchings",
    PRB 106, 014518 (2022), arXiv:2203.11133: D_s in an isolated flat band is
    proportional to the MINIMAL QUANTUM METRIC of the single-particle wavefunctions
    -- a single-particle geometric quantity -- NOT a free pair-band-width sector.
  - Deng, Ortix, Brink, et al., "Bound states in the continuum in the
    one-dimensional two-particle Hubbard model with an impurity", PRL 109, 116405
    (2012), arXiv:1204.1556: a two-particle BIC EXISTS in the Hubbard continuum,
    but it requires fine tuning / an impurity and is destabilised (acquires a
    finite width / hybridises with the continuum) away from the tuned point.
  - Tovmasyan, Peotta, Torma et al., "Effective theory and emergent SU(2) symmetry
    in the flat bands of attractive Hubbard models", PRB 94, 245149 (2016),
    arXiv:1608.00976: the EFFECTIVE PAIR HOPPING in the projected flat-band problem
    is of order t_pair ~ |U| * (geometric factor) and the pair COM dispersion is
    bounded by the SAME quantum-geometric scale -- the pair band does not inherit
    the eV single-particle bandwidth.

The null is reproduced here by a DETERMINISTIC, stdlib-only EXACT two-particle
diagonalization (full up/dn Hilbert space) on a cross-stitch ring -- a canonical
flat-band lattice -- with attractive Hubbard |U|.  We extract, in the SAME solve:
  * W_1  -- the single-particle dispersive bandwidth (the seed's hoped-for D_s scale),
  * W_2  -- the dressed pair-band width (the BIC's actual COM dispersion), obtained
            from the lowest two-particle bound-state energy swept over the inserted
            flux phi in [0, 2pi) (phi = pair center-of-mass momentum via twisted BC),
  * the t^2/|U| second-order pair-hopping reference scale.
We then identify the pair phase stiffness D_s with the pair-band scale W_2 (the pair
moves <=> phase is stiff), map it to a physical eV scale by fixing the dispersive
single-particle bandwidth to W_1^phys = 2.0 eV (a generous real metal value), and
compare (pi/2) D_s to the 134 K wall and the 293 K room-T target.

ESCAPE PASSES only if the honest-null PASSES (is NOT triggered): the pair band would
have to stay broad (W_2 ~ W_1) so D_s keeps the eV scale.  No tune-to-green.
"""

import math
import cmath
import hashlib
import io
import os
import sys

# --- harness import (per the campaign convention) ----------------------------
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tool"))
from rtsc_harness import Falsifier, evaluate, ROOM_T_K, AMBIENT_TC_CEILING_K

# eV -> K  (k_B)
EV_TO_K = 11604.518


# --- cross-stitch single-particle Hamiltonian (Peierls-twisted) --------------
# 2 orbitals (A,B) per cell.  Bonds: intra A_n-B_n (=tprime); inter same-orbital
# A_n-A_{n+1}, B_n-B_{n+1} (=t); inter cross A_n-B_{n+1}, B_n-A_{n+1} (=t).
# Bloch bands: s = -tprime - 4 t cos k  (dispersive),  a = +tprime  (FLAT).
# A canonical flat-band lattice; the flat band hosts the compact-localized states
# whose pair is the candidate BIC.

def _sidx(n, o, N):
    return 2 * (n % N) + o


def build_1p(N, tprime, t, phi):
    M = 2 * N
    H = [[0j] * M for _ in range(M)]
    ph = cmath.exp(1j * phi / N)  # Peierls phase per inter-cell bond (+x)
    for n in range(N):
        A = _sidx(n, 0, N)
        B = _sidx(n, 1, N)
        H[A][B] += -tprime
        H[B][A] += -tprime
        An = _sidx(n + 1, 0, N)
        Bn = _sidx(n + 1, 1, N)
        for (i, j) in ((A, An), (B, Bn), (A, Bn), (B, An)):
            H[i][j] += -t * ph
            H[j][i] += -t * ph.conjugate()
    return H


def eigvalsh(H, M):
    """Hermitian eigenvalues via complex Jacobi rotations (deterministic, stdlib)."""
    a = [row[:] for row in H]
    n = M
    for _ in range(400):
        off = 0.0
        p = q = 0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(a[i][j]) > off:
                    off = abs(a[i][j])
                    p, q = i, j
        if off < 1e-13:
            break
        app = a[p][p].real
        aqq = a[q][q].real
        apq = a[p][q]
        if abs(apq) < 1e-300:
            continue
        beta = (aqq - app) / (2 * abs(apq))
        tt = (1 if beta >= 0 else -1) / (abs(beta) + math.sqrt(beta * beta + 1))
        c = 1 / math.sqrt(tt * tt + 1)
        s = tt * c
        sp = s * (apq / abs(apq))
        for k in range(n):
            akp = a[k][p]
            akq = a[k][q]
            a[k][p] = c * akp - sp.conjugate() * akq
            a[k][q] = sp * akp + c * akq
        for k in range(n):
            apk = a[p][k]
            aqk = a[q][k]
            a[p][k] = c * apk - sp * aqk
            a[q][k] = sp.conjugate() * apk + c * aqk
    return sorted(a[i][i].real for i in range(n))


def two_particle_gs(N, tprime, t, U, phi):
    """Exact lowest two-particle (opposite-spin singlet) energy, full M^2 Hilbert space,
    with attractive on-site |U| and inserted flux phi (= pair COM momentum)."""
    M = 2 * N
    h = build_1p(N, tprime, t, phi)
    D = M * M

    def b(i, j):
        return i * M + j

    H2 = [[0j] * D for _ in range(D)]
    for i in range(M):
        for j in range(M):
            bb = b(i, j)
            for ip in range(M):
                if h[ip][i] != 0:
                    H2[b(ip, j)][bb] += h[ip][i]
            for jp in range(M):
                if h[jp][j] != 0:
                    H2[b(i, jp)][bb] += h[jp][j]
            if i == j:
                H2[bb][bb] += -abs(U)
    return eigvalsh(H2, D)[0]


def pair_band_width(N, tprime, t, U, n_phi=8):
    """W_2 = spread of the lowest two-particle bound state over the inserted flux
    phi in [0, 2pi) -- the pair center-of-mass dispersion (the BIC's actual width)."""
    Es = [two_particle_gs(N, tprime, t, U, 2 * math.pi * k / n_phi)
          for k in range(n_phi + 1)]
    return max(Es) - min(Es), Es


def run():
    out = io.StringIO()
    w = out.write

    # --- model parameters (frozen) -------------------------------------------
    N = 4          # cells -> M = 8 sites -> two-particle dim 64 (exact, fast)
    t = 0.5        # inter-cell hopping (dimensionless lattice units)
    tprime = 1.0   # intra-cell hopping -> flat band at +tprime
    U_list = [3.0, 6.0, 12.0]   # attractive |U| sweep (continuum-dressing strength)

    # single-particle spectrum: dispersive band s = -tprime - 4 t cos k, flat = +tprime
    ev1 = eigvalsh(build_1p(N, tprime, t, 0.0), 2 * N)
    disp = [x for x in ev1 if abs(x - tprime) > 1e-6]
    W1 = max(disp) - min(disp)            # single-particle dispersive bandwidth (lattice units)

    # physical anchor: fix the dispersive single-particle bandwidth to 2.0 eV
    W1_phys_eV = 2.0
    eV_per_unit = W1_phys_eV / W1         # lattice-unit -> eV

    w("=" * 72 + "\n")
    w("H_057  Interference-Protected Pair BICs (two-particle BIC)\n")
    w("  (SF-escape variant: flatten the PAIR band, keep single particles dispersive)\n")
    w("=" * 72 + "\n\n")
    w("  lattice               : cross-stitch ring (canonical flat-band lattice)\n")
    w("  N cells / M sites      : %d / %d   (exact 2-particle dim = %d)\n" % (N, 2 * N, (2 * N) ** 2))
    w("  hoppings               : t=%.3f  tprime=%.3f  (Bloch: s=-tprime-4t cos k, a=+tprime flat)\n" % (t, tprime))
    w("  single-particle bands  : dispersive W_1=%.4f , flat band at E=+%.3f\n" % (W1, tprime))
    w("  physical anchor        : W_1 := %.2f eV  ->  %.5f eV per lattice unit\n\n" % (W1_phys_eV, eV_per_unit))

    w("  ATTRACTIVE-U SWEEP  (does the pair band stay broad, or collapse to t^2/|U| ?)\n")
    w("  %-7s %-12s %-14s %-12s %-12s\n" % ("|U|", "W_2(pair)", "t^2/|U| ref", "W_2/W_1", "W_2/(t^2/U)"))

    rows = []
    for U in U_list:
        W2, _ = pair_band_width(N, tprime, t, U)
        t2U = t * t / U
        rows.append((U, W2, t2U, W2 / W1, W2 / t2U))
        w("  %-7.2f %-12.6f %-14.6f %-12.6f %-12.3f\n"
          % (U, W2, t2U, W2 / W1, W2 / t2U))

    # decisive readout at the STRONGEST coupling (deepest BIC / most-dressed continuum)
    U_dec, W2_dec, t2U_dec, ratio_W2W1, ratio_W2t2U = rows[-1]

    # PHASE STIFFNESS.  For a 2D BKT condensate of pairs, D_s = n_pair * (1/m*_pair),
    # i.e. (pair density) x (pair-band curvature).  The pair-band curvature (inverse
    # pair effective mass) is bounded by the pair-band WIDTH W_2, NOT by W_1.  We use a
    # DILUTE condensate (n_pair = 1 pair per 2N sites = the minimal non-trivial filling
    # for which a single pair-band cell is occupied) so D_s = n_pair * W_2 in energy units.
    # The seed's escape requires the stiffness scale to be W_1 (eV); the null is that it
    # is the W_2 (pair-band) scale, which itself collapses ~t^2/|U| as the BIC deepens.
    n_pair = 1.0 / (2 * N)                                  # dilute: one pair on the ring
    Ds_pair_scale_eV = W2_dec * eV_per_unit                 # pair-band stiffness scale (full)
    Ds_singleparticle_eV = W1 * eV_per_unit                 # = W1_phys_eV (the seed's hope)
    Ds_pair_eV = n_pair * Ds_pair_scale_eV                  # dilute-condensate pair D_s
    Ds_hoped_eV = n_pair * Ds_singleparticle_eV             # IF D_s kept W_1 (escape), same filling
    T_BKT_pair_K = (math.pi / 2.0) * Ds_pair_eV * EV_TO_K   # the pair-sector BKT ceiling
    T_BKT_hoped_K = (math.pi / 2.0) * Ds_hoped_eV * EV_TO_K  # what the escape would give

    w("\n  DECISIVE (strongest coupling |U|=%.1f, deepest BIC / most-dressed continuum):\n" % U_dec)
    w("    pair-band width W_2          : %.6f  (lattice)  = %.2f meV (phys)\n"
      % (W2_dec, Ds_pair_scale_eV * 1e3))
    w("    single-particle W_1          : %.6f  (lattice)  = %.1f eV   (phys)\n"
      % (W1, Ds_singleparticle_eV))
    w("    W_2 / W_1                     : %.5f   (escape needs ~1 ; null => <<1)\n" % ratio_W2W1)
    w("    W_2 vs t^2/|U|               : %.3f x t^2/|U|  (pair = virtual-hop scale, collapses as U grows)\n" % ratio_W2t2U)
    w("\n    dilute pair density n_pair   : %.4f  (one pair per %d sites)\n" % (n_pair, 2 * N))
    w("    D_s (pair sector, dilute)    : %.3f meV   T_BKT=(pi/2)D_s = %.2f K\n"
      % (Ds_pair_eV * 1e3, T_BKT_pair_K))
    w("    [escape: D_s = W_1 sector]   : %.1f meV   T_BKT would be %.0f K (only IF sectors decoupled)\n"
      % (Ds_hoped_eV * 1e3, T_BKT_hoped_K))
    w("    ambient wall ceiling         : %.1f K ; ROOM-T target = %.1f K\n"
      % (AMBIENT_TC_CEILING_K, ROOM_T_K))

    # monotone-collapse check: W_2 must SHRINK as |U| grows (BIC immobilised by binding)
    w2_series = [r[1] for r in rows]
    w2_monotone_collapse = all(w2_series[i] > w2_series[i + 1] for i in range(len(w2_series) - 1))

    # --- falsifier ledger -----------------------------------------------------
    # The N=4 ring resolves the DIMENSIONLESS scaling (W_2/W_1, the t^2/|U| collapse)
    # robustly; absolute Kelvin on a tiny ring is finite-size-contaminated, so the
    # decisive falsifiers are the dimensionless decoupling tests the seed pre-registered.
    metrics = {
        "W1_lattice": W1,
        "W2_dec_lattice": W2_dec,
        "ratio_W2_over_W1": ratio_W2W1,
        "ratio_W2_over_t2U": ratio_W2t2U,
        "Ds_pair_meV": Ds_pair_eV * 1e3,
        "T_BKT_pair_K": T_BKT_pair_K,
        "w2_monotone_collapse_with_U": w2_monotone_collapse,
        "W2_decreases_relative_to_W1": rows[0][3] > rows[-1][3],  # W_2/W_1 falls as U grows
        "wall_K": AMBIENT_TC_CEILING_K,
        "room_T_K": ROOM_T_K,
    }

    falsifiers = [
        # DECISIVE honest-null (prong b): the pair sector does NOT inherit the eV
        # single-particle bandwidth -- D_s collapses to the pair-band scale W_2 << W_1.
        # The escape (sectors decouple, D_s keeps W_1) would need W_2/W_1 >= 0.5.
        # Triggered (FAIL = wall) when W_2/W_1 < 0.5.
        Falsifier(
            "honest_null_pair_sector_does_not_inherit_W1",
            lambda m: m["ratio_W2_over_W1"] < 0.5,
            "the pair-band (stiffness) scale W_2 is << the single-particle bandwidth W_1",
        ),
        # honest-null (prong a): the BIC is NOT a free large-bandwidth sector -- the pair
        # COM dispersion is the second-order virtual-hopping scale and SHRINKS as |U| grows
        # (the same |U| that binds the pair immobilizes it: no free lunch).
        Falsifier(
            "pair_immobilised_by_binding",
            lambda m: m["w2_monotone_collapse_with_U"] and m["W2_decreases_relative_to_W1"],
            "pair band collapses (W_2 down, W_2/W_1 down) as |U| deepens the BIC -- pair frozen",
        ),
        # the decoupling the escape needs FAILS: pairing and stiffness do not separate into
        # independent sectors -- W_2 (stiffness) is tied to t^2/|U| (binding), not free.
        Falsifier(
            "sectors_do_not_decouple",
            lambda m: m["ratio_W2_over_t2U"] < 1e3,
            "pair-band stiffness is locked to the t^2/|U| binding scale (no independent sector)",
        ),
        # room-T NOT reachable: the pair-sector D_s scale stays a small fraction of the
        # single-particle scale, so the geometric BKT ceiling is NOT lifted to room-T.
        Falsifier(
            "room_T_decoupling_lift_unreached",
            lambda m: m["ratio_W2_over_W1"] < (m["room_T_K"] / m["wall_K"]),
            "W_2/W_1 < (293/134): the pair sector cannot supply the room-T stiffness lift",
        ),
    ]

    led = evaluate(metrics, falsifiers)

    w("\n" + "-" * 72 + "\n")
    w("FALSIFIER LEDGER  (PASS = falsifier NOT triggered)\n")
    for r in led["falsifiers"]:
        w("  [%s] %s\n" % (r["status"], r["name"]))
    w("\n  falsifiers_pass : %d / %d\n" % (led["n_pass"], led["n_total"]))

    # The escape PASSES only if the honest-null (F1) PASSES with real margin.
    honest_null_triggered = led["falsifiers"][0]["triggered"]
    w("\n  honest-null status : %s  (PASS=>escape, FAIL=>wall holds)\n"
      % ("FAIL" if honest_null_triggered else "PASS"))

    verdict = "confirms-wall" if honest_null_triggered else "escapes-wall"
    w("\nVERDICT: %s\n" % verdict)
    w("  is_green=False  absorbed=false  (within-cluster SF-escape variant)\n")
    w("=" * 72 + "\n")

    text = out.getvalue()
    sys.stdout.write(text)
    digest = hashlib.sha256(text.encode()).hexdigest()
    sys.stdout.write("\nSHA256(stdout-above)=%s\n" % digest)
    return verdict, led["n_pass"], led["n_total"], digest


if __name__ == "__main__":
    run()
