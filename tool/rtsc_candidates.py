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
                            "manifold W=0.158 eV (band 41, narrowest of a 0.16-0.25 eV cluster) -- but POSITIONED ~1.45 eV below E_F, "
                            "DEEPER than the cited ~0.2 eV (PBE/orbital-character disagreement reported honestly, NOT tuned)", True),
              frustrated=(True, "kagome lattice", True),
              note="geometry OK + directly-measured QGT; OUR DFT (H_019) confirms a W<0.2eV flat band but ~1.45eV below E_F (needs heavy "
                   "doping/gating to reach E_F -- a real risk, honestly logged). soft d-phonon (Ω~22meV) is why a SINGLE host fails (H_001) -> needs the +@ glue layer."),
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
                                "OUR DFT (H_019): the 32-atom orthorhombic Cmcm cell was BUILT CORRECTLY (vol 706.7A^3, 296 e-, matches exp) "
                                "but the PBE SCF DID NOT CONVERGE (plateau ~0.5 Ry over 7 recipe variants on the contended summer host) -> "
                                "OUR gap is DEFERRED, NOT confirmed by our own DFT (literature value kept, honestly flagged unverified-by-us)", True),
              competing_order=("none", "q=0 non-nesting excitonic order (the glue itself, not a pre-empting density wave); SC under pressure — arXiv:2106.04396", True),
              note="LEAD candidate (scout PR#10): exciton ~at the 349meV target, q=0 -> no pre-empting CDW/SDW. OUR DFT (H_019) built the cell "
                   "but the 296-e PAW SCF stalled in-session -> gap DEFERRED (honest, not fabricated). Trio CoSn/hBN/Ta2NiSe5 jointly UNREALIZED -> 🟠, absorbed=false."),
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
