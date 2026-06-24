#!/bin/bash
# L44 S3-full: kagome flat-band attractive-Hubbard D_s via twist Phi_X sweep (D_s ~ d^2E/dPhi^2).
# 작은 검증판(4x4·U=-4·Phi 3값). E(Phi) 곡률로 superfluid weight sanity. summer FREE.
set -e
ALF=~/ALF/Prog/ALF.out
ANA=~/ALF/Analysis/ana.out
base=~/kagome_run/twist_sweep
rm -rf "$base"; mkdir -p "$base"; cd "$base"
for phi in 0.00 0.06 0.12; do
  d="p$phi"; mkdir -p "$d"; cd "$d"
  cat > parameters <<PEOF
&VAR_ham_name
ham_name = "Hubbard"
/
&VAR_lattice
Lattice_type = "KAGOME"
L1 = 4
L2 = 4
/
&VAR_Model_Generic
N_SUN = 2
N_FL = 1
Phi_X = ${phi}d0
Dtau = 0.1d0
Beta = 8.d0
Projector = .F.
/
&VAR_Hubbard
ham_T = 1.d0
Ham_chem = 0.d0
Ham_U = -4.d0
Mz = .F.
/
&VAR_QMC
Nwrap = 10
NSweep = 80
NBin = 12
Ltau = 0
CPU_MAX = 0.0
/
PEOF
  echo 12345 > seeds
  OMP_NUM_THREADS=4 "$ALF" > run.log 2>&1 && echo "Phi=$phi RUN ok" || echo "Phi=$phi RUN FAIL"
  # 분석: ana로 Ener_scal 평균 (실패시 raw)
  "$ANA" Ener_scal > ana.log 2>&1 && echo "Phi=$phi ANA ok" || echo "Phi=$phi ANA fail(raw 보존)"
  cd ..
done
echo "=== E(Phi) 요약 ==="
for phi in 0.00 0.06 0.12; do
  echo -n "Phi=$phi  "
  grep -iE "energ|OBS" "p$phi/Ener_scalJ" 2>/dev/null | head -1 || tail -2 "p$phi/ana.log" 2>/dev/null | head -1 || echo "(분석출력 미확인)"
done
echo "DONE_TWIST_SWEEP"
