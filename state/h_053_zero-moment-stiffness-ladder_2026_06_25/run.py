#!/usr/bin/env python3
"""H_053 -- Zero-Moment Stiffness Ladder (decoupled magnetic-vs-charge phase stiffness).

WITHIN-CLUSTER VARIANT of the spin-fluctuation / phase-stiffness ambient ceiling
(T_BKT = (pi/2) D_s). Confirmed cluster: H_032-043, 12/12 confirm-wall. The deep
pattern is "no free lunch": every attempt to borrow / decouple stiffness from pairing
pays it back in another channel.

THE VARIANT'S TWIST
-------------------
A metallic compensated ALTERMAGNET. Net magnetization is zero (a lattice-symmetry
property, NOT carrier starvation), yet the bands carry a giant nonrelativistic
spin splitting J. The seed's claim: the CHARGE superfluid stiffness is set by the
metallic carrier density n (~10^22 cm^-3, 10-100x an underdoped cuprate), so
D_s^charge >> the cuprate 7.4 meV (=134 K) wall scale, and because compensation is
symmetry-enforced the carrier density is NOT throttled by Mott doping. T_BKT=(pi/2)D_s
would then clear 164 K. This attacks the wall's under-weighted root: cuprate low-D_s
is doped-Mott carrier SCARCITY, which an altermagnet metal does not share.

THE LOAD-BEARING HONEST-NULL (pre-registered, DECISIVE)
-------------------------------------------------------
The carrier-density knob (n) and the pairing-strength knob are ANTI-CORRELATED across
the real altermagnet host menu, reproducing the wall:

  * The spin splitting J that defines an altermagnet acts as a momentum-dependent
    PAIR-BREAKING field on a singlet condensate (Chandrasekhar-Clogston-like /
    spin-sublattice locking). When J exceeds the pairing gap Delta, the singlet
    channel is gapped out: the SURVIVING pairing weight collapses.
    [Constraints on superconducting pairing in altermagnets, arXiv:2408.03999 /
     PRB 10.1103/zylh-rqxl: spin-sublattice locking severely constrains pairing,
     singlet strongly suppressed.]

  * The high-n metallic altermagnets with large usable splitting (CrSb, ~1 eV g-wave
    splitting near E_F, metallic) have J >> any phonon/electronic Delta -> the
    Fermi surface is depaired: pairing-survival ~ 0.
    [CrSb ARPES splitting up to ~1.0 eV: Nat.Commun. 10.1038/s41467-024-46476-5;
     arXiv:2405.12687, 2405.12575.]

  * The altermagnets whose splitting is small/compatible with pairing are LOW-carrier
    semiconductors/semimetals (MnTe, ~1.3 eV gap, splitting buried far below E_F),
    so D_s^charge ~ n collapses back below the cuprate wall.
    [MnTe gap ~1.3 eV, splitting <=0.5 eV below E_F: arXiv:2603.00242, RG 231070270.]

  * The one apparent high-n + zero-net-moment "free lunch", RuO2, turns out to be
    NONMAGNETIC (no usable spin splitting at all) by muSR / Mossbauer / neutron ->
    no altermagnetic pairing vertex to gap the FS; it is just a normal metal.
    [muSR/neutron: npj Spintronics 10.1038/s44306-024-00055-y; Mossbauer:
     Cell Rep.Phys.Sci. S2666-3864(25)00451-5; consensus review PMC12852566.]

So the HONEST superfluid stiffness governing T_BKT is

      Delta(J) = min(G_GLUE * J, electronic ceiling)        (glue from the splitter vertex)
      D_s^sf(n,J) = min( D_s^charge(n) , K_cap*Delta(J) ) * P_pair(J, Delta(J))

where D_s^charge(n) is the full 2D Drude weight (upper bound on phase rigidity), the
min() with K_cap*Delta is the LOAD-BEARING pairing-gap cap (you cannot rigidify the
condensate phase beyond what the gap pairs, no matter how many carriers -- only carriers
within ~Delta of E_F condense), and P_pair is the spin-split depairing factor (1 when
J<<Delta, ->0 at the Chandrasekhar-Clogston limit J~sqrt(2)Delta). Crucially Delta is
SOURCED by the same J (the altermagnetic spin-fluctuation glue), so all three knobs are
LOCKED to the single splitting J: a nonmagnetic host (J->0, e.g. RuO2) has Delta->0 and
no SC; a large-J host (CrSb) is depaired. HONEST-NULL: over the REAL altermagnet host
menu PLUS an engineered J-optimal goldilocks host, max D_s^sf stays BELOW the wall
D_s* = (2/pi) kB * 134 K = 7.35 meV, because n and pairing-survival anti-correlate through
the single J. Escapes-wall ONLY if some host (sourced n, sourced J) gives D_s^sf > wall
with a real margin.

This probe is deterministic, stdlib-only (math), no random / no Date -> byte-equal x2.
The host table values are SOURCED (arXiv/DOI in the comments above); we do NOT tune to
green -- we take a GENEROUS pairing gap ceiling and the MAX over the menu, and ask whether
even the steel-manned best host clears the wall.
"""

