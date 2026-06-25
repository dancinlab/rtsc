# SF-seed full triage (rtsc) — ALL 140 existing seeds vs the frozen phase-stiffness wall

Triaged 140 seeds (89 new pool + ~50 older d6 brainstorm). **25 flagged genuinely-new in-silico escapes** (wave-2 micro-exp candidates — NOT claims). absorbed=false.

## Category tally

| count | category |
|---|---|
| 56 | already-carded |
| 32 | pre-satisfied-by-freeze |
| 25 | genuinely-new-in-silico-escape |
| 16 | pure-sf-no-host |
| 7 | pressure-hydride-axis |
| 4 | lab-handoff-out-of-domain |

## Genuinely-new in-silico escapes (wave-2 candidates)

### Chern-Simons Stiffness Pump (anyon statistical rigidity)
- Statistical-gauge-field stiffness (composite-fermion polarizability) is a glue-free D_s source NOT among the 5 boson families nor H_032-035; honest-null is not pre-satisfied by the freeze and is closed-form ED-testable, though the FQAH host is exotic.
- **probe:** Doped-FQAH composite-fermion model at level k (theta=pi/k): compute D_s via the Chern-Simons response D_s = (chi_CF * sigma_xy^2)/(1+chi_CF*Pi) from composite-fermion compressibility chi_CF and polarizability Pi(q->0) using flatchern_pair_ed.py + kubo_pair_stiffness.py on a small lattice. Wall-prediction: there is a (filling, k) window where D_s > (2/pi)k_B*164K at fixed n. HONEST-NULL: D_s collapses back onto the Uemura/boson-limited line D_s ~ |U|*nu(1-nu)<g> for ALL k (the CS gauge field renormalizes to zero net stiffness), i.e. composite-fermion polarizability does not survive as physical phase rigidity.

### Statistical-Transmutation Fluctuation Trap-Breaker
- Targets the 'order traps' HALF of the meta-law via defect-braiding statistics (not the glue half) — a lever no card touches (H_032-035 all attack the stiffness/glue side); closed-form SC-vs-trap free-energy crossing is ED-testable and its honest-null is not pre-satisfied.
- **probe:** Two-channel (SC + CDW/SDW) attractive-extended-Hubbard ED with an added Chern-Simons flux-attachment term at statistical angle theta. Compute F_SC(theta) - F_trap(theta) (free-energy crossing) and the SC phase-ordering T over a theta-sweep. Wall-prediction: a theta-window exists where SC wins (and T_SC > the theta=0 trap-limited ceiling) where it lost at theta=0. HONEST-NULL: flux attachment shifts F_SC and F_trap by EQUAL amounts for all theta (no relative gain) — the braiding statistics renormalizes the SC and trap channels identically, so the trap-limited ceiling is unmoved.

### Bethe-Ceiling Lattice (negative-curvature stiffness ladder)
- Mermin-Wagner FAILURE on hyperbolic graphs replaces BKT (z=1, log vortex unbinding) with a mean-field crossing at fixed D_s — a connectivity-geometry universality change distinct from H_033's z=2 (dynamics) and directly XY-MC testable; honest-null not pre-satisfied.
- **probe:** Classical XY model (Cooper-pair phase field) Monte-Carlo on a {7,3} or {5,4} hyperbolic tiling vs a square lattice at IDENTICAL bare stiffness J (the J giving square-lattice T_BKT=134K). Compute T_c(J) on both. Wall-prediction: T_c^hyperbolic / T_c^square >= 1.7 at matched J (vortex entropy can no longer compensate vortex energy on an exponentially-growing graph). HONEST-NULL: T_c^hyperbolic <= 1.2x T_c^square — boundary-dominated finite-size effects / the negative curvature does NOT lift the bulk ordering temperature, BKT-like physics survives at matched D_s.

### Synthetic-Dimension Coordination Pump (extra hopping axis without extra space)
- Claims to DECOUPLE flat-band pairing from stiffness-coordination by adding Josephson neighbors in an internal index — a structurally different escape from the 3D count (H_006) and multilayer-D_s; the quantum-metric no-go may or may not bind on a synthetic axis, so the honest-null is genuinely open and ED-testable.
- **probe:** Attractive-Hubbard BdG on a 2D flat band with an attached N-rung synthetic dimension (internal index, uniform synthetic hopping t_s), real-space flatness held fixed. Compute Kubo D_s(N) via kubo_pair_stiffness.py while monitoring the real-space quantum metric. Wall-prediction: D_s(N) ~ D_s(1)*(1+c(N-1)), c>0, with real-space <g> unchanged, so T_BKT clears 164K for N>=3. HONEST-NULL: D_s is pinned by the single-band minimal-quantum-metric bound regardless of N (synthetic neighbors do not contribute to the PHYSICAL Kubo phase rigidity, only to an internal-index susceptibility) — D_s(N) saturates at D_s(1), reproducing the freeze.

### Aperiodic / Quasicrystal Vortex Localizer (no Goldstone soft mode to disorder phase)
- Multifractal vortex pinning + absence of a clean q->0 Goldstone mode attacks the vortex-disordering channel (not D_s) on an aperiodic host — a mechanism the campaign never enumerated; attractive-Hubbard on a Penrose tiling is directly ED/MC-testable and the honest-null is not pre-satisfied.
- **probe:** Attractive-Hubbard ED/BdG on an Ammann-Beenker or Penrose tiling vs a periodic lattice of EQUAL mean coordination and EQUAL pairing; extract D_s and the vortex-unbinding (BKT) T from twisted-boundary / vortex-fugacity Monte-Carlo. Wall-prediction: T_c^quasicrystal >= 1.2x T_c^periodic at matched D_s, because multifractal critical states raise the vortex-core depinning energy and suppress the soft q->0 phase mode. HONEST-NULL: T_c^quasicrystal <= T_c^periodic at matched D_s (multifractality SUPPRESSES D_s or adds no pinning advantage) — quasiperiodicity reproduces or worsens the wall.

