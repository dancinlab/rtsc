#!/usr/bin/env python3
"""H_038 - Ligand-Hole Negative-U: the pair lives on oxygen, not the cation.

Escape cluster: "light real-space pairs decouple eV binding from stiffness".

CLAIM (escape seed, triage.md line 66-68):
  A BaBiO3-class delocalized-ligand negative-U gives a LIGHT real-space pair (a
  preformed intersite bipolaron on the symmetric O6 molecular orbital, NOT a
  flat-band quantum-metric pair, NOT a phonon-Holstein H_008 pair, NOT a k-space
  Leggett-H_032 pair). Its superfluid stiffness comes from low m* + high n_pair, so
  the eV-scale binding |U_eff| is DECOUPLED from the stiffness. If m* drops below
  ~3 m_e as the ligand bandwidth W grows at fixed |U_eff|, the pair Bose gas
  condenses with T_BKT = (pi/2) D_s above the 134-164 K spin-fluctuation /
  phase-stiffness ambient ceiling.

  Stiffness of a 2D dilute pair Bose gas (real-space pairs):
      D_s = hbar^2 * n_pair / (2 m*)                [Emery-Kivelson energy units]
      T_BKT = (pi/2) * D_s                          (per the freeze relation)
  with n_pair the areal pair density and m* the bipolaron band mass. The eV binding
  enters only through whether the pair is BOUND, never through D_s -> decoupling.

WHICH OF THE 5 FREEZE PREMISES THIS VIOLATES:
  The freeze ceiling (~134-164 K) was measured on hosts that are
  {Q=0 / single-particle-flat / crystalline / quasiparticle-coherent / equilibrium}.
  This escape violates the **single-particle / quasiparticle-coherent** premise: the
  charge carrier is a COMPOSITE real-space boson (a preformed bipolaron), NOT a BCS
  Bogoliubov quasiparticle on a single-particle band. Stiffness is set by the
  boson's m*/n (a Bose-gas response), not by D_s = 4|U| nu(1-nu) <g> (the
  single-particle flat-band geometric formula). So the freeze's D_s law need not bind.

HONEST-NULL (load-bearing decisive falsifier - NOT engineered around, triage.md):
  "Binding<->delocalization lock / self-trapping." For a real-space pair, large
  |U_eff| that BINDS the two holes simultaneously DRESSES the pair so its band mass
  m*(W) ~ m0 * exp(+c*|U_eff|/W) grows (Holstein/Lang-Firsov band-narrowing
  exp(g^2); arXiv:0907.4572, cond-mat/9809025). You cannot make the pair both
  tightly bound (eV) and light: the SAME |U_eff| that gives eV binding self-traps
  the pair. If m*(W) stays > 10 m_e for ALL W with the pair still bound, then
  D_s never clears the cuprate 7.4 meV (~164 K) scale and the wall HOLDS.

LITERATURE ANCHOR (research-first, cited - never fabricated):
  - The intersite "superlight" bipolaron is REAL and DOES beat naive Holstein
    self-trapping (first-order hopping): Alexandrov & Kornilovitch, "Superlight
    small bipolarons" cond-mat/0606036; "a route to room temperature
    superconductivity" cond-mat/0701412.
  - BUT even the MOST optimized superlight intersite bipolaron BEC tops out at
    Tc ~ 90-120 K for realistic parameters (Alexandrov cond-mat/0701412 abstract;
    medium coupling, small intersite pair).
  - Recent unbiased QMC (Adebanjo, Hague & Kornilovitch, arXiv:2507.17398, 2025):
    close-packing bipolaron Tc ceiling ~ 0.01-0.02 t, with optimal bipolaron mass
    m* ~ 50-100 m0 on FCC/BCC -> the binding<->mass lock is NOT escaped at the level
    needed for room-T. BaBiO3 itself: bond-disproportionation hole pair on the
    contracted O6 octahedron (arXiv:1807.07168) - real molecular negative-U, but a
    heavy CDW/bipolaron, gapped insulator until doped.

  BEC formula (Alexandrov): T_BEC = 3.31 * hbar^2 * n^(2/3) / (kB * m**).

DETERMINISTIC, stdlib-only, no Date/random -> byte-equal across runs.
escapes-wall ONLY if the honest-null genuinely PASSES with a real margin.
absorbed=false. is_green=False. No material is claimed to BE an RTSC.
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tool'))
from rtsc_harness import Falsifier, evaluate, ROOM_T_K

# --- physical constants (SI / convenient units) ------------------------------
HBAR = 1.054571817e-34      # J s
KB = 1.380649e-23           # J / K
M_E = 9.1093837015e-31      # kg
EV = 1.602176634e-19        # J
ANG = 1.0e-10               # m
MEV = 1.0e-3 * EV

# Freeze ceiling band (spin-fluctuation / phase-stiffness ambient), in K.
CEIL_LO_K = 134.0
CEIL_HI_K = 164.0
# Cuprate phase-stiffness scale the pair must clear: T_BKT ~ 164 K <-> D_s ~ 7.4 meV.
CUPRATE_DS_MEV = 7.4

# -----------------------------------------------------------------------------
# Real-space pair stiffness of a 2D dilute pair Bose gas (Nelson-Kosterlitz line
# for bosons of mass m* and areal density n2d): D_s = hbar^2 n2d / (2 m*), and the
# freeze relation T_BKT = (pi/2) D_s. This is the boson analogue of the
# Emery-Kivelson single-particle D_s the freeze uses.
# -----------------------------------------------------------------------------

def ds_meV_from_pair_gas(n2d_per_m2, mstar_me):
    """Superfluid phase stiffness D_s (meV) of a 2D pair Bose gas."""
    mstar = mstar_me * M_E
    ds_J = (HBAR * HBAR) * n2d_per_m2 / (2.0 * mstar)
    return ds_J / MEV


def tbkt_K_from_ds_meV(ds_meV):
    """Freeze relation T_BKT = (pi/2) * D_s, with D_s in meV -> K."""
    ds_J = ds_meV * MEV
    return (math.pi / 2.0) * ds_J / KB


# -----------------------------------------------------------------------------
# THE BINDING<->MASS LOCK, parametrized by the ONE dimensionless coupling
#     g  ==  |U_eff| / W        (attraction / ligand bandwidth).
# Binding AND mass are BOTH monotone functions of the SAME g -- they are NOT
# independent knobs. This is the physical content of the honest-null: you cannot
# choose eV binding and light mass separately.
#
#   pair binding energy (small real-space pair):
#       E_bind(g) = |U_eff| * g / (1 + g)                 (eV)
#       -> E_bind -> |U_eff| (eV-scale) only as g -> large (strong coupling).
#       -> E_bind -> 0 as g -> 0 (weak coupling, no real-space pair).
#
#   pair band mass (intersite "superlight" branch -- the LIGHTEST channel, most
#   generous to the claim; the on-site Holstein branch exp(g) is heavier still):
#       m*(g)/m0 = 1 + a * g^2
#   ANCHORED (NOT tuned-to-green) to the one hard literature datum: unbiased QMC
#   gives optimal-Tc bipolaron mass m* ~ 50 m0 at strong coupling g ~ 5
#   (arXiv:2507.17398). Solve 1 + a*25 = 50 -> a = 1.96 ~ 2.0. Fixed, not free.
#
# Consequence: at the g that delivers eV-scale binding (g ~ 5, E_bind ~ 0.83*|U|),
# m* is FORCED to ~50 m0 -> the pair is heavy -> D_s collapses. The seed's claimed
# "m* < 3 m_e WHILE eV-bound" lives at g ~ 1, where E_bind = |U|/2 ~ 0.4 eV is
# sub-eV: a marginal pair, NOT the eV-bound real-space pair the premise requires.
# -----------------------------------------------------------------------------

A_INTERSITE = 2.0          # mass prefactor, anchored to QMC m*~50 @ g~5 (2507.17398)
EV_BIND_FLOOR_EV = 0.50    # "eV-scale" binding the seed's premise itself requires


def coupling_g(U_eff_eV, W_eV):
    return U_eff_eV / W_eV


def pair_binding_eV(U_eff_eV, W_eV):
    """Small-pair binding E_bind(g)=|U|*g/(1+g): eV-scale only at strong coupling."""
    g = coupling_g(U_eff_eV, W_eV)
    return U_eff_eV * g / (1.0 + g)


def mstar_intersite(U_eff_eV, W_eV, a=A_INTERSITE):
    """Lightest (superlight intersite) channel; anchored to QMC (arXiv:2507.17398)."""
    g = coupling_g(U_eff_eV, W_eV)
    return 1.0 + a * g * g


def mstar_holstein(U_eff_eV, W_eV):
    """Heavier on-site self-trapping channel, exp(g) (arXiv:0907.4572)."""
    return math.exp(coupling_g(U_eff_eV, W_eV))


def mstar_physical(U_eff_eV, W_eV):
    """Lighter (more generous to the claim) of the two locked channels."""
    return min(mstar_intersite(U_eff_eV, W_eV), mstar_holstein(U_eff_eV, W_eV))


def pair_is_ev_bound(U_eff_eV, W_eV):
    """True iff the pair carries the eV-scale binding the seed's claim requires."""
    eb = pair_binding_eV(U_eff_eV, W_eV)
    return eb >= EV_BIND_FLOOR_EV, eb


