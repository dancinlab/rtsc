# rtsc

Room-temperature superconductor (RTSC) discovery as an **honest falsification
framework** — predict/screen candidates, run the falsifier cascade, and report
negative rulings as results. Target = 293 K @ 1 atm. Materials carried over from
the demiurge repo (this is the dedicated home for the RTSC campaign).

## Structure

```
rtsc/
├─ src/              — predictor / screening / ED-solver tools (flat-band geometry, kubo stiffness, deck builders)
├─ state/            — all work artifacts (ledger · exports · campaign state · papers · domain spec), git-tracked
│  ├─ RTSC_LEDGER.jsonl          — per-material campaign ledger (SSOT)
│  ├─ RTSC_HARVEST_PARTIAL.jsonl — partial harvest log
│  ├─ rtsc.demi                  — 7-verb pipeline manifest
│  ├─ exports/                   — per-material verdict records + turnkey decks
│  ├─ campaign/                  — rtsc-* campaign sub-states
│  └─ papers/                    — RTSC papers (incl. the closed-negative flat-band paper)
├─ ARCHITECTURE.json — final architecture SSOT (JSON `children` tree, update-in-place)
├─ architecture.html — human viewer for the JSON (run `python3 serve.py`)
└─ CHANGELOG.md      — history (append-only)
```

## Rules

- **Falsifier-first / honest (commons honesty).** All gates stay GATE_OPEN /
  absorbed=false. No candidate is claimed to BE an RTSC. `absorbed=true` requires
  accredited 4-probe transport + Meissner expulsion + measured H_c2 / T_c.
- **Every active hypothesis gets a card (no orphan hypotheses).** Any hypothesis under investigation
  MUST have its own pre-registered `HYPOTHESES/cards/H_*.md` — frozen predictions + ≥4 measurable
  falsifiers + ≥5 honest limits + the **verbatim** run verdict (no LLM self-judge) + a row in
  `HYPOTHESES/HYPOTHESES.jsonl`. The card is created BEFORE/as the hypothesis is run, not after; a
  hypothesis is never pursued, reported, or carried in the ledger without its card. Negative /
  inconclusive / deferred verdicts are still carded (kept as results). One card per hypothesis,
  canonical `H_NNN_<slug>.md`, update-in-place.
- **In-silico-only domain (scope boundary).** This campaign's domain is IN SILICO — predict /
  screen / simulate / falsify by computation. Physical synthesis, fabrication, doping-to-spec, and
  accredited measurement (the `absorbed=true` gate) are **OUT OF DOMAIN**: a hand-off to the
  laboratory, never our failure and never computationally satisfiable. **Our success criterion =
  satisfy / characterize every in-silico-settleable lever** ("the rest"); a candidate clearing all
  of those is *domain-complete* even while it stays `absorbed=false` (the lab gate is not ours).
  Domain-complete is NOT a discovery claim — only a computationally-exhausted, honestly-characterized
  hand-off; no simulation flips `absorbed=true`. Do NOT treat the un-built / un-measured state as a
  campaign failure — it is the domain edge, not a wall to break.
- Negative and inconclusive results are kept as results — never deleted (the ledger
  preserves deferred/crashed runs with retry recipes).
- Artifacts go under `state/` only (commons preserve-state).
- Code/design change → update `ARCHITECTURE.json` in lockstep; log in `CHANGELOG.md`.
- **Research before real measurement (실측전 research).** Before renting compute or running an
  expensive real measurement (DFT / cRPA / GPU pod / long bench), do a literature research pass
  FIRST — the answer may already be in the literature, or a cheap proxy may suffice. Only spend on
  real compute after research justifies it. (Precedent: the cRPA GPU rental was avoided because
  interlayer Coulomb-drag-through-hBN was already measured — `state/research-crpa-glue-transparency-*.md`.)

## Gotchas

- Per-material truth lives in `state/RTSC_LEDGER.jsonl`, not in prose — read it first.
- The 568 MB `Li2MgH16` raw staging tarball was intentionally NOT copied from demiurge
  (regenerable compute output). Other per-material compute dirs are kept.
- Predictor tools are verification/ranking tools, not discovery tools — every predicted
  material is already published (novelty = 0).