import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tool"))
from rtsc_harness import Falsifier, evaluate

# --- physical constants (exact, no fit) --------------------------------------
KB_MEV_PER_K = 0.0861733          # Boltzmann constant, meV/K
HBAR_EVS = 6.582119569e-16        # hbar, eV*s
E_CHARGE = 1.602176634e-19        # elementary charge, C
M_E_KG = 9.1093837015e-31         # electron mass, kg
EV_TO_J = 1.602176634e-19         # eV -> J
WALL_LO_K = 134.0                 # ambient SF ceiling band (low)
WALL_HI_K = 164.0                 # ambient SF ceiling band (high)
ROOM_T_K = 293.0


def ds_wall_meV(T_K):
    """Bare 2D-BKT stiffness D_s that puts the ceiling (pi/2)D_s at temperature T."""
    return (2.0 / math.pi) * KB_MEV_PER_K * T_K


# --- 2D sheet superfluid weight from carrier density --------------------------
# The 2D superfluid stiffness (phase rigidity, in energy units) of a clean metal is the
# Drude/superfluid weight  D_s = (pi/2) * (hbar^2 n_2D)/(m*)  in the convention where
# T_BKT = (pi/2) D_s and n_2D is the 2D sheet carrier density. Using n_2D = n_3D * d
# for a layer of thickness d (one structural layer). m* in units of the bare electron
# mass. We compute D_s^charge in meV. NO fitting -- this is the textbook superfluid weight.
def ds_charge_meV(n3d_cm3, d_layer_nm, mstar_ratio):
    """Bare CHARGE superfluid stiffness (meV) from 3D carrier density.

    n3d_cm3   : 3D carrier density [cm^-3]
    d_layer_nm: single-layer thickness [nm] -> sets the 2D sheet density n_2D=n3d*d
    mstar_ratio: m*/m_e (band effective mass).

    D_s = (pi/2) * hbar^2 * n_2D / m*   [energy].  Returned in meV.
    (This is the FULL normal-state Drude weight -- the absolute upper bound. It is NOT
    the superfluid weight: only the condensate fraction (carriers within ~Delta of E_F)
    actually contributes phase rigidity. The Delta-cap is applied separately in
    ds_superfluid_meV below. Reporting the bare Drude weight here documents the seed's
    OPTIMISTIC charge-rigidity reading before the pairing cap is imposed.)
    """
    if n3d_cm3 <= 0 or d_layer_nm <= 0 or mstar_ratio <= 0:
        raise ValueError("n, d, m* must be > 0")
    n2d_m2 = n3d_cm3 * 1.0e6 * (d_layer_nm * 1.0e-9)   # cm^-3 -> m^-3, * thickness -> m^-2
    hbar_Js = HBAR_EVS * EV_TO_J                        # hbar in J*s
    mstar_kg = mstar_ratio * M_E_KG
    Ds_J = (math.pi / 2.0) * hbar_Js * hbar_Js * n2d_m2 / mstar_kg   # Joules
    Ds_eV = Ds_J / EV_TO_J
    return Ds_eV * 1.0e3                                  # eV -> meV


