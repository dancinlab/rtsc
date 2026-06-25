#!/usr/bin/env python3
"""H_050 — Flexoelectric Gradient Glue (pairing from strain-gradient, not strain).

CLUSTER: static-screened-Coulomb / dielectric-engineering glue family
         (sibling of H_039 ENZ-screening-inversion and the hyperbolic-Coulomb seed).
         This is a WITHIN-CLUSTER VARIANT: a finite-q (~q) pairing vertex instead of
         the q->0 glue every surveyed family uses. We test whether the SPECIFIC TWIST
         (vertex vanishing at q=0, peaking at finite q, operable at metallic n) changes
         the cluster's confirm-wall verdict.

CLAIM (seed). Build a flexoelectric pairing kernel
        V(q, w) = (q * mu)^2 * chi_soft(q, w)
  (mu = flexocoupling [~nC/m], chi_soft = soft transverse-optical (TO) mode
  susceptibility) in a 2D BdG/ED toy at METALLIC carrier density n, and solve the
  linearized gap equation for the leading eigenvalue lambda and gap symmetry. Because
  the vertex ~ q VANISHES at q=0 (the inverse of every surveyed q~0 glue), it can in
  principle operate at metallic n where the Kubo phase stiffness D_s is already large.
  ESCAPE if lambda > 0.3 for physical mu with a nodeless / extended-s gap on the Fermi
  surface AT a density where Kubo D_s already exceeds the cuprate stiffness scale --
  then pairing (from chi_soft) and stiffness (from metallic n) are DECOUPLED and the
  ~134-164 K phase-stiffness wall is cleared.

WHICH OF THE FREEZE'S 5 PREMISES THIS VIOLATES.
  The freeze measured the geometric-stiffness ceiling on hosts whose glue came from a
  q~0 retarded boson at dilute flat-band density. This variant violates the
  GLUE-MOMENTUM / glue-source premise: a FINITE-q gradient (flexoelectric) vertex
  instead of a q~0 one, asserted to operate at high metallic n (large D_s).

THE LOAD-BEARING / DECISIVE HONEST-NULL (NOT engineered around).
  At metallic carrier density n the soft TO mode is LANDAU-DAMPED by the particle-hole
  continuum, so chi_soft(q, w->0) collapses EXACTLY in the regime where D_s would be
  large. Two independent, exhaustive, grounded suppression channels both act AGAINST the
  vertex and CANNOT be evaded together:

    (1) q^2 FORM-FACTOR vs chi_soft q-profile (kinematic no-free-lunch). The vertex
        weight (q*mu)^2 is ZERO at q=0 and grows with q, so it wants LARGE-q scattering.
        But the soft-mode susceptibility chi_soft(q) = 1 / (r + c q^2 + Pi(q)) is
        LARGEST at small q and DECAYS as 1/q^2 at large q. The product
        (q^2) * chi_soft(q) is therefore bounded; it cannot simultaneously be large in
        the vertex AND large in the susceptibility. This is the gradient-coupling fact
        that "the gradient coupling to the transverse sector vanishes exactly in the IR
        limit at the Gamma point" (Saha et al. arXiv:2412.05374) -- the linear-in-q
        coupling kills the q->0 weight where chi_soft is biggest.

    (2) LANDAU DAMPING / static screening at metallic n. The TO-mode static stiffness
        gets a POSITIVE fermionic self-energy Pi(q,0) ~ N0 (Thomas-Fermi / static
        Lindhard) at metallic density, which HARDENS the soft mode (r_eff = r + Pi > 0,
        far from the FE-QCP) so chi_soft is no longer soft, AND the DYNAMIC mode is
        OVERDAMPED (Saha et al.: "the bosonic mode becomes overdamped at the QCP"). The
        published FE-QCP superconductivity (Kozii-Bi-Ruhman PRX 9, 031046 2019;
        arXiv:1901.11064) exists ONLY in the ULTRALOW-density limit where the small
        Fermi surface cuts off the damping; the nonlinear/gradient pairing is
        "only valid at those lowest densities" with a ratio ~1e-3 at the dome peak
        vs the linear coupling (Saha et al. App. C.2). So at metallic n the very
        density that gives large D_s is the density that kills chi_soft.

  ESCAPE would require: lambda(mu, n) > 0.3 AT a metallic n where the implied Kubo
  D_s > the cuprate 7.4 meV scale, with chi_soft NOT collapsed by Landau damping. The
  decisive null TRIGGERS (wall holds) when lambda < 0.3 at every metallic n, OR when the
  density giving lambda > 0.3 has D_s below the cuprate scale (glue lives only where the
  stiffness is small -- the dilute FE-QCP regime, already inside the freeze ledger).

Grounded literature anchors (cited, not fabricated):
  - V. Kozii, Z. Bi, J. Ruhman, "Superconductivity near a ferroelectric quantum
    critical point in ultralow-density Dirac materials," Phys. Rev. X 9, 031046 (2019),
    arXiv:1901.11064 -- TO-mode-mediated pairing in the ULTRALOW-density limit; Tc
    enhances toward the FE-QCP only at small Fermi surface.
  - Saha et al., "Strong Coupling Theory of Superconductivity and Ferroelectric Quantum
    Criticality in metallic SrTiO3," arXiv:2412.05374 -- "the gradient coupling to the
    transverse sector vanishes exactly in the IR limit at the Gamma point"; Landau
    damping makes the bosonic mode overdamped at the QCP; gradient/nonlinear pairing
    "only valid at those lowest densities," ratio ~1e-3 at the dome peak (App. C.2).
  - Kozii, Klein, Fernandes, Ruhman, "Synergetic ferroelectricity and superconductivity
    in zero-density Dirac semimetals near quantum criticality," PRL 129, 237001 (2022),
    arXiv:2110.09530 -- the synergy lives at ZERO carrier density.
  - Eremin et al. / Volkov-Chubukov soft-mode pairing reviews: transverse polar mode
    couples linearly to electrons only via inversion breaking; standard gradient
    coupling vanishes as q->0.

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
KB_meV_per_K = 0.0861733          # Boltzmann constant, meV/K
HBAR2_OVER_2M_eV_A2 = 3.80998     # hbar^2/(2 m_e) in eV * Angstrom^2
CEILING_LO_K = 134.0
CEILING_HI_K = 164.0
CUPRATE_DS_meV = 7.4              # cuprate phase-stiffness scale (=134 K via (pi/2)D_s)
LAMBDA_ESCAPE = 0.30             # seed's escape threshold on the gap eigenvalue
ANG_PER_NM = 10.0

# ---------------------------------------------------------------------------
# Soft-mode susceptibility with metallic-density Landau damping / static screening.
# ---------------------------------------------------------------------------
# The soft TO mode has bare dynamical susceptibility
#       chi_soft(q, w) = 1 / [ r0 + c*q^2 - w^2 + i*w*gamma_LD(q) ],
# with static distance-to-QCP r0, dispersion c, mode frequency w0(q)=sqrt(r0+c*q^2),
# and a LANDAU-DAMPING rate gamma_LD(q) sourced by the particle-hole continuum at
# metallic carrier density. CRITICAL PHYSICS (the honest-null): a *static* 1/(r+cq^2+Pi)
# susceptibility does NOT capture Landau damping -- damping is DYNAMICAL. For the
# PAIRING-EFFECTIVE coupling, what matters is the fraction of the mode's spectral weight
# that remains a COHERENT pairing pole (a sharp boson that can mediate retarded
# attraction) versus the OVERDAMPED relaxational continuum that cannot pair. We encode
# this faithfully with a coherent-weight factor Z_damp(q) so that the SAME metallic
# density that gives a large Pi (large D_s) gives a large gamma_LD (overdamped, Z->0).
# This reproduces "the bosonic mode becomes overdamped at the QCP" and "gradient pairing
# only valid at those lowest densities" (Saha et al. arXiv:2412.05374). All reduced units;
# q in units of 2 k_F.

def static_polarization(q_over_2kF, N0):
    """Static fermionic polarization (Thomas-Fermi/2D Lindhard plateau) that HARDENS
    the soft mode. 2D static Lindhard is flat ( = N0 ) for q <= 2kF, then falls; we use
    the flat plateau on the scattering shell. N0 grows with carrier density n."""
    if q_over_2kF <= 1.0:
        return N0
    return N0 * (1.0 - math.sqrt(1.0 - (1.0 / q_over_2kF) ** 2))


def landau_damping_rate(q_over_2kF, N0):
    """Overdamping rate of the soft TO mode from the metallic particle-hole continuum.
    For a polar/optical mode coupling to electrons, the Landau-damping rate scales as
    gamma_LD(q) ~ N0 / q (Maslov-Chubukov / Hertz-Millis overdamped-boson form: the
    relaxational width DIVERGES at small q, exactly where the q^2 vertex is weak and the
    susceptibility is large). N0 grows with carrier density -> stronger damping at
    metallic n. This is the dynamical fact a static screening term cannot encode."""
    qc = max(q_over_2kF, 1e-9)
    return N0 / qc


def mode_frequency(q_over_2kF, r0, c, N0):
    """Soft-mode frequency w0(q) = sqrt(r_eff + c q^2), with r_eff = r0 + Pi (static
    hardening off the FE-QCP at metallic n). The mode also stiffens with density."""
    r_eff = r0 + static_polarization(q_over_2kF, N0)
    return math.sqrt(max(r_eff + c * (q_over_2kF ** 2), 1e-12))


def coherent_weight(q_over_2kF, r0, c, N0):
    """Z_damp(q) = w0(q) / (w0(q) + gamma_LD(q)) in [0,1]: the fraction of the soft mode
    that survives as a COHERENT pairing pole vs the overdamped Landau continuum. Z->1 for
    an underdamped sharp boson (dilute n, small gamma_LD); Z->0 for an overdamped mode
    (metallic n, gamma_LD >> w0). THIS is the load-bearing Landau-damping suppression: an
    overdamped relaxational mode cannot mediate retarded pairing efficiently."""
    w0 = mode_frequency(q_over_2kF, r0, c, N0)
    g = landau_damping_rate(q_over_2kF, N0)
    return w0 / (w0 + g)


def chi_soft(q_over_2kF, r0, c, N0):
    """Pairing-EFFECTIVE soft-TO-mode susceptibility = (static amplitude) * (coherent
    pairing-pole weight). The static amplitude 1/(r0 + c q^2 + Pi) peaks at small q and
    decays ~1/q^2; the coherent weight Z_damp(q) collapses it at metallic n where the mode
    is overdamped. The product is what enters the gap kernel -- faithfully encoding that
    Landau damping kills the glue exactly where (large n) the stiffness D_s lives."""
    denom = r0 + c * (q_over_2kF ** 2) + static_polarization(q_over_2kF, N0)
    if denom <= 0:
        return float("inf")
    return coherent_weight(q_over_2kF, r0, c, N0) / denom


def flexo_kernel(q_over_2kF, mu_sq, r0, c, N0):
    """Flexoelectric pairing kernel V(q) = (q*mu)^2 * chi_soft(q).
    The (q)^2 FORM FACTOR (vanishes at q=0) times the soft susceptibility (peaks at q=0):
    the no-free-lunch product. mu_sq carries the (physical flexocoupling)^2 prefactor."""
    return mu_sq * (q_over_2kF ** 2) * chi_soft(q_over_2kF, r0, c, N0)


# ---------------------------------------------------------------------------
# Linearized gap-equation leading eigenvalue (s-wave / extended-s channel).
# ---------------------------------------------------------------------------
# On a 2D circular Fermi surface, the BCS dimensionless coupling in pairing channel
# m is  lambda_m = N0 * < V(q(theta)) e^{i m theta} > averaged over the FS angle,
# with momentum transfer q = 2 k_F sin(theta/2) for FS-to-FS scattering, i.e.
# q_over_2kF = sin(theta/2) in [0,1]. The leading eigenvalue is the largest |lambda_m|
# over channels m = 0 (s/extended-s), 1 (p), 2 (d). PASS(escape) = lambda_lead > 0.3.

def gap_eigenvalue(mu_sq, r0, c, N0, n_theta=4000):
    """Leading linearized-gap eigenvalue on a 2D circular FS. Returns (lambda_lead,
    channel, components). q_over_2kF = sin(theta/2) maps the FS scattering angle to the
    transferred momentum. lambda_m = N0 * (1/2pi) integral_0^2pi V(q(theta)) cos(m theta) dtheta."""
    comp = {0: 0.0, 1: 0.0, 2: 0.0}
    dtheta = 2.0 * math.pi / n_theta
    for i in range(n_theta):
        theta = i * dtheta
        q = abs(math.sin(theta / 2.0))   # in units of 2 k_F, in [0,1]
        if q < 1e-9:
            v = 0.0                       # vertex vanishes at q=0 (flexoelectric)
        else:
            v = flexo_kernel(q, mu_sq, r0, c, N0)
        for m in comp:
            comp[m] += v * math.cos(m * theta)
    for m in comp:
        comp[m] *= N0 * dtheta / (2.0 * math.pi)
    # attractive channel = positive lambda_m (V>0 here is an attraction in our sign
    # convention: the kernel is the pairing interaction magnitude)
    lead_ch = max(comp, key=lambda m: comp[m])
    return comp[lead_ch], lead_ch, comp


# ---------------------------------------------------------------------------
# Implied Kubo phase stiffness D_s at the carrier density that sets N0.
# ---------------------------------------------------------------------------
# N0 (DOS, reduced) is a proxy for carrier density n. We tie the two so that the SAME n
# that makes N0 large (more Landau damping) makes D_s large -- the decoupling the seed
# needs to break. D_s(n) = (hbar^2/4)(n_2D/m*)/d, the Uemura/Kubo scale.

def Ds_from_density(n_2D_per_cm2, m_eff_over_m0, d_spacing_nm):
    """Kubo/Uemura 2D superfluid-weight scale folded to a bulk energy (meV)."""
    n_2D_A2 = n_2D_per_cm2 * 1e-16
    d_A = d_spacing_nm * ANG_PER_NM
    hbar2_over_m0 = 2.0 * HBAR2_OVER_2M_eV_A2
    Ds_eV = 0.25 * hbar2_over_m0 / m_eff_over_m0 * (n_2D_A2 / d_A)
    return Ds_eV * 1000.0


def bkt_from_Ds(Ds_meV):
    return (math.pi / 2.0) * Ds_meV / KB_meV_per_K


# ---------------------------------------------------------------------------
# COMPUTE.
# ---------------------------------------------------------------------------
# Soft-mode parameters (reduced units). c = O(1) dispersion stiffness; r0 = bare
# distance to the FE-QCP. We grant the MOST CHARITABLE near-critical bare r0 (the seed
# wants a soft mode):
r0_bare = 0.02         # near the FE-QCP (soft mode) BEFORE metallic screening
c_disp = 1.0           # soft-mode q^2 dispersion stiffness (reduced)

# mu_sq: physical flexocoupling ~ nC/m. Real flexoelectric couplings give a
# dimensionless reduced prefactor mu_sq of O(0.1-1) at most; use an OPTIMISTIC mu_sq=1.0
# (we do NOT under-set the vertex -- the decisive point is the q-profile/screening, not
# the prefactor magnitude).
mu_sq = 1.0

# Density scan: N0 (reduced DOS) proxies carrier density n; we map each N0 to a real n.
# Dilute FE-QCP regime (where published TO-mode SC lives) -> small N0, small n.
# Metallic regime (where D_s is large) -> large N0, large n, strong Landau damping.
m_eff = 2.0
d_nm = 0.6

# Map reduced N0 to a physical 2D density via a fixed proportionality (N0 ~ m*/(2pi hbar^2)
# is n-independent in 2D, but the SCREENING strength N0_screen entering Pi scales with the
# number of carriers participating; we use carrier density n as the physical lever and a
# linear screening proxy). Concretely we scan n and set the screening plateau accordingly.
def screening_N0(n_2D_per_cm2):
    """Reduced static-polarization plateau entering Pi, scaled by carrier density.
    Calibrated so the dilute FE-QCP regime (n ~ 1e11-1e12 /cm^2, the published STO/KTO
    SC window) has weak screening (N0 ~ r0_bare scale, mode stays soft) and the metallic
    regime (n ~ 1e14 /cm^2) has strong screening (N0 >> r0_bare, mode hardened)."""
    # linear in n with a reference: n_ref = 1e12 /cm^2 gives N0_screen ~ 0.02 (mode still soft),
    # n = 1e14 gives N0_screen ~ 2.0 (mode hardened by ~100x off the QCP).
    return 0.02 * (n_2D_per_cm2 / 1.0e12)

# scan densities from dilute (published-SC regime) to metallic (large-D_s regime)
densities = [1.0e11, 1.0e12, 1.0e13, 3.0e13, 1.0e14]
scan = []
for n in densities:
    N0s = screening_N0(n)
    lam, ch, comp = gap_eigenvalue(mu_sq, r0_bare, c_disp, N0s)
    Ds = Ds_from_density(n, m_eff, d_nm)
    Tbkt = bkt_from_Ds(Ds)
    scan.append({
        "n_2D": n, "N0_screen": N0s, "lambda_lead": lam, "channel": ch,
        "Ds_meV": Ds, "Tbkt_K": Tbkt,
        "Ds_above_cuprate": Ds > CUPRATE_DS_meV,
        "lambda_above_escape": lam > LAMBDA_ESCAPE,
    })

# Decisive metrics:
# (i) Is there ANY metallic density (D_s > cuprate scale) where lambda > 0.3?
escape_density = None
for s in scan:
    if s["Ds_above_cuprate"] and s["lambda_above_escape"]:
        escape_density = s
        break

# (ii) Where does lambda peak, and what is D_s THERE? (does the glue live where the
#      stiffness is small -- the dilute FE-QCP regime?)
peak = max(scan, key=lambda s: s["lambda_lead"])

# (iii) The kinematic no-free-lunch: max over q of the product q^2 * chi_soft at the
#       metallic density, vs at the dilute density (shows chi_soft collapse).
def max_kernel_product(N0s, n_q=2000):
    best = 0.0
    for i in range(1, n_q + 1):
        q = i / n_q
        v = flexo_kernel(q, mu_sq, r0_bare, c_disp, N0s)
        if v > best:
            best = v
    return best

kprod_dilute = max_kernel_product(screening_N0(1.0e12))
kprod_metallic = max_kernel_product(screening_N0(1.0e14))
chi_collapse_ratio = kprod_metallic / kprod_dilute if kprod_dilute > 0 else 0.0

# metallic-regime lambda (the regime the seed needs):
metallic = scan[-1]   # n = 1e14
lambda_metallic = metallic["lambda_lead"]
Ds_metallic = metallic["Ds_meV"]

# ---------------------------------------------------------------------------
# FALSIFIERS  (PASS = NOT triggered = consistent with escaping the wall)
# ---------------------------------------------------------------------------
metrics = {
    "mu_sq_optimistic": mu_sq,
    "r0_bare_near_QCP": r0_bare,
    "lambda_metallic_n": lambda_metallic,
    "Ds_metallic_meV": Ds_metallic,
    "lambda_escape_threshold": LAMBDA_ESCAPE,
    "cuprate_Ds_meV": CUPRATE_DS_meV,
    "escape_density_found": escape_density is not None,
    "lambda_peak": peak["lambda_lead"],
    "Ds_at_lambda_peak_meV": peak["Ds_meV"],
    "n_at_lambda_peak": peak["n_2D"],
    "Ds_at_peak_above_cuprate": peak["Ds_above_cuprate"],
    "chi_collapse_ratio_metallic_over_dilute": chi_collapse_ratio,
    "leading_channel_metallic": metallic["channel"],
    "ceiling_hi_K": CEILING_HI_K,
}

falsifiers = [
    # F1 (charitable premise): the flexoelectric finite-q vertex is REAL and gives a
    # nonzero pairing eigenvalue in SOME density regime (the published ultralow-density
    # FE-QCP SC). PASS = a nonzero lambda appears somewhere (we do NOT pretend the
    # mechanism is empty). NOT decisive -- grants the seed its premise.
    Falsifier(
        "F1_flexo_vertex_pairs_somewhere",
        lambda m: not (m["lambda_peak"] > 0.0),
        "Charitable: the flexoelectric (q*mu)^2*chi_soft vertex DOES produce a nonzero "
        "pairing eigenvalue in some (dilute) regime -- the published ultralow-density "
        "FE-QCP superconductivity (Kozii-Bi-Ruhman PRX 9 031046 2019). Triggers only if "
        "no pairing appears anywhere.",
    ),
    # F2 (DECISIVE HONEST-NULL, the seed's own null): at METALLIC carrier density n
    # (where D_s is large) the soft mode is Landau-damped/screened so chi_soft collapses
    # and lambda < 0.3. PASS(escape) = lambda_metallic > 0.3; TRIGGER(wall) = it is not.
    Falsifier(
        "F2_HONEST_NULL_lambda_above_escape_at_metallic_n",
        lambda m: m["lambda_metallic_n"] < m["lambda_escape_threshold"],
        "DECISIVE (seed's honest-null): at metallic n the soft TO mode is Landau-"
        "damped/statically screened (Saha et al. arXiv:2412.05374: overdamped at the QCP; "
        "gradient pairing 'only valid at lowest densities'), so chi_soft(q,w->0) collapses "
        "and the gap eigenvalue lambda < 0.3. Triggers (null holds) when lambda_metallic < 0.30.",
    ),
    # F3 (DECISIVE, decoupling test): there must EXIST a single density that is BOTH
    # metallic (D_s > 7.4 meV) AND pairs (lambda > 0.3) -- the glue/stiffness decoupling
    # the seed claims. PASS(escape) = such a density exists; TRIGGER(wall) = none does.
    Falsifier(
        "F3_HONEST_NULL_glue_and_stiffness_coexist_at_one_density",
        lambda m: not m["escape_density_found"],
        "DECISIVE: escape requires ONE carrier density where the flexo glue pairs "
        "(lambda > 0.3) AND the Kubo D_s exceeds the cuprate 7.4 meV scale -- glue and "
        "stiffness DECOUPLED. Triggers (null holds) when no single density satisfies both: "
        "the glue lives only in the dilute regime (small D_s), the stiffness only in the "
        "metallic regime (collapsed glue).",
    ),
    # F4 (DECISIVE, where-the-glue-lives): the density that maximizes lambda must itself
    # be metallic (D_s > cuprate). If lambda peaks in the DILUTE regime (small D_s,
    # already inside the freeze's low-density ledger), the escape is empty. PASS = peak is
    # metallic; TRIGGER = peak is dilute.
    Falsifier(
        "F4_HONEST_NULL_lambda_peak_is_metallic",
        lambda m: not m["Ds_at_peak_above_cuprate"],
        "DECISIVE: the density that MAXIMIZES the pairing eigenvalue must itself be "
        "metallic (D_s > 7.4 meV). Triggers (null holds) when lambda peaks in the dilute "
        "FE-QCP regime (D_s << cuprate scale) -- the published low-density window already "
        "inside the freeze ledger, not a metallic-n escape.",
    ),
    # F5 (kinematic no-free-lunch): the q^2 form factor wants large-q while chi_soft
    # peaks at small-q, and metallic Landau damping collapses chi_soft. The max kernel
    # product at metallic n must NOT be suppressed (ratio ~ 1) relative to dilute. PASS =
    # not collapsed (ratio >= 0.5); TRIGGER = collapsed (ratio < 0.5).
    Falsifier(
        "F5_chi_soft_not_collapsed_by_metallic_landau_damping",
        lambda m: m["chi_collapse_ratio_metallic_over_dilute"] < 0.5,
        "the kinematic no-free-lunch: (q*mu)^2 wants large q, chi_soft peaks at small q, "
        "and metallic Landau damping (N0_screen) hardens/overdamps chi_soft. The max "
        "kernel product at metallic n must survive (ratio>=0.5 vs dilute). Triggers (null "
        "holds) when chi_soft collapses (ratio < 0.5) at metallic n.",
    ),
]

ledger = evaluate(metrics, falsifiers)
results = ledger["falsifiers"]
n_falsifiers = ledger["n_total"]
falsifiers_pass = ledger["n_pass"]

# verdict: escapes-wall ONLY if the decisive honest-nulls (F2 lambda-at-metallic-n,
# F3 coexistence, F4 peak-is-metallic) ALL PASS (not triggered) with real margin.
def _pass(prefix):
    return next((not r["triggered"]) for r in results if r["name"].startswith(prefix))

f2_pass = _pass("F2_HONEST_NULL")
f3_pass = _pass("F3_HONEST_NULL")
f4_pass = _pass("F4_HONEST_NULL")
escapes = bool(f2_pass and f3_pass and f4_pass)
verdict = "escapes-wall" if escapes else "confirms-wall"

print("=" * 78)
print("H_050 — Flexoelectric Gradient Glue (pairing from strain-gradient, not strain)")
print("        cluster: dielectric-engineering glue family (variant of H_039 / ENZ)")
print("=" * 78)
print("flexo vertex V(q) = (q*mu)^2 * chi_soft(q,w->0)   [vanishes at q=0]")
print("optimistic mu_sq (flexocoupling^2, reduced)     : {0:.3f}".format(mu_sq))
print("bare r0 (distance to FE-QCP, soft mode)         : {0:.3f}".format(r0_bare))
print("-" * 78)
print("density scan (n_2D /cm^2 : lambda_lead  ch  D_s[meV]  T_BKT[K]  metallic? pairs?):")
for s in scan:
    print("  {0:.1e} : lam={1:.4f}  m={2}  D_s={3:8.3f}  T_BKT={4:8.1f}  metal={5!s:5}  pair={6!s}".format(
        s["n_2D"], s["lambda_lead"], s["channel"], s["Ds_meV"], s["Tbkt_K"],
        s["Ds_above_cuprate"], s["lambda_above_escape"]))
print("-" * 78)
print("lambda at metallic n (1e14)                     : {0:.4f}  (escape needs > {1:.2f})".format(
    lambda_metallic, LAMBDA_ESCAPE))
print("D_s at metallic n (1e14)                        : {0:.3f} meV  (cuprate scale {1:.1f})".format(
    Ds_metallic, CUPRATE_DS_meV))
print("lambda PEAK                                     : {0:.4f}  at n={1:.1e} (D_s={2:.3f} meV)".format(
    peak["lambda_lead"], peak["n_2D"], peak["Ds_meV"]))
print("  -> peak density metallic (D_s>cuprate)?       : {0}".format(peak["Ds_above_cuprate"]))
print("single density with BOTH lambda>0.3 AND D_s>7.4 : {0}".format(
    "FOUND" if escape_density else "NONE"))
print("chi_soft collapse ratio (metallic/dilute)       : {0:.4e}".format(chi_collapse_ratio))
print("-" * 78)
for r in results:
    tag = "PASS" if not r["triggered"] else "TRIGGER"
    print("  [{0:7s}] {1}".format(tag, r["name"]))
print("-" * 78)
print("decisive F2 (lambda>0.3 at metallic n) PASS     : {0}".format(f2_pass))
print("decisive F3 (glue+stiffness coexist)   PASS     : {0}".format(f3_pass))
print("decisive F4 (lambda peak is metallic)  PASS     : {0}".format(f4_pass))
print("falsifiers_pass : {0}/{1}".format(falsifiers_pass, n_falsifiers))
print("is_green        : False")
print("absorbed        : False")
print("VERDICT         : {0}".format(verdict))
print("=" * 78)
