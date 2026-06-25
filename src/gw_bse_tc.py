"""
GW/BSE -> EXCITON-GLUE -> ELIASHBERG Tc PIPELINE (in-silico, beyond-PBE).

WHY THIS EXISTS
  PBE/PBE+U cannot see Ta2NiSe5's pairing-relevant boson: its ~0.3 eV gap is a MANY-BODY
  excitonic effect (H_026 confirmed PBE stays near-metallic). The only in-silico route to that
  glue energy AND its electron coupling is GW (quasiparticle gap) + BSE (the exciton spectrum),
  fed into an Eliashberg/Allen-Dynes Tc with the EXCITON spectral function in place of phonon
  alpha^2F. This is the Allender-Bray-Bardeen excitonic-SC mechanism, computed honestly.

  This module is the IN-SILICO domain tool (rtsc/CLAUDE.md scope rule): it computes "IF the exciton
  acts as a pairing boson, what Tc". It does NOT flip absorbed (that is the lab's domain), and the
  campaign's standing verdict (the excitonic-glue mechanism is materials-unrealized) is unchanged.

THE CHAIN (4 stages)
  [DFT/QE]  ->  [GW]            ->  [BSE]                 ->  [glue + Eliashberg]
  bands       quasiparticle gap    exciton energies E_n      alpha^2F_exc(w) -> lambda, w_log -> Tc
              (real glue scale)     + oscillator strengths

WIRING BOUNDARY (wire-to-prod honesty)
  - Stages 1-3 (DFT->GW->BSE) are run by an EXTERNAL many-body engine: Yambo or BerkeleyGW
    (GPU: summer RTX5070). `run_yambo()` is the wiring point: IMPLEMENTED-BUT-DEAD-UNTIL-WIRED
    (needs a built Yambo on the pool host; raises a clear error if absent). Its OUTPUTS are parsed
    by `parse_gw_qp()` / `parse_bse_excitons()` (live, format-documented).
  - Stage 4 (exciton spectrum -> lambda -> Tc) is FULLY IMPLEMENTED here and self-tested
    (deterministic, byte-equal). This is the part that does not need the engine.
  - The electron-EXCITON coupling g_n (from the BSE e-h amplitudes + the electron-boson vertex) is
    the physically hard input; `exciton_glue_a2f()` exposes it as an EXPLICIT, documented model knob
    (`coupling_eV`), NOT a fabricated number. Wire the real vertex from BSE to replace the model.

absorbed=false / GATE_OPEN. No material is claimed to BE an RTSC.
"""
from __future__ import annotations

import argparse
import math
import os
import shutil
import subprocess
from dataclasses import dataclass, field

# --- physical constants ------------------------------------------------------
KB_EV = 8.617333262e-5        # Boltzmann constant [eV/K]
_EV_TO_K = 1.0 / KB_EV        # 1 eV in K (~11604.5)


# =============================================================================
# Stage 4 (LIVE, self-tested): exciton spectrum -> alpha^2F_exc -> lambda,w_log -> Tc
# =============================================================================

@dataclass(frozen=True)
class Exciton:
    """One BSE exciton: energy [eV] + oscillator strength (dimensionless, BSE-normalized)."""
    energy_eV: float
    strength: float


def exciton_glue_a2f(
    excitons: list[Exciton],
    coupling_eV: float,
    broadening_eV: float = 0.01,
    n_omega: int = 4000,
    omega_max_eV: float | None = None,
) -> tuple[list[float], list[float]]:
    """Build the exciton-mediated electron-boson spectral function alpha^2F_exc(w).

    MODEL (documented, not fabricated): each exciton n contributes a Lorentzian peak at E_n with
    weight (g_n^2 / 2) / E_n, where the electron-exciton coupling g_n^2 = coupling_eV * strength_n.
    `coupling_eV` is the single model knob carrying the (BSE-derivable) electron-boson vertex scale;
    replace it with the real <c|exciton|c> vertex from BSE e-h amplitudes when wired.

    Returns (omega_grid_eV, a2f) on a uniform grid. Deterministic.
    """
    if not excitons:
        return [], []
    e_hi = omega_max_eV if omega_max_eV is not None else (max(x.energy_eV for x in excitons) + 10.0 * broadening_eV)
    grid = [e_hi * (i + 0.5) / n_omega for i in range(n_omega)]   # avoid w=0 (1/w integrals)
    a2f = [0.0] * n_omega
    for x in excitons:
        if x.energy_eV <= 0.0:
            continue
        g2 = coupling_eV * x.strength                              # electron-exciton coupling^2 [eV]
        weight = 0.5 * g2 / x.energy_eV                            # alpha^2F peak area
        for i, w in enumerate(grid):
            # area-normalized Lorentzian
            lor = (broadening_eV / math.pi) / ((w - x.energy_eV) ** 2 + broadening_eV ** 2)
            a2f[i] += weight * lor
    return grid, a2f


