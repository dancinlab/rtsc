#!/usr/bin/env python3
"""
H_029 — CoSn correlation lens: DFT+U flat-band position vs U.
For each U in {1,2,3,4,5}: read scf_U{U}.out (E_F, magnetization) and
cosnU{U}_bands.dat.gnu (60 bands x 161 k), locate the flat band near E_F on the
Gamma-K-M-Gamma (kz=0) plane, report E_flat-E_F and W, and recompute the
NN-kagome TB-fit metric integral I = (1/2pi) int tr g d2k (SAME route as H_024/H_027).
Honest: every number is verbatim pw.x stdout or a labelled deterministic TB fit.
"""
import numpy as np, math, re, sys, glob, os
from math import erf

A_LAT = 9.9760*0.529177  # Angstrom hexagonal a (same cell as H_027)
PLANE_N = 121            # kz=0 kagome plane points on the G-K-M-G path (first 3 segments)

def load_gnu(path):
    blocks=[];cur=[]
    for line in open(path):
        s=line.strip()
        if not s:
            if cur: blocks.append(cur);cur=[]
            continue
        p=s.split();cur.append((float(p[0]),float(p[1])))
    if cur: blocks.append(cur)
    return blocks

def get_EF(scfout):
    txt=open(scfout).read()
    m=re.findall(r"the Fermi energy is\s*([-\d.]+)\s*ev", txt)
    if not m:
        m=re.findall(r"Fermi energy is\s*([-\d.]+)", txt)
    ef=float(m[-1])
    mag=re.findall(r"total magnetization\s*=\s*([-\d.]+)\s*Bohr", txt)
    absmag=re.findall(r"absolute magnetization\s*=\s*([-\d.]+)\s*Bohr", txt)
    conv = "convergence has been achieved" in txt
    niter=re.findall(r"convergence has been achieved in\s*(\d+)", txt)
    return ef, (float(mag[-1]) if mag else None), (float(absmag[-1]) if absmag else None), conv, (int(niter[-1]) if niter else None)

def split_spin(blocks, nbnd=60):
    """nspin=2 bands.x writes 2*nbnd blocks (spin-up then spin-down). Return
    (up_blocks, dn_blocks) if 120-block, else (all, None) for a single channel."""
    if len(blocks) >= 2*nbnd:
        return blocks[:nbnd], blocks[nbnd:2*nbnd]
    return blocks, None

FLAT_W = 0.40   # a kagome flat band is genuinely narrow (W < ~0.40 eV on the kz=0 plane)
FLAT_WIN = 6.5  # search the flat band within this many eV of E_F (it sinks deep at high U)

def flat_scan(blocks, ef, spin_label=""):
    """Identify the kagome FLAT band (genuinely narrow, W<FLAT_W) closest to E_F.
    Scanning the WHOLE spectrum (not a near-E_F window) so the flat band is tracked
    even when +U sinks it far below E_F. Falls back to the flattest near-E_F band if
    no narrow band is found."""
    rows=[]
    for i,b in enumerate(blocks):
        E=np.array([e for _,e in b])[:PLANE_N]
        rows.append((i+1, E.mean(), E.max()-E.min(), E.min(), E.max(), spin_label))
    narrow=[r for r in rows if r[2] < FLAT_W and abs(r[1]-ef) < FLAT_WIN]
    if narrow:
        # among genuinely-narrow bands, pick the one closest to E_F (lever-relevant)
        narrow.sort(key=lambda r: abs(r[1]-ef))
        ranked=narrow
    else:
        # no narrow band within 4 eV -> report the flattest within 2.6 eV (degenerate case)
        ranked=sorted([r for r in rows if abs(r[1]-ef)<2.6], key=lambda r:r[2])
    return ranked, {r[0]:r for r in rows}

# --- NN-kagome TB-fit metric (verbatim H_027 route) ---
def Hk(k1,k2,t,e0):
    pab=math.pi*k1; pac=math.pi*k2; pbc=math.pi*(k2-k1)
    return np.array([[e0,-2*t*math.cos(pab),-2*t*math.cos(pac)],
                     [-2*t*math.cos(pab),e0,-2*t*math.cos(pbc)],
                     [-2*t*math.cos(pac),-2*t*math.cos(pbc),e0]],dtype=float)

def metric_integral(t,e0,a_lat,Ngrid=60,cap=200.0):
    es=[np.sort(np.linalg.eigvalsh(Hk(i/12,j/12,t,e0))) for i in range(12) for j in range(12)]
    es=np.array(es); fi=int(np.argmin(es.max(0)-es.min(0)))
    B=4*math.pi/(math.sqrt(3)*a_lat)
    Gm=np.array([[B*B,-0.5*B*B],[-0.5*B*B,B*B]]); Ginv=np.linalg.inv(Gm)
    BZ=B*B*math.sqrt(3)/2
    def proj(k1,k2):
        w,v=np.linalg.eigh(Hk(k1,k2,t,e0)); o=np.argsort(w)
        u=v[:,o[fi]]; return np.outer(u,u.conj())
    dk=1.0/Ngrid; h=dk; samp=[]; ndiv=0
    for i in range(Ngrid):
        for j in range(Ngrid):
            k1=i*dk;k2=j*dk
            dP1=(proj(k1+h,k2)-proj(k1-h,k2))/(2*h)
            dP2=(proj(k1,k2+h)-proj(k1,k2-h))/(2*h)
            g11=0.5*np.real(np.trace(dP1@dP1)); g22=0.5*np.real(np.trace(dP2@dP2))
            g12=0.5*np.real(np.trace(dP1@dP2))
            trg=np.sum(Ginv*np.array([[g11,g12],[g12,g22]]))
            if not np.isfinite(trg): continue
            if trg>cap: ndiv+=1; trg=cap
            samp.append(trg)
    samp=np.array(samp); avg=samp.mean()
    return avg*BZ/(2*math.pi), avg, ndiv

