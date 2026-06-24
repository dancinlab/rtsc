# H_023 RTSC 레버 — DFT 런 준비도 점검 (SAFE prep · 컴퓨트 미실행)

- **날짜**: 2026-06-25
- **레인**: readiness-prep (READ + VERIFY + DOCUMENT only — **DFT 미실행 · pw.x 미실행 · 클라우드 미대여**)
- **대상**: H_023 demand-relaxation 레버의 단일 미지수 — 다층(N=2) Ta2NiSe5 초유체 강성(superfluid
  stiffness) D_s 가 `f_mult ≥ 1.164` 를 클리어하는지(→ 모델 상온 299–356 K).
- **목표**: 사용자가 "한 단어"로 실제 런을 승인할 수 있도록, 기존 덱·레시피·호스트·판정식을 검증하고
  정직한 준비도 판정을 남긴다.

---

## 0. 핵심 결론 (먼저)

**🔴 이 레버는 단순 pw.x DFT 덱으로는 "run-ready"가 아니다 — 숨은 *방법 벽(method wall)*이 있다.**

두 개의 독립된 벽이 측정·문서로 이미 확인되어 있다:

1. **관측량 벽 (치명적)**: `f_mult`를 결정하는 양은 **다층 초유체 강성 D_s** 인데, 이는 **표준 pw.x
   가 출력하는 관측량이 아니다.** pw.x(SCF/NSCF/DFPT)는 총에너지·밴드·포논을 주지, 초유체 가중치
   D_s 를 주지 않는다. D_s 는 (a) Wannier 함수의 양자계량(quantum metric, Fubini–Study) BZ 적분
   + Peotta–Törmä/Huhtinen 평탄밴드 공식, 또는 (b) 다체(many-body) BSE/DMFT 수준 계산을 요한다.
   기존 `state/h019_named_candidate_dft_2026_06_25/decks/`의 덱들은 **전부 밴드갭 SCF 덱**이며 D_s
   를 계산하지 **않는다**.
2. **PBE 이론 벽 (이미 측정됨)**: Ta2NiSe5 의 갭은 본질적으로 **여기자(excitonic)·다체** 성질이다.
   H_025/H_026 이 실제로 MPI 빌드 pw.x 로 측정한 결과, 단층(monoclinic C2/c) SCF 는 PBE·PBE+U·
   고-스미어링 세 레시피 모두 ~30–38× 하강 후 **근금속 평탄역(near-metallic plateau)에서 영구 진동**
   하며 conv_thr=1e-6 에 **결코 도달하지 못한다** — 컴퓨트 한계가 아니라 **PBE가 다체 여기자 갭을
   담지 못하는 물리적 한계**(정직한 음성). 즉 평범한 PBE pw.x 로는 단층 갭조차 못 푼다. N=2 다층 D_s
   는 더 어렵다.

**따라서 "DFT가 f_mult 를 클리어한다"는 경로에는 숨은 방법 벽이 있다 — 어셋먼트가 가정한 것보다 이
레버는 더 어렵다.** 가장 정직한 다음 수는 *평범한 pw.x 풀-스택 SCF가 아니라* (a) 양자기하 D_s 바운드
(H_024 가 이미 한 cheap route), 또는 (b) beyond-PBE(HSE/GW/BSE)인데 이건 훨씬 더 큰 컴퓨트를 요한다.

> ⚠️ **정직성 가드 (어떤 경우에도)**: 설령 어떤 계산이 `f_mult ≥ 1.164`를 클리어해도, 그것은
> **반증을-생존한 예측(prediction)이지 발견(discovery)이 아니다.** RTSC 게이트는 `absorbed=false` 로
> 유지되며, 이를 닫으려면 **공인 4-프로브 수송 측정 + Meissner 배제 + 측정된 H_c2/T_c** 가 필요하다.
> 어떤 시뮬레이션도 이 게이트를 뒤집지 못한다. "런하면 노벨"은 **과잉주장**이다.

---

