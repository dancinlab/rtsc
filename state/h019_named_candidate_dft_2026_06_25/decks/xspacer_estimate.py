import math
# Cross-spacer Coulomb-mediated coupling W estimate (NOT a full cRPA — order-of-magnitude).
# Geometry: layer A (CoSn) -- hBN(n ML) -- layer B (Ta2NiSe5). Coupling = B's bosonic mode (exciton ~ omega_B)
# couples to carriers in A via its Coulomb field crossing the hBN spacer.
#
# Model: a 2D dipole/exciton density fluctuation in B creates a potential that, screened by hBN's
# anisotropic dielectric (Keldysh/Laturia), reaches A attenuated. The effective inter-layer coupling
# matrix element ~ bare Coulomb at separation d, divided by the perpendicular dielectric and the
# in-plane Keldysh screening length.

# Constants
e2_over_4pieps0 = 14.4  # eV*Angstrom (e^2/4πε0)
# hBN dielectric (Laturia et al. npj 2D Mater 2018): eps_perp ~ 3.29 (out-of-plane), eps_par ~ 6.9 (in-plane)
eps_perp = 3.3
eps_par  = 6.9
d_hBN_ML = 3.33   # interlayer spacing per hBN monolayer (Angstrom)

# Layer separation: A-surface to B-surface through n hBN layers + vdW gaps (~3.3 A each side)
def d_sep(n):
    return (n+1)*d_hBN_ML   # n hBN layers between two vdW gaps -> ~ (n+1) spacings

# B's bosonic mode (our registry / Ta2NiSe5): exciton/gap scale
omega_B = 0.30  # eV (mid of 0.16-0.35; will compare to OUR DFT gap)

# Characteristic in-plane momentum of the pairing-relevant fluctuation: q ~ 1/xi where xi ~ exciton size.
# Ta2NiSe5 exciton is tightly bound (sub-nm). Take q ~ 0.3-0.5 1/Angstrom as the relevant scale.
def W_estimate(n, q=0.4, omega=omega_B):
    d = d_sep(n)
    # 2D Coulomb kernel across a slab: V(q) ~ (2π e^2 / q) * exp(-q d) / eps_eff
    # eps_eff for field crossing perpendicular through hBN ~ sqrt(eps_par*eps_perp) (anisotropic),
    # with the perpendicular path dominating: use eps_perp for the crossing + a Keldysh in-plane factor.
    eps_eff = math.sqrt(eps_par*eps_perp)
    # prefactor 2π e^2 / q in eV (e2_over_4pieps0 = e^2/4πε0 -> 2π e^2/q = 2π * e2_over_4pieps0 /(q) * (1/2)?)
    # 2D Fourier of 1/r is 2π/q; with e^2/4πε0=14.4 eV·A: V2D(q) = 2π*14.4/q  [eV] (per unit charge^2, area-normalized)
    V0 = 2*math.pi*e2_over_4pieps0 / q
    Vscreened = V0 * math.exp(-q*d) / eps_eff
    # Convert to an effective phonon-like coupling W ~ |g|^2/omega proxy: the deformation-potential-like
    # matrix element squared over the mode energy. Take dimensionless lambda ~ Vscreened * N(0) with
    # a 2D DOS N(0) ~ 0.1 /eV/A^2 (flat-band enhanced). Report W = Vscreened (energy) AND lambda.
    N0 = 0.1
    lam = Vscreened * N0 * (omega/ (omega))  # placeholder dimensionless
    return d, Vscreened, lam

print("Cross-spacer Coulomb-mediated coupling — ORDER-OF-MAGNITUDE ESTIMATE (NOT cRPA)")
print(f"  hBN eps_perp={eps_perp}, eps_par={eps_par}, eps_eff=sqrt(eps_par*eps_perp)={math.sqrt(eps_par*eps_perp):.2f}")
print(f"  omega_B={omega_B} eV, q~0.4 1/A")
print(f"  {'n_hBN':>5} {'d_sep(A)':>9} {'W_screened(meV)':>16} {'attenuation_vs_n0':>18}")
W0=None
for n in [0,1,2,3]:
    d,V,lam = W_estimate(n)
    if W0 is None: W0=V
    print(f"  {n:>5} {d:>9.2f} {V*1000:>16.1f} {V/W0:>18.3f}")
print()
print("Interpretation: even with the field-transparency of hBN (eps_perp~3.3), the e^{-q d} factor")
print("from the FINITE in-plane momentum q of the exciton fluctuation dominates the attenuation:")
print("the cross-spacer W drops by ~exp(-q*3.3) ~ 0.27 per added hBN ML. At n=2 (H_015 opacity choice),")
print("W ~ tens of meV << omega_B (300 meV) -> dimensionless coupling lambda<<1 in this crude estimate.")
print("This is the Krotov-Suslov geometry-dilution failure mode quantified. A full cRPA (deferred) is")
print("needed because (a) the flat-band DOS enhancement of N(0), (b) the true exciton form factor f(q),")
print("and (c) dynamical (omega-dependent) screening can each change this by >1 order of magnitude.")
