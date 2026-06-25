# H_036 — Statistical-Transmutation Fluctuation Trap-Breaker

- **id:** H_036 · **slug:** statistical-transmutation-trap-breaker
- **cluster:** order-traps-half (braiding statistics)
- **escape_class:** (d) order-trap removal via carrier statistics (Chern-Simons flux attachment)
- **date:** 2026-06-25 · **status:** closed-negative · **verdict:** confirms-wall
- **is_green:** false · **absorbed:** false · **deterministic:** true
- **run:** `state/h_036_statistical-transmutation-trap-breaker_2026_06_25/run.py`

## Frozen pre-registration
Claim: in a two-channel competing-order system (SC vs a CDW TRAP), attaching a Chern-Simons statistical flux at angle theta (theta=pi/k for level-k anyons) re-weights the two channels ASYMMETRICALLY, opening a theta-window where SC newly WINS over the CDW trap even where it lost at theta=0, lifting the trap-limited ceiling band ~134-164 K WITHOUT adding phase stiffness (the lever H_032-035 all attacked).

Violated freeze premise: SINGLE-PARTICLE / QUASIPARTICLE-COHERENT carriers. Statistical transmutation re-statisticizes the carriers (fermion<->anyon via flux attachment) — the "order-traps half" of the meta-law, untouched by H_032-035.

Bar: trap-limited ceiling upper edge 164 K. Escape condition: ALL four falsifiers PASS (the honest-null F2 must PASS, requiring the trap-vs-SC margin to genuinely depend on theta).

## The honest null (load-bearing, decisive)
A CS statistical gauge field is a PURE PHASE tied to the conserved charge density (a_ij ~ theta*(n_i+n_j)/2). The bare CS term is metric-independent/topological: its stress tensor VANISHES and it contributes NOTHING to energy/free energy/partition function (arXiv:hep-th/9509138; Schwarz-type TQFT). The SAME gauge field couples to the SAME density that BOTH the CDW trap and SC pair orders are built from; the flux-attachment unitary is diagonal in density and leaves the order moduli invariant, so it shifts both channels IDENTICALLY: margin(theta)=S_CDW(theta)-P_SC(theta)=margin(0). The crossing — hence the ceiling — is UNMOVED. Wall holds.

## Probe
Exact in-process ED of an extended-Hubbard ring (L=4, (N_up,N_dn)=(2,2), half filling), stdlib-only (math + hand-rolled deterministic cyclic-Jacobi on the real-symmetric embedding of the complex Hermitian H; no numpy/random). Flux attachment = explicit occupation-tied Peierls phase on ring hoppings. Params t=100, U=-120, V=+260 meV so the CDW trap genuinely wins at theta=0 (margin +3.15). theta swept [0,pi]; CDW(Q=pi) and on-site s-wave pair structure factors measured in the EXACT ground state. T-mapping deliberately charitable (SC win -> T=164*(1+|margin|)).

## Result (verbatim — no LLM self-judge)
margin flat to 3.6e-15 across the entire theta-sweep; CDW trap wins at theta=0 and never flips. F2 (honest-null) TRIGGERED -> null holds exactly -> confirms-wall. falsifiers_pass=0/4. Byte-equal across runs (md5 437f1b5c92981bc8bc576eed0b9baf2c, 2172 bytes).

## Falsifiers (4; PASS=not triggered) — all FAIL (triggered)
1. F1_no_theta_window_sc_newly_wins — FAIL (SC never newly wins).
2. F2_HONEST_NULL_equal_shift_margin_theta_independent — DECISIVE — FAIL (swing 3.6e-15; null holds exactly).
3. F3_best_tc_below_ceiling — FAIL (best T=164 K, pinned).
4. F4_tc_not_raised_vs_theta0 — FAIL (no gain over ordinary fermions).

## Honest limits (>=6)
1. Tiny L=4 cluster — exact but cannot resolve a true thermodynamic CDW<->SC transition; tests the theta-response of the balance (the load-bearing question), not the absolute crossing.
2. Lattice flux attachment != continuum CS — the bare Peierls phase omits gauge-field fluctuations (a 2D fluctuating-CS MC would be the stronger test; the null predicts they add no net free energy).
3. No genuine anyon host — real statistical-glue SC lives on exotic doped-FQAH/composite-fermion hosts (arXiv:2506.02108, 2605.19036), not the ambient crystalline metal modeled; this stays in the freeze's domain by construction.
4. Charitable T-mapping never exercised in the SC-win branch (margin never flips), so the negative is robust to it.
5. Single filling / single (U,V) operating point; the honest-null is an operator-level statement independent of the point, demonstrated numerically here.
6. No SDW (spin) trap channel modeled — only CDW (charge); the same null argument applies but was not separately computed.

## Pool compute that would strengthen (not required)
A 2D fluctuating lattice-CS + extended-Hubbard determinant/auxiliary-field or worm Monte-Carlo on an exotic-host filling, large enough to host a real CDW<->SC transition, to test whether gauge-field fluctuations (absent here) move the crossing. Does not fit in-process; the null predicts no movement.

## Refs
arXiv:hep-th/9204033 · arXiv:hep-th/9509138 · arXiv:2506.02108 · arXiv:2605.19036