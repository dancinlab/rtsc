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


# --- H_002: Allen-Dynes T_c (ambient superhydride) ----------------------------

def allen_dynes_tc(omega_log_K: float, lam: float, mu_star: float = 0.10) -> float:
    """Allen-Dynes T_c (K). Returns 0.0 when the prefactor bracket is non-positive
    (sub-threshold lambda), which itself is a falsifier signal."""
    denom = lam - mu_star * (1.0 + 0.62 * lam)
    if denom <= 0:
        return 0.0
    return (omega_log_K / 1.2) * math.exp(-1.04 * (1.0 + lam) / denom)


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
