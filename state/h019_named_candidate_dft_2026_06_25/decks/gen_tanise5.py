# Generate Ta2NiSe5 Cmcm (#63) conventional cell atom list from Wyckoff sites.
# a=3.5029 b=12.8699 c=15.6768. Cmcm symmetry operations (#63), then C-centering (0,0,0)+(1/2,1/2,0).
import itertools
a,b,c = 3.5029, 12.8699, 15.6768

# Cmcm general positions (without centering) for the point group operations of Cmcm.
# Cmcm = C-centered, generators: mirror m_z (x,y,-z? ) -- use the standard 16 ops of Cmcm:
# Standard Cmcm (#63) coordinates of equivalent positions (from ITA), centering (0,0,0)(1/2,1/2,0):
# (1) x,y,z (2) -x,-y,z+1/2 (3) x,-y,-z+1/2 (4) -x,y,z  -- careful. Use ITA #63 list:
ops = [
    lambda x,y,z:( x, y, z),
    lambda x,y,z:(-x,-y,-z),
    lambda x,y,z:(-x,-y, z+0.5),
    lambda x,y,z:( x, y,-z+0.5),
    lambda x,y,z:(-x, y,-z+0.5),
    lambda x,y,z:( x,-y, z+0.5),
    lambda x,y,z:( x,-y,-z),
    lambda x,y,z:(-x, y, z),
]
cent = [(0,0,0),(0.5,0.5,0.0)]

def frac(v): return v - round(v - 1e-9) if False else v%1.0

sites = {
 'Ta':[(0.5,0.221158,0.110222)],
 'Ni':[(1.0,0.20096,0.25)],
 'Se':[(0.5,0.32679,0.25),(0.0,0.354170,0.049338),(1.0,0.080461,0.137726)],
}

out={}
for el,wlist in sites.items():
    pts=set()
    for (x,y,z) in wlist:
        for op in ops:
            xx,yy,zz=op(x,y,z)
            for (cx,cy,cz) in cent:
                p=(round((xx+cx)%1.0,6),round((yy+cy)%1.0,6),round((zz+cz)%1.0,6))
                pts.add(p)
    out[el]=sorted(pts)

tot=0
lines=[]
for el in ['Ta','Ni','Se']:
    for p in out[el]:
        lines.append(f"  {el}  {p[0]:.6f}  {p[1]:.6f}  {p[2]:.6f}")
        tot+=1
    print(f"# {el}: {len(out[el])} atoms")
print(f"# TOTAL {tot} (expect Ta8 Ni4 Se20 = 32)")
with open('/private/tmp/claude-501/-Users-mini-dancinlab-rtsc/94aead32-aac7-4cc9-ad44-1550c188a432/scratchpad/tanise5_atoms.txt','w') as f:
    f.write("\n".join(lines)+"\n")
print("\n".join(lines))
