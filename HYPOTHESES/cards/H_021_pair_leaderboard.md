---
id: H_021
slug: pair-leaderboard
title: A×B pair leaderboard over the candidate registry — CoSn/hBN/Ta2NiSe5 tops it (only fully-verified box-clearing pair, ~252 K coordinate); all higher-Tc pairs are gap-blocked (unverified ⟨g⟩ or competing-order glue)
domain: rtsc
status: model-probe
exploration_method: closed-form ranking of all A×B registry pairs against the +@ box
verification_method: W1 (pre-register frozen) + W2 (falsifier-5) + W3 (deterministic) + W5 (honest-limits-5)
deterministic: true
llm: none
pre_register_frozen: true
frozen_at: 2026-06-25
compute: fleet lane (named-candidate deepen)
---

# H_021 — A×B pair leaderboard (rtsc)

## Hypothesis

Ranking EVERY layer-A × layer-B pair in `tool/rtsc_candidates.py` against the +@ box (using ONLY
verified property values; unverified → the pair is gap-blocked) yields a leaderboard whose top is
the only fully-verified box-clearing pair. Test: is CoSn/hBN/Ta2NiSe5 the lead, and are all
higher-Tc pairs blocked by a named gap (not a fabricated value)?

## Why

Operationalizes "which named trio is closest" — the leaderboard makes the 🟠 state concrete and
shows exactly which gap (unverified ⟨g⟩, or a competing-order glue) blocks each higher pair, so
each research round knows what to verify next.

## Falsifiers (≥5 — pre-registered)

- **F1_verified_pair_exists**: PASS = ≥1 fully-verified box-clearing pair exists.
- **F2_leaderboard_monotone**: PASS = ranking is monotone in the computed Tc.
- **F3_no_fabricated_values**: PASS = only verified registry values used.
- **F4_best_is_CoSn_Ta2NiSe5**: PASS = the top fully-verified pair is CoSn/hBN/Ta2NiSe5.
- **F5_gaps_named**: PASS = every blocked pair names its specific gap.

## Honest Limits (≥5)

- **L1**: Tc is the calibrated BKT coordinate (H_018 scatter), not a prediction.
- **L2**: the box check uses verified per-layer values; the PAIR working together is unmeasured (jointly unrealized).
- **L3**: the registry is small/incomplete — a missing material could outrank the lead.
- **L4**: "gap-blocked" reflects what is unverified TODAY; filling a gap may qualify or disqualify a pair.
- **L5**: `absorbed=false`; no claim any pair IS an RTSC.

## Cross-Links

- tool/rtsc_candidates.py (the registry ranked here) · H_020 (the lead's amplitude verdict) ·
  the backup-candidate research (state/research-backup-candidates-2026-06-25.md — the rows to add next).

## Verdict

**🟡 MODEL-PROBE → CREDIBLE-PARTIAL (CoSn/hBN/Ta2NiSe5 leads).** Verbatim stdout
(`state/h021_pair_leaderboard_2026_06_25/run_h021.py`):

```
BEST fully-verified pair : CoSn/hBN/Ta2NiSe5  in_box=True  bkt_Tc_2D=136.8K  bkt_Tc_3D=251.6K
BEST if-gaps-filled pair : CsV3Sb5/hBN/Ta2NiSe5  bkt_Tc_3D_if_filled=251.6K  (needs: A.g_mean(CsV3Sb5))
  CoSn/hBN/1T-TiSe2     Tc3D_if_filled= n/a   gaps: B.boson_meV(1T-TiSe2): unknown
  falsifiers: 5/5 PASS  all_pass=True
VERDICT: 🟠 CREDIBLE-PARTIAL — CoSn/hBN/Ta2NiSe5 tops the leaderboard (best of two box-clearing
  pairs; ties Nb3Cl8/hBN/Ta2NiSe5 on bkt, wins on g=2.87>2.11). bkt_Tc_3D=251.6K @ coordinate;
  trio JOINTLY UNREALIZED, bkt_Tc is a COORDINATE not a prediction. absorbed=false. Strongest 🟠.
```

- **structural_finding**: CoSn/hBN/Ta2NiSe5 is the only fully-verified box-clearing pair (~252 K
  coordinate). Higher-Tc pairs are gap-blocked: CoSn/1T-TiSe2 would clear room-T (1T-TiSe2's mode
  is ~400 meV per the backup research) but its boson_meV is unregistered AND it carries a CDW
  (competing-order gap). The leaderboard makes the 🟠→🟢 path concrete: fill 1T-TiSe2's energy +
  break its CDW (H_016 frustration), OR verify ⟨g⟩ of a backup flat-band metal. absorbed=false.
- **record**: `state/h021_pair_leaderboard_2026_06_25/result.json`.
