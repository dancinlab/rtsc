"""
Scan a QE scf.out (verbosity='high') for flat bands near E_F.
For each band index, compute bandwidth W = max_k(E) - min_k(E) over the IBZ k-points
printed after the final SCF iteration, and flag narrow bands (W small) that sit near
or cross the Fermi energy — the flat-band@E_F gate for the FB-GEOM superconductivity
candidate screen. Run on the compute host: python3 flat_band_scan.py scf.out <E_F_eV>
"""
# @convergence state=ossified id=FBGEOM-LIGHT-ELEM value="light-element (Li/Be/B/C) metals carry wide sigma/pi dispersive bands at E_F — flat-band@E_F is structurally absent (LiBeB/Be4B/LiC12 all FAIL)" threshold="a 'metallic + light-element' catalogue filter does NOT guarantee flat-band@E_F; flat-band needs a d-electron kagome/Lieb lattice topology. Screen lattice topology BEFORE heavy DFT."
# @convergence state=ossified id=DELEC-DETACH-DEATH value="a long d-electron scf (slow per-iteration) dies even under setsid+nohup when the SSH exec session ends (RhPb died at iter#2; light-element runs finish fast enough to escape it)" threshold="launch d-electron / long DFT via 'tmux new-session -d' (SSH-independent); if a detach launch shows PWX=0 after grid setup, relaunch under tmux."
import re
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "scf.out"
ef = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0

txt = open(path).read()
end = txt.rfind("End of self-consistent calculation")
seg = txt[end:] if end > 0 else txt

# QE prints, per k-point:  "...bands (ev):\n\n   E1  E2  E3 ...\n\n"
blocks = re.findall(r"bands \(ev\):\s*\n\s*\n(.*?)(?=\n\s*\n)", seg, re.S)
bands = []
for b in blocks:
    vals = []
    for tok in b.split():
        try:
            vals.append(float(tok))
        except ValueError:
            pass
    if vals:
        bands.append(vals)

if not bands:
    print("NO_BANDS_PARSED")
    sys.exit(0)

nb = min(len(x) for x in bands)
nk = len(bands)
cols = [[bands[k][i] for k in range(nk)] for i in range(nb)]

print("nk=%d nband=%d EF=%.4f" % (nk, nb, ef))
print("--- bands within +/-3 eV of E_F (W=bandwidth) ---")
flat_hits = []
for i in range(nb):
    c = cols[i]
    lo, hi = min(c), max(c)
    w = hi - lo
    mid = 0.5 * (lo + hi)
    if abs(mid - ef) < 3.0:
        cross = lo < ef < hi
        tag = "  <== FLAT@EF" if (w < 0.6 and (cross or abs(mid - ef) < 1.0)) else ""
        if tag:
            flat_hits.append((i, w))
        print("band%2d: W=%.3f eV  [%.2f, %.2f]  EF_cross=%s%s" % (i, w, lo, hi, cross, tag))
print("FLAT_AT_EF_COUNT=%d" % len(flat_hits))
if flat_hits:
    bi, bw = min(flat_hits, key=lambda t: t[1])
    print("NARROWEST_NEAR_EF: band%d W=%.3f eV" % (bi, bw))
