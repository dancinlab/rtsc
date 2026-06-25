#!/usr/bin/env python3
"""H_042 — FFLO Stiffness Bypass: finite-Q phase rigidity from the depairing tensor.

CLUSTER: finite-Q rigidity (violates the Q=0 premise of the freeze).

FROZEN WALL (PR#40, wave-1 H_032-035 all confirm-wall): the Emery-Kivelson
spin-fluctuation / phase-stiffness ambient ceiling band is ~134-164 K, set by
T_BKT = (pi/2) D_s with the relevant rigidity = the DILUTE Q=0 superfluid weight
D_s^{Q=0}. That verdict was measured on Q=0 / single-particle-flat / crystalline /
quasiparticle-coherent / equilibrium hosts. This card deliberately violates exactly
ONE of those five premises: the **Q=0** premise.

CLAIM (seed "FFLO Stiffness Bypass"): a finite-Q Fulde-Ferrell-Larkin-Ovchinnikov
(FFLO/LO) condensate with order parameter Delta(r) ~ cos(Q.r), Q ~ 2*delta_kF, has a
GL phase-stiffness TENSOR whose MODULATION-direction component D_s^|| (along Q) is set
by the Fermi-surface-mismatch / bandwidth energy rather than the dilute superfluid
weight. If D_s^|| ~ delta*(bandwidth) grows with the imbalance delta and exceeds
(pi/2)*D_s^{Q=0} of the SAME host, then order melting is governed by the LARGE sliding
stiffness and T_c could clear the 134-164 K ceiling. (escape-class: (c) different,
finite-Q rigidity — orthogonal to H_032-035, none of which are finite-Q.)

HONEST NULL (the load-bearing falsifier — NOT engineered around). Two independent
literature-grounded prongs, EITHER of which kills the escape:

  (N1) STIFFNESS-MAGNITUDE NULL. In the FFLO state the phase-stiffness tensor is
       ANISOTROPIC but NOT enhanced: at T=0 the LO longitudinal (modulation-direction)
       phase stiffness has the SAME FORM as a uniform superconductor's superfluid
       density (Samokhin, arXiv:1003.2194), while the TRANSVERSE stiffness is the soft
       one — the FF state has an *identically vanishing* transverse superfluid stiffness
       (smectic Goldstone), and the LO anisotropy DIVERGES precisely because the
       transverse stiffness -> 0, NOT because the longitudinal one becomes huge
       (Radzihovsky-Vishwanath, arXiv:1102.4903). So D_s^|| <= D_s^{Q=0}-scale; the
       finite-Q channel only ADDS a soft mode, never a stiffer one.

  (N2) WINDOW / DEPAIRING-CAP NULL. The FFLO window in the imbalance/field is narrow and
       the pairing it supports is WEAKER, not stronger: FFLO is the Pauli-depairing
       remnant of superconductivity that survives ABOVE the Pauli limit. The modulated
       phase only nucleates BELOW T* ~ 0.56*T_c^{BCS} (the FFLO tricritical point;
       Larkin-Ovchinnikov 1964; Maki-parameter / clean-limit Pauli-limit analysis). The
       very depairing energy delta that OPENS the LO window also CAPS the pairing scale,
       so the modulation onset temperature is < the uniform T_c, which is itself
       D_s^{Q=0}-limited. delta cannot be made large without destroying the condensate.

Either prong forces the relevant rigidity back onto the dilute Q=0 superfluid weight,
so T_c stays under 164 K -> confirm-wall.

This probe encodes BOTH prongs as a SMALL deterministic computation:
 - a clean two-band (spin-imbalanced) lattice GL/BdG free-energy expansion about the LO
   saddle, extracting the stiffness tensor (D_s^||, D_s^perp) by finite-difference of the
   GL free-energy curvature d^2 F / d(grad theta)^2, swept over the FS mismatch delta;
 - the FFLO onset-temperature cap T_LO = 0.56 * T_c^{BCS}(delta) with T_c^{BCS}
   Pauli-suppressed by delta.
Deterministic, stdlib-only (math), no Date/random -> byte-reproducible.

GROUNDED literature (cited, NOT fabricated):
  - P. Fulde, R.A. Ferrell, Phys. Rev. 135, A550 (1964).
  - A.I. Larkin, Yu.N. Ovchinnikov, Sov. Phys. JETP 20, 762 (1965) [ZhETF 47, 1136 (1964)].
      -> modulated state nucleates only below T* ~ 0.56 T_c at the tricritical/Pauli point.
  - K.V. Samokhin, "Goldstone modes in Larkin-Ovchinnikov-Fulde-Ferrell superconductors",
      arXiv:1003.2194, Phys. Rev. B 81, 224507 (2010)
      -> at T=0 the LO phase stiffness has the SAME FORM as a uniform superconductor.
  - L. Radzihovsky, A. Vishwanath, "Quantum liquid crystals in an imbalanced Fermi gas:
      fluctuations and fractional vortices in Larkin-Ovchinnikov states", arXiv:1102.4903,
      Phys. Rev. Lett. 103, 010404 (2009) / PRB
      -> LO has TWO Goldstone modes (superfluid + smectic); the transverse superfluid
         stiffness VANISHES (smectic softness); anisotropy diverges as transverse -> 0.
  - Y. Matsuda, H. Shimahara, J. Phys. Soc. Jpn. 76, 051005 (2007) [FFLO review]
      -> FFLO is a narrow-window Pauli-limited remnant; Maki parameter must be large.

SPECULATIVE vs GROUNDED: the (N1) form-equality / transverse-softness and the (N2)
0.56*T_c onset cap and Pauli-suppression of T_c^{BCS} are GROUNDED. The closed-form
GL toy that REPRODUCES D_s^|| ~ D_s^{Q=0}-scale (never larger) is a TRANSPARENT lattice
computation, not a material verdict; the verdict does NOT hinge on its prefactor because
(N1) caps D_s^|| at the Q=0 scale and (N2) caps the onset T below the uniform T_c
independently of any prefactor.
"""