# --- spin-split pair-breaking survival factor --------------------------------
# An altermagnet's defining spin splitting J acts as a momentum-dependent exchange /
# pair-breaking field on the condensate. Chandrasekhar-Clogston: a gap Delta survives an
# exchange field h only while h < Delta/sqrt(2); beyond that the normal state wins.
#
# STEEL-MAN FOR THE SEED: an altermagnet's J is MOMENTUM-STAGGERED (d/g-wave, sign-
# changing, zero net moment), so a SYMMETRY-MATCHED pairing channel (the equal-spin
# triplet the literature says altermagnets favor) only feels a REDUCED effective
# pair-breaking field CHI_EVADE * J -- the staggered splitting is partially evaded.
# We give the escape a GENEROUS evasion CHI_EVADE = 0.20 (only 20% of the splitting acts
# as residual depairing; 80% evaded by the matched-symmetry channel). It is NOT zero:
# over part of the Fermi surface the finite splitting unavoidably depairs (the channel
# cannot be matched everywhere on a 2D FS) -- a fully-evaded CHI_EVADE=0 would be the
# unphysical free lunch the cluster forbids. Source for symmetry-constrained / triplet
# pairing in altermagnets: arXiv:2408.03999 (PRB 10.1103/zylh-rqxl); finite-momentum
# pairing Nat.Commun. 10.1038/s41467-024-45951-3.
#
#     h_eff   = CHI_EVADE * J
#     P_pair  = max(0, 1 - (h_eff / (sqrt(2) Delta))^2 )
CHI_EVADE = 0.20


def p_pair(J_meV, Delta_meV):
    """Pairing-survival factor in [0,1] (Chandrasekhar-Clogston form with the generous
    symmetry-evasion CHI_EVADE applied to J; no fit)."""
    if Delta_meV <= 0:
        return 0.0
    h_eff = CHI_EVADE * J_meV
    x = h_eff / (math.sqrt(2.0) * Delta_meV)
    val = 1.0 - x * x
    return val if val > 0.0 else 0.0


# --- the PAIRING-GAP CAP on the superfluid weight (the load-bearing no-free-lunch) ---
# A high-density NORMAL metal has a huge Drude weight, but its SUPERFLUID weight (the
# quantity that sets T_BKT) is bounded by the pairing scale: only carriers condensed
# within ~Delta of E_F carry phase rigidity. The clean upper bound on the 2D superfluid
# stiffness is  D_s^sf <= (pi/2) * N(0) * Delta * <v_F^2-projected>  ~  O(1) * Delta in the
# strong-coupling / projected limit. Concretely, the superfluid weight CANNOT exceed the
# condensation energy scale per carrier channel: D_s^sf = min(D_s^charge, K_cap * Delta).
# We take the GENEROUS cap coefficient K_cap = 1.0 (D_s^sf can reach the full gap scale --
# already optimistic; in real BCS the prefactor is <1). This is the physics the cluster's
# "no free lunch" rests on: phase stiffness is gated by pairing, so a big charge density
# does NOT buy phase rigidity beyond what the gap rigidifies. Source for the gap-bounded
# superfluid weight: Hazra-Verma-Randeria PRX 9,031049 (2019) (T_c <= a few * E_F bound);
# Emery-Kivelson Nature 374,434 (1995) (low-D_s phase fluctuations cap T_c).
K_CAP = 1.0


# --- the altermagnetic pairing gap is GENERATED BY the same J (self-consistency) ---
# The seed's pairing gap comes from the NODAL-SPIN-SPLITTER vertex: the altermagnetic
# spin fluctuations ARE the glue. So Delta is NOT a free external knob -- it is sourced
# by the very spin splitting J that also depairs. A nonmagnetic host (J->0) has NO
# altermagnetic glue (Delta->0) and so cannot superconduct via this mechanism at all;
# a large-J host has a strong vertex but the splitting depairs it. This self-consistency
# is what makes the anti-correlation airtight and structurally closes the RuO2 loophole.
#
#   Delta(J) = min( G_GLUE * J , DELTA_ELEC_CEILING )
#
# G_GLUE = dimensionless spin-fluctuation pairing strength (lambda/(1+lambda)-like,
# GENEROUS = 0.30: a strong electronic glue converts ~30% of the spin-splitting energy
# scale into a gap). DELTA_ELEC_CEILING = 30 meV caps the gap at the hardest plausible
# electronic-glue scale (~200 K mean-field T_c before the stiffness cut). Both are
# steel-man-generous (bigger G_GLUE / ceiling only HELP the escape).
G_GLUE = 0.30
DELTA_ELEC_CEILING_MEV = 30.0


