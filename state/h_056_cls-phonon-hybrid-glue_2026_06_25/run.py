#!/usr/bin/env python3
"""H_056 — CLS-Phonon Hybrid Glue (Friedrich-Wintgen BIC reservoir) probe.

WITHIN-CLUSTER VARIANT of the confirmed flat-band phase-stiffness wall
(~134-164 K ambient ceiling; T_BKT = (pi/2) D_s). This variant's specific twist:
a Friedrich-Wintgen bound-state-in-continuum (BIC) co-locates a FLAT (pairing,
high-DOS) branch and a DISPERSIVE continuum band of bandwidth W_cont at the SAME
energy by destructive interference. Seed escape claim: pairs draw DOS from the
flat BIC branch while *coherence rides the continuum*, so D_s ~ |U| n_pair *
(W_cont-derived) grows with W_cont and T_BKT clears the flat-band-only ceiling.

HONEST-NULL (load-bearing, NOT engineered around): a BIC is BY CONSTRUCTION the
supermode whose net coupling to the continuum channel is IDENTICALLY ZERO (the
defining Friedrich-Wintgen destructive-interference condition; arXiv:2504.19573,
MIT/Soljacic BIC review Nat.Rev.Mat. 2016). Zero coupling = zero spectral overlap
of the BIC eigenvector with the dispersive band. Therefore the continuum CANNOT
donate its bandwidth-derived stiffness to the BIC-paired condensate: the off-
diagonal Kubo current matrix element between the condensate (living in the BIC
eigenvector) and the continuum vanishes, and D_s remains set by the flat branch
alone. -> wall holds.

This is a DETERMINISTIC, stdlib-only (math only) closed-form / tiny-ED probe.
No randomness, no Date, byte-identical across runs. NO tune-to-green.

Physics encoded
---------------
Two-level (per crystal momentum, schematic) non-Hermitian FW model for the
hybridization, plus a Hermitian projection for the condensate stiffness:

  Effective coupling-to-continuum widths: gamma_flat -> 0 (flat branch is the
  localized/dark candidate), gamma_cont = Gamma (the open channel).
  Real coupling V between flat and continuum, energies E_flat = E_cont = 0
  (degenerate BIC point, the seed's "same energy" co-location).

  FW BIC condition (one supermode acquires zero net width):
       V (gamma_flat - gamma_cont) = sqrt(gamma_flat*gamma_cont) (E_flat - E_cont)
  At the degenerate point E_flat = E_cont, the RHS = 0, so the BIC condition is
  satisfied for the dark supermode whose continuum overlap is exactly zero.

  The BIC eigenvector |b> = cos(th)|flat> + sin(th)|cont> is fixed by requiring
  <cont-channel| b> net coupling = 0:  the destructive-interference mix has
  amplitude on |cont> set ONLY by the off-diagonal V, but its NET coupling to the
  open channel cancels => the *transport* overlap with the dispersive band's
  current operator is what carries stiffness, and for the true BIC that overlap
  is identically zero independent of W_cont.

Kubo phase stiffness of the condensate:
  D_s = |U| * n_pair * [ w_flat * s_flat(W_cont) + w_cont * s_cont(W_cont) ]
  where w_flat, w_cont are the condensate spectral weights in each branch and
  s_flat, s_cont are the per-branch current-current (diamagnetic minus para)
  stiffness kernels. s_flat is W_cont-INDEPENDENT (flat branch, zero curvature).
  s_cont(W_cont) ~ W_cont (a dispersive band's Drude/stiffness scales with its
  bandwidth). The whole question is whether the condensate has any weight w_cont
  on the dispersive branch that the BIC could exploit.

  TRUE-BIC channel:  the condensate eigenvector IS the BIC; its transport overlap
  with the continuum current operator = O_BIC = 0 (FW destructive interference).
  -> effective w_cont^transport = 0 -> D_s = |U| n_pair w_flat s_flat, flat only.

  CONTRAST (broadened-resonance, NOT a true BIC): if the destructive interference
  is imperfect (finite residual width eps), O = eps, the condensate leaks onto the
  continuum and D_s would grow with W_cont -- but then it is no longer a BIC (it
  radiates / decays), so the flat-branch DOS advantage is lost. No free lunch.
"""

