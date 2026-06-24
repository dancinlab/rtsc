"""rtsc_harness — shared runnable harness for HYPOTHESES hypothesis cards.

Deterministic, dependency-free (stdlib `math` only) primitives for the
room-temperature superconductor (RTSC) campaign. HYPOTHESES cards reference these
functions from their per-hypothesis run scripts under `state/<hX>/` (anima-parity:
shared machinery lives in repo-root `tool/`, per-hypothesis runs live in `state/`).

Heavy compute (DFT / DFPT / el-ph) lives in `src/` and on cloud pods; this harness
holds only the closed-form / threshold logic a card's falsifiers are evaluated against.
No fitting, no hidden constants beyond documented defaults. Mirrors the Falsifier /
evaluate API of the sibling lumen `tool/lumen_optics.py` so both repos share one idiom.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


# --- ambient-pressure context -------------------------------------------------

#: Highest confirmed superconducting T_c at ambient pressure (cuprate ceiling, K).
AMBIENT_TC_CEILING_K = 133.0

#: Room-temperature target (K @ 1 atm).
ROOM_T_K = 293.0


# --- H_001: flat-band two-lever design box ------------------------------------

def two_lever_box_check(
    g_mean: float,
    omega_meV: float,
    u_over_omega: float,
    g_min: float = 2.0,
    omega_min_meV: float = 130.0,
    u_over_omega_min: float = 1.5,
) -> dict:
    """Honest design box for a room-T geometric superconductor.

    Room-T flat-band SC needs THREE thresholds met simultaneously: large quantum
    geometry (g_mean), strong coupling phonon scale (omega_meV), and U/Omega. The
    Fubini-Study bound makes large g_mean and large omega_meV anti-correlated, so a
    real host typically clears one lever but not the other.
    Returns per-gate booleans and `in_box` (all gates pass).
    """
    gates = {
        "g": g_mean >= g_min,
        "omega": omega_meV >= omega_min_meV,
        "u_over_omega": u_over_omega >= u_over_omega_min,
    }
    return {"gates": gates, "in_box": all(gates.values())}


def geometric_bkt_tc_band(omega_meV: float, deflate: float = 2.8) -> float:
    """Order-of-magnitude 2D-BKT T_c (K) for a geometric flat band, calibrated by
    deflating the raw estimate by the measured anchor over-prediction factor
    (~2.8x geomean vs MATBG/tMoTe2/Re6Se8Cl2). Coupling scale enters via omega.
    """
    if omega_meV <= 0:
        raise ValueError(f"omega_meV must be > 0: {omega_meV}")
    # raw ~ (omega in K) * O(0.1); deflate to the calibrated band.
    omega_K = omega_meV * 11.604  # meV -> K
    return (0.11 * omega_K) / deflate


#: Hardest optical-phonon scale at ambient (H–H stretch order, meV) — the phonon
#: glue ceiling. Above this an effective coupling must come from a non-phonon
#: (electronic: exciton / plasmon / magnon, eV-scale) reservoir.
PHONON_CEILING_MEV = 200.0


def omega_for_bkt_tc(tc_K: float, deflate: float = 2.8) -> float:
    """Inverse of `geometric_bkt_tc_band`: the coupling scale Omega (meV) a geometric
    flat band needs to reach target T_c. Tells whether room-T is phonon-reachable."""
    if tc_K <= 0:
        raise ValueError(f"tc_K must be > 0: {tc_K}")
    return (tc_K * deflate) / (0.11 * 11.604)


#: Real 3D-vs-2D T_c lever, measured by src/fbgeom_3d.py (NOT a toy): BKT-vortex
#: removal f_BKT=1.50 x coordination boost f_z=sqrt(z3d/z2d)=1.22 -> L_3D=1.84.
#: A real but PARTIAL lever (~1.8x, not the ~5x room-T needs); native 3D flat bands
#: are gapless band-touchings (geometry contaminated), so it carries its own bill.
THREED_TC_LEVER = 1.84


def stacked_tc(omega_meV: float, three_d: bool = False) -> float:
    """Combination T_c (K): the calibrated geometric BKT band, optionally lifted by the
    real 3D lever. Stacking levers multiplies; this is the N-combination T_c."""
    base = geometric_bkt_tc_band(omega_meV)
    return base * (THREED_TC_LEVER if three_d else 1.0)


def omega_for_stacked_tc(tc_K: float, three_d: bool = False) -> float:
    """Coupling scale Omega (meV) a stacked combination needs to reach target T_c.
    Adding the 3D lever RELAXES the glue demand by THREED_TC_LEVER (the point of a
    3-lever stack vs a 2-lever one)."""
    eff_tc = tc_K / (THREED_TC_LEVER if three_d else 1.0)
    return omega_for_bkt_tc(eff_tc)


# --- H_002: Allen-Dynes T_c (ambient superhydride) ----------------------------

def allen_dynes_tc(omega_log_K: float, lam: float, mu_star: float = 0.10) -> float:
    """Allen-Dynes T_c (K). Returns 0.0 when the prefactor bracket is non-positive
    (sub-threshold lambda), which itself is a falsifier signal."""
    denom = lam - mu_star * (1.0 + 0.62 * lam)
    if denom <= 0:
        return 0.0
    return (omega_log_K / 1.2) * math.exp(-1.04 * (1.0 + lam) / denom)


# --- H_006: quantum-metric dimension scan (toy model, real computation) -------
# Tests whether the quantum-geometry lever (integrated trace of the Fubini-Study
# metric, the "g" lever of the two-lever wall) is capped at 2D or grows with
# dimension. This is a TOY tight-binding computation, not a real-material verdict:
# the metric is computed by finite difference on the BZ grid (no fitting).

def _trapz_metric_1d(n_k):
    """BZ-averaged quantum metric of a canonical 2-level 1D winding band.

    d(k) = (sin k, 0, cos k) is already unit, so n_hat = d. The 2-level FS metric
    is g_kk = (1/4) |d n_hat / dk|^2. Returns <g_kk> over the Brillouin zone.
    """
    import math
    total = 0.0
    dk = 2.0 * math.pi / n_k
    for i in range(n_k):
        k = -math.pi + i * dk
        # central finite difference of n_hat
        kp, km = k + dk, k - dk
        np_ = (math.sin(kp), 0.0, math.cos(kp))
        nm_ = (math.sin(km), 0.0, math.cos(km))
        dn = tuple((np_[j] - nm_[j]) / (2.0 * dk) for j in range(3))
        g_kk = 0.25 * sum(c * c for c in dn)
        total += g_kk
    return total / n_k


def quantum_metric_trace_separable(dim, n_k=400):
    """<tr g> for a separable d-dimensional flat-geometry model = dim independent
    winding directions, each contributing the 1D metric. Tests dimension-extensivity
    of the geometry lever (closed-form expectation: 0.25 * dim)."""
    if dim < 1:
        raise ValueError(f"dim must be >= 1: {dim}")
    return dim * _trapz_metric_1d(n_k)


def quantum_metric_trace_2d_dirac(m=1.0, n_k=60):
    """<tr g> for a NON-separable 2D two-band model d(kx,ky) =
    (sin kx, sin ky, m + cos kx + cos ky). Genuine 2D finite-difference metric
    (g_xx + g_yy), averaged over the BZ — a coupled-direction sanity check."""
    import math

    def nhat(kx, ky):
        d = (math.sin(kx), math.sin(ky), m + math.cos(kx) + math.cos(ky))
        norm = math.sqrt(sum(c * c for c in d))
        return tuple(c / norm for c in d)

    total = 0.0
    dk = 2.0 * math.pi / n_k
    h = 1e-4
    cells = 0
    for ix in range(n_k):
        kx = -math.pi + ix * dk
        for iy in range(n_k):
            ky = -math.pi + iy * dk
            nx1, nx0 = nhat(kx + h, ky), nhat(kx - h, ky)
            ny1, ny0 = nhat(kx, ky + h), nhat(kx, ky - h)
            dnx = tuple((nx1[j] - nx0[j]) / (2 * h) for j in range(3))
            dny = tuple((ny1[j] - ny0[j]) / (2 * h) for j in range(3))
            g_xx = 0.25 * sum(c * c for c in dnx)
            g_yy = 0.25 * sum(c * c for c in dny)
            total += g_xx + g_yy
            cells += 1
    return total / cells


# --- H_003: +@ bilayer division-of-labor (SPLIT the two levers) ---------------
# The two-lever wall (H_001) forbids one host from holding BOTH large geometry
# g AND stiff coupling Omega. The +@ bypass (brainstorm seed B2, meta-principle
# M1 SPLIT) puts geometry in layer A and glue in layer B, proximity-coupled.
# This is a TOY transfer model, not a real heterostructure verdict: the proximity
# weight eta and the electron-hybridization cost are explicit swept knobs.


def proximity_bilayer_levers(
    g_A: float,
    omega_A_meV: float,
    omega_B_meV: float,
    eta: float,
    electron_cost: float,
) -> dict:
    """Effective two-lever values of a +@ division-of-labor bilayer.

    Layer A = flat-band geometry host (large `g_A`, soft `omega_A_meV`).
    Layer B = stiff-glue host (large `omega_B_meV`, no flat-band geometry, g_B~0).
    `eta` in [0,1] = proximity transfer weight (interface transparency to the glue).
    `electron_cost` in [0,1] = how much generic electron hybridization the same
    interface forces (0 = ideal phonon-transparent / electron-opaque spacer,
    1 = generic interface where importing glue hybridizes electrons just as much).

    Importing stiff phonons raises the coupling A's flat band feels:
        omega_eff = omega_A + eta * (omega_B - omega_A)
    but hybridization dilutes the flat-band geometry:
        g_eff = g_A * (1 - electron_cost * eta)
    The product g_eff * omega_eff is the relocated two-lever budget.
    """
    for nm, v in (("eta", eta), ("electron_cost", electron_cost)):
        if not (0.0 <= v <= 1.0):
            raise ValueError(f"{nm} out of [0,1]: {v}")
    if g_A < 0 or omega_A_meV < 0 or omega_B_meV < 0:
        raise ValueError("levers must be >= 0")
    omega_eff = omega_A_meV + eta * (omega_B_meV - omega_A_meV)
    g_eff = g_A * (1.0 - electron_cost * eta)
    return {"g_eff": g_eff, "omega_eff": omega_eff, "eta": eta}


def critical_electron_cost(
    g_A: float,
    omega_A_meV: float,
    omega_B_meV: float,
    g_min: float = 2.0,
    omega_min_meV: float = 130.0,
    n_eta: int = 1001,
) -> dict:
    """Sweep eta in [0,1]; for each, find the LARGEST electron_cost that still keeps
    g_eff >= g_min while omega_eff >= omega_min_meV. The maximum over eta is the
    interface-quality budget the +@ bilayer demands: the box opens iff a real
    interface achieves electron_cost <= this threshold. Returns the threshold,
    the eta that realizes it, and whether the box opens even at the ideal
    interface (electron_cost = 0)."""
    if omega_B_meV <= omega_A_meV:
        raise ValueError("glue layer B must be stiffer than geometry layer A")
    best_ec = -1.0
    best_eta = None
    opens_ideal = False
    for i in range(n_eta):
        eta = i / (n_eta - 1)
        omega_eff = omega_A_meV + eta * (omega_B_meV - omega_A_meV)
        if omega_eff < omega_min_meV:
            continue
        # ideal interface (electron_cost=0) keeps g_eff = g_A
        if g_A >= g_min:
            opens_ideal = True
        # largest electron_cost with g_A*(1-ec*eta) >= g_min
        if eta == 0:
            ec = 1.0 if g_A >= g_min else -1.0
        else:
            ec = (1.0 - g_min / g_A) / eta
        ec = max(-1.0, min(1.0, ec))
        if ec > best_ec:
            best_ec, best_eta = ec, eta
    return {
        "critical_electron_cost": best_ec,
        "eta_at_critical": best_eta,
        "opens_at_ideal_interface": opens_ideal,
        "generic_interface_opens": best_ec >= 1.0,
    }


# --- H_009: connector spacer C as the third material (trilayer A/C/B) ---------
# H_003 left the interface as an abstract electron_cost knob. The 3rd material is the
# connector itself: a spacer C of thickness d (monolayers) whose job is to be
# electron-OPAQUE (block hybridization) yet phonon-TRANSPARENT (pass the glue). Both
# decay with thickness, at different rates set by C's electronic gap and phonon match.


def spacer_electron_cost(d_ml: float, lambda_e: float) -> float:
    """Electron-hybridization cost through a spacer of thickness d (monolayers).
    Tunneling decays as exp(-d/lambda_e); lambda_e is short for a wide-gap spacer.
    d=0 -> cost 1 (generic, no spacer); thick -> cost 0 (electron-opaque)."""
    if lambda_e <= 0 or d_ml < 0:
        raise ValueError("lambda_e > 0 and d_ml >= 0 required")
    return math.exp(-d_ml / lambda_e)


def spacer_phonon_transmission(d_ml: float, lambda_ph: float) -> float:
    """Phonon (glue) transmission through the spacer = exp(-d/lambda_ph); lambda_ph is
    long for a stiff, phonon-matched spacer. d=0 -> 1 (full transmission)."""
    if lambda_ph <= 0 or d_ml < 0:
        raise ValueError("lambda_ph > 0 and d_ml >= 0 required")
    return math.exp(-d_ml / lambda_ph)


def spacer_window(lambda_e: float, lambda_ph: float,
                  ec_max: float = 0.415, eta_min: float = 0.70,
                  n_d: int = 2001, d_max: float = 10.0) -> dict:
    """Does a connector thickness window exist where the spacer is BOTH electron-opaque
    (electron_cost <= ec_max, the H_003 critical) AND phonon-transparent (transmission
    >= eta_min, enough to import the glue)? Sweeps d in [0, d_max] monolayers. The window
    exists iff the spacer's electron decay is sufficiently faster than its phonon decay
    (lambda_e << lambda_ph), i.e. a wide-gap, phonon-matched material like hBN."""
    d_lo = None
    d_hi = None
    for i in range(n_d):
        d = d_max * i / (n_d - 1)
        ec = math.exp(-d / lambda_e)
        eta = math.exp(-d / lambda_ph)
        if ec <= ec_max and eta >= eta_min:
            if d_lo is None:
                d_lo = d
            d_hi = d
    return {
        "window_exists": d_lo is not None,
        "d_lo_ml": d_lo,
        "d_hi_ml": d_hi,
        "window_width_ml": (d_hi - d_lo) if d_lo is not None else 0.0,
    }


# --- H_011: does the electronic glue pass an electron-opaque spacer? ----------
# The crux (H_009 L2): the connector must block single-electron tunneling (preserve
# geometry) yet pass the electronic glue (reach room-T Omega). Resolution candidate:
# a bosonic/neutral collective glue (exciton/plasmon) couples via a LONG-RANGE Coulomb/
# dipole FIELD, not wavefunction overlap, so it penetrates an electron-tunneling barrier
# (cf. Forster transfer / Coulomb drag across an insulator).


def coulomb_glue_coupling(d_ml: float, lambda_coulomb: float) -> float:
    """Cross-spacer coupling of a NEUTRAL/collective bosonic glue (exciton/plasmon) via its
    Coulomb/dipole field: decays slowly (long lambda_coulomb) since the field is long-range,
    unlike single-electron tunneling. exp(-d/lambda_coulomb), d in monolayers."""
    if lambda_coulomb <= 0 or d_ml < 0:
        raise ValueError("lambda_coulomb > 0 and d_ml >= 0 required")
    return math.exp(-d_ml / lambda_coulomb)


def glue_through_spacer_window(lambda_e: float, lambda_glue: float,
                               glue_is_bosonic: bool,
                               ec_max: float = 0.415, glue_min: float = 0.70,
                               n_d: int = 2001, d_max: float = 10.0) -> dict:
    """Does a thickness window exist where the spacer is electron-opaque (electron_cost
    <= ec_max) AND still passes the glue (coupling >= glue_min)?
    A BOSONIC glue couples via the long-range field (lambda_glue = lambda_coulomb, long);
    a FERMIONIC glue (needs electron transfer) decays like the electron itself
    (lambda_glue = lambda_e) -> blocked exactly where the electron is blocked (no window)."""
    eff_lambda = lambda_glue if glue_is_bosonic else lambda_e
    d_lo = d_hi = None
    for i in range(n_d):
        d = d_max * i / (n_d - 1)
        ec = math.exp(-d / lambda_e)
        glue = math.exp(-d / eff_lambda)
        if ec <= ec_max and glue >= glue_min:
            if d_lo is None:
                d_lo = d
            d_hi = d
    return {
        "window_exists": d_lo is not None,
        "d_lo_ml": d_lo,
        "d_hi_ml": d_hi,
        "window_width_ml": (d_hi - d_lo) if d_lo is not None else 0.0,
    }


# --- falsifier harness (API-compatible with lumen tool/lumen_optics.py) -------

@dataclass
class Falsifier:
    """One pre-registered, measurable falsifier. `predicate(metrics) -> bool`
    returns True when the falsifier is TRIGGERED (hypothesis component refuted)."""

    name: str
    predicate: object  # callable(dict) -> bool
    desc: str = ""


def evaluate(metrics: dict, falsifiers: list) -> dict:
    """Run each falsifier against measured metrics. A falsifier PASSes when it is
    NOT triggered. Returns a JSON-safe verdict ledger (stdlib only)."""
    results = []
    for f in falsifiers:
        triggered = bool(f.predicate(metrics))
        results.append(
            {"name": f.name, "triggered": triggered, "status": "FAIL" if triggered else "PASS"}
        )
    n_pass = sum(1 for r in results if r["status"] == "PASS")
    return {
        "metrics": metrics,
        "falsifiers": results,
        "n_pass": n_pass,
        "n_total": len(results),
        "all_pass": n_pass == len(results),
    }
