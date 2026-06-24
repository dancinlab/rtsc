#!/usr/bin/env bash
# H_024 geometry pipeline (deterministic, local): CoSn kagome flat-band metric -> D_s(N=2) bound.
# Usage: bash run_h024_geometry.sh <cosn.densebands.out>
set -e
D=$(cd "$(dirname "$0")" && pwd)
BANDS="${1:-$D/../out/cosn.densebands.out}"
echo "================ H_024 CoSn flat-band quantum geometry (TB fit) ================"
OUT=$(python3 "$D/kagome_metric.py" "$BANDS")
echo "$OUT"
# extract I and g_normalised from the metric output
I=$(echo "$OUT" | grep -oE 'dimensionless  I = .* = [0-9.]+' | grep -oE '[0-9.]+$' | tail -1)
GN=$(echo "$OUT" | grep -oE '<tr g>/A_uc = [0-9.]+' | grep -oE '[0-9.]+' | tail -1)
echo
echo "================ H_024 D_s(N=2) geometric bound (Peotta-Tormae+Huhtinen) ========"
python3 "$D/ds_n2_bound.py" "$I" "$GN"