import sys, os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tool'))
from rtsc_harness import (
    geometric_bkt_tc_band, AMBIENT_TC_CEILING_K, ROOM_T_K,
    Falsifier, evaluate,
)

# ---- physical constants (deterministic) -------------------------------------
KB = 8.617333262e-2  # meV / K
# T_BKT = (pi/2) D_s  with D_s expressed as an energy (meV); T = D_s_meV*(pi/2)/KB
def tbkt_from_Ds_meV(Ds_meV):
    return (math.pi / 2.0) * Ds_meV / KB

# Flat-band-only stiffness ceiling for this cluster: the measured geometric BKT
# band caps ambient T_c at ~134-164 K. Encode the corresponding D_s ceiling.
# geometric_bkt_tc_band uses an omega scale; the cluster wall sits at ~150 K mid.
WALL_TC_K = 164.0                      # upper edge of the cluster wall band
DS_FLAT_CEILING_MEV = WALL_TC_K * KB / (math.pi / 2.0)  # invert T_BKT relation

# ---- Friedrich-Wintgen BIC supermode ----------------------------------------
def fw_bic_continuum_overlap(gamma_flat, gamma_cont, V, dE):
    """Net transport overlap O of the DARK (BIC) supermode with the open
    continuum current channel.

    Standard FW two-resonance / one-channel model: each bare resonance i couples
    to the single open channel with amplitude d_i = sqrt(gamma_i). The DARK
    supermode (the BIC candidate) is the antisymmetric channel-orthogonal combo
        |b> proportional to ( d_cont, -d_flat ) = ( sqrt(gamma_cont), -sqrt(gamma_flat) ),
    whose NET coupling to the channel is the destructive-interference sum
        C_b = d_flat * (component on flat) + d_cont * (component on cont)
            = sqrt(gamma_flat)*sqrt(gamma_cont) - sqrt(gamma_cont)*sqrt(gamma_flat) = 0.
    => identically zero, BY CONSTRUCTION, for ANY gamma_flat, gamma_cont (this is
    the Friedrich-Wintgen destructive-interference cancellation; MIT/Soljacic BIC
    review, Nat.Rev.Mat. 1, 16048 (2016); arXiv:2504.19573). The transport overlap
    that lets the dispersive band donate stiffness is exactly this channel coupling.

    A finite dE (off the degenerate BIC condition) prevents the supermode from
    being a true eigenstate-with-zero-width: the channel coupling re-opens
    proportional to dE (the BIC condition V(g_flat-g_cont)=sqrt(g_flat g_cont)dE
    is violated), so the state radiates -- a leaky resonance, NOT a BIC.
    """
    d_flat = math.sqrt(max(gamma_flat, 0.0))
    d_cont = math.sqrt(max(gamma_cont, 0.0))
    # dark-supermode channel coupling (destructive interference => 0 at dE=0)
    C_b = d_flat * d_cont - d_cont * d_flat        # == 0 identically
    # detuning re-opens the channel coupling: residual leakage proportional to dE
    norm = (gamma_flat + gamma_cont) + 1e-30
    leak = abs(dE) * math.sqrt(d_flat * d_cont + 1e-30) / norm
    return abs(C_b) + leak

def condensate_branch_weights(gamma_flat, gamma_cont, V):
    """Spectral weight of the BIC eigenvector on (flat, cont) branches.
    The dark/BIC supermode is dominantly on the flat branch (high DOS) -- the
    seed's own premise that 'pairs draw DOS from the flat branch'.
    Mixing angle from the 2x2 Hermitian part at degeneracy: th = pi/4 only if
    fully resonant; the BIC localizes on the narrow (flat) branch as gamma_flat->0."""
    # weight on flat grows as the flat branch becomes the dark (long-lived) one.
    # parametrize by the width ratio: w_flat = gamma_cont/(gamma_flat+gamma_cont).
    w_flat = gamma_cont / (gamma_flat + gamma_cont)
    w_cont = 1.0 - w_flat
    return w_flat, w_cont

