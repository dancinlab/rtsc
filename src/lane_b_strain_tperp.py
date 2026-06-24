"""
LANE B — TB strain -> t_perp -> pairing-scale design-law for bilayer/trilayer nickelates.

Minimal tight-binding (TB) model of the Ni e_g manifold (d_x2y2 + d_z2) in:
  - bilayer  La3Ni2O7  (2 NiO2 planes coupled by apical-O-mediated t_perp on d_z2)
  - trilayer R4Ni3O10  (3 NiO2 planes, 2 apical bonds; inner layer doubly coupled)

Biaxial strain epsilon (in-plane, -4%..+2%) is applied by Harrison d^-n scaling of the
hoppings.  Compression (eps<0) shortens the in-plane Ni-O bond AND, via c-axis Poisson
relaxation, shortens the apical Ni-O-Ni distance -> raises the interlayer t_perp on d_z2.

We compute, vs epsilon:
  t_perp(eps), in-plane bandwidth W(eps), N(E_F)(eps), d_z2 bonding-antibonding splitting,
  and a pairing-scale proxy kTc ~ W * exp(-1/(N(E_F)*V)) with a t_perp-driven coupling V.

The optimum (max pairing scale) is mapped back to an in-plane lattice parameter -> substrate.

HONEST (d6): TB + Harrison is a TREND model, NOT DFT. Absolute Tc is NOT trustworthy; the
SHAPE (monotonic-in-compression, where it saturates) and the relative substrate ranking are
the deliverable. Numbers are anchored to published DFT TB params (arXiv 2502.01624) so the
trend is calibrated, but uncertainty is large (stated below).
"""
import numpy as np

# ---------------------------------------------------------------------------
# 1. ANCHOR PARAMETERS (published DFT/Wannier TB for La3Ni2O7), eV
#    Source anchors: Luo/Yang bilayer 2-orbital models + Bhatta 2502.01624 strain TB.
#    Unstrained (ambient bulk / thin-film I4/mmm-like) Ni e_g 2-orbital params:
# ---------------------------------------------------------------------------
# d_x2y2 NN in-plane hopping (the wide, metallic band)
t_x_0      = 0.483      # eV  (|t1^x| ~ 0.48-0.51 in the literature)
# d_z2 NN in-plane hopping (narrow in-plane)
t_z_0      = 0.110      # eV  (d_z2 in-plane is small, ~0.10-0.14)
# interlayer apical-O-mediated d_z2 hopping (the pairing-relevant sigma bond)
tperp_0    = 0.635      # eV  (t_perp^z ~ 0.6-0.65, the dominant interlayer term)
# interlayer d_x2y2 (very small, pi-like)
tperp_x_0  = 0.005      # eV  negligible
# crystal-field on-site splitting Delta = e(z2) - e(x2y2) at zero strain
Delta_0    = 0.367      # eV  (z2 sits below; bulk ~ -0.4..-0.3; magnitude ~0.37)
# Hund-renormalized pair coupling scale carried by interlayer d_z2 (proxy)
V_scale    = 0.42       # dimensionless prefactor folding J_H * (interlayer pair channel)

# ---------------------------------------------------------------------------
# 2. STRAIN -> BOND-LENGTH GEOMETRY
#    eps = in-plane biaxial strain (a/a0 - 1). c-axis responds by Poisson ratio.
#    In-plane Ni-O bond:  d_par/d_par0 = 1 + eps
#    Apical Ni-O (c-axis): d_ap/d_ap0  = 1 + eps_c,  eps_c = -2*nu/(1-nu) * eps  (biaxial)
#    For a perovskite-derived oxide nu ~ 0.30 -> eps_c = -0.857*eps.
#    Compression (eps<0) => eps_c>0? NO: biaxial in-plane compression EXPANDS c only if
#    Poisson; BUT in RP nickelates the experimentally observed c-axis response to in-plane
#    COMPRESSION is a c-axis CONTRACTION of the apical bond (octahedral rotation flattens,
#    straightening Ni-O-Ni toward 180 and SHORTENING the effective apical Ni-Ni hop path).
#    We model the EFFECTIVE apical hopping distance with an empirical contraction:
#       d_ap/d_ap0 = 1 + k_ap * eps,  k_ap ~ +0.55 (compression shortens apical path).
#    This sign is the published mechanism (compression -> straighter bond -> bigger t_perp).
# ---------------------------------------------------------------------------
NU      = 0.30
k_ap    = 0.55   # effective apical-path response to in-plane strain (compression shortens)

