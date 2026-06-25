# H_050 — Flexoelectric Gradient Glue (pairing from strain-gradient, not strain)

- **id:** H_050 · **slug:** flexoelectric-gradient-glue
- **cluster:** dielectric-engineering glue family (within-cluster VARIANT of H_039 ENZ-screening-inversion / hyperbolic-Coulomb sibling)
- **escape_class:** (b) different glue — a FINITE-q (~q) flexoelectric gradient vertex V(q,w)=(q*mu)^2*chi_soft(q,w) that VANISHES at q=0, asserted to operate at metallic n
- **violated_freeze_premise:** glue-momentum/glue-source
- **date:** 2026-06-25 · **status:** closed-negative
- **verdict (verbatim from run):** `confirms-wall`
- **is_green:** False · **absorbed:** False · **deterministic:** True (byte-equal x3, md5 17f04ec8b862aae0f1c3d2084bf1e0ca)
- **run:** state/h_050_flexoelectric-gradient-glue_2026_06_25/run.py

## Frozen pre-registration
Claim (seed): build V(q,w)=(q*mu)^2*chi_soft(q,w) in a 2D BdG/ED toy at METALLIC n and solve the linearized gap equation; because the vertex ~q vanishes at q=0 it can in principle operate at metallic n where D_s is large. ESCAPE if lambda>0.3 for physical mu with nodeless/extended-s gap AT a density where Kubo D_s already exceeds the cuprate scale (glue and stiffness decoupled). Violates the glue-momentum/glue-source premise (finite-q gradient vertex, not a q~0 retarded boson, at high metallic n). Frozen escape condition: a SINGLE density both metallic (D_s>7.4 meV) AND pairing (lambda>0.3), chi_soft not Landau-collapsed.

## Load-bearing HONEST-NULL (decisive, not engineered around)
At metallic n the soft TO mode is Landau-damped so chi_soft(q,w->0) collapses exactly where D_s would be large. Two inescapable channels: (1) q^2 form-factor wants large-q while chi_soft peaks at small-q (gradient coupling vanishes in the IR at Gamma, Saha arXiv:2412.05374); (2) Landau overdamping gamma_LD~N0/q at metallic n drives the coherent pairing-pole weight Z_damp=w0/(w0+gamma_LD)->0 (published FE-QCP SC is ULTRALOW-density only, Kozii-Bi-Ruhman PRX 9 031046; gradient pairing "only valid at lowest densities," overdamped at the QCP, Saha App. C.2). HONEST CORRECTION during BUILD (no tune-to-green): an initial STATIC 1/(r+cq^2+Pi) susceptibility could not encode dynamical Landau damping and gave a spurious rising lambda at high n; corrected to the faithful coherent-weight form chi_soft=Z_damp(q)/(r+cq^2+Pi), after which lambda MONOTONICALLY collapses at genuinely metallic densities (0.100 at n=5e14 D_s=7.9 meV -> 0.009 at n=1e17). No threshold moved. Run result: lambda peaks at only 0.147 at n=1e14 where D_s is only 1.587 meV (sub-cuprate); no single density has both lambda>0.3 AND D_s>7.4 meV; the glue lives only in the dilute regime (already inside the freeze ledger), the stiffness only in the metallic regime (collapsed glue).

## Falsifiers (PASS = NOT triggered). Verbatim 1/5 pass
| # | name | role | result |
|---|---|---|---|
| F1 | F1_flexo_vertex_pairs_somewhere | charitable premise (pairs in dilute regime) | PASS (lambda_peak=0.147>0) |
| F2 | F2_HONEST_NULL_lambda_above_escape_at_metallic_n | DECISIVE — lambda>0.3 at metallic n | TRIGGER (0.147<0.30) |
| F3 | F3_HONEST_NULL_glue_and_stiffness_coexist_at_one_density | DECISIVE — one density with lambda>0.3 AND D_s>7.4 | TRIGGER (none) |
| F4 | F4_HONEST_NULL_lambda_peak_is_metallic | DECISIVE — lambda-peak density is metallic | TRIGGER (peak D_s=1.587<7.4) |
| F5 | F5_chi_soft_not_collapsed_by_metallic_landau_damping | kinematic no-free-lunch (ratio>=0.5) | TRIGGER (0.163<0.5) |
Verdict logic: escapes-wall iff F2 AND F3 AND F4 all PASS with margin. They do NOT => confirms-wall.

## Honest limits (>=5)
1. Toy linearized-gap eigenvalue on a circular 2D FS, not self-consistent Eliashberg (frequency resolution would STRENGTHEN the overdamping suppression).
2. chi_soft and gamma_LD~N0/q, Z_damp=w0/(w0+gamma_LD) are reduced-unit Maslov-Chubukov/Hertz-Millis scaling forms, not a cRPA of a real flexoelectric host — capture sign/q-profile, not material Tc.
3. density->N0_screen is a linear proxy; the decisive monotonicity (lambda falls past the cuprate-D_s density) is prefactor-robust; the cross-over density is not a material prediction.
4. mu set OPTIMISTICALLY (mu_sq=1.0); a larger mu scales lambda uniformly but does not change the density where decoupling fails.
5. D_s(n) is order-of-magnitude Uemura/Kubo (fixed m*=2, d=0.6 nm); no self-consistent BdG+Kubo on the paired state (still n/m*-capped, still collapsed glue).
6. Single-band, T=0, isotropic FS; multiband/anisotropy/finite-T add more particle-hole phase space (more damping), sharpening the null.

## Verbatim run VERDICT (no LLM self-judge)
```
  [PASS   ] F1_flexo_vertex_pairs_somewhere
  [TRIGGER] F2_HONEST_NULL_lambda_above_escape_at_metallic_n
  [TRIGGER] F3_HONEST_NULL_glue_and_stiffness_coexist_at_one_density
  [TRIGGER] F4_HONEST_NULL_lambda_peak_is_metallic
  [TRIGGER] F5_chi_soft_not_collapsed_by_metallic_landau_damping
decisive F2 (lambda>0.3 at metallic n) PASS     : False
decisive F3 (glue+stiffness coexist)   PASS     : False
decisive F4 (lambda peak is metallic)  PASS     : False
falsifiers_pass : 1/5
is_green        : False
absorbed        : False
VERDICT         : confirms-wall
```

## References (cited, not fabricated)
- Kozii, Bi, Ruhman, PRX 9, 031046 (2019), arXiv:1901.11064 — TO-mode pairing in the ULTRALOW-density limit.
- Saha et al., arXiv:2412.05374 — gradient coupling vanishes in the IR at Gamma; mode overdamped at the QCP; gradient pairing only valid at lowest densities (ratio ~1e-3 at dome peak, App. C.2).
- Kozii, Klein, Fernandes, Ruhman, PRL 129, 237001 (2022), arXiv:2110.09530 — FE+SC synergy at ZERO density.
- Maslov-Chubukov / Hertz-Millis overdamped-boson Landau-damping form (gamma_LD~N0/q).