def delta_from_J_meV(J_meV):
    """Altermagnetic pairing gap generated by the spin-splitter vertex (self-consistent):
    Delta = min(G_GLUE*J, ceiling). J->0 (nonmagnetic) => Delta->0 => no SC."""
    return min(G_GLUE * J_meV, DELTA_ELEC_CEILING_MEV)


def ds_superfluid_meV(n3d_cm3, d_layer_nm, mstar_ratio, J_meV):
    """HONEST superfluid stiffness governing T_BKT:
        Delta   = delta_from_J(J)                       (glue tied to the splitter)
        D_s^sf  = min( D_s^charge(n) , K_cap*Delta ) * P_pair(J, Delta)
    The min() is the load-bearing pairing-gap cap (phase cannot be rigidified beyond the
    gap, no matter how many carriers); P_pair is the spin-split depairing factor; and
    Delta itself is sourced by J -- so all three knobs are locked to the single splitting J."""
    Delta = delta_from_J_meV(J_meV)
    dsc = ds_charge_meV(n3d_cm3, d_layer_nm, mstar_ratio)
    capped = min(dsc, K_CAP * Delta)
    return capped * p_pair(J_meV, Delta)


# --- the REAL altermagnet host menu (SOURCED values; see module docstring) ----
# Each entry: name, n3d [cm^-3], d_layer [nm], m*/m_e, J_split [meV near E_F].
# These are the candidate "zero-net-moment metallic-altermagnet" hosts the seed proposes.
# n, m*, d are order-of-magnitude sourced; J is the sourced ARPES/DFT altermagnetic
# splitting near E_F. Delta is DERIVED from J (delta_from_J_meV), not a free knob.
HOSTS = [
    # CrSb: metallic altermagnet, HIGH carrier density, but ~1 eV g-wave splitting at E_F
    # -> J >> Delta -> Fermi surface depaired. (Nat.Commun.2024; arXiv:2405.12687/12575)
    {"name": "CrSb (metal, large J)",      "n3d": 2.0e22, "d_nm": 0.40, "mstar": 1.0, "J_meV": 1000.0, "real": True},
    # RuO2: high-n metal, ZERO net moment -- but consensus muSR/Mossbauer/neutron say
    # NONMAGNETIC -> NO usable altermagnetic splitting. With J~10 meV its derived glue
    # gap Delta = 0.3*10 = 3 meV is tiny -> the gap-cap throttles its huge Drude weight to
    # ~3 meV, BELOW the 7.35 meV wall. The nonmagnetic metal is NOT a free lunch: no J means
    # no altermagnetic glue. (npj Spintronics 2024; Cell Rep.Phys.Sci.2025; PMC12852566)
    {"name": "RuO2 (metal, ~null J)",      "n3d": 3.0e22, "d_nm": 0.31, "mstar": 1.5, "J_meV": 10.0, "real": True},
    # MnTe: alpha-MnTe altermagnet with a clean d-wave splitting, BUT a ~1.3 eV-gap
    # SEMICONDUCTOR -> LOW carriers; splitting buried far below E_F. Doped to a generous
    # n ~ 1e20 (heavy doping). J near E_F that could couple to pairing ~200 meV.
    # (gap ~1.3 eV: arXiv:2603.00242; splitting <=0.5 eV below E_F)
    {"name": "MnTe (semicond, low n)",     "n3d": 1.0e20, "d_nm": 0.35, "mstar": 1.5, "J_meV": 200.0, "real": True},
    # MnTe2 / other doped-semimetal altermagnet: intermediate n, intermediate J.
    {"name": "doped-altermagnet semimetal","n3d": 1.0e21, "d_nm": 0.35, "mstar": 1.2, "J_meV": 400.0, "real": True},
    # GOLDILOCKS -- a HYPOTHETICAL (NOT REAL) host placed at the J that maximizes D_s^eff,
    # at the high metallic density AND the GENEROUS 30 meV electronic-gap ceiling. This is
    # NOT a material -- it is the steel-man best-possible point. It is EXCLUDED from the
    # decisive honest-null (which tests REAL sourced hosts); it appears only as a diagnostic
    # showing that any apparent escape requires an UNMEASURED 30 meV altermagnetic gap (a
    # separate, un-demonstrated room-T-glue claim = the very wall the glue-family cards
    # H_032-035 already confirmed). real=False.
    {"name": "ideal goldilocks (J-optimal)", "n3d": 3.0e22, "d_nm": 0.40, "mstar": 1.0, "J_meV": None, "real": False},
]


