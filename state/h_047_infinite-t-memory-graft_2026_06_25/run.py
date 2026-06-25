#!/usr/bin/env python3
"""H_047 — Infinite-T Memory Graft (subsystem-code symmetry that does not melt).

CLUSTER: code-/symmetry-protected order-class (attack the BKT/energetic order-trap
mechanism by replacing energetic, stiffness-limited order with a CONSERVED subsystem-
code symmetry charge that has, by theorem, no finite melting temperature). This is a
WITHIN-CLUSTER VARIANT of the carded H_043 "Vortex-Code Phase Lock" (also code/
symmetry-protected order at fixed D_s) and of H_036 (a [S,H] flux-attachment commutator
test). The specific twist tested here: the order is not energetic at all -- it is a
SUBSYSTEM (gauge-like, sub-extensive) symmetry charge, the kind that in fracton/
subsystem-code language "does not melt" up to infinite T. The question is whether the
charge-2e coupling that makes it a SUPERCONDUCTOR preserves that protecting symmetry.

CLAIM (seed "Infinite-T Memory Graft"):
  Build a subsystem-code Hamiltonian H_code (Z2xZ2 row/column subsystem symmetries --
  the plaquette/Xu-Moore class, whose generators S_row, S_col are NOT global but
  sub-extensive line operators). The logical operator of that code is the order
  parameter. Augment H_code with a pair-hopping term that ties the logical operator
  to a charge-2e bilinear b_i^dag b_j (b_i = c_{i,dn} c_{i,up}) so the ordered phase is
  a SUPERCONDUCTOR. Because the protecting symmetry is a conserved subsystem charge with
  no finite melting T by theorem (generalized Elitzur / dimensional-reduction), the
  logical (= order-parameter) autocorrelation C(t) should show NO Arrhenius decay and
  NO finite-T cusp up to the lattice cutoff -- a room-T-robust condensate that bypasses
  the (pi/2)D_s energetic phase-stiffness ceiling entirely.

WHICH FREEZE PREMISE THIS VIOLATES:
  The frozen wall T_BKT = (pi/2)D_s is measured on EQUILIBRIUM hosts whose order is an
  energetic condensate whose melting is set by the free energy (vortex/spin-wave
  proliferation). This probe attacks the EQUILIBRIUM / energetic-order-trap premise:
  it tries to host the order in a topological/subsystem-conserved sector that is, by
  construction, decoupled from the free-energy melting argument.

THE HONEST NULL (load-bearing, decisive falsifier -- CRUX, tested FIRST, NOT engineered
around):
  Adding the charge-2e pair-hopping coupling that makes the code a SUPERCONDUCTOR makes
  the protecting subsystem-symmetry generator FAIL to commute with H:
      [S_row, H] != 0  and/or  [S_col, H] != 0.
  Reason (analytic, then checked exactly): the subsystem generators of the plaquette/
  Xu-Moore code are products of sigma^x along a row or column; the charge-2e pair
  operator b_i^dag = c_{i,up}^dag c_{i,dn}^dag is, in the code's logical encoding, a
  sigma^z-type (logical-flip) operator. A sigma^z ANTICOMMUTES with the sigma^x line
  generator that passes through site i, so the pair-hopping bilinear that creates the
  condensate ANTICOMMUTES with (hence does NOT commute with) the very subsystem charge
  that was supposed to protect it. The literature result is decisive: ANY term
  anticommuting with a subsystem symmetry destroys the subsystem-protected order for any
  finite coupling (Devakul-You-Burnell-Sondhi; You-Devakul-Burnell-Sondhi). So the
  conserved quantity is destroyed by the coupling that makes it a superconductor, the
  protection evaporates, and the order reverts to a finite-T ENERGETIC condensate -- now
  bounded again by the (pi/2)D_s phase-stiffness ceiling. The wall applies.

  BACKSTOP (even charitably granting [S,H]=0): the protecting symmetry of this code is a
  d_sub=1 (line) subsystem symmetry, and by the generalized Elitzur theorem / dimensional
  reduction (Batista-Nussinov cond-mat/0410599; Nussinov-Ortiz Ann.Phys.324,977) a
  d_sub<=2 subsystem symmetry CANNOT spontaneously break at any finite T -- so the
  "logical order parameter" cannot acquire a finite-T condensate at all (T_order=0), OR
  the order that does survive is a higher-dimensional ENERGETIC one (the plaquette-Ising
  first-order T_c ~ 0.55 J in 3D), i.e. an energetic condensate bounded by J = D_s again.
  Either branch -> confirm-wall.

This probe BUILDS the explicit 4-site (2x2 plaquette) subsystem-code Hamiltonian with
Z2xZ2 row/column subsystem generators, augments it with a charge-2e pair-hopping term at
coupling g, and EXACTLY computes:
  (1) CRUX: ||[S_row,H(g)]|| and ||[S_col,H(g)]|| as g is turned on (the honest-null:
      a nonzero commutator means the protecting charge is destroyed by the SC coupling);
  (2) the logical-operator autocorrelation C(t) = <O_L(t) O_L(0)> in the exact spectrum
      and whether it shows a finite-T cusp / Arrhenius decay (energetic) vs flat (protected);
  (3) the resulting ordering temperature vs the (pi/2)D_s energetic ceiling and the wall.
It then evaluates >=4 pre-registered Falsifiers, the crux honest-null F1 decisive.

Grounded literature anchors (cited, not fabricated; verified via web search 2026-06-25):
  - Z. Nussinov, G. Ortiz, "A symmetry principle for topological quantum order,"
    Ann. Phys. 324, 977 (2009), arXiv:cond-mat/0702377 -- subsystem (gauge-like, d-
    dimensional) symmetries, dimensional reduction, T_c bounded by a lower-d model.
  - C. D. Batista, Z. Nussinov, "Generalized Elitzur's theorem and dimensional
    reduction," Phys. Rev. B 72, 045137 (2005), arXiv:cond-mat/0410599 -- a d<=2
    subsystem (intermediate) symmetry cannot break spontaneously => no finite-T order.
  - T. Devakul, Y. You, F. J. Burnell, S. L. Sondhi, "Fractal Symmetric Phases of
    Matter," SciPost Phys. 6, 007 (2019), arXiv:1805.04097; Y. You, T. Devakul,
    F. J. Burnell, S. L. Sondhi, "Subsystem symmetry protected topological order,"
    Phys. Rev. B 98, 035112 (2018), arXiv:1803.02369 -- a perturbation anticommuting
    with the subsystem symmetry destroys the SSPT order at any finite coupling.
  - R. Moessner, S. L. Sondhi, plaquette (Xu-Moore) Ising; D. A. Johnston et al.,
    "Macroscopic degeneracy and order in the 3d plaquette Ising model," arXiv:1507.05784
    -- the plaquette/subsystem Ising orders at a FINITE first-order T_c ~ 0.55 J (an
    ENERGETIC transition; the subsystem symmetry does NOT give infinite-T protection of
    a thermodynamic order parameter).

All math is exact small ED / closed form, stdlib-only, deterministic (no Date, no random).
"""