# Harrison exponents: sigma e_g-O-Ni superexchange-like hopping ~ d^-n
N_INPLANE = 3.5  # d_x2y2 in-plane (Harrison pd-sigma chained -> ~3-4)
N_ZIN     = 3.5  # d_z2 in-plane
N_APICAL  = 4.0  # apical d_z2 sigma is steeper (two pd-sigma + angle straightening)

def scale_hoppings(eps):
    d_par = 1.0 + eps
    d_ap  = 1.0 + k_ap*eps
    t_x   = t_x_0     * d_par**(-N_INPLANE)
    t_z   = t_z_0     * d_par**(-N_ZIN)
    tperp = tperp_0   * d_ap**(-N_APICAL)
    tperp_x = tperp_x_0 * d_ap**(-N_APICAL)
    # crystal field: compression flattens octahedron -> raises z2 relative to x2y2
    # (apical shortening pushes z2 up). Linear-in-eps model, calibrated to 2502.01624
    # which reports Delta grows ~50% at -2.5% strain => slope = 0.50/0.025 = 20 per unit eps.
    Delta = Delta_0 * (1.0 - 20.0*eps)   # eps<0 -> Delta larger (z2-x2y2 split grows)
    return t_x, t_z, tperp, tperp_x, Delta

# ---------------------------------------------------------------------------
# 3. TB HAMILTONIANS over the 2D BZ (k_perp folded into bilayer/trilayer blocks)
#    Orbital order per layer: [x2y2, z2]. Layers stacked.
# ---------------------------------------------------------------------------
def eps_x(k, t_x):   # d_x2y2 in-plane dispersion (2D square)
    kx, ky = k
    return -2*t_x*(np.cos(kx) + np.cos(ky))

def eps_z(k, t_z):   # d_z2 in-plane (weak)
    kx, ky = k
    return -2*t_z*(np.cos(kx) + np.cos(ky))

def H_bilayer(k, t_x, t_z, tperp, tperp_x, Delta, mu=0.0):
    """4x4: layers {1,2} x orbitals {x,z}."""
    ex = eps_x(k, t_x); ez = eps_z(k, t_z) - Delta
    H = np.zeros((4,4), complex)
    # layer1: x(0), z(1) ; layer2: x(2), z(3)
    H[0,0]=ex; H[1,1]=ez; H[2,2]=ex; H[3,3]=ez
    H[1,3]=H[3,1]=-tperp     # interlayer z-z (the pairing channel)
    H[0,2]=H[2,0]=-tperp_x   # interlayer x-x (tiny)
    return H - mu*np.eye(4)

def H_trilayer(k, t_x, t_z, tperp, tperp_x, Delta, mu=0.0):
    """6x6: layers {1,2,3} x {x,z}. Apical bonds 1-2 and 2-3 (inner layer doubly coupled)."""
    ex = eps_x(k, t_x); ez = eps_z(k, t_z) - Delta
    H = np.zeros((6,6), complex)
    for L in range(3):
        H[2*L,2*L]=ex; H[2*L+1,2*L+1]=ez
    # z-z apical 1-2 (rows 1,3) and 2-3 (rows 3,5)
    H[1,3]=H[3,1]=-tperp
    H[3,5]=H[5,3]=-tperp
    H[0,2]=H[2,0]=-tperp_x
    H[2,4]=H[4,2]=-tperp_x
    return H - mu*np.eye(6)

# ---------------------------------------------------------------------------
# 4. DOS / N(E_F) via tetrahedron-free Gaussian smearing on a dense k-grid,
#    with chemical potential set to the physical e_g filling.
#    La3Ni2O7: Ni^2.5+, d^7.5 => e_g filling = 1.5 e- per Ni per 2 e_g orbitals
#    => n_eg = 1.5 of 2 -> fill fraction 0.75 of the e_g manifold.
# ---------------------------------------------------------------------------
def bands(Hfun, eps, nk=64, mu=0.0):
    p = scale_hoppings(eps)
    bz = 2*np.pi*np.arange(nk)/nk
    nb = Hfun((0.0,0.0), *p, mu).shape[0]
    E = np.empty((nk*nk, nb))
    idx=0
    for kx in bz:
        for ky in bz:
            w = np.linalg.eigvalsh(Hfun((kx,ky), *p, mu))
            E[idx]=w; idx+=1
    return E, p

def fermi_level(E, fill_frac):
    """fill_frac = fraction of ALL states (n_orbitals*n_layers) filled."""
    flat = np.sort(E.ravel())
    nfill = int(round(fill_frac*flat.size))
    nfill = max(1, min(flat.size-1, nfill))
    return 0.5*(flat[nfill-1]+flat[nfill])

def dos_at(E, Ef, sigma=0.05, W=None):
    if W is None:
        x = (E.ravel()-Ef)/sigma
        g = np.exp(-0.5*x*x)/(sigma*np.sqrt(2*np.pi))
        return g.sum()/E.shape[0]
    # weighted DOS variant below uses projected weights
    raise RuntimeError

