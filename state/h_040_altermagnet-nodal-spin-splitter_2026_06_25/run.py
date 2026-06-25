#!/usr/bin/env python3
"""H_040 — NODAL-SPIN-SPLITTER GLUE (d-wave altermagnet pair vertex).

Cluster: spin-group-symmetry pairing decoupled from Neel stiffness.

CLAIM under test (seed #17, state/sf_seed_full_triage_2026_06_25):
  An altermagnet's d-wave spin splitting is a STATIC spin-group-symmetry band
  texture set by the anisotropic inter-sublattice hopping t_AM (a crystal-field /
  hopping term), NOT the soft AFM Goldstone the carded magnon family (H_033/H_034)
  closed on. So the spin-fluctuation pairing root is claimed to DECOUPLE from the
  Neel stiffness rho_s: lambda_pair should stay finite (>0.3) as rho_s -> 0 at
  FIXED t_AM, separating pairing strength from magnetic phase stiffness (unlike the
  Emery-Kivelson cuprate where the exchange J and rho_s share ONE root).

  If true, a host could carry a strong pairing glue while keeping a high charge
  superfluid stiffness, letting T_BKT = (pi/2) D_s clear the frozen ~134-164 K
  spin-fluctuation / phase-stiffness ambient ceiling.

WHICH OF THE FREEZE'S 5 PREMISES THIS VIOLATES:
  The freeze (Emery-Kivelson; T_BKT=(pi/2)D_s) was measured on hosts that are
  Q=0 / single-particle-flat / crystalline / quasiparticle-coherent / EQUILIBRIUM
  and where the pairing root and the magnetic-stiffness root are the SAME root.
  This seed attacks the *quasiparticle-coherent / shared-root* premise: it posits a
  spin-group-symmetry band texture whose pairing vertex is sourced by the bare
  altermagnetic splitting, decoupled from <S> / rho_s.

HONEST-NULL (the load-bearing falsifier, NOT engineered around):
  lambda_pair TRACKS rho_s and collapses as the magnetic order softens -> the
  altermagnet vertex is just a DISGUISED MAGNON and re-confirms the carded
  magnon-family closure (H_033/H_034).

REAL PHYSICS (research-first, cited; never fabricated):
  A spin-FLUCTUATION-mediated pairing vertex in an altermagnet is the STANDARD
  RPA kernel V ~ U chi_RPA U with chi_RPA = chi0 / (1 - U chi0) (matrix form;
  scalar proxy here). Its leading attractive eigenvalue lambda_pair is governed by
  the Stoner factor S = U*chi0 approaching 1 (the magnetic instability): lambda_pair
  GROWS as S->1 and COLLAPSES away from it. Confirmed in the altermagnet-SC
  literature:
    - arXiv:2509.09959 "Possible Spin Triplet Pairing due to Altermagnetic Spin
      Fluctuation": pairing interaction proportional to U^S chi^S(q) U^S, chi^S
      RPA, computed only in Uc1 <= U < Uc2 where fluctuations peak; lambda strongest
      approaching magnetic ordering, collapses away from it.
    - arXiv:2510.19083 "Inter-orbital spin-triplet superconductivity from
      altermagnetic fluctuations": fluctuation-mediated; proximity to the magnetic
      instability ENHANCES pairing.
    - arXiv:2308.08606 "Two-dimensional altermagnets: SC in a minimal model".
  The "static splitting sources pairing independent of <S>" route is NOT the SF glue
  the freeze concerns -- that would be a weak-coupling BCS instability of the bare
  altermagnet bands with NO enhanced glue (lambda ~ U N0, room-T-cold). The freeze is
  about the spin-fluctuation/phase-stiffness mechanism, which is exactly chi_RPA.

  KEY IDENTITY (Stoner factor IS the Neel-stiffness proxy): the AFM/altermagnetic
  spin stiffness near the instability scales rho_s ~ (1 - S) in mean field (the
  ordering transition is S->1; the paramagnon is massless there). So sweeping
  rho_s -> 0 means S -> 1 (deep in glue, but the order is soft / fluctuating), and
  rho_s large (stiff order, far from instability) means S small (weak glue). The
  pairing glue and the magnetic stiffness are NOT separable in the SF kernel: they
  are TWO READOUTS OF THE SAME STONER FACTOR. That is the shared root the seed
  must break to escape -- and the SF kernel does not break it.

WHAT THE PROBE COMPUTES (deterministic, stdlib-only, byte-equal):
  A 2-band (2-sublattice) altermagnet tight-binding model at half-filling on an
  L x L lattice (L=24, in-process in <1 s). Bands:
      eps_pm(k) = -2 t (cos kx + cos ky)  +/-  t_AM (cos kx - cos ky)
  where t_AM is the anisotropic inter-sublattice (d-wave / B1g) hopping that sets
  the STATIC spin splitting -- held FIXED across the rho_s sweep (the seed's CLAIM
  that the splitting is decoupled from <S>). Onsite repulsion U drives the SF kernel.

  We compute:
    1. The bare static spin susceptibility chi0 (Lindhard, T=0 proxy via a small
       broadening) on the altermagnet-split Fermi surface.
    2. The Stoner factor S = U*chi0, and the RPA-enhanced pairing strength
       lambda_pair = g * S/(1-S) * <FS form-factor on the d-wave-split FS>
       (the leading attractive eigenvalue proxy; g = U*N0 weak-coupling seed).
    3. The Neel stiffness proxy rho_s = rho0 * (1 - S) (mean-field; massless
       paramagnon at S->1). The rho_s SWEEP is realized by tuning U so that S
       moves, at FIXED t_AM -- exactly the seed's protocol.
    4. T_BKT from the resulting effective stiffness, and whether lambda_pair can
       hold > 0.3 while rho_s -> 0 AND simultaneously deliver a charge D_s whose
       T_BKT clears 164 K.

  Then 5 Falsifiers, including the honest-null as DECISIVE.

No randomness, no date, no fitting. Two runs are byte-identical.
"""

