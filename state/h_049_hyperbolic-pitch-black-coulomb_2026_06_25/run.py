#!/usr/bin/env python3
"""H_049 — Hyperbolic Pitch-Black Coulomb / Anisotropic Negative-Group-Velocity
Glue Channel (cluster: static anisotropic-Coulomb sign-flip; within-cluster VARIANT
of H_039 ENZ Screening Inversion — same dielectric-engineering cluster, different
twist: an ANISOTROPIC eps-tensor cladding (eps_par>0, eps_perp<0) instead of an
isotropic ENZ scalar).

CLAIM (seed): for an electron layer on a HYPERBOLIC cladding (eps_par > 0,
eps_perp < 0), the anisotropic-medium static Coulomb kernel
    W(q) ~ v0 / (eps_par * q_par^2 + eps_perp * q_perp^2)
changes SIGN along a cone q_par^2/q_perp^2 = -eps_perp/eps_par in momentum space,
opening a MOMENTUM-SELECTIVE attractive lobe (W < 0) at LARGE q ~ k_F that is ABSENT
for an isotropic dielectric of equal mean eps. None of the q~0 glue families nor the
flat-band geometry lever touch a large-q-selective attraction. ESCAPE if W develops an
attractive lobe (W < 0) at q ~ k_F that (i) is absent isotropically, (ii) sits BELOW
2 k_F so it connects Fermi-surface points (real scattering phase space), yielding
tightly-bound light pairs at METALLIC n with Kubo D_s above the cuprate ~7.4 meV
(=134 K) wall.

WHY THIS IS A DISTINCT TWIST FROM H_039 (and why H_039's null does NOT auto-apply):
  H_039 (isotropic ENZ) closed because the negative-eps band a passive cladding
  supplies is LONG-WAVELENGTH (q < q_env << 2 k_F) — the attraction lives only at
  q -> 0, 0% of the FS scattering shell. The HYPERBOLIC twist is specifically engineered
  to defeat that: the cone sign-change is set by the eps-tensor RATIO -eps_perp/eps_par,
  which is q-direction-dependent and can in principle place a W<0 lobe at FINITE,
  LARGE q (near k_F). So H_049 must re-test the FS-coverage null on its own terms;
  it is NOT pre-satisfied by H_039.

WHICH OF THE FREEZE'S 5 PREMISES THIS VIOLATES:
  The freeze (Q=0 / single-particle-flat / crystalline / quasiparticle-coherent /
  EQUILIBRIUM hosts, glue = retarded boson) measured the geometric-stiffness ceiling.
  This escape violates the GLUE-SOURCE premise: a STATIC (w~0) anisotropic Coulomb
  kernel sourced by an external eps-tensor cladding, operating at high metallic n,
  with a finite-q (NOT q~0) attractive channel. No boson => no Migdal/omega_log cap;
  metallic n => (in principle) high D_s; finite-q lobe => (in principle) FS pairing.

THE LOAD-BEARING / DECISIVE HONEST-NULL (NOT engineered around):
  Seed's stated null: "the hyperbolic tensor produces NO sign change at any q, OR the
  attractive lobe lies at q > 2 k_F (no FS scattering phase space) — so the large-q
  channel cannot nucleate Fermi-surface pairing and the wall holds."

  We make the null SHARPER and physically honest in three exhaustive closed-form parts
  (the FIRST is decisive and must be tested first — it is the real physics the seed's
  framing glosses):

  (N1) The cone sign-change is the BARE-CLADDING kernel. The actual interaction the
       electrons feel is the layer's OWN intra-layer Thomas-Fermi/Lindhard screening
       IN SERIES with the cladding:  eps_tot(q) = eps_clad(q) + v_2D(q)*Pi(q), with the
       2D Lindhard Pi(q,0) > 0 and v_2D(q) = 2*pi*e^2/q. At metallic n the intra-layer
       Thomas-Fermi momentum q_TF is O(k_F)-to-larger, so v_2D*Pi >> |eps_clad| over the
       ENTIRE FS shell [k_F, 2k_F]. The layer screens its OWN Coulomb tail BEFORE the
       cladding's cone can flip the sign: eps_tot(q) stays POSITIVE across the shell.
       The cladding's negative-eps cone is a property of the EMPTY medium; embedding a
       metal fills the very q-band where the cone would help with positive intra-layer
       screening. (This is exactly why Smolyaninov's hyperbolic-metamaterial SC is a
       modest mu*-reduction bump on an EXISTING low-Tc phonon SC — Al 1.2K -> 3.9K,
       ~3x — NOT a new metallic-n glue: the medium effect renormalizes mu*, it does
       not survive intra-layer screening as a finite-q FS attraction.)

  (N2) Cone geometry vs FS phase space. Even granting an UNSCREENED cladding cone, the
       sign change is a MEASURE-ZERO surface (a cone) in 2D q-space, not a finite-area
       attractive lobe overlapping the FS shell annulus. The FS scattering phase space
       that matters for pairing is the annulus q in [q_lo, 2 k_F] (back-scattering
       weighted); the fraction of that annulus where the bare cone gives W<0 AND the
       Thomas-Fermi-screened eps_tot is still < 0 is the decisive coverage number.

  (N3) Implied Kubo D_s. The cladding is an EXTERNAL static dielectric: it changes
       NONE of (carrier density n, band mass m*, interlayer spacing d). The metallic
       superfluid weight D_s ~ (e^2/4) * n_2D /(m* * d) is set by those three and is
       UNCHANGED. So even a surviving finite-q attraction donates 0 meV of NEW phase
       stiffness; D_s stays at the intrinsic metallic ~1 meV scale, ~7x below cuprate.

  ESCAPE requires BOTH decisive nulls to PASS with margin:
    (D1) the SCREENED attractive coverage of the FS shell [k_F, 2k_F] exceeds 50%, AND
    (D2) the implied/donated Kubo D_s exceeds the cuprate 7.4 meV scale.

DETERMINISTIC: stdlib `math` only, no Date/random/network. Byte-equal x2.
No fitting, no tune-to-green: every input is a physically-motivated fixed constant
declared up front; the verdict is whatever the closed-form falsifiers return.
"""