# -----------------------------------------------------------------------------
# Scan realistic BaBiO3-class ligand-hole parameters.
#   |U_eff| ~ 0.5-1.0 eV (molecular negative-U on the O6 MO; bond-disprop.)
#   W swept 0.2 .. 3.0 eV (M-O-M-angle-tuned ligand bandwidth).
#   n2d = generous high-density 0.30 pairs / a^2 (a = 4.35 Ang) -> favors the claim.
# -----------------------------------------------------------------------------

A_LAT = 4.35 * ANG                  # BaBiO3 cubic-perovskite lattice const (m)
N2D_PAIR = 0.30 / (A_LAT * A_LAT)   # pairs / m^2  (generous high-n limit)
U_EFF_EV = 0.75                     # molecular negative-U on the O6 MO (eV)

W_grid = [0.2 + 0.1 * i for i in range(29)]   # 0.2 .. 3.0 eV, deterministic

best = {"tbkt_K": -1.0}
scan_rows = []
for W in W_grid:
    bound, e_bind = pair_is_ev_bound(U_EFF_EV, W)
    m = mstar_physical(U_EFF_EV, W)
    ds = ds_meV_from_pair_gas(N2D_PAIR, m)
    tbkt = tbkt_K_from_ds_meV(ds)
    row = {"W_eV": round(W, 3), "mstar_me": m, "bound": bound,
           "e_bind_eV": round(e_bind, 4), "ds_meV": ds, "tbkt_K": tbkt}
    scan_rows.append(row)
    if bound and tbkt > best["tbkt_K"]:
        best = dict(row)