def dos_projected(Hfun, eps, p, Ef, orb_indices, nk, sigma=0.05):
    """Partial DOS at E_F projected onto a set of orbital indices (e.g. all d_z2)."""
    bz = 2*np.pi*np.arange(nk)/nk
    nb = Hfun((0.,0.), *p, 0.0).shape[0]
    acc = 0.0; nkpt = nk*nk
    for kx in bz:
        for ky in bz:
            w,v = np.linalg.eigh(Hfun((kx,ky), *p, 0.0))
            wt = np.sum(np.abs(v[orb_indices,:])**2, axis=0)   # z2 weight per band
            gx = np.exp(-0.5*((w-Ef)/sigma)**2)/(sigma*np.sqrt(2*np.pi))
            acc += np.dot(gx, wt)
    return acc/nkpt

# ---------------------------------------------------------------------------
# 5. PAIRING-SCALE PROXY  (physically-grounded, calibrated)
#    Mechanism (Yang/Lu/Zhang bilayer-dimer picture): interlayer pairing is driven
#    by the d_z2 super-exchange  J_perp = 4 t_perp^2 / U  acting on the dimer, with
#    the d_z2 partial DOS at E_F, N_z(E_F), setting the available pair phase space.
#    Weak-coupling McMillan-like form:
#        k_B Tc = PREF * omega0 * exp( -1 / (N_z(E_F) * J_perp) )
#    omega0 = an electronic pairing-glue scale (we use the in-plane d_x2y2 half-bandwidth
#    as the spin-fluctuation scale, ~0.5*W_x).  PREF folded into the anchor calibration.
#    CALIBRATION ANCHOR (d6): tuned so the LaAlO3 substrate point (eps=-1.30%) returns the
#    EXPERIMENTAL onset Tc ~ 48 K (Nature 2024 / Comm Phys 2025).  Then the relative
#    substrate ranking and the optimum-strain SHAPE are predictions, not the anchor.
# ---------------------------------------------------------------------------
U_HUB     = 3.0      # eV  Ni e_g Hubbard U (literature 3-4 eV)
ZZ_INDICES_BI  = [1,3]       # d_z2 rows in 4x4 bilayer
ZZ_INDICES_TRI = [1,3,5]     # d_z2 rows in 6x6 trilayer
PREF_CAL  = None     # set by calibration

def _raw_kTc(Hfun, eps, fill_frac, zz_idx, nk, pref):
    E, p = bands(Hfun, eps, nk)
    t_x,t_z,tperp,tperp_x,Delta = p
    W  = E.max()-E.min()
    Ef = fermi_level(E, fill_frac)
    Nz = dos_projected(Hfun, eps, p, Ef, zz_idx, nk)   # d_z2 partial DOS at E_F
    J_perp = 4.0*tperp**2/U_HUB                         # eV, interlayer super-exchange
    omega0 = 0.5*(2*max(t_x,1e-6)*4) * 0.0 + 0.5*W      # glue scale ~ 0.5 W
    lam = Nz * J_perp
    kTc = pref*omega0*np.exp(-1.0/lam) if lam>0 else 0.0
    return dict(eps=eps, t_x=t_x, t_z=t_z, tperp=tperp, Delta=Delta, W=W,
                Nz=Nz, J_perp=J_perp, omega0=omega0, lam=lam,
                kTc_eV=kTc, Tc_K=kTc/8.617e-5)

def calibrate(Hfun, fill_frac, zz_idx, eps_anchor, Tc_anchor_K, nk=48):
    r1 = _raw_kTc(Hfun, eps_anchor, fill_frac, zz_idx, nk, pref=1.0)
    if r1['kTc_eV']<=0: return 1.0
    target_eV = Tc_anchor_K*8.617e-5
    return target_eV/r1['kTc_eV']

def pairing_scale(Hfun, eps, fill_frac, nk=64, zz_idx=ZZ_INDICES_BI, pref=1.0):
    return _raw_kTc(Hfun, eps, fill_frac, zz_idx, nk, pref)

# ---------------------------------------------------------------------------
# 6. SUBSTRATE MAP
#    Bulk pseudo-cubic in-plane param of La3Ni2O7 ~ a0 = 3.84 A (sqrt2-reduced).
#    eps = a_sub/a0 - 1.  List real substrates by their pseudocubic a (A).
# ---------------------------------------------------------------------------
A0 = 3.84   # A, reference (bulk/relaxed) Ni-Ni in-plane spacing
SUBSTRATES = [
    ("LaAlO3 (LAO)",    3.79),
    ("SrLaAlO4 (SLAO)", 3.756),
    ("LSAT",            3.868),
    ("SrTiO3 (STO)",    3.905),
    ("NdGaO3 (NGO)",    3.86),
    ("(LaAlO3)-rich",   3.74),   # hypothetical stronger-compression target
    ("YAlO3 (YAO)",     3.71),   # very strong compression
]
def eps_of(a_sub): return a_sub/A0 - 1.0

