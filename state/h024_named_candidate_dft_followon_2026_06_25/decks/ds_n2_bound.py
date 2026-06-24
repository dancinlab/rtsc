#!/usr/bin/env python3
"""
H_024 task 3: bound the multilayer superfluid weight D_s(N=2) of the lead 🟢-path
(H_023 demand-relaxation) from flat-band quantum geometry — the CHEAP route
(Peotta-Tormae geometric bound + Huhtinen 2022 minimal-metric correction), NOT the
intractable full N=2 stack SCF.

Question (H_023's single unknown): does the quantum-geometry evidence support
f_mult >= 1.164 at N=2 for THIS CoSn kagome flat band, or not?

Framework:
 - Peotta-Tormae (Nature Comm 2015, arXiv:1506.02815): in a flat band the conventional
   (intraband) superfluid weight vanishes; the GEOMETRIC contribution is
       D_s^geom = (4 e^2/hbar^2) * U * n(1-n) * <g>_min   (per flat band, 2D),
   i.e. D_s is LOWER-BOUNDED by the quantum metric integral; the bound is
       D_s >= (e^2/hbar^2) * (8/A_uc) * U * nu(1-nu) * B_min,
   where B_min = (1/2pi) int tr g d2k is the BZ metric integral and the inequality
   tr g >= |Berry curvature| ties it to a topological floor.
 - Huhtinen et al. 2022 (PRB 106, 014518, arXiv:2203.11133): the relevant quantity is
   the MINIMAL quantum metric g_min (after removing the part that can be gauged into
   trivial localisation); and for an N_flat-fold manifold over N_orb orbitals the
   effective per-layer geometric weight scales with N_flat/N_orb. For a multilayer
   stack of N copies, the geometric D_s is EXTENSIVE in N to leading order
   (D_s(N) ~ N * D_s(1)) when interlayer coherence is maintained -> f_mult(N) on the
   Tc lever.

We do NOT have a measured multilayer D_s. We test the WEAKER, falsifiable claim that
H_023 actually rests on: does the geometry give a per-layer D_s large enough that the
H_023 scaling models (sqrt(N) optimistic / N^0.25 conservative) reaching f_mult>=1.164
at N=2 is SUPPORTED by a non-vanishing, O(1) quantum-geometry lever for THIS band?

Inputs (honest):
  - G_int : dimensionless BZ metric integral I = (1/2pi) int tr g d2k for the CoSn
            kagome flat band, from kagome_metric.py (TB fit to OUR DFT).
  - g_qgt : measured QGT ledger value 2.87 (arXiv:2412.17809) for comparison.
  - position : flat band ~1.45 eV below E_F (OUR PBE) -> filling nu of the FLAT band
               is NOT near optimal nu=1/2 without heavy doping (logged risk).
"""
import sys, math

