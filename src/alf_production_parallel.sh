#!/bin/bash
# L44 S3-full production 병렬판: 12 run(4U x 3phi) xargs -P3 동시·OMP=2 → 6코어만(공유 절제·6코어 여유).
# kagome flat-band attractive-Hubbard D_s(|U|) via small twist Phi. summer FREE. hexa_run 미간섭.
ALF=$HOME/ALF/Prog/ALF.out
base=$HOME/kagome_run/production
rm -rf "$base"; mkdir -p "$base"
run_one() {
  local U=$1 phi=$2
  local d="$base/U${U}_p${phi}"
  mkdir -p "$d"; cd "$d" || return
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
  OMP_NUM_THREADS=2 "$ALF" > run.log 2>&1 && echo "U=$U phi=$phi ok" || echo "U=$U phi=$phi FAIL"
}
export -f run_one; export ALF base
printf "%s %s\n" 1.0 0.00 1.0 0.02 1.0 0.04 2.0 0.00 2.0 0.02 2.0 0.04 4.0 0.00 4.0 0.02 4.0 0.04 8.0 0.00 8.0 0.02 8.0 0.04 \
  | xargs -P 3 -n 2 bash -c 'run_one "$@"' _
echo "DONE_PRODUCTION_PARALLEL"
