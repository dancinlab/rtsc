# rtsc 검증-지식 전수수집 census (2026-06-25)

상온초전도체(RTSC) 탐색 리포 `rtsc`의 검증-지식 레지스트리 전수수집(census). READ-MOSTLY
수확 + 단일 추가 산출물. 모든 수치는 grep/wc/python 파싱으로 **측정**한 값이다(추정 아님).

- repo: `rtsc` (`/Users/mini/dancinlab/rtsc`)
- default branch: `main` (HEAD `a086574`)
- 임베디드 atlas(`*.hexa` @P/@C/@L atom): **없음** — 이 리포는 hexa-atom atlas가 아니라
  가설-카드 + 물질-원장(ledger) 형식의 검증 레지스트리다.

## 레지스트리별 카운트 (MEASURED)

| 레지스트리 | 경로 | 엔트리 수 | 비고 |
|---|---|---|---|
| 가설 레지스트리 (jsonl) | `HYPOTHESES/HYPOTHESES.jsonl` | 22 | `wc -l`=22, 카드 1:1 |
| 가설 카드 (md) | `HYPOTHESES/cards/*.md` | 23 (+`_TEMPLATE.md`) | H_001~H_023 (H_019 결번) |
| 물질 캠페인 원장 (SSOT) | `state/RTSC_LEDGER.jsonl` | 92 (+`_meta` 1) | `wc -l`=93 |
| harvest 부분원장 | `state/RTSC_HARVEST_PARTIAL.jsonl` | 16 (+`_meta` 1) | `wc -l`=17, DFPT 중간산출 banked |
| exports 판정/덱 레코드 | `state/exports/` | 48 항목 | `*_verdict.json`·`*_gatecheck.json`·decks |
| 논문 | `state/papers/` | 4 (flatband closed-neg 포함) | |

## 1) 가설 레지스트리 — tier 분포 (HYPOTHESES.jsonl, n=22, MEASURED)

| tier (verdict 선두 마커) | 개수 |
|---|---|
| 🟢 (MODEL-PROBE room-T-reachable / REAL-ED / REAL-DFT) | 3 |
| 🟡 (MODEL-PROBE · 모형 탐침) | 17 |
| 🟠 (INCONCLUSIVE deferred) | 1 |
| 🔴 (CLOSED-NEGATIVE refuted) | 1 |
| **합계** | **22** |

honesty 게이트: **모든 가설 `absorbed=false` / GATE_OPEN** — 어떤 물질도 RTSC로 단정하지
않음(CLAUDE.md falsifier-first 규율). 🟢조차 "toy-band / real-ED-corner / real-DFT-부분"
좌표이지 상온초전도 달성 주장 아님.

### 헤드라인 가설 (검증 강도 순)