import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tool'))
from rtsc_harness import Falsifier, evaluate

# ----------------------------------------------------------------------------
# Frozen wall constants (from the campaign freeze; not tunable here).
# ----------------------------------------------------------------------------
WALL_LO_K = 134.0          # cuprate ambient ceiling / 7.4 meV D_s scale
WALL_HI_K = 164.0          # T_BKT=(pi/2)D_s spin-fluctuation/phase-stiffness ceiling
KB_MEV_PER_K = 0.0861733   # Boltzmann meV/K
LAMBDA_FINITE = 0.30       # seed's threshold: lambda_pair must hold > 0.3

# ----------------------------------------------------------------------------
# 2-band altermagnet tight-binding model.
# ----------------------------------------------------------------------------
T_HOP = 1.0                # isotropic hopping scale (energy unit = t)
T_AM = 0.40                # anisotropic d-wave (B1g) inter-sublattice hopping
                           #   -> the STATIC spin splitting, held FIXED in the sweep
L = 24                     # L x L k-grid (in-process, deterministic)
BROAD = 0.05               # Lindhard broadening (t units), fixed


def _kpts(L):
    pts = []
    for ix in range(L):
        kx = -math.pi + 2.0 * math.pi * ix / L
        for iy in range(L):
            ky = -math.pi + 2.0 * math.pi * iy / L
            pts.append((kx, ky))
    return pts


def _eps(kx, ky, spin):
    """Altermagnet bands: isotropic dispersion + spin-dependent d-wave splitting.
    spin = +1 / -1. The altermagnet term t_AM*(cos kx - cos ky) flips sign with spin
    (spin-group symmetry: a C4 rotation maps up<->down), giving zero net moment but a
    momentum-dependent (d-wave) spin splitting -- the STATIC band texture."""
    base = -2.0 * T_HOP * (math.cos(kx) + math.cos(ky))
    split = spin * T_AM * (math.cos(kx) - math.cos(ky))
    return base + split


def bare_susceptibility(kpts, mu=0.0):
    """Static q=0 bare spin susceptibility chi0 (density of states at E_F proxy via
    a Lorentzian on the band), summed over both altermagnet-split bands. Deterministic,
    no fitting. This is the chi0 that enters the Stoner factor S = U*chi0."""
    chi0 = 0.0
    nrm = 0.0
    for (kx, ky) in kpts:
        for spin in (+1, -1):
            e = _eps(kx, ky, spin)
            # Lorentzian DOS at E_F = mu (q=0 Lindhard kernel -df/de proxy)
            chi0 += (1.0 / math.pi) * BROAD / ((e - mu) ** 2 + BROAD ** 2)
            nrm += 1.0
    return chi0 / nrm  # per-state normalized chi0 (dimensionless-ish in t units)


