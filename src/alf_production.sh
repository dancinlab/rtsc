#!/bin/bash
# L44 S3-full production: kagome flat-band attractive-Hubbard D_s(|U|) via small twist Phi sweep.
# 여러 U(1,2,4,8) x 작은 Phi(0,0.02,0.04) x 6x6 x Beta12 x NBin40. D_s = d^2E/dPhi^2 per-site.
# 처방 검증: flat-band D_s가 강결합 BEC-side서 포화=PASS / falls=FALSIFY. summer FREE.
ALF=~/ALF/Prog/ALF.out
base=~/kagome_run/production
rm -rf "$base"; mkdir -p "$base"; cd "$base"
for U in 1.0 2.0 4.0 8.0; do
 for phi in 0.00 0.02 0.04; do
  d="U${U}_p${phi}"; mkdir -p "$d"; cd "$d"
  cat > parameters <<PEOF
&VAR_ham_name
ham_name = "Hubbard"
/
&VAR_lattice
Lattice_type = "KAGOME"
L1 = 6
L2 = 6
/
&VAR_Model_Generic
N_SUN = 2
N_FL = 1
Phi_X = ${phi}d0
Dtau = 0.1d0
Beta = 12.d0
Projector = .F.
/
&VAR_Hubbard
ham_T = 1.d0
Ham_chem = 0.d0
Ham_U = -${U}d0
Mz = .F.
/
&VAR_QMC
Nwrap = 10
NSweep = 200
NBin = 40
Ltau = 0
CPU_MAX = 0.0
/
PEOF
  echo 12345 > seeds
  OMP_NUM_THREADS=4 "$ALF" > run.log 2>&1 && echo "U=$U phi=$phi ok" || echo "U=$U phi=$phi FAIL"
  cd ..
 done
done
echo "DONE_PRODUCTION"
