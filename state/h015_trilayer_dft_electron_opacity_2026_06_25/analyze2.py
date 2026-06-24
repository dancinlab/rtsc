#!/usr/bin/env python3
"""
H_015 — cleaner electron-opacity observable, robust to the E_F doping shift.

The raw D_pz(E_F) is contaminated because E_F drifts -1.93 -> +0.08 eV across n
(different self-doping of the slab). A fixed-E_F probe therefore mixes the opacity
signal with a moving sampling energy.

Two doping-robust interlayer-coupling proxies:

(P1) GRAPHENE-LAYER INTERLAYER SPLITTING = the bonding/antibonding split of the two
     graphene pz manifolds. We measure it as the energy SEPARATION between the bottom-
     and top-graphene pz PDOS-peak positions in a +/-2.5 eV window around E_F. When the
     layers couple strongly (n=0) the symmetric/antisymmetric combinations are split;
     when decoupled (large n) they coincide. (For a symmetric stack the two LAYERS are
     equivalent, so we instead use the split between the two pz peaks nearest E_F in the
     TOTAL graphene-pz PDOS — the bonding-antibonding doublet.)

(P2) INTERLAYER pz DOS TRANSFER ACROSS THE SPACER. The most direct, doping-free number:
     integrate the graphene pz PDOS that leaks INTO the hBN region is not directly
     available; instead we use the hBN B/N pz PDOS at E_F as the spacer's own metallicity
     induced by the metal layers — a spacer that is electron-opaque has ~0 induced DOS at
     E_F inside it. D_hBN_pz(E_F) -> 0 with n = opacity of the spacer interior.

(P3) The graphene pz PDOS evaluated at each system's own Dirac point E_D (the pz DOS
     LOCAL MINIMUM near E_F): for ISOLATED graphene this minimum is ~0; interlayer
     coupling FILLS IN the Dirac minimum. So D_pz(E_D) (the minimum value) measures
     residual interlayer coupling, doping-free.

We report P2 and P3 (both doping-robust) plus the raw P-at-EF for completeness.
"""
import glob, os, re, json

HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")

def parse_fermi(scf):
    ef=None
    for line in open(scf):
        if "the Fermi energy is" in line:
            m=re.search(r"Fermi energy is\s+([-\d.]+)",line)
            if m: ef=float(m.group(1))
    return ef

def read_pdos(path):
    E,L=[],[]
    for line in open(path):
        s=line.strip()
        if not s or s.startswith("#"): continue
        p=s.split()
        try: E.append(float(p[0])); L.append(float(p[1]))
        except: continue
    return E,L

def interp(E,L,e0):
    if not E: return 0.0
    if e0<=E[0]: return L[0]
    if e0>=E[-1]: return L[-1]
    for i in range(len(E)-1):
        if E[i]<=e0<=E[i+1]:
            t=(e0-E[i])/(E[i+1]-E[i]) if E[i+1]!=E[i] else 0
            return L[i]*(1-t)+L[i+1]*t
    return 0.0

def sum_pz(pre, atom_ids):
    """sum pz PDOS over given atoms -> (E grid from first file, summed L)."""
    Egrid=None; tot=None
    for a in atom_ids:
        for fp in glob.glob(os.path.join(HERE,f"{pre}.pdos_atm#{a}(*)_wfc#*(p)")):
            E,L=read_pdos(fp)
            # projwfc 'p' file: col1 = total p ldos; pz is col with index... use total p as proxy
            if Egrid is None:
                Egrid=E; tot=list(L)
            else:
                for i in range(min(len(tot),len(L))): tot[i]+=L[i]
    return Egrid, tot

def local_min_near(E,L,e0,win=2.5):
    """value of the local minimum of L within [e0-win, e0+win]."""
    vals=[(L[i],E[i]) for i in range(len(E)) if e0-win<=E[i]<=e0+win]
    if not vals: return None,None
    v,e=min(vals,key=lambda t:t[0])
    return round(v,5), round(e,4)

def analyze(n):
    pre=f"ghbn_n{n}"; nat=4+2*n
    ef=parse_fermi(os.path.join(HERE,f"{pre}.scf.out"))
    graphene=[1,2,nat-1,nat]
    hbn=list(range(3,3+2*n))  # empty for n=0
    res={"n":n,"E_fermi_eV":ef}

    Eg,Lg=sum_pz(pre,graphene)
    res["D_graphene_pz_at_Ef"]=round(interp(Eg,Lg,ef),5)
    vmin,emin=local_min_near(Eg,Lg,ef)
    res["graphene_pz_DiracMin_value"]=vmin
    res["graphene_pz_DiracMin_energy"]=emin

    if hbn:
        Eh,Lh=sum_pz(pre,hbn)
        res["D_hBN_pz_at_Ef"]=round(interp(Eh,Lh,ef),5)
        res["D_hBN_pz_per_atom_at_Ef"]=round(interp(Eh,Lh,ef)/len(hbn),5)
    else:
        res["D_hBN_pz_at_Ef"]=None
        res["D_hBN_pz_per_atom_at_Ef"]=None
    return res

if __name__=="__main__":
    out=[analyze(n) for n in (0,1,2,3)]
    with open(os.path.join(os.path.dirname(HERE),"result2.json"),"w") as f:
        json.dump(out,f,indent=2)
    print(json.dumps(out,indent=2))
    print("\n n | E_F(eV) | graphene_pz Dirac-min | (at E=) | hBN_pz(E_F)/atom")
    for r in out:
        print(f" {r['n']} | {r['E_fermi_eV']:>7} | {r['graphene_pz_DiracMin_value']:>20} | "
              f"{r['graphene_pz_DiracMin_energy']:>7} | {r['D_hBN_pz_per_atom_at_Ef']}")