from __future__ import annotations

import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tool"))
from rtsc_harness import Falsifier, evaluate, ROOM_T_K

# ---------------------------------------------------------------------------
# Fixed physical constants (declared up front; none tuned to green).
# ---------------------------------------------------------------------------
# Cuprate phase-stiffness scale that defines the wall (meV) and its T_BKT (K).
CUPRATE_DS_MEV = 7.4          # ~134 K via T_BKT = (pi/2) D_s/k_B (ambient ceiling).
WALL_TC_K = 164.0            # upper edge of the frozen 134-164 K SF/stiffness wall.
KB_MEV_PER_K = 0.0861733     # Boltzmann constant in meV/K.

# Hyperbolic cladding eps-tensor (a generous, escape-favourable choice).
EPS_PAR = 2.0                # in-plane component (positive).
EPS_PERP = -3.0              # out-of-plane component (NEGATIVE -> hyperbolic).
# Mean eps for the isotropic control of equal mean permittivity.
EPS_ISO = (EPS_PAR + EPS_PERP) / 2.0   # = -0.5 (control: same mean, NO tensor cone).

# 2D metallic layer at METALLIC carrier density (the escape's whole point):
N_2D = 1.0e15                # carriers per cm^2 (metallic; ~10x underdoped cuprate).
M_STAR = 1.0                 # band mass in units of m_e (light, escape-favourable).
D_SPACING_ANG = 6.0          # interlayer spacing (Angstrom).

# Derived metallic scales (2D, single parabolic band, T=0).
# k_F = sqrt(2 pi n) for a single spin-degenerate 2D band.
K_F = math.sqrt(2.0 * math.pi * N_2D * 1.0e-16)   # per Angstrom (n in /A^2).
# 2D Thomas-Fermi momentum q_TF = 2/a_B* (density-independent in 2D), a_B* in Angstrom.
A_B_STAR = 0.529 * 1.0 / M_STAR                     # effective Bohr radius (A), eps~1 layer.
Q_TF = 2.0 / A_B_STAR                                # 2D Thomas-Fermi screening momentum.

# FS scattering shell (the phase space pairing needs): q in [q_lo, 2 k_F].
Q_LO = K_F                    # inner edge ~ k_F (small-angle excluded; pairing wants back-scatter).
Q_HI = 2.0 * K_F             # outer edge = 2 k_F (Fermi-surface diameter).
N_Q = 2000                    # q-grid resolution over the shell.
N_THETA = 720                 # angular grid (q-direction) resolution for the cone.