import sys
import os
import math
import cmath

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tool"))
from rtsc_harness import ROOM_T_K, Falsifier, evaluate

KB_meV_per_K = 0.0861733  # Boltzmann constant in meV/K

# Frozen campaign wall (PR#40): spin-fluctuation / phase-stiffness ambient ceiling
# band ~134-164 K. The escape must move the ordering T past the UPPER edge WITHOUT
# the order being an energetic condensate bounded by (pi/2)D_s.
CEILING_LO_K = 134.0
CEILING_HI_K = 164.0

# Frozen flat-band geometric phase stiffness window (meV), carried from H_043/the freeze.
DS_LO_meV = 0.06
DS_HI_meV = 0.44

# ===========================================================================
# 4-site (2x2 plaquette) subsystem-code spin-1/2 model. Sites laid out as:
#     0 -- 1     (row R0 = {0,1})      (col C0 = {0,2})
#     |    |
#     2 -- 3     (row R1 = {2,3})      (col C1 = {1,3})
#
# Subsystem code Hamiltonian (Xu-Moore / plaquette class): the single plaquette term is
#     H_code = -K * X0 X1 X2 X3            (the 4-body plaquette stabilizer)
# whose PROTECTING subsystem symmetries are the ROW and COLUMN line operators built from
# sigma^z:   S_R0 = Z0 Z1, S_R1 = Z2 Z3, S_C0 = Z0 Z2, S_C1 = Z1 Z3.
# (These are the sub-extensive "gauge-like" generators: each flips a whole line; they all
# commute with the plaquette X-stabilizer, [S, H_code] = 0, since each line shares an EVEN
# number of sites with the plaquette.) Z2 x Z2 = {row parity} x {column parity}.
#
# LOGICAL / order-parameter operator of the encoded qubit: O_L = Z0 (a single sigma^z,
# the variable the subsystem symmetry is supposed to protect from melting).
#
# SC GRAFT: tie the logical to a charge-2e pair bilinear. In the spin->hardcore-boson
# encoding the on-site pair operator b_i (= c_{i,dn} c_{i,up}) maps to a sigma^- /
# sigma^+ (a sigma^x +- i sigma^y), i.e. a transverse (logical-FLIP) operator. The
# charge-2e pair-hopping term that condenses the SC is
#     H_SC(g) = -g * sum_<ij> ( b_i^dag b_j + h.c. )  ->  -g * sum_<ij> ( S+_i S-_j + h.c. )
# = -g * sum_<ij> ( X_i X_j + Y_i Y_j )/2   (XY pair-hopping; a sigma^x/sigma^y bilinear).
# This is the coupling that makes it a superconductor.
#
# H(g) = H_code + H_SC(g).
# CRUX: a sigma^x/sigma^y bilinear ANTICOMMUTES with the sigma^z line generators on the
# sites it touches, so [S_row, H(g)] and [S_col, H(g)] become NONZERO for g != 0. Tested
# exactly below (no hand-waving).
# ===========================================================================