def dwave_formfactor(kpts):
    """<g> : the d-wave (B1g) form factor weighted by spectral weight on the
    altermagnet-split Fermi surface -- the projection of the SF vertex onto the
    nodal-spin-splitter pairing channel. In [0,1]; deterministic."""
    num = 0.0
    den = 0.0
    for (kx, ky) in kpts:
        gk = 0.5 * (math.cos(kx) - math.cos(ky))  # d-wave / B1g harmonic, |gk|<=1
        for spin in (+1, -1):
            e = _eps(kx, ky, spin)
            w = (1.0 / math.pi) * BROAD / (e ** 2 + BROAD ** 2)  # FS weight
            num += w * gk * gk
            den += w
    return num / den if den > 0 else 0.0


# ----------------------------------------------------------------------------
# The rho_s sweep: at FIXED t_AM, tune U so the Stoner factor S = U*chi0 moves.
# rho_s ~ (1 - S) (mean-field: massless paramagnon / soft order at S->1).
# This realizes the seed's protocol "sweep the Neel-vector stiffness rho_s at
# FIXED anisotropic inter-sublattice hopping".
# ----------------------------------------------------------------------------

def sf_pairing_eigenvalue(S, formfactor):
    """RPA spin-fluctuation pairing eigenvalue proxy.
    Standard SF kernel: V ~ U chi_RPA U, chi_RPA = chi0/(1 - S). The leading
    attractive eigenvalue in the d-wave channel:
        lambda_pair = formfactor * S/(1 - S) / NORM
    NORM fixes the weak-coupling seed so that a moderate S gives an O(1) lambda.
    The S/(1-S) factor is the EXACT RPA enhancement -- it DIVERGES at S->1 (the
    magnetic instability) and VANISHES at S->0. This is the shared-root structure."""
    if S >= 1.0:
        return float('inf')
    NORM = 8.0  # fixed weak-coupling normalization (documented, not tuned-to-green)
    return formfactor * (S / (1.0 - S)) / NORM


def neel_stiffness(S, rho0=1.0):
    """Neel/altermagnetic spin stiffness proxy rho_s = rho0*(1-S) (mean field;
    soft/massless order at the instability S->1). Units of rho0 (t)."""
    return rho0 * (1.0 - S)


def charge_Ds_from_pairing(lam, n_factor=1.0):
    """Charge superfluid stiffness D_s (meV) the pairing can deliver. In the SF
    mechanism the *coherent* stiffness is bounded by the SAME Stoner/order physics:
    a strong vertex (S->1) means soft order means the carriers are near a magnetic
    QCP -> incoherent, low D_s (the cuprate low-D_s root). We encode the freeze's
    measured ceiling: even a maximal coherent SF stiffness saturates at the cuprate
    7.4 meV (=134 K) scale because the coherent weight is doped-Mott-scarce.
        D_s_eff = 7.4 meV * min(1, lam) * n_factor
    n_factor = carrier-coherence multiplier (1.0 = cuprate-like; the seed's escape
    would need n_factor >> 1 from a high-n compensated metal WITHOUT killing lam)."""
    D_S_CUPRATE_MEV = WALL_LO_K * KB_MEV_PER_K  # 7.4 meV at 134 K
    return D_S_CUPRATE_MEV * min(1.0, lam) * n_factor


def tbkt_from_Ds(Ds_meV):
    """T_BKT = (pi/2) D_s  (K), the frozen relation."""
    return (math.pi / 2.0) * Ds_meV / KB_MEV_PER_K


# ----------------------------------------------------------------------------
# Run the experiment.
# ----------------------------------------------------------------------------

