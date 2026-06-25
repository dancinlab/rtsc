#!/usr/bin/env python3
"""H_058 — PDW Commensurate Lock: pair-density-wave pinned to the lattice.

Within-cluster variant of the finite-Q / "order-traps" escape family (sibling of
H_042 FFLO, H_043 vortex-code). The seed's escape mechanism:

  A commensurate (Q = G/n) pair-density wave Delta(r) ~ Delta_0 cos(Q.r) has a
  sliding Goldstone (the PDW phason). A lattice-commensurate Umklapp term
  V_p * cos(n*theta) PINS that phason, opening a phase gap

       Delta_phason ~ sqrt(V_p * rho_s).

  A free vortex / phase slip then costs Delta_phason instead of (pi/2)*D_s.
  If Delta_phason (in Kelvin) > 164 K while the pairing eigenvalue is UNCHANGED,
  the soft phase channel is gapped out and BKT melting no longer caps T_c.
  T_melt ~ max[ (pi/2)*D_s , Delta_phason ].

DECISIVE HONEST-NULL (confirm-wall, load-bearing — NOT engineered around):
  The same commensurate Umklapp that pins the phase is, microscopically, an
  n-th-order process in the small ratio (Delta_0 / W) (Lee-Rice-Anderson /
  McMillan-Nakanishi-Shiba commensurability energy). It both
    (N1) makes V_p exponentially small in n  ->  Delta_phason capped near the
         dilute Q=0 superfluid weight (the frozen ceiling), AND
    (N2) mixes the +Q and -Q pairing components -> suppresses the finite-Q
         pairing eigenvalue lambda_pair as V_p rises.
  Pinning gap and pairing scale cannot both be large: no free lunch. The family
  closes at the same ~134-164 K wall.

References (grounding, not fabricated; ids verified via web search 2026-06-25):
  - Lee, Rice & Anderson, "Conductivity from charge or spin density waves",
    Solid State Commun. 14, 703 (1974)  [amplitudon/phason spectrum].
  - McMillan, "Landau theory of charge-density waves", Phys. Rev. B 12, 1187
    (1975); Nakanishi-Shiba framework  [higher-order umklapp commensurability
    energy ~ cos(n*theta), V_p high-order in (Delta/W)].
  - Lock-in / commensurability energy proportional to cos(M*phi), gliding the
    density wave costs finite energy -> finite phason gap (commensurate pinning):
    arXiv:1706.07231 (reinterpretation of McMillan's lock-in theory),
    arXiv:2409.02236 (umklapp-driven CDW transition).
  - Sibling finite-Q cards: H_042 (FFLO, arXiv:1003.2194 / 1102.4903),
    H_043 (vortex-code phase-lock).

Deterministic, stdlib-only (math). No Date, no RNG. Byte-reproducible.
PASS = falsifier NOT triggered (rtsc_harness convention).
"""

import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tool"))
from rtsc_harness import Falsifier, evaluate, ROOM_T_K

# ---------------------------------------------------------------------------
# Physical constants / host (all explicit; no fitting).
# ---------------------------------------------------------------------------
KB_MEV_PER_K = 0.0861733          # k_B in meV/K
ROOM_K = ROOM_T_K                 # 293.0 K target
CEILING_TOP_K = 164.0             # charitable TOP of the frozen 134-164 K band
CEILING_BOT_K = 134.0

# Clean tight-binding host, IDENTICAL charity convention as H_042:
#   e(k) = -2t(cos kx + cos ky), bandwidth W = 8t.
T_HOP_EV = 0.300                  # 0.3 eV hop
W_EV = 8.0 * T_HOP_EV            # 2.4 eV bandwidth
W_MEV = W_EV * 1000.0           # 2400 meV
DELTA0_MEV = 20.0                # finite-Q PDW amplitude (same as H_042 Delta0)

