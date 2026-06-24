"""
L44 S3-full analysis: D_s(|U|) from ALF kagome flat-band attractive-Hubbard twist sweep.
Parse Ener_scal raw (col: N (Re,Im) weight) per U,Phi -> E(Phi) mean +/- stderr (warmup-dropped).
D_s ~ 2*(E(Phi)-E(0))/Phi^2 per-site (108=6x6x3). Strong-coupling U=8 BEC-side: D_s sustain=PASS / collapse=FALSIFY.
NB: U=8 p0.00 only ~11 bins (ALF crashes at bin~12 for strong-coupling Phi=0) -> noisy, flagged.
# @convergence state=stable id=ALF-STRONGU-NWRAP value="strong-coupling attractive-Hubbard DQMC (|U|>=8) crashes near bin~12 with default Nwrap=10 (matrix condition-number blowup at large U)" threshold="halve Nwrap (10->5) for |U|>=8 to re-orthogonalize twice as often; stabilizes the strong-coupling run"
"""
import re, os, math, glob

BASE = os.path.expanduser("~/kagome_run/production")
NSITES = 108
WARMUP = 5  # drop first bins

def parse_E(path):
    vals = []
    f = path + "/Ener_scal"
    if not os.path.exists(f):
        return None
    for line in open(f):
        m = re.search(r"\(\s*([-0-9.E+]+)\s*,", line)
        if m:
            try:
                vals.append(float(m.group(1)))
            except ValueError:
                pass
    if len(vals) <= WARMUP + 2:
        return (None, None, len(vals))
    v = vals[WARMUP:]
    n = len(v)
    mean = sum(v) / n
    var = sum((x - mean) ** 2 for x in v) / (n - 1)
    return (mean, math.sqrt(var / n), n)

print("=" * 78)
print("[D_s(|U|)] kagome flat-band attractive-Hubbard twist-sweep (per-site, 108 sites)")
print("=" * 78)
print(f"{'U':>5}{'E(0)':>12}{'E(.02)':>12}{'E(.04)':>12}{'D_s(.02)':>11}{'D_s(.04)':>11}  note")
rows = []
for U in [1.0, 2.0, 4.0, 8.0]:
    Es = {}
    for phi in [0.00, 0.02, 0.04]:
        d = f"{BASE}/U{U}_p{phi:.2f}"
        Es[phi] = parse_E(d)
    e0 = Es[0.00]; e2 = Es[0.02]; e4 = Es[0.04]
    def ds(ephi, phi, e0):
        if not ephi or not e0 or ephi[0] is None or e0[0] is None:
            return None
        return 2.0 * (ephi[0] - e0[0]) / (phi ** 2) / NSITES
    d2 = ds(e2, 0.02, e0); d4 = ds(e4, 0.04, e0)
    def fmt(e): return f"{e[0]:.3f}" if e and e[0] is not None else "NA"
    nb0 = e0[2] if e0 else 0
    note = "OK" if nb0 >= 35 else f"p0.00 only {nb0}b (noisy)"
    print(f"{U:>5.0f}{fmt(e0):>12}{fmt(e2):>12}{fmt(e4):>12}"
          f"{(f'{d2:.4f}' if d2 is not None else 'NA'):>11}"
          f"{(f'{d4:.4f}' if d4 is not None else 'NA'):>11}  {note}")
    rows.append((U, d2, d4, nb0))
print("-" * 78)
print("[해석] D_s>0 = 초유체 강성 존재(diamagnetic twist response). U 따라 추세:")
print("  약→강결합서 D_s 포화/유지면 처방 PASS(geometric stiffness가 BEC localize 막음),")
print("  급감하면 FALSIFY. 단 U=8 p0.00=11bins라 강결합점 노이즈 큼(d6 정직).")
print("[d6] twist Phi 곡률 노이즈·작은Phi 2점 곡률·warmup 5 drop. 절대 Tc 아님(상대 D_s 추세).")