# Honest-null is evaluated ONLY on the eV-bound set (the seed's actual claim):
# the lightest mass achievable WHILE carrying eV-scale binding.
bound_rows = [r for r in scan_rows if r["bound"]]
min_mstar_bound = min((r["mstar_me"] for r in bound_rows), default=float("inf"))
best_bound_tbkt = max((r["tbkt_K"] for r in bound_rows), default=0.0)

# Literature ceiling cross-check.
LIT_SUPERLIGHT_TC_MAX_K = 120.0     # cond-mat/0701412, best realistic case
LIT_QMC_MSTAR_OPTIMAL = 50.0        # arXiv:2507.17398 optimal-Tc bipolaron mass

metrics = {
    "U_eff_eV": U_EFF_EV,
    "n2d_pair_per_m2": N2D_PAIR,
    "best_bound_tbkt_K": best_bound_tbkt,
    "min_mstar_bound_me": min_mstar_bound,
    "ceil_lo_K": CEIL_LO_K,
    "ceil_hi_K": CEIL_HI_K,
    "room_T_K": ROOM_T_K,
    "lit_superlight_tc_max_K": LIT_SUPERLIGHT_TC_MAX_K,
    "lit_qmc_mstar_optimal_me": LIT_QMC_MSTAR_OPTIMAL,
    "cuprate_ds_meV": CUPRATE_DS_MEV,
    "best_row": best,
}

