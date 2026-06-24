import numpy as np, re, sys
F="/home/summer/rtsc_cosn/scf.out"
txt=open(F).read()
EF=14.7132
NELEC=93.0

# parse k-weights (wk) -- 28 kpts, listed once (spin-independent weights)
wk=[float(m) for m in re.findall(r"wk =\s*([\d.]+)", txt)]
wk=wk[:28]
wk=np.array(wk)
# QE wk for nspin=2 sum to 2.0 (1 per spin channel); normalize so sum over kpts =1 for per-spin integration
# Actually QE: sum wk = 2.0 for nspin=2. We'll handle by using raw wk and the fact each (k,spin) eig carries weight wk/2? 
# Standard: occupation count N = sum_{k,spin,band} wk_k * f * (1) with sum_k wk =2 covering both spins via separate spin blocks each weighted wk... 
# QE convention nspin=2: wk printed sum to 2; each spin channel uses the SAME wk, and total electrons = sum_spin sum_k wk_k/?  
# Empirically QE: N = sum_{spin} sum_k sum_band wk_k*f_{k,spin,band} with sum_k wk =1 (per spin). Printed wk sum check:
print("sum wk printed =",wk.sum(), "(nspin=2 => expect ~2.0; per-spin weight = wk)")

# split spin up / down blocks
iu=txt.index("------ SPIN UP")
idn=txt.index("------ SPIN DOWN")
up=txt[iu:idn]
dn=txt[idn:]

def parse_eigs(block):
    # each k: "bands (ev):" then numeric lines until blank/next 'k ='
    eigs=[]
    chunks=re.split(r"k =.*?bands \(ev\):", block)[1:]
    for c in chunks:
        nums=[]
        for line in c.splitlines():
            t=line.strip()
            if t=="" : 
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

Eup=parse_eigs(up); Edn=parse_eigs(dn)
print("nk up,dn:",len(Eup),len(Edn),"nbnd:",len(Eup[0]),len(Edn[0]))

# normalize weights to per-spin sum=1
w = wk / wk.sum() * 1.0   # now sum=1 per spin channel
# Build occupation: gaussian smearing CDF
SIG=0.10  # eV smearing for occupation (rigid-band, indicative)
from math import erf
def occ(e, ef):
    # fraction occupied = 0.5*erfc((e-ef)/sig) ; use erf
    return 0.5*(1.0-erf((e-ef)/(SIG*np.sqrt(2))))
vocc=np.vectorize(occ)

Eup=np.array([np.array(x) for x in Eup])
Edn=np.array([np.array(x) for x in Edn])

def Ntot(ef):
    N=0.0
    for ik in range(len(Eup)):
        N+=w[ik]*np.sum(vocc(Eup[ik],ef))
        N+=w[ik]*np.sum(vocc(Edn[ik],ef))
    return N

# sanity: N at EF should be ~93
print("N(E_F=%.4f) = %.3f  (should be ~%.1f)"%(EF,Ntot(EF),NELEC))

def DOS(ef,dE=0.02):
    return (Ntot(ef+dE)-Ntot(ef-dE))/(2*dE)

print("\n# Rigid-band hole-doping sweep (BZ tetrahedron-grid weighted, gaussian sig=%.2f eV)"%SIG)
print("%-10s %-12s %-14s %-14s"%("E_F_target","N(E_F)","Delta_n(hole)","DOS(states/eV/cell)"))
N0=Ntot(EF)
flatrow=None
for ef in np.arange(14.71,14.19,-0.05):
    N=Ntot(ef); dn=N0-N; d=DOS(ef)
    print("%-10.2f %-12.4f %-14.4f %-14.3f"%(ef,N,dn,d))
print("\n# DOS at undoped E_F = %.3f states/eV/cell"%DOS(EF))
# flat band center band45 ~14.2697
for ctr in [14.2697,14.2477]:
    N=Ntot(ctr); dn=N0-N; d=DOS(ctr)
    print("# FLAT BAND target E_F=%.4f : hole-doping = %.4f e/cell ; N(E_F)=%.3f states/eV/cell (vs undoped %.3f, x%.2f)"%(ctr,dn,d,DOS(EF),d/DOS(EF)))
