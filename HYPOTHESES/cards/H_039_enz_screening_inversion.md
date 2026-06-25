# H_039 — ENZ Screening Inversion (the Permittivity Mirror)

- **id:** H_039 · **slug:** enz-screening-inversion
- **cluster:** static Coulomb sign-flip (no exchanged boson, no competing order)
- **escape_class:** (b) different glue — a STATIC (omega=0) sign-flipped Coulomb kernel from a negative-permittivity dielectric environment, in place of a retarded boson
- **date:** 2026-06-25 · **status:** closed-negative
- **verdict (verbatim from run):** `confirms-wall`
- **is_green:** False · **absorbed:** False · **deterministic:** True (byte-equal x2, md5 14eb3d49…)
- **run:** `state/h_039_enz-screening-inversion_2026_06_25/run.py`

## Frozen pre-registration
**Claim (seed).** Embed a 2D electron layer in a medium with engineered `Re[eps_env(q,omega~0)]<0` (ENZ / negative-permittivity "permittivity mirror"). Negative static env permittivity flips the static screened-Coulomb sign, `W(q,0)=v(q)/eps_tot(q,0)<0` → a real static attraction with NO boson, NO competing order. At metallic n the implied Kubo `D_s` would sit above the cuprate ~7.4 meV (=134 K) scale and clear the ~134–164 K wall.

**Premise violated.** The freeze (Q=0 / single-particle-flat / crystalline / quasiparticle-coherent / EQUILIBRIUM) measured the geometric-stiffness ceiling on hosts whose glue was a retarded boson at dilute flat-band n. This escape violates the **glue-source/equilibrium** premise: a static sign-flipped Coulomb kernel from an external dielectric, at high metallic n (no boson → no omega_log cap; high n → in-principle high D_s).

**Frozen escape condition.** ESCAPE iff a passive embedding delivers `Re[eps_tot(q,0)]<0` over a finite band INSIDE the FS scattering shell `q∈(0,2k_F]` that is NOT the layer's own already-counted 2k_F overscreening, AND the implied Kubo `D_s` exceeds 7.4 meV (T_BKT>164 K).

## Load-bearing HONEST-NULL (decisive, not engineered around)
The seed's stated null ("KK + passivity force integrated W>0 for every passive cladding") is **physically WRONG, and the card says so honestly.** Dolgov–Kirzhnitz–Maksimov (RMP 53, 81, 1981) prove the static eps(q,0) at finite q does NOT obey KK in q, and eps(q,0)<0 (overscreening) is stable for a wide class of media; the forbidden window is `0<eps(q,0)<1`, both eps≥1 and eps<0 are stable. So static `W<0` is REAL (run grants this via F1 PASS). The DECISIVE q-resolved null, two exhaustive cases: **(a)** a passive EXTERNAL cladding's negative-eps band is long-wavelength (`q<q_env≪2k_F`); the layer's own Thomas-Fermi screening `(q_TF/q)S(q)` diverges as q→0 and restores eps_tot>1 across the FS shell → attraction confined to a tiny-q corner (0% of outer half [k_F,2k_F]). **(b)** any eps_tot<0 reaching `q~2k_F` is the layer's OWN Kohn–Luttinger 2k_F overscreening, already in the host kernel / freeze ledger; an external static cladding changes neither n, m*, nor d → donates 0 meV stiffness (only renormalizes mu*, the Smolyaninov metamaterial-SC route, arXiv:1311.3277/1801.03438). Both → D_s below cuprate scale → wall holds.

## Falsifiers (PASS = not triggered). Run: 1/5 pass
| # | name | role | result |
|---|---|---|---|
| F1 | F1_static_signflip_is_real_DKM | charitable/DKM premise (overscreening real; seed no-go false) | PASS (eps_tot<0 at q=0.030·2k_F) |
| F2 | F2_HONEST_NULL_attraction_covers_FS_scattering_shell | DECISIVE — W<0 must cover [k_F,2k_F] ≥50% | TRIGGER (outer-half=0.000) |
| F3 | F3_HONEST_NULL_implied_Ds_exceeds_cuprate_scale | DECISIVE — donated D_s must exceed 7.4 meV | TRIGGER (donated=0 meV) |
| F4 | F4_new_metallic_n_glue_not_mustar_renorm | new metallic-n attraction, not mu* renorm | TRIGGER |
| F5 | F5_finiteq_attraction_beyond_intrinsic_KohnLuttinger | beyond intrinsic 2k_F Kohn-Luttinger | TRIGGER (q_env=0.15<0.5) |

Escape iff BOTH decisive nulls (F2 AND F3) PASS with margin. They do NOT → **confirms-wall**.

## Honest limits (≥5)
1. Toy q-profile, not a full first-principles cRPA W(q,0) of a real ENZ heterostructure — captures sign/q-coverage, not material numbers.
2. 2D Stern/Lindhard at T=0, single band; multi-band/finite-T/vertex add MORE small-q screening (sharpen the null), not less.
3. `q_env≪2k_F` is asserted from the physical plasma/unit-cell scale of real metamaterials, not derived per material; an anomalously short-wavelength negative band (the anisotropic "Hyperbolic Pitch-Black Coulomb" sibling) is a separate card.
4. D_s ledger is order-of-magnitude; "0 meV donated" is the scaling fact that an external static dielectric moves none of (n,m*,d) — no self-consistent embedded BdG+Kubo run (it would be capped by the same n/m*).
5. The μ*-reduction Tc bump (the real Smolyaninov effect) is asserted, not quantified.
6. The DKM stability window (0<eps(q,0)<1 forbidden, eps<0 allowed) is taken from cited literature (DKM 1981; arXiv:0707.2489), not re-derived.

## Verbatim run VERDICT (no LLM self-judge)
```
  [PASS   ] F1_static_signflip_is_real_DKM
  [TRIGGER] F2_HONEST_NULL_attraction_covers_FS_scattering_shell
  [TRIGGER] F3_HONEST_NULL_implied_Ds_exceeds_cuprate_scale
  [TRIGGER] F4_new_metallic_n_glue_not_mustar_renorm
  [TRIGGER] F5_finiteq_attraction_beyond_intrinsic_KohnLuttinger
decisive F2 (FS-shell coverage) PASS     : False
decisive F3 (implied D_s > cuprate) PASS : False
falsifiers_pass : 1/5
VERDICT         : confirms-wall
```

## References (cited, not fabricated)
- Dolgov, Kirzhnitz, Maksimov, RMP 53, 81 (1981), DOI 10.1103/RevModPhys.53.81 — admissible sign of static eps; eps(q,0)<0 stable, forbidden window 0<eps<1.
- arXiv:0707.2489 ("A Little About Folklore") — static eps(q,0) at finite q does not obey KK in q.
- Smolyaninov & Smolyaninova, arXiv:1311.3277 — metamaterial route to high-Tc.
- Smolyaninov & Smolyaninova, arXiv:1801.03438 — Metamaterial Superconductors (mu* engineering).
- Kohn–Luttinger / 2k_F Friedel non-analyticity of the 2D Lindhard function.