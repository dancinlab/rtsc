#!/usr/bin/env python3
"""
BK-borophene real-DFT analysis: combine vc-relax + scf + bands + frozen-phonon -> the 4 numbers.
Compares real-DFT vs TB-est, runs the validated bond-bipolaron solver, emits the closed-negative verdict.
"""
import numpy as np, sys, os, json

RY2EV = 13.605693
HBAR  = 1.054571817e-34
AMU   = 1.66053907e-27
ME    = 9.1093837e-31
ECH   = 1.602176634e-19
KB    = 1.380649e-23
EV2J  = ECH

# ---- real-DFT inputs (from the summer QE 7.5 run) ----
BOND_DFT_A   = 1.7131       # relaxed kagome NN B-B bond (vc-relax)
A_DFT_A      = 3.4262       # relaxed in-plane lattice const
INTERLAYER_A = 2.0488       # relaxed bilayer spacing
PRESS_KBAR   = 0.05         # final stress ~ ambient (1 atm = 1e-3 kbar; ~0 GPa)
EF_EV        = -4.0969      # scf Fermi energy

# frozen-phonon A1g breathing E(u) curve (u = bond stretch in Angstrom)  -- FILLED from run
# E in Ry; the curve probes all 3 NN bonds of one kagome triangle stretched by u.
FP = {
  -0.06: None, -0.03: None, 0.00: None, 0.03: None, 0.06: None,
}

# kagome-active manifold single-band widths from bands.out (eV) -- DFT band structure
# (bands 7-11 near EF; widest dispersive ~3.2 eV)
KAGOME_BAND_WIDTHS = {7:3.074, 8:2.725, 9:2.727, 10:2.179, 11:3.245}
MANIFOLD_SPAN_EV   = 7.442   # bands 7-11 total span

def load_fp(energies):
    """energies: dict u->E_Ry"""
    for k in FP: FP[k] = energies.get(k)

def omega_from_fp():
    """harmonic Omega of the A1g triangle-breathing mode from E(u).
    Three bonds stretched by u; energy per the collective coordinate. We fit
    E(u) = E0 + 0.5*k*u^2 (u in meters along bond). The mode reduced mass:
    A1g breathing of an equilateral B3 triangle (each atom moves radially dr=u/sqrt3),
    effective mass for the bond-coordinate u ~ M_B (per-bond reduced mass ~ M_B/2 ... we
    take the SSH bond-stretch reduced mass mu = M_B/2 as in the TB pipeline). We report
    Omega_bond = sqrt(k_bond / mu) with k_bond = (1/3) d2E/du2 (3 bonds share the curvature).
    """
    us = np.array(sorted([u for u in FP if FP[u] is not None]))
    Es = np.array([FP[u] for u in us]) * RY2EV   # eV
    if len(us) < 3: return None
    # quadratic fit
    c = np.polyfit(us, Es, 2)   # c[0]*u^2 + ...
    d2E_du2_eV_per_A2 = 2*c[0]   # eV/A^2 ; this is for the COLLECTIVE u (all 3 bonds)
    # per-bond curvature: 3 bonds stretched simultaneously -> total curvature = 3*k_singlebond
    k_bond_eV_per_A2 = d2E_du2_eV_per_A2 / 3.0
    # convert to SI: J/m^2
    k_SI = k_bond_eV_per_A2 * EV2J / (1e-10**2)
    mu = 0.5 * 10.811 * AMU      # reduced mass of the 2-B bond
    omega_rad = np.sqrt(k_SI/mu)             # rad/s
    omega_eV  = HBAR*omega_rad/EV2J
    omega_meV = omega_eV*1000
    omega_cm  = omega_meV/0.123984
    return dict(fit=c.tolist(), d2E_du2_eV_per_A2=d2E_du2_eV_per_A2,
                k_bond_eV_per_A2=k_bond_eV_per_A2, Omega_meV=omega_meV, Omega_cm=omega_cm,
                us=us.tolist(), Es=Es.tolist())

