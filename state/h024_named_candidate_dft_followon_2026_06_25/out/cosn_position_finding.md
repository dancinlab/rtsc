# CoSn flat-band position: REAL (orbital-selection), NOT a PBE artifact — H_024 task 2

## Question (H_019 F2 FAIL follow-up)
Our PBE puts the narrowest CoSn kagome flat band (band 41, W=0.158 eV) at ~1.45 eV BELOW E_F,
DEEPER than the cited ~0.2 eV (Liu/Kang arXiv:2001.11738). Is that deep position a PBE
correlated-flat-band failure, or real?

## Finding: REAL — multiple orbital flat bands, our path picked the deeper in-plane-d manifold
Kang et al., "Topological flat bands in frustrated kagome lattice CoSn", Nat. Commun. 11, 4004
(2020) [arXiv:2001.11738], ARPES + DFT-PBE+SOC:
- CoSn hosts SEVERAL kagome-derived flat bands from DIFFERENT Co 3d orbitals. The
  **d_xz/d_yz-derived** flat band sits near E_F (~0.2 eV below), with an 80 meV SOC gap at the
  quadratic touching point. The **in-plane d (d_xy/d_x2-y2)** kagome flat bands sit DEEPER
  (~ -1 to -2 eV).
- Crucially, the DFT Fermi level needed only a **~140 meV** downward shift to fit the experimental
  bands (attributed to slight Sn off-stoichiometry) — i.e. PBE places the bands ACCURATELY; it is
  NOT a large correlated mis-placement.

Our 81-point Γ-M-K path + min-width selection picked the FLATTEST band, which is the deeper
in-plane-d manifold (W=0.158 eV at -1.45 eV), not the shallower d_xz/d_yz band near E_F. Both
exist. So:
- The deep position is **REAL** (orbital-selection of the extraction, confirmed by ARPES), NOT a
  PBE artifact. PBE is faithful here (140 meV off ARPES, no correlated collapse).
- The geometry lever (∫tr g, I=2.86) is a property of the kagome destructive-interference geometry
  and survives regardless of WHICH orbital flat band — so g≥2 holds (matches measured QGT 2.87).

## Consequence (unchanged, honestly logged)
Reaching a flat band AT E_F still needs doping/gating — but the NEAR-E_F d_xz/d_yz flat band
(~0.2 eV) is the realistic target for that, and it carries the same kagome geometry. The H_019 F2
"position" FAIL is an artifact of WHICH flat band our sparse-path min-width selection captured, not
a failure of PBE nor of the geometry lever. The trio stays 🟠; absorbed=false.

Sources:
- Kang et al., Nat. Commun. 11, 4004 (2020), arXiv:2001.11738 (https://www.nature.com/articles/s41467-020-17465-1)
- QGT measurement: Kang et al., arXiv:2412.17809 (g=2.87)