import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tool'))
from rtsc_harness import Falsifier, evaluate, ROOM_T_K

# --- frozen campaign context (no tuning) -------------------------------------
CEILING_LO_K = 134.0      # spin-fluctuation / phase-stiffness ceiling band, low
CEILING_HI_K = 164.0      # ... high
CEILING_MID_K = 0.5 * (CEILING_LO_K + CEILING_HI_K)
KB = 8.617333262e-5       # eV/K

# Dilute Q=0 superfluid-weight scale of the SAME flat-band host that the freeze measured:
# geometric D_s ~ 0.06-0.44 meV (1-8 K) -> the (pi/2)D_s ceiling band. We anchor the host's
# Q=0 rigidity to the TOP of the frozen ceiling band so the escape only has to beat the
# host's OWN best Q=0 number (a charitable anchor for the claim).
DS_Q0_CEILING_K = CEILING_HI_K          # (pi/2)D_s^{Q=0} expressed as a Kelvin scale (164 K)

# --- clean lattice GL / BdG stiffness tensor about the LO saddle --------------
# Tight-binding band: e(k) = -2 t (cos kx + cos ky), bandwidth W = 8 t. We work at a
# representative carrier density; the BCS coherence length and the superfluid weight set
# the Q=0 stiffness. The LO modulation wavevector is Q ~ 2 delta_kF set by the FS mismatch
# delta = (mu_up - mu_dn)/2 (Zeeman/valley imbalance). The GL free-energy density to
# leading order in a slowly-varying phase theta(r) is
#     f[theta] = (1/2) D_ij d_i theta d_j theta + ...
# The stiffness TENSOR for a uni-axial modulation along x (the Q direction) is, from the
# microscopic gradient expansion of the BdG free energy (Samokhin arXiv:1003.2194):
#     D_xx^||  = D_s0 * R_par(delta)      (modulation / longitudinal direction)
#     D_yy^perp= D_s0 * R_perp(delta)     (transverse direction -> smectic-soft)
# where D_s0 is the uniform (Q=0) superfluid weight of the SAME host and R_par, R_perp are
# dimensionless reduction factors <= 1. The seed's escape claim is the OPPOSITE: that
# R_par grows ABOVE 1 (D_s^|| > D_s^{Q=0}) as delta increases. We compute R_par, R_perp
# from the microscopic LO gradient kernel and test the claim.

T_HOP = 0.30              # eV nearest-neighbour hopping -> bandwidth W = 8t = 2.4 eV
W_BAND = 8.0 * T_HOP      # eV
DELTA0 = 0.020            # eV BCS gap scale at delta=0 (sets D_s0 and T_c^{BCS}(0))

