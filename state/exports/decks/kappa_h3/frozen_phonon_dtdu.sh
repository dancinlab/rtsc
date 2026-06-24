#!/usr/bin/env bash
# kappa-H3(Cat-EDT-TTF)2 — O-H-O off-diagonal dt/du frozen-phonon scan (RESUME RECIPE)
# ===========================================================================
# Displace the BRIDGE proton along the O...O axis by u in [-0.15, +0.15] A and,
# at each u, run scf + projwfc/wannier90 to read the inter-pi (inter-dimer)
# transfer integral t(u). dt/du = slope of t(u) at u=0 -> g = dt/du * u0 -> g/t.
# Ω(O-H-O) cross-checked from ph_oho.in (DFPT) and from the t(u) curvature.
#
# This is the REAL-DFT version of the lane's TB-grade estimate. Run on summer FREE.
# pool-qe-detached-fire-recipe: -np <= 6, serial SCF, pgrep -c pw.x before relaunch.
# NO billing pod (d17 scope = compute autonomy, but summer free is the routing here).
set -euo pipefail
QE=/home/summer/miniforge3/envs/qe/bin
WORK=/tmp/kappa_h3
cd "$WORK"

# bridge proton row index in scf.in ATOMIC_POSITIONS (set after CIF fill):
H_BRIDGE_LINE="${H_BRIDGE_LINE:?set H_BRIDGE_LINE to the bridge-proton ATOMIC_POSITIONS line}"
# O...O unit vector (from the two bridging O coords) — set after CIF fill:
UX="${UX:-1.0}"; UY="${UY:-0.0}"; UZ="${UZ:-0.0}"

for u in -0.15 -0.10 -0.05 0.00 0.05 0.10 0.15; do
  tag="u${u}"
  # build displaced scf deck: shift bridge H by u*(UX,UY,UZ) Angstrom along O...O
  python3 - "$u" "$H_BRIDGE_LINE" "$UX" "$UY" "$UZ" <<'PY' > "scf_${u}.in"
import sys
u=float(sys.argv[1]); line=int(sys.argv[2]); ux,uy,uz=map(float,sys.argv[3:6])
src=open("scf.in").read().splitlines()
# (resume: locate ATOMIC_POSITIONS, displace row `line` by u along (ux,uy,uz);
#  if positions are 'crystal', convert u(Angstrom) along O...O to fractional first.)
print("\n".join(src))   # placeholder: real displacement injected once coords are filled
PY
  if [ "$(pgrep -c pw.x || true)" -gt 0 ]; then echo "pw.x busy, waiting"; fi
  $QE/pw.x -nk 1 < "scf_${u}.in" > "scf_${tag}.out" 2>&1
  # projwfc for a quick t proxy; wannier90 for the clean inter-dimer t:
  $QE/projwfc.x < proj.in > "proj_${tag}.out" 2>&1 || true
  echo "$u done"
done

# extract t(u) -> dt/du -> g/t (post-process; w90 inter-dimer Wannier hopping is the t)
echo "scan complete; run w90/ downfold then fit t(u) slope at u=0 for dt/du."