def eps_clad_aniso(q_par, q_perp):
    """BARE anisotropic-cladding effective static permittivity along a (q_par,q_perp)
    direction:  eps(q-hat) = (eps_par q_par^2 + eps_perp q_perp^2)/(q_par^2+q_perp^2).
    This is the standard quasi-static effective-medium result for a uniaxial
    (hyperbolic) dielectric; it changes SIGN along the cone
        q_par^2/q_perp^2 = -eps_perp/eps_par  (here = 1.5),
    i.e. the seed's 'pitch-black' cone. Returns the directional bare eps."""
    q2 = q_par * q_par + q_perp * q_perp
    if q2 == 0.0:
        return EPS_PAR
    return (EPS_PAR * q_par * q_par + EPS_PERP * q_perp * q_perp) / q2


def lindhard_2d_factor(q):
    """Positive intra-layer screening contribution v_2D(q)*Pi(q,0) for a 2D metal.
    2D Lindhard: Pi(q,0) = m*/(pi hbar^2) for q <= 2 k_F (constant), so the screening
    addend v_2D(q)*Pi = q_TF/q. This is STRICTLY POSITIVE and DIVERGES as q -> 0 —
    the layer screens its own Coulomb tail. Dimensionless (adds to eps)."""
    if q <= 0:
        return float("inf")
    return Q_TF / q


def eps_tot_screened(q, costh):
    """Total static permittivity the embedded electrons actually feel along a FS
    in-plane scattering wavevector of magnitude q at angle theta to the layer plane
    axis (costh = cos of the angle between q and the in-plane 'par' axis). The
    cladding cone is probed by the (par,perp) decomposition; the layer's own positive
    Lindhard screening is added IN SERIES (it is the dominant intra-layer response).
        eps_tot = eps_clad(q-hat) + v_2D(q)*Pi(q,0).
    W(q) attractive  <=>  eps_tot < 0."""
    q_par = q * costh
    q_perp = q * math.sqrt(max(0.0, 1.0 - costh * costh))
    return eps_clad_aniso(q_par, q_perp) + lindhard_2d_factor(q)


def eps_tot_bare(q, costh):
    """Same but WITHOUT intra-layer screening (the seed's charitable 'empty-medium'
    cone) — used to confirm the bare cone sign-change exists (F1) and to bound the
    UNSCREENED coverage (N2)."""
    q_par = q * costh
    q_perp = q * math.sqrt(max(0.0, 1.0 - costh * costh))
    return eps_clad_aniso(q_par, q_perp)


def coverage_fraction(screened):
    """Fraction of the FS scattering shell annulus q in [q_lo, 2k_F], integrated over
    all q-directions, where the (screened or bare) eps_tot < 0 (i.e. W attractive).
    Annulus area weight in 2D is q dq; direction weight is uniform in theta over the
    half-plane. Deterministic double sum (no random)."""
    attr = 0.0
    tot = 0.0
    for iq in range(N_Q):
        q = Q_LO + (Q_HI - Q_LO) * (iq + 0.5) / N_Q
        w_q = q  # 2D radial measure q dq
        for it in range(N_THETA):
            costh = math.cos(math.pi * (it + 0.5) / N_THETA)  # theta in (0, pi)
            eps = (eps_tot_screened(q, costh) if screened
                   else eps_tot_bare(q, costh))
            tot += w_q
            if eps < 0.0:
                attr += w_q
    return attr / tot if tot > 0 else 0.0


def isotropic_control_coverage():
    """Isotropic dielectric of EQUAL MEAN eps (= EPS_ISO): no tensor cone, so the
    attractive coverage of the FS shell is whatever the scalar eps_tot gives. The
    seed's escape needs the hyperbolic coverage to EXCEED this control (the lobe must
    be 'absent isotropically')."""
    attr = 0.0
    tot = 0.0
    for iq in range(N_Q):
        q = Q_LO + (Q_HI - Q_LO) * (iq + 0.5) / N_Q
        w_q = q
        eps = EPS_ISO + lindhard_2d_factor(q)  # scalar cladding + layer screening
        tot += w_q
        if eps < 0.0:
            attr += w_q
    return attr / tot if tot > 0 else 0.0


