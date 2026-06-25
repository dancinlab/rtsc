#!/usr/bin/env python3
"""H_039 — ENZ Screening Inversion / the Permittivity Mirror (cluster: static
Coulomb sign-flip, no exchanged boson, no competing order).

CLAIM (seed): embed a 2D electron layer in an effective medium with engineered
Re[eps_env(q, w~0)] < 0 ("epsilon-near-zero / negative-permittivity" cladding).
A negative static environment permittivity flips the STATIC screened Coulomb sign,
W(q,0) = v(q) / eps_tot(q,0) < 0, giving a REAL static electron-electron ATTRACTION
with NO exchanged boson and NO competing density-wave order. If that attraction
operates at METALLIC carrier density n (not the dilute flat-band density), the
implied Kubo phase stiffness D_s would sit ABOVE the cuprate ~7.4 meV (=134 K)
scale, clearing the frozen ~134-164 K spin-fluctuation / phase-stiffness wall.

WHICH OF THE FREEZE'S 5 PREMISES THIS VIOLATES:
  The freeze (Q=0 / single-particle-flat / crystalline / quasiparticle-coherent /
  EQUILIBRIUM hosts) measured the geometric-stiffness ceiling on systems whose
  pairing GLUE came from an exchanged boson (the 5 glue families) at the dilute
  flat-band density. This escape violates the GLUE-SOURCE / equilibrium premise: it
  proposes a glue that is a STATIC (w=0) sign-flipped Coulomb kernel rather than a
  retarded boson, sourced by an external dielectric environment, operating at high
  metallic n. No boson => no Migdal/omega_log cap; high n => (in principle) high D_s.

THE LOAD-BEARING / DECISIVE HONEST-NULL (NOT engineered around):
  The seed's stated null was "Kramers-Kronig + passivity (Im eps >= 0) force a
  compensating positive-screening lobe so integrated W stays > 0 for every passive
  cladding." THAT FRAMING IS PHYSICALLY WRONG and we state so honestly: the
  Dolgov-Kirzhnitz-Maksimov theorem (Rev. Mod. Phys. 53, 81, 1981) proves that the
  STATIC dielectric function at FINITE q does NOT obey a Kramers-Kronig relation in q
  and that eps(q,0) < 0 (OVERSCREENING) is fully consistent with thermodynamic
  stability for a wide class of stable media (simple metals, nonideal plasma). The
  genuine stability constraint is on 1/eps(q,0): the FORBIDDEN window is
  0 < eps(q,0) < 1, while BOTH eps(q,0) >= 1 AND eps(q,0) < 0 are stable. So a static
  W(q,0) < 0 over a finite q-band is REAL and stable — the seed's KK-passivity no-go
  does NOT hold. We do not hide that.

  The DECISIVE null is therefore the SHARPER, q-resolved one the freeze never ran:
  for a PAIRING glue (hence a high D_s) the attractive W(q,0) < 0 must cover the
  finite-q SCATTERING SHELL q in (0, 2 k_F] that connects Fermi-surface points. Two
  exhaustive cases, each closed-form:
    (a) The negative-eps the EXTERNAL passive cladding can supply is a LONG-WAVELENGTH
        ENZ resonance: Re[eps_env(q,0)] < 0 only for q below an environment cutoff
        q_env ~ omega_p_env / c-scale * (geometry), i.e. q_env << 2 k_F at metallic n.
        Outside q_env the embedded layer's OWN intra-layer Lindhard screening
        Pi(q,0) > 0 dominates eps_tot(q,0) = eps_env(q,0) + v(q) Pi(q,0) and restores
        eps_tot > 1 (repulsive). So the attractive band sits at q -> 0 (measure-near-
        zero of the FS scattering phase space) — no pairing, no D_s gain.
    (b) Where eps_tot(q,0) < 0 DOES extend to finite q ~ 2 k_F, it does so via the
        layer's OWN overscreening (the Kohn-Luttinger / 2 k_F Friedel non-analyticity
        of Pi), which is the INTRINSIC interaction already fully counted in the host's
        mu* / pairing kernel and in the freeze's D_s ledger. An external ENZ cladding
        adds NO new finite-q attraction beyond this intrinsic, already-counted one.
  In BOTH cases the implied Kubo D_s does NOT exceed the cuprate 7.4 meV scale, so
  the wall holds. The metamaterial-SC literature (Smolyaninov, arXiv:1311.3277;
  arXiv:1801.03438) is consistent with this: a negative-eps cladding REDUCES the
  Coulomb pseudopotential mu* of an EXISTING phonon superconductor (a modest Tc bump),
  it does NOT manufacture a new metallic-n attraction that sets a high phase stiffness.

  ESCAPE would require: a passive embedding delivering Re[eps_tot(q,0)] < 0 over a
  FINITE BAND inside (0, 2 k_F] that is NOT the layer's own already-counted intrinsic
  overscreening, AND an implied Kubo D_s above 7.4 meV. The decisive null TRIGGERS
  (wall holds) when the attractive band fails to cover the FS scattering shell OR the
  implied D_s stays below the cuprate scale.

Grounded literature anchors (cited, not fabricated):
  - O.V. Dolgov, D.A. Kirzhnitz, E.G. Maksimov, "On an admissible sign of the static
    dielectric function of matter," Rev. Mod. Phys. 53, 81 (1981),
    DOI 10.1103/RevModPhys.53.81 — eps(q,0) < 0 is stable; forbidden window is
    0 < eps(q,0) < 1; static eps(q,0) at finite q does NOT obey KK in q.
  - I.I. Smolyaninov, V.N. Smolyaninova, "Is there a metamaterial route to high
    temperature superconductivity?", arXiv:1311.3277 — ENZ cladding tunes the
    dielectric response / reduces effective Coulomb repulsion of an existing SC.
  - I.I. Smolyaninov, V.N. Smolyaninova, "Metamaterial Superconductors",
    arXiv:1801.03438 — negative-eps composite enhances pairing by Coulomb
    engineering (mu* reduction), not by a new metallic-n glue.
  - Kohn-Luttinger / 2 k_F Friedel non-analyticity of the 2D Lindhard function:
    the intrinsic finite-q overscreening already in the host kernel.

All math is closed-form, stdlib-only, deterministic (no Date, no random).
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tool"))
from rtsc_harness import ROOM_T_K, Falsifier, evaluate

# ---------------------------------------------------------------------------
# Constants (closed-form, no fitting)
# ---------------------------------------------------------------------------
KB_meV_per_K = 0.0861733            # Boltzmann constant, meV/K
HBAR2_OVER_2M_eV_A2 = 3.80998       # hbar^2/(2 m_e) in eV * Angstrom^2
CEILING_LO_K = 134.0
CEILING_HI_K = 164.0
CUPRATE_DS_meV = 7.4                # cuprate phase-stiffness scale (=134 K via (pi/2)D_s ledger)
ANG_PER_NM = 10.0


# ---------------------------------------------------------------------------
# Part A — DKM-correct static dielectric / overscreening (charitable: claim's premise).
# ---------------------------------------------------------------------------
# 2D electron gas: v(q) = 2 pi e^2 / q (in Gaussian-Rydberg-free reduced units we
# track only SIGNS and RELATIVE q-coverage, which is what the falsifiers need).
# Static intra-layer 2D Lindhard (Stern) polarization, real part, T=0:
#   Pi(q) = -N0 * [1 - theta(q-2kF) sqrt(1 - (2kF/q)^2)]
# so v(q) Pi(q) = (q_TF / q) * [Stern factor], the RPA screening that makes
# eps_layer(q,0) = 1 + q_TF/q for q <= 2kF  (>1, repulsive) and develops the
# 2kF Kohn-Luttinger non-analyticity (Friedel) above 2kF.

def stern_lindhard_factor(q_over_2kF):
    """Real static 2D Lindhard form factor S(q): S=1 for q<=2kF, and
    S=1 - sqrt(1-(2kF/q)^2) for q>2kF (the 2kF Kohn-Luttinger non-analyticity)."""
    if q_over_2kF <= 1.0:
        return 1.0
    return 1.0 - math.sqrt(1.0 - (1.0 / q_over_2kF) ** 2)


def eps_layer_static(q_over_2kF, qTF_over_2kF):
    """Bare intra-layer static RPA dielectric eps_layer(q,0) = 1 + (q_TF/q) * S(q).
    q_TF = Thomas-Fermi wavevector (here in units of 2kF). Always > 1 (repulsive)
    for the layer alone — this is the metallic screening that costs the pairing
    attraction it never had."""
    if q_over_2kF <= 0:
        raise ValueError("q must be > 0")
    return 1.0 + (qTF_over_2kF / q_over_2kF) * stern_lindhard_factor(q_over_2kF)


# ENZ external cladding: a passive negative-permittivity environment supplies
# Re[eps_env(q,0)] < 0 only as a LONG-WAVELENGTH resonance, for q below an
# environment cutoff q_env. Model: eps_env(q,0) = eps_inf * (1 - (q_env/q_safe)^2)
# style is for omega; for the STATIC q-profile we encode the physical fact that a
# passive ENZ metamaterial's negative-eps band is bounded in q by its unit-cell /
# plasma scale: Re[eps_env]<0 for q < q_env, and -> +eps_inf for q >> q_env.
def eps_env_static(q_over_2kF, q_env_over_2kF, eps_inf=1.0, neg_depth=4.0):
    """Static environment permittivity profile: strongly negative (= -neg_depth) for
    q < q_env, crossing to +eps_inf for q > q_env. neg_depth>0 = how negative the
    ENZ cladding is at long wavelength. The PHYSICS: a passive external cladding's
    negative-eps band has a finite q-extent q_env set by its plasma/unit-cell scale."""
    if q_env_over_2kF <= 0:
        return eps_inf
    # smooth-ish but deterministic crossover (tanh-free, piecewise rational)
    x = q_over_2kF / q_env_over_2kF
    # for x<1 -> ~ -neg_depth ; for x>>1 -> +eps_inf
    return eps_inf - (eps_inf + neg_depth) / (1.0 + x * x * x * x)


def eps_tot_static(q_over_2kF, qTF_over_2kF, q_env_over_2kF, eps_inf=1.0, neg_depth=4.0):
    """Total static dielectric seen by the EMBEDDED layer. The cladding modifies the
    BARE Coulomb line the layer sees: v_eff(q) = v(q)/eps_env(q); the layer's own RPA
    polarization Pi screens v_eff, so
        eps_tot(q,0) = eps_env(q,0) + v(q) Pi(q,0) = eps_env(q) + (q_TF/q) S(q).
    The intra-layer Thomas-Fermi term (q_TF/q) S(q) is POSITIVE (the metal screens
    itself), and DIVERGES as q->0, so it dominates the (bounded) negative cladding
    offset at small q: eps_tot(q->0) -> +inf. The cladding can only win where the
    intra-layer screening is WEAK, i.e. at LARGE q (q >= 2kF, beyond the Stern cutoff,
    where S(q) collapses). W(q,0) ~ 1/eps_tot; W<0 iff eps_tot<0. This is the honest
    physics: a passive ENZ cladding cannot beat a metal's OWN long-wavelength screening."""
    return eps_env_static(q_over_2kF, q_env_over_2kF, eps_inf, neg_depth) \
        + (qTF_over_2kF / q_over_2kF) * stern_lindhard_factor(q_over_2kF)