# Dilute Q=0 geometric superfluid weight of the host, expressed as a rigidity in
# Kelvin. CHARITY: anchor (pi/2)*D_s^{Q=0} to the TOP of the frozen band (164 K),
# the most favorable choice for the escape (the real flat-band D_s is 1-8 K).
RIGIDITY_Q0_K = CEILING_TOP_K              # (pi/2) D_s^{Q=0}, charitable anchor
RHO_S_MEV = RIGIDITY_Q0_K * KB_MEV_PER_K   # rho_s as an energy scale (meV)


# ---------------------------------------------------------------------------
# Commensurability (Umklapp) pinning energy.
# ---------------------------------------------------------------------------
# A commensurate PDW with Q = G/n locks via an n-th-order Umklapp. The
# Lee-Rice-Anderson / McMillan-Nakanishi-Shiba commensurability free-energy term
# is  -V_p cos(n*theta)  with the coefficient HIGH-ORDER in the small gap ratio:
#
#     V_p(n) ~ W * (Delta0 / W)^n .
#
# This is the standard result that the lock-in/commensurability energy is a
# high-order process: every extra factor of the order parameter needed to span
# n lattice periods costs another power of (Delta0/W) << 1. n=1 is the trivial
# Q=0 limit (no modulation), so the smallest non-trivial commensurate modulation
# is n=2 and physical PDWs sit at n = 2,3,4,...
def vp_commensurability_meV(n):
    """McMillan/LRA commensurability (Umklapp pinning) energy V_p(n) in meV."""
    if n < 2:
        raise ValueError("commensurate modulation needs n>=2 (n=1 is Q=0)")
    ratio = DELTA0_MEV / W_MEV                      # (Delta0/W) << 1
    return W_MEV * (ratio ** n)


def phason_gap_K(n):
    """Pinned PDW phason gap Delta_phason ~ sqrt(V_p * rho_s), returned in Kelvin.

    V_p and rho_s are both energies (meV); sqrt(V_p*rho_s) is an energy -> /k_B.
    """
    vp = vp_commensurability_meV(n)                 # meV
    gap_meV = math.sqrt(vp * RHO_S_MEV)             # meV
    return gap_meV / KB_MEV_PER_K                    # K


# ---------------------------------------------------------------------------
# Finite-Q pairing eigenvalue suppression by the SAME Umklapp.
# ---------------------------------------------------------------------------
# The commensurate Umklapp that pins the phase also couples the +Q and -Q PDW
# components (it is exactly the cos(n*theta) phase-locking term acting on the
# pair field). For small n (where V_p is largest, i.e. the only way to make the
# phason gap big) the +Q/-Q mixing is STRONG -> it is pair-breaking for the
# finite-Q channel. We encode the depairing as the relative reduction of the
# finite-Q pairing eigenvalue:
#
#     lambda_pair(n) / lambda0 = 1 - mixing(n),  mixing(n) = (Delta0/W)^(n-1).
#
# n=2 (strongest pinning) gives the LARGEST mixing (most pair-breaking);
# large n gives negligible mixing but then V_p -> 0 (no pinning). This is the
# explicit no-free-lunch trade: V_p(n) and pairing-survival pull oppositely in n.
LAMBDA0 = 1.0                                       # unperturbed finite-Q eigenvalue


def lambda_pair(n):
    ratio = DELTA0_MEV / W_MEV
    mixing = ratio ** (n - 1)
    return LAMBDA0 * (1.0 - mixing)


def t_melt_K(n):
    """T_melt ~ max[(pi/2)D_s , Delta_phason], but the pinning channel only
    counts if the finite-Q pairing still EXISTS (lambda_pair>0). We gate the
    phason contribution by the surviving pairing fraction (no condensate -> no
    phason to pin)."""
    survive = max(0.0, lambda_pair(n) / LAMBDA0)
    return max(RIGIDITY_Q0_K, phason_gap_K(n) * survive)


# ---------------------------------------------------------------------------
# Sweep over commensurability order n and report.
# ---------------------------------------------------------------------------
N_VALUES = [2, 3, 4, 5, 6]

rows = []
for n in N_VALUES:
    rows.append({
        "n": n,
        "Vp_meV": vp_commensurability_meV(n),
        "phason_gap_K": phason_gap_K(n),
        "lambda_ratio": lambda_pair(n) / LAMBDA0,
        "t_melt_K": t_melt_K(n),
    })

