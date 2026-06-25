# H_059 — Pinning-Memory Ratchet (Glassy-Phason Non-Equilibrium Stiffness Ballast)

- **id:** H_059 · **slug:** pinning-memory-ratchet · **date:** 2026-06-25
- **status:** closed-negative · **verdict:** confirms-wall
- **is_green:** false · **absorbed:** false · **deterministic:** true
- **cluster:** spin-fluctuation / phase-stiffness ambient ceiling (T_BKT = (pi/2) rho_s; Emery-Kivelson) — within-cluster variant
- **escape_class:** (a) borrow stiffness from a non-electronic reservoir — a PINNED STRUCTURAL GLASS (overdamped-phason / TLS bath) added to the phase action as a memory kernel, with NO Leggett mode to the SC condensate
- **siblings:** H_032 (electronic multiband donation), H_048 (Overhauser nuclear ballast), H_041 (Yukawa-SYK incoherent D_s)
- **run:** state/h_059_pinning-memory-ratchet_2026_06_25/run.py

## Frozen pre-registration

Seed phase action S = (1/2)∫d²r dτ[rho_s^el(∇θ)² + chi_glass(ω)(∂_τθ)²], chi_glass(ω)=Σ_i w_i Γ_i/(ω²+Γ_i²), kernel from Jiang-Zaccone-Setty-Baggioli PRB 108 054203 (2023)=arXiv:2305.05407. Escape: the pinned glass lifts rho_s^eff above (2/π)k_B·164 K so T_BKT=(π/2)rho_s^eff>164 K. Frozen criterion (no LLM self-judge): escapes-wall iff BOTH decisive honest-nulls (N1 frequency-mismatch, N2 wrong-channel) PASS with a real margin. Honest expectation: confirm-wall.

## Decisive honest-null (load-bearing — NOT engineered around)

chi_glass multiplies (∂_τθ)² — a TEMPORAL (compressibility) term, NOT the spatial rho_s(∇θ)² that Nelson-Kosterlitz turns into T_BKT. N1: glass is slow (Γ_i≪ω_J), so at the vortex/Josephson scale chi_glass(ω→ω_J)~Σw_iΓ_i/ω_J²→0; only static chi_glass(0)=Σw_i/Γ_i is large but that is the compressibility. N2 (stronger): even chi_glass(0) feeds the temporal term; T_BKT=(π/2)J depends on SPATIAL stiffness only, so dT_BKT/dchi_glass=0 for ANY w_i,Γ_i. No free lunch: a glass rigid enough to add static weight is too slow AND in the wrong channel.

## Falsifiers (PASS = NOT triggered)

| # | name | role | result |
|---|------|------|--------|
| F1 | honest_null_N1_glass_decoupled_at_vortex_scale | DECISIVE (freq mismatch); triggered when surviving frac chi(ω_J)/chi(0)<1e-3 | FAIL (frac=9.9991e-7) |
| F2 | honest_null_N2_temporal_kernel_does_not_enter_TBKT | DECISIVE (wrong channel); triggered when honest T_BKT=electronic-only to machine precision | FAIL (T_BKT=164.00 K) |
| F3 | honest_TBKT_below_room_target | triggered when real-channel T_BKT<293 K | FAIL (164<293) |
| F4 | frequency_cut_TBKT_below_ceiling | triggered when charitable freq-cut spatial-add ≤164 K | PASS (164.64 K — surviving weight negligible) |
| F5 | glass_is_slow_guard | charity witness: every Γ_i<ω_J AND chi(0)>rho_s^el | PASS (strongest slow glass tested) |

falsifiers_pass = 2/5. Both decisive nulls (F1,F2) TRIGGERED ⇒ confirms-wall. (The naive static-add the escape requires gives an absurd 6.4e5 K, printed to flag the unphysical reading.)

## Honest limits

1. Toy closed-form / Nelson-Kosterlitz channel argument, not self-consistent dynamical glass+BdG Eliashberg; magnitude of any real coupling not solved.
2. Single charitable host anchor: (π/2)rho_s^el pinned to band TOP (164 K); real flat-band D_s is 1–8 K (wall harder).
3. ω_J taken small (10 meV) — most favorable for a slow bath; larger ω_J deepens the mismatch. Conservative.
4. Glass (w_i,Γ_i) illustrative, not material-fit; but N2 verdict is parameter-independent (exactly zero) and N1 holds for any slow bath (Γ≪ω_J).
5. The pairing-axis escape is NOT tested: arXiv:2305.05407's real result (phason-Eliashberg vertex, non-monotonic T_c) is the glue axis (H_032/H_041 manifold), a different lever — a separate card.
6. Non-equilibrium "ratchet"/driven framing not modeled (would face H_022/H_034 driven-transient closure).
7. In-silico only; no host claimed to BE an RTSC; absorbed=false (lab gate out of domain).

## References (verified)

- Jiang, Zaccone, Setty, Baggioli, Phys. Rev. B 108, 054203 (2023) = arXiv:2305.05407 (verified web search 2026-06-25)
- Nelson & Kosterlitz, PRL 39, 1201 (1977)
- Emery & Kivelson, PRB 52, 6122 (1995)
- Benfatto, BKT-films review (cond-mat.de/events/correl24)

(Full verbatim stdout stored in the card and in verbatim_stdout; run byte-identical x2, md5 e97a4ba7f6462567d514e48e86f5a9c7.)