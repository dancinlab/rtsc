#!/usr/bin/env python3
"""run_h_018 — ADVERSARIAL held-out calibration check of the campaign's CENTRAL Tc tool.

THE CLAIM UNDER TEST
--------------------
The whole RTSC flat-band campaign hangs its Tc map (and its room-T design box,
Omega ~ 643 meV for 293 K) on ONE estimator, the calibrated 2D-BKT band:

    Tc[K] = 0.11 * (Omega[meV] * 11.604) / 2.8        (campaign SSOT form)
          = 0.4559 * Omega[meV]

It was calibrated to exactly THREE in-sample anchors (MATBG, tMoTe2, Re6Se8Cl2).
A 3-point in-sample calibration that is then used to extrapolate ~50x in Omega (10-16
meV anchors -> 643 meV room-T demand) is a textbook over-fit risk. If the estimator
systematically fails on HELD-OUT real superconductors, the entire Tc map -- and every
room-T claim built on it -- is undermined.

WHAT THIS SCRIPT DOES (no fitting, no tune-to-green, no fabricated material values)
----------------------------------------------------------------------------------
1. Re-derive the 3 in-sample anchor predictions to fix the baseline scatter.
2. Apply the SAME frozen formula to HELD-OUT real flat-band / strong-coupling SCs,
   each with a PUBLISHED Tc and a citable characteristic coupling/boson scale Omega.
   Every Omega is a REAL, citable number with its source-type labelled (textbook
   phonon/Debye scale, measured boson energy, or bandwidth-derived). NONE is fitted.
3. Compute predicted Tc from Omega ALONE (the campaign simplified form drops g and
   U/Omega -> Tc is a pure function of Omega), form the ratio pred/measured, and ask:
     - is the held-out GEOMEAN error within the calibrated band (<= ~3x)?
     - is there a systematic over- or under-bias (sign of log-ratios)?
     - is the predictor MONOTONIC (higher Omega -> higher predicted Tc) -- trivially
       true for a linear law, kept as a registered sanity falsifier?
     - does the held-out scatter stay inside the in-sample scatter envelope, or does
       extrapolation blow the band open?

HONEST FRAMING (tier MODEL-PROBE, d6). This does NOT claim any material is/ isn't an
RTSC. It is an audit of a PREDICTOR. A held-out FAIL is a fully valid, useful negative
(it would down-rank the campaign's room-T extrapolation). Every helper is INLINE; we
deliberately do NOT import src/fbgeom_predictor.py (campaign idiom: avoid tool edits).

ON 'Omega' FOR NON-PHONON SUPERCONDUCTORS (a registered limitation, not a fudge)
--------------------------------------------------------------------------------
The campaign formula reads Omega as "the coupling/boson energy scale in meV". For
phonon SCs that is a Debye/characteristic-phonon energy; for moire/flat-band SCs the
campaign anchors used the flat-band bandwidth/interaction scale (~10-16 meV). To keep
the held-out test on the SAME footing as the calibration, each held-out Omega is the
analogous characteristic energy scale for that material, taken from PUBLISHED values,
with its nature stated. This cross-class heterogeneity is itself one of the honest
limits below -- it is exactly the ambiguity an over-extended single-knob estimator
hides, so surfacing it is part of the adversarial test.

stdout is pasted VERBATIM into the card. Run twice; bytes must be identical.
"""
import json
import math
import os

# ----------------------------------------------------------------------------- inline harness
class Falsifier:
    """Named predicate(metrics)->bool, TRUE when TRIGGERED (estimator refuted). PASS = not triggered."""
    def __init__(self, name, predicate, desc):
        self.name = name
        self.predicate = predicate
        self.desc = desc

def evaluate(metrics, falsifiers):
    results = []
    for f in falsifiers:
        trig = bool(f.predicate(metrics))
        results.append({"name": f.name, "triggered": trig,
                        "status": "FAIL" if trig else "PASS", "desc": f.desc})
    n_pass = sum(1 for r in results if not r["triggered"])
    return {"falsifiers": results, "n_pass": n_pass, "n_total": len(results),
            "all_pass": n_pass == len(results)}