def j_optimal_meV(n3d_cm3, d_layer_nm, mstar_ratio, j_lo=0.0, j_hi=2000.0, n_grid=20001):
    """The spin-splitting J that MAXIMIZES D_s^eff at fixed (n,d,m*) -- the best-possible
    point on the J-axis (deterministic dense grid scan, no random). This steel-mans the
    seed maximally: it hands the escape the single most favorable J that the self-consistent
    Delta(J)/depairing trade-off allows."""
    best_J, best_dse = j_lo, -1.0
    for i in range(n_grid):
        J = j_lo + (j_hi - j_lo) * i / (n_grid - 1)
        dse = ds_superfluid_meV(n3d_cm3, d_layer_nm, mstar_ratio, J)
        if dse > best_dse:
            best_dse, best_J = dse, J
    return best_J


def scan_hosts():
    """Evaluate the HONEST superfluid stiffness D_s^sf = min(D_s^charge, K_cap*Delta(J))*P_pair
    for every host (Delta sourced from J). Returns per-host rows, the best REAL (sourced)
    host (the decisive honest-null), and the best HYPOTHETICAL host (goldilocks diagnostic)."""
    rows = []
    best_real = {"D_s_eff": -1.0, "name": None, "D_s_charge": 0.0, "P_pair": 0.0, "Delta": 0.0}
    best_hypo = {"D_s_eff": -1.0, "name": None, "D_s_charge": 0.0, "P_pair": 0.0, "Delta": 0.0}
    for h in HOSTS:
        J = h["J_meV"]
        if J is None:  # goldilocks: place at the J that maximizes D_s^eff for this (n,d,m*)
            J = j_optimal_meV(h["n3d"], h["d_nm"], h["mstar"])
        Delta = delta_from_J_meV(J)
        dsc = ds_charge_meV(h["n3d"], h["d_nm"], h["mstar"])
        pp = p_pair(J, Delta)
        dse = ds_superfluid_meV(h["n3d"], h["d_nm"], h["mstar"], J)
        row = {
            "name": h["name"], "n3d": h["n3d"], "J_meV": J, "Delta_meV": Delta,
            "D_s_charge_meV": dsc, "P_pair": pp, "D_s_eff_meV": dse, "real": h["real"],
        }
        rows.append(row)
        target = best_real if h["real"] else best_hypo
        if dse > target["D_s_eff"]:
            upd = {"D_s_eff": dse, "name": h["name"], "D_s_charge": dsc,
                   "P_pair": pp, "Delta": Delta}
            if h["real"]:
                best_real = upd
            else:
                best_hypo = upd
    return rows, best_real, best_hypo


def best_drude_only():
    """The UNCAPPED full-Drude-weight upper bound (no gap cap, P_pair:=1) across the menu
    -- the seed's MOST optimistic reading (ignore BOTH the pairing-gap cap AND depairing).
    Positive-control diagnostic: this is huge (eV-scale) and trivially clears the wall;
    contrasting it with the honest capped D_s^sf shows the wall is held by the gap cap +
    depairing, not by a feeble carrier density."""
    best = -1.0
    name = None
    for h in HOSTS:
        dsc = ds_charge_meV(h["n3d"], h["d_nm"], h["mstar"])
        if dsc > best:
            best, name = dsc, h["name"]
    return best, name