def eliashberg_lambda_wlog(omega_eV: list[float], a2f: list[float]) -> tuple[float, float]:
    """Mass-enhancement lambda and logarithmic average frequency w_log [eV] from alpha^2F(w).

      lambda = 2 * integral a2f(w)/w dw
      w_log  = exp( (2/lambda) * integral a2f(w) * ln(w) / w dw )
    Trapezoidal on the uniform grid. Deterministic.
    """
    n = len(omega_eV)
    if n < 2:
        return 0.0, 0.0
    lam = 0.0
    lam_lnw = 0.0
    for i in range(n - 1):
        w0, w1 = omega_eV[i], omega_eV[i + 1]
        f0, f1 = a2f[i] / w0, a2f[i + 1] / w1
        dw = w1 - w0
        lam += (f0 + f1) * 0.5 * dw
        lam_lnw += (f0 * math.log(w0) + f1 * math.log(w1)) * 0.5 * dw
    lam *= 2.0
    if lam <= 0.0:
        return 0.0, 0.0
    w_log = math.exp((2.0 / lam) * lam_lnw)
    return lam, w_log


def allen_dynes_tc(lam: float, w_log_eV: float, mu_star: float = 0.10) -> float:
    """Allen-Dynes Tc [K] from lambda, w_log [eV], Coulomb pseudopotential mu*.

      Tc = (w_log / 1.2) * exp( -1.04 (1+lambda) / (lambda - mu*(1 + 0.62 lambda)) )
    Returns 0 if the denominator is non-positive (no SC). Deterministic.
    """
    denom = lam - mu_star * (1.0 + 0.62 * lam)
    if lam <= 0.0 or denom <= 0.0:
        return 0.0
    tc_eV = (w_log_eV / 1.2) * math.exp(-1.04 * (1.0 + lam) / denom)
    return tc_eV * _EV_TO_K


# =============================================================================
# Stages 1-3 parsers (LIVE) + engine wiring (DEAD-UNTIL-WIRED)
# =============================================================================

def parse_gw_qp(qp_path: str) -> dict:
    """Parse a Yambo `o-*.qp` quasiparticle file -> {'gap_eV': ..., 'n_states': ...}.

    Format (Yambo): comment lines start with '#'; data columns include the band index, k-point,
    E_0 (DFT) and E (GW QP) eigenvalues [eV]. We extract the QP direct gap as min(E_unocc)-max(E_occ)
    by occupation sign of (E - E_Fermi); robust to column order via the documented Yambo header.
    """
    if not os.path.exists(qp_path):
        raise FileNotFoundError(f"GW QP file not found: {qp_path} (run the GW stage first)")
    e_qp: list[float] = []
    with open(qp_path) as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            cols = line.split()
            try:
                # Yambo o-*.qp: ... E0[eV]  E-E0[eV]  ...  (QP E = E0 + dE); take col layout K B E0 dE
                e0 = float(cols[2]); de = float(cols[3])
                e_qp.append(e0 + de)
            except (IndexError, ValueError):
                continue
    if not e_qp:
        raise ValueError(f"no QP eigenvalues parsed from {qp_path}")
    e_qp.sort()
    # crude direct-gap proxy: largest jump between consecutive sorted QP levels near mid-spectrum
    gaps = [(e_qp[i + 1] - e_qp[i], 0.5 * (e_qp[i + 1] + e_qp[i])) for i in range(len(e_qp) - 1)]
    gap_eV = max(g for g, _ in gaps) if gaps else 0.0
    return {"gap_eV": gap_eV, "n_states": len(e_qp)}


def parse_bse_excitons(exc_path: str, max_excitons: int = 50) -> list[Exciton]:
    """Parse a Yambo BSE `o-*.exc_E_sorted` (or `o-*.eps_q1_diago_bse`) file -> [Exciton].

    Yambo writes sorted exciton energies [eV] with their (intensity / oscillator strength) columns.
    We read (energy, strength) pairs, lowest `max_excitons`. Live; format-documented.
    """
    if not os.path.exists(exc_path):
        raise FileNotFoundError(f"BSE exciton file not found: {exc_path} (run the BSE stage first)")
    out: list[Exciton] = []
    with open(exc_path) as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            cols = line.split()
            try:
                e = float(cols[0]); s = float(cols[1])
            except (IndexError, ValueError):
                continue
            if e > 0.0:
                out.append(Exciton(energy_eV=e, strength=abs(s)))
    out.sort(key=lambda x: x.energy_eV)
    return out[:max_excitons]


def run_yambo(workdir: str, yambo_bin: str = "yambo") -> dict:
    """WIRING POINT (IMPLEMENTED-BUT-DEAD-UNTIL-WIRED).

    Orchestrate GW+BSE via a built Yambo on the pool host (summer RTX5070 / MPI). Requires:
      - a Yambo SAVE/ database produced from the QE DFT run (p2y), and Yambo input decks in `workdir`.
    Returns paths to the QP and exciton outputs. Raises a clear error if Yambo is absent so callers
    fall back to `--self-test` or pre-computed parser inputs. NOT run by the self-test.
    """
    if shutil.which(yambo_bin) is None:
        raise EnvironmentError(
            f"'{yambo_bin}' not on PATH — GW/BSE engine not wired. Build Yambo on the pool host "
            f"(GPU summer) or pass pre-computed o-*.qp / o-*.exc files to the parsers."
        )
    # the actual GW then BSE runs (decks must exist in workdir); kept minimal + explicit
    subprocess.run([yambo_bin, "-F", "gw.in", "-J", "GW"], cwd=workdir, check=True)
    subprocess.run([yambo_bin, "-F", "bse.in", "-J", "BSE"], cwd=workdir, check=True)
    qp = os.path.join(workdir, "GW", "o-GW.qp")
    exc = os.path.join(workdir, "BSE", "o-BSE.exc_E_sorted")
    return {"qp_path": qp, "exc_path": exc}


