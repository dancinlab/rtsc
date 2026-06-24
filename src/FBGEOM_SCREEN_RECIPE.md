# 🧲 FB-GEOM flatness-우선 스크린 레시피

flat-band 양자기하 초전도(FB-GEOM) 후보를 **무거운 vc-relax 전에 빠르게 거르는** 레시피.
SSOT 법칙 = `ARCHITECTURE.json` LAWS/MATH-SPECTRA · 메타결론 = results_index/flatness_screen_metaconclusion.

## 핵심 원칙 (재발방지)

```
전 (LiBeB 방식)              후 (flatness-우선)
───────────                ───────────
 vc-relax(1시간+) 먼저   →   MP relaxed 구조로 바로 scf
 scf 후에야 flat 확인     →   빠른 scf로 flat-band 먼저 1차컷
 flat 없으면 헛수고       →   flat 있을 때만 무거운 정밀계산
 = 후보당 1시간+          →   = 후보당 ~10분 (6× 효율)
```

## 단계

1. **MP 구조 fetch** — Materials Project API (User-Agent 헤더 필수·403 회피). MP 구조는 이미 DFT-relaxed → vc-relax 생략.
2. **빠른 scf 덱** — `verbosity='high'`(밴드 전출력 필수) · 성긴 k(8³·금속 smearing) · MP relaxed 구조 그대로. `exports/rtsc/decks/<NAME>/scf_screen.in`.
3. **발사** — 경원소(가벼움)는 `setsid nohup` detach 가능. **d-electron/긴 scf는 반드시 `tmux new-session -d`**(SSH-독립 — detach는 세션 종료 시 죽음, RhPb iter#2 교훈 · `flat_band_scan.py` @convergence DELEC-DETACH-DEATH).
   - ⚠️ **DFPT(ph.x)로 승격할 거면 scf를 `ibrav=0`이 아니라 Bravais 명시(`ibrav=4` 등 + `celldm`)로 계산하라** — `ibrav=0` free-cell scf의 out/을 ph.x DFPT에 넘기면 대칭 처리에서 SIGSEGV(병렬·단일코어 둘다·pseudo lpaw=false여도). RhPb 교훈. flatness 스크린은 ibrav=0이어도 OK이나, ph.x 승격 셀은 ibrav 명시.
4. **판정** — `python3 flat_band_scan.py scf.out <E_F>` → `FLAT_AT_EF_COUNT`.
   - `>0` → 🟢 생존: **arxiv 신규성 프로브 선행(d_novel_only)** 후 정밀 vc-relax→scf→Γ-phonon 승격.
   - `=0` → 🔴 CLOSED-NEGATIVE, ARCHITECTURE+ING 박제 후 다음 후보.

## 박제된 메타결론 (필요조건)

- **경원소(Li/Be/B/C) 금속 = E_F에 넓은 σ/π 분산밴드 → flat-band@E_F 구조적 부재** (LiBeB·Be4B·LiC12 3종 FAIL).
- "metallic + 경원소" 추출 필터는 flat-band@E_F 보장 못 함 — flat-band은 **d-전자 kagome/Lieb 격자위상**에서 나옴.
- 현재 공략: **약혼성 4d/5d kagome**(RhPb 등 — CoSn Co-3d 강혼성·m=0 under-resolved 벽의 약혼성 버전). 격자위상을 scf 전에 확인할 것.
