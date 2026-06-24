#!/usr/bin/env python3
# Read the Kohn-Sham band gap from a converged QE pw.x SCF/NSCF output.
# Strategy: parse all k-point eigenvalue blocks (verbosity='high' prints them),
# find the highest occupied and lowest unoccupied levels relative to E_Fermi.
# For a smearing run we use the Fermi energy printed by QE; the "gap" is the
# direct/indirect separation of the bands straddling E_F.
#
# Usage: python3 read_gap.py <pw.out>
import sys, re

fn = sys.argv[1]
txt = open(fn).read()

# Fermi energy
mf = re.findall(r"the Fermi energy is\s+([-\d.]+)\s+ev", txt)
ef = float(mf[-1]) if mf else None

# highest occupied / lowest unoccupied (printed when insulating, fixed occ)
mhl = re.findall(r"highest occupied,?\s+lowest unoccupied level \(ev\):\s+([-\d.]+)\s+([-\d.]+)", txt)
homo_lumo = (float(mhl[-1][0]), float(mhl[-1][1])) if mhl else None

# Parse eigenvalue blocks. Each k block: "k = ... bands (ev):" then numbers.
blocks = re.split(r"\n\s*k =", txt)
all_eigs = []  # list of (kindex, sorted eigenvalue list)
for i, b in enumerate(blocks[1:], 1):
    # eigenvalues appear after "bands (ev):" or right after the k line
    m = re.search(r"bands \(ev\):\s*\n(.*?)(?:\n\s*\n|\n\s*k =|\Z)", b, re.S)
    seg = m.group(1) if m else b
    nums = re.findall(r"[-]?\d+\.\d+", seg)
    eigs = sorted(float(x) for x in nums)
    if len(eigs) > 10:
        all_eigs.append(eigs)

print(f"# file: {fn}")
print(f"# Fermi energy E_F = {ef} eV")
if homo_lumo:
    h, l = homo_lumo
    print(f"# QE-printed HOMO/LUMO: {h} / {l} eV  -> gap = {l-h:.4f} eV")

if ef is not None and all_eigs:
    # gap from smearing run: per-k, highest eig below E_F and lowest above E_F
    vbm = -1e9  # valence band max (highest occupied across all k)
    cbm = 1e9   # conduction band min (lowest unoccupied across all k)
    vbm_k = cbm_k = -1
    for ki, eigs in enumerate(all_eigs):
        below = [e for e in eigs if e <= ef]
        above = [e for e in eigs if e > ef]
        if below and max(below) > vbm:
            vbm = max(below); vbm_k = ki
        if above and min(above) < cbm:
            cbm = min(above); cbm_k = ki
    print(f"# n k-blocks parsed = {len(all_eigs)}, bands/k = {len(all_eigs[0])}")
    print(f"# VBM (highest occ, any k) = {vbm:.4f} eV at kblock {vbm_k}")
    print(f"# CBM (lowest unocc, any k) = {cbm:.4f} eV at kblock {cbm_k}")
    gap = cbm - vbm
    print(f"# INDIRECT gap (CBM-VBM) = {gap:.4f} eV  {'(metallic/overlap)' if gap<=0 else ''}")
    # also direct gap: min over k of (lowest above - highest below) at same k
    direct = 1e9
    for eigs in all_eigs:
        below = [e for e in eigs if e <= ef]; above = [e for e in eigs if e > ef]
        if below and above:
            direct = min(direct, min(above) - max(below))
    if direct < 1e8:
        print(f"# DIRECT gap (min over k) = {direct:.4f} eV")