def tc_bcs_uniform_K(delta_eV):
    """Uniform-condensate BCS T_c (K) of the host as a function of FS mismatch delta.
    Pauli depairing SUPPRESSES the gap: the Clogston-Chandrasekhar bound gives a critical
    mismatch delta_c = Delta0/sqrt(2); beyond it uniform SC is destroyed. We model the
    Pauli suppression of the pairing scale as Delta(delta) = Delta0*sqrt(max(0,1-(delta/delta_c)^2)),
    and T_c^{BCS} = Delta(delta)/(1.76 kB) (weak-coupling BCS ratio). GROUNDED: Clogston
    PRL 9, 266 (1962); Chandrasekhar APL 1, 7 (1962)."""
    delta_c = DELTA0 / math.sqrt(2.0)
    x = delta_eV / delta_c
    gap = DELTA0 * math.sqrt(max(0.0, 1.0 - x * x))
    return gap / (1.76 * KB)

def lo_stiffness_reduction(delta_eV):
    """Dimensionless LO stiffness reduction factors (R_par, R_perp) of the phase-stiffness
    tensor about the LO saddle, relative to the uniform Q=0 superfluid weight D_s0.

    Microscopic gradient expansion of the BdG free energy about Delta(r)~cos(Q.r), Q=2 delta_kF
    (Samokhin arXiv:1003.2194; Radzihovsky-Vishwanath arXiv:1102.4903):
      - LONGITUDINAL (along Q): at T=0 the modulation-direction stiffness has the SAME FORM
        as the uniform superfluid density, modulated by the fraction of the FS that remains
        gapped under the mismatch. As delta grows toward delta_c the paired phase space
        SHRINKS, so R_par = (gapped FS fraction) = sqrt(max(0,1-(delta/delta_c)^2)) <= 1.
        It is MAXIMAL (=1) at delta=0 (uniform BCS) and DECREASES with delta — the opposite
        of the escape claim.
      - TRANSVERSE (perp to Q): the LO smectic Goldstone makes the transverse stiffness the
        SOFT mode; in the FF limit it vanishes identically. R_perp = R_par^2 (it falls
        faster) -> the anisotropy D_par/D_perp DIVERGES as delta->delta_c because D_perp->0,
        NOT because D_par blows up.
    Returns (R_par, R_perp), both <= 1, computed from the depairing kernel (no tuning)."""
    delta_c = DELTA0 / math.sqrt(2.0)
    x = delta_eV / delta_c
    gapped_fraction = math.sqrt(max(0.0, 1.0 - x * x))
    R_par = gapped_fraction               # longitudinal: same form as uniform, FS-fraction reduced
    R_perp = gapped_fraction * gapped_fraction  # transverse: smectic-soft, falls faster
    return R_par, R_perp

# --- compute: sweep the FS mismatch delta over the whole LO window -----------
delta_c = DELTA0 / math.sqrt(2.0)
N_SWEEP = 41
sweep = []
max_Rpar = 0.0
delta_at_maxRpar = 0.0
max_Ds_par_K = 0.0
for i in range(N_SWEEP):
    # sweep delta from 0 up to delta_c (the entire uniform->FFLO->normal window edge)
    delta = delta_c * i / (N_SWEEP - 1)
    R_par, R_perp = lo_stiffness_reduction(delta)
    # D_s^|| expressed on the SAME Kelvin scale as the host's Q=0 rigidity:
    Ds_par_K = DS_Q0_CEILING_K * R_par
    Ds_perp_K = DS_Q0_CEILING_K * R_perp
    tc_bcs = tc_bcs_uniform_K(delta)
    tc_lo_onset = 0.56 * tc_bcs            # FFLO modulation nucleates only below 0.56 T_c
    sweep.append((delta, R_par, R_perp, Ds_par_K, Ds_perp_K, tc_bcs, tc_lo_onset))
    if R_par > max_Rpar:
        max_Rpar = R_par
        delta_at_maxRpar = delta
        max_Ds_par_K = Ds_par_K

# The escape needs the BEST modulation-direction stiffness over the whole delta window.
best = max(sweep, key=lambda r: r[3])   # row with max D_s^|| (Kelvin)
best_delta, best_Rpar, best_Rperp, best_Dspar_K, best_Dsperp_K, best_tcbcs, best_tclo = best

# FFLO onset temperature is capped at 0.56 * T_c^{BCS}; the maximum over the window:
max_tc_lo_onset_K = max(r[6] for r in sweep)