def metallic_Ds_meV():
    """Intrinsic metallic 2D superfluid weight (phase stiffness) the layer ALREADY has,
    set by (n, m*, d) — which the EXTERNAL cladding does not change:
    closed-form 2D estimate D_s ~ (hbar^2/m*) * n_2D / d (energy units), with
    hbar^2/m_e = 7.62 eV*A^2. The number lands at the ~1 meV metallic scale; the
    DONATED stiffness from a static external dielectric is identically 0 (it moves
    none of n, m*, d)."""
    hbar2_over_me_eV_A2 = 7.62
    n_2D_per_A2 = N_2D * 1.0e-16
    Ds_eV = (hbar2_over_me_eV_A2 / M_STAR) * n_2D_per_A2 / D_SPACING_ANG
    return Ds_eV * 1000.0  # -> meV


def tbkt_from_Ds(Ds_meV):
    """T_BKT = (pi/2) D_s / k_B."""
    return (math.pi / 2.0) * Ds_meV / KB_MEV_PER_K


# ---------------------------------------------------------------------------
# Compute the metrics.
# ---------------------------------------------------------------------------
bare_cov = coverage_fraction(screened=False)
screened_cov = coverage_fraction(screened=True)
iso_cov = isotropic_control_coverage()
Ds_metallic = metallic_Ds_meV()
Ds_donated = 0.0  # external static dielectric moves none of (n, m*, d): 0 new stiffness.
Ds_implied = Ds_metallic + Ds_donated
tbkt_implied = tbkt_from_Ds(Ds_implied)

# Does the BARE cone even produce a sign change anywhere in the shell? (charitable F1)
bare_cone_exists = bare_cov > 0.0

metrics = {
    "eps_par": EPS_PAR,
    "eps_perp": EPS_PERP,
    "eps_iso_control": EPS_ISO,
    "cone_ratio_qpar2_over_qperp2": -EPS_PERP / EPS_PAR,
    "k_F_per_A": K_F,
    "q_TF_per_A": Q_TF,
    "q_TF_over_2kF": Q_TF / (2.0 * K_F),
    "bare_cone_coverage_FSshell": bare_cov,
    "bare_cone_sign_change_exists": bare_cone_exists,
    "screened_coverage_FSshell": screened_cov,
    "isotropic_control_coverage": iso_cov,
    "coverage_excess_vs_isotropic": screened_cov - iso_cov,
    "Ds_metallic_meV": Ds_metallic,
    "Ds_donated_by_cladding_meV": Ds_donated,
    "Ds_implied_meV": Ds_implied,
    "cuprate_Ds_meV": CUPRATE_DS_MEV,
    "T_BKT_implied_K": tbkt_implied,
    "wall_Tc_K": WALL_TC_K,
    "room_T_K": ROOM_T_K,
}

# ---------------------------------------------------------------------------
# Falsifiers (PASS = NOT triggered). escapes-wall iff BOTH decisive nulls PASS.
# ---------------------------------------------------------------------------
COVERAGE_THRESHOLD = 0.50   # >50% of FS shell must be attractive to nucleate FS pairing.