K_PLAQ = 100.0   # meV plaquette-stabilizer strength (the code energy scale)
NSITE = 4
DIM = 1 << NSITE  # 16

ROWS = [(0, 1), (2, 3)]
COLS = [(0, 2), (1, 3)]
NN_BONDS = [(0, 1), (2, 3), (0, 2), (1, 3)]  # plaquette nearest-neighbour bonds

# ---- single-qubit Pauli action on a computational basis state (bit string) ----
# Convention: basis state = integer, bit b at site i = (state >> i) & 1 ; bit=1 => |1> (down,
# eigenvalue -1 of Z); bit=0 => |0> (up, +1 of Z).

def _z_eig(state, i):
    return 1.0 if ((state >> i) & 1) == 0 else -1.0

def _flip(state, i):
    return state ^ (1 << i)

# Apply X_i: |s> -> |s flip i> with amplitude 1.
def apply_X(vec, i):
    out = [0j] * DIM
    for s in range(DIM):
        a = vec[s]
        if a != 0j:
            out[_flip(s, i)] += a
    return out

# Apply Y_i: Y = i * X * Z ; Y|0>=i|1>, Y|1>=-i|0>. So Y_i|s> = i*(+1 if bit0 else -1)|flip>.
def apply_Y(vec, i):
    out = [0j] * DIM
    for s in range(DIM):
        a = vec[s]
        if a != 0j:
            sign = 1.0 if ((s >> i) & 1) == 0 else -1.0  # |0>-> i|1>, |1>-> -i|0>
            out[_flip(s, i)] += a * complex(0.0, sign)
    return out

# Apply Z_i.
def apply_Z(vec, i):
    return [vec[s] * _z_eig(s, i) for s in range(DIM)]

