"""rtsc_candidates — living candidate-materials registry + verifier for the +@ trilayer.

The binding wall of the +@ room-T architecture is MATERIALS existence (research verdict
🟠 MATERIALS-LIMITED, state/research-excitonic-sc-wall-classification-*.md): the mechanism
is allowed but no real material yet supplies the load-bearing layers. This is the LIVING
ledger we grow every research round — layer-A flat-band-geometry hosts and layer-B
bosonic-glue hosts, each with published properties + a citation + a `verified` flag.

The VERIFIER (검증기) is NOT a new engine — it reuses the campaign's shared falsifier engine
in tool/rtsc_harness.py (two_lever_box_check / Falsifier / evaluate). `verify()` runs a
candidate (or an A+B pair) through pre-registered, measurable falsifiers and returns a
verbatim verdict; only VERIFIED properties pass — unverified ones surface as `gaps`.

HONESTY (commons): every numeric property carries (value, source, verified). NO fabricated
values; a gap is "what research must still confirm", never tune-to-green. absorbed=false.

Run:  python3 tool/rtsc_candidates.py   (leaderboard + a verify() demo)
"""

from __future__ import annotations

import math
import os
import sys
from dataclasses import dataclass

_HERE = os.path.dirname(__file__)
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from rtsc_harness import two_lever_box_check, geometric_bkt_tc_band, Falsifier, evaluate

# --- design-box targets (the +@ levers) --------------------------------------
G_MIN = 2.0                     # flat-band quantum-geometry lever (∫tr g)
GLUE_BAND_MEV = (100.0, 600.0)  # an electronic/bosonic glue mode must land in this window
GLUE_TARGET_MEV = 349.0         # relaxed room-T glue scale (H_007 3-lever)


@dataclass
class Candidate:
    """One material candidate for a +@ layer. role = 'A' (geometry) | 'B' (glue).
    Each property = (value_or_None, source, verified)."""
    name: str
    role: str
    lattice: str = ""
    g_mean: tuple = (None, "", False)            # A: ∫tr g (quantum geometry)
    boson_meV: tuple = (None, "", False)         # B: bosonic mode energy (exciton/plasmon)
    frustrated: tuple = (None, "", False)        # A: frustrated lattice? (H_016 escape)
    competing_order: tuple = (None, "", False)   # 'none'|'CDW'|'SDW'|... (H_014 risk)
    note: str = ""

    def gaps(self) -> list:
        """Unverified / missing properties research must still confirm."""
        rel = ["g_mean", "frustrated"] if self.role == "A" else ["boson_meV", "competing_order"]
        out = []
        for attr in rel:
            val, src, ver = getattr(self, attr)
            if val is None:
                out.append(f"{attr}: unknown")
            elif not ver:
                out.append(f"{attr}={val}: UNVERIFIED ({src or 'no source'})")
        return out


# --- the verifier (검증기): reuse the harness falsifier engine ------------------

def verify(c: Candidate) -> dict:
    """Run a single candidate through pre-registered falsifiers via the harness engine.
    PASS = not triggered. Only VERIFIED properties can pass; unverified ones trigger."""
    g_val, _, g_ver = c.g_mean
    b_val, _, b_ver = c.boson_meV
    fr_val, _, fr_ver = c.frustrated
    co_val, _, co_ver = c.competing_order
    metrics = {
        "role": c.role,
        "g_verified_ge_min": bool(g_ver and g_val is not None and g_val >= G_MIN),
        "boson_verified_in_band": bool(b_ver and b_val is not None and GLUE_BAND_MEV[0] <= b_val <= GLUE_BAND_MEV[1]),
        "frustrated_verified": bool(fr_ver and fr_val),
        "competing_clean_verified": bool(co_ver and co_val == "none"),
    }
    if c.role == "A":
        fals = [
            Falsifier("FA1_geometry_verified", lambda m: not m["g_verified_ge_min"],
                      "PASS = a VERIFIED ⟨g⟩>=2 (geometry lever met)."),
            Falsifier("FA2_frustrated_verified", lambda m: not m["frustrated_verified"],
                      "PASS = a VERIFIED frustrated lattice (H_016 competing-order escape)."),
        ]
    else:
        fals = [
            Falsifier("FB1_mode_verified_in_band", lambda m: not m["boson_verified_in_band"],
                      "PASS = a VERIFIED bosonic mode inside the glue band."),
            Falsifier("FB2_competing_order_clean", lambda m: not m["competing_clean_verified"],
                      "PASS = VERIFIED absence of a pre-empting CDW/SDW (H_014 risk)."),
        ]
    v = evaluate(metrics, fals)
    return {"name": c.name, "role": c.role, "qualified": v["all_pass"],
            "n_pass": v["n_pass"], "n_total": v["n_total"], "gaps": c.gaps()}


