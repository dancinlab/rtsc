#!/bin/bash
# H_015 — run scf + projwfc for graphene/hBN(n)/graphene on summer.
# Uses the self-built QE 7.2 (serial) — the apt 6.7MaX build aborts with a
# fortify buffer-overflow on ANY input on this host.
set -e
cd "$(dirname "$0")"
export OMP_NUM_THREADS=6           # gfortran-serial pw.x is single-process; let BLAS thread
PWX=$HOME/qe_build/q-e-qe-7.2/bin/pw.x
PROJ=$HOME/qe_build/q-e-qe-7.2/bin/projwfc.x

for n in 0 1 2 3; do
  pre="ghbn_n${n}"
  echo "=== SCF n=${n} $(date) ==="
  $PWX -in ${pre}.scf.in > ${pre}.scf.out 2>&1 || { echo "SCF n=$n FAILED"; tail -20 ${pre}.scf.out; continue; }
  grep -m1 "convergence has been achieved" ${pre}.scf.out || echo "  (no convergence line n=$n)"

  cat > ${pre}.proj.in <<EOF
&PROJWFC
  prefix = '${pre}'
  outdir = './tmp'
  DeltaE = 0.05
  ngauss = 0
  degauss = 0.02
  Emin = -10.0
  Emax = 10.0
  filpdos = '${pre}'
/
EOF
  echo "=== PROJWFC n=${n} $(date) ==="
  $PROJ -in ${pre}.proj.in > ${pre}.proj.out 2>&1 || { echo "PROJWFC n=$n FAILED"; tail -20 ${pre}.proj.out; }
done
echo "=== ALL DONE $(date) ==="
