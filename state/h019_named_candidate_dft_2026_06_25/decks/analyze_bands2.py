import re
EF=16.0015
txt=open('/private/tmp/claude-501/-Users-mini-dancinlab-rtsc/94aead32-aac7-4cc9-ad44-1550c188a432/scratchpad/cosn_bands_block1.txt').read()
# split into k-blocks
blocks=re.split(r'k = ',txt)
kdata=[]
klabels=['G','GM.25','M','MK.1','MK.2','K','KG.3','KG.6','G(end)']
for b in blocks[1:]:
    lines=b.split('\n')
    kxyz=lines[0].split('(')[0].strip()
    evs=[]
    for ln in lines[1:]:
        nums=re.findall(r'-?\d+\.\d+',ln)
        if nums and re.match(r'^[\s\-0-9.]+$',ln) and ln.strip():
            evs+=[float(x) for x in nums]
    if evs: kdata.append((kxyz,evs))
nb=min(len(e) for _,e in kdata)
print(f"{len(kdata)} k-points, {nb} bands, E_F={EF}")
# bandwidth per band over the path
print("\nbands near E_F (band#, W=max-min over path, mid-EF, min-EF, max-EF):")
rows=[]
for ib in range(nb):
    vals=[e[ib] for _,e in kdata]
    w=max(vals)-min(vals); mid=(max(vals)+min(vals))/2-EF
    rows.append((ib,w,mid,min(vals)-EF,max(vals)-EF))
near=[r for r in rows if -2.5<r[2]<2.5]
near.sort(key=lambda r:r[1])
for r in near[:10]:
    print(f"  band {r[0]:2d}  W={r[1]:.3f} eV  mid={r[2]:+.3f}  range[{r[3]:+.3f},{r[4]:+.3f}] eV")
print("\nAll bands sorted by width (narrowest):")
for r in sorted(rows,key=lambda r:r[1])[:8]:
    print(f"  band {r[0]:2d}  W={r[1]:.3f} eV  mid={r[2]:+.3f} eV")
# print the eigenvalues 14-17 eV across k to eyeball flatness
print("\nEigenvalues in [13.5,16.5] eV at each k (band manifold near E_F):")
for kxyz,evs in kdata:
    near_ef=[f"{v:.2f}" for v in evs if 13.5<v<16.5]
    print(f"  k={kxyz:22s}: {near_ef}")
