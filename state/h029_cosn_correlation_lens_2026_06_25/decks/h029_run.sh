#!/bin/bash
cd ~/rtsc_cosn/h029_U
source ~/miniforge3/etc/profile.d/conda.sh; conda activate qe
PW=~/miniforge3/envs/qe/bin/pw.x
BX=~/miniforge3/envs/qe/bin/bands.x
echo "RUN START $(date)" > run.log
for U in 1 2 3 4 5; do
  echo "=== U=$U SCF $(date) ===" >> run.log
  mpirun -np 6 $PW -npool 2 -in scf_U${U}.in > scf_U${U}.out 2>&1
  echo "U=$U scf exit=$? $(grep -c 'convergence has been achieved' scf_U${U}.out) conv; EF=$(grep 'Fermi energy' scf_U${U}.out | tail -1)" >> run.log
  echo "=== U=$U BANDS $(date) ===" >> run.log
  mpirun -np 6 $PW -npool 2 -in bands_U${U}.in > bands_U${U}.out 2>&1
  echo "U=$U bands exit=$?" >> run.log
  mpirun -np 6 $BX -npool 2 -in bandsx_U${U}.in > bandsx_U${U}.out 2>&1
  echo "U=$U bandsx exit=$? gnu=$(ls -la cosnU${U}_bands.dat.gnu 2>/dev/null | awk '{print $5}')" >> run.log
done
echo "RUN DONE $(date)" >> run.log
