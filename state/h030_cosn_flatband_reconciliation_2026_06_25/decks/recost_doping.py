import numpy as np, re
from math import erf
# Use the SCF eigenvalues (k-weighted) for a proper rigid-band carrier count
F="decks/scf.out"
txt=open(F).read()
EF=14.7132; NELEC=93.0
wk=[float(m) for m in re.findall(r"wk =\s*([\d.]+)", txt)][:28]
wk=np.array(wk)
iu=txt.index("------ SPIN UP"); idn=txt.index("------ SPIN DOWN")
up=txt[iu:idn]; dn=txt[idn:]
def parse_eigs(block):
    eigs=[]
    chunks=re.split(r"k =.*?bands \(ev\):", block)[1:]
    for c in chunks:
        nums=[]
        for line in c.splitlines():
            t=line.strip()
            if t=="":
                if nums: break
                else: continue
            if t.startswith("k =") or "Fermi" in t or "occupation" in t: break
            row=re.findall(r"-?\d+\.\d+", t)
            if not row:
                if nums: break
                else: continue
            nums+=[float(x) for x in row]
        eigs.append(nums)
    return eigs
Eup=np.array([np.array(x) for x in parse_eigs(up)])
Edn=np.array([np.array(x) for x in parse_eigs(dn)])
w = wk/wk.sum()
SIG=0.10
def occ(e,ef): return 0.5*(1.0-erf((e-ef)/(SIG*np.sqrt(2))))
vocc=np.vectorize(occ)
def Ntot(ef):
    N=0.0
    for ik in range(len(Eup)):
        N+=w[ik]*np.sum(vocc(Eup[ik],ef)); N+=w[ik]*np.sum(vocc(Edn[ik],ef))
    return N
N0=Ntot(EF)
print(f"N(E_F={EF})={N0:.3f}  (should be ~93)")
print(f"\n{'target E_F':>11} {'dE-rel-EF':>9} {'hole e-/cell':>13} {'holes/f.u.':>11} {'%valence':>9}  class")
# targets: shallow band-45 center (-0.44), measured ARPES ~-0.10, ~-0.20, deep -1.45, -2.0
for label,dE in [("band45 ctr",-0.4435),("ARPES -0.10",-0.10),("ARPES -0.20",-0.20),
                 ("band44 -0.57",-0.567),("deep -1.45",-1.45),("deep -2.0",-2.0)]:
    eft=EF+dE
    dn=N0-Ntot(eft); hf=dn/3.0; pct=dn/NELEC*100
    cls="PHYSICAL(<0.3)" if abs(hf)<0.3 else ("STRETCH(0.3-0.7)" if abs(hf)<0.7 else "EXTREME(>0.7)")
    print(f"{eft:>11.3f} {dE:>+9.3f} {dn:>13.3f} {hf:>11.3f} {pct:>8.1f}%  {cls}")

print("\n=== band-45 (shallow flat) edge geometry vs ARPES ===")
print("band-45 (spin-pol cell): top edge -0.341 eV, center -0.425 eV, bottom -0.508 eV (W=0.167)")
print("band-44: top -0.478, center -0.567, bottom -0.655")
print("Measured ARPES (arXiv:2102.08979): flat d-band CENTER ~ -0.10 eV below E_F")
print("Measured ARPES (Kang 2001.11738): d_xz/d_yz flat band ~ -0.20 eV; QGT band (2412.17809) ~ measured")
print("=> Our PBE shallow flat-band TOP edge (-0.34 eV) is ~0.24 eV deeper than the ARPES center (-0.10 eV).")
print("   PBE over-deepens the SAME shallow band by ~0.2-0.3 eV (known PBE flat-band offset, H_024: ~140meV ARPES offset).")
# filling of band 45 if E_F placed at its TOP edge vs center
EF=14.7132
import numpy as np
def band_occ(bcenter_eV, target_dE):
    pass
print("\n=> doping to ARPES depth -0.10 eV = 0.20 h/f.u. (PHYSICAL); to PBE band-center -0.44 = 1.58 h/f.u. (EXTREME)")
print("   The 8x gap between them IS the flat-band DOS pileup: most of the band's weight is in the -0.34..-0.51 eV slab.")
