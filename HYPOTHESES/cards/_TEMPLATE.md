---
id: H_000
slug: short-kebab-slug
title: one-line falsifiable claim
domain: rtsc
status: seed-pending          # seed-pending | running | closed-supported | closed-negative | inconclusive
exploration_method: E?        # how the hypothesis was found
verification_method: W1 (pre-register frozen) + W2 (falsifier-5+) + W3 (deterministic) + W5 (honest-limits-5+)
deterministic: true
llm: none
pre_register_frozen: false    # flip true once Predictions/Criteria/Falsifiers are frozen
frozen_at: YYYY-MM-DD
since: YYYY-MM-DD
---

# H_000 — <one-line claim> (rtsc)

## Hypothesis

<the falsifiable claim, stated so a single deterministic run can refute it. Target = 293 K @ 1 atm unless stated.>

## Why

- <physical / literature motivation, cited>

## Predictions

- **H?.1**: <quantitative prediction with a number and a pass threshold>
- **H?.2**: ...

## Variables

- **axis1**: [...]
- grid size = ... cells × N reps

## Run Protocol

- deterministic: seed=fnv(axes+rep_id)
- tool: src/<runner>.py    # rtsc execution skeleton lives in src/
- record: state/exports/<material>/<verdict>.json  +  one line in state/RTSC_LEDGER.jsonl
- runtime/cost estimate: <local | cloud pod>

## Criteria

- **C1**: ...
- **verdict_rule**: SUPPORTED = ...; INCONCLUSIVE = ...; REFUTED = ...

## Falsifiers (≥5 — pre-registered)

- **F1**: <observation that would refute this> → halt / FALSIFIED
- **F2**: ...
- **F3**: ...
- **F4**: ...
- **F5**: <post-hoc edit to criteria → pre-register violation>

## Honest Limits (≥5)

- **L1**: <what this run does NOT establish>
- **L2**: ...
- **L3**: ...
- **L4**: ...
- **L5**: <absorbed=true still requires accredited 4-probe transport + Meissner + measured H_c2/T_c>

## Cross-Links

- **ledger**: state/RTSC_LEDGER.jsonl (material rows)
- **tools**: src/<...>.py
- **literature**: <refs>

## Verdict

<empty until run — then paste VERBATIM stdout of the deterministic run. No paraphrase.>
