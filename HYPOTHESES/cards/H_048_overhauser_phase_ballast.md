# H_048 — Overhauser-Locked Phase Ballast: nuclear-spin co-condensate (parallel D_s)

- **id**: H_048
- **slug**: overhauser-phase-ballast
- **escape_class**: (c) different rigidity — parallel stiffness donation from a non-electronic (nuclear-spin) reservoir
- **cluster**: stiffness sourced from a non-quasiparticle / non-electronic reservoir (within-cluster VARIANT of H_041 Yukawa-SYK incoherent-D_s and the H_032 multiband-donation manifold)
- **status**: closed-negative (confirms-wall)
- **date**: 2026-06-25
- **is_green**: false
- **absorbed**: false
- **run**: `state/h_048_overhauser-phase-ballast_2026_06_25/run.py` (stdlib-only, deterministic, byte-reproducible)

## Which premise / cluster this varies

The freeze's phase-stiffness ceiling rests on the relevant rigidity being the **electronic Q=0 superfluid weight**. The carded escapes that try to ADD rigidity from another reservoir (H_032 multiband donation borrows from another ELECTRON band; H_041 Yukawa-SYK incoherent stiffness) all confirm-wall via "no free lunch." This card tests the SPECIFIC twist not yet run: a genuinely **non-electronic** bath — the **nuclear-spin system** — acting as a SECOND, PARALLEL phase-rigidity reservoir, sourced by nuclear-moment density rather than carrier density. The isotope-monotonic falsifier (spin-I vs spin-0 even-even isotope on the same lattice) is a signature the freeze never tested.

## Hypothesis (frozen pre-register)

Treat the nuclear-spin bath as a co-condensate whose own phase rigidity adds in PARALLEL to the electronic superfluid weight: `rho_s = rho_el + lambda^2 * rho_nuc`, with `lambda = A_hf / W` and `T_BKT = (pi/2) rho_s`, where `A_hf` = contact-hyperfine energy, `W` = electron bandwidth, and `rho_nuc` = nuclear spin-wave stiffness of a high-moment/high-abundance isotope (51V, I=7/2). The escape CLAIM: the parallel nuclear ballast lifts `T_BKT` above the electronic-only ceiling, with a sizeable positive isotope contrast `Delta-T_BKT(spin-I vs spin-0) = (pi/2) lambda^2 rho_nuc`.

## Why it confirms the wall (mechanism + literature grounding)

Both factors in `lambda^2 * rho_nuc` are catastrophically small by INDEPENDENT grounded physics — they COMPOUND:
- **(N-a) Hyperfine weakness.** `A_hf ~ 1e-7..1e-6 eV` (MHz..hundreds-of-MHz hyperfine fields), `W ~ 1..10 eV`, so `lambda = A_hf/W ~ 1e-8..1e-6`, `lambda^2 ~ 1e-16..1e-12`. (Slichter; 51V s-d cancellation.)
- **(N-b) Nuclear ordering scale.** `rho_nuc` is set by RKKY nuclear ordering at nK..pK (Cu ~58 nK, Ag ~560 pK; enhanced 2DEG ~mK). So `rho_nuc/rho_el <= 1e-5`. (Oja-Lounasmaa RMP 69,1 1997; Simon-Loss arXiv:0709.0164.)

Compounded: ballast/rho_el ~ 1e-17 or smaller — 16+ orders too small. Isotope contrast ~4e-16 K vs the >=1 K needed. No-free-lunch: the donor either decouples (small lambda) or has no ambient rigidity (nK ordering) — here both.

## Probe

`run.py` encodes the parallel two-stiffness ansatz, sweeps lambda over the realistic metal range against rho_nuc over the grounded band (58 nK -> 1 mK) plus a charitable absurd overshoot (1000 K), computes `T_BKT=(pi/2)(rho_el+lambda^2 rho_nuc)` and the spin-I vs spin-0 isotope contrast. rho_el anchored so `(pi/2)rho_el = 164 K` (charitable). Deterministic, stdlib-only, byte-reproducible (sha verified x2).

## Falsifiers (pre-registered; PASS = NOT triggered; FAIL = escape-claim refuted)

1. **honest_null_ballast_cannot_reach_room_T** (DECISIVE) — T_BKT with realistic ballast < 293 K. TRIGGERED (FAIL).
2. **honest_null_ballast_negligible_vs_electronic** (decisive) — lambda^2 rho_nuc < 1e-3 rho_el. TRIGGERED (FAIL).
3. **isotope_contrast_unmeasurable** — Delta-T_BKT < 1 K (~4e-16 K). TRIGGERED (FAIL).
4. **absurd_overshoot_still_below_room_T** — even rho_nuc=1000K can't reach room-T (lambda^2 caps it). TRIGGERED (FAIL).
5. **joint_escape_unsatisfiable** — no realistic (lambda,rho_nuc) lifts T_BKT by >1 K. TRIGGERED (FAIL).
6. **electronic_anchor_consistency_guard** (sanity) — (pi/2)rho_el == 164 K exactly. NOT triggered (PASS).

Decisive honest-null TRIGGERED -> no escape. falsifiers_pass = 1/6 -> confirms-wall.

## Honest limits (>=5)

1. The parallel two-stiffness ansatz is the seed's OWN ungrounded construction; adopted charitably (most-favorable additive form), so the charity cannot bias toward confirm-wall.
2. A_hf/W and the nuclear-ordering band are order-of-magnitude literature values, not first-principles per-material; the ~16-order margin survives any O(1)..O(10) revision.
3. The isotope contrast assumes a spin-0 even-even reference zeroes the ballast; residual orbital/quadrupolar effects neglected (only smaller).
4. rho_nuc equated with the nuclear ordering temperature; the true spin-wave stiffness could differ by an O(1) prefactor, immaterial against the gap.
5. Electronic ceiling anchored to 164 K (top of band), not per-host — charitable; a lower per-host rho_el makes the ballast even more negligible.
6. In-silico-only closed-form scaling; the lab gate (absorbed=true) is out of domain and neither claimed nor needed.

## Verbatim run verdict (no LLM self-judge)

(see verbatim_stdout — confirms-wall, falsifiers_pass=1/6, is_green=False, absorbed=false)

## References (grounded — not fabricated)

- A.S. Oja, O.V. Lounasmaa, Rev. Mod. Phys. 69, 1 (1997). DOI 10.1103/RevModPhys.69.1 — RKKY nuclear ordering at nK (Cu ~58 nK) / pK (Ag ~560 pK).
- P. Simon, D. Loss, arXiv:0709.0164, PRL 98, 156401 (2007) — interaction-enhanced nuclear Curie T only into the mK range.
- C.P. Slichter, Principles of Magnetic Resonance — contact-hyperfine magnitudes (A_hf ~ 1e-7..1e-6 eV).
- 51V Knight-shift reviews (s-d hyperfine cancellation -> small net contact term).