import numpy as np
EF=14.7132
blocks=[]; cur=[]
for line in open("decks/cosn_bands.dat.gnu"):
    s=line.strip()
    if not s:
        if cur: blocks.append(cur); cur=[]
        continue
    p=s.split(); cur.append((float(p[0]),float(p[1])))
if cur: blocks.append(cur)
nb=len(blocks); nk=len(blocks[0])
print(f"nbands={nb} nk={nk}  E_F={EF} eV (H_027/H_029 SPIN-POL Co3Sn3 cell)")
plane=slice(0,121)  # Gamma-K-M-Gamma kz=0 plane
rows=[]
for i,b in enumerate(blocks):
    E=np.array([e for _,e in b]); Ep=E[plane]
    w=Ep.max()-Ep.min(); mid=(Ep.max()+Ep.min())/2-EF
    rows.append((i+1,w,mid,Ep.min()-EF,Ep.max()-EF))
print("\n=== ALL narrow bands (W<0.30 eV) within +/-3 eV of E_F, by position ===")
narrow=[r for r in rows if r[1]<0.30 and -3.0<r[2]<3.0]
narrow.sort(key=lambda r:r[2])
print(f"{'band':>4} {'W(eV)':>7} {'mid-EF':>8} {'min-EF':>8} {'max-EF':>8}")
for r in narrow:
    print(f"{r[0]:>4} {r[1]:>7.3f} {r[2]:>+8.3f} {r[3]:>+8.3f} {r[4]:>+8.3f}")
print("\n=== bands within +/-1.0 eV of E_F (any width) ===")
for r in sorted([r for r in rows if -1.0<r[2]<1.0], key=lambda r:r[2]):
    print(f"band {r[0]:>3}  W={r[1]:.3f}  mid={r[2]:+.3f}  range[{r[3]:+.3f},{r[4]:+.3f}]")