def analyze_U(U, ddir):
    scfout=os.path.join(ddir,f"scf_U{U}.out")
    gnu=os.path.join(ddir,f"cosnU{U}_bands.dat.gnu")
    if not (os.path.exists(scfout) and os.path.exists(gnu)):
        return None
    ef,mag,absmag,conv,niter=get_EF(scfout)
    blocks=load_gnu(gnu)
    if len(blocks)<2: return None
    # nspin=2 bands.x writes ONE spin channel here (60 blocks, same as H_027 PBE).
    up,dn=split_spin(blocks,60)
    chan = up  # single channel present in the .gnu
    # PRIMARY: track the kagome flat band by IDENTITY = the genuinely-narrow (W<FLAT_W)
    # band CLOSEST to E_F. As +U sinks the kagome manifold, this follows the same flat
    # feature down (cross-checked against the fixed PBE near-E_F band 45 below).
    ranked, allrows = flat_scan(chan, ef)
    flat=ranked[0]
    bidx,Eflat,Wflat=flat[0],flat[1],flat[2]
    means={k:v[1] for k,v in allrows.items()}
    grp=[bidx-1,bidx,bidx+1] if (bidx-1 in means and bidx+1 in means) else [bidx,bidx+1,bidx+2]
    gE=[means[b] for b in grp if b in means]
    span=max(gE)-min(gE); t_fit=span/6.0; e0_fit=Eflat-2*t_fit
    I,avg,ndiv=metric_integral(t_fit,e0_fit,A_LAT)
    # CROSS-CHECK: the fixed PBE near-E_F kagome flat band index (45) trajectory
    ref=allrows.get(45)
    ref_dE = (ref[1]-ef) if ref else None
    ref_W  = ref[2] if ref else None
    return dict(U=U,ef=ef,mag=mag,absmag=absmag,conv=conv,niter=niter,nbk=len(blocks),
                bidx=bidx,Eflat=Eflat,dE=Eflat-ef,W=Wflat,I=I,t=t_fit,span=span,grp=grp,
                spin="", other=None, ref_dE=ref_dE, ref_W=ref_W)

def main():
    ddir=sys.argv[1] if len(sys.argv)>1 else "."
    print("="*78)
    print("H_029 — CoSn CORRELATION LENS (DFT+U ortho-atomic on Co-3d): E_flat-E_F vs U")
    print("  cell = H_027 spin-pol Co3Sn3 (a=9.9760 a.u., c/a=0.80680, 93 e-)")
    print("  PBE baseline (U=0, H_027): near-E_F flat band 45, dE=-0.4435 eV, W=0.167, I=2.855")
    print("="*78)
    print(f"\n{'U(eV)':>6} {'conv':>5} {'niter':>6} {'E_F(eV)':>9} {'|mag|μB':>8} "
          f"{'band':>5} {'E_flat-E_F':>11} {'W(eV)':>7} {'I=∫trg/2π':>10}  {'band45 dE(W)':>14}")
    rows=[]
    # U=0 PBE baseline from H_027 (verbatim)
    print(f"{'0*':>6} {'Y':>5} {'25':>6} {'14.7132':>9} {'0.43':>8} "
          f"{'45':>5} {'-0.4435':>11} {'0.167':>7} {'2.855':>10}  {'-0.444(0.17)':>14}")
    for U in [1,2,3,4,5]:
        r=analyze_U(U,ddir)
        if r is None:
            print(f"{U:>6} {'--':>5} (pending/missing)")
            continue
        rows.append(r)
        amags=f"{r['absmag']:.2f}" if r['absmag'] is not None else "?"
        rf=f"{r['ref_dE']:+.3f}({r['ref_W']:.2f})" if r['ref_dE'] is not None else "-"
        print(f"{U:>6} {'Y' if r['conv'] else 'N':>5} {str(r['niter']):>6} {r['ef']:>9.4f} "
              f"{amags:>8} {r['bidx']:>5} {r['dE']:>+11.4f} {r['W']:>7.4f} {r['I']:>10.4f}  {rf:>14}")
    print("\n* U=0 row = H_027 PBE baseline (reproduced verbatim, not recomputed here).")
    print("  band/E_flat-E_F/W = the kagome FLAT band (genuinely narrow, W<%.2f eV) CLOSEST to E_F."%FLAT_W)
    print("  band45 dE(W) = the FIXED PBE near-E_F kagome flat-band index (45) trajectory")
    print("  (orbital-consistent cross-check; same flat feature tracked down as +U sinks it).")
    # verdict logic
    print("\n--- VERDICT LOGIC ---")
    if rows:
        approaches=[r for r in rows if r['dE']>-0.2]
        survives=[r for r in rows if r['I']>=2.0]
        print(f"flat band within 0.2 eV of E_F at any U: "
              f"{'YES @ U='+','.join(str(r['U']) for r in approaches) if approaches else 'NO'}")
        print(f"∫tr g >= 2 (geometry survives) at: U="
              f"{','.join(str(r['U']) for r in survives) if survives else 'none'}")
        dEs=[r['dE'] for r in rows]
        print(f"E_flat-E_F range across U=1..5: [{min(dEs):+.3f}, {max(dEs):+.3f}] eV (PBE U=0: -0.444)")
        # magnetic order watch
        mags=[r['absmag'] for r in rows if r['absmag'] is not None]
        if mags:
            print(f"absolute magnetization range: [{min(mags):.2f}, {max(mags):.2f}] uB/cell "
                  f"(PBE residual ~0.43) -- watch for U-induced magnetic order")
    print("="*78)

if __name__=='__main__': main()