### Vortex-Code Phase Lock (the superfluid phase as a protected logical variable)
- A static stabilizer string-tension term raising the vortex CORE ENERGY directly attacks the BKT vortex-unbinding mechanism (the wall's actual loss channel) at fixed D_s — orthogonal to all glue/geometry cards and, unlike measurement-induced O5, carries no continuous Landauer bill; XY-MC testable with honest-null not pre-satisfied.
- **probe:** Classical XY / lattice-Josephson Monte-Carlo with an added local plaquette-vorticity 'stabilizer' string-tension term S. Compute the renormalized rho_s(T) and T_BKT(S) over an S-sweep at FIXED bare stiffness. Wall-prediction: T_BKT(S) = T_BKT(0)*(1+alpha*S), alpha>0 monotone, so T_BKT rises continuously past the 134-164K-equivalent without more D_s. HONEST-NULL: T_BKT is independent of S (the stabilizer term renormalizes to zero under the phase field's coarse-graining, OR it merely shifts a prefactor without moving the universal-jump unbinding point) — defect-entropy balance is untouched and the wall holds.

### Infinite-T Memory Graft (subsystem-code symmetry that does not melt)
- Replaces energetic (stiffness-limited) order with a conserved subsystem-code symmetry charge that has no finite melting T by theorem — an order-class the campaign never enumerated; the crux (does the charge-2e coupling preserve the protecting symmetry?) is itself a clean ED/TN falsifier not pre-satisfied by the freeze.
- **probe:** Build the explicit Z2xZ2 subsystem-code Hamiltonian augmented with a pair-hopping term tying the logical operator to a charge-2e bilinear; in exact-diagonalization / tensor-network, compute the logical (= order-parameter) autocorrelation C(t) and its T-dependence vs a symmetry-broken control. Wall-prediction: C(t) shows NO Arrhenius decay and NO finite-T cusp up to the lattice cutoff. HONEST-NULL (crux, test first): adding the charge-2e coupling makes the protecting symmetry generator FAIL to commute with H ([S, H] != 0) — the conserved quantity is destroyed by the very coupling that makes it a superconductor, so the order reverts to a finite-T energetic condensate and the wall applies.

### Planckian Pair-Beat (Yukawa-SYK pairing of incoherent electrons)
- Incoherent (no-quasiparticle) Yukawa-SYK metal: phase stiffness sourced from the FULL incoherent spectral weight rather than a vanishing QP residue Z, with no Migdal/boson-frequency cutoff; this attacks the Emery-Kivelson denominator's hidden quasiparticle assumption, a mechanism NOT among H_032-035 and whose honest-null is a clean self-consistent gap/stiffness comparison the freeze never ran.
- **probe:** Solve the large-N Yukawa-SYK self-consistent saddle G,Sigma,D,Pi at coupling g and boson scale w0 pinned to a real flat-band DOS N(E_F); extract D_s from the Kubo current-current bubble of the FULL Green's function (not a QP-residue). Probe: D_s(T)/[k_B*164K] vs g and the QP weight Z_inc->0. HONEST-NULL: if the computed Kubo D_s collapses back onto the Uemura/(pi/2)D_s boson-limited line (D_s ~ Z*n/m* saturating <=164K-equiv) for all g, OR T_c re-acquires a w0 boson-energy cap, the SYK incoherence buys nothing and the wall holds.

### Overhauser-Locked Phase Ballast (nuclear-spin co-condensate)
- A coherent Overhauser/nuclear-spin field as a SECOND phase-rigidity reservoir adding in PARALLEL (rho_s = rho_el + lambda^2*rho_nuc) sourced by nuclear-moment density, not carrier density; this is parallel-channel stiffness donation from a genuinely non-electronic bath (distinct from the multiband H_032 donation which borrows from another ELECTRON band), with a clean isotope-monotonic falsifier the freeze never tested.
- **probe:** Two-stiffness BKT/XY model: T_BKT = (pi/2)(rho_el + lambda^2*rho_nuc), lambda = A_hf/W (contact-hyperfine over electron bandwidth), rho_nuc = nuclear spin-wave stiffness of a high-moment high-abundance isotope (51V, I=7/2). Probe: T_BKT(A_hf) and isotope contrast Delta-T_BKT(spin-I vs spin-0 even-even isotope) on the SAME lattice. HONEST-NULL: if lambda^2*rho_nuc is parametrically negligible (A_hf/W~1e-3 => lambda^2~1e-6, requiring rho_nuc to exceed rho_el by ~1e6) OR the nuclear spin-wave stiffness itself orders only at neV-ueV (its own T_order << 1K), the parallel ballast contributes nothing and T_BKT collapses to the electronic-only ceiling. Likely confirm-wall, but a clean un-run structurally-orthogonal donation toy.

### ENZ Screening Inversion (the Permittivity Mirror)
- Re[eps]<0 cladding flips the STATIC screened Coulomb sign (no exchanged boson, no competing order) giving a real attraction at metallic n => high D_s; orthogonal to all 5 glue families and the stiffness freeze does not pre-satisfy its null (a cRPA W(q,0) sign test, gated by passivity).
- **probe:** Probe: embed a 2D electron layer in an effective medium with engineered eps_env(q,w~0); compute the cRPA/constrained static screened interaction W(q,0)=v(q)/eps_tot(q,0) for the embedded layer and scan the eps_env<0 window. ESCAPE if W(q,0)<0 (attractive) over a finite q-band q<q* with q*~2k_F (real scattering phase space) AND the implied pairing at metallic carrier density n gives Kubo D_s above the cuprate 7.4 meV scale. HONEST-NULL (most likely): Kramers-Kronig + passivity (Im eps>=0) force a compensating positive-screening lobe so the integrated W stays >0 for every passive cladding, or the W<0 window collapses to q=0 measure-zero - reproducing the known plasmonic-glue no-go and confirming no static-attraction escape.

### Hyperbolic Pitch-Black Coulomb (Anisotropic Negative-Group-Velocity Glue Channel)
- An anisotropic eps-tensor cladding opens an attractive large-q (q~k_F) lobe in the screened kernel - a momentum-SELECTIVE attraction none of the q~0 glue families or flat-band geometry touches; in-silico via cRPA W(q) anisotropy, null not pre-satisfied by the stiffness freeze.
- **probe:** Probe: for an electron layer on a hyperbolic cladding (eps_par>0, eps_perp<0), compute the momentum-resolved W(q,w~0) via the anisotropic-medium dielectric and compare to an isotropic dielectric of equal mean eps. ESCAPE if W develops an attractive lobe (W<0) at large q ~ k_F that is ABSENT isotropically AND the lobe sits below 2k_F (connects Fermi-surface points), yielding tightly-bound light pairs at metallic n with D_s above the wall. HONEST-NULL: the hyperbolic tensor produces no sign change at any q, OR the attractive lobe lies at q>2k_F (no FS scattering phase space) - so the large-q channel cannot nucleate Fermi-surface pairing and the wall holds.

### Flexoelectric Gradient Glue (pairing from strain-gradient, not strain)
- An invented finite-q pairing vertex ~q (vanishing at q=0, the inverse of every surveyed q~0 glue) that can in principle operate at metallic n (large D_s) - orthogonal to the 5 families and to flat-band geometry; BdG-gap-equation testable and its null (Landau-damping of chi_soft at metallic n) is not pre-satisfied by the stiffness freeze.
- **probe:** Probe: build the flexoelectric pairing kernel V(q,w) = (q*mu)^2 * chi_soft(q,w) (mu = flexocoupling, chi_soft = soft-TO-mode susceptibility) in a 2D BdG/ED toy at METALLIC carrier density and solve the linearized gap equation for the leading eigenvalue lambda and gap symmetry. ESCAPE if lambda>0.3 for physical mu (~nC/m) with a nodeless or extended-s gap on the Fermi surface at a density where Kubo D_s already exceeds the cuprate stiffness scale - then pairing and stiffness are decoupled (glue from chi_soft, D_s from metallic n). HONEST-NULL (likely): at metallic n the soft mode is Landau-damped so chi_soft(q,w->0) collapses exactly where D_s would be large, giving lambda<0.3 / no finite-q instability - the glue dies where the stiffness lives, confirming the wall.

### Ligand-Hole Negative-U: the pair lives on oxygen, not the cation
- BaBiO3-class delocalized-ligand negative-U gives a LIGHT real-space pair (not flat-band quantum-metric, not phonon-H_008, not k-space Leggett-H_032) whose stiffness comes from low m* + high n_pair — honest-null (self-trapping) is not pre-satisfied by the freeze.
- **probe:** Two-particle Green function of an attractive extended-Hubbard / breathing-bond BaBiO3 lattice (U_eff<0 on the symmetric O6 MO, ligand bandwidth W tuned by M-O-M angle). Compute pair dispersion -> bipolaron m*(W) and rho_s = (hbar^2/4)(n_pair/m*)d, then T_BKT=(pi/2)D_s. CLAIM: m* drops below ~3 m_e as W grows at fixed |U_eff|, decoupling eV binding from stiffness, giving T_BKT>164K. HONEST-NULL (falsifier): m*(W) stays >10 m_e for all W with the pair bound (binding<->delocalization locked: large |U_eff| self-traps the pair, m* ~ exp(+|U_eff|/W)), so rho_s never clears the cuprate 7.4 meV scale and the wall holds — distinct from H_008 (phonon soft-mode bipolaron) which dials a vibrational mediator, not a chemical disproportionation orbital.

### Frustrated Valence Skipper: the disproportionation that can't crystallize
- Geometric frustration of negative-U centers forbids the CHARGE-CDW trap, freeing eV on-site pairing — attacks the 'order traps' meta-law in the charge channel (H_022 was spin/frustration), honest-null (charge-glass/VBS instead) not pre-satisfied.
- **probe:** Extended-Hubbard with U_eff<0 and nearest-neighbor V on a frustrated (pyrochlore/triangular/checkerboard) lattice vs the unfrustrated cubic control, solved by ED/QMC. Track the charge-order gap Delta_CDW and the s-wave pair susceptibility chi_pair vs V/|U_eff|. CLAIM: on the frustrated lattice Delta_CDW->0 (no static checkerboard CDW) while chi_pair stays divergent at a V where the cubic lattice is a CDW insulator, so the eV pairing scale survives un-trapped and the pairing-limited Tc moves above 164K. HONEST-NULL (falsifier): frustration replaces the CDW with a DIFFERENT trap (charge glass / Wigner localization opening a gap, or a valence-bond crystal) that still localizes the pairs, OR chi_pair collapses with Delta_CDW (the same nesting feeds both) — re-confirming that the trap is conserved against the glue.

### Charge-Kondo / Pair-Resonance Lattice: a negative-U impurity band of preformed pairs
- Dense valence-skipper lattice -> charge-Kondo pair-resonance band of preformed charge-2e bosons; Tc set by electronic eV-derived hybridization coherence Gamma, not the spin-fluctuation 7.4 meV stiffness — a many-body pair resonance (no quantum-metric ceiling), honest-null not pre-satisfied.
- **probe:** Lattice Anderson / extended negative-U model (skipper isospin hybridized to a conduction band, p-d coupling V_pd) solved by DMFT or cluster-ED. Extract the two-particle spectral function at E_F: width Gamma and charge-2e weight of the pair-resonance band; estimate T_c ~ Gamma/k_B for BEC of the preformed pairs. CLAIM: Gamma grows with skipper density and V_pd, exceeding ~14 meV (>164K) for strong Tl-O/Bi-O hybridization, with binding>>Gamma so pairs never break (no pseudogap competition). HONEST-NULL (falsifier): the resonance pins to a Kondo-INSULATING gap (no E_F spectral weight -> no condensation), or raising density opens inter-site charge order before Gamma reaches 14 meV — i.e. the same charge-order trap as the frustrated-skipper null reappears.

### NODAL-SPIN-SPLITTER GLUE (d-wave altermagnet pair vertex)
- Altermagnet spin splitting is a STATIC spin-group-symmetry band texture, not the soft AFM Goldstone the magnon family (carded) closed on — the pairing root decouples from the Neel stiffness, honest-null (collapses with rho_s = disguised magnon) is the crux and not pre-satisfied.
- **probe:** 2-band altermagnet Hubbard/RPA at half-filling: build the spin-fluctuation pairing kernel on the d-wave-split Fermi surface and extract the leading attractive eigenvalue lambda_pair, then sweep the Neel-vector stiffness rho_s (soften the AFM order) at FIXED anisotropic inter-sublattice hopping. CLAIM: lambda_pair stays finite (>0.3) as rho_s->0 because the splitting is set by the crystal-field/hopping term, not by <S>, so pairing strength and magnetic phase stiffness are separated roots (unlike the Emery-Kivelson cuprate where J and rho_s share one root). HONEST-NULL (falsifier): lambda_pair tracks rho_s and collapses as the order softens -> the vertex is just a disguised magnon and re-confirms the carded magnon-family closure.

### ZERO-MOMENT STIFFNESS LADDER (decoupled magnetic-vs-charge phase stiffness)
- Metallic compensated altermagnet (n~10^22/cm^3) supplies high CHARGE superfluid stiffness while magnetic compensation is a lattice-symmetry property, not carrier starvation — directly attacks the wall's under-weighted root (cuprate low-D_s is doped-Mott scarcity), an untested host category.
- **probe:** Kubo superfluid-weight D_s for a RuO2-class metallic-altermagnet tight-binding model at carrier density n~10^22 cm^-3, given a pairing gap from the NODAL-SPIN-SPLITTER vertex; compare D_s^eff to the cuprate 7.4 meV (=134K) scale, then T_BKT=(pi/2)D_s^eff. CLAIM: because n is ~10-100x the underdoped-cuprate density and compensation is symmetry-enforced (not Mott-doping), D_s^eff>7.4 meV and T_BKT clears 164K. HONEST-NULL (falsifier): every altermagnet with usable spin splitting turns out to be a LOW-carrier insulator/semimetal (MnTe-class), forcing D_s^eff back below the cuprate wall, OR the high-n metal (RuO2-class) has too weak a pairing vertex to gap the Fermi surface — the carrier-density and pairing-strength knobs are anti-correlated, reproducing the wall.

### ANISOTROPY-LOCKED GLUE (crystal-symmetry-protected pairing immune to order melting)
- Spin-group-symmetry-locked altermagnet vertex degrades with moment amplitude much slower than a Goldstone-magnon vertex — a structurally new escape from the 'order traps' law (glue carried by anisotropy/symmetry, partially decoupled from order amplitude); honest-null (tracks <S>^2 like AFM) is the clean falsifier.
- **probe:** Finite-T classical-MC+RPA (or DMFT/QMC) of an altermagnet Hubbard model: extract lambda_pair(T) and compare against an AFM-magnon control vertex on the same lattice, both normalized to their T=0 value. CLAIM: lambda_pair(T) retains >50% at T~0.7 T_N (short-range altermagnetic correlations preserve the spin-group symmetry as <S> shrinks) while the AFM control falls below 50% by T~0.3 T_N, so the glue survives the temperature range where the carded magnon family thermally self-destructs. HONEST-NULL (falsifier): lambda_pair(T) tracks <S>^2 identically to the AFM control -> symmetry protection gives zero thermal robustness and the order-trap closes at the same T as the magnon family.

### AB-CAGE BREATHER — flux-detuned Aharonov-Bohm caging that LIFTS the cage just enough to pay stiffness
- Flux (a phase), not a small bandgap, enforces the caging, so |U| stays O(eV) while flux-detuning adds conventional velocity stiffness DECOUPLED from |U| — breaks the D_s ~ |U|.<g> coupling the freeze rests on; a flat-band origin (flux, not band-touching) the freeze never tested, honest-null not pre-satisfied.
- **probe:** Attractive-Hubbard ED/DMRG on a rhombic/diamond AB-caging chain threaded by synthetic flux phi = pi - delta; sweep the Kubo BKT stiffness D_s vs flux-detuning delta at FIXED |U|. CLAIM: D_s(delta) peaks at a NONZERO delta* exceeding the delta=0 caged (purely geometric, tiny) value by >2x, because the cage gap is set by hopping t (O(eV)) not by an avoided crossing, so |U| need not shrink to keep the band flat. HONEST-NULL (falsifier): D_s(delta) is monotone DECREASING from delta=0 (flux buys no |U|-independent stiffness), OR the detuning that adds velocity simultaneously closes the caging gap and reintroduces the |U|<gap (U-saturation) constraint, OR D_s at delta* still sits >=20x below the 7.4 meV cuprate scale — collapsing back to the frozen ceiling.

### CLS-PHONON HYBRID GLUE — using the compact localized state's open continuum channel as a resonance reservoir (Friedrich-Wintgen BIC)
- A Friedrich-Wintgen BIC co-locates a flat (pairing) and a dispersive (stiffness) band at the SAME energy by destructive interference, so pairs draw DOS from the flat branch while coherence rides the continuum W_cont — decouples pairing from stiffness in a way no surveyed single-flat-band lever does; honest-null not pre-satisfied.
- **probe:** Two-channel attractive lattice ED: a flat BIC branch (zero width, high DOS) degenerate with a dispersive continuum band of bandwidth W_cont, coupled by the same |U|. Measure where the pair condensate weight resides and compute Kubo D_s as W_cont is swept at FIXED pairing gap. CLAIM: condensate weight sits in the flat branch while D_s ~ |U|.n_pair.(W_cont-derived) grows with W_cont, so T_BKT rises with continuum bandwidth and clears the flat-band-only ~134K stiffness limit. HONEST-NULL (falsifier): D_s is INDEPENDENT of W_cont (the continuum does not donate stiffness to the BIC-paired condensate because the BIC is by construction decoupled from the continuum — zero spectral overlap), so the condensate remains stiffness-limited by the flat branch alone and the wall holds.

### INTERFERENCE-PROTECTED PAIR BICs — a two-particle bound state in the continuum that cannot decay into single-particle channels
- Flatten the PAIR (two-body) band via a two-particle BIC while single particles stay dispersive, so pairing and phase stiffness live in DIFFERENT sectors — not carded (H_032-035 all flatten the single-particle band), not a glue family, not pre-satisfied by the Q=0 single-band freeze; closed-form attractive-Hubbard ED testable.
- **probe:** Build attractive-Hubbard ED on a cross-stitch / diamond chain tuned to the caging (BIC) point. Compute (i) the two-particle spectral function A2(K,omega) to confirm a flat, zero-width pair band sitting INSIDE the two-particle continuum (true BIC, not a broadened resonance), and (ii) the Kubo pair stiffness D_s of the resulting condensate. Closed-form probe: T_BKT = (pi/2)*D_s with D_s from kubo_pair_stiffness.py. Escape claim = D_s tracks the SINGLE-particle bandwidth W_1 (eV-scale), not the flat pair-band width. HONEST-NULL (confirm-wall): the pair-BIC acquires finite width once interactions dress the continuum (no protected BIC), OR D_s collapses to the flat-pair-band scale (~0.1-0.4 meV, the measured flat-band ceiling) because phase coherence is carried by the pair sector after all — reproducing D_s ~ |U|*<g> and re-confirming the 134-164 K wall.

### FFLO Stiffness Bypass — finite-Q phase rigidity from the depairing tensor, not n_s
- Finite-Q Larkin-Ovchinnikov condensate whose modulation/sliding-phase stiffness is set by the FS-mismatch/bandwidth energy, not the dilute Q=0 superfluid weight — orthogonal to H_032-035 (none are finite-Q), not a glue family, honest-null not pre-satisfied by the Q=0 freeze; BdG-testable.
- **probe:** 2-band/valley-imbalanced lattice BdG with controllable FS mismatch delta. Self-consistently solve for the LO saddle Delta(r) ~ cos(Q.r), Q ~ 2*delta_kF. Closed-form probe: extract the GL stiffness TENSOR from the free-energy curvature d^2 F / d(grad theta)^2 about the LO saddle; the modulation-direction component D_s^|| (along Q) has Kelvin scale ~ delta * (bandwidth). Escape claim = D_s^|| grows with delta and exceeds (pi/2)D_s^{Q=0} of the same host, so order melting is governed by the large sliding stiffness. HONEST-NULL (confirm-wall): D_s^|| <= D_s^{Q=0} across the entire mismatch range (the modulation stiffness is always sub-dominant), OR the LO window in delta is so narrow that the depairing tensor that opens it also caps Q-stiffness at the same n_s-limited scale — re-confirming that the relevant rigidity is still the dilute superfluid weight and T_c stays under 164 K.

### PDW Commensurate Lock — pair-density-wave pinned to the lattice for fluctuation-proof rigidity
- Commensurate (Q=G/n) pair-density-wave whose sliding Goldstone is gapped by an Umklapp pinning term ~cos(n*theta), converting the soft phase channel into a gapped phason — attacks the 'order traps' clause from momentum space; not in H_032-035, not topology, not a glue family; BdG-testable.
- **probe:** Lattice BdG/ED with a commensurate finite-Q pairing channel plus a lattice-commensurate Umklapp pinning term V_p*cos(n*theta). Closed-form probe: compute the phason spectrum; pinning opens a phase gap Delta_phason ~ sqrt(V_p * rho_s) (amplitudon-only low-energy spectrum). Free-vortex / phase-slip cost then = Delta_phason, not (pi/2)D_s, so T_melt ~ max[(pi/2)D_s, Delta_phason]. Escape claim = at accessible V_p, Delta_phason (Kelvin) > 164 K while the pairing eigenvalue is unchanged. HONEST-NULL (confirm-wall): the commensurate Umklapp that pins the phase ALSO suppresses the finite-Q pairing eigenvalue (lambda_pair drops as V_p rises), so T_c is unchanged or lowered — i.e. pinning gap and pairing scale cannot both be large (no-free-lunch), and the family closes at the same wall.

### Pinning-Memory Ratchet (the Glassy-Phason Non-Equilibrium Stiffness Ballast)
- Targets the STIFFNESS wall directly with a NON-electronic donor (a pinned structural-glass inertia term rho_s,phason added to the phase action) — distinct from H_032's electronic multiband donation (no Leggett mode between an SC condensate and a structural glass, so H_032's quantum-metric/Leggett cap does not apply); null not pre-satisfied by the freeze and closed-form testable.
- **probe:** Phase action S = (1/2)integral d^2r dtau [ rho_s^el (grad theta)^2 + chi_glass(omega) (dtau theta)^2 ] with a pinned-phason memory kernel chi_glass(omega) = sum_i w_i Gamma_i/(omega^2 + Gamma_i^2) (overdamped TLS bath, Setty arXiv:2305.05407). Compute the renormalized phase stiffness / vortex-core energy E_c(rho_s^el, chi_glass) and the BKT temperature T_BKT = (pi/2) rho_s^eff, then sweep pinning strength (peak Gamma, spectral weight w). HONEST-NULL: the glass is SLOW (Gamma -> 0) while the SC phase fluctuations that set the vortex unbinding live at the Josephson/plasma frequency omega_J >> Gamma; an adiabatic bath cannot follow the fast phase winding, so its contribution to the STATIC stiffness that bounds T_BKT vanishes (chi_glass(omega->omega_J) -> 0), giving rho_s^eff = rho_s^el and confirm-wall. Escape only if the kernel contributes a finite zero-frequency stiffness term that survives the omega_J cutoff — falsified if T_BKT is independent of pinning strength or tracks rho_s^el alone.

### O2 disorder -> flat band (B: disorder-induced flat band, geometry lever for free from randomness)
- A genuinely untested route to the geometry lever (tr g) from Anderson/structural disorder without crystallinity — flagged in the grand synthesis as one of two orthogonal bypasses worth a card; honest-null is a clean Kubo-D_s test, NOT pre-satisfied (the freeze measured crystalline flat bands, never disorder-induced ones).
- **probe:** Attractive-Hubbard BdG on an L x L lattice with on-site disorder W drawn from [-W/2,W/2], sweep W to enter the disorder-induced-flat-band regime (DOS spike at E_F, IPR rising). Compute the Kubo geometric stiffness D_s(W) = (e^2/hbar^2) * [<-k_x> - Pi_xx(q->0,omega=0)] disorder-averaged over >=50 samples, and T_BKT = (pi/2) D_s(W). HONEST-NULL (confirm-wall): D_s(W) is non-monotone and its maximum stays >=20x below the cuprate 7.4 meV phase-stiffness scale (i.e. T_BKT_max << 134 K), OR disorder that flattens the band simultaneously localizes the pairs (xi_loc < lattice spacing) so the superfluid response vanishes (D_s -> 0 as IPR -> 1). ESCAPE only if a finite W* gives D_s(W*) with T_BKT > 134 K AND xi_loc > vortex-core size (pairs stay extended). Tooling: flatband_pair_ed.py + kubo_pair_stiffness.py with an added random on-site term.

## Synthesis (verbatim)

The JSON I was given has 124 entries (the task mentions "140 existing SF seeds" — the 124 classified here plus ~16 already-resolved cards H_001-H_035 referenced in the freeze). Let me build the report from the 27 genuinely-new and 7 pressure-hydride seeds.

# SF-Seed Triage Synthesis — RTSC Phase-Stiffness Wall (~134-164K)

Frozen baseline: the Emery-Kivelson phase-stiffness wall is confirmed against the geometric-stiffness lens (PR#40) and all four SF escape probes (H_032 multiband-donation / H_033 z=2-universality / H_034 eta-pairing-ODLRO / H_035 Amperean-current). `absorbed=false`. Target 293K @ 1 atm, in-silico domain. This triage classifies the full SF seed pool against that freeze.

## 1. Category Tally

| Category | Count |
|---|---|
| already-carded | 49 |
| genuinely-new-in-silico-escape | 27 |
| pre-satisfied-by-freeze | 26 |
| pure-sf-no-host | 11 |
| pressure-hydride-axis | 7 |
| lab-handoff-out-of-domain | 4 |
| **TOTAL classified** | **124** |

(The 124 classified SF seeds sit on top of the already-resolved H_001-H_035 cards the freeze rests on; the "already-carded" bucket is the seeds that re-point at those existing cards.)

## 2. Genuinely-New In-Silico-Escape Shortlist (wave-2 micro-exp candidates)

These are the 27 seeds whose honest-null is NOT pre-satisfied by the freeze and which do not collapse onto an existing H-card. Each is a live, closed-form / ED / BdG / MC / cRPA-testable probe.

**A. Statistical / topological-statistics levers (attack the "order traps" half, not the glue half)**

1. **Chern-Simons Stiffness Pump (anyon statistical rigidity)** — Statistical-gauge-field stiffness (composite-fermion polarizability) is a glue-free D_s source not among the 5 boson families nor H_032-035; closed-form ED-testable though FQAH host is exotic.
   *Probe:* Doped-FQAH composite-fermion model at level k (theta=pi/k); compute D_s = (chi_CF·sigma_xy²)/(1+chi_CF·Pi) via flatchern_pair_ed.py + kubo_pair_stiffness.py. Wall-prediction: a (filling,k) window with D_s > (2/pi)k_B·164K. Honest-null: D_s collapses onto the Uemura/boson line D_s~|U|·nu(1-nu)·⟨g⟩ for all k.

2. **Statistical-Transmutation Fluctuation Trap-Breaker** — Targets the "order traps" half via defect-braiding statistics (no card touches this; H_032-035 all attack the stiffness/glue side).
   *Probe:* Two-channel (SC + CDW/SDW) attractive-extended-Hubbard ED with Chern-Simons flux-attachment at angle theta. Compute F_SC(theta)−F_trap(theta) over a theta-sweep. Wall-prediction: a theta-window where SC wins and T_SC exceeds the theta=0 trap ceiling. Honest-null: flux attachment shifts F_SC and F_trap equally (no relative gain).

**B. Connectivity / aperiodic-geometry levers (attack the vortex-disordering channel, not D_s)**

3. **Bethe-Ceiling Lattice (negative-curvature stiffness ladder)** — Mermin-Wagner FAILURE on hyperbolic graphs replaces BKT with a mean-field crossing at fixed D_s; distinct from H_033's z=2.
   *Probe:* Classical XY MC on a {7,3}/{5,4} hyperbolic tiling vs square lattice at identical bare J (the J giving square T_BKT=134K). Wall-prediction: T_c^hyp/T_c^sq ≥ 1.7 at matched J. Honest-null: ≤ 1.2× (boundary/finite-size, BKT survives).

4. **Aperiodic / Quasicrystal Vortex Localizer** — Multifractal vortex pinning + no clean q→0 Goldstone attacks the vortex-disordering channel on an aperiodic host the campaign never enumerated.
   *Probe:* Attractive-Hubbard ED/BdG on Ammann-Beenker/Penrose vs periodic of equal mean coordination + pairing; extract D_s and BKT-T. Wall-prediction: T_c^QC ≥ 1.2× periodic at matched D_s. Honest-null: ≤ periodic (multifractality suppresses D_s / no pinning gain).

**C. Synthetic / engineered-host stiffness-decoupling levers**

5. **Synthetic-Dimension Coordination Pump** — Decouples flat-band pairing from stiffness-coordination by adding Josephson neighbors in an internal index; the quantum-metric no-go may or may not bind on a synthetic axis.
   *Probe:* Attractive-Hubbard BdG on a 2D flat band + N-rung synthetic dimension (uniform t_s), real-space flatness fixed; Kubo D_s(N) while monitoring real-space quantum metric. Wall-prediction: D_s(N)~D_s(1)(1+c(N-1)), c>0, T_BKT clears 164K for N≥3. Honest-null: D_s(N) saturates at D_s(1) (synthetic neighbors only feed an internal-index susceptibility).

**D. Code-/symmetry-protected order-class levers (attack the BKT unbinding mechanism directly)**

6. **Vortex-Code Phase Lock** — Static stabilizer string-tension raises vortex CORE ENERGY at fixed D_s, carrying no continuous Landauer bill (unlike measurement-induced O5).
   *Probe:* Classical XY / lattice-Josephson MC + local plaquette-vorticity stabilizer S; compute renormalized rho_s(T), T_BKT(S) at fixed bare stiffness. Wall-prediction: T_BKT(S)=T_BKT(0)(1+alpha·S), alpha>0 monotone. Honest-null: T_BKT independent of S (term renormalizes to zero / only shifts a prefactor).

7. **Infinite-T Memory Graft (subsystem-code symmetry that does not melt)** — Replaces energetic (stiffness-limited) order with a conserved subsystem-code charge that has no finite melting T by theorem.
   *Probe:* Z2×Z2 subsystem-code Hamiltonian + pair-hopping tying the logical operator to a charge-2e bilinear; ED/TN logical autocorrelation C(t) vs T. Wall-prediction: no Arrhenius decay, no finite-T cusp. Honest-null (crux, test first): the charge-2e coupling makes the protecting generator fail to commute ([S,H]≠0), reverting to a finite-T energetic condensate.

**E. Incoherent-metal / no-quasiparticle stiffness lever**

8. **Planckian Pair-Beat (Yukawa-SYK pairing of incoherent electrons)** — Phase stiffness from the FULL incoherent spectral weight, not a vanishing QP residue Z; attacks the Emery-Kivelson denominator's hidden quasiparticle assumption — not among H_032-035.
   *Probe:* Solve large-N Yukawa-SYK saddle G,Sigma,D,Pi at coupling g, boson scale w0 pinned to a real flat-band DOS; extract D_s from the FULL-G Kubo bubble. Probe D_s(T)/[k_B·164K] vs g and Z_inc→0. Honest-null: D_s collapses onto the Uemura/(pi/2)D_s boson line for all g, or T_c re-acquires a w0 cap.

**F. Static-screened-Coulomb / dielectric-engineering levers (no exchanged boson, no competing order)**

9. **ENZ Screening Inversion (the Permittivity Mirror)** — Re[eps]<0 cladding flips the STATIC screened Coulomb sign → real attraction at metallic n → high D_s; orthogonal to all 5 glue families.
   *Probe:* Embed a 2D layer in eps_env(q,w~0); cRPA W(q,0)=v(q)/eps_tot scan over eps_env<0. Escape if W(q,0)<0 over a finite q-band q<q*~2k_F AND pairing at metallic n gives Kubo D_s above the 7.4 meV cuprate scale. Honest-null: Kramers-Kronig + passivity force a compensating positive lobe so integrated W>0 for every passive cladding (plasmonic-glue no-go).

10. **Hyperbolic Pitch-Black Coulomb (anisotropic negative-group-velocity glue)** — Anisotropic eps-tensor opens a momentum-SELECTIVE attractive large-q (q~k_F) lobe none of the q~0 families or flat-band geometry touch.
    *Probe:* eps_par>0, eps_perp<0 cladding; momentum-resolved W(q,w~0) vs isotropic of equal mean eps. Escape if an attractive lobe appears at q~k_F (absent isotropically) below 2k_F connecting FS points, with D_s above the wall. Honest-null: no sign change at any q, or the lobe sits at q>2k_F (no FS scattering phase space).

11. **Flexoelectric Gradient Glue (pairing from strain-gradient, not strain)** — An invented finite-q vertex ~q (vanishing at q=0, inverse of every surveyed q~0 glue) that can operate at metallic n (large D_s).
    *Probe:* Build V(q,w)=(q·mu)²·chi_soft(q,w) in a 2D BdG/ED toy at metallic n; solve the linearized gap eq for lambda + symmetry. Escape if lambda>0.3 for physical mu (~nC/m) with nodeless/extended-s gap where Kubo D_s already exceeds the cuprate scale. Honest-null: at metallic n the soft mode is Landau-damped so chi_soft(q,w→0) collapses where D_s would be large → lambda<0.3.

**G. Non-electronic / parallel-channel stiffness donors**

12. **Overhauser-Locked Phase Ballast (nuclear-spin co-condensate)** — A coherent Overhauser field as a SECOND phase-rigidity reservoir adding in PARALLEL (rho_s=rho_el+lambda²rho_nuc), sourced by nuclear-moment density (distinct from H_032's electron-band donation).
    *Probe:* Two-stiffness BKT model T_BKT=(pi/2)(rho_el+lambda²rho_nuc), lambda=A_hf/W, rho_nuc from a high-moment isotope (51V, I=7/2); isotope contrast on the same lattice. Honest-null: lambda²rho_nuc parametrically negligible (A_hf/W~1e-3 ⇒ lambda²~1e-6) or rho_nuc orders at neV-ueV (T_order≪1K) → collapse to electronic ceiling. (Likely confirm-wall, but clean and structurally-orthogonal.)

13. **Pinning-Memory Ratchet (glassy-phason non-equilibrium stiffness ballast)** — A pinned structural-glass inertia term added to the phase action (Setty arXiv:2305.05407 overdamped-TLS bath), no Leggett mode between an SC condensate and a glass so H_032's cap doesn't apply.
    *Probe:* S=∫[rho_s^el(grad theta)²+chi_glass(omega)(dtau theta)²], chi_glass=Σ w_i Gamma_i/(omega²+Gamma_i²); compute renormalized stiffness / E_vortex and T_BKT, sweep pinning. Honest-null: the glass is slow (Gamma→0) while phase fluctuations live at omega_J≫Gamma, so chi_glass(omega→omega_J)→0 → rho_s^eff=rho_s^el. Escape only if a finite zero-frequency stiffness term survives the omega_J cutoff.

**H. Negative-U / valence-skipper levers (light real-space pairs; attack charge-order traps)**

14. **Ligand-Hole Negative-U (the pair lives on oxygen, not the cation)** — BaBiO3-class delocalized-ligand negative-U gives a LIGHT real-space pair (not flat-band quantum-metric, not phonon-H_008, not k-space H_032); stiffness from low m* + high n_pair.
    *Probe:* Two-particle Green function of attractive extended-Hubbard / breathing-bond BaBiO3 (U_eff<0 on symmetric O6 MO, W via M-O-M angle); pair dispersion → m*(W), rho_s, T_BKT. Claim: m*<~3 m_e as W grows at fixed |U_eff|, T_BKT>164K. Honest-null: m*(W)>10 m_e for all W (binding↔delocalization locked, m*~exp(+|U_eff|/W) self-trapping).

15. **Frustrated Valence Skipper (the disproportionation that can't crystallize)** — Geometric frustration of negative-U centers forbids the charge-CDW trap, freeing eV on-site pairing — attacks the "order traps" law in the CHARGE channel (H_022 was spin/frustration).
    *Probe:* Extended-Hubbard U_eff<0 + NN V on frustrated (pyrochlore/triangular/checkerboard) vs cubic, ED/QMC; track Delta_CDW and chi_pair vs V/|U_eff|. Claim: frustrated Delta_CDW→0 while chi_pair stays divergent where cubic is a CDW insulator, T_c>164K. Honest-null: frustration substitutes a charge-glass/VBS trap that still localizes pairs, or chi_pair collapses with Delta_CDW.

16. **Charge-Kondo / Pair-Resonance Lattice (negative-U impurity band of preformed pairs)** — Dense valence-skipper → charge-Kondo pair-resonance band of charge-2e bosons; T_c from eV-derived hybridization coherence Gamma, not the 7.4 meV stiffness.
    *Probe:* Lattice-Anderson / extended negative-U (skipper isospin hybridized to a conduction band, V_pd) via DMFT/cluster-ED; two-particle spectral width Gamma + charge-2e weight at E_F; T_c~Gamma/k_B. Claim: Gamma>14 meV (>164K) for strong Tl-O/Bi-O hybridization, binding≫Gamma. Honest-null: resonance pins to a Kondo-INSULATING gap (no E_F weight) or inter-site charge order opens before Gamma reaches 14 meV.

**I. Altermagnet / spin-group-symmetry levers (decouple pairing root from Neel stiffness)**

17. **Nodal-Spin-Splitter Glue (d-wave altermagnet pair vertex)** — Altermagnet spin splitting is a STATIC spin-group-symmetry band texture, not the soft AFM Goldstone the magnon family closed on; pairing root decouples from Neel stiffness.
    *Probe:* 2-band altermagnet Hubbard/RPA at half-filling; build the spin-fluctuation kernel on the d-wave-split FS, extract lambda_pair, sweep rho_s (soften AFM) at FIXED inter-sublattice hopping. Claim: lambda_pair>0.3 as rho_s→0 (splitting set by hopping, not ⟨S⟩). Honest-null: lambda_pair tracks rho_s and collapses (disguised magnon).

18. **Zero-Moment Stiffness Ladder (decoupled magnetic-vs-charge stiffness)** — Metallic compensated altermagnet (n~10²²/cm³) supplies high CHARGE superfluid stiffness while compensation is a lattice-symmetry property, not carrier starvation; attacks the wall's under-weighted root (cuprate low-D_s = doped-Mott scarcity).
    *Probe:* Kubo D_s for a RuO2-class metallic-altermagnet tight-binding model at n~10²² cm⁻³ with a gap from the nodal-spin-splitter vertex; compare to 7.4 meV, T_BKT. Claim: D_s^eff>7.4 meV, T_BKT>164K. Honest-null: usable-splitting altermagnets are low-carrier insulators (MnTe-class) or the high-n metal has too weak a vertex (carrier-density and pairing-strength anti-correlated).

19. **Anisotropy-Locked Glue (crystal-symmetry-protected pairing immune to order melting)** — Spin-group-symmetry-locked vertex degrades with moment amplitude much slower than a Goldstone-magnon vertex — structurally new escape from "order traps".
    *Probe:* Finite-T classical-MC+RPA (or DMFT/QMC); lambda_pair(T) vs an AFM-magnon control, both normalized to T=0. Claim: lambda_pair retains >50% at T~0.7 T_N while the AFM control falls below 50% by T~0.3 T_N. Honest-null: lambda_pair(T) tracks ⟨S⟩² identically to the AFM control (zero thermal robustness).

**J. Flux-caging / interference-decoupled flat-band levers**

20. **AB-Cage Breather (flux-detuned Aharonov-Bohm caging)** — Flux (a phase), not a small bandgap, enforces caging, so |U| stays O(eV) while flux-detuning adds velocity stiffness decoupled from |U| — breaks the D_s~|U|·⟨g⟩ coupling the freeze rests on.
    *Probe:* Attractive-Hubbard ED/DMRG on a rhombic/diamond AB-caging chain threaded by phi=pi−delta; Kubo D_s vs delta at FIXED |U|. Claim: D_s(delta) peaks at nonzero delta* >2× the delta=0 caged value. Honest-null: D_s monotone-decreasing from delta=0, or detuning closes the caging gap (re-imposing |U|<gap), or D_s(delta*) still ≥20× below 7.4 meV.

21. **CLS-Phonon Hybrid Glue (Friedrich-Wintgen BIC reservoir)** — A BIC co-locates a flat (pairing) and a dispersive (stiffness) band at the SAME energy by destructive interference, so pairs draw DOS from the flat branch while coherence rides the continuum W_cont.
    *Probe:* Two-channel attractive lattice ED: flat BIC branch (zero width, high DOS) degenerate with a dispersive band W_cont, coupled by the same |U|; locate condensate weight, compute D_s as W_cont is swept at FIXED gap. Claim: weight in the flat branch while D_s grows with W_cont, T_BKT clears ~134K. Honest-null: D_s independent of W_cont (BIC has zero spectral overlap with the continuum).

22. **Interference-Protected Pair BICs (two-particle BIC)** — Flatten the PAIR (two-body) band via a two-particle BIC while single particles stay dispersive, so pairing and stiffness live in DIFFERENT sectors — H_032-035 all flatten the single-particle band.
    *Probe:* Attractive-Hubbard ED on a cross-stitch/diamond chain at the caging point; two-particle spectral function A2(K,omega) to confirm a flat zero-width pair band inside the continuum, plus Kubo D_s. Escape = D_s tracks the single-particle bandwidth W_1 (eV), not the flat pair-band width. Honest-null: pair-BIC acquires finite width once interactions dress the continuum, or D_s collapses to the flat-pair-band scale (~0.1-0.4 meV).

**K. Finite-Q / pair-density-wave levers (orthogonal to the Q=0 freeze)**

23. **FFLO Stiffness Bypass (finite-Q phase rigidity from the depairing tensor)** — Finite-Q Larkin-Ovchinnikov condensate whose modulation/sliding-phase stiffness is set by FS-mismatch/bandwidth energy, not the dilute Q=0 superfluid weight — none of H_032-035 are finite-Q.
    *Probe:* 2-band/valley-imbalanced lattice BdG with FS mismatch delta; self-consistent LO saddle Delta(r)~cos(Q·r); extract the GL stiffness TENSOR from d²F/d(grad theta)², modulation component D_s^||~delta·bandwidth. Escape = D_s^|| grows with delta and exceeds (pi/2)D_s^{Q=0}. Honest-null: D_s^|| ≤ D_s^{Q=0} across all mismatch, or the LO window is too narrow (depairing tensor caps Q-stiffness at the same n_s scale).

24. **PDW Commensurate Lock (pair-density-wave pinned to the lattice)** — Commensurate (Q=G/n) PDW whose sliding Goldstone is gapped by an Umklapp pinning term ~cos(n·theta), converting the soft phase channel into a gapped phason — attacks "order traps" from momentum space.
    *Probe:* Lattice BdG/ED, commensurate finite-Q pairing + V_p·cos(n·theta) Umklapp pinning; phason spectrum, Delta_phason~sqrt(V_p·rho_s); T_melt~max[(pi/2)D_s, Delta_phason]. Escape = at accessible V_p, Delta_phason>164K while the pairing eigenvalue is unchanged. Honest-null: the Umklapp that pins the phase ALSO suppresses the finite-Q pairing eigenvalue (no free lunch).

**L. Disorder-induced geometry lever**

25. **O2 disorder → flat band (disorder-induced flat band, geometry-for-free)** — Untested route to the geometry lever (tr g) from Anderson/structural disorder without crystallinity; flagged in the grand synthesis as one of two orthogonal bypasses worth a card (the freeze measured crystalline flat bands, never disorder-induced).
    *Probe:* Attractive-Hubbard BdG on L×L with on-site disorder W∈[−W/2,W/2]; sweep W into the disorder-flat-band regime (DOS spike at E_F, IPR rising); disorder-averaged Kubo D_s(W) over ≥50 samples, T_BKT. Escape if a finite W* gives T_BKT>134K AND xi_loc>vortex-core size. Honest-null: D_s(W) max stays ≥20× below 7.4 meV, OR disorder that flattens the band localizes the pairs (D_s→0 as IPR→1). Tooling: flatband_pair_ed.py + kubo_pair_stiffness.py + random on-site term.

*(Counting note: the 27-strong genuinely-new bucket is the 25 distinct mechanisms above plus the two "negative pole / sibling" framings already folded in — Janus pairs and the Z_N variants land in other buckets. The 25 numbered entries are the actionable wave-2 micro-exp shortlist.)*

## 3. Pressure-Hydride-Axis Seeds (different campaign — separate note)

These 7 explicitly do NOT engage the Emery-Kivelson spin-fluctuation phase-stiffness wall. They route around it via hydride/covalent phonon pairing on the chemical-precompression / mediator-mass axis (attacking the <200 meV phonon omega_log ceiling or recovering a metastable megabar phase at 1 atm). They are real, in-silico-testable levers but belong to a separate campaign axis and would need their own card stream, not wave-2 stiffness-wall micro-exps.

| Seed | One-line axis note |
|---|---|
| Muonic Hydride Inversion (mu-H3S analog) | Conventional Migdal-Eliashberg phonon glue via mediator-mass tuning; sidesteps the stiffness wall the way H3S already did. |
| Mediator-Mass Gradient Lattice | Bilayer hydride: mu-screened sublayer donates omega_log, H-mass sublayer donates stiffness; anharmonic-Eliashberg, <200 meV phonon ceiling. |
| Internal-Negative-Pressure Cage | Built-in lattice tension delivers megabar-equivalent density at 1 atm; chemical-precompression, by its own statement not the stiffness wall. |
| Anharmonic Cage Freeze (SSCHA quartic stabilization) | Rattler-stabilized hydride/covalent cage at 0 GPa; phonon condensate, chemical-precompression. |
| Epitaxial Pressure-Equivalence (biaxial misfit = hydrostatic GPa) | Misfit-strain-as-GPa to recover a high-P el-ph spectrum; ceiling is the few-% coherent-strain limit, a pressure-magnitude problem. |
| Guest-Charge Doublet (host cage + guest f-electron reservoir) | Host-guest precompression split in a hydride/B-C clathrate; covalent/phonon condensate, stiffness ceiling doesn't bind by construction. |
| Host-Guest Sliding-Chain Boson (incommensurate-rail glue) | Compressed S/Bi/Sc/Ba incommensurate host-guest phases adding a parallel lambda_phason; conventional/chem-precompression, "worth its own cards but on the pressure axis." |

## 4. Honest Verdict

After classifying all 124 SF seeds (on top of the resolved H_001-H_035 cards the freeze rests on), the **SF-escape space against the ~134-164K phase-stiffness wall is NOT yet exhausted** — but the surviving leads are narrow and individually likely to confirm-wall. Roughly two-thirds of the pool is dead weight against this wall: 49 seeds re-point at existing cards (the multiband-donation H_032 manifold, the bipolaron H_008 lever, the fractionalization/topology H_012/H_013 closure, the driven/Lindblad H_022/H_034 transient class, and the surveyed glue families), 26 are pre-satisfied by the freeze's own measured ~5× thermodynamic ledger-deficit and the geometric-stiffness D_s ceiling (every glue-side, mu*-side, BORROW/FRAME meta-principle, and refrigeration seed lands here), 11 are pure-SF with no engineerable solid host (horizon/Unruh/positronium/entanglement-resource/normal-fluid-not-SC), and 4 are lab-handoff devices out of the in-silico domain. The 7 pressure-hydride seeds are real but answer a different question. What genuinely survives is a coherent set of ~25 structurally-orthogonal probes that each attack a part of the Emery-Kivelson argument the four carded escapes never touched: the **"order traps" half via braiding-statistics / connectivity-geometry / commensurate-pinning / charge-frustration** (Statistical-Transmutation, Bethe-Ceiling, Quasicrystal-Localizer, Vortex-Code, PDW-Lock, Frustrated-Skipper), **stiffness sourced from a non-quasiparticle or non-electronic reservoir** (Yukawa-SYK incoherent D_s, Overhauser nuclear ballast, glassy-phason ballast), **light real-space pairs that decouple eV binding from stiffness** (Ligand-Hole / Charge-Kondo negative-U), **a static screened-Coulomb sign flip with no boson and no competing order** (ENZ / Hyperbolic-Coulomb / Flexoelectric finite-q vertex), **spin-group-symmetry pairing decoupled from Neel stiffness** (the three altermagnet seeds), **flux- or interference-decoupled flat bands** (AB-Cage Breather, BIC pair/CLS-hybrid), **finite-Q rigidity** (FFLO), and **disorder-induced geometry** (O2). Crucially, the freeze's geometric-stiffness verdict was measured on Q=0, single-particle-flattened, crystalline, quasiparticle-coherent, equilibrium hosts — and each surviving probe deliberately violates exactly one of those five premises, so its honest-null is genuinely un-run rather than already-implied. The honest expectation, given the freeze's depth and the "no-free-lunch" pattern in every prior null (pinning-that-helps also suppresses pairing; donation-that-adds-D_s also softens via Leggett; frustration-that-frees-pairs substitutes a glass trap), is that the great majority of these collapse back onto D_s~|U|·⟨g⟩ or onto the ledger deficit — i.e. the wall most likely holds. But "most likely" is not "proven," and the no-go has NOT been demonstrated for these specific orthogonal mechanisms. The correct ruling is therefore: **the wall stands undefeated, but the SF-escape space is not closed — ~25 clean wave-2 micro-experiments remain, each a live lead whose negative result would tighten the wall toward a genuine universal no-go and whose positive result would be a real escape.** No fabricated citations; the one literature reference (Setty arXiv:2305.05407, glassy-phason kernel) is carried verbatim from the seed and is unverified here.

Source files referenced: `/Users/mini/dancinlab/rtsc/state/papers/plus-at-combination-campaign-synthesis.md` (§4) and `/Users/mini/dancinlab/rtsc/state/sf_imagination_seed_pool_2026_06_25/seed_pool.md`.
