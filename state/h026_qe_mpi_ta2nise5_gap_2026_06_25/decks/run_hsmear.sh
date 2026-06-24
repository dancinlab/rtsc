#!/bin/bash
cd ~/h025
export OMP_NUM_THREADS=1
rm -rf out_mono_h
mpirun -np 6 ~/qe_build/q-e-qe-7.2/bin/pw.x -npool 2 -in tanise5.mono.hsmear.in > tanise5.mono.hsmear.mpi.out 2>&1
echo "SCF_EXIT=$?" >> tanise5.mono.hsmear.mpi.out