# ---- build dense operators as 16x16 complex matrices (columns = images of basis e_s) ----

def _basis_vec(s):
    v = [0j] * DIM
    v[s] = 1.0 + 0j
    return v

def op_from_apply(apply_chain):
    """Build the dense matrix of an operator given as a function vec->vec (applied to each
    basis column)."""
    M = [[0j] * DIM for _ in range(DIM)]
    for s in range(DIM):
        col = apply_chain(_basis_vec(s))
        for r in range(DIM):
            M[r][s] = col[r]
    return M

def matadd(A, B, sa=1.0, sb=1.0):
    return [[sa * A[r][c] + sb * B[r][c] for c in range(DIM)] for r in range(DIM)]

def matmul(A, B):
    C = [[0j] * DIM for _ in range(DIM)]
    for r in range(DIM):
        Ar = A[r]
        Cr = C[r]
        for k in range(DIM):
            a = Ar[k]
            if a != 0j:
                Bk = B[k]
                for c in range(DIM):
                    Cr[c] += a * Bk[c]
    return C

def frob_norm(M):
    return math.sqrt(sum((abs(M[r][c]) ** 2) for r in range(DIM) for c in range(DIM)))


# ---- the code stabilizer X0 X1 X2 X3 ----
def apply_plaquette(vec):
    v = vec
    for i in range(NSITE):
        v = apply_X(v, i)
    return v

# ---- subsystem generators S = product of Z over a line ----
def apply_line_Z(vec, sites):
    v = vec
    for i in sites:
        v = apply_Z(v, i)
    return v

# ---- charge-2e pair-hopping bilinear on a bond: (X_i X_j + Y_i Y_j)/2 ----
def apply_pairhop_bond(vec, i, j):
    xx = apply_X(apply_X(vec, j), i)
    yy = apply_Y(apply_Y(vec, j), i)
    return [0.5 * (xx[s] + yy[s]) for s in range(DIM)]


def build_H(g):
    """H(g) = -K * (X0X1X2X3) - g * sum_<ij> (X_iX_j + Y_iY_j)/2  as a dense 16x16 matrix."""
    # code term
    Hc = op_from_apply(apply_plaquette)
    Hc = [[-K_PLAQ * Hc[r][c] for c in range(DIM)] for r in range(DIM)]
    # SC pair-hopping term
    Hsc = [[0j] * DIM for _ in range(DIM)]
    for (i, j) in NN_BONDS:
        Bij = op_from_apply(lambda v, i=i, j=j: apply_pairhop_bond(v, i, j))
        Hsc = matadd(Hsc, Bij, 1.0, 1.0)
    Hsc = [[-g * Hsc[r][c] for c in range(DIM)] for r in range(DIM)]
    return matadd(Hc, Hsc, 1.0, 1.0)


def commutator_norm(S_apply, H):
    """||[S, H]||_Frobenius for a line-generator S (given as an apply function) and dense H."""
    S = op_from_apply(S_apply)
    SH = matmul(S, H)
    HS = matmul(H, S)
    comm = matadd(SH, HS, 1.0, -1.0)
    return frob_norm(comm)


# ===========================================================================
# Hermitian eigensolver (cyclic Jacobi on the real-symmetric embedding) -- reused idiom
# from H_036, deterministic, stdlib-only.
# ===========================================================================

def _jacobi_real_sym(A):
    n = len(A)
    a = [row[:] for row in A]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _sweep in range(200):
        off = sum(a[p][q] * a[p][q] for p in range(n) for q in range(p + 1, n))
        if off < 1e-22:
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


