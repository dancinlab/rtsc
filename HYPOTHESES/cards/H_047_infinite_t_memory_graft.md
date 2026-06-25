# H_047 — Infinite-T Memory Graft (subsystem-code symmetry that does not melt)

- **id:** H_047 · **slug:** infinite-t-memory-graft
- **cluster:** code-/symmetry-protected order-class — conserved subsystem-code charge with no finite melting T by theorem (within-cluster VARIANT of carded H_043 vortex-code; same family as H_036 [S,H] commutator test)
- **escape_class:** (b) attack the equilibrium energetic-melting order-trap premise via a subsystem-conserved order sector (not the stiffness)
- **date:** 2026-06-25 · **status:** closed-negative · **verdict:** confirms-wall
- **is_green:** false · **absorbed:** false · **deterministic:** true (byte-equal x2, sha c1808a09…)
- **run:** state/h_047_infinite-t-memory-graft_2026_06_25/run.py

## Frozen pre-register
Seed (triage D#7): replace energetic (stiffness-limited) order with a conserved SUBSYSTEM-code charge that has no finite melting T by theorem. Build a Z2xZ2 plaquette/Xu-Moore subsystem code whose LOGICAL operator is the order parameter; graft a pair-hopping term tying the logical to a charge-2e bilinear so the ordered phase is a superconductor. ED: logical autocorrelation C(t) and its T-dependence.
Wall-prediction (escape): C(t) shows no Arrhenius decay and no finite-T cusp up to the lattice cutoff — a room-T-robust condensate bypassing the (pi/2)D_s ceiling.
HONEST-NULL (decisive CRUX, tested first): the charge-2e pair-hopping coupling that makes it a superconductor makes the protecting subsystem generator FAIL to commute with H ([S,H]≠0): the σx/σy pair bilinear anticommutes with the σz line generator, destroying the conserved charge for any finite coupling (You-Devakul-Burnell-Sondhi arXiv:1803.02369). Order reverts to energetic → bounded by (pi/2)D_s. BACKSTOP: a d_sub=1 line subsystem symmetry cannot break at finite T (generalized Elitzur / dimensional reduction, Batista-Nussinov arXiv:cond-mat/0410599), so T_order=0 or an energetic plaquette-Ising Tc≈0.55J (arXiv:1507.05784). Either branch → confirm-wall.
Premise violated: equilibrium / energetic-order-trap (order hosted in a subsystem-conserved sector, not a free-energy condensate).
Method: exact ED of a 4-site (2x2) Xu-Moore code H_code=−K·X0X1X2X3 (K=100 meV), generators S_R0=Z0Z1,S_R1=Z2Z3,S_C0=Z0Z2,S_C1=Z1Z3, logical O_L=Z0; SC graft −g·Σ(XiXj+YiYj)/2, g=50 meV. Compute (1) ‖[S,H(g)]‖ for code vs graft, (2) infinite-time Mazur plateau of the canonical logical autocorrelation at T=50,150,293,1000,1e6 K and β=0, (3) energetic (pi/2)D_s ceiling vs the 134–164 K wall.

## Verbatim run verdict (no LLM self-judge)
```
H_047  Infinite-T Memory Graft (subsystem-code symmetry that does not melt)
(1) CRUX: ||[S,H_code]||=0.0 (all 4 generators)  ||[S,H_SC]||=4.000000e+02 (all 4)
    symmetry preserved by bare code? True ; BROKEN by SC graft? True  <== CRUX honest-null
(2) logical plateau C(inf):  code=1.000000 at every T incl inf-T ; SC-grafted=0.031250 at inf-T
    (room T 293 K: code 1.000000, SC 0.000029)
    code protected? True (pos control) ; SC-grafted protected? False (escape needs True)
(3) energetic (pi/2)D_s ceiling = 1.09-8.02 K ; D_s needed for 134 K = 7.351 meV (~16.7x)
    best resulting ordering T = 8.02 K ; wall = 134-164 K
  [FAIL] F1_CRUX_HONEST_NULL_SC_graft_breaks_subsystem_symmetry
  [FAIL] F2_HONEST_NULL_grafted_logical_not_protected_at_infinite_T
  [FAIL] F3_best_order_tc_below_wall
  [PASS] F4_code_logical_IS_protected_positive_control
  [PASS] F5_code_symmetry_commutes_positive_control
falsifiers_pass = 2/5 ; CRUX honest-null (F1) triggered = True
VERDICT: confirms-wall ; falsifiers_pass: 2 ; is_green: False  absorbed: false
```
falsifiers_pass = 2/5. Three FAILs are the decisive confirm-wall falsifiers (F1 crux, F2 logical-melts, F3 ceiling deficit); two PASS are positive controls proving the bare code conserves+protects the logical, so F1's collapse is caused by the SC graft. decisive_null_triggered=true.

## Falsifiers (≥4; crux decisive)
1. F1 CRUX honest-null — TRIGGERED. ‖[S,H_code]‖=0 (all 4), ‖[S,H_SC]‖=400 meV (all 4): σx/σy pair bilinear anticommutes with σz line generators; protecting charge destroyed by the SC coupling; [S,H]≠0 exact.
2. F2 grafted-logical-not-protected — TRIGGERED. plateau 1.000→0.031 at inf-T (2.9e-5 at room T), below 0.5: O_L not conserved once SC is on; order melts.
3. F3 best-order-Tc-below-wall — TRIGGERED. energetic (pi/2)D_s=1.1–8.0 K for frozen D_s; 7.351 meV (~16.7x) needed for 134 K — same deficit as H_043.
4. F4 code-logical-protected positive control — PASS. pure code plateau=1.000 at all T incl inf-T.
5. F5 code-symmetry-commutes positive control — PASS. [S,H_code]=0 all 4 generators.

## Honest limits (≥5)
1. Small ED (single plaquette, 16-dim): the commutator/anticommutation crux is L-independent and exact (400 meV is an algebraic identity), not a finite-size estimate; verdict rests on the symmetry algebra, not a thermodynamic-limit Tc extraction.
2. No-free-lunch lock is generic: forced by σz(logical)–σx/σy(pair) anticommutation; a diagonal (commuting) pair operator would not flip the logical ⇒ no ODLRO ⇒ not an SC. Commuting⇒not-SC; SC⇒not-commuting.
3. Backstop (generalized Elitzur, d≤2 no finite-T breaking) carried analytically from cited theorems, not separately run, because F1 already triggers.
4. (pi/2)D_s energetic ceiling inherited from frozen flat-band D_s=0.06–0.44 meV / H_043; a host with D_s~7.4 meV would reach 134 K but then stiffness is the win (the existing wall), code irrelevant.
5. Mazur/diagonal-plateau is the operationally correct thermal "does the memory survive" measure (=1 iff O_L conserved); it equals the seed's no-cusp C(t) statement, which the SC branch fails.
6. JW/hardcore-boson mapping b_i↔σ−_i is standard; a fermionic charge-2e operator with a JW string would only add more non-commuting structure, never restore commutation (charitable to the escape).
7. No fabricated citations — all anchors located via web search 2026-06-25; the anticommutation-destroys-SSPT and d≤2 no-finite-T-breaking results are the load-bearing facts, reported not invented.

## Conclusion
The "infinite-T memory" of a subsystem code is real only while the protecting charge is conserved — and the charge-2e pair-hopping coupling that turns the code into a superconductor anticommutes with the subsystem generators (‖[S,H_SC]‖=400 meV exact), destroying the charge for any finite coupling. The logical plateau collapses 1.0→0.031 at inf-T: the order melts. Once protection is gone the order is energetic, bounded by (pi/2)D_s=1.1–8.0 K — 16.7x and ~126 K short of the wall (the identical deficit as H_043). Same no-free-lunch lock the cluster keeps hitting. Confirms the wall via the equilibrium-order-trap channel. absorbed=false.

## Refs
- Nussinov & Ortiz, Ann.Phys.324,977 (2009), arXiv:cond-mat/0702377 — subsystem symmetries, dimensional reduction, Tc bounded by lower-d model.
- Batista & Nussinov, PRB 72,045137 (2005), arXiv:cond-mat/0410599 — generalized Elitzur: d≤2 subsystem symmetry cannot break ⇒ no finite-T order.
- You, Devakul, Burnell, Sondhi, PRB 98,035112 (2018), arXiv:1803.02369 — SSPT; anticommuting perturbation destroys order at any finite coupling.
- Devakul, You, Burnell, Sondhi, SciPost Phys.6,007 (2019), arXiv:1805.04097 — fractal/subsystem symmetric phases; same rule.
- Johnston et al., arXiv:1507.05784 — 3d plaquette (Xu-Moore) Ising orders at a FINITE first-order Tc≈0.55J.