# -----------------------------------------------------------------------------
# Falsifiers. predicate(metrics) -> True == TRIGGERED (refuted). PASS = not triggered.
# -----------------------------------------------------------------------------
falsifiers = [
    # F1 HONEST-NULL (decisive): binding<->delocalization / self-trapping lock.
    Falsifier(
        name="honest_null_self_trapping_lock",
        predicate=lambda m: m["min_mstar_bound_me"] > 10.0,
        desc="DECISIVE honest-null: lightest BOUND pair mass exceeds 10 m_e "
             "(binding self-traps the pair; m* never drops to the claimed <3 m_e "
             "while bound) -> eV binding does NOT decouple from stiffness.",
    ),
    # F2: best-case bound T_BKT must clear the LOWER freeze ceiling (134 K).
    Falsifier(
        name="tbkt_below_freeze_floor",
        predicate=lambda m: m["best_bound_tbkt_K"] < m["ceil_lo_K"],
        desc="Best-case bound-pair T_BKT below the 134 K freeze floor.",
    ),
    # F3: must clear the cuprate phase-stiffness scale (D_s >= 7.4 meV <-> ~164 K).
    Falsifier(
        name="ds_below_cuprate_scale",
        predicate=lambda m: ds_meV_from_pair_gas(N2D_PAIR, m["min_mstar_bound_me"])
        < m["cuprate_ds_meV"],
        desc="Lightest-bound-pair D_s below the cuprate 7.4 meV phase-stiffness scale.",
    ),
    # F4: literature cross-check -- realistic superlight bipolaron BEC < 164 K.
    Falsifier(
        name="lit_superlight_below_ceiling",
        predicate=lambda m: m["lit_superlight_tc_max_K"] < m["ceil_hi_K"],
        desc="Literature superlight-bipolaron BEC ceiling (cond-mat/0701412, "
             "~120 K) is below the 164 K freeze ceiling.",
    ),
    # F5: room-T sanity -- best-case bound T_BKT must reach 293 K target.
    Falsifier(
        name="tbkt_below_room_T",
        predicate=lambda m: m["best_bound_tbkt_K"] < m["room_T_K"],
        desc="Best-case bound-pair T_BKT below the 293 K room-T target.",
    ),
]

result = evaluate(metrics, falsifiers)
passes = result["n_pass"]
total = result["n_total"]

honest_null = next(r for r in result["falsifiers"]
                   if r["name"] == "honest_null_self_trapping_lock")
honest_null_passes = (honest_null["status"] == "PASS")
clears_floor = best_bound_tbkt >= CEIL_LO_K

if honest_null_passes and clears_floor:
    verdict = "escapes-wall"
else:
    verdict = "confirms-wall"

# -----------------------------------------------------------------------------
# Verbatim report.
# -----------------------------------------------------------------------------
print("=" * 72)
print("H_038 Ligand-Hole Negative-U: the pair lives on oxygen, not the cation")
print("escape cluster: light real-space pairs decouple eV binding from stiffness")
print("=" * 72)
print("freeze premise violated: single-particle / quasiparticle-coherent")
print("  (carrier = composite real-space boson, not a BCS quasiparticle)")
print("-" * 72)
print("inputs: U_eff = %.3f eV, n2d_pair = %.3e /m^2 (%.2f pairs/a^2, a=%.2f Ang)"
      % (U_EFF_EV, N2D_PAIR, 0.30, A_LAT / ANG))
print("W swept %.2f .. %.2f eV (M-O-M angle / ligand bandwidth)"
      % (W_grid[0], W_grid[-1]))
print("-" * 72)
print("scan (W_eV  mstar/m_e  eV-bound E_bind_eV   D_s_meV    T_BKT_K):")
for r in scan_rows:
    print("  %5.2f   %9.3f    %-5s   %7.4f   %8.4f   %8.2f"
          % (r["W_eV"], r["mstar_me"], str(r["bound"]),
             r["e_bind_eV"], r["ds_meV"], r["tbkt_K"]))
print("-" * 72)
print("lightest eV-BOUND pair mass          : %.3f m_e" % min_mstar_bound)
print("best-case eV-BOUND T_BKT             : %.2f K" % best_bound_tbkt)
print("freeze ceiling band                  : %.0f - %.0f K" % (CEIL_LO_K, CEIL_HI_K))
print("cuprate phase-stiffness scale         : %.1f meV  (~164 K)" % CUPRATE_DS_MEV)
print("lit superlight bipolaron BEC ceiling : ~%.0f K (Alexandrov cond-mat/0701412)"
      % LIT_SUPERLIGHT_TC_MAX_K)
print("lit QMC optimal bipolaron mass        : ~%.0f m_e (arXiv:2507.17398)"
      % LIT_QMC_MSTAR_OPTIMAL)
print("-" * 72)
for r in result["falsifiers"]:
    print("  [%s] %s" % (r["status"], r["name"]))
print("-" * 72)
print("honest_null (self-trapping lock) PASS : %s" % honest_null_passes)
print("best-case bound T_BKT clears 134 K    : %s" % clears_floor)
print("falsifiers_pass=%d/%d" % (passes, total))
print("VERDICT: %s" % verdict)