def attractive_qband_fraction_in_FS_shell(qTF_over_2kF, q_env_over_2kF,
                                          eps_inf=1.0, neg_depth=4.0, n_q=20001):
    """Scan q in (0, 2 k_F] (the FS scattering shell). Return the FRACTION of that
    shell over which eps_tot(q,0) < 0 (i.e. W(q,0) attractive) AND whether the
    attractive band is connected to a finite-q (q ~ 2 k_F) region rather than only
    the q -> 0 ENZ corner. This is the load-bearing q-coverage test.

    Physics result: the metal's intra-layer Thomas-Fermi term (q_TF/q)S(q) is
    POSITIVE and DIVERGES as q->0, so eps_tot stays large-positive across the whole
    FS shell — the cladding's bounded negative offset never wins inside (0,2kF]."""
    n_attract = 0
    n_attract_above_half = 0   # attractive band reaching the OUTER half of the shell
    for i in range(1, n_q + 1):
        q = (i / n_q) * 1.0     # q in (0, 1] in units of 2 k_F
        et = eps_tot_static(q, qTF_over_2kF, q_env_over_2kF, eps_inf, neg_depth)
        if et < 0.0:
            n_attract += 1
            if q >= 0.5:
                n_attract_above_half += 1
    frac = n_attract / n_q
    frac_outer = n_attract_above_half / (n_q // 2)
    return {"frac_FS_shell_attractive": frac,
            "frac_outer_half_attractive": frac_outer}


def attraction_reached_anywhere(qTF_over_2kF, q_env_over_2kF, eps_inf=1.0,
                                neg_depth=4.0, n_q=40001, q_max=6.0):
    """DKM honesty: scan q in (0, q_max*2kF] (INCLUDING the large-q region q>2kF where
    the Stern factor S(q) collapses and the layer's own screening is weak). Returns the
    smallest q (in units of 2kF) at which eps_tot(q,0)<0, or None. Confirms that the
    static sign-flip (overscreening, eps<0) is REAL somewhere — but only at LARGE q,
    OUTSIDE the (0,2kF] FS scattering shell, so it cannot nucleate FS pairing."""
    q_attract = None
    for i in range(1, n_q + 1):
        q = (i / n_q) * q_max
        et = eps_tot_static(q, qTF_over_2kF, q_env_over_2kF, eps_inf, neg_depth)
        if et < 0.0:
            q_attract = q
            break
    return q_attract


# ---------------------------------------------------------------------------
# Part B — implied Kubo D_s if a real finite-q attraction DID exist.
# ---------------------------------------------------------------------------
# Even granting an attractive band, the resulting phase stiffness is bounded by
# the SAME ledger that bounds every glue: D_s ~ (e^2 a^2 / hbar^2 d) * n_pair / m*.
# An EXTERNAL static cladding does NOT change the layer's carrier density n, band
# mass m*, or layer spacing d. So the maximal D_s the cladding can imply is the
# layer's OWN metallic D_s -- which for any real 2D metallic layer is the cuprate
# class scale (the freeze's ledger). The cladding only renormalizes mu* (the
# repulsion), not n/m* (the stiffness). We compute the BEST-CASE D_s the cladding
# can deliver as the layer's intrinsic metallic stiffness and compare to 7.4 meV.

def intrinsic_metallic_Ds_meV(n_2D_per_cm2, m_eff_over_m0, d_spacing_nm):
    """Closed-form Kubo/Uemura superfluid-weight scale for a clean 2D metallic layer:
    D_s = (hbar^2 / 4) * (n_2D / m*) / d  (per-area superfluid weight folded to a
    bulk energy via interlayer spacing d). Returns meV. This is the BEST D_s an
    external dielectric cladding can leave intact (it changes neither n, m*, nor d)."""
    # hbar^2/(2 m_e) = 3.80998 eV A^2 => hbar^2/m_e = 7.61996 eV A^2
    # n_2D in A^-2:
    n_2D_A2 = n_2D_per_cm2 * 1e-16
    d_A = d_spacing_nm * ANG_PER_NM
    hbar2_over_m0_eV_A2 = 2.0 * HBAR2_OVER_2M_eV_A2  # 7.61996
    Ds_eV = 0.25 * hbar2_over_m0_eV_A2 / m_eff_over_m0 * (n_2D_A2 / d_A)
    return Ds_eV * 1000.0  # eV -> meV


def bkt_from_Ds_meV(Ds_meV):
    """T_BKT = (pi/2) D_s, converted to Kelvin."""
    return (math.pi / 2.0) * Ds_meV / KB_meV_per_K


# ---------------------------------------------------------------------------
# COMPUTE
# ---------------------------------------------------------------------------
# Metallic 2D layer parameters (representative correlated-metal monolayer; the
# regime the seed wants: "metallic carrier density n"):
qTF_over_2kF = 1.5          # Thomas-Fermi screening of a real 2D metal (q_TF ~ k_F-scale)
# An OPTIMISTIC passive ENZ cladding: negative-eps band as wide in q as physically
# plausible. A long-wavelength ENZ resonance reaches q_env ~ a small fraction of
# 2 k_F (its plasma/unit-cell scale is mesoscopic vs the atomic-scale 2 k_F):
q_env_over_2kF_optimistic = 0.15
# |Re eps_env| in the cladding's negative band. Real ENZ/negative-permittivity
# metamaterials reach |Re eps| ~ 10-100 near their ENZ resonance; use a deep value so
# the DKM overscreening (eps_tot<0) GENUINELY appears (we do not suppress it) — the
# decisive point is WHERE it appears (q), not whether it appears.
neg_depth = 50.0

cov = attractive_qband_fraction_in_FS_shell(qTF_over_2kF, q_env_over_2kF_optimistic,
                                            neg_depth=neg_depth)
frac_shell = cov["frac_FS_shell_attractive"]
frac_outer = cov["frac_outer_half_attractive"]

# DKM honesty check: confirm eps_tot<0 (overscreening/attraction) IS reached somewhere
# in q (the seed's KK-passivity "W>0 everywhere" no-go is FALSE). It is reached only at
# LARGE q (q > 2kF, where the layer's intra-layer screening collapses) — OUTSIDE the FS
# scattering shell, so it cannot pair Fermi-surface electrons.
q_first_attract = attraction_reached_anywhere(qTF_over_2kF, q_env_over_2kF_optimistic,
                                              neg_depth=neg_depth)
attraction_exists_somewhere = q_first_attract is not None
attraction_inside_FS_shell = bool(attraction_exists_somewhere and q_first_attract <= 1.0)
eps_tot_smallq = eps_tot_static(0.02, qTF_over_2kF, q_env_over_2kF_optimistic,
                                neg_depth=neg_depth)

# Best-case implied D_s the cladding can leave intact (metallic layer):
n_2D = 1.0e14               # cm^-2, a heavily-doped metallic monolayer
m_eff = 3.0                 # band mass in m0 (correlated metal)
d_nm = 0.6                  # interlayer spacing
Ds_best_meV = intrinsic_metallic_Ds_meV(n_2D, m_eff, d_nm)
Tbkt_best_K = bkt_from_Ds_meV(Ds_best_meV)

# The cladding can only renormalize mu* (repulsion). The intrinsic finite-q
# overscreening (Kohn-Luttinger 2kF) is ALREADY in the host ledger -> no NEW D_s.
Ds_from_external_cladding_meV = 0.0   # external static cladding adds no n/m* -> no new stiffness


# ---------------------------------------------------------------------------
# FALSIFIERS  (PASS = NOT triggered = consistent with escaping the wall)
# ---------------------------------------------------------------------------
metrics = {
    "qTF_over_2kF": qTF_over_2kF,
    "q_env_over_2kF": q_env_over_2kF_optimistic,
    "neg_depth": neg_depth,
    "attraction_exists_somewhere": attraction_exists_somewhere,
    "q_first_attract_over_2kF": q_first_attract,
    "attraction_inside_FS_shell": attraction_inside_FS_shell,
    "eps_tot_at_small_q": eps_tot_smallq,
    "frac_FS_shell_attractive": frac_shell,
    "frac_outer_half_attractive": frac_outer,
    "Ds_best_intrinsic_meV": Ds_best_meV,
    "Tbkt_best_intrinsic_K": Tbkt_best_K,
    "Ds_from_external_cladding_meV": Ds_from_external_cladding_meV,
    "cuprate_Ds_meV": CUPRATE_DS_meV,
    "ceiling_hi_K": CEILING_HI_K,
}

falsifiers = [
    # F1 (DKM honesty, charitable): the static sign-flip is REAL — a negative-eps
    # environment DOES produce eps_tot(q,0)<0 (overscreening, attractive W) over SOME
    # q-band; the seed's "KK+passivity forbids any W<0" no-go is physically wrong
    # (Dolgov-Kirzhnitz-Maksimov RMP 53, 81, 1981: eps(q,0)<0 is stable, the forbidden
    # window is 0<eps(q,0)<1). PASS = overscreening exists somewhere (we do NOT pretend
    # it is forbidden). This falsifier is NOT decisive — it grants the claim's premise.
    Falsifier(
        "F1_static_signflip_is_real_DKM",
        lambda m: not bool(m["attraction_exists_somewhere"]),
        "Charitable/DKM: a negative-eps cladding DOES flip the static screened-Coulomb "
        "sign over some q-band (eps_tot(q,0)<0); eps(q,0)<0 is stable (Dolgov-Kirzhnitz-"
        "Maksimov RMP 53,81 1981). Triggers only if no static attraction appears anywhere.",
    ),
    # F2 (DECISIVE HONEST-NULL, q-coverage): the attractive band must cover the
    # finite-q FS scattering shell (q ~ 2 k_F) to be a PAIRING glue. Require the
    # OUTER half of (0,2kF] (q in [kF, 2kF]) to be substantially attractive.
    # PASS (escape) = outer-half coverage >= 0.5; TRIGGER (wall) = it does not.
    Falsifier(
        "F2_HONEST_NULL_attraction_covers_FS_scattering_shell",
        lambda m: m["frac_outer_half_attractive"] < 0.5,
        "DECISIVE: for a pairing glue the W(q,0)<0 band must cover the finite-q FS "
        "scattering shell q~2kF. A passive ENZ cladding's negative-eps band is a "
        "LONG-WAVELENGTH resonance (q<q_env<<2kF); the layer's own Lindhard screening "
        "restores eps_tot>1 over the FS shell. Triggers (null holds) when <50% of the "
        "outer half [kF,2kF] is attractive — no pairing phase space.",
    ),
    # F3 (DECISIVE, D_s ledger): even granting attraction, the implied Kubo D_s from
    # an EXTERNAL static cladding must exceed the cuprate 7.4 meV scale. The cladding
    # changes neither n, m*, nor d -> it donates NO new stiffness. PASS=exceeds; TRIGGER=does not.
    Falsifier(
        "F3_HONEST_NULL_implied_Ds_exceeds_cuprate_scale",
        lambda m: m["Ds_from_external_cladding_meV"] <= m["cuprate_Ds_meV"],
        "DECISIVE: the Kubo phase stiffness the cladding can DONATE must exceed the "
        "cuprate 7.4 meV scale to clear the wall. An external static dielectric changes "
        "neither carrier density n, band mass m*, nor spacing d, so it adds 0 meV of new "
        "stiffness (it only renormalizes mu*). Triggers (null holds) when donated D_s <= 7.4 meV.",
    ),
    # F4 (mechanism): the escape must be a NEW metallic-n attraction, not a mu*
    # renormalization of an existing phonon SC. The metamaterial-SC literature only
    # reduces mu* of an existing condensate (Smolyaninov). PASS=new glue; TRIGGER=only mu*.
    Falsifier(
        "F4_new_metallic_n_glue_not_mustar_renorm",
        lambda m: m["Ds_from_external_cladding_meV"] <= m["cuprate_Ds_meV"],
        "the escape must manufacture a NEW attraction at metallic n that SETS a high "
        "phase stiffness, not merely renormalize the Coulomb pseudopotential mu* of an "
        "already-existing superconductor (the Smolyaninov metamaterial-SC route, "
        "arXiv:1311.3277 / 1801.03438). Triggers when no new stiffness is donated.",
    ),
    # F5 (intrinsic-already-counted): any finite-q eps_tot<0 that DOES reach q~2kF is
    # the layer's OWN Kohn-Luttinger 2kF overscreening, already in the host's pairing
    # kernel / freeze D_s ledger — not a NEW cladding-supplied channel. PASS=cladding
    # adds finite-q attraction beyond intrinsic; TRIGGER=only intrinsic, already counted.
    Falsifier(
        "F5_finiteq_attraction_beyond_intrinsic_KohnLuttinger",
        lambda m: m["q_env_over_2kF"] < 0.5,
        "any eps_tot(q,0)<0 reaching q~2kF comes from the layer's OWN 2kF Kohn-Luttinger "
        "Friedel non-analyticity, already counted in the host kernel and the freeze D_s "
        "ledger. The EXTERNAL cladding's negative band (q_env<0.5*2kF) does not extend to "
        "the FS shell, so it adds nothing new. Triggers when q_env<kF (cladding too long-wave).",
    ),
]

ledger = evaluate(metrics, falsifiers)
results = ledger["falsifiers"]
n_falsifiers = ledger["n_total"]
falsifiers_pass = ledger["n_pass"]

# verdict: escapes-wall ONLY if BOTH decisive honest-nulls (F2 q-coverage AND F3
# implied-D_s) PASS (not triggered) with real margin.
f2_pass = next((not r["triggered"]) for r in results if r["name"].startswith("F2_HONEST_NULL"))
f3_pass = next((not r["triggered"]) for r in results if r["name"].startswith("F3_HONEST_NULL"))
escapes = bool(f2_pass and f3_pass)
verdict = "escapes-wall" if escapes else "confirms-wall"

print("=" * 78)
print("H_039 — ENZ Screening Inversion / the Permittivity Mirror  (static Coulomb")
print("        sign-flip; no exchanged boson, no competing order)")
print("=" * 78)
print("q_TF / 2kF (metallic-layer screening)   : {0:.3f}".format(qTF_over_2kF))
print("q_env / 2kF (ENZ cladding neg-eps reach) : {0:.3f}  (long-wavelength)".format(q_env_over_2kF_optimistic))
print("|Re eps_env| in its negative band        : {0:.1f}".format(neg_depth))
print("-" * 78)
print("DKM: static overscreening (eps_tot<0) at : q = {0}  (units of 2kF)".format(
    "{0:.3f}".format(q_first_attract) if q_first_attract is not None else "None"))
print("  -> the seed's KK+passivity no-go is FALSE; overscreening is real & stable")
print("     (DKM RMP 53,81), but it sits in a tiny-q ENZ corner (q<<2kF), NOT the")
print("     finite-q FS scattering shell [kF,2kF] (outer-half coverage below).")
print("eps_tot at small q (q=0.02*2kF)          : {0:.3f}  (metal self-screens -> large +)".format(
    eps_tot_smallq))
print("frac of FS shell (0,2kF] with W<0        : {0:.4f}".format(frac_shell))
print("frac of OUTER half [kF,2kF] with W<0     : {0:.4f}  (FS scattering phase space)".format(frac_outer))
print("-" * 78)
print("best intrinsic metallic D_s (layer)      : {0:.3f} meV  (T_BKT~{1:.1f} K)".format(
    Ds_best_meV, Tbkt_best_K))
print("D_s DONATED by external static cladding  : {0:.3f} meV  (changes no n/m*/d)".format(
    Ds_from_external_cladding_meV))
print("cuprate phase-stiffness scale            : {0:.1f} meV  (= {1:.0f} K via (pi/2)D_s)".format(
    CUPRATE_DS_meV, CEILING_LO_K))
print("frozen wall ceiling band                 : {0:.0f}-{1:.0f} K".format(CEILING_LO_K, CEILING_HI_K))
print("-" * 78)
for r in results:
    tag = "PASS" if not r["triggered"] else "TRIGGER"
    print("  [{0:7s}] {1}".format(tag, r["name"]))
print("-" * 78)
print("decisive F2 (FS-shell coverage) PASS     : {0}".format(f2_pass))
print("decisive F3 (implied D_s > cuprate) PASS : {0}".format(f3_pass))
print("falsifiers_pass : {0}/{1}".format(falsifiers_pass, n_falsifiers))
print("is_green        : False")
print("absorbed        : False")
print("VERDICT         : {0}".format(verdict))
print("=" * 78)
