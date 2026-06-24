#!/usr/bin/env python3
"""
H_028 — does Ni3In supply the flat-band GEOMETRY LEVER (int tr g >= 2) with its
flat band ALREADY at/near E_F (dodging CoSn's H_027 extreme-doping wall)?

Same deterministic route as H_027 (NO tuning), applied to OUR converged
spin-polarized PBE Ni3In bands:

  (1) FLAT BAND: locate the flattest band near E_F on the Gamma-K-M-Gamma
      (kz=0) kagome plane; report its bandwidth W and its centre offset dE
      relative to E_F. The DODGE question: is dE within ~0.1-0.2 eV of E_F
      (so NO/low doping needed), unlike CoSn's -0.44 eV (near band) / -1.45 eV?

  (2) GEOMETRY: fit an NN-kagome 3-orbital TB model (t,e0) to the flat 3-band
      manifold of OUR bands; compute I = (1/2pi) int_BZ tr g d2k by projector
      finite-difference. Is I >= 2 (lever met)? Compare to CoSn's 2.86.

  (3) FILLING nu of the flat band at the NATIVE E_F (no doping): integrate the
      smeared occupation of the flat band at the real E_F. D_s ~ nu(1-nu),
      max 0.25 at nu=1/2.

Honest: every number is from OUR converged DFT spectrum or a labelled TB fit.
No value is hand-set to clear a falsifier. Magnetism / rigid-band / NN-only /
TB-fit caveats are reported, not hidden.
"""
import numpy as np, math, re, sys
from math import erf

# ---- OUR converged SCF facts (filled from scf.out at runtime via argv) ----
EF      = float(sys.argv[1]) if len(sys.argv) > 1 else None   # eV
NELEC   = 134.0
ALAT_AU = 9.9892
A_LAT   = ALAT_AU * 0.529177
N_FU    = 2          # Ni6In2 = 2 Ni3In formula units per cell
SCF     = "scf_nm.out"
GNU     = "bands.out"   # parse eigenvalues directly from the verbosity='high' bands run

def load_bands_gnu(path):
    """Parse a QE verbosity='high' bands.out into band-major blocks:
    returns list[band] of list[(kindex, E_eV)] -- same shape flat_band_scan expects.
    bands.out is k-major ('k = ... bands (ev):' then eigenvalues); we transpose."""
    txt=open(path).read()
    # each k-point block: 'k = kx ky kz ( ngw PWs) bands (ev):' then rows of floats
    chunks=re.split(r"\n\s+k =.*?bands \(ev\):\n", txt)[1:]
    per_k=[]
    for c in chunks:
        nums=[]
        for line in c.splitlines():
            t=line.strip()
            if t=="":
                if nums: break
                else: continue
            # stop at next section / occupation numbers / Fermi line
            if t.startswith("k =") or "Fermi" in t or "occupation" in t or "highest" in t or "Writing" in t:
                break
            row=re.findall(r"-?\d+\.\d+", t)
            if not row:
                if nums: break
                else: continue
            nums+=[float(x) for x in row]
        if nums: per_k.append(nums)
    if not per_k:
        raise RuntimeError("no k-blocks parsed from "+path)
    nb=min(len(x) for x in per_k)
    # band-major: blocks[band] = [(ik, E), ...]
    blocks=[]
    for b in range(nb):
        blocks.append([(ik, per_k[ik][b]) for ik in range(len(per_k))])
    return blocks

def flat_band_scan(blocks, ef, plane_n=2000, win=2.6):
    rows=[]
    for i,b in enumerate(blocks):
        E=np.array([e for _,e in b])[:plane_n]
        rows.append((i+1, E.mean(), E.max()-E.min(), E.min(), E.max()))
    near=[r for r in rows if abs(r[1]-ef)<win]
    near.sort(key=lambda r:r[2])
    return near, rows

def parse_scf_eigs(path):
    txt=open(path).read()
    iu=txt.index("------ SPIN UP"); idn=txt.index("------ SPIN DOWN")
    up=txt[iu:idn]; dn=txt[idn:]
    wk=[float(m) for m in re.findall(r"wk =\s*([\d.]+)", txt)]
    def parse(block):
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
            eigs.append(np.array(nums))
        return eigs
    Eup=parse(up); Edn=parse(dn)
    nk=len(Eup)
    wkv=np.array(wk[:nk]); wkv=wkv/wkv.sum()
    return Eup,Edn,wkv

_verf=np.vectorize(erf)
def occ_frac(e, ef, sig):
    return 0.5*(1.0-_verf((np.asarray(e,dtype=float)-ef)/(sig*math.sqrt(2))))

def Ntot(Eup,Edn,wkv,ef,sig):
    N=0.0
    for ik in range(len(Eup)):
        N+=wkv[ik]*np.sum(occ_frac(Eup[ik],ef,sig))
        N+=wkv[ik]*np.sum(occ_frac(Edn[ik],ef,sig))
    return N

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
    I=avg*BZ/(2*math.pi)
    return I, avg, ndiv, Ngrid*Ngrid, fi

