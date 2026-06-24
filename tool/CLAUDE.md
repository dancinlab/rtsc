# tool — shared HYPOTHESES harness (rtsc)

Anima-parity: the shared, deterministic execution skeleton for HYPOTHESES hypothesis
cards lives here in repo-root `tool/`. Heavy compute (DFT / DFPT / el-ph predictors,
ED solvers) stays in `src/`; `tool/` holds only the closed-form / threshold logic a
card's falsifiers are evaluated against.

## Key files

- `rtsc_harness.py` — stdlib-only (math) primitives + falsifier harness:
  - `two_lever_box_check` (H_001 room-T design box), `geometric_bkt_tc_band`,
    `allen_dynes_tc` (H_002), `AMBIENT_TC_CEILING_K`, `ROOM_T_K`.
  - `Falsifier` dataclass + `evaluate(metrics, falsifiers)` → JSON-safe verdict ledger.
    API-compatible with the sibling lumen `tool/lumen_optics.py`.

## Rules

- Dependency-free (stdlib only) and deterministic — a card run must reproduce byte-for-byte.
- No fitting / no hidden constants beyond documented defaults; all inputs explicit.
- Per-hypothesis run scripts under `state/<hX>/` import from here via a relative path.