def verify_pair(a: Candidate, b: Candidate) -> dict:
    """Verify an A+B pair against the +@ two-lever box (harness), using ONLY verified values.
    Returns box result + a combined qualified flag + all gaps."""
    g_val, _, g_ver = a.g_mean
    b_val, _, b_ver = b.boson_meV
    g_use = g_val if g_ver and g_val is not None else 0.0
    om_use = b_val if b_ver and b_val is not None else 0.0
    box = two_lever_box_check(g_use, om_use, u_over_omega=2.0)
    bkt = geometric_bkt_tc_band(om_use) if om_use > 0 else 0.0
    va, vb = verify(a), verify(b)
    return {"pair": f"{a.name}/hBN/{b.name}", "in_box": box["in_box"],
            "bkt_tc_K": round(bkt, 1), "A_qualified": va["qualified"],
            "B_qualified": vb["qualified"], "gaps": va["gaps"] + vb["gaps"]}


# --- seed registry (grow this every research round; verified=True only with a real source) ---
# Layer A — CoSn/Nb3Cl8 ⟨g⟩ are the campaign's published ledger anchors (H_001) -> verified.
LAYER_A: list = [
    Candidate("CoSn", "A", "kagome",
              g_mean=(2.87, "H_001 ledger; QGT directly measured arXiv:2412.17809 (Kang 2024); flat band W<0.2eV arXiv:2001.11738; "
                            "narrow-band CONFIRMED by our DFT (H_019): PBE QE7.2 scf+bands a=5.2693/c=4.2431A finds a kagome flat-band "
                            "manifold W=0.158 eV (band 41, narrowest of a 0.16-0.25 eV cluster). OUR-DFT QUANTUM GEOMETRY (H_024): a NN-kagome "
                            "tight-binding fit to OUR bands (t=0.077 eV from the 3-band group [39,40,41] span=0.462 eV=6t; no wannier90 built) "
                            "gives the QGT-convention metric integral I=(1/2pi)int tr g d2k = 2.856 -- which SUPPORTS g>=2 and MATCHES the "
                            "measured QGT 2.87 (geometry lever survives OUR DFT). Position ~1.45 eV below E_F is the DEEPER in-plane-d kagome "
                            "manifold and is REAL not a PBE artifact (CoSn hosts multiple orbital flat bands; the dxz/dyz one is near E_F, the "
                            "in-plane ones are deeper; DFT E_F only ~140 meV off ARPES, Kang Nat.Comm.2020) -- still needs doping/gating to E_F. "
                            "H_027 MEASURED that doping-to-E_F requirement on OUR fuller spin-polarized Co3Sn3 bands: the near-E_F flat band needs "
                            "4.73 e-/cell = 1.58 holes/CoSn f.u. (EXTREME, beyond gating) to reach E_F; at that doped E_F the geometry SURVIVES "
                            "(TB-fit I=2.855~=QGT 2.87) and the filling is FAVOURABLE (nu=0.507 -> nu(1-nu)=0.250, the half-filling D_s max) -> "
                            "geometry/filling robust IF reachable, but accessibility EXTREME", True),
              frustrated=(True, "kagome lattice", True),
              note="geometry OK + directly-measured QGT + OUR-DFT metric integral I=2.86~=QGT 2.87 (H_024). OUR DFT (H_019) confirms a W<0.2eV "
                   "flat band but ~1.45eV below E_F -- the DEEPER in-plane-d kagome manifold (REAL, not PBE artifact; CoSn has multiple orbital "
                   "flat bands), so reaching E_F needs heavy doping/gating (a real risk, honestly logged; H_019 F2 FAILED on position). "
                   "H_027 SETTLED the doping-to-E_F conditional on OUR fuller spin-polarized Co3Sn3 PBE bands (near-E_F flat band 45, W=0.167eV, "
                   "-0.44eV below E_F): (1) DOPING to slide E_F onto it = 4.73 e-/cell = 1.58 holes/CoSn f.u. = 5.1% of valence -> EXTREME "
                   "(>0.7 h/f.u.; beyond electrostatic gating, needs full chemical substitution -- a direct consequence of the flat band's huge DOS, "
                   "5->17 states/eV/cell). (2) GEOMETRY at that doped E_F survives: NN-kagome TB-fit metric integral I=2.855 ~= measured QGT 2.87 "
                   "(rigid-band; real doping can hybridize/spin-split -> caveat). (3) FILLING at E_F-on-band nu=0.507 -> nu(1-nu)=0.250 = the FAVOURABLE "
                   "half-filling D_s^geom maximum. VERDICT: geometry + filling SURVIVE (best case if reachable) but the doping to REACH E_F is EXTREME "
                   "-> the lead path is WEAKENED on ACCESSIBILITY, not on geometry. Live doped SCF (tot_charge=4) is delicate (high-DOS metal, slow under "
                   "MPI; prior tot_charge=2 MPI_ABORTed) -> no converged doped E_F, honest. soft d-phonon (Ω~22meV) is why a SINGLE host fails (H_001) "
                   "-> needs the +@ glue layer."),
    Candidate("Ni3In", "A", "kagome",
              g_mean=(2.854, "research-backup A-backup-1 (Ye 2021 arXiv:2106.10824): Ni-3d kagome flat band ~50meV near E_F "
                             "(a CORRELATED/DMFT position). OUR DFT (H_028): paramagnetic PBE QE7.2 MPI scf on the DO19 Ni3Sn-type "
                             "cell (P6_3/mmc, a=5.286/c=4.243A, Ni6In2 8-atom 134 e-, Ni 6h kagome net NN=a/2, In 2c; conv 1e-7, "
                             "E_F=16.5270eV) + Gamma-K-M-Gamma bands. NN-kagome TB-fit metric integral I=(1/2pi)int tr g d2k = 2.854 "
                             "~= CoSn's 2.855 ~= measured QGT 2.87 -> GEOMETRY LEVER MET (the kagome geometry is real and strong). "
                             "BUT the flat band sits -1.57eV BELOW E_F (band 56, W=0.255eV; whole narrow-d manifold -0.84 to -1.57eV) "
                             "-> ν=1.0 fully occupied -> ν(1-ν)=0 edge-suppressed -> NO superfluid lever without doping. g verified, "
                             "but flat-band-at-E_F (the dodge) FAILS in PBE", True),
              frustrated=(True, "kagome lattice (Ni 6h forms a kagome net, NN=a/2, same in-plane net as CoSn; confirmed in OUR DFT)", True),
              competing_order=("SDW", "OUR DFT (H_028): spin-polarized SCF is magnetically UNSTABLE across 3 recipes (accuracy "
                                      "oscillates 11-37 Ry, absolute magnetization swings 11-27 uB/cell with small net ~2 uB = frustrated "
                                      "large-local-moment kagome) -> a competing magnetic-order risk CoSn does not carry; "
                                      "literature reports NO static CDW but a correlated strange metal (Ye 2021 arXiv:2106.10824)", True),
              note="H_028 verdict: NOT a better layer-A than CoSn. Backup research (A-backup-1) named Ni3In as the kagome metal whose "
                   "flat band sits ~50meV NEAR E_F (Ye 2021) -- the natural dodge of H_027's CoSn extreme-doping wall. OUR REAL PBE DFT "
                   "does NOT confirm the dodge: the Ni-kagome flat-band manifold sits ~0.84-1.57eV BELOW E_F (paramagnetic PBE), AT LEAST "
                   "as deep as CoSn's (-0.44 near / -1.45 deep), so Ni3In needs the SAME-or-worse doping-to-E_F. Geometry lever is genuinely "
                   "MET (I=2.854~=CoSn 2.855~=QGT 2.87, kagome NN=a/2) but a geometry lever BELOW E_F is exactly CoSn's accessibility-limited "
                   "situation (H_027). Filling ν=1.0 at native E_F -> D_s edge-suppressed. WORSE than CoSn on a second axis: spin-pol SCF is "
                   "magnetically unstable (frustrated large-local-moment kagome, abs-mag 11-27uB) -> competing-order (H_014) risk CoSn lacks. "
                   "CAVEAT: the cited ~50meV near-E_F flat band is a CORRELATED feature; DMFT/+U/GW could pull it toward E_F -> this is a "
                   "PBE-level negative on the dodge, not a proof it can never be near-E_F. Lead A-layer stays CoSn; trio stays 🟠, absorbed=false."),
    Candidate("Nb3Cl8", "A", "breathing-kagome",
              g_mean=(2.11, "H_001 ledger / RTSC_LEDGER.jsonl", True),
              frustrated=(True, "breathing kagome", True),
              note="flat-band Mott candidate; geometry OK, coupling unverified."),
    Candidate("CsV3Sb5", "A", "kagome",
              g_mean=(None, "needs DFT ⟨g⟩", False),
              frustrated=(True, "kagome", True),
              competing_order=("CDW", "known CDW host (unverified for B-role)", False),
              note="kagome SC but a CDW competes (H_014 risk); ⟨g⟩ unverified."),
]
# Layer B — bosonic-glue hosts. Energies seeded UNVERIFIED until a research round sources them.
LAYER_B: list = [
    Candidate("Ta2NiSe5", "B", "excitonic-insulator",
              boson_meV=(300.0, "exciton gap 0.16-0.35 eV, onset ~325K — arXiv:2007.08212 (Kim 2020) / arXiv:2106.04396 (Matsubayashi 2021). "
                                "OUR DFT: the orthorhombic Cmcm parent SCF FROZE across 10 recipes (H_019+H_024; estimated scf accuracy byte-identical "
                                "iter-to-iter, e.g. 13.94569806=13.94569806) -> H_024 diagnosed high-symmetry excitonic-PARENT ill-conditioning. "
                                "H_025 TESTED the fix: built the EXPERIMENTAL low-T MONOCLINIC C2/c ground state (Sunshine&Ibers 1985 via arXiv:2201.07750; "
                                "vol 701.5A^3, 296 e-) and ran plain PBE AND PBE+U(Ni-3d=3eV). BOTH BREAK THE FREEZE: residual descends ~30x (17-18 Ry -> "
                                "0.45-0.64 Ry) with LIVE charge dynamics (every iter differs) -> the symmetry-breaking insight CONFIRMED. BUT both then "
                                "PLATEAU near-metallic (~0.5-0.9 Ry) and DO NOT reach conv_thr 1e-6 on the then-SERIAL QE build. H_026 ROOT-CAUSE-FIXED "
                                "the serial wall (rebuilt ~/qe_build QE7.2 WITH MPI in place: sudo apt libopenmpi-dev + configure --enable-parallel + make pw; "
                                "banner now 'Parallel version (MPI)', make.inc DFLAGS=-D__MPI, ldd links libmpi.so) and re-ran the monoclinic SCF under GENUINE "
                                "6-core MPI to MANY MORE iterations than the serial budget allowed. VERDICT (budget wall removed): across robust-PBE, PBE+U(Ni3d=3eV) "
                                "AND a higher-smearing(degauss0.03) variant the SCF descends ~30-38x then OSCILLATES PERSISTENTLY in the ~0.5-1.7 Ry near-metallic "
                                "plateau and NEVER reaches 1e-6 -> the plateau is PHYSICAL (PBE/PBE+U lack the many-body excitonic gap -> monoclinic Ta2NiSe5 is "
                                "near-metallic in PBE -> ill-conditioned SCF), NOT a compute artifact. Gap STILL UNRESOLVED-by-us, NOT fabricated; the only remaining "
                                "path is beyond-PBE (HSE/GW/many-body) which needs far more compute. Literature value kept, honestly flagged unverified-by-us.", True),
              competing_order=("none", "q=0 non-nesting excitonic order (the glue itself, not a pre-empting density wave); SC under pressure — arXiv:2106.04396", True),
              note="LEAD candidate (scout PR#10): exciton ~at the 349meV target, q=0 -> no pre-empting CDW/SDW. OUR DFT (H_019/H_024/H_025): Cmcm parent SCF "
                   "FROZE (10 recipes); H_025 showed the EXPERIMENTAL MONOCLINIC C2/c ground state BREAKS the freeze (~30x descent, both PBE & PBE+U) -> the "
                   "H_024 ill-conditioning diagnosis CONFIRMED & sharpened. H_026 FIXED the substrate (rebuilt QE7.2 WITH MPI in place; banner 'Parallel "
                   "version (MPI)') and re-ran under genuine 6-core MPI: with the serial budget wall removed, ALL THREE recipes (PBE/PBE+U/high-smear) descend "
                   "~30-38x then OSCILLATE in the near-metallic plateau without reaching 1e-6 -> the no-gap is PHYSICAL (PBE lacks the many-body excitonic gap), "
                   "an HONEST NEGATIVE on a PBE-DFT gap (not a budget artifact) -> gap NOT graduated to our-DFT (beyond-PBE only). H_024 BOUNDED the lead 🟢-path (H_023) D_s(N=2) lever from CoSn quantum "
                   "geometry instead (∫tr g I=2.86~=QGT 2.87 -> geometry SUPPORTS f_mult>=1.164 at N=2, conditional on doping+coherence, is_green=False). "
                   "Trio CoSn/hBN/Ta2NiSe5 jointly UNREALIZED -> 🟠, absorbed=false."),
    Candidate("1T-TiSe2", "B", "exciton-CDW",
              boson_meV=(None, "exciton-driven CDW scale — needs sourced value", False),
              competing_order=("CDW", "exciton condensation drives a CDW", False),
              note="competing-order intrinsic; classic exciton-CDW."),
]