# ----------------------------------------------------------------------------- the FROZEN central tool
KB = 11.604     # meV per K (1/0.08617)
DEFLATE = 2.8   # campaign deflate factor
SLOPE0 = 0.11   # campaign 2D-BKT prefactor
def tc_campaign(Omega_meV):
    """The campaign's CENTRAL Tc estimator, byte-for-byte the SSOT form. Tc[K]=0.11*(Om*11.604)/2.8."""
    return SLOPE0 * (Omega_meV * KB) / DEFLATE

# ----------------------------------------------------------------------------- IN-SAMPLE anchors (calibration)
# (name, Omega_meV, Tc_measured_K, source-note). These are the 3 the tool was calibrated to.
IN_SAMPLE = [
    ("MATBG",      16.0, 1.7,
     "magic-angle TBLG; Tc~1.7K [Cao Nature 2018]; Omega~flat-band scale 16meV [campaign anchor]"),
    ("tMoTe2",     10.0, 2.0,
     "twisted MoTe2 moire; Tc~1-3K (~2K) [Cai/Anderson Nature 2023 family]; Omega~10meV flat-band scale"),
    ("Re6Se8Cl2",  11.0, 8.0,
     "superatomic cluster SC; Tc~8K [Xie/Roy Nature 2024]; Omega~11meV cluster boson scale [campaign]"),
]

# ----------------------------------------------------------------------------- HELD-OUT anchors (the test)
# Each: (name, Omega_meV, Tc_measured_K, omega_kind, citation-note). Real, citable, NOT fitted.
# Omega is the published characteristic coupling/boson energy on the SAME footing as the calibration.
HELD_OUT = [
    # --- moire / flat-band family (closest class to the calibration anchors) ---
    ("tTLG (magic-angle trilayer graphene)", 30.0, 2.9, "flat-band/coupling scale",
     "Tc~2.9K [Park/Hao/Cao-Kim 2021, Nature/Science]; flat-band/Coulomb scale ~30meV (wider window than TBLG) [ARPES/transport-derived]"),
    ("Bilayer graphene (RTG, e-doped)", 12.0, 0.026, "flat-band scale",
     "rhombohedral trilayer/bilayer SC Tc~26mK [Zhou/Young 2021/2022 Nature]; flat-band scale ~12meV [transport]"),
    # --- kagome metal (flat-band-adjacent, charge-ordered) ---
    ("CsV3Sb5 (kagome)", 11.0, 2.5, "Debye/phonon scale",
     "Tc~2.5K [Ortiz PRL/PRM 2020]; characteristic phonon/Debye energy ~11meV (~130K Debye) [specific-heat/phonon refs]"),
    # --- classic strong-coupling phonon SCs (textbook lambda, Omega well-defined) ---
    ("MgB2", 67.0, 39.0, "phonon (E2g) scale",
     "Tc=39K [Nagamatsu Nature 2001]; dominant E2g phonon ~67meV (~540 cm-1) [neutron/Raman, textbook]"),
    ("Pb (lead)", 4.4, 7.2, "Debye phonon scale",
     "Tc=7.2K [textbook]; Debye energy ~k_B*105K~9meV, char. phonon peak ~4.4meV (transverse) [tunneling alpha2F, McMillan]"),
    ("Nb (niobium)", 23.7, 9.25, "Debye phonon scale",
     "Tc=9.25K [textbook]; Debye temp ~275K -> ~23.7meV [textbook Debye]"),
    ("K3C60 (fulleride)", 60.0, 19.0, "intramolecular phonon scale",
     "Tc~19K [Hebard/Rosseinsky Nature 1991]; coupling intramolecular Hg phonons ~60meV (~480 cm-1) [Raman/textbook]"),
    ("YBCO (cuprate, optimal)", 40.0, 92.0, "magnetic/phonon boson scale",
     "Tc=92K [Wu/Chu PRL 1987]; characteristic boson (spin-resonance/buckling phonon) ~40meV [INS resonance ~41meV]"),
]