def eigh_complex(H):
    """Eigenvalues + eigenvectors (complex) of a small dense Hermitian H via the real
    embedding [[Re,-Im],[Im,Re]]. Returns (evals_sorted, evecs_complex_columns)."""
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
    evals, evecs = _jacobi_real_sym(M)
    # The real embedding doubles every eigenvalue; take each distinct pair once (lowest n).
    order = sorted(range(m), key=lambda i: evals[i])
    chosen = order[0:m:2]  # every other one after sorting -> n eigenpairs
    out_vals = []
    out_vecs = []
    for idx in chosen:
        out_vals.append(evals[idx])
        col = [evecs[r][idx] for r in range(m)]
        psi = [complex(col[r], col[r + n]) for r in range(n)]
        nrm = math.sqrt(sum(abs(z) * abs(z) for z in psi))
        psi = [z / nrm for z in psi]
        out_vecs.append(psi)
    return out_vals, out_vecs


def mat_vec(M, v):
    return [sum(M[r][c] * v[c] for c in range(len(v))) for r in range(len(M))]


def expect(M, v):
    Mv = mat_vec(M, v)
    return sum(v[r].conjugate() * Mv[r] for r in range(len(v)))


# ===========================================================================
# Logical-operator autocorrelation C(t) at temperature T (canonical ensemble) and its
# finite-T behaviour. O_L = Z0 (the protected logical variable).
#   C(t;T) = (1/Z) sum_{m,n} e^{-beta E_m} <m|O_L|n><n|O_L|m> e^{i(E_m-E_n)t}
# Equal-time logical susceptibility / order parameter:
#   chi_L(T) = (1/Z) sum_m e^{-beta E_m} <m|O_L^2|m> = 1 (O_L^2=I) -- so we instead use the
#   long-time PLATEAU of |C(t)| (the Mazur/Drude weight of O_L), which is the conserved part
#   of the logical operator. A truly PROTECTED (conserved) logical has plateau = 1 at all T
#   (C(t) flat, no decay). An UNPROTECTED logical has plateau -> 0 (C(t) decays, finite-T cusp).
# Plateau (infinite-time average) = (1/Z) sum_{E_m=E_n} e^{-beta E_m} |<m|O_L|n>|^2 / ...,
# i.e. the diagonal (energy-conserving) weight = Mazur bound on the conserved fraction.
# ===========================================================================

def logical_plateau(g, beta):
    """Infinite-time plateau of the normalized logical autocorrelation at coupling g and
    inverse temperature beta. =1 iff O_L=Z0 is conserved (protected); ->0 iff it decays.
    Computed as the energy-diagonal (Mazur) weight of O_L in the canonical ensemble,
    normalized by the equal-time value <O_L^2>=1."""
    H = build_H(g)
    evals, evecs = eigh_complex(H)
    n = len(evals)
    OL = op_from_apply(lambda v: apply_Z(v, 0))  # logical operator Z0
    # matrix elements <m|O_L|n>
    Z = sum(math.exp(-beta * (E - min(evals))) for E in evals)
    # group degenerate energies (tolerance) for the infinite-time average
    TOLE = 1e-6
    plateau = 0.0
    eq_time = 0.0
    for m in range(n):
        wm = math.exp(-beta * (evals[m] - min(evals))) / Z
        OLm = mat_vec(OL, evecs[m])
        for nn in range(n):
            amp = sum(evecs[nn][r].conjugate() * OLm[r] for r in range(DIM))
            p = abs(amp) ** 2
            eq_time += wm * p  # equal-time = <m|O_L^2|m> summed = 1 (sanity)
            if abs(evals[m] - evals[nn]) < TOLE:
                plateau += wm * p  # energy-conserving (infinite-time) part
    # normalize by equal-time (=1 for O_L^2=I); guard
    return plateau / eq_time if eq_time > 0 else 0.0


# ===========================================================================
# Ordering temperature of the order parameter. If the logical is protected (plateau ~1 at
# all T including infinite T), the order "does not melt" -> T_order = infinity (escape
# direction). If it decays (plateau falls below 1/2 at finite T), the order is an ENERGETIC
# condensate; its melting T is set by the spectral gap / coupling, i.e. bounded by the
# energy scale (-> the (pi/2)D_s ceiling once mapped to the SC stiffness).
# ===========================================================================