best_gap = max(r["phason_gap_K"] for r in rows)
best_gap_n = max(rows, key=lambda r: r["phason_gap_K"])["n"]
best_tmelt = max(r["t_melt_K"] for r in rows)
# Joint escape: need SOME n where BOTH the phason gap clears 164 K AND the
# finite-Q pairing is essentially unchanged (lambda_ratio >= 0.95).
joint_escape = any(
    (r["phason_gap_K"] > CEILING_TOP_K) and (r["lambda_ratio"] >= 0.95)
    for r in rows
)
# Most-charitable n=2 numbers (strongest possible pinning).
n2 = rows[0]

metrics = {
    "best_phason_gap_K": best_gap,
    "best_phason_gap_n": best_gap_n,
    "best_t_melt_K": best_tmelt,
    "n2_phason_gap_K": n2["phason_gap_K"],
    "n2_lambda_ratio": n2["lambda_ratio"],
    "ceiling_top_K": CEILING_TOP_K,
    "room_K": ROOM_K,
    "joint_escape": joint_escape,
    "rho_s_meV": RHO_S_MEV,
    "W_meV": W_MEV,
    "Delta0_meV": DELTA0_MEV,
}

# ---------------------------------------------------------------------------
# Falsifiers (PASS = NOT triggered). F1 & F2 are the DECISIVE honest-nulls.
# ---------------------------------------------------------------------------
# Convention (matches H_042 / rtsc_harness): predicate(m) -> True means the
# falsifier is TRIGGERED (FAIL) = the escape-refuting / null-confirming condition
# HOLDS. PASS (not triggered) would be needed for an escape. The two decisive
# honest-nulls (F1, F2) are EXPECTED to be triggered (FAIL) when the wall holds.
falsifiers = [
    Falsifier(
        name="honest_null_N1_phason_gap_stays_below_ceiling",
        predicate=lambda m: m["best_phason_gap_K"] <= m["ceiling_top_K"],
        desc=("DECISIVE honest-null. TRIGGERED (FAIL) when the best commensurate "
              "phason gap over the whole n-sweep stays AT OR BELOW the 164 K ceiling "
              "top -> the pinning gap cannot out-run the wall. PASS (escape) would "
              "need the phason gap to exceed 164 K."),
    ),
    Falsifier(
        name="honest_null_N2_strong_pinning_depairs_finiteQ",
        predicate=lambda m: m["n2_lambda_ratio"] < 1.0,
        desc=("DECISIVE honest-null (no-free-lunch). TRIGGERED (FAIL) when, at the "
              "STRONGEST pinning (n=2, largest V_p), the finite-Q pairing eigenvalue "
              "is reduced (lambda_ratio<1) -> the same Umklapp that pins the phase "
              "depairs the finite-Q channel. PASS (escape) would need pairing exactly "
              "unchanged while the gap is large."),
    ),
    Falsifier(
        name="honest_null_N3_no_joint_gap_and_pairing",
        predicate=lambda m: not m["joint_escape"],
        desc=("DECISIVE honest-null. TRIGGERED (FAIL) when NO n simultaneously clears "
              "the 164 K phason gap AND keeps lambda_ratio>=0.95 -> big gap and intact "
              "pairing are mutually exclusive. PASS (escape) would need one n to do "
              "both."),
    ),
    Falsifier(
        name="t_melt_below_room_target",
        predicate=lambda m: m["best_t_melt_K"] < m["room_K"],
        desc=("TRIGGERED (FAIL) when max T_melt=max[(pi/2)Ds,Delta_phason] stays below "
              "the 293 K room target. PASS (escape) would need T_melt>=293 K."),
    ),
    Falsifier(
        name="commensurability_energy_high_order_guard",
        predicate=lambda m: not (m["W_meV"] > 0 and m["Delta0_meV"] > 0
                                 and m["Delta0_meV"] < m["W_meV"]),
        desc=("Physical guard. TRIGGERED (FAIL) iff the small-ratio expansion is "
              "INVALID; PASS means 0<Delta0<W holds so V_p~W*(Delta0/W)^n is a real "
              "high-order commensurability energy and the kernel is meaningful."),
    ),
]