def leaderboard() -> None:
    print("=== rtsc_candidates — +@ trilayer materials ledger + verifier (LIVING) ===")
    print(f"  targets: A ⟨g⟩>= {G_MIN} + frustrated · B bosonic mode in {GLUE_BAND_MEV} meV + no competing order")
    for role, reg in (("A (flat-band geometry)", LAYER_A), ("B (bosonic glue)", LAYER_B)):
        print(f"  -- Layer {role} --")
        for r in sorted((verify(c) for c in reg), key=lambda x: -x["n_pass"]):
            print(f"    [{r['n_pass']}/{r['n_total']}] {r['name']:10s} qualified={r['qualified']}")
            for g in r["gaps"]:
                print(f"            gap: {g}")
    a_ok = sum(1 for c in LAYER_A if verify(c)["qualified"])
    b_ok = sum(1 for c in LAYER_B if verify(c)["qualified"])
    print(f"  fully-verified: A={a_ok}/{len(LAYER_A)}  B={b_ok}/{len(LAYER_B)}")
    print("  -- verify_pair demo (best A x best B) --")
    p = verify_pair(LAYER_A[0], LAYER_B[0])
    print(f"    {p['pair']}: in_box={p['in_box']} bkt_Tc~{p['bkt_tc_K']}K A_ok={p['A_qualified']} B_ok={p['B_qualified']}")
    print("  VERDICT: 🟠 CREDIBLE-PARTIAL — a NAMED per-layer-verified candidate (CoSn/hBN/Ta2NiSe5) now")
    print("    clears the +@ box on paper (bkt_Tc~137K @ 2D coordinate, ~252K with the 3D lever H_006) —")
    print("    but the trio is JOINTLY UNREALIZED (never built/measured together) and bkt_Tc is a coordinate,")
    print("    NOT a prediction (H_018 scatter). absorbed=false / GATE_OPEN. The strongest 🟠, not 🟢.")


if __name__ == "__main__":
    leaderboard()