## 1. 기존 DFT 덱 검증 (file:line 인용)

검증 대상: `state/h019_named_candidate_dft_2026_06_25/decks/` (사전 세션 산출물).

### 1.1 `gen_tanise5.py` — 구조 생성기
- Cmcm(#63) 직교정 모셀에서 Wyckoff 사이트를 펼친다 (`gen_tanise5.py:24-28` 사이트,
  `:10-19` 대칭연산, `:20` C-centering). 기대값 주석 "Ta8 Ni4 Se20 = 32" (`:48`).
- **물리 점검**: 격자 a=3.5029 b=12.8699 c=15.6768 Å (`:4`)는 Ta2NiSe5 직교정 **고온 Cmcm 부모상**
  과 일치 — 문헌 셀. 화학량 Ta8Ni4Se20=32 원자도 정상.
- **결함 (치명)**: 이 셀은 **H_019/H_024 에서 10개 레시피 전부 SCF 가 얼어붙은(froze) 바로 그
  근금속 Cmcm 부모상**이다(registry `tool/rtsc_candidates.py:146-147`, `state/...result.json` 맥락).
  H_025 가 진짜 바닥상태는 **대칭깨짐 monoclinic C2/c** 임을 확인하고 freeze 를 깼다. 따라서
  `gen_tanise5.py`/`tanise5*.in` 는 **물리적으로 잘못된(부모) 셀**이며 **이미 폐기(superseded)** 되었다.
  현역 셀은 `state/h025_ta2nise5_symbroken_gap_2026_06_25/decks/tanise5.mono*.in` (ibrav=0,
  CELL_PARAMETERS β=90.53°, `tanise5.mono.in:10,30-33`).

### 1.2 `tanise5.scf.in` / `.fixed.in` / `.scf.gamma.in` — SCF 덱
- 공통: `ibrav=8 a/b/c` (`tanise5.scf.in:9-12`), `nat=32 ntyp=3` (`:13-14`),
  `ecutwfc=45 ecutrho=360 Ry` (`:15-16`), PBE PAW/USPP 의사퍼텐셜(`:29-31`:
  `Ta.pbe-spn-rrkjus_psl.1.0.0`, `Ni.pbe-spn-kjpaw_psl.1.0.0`, `Se.pbe-n-rrkjus_psl.1.0.0`).
- **컷오프**: 45/360 Ry 는 PSL 1.0.0 USPP/PAW 에 대해 **합리적**(이 계열 권장 ~40–50/320–400).
- **k-점**: `tanise5.scf.in:65-66` = `4 1 1 0 0 0` (b,c 축이 ~12.9/15.7 Å 로 길어 1×1 정당), 또는
  `.fixed.in:66`/`.scf.gamma.in:67` = **Γ-only**. Γ-only 는 큰 단위셀에 흔하나 정밀 갭/금속성 판정엔
  거칠다 (H_026 L5 가 명시한 k-샘플링 계통오차).
- **스미어링/스핀**: `nspin=1`(`:21`), gaussian degauss 0.01(`:18-19`). Ni-3d 자성 가능성은 무시
  (nspin=1) — EI 상에선 보통 OK 지만 PBE+U 변종(`tanise5.mono.u3.in`)이 따로 존재.
- **수렴 보강**: `.fixed.in:24-27` local-TF + mixing_beta 0.1 + ndim 12 + startingpot=file — Cmcm
  freeze 를 뚫으려는 시도였으나 실패한 레시피군.
- **물리적 정합성 판정**: 의사퍼텐셜·컷오프·화학량은 **sane**. 그러나 **셀이 잘못된 부모상**이고
  **k-그리드가 거칠며**, **무엇보다 이 덱들은 밴드갭 SCF 덱이지 D_s/다층 계산 덱이 아니다.**

### 1.3 누락/갭 (multilayer-D_s 관점에서)
- **다층(N=2) 셀 없음**: 모든 덱은 단일 Ta2NiSe5 벌크. CoSn/hBN/Ta2NiSe5 N=2 헤테로구조 셀이
  **존재하지 않는다.** (H_024 가 "풀 N=2 스택 SCF 는 12코어에서 intractable, 시도 안 함"이라 명시.)
