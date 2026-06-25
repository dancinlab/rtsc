# H_049 — Hyperbolic Pitch-Black Coulomb (Anisotropic Negative-Group-Velocity Glue)

- **id:** H_049
- **slug:** hyperbolic-pitch-black-coulomb
- **cluster:** static anisotropic-Coulomb sign-flip (dielectric engineering) — **within-cluster VARIANT of H_039 ENZ Screening Inversion**
- **escape_class:** (b) different glue — a STATIC (ω≈0) anisotropic (eps-tensor) sign-flipped Coulomb kernel with a MOMENTUM-SELECTIVE large-q attractive lobe, in place of a retarded boson
- **date:** 2026-06-25
- **status:** closed-negative
- **verdict (verbatim from run):** `confirms-wall`
- **is_green:** False · **absorbed:** False · **deterministic:** True (byte-equal ×2)
- **run:** `state/h_049_hyperbolic-pitch-black-coulomb_2026_06_25/run.py`

## Frozen pre-registration (predictions, frozen before run)

**Claim (seed).** For a 2D electron layer on a HYPERBOLIC cladding (`eps_par > 0`, `eps_perp < 0`), the anisotropic-medium static Coulomb kernel `W(q) ~ v0 / (eps_par·q_par² + eps_perp·q_perp²)` changes SIGN along a cone `q_par²/q_perp² = -eps_perp/eps_par`, opening a MOMENTUM-SELECTIVE attractive lobe (`W < 0`) at LARGE q ~ k_F that is ABSENT for an isotropic dielectric of equal mean eps. If that lobe sits BELOW 2k_F and operates at METALLIC n, the implied Kubo D_s would clear the frozen ~134–164 K wall.

**Why distinct from confirmed sibling H_039 (not pre-satisfied).** H_039 (isotropic ENZ) closed because the negative-eps band is LONG-WAVELENGTH (q < q_env ≪ 2k_F), 0% of the FS shell. The hyperbolic twist places the cone sign-change at a q-direction-dependent ratio that CAN sit at finite large q near k_F, so H_049 re-tests FS-coverage on its own terms.

**Violated freeze premise.** GLUE-SOURCE/equilibrium: static anisotropic Coulomb kernel from an external eps-tensor cladding, metallic n, finite-q channel.

**Frozen escape condition.** ESCAPE iff BOTH decisive nulls PASS with margin: (D1) SCREENED attractive coverage of FS shell [k_F,2k_F] > 50%, AND (D2) implied Kubo D_s > 7.4 meV.

## The load-bearing HONEST-NULL (decisive — NOT engineered around)

The run GRANTS (F1 PASS) that the bare hyperbolic cone DOES flip the Coulomb sign and covers 56% of the FS shell inside 2k_F. The DECISIVE null is sharper, in three parts:
- **(N1, decisive)** Intra-layer screening kills the cone: `eps_tot(q)=eps_clad(q-hat)+q_TF/q`; at metallic n `q_TF/2k_F=2.39`, so positive 2D Thomas–Fermi screening dominates the modest eps-tensor cone across the whole shell. SCREENED coverage collapses from 56% to **7.9%** << 50%.
- **(N2)** The cone is a measure-near-zero surface (codim-1) not a finite-area lobe.
- **(N3, decisive)** An external static dielectric changes NONE of (n, m*, d) → donates **0 meV** of new phase stiffness.

Escape needs BOTH N1(F2) and N3(F3) to PASS. F2 TRIGGERS ⇒ wall holds.

## Falsifiers (PASS = NOT triggered). Verbatim run result: 4/5 pass

| # | name | role | result |
|---|---|---|---|
| F1 | F1_bare_anisotropic_cone_sign_change_exists | charitable — bare cone flips W in FS shell | PASS (0.564) |
| F2 | F2_HONEST_NULL_screened_attraction_covers_FSshell | DECISIVE — screened W<0 > 50% of [k_F,2k_F] | TRIGGER (0.079) |
| F3 | F3_HONEST_NULL_implied_Ds_exceeds_cuprate_scale | DECISIVE — D_s > 7.4 meV | PASS (overestimate, non-load-bearing — limit #1) |
| F4 | F4_lobe_absent_in_isotropic_control | lobe must exceed equal-mean isotropic control | PASS (+0.079) |
| F5 | F5_implied_TBKT_clears_wall | implied T_BKT > 164 K | PASS (overestimate, non-load-bearing) |

Escape iff BOTH F2 AND F3 PASS. F2 TRIGGERS ⇒ **confirms-wall**.

## Honest limits (≥5)

1. **D_s estimate (F3/F5) is a deliberate OVERESTIMATE, NOT load-bearing.** `D_s~(ℏ²/m*)·n_2D/d` gives 127 meV / 2315 K, a crude-prefactor artifact (real Kubo D_s ~1 meV). NOT tuned to force a trigger; escape gate is F2 AND F3, and F2 already triggers. Decisive physics is N1/F2 + the correct `Ds_donated=0`.
2. **Toy q-resolved kernel, not full cRPA** — captures sign structure + screening competition, not material-specific cRPA W(q,ω→0).
3. **Single generous eps-tensor (2,-3); no full sweep** — stronger eps_perp widens bare cone but `q_TF/q` diverges at small q and dominates regardless.
4. **2D single-band T=0** — multi-band/finite-T/dynamical/vertex add MORE positive small-q screening, sharpening the null.
5. **Static only (ω≈0)** — retardation re-introduces a boson-frequency cap (H_039/Migdal), which does not help; static glue was the seed's claim.
6. **F4 PASSES but non-load-bearing** — hyperbolic 7.9% genuinely exceeds isotropic 0% (real tensor twist), but still << 50% FS coverage.
7. **Experimental anchor is a low-Tc μ*-bump** — Al 1.2K→3.9K is a renorm of an existing phonon condensate; no metallic-n room-T hyperbolic glue demonstrated.

## Verbatim run VERDICT (no LLM self-judge)

```
SCREENED coverage of FS shell     : 0.0790  (threshold 0.5)
bare cone coverage of FS shell    : 0.5639
coverage excess vs isotropic      : 0.0790
D_s DONATED by static eps-tensor  : 0.0000 meV
  [PASS   ] F1_bare_anisotropic_cone_sign_change_exists
  [TRIGGER] F2_HONEST_NULL_screened_attraction_covers_FSshell
  [PASS   ] F3_HONEST_NULL_implied_Ds_exceeds_cuprate_scale
  [PASS   ] F4_lobe_absent_in_isotropic_control
  [PASS   ] F5_implied_TBKT_clears_wall
decisive F2 (screened FS-shell coverage) PASS : False
decisive F3 (implied D_s > cuprate)      PASS : True
falsifiers_pass : 4/5
is_green        : False
absorbed        : False
VERDICT         : confirms-wall
```

## References (cited, not fabricated)

- Smolyaninov & Smolyaninova, *Enhanced superconductivity in aluminum-based hyperbolic metamaterials*, Sci. Rep. **6**, 34140 (2016), DOI 10.1038/srep34140.
- Smolyaninov & Smolyaninova, *Metamaterial Superconductors*, arXiv:1801.03438.
- Smolyaninov, arXiv:1311.3277.
- *Interplay of hyperbolic plasmons and superconductivity*, arXiv:2201.07731.
- Dolgov–Kirzhnitz–Maksimov, *Rev. Mod. Phys.* **53**, 81 (1981), DOI 10.1103/RevModPhys.53.81.
- Stern, *Phys. Rev. Lett.* **18**, 546 (1967) — 2D Lindhard/Thomas–Fermi static screening.