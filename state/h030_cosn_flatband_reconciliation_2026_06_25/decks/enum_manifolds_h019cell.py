import re
EF=16.0015
txt=open('out/cosn.bands.out').read()
# isolate the band-structure section (after "End of band structure" or just parse all 'bands (ev):' blocks at end)
# Find the LAST occurrence region: split on 'bands (ev):'
chunks=txt.split('bands (ev):')
kdata=[]
for c in chunks[1:]:
    lines=c.split('\n')
    evs=[]
    for ln in lines:
        if 'k =' in ln: break
        if 'occupation' in ln or 'Fermi' in ln or 'End of' in ln: break
        nums=re.findall(r'-?\d+\.\d+',ln)
        # only accept lines that are pure numbers
        if nums and re.match(r'^[\s\-0-9.]+$',ln.rstrip()) and ln.strip():
            evs+=[float(x) for x in nums]
        elif evs and not ln.strip():
            continue
    if evs: kdata.append(evs)
nb=min(len(e) for e in kdata)
print(f"{len(kdata)} k-points parsed, {nb} bands, E_F={EF} eV (H_019 non-spin-pol cell)")
rows=[]
for ib in range(nb):
    vals=[e[ib] for e in kdata]
    w=max(vals)-min(vals); mid=(max(vals)+min(vals))/2-EF
    rows.append((ib+1,w,mid,min(vals)-EF,max(vals)-EF))  # 1-indexed band#
print("\n=== ALL narrow bands (W<0.30 eV) within +/-3 eV of E_F, by position ===")
narrow=[r for r in rows if r[1]<0.30 and -3.0<r[2]<3.0]
narrow.sort(key=lambda r:r[2])  # by position
print(f"{'band':>4} {'W(eV)':>7} {'mid-EF':>8} {'min-EF':>8} {'max-EF':>8}")
for r in narrow:
    print(f"{r[0]:>4} {r[1]:>7.3f} {r[2]:>+8.3f} {r[3]:>+8.3f} {r[4]:>+8.3f}")
print("\n=== narrowest 12 overall within +/-3 eV ===")
near=[r for r in rows if -3.0<r[2]<3.0]
near.sort(key=lambda r:r[1])
for r in near[:12]:
    print(f"band {r[0]:>3}  W={r[1]:.3f}  mid={r[2]:+.3f}  range[{r[3]:+.3f},{r[4]:+.3f}]")