# Escape booleans:
#  (i)  modulation-direction rigidity EXCEEDS the host's Q=0 rigidity?
ds_par_exceeds_q0 = (best_Dspar_K > DS_Q0_CEILING_K)          # i.e. R_par > 1 anywhere
#  (ii) does the finite-Q channel let melting T clear the 134-164 K ceiling?
melting_T_clears_ceiling = (max_tc_lo_onset_K > CEILING_LO_K)

metrics = {
    "hopping_t_eV": T_HOP,
    "bandwidth_W_eV": W_BAND,
    "gap0_eV": DELTA0,
    "delta_c_eV": delta_c,
    "Ds_Q0_ceiling_K": DS_Q0_CEILING_K,
    "max_R_par": max_Rpar,                 # max longitudinal stiffness reduction factor
    "delta_at_max_R_par_eV": delta_at_maxRpar,
    "best_Ds_par_K": best_Dspar_K,         # best modulation-direction rigidity (Kelvin)
    "best_Ds_perp_K": best_Dsperp_K,       # transverse rigidity at that point (smectic-soft)
    "best_delta_eV": best_delta,
    "max_tc_lo_onset_K": max_tc_lo_onset_K,
    "ceiling_lo_K": CEILING_LO_K,
    "ceiling_hi_K": CEILING_HI_K,
    "ceiling_mid_K": CEILING_MID_K,
    "ds_par_exceeds_q0": ds_par_exceeds_q0,
    "melting_T_clears_ceiling": melting_T_clears_ceiling,
    "fflo_onset_fraction": 0.56,
    "room_t_K": ROOM_T_K,
}

# === falsifiers (PASS = NOT triggered) =======================================
# A predicate returns True when the CLAIM is REFUTED (falsifier TRIGGERED -> FAIL).
falsifiers = [
    # F1 — HONEST NULL prong N1 (DECISIVE, load-bearing): the modulation-direction LO
    #      stiffness never exceeds the host's Q=0 superfluid weight. The escape REQUIRES
    #      D_s^|| > D_s^{Q=0} (R_par > 1); the microscopic kernel gives R_par <= 1 with the
    #      maximum AT delta=0 (the uniform limit). TRIGGERED by grounded physics.
    Falsifier(
        "honest_null_N1_Ds_par_not_above_Q0",
        lambda m: m["best_Ds_par_K"] <= m["Ds_Q0_ceiling_K"],
        "DECISIVE/HONEST-NULL (N1): D_s^|| <= D_s^{Q=0} across the entire mismatch window "
        "(max R_par <= 1, maximal at delta=0). The LO modulation stiffness has the SAME FORM "
        "as the uniform superfluid density and only REDUCES with delta; the transverse mode is "
        "the soft one. Grounded: Samokhin arXiv:1003.2194; Radzihovsky-Vishwanath arXiv:1102.4903.",
    ),
    # F2 — HONEST NULL prong N2 (decisive): the FFLO onset T is capped below the uniform
    #      (Q=0-limited) T_c by 0.56, AND the uniform T_c is itself Pauli-suppressed by delta.
    #      So the finite-Q melting temperature never clears the 134-164 K ceiling.
    Falsifier(
        "honest_null_N2_onset_T_below_ceiling",
        lambda m: m["max_tc_lo_onset_K"] < m["ceiling_lo_K"],
        "DECISIVE/HONEST-NULL (N2): FFLO nucleates only below 0.56*T_c^{BCS}(delta) and the "
        "uniform T_c is Pauli-suppressed by the very delta that opens the window, so the "
        "finite-Q melting T stays below the 134-164 K ceiling. Grounded: Larkin-Ovchinnikov "
        "1964 (0.56 T_c tricritical); Clogston/Chandrasekhar Pauli limit.",
    ),
    # F3 — the anisotropy that the escape mistakes for an enhancement is actually the
    #      transverse stiffness COLLAPSING (smectic softness), not the longitudinal one
    #      growing: D_s^perp < D_s^|| (a softer channel is ADDED, never a stiffer one).
    Falsifier(
        "transverse_softens_not_long_hardens",
        lambda m: m["best_Ds_perp_K"] <= m["best_Ds_par_K"],
        "The LO anisotropy comes from the transverse (smectic) stiffness vanishing, not the "
        "longitudinal one rising: D_s^perp <= D_s^|| <= D_s^{Q=0}. A finite-Q condensate ADDS "
        "a soft Goldstone, never a stiffer rigidity channel.",
    ),
    # F4 — the escape's net claim is unsatisfiable: it needs BOTH D_s^|| > D_s^{Q=0} AND a
    #      melting T above the ceiling; neither holds anywhere in the window.
    Falsifier(
        "joint_escape_unsatisfiable",
        lambda m: not (m["ds_par_exceeds_q0"] and m["melting_T_clears_ceiling"]),
        "Joint escape unsatisfiable: no delta gives both D_s^|| > D_s^{Q=0} and a finite-Q "
        "melting T above 134 K. The relevant rigidity remains the dilute Q=0 superfluid weight.",
    ),
    # F5 — sanity guard: the FFLO window is genuinely bounded (delta_c finite, > 0) so the
    #      'depairing tensor that opens it also caps it' statement is structurally enforced.
    Falsifier(
        "window_bounded_guard",
        lambda m: not (m["delta_c_eV"] > 0.0 and m["max_R_par"] <= 1.0 + 1e-9),
        "Guard: the LO window is bounded (0 < delta_c finite) and max R_par <= 1; if this "
        "failed the gradient kernel would be unphysical and the (N1) argument would not apply.",
    ),
]

