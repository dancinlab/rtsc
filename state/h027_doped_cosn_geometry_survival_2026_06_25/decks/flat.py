import numpy as np
EF=14.7132
# parse .dat.gnu : 60 blocks each 161 (kx,E) separated by blank line
blocks=[]
cur=[]
for line in open("/home/summer/rtsc_cosn/cosn_bands.dat.gnu"):
    s=line.strip()
    if not s:
        if cur: blocks.append(cur); cur=[]
        continue
    p=s.split()
    cur.append((float(p[0]),float(p[1])))
if cur: blocks.append(cur)
print("nbands=",len(blocks),"nk=",len(blocks[0]))
nb=len(blocks); nk=len(blocks[0])
# k-index ranges: Gamma-K-M-Gamma = first 121 pts (segments 1-3, kz=0 kagome plane)
plane=slice(0,121)
rows=[]
for i,b in enumerate(blocks):
    E=np.array([e for _,e in b])
    Ep=E[plane]
    disp=Ep.max()-Ep.min()
    mean=Ep.mean()
    rows.append((i+1,mean,disp,Ep.min(),Ep.max()))
# bands with mean within +-2 eV of EF, sorted by dispersion (flattest first)
near=[r for r in rows if abs(r[1]-EF)<2.5]
near.sort(key=lambda r:r[2])
print("\n# Bands within 2.5 eV of E_F=%.4f, sorted by Gamma-K-M dispersion (flattest first):"%EF)
print("band  meanE(eV)  disp(eV)  Emin     Emax    dE=mean-EF")
for r in near[:8]:
    print("%4d  %8.4f  %7.4f  %7.4f  %7.4f   %+7.4f"%(r[0],r[1],r[2],r[3],r[4],r[1]-EF))
# overall flattest band anywhere in plane
allf=sorted(rows,key=lambda r:r[2])
print("\n# Flattest 5 bands overall (Gamma-K-M):")
for r in allf[:5]:
    print("band %d meanE=%.4f disp=%.4f dE=%.4f"%(r[0],r[1],r[2],r[1]-EF))