- **DFPT/phonon 셋업 없음**: `ph.x` 입력 없음. (단, D_s 는 포논이 아니라 전자 양자기하 관측량이라
  DFPT 가 옳은 도구도 아님 — §2 참조.)
- **Wannier90 없음**: `tool/CLAUDE.md` 및 H_024 L3 가 "summer 에 wannier90.x 빌드 안 됨" 명시 →
  H_024 는 NN tight-binding 적합으로 양자계량 ∫tr g 를 우회 추출(`ds_n2_bound.py` route).
- **의사퍼텐셜 인벤토리 미문서화**: `pseudo_dir=../pseudo` 참조하나 `tool/CLAUDE.md` 컴퓨트
  서브스트레이트 절에 의사퍼텐셜 보유 목록이 기록돼 있지 않다(런 전 `ls ~/.../pseudo` 확인 필요).

---

## 2. 정확한 런 레시피 (사용자가 승인할 것) — **두 가지 정직한 옵션**

`f_mult` 를 결정하는 D_s 는 pw.x 1회 SCF 의 출력이 아니므로, "한 번의 DFT 런" 레시피는 존재하지
않는다. 정직한 옵션은 두 가지:

### 옵션 A — **양자기하 D_s 바운드** (cheap · 이미 한번 수행됨 · 권장 첫 수)
H_024 가 정확히 이 경로를 수행했다(`H_024_named_candidate_dft_followon.md`, `ds_n2_bound.py`):
1. **SCF/NSCF** (현역 monoclinic 셀): summer MPI pw.x, `mpirun -np 6 pw.x -npool 2`.
2. **밴드 → tight-binding 적합** → 평탄밴드 양자계량 ∫tr g BZ 적분 (Wannier90 부재 시 NN-TB 적합).
3. **Peotta–Törmä(arXiv:1506.02815) + Huhtinen(arXiv:2203.11133)** 평탄밴드 D_s 바운드 공식 →
   기하가 `f_mult ≥ 1.164 @ N=2` 를 **라이선스(license)** 하는지 SUPPORTED/PARTIAL/NOT 판정.
- **이미 결과 있음**: H_024 verdict = ∫tr g I≈2.86 ≈ 측정 QGT 2.87 → **f_mult≥1.164 @ N=2 SUPPORTED
  (단, 도핑 ν→E_F + 층간 코히런스 보존 조건부), is_green=False.** 즉 **cheap route 는 이미 닫혔고
  음성/조건부 결과까지 나와 있다.** 추가 런의 한계효용이 낮다.
- **호스트/비용**: summer (6 물리코어/12스레드, 무료 풀 호스트). monoclinic SCF ~수십 분/레시피.
  클라우드 불필요.

### 옵션 B — **실제 다층 D_s (decisive test)** — *방법 벽에 막혀 있음*
어셋먼트가 상상한 "진짜" 테스트 = 제작된 CoSn/hBN/Ta2NiSe5 N=2 스택의 실제 D_s:
1. **N=2 헤테로구조 셀 작성** (현재 부재). vdW 갭·격자 부정합·hBN 스페이서 → 거대 슈퍼셀(원자 수백~).
2. **SCF + Wannier 화** → 다층 평탄밴드 Bloch QGT.
3. D_s = 양자계량 적분 (or 다체 BSE 로 여기자 강성).
- **호스트/비용 추정**: N=2 풀 스택 SCF 는 **6코어 summer 에서 intractable**(H_024 명시). 클라우드
  GPU/대형 MPI 노드(수십~수백 코어, ≥수십 GB RAM, 다일~) 필요 추정. **그러나 beyond-PBE(여기자
  갭은 PBE 부재)가 깔려 있어 단순 GPU 스케일업으로도 풀리지 않는다 — 방법 벽이 선행한다.**
