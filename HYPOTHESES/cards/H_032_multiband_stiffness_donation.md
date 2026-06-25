# H_032 — Multi-channel stiffness donation (escape class (a): borrow stiffness)

- **id:** H_032 · **slug:** multiband-stiffness-donation · **escape_class:** (a) borrow stiffness
- **status:** CLOSED-negative (🔴) — `confirms-wall` · **absorbed:** false · **is_green:** false · **created:** 2026-06-25
- **run:** `state/h_032_multiband-stiffness-donation_2026_06_25/run.py` (stdlib-only, deterministic, byte-equal x2; sha256 `733ac01b…`)

## Hypothesis (frozen)
Pairing lives on the flat band (high QGT/DOS), but `D_s` is **donated** by a co-resident high-v_F dispersive band — pairing and stiffness as different k-space objects. If they add freely, `D_s_total = D_s_flat + D_s_disp` could clear the ~134–164 K spin-fluctuation/phase-stiffness ceiling (Emery–Kivelson, `T_BKT=(π/2)D_s`) toward 293 K.

## Why it could escape (grounded)
Multiband superfluid weight IS additive in the diamagnetic/f-sum sense; "giant amplification" of T_BKT from cooperative two-band interplay is reported (arXiv:2311.17511, arXiv:2511.16385).

## Honest null (decisive, NOT engineered around)
**Leggett softening + v_F decoupling.** Donated stiffness reaches the order-parameter phase only via interband Josephson J; the relative-phase (Leggett) mode costs energy ∝ J (arXiv:1408.5938, arXiv:1704.00333). The quantum-metric **no-go** (arXiv:2604.04719) is a trade-off: max flat-band pairing needs the band ISOLATED, max locking J needs strong hybridization — incompatible. Strong J that donates fully DESTROYS the pairing. Conserves `Tc=min(T_pair,T_phase)`.

## Central scaling (closed form)
`η_donate(x)=x`, `s_pair(x)=1−x`; `D_s_eff=D_s_flat(1−x)+D_s_disp·x(1−x)`; `T_phase=(π/2)D_s_eff`; `T_pair=164·(1−x)`; `Tc=min`. Donor term `x(1−x)` maxes at **1/4** — can never donate >¼ of bare dispersive stiffness.

## Result
Best `x*=0.3214` → **Tc=111.29 K** at the crossover `T_phase≈T_pair≈111.3 K`; 52.7 K below the 164 K ceiling, 181.7 K below 293 K. Naive additive fantasy 483.8 K collapses ~77%. `confirms-wall` — publishable closed-negative. `absorbed=false`.

## Falsifiers (4; PASS = not triggered)
1. **honest_null_leggett_nogo_escape** (DECISIVE) — best Tc>164 K → NO (margin −52.7 K).
2. **reaches_room_T_target** — Tc≥293 K → NO (111.3 K).
3. **free_additive_donation_realized** — Tc≥50% of additive fantasy → NO (23%; gate dominates).
4. **pairing_stiffness_tradeoff_broken** — one channel >3× the other → NO (ratio≈1; conserved).

## Honest limits (≥5)
1. Toy linear gates `η=x`, `s=1−x`; real non-linear, the ¼ cap exact only for this product form. 2. J parameterized by x, not from real bandstructure/cRPA. 3. Donor `D_s_disp=300 K` already 3× cuprate-class; real likely less → more negative. 4. Strict 2D-BKT; a 3D donor (~1.84×) → ~205 K, still misses 293 K. 5. No competing order (CDW/AFM could pre-empt SC). 6. Single knob x; real heterostructures have more independent levers. 7. No LLM self-judge — verdict is verbatim program output.

## Cross-links
PR#40 wall; H_001/H_006/H_007/H_031; `tool/rtsc_harness.py`. Anchors: Emery–Kivelson PRB1995, arXiv:2604.04719, arXiv:2311.17511, arXiv:2511.16385, arXiv:1408.5938, arXiv:1704.00333, arXiv:2203.11133.

## Verbatim verdict
```
falsifiers_pass=4/4
VERDICT: confirms-wall
best Tc=111.2904 K @ x*=0.3214 ; margin vs 164 K ceiling = -52.7096 K
```