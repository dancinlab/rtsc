# LaY_H10 (B08) — RTSC DFT el-ph 런북

🧪 **LaY_H10** · 별칭 **란타넘-이트륨 이중금속 수소화물** · LaH10/YH10 의 이중금속 합금 (직계 YH10 family)

검증된 **YH10 (Tc=227.5K@250GPa, #1909)** 의 H32 클라스레이트 케이지에 **La+Y 이중금속**을
올려, LaH10 의 **더 낮은 압력 안정성** 과 YH10 의 **높은 Tc** 를 같은 케이지에서 결합하려는
직계 family 확장. 클라스레이트 메커니즘 클래스 그대로, 금속 site 만 La/Y 0.5/0.5 ordered.

- **anchor**: LaH10 / YH10 sodalite clathrate, **Fm-3m (SG 225)**. YH10 = 검증 라인 #1909;
  LaH10 Tc~250K@~170GPa (실험). 둘 다 H32 케이지가 금속 둘러싸는 클라스레이트 초수소화물.
- **구조 (1차 deck)**: ibrav=6 simple tetragonal (Fm-3m 원시셀의 [100] 2×1×1 ordered 초격자),
  **nat=22, ntyp=3** — **2 formula units** (La 1 + Y 1 + H 20). La @ 하단 금속 site (z~0),
  Y @ 상단 금속 site (z~0.5), 20 H 가 두 적층 sodalite 케이지를 채움. **물리적으로 정직한 ordered 셀**.
- **격자 START**: celldm(1)=6.80 Bohr (a=3.60 Å), celldm(3)=2.00 (doubled c). vc-relax 가
  진짜 a, c/a, H 케이지를 찾음. La(1.17Å, 4f) + Y(1.04Å) ordered.
- **목표 압력**: vc-relax `press=2500.0` kbar = **250 GPa** (YH10-anchor 안정화 레짐 #1909).
  ⚠ **lower-P fallback**: LaH10-like `press=1700.0` (170 GPa) — La 가 더 낮은 압력 안정성 부여.

> ⚠ **클라스레이트 좌표는 START guess** 다. 20 H 좌표는 H32 sodalite 케이지의 물리적 초기
> 추정이며, **vc-relax 가 진짜 Fm-3m-유래 최소점으로 완화**한다. 완화 후 대칭 분석으로 SG 확인.

---

## ⚠⚠ 사이징 정직성 (#1885 · d11) — 단일팟 비현실, SPLIT-Q 또는 VCA 필수

```bash
# 1차 deck = 22-atom ordered 셀:
hexa cloud preflight --kind dft-phonon --atoms 22 --nq 8 --metallic
# → est = 3,577,728 s (993.8 h ≈ 41일!) · floor (×1.5) = 5,366,592 s (1490.7 h ≈ 62일)
#   atoms³ 스케일링 → 22-atom 은 단일팟 비현실 (d11 feasibility-size 경고).

# 11-atom VCA(virtual crystal) 단일-site 대안:
hexa cloud preflight --kind dft-phonon --atoms 11 --nq 8 --metallic
# → est = 447,216 s (124.2 h) · floor (×1.5) = 670,824 s (186.3 h) — 단일팟 feasible.
```

**두 실행 경로 (dispatcher 선택):**

1. **SPLIT-Q 멀티팟** (정직한 ordered 22-atom 셀 유지) — ph.x 의 `start_q`/`last_q` 로
   IBZ q 를 팟별 분할. nq=8 → 예: pod-1 `start_q=1 last_q=4`, pod-2 `start_q=5 last_q=8`.
   각 팟 ~125-250h, recover=.true. 로 안전. q 별 .dyn 을 모아 `q2r`/하베스트.
   → 정확도 최선, 자원 多 (병렬 팟 ≥2).

2. **VCA 11-atom 단일팟** (단일 금속 site 에 (La₀.₅Y₀.₅) 평균 의사퍼텐셜) — `max_seconds=670824`,
   단일팟 feasible (~124h). VCA UPF 합성 필요 (`virtual_v2.x` 또는 `virtual.x` 로
   La/Y UPF 를 50/50 가중 합성). 케이지 1개 (1 f.u.), ibrav=2 (fcc Fm-3m 원시셀) 로 재작성.
   → 비용 최소, 합금 무질서를 평균장으로 근사 (ordering 효과 상실).

> **권장**: ssh9 $0 여유 코어가 ≥2 팟 분이면 **SPLIT-Q (경로 1)**. 단일 슬롯만 가용이면
> **VCA (경로 2)**. ph.in 의 `max_seconds=670824` 는 VCA 기준; SPLIT-Q 는 q-그룹별로 재산정.

---

## 의사퍼텐셜 (d13)

PSL 1.0.0 (PBE, RRKJUS ultrasoft) 패밀리로 통일. **3종 모두 `pseudo/` 에 스테이징 + 실행 전 grep 확인**.

| 원소 | UPF 파일명 | 상대론 처리 | 비고 |
|------|-----------|------------|------|
| La | `La.pbe-spfn-rrkjus_psl.1.0.0.UPF` | scalar | ⚠ **4f 란타넘** — spfn (s,p,**f**,n semicore) |
| Y  | `Y.pbe-spn-rrkjus_psl.1.0.0.UPF` | scalar | spn semicore (4s4p4d5s) |
| H  | `H.pbe-rrkjus_psl.1.0.0.UPF` | — | YH10/SrAuH3 anchor 재사용 (로컬 확인됨) |

> ⚠ **La 는 4f 란타넘 — UPF 라이브러리에 La 항목이 실제로 있는지 반드시 grep (d13).**
> PSL 1.0.0 은 La 를 **`La.pbe-spfn-rrkjus_psl.1.0.0.UPF`** (spfn = s,p,**f**,n semicore,
> 4f 를 valence 로 처리) 로 제공한다 (PSL 은 보통 La 를 커버하지만 **헤더에서 직접 확인**).
> NWChem def2 의 란타넘 결손 (d13 사례) 과 달리 QE PSL 은 La 가 있으나, **버전·variant 명
> (spfn vs spdfn) 이 라이브러리마다 달라 grep 필수**. SOC 는 4f 에 의미있을 수 있으나
> baseline 은 scalar-relativistic; full-rel La UPF 가 있으면 SOC 교차검증.
>
> ```bash
> ls -l ~/rtsc_layh10/pseudo/La.pbe-spfn-rrkjus_psl.1.0.0.UPF || {
>   echo "MISSING_La_PSEUDO — pslibrary 에서 다운로드 (psl.1.0.0 spfn, 4f valence)";
>   echo "  대체 variant 확인: La.pbe-spdfn-* 또는 La.pbe-fspn-* 명명도 가능";
> }
> ```

> ⚠ **로컬 확인 결과**: `H` 는 `~/rtsc_srauh3_stage/pseudo/` 에 존재 (확인됨).
> **La, Y 는 로컬 디스크에 없음** — 위 파일명은 PSL 1.0.0 표준 명명규칙 기준. dispatcher 가
> 실행 직전 **반드시 on-pod grep 확인** (d13). VCA 경로면 (La+Y) 합성 UPF 도 별도 grep.

---

## 실행 체인

vast.ai GPU 팟 (SPLIT-Q 면 ≥2 팟) 에서 아래 체인 실행. workdir = `/home/aiden/rtsc_layh10`.
아래는 22-atom ordered 셀 + 전체-q 템플릿. **SPLIT-Q 면 step 3 의 ph.in 에 start_q/last_q 를
팟별로 주입**. **VCA 면 vc-relax.in/scf.in 을 ibrav=2 11-atom 1-f.u. + 합성 UPF 로 교체**.

```bash
set -e

# 0) 환경 + 워크디렉터리
SRC=/home/aiden/rtsc_layh10
mkdir -p "$SRC/out" "$SRC/pseudo"
cd "$SRC"
export OMP_NUM_THREADS=1
NP=6                                    # physcores; --oversubscribe 금지 (feedback: load thrash)
source ~/miniforge3/etc/profile.d/conda.sh
conda activate qe

# 0.1) 의사퍼텐셜 존재 확인 (d13) — 3종 모두 (La 4f 주의)
for f in La.pbe-spfn-rrkjus_psl.1.0.0.UPF \
         Y.pbe-spn-rrkjus_psl.1.0.0.UPF \
         H.pbe-rrkjus_psl.1.0.0.UPF; do
  ls -l "$SRC/pseudo/$f" || { echo "MISSING_PSEUDO: $f"; exit 1; }
done

# 1) vc-relax — 격자/위치 완화 (press=2500 kbar = 250 GPa). 진짜 celldm + 케이지 찾음.
timeout 12h mpirun -np $NP --bind-to none pw.x -in vc-relax.in > vc-relax.out 2>&1
grep -q "JOB DONE" vc-relax.out || { echo "VCRELAX_FAIL"; exit 1; }

# 1.1) 완화된 celldm(1), celldm(3) + 좌표를 scf.in 으로 반영 (수동 또는 파서)
grep -A2 "Begin final coordinates" vc-relax.out
echo ">>> scf.in 의 celldm(1)/celldm(3) 을 위 완화값으로 갱신했는지 확인"

# 2) scf — dense 16x16x10 k (electron_phonon=simple 의 double-delta EPC 용)
timeout 8h mpirun -np $NP --bind-to none pw.x -in scf.in > scf.out 2>&1
grep -q "JOB DONE" scf.out || { echo "SCF_FAIL"; exit 1; }

# 3) ph.x — 2^3 q 포논 + el-ph. ⚠ 22-atom 전체-q = ~994h 단일팟.
#    SPLIT-Q: ph.in 에 start_q/last_q 주입해 팟별 q-그룹만 (예: pod-1=1..4 / pod-2=5..8).
#    VCA: 11-atom 셀이면 단일팟 ~124h 로 전체-q 가능.
#    recover=.true. → 재-dispatch 안전.
timeout 200h mpirun -np $NP --bind-to none ph.x -in ph.in > ph.out 2>&1
grep -q "JOB DONE" ph.out || { echo "PH_FAIL — recover 로 재개 또는 split-q 확인"; exit 1; }

# 4) 완료 플래그
touch "$SRC/ALL_DONE.flag"
echo "JOB DONE"
```

---

## 하베스트 / 파서

- **parser**: `rtsc-dft-elph` (Allen-Dynes Tc).
- λ (전자-포논 결합): sigma-plateau (sigma ≳ 0.025 Ry) 에서 읽는다 — 단조 broadening 꼬리 ❌.
- ω_log: 실수 모드에 대한 Allen-weighted exp(<ln ω>), BZ 평균.
- SPLIT-Q 면 팟별 .dyn 을 모아 full-q 격자에서 평균 (q2r/matdyn 또는 하베스터가 병합).
- 안정성: 모든 IBZ q 의 모드가 실수여야 함 (허수 → 동적 불안정).
- Tc: Allen-Dynes
  ```bash
  hexa verify --expr allen_dynes_tc <lambda> <omega_log> 0.10 --compute   # μ*=0.10
  hexa verify --expr allen_dynes_tc <lambda> <omega_log> 0.13 --compute   # μ*=0.13
  ```

## 정직성 (d6 · g3 · d11)

- λ_BZ 미측정 → Tc 추정뿐. full-BZ Allen-weighted ω_log 가 진실값.
- **사이징 정직성 (d11)**: 22-atom 단일팟 = ~994h 비현실 → SPLIT-Q 또는 VCA 명시 (위 §사이징).
  under-converged / 단일팟 강행 금지 — 정직한 경로 선택을 dispatcher 가 기록.
- plateau 강요 금지 — 정직한 sigma-plateau 또는 under-converged 로 보고.
- **사전등록 falsifier**: 250 GPa 에서 허수 모드 → 동적 비안정 → **closed-negative**
  (La+Y 이중금속 합금 축이 YH10-family Tc 목표에 ⊥). 압력 스윕(170 GPa LaH10-like) 재시도.
- VCA 평균장이 ordering 효과를 놓칠 수 있음 — VCA 결과는 ordered 셀의 근사임을 명시.

---

## INFRA-READY 계약

- **runnable**: 위 실행 체인 (RUNBOOK.md) — SPLIT-Q / VCA 경로 명시됨
- **inputs**: `vc-relax.in` · `scf.in` · `ph.in`
- **parser**: `rtsc-dft-elph` (allen_dynes_tc)
- **workdir**: `exports/rtsc/decks/LaY_H10/`