| id | tier | 핵심 verdict | cite |
|---|---|---|---|
| **H_015** | 🟢 REAL-DFT | graphene/hBN(n)/graphene 실측 DFT(self-built QE 7.2): hBN 스페이서가 층간 전자결합 억제 — Dirac-point 잔여 DOS n0=0.0472→n1=0.0061 (**7.7× 감소**) 후 plateau; +@ "전자-불투명" 절반 확정(cRPA bosonic-glue 절반 deferred) | `HYPOTHESES.jsonl` H_015 · `state/h015_*/result.json` |
| **H_008** | 🟢 REAL-ED | sign-free 2e+phonon ED(pool host summer, dim≤562500): pair-channel `<g>_pair`=0.822 vs 단일입자 0.192 (**4.27×**), 반단열 코너 Ω≫g 한정. static-U mean-field가 닫은 glue crack를 retarded vertex가 재개방 | `HYPOTHESES.jsonl` H_008 · `state/h008_*/lane_a_summer.out` |
| **H_005** | 🟢 MODEL-PROBE | full-stack(geo×electronic-glue×ideal-interface) toy band에서 bkt_Tc~319K 상온 CLEAR; 3-레버 각각 필요(ablation FAIL). 돌파=인수분해(전자-불투명 계면 + 경쟁질서-없는 전자 glue). 5/5 falsifier PASS, real-pending | `HYPOTHESES.jsonl` H_005 · `state/h005_*/result.json` |
| **H_023** | 🟡→🟠 CONDITIONAL | demand-relaxation: 다층 D_s boost f_mult≥1.164(~16%, N=2)면 CLEAN Ta2NiSe5 트리오(300meV, q=0, 경쟁질서無)가 299–356K 상온 도달. **가장 강한 🟢-path**(exotic glue 불필요). 7/7 PASS, real multilayer D_s(DFT) 단일 미지 | `HYPOTHESES.jsonl` H_023 · `state/h023_*/result.json` |
| **H_001** | 🔴 CLOSED-NEGATIVE | flat-band 양자기하 → 상온: 0/2 real host(CoSn g2.87, Nb3Cl8 g2.11) box 진입 실패, Ω~15–30meV가 130meV 게이트 미달(Fubini-Study two-lever wall). bkt_Tc max~10K. **10-path 완전봉쇄** | `HYPOTHESES.jsonl` H_001 · `state/papers/flatband-geometry-ambient-roomt-closed/` |
| **H_016** | 🟡 HONEST-POSITIVE | 경쟁질서 wall은 **제거가능** — frustration η_nest 0.85→0.10 sweep, SDW-vs-SC 임계 η*=0.45(>plausibility floor 0.30). 단 room-T amplitude 미해결(U=0.543<2.22) | `HYPOTHESES.jsonl` H_016 · `state/h016_*/result.json` |
| **H_011** | 🟡 crux-resolved | +@ 트릴레이어는 **bosonic(장-결합) glue에서만** 자기일관 — 중성 exciton/plasmon이 장거리 Coulomb으로 전자-불투명 connector 관통, fermionic 전달 glue는 차단. +@ 체인을 단일요구(bosonic ~349meV glue·경쟁질서無)로 붕괴 | `HYPOTHESES.jsonl` H_011 · `state/h011_*/result.json` |
| **H_010** | 🟡 top-down | 레버多=achievability(중복 아님). 최소 achievable 카운트=4(geo·connector·glue·3D), 어느 것도 제거불가. ~5× 결손을 분산해 각 레버 demand를 material-achievable로 | `HYPOTHESES.jsonl` H_010 · `state/h010_*/result.json` |

### 🟡 CLOSED-NEGATIVE 서브셋(모형탐침이 닫은 벽 — 결과로 보존)
- H_012 topology gap = 위상은 amplitude 레버, room-T는 phase-stiffness-limited → H_001 기하로 붕괴(직교 5번째 축 아님)
- H_014 competing-order = toy Stoner/RPA에서 SDW가 SC보다 먼저 발산(0/5), 단 nesting 0.85 조건부(H_016이 escape)
- H_017 disorder flat-band = flat-AND-delocalized window 공집합(W_dis≥1.0 vs 비편재 W_dis>0.67 모순)
- H_018 predictor calibration = Tc 추정기 평균 1.86× OK이나 per-material scatter 1061× FAIL → room-T Tc는 order-of-magnitude 불확실(좌표로 읽을 것)
- H_020 named-candidate = CoSn/hBN/Ta2NiSe5 = HIGH-Tc 좌표(~252K w/3D) but NOT room-T(~41K/49meV 부족)
- H_022 frustration-unlock = 모형 양 블로커 통과(335.5K) but research가 coexistence를 CLOSE(400meV exciton=excitonic-CDW 자체)

## 2) 물질 캠페인 원장 — verdict tier (RTSC_LEDGER.jsonl, n=92, MEASURED)

| tier | 개수 | 의미 |
|---|---|---|
| PENDING | 36 | 미실행/대기(deferred-no-delete, retry recipe 보존) |
| 🟢 verified-family | 17 | textbook-proof·novel·measured·GATE_PASS·BCS-anchor |
| 🔴 CLOSED-negative/FALSIFIED | 11 | |
| 🟠 partial/INCONCLUSIVE/IN-FLIGHT/BLOCKED | 8 | |
| 기타(SCREEN-RELAXED·diagnostic·discovery·meta·MATH-SPECTRA probe·crashed) | 20 | 과정-노트·정리검증·탐색 메타 |

