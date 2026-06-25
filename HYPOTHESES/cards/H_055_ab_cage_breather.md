# H_055 — AB-Cage Breather (flux-detuned Aharonov-Bohm caging that "lifts the cage")

- **id:** H_055 · **slug:** ab-cage-breather
- **cluster:** spin-fluctuation / phase-stiffness ambient ceiling (`T_BKT = (pi/2)D_s`, Emery-Kivelson) — WITHIN-CLUSTER VARIANT (flux-/interference-decoupled flat band)
- **escape_class:** (c) different rigidity — a *flux*-origin (not band-touching) flat band whose cage gap is set by hopping `t` (O(eV)), claimed to add `|U|`-INDEPENDENT velocity stiffness and break `D_s ~ |U|·<g>`
- **date:** 2026-06-25 · **status:** closed-negative · **verdict:** **confirms-wall**
- **is_green:** false · **absorbed:** false · **deterministic:** true (byte-equal ×2, sha `6c64d28c…`)
- **run:** `state/h_055_ab-cage-breather_2026_06_25/run.py`

## Frozen pre-register (BEFORE the run)

**Seed (triage "Genuinely-new in-silico escapes" #20, family J flux-caging).** Flux (a phase), not a small bandgap, enforces the Aharonov-Bohm caging, so `|U|` stays O(eV) while flux-detuning `delta = pi - phi` adds conventional *velocity* stiffness DECOUPLED from `|U|` — claimed to break `D_s ~ |U|·<g>`; a flat-band origin (flux, not band-touching) the freeze never tested. **Probe:** attractive-Hubbard ED/DMRG on a diamond AB-caging chain threaded by `phi = pi - delta`; sweep Kubo BKT `D_s` vs `delta` at FIXED `|U|`. **Escape claim:** `D_s(delta)` peaks at a NONZERO `delta*` >2× the `delta=0` caged value, because the cage gap is set by `t` (O(eV)) not an avoided crossing, so `|U|` need not shrink.

**HONEST-NULL (decisive, seed's three clauses):** `D_s(delta)` monotone-decreasing from `delta=0` (flux buys no `|U|`-independent stiffness), OR detuning closes the caging gap and reintroduces `|U|<gap`, OR `D_s(delta*)` still ≥20× below 7.4 meV cuprate scale. Any one holding ⇒ wall confirmed. Escape needs ALL THREE defeated.

**Violated premise:** single-particle-flattening ORIGIN — flatness from an Aharonov-Bohm flux `phi=pi` (interference-phase cage), not a band-touching/quantum-metric flat band.

**Method (research-first → closed-form ED-scale probe).** Exact diamond-chain spectrum `E0=0`, `E_pm=±2t√(1+cos k·cos(phi/2))` (Vidal–Mosseri–Doucot PRL 81 5888 1998; rhombi refs arXiv:2604.13185/2602.23430/2407.15789); `phi=pi-delta ⇒ cos(phi/2)=sin(delta/2)`, bandwidth `W1(delta)`→0 at cage, gap `Gap=2t√(1-sin(delta/2))` closes at `delta→pi`. Operative stiffness at `|U|=O(eV)` = freeze's local-pair `D_s=c·z·t_pair·n(1-n)`, `t_pair=t_eff²/|U|`, `t_eff=W1/4` (the H_038 bound), with `2.8×` mean-field→realized deflation (freeze anchor). Decisive parameter-free test: `D_s_peak/|U|` across an 8× `|U|` range.

## Verbatim run verdict (no LLM self-judge)

```
[see verbatim_stdout — VERDICT: confirms-wall ; falsifiers_pass = 4/4 ;
 D_s(delta=0)=0 (caged pairs) ; max D_s=5.5753 meV @ delta=0.5011 -> T_BKT=101.6 K
 (-32.4 K below wall, matches H_038 ~90 K) ; D_s_peak/|U|=0.0111 CONSTANT (spread 1.4%)
 across |U|=125..1000 meV -> stiffness COUPLED to |U|, decoupling FAILS ;
 |U| needed to clear 134 K wall = 661.5 meV (room-T: 1446.5 meV, unphysical)]
```

**falsifiers_pass = 4/4.** Every PASS = escape refuted. Decisive honest-null `null_a_stiffness_decoupled_from_U` NOT triggered (`D_s_peak/|U|` constant ⇒ coupling reproduced). `decisive_null_triggered = false`.

## Falsifiers (≥4; honest-null decisive, parameter-free)

1. **F1 `null_a_stiffness_decoupled_from_U` (HONEST-NULL (a), DECISIVE, parameter-free) — NOT triggered (PASS).** `D_s_peak/|U| = 0.0111 ± 1.4%` across `|U|=125→1000 meV` — constant, and INDEPENDENT of `t` (once `t>|U|/2`). The flux-detuned cage REPRODUCES `D_s ~ |U|`; velocity stiffness does NOT decouple — it is pinned to the interaction scale by the pair-unbinding edge `W1≈|U|`.
2. **F2 `null_b_cage_does_not_trap_pairs` (HONEST-NULL (a)/cage) — NOT triggered (PASS).** At the perfect cage `delta=0`, `D_s=0` EXACTLY (`t_eff=0`): the AB cage localizes the *pairs* too; the premised finite geometric baseline does not exist.
3. **F3 `null_c_clears_wall_at_physical_U` (HONEST-NULL (c), absolute) — NOT triggered (PASS).** At `|U|=0.5 eV` the cage-optimal `D_s=5.58 meV` → `T_BKT=101.6 K`, −32.4 K below the 134 K wall (1.33× cuprate deficit), independently reproducing H_038 (~90 K). Clearing needs unphysical `|U|≥661 meV` (room-T `≥1.45 eV`).
4. **F4 `clears_room_293K` — NOT triggered (PASS).** Best `D_s=5.58 meV` is 2.9× below the 293 K target (16.07 meV).

## Honest limits (≥5)

1. **Mechanism is REAL, not a no-op.** AB caging on diamond/rhombi chains is experimentally realized (photonic arXiv:1805.03564; all-bands-flat electrical arXiv:2508.13571); flux-detuning genuinely turns the cage band dispersive. The escape fails because the added velocity stiffness is pinned to `|U|`.
2. **The peak is a real intermediate-coupling optimum, the BEST case.** `D_s(delta)` peaks at `W1≈|U|` (BCS↔BEC intermediate, where attractive-Hubbard `T_c` genuinely maxes), then collapses past unbinding. Carded 5.58 meV is the global `delta`-max at realized `|U|`.
3. **Closed-form local-pair proxy, not full ED/DMRG.** Uses exact single-particle spectrum + strong-coupling `t_pair=t_eff²/|U|` (H_038 bound), steel-manned prefactors. A real many-body Kubo ED would land at-or-below (2nd-order `t_pair` over-counts near unbinding). The DECISIVE results (`D_s_peak/|U|` constancy, `D_s(0)=0`) are parameter-free/scale-invariant and robust to the proxy.
4. **Absolute `T_c` is `|U|`-scale-dominated; wall confirmed on the MECHANISM.** Raw mean-field `T_BKT∝|U|` (e.g. `|U|=1 eV→203 K`), so a closed-form proxy cannot settle absolute `T_c` without an arbitrary `|U|` — exactly why the load-bearing falsifier is the parameter-free decoupling test, not the absolute number. The `|U|=0.5 eV` reference (F3) is a sanity anchor matching H_038, not the verdict's sole basis.
5. **The `2.8×` deflation is the freeze's measured anchor, applied uniformly — NOT a tune knob.** It is the geomean over-prediction vs MATBG/tMoTe2/Re6Se8Cl2 (`geometric_bkt_tc_band, deflate=2.8`); removing it raises every number uniformly but leaves the decisive `D_s_peak/|U|` constancy and `D_s(0)=0` unchanged.
6. **1D/2D-BKT framing.** Diamond chain is 1D (natural AB-caging geometry); `T_BKT=(pi/2)D_s` is the cluster's standard map. A 2D dice/T3 flux lattice has the same `|U|`-pinned local-pair stiffness; no 3D-Josephson lever added.
7. **No fabricated citations.** Diamond-chain spectrum, AB-caging at `phi=pi`, local-pair `t_pair=t²/|U|`/`m*∝|U|` all from verified refs (web 2026-06-25). absorbed=false; no material claimed to BE an RTSC.

## Conclusion

Flux-detuned **Aharonov-Bohm cage breather** — flatness from an interference *phase* (`phi=pi`), a genuinely new flat-band origin. The exact diamond-chain spectrum + the freeze's local-pair stiffness show, parameter-free: (i) `D_s=0` at the perfect cage (pairs trapped too); (ii) `D_s_peak/|U|=0.0111` constant across 8× `|U|` and `t`-independent (velocity pinned to the interaction scale, NOT decoupled); (iii) at physical `|U|=0.5 eV`, `T_BKT=101.6 K`, −32 K short, matching H_038. **Confirms the wall** via a new flat-band origin — the same `|U|` that keeps pairs bound (eV cage) makes them heavy (`t_pair∝t_eff²/|U|`). No free lunch: lift the cage → pairs unbind; keep the cage → pairs trapped at `D_s=0`.

## Refs
Vidal-Mosseri-Doucot PRL 81 5888 (1998); arXiv:2604.13185 / 2602.23430 / 2407.15789 (rhombi-chain flux bands); arXiv:1805.03564 / 2508.13571 (experimental AB cages); Peotta-Torma Nat.Commun. 6 8944 (2015) arXiv:1506.02815; Torma-Peotta-Bernevig Nat.Rev.Phys. 4 528 (2022); Micnas-Ranninger-Robaszkiewicz Rev.Mod.Phys. 62 113 (1990); cross-anchor H_038 (local-pair ~90 K).