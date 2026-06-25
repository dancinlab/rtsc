set -e
cd ~/rtsc_cosn
mkdir -p h029_U
cd h029_U
# copy pseudos link
ln -sf ../pseudo pseudo

# common atomic block
read -r -d '' CELL << 'EOF' || true
  ibrav=4
  celldm(1)=9.9760
  celldm(3)=0.80680
  nat=6
  ntyp=2
  ecutwfc=65
  ecutrho=520
  occupations='smearing'
  smearing='mp'
  degauss=0.03
  nspin=2
  starting_magnetization(1)=0.3
  starting_magnetization(2)=0.0
EOF

read -r -d '' ATOMS << 'EOF' || true
ATOMIC_SPECIES
  Co 58.933 Co.pbe-spn-rrkjus_psl.0.3.1.UPF
  Sn 118.71 Sn.pbe-dn-rrkjus_psl.1.0.0.UPF
ATOMIC_POSITIONS crystal
  Co 0.500000 0.000000 0.000000
  Co 0.000000 0.500000 0.000000
  Co 0.500000 0.500000 0.000000
  Sn 0.000000 0.000000 0.000000
  Sn 0.333333 0.666667 0.500000
  Sn 0.666667 0.333333 0.500000
EOF

for U in 1 2 3 4 5; do
  # SCF input
  cat > scf_U${U}.in << EOF
&control
  calculation='scf'
  prefix='cosnU${U}'
  outdir='./outU${U}'
  pseudo_dir='./pseudo'
/
&system
${CELL}
/
&electrons
  conv_thr=1.0d-7
  mixing_beta=0.3
  electron_maxstep=300
/
${ATOMS}
K_POINTS automatic
  6 6 6 0 0 0
HUBBARD (ortho-atomic)
  U Co-3d ${U}.0
EOF
  # bands input
  cat > bands_U${U}.in << EOF
&control
  calculation='bands'
  prefix='cosnU${U}'
  outdir='./outU${U}'
  pseudo_dir='./pseudo'
/
&system
${CELL}
  nbnd=60
/
&electrons
  conv_thr=1.0d-7
/
${ATOMS}
K_POINTS crystal_b
5
  0.0000 0.0000 0.0000 40
  0.3333 0.3333 0.0000 40
  0.5000 0.0000 0.0000 40
  0.0000 0.0000 0.0000 40
  0.0000 0.0000 0.5000 1
HUBBARD (ortho-atomic)
  U Co-3d ${U}.0
EOF
  # bands.x post input
  cat > bandsx_U${U}.in << EOF
&bands
  prefix='cosnU${U}'
  outdir='./outU${U}'
  filband='cosnU${U}_bands.dat'
/
EOF
done
echo "decks created:"; ls scf_U*.in bands_U*.in bandsx_U*.in
