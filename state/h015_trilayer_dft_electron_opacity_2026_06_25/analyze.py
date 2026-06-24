#!/usr/bin/env python3
"""
H_015 — extract the electron-opacity observable vs n from pw.x + projwfc output.

Electron-opacity proxy (primary): the INTERLAYER ELECTRONIC COUPLING between the two
graphene layers, measured as the graphene C-2pz projected DOS at the Fermi level,
D_pz^graphene(E_F).

Physics: two graphene layers in DIRECT CONTACT (n=0) hybridize — their Dirac pz manifolds
overlap and the bonding/antibonding interlayer splitting puts finite pz spectral weight at
E_F (and breaks the isolated-graphene Dirac-point pinning). Inserting wide-gap hBN spacers
(n=1,2,3) suppresses interlayer wavefunction overlap, decoupling the layers so each recovers
isolated-graphene character (pz DOS at E_F -> the small isolated-monolayer value). A
MONOTONIC DECAY of D_pz^graphene(E_F) with n is the electron-opacity signature.

Secondary observables:
  - total PDOS at E_F (whole-cell metallicity).
  - per-atom Lowdin charge on graphene C (charge sharing across the junction).

The atom ordering (from build_decks.py): for n hBN layers,
  atoms 1,2          = bottom graphene C
  atoms 3 .. 2+2n    = hBN (B,N) — absent for n=0
  atoms (nat-1),nat  = top graphene C
stdlib only.
"""
import glob, os, re, json

HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")

def parse_fermi(scf):
    ef = None
    with open(scf) as f:
        for line in f:
            if "the Fermi energy is" in line:
                m = re.search(r"Fermi energy is\s+([-\d.]+)", line)
                if m: ef = float(m.group(1))
    return ef

def parse_lowdin(proj):
    """One total charge per atom (take the 's =' line, which carries the total)."""
    charges = {}
    with open(proj) as f:
        for line in f:
            m = re.search(r"Atom #\s*(\d+):\s*total charge =\s*([\d.]+),\s*s =", line)
            if m:
                charges[int(m.group(1))] = float(m.group(2))
    return [charges[k] for k in sorted(charges)]

def read_pdos(path):
    E, L = [], []
    with open(path) as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith("#"): continue
            p = s.split()
            try:
                E.append(float(p[0])); L.append(float(p[1]))
            except (ValueError, IndexError):
                continue
    return E, L

def interp(E, L, e0):
    if not E: return 0.0
    if e0 <= E[0]: return L[0]
    if e0 >= E[-1]: return L[-1]
    for i in range(len(E)-1):
        if E[i] <= e0 <= E[i+1]:
            if E[i+1]==E[i]: return L[i]
            t=(e0-E[i])/(E[i+1]-E[i])
            return L[i]*(1-t)+L[i+1]*t
    return 0.0

def analyze_n(n):
    pre = f"ghbn_n{n}"
    scf  = os.path.join(HERE, f"{pre}.scf.out")
    proj = os.path.join(HERE, f"{pre}.proj.out")
    nat = 4 + 2*n
    ef = parse_fermi(scf)
    low = parse_lowdin(proj) if os.path.exists(proj) else []
    res = {"n": n, "nat": nat, "E_fermi_eV": ef, "lowdin_total_charge": low}

    graphene_atoms = [1, 2, nat-1, nat]
    # graphene pz PDOS at E_F
    d_pz = 0.0
    for a in graphene_atoms:
        for fp in glob.glob(os.path.join(HERE, f"{pre}.pdos_atm#{a}(*)_wfc#*(p)")):
            E, L = read_pdos(fp)
            if ef is not None:
                d_pz += interp(E, L, ef)
    res["D_graphene_pz_at_Ef"] = round(d_pz, 5)

    # total cell PDOS at E_F
    tp = os.path.join(HERE, f"{pre}.pdos_tot")
    if os.path.exists(tp) and ef is not None:
        E, L = read_pdos(tp)
        res["D_total_at_Ef"] = round(interp(E, L, ef), 5)

    if len(low) == nat:
        res["q_graphene_avg"] = round(sum(low[i] for i in [0,1,nat-2,nat-1])/4.0, 4)
    return res

if __name__ == "__main__":
    out = [analyze_n(n) for n in (0,1,2,3)]
    # opacity ratio relative to direct contact (n=0)
    d0 = out[0]["D_graphene_pz_at_Ef"]
    for r in out:
        r["coupling_ratio_vs_n0"] = round(r["D_graphene_pz_at_Ef"]/d0, 4) if d0 else None
    with open(os.path.join(os.path.dirname(HERE), "result.json"), "w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out, indent=2))
    print("\n n | nlayers | E_F (eV) | D_graphene_pz(E_F) | D_total(E_F) | coupling_ratio")
    for r in out:
        print(f" {r['n']} |   {2 if r['n']==0 else 2+r['n']}+G  | {r['E_fermi_eV']:>8} | "
              f"{r['D_graphene_pz_at_Ef']:>17} | {r.get('D_total_at_Ef','?'):>11} | "
              f"{r['coupling_ratio_vs_n0']}")