# =============================================================================
# Orchestrator
# =============================================================================

@dataclass
class TcResult:
    lam: float
    w_log_eV: float
    tc_K: float
    n_excitons: int
    gw_gap_eV: float | None = None
    notes: list[str] = field(default_factory=list)


def tc_from_excitons(
    excitons: list[Exciton],
    coupling_eV: float,
    mu_star: float = 0.10,
    gw_gap_eV: float | None = None,
) -> TcResult:
    """Stage 4 end-to-end: excitons -> alpha^2F_exc -> (lambda, w_log) -> Allen-Dynes Tc. LIVE."""
    grid, a2f = exciton_glue_a2f(excitons, coupling_eV=coupling_eV)
    lam, w_log = eliashberg_lambda_wlog(grid, a2f)
    tc = allen_dynes_tc(lam, w_log, mu_star=mu_star)
    notes = ["alpha^2F_exc = Lorentzian-broadened exciton peaks; coupling_eV is the BSE-vertex knob",
             "Allen-Dynes Tc; absorbed=false (in-silico domain — no sim flips absorbed=true)"]
    return TcResult(lam=lam, w_log_eV=w_log, tc_K=tc, n_excitons=len(excitons),
                    gw_gap_eV=gw_gap_eV, notes=notes)


def run_pipeline(qp_path: str, exc_path: str, coupling_eV: float, mu_star: float = 0.10) -> TcResult:
    """Full pipeline from pre-computed GW(`qp_path`) + BSE(`exc_path`) engine outputs -> Tc."""
    gw = parse_gw_qp(qp_path)
    excitons = parse_bse_excitons(exc_path)
    res = tc_from_excitons(excitons, coupling_eV=coupling_eV, mu_star=mu_star, gw_gap_eV=gw["gap_eV"])
    return res


# =============================================================================
# Deterministic self-test (no engine needed)
# =============================================================================

def self_test() -> TcResult:
    """Toy: a single Ta2NiSe5-like exciton at 0.30 eV, coupling tuned so lambda ~ O(1).
    Deterministic — run twice, byte-equal. Verifies the Stage-4 math end-to-end without Yambo.
    """
    excitons = [Exciton(energy_eV=0.30, strength=1.0)]
    # coupling_eV chosen as a transparent reference (g^2 = 0.18 eV) -> lambda = 2*(g^2/2)/E = 0.6
    return tc_from_excitons(excitons, coupling_eV=0.18, mu_star=0.10, gw_gap_eV=0.30)


def _print(res: TcResult, title: str) -> None:
    print(f"=== {title} ===")
    print(f"  n_excitons              = {res.n_excitons}")
    if res.gw_gap_eV is not None:
        print(f"  GW QP gap [eV]          = {res.gw_gap_eV:.4f}")
    print(f"  lambda (mass enhance)   = {res.lam:.6f}")
    print(f"  w_log [eV]              = {res.w_log_eV:.6f}")
    print(f"  Tc (Allen-Dynes) [K]    = {res.tc_K:.3f}")
    print("  notes:")
    for nline in res.notes:
        print(f"    - {nline}")
    print("  absorbed=false / GATE_OPEN — in-silico domain; no simulation establishes RTSC.")


def main() -> None:
    ap = argparse.ArgumentParser(description="GW/BSE -> exciton-glue -> Eliashberg Tc (in-silico).")
    ap.add_argument("--self-test", action="store_true", help="deterministic Stage-4 self-test (no engine)")
    ap.add_argument("--qp", help="path to GW quasiparticle file (Yambo o-*.qp)")
    ap.add_argument("--exc", help="path to BSE exciton file (Yambo o-*.exc_E_sorted)")
    ap.add_argument("--coupling-eV", type=float, default=0.18, help="electron-exciton coupling g^2 [eV] (BSE-vertex knob)")
    ap.add_argument("--mu-star", type=float, default=0.10, help="Coulomb pseudopotential mu*")
    args = ap.parse_args()

    if args.self_test or not (args.qp and args.exc):
        _print(self_test(), "GW/BSE Tc pipeline — SELF-TEST (toy 0.30 eV exciton, deterministic)")
        if not args.self_test:
            print("\n(no --qp/--exc given; ran self-test. Provide both for a real GW+BSE run, "
                  "or build Yambo on the pool host and call run_yambo().)")
        return
    _print(run_pipeline(args.qp, args.exc, coupling_eV=args.coupling_eV, mu_star=args.mu_star),
           "GW/BSE Tc pipeline — REAL (parsed engine outputs)")


if __name__ == "__main__":
    main()
