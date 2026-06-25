# H_056 — CLS-Phonon Hybrid Glue (Friedrich-Wintgen BIC reservoir)

- **id:** H_056
- **slug:** cls-phonon-hybrid-glue
- **cluster:** spin-fluctuation / phase-stiffness ambient ceiling (T_BKT=(π/2)·D_s) — within-cluster variant
- **escape_class:** (a) borrow stiffness from a co-located dispersive reservoir while pairing stays on a flat branch (interference-decoupled flat band, BIC channel)
- **date:** 2026-06-25
- **status:** closed-negative
- **verdict:** **confirms-wall**
- **is_green:** false · **absorbed:** false · **deterministic:** true (byte-equal ×2, sha256 `dd86f1084253…`)
- **violated_freeze_premise:** single-particle-flattened / clean band — the BIC co-locates a flat (pairing) and a dispersive (stiffness) branch at the SAME energy by destructive interference
- **run:** `state/h_056_cls-phonon-hybrid-glue_2026_06_25/run.py`

## Frozen pre-register
Seed (triage genuinely-new escape #21). A Friedrich-Wintgen BIC co-locates a flat (pairing, high-DOS) band and a dispersive continuum band of bandwidth W_cont at the SAME energy by destructive interference; pairs draw DOS from the flat branch while coherence rides the continuum.

**Escape claim:** condensate weight sits in the flat branch WHILE D_s ~ |U|·n_pair·(W_cont-derived) GROWS with W_cont, so T_BKT clears the ~134–164 K flat-band-only limit.

**HONEST-NULL (decisive):** D_s is INDEPENDENT of W_cont because a FW BIC is, by construction, the supermode whose net coupling to the continuum channel is identically zero (destructive-interference cancellation). Zero coupling = zero transport overlap with the dispersive band ⇒ continuum donates no stiffness ⇒ condensate pinned to the flat branch ⇒ wall holds.

Violated premise: single-particle-flattened/clean-band (of the freeze's 5). Method: deterministic stdlib-only two-resonance/one-channel FW model; dark BIC supermode ∝ (√γ_cont, −√γ_flat) with computed (not hand-zeroed) channel coupling √γ_flat·√γ_cont − √γ_cont·√γ_flat = 0; Kubo D_s = |U|·n_pair·[w_flat·s_flat + O·w_cont·s_cont(W_cont)], continuum term gated by the physically computed BIC→continuum overlap O, s_cont ~ W_cont, s_flat calibrated to the 164 K ceiling; sweep W_cont 0→1600 meV at fixed gap + BIC condition, plus a no-free-lunch detuning contrast. Escape passes only if O>0 with margin AND T_BKT clears the wall as a genuine BIC. No tune-to-green.

## Research-first (cited)
- Hsu, Zhen, Stone, Joannopoulos, Soljačić, "Bound states in the continuum," Nat. Rev. Mat. 1, 16048 (2016): FW BIC = complete destructive interference of two resonances through a shared channel ⇒ dark supermode has ZERO coupling to the continuum.
- Friedrich & Wintgen, Phys. Rev. A 32, 3231 (1985): two-resonance/one-channel construction; BIC condition V(γ₁−γ₂)=√(γ₁γ₂)(E₁−E₂) makes one supermode's width vanish.
- arXiv:2504.19573 (2025): rigorous FW-BIC existence; BIC = zero-net-coupling supermode.
- Peotta & Törmä, Nat. Commun. 6, 8944 (2015); D_s ≤ e_n|U|Ω/2 (PNAS 118 e2106744118 2021; arXiv:2304.07318): a condensate's stiffness is set by the branch it occupies, not by a band it has zero overlap with.

## Verbatim run verdict
(see verbatim_stdout: O=0 for all W_cont 0→1600 meV; D_s pinned at 8.9970 meV / T_BKT=164.000 K; contrast eps>0 gains stiffness only with still_BIC=False; falsifiers_pass=5/5; VERDICT=confirms-wall)

## Falsifiers (5) — outcome
1. honest_null_zero_continuum_overlap (decisive) — triggers if O>1e-9 — PASS (O=0.000 exactly; continuum decoupled).
2. Ds_grows_with_Wcont — triggers if D_s grows >5% — PASS (growth=0).
3. Tc_clears_cluster_wall — triggers if T_BKT>164 K — PASS (pinned at 164 K).
4. Tc_reaches_room_T — triggers if T_BKT≥293 K — PASS (164<293).
5. free_lunch_continuum_donation_keeps_BIC (no-free-lunch witness) — triggers if a wall-clearing state stays a BIC — PASS (eps>0 states have still_BIC=False).

All 5 not triggered ⇒ escape mechanism absent at every test point ⇒ confirms-wall.

## Honest limits (≥5)
1. Two-resonance/one-channel reduction, not full two-channel lattice ED (A₂(K,ω) on cross-stitch/diamond chain) — pool-tier upgrade; can only confirm the FW cancellation.
2. s_cont ~ W_cont is a closed-form Drude proxy, not a self-consistent BdG Kubo tensor — conservative for the escape (most generous continuum stiffness, still gated to 0 by O=0).
3. Flat-branch kernel calibrated to the 164 K high edge — generous to the escape; verdict independent of exact ceiling.
4. Single-energy (dE=0) BIC degeneracy; finite detuning IS the contrast (re-opens channel, destroys BIC). Per-k cancellation is the same identity.
5. Mean-field/equilibrium BKT ceiling T_BKT=(π/2)D_s over-counts T_c — generous to escape, still fails.
6. No interaction-dressing of the continuum — would only help the wall (a dressed finite-width BIC is a leaky resonance, forfeiting the flat-branch advantage). Clean-BIC limit is the most favorable case and still confirms.

## Ledger note
Within-cluster SF-escape variant (BIC/interference-decoupled-flat-band lever). Confirms the wall: a FW BIC co-locating a flat (pairing) and dispersive (stiffness) branch does NOT let the continuum donate stiffness, because the BIC is by definition the supermode of zero coupling to the continuum channel. The transport overlap carrying the continuum's bandwidth-derived stiffness is identically the channel coupling the BIC nullifies ⇒ D_s independent of W_cont (0→1600 meV), condensate pinned at 164 K. No-free-lunch witness sharp: donation purchasable only by detuning off the BIC condition (state becomes leaky/decaying). Deterministic, byte-equal ×2 (sha256 dd86f1084253…). absorbed=false, is_green=false. Kept as a negative result.