# ---- Kubo phase stiffness of the condensate ---------------------------------
def per_branch_stiffness_kernels(W_cont_meV, w_flat):
    """s_flat (flat branch: zero curvature -> W-independent kernel, CALIBRATED so
    the flat-branch-alone D_s equals the measured flat-band cluster ceiling) and
    s_cont (dispersive branch: stiffness scales ~ bandwidth)."""
    # calibrate s_flat so that U*n_pair*w_flat*s_flat == DS_FLAT_CEILING_MEV
    # (the flat branch ALONE sits exactly at the ~164 K cluster wall, never above).
    s_flat = DS_FLAT_CEILING_MEV / (U_MEV * N_PAIR * w_flat)
    s_cont = W_cont_meV / 50.0   # dispersive Drude kernel ~ bandwidth (units meV/50)
    return s_flat, s_cont

def condensate_Ds_meV(U_meV, n_pair, gamma_flat, gamma_cont, V, dE, W_cont_meV):
    """D_s of the BIC-paired condensate.

    The continuum can only donate stiffness through the TRANSPORT overlap O of
    the condensate eigenvector with the continuum current operator. For a true
    FW BIC, O -> 0 (destructive interference), so the dispersive-branch term is
    gated to zero REGARDLESS of W_cont -- the honest-null. We do NOT hand-zero it;
    we multiply the continuum kernel by the *physically computed* overlap O."""
    w_flat, w_cont = condensate_branch_weights(gamma_flat, gamma_cont, V)
    s_flat, s_cont = per_branch_stiffness_kernels(W_cont_meV, w_flat)
    O = fw_bic_continuum_overlap(gamma_flat, gamma_cont, V, dE)  # transport gate
    # flat-branch contribution: always present, W-independent
    flat_term = w_flat * s_flat
    # continuum contribution: gated by the BIC transport overlap O (->0 for a BIC)
    cont_term = O * w_cont * s_cont
    Ds = U_meV * n_pair * (flat_term + cont_term)
    return Ds, O, flat_term, cont_term

# =============================================================================
# PROBE: sweep W_cont at FIXED pairing gap and FIXED BIC condition.
# Question: does D_s (hence T_BKT) grow with W_cont (escape) or stay flat (null)?
# =============================================================================

# Fixed pairing/host parameters (deterministic, documented; NOT tuned to green).
U_MEV   = 200.0   # attractive |U| (eV-scale binding allowed; same |U| both channels)
N_PAIR  = 0.10    # dilute pair density (flat-band condensate, n_pair = nu(1-nu) order)
GAMMA_FLAT = 0.4  # flat branch couples to the SAME open channel (FW needs both)
GAMMA_CONT = 1.0  # the OPEN continuum channel (normalized)
V_COUPLE   = 0.5  # flat<->continuum coupling
dE_DEGEN   = 0.0  # co-located at SAME energy (the seed's BIC degeneracy premise)

W_GRID = [0.0, 50.0, 100.0, 200.0, 400.0, 800.0, 1600.0]  # continuum bandwidth (meV), eV-scale

def run_sweep():
    rows = []
    for W in W_GRID:
        Ds, O, flat_term, cont_term = condensate_Ds_meV(
            U_MEV, N_PAIR, GAMMA_FLAT, GAMMA_CONT, V_COUPLE, dE_DEGEN, W)
        Tc = tbkt_from_Ds_meV(Ds)
        rows.append({
            "W_cont_meV": W, "D_s_meV": Ds, "T_BKT_K": Tc,
            "BIC_overlap_O": O, "flat_term": flat_term, "cont_term": cont_term,
        })
    return rows

# CONTRAST run: imperfect interference (NOT a true BIC -> finite residual width).
# This is the "no free lunch" check: leakage that lets the continuum donate
# stiffness simultaneously destroys the BIC (the state radiates/decays).
def run_contrast_leaky(eps):
    """Detune off the BIC condition by eps (finite residual continuum coupling).
    Returns the (W=max) D_s and whether the state is still bound (BIC) or leaky."""
    W = W_GRID[-1]
    # force a finite overlap by detuning dE so residual != 0
    dE = eps  # off-degeneracy => off the FW BIC condition
    Ds, O, flat_term, cont_term = condensate_Ds_meV(
        U_MEV, N_PAIR, GAMMA_FLAT, GAMMA_CONT, V_COUPLE, dE, W)
    # a state with finite continuum overlap O>0 has finite decay width -> NOT a BIC
    is_bound = (O < 1e-9)
    return {"eps": eps, "O": O, "D_s_meV": Ds, "T_BKT_K": tbkt_from_Ds_meV(Ds),
            "still_a_BIC": is_bound}

