import numpy as np
EF=14.7132
blocks=[];cur=[]
for line in open("/home/summer/rtsc_cosn/cosn_bands.dat.gnu"):
    s=line.strip()
    if not s:
        if cur: blocks.append(cur);cur=[]
        continue
    p=s.split();cur.append((float(p[0]),float(p[1])))
if cur: blocks.append(cur)
# crude states-counting on the band-path (NOT a proper BZ integral, indicative only)
# count band-eigenvalues in window [E_flat_center, E_F] across all path k-pts / nk = avg occupancy gain
nk=len(blocks[0])
Eflat=14.2697  # band 45 center
gained=0.0
for b in blocks:
    E=np.array([e for _,e in b])
    # fraction of k where this band sits in (Eflat, EF) -> states that would fill on raising occ to EF
    frac=np.mean((E>Eflat)&(E<EF))
    gained+=frac*2  # spin factor approx (2 e- per filled band-state); nspin handled crudely
print("path-based crude states between flat-band center(%.3f) and E_F(%.3f): ~%.3f e-/cell"%(Eflat,EF,gained))
print("(indicative ONLY - path sampling, not a tetrahedron BZ integral)")