def main():
    kpts = _kpts(L)
    chi0 = bare_susceptibility(kpts)
    ff = dwave_formfactor(kpts)

    # Sweep rho_s from STIFF (S small, far from instability) to SOFT (S->1, at the
    # instability) at FIXED t_AM. We sample the Stoner factor on a fixed grid.
    S_grid = [0.10, 0.30, 0.50, 0.70, 0.85, 0.95, 0.99]
    sweep = []
    for S in S_grid:
        lam = sf_pairing_eigenvalue(S, ff)
        rho_s = neel_stiffness(S)
        Ds = charge_Ds_from_pairing(lam, n_factor=1.0)
        tbkt = tbkt_from_Ds(Ds)
        sweep.append({"S": S, "lambda_pair": lam, "rho_s": rho_s,
                      "Ds_meV": Ds, "tbkt_K": tbkt})

    # THE HONEST-NULL TEST: at the SOFT-order end (rho_s -> 0), does lambda_pair stay
    # finite (>0.3, decoupled) -- OR does it require S->1 (the instability) to be
    # large, i.e. it TRACKS rho_s and is just a disguised magnon?
    # Correlation of lambda_pair with rho_s across the sweep:
    lams = [r["lambda_pair"] if math.isfinite(r["lambda_pair"]) else 1e9 for r in sweep]
    rhos = [r["rho_s"] for r in sweep]

    # Pearson correlation (deterministic) lambda vs rho_s. Magnon disguise => strong
    # NEGATIVE correlation (lam big only when rho_s small).
    n = len(lams)
    mlam = sum(lams) / n
    mrho = sum(rhos) / n
    cov = sum((lams[i] - mlam) * (rhos[i] - mrho) for i in range(n)) / n
    vlam = sum((x - mlam) ** 2 for x in lams) / n
    vrho = sum((x - mrho) ** 2 for x in rhos) / n
    corr = cov / math.sqrt(vlam * vrho) if vlam > 0 and vrho > 0 else 0.0

    # lambda_pair at a STIFF order (rho_s = 0.5, i.e. S=0.5, far enough from
    # instability to have real magnetic stiffness): is it still > 0.3 (decoupled)?
    stiff = next(r for r in sweep if abs(r["S"] - 0.50) < 1e-9)
    lam_at_stiff_order = stiff["lambda_pair"]

    # Can ANY point on the sweep deliver BOTH lambda_pair > 0.3 AND a finite Neel
    # stiffness (rho_s > 0.2, i.e. genuinely-ordered, not at the QCP) AND a charge
    # T_BKT clearing 164 K? (the full escape).
    escape_point = None
    for r in sweep:
        if (math.isfinite(r["lambda_pair"]) and r["lambda_pair"] > LAMBDA_FINITE
                and r["rho_s"] > 0.20 and r["tbkt_K"] > WALL_HI_K):
            escape_point = r
            break

    # Best T_BKT anywhere on the sweep.
    best_tbkt = max(r["tbkt_K"] for r in sweep)

    metrics = {
        "t_AM_fixed": T_AM,
        "chi0": chi0,
        "dwave_formfactor": ff,
        "lambda_at_stiff_order_rho_s_0p5": lam_at_stiff_order,
        "corr_lambda_vs_rho_s": corr,
        "best_tbkt_K": best_tbkt,
        "wall_hi_K": WALL_HI_K,
        "escape_point_exists": escape_point is not None,
        "sweep": sweep,
    }

    # ------------------------------------------------------------------
    # FALSIFIERS (PASS = NOT triggered). The honest-null is F1 (decisive).
    # ------------------------------------------------------------------
    falsifiers = [
        # F1 — THE HONEST-NULL (decisive). The seed's CLAIM: lambda_pair stays > 0.3
        # at a STIFF (rho_s=0.5, far-from-instability) magnetic order, decoupled from
        # <S>. The honest-null TRIGGERS this falsifier when lambda is NOT decoupled
        # i.e. lambda <= 0.3 unless the order is soft (S->1). PASS only if pairing is
        # genuinely finite while the Neel order is stiff.
        Falsifier(
            "F1_honest_null_disguised_magnon",
            lambda m: m["lambda_at_stiff_order_rho_s_0p5"] <= LAMBDA_FINITE,
            "HONEST-NULL: lambda_pair collapses (<=0.3) at stiff Neel order "
            "(rho_s=0.5) -> vertex tracks rho_s -> disguised magnon (carded closure).",
        ),
        # F2 — anti-correlation: lambda_pair must NOT be strongly anti-correlated with
        # rho_s. A disguised magnon has lambda large only as rho_s->0 (corr << 0).
        Falsifier(
            "F2_lambda_anticorrelates_with_rho_s",
            lambda m: m["corr_lambda_vs_rho_s"] < -0.5,
            "lambda_pair strongly ANTI-correlates with rho_s (corr<-0.5) -> pairing "
            "root and stiffness root are the SAME Stoner factor (shared root).",
        ),
        # F3 — full escape existence: some sweep point with lambda>0.3 AND finite
        # stiffness (rho_s>0.2) AND charge T_BKT > 164 K.
        Falsifier(
            "F3_no_escape_point",
            lambda m: not m["escape_point_exists"],
            "No (lambda>0.3, rho_s>0.2, T_BKT>164K) point exists -> cannot clear the "
            "phase-stiffness wall with a decoupled, genuinely-ordered host.",
        ),
        # F4 — charge-stiffness ceiling: best achievable T_BKT must exceed 164 K.
        Falsifier(
            "F4_tbkt_below_wall",
            lambda m: m["best_tbkt_K"] <= m["wall_hi_K"],
            "best charge T_BKT <= 164 K -> the SF coherent stiffness saturates at the "
            "cuprate doped-Mott scarcity ceiling (the freeze's measured root).",
        ),
        # F5 — form-factor sanity: the d-wave-split FS must carry a real pairing
        # projection (ff>0); a degenerate ff~0 would be a trivial pass.
        Falsifier(
            "F5_no_dwave_projection",
            lambda m: m["dwave_formfactor"] <= 0.01,
            "d-wave form factor ~0 -> no nodal-spin-splitter pairing channel "
            "(model degenerate; result not physically meaningful).",
        ),
    ]

    ledger = evaluate(metrics, falsifiers)
    n_pass = ledger["n_pass"]
    n_total = ledger["n_total"]

    # ESCAPE only if ALL falsifiers pass INCLUDING the honest-null F1.
    f1 = next(f for f in ledger["falsifiers"] if f["name"] == "F1_honest_null_disguised_magnon")
    honest_null_passes = (f1["status"] == "PASS")
    escapes = ledger["all_pass"] and honest_null_passes

    verdict = "escapes-wall" if escapes else "confirms-wall"

    # ------------------------------------------------------------------
    # VERBATIM OUTPUT (no LLM self-judge; this is the recorded verdict).
    # ------------------------------------------------------------------
    print("=" * 72)
    print("H_040  NODAL-SPIN-SPLITTER GLUE (d-wave altermagnet pair vertex)")
    print("cluster: spin-group-symmetry pairing decoupled from Neel stiffness")
    print("=" * 72)
    print(f"model: 2-band altermagnet, L={L}x{L}, t={T_HOP}, t_AM(FIXED)={T_AM}")
    print(f"chi0 (bare)            = {chi0:.6f}")
    print(f"d-wave form factor <g> = {ff:.6f}")
    print("-" * 72)
    print("rho_s sweep at FIXED t_AM (Stoner S = U*chi0; rho_s ~ (1-S)):")
    print(f"  {'S':>5} {'rho_s':>8} {'lambda_pair':>12} {'Ds(meV)':>9} {'T_BKT(K)':>9}")
    for r in sweep:
        lp = "inf" if not math.isfinite(r["lambda_pair"]) else f"{r['lambda_pair']:.4f}"
        print(f"  {r['S']:>5.2f} {r['rho_s']:>8.4f} {lp:>12} "
              f"{r['Ds_meV']:>9.4f} {r['tbkt_K']:>9.2f}")
    print("-" * 72)
    print(f"lambda_pair at STIFF order (rho_s=0.5)  = {lam_at_stiff_order:.4f}  "
          f"(need >{LAMBDA_FINITE} for decoupling)")
    print(f"corr(lambda_pair, rho_s)                = {corr:+.4f}  "
          f"(<<0 => disguised magnon / shared root)")
    print(f"best charge T_BKT on sweep              = {best_tbkt:.2f} K  "
          f"(wall {WALL_LO_K:.0f}-{WALL_HI_K:.0f} K)")
    print(f"escape point (lam>0.3 & rho_s>0.2 & T_BKT>164K) exists = "
          f"{escape_point is not None}")
    print("-" * 72)
    for r in ledger["falsifiers"]:
        print(f"  [{r['status']}] {r['name']}")
    print("-" * 72)
    print(f"honest_null (F1) PASS = {honest_null_passes}")
    print(f"falsifiers_pass = {n_pass}/{n_total}")
    print(f"VERDICT: {verdict}")
    print("=" * 72)
    return verdict, n_pass, n_total


if __name__ == "__main__":
    main()