verdict_ledger = evaluate(metrics, falsifiers)
falsifiers_pass = verdict_ledger["n_pass"]
n_total = verdict_ledger["n_total"]

# Decisive honest-null logic (NO LLM self-judge): escapes-wall ONLY if the two
# decisive honest-null prongs (F1, F2) and the joint-escape prong (F3) all PASS
# (i.e. are NOT triggered) — meaning the gap genuinely beat the ceiling AND the
# pairing genuinely survived. The expected closed-negative is that F1, F2, F3 are
# all TRIGGERED (FAIL).
f1_pass = not verdict_ledger["falsifiers"][0]["triggered"]
f2_pass = not verdict_ledger["falsifiers"][1]["triggered"]
f3_pass = not verdict_ledger["falsifiers"][2]["triggered"]
escapes = f1_pass and f2_pass and f3_pass
verdict = "escapes-wall" if escapes else "confirms-wall"

# ---------------------------------------------------------------------------
# Verbatim report.
# ---------------------------------------------------------------------------
L = "=" * 74
print(L)
print("H_058  PDW Commensurate Lock — pair-density-wave pinned to the lattice")
print(L)
print("cluster: finite-Q / order-traps (violates the Q=0 premise of the freeze)")
print("host band: t={:.3f} eV, W=8t={:.3f} eV, Delta0={:.1f} meV".format(
    T_HOP_EV, W_EV, DELTA0_MEV))
print("dilute Q=0 rigidity (pi/2)D_s^Q0 anchor = {:.1f} K (TOP of frozen band, charitable)".format(
    RIGIDITY_Q0_K))
print("rho_s = {:.4f} meV ;  (Delta0/W) = {:.5f}".format(RHO_S_MEV, DELTA0_MEV / W_MEV))
print("commensurability energy V_p(n) ~ W*(Delta0/W)^n  (LRA / McMillan-Nakanishi-Shiba)")
print("phason gap Delta_phason(n) ~ sqrt(V_p*rho_s) ;  finite-Q pairing mixing ~ (Delta0/W)^(n-1)")
print("-" * 74)
print("{:>3} {:>14} {:>14} {:>13} {:>11}".format(
    "n", "Vp(meV)", "Dphason(K)", "lambda/lam0", "T_melt(K)"))
for r in rows:
    print("{:>3} {:>14.6e} {:>14.4e} {:>13.6f} {:>11.2f}".format(
        r["n"], r["Vp_meV"], r["phason_gap_K"], r["lambda_ratio"], r["t_melt_K"]))
print("-" * 74)
print("best phason gap over n-sweep    = {:.4e} K  (at n={})".format(best_gap, best_gap_n))
print("  vs ceiling top                = {:.1f} K".format(CEILING_TOP_K))
print("n=2 (strongest pinning) gap     = {:.4e} K, lambda/lam0 = {:.6f}".format(
    n2["phason_gap_K"], n2["lambda_ratio"]))
print("best T_melt = max[(pi/2)Ds, Dph]= {:.2f} K".format(best_tmelt))
print("campaign ceiling                = {:.0f}-{:.0f} K (room-T target {:.0f} K)".format(
    CEILING_BOT_K, CEILING_TOP_K, ROOM_K))
print("-" * 74)
for r in verdict_ledger["falsifiers"]:
    tag = "FAIL" if r["triggered"] else "PASS"
    print("  [{}] {}".format(tag, r["name"]))
print("-" * 74)
print("HONEST-NULL N1 escape-PASS (gap beats ceiling) = {}".format(f1_pass))
print("HONEST-NULL N2 escape-PASS (pairing fully intact) = {}".format(f2_pass))
print("HONEST-NULL N3 escape-PASS (joint gap+pairing) = {}".format(f3_pass))
print("falsifiers_pass = {}/{}".format(falsifiers_pass, n_total))
print("is_green = False")
print("absorbed = false")
print("VERDICT: {}".format(verdict))
print(L)