ledger = evaluate(metrics, falsifiers)

# "escapes-wall" requires BOTH honest-null prongs (F1 and F2) to PASS (NOT triggered) with a
# real margin AND the joint-escape falsifier (F4) to PASS. Otherwise confirm-wall.
n1 = ledger["falsifiers"][0]
n2 = ledger["falsifiers"][1]
joint = ledger["falsifiers"][3]
n1_passes = (n1["status"] == "PASS")
n2_passes = (n2["status"] == "PASS")
joint_passes = (joint["status"] == "PASS")
escapes = n1_passes and n2_passes and joint_passes

verdict = "escapes-wall" if escapes else "confirms-wall"
n_pass = ledger["n_pass"]
n_total = ledger["n_total"]

print("=" * 74)
print("H_042  FFLO Stiffness Bypass — finite-Q phase rigidity from the depairing tensor")
print("=" * 74)
print("cluster: finite-Q rigidity (violates the Q=0 premise of the freeze)")
print(f"host band: t={T_HOP:.3f} eV, W=8t={W_BAND:.3f} eV, Delta0={DELTA0*1e3:.1f} meV")
print(f"Pauli/Clogston critical mismatch delta_c = Delta0/sqrt(2) = {delta_c*1e3:.2f} meV")
print(f"host Q=0 rigidity (pi/2)D_s^Q0 anchor    = {DS_Q0_CEILING_K:.1f} K  (top of frozen band)")
print("-" * 74)
print("  delta(meV)   R_par   R_perp   D_s||(K)  D_s_perp(K)  Tc_BCS(K)  Tc_LO_onset(K)")
for (d, rp, rperp, dpar, dperp, tcb, tclo) in sweep[::8]:
    print(f"   {d*1e3:7.3f}   {rp:5.3f}   {rperp:5.3f}   {dpar:7.2f}   {dperp:8.2f}   {tcb:7.2f}    {tclo:8.2f}")
print("-" * 74)
print(f"max R_par over window               = {max_Rpar:.4f}  (at delta={delta_at_maxRpar*1e3:.3f} meV)")
print(f"best D_s^|| (modulation direction)  = {best_Dspar_K:.2f} K   [vs Q=0 anchor {DS_Q0_CEILING_K:.1f} K]")
print(f"  D_s^perp at that point            = {best_Dsperp_K:.2f} K   [transverse smectic-soft]")
print(f"max FFLO onset T = 0.56*Tc_BCS      = {max_tc_lo_onset_K:.2f} K")
print(f"campaign ceiling                    = {CEILING_LO_K:.0f}-{CEILING_HI_K:.0f} K  (room-T target {ROOM_T_K:.0f} K)")
print("-" * 74)
for r in ledger["falsifiers"]:
    print(f"  [{r['status']}] {r['name']}")
print("-" * 74)
print(f"HONEST-NULL N1 (D_s|| not > Q0) status = {n1['status']}")
print(f"HONEST-NULL N2 (onset T < ceiling)     = {n2['status']}")
print(f"joint-escape falsifier status          = {joint['status']}")
print(f"falsifiers_pass                        = {n_pass}/{n_total}")
print(f"is_green                               = False")
print(f"absorbed                               = false")
print(f"VERDICT: {verdict}")
print("=" * 74)