def geomean(xs):
    return math.exp(sum(math.log(x) for x in xs) / len(xs))

def main():
    out = []
    P = out.append
    P("=" * 78)
    P("H_018 — ADVERSARIAL HELD-OUT CALIBRATION of the campaign CENTRAL Tc estimator")
    P("        Tc[K] = 0.11*(Omega[meV]*11.604)/2.8  =  %.4f * Omega[meV]" % (SLOPE0*KB/DEFLATE))
    P("        (campaign SSOT form; depends on Omega ALONE -- g and U/Omega dropped)")
    P("=" * 78)

    # ---- 1. in-sample baseline scatter ----
    P("\n[1] IN-SAMPLE anchors (the 3 the tool was calibrated to) -- baseline scatter")
    P("    %-12s %8s %8s %8s  %6s" % ("name", "Om(meV)", "pred(K)", "meas(K)", "ratio"))
    in_ratios = []
    for nm, Om, meas, _note in IN_SAMPLE:
        pred = tc_campaign(Om); r = pred / meas; in_ratios.append(r)
        P("    %-12s %8.1f %8.2f %8.2f  %6.2f" % (nm, Om, pred, meas, r))
    in_gm = geomean(in_ratios)
    in_lo, in_hi = min(in_ratios), max(in_ratios)
    P("    in-sample geomean ratio = %.2f   (band scatter %.2f .. %.2f x)" % (in_gm, in_lo, in_hi))

    # ---- 2. held-out application ----
    P("\n[2] HELD-OUT anchors (real published SCs, NOT used in calibration)")
    P("    %-40s %8s %8s %9s  %7s  %s" % ("name", "Om(meV)", "pred(K)", "meas(K)", "ratio", "Om-kind"))
    ho_ratios, ho_rows = [], []
    for nm, Om, meas, kind, _note in HELD_OUT:
        pred = tc_campaign(Om); r = pred / meas; ho_ratios.append(r)
        ho_rows.append((nm, Om, pred, meas, r))
        P("    %-40s %8.1f %8.2f %9.3f  %7.2f  %s" % (nm, Om, pred, meas, r, kind))

    n_ho = len(ho_ratios)
    ho_gm = geomean(ho_ratios)
    ho_lo, ho_hi = min(ho_ratios), max(ho_ratios)
    # bias = geomean of log-ratios (in dex); >0 over-predicts, <0 under-predicts
    log_ratios = [math.log10(r) for r in ho_ratios]
    bias_dex = sum(log_ratios) / len(log_ratios)
    # spread of held-out scatter (max/min ratio) vs in-sample spread
    ho_spread = ho_hi / ho_lo
    in_spread = in_hi / in_lo
    # monotonicity: sort held-out by Omega, check predicted Tc non-decreasing
    by_om = sorted(ho_rows, key=lambda t: t[1])
    mono = all(by_om[i][2] <= by_om[i+1][2] + 1e-12 for i in range(len(by_om)-1))
    # fraction of held-out within 3x (|log10 ratio| <= log10(3))
    within3 = sum(1 for r in ho_ratios if abs(math.log10(r)) <= math.log10(3.0))
    frac_within3 = within3 / n_ho

    P("\n[3] HELD-OUT statistics")
    P("    n held-out                 = %d" % n_ho)
    P("    held-out geomean ratio     = %.3f   (1.0 = perfect; >1 over-predicts)" % ho_gm)
    P("    held-out ratio band        = %.3f .. %.3f x" % (ho_lo, ho_hi))
    P("    held-out bias              = %+.3f dex  (geomean log10 pred/meas)" % bias_dex)
    P("    held-out scatter spread    = %.1fx   (in-sample spread = %.1fx)" % (ho_spread, in_spread))
    P("    within +-3x                = %d/%d (%.0f%%)" % (within3, n_ho, 100*frac_within3))
    P("    monotonic in Omega         = %s" % mono)

    metrics = {
        "n_held_out": n_ho,
        "ho_geomean_ratio": ho_gm,
        "ho_ratio_lo": ho_lo, "ho_ratio_hi": ho_hi,
        "ho_bias_dex": bias_dex,
        "ho_spread": ho_spread, "in_spread": in_spread,
        "frac_within_3x": frac_within3,
        "within_3x": within3,
        "monotonic": mono,
        "in_geomean_ratio": in_gm,
    }

    # ----------------------------------------------------------------- pre-registered falsifiers
    # Each predicate TRUE => TRIGGERED => estimator refuted on that axis. PASS = not triggered.
    falsifiers = [
        Falsifier(
            "F1_geomean_within_3x",
            lambda m: not (1.0/3.0 <= m["ho_geomean_ratio"] <= 3.0),
            "held-out geomean pred/meas must sit within the calibrated ~3x band [1/3, 3]"),
        Falsifier(
            "F2_no_systematic_bias",
            lambda m: abs(m["ho_bias_dex"]) > math.log10(3.0),
            "held-out bias must be < 0.477 dex (no systematic >3x over/under-prediction)"),
        Falsifier(
            "F3_majority_within_3x",
            lambda m: m["frac_within_3x"] < 0.5,
            "at least half of held-out anchors must individually land within +-3x"),
        Falsifier(
            "F4_scatter_not_blown_open",
            lambda m: m["ho_spread"] > 100.0,
            "held-out scatter spread must stay below 100x (estimator not effectively random)"),
        Falsifier(
            "F5_monotonic_in_Omega",
            lambda m: not m["monotonic"],
            "predicted Tc must be monotonic non-decreasing in Omega (sanity of the law)"),
    ]
    res = evaluate(metrics, falsifiers)

    P("\n" + "=" * 78)
    P("PRE-REGISTERED FALSIFIERS (PASS = not triggered = estimator survives that axis)")
    P("=" * 78)
    for r in res["falsifiers"]:
        P("  [%s] %-26s : %s" % (r["status"], r["name"], r["desc"]))
    P("\nfalsifiers_pass = %d/%d" % (res["n_pass"], res["n_total"]))

    # ----------------------------------------------------------------- verdict
    P("\n" + "=" * 78)
    P("VERDICT")
    P("=" * 78)
    if res["all_pass"]:
        verdict = "SURVIVED-HELDOUT"
        P("  The central estimator SURVIVES the held-out adversarial check:")
        P("  held-out geomean error %.2fx is within the calibrated ~3x band, no >3x" % ho_gm)
        P("  systematic bias, majority within 3x, scatter bounded, monotonic.")
        P("  -> The Tc map is NOT refuted by this test. BUT (see honest limits) this is")
        P("     a low-N, cross-class, interpolation-range check; it does NOT validate the")
        P("     ~50x extrapolation to the 643 meV room-T demand.")
    else:
        verdict = "REFUTED-HELDOUT"
        P("  The central estimator FAILS the held-out adversarial check on >=1 axis.")
        P("  -> The campaign Tc map and its room-T extrapolation are UNDERMINED; the")
        P("     estimator should be re-banded or down-weighted. This is a VALID honest")
        P("     negative (closed-negative for the 'predictor is held-out-valid' claim).")
    P("=" * 78)

    text = "\n".join(out)
    print(text)

    result = {
        "id": "H_018", "slug": "h018-predictor-calibration",
        "tier": "MODEL-PROBE", "domain": "rtsc",
        "verdict": verdict,
        "n_pass": res["n_pass"], "n_total": res["n_total"],
        "metrics": metrics,
        "falsifiers": [{"name": f["name"], "status": f["status"]} for f in res["falsifiers"]],
        "in_sample": [{"name": n, "Omega_meV": o, "Tc_meas_K": m} for n, o, m, _ in IN_SAMPLE],
        "held_out": [{"name": n, "Omega_meV": o, "Tc_meas_K": m, "omega_kind": k}
                     for n, o, m, k, _ in HELD_OUT],
    }
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "result.json"), "w") as fh:
        json.dump(result, fh, indent=2, sort_keys=True)
        fh.write("\n")

if __name__ == "__main__":
    main()