def main():
    # ---------- (1) CRUX: does the SC coupling preserve the protecting symmetry? ----------
    # commutator of each subsystem generator with H_code (g=0) and with H(g) (SC on).
    g_SC = 50.0  # representative finite SC pair-hopping coupling (meV)
    H0 = build_H(0.0)        # pure code
    Hg = build_H(g_SC)       # code + SC graft

    # row/col generators
    gen_apply = {
        "S_R0": lambda v: apply_line_Z(v, ROWS[0]),
        "S_R1": lambda v: apply_line_Z(v, ROWS[1]),
        "S_C0": lambda v: apply_line_Z(v, COLS[0]),
        "S_C1": lambda v: apply_line_Z(v, COLS[1]),
    }
    comm_code = {name: commutator_norm(ap, H0) for name, ap in gen_apply.items()}
    comm_sc = {name: commutator_norm(ap, Hg) for name, ap in gen_apply.items()}

    max_comm_code = max(comm_code.values())
    max_comm_sc = max(comm_sc.values())
    # the protecting symmetry survives the code but is BROKEN by the SC graft if the
    # commutator jumps from ~0 (code) to >0 (SC on).
    COMM_TOL = 1e-9
    symmetry_preserved_by_code = max_comm_code <= COMM_TOL
    symmetry_broken_by_SC = max_comm_sc > COMM_TOL

    # ---------- (2) logical autocorrelation plateau vs temperature ----------
    # If protected, plateau stays ~1 up to infinite T (beta->0). If the SC graft broke the
    # symmetry, the logical is no longer conserved and the plateau collapses.
    temps_K = [50.0, 150.0, 293.0, 1000.0, 1e6]  # up to ~infinite T (room-T = 293 K marked)
    plateau_code = []
    plateau_sc = []
    for TK in temps_K:
        beta = 1.0 / (KB_meV_per_K * TK)
        plateau_code.append(logical_plateau(0.0, beta))
        plateau_sc.append(logical_plateau(g_SC, beta))

    # infinite-T plateau (beta=0): the "does not melt up to lattice cutoff" claim.
    inf_plateau_code = logical_plateau(0.0, 0.0)
    inf_plateau_sc = logical_plateau(g_SC, 0.0)

    # The escape needs the SC (grafted) logical to RETAIN protection: plateau ~ 1 at infinite T.
    PROTECT_THRESH = 0.5
    sc_logical_protected_infT = inf_plateau_sc >= PROTECT_THRESH
    code_logical_protected_infT = inf_plateau_code >= PROTECT_THRESH  # positive control

    # ---------- (3) resulting ordering T vs the energetic ceiling ----------
    # Branch A (crux fails / symmetry broken by SC): order is energetic; melting T bounded by
    # the SC energy scale mapped to phase stiffness. With the frozen flat-band D_s the
    # energetic ceiling is (pi/2)D_s:
    tc_energetic_hi_K = (math.pi / 2.0) * DS_HI_meV / KB_meV_per_K  # ~8 K (same as H_043)
    tc_energetic_lo_K = (math.pi / 2.0) * DS_LO_meV / KB_meV_per_K
    # D_s needed to put the energetic ceiling AT the wall lower edge:
    ds_needed_for_wall_meV = CEILING_LO_K * KB_meV_per_K / (math.pi / 2.0)

    # Branch B (backstop / generalized Elitzur): a d_sub=1 line subsystem symmetry cannot
    # break at finite T -> the logical order parameter has T_order = 0 (no finite-T condensate).
    # Either branch caps the *thermodynamic* order at the energetic ceiling (Branch A) or 0
    # (Branch B); neither clears 134 K via the protection mechanism.
    best_order_tc_K = tc_energetic_hi_K  # most generous: the energetic branch's ceiling

    metrics = {
        "K_plaq_meV": K_PLAQ,
        "g_SC_meV": g_SC,
        "max_comm_code": max_comm_code,
        "max_comm_SC": max_comm_sc,
        "comm_tol": COMM_TOL,
        "symmetry_preserved_by_code": symmetry_preserved_by_code,
        "symmetry_broken_by_SC_graft": symmetry_broken_by_SC,
        "inf_T_plateau_code": inf_plateau_code,
        "inf_T_plateau_SC": inf_plateau_sc,
        "code_logical_protected_infT": code_logical_protected_infT,
        "sc_logical_protected_infT": sc_logical_protected_infT,
        "protect_thresh": PROTECT_THRESH,
        "tc_energetic_hi_K": tc_energetic_hi_K,
        "tc_energetic_lo_K": tc_energetic_lo_K,
        "ds_needed_for_wall_meV": ds_needed_for_wall_meV,
        "ds_hi_meV": DS_HI_meV,
        "best_order_tc_K": best_order_tc_K,
        "wall_lo_K": CEILING_LO_K,
        "wall_hi_K": CEILING_HI_K,
    }

    # ---- pre-registered falsifiers (PASS = NOT triggered). Escape ONLY if ALL pass, in
    # particular the CRUX honest-null F1 must PASS (the SC graft must PRESERVE the symmetry).
    falsifiers = [
        Falsifier(
            name="F1_CRUX_HONEST_NULL_SC_graft_breaks_subsystem_symmetry",
            predicate=lambda m: m["symmetry_broken_by_SC_graft"],
            desc="DECISIVE CRUX (tested first): TRIGGERED if the charge-2e pair-hopping graft "
                 "that makes it a superconductor makes a subsystem generator FAIL to commute "
                 "with H ([S,H]!=0). The sigma^x/sigma^y pair bilinear anticommutes with the "
                 "sigma^z line generator -> the protecting charge is destroyed by the very "
                 "coupling that condenses the SC. Then the order reverts to energetic and the "
                 "wall applies.",
        ),
        Falsifier(
            name="F2_HONEST_NULL_grafted_logical_not_protected_at_infinite_T",
            predicate=lambda m: not m["sc_logical_protected_infT"],
            desc="TRIGGERED if the grafted (SC) logical autocorrelation plateau falls below "
                 "0.5 at infinite T -- i.e. the order DOES melt: O_L is no longer conserved "
                 "once the SC coupling is on. The 'infinite-T memory' claim fails for the "
                 "superconducting Hamiltonian.",
        ),
        Falsifier(
            name="F3_best_order_tc_below_wall",
            predicate=lambda m: m["best_order_tc_K"] <= m["wall_lo_K"],
            desc="TRIGGERED if the most-generous resulting ordering T (the energetic-branch "
                 "ceiling once protection is gone) stays below the 134 K wall lower edge -- "
                 "the protection mechanism buys no thermodynamic ordering temperature.",
        ),
        Falsifier(
            name="F4_code_logical_IS_protected_positive_control",
            predicate=lambda m: not m["code_logical_protected_infT"],
            desc="POSITIVE CONTROL: TRIGGERED if the PURE code (g=0) logical is NOT protected "
                 "at infinite T -- which would mean the subsystem code itself is broken and the "
                 "test is meaningless. PASS confirms the code genuinely protects the logical "
                 "BEFORE the SC graft, so F1's collapse is caused by the graft, not a bug.",
        ),
        Falsifier(
            name="F5_code_symmetry_commutes_positive_control",
            predicate=lambda m: not m["symmetry_preserved_by_code"],
            desc="POSITIVE CONTROL: TRIGGERED if the subsystem generators do NOT commute with "
                 "the bare code H_code (g=0). PASS confirms [S,H_code]=0 (the code really does "
                 "host the conserved subsystem charge), isolating the SC graft as the cause of "
                 "the F1 breakage.",
        ),
    ]

    ledger = evaluate(metrics, falsifiers)
    n_pass, n_total = ledger["n_pass"], ledger["n_total"]
    crux = next(r for r in ledger["falsifiers"] if r["name"].startswith("F1_CRUX"))
    escapes = ledger["all_pass"]
    verdict = "escapes-wall" if escapes else "confirms-wall"

    # ---- verbatim print block (load-bearing stdout) ----
    print("=" * 74)
    print("H_047  Infinite-T Memory Graft (subsystem-code symmetry that does not melt)")
    print("cluster: code-/symmetry-protected order-class (variant of H_043 vortex-code)")
    print("=" * 74)
    print(f"host: 4-site (2x2 plaquette) Xu-Moore subsystem code,  K_plaq={K_PLAQ} meV")
    print(f"      subsystem generators S_R0=Z0Z1 S_R1=Z2Z3 S_C0=Z0Z2 S_C1=Z1Z3 (Z2xZ2)")
    print(f"      logical O_L=Z0 ; SC graft = -g*sum_<ij>(X_iX_j+Y_iY_j)/2, g={g_SC} meV")
    print("-" * 74)
    print("(1) CRUX -- does the charge-2e SC graft preserve the protecting subsystem symmetry?")
    print(f"  {'generator':>8} {'||[S,H_code]||':>16} {'||[S,H_SC]||':>16}")
    for name in ("S_R0", "S_R1", "S_C0", "S_C1"):
        print(f"  {name:>8} {comm_code[name]:16.6e} {comm_sc[name]:16.6e}")
    print(f"  max ||[S,H_code]|| = {max_comm_code:.6e}  (~0 => code preserves the subsystem charge)")
    print(f"  max ||[S,H_SC]||   = {max_comm_sc:.6e}  (>0 => SC graft BREAKS it: [S,H]!=0)")
    print(f"  symmetry preserved by bare code? {symmetry_preserved_by_code}")
    print(f"  symmetry BROKEN by SC graft?     {symmetry_broken_by_SC}   <== CRUX honest-null")
    print("-" * 74)
    print("(2) logical autocorrelation plateau C(inf) vs T  (1 => protected/no-melt, 0 => melts)")
    print(f"  {'T(K)':>10} {'plateau_code':>14} {'plateau_SC':>12}")
    for TK, pc, ps in zip(temps_K, plateau_code, plateau_sc):
        tag = "  <- room T" if abs(TK - 293.0) < 1e-6 else ""
        print(f"  {TK:10.1f} {pc:14.6f} {ps:12.6f}{tag}")
    print(f"  infinite-T plateau: code={inf_plateau_code:.6f}  SC-grafted={inf_plateau_sc:.6f}")
    print(f"  code logical protected at inf T? {code_logical_protected_infT}  (positive control)")
    print(f"  SC-grafted logical protected?    {sc_logical_protected_infT}  (escape needs True)")
    print("-" * 74)
    print("(3) resulting ordering T vs the energetic (pi/2)D_s ceiling and the wall")
    print(f"  frozen flat-band D_s window           = {DS_LO_meV}-{DS_HI_meV} meV")
    print(f"  energetic ceiling (pi/2)D_s           = {tc_energetic_lo_K:.2f}-{tc_energetic_hi_K:.2f} K")
    print(f"  D_s needed to put ceiling at 134 K    = {ds_needed_for_wall_meV:.3f} meV "
          f"(~{ds_needed_for_wall_meV/DS_HI_meV:.1f}x above frozen hi D_s)")
    print(f"  best resulting ordering T             = {best_order_tc_K:.2f} K   wall = "
          f"{CEILING_LO_K}-{CEILING_HI_K} K")
    print("-" * 74)
    for fr in ledger["falsifiers"]:
        print(f"  [{fr['status']}] {fr['name']}")
    print(f"falsifiers_pass = {n_pass}/{n_total}")
    print(f"CRUX honest-null (F1) triggered = {crux['triggered']}  "
          f"(triggered => SC graft breaks the symmetry => wall confirmed)")
    print("-" * 74)
    print(f"VERDICT: {verdict}")
    print(f"falsifiers_pass: {n_pass}")
    print(f"is_green: False   absorbed: false")
    print("=" * 74)


if __name__ == "__main__":
    main()