### 🟢 원장 검증 항목 (17, MEASURED)
- **textbook-proof (2):** CaH6, H3S-proof — 문헌-검증 BCS/Eliashberg anchor
- **measured/BCS-anchor (3):** H3Br(measured), Nb(BCS-anchor), YH10(🟢 GATE_CLOSED_MEASURED)
- **novel (9):** H3O · H3Cl · H3Se · H3Si · H3Te · SrAuH3 · H3PO · H3As · H3F — novel 수소화물 예측 노드
- **flat-band GATE_PASS (3):** LaRu3Si2(dE=-0.055eV, m=0.00µB — 가장 강한 no-cooling RTSC lead, real Tc=7K) · LaOs3Si2(GATE_PASS) · LaOs3Si2(GATE_PASS_CONFIRMED)

### 🔴 원장 falsified 헤드라인
- MoSn(dE=-2.38eV, flat band E_F서 2.4eV 아래) · CoSn-edope(단조 deeper, doping-dial 전제 REFUTED) · CoSn hole-doped(FALSIFIED) · LaRh3Si2 · CaAuH3 · CaBeH8 · Mg2IrH6 · Li2CuH6(ambient-unstable) · Os-O Lieb/checkerboard plane(FALSIFIED-realization) · MgH6/YH6(data-wall, engine 무결)

### 그래프-위상 메타-finding (TRIANGULATE V2→V4, MATH-SPECTRA probe1–6)
flat-band-at-E_F = chemistry guess가 아니라 **그래프-위상 탐색**: (1) line-graph 정리(kagome=L(honeycomb)) (2) bipartite sublattice-imbalance(Lieb). 두 직교 물리 screen(dE~0 AND non-magnetic)으로 게이트. 도핑축은 MEASURED-dead, chemistry/lattice축이 실 레버(3.30eV span). MATH-SPECTRA probe4·5 = 정수론적 구조 GENUINELY present(치환-특정, Perron letter frequency 결정).

## 3) 논문 (state/papers/, n=4)
- `flatband-geometry-ambient-roomt-closed/` — H_001 closed-negative 논문(검증된 봉쇄 결과)
- `rtsc-dft-h3s-textbook-2026-05-22/` · `rtsc-campaign-2026/` · `rtsc-superconductor/`

## 합계 (TOTALS, MEASURED)

- **총 레지스트리 엔트리 = 114** (가설 22 + 물질원장 92)
  - VERIFIED(🟢 / GATE_PASS / textbook-proof / measured / REAL-DFT / REAL-ED) = **20**
    (가설 🟢 3 + 원장 🟢 17)
  - REFUTED / CLOSED-NEGATIVE(🔴) = **12** (가설 1 + 원장 11; 🟡 내부 closed-neg 6건은 별도)
  - INCONCLUSIVE / partial / blocked(🟠) = **9** (가설 1 + 원장 8)
  - MODEL-PROBE 미실증(🟡, real-pending) = **17** (전부 가설)
  - PENDING(미실행) = **36** (원장)
  - 기타 메타/과정-노트 = **20** (원장)
- harvest 부분원장 16 · exports 판정·덱 48 (전수 나열 아님 — 요약함)
- **핵심: VERIFIED 20건조차 `absorbed=false` / GATE_OPEN** — RTSC 단정 0건(인증된 4-probe
  transport + Meissner + H_c2/T_c 실측 시에만 absorbed=true).

## 정직한 갭 (honest gaps)
- 임베디드 hexa-atom atlas 부재(이 리포에 없음 — 가설카드/원장 형식). @verify/verified:true
  필드 미사용; tier 마커가 검증 SSOT.
- `state/exports/` 48항목·harvest 16덱은 **개별 나열하지 않고 카운트+헤드라인만 요약**(silent
  truncation 아님 — 명시함). 개별 `*_verdict.json`/`*_gatecheck.json` 세부값 미전수.
- 원장 "기타 20"은 verdict 문자열이 자유서술(diagnostic·discovery·MATH-SPECTRA·meta)이라
  단일 tier로 정규화 불가 — 위에 서술 요약함.
- 🟡 MODEL-PROBE 17은 전부 **real-pending**(toy/DFT 미실증) — 검증으로 집계 안 함.