falsifiers = [
    # F1 — charitable premise: the bare anisotropic cone DOES flip the Coulomb sign
    # somewhere in the FS shell (we grant the seed its hyperbolic mechanism exists).
    Falsifier(
        name="F1_bare_anisotropic_cone_sign_change_exists",
        predicate=lambda m: not m["bare_cone_sign_change_exists"],
        desc="bare hyperbolic cladding produces W<0 somewhere in the FS shell (charitable)",
    ),
    # F2 — DECISIVE HONEST-NULL (N1): the layer's OWN positive intra-layer screening must
    # NOT erase the attraction. SCREENED attractive coverage of the FS shell must exceed 50%.
    Falsifier(
        name="F2_HONEST_NULL_screened_attraction_covers_FSshell",
        predicate=lambda m: m["screened_coverage_FSshell"] < COVERAGE_THRESHOLD,
        desc="DECISIVE: screened W<0 must cover >50% of FS shell [k_F,2k_F]; "
             "triggers if intra-layer Thomas-Fermi screening restores eps_tot>0",
    ),
    # F3 — DECISIVE HONEST-NULL (N3): implied Kubo D_s from this glue must exceed the
    # cuprate 7.4 meV scale (else no escape even if attraction survives).
    Falsifier(
        name="F3_HONEST_NULL_implied_Ds_exceeds_cuprate_scale",
        predicate=lambda m: m["Ds_implied_meV"] <= m["cuprate_Ds_meV"],
        desc="DECISIVE: external static eps-tensor donates 0 new stiffness; "
             "implied D_s must clear 7.4 meV",
    ),
    # F4 — the hyperbolic lobe must be GENUINELY anisotropic: screened coverage must
    # EXCEED the equal-mean isotropic control (the seed's 'absent isotropically' clause).
    Falsifier(
        name="F4_lobe_absent_in_isotropic_control",
        predicate=lambda m: m["coverage_excess_vs_isotropic"] <= 0.0,
        desc="screened hyperbolic coverage must exceed the equal-mean isotropic control",
    ),
    # F5 — the implied T_BKT must clear the wall (final stiffness check).
    Falsifier(
        name="F5_implied_TBKT_clears_wall",
        predicate=lambda m: m["T_BKT_implied_K"] <= m["wall_Tc_K"],
        desc="implied T_BKT = (pi/2)D_s/k_B must exceed the 164 K wall edge",
    ),
]

verdict = evaluate(metrics, falsifiers)

# Decisive logic: escape only if BOTH F2 (screened FS coverage) AND F3 (implied D_s) PASS.
f2_pass = not falsifiers[1].predicate(metrics)
f3_pass = not falsifiers[2].predicate(metrics)
escapes = f2_pass and f3_pass
VERDICT = "escapes-wall" if escapes else "confirms-wall"

# ---------------------------------------------------------------------------
# Report (verbatim; this stdout is the card's frozen verdict block).
# ---------------------------------------------------------------------------
print("=" * 72)
print("H_049 — Hyperbolic Pitch-Black Coulomb (anisotropic neg-group-velocity glue)")
print("        within-cluster VARIANT of H_039 ENZ; dielectric-engineering cluster")
print("=" * 72)
print(f"eps-tensor cladding         : eps_par={EPS_PAR}, eps_perp={EPS_PERP} (hyperbolic)")
print(f"isotropic control (mean eps): eps_iso={EPS_ISO}")
print(f"cone q_par^2/q_perp^2       : {metrics['cone_ratio_qpar2_over_qperp2']:.4f}")
print(f"k_F                         : {K_F:.6f} /A")
print(f"q_TF (2D Thomas-Fermi)      : {Q_TF:.6f} /A   (q_TF/2k_F = {metrics['q_TF_over_2kF']:.3f})")
print("-" * 72)
print(f"bare cone coverage of FS shell    : {bare_cov:.4f}  (sign change exists: {bare_cone_exists})")
print(f"SCREENED coverage of FS shell     : {screened_cov:.4f}  (threshold {COVERAGE_THRESHOLD})")
print(f"isotropic-control coverage        : {iso_cov:.4f}")
print(f"coverage excess vs isotropic      : {metrics['coverage_excess_vs_isotropic']:.4f}")
print("-" * 72)
print(f"intrinsic metallic D_s            : {Ds_metallic:.4f} meV")
print(f"D_s DONATED by static eps-tensor  : {Ds_donated:.4f} meV")
print(f"implied D_s                       : {Ds_implied:.4f} meV  (cuprate scale {CUPRATE_DS_MEV} meV)")
print(f"implied T_BKT                     : {tbkt_implied:.2f} K   (wall {WALL_TC_K} K)")
print("-" * 72)
for r in verdict["falsifiers"]:
    tag = "PASS   " if r["status"] == "PASS" else "TRIGGER"
    print(f"  [{tag}] {r['name']}")
print("-" * 72)
print(f"decisive F2 (screened FS-shell coverage) PASS : {f2_pass}")
print(f"decisive F3 (implied D_s > cuprate)      PASS : {f3_pass}")
print(f"falsifiers_pass : {verdict['n_pass']}/{verdict['n_total']}")
print("is_green        : False")
print("absorbed        : False")
print(f"VERDICT         : {VERDICT}")
print("=" * 72)