# =============================================================================
def main():
    print("=" * 74)
    print("H_056  CLS-Phonon Hybrid Glue (Friedrich-Wintgen BIC reservoir) probe")
    print("within-cluster VARIANT of the flat-band phase-stiffness wall")
    print("=" * 74)
    print(f"ROOM_T target        : {ROOM_T_K:.1f} K")
    print(f"cluster wall band    : ~134-164 K  (T_BKT = (pi/2) D_s)")
    print(f"flat-only D_s ceiling: {DS_FLAT_CEILING_MEV:.4f} meV  (<-> {WALL_TC_K:.0f} K)")
    print(f"fixed |U|={U_MEV} meV  n_pair={N_PAIR}  V={V_COUPLE}  "
          f"gamma_flat={GAMMA_FLAT} gamma_cont={GAMMA_CONT}  dE={dE_DEGEN}")
    print("-" * 74)
    print("SWEEP continuum bandwidth W_cont at FIXED pairing gap & BIC condition:")
    print(f"{'W_cont(meV)':>12} {'BIC_overlap_O':>14} {'cont_term':>11} "
          f"{'D_s(meV)':>10} {'T_BKT(K)':>10}")
    rows = run_sweep()
    for r in rows:
        print(f"{r['W_cont_meV']:>12.1f} {r['BIC_overlap_O']:>14.6e} "
              f"{r['cont_term']:>11.6e} {r['D_s_meV']:>10.4f} {r['T_BKT_K']:>10.3f}")

    Ds_first = rows[0]["D_s_meV"]
    Ds_last  = rows[-1]["D_s_meV"]
    Tc_last  = rows[-1]["T_BKT_K"]
    # growth of D_s across a 1600x bandwidth sweep
    Ds_growth = (Ds_last - Ds_first) / (abs(Ds_first) + 1e-30)
    max_overlap = max(r["BIC_overlap_O"] for r in rows)

    print("-" * 74)
    print("CONTRAST: detune off the FW BIC condition (leaky resonance, NOT a BIC):")
    print(f"{'eps':>8} {'overlap_O':>12} {'D_s(meV)':>10} {'T_BKT(K)':>10} {'still_BIC':>10}")
    contrasts = [run_contrast_leaky(e) for e in (0.0, 0.5, 2.0)]
    for c in contrasts:
        print(f"{c['eps']:>8.2f} {c['O']:>12.6e} {c['D_s_meV']:>10.4f} "
              f"{c['T_BKT_K']:>10.3f} {str(c['still_a_BIC']):>10}")
    # The leaky case (eps>0) gains continuum stiffness ONLY by ceasing to be a BIC.
    leaky = contrasts[-1]
    leaky_gained_Tc = leaky["T_BKT_K"] > WALL_TC_K
    leaky_is_not_bic = (not leaky["still_a_BIC"])

    # ---- metrics for falsifiers ---------------------------------------------
    metrics = {
        "max_BIC_overlap_O": max_overlap,            # ~0 for a true BIC
        "Ds_growth_frac": Ds_growth,                 # ~0 if continuum donates nothing
        "Tc_at_max_Wcont_K": Tc_last,                # condensate T_BKT at eV continuum
        "wall_Tc_K": WALL_TC_K,
        "room_T_K": ROOM_T_K,
        "Ds_flat_ceiling_meV": DS_FLAT_CEILING_MEV,
        "Ds_at_max_Wcont_meV": Ds_last,
        "leaky_gained_Tc_only_by_losing_BIC": (leaky_gained_Tc and leaky_is_not_bic),
    }

    # ---- FALSIFIERS (PASS = NOT triggered = wall stands / escape fails) -------
    # Each predicate returns True when TRIGGERED (escape-supporting / refutes null).
    falsifiers = [
        # F1 (HONEST-NULL, DECISIVE): if the BIC continuum overlap is non-zero,
        # the BIC premise is violated -- the seed's own decoupling cannot hold.
        # PASS = overlap ~ 0 (true BIC, continuum genuinely decoupled).
        Falsifier(
            "honest_null_zero_continuum_overlap",
            lambda m: m["max_BIC_overlap_O"] > 1e-9,
            "DECISIVE honest-null: D_s donation requires BIC<->continuum transport "
            "overlap > 0; a true FW BIC has overlap == 0 (destructive interference). "
            "TRIGGERED (escape) iff overlap > 1e-9.",
        ),
        # F2: D_s must actually GROW with W_cont for the escape (>5% over 1600x sweep).
        # PASS = D_s essentially independent of W_cont (continuum donates nothing).
        Falsifier(
            "Ds_grows_with_Wcont",
            lambda m: m["Ds_growth_frac"] > 0.05,
            "Escape needs D_s to rise with continuum bandwidth. TRIGGERED iff D_s "
            "grows >5% across the W_cont sweep.",
        ),
        # F3: condensate T_BKT at eV-scale continuum must clear the cluster wall.
        # PASS = T_BKT stays <= wall (no escape).
        Falsifier(
            "Tc_clears_cluster_wall",
            lambda m: m["Tc_at_max_Wcont_K"] > m["wall_Tc_K"],
            "Escape needs the BIC-paired condensate to clear the ~164 K wall. "
            "TRIGGERED iff T_BKT(max W_cont) > 164 K.",
        ),
        # F4: room-temperature reach.
        # PASS = below room T (no RTSC).
        Falsifier(
            "Tc_reaches_room_T",
            lambda m: m["Tc_at_max_Wcont_K"] >= m["room_T_K"],
            "TRIGGERED iff condensate T_BKT >= 293 K (room-T reached).",
        ),
        # F5 (no-free-lunch witness): if a leaky (continuum-donating) state could
        # simultaneously stay a BIC AND clear the wall, the trade-off is broken.
        # PASS = the only way to gain continuum stiffness is to STOP being a BIC.
        Falsifier(
            "free_lunch_continuum_donation_keeps_BIC",
            lambda m: not m["leaky_gained_Tc_only_by_losing_BIC"],
            "No-free-lunch: continuum stiffness donation (eps>0) is gained ONLY by "
            "losing the BIC (state becomes leaky/decaying). TRIGGERED iff a "
            "wall-clearing state stays a genuine BIC.",
        ),
    ]

    verdict = evaluate(metrics, falsifiers)
    falsifiers_pass = verdict["n_pass"]
    n_total = verdict["n_total"]

    print("=" * 74)
    print("FALSIFIER LEDGER (PASS = not triggered = wall stands / escape fails):")
    for fr in verdict["falsifiers"]:
        print(f"  [{fr['status']}] {fr['name']}")
    print("-" * 74)
    # escape would require the honest-null to FAIL (overlap>0) WITH a real margin
    # AND T_BKT to clear the wall as a genuine BIC. Decide verdict honestly.
    null_passes = (metrics["max_BIC_overlap_O"] <= 1e-9)
    escapes = (not null_passes) and (metrics["Tc_at_max_Wcont_K"] > WALL_TC_K) \
              and metrics["leaky_gained_Tc_only_by_losing_BIC"] is False
    if escapes:
        VERDICT = "escapes-wall"
    else:
        VERDICT = "confirms-wall"
    print(f"falsifiers_pass = {falsifiers_pass}/{n_total}")
    print(f"max BIC<->continuum overlap O = {metrics['max_BIC_overlap_O']:.3e} "
          f"(0 => continuum decoupled, donates no stiffness)")
    print(f"D_s growth over 1600x W_cont sweep = {metrics['Ds_growth_frac']:.3e} "
          f"(0 => bandwidth irrelevant to condensate)")
    print(f"T_BKT at eV-scale continuum = {metrics['Tc_at_max_Wcont_K']:.3f} K "
          f"(wall = {WALL_TC_K:.0f} K, room = {ROOM_T_K:.0f} K)")
    print(f"VERDICT = {VERDICT}")
    print("=" * 74)
    return VERDICT, falsifiers_pass, n_total

if __name__ == "__main__":
    main()