def main():
    line = "=" * 78
    print(line)
    print("H_053  Zero-Moment Stiffness Ladder  -  decoupled magnetic-vs-charge stiffness")
    print(line)
    print("Cluster: spin-fluctuation / phase-stiffness ambient ceiling  T_BKT=(pi/2)D_s")
    print("         (confirmed wall: H_032-043, 12/12 confirm-wall; deep law = no free lunch)")
    print("Variant twist: metallic COMPENSATED ALTERMAGNET -- zero net moment is a lattice-")
    print("    symmetry property (NOT carrier starvation), so charge density n is not Mott-")
    print("    throttled; claim D_s^charge ~ n (n~10^22, 10-100x cuprate) clears 164 K.")
    print("HONEST-NULL: n and pairing-survival ANTI-CORRELATE through a SINGLE J --")
    print("    the J that makes it an altermagnet both SOURCES the glue Delta=G*J AND")
    print("    PAIR-BREAKS it; D_s^sf=min(D_s^charge, K*Delta)*P_pair (gap-capped + CC).")
    print("Sources: arXiv:2408.03999 (pairing constraints); CrSb Nat.Commun.2024 (J~1eV);")
    print("    RuO2 npj Spintronics 2024 + Cell Rep.Phys.Sci.2025 (nonmagnetic, J~0);")
    print("    MnTe arXiv:2603.00242 (1.3 eV-gap semiconductor, low n).")
    print("-" * 78)

    ds_wall_lo = ds_wall_meV(WALL_LO_K)
    ds_wall_hi = ds_wall_meV(WALL_HI_K)
    ds_wall_room = ds_wall_meV(ROOM_T_K)

    print(f"  glue strength G_GLUE (Delta=G_GLUE*J) = {G_GLUE:.3f}  (steel-man)")
    print(f"  electronic gap ceiling DELTA_ELEC     = {DELTA_ELEC_CEILING_MEV:.3f} meV (steel-man)")
    print(f"  superfluid-weight gap cap K_cap       = {K_CAP:.3f}  (D_s^sf<=K_cap*Delta)")
    print(f"  D_s* (wall_lo,134 K) = (2/pi)kB*134 = {ds_wall_lo:.4f} meV")
    print(f"  D_s* (wall_hi,164 K) = (2/pi)kB*164 = {ds_wall_hi:.4f} meV")
    print(f"  D_s* (room, 293 K)   = (2/pi)kB*293 = {ds_wall_room:.4f} meV")
    print("-" * 78)
    print("  HOST MENU  (Delta=min(G_GLUE*J,ceiling); D_s^sf=min(Dchg,K*Delta)*P_pair):")
    print(f"    {'host':<32}{'n3d[cm^-3]':>11}{'J[meV]':>8}{'Del[meV]':>9}"
          f"{'Dchg':>9}{'P_pair':>8}{'Dsf[meV]':>10}{'real':>6}")
    rows, best_real, best_hypo = scan_hosts()
    for r in rows:
        print(f"    {r['name']:<32}{r['n3d']:>11.2e}{r['J_meV']:>8.0f}{r['Delta_meV']:>9.3f}"
              f"{r['D_s_charge_meV']:>9.1f}{r['P_pair']:>8.4f}{r['D_s_eff_meV']:>10.4f}"
              f"{('Y' if r['real'] else 'HYPO'):>6}")
    print("-" * 78)

    bc_drude, bc_name = best_drude_only()
    tbkt_real = (math.pi / 2.0) * best_real["D_s_eff"] / KB_MEV_PER_K
    tbkt_hypo = (math.pi / 2.0) * best_hypo["D_s_eff"] / KB_MEV_PER_K
    print("  DECISIVE NULL -- best REAL (sourced) altermagnet host:")
    print(f"    host                              = {best_real['name']}")
    print(f"    D_s^charge (uncapped Drude)       = {best_real['D_s_charge']:.4f} meV")
    print(f"    Delta (glue from J)               = {best_real['Delta']:.4f} meV")
    print(f"    P_pair                            = {best_real['P_pair']:.4f}")
    print(f"    D_s^sf (gap-capped, honest)       = {best_real['D_s_eff']:.4f} meV")
    print(f"    T_BKT from D_s^sf                 = (pi/2)D_s/kB = {tbkt_real:.3f} K")
    margin_K = tbkt_real - WALL_LO_K
    print(f"    margin to wall_lo (134 K)         = {margin_K:+.3f} K")
    print("  DIAGNOSTIC -- engineered HYPOTHETICAL goldilocks (NOT a real material):")
    print(f"    host                              = {best_hypo['name']}")
    print(f"    D_s^sf (needs UNMEASURED {DELTA_ELEC_CEILING_MEV:.0f} meV gap) = {best_hypo['D_s_eff']:.4f} meV"
          f"  -> T_BKT={tbkt_hypo:.1f} K")
    print(f"    (this 'escape' rides on an unproven {DELTA_ELEC_CEILING_MEV:.0f} meV altermagnetic gap =")
    print("     a separate un-demonstrated room-T-glue claim = the H_032-035 glue wall.)")
    print(f"  uncapped full-Drude upper bound (no gap cap, P_pair:=1) = {bc_drude:.1f} meV "
          f"(host {bc_name})")
    print("-" * 78)

    metrics = {
        "ds_eff_real_meV": best_real["D_s_eff"],
        "ds_charge_real_meV": best_real["D_s_charge"],
        "delta_real_meV": best_real["Delta"],
        "p_pair_real": best_real["P_pair"],
        "ds_eff_hypo_meV": best_hypo["D_s_eff"],
        "ds_drude_only_upper_meV": bc_drude,
        "ds_wall_lo_meV": ds_wall_lo,
        "ds_wall_room_meV": ds_wall_room,
        "tbkt_real_K": tbkt_real,
        "delta_elec_ceiling_meV": DELTA_ELEC_CEILING_MEV,
    }

    falsifiers = [
        # F1 HONEST-NULL (DECISIVE): does the best honest superfluid stiffness D_s^sf over
        # the REAL, SOURCED altermagnet host menu (CrSb / RuO2 / MnTe / doped semimetal)
        # clear the wall? D_s^sf = min(Drude, K*Delta(J)) * P_pair, with Delta sourced from
        # the same J that depairs. Escape iff TRIGGERED. The hypothetical goldilocks is
        # EXCLUDED -- a fictional host at an unmeasured 30 meV gap is not a discovery.
        Falsifier(
            "honest_null_real_host_clears_wall",
            lambda m: m["ds_eff_real_meV"] >= m["ds_wall_lo_meV"],
            "DECISIVE honest-null: best REAL altermagnet D_s^sf >= wall D_s (134 K).",
        ),
        # F2 anti-correlation: does any REAL host have BOTH huge charge stiffness (Drude>=wall)
        # AND a surviving honest D_s^sf>=wall? (the n and pairing knobs decouple in a REAL
        # material). If yes, the seed's decoupling works without the fictional goldilocks.
        Falsifier(
            "real_high_n_and_pairing_coexist",
            lambda m: (m["ds_charge_real_meV"] >= m["ds_wall_lo_meV"]) and
                      (m["ds_eff_real_meV"] >= m["ds_wall_lo_meV"]),
            "Anti-correlation broken in a REAL host: huge Drude AND honest D_s^sf>=wall.",
        ),
        # F3 POSITIVE CONTROL: the UNCAPPED full Drude weight (no gap cap, no depairing) is
        # eV-scale and trivially clears the wall. SHOULD trigger -- documents that the wall
        # is held by the gap cap + depairing, NOT by carrier scarcity (the seed's premise
        # that high n helps is literally true for the bare Drude weight; it just isn't the
        # superfluid weight). A non-triggered F3 would be a bug.
        Falsifier(
            "uncapped_drude_clears_wall_positive_control",
            lambda m: m["ds_drude_only_upper_meV"] >= m["ds_wall_lo_meV"],
            "POSITIVE CONTROL: uncapped full Drude weight clears the wall (sanity).",
        ),
        # F4: room-T reach of the honest REAL-host superfluid stiffness.
        Falsifier(
            "real_host_reaches_room_T",
            lambda m: m["ds_eff_real_meV"] >= m["ds_wall_room_meV"],
            "Best REAL host honest D_s^sf reaches the 293 K target D_s (room-T escape).",
        ),
    ]

    res = evaluate(metrics, falsifiers)
    print("FALSIFIER LEDGER (PASS = not triggered):")
    for r in res["falsifiers"]:
        tag = "FAIL" if r["triggered"] else "PASS"
        print(f"  [{tag}] {r['name']}")
    print("-" * 78)

    f1 = next(r for r in res["falsifiers"] if r["name"] == "honest_null_real_host_clears_wall")
    null_passes_escape = bool(f1["triggered"])
    falsifiers_pass = res["n_pass"]
    n_total = res["n_total"]

    verdict = "escapes-wall" if null_passes_escape else "confirms-wall"

    print(f"  honest-null (F1) shows a REAL host clears wall? {null_passes_escape}"
          f"   real-host margin = {margin_K:+.3f} K")
    print(f"  falsifiers_pass = {falsifiers_pass}/{n_total}")
    print(f"VERDICT: {verdict}")
    print(line)


if __name__ == "__main__":
    main()