# ---------------------------------------------------------------------------
# 7. RUN
# ---------------------------------------------------------------------------
def sweep(Hfun, fill_frac, label, zz_idx, pref, nk=48):
    print(f"\n=== {label}  (fill_frac={fill_frac:.3f}, pref={pref:.4g}) ===")
    print(f"{'eps%':>6} {'t_perp':>8} {'Delta':>7} {'W':>6} {'Nz(Ef)':>7} {'Jperp':>7} {'lam':>6} {'Tc_K':>8}")
    rows=[]
    for eps in np.linspace(-0.04, 0.02, 25):
        r = pairing_scale(Hfun, eps, fill_frac, nk, zz_idx, pref)
        rows.append(r)
        print(f"{eps*100:6.2f} {r['tperp']:8.4f} {r['Delta']:7.3f} {r['W']:6.3f} "
              f"{r['Nz']:7.3f} {r['J_perp']:7.4f} {r['lam']:6.3f} {r['Tc_K']:8.2f}")
    best = max(rows, key=lambda r:r['Tc_K'])
    print(f"  -> OPTIMUM: eps={best['eps']*100:.2f}%  t_perp={best['tperp']:.3f} eV  "
          f"Tc_proxy={best['Tc_K']:.1f} K  a_sub={A0*(1+best['eps']):.3f} A")
    return rows, best

if __name__ == "__main__":
    np.set_printoptions(suppress=True)
    fill_bi = 0.75
    fill_tri= 0.75
    # CALIBRATE bilayer to LaAlO3 anchor: eps=-1.30%, experimental onset Tc ~ 48 K
    eps_LAO = eps_of(3.79)
    pref_bi = calibrate(H_bilayer, fill_bi, ZZ_INDICES_BI, eps_LAO, 48.0)
    pref_tri= calibrate(H_trilayer,fill_tri,ZZ_INDICES_TRI, eps_LAO, 30.0)  # R4Ni3O10 ~30K anchor
    print(f"[calibration] bilayer pref={pref_bi:.4g} (LAO eps={eps_LAO*100:.2f}% -> 48 K)")
    print(f"[calibration] trilayer pref={pref_tri:.4g} (LAO eps={eps_LAO*100:.2f}% -> 30 K)")

    rb, bb = sweep(H_bilayer,  fill_bi,  "BILAYER La3Ni2O7  (Ni d7.5, e_g 75% filled)",
                   ZZ_INDICES_BI, pref_bi)
    rt, bt = sweep(H_trilayer, fill_tri, "TRILAYER R4Ni3O10 (Ni d7.33, e_g ~73% filled)",
                   ZZ_INDICES_TRI, pref_tri)

    print("\n=== SUBSTRATE RANKING (bilayer pairing proxy, calibrated to LAO=48K) ===")
    print(f"{'substrate':<18}{'a(A)':>7}{'eps%':>7}{'t_perp':>8}{'Nz':>7}{'Tc_proxy_K':>12}")
    sub_rows=[]
    for name,a in SUBSTRATES:
        eps=eps_of(a)
        r=pairing_scale(H_bilayer, eps, fill_bi, 48, ZZ_INDICES_BI, pref_bi)
        sub_rows.append((name,a,eps,r))
    for name,a,eps,r in sorted(sub_rows,key=lambda x:-x[3]['Tc_K']):
        print(f"{name:<18}{a:7.3f}{eps*100:7.2f}{r['tperp']:8.4f}{r['Nz']:7.3f}{r['Tc_K']:12.2f}")

    # closed-form design law fit: t_perp(eps) and Tc(eps) near optimum
    eps_arr=np.array([r['eps'] for r in rb]); tp=np.array([r['tperp'] for r in rb])
    # log-linear: ln t_perp = ln t0 - N_AP*ln(1+k_ap*eps); report effective slope at eps=0
    slope = (tp[13]-tp[11])/(eps_arr[13]-eps_arr[11])
    print(f"\n[design-law] d t_perp/d eps |_0 = {slope:.3f} eV per unit strain "
          f"= {slope*0.01:.4f} eV per 1% strain")
    print(f"[design-law] t_perp(eps) = {tperp_0:.3f}*(1+{k_ap}*eps)^(-{N_APICAL})  [Harrison]")
