# H_053 — Zero-Moment Stiffness Ladder (decoupled magnetic-vs-charge phase stiffness)

- **id:** H_053
- **slug:** zero-moment-stiffness-ladder
- **cluster:** spin-fluctuation / phase-stiffness ambient ceiling (`T_BKT = (pi/2)D_s`) — WITHIN-CLUSTER VARIANT
- **escape_class:** (c) different rigidity — supply high CHARGE superfluid stiffness from a metallic compensated altermagnet (zero net moment as a lattice-symmetry property, not carrier starvation)
- **date:** 2026-06-25
- **status:** closed-negative
- **verdict:** **confirms-wall**
- **is_green:** false · **absorbed:** false · **deterministic:** true (byte-equal ×2, md5 `633136f0a4e5a3cb3b919226610a3d3e`)
- **run:** `state/h_053_zero-moment-stiffness-ladder_2026_06_25/run.py`

## Frozen pre-register (BEFORE the run)

**Seed (triage "Genuinely-new in-silico escapes" #18).** A metallic compensated **altermagnet** (`n ~ 10^22 cm^-3`) supplies high CHARGE superfluid stiffness while magnetic compensation is a **lattice-symmetry property, not carrier starvation** — attacking the wall's under-weighted root (cuprate low-`D_s` is doped-Mott carrier *scarcity*). **Escape claim:** because `n` is ~10–100× the underdoped-cuprate density and compensation is symmetry-enforced, `D_s^eff > 7.4 meV` and `T_BKT` clears 164 K.

**HONEST-NULL (decisive):** `n` and the pairing-strength knob are **anti-correlated through the single altermagnetic spin splitting `J`**. (a) `J` is a momentum-dependent pair-breaking field (Chandrasekhar–Clogston / spin-sublattice locking, arXiv:2408.03999). (b) The high-`n` metal with large splitting (CrSb, ~1 eV) is depaired. (c) The pairing-compatible altermagnets are low-`n` semiconductors (MnTe, ~1.3 eV gap). (d) The apparent high-`n` zero-moment "free lunch" RuO2 is nonmagnetic (μSR/Mössbauer/neutron). So `D_s^eff = min(D_s^charge(n), K·Δ(J))·P_pair(J,Δ)` stays below the wall for every REAL host.

**Method (research-first).** Web search 2026-06-25 confirmed: altermagnet pairing constraints (arXiv:2408.03999/PRB zylh-rqxl), RuO2 nonmagnetic (npj Spintronics s44306-024-00055-y; Cell Rep.Phys.Sci. S2666-3864(25)00451-5), CrSb ~1 eV splitting (Nat.Commun. s41467-024-46476-5), MnTe 1.3 eV gap (arXiv:2603.00242). Closed-form superfluid-weight model `D_s^sf = min(full-Drude(n,d,m*), K_cap·Δ(J))·P_pair(J,Δ)` with Δ sourced from the same J (Δ=min(0.3·J, 30 meV)).

## Verbatim run verdict (no LLM self-judge)

```
VERDICT: confirms-wall
  honest-null (F1) shows a REAL host clears wall? False   real-host margin = -91.467 K
  falsifiers_pass = 3/4
  best REAL host RuO2: D_s^sf=2.3333 meV -> T_BKT=42.533 K (-91.467 K vs 134 K)
  [PASS] honest_null_real_host_clears_wall  [PASS] real_high_n_and_pairing_coexist
  [FAIL] uncapped_drude_clears_wall_positive_control  [PASS] real_host_reaches_room_T
```

**falsifiers_pass = 3/4.** F1 (decisive honest-null) NOT triggered → escape refuted. F3 is the positive control, TRIGGERED by design (uncapped Drude 1436 meV clears wall, proving the wall is held by the gap-cap+depairing not carrier scarcity). decisive_null_triggered=false.

## Falsifiers (≥4; honest-null decisive)

1. **F1 `honest_null_real_host_clears_wall` (decisive) — NOT triggered (PASS).** Best real host RuO2: D_s^sf=2.33 meV → T_BKT=42.5 K, −91.5 K below wall. CrSb depaired (P_pair=0), RuO2 gap-capped (Δ=3 meV), MnTe low-n (2.8 meV), semimetal depaired.
2. **F2 `real_high_n_and_pairing_coexist` — NOT triggered (PASS).** No real host has both Drude≥wall AND honest D_s^sf≥wall: n and pairing-survival do not decouple.
3. **F3 `uncapped_drude_clears_wall_positive_control` — TRIGGERED (FAIL by design).** Uncapped Drude 1436 meV ≫ wall: high n gives huge Drude weight, but the wall lives in the gap-bounded superfluid weight.
4. **F4 `real_host_reaches_room_T` — NOT triggered (PASS).** Best D_s^sf (2.33 meV) far below 293 K target (16.07 meV).

## Honest limits (≥5)

1. The carrier-density premise is REAL (eV-scale Drude weight, no Mott throttle); the bottleneck relocates to the gap-bounded superfluid weight.
2. The gap cap `D_s^sf ≤ K·Δ` is a closed-form bound (Hazra-Verma-Randeria PRX 9 031049; Emery-Kivelson Nature 374 434), not a Kubo-BdG ED; K_cap=1 generous; real ED lands at-or-below.
3. P_pair and CHI_EVADE=0.20 (80% symmetry evasion of the staggered splitting) are steel-man-generous; fully-evaded would be the unphysical free lunch.
4. Δ=min(0.30·J, 30 meV) generous on both knobs (30 meV ≈ 200 K mean-field T_c); larger only helps the escape.
5. The "goldilocks" apparent escape is a FICTIONAL host requiring an unmeasured 30 meV altermagnetic gap = the separate glue wall (H_032-035), correctly excluded from the decisive null (tune-to-green avoided).
6. RuO2 magnetism contested; handled conservatively (residual J=10 meV); wall holds whether J=10 or 0.
7. No fabricated citations; in-silico-only; absorbed=false.

## Conclusion

A metallic compensated altermagnet carries eV-scale charge Drude weight with no Mott-doping scarcity (F3 positive control confirms ~1.4 eV Drude). But T_BKT is set by the gap-bounded superfluid weight, and the altermagnetic gap is sourced by and depaired by the same J: nonmagnetic high-n (RuO2) → Δ→0; large-J metal (CrSb) → depaired; pairing-compatible (MnTe) → low-n semiconductor. Best real-host D_s^sf=2.33 meV → T_BKT=42.5 K, 91 K short of the 134 K wall. The only escape requires a fictional 30 meV-gap host, relocating the bill to the glue wall. **Confirms the wall** in the carrier-density / zero-moment-altermagnet channel — same no-free-lunch as the 12 prior SF-escape probes.

## Refs

- arXiv:2408.03999 / PRB 10.1103/zylh-rqxl (constraints on SC pairing in altermagnets)
- Nat.Commun. 10.1038/s41467-024-45951-3 (finite-momentum Cooper pairing)
- npj Spintronics 10.1038/s44306-024-00055-y (RuO2 nonmagnetic, μSR+neutron); Cell Rep.Phys.Sci. S2666-3864(25)00451-5 (Mössbauer) + PMC12852566 (consensus)
- Nat.Commun. 10.1038/s41467-024-46476-5 + arXiv:2405.12687/2405.12575 (CrSb ~1 eV g-wave splitting)
- arXiv:2603.00242 (α-MnTe 1.3 eV-gap semiconductor)
- Hazra-Verma-Randeria PRX 9 031049 (2019); Emery-Kivelson Nature 374 434 (1995) (gap-bounded D_s)