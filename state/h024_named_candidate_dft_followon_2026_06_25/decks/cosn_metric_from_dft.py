#!/usr/bin/env python3
"""
H_024 task 2 (canonical, deterministic): CoSn kagome flat-band quantum geometry tr g
from OUR converged PBE DFT bands via a nearest-neighbour kagome tight-binding fit.

PROVENANCE of the TB parameters (no tuning):
  source bands : state/h019_named_candidate_dft_2026_06_25/out/cosn.bands.out
                 (OUR converged PBE QE7.2 scf+bands, 81-pt Gamma-M-K path, E_F=16.0015 eV)
  fit          : the kagome flat-band manifold is bands 37-42; the cleanest 3-band kagome
                 sub-group [39,40,41] spans 0.462 eV. For an ideal single-orbital NN kagome
                 the 3-band span = 6t and the flat band sits at the TOP (e0+2t).
                 -> t = 0.462/6 = 0.0770 eV ;  flat band (41) at -1.449 eV rel E_F
                 -> e0 = -1.449 - 2t = -1.603 eV rel E_F.
  (No wannier90.x is built on summer -> this TB-fit route is the named fallback. The
   absolute number carries the NN-only + Gamma-touching caveats; see card L3/L4.)

We compute the Fubini-Study quantum metric g_ab(k) = (1/2)Tr[dP dP], P=|u_flat><u_flat|,
by projector finite-difference on a 60x60 BZ grid, contract the crystal-coordinate metric
with the hexagonal reciprocal-metric inverse to get the PHYSICAL tr g(k), and report:
  - <tr g>_BZ (A^2),
  - I = (1/2pi) int_BZ tr g d2k   (the QGT-convention dimensionless metric integral, the
        Peotta-Tormae lower-bound lever; this is the number directly comparable to the
        MEASURED QGT trace g=2.87 of arXiv:2412.17809),
  - <tr g>/A_uc (an alternative per-cell normalisation).
Deterministic; numpy only.
"""
import numpy as np, math

A_LAT = 5.2693          # Angstrom (OUR scf alat = exp a)
E_F = 16.0015           # eV (OUR cosn.scf.out)
t   = 0.0770            # eV, fitted NN hopping (= 0.462/6, see provenance)
e0  = -1.603 + E_F      # on-site (abs eV); metric is E_F/e0-shift invariant
FLAT_MID = -1.449       # eV rel E_F (band 41), for reporting
W_DFT = 0.158           # eV, DFT flat-band width (band 41)

def Hk(k1, k2):
    p_ab = math.pi*k1; p_ac = math.pi*k2; p_bc = math.pi*(k2-k1)
    return np.array([[e0, -2*t*math.cos(p_ab), -2*t*math.cos(p_ac)],
                     [-2*t*math.cos(p_ab), e0, -2*t*math.cos(p_bc)],
                     [-2*t*math.cos(p_ac), -2*t*math.cos(p_bc), e0]], dtype=float)

def flat_index():
    es = []
    for i in range(12):
        for j in range(12):
            es.append(np.sort(np.linalg.eigvalsh(Hk(i/12, j/12))))
    es = np.array(es)
    return int(np.argmin(es.max(0) - es.min(0)))

def proj(k1, k2, fi):
    w, v = np.linalg.eigh(Hk(k1, k2)); o = np.argsort(w)
    u = v[:, o[fi]]; return np.outer(u, u.conj())

def main():
    fi = flat_index()
    print("="*70)
    print("H_024 task 2 — CoSn kagome flat-band quantum metric (NN TB fit to OUR DFT)")
    print("="*70)
    print(f"TB params (from OUR cosn.bands.out, NO tuning): t = {t:.4f} eV, e0 = {e0-E_F:+.3f} eV rel E_F")
    print(f"DFT flat band (band 41): W = {W_DFT:.3f} eV, mid = {FLAT_MID:+.3f} eV rel E_F")

    # band widths
    es = []
    for i in range(24):
        for j in range(24):
            es.append(np.sort(np.linalg.eigvalsh(Hk(i/24, j/24))))
    es = np.array(es); W = es.max(0) - es.min(0)
    print(f"TB band widths (eV): {np.round(W,4)} -> flat band ascending-index {fi}, W_TB={W[fi]*1000:.2f} meV")
    print(f"  (TB flat band is exactly flat; DFT W=158 meV is the real, smearing-broadened width)")

    B = 4*math.pi/(math.sqrt(3)*A_LAT)               # |b1|=|b2|, 1/A
    Gm = np.array([[B*B, -0.5*B*B], [-0.5*B*B, B*B]])  # reciprocal metric of (k1,k2)
    Ginv = np.linalg.inv(Gm)
    A_uc = math.sqrt(3)/2*A_LAT**2
    BZ = B*B*math.sqrt(3)/2

    N = 60; dk = 1.0/N; h = dk
    CAP = 200.0
    samp = []; samp_unc = []; ndiv = 0
    for i in range(N):
        for j in range(N):
            k1 = i*dk; k2 = j*dk
            dP1 = (proj(k1+h, k2, fi) - proj(k1-h, k2, fi))/(2*h)
            dP2 = (proj(k1, k2+h, fi) - proj(k1, k2-h, fi))/(2*h)
            g11 = 0.5*np.real(np.trace(dP1@dP1))
            g22 = 0.5*np.real(np.trace(dP2@dP2))
            g12 = 0.5*np.real(np.trace(dP1@dP2))
            trg = np.sum(Ginv*np.array([[g11, g12], [g12, g22]]))
            if not np.isfinite(trg):
                continue
            samp_unc.append(trg)
            if trg > CAP:
                ndiv += 1; trg = CAP
            samp.append(trg)
    samp = np.array(samp); samp_unc = np.array(samp_unc)
    avg = samp.mean()
    I = avg*BZ/(2*math.pi)
    print(f"\nGamma band-touching: {ndiv}/{N*N} grid pts capped at tr g={CAP} A^2 (integrable singularity, card L4)")
    print(f"<tr g>_BZ (physical)              = {avg:.4f} A^2   (uncapped {samp_unc.mean():.3f}, max {samp_unc.max():.0f})")
    print(f"A_uc = {A_uc:.3f} A^2 ; BZ area = {BZ:.4f} 1/A^2")
    print(f"\nI = (1/2pi) int_BZ tr g d2k     = {I:.4f}   <-- QGT-convention metric integral (the D_s lever)")
    print(f"<tr g>/A_uc                       = {avg/A_uc:.4f}   (alt per-cell normalisation)")
    print(f"\nMEASURED QGT (arXiv:2412.17809)   g = 2.87")
    print(f"verdict: OUR-DFT-fit metric integral I = {I:.3f} -> {'SUPPORTS g>=2' if I>=2 else 'BELOW g>=2'} "
          f"({'matches' if abs(I-2.87)<0.3 else 'differs from'} the measured QGT 2.87)")

if __name__ == '__main__':
    main()