def t_from_bandwidth():
    """real-DFT kagome NN hopping t from the dispersive bandwidth. For an ideal NN kagome
    3-band block the full block spans 6t; a single dispersive band spans ~ up to 4t-6t.
    Take t from the widest dispersive band W_single ~ 6t (conservative) and ~4t (upper)."""
    W_single = max(KAGOME_BAND_WIDTHS.values())
    return dict(W_single_eV=W_single, t_lo=W_single/6.0, t_hi=W_single/4.0,
                t_mid=W_single/5.0)

def g_over_t_structural():
    """g/t = 2*u0/d  (t-independent SSH coupling), with u0 = sqrt(hbar/(2*mu*Omega))."""
    return None  # filled in main with the DFT Omega

def main():
    out = {}
    out['geometry'] = dict(bond_A=BOND_DFT_A, a_A=A_DFT_A, interlayer_A=INTERLAYER_A,
                            press_kbar=PRESS_KBAR, EF_eV=EF_EV)
    # FP energies are injected via stdin json (u->E_Ry)
    fp_in = json.load(open(sys.argv[1])) if len(sys.argv)>1 else {}
    load_fp({float(k):v for k,v in fp_in.items()})
    om = omega_from_fp()
    out['frozen_phonon'] = om
    tt = t_from_bandwidth()
    out['hopping_t'] = tt

    if om:
        Omega_meV = om['Omega_meV']
        Omega_J = Omega_meV/1000*EV2J
        mu = 0.5*10.811*AMU
        u0_m = np.sqrt(HBAR/(2*mu*Omega_J/HBAR))   # u0 = sqrt(hbar/(2 mu omega)), omega=Omega_J/hbar
        # careful: omega_rad = Omega_J/HBAR
        omega_rad = Omega_J/HBAR
        u0_m = np.sqrt(HBAR/(2*mu*omega_rad))
        u0_A = u0_m*1e10
        d_A = BOND_DFT_A
        g_over_t = 2*u0_A/d_A
        out['g_over_t_structural'] = dict(u0_pm=u0_A*100, d_A=d_A, g_over_t=g_over_t,
            note="g/t = 2*u0/d is t-INDEPENDENT (Harrison: g_SSH=(2t/d)*u0, t cancels)")
        # absolute g_SSH for the solver (eV) = (2t/d)*u0, take t_mid
        t_mid = tt['t_mid']
        g_ssh_eV = (2*t_mid/d_A)*u0_A
        out['g_ssh_eV'] = g_ssh_eV
        # binding threshold from solver
        try:
            sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                            "..","..","..","..","state","fb-geom-lambda","bond-bipolaron"))
            import solver as bp
            Omega_t = (Omega_meV/1000.0)/t_mid
            U_t = 0.0   # neutral channel; U scanned separately. Use modest U/Omega=2 -> U_t
            U_over_Omega = 2.0
            U_t = U_over_Omega*(Omega_meV/1000.0)/t_mid
            scan=[]; thr=None
            for gt in [0.05,0.06,0.1,0.2,0.5,0.8,1.0,1.2,1.5,2.0]:
                r = bp.bipolaron(L=4, Nb=7, t=1.0, Omega=Omega_t, g=gt, coupling='ssh', U=U_t)
                scan.append((float(gt), float(r['binding'])))
                if r['binding']<0 and thr is None: thr=gt
            out['solver'] = dict(Omega_t=Omega_t, U_t=U_t, g_threshold_t=thr,
                                 g_realistic_t=g_over_t, binding_scan=scan,
                                 shortfall=(thr/g_over_t if (thr and g_over_t) else None),
                                 bound=bool(g_over_t>=thr) if thr else False)
        except Exception as e:
            out['solver']=dict(err=str(e))

    print(json.dumps(out, indent=2))
    json.dump(out, open(os.path.join(os.path.dirname(__file__),"dft_results.json"),"w"), indent=2)

if __name__=="__main__":
    main()