def main():
    # --- read the metric integral from kagome_metric output if passed, else placeholder ---
    G_int = float(sys.argv[1]) if len(sys.argv) > 1 else None
    g_norm = float(sys.argv[2]) if len(sys.argv) > 2 else None
    if G_int is None:
        print("usage: ds_n2_bound.py <I_metric_integral> <g_normalised>")
        return

    g_qgt = 2.87        # ledger measured QGT (arXiv:2412.17809)
    f_mult_req = 1.164  # H_023 required boost (=349.3/300)

    print("="*70)
    print("D_s(N=2) geometric bound — Peotta-Tormae + Huhtinen 2022 (CHEAP route)")
    print("="*70)
    print(f"flat-band metric integral  I = (1/2pi)int tr g d2k = {G_int:.4f}")
    print(f"normalised per-cell metric <tr g>/A_uc            = {g_norm:.4f}")
    print(f"ledger measured QGT value (arXiv:2412.17809)       g = {g_qgt:.3f}")

    # The geometric stability criterion (Peotta-Tormae): a non-vanishing D_s in a flat
    # band requires the quantum-metric integral to be NON-ZERO and O(1). The topological
    # floor is  I >= |C|  (Chern number); a trivial flat band still needs I>0 to superconduct.
    # "Does our DFT support g>=2?" -> compare the per-cell metric and I to 2.
    supports_g2 = (g_norm >= 2.0)
    print(f"\nQ2: does OUR DFT support g >= 2 ?  ->  {supports_g2}  "
          f"(<tr g>/A_uc = {g_norm:.3f} vs threshold 2.0; QGT measured = {g_qgt})")

    # --- multilayer f_mult from geometry ---
    # H_023 brackets f_mult(N) by sqrt(N) (optimistic, extensive Peotta-Tormae D_s) and
    # N^0.25 (conservative Josephson stack). BOTH require the SINGLE-LAYER geometric D_s to
    # be non-vanishing and the interlayer coherence to preserve the metric. The geometry
    # number does NOT change f_mult(N) (that is set by the stacking model); what it sets is
    # whether the lever EXISTS at all (D_s^geom > 0 and not parametrically tiny).
    N = 2
    f_sqrt = math.sqrt(N)
    f_quarter = N**0.25
    print(f"\nf_mult required (H_023)            = {f_mult_req:.4f}")
    print(f"f_mult(N=2) optimistic sqrt(N)     = {f_sqrt:.4f}   -> {'>=req' if f_sqrt>=f_mult_req else '<req'}")
    print(f"f_mult(N=2) conservative N^0.25    = {f_quarter:.4f}   -> {'>=req' if f_quarter>=f_mult_req else '<req'}")

    # The geometry GATE on whether those models are physically licensed:
    #  - lever exists  : I > 0 (metric non-trivial) AND the flat band is genuinely flat.
    #  - lever usable  : flat band reachable at E_F (filling nu ~ 1/2). OUR PBE puts it
    #                    ~1.45 eV BELOW E_F -> usable ONLY under heavy doping/gating.
    lever_exists = (G_int > 0.05)   # non-vanishing metric integral
    # honest verdict
    print("\n--- VERDICT on H_023's single unknown (geometry route) ---")
    if lever_exists and supports_g2:
        print("geometry lever EXISTS and is O(1)/strong (g>=2): the Peotta-Tormae")
        print("D_s^geom is non-vanishing, so f_mult(N=2)>=1.164 is SUPPORTED by both")
        print("scaling models -- CONDITIONAL on (a) doping the flat band to E_F and")
        print("(b) interlayer coherence preserving the metric. is_green stays False.")
        verdict = "SUPPORTED (conditional on doping + coherence)"
    elif lever_exists and not supports_g2:
        print("geometry lever EXISTS (I>0, non-trivial metric) but our DFT TB-fit metric")
        print(f"is BELOW the g>=2 mark (<tr g>/A_uc={g_norm:.2f}). The f_mult(N=2) models")
        print("are not REFUTED (they depend on stacking, not the absolute g), but the")
        print("absolute geometric weight is WEAKER than the measured QGT (2.87) implies,")
        print("so support is PARTIAL: lever present, magnitude under-shoots the QGT lever.")
        verdict = "PARTIAL (lever present; our-DFT g below QGT 2.87 and below 2.0)"
    else:
        print("geometry metric integral is ~0 (flat band trivial/quenched in our fit):")
        print("the Peotta-Tormae D_s^geom would VANISH -> f_mult(N=2) lever NOT supported.")
        verdict = "NOT SUPPORTED (geometric weight vanishes in our fit)"

    print(f"\nposition caveat: OUR PBE flat band ~1.45 eV below E_F -> nu far from 1/2;")
    print("D_s^geom ∝ nu(1-nu) is maximised at half-filling, so the UNDOPED band gives")
    print("a SMALL prefactor regardless of g. Reaching the geometric optimum needs the")
    print("logged heavy-doping/gating step (F2 of H_019 already FAILED on position).")
    print(f"\nVERDICT: {verdict}")
    print("is_green = False (no measured multilayer D_s; trio stays orange, absorbed=false)")

if __name__ == '__main__':
    main()