- **판정**: 이 옵션은 **현재 run-ready 아님.** 셀 부재 + 방법 벽(PBE 갭 부재 + D_s≠pw.x 관측량).

### D_s → f_mult → PASS 계산 사슬 (어느 옵션이든 동일)
- D_s(N) → `f_mult(N) = sqrt(D_s(N)/D_s(1))` (or 보수 모델 N^0.25), `run_h023.py:116-122`.
- `f_mult_required = OMEGA_REQ_ROOMT_3D / glue = 349.31/300 = 1.1644` (`run_h023.py:90-92`,
  `result.json` metrics).
- **PASS 기준**: `f_mult(N=2) ≥ 1.164` → 모델 상온 Tc = `tc_3d_baseline(251.64K) * f_mult` ∈
  **299.25 K (보수 N^0.25) ~ 355.87 K (낙관 sqrt N)** (`result.json` sweep N=2).

### 어셋먼트가 명명한 교차 게이트 (cross-gates)
- **H_016 경쟁질서 η<0.45**: Ta2NiSe5 는 **해당 없음** — q=0 EI 질서 자체가 페어링 채널이라
  선점하는 유한-q CDW/SDW 가 없다(`H_023` F5, `rtsc_candidates.py:160` competing_order="none").
  (η<0.45 게이트는 1T-TiSe2 경로용; Ta2NiSe5 는 구조적으로 통과.)
- **동역학 안정성 (dynamical stability)**: ph.x 포논으로 허수 모드 부재 확인 — **현재 덱에 없음**
  (DFPT 셋업 부재). 다층 셀 확정 후 추가 필요.
- **H_022 여기자-CDW 비충돌**: Ta2NiSe5 q=0 EI 는 1T-TiSe2 의 여기자-CDW 충돌과 무관(F5 와 동일
  논거) — 구조적으로 통과.

---

## 3. 정직한 준비도 판정 (readiness verdict)

| 항목 | 상태 |
|---|---|
| 의사퍼텐셜·컷오프·화학량 sane? | ✅ (단, 의사퍼텐셜 보유목록 런 전 확인 필요) |
| 셀이 물리적으로 옳은가? | ❌ h019 덱은 **잘못된 Cmcm 부모상**(이미 폐기) · 현역=h025 monoclinic |
| MPI pw.x 호스트 준비? | ✅ summer (H_026 에서 MPI 빌드 완료, banner "Parallel (MPI)") |
| 단층 갭 풀림? | ❌ **PBE 이론 벽** — 세 레시피 모두 근금속 평탄역 진동, conv_thr 미도달(정직한 음성) |
| **다층 D_s 가 pw.x 관측량인가?** | ❌ **관측량 벽** — D_s≠pw.x 출력 · 양자기하/BSE 요함 |
| N=2 헤테로구조 셀 존재? | ❌ 부재 (H_024 가 intractable 로 명시) |
| Cheap 양자기하 바운드? | ✅ **이미 수행됨** (H_024: f_mult≥1.164 @ N=2 SUPPORTED-conditional, is_green=False) |

**판정: 🔴 BLOCKED — 단순 DFT 덱으로는 run-ready 아님. 두 개의 측정된 벽이 선행한다.**

정확히 무엇이 실제 런을 막는가:
1. **방법 벽 (1차, 가장 치명)**: 다층 초유체 강성 D_s 는 **평범한 pw.x 관측량이 아니다.** 양자기하
   (Wannier QGT) 또는 beyond-DFT(BSE) 가 필요. 어셋먼트가 가정한 "DFT 가 f_mult 를 클리어"는
   *한 번의 pw.x 런*으로 환원되지 않는다.
2. **이론 벽 (PBE)**: Ta2NiSe5 여기자 갭은 PBE/PBE+U 에 부재 → 단층 SCF 조차 근금속 진동(측정됨).
   다층은 더 어렵다. beyond-PBE 는 훨씬 큰 컴퓨트.
