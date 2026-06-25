# H_051 — Frustrated Valence Skipper: the disproportionation that can't crystallize

- id: H_051 | slug: frustrated-valence-skipper | escape_class: (d) order-trap removal via geometric frustration (CHARGE channel)
- cluster: negative-U / valence-skipper (sibling of H_038, H_036) | status: closed-negative (confirms-wall) | date: 2026-06-25
- is_green: false | absorbed: false | violated_premise: crystalline / equilibrium-ordered
- run: state/h_051_frustrated-valence-skipper_2026_06_25/run.py (stdlib-only, deterministic, byte-reproducible md5 d78aef5e)

FULL CARD WRITTEN TO: /Users/mini/dancinlab/rtsc/state/HYPOTHESES/cards/H_051_frustrated-valence-skipper.md

## Hypothesis (frozen)
A negative-U valence skipper (Bi3+/Bi5+, Tl1+/Tl3+) on a geometrically frustrated lattice (pyrochlore/triangular/checkerboard) vs the cubic control. Bet: the charge-CDW that traps the pairs cannot tile a frustrated lattice, so Delta_CDW->0 while chi_pair stays divergent where the cubic host is a CDW insulator, freeing the eV pairing scale above the 134-164 K ceiling toward 293 K. Attacks the order-traps half of the no-free-lunch meta-law in the CHARGE channel (H_022 was spin).

## Freeze premise violated
crystalline / equilibrium-ordered (destabilize the competing crystalline CDW so pairing is not pre-empted).

## Decisive physics + HONEST-NULL (theorem, not fit)
Yang/Zhang pseudospin SU(2) (cond-mat/9504019): in the bipartite negative-U Hubbard model at half-filling V=0, the s-wave PAIR and CDW order parameters are an exact pseudospin SU(2) rotation -> two arms of ONE vector of fixed length |U_eff|nu(1-nu). Tipping CDW->SC by V/doping/frustration ROTATES, never LENGTHENS (arXiv:0802.1011: frustration-driven CDW->SC is real but chi_pair and chi_CDW diverge together). Probe = real 16-state Fock-space ED of the negative-U extended-Hubbard dimer measuring CDW gap, the Shiba spectral duality spectrum(U<0)=-spectrum(U>0) to 3.1e-15, the conserved eV binding, and the binding!=stiffness firewall.
HONEST-NULL (both branches lit-confirmed): (A) frustration rotates not lengthens -> freed stiffness stays pinned on the cuprate D_s<=7.4 meV line (T_BKT~135 K), chi_pair never exceeds the trap-setting scale; (B) frustration substitutes a charge-cluster GLASS that re-localizes the pairs (Kanoda/Sato arXiv:1311.0344, 1408.2913). EITHER holding => wall holds.

## Falsifiers (PASS=not triggered=escape survives; all 5 FAIL=triggered=wall holds)
1. honest_null_A_stiffness_pinned_to_cuprate_line (DECISIVE) FAIL — freed stiffness <=7.4 meV (length conserved; stiffness is metric-weighted projection, not raw eV binding).
2. honest_null_B_charge_glass_substitution (DECISIVE) FAIL — frustrated GS is a charge-cluster glass (arXiv:1311.0344).
3. su2_shiba_duality_holds FAIL — Shiba duality measured to residual 3.1e-15 (one conserved instability).
4. binding_not_stiffness_firewall FAIL — eV binding mis-read as stiffness => 3418 K, but real stiffness-bounded T_BKT=134.9 K (same lock H_038 hit).
5. tbkt_below_room_T FAIL — 134.9 K < 293 K.
Verdict logic: escapes-wall needs BOTH nulls PASS AND T_BKT>=293 K; none hold -> confirms-wall.

## Honest limits (>=5)
1. Two-site dimer ED is real but cannot host the eta-pairing condensate: half-filled GS is the eta=0 pseudospin SINGLET so chi_pair legitimately vanishes (honestly annotated); SU(2) read from Shiba duality, not finite-cluster chi_pair (full QMC out-of-process).
2. Delta_CDW->0 on the frustrated lattice is GRANTED (f=0, seed's best case), not computed from a pyrochlore dispersion.
3. Freed stiffness capped at the calibrated cuprate D_s=7.4 meV (charitable; material-specific would be lower).
4. Charge-glass null (B) is an external literature datum (theta-(BEDT-TTF)2X), not produced by the dimer.
5. U_eff=0.75 eV, nu=1/2 are generous representative values; a real dilute doped bismuthate makes the wall hold harder.
6. The SU(2) theorem is exact only at V=0/half-filling/bipartite, but lifting it (V/doping/frustration) only rotates the conserved vector — the null is robust to, not contingent on, the approximation.

## Verdict
confirms-wall. Genuine escape in KIND (frustration can kill the crystalline CDW) but not in MAGNITUDE: the pseudospin SU(2) lock (Shiba duality 3.1e-15) makes CDW and SC two arms of one conserved instability; frustration rotates CDW->SC but cannot lengthen the vector, freeing eV BINDING not phase STIFFNESS (pinned on cuprate D_s=7.4 meV, T_BKT~135 K), and substitutes a charge-cluster glass that re-localizes the pairs. Both decisive nulls triggered. The trap is conserved against the glue — the same no-free-lunch pattern as the 12 prior probes, now in the charge-order channel. is_green=false; absorbed=false; no material claimed to BE an RTSC.

## References
arXiv:cond-mat/9504019 (Yang-Zhang pseudospin SU(2)) ; arXiv:cond-mat/0602536 ; arXiv:0802.1011 (PRB 77 180515(R)) ; arXiv:1311.0344 (charge-cluster glass) ; arXiv:1408.2913