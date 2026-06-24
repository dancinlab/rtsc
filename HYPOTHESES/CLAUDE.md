# HYPOTHESES — hypothesis-verification system (rtsc)

Popperian falsification lab, modeled on anima's `UNIVERSE/`. Each campaign question
becomes a numerically falsifiable, runnable card.

## Key files

- `HYPOTHESES.jsonl` — flat registry, one JSON line per hypothesis
  (`id · slug · tier · title · card · verdict · source · archived · artifacts`).
- `cards/H_*.md` — one card per hypothesis: frozen pre-registration + predictions +
  **≥5 measurable falsifiers** + **≥5 honest limits** + **verbatim** run verdict.
- `cards/_TEMPLATE.md` — the card skeleton; copy it to start a new hypothesis.

## Rules

- Pre-register frozen BEFORE running (predictions/criteria/falsifiers locked). A post-hoc
  edit to criteria is itself a falsifier (pre-register violation).
- The `## Verdict` section is **verbatim stdout** of the deterministic run — no paraphrase,
  no LLM self-judge.
- Falsifier PASS = NOT triggered. Negative/inconclusive verdicts are kept as results.
- Runs live in `state/<hX>_<slug>_<date>/` and import the shared harness from `tool/`.
- `absorbed=true` for an RTSC card requires accredited 4-probe transport + Meissner +
  measured H_c2 / T_c — no simulation flips that gate.