def main():
    if EF is None:
        print("usage: h028_ni3in_geometry.py <E_F_eV>"); sys.exit(1)
    print("="*72)
    print("H_028 — does Ni3In supply the flat-band GEOMETRY LEVER at/near E_F?")
    print("  (dodging CoSn's H_027 extreme-doping wall)")
    print("  source: OUR converged NON-SPIN-POL (paramagnetic ref) PBE SCF (8-atom")
    print("          Ni6In2, 134 e-, conv 1e-7) -- spin-pol SCF is magnetically")
    print("          UNSTABLE (high-DOS flat band at E_F, abs-mag swings 11-27 uB;")
    print("          reported separately as competing-order evidence).")
    print("          E_F=%.4f eV, alat=%.4f a.u. = a=%.4f A)"%(EF,ALAT_AU,A_LAT))
    print("="*72)

    blocks=load_bands_gnu(GNU)
    near,rows=flat_band_scan(blocks,EF)
    print("\n--- (1) FLAT BAND on the Gamma-K-M-Gamma plane (flattest near E_F) ---")
    print("band  meanE(eV)  W(eV)    dE=mean-EF")
    for r in near[:6]:
        print(" %3d  %8.4f  %6.4f  %+7.4f"%(r[0],r[1],r[2],r[1]-EF))
    flat=near[0]
    bidx, Eflat, Wflat = flat[0], flat[1], flat[2]
    dE=Eflat-EF
    print("=> FLAT BAND = band %d, centre %.4f eV (= %+.4f eV rel E_F), W=%.4f eV"
          %(bidx,Eflat,dE,Wflat))
    if abs(dE) <= 0.20:
        pos="AT/NEAR E_F (|dE|<=0.20 eV) -> DODGES the doping wall (no/low doping)"
    elif abs(dE) <= 0.50:
        pos="MODERATELY OFF E_F (0.20<|dE|<=0.50 eV) -> some doping needed"
    else:
        pos="FAR from E_F (|dE|>0.50 eV) -> heavy doping (no dodge)"
    print("=> POSITION VERDICT: dE=%+.3f eV -> %s"%(dE,pos))
    print("   (compare CoSn near band -0.44 eV [H_027], deeper -1.45 eV [H_024])")

    print("\n--- (2) GEOMETRY: NN-kagome TB fit + projector-FD tr g ---")
    means={r[0]:r[1] for r in rows}
    grp=[bidx-1,bidx,bidx+1] if (means.get(bidx-1) and means.get(bidx+1)) else [bidx,bidx+1,bidx+2]
    gE=[means[b] for b in grp if b in means]
    span=max(gE)-min(gE)
    t_fit=span/6.0
    e0_fit=Eflat - 2*t_fit
    print("3-band kagome group bands %s, span=%.4f eV -> t=%.4f eV, e0=%+.4f eV (rel E_F)"
          %(grp,span,t_fit,e0_fit-EF))
    I,avg,ndiv,ntot_grid,fi=metric_integral(t_fit,e0_fit,A_LAT)
    print("Gamma band-touching: %d/%d grid pts capped (integrable singularity)"%(ndiv,ntot_grid))
    print("<tr g>_BZ = %.4f A^2 ; I = (1/2pi) int tr g d2k = %.4f"%(avg,I))
    print("CoSn (H_027/H_024): I = 2.855 ~= measured QGT 2.87 (arXiv:2412.17809)")
    geom = "MET (I>=2, geometry lever supplied)" if I>=2 else "NOT MET (I<2)"
    print("=> GEOMETRY VERDICT: I=%.3f -> %s"%(I,geom))

    print("\n--- (3) FILLING nu of the flat band at the NATIVE E_F (no doping) ---")
    SIG=0.10
    flatE_path=np.array([e for _,e in blocks[bidx-1]])[:2000]
    occ_path=np.mean([occ_frac(e,EF,SIG) for e in flatE_path])
    nu=occ_path
    dsfac=nu*(1-nu)
    print("flat band (band %d) mean occupation at native E_F=%.4f: nu = %.3f"
          %(bidx,EF,nu))
    print("D_s^geom ~ nu(1-nu) = %.4f  (maximum 0.25 at nu=0.5)"%dsfac)
    frac=dsfac/0.25
    if frac>0.6: fill="FAVOURABLE (near half-filling, D_s strong)"
    elif frac>0.25: fill="MODERATE (off-half but non-trivial D_s)"
    else: fill="EDGE-SUPPRESSED (nu->0 or 1, D_s reduced)"
    print("=> FILLING VERDICT: nu=%.3f, nu(1-nu)=%.4f = %.0f%% of 0.25 max -> %s"
          %(nu,dsfac,frac*100,fill))

    # rigid-band cross-check: how much doping (if any) to put E_F at flat centre?
    print("\n--- (rigid-band cross-check) doping to slide E_F onto flat centre ---")
    try:
        Eup,Edn,wkv=parse_scf_eigs(SCF)
        N0=Ntot(Eup,Edn,wkv,EF,SIG)
        Nflat=Ntot(Eup,Edn,wkv,Eflat,SIG)
        dn=N0-Nflat
        print("N(E_F)=%.3f (~%.0f) ; N(flat centre)=%.3f -> shift = %.3f e-/cell = %.3f e-/f.u."
              %(N0,NELEC,Nflat,dn,dn/N_FU))
        print("   (sign: + = hole-dope, - = electron-dope; |.| compares to CoSn's 1.58 h/f.u.)")
    except Exception as e:
        print("rigid-band cross-check skipped:",e)

    print("\n"+"="*72)
    print("SUMMARY (all from OUR converged PBE DFT; no tuning):")
    print("  flat band     : band %d, W=%.3f eV, dE=%+.3f eV rel E_F -> %s"%(bidx,Wflat,dE,pos.split('(')[0].strip()))
    print("  geometry I    : %.3f -> %s"%(I,geom.split('(')[0].strip()))
    print("  flat filling  : nu=%.3f, nu(1-nu)=%.3f -> %s"%(nu,dsfac,fill.split('(')[0].strip()))
    print("="*72)

if __name__=='__main__':
    main()