3. **인풋 벽 (부차)**: N=2 헤테로구조 셀 부재 + h019 덱은 폐기된 부모상 + 의사퍼텐셜 인벤토리 미문서.

**그리고 cheap 양자기하 route(옵션 A)는 H_024 가 이미 닫았다** — 기하는 f_mult≥1.164 를
*조건부 SUPPORT* 하나 is_green=False(측정 D_s 아님). 즉 **승인할 만한 "새로운 한 방의 DFT 런"이
사실상 남아있지 않다** — 남은 건 (a) intractable 한 풀 N=2 스택(클라우드+방법 벽) 또는 (b) 이미
음성으로 닫힌 cheap 바운드의 재실행뿐.

---

## 4. 원-커맨드 승인 스펙 (사용자가 "한 단어"로 고를 것)

> **권고: 새 heavy 런을 승인하기 전에, 위 방법 벽을 먼저 받아들일지 결정.** cheap route 는 이미
> 닫혔고, decisive route 는 intractable+방법벽이다. 그럼에도 진행을 원한다면:

- **승인어 "A" (cheap 재확인 · 무료 · 권장 안 함 — 이미 닫힘)**:
  ```
  pool on summer 'cd ~/qe_build && mpirun -np 6 ~/qe_build/q-e-qe-7.2/bin/pw.x -npool 2 \
    -in <monoclinic SCF>.in > scf.out; python3 read_gap.py; python3 ds_n2_bound.py'
  ```
  → H_024 의 ∫tr g + D_s 바운드 재생성. 새 정보 거의 없음(is_green 불변).

- **승인어 "B" (decisive · intractable · 방법 벽 — 셀+방법 선행 필요)**:
  N=2 CoSn/hBN/Ta2NiSe5 슈퍼셀 작성 → Wannier QGT 또는 BSE 파이프라인 구축 → 대형 MPI/GPU 호스트
  대여. **현재 셀·방법·호스트 모두 미비 → 승인 즉시 실행 불가, 별도 빌드 라운드 필요.**

- **승인어 "WALL" (정직한 종료 · 권장)**: 두 벽을 캠페인 SSOT 에 측정-벽으로 기록하고, 레버를
  "in-silico 로는 닫힘(방법 벽), 진짜 게이트는 실험 4-프로브"로 정직하게 마감.

**어느 경우에도 `absorbed=false` · GATE_OPEN 불변 — 시뮬은 RTSC 게이트를 닫지 못한다.**

---

## 5. 정직성 명세 (Honesty)
- 설령 옵션 A/B 가 `f_mult≥1.164` 를 내도 = **반증-생존 예측**이지 발견 아님.
- RTSC 게이트 닫힘 = 공인 4-프로브 수송 + Meissner 배제 + 측정 H_c2/T_c. 시뮬 무관.
- "런하면 노벨"은 과잉주장. 이 노트는 **실측 컴퓨트 없이** 준비도만 점검했다.
- 한계: summer 의 의사퍼텐셜 보유 목록·정확한 walltime 은 런 전 호스트에서 확인 필요(미문서).

## 6. 교차링크
- `HYPOTHESES/cards/H_023_demand_relaxation.md` (레버 · L1 단일 미지수)
- `HYPOTHESES/cards/H_024_named_candidate_dft_followon.md` (양자기하 D_s 바운드 — cheap route 이미 수행)
- `HYPOTHESES/cards/H_025_..` / `H_026_..` (PBE 갭 벽 · MPI 빌드 — 측정된 이론 벽)
- `state/research-multilayer-ds-boost-2026-06-25.md` (D_s-vs-N prior: plausible·host-unverified)
- `state/h019_named_candidate_dft_2026_06_25/decks/` (검증 대상 — 폐기된 Cmcm 부모상 SCF 덱)
- `tool/rtsc_candidates.py:144-167` (Ta2NiSe5 registry: 갭 unverified-by-us · D_s SUPPORTED-conditional)
- `tool/CLAUDE.md:30-46` (컴퓨트 서브스트레이트: summer MPI QE 7.2/7.5)
