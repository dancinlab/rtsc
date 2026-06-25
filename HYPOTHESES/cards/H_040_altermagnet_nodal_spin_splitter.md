# H_040 — NODAL-SPIN-SPLITTER GLUE: d-wave altermagnet pair vertex

- **id**: H_040
- **slug**: altermagnet-nodal-spin-splitter
- **escape_class**: (a) different glue root — spin-group-symmetry pairing claimed decoupled from Neel stiffness
- **cluster**: spin-group-symmetry pairing decoupled from Neel stiffness
- **status**: closed-negative (confirms-wall)
- **date**: 2026-06-25
- **is_green**: false
- **absorbed**: false
- **run**: `state/h_040_altermagnet-nodal-spin-splitter_2026_06_25/run.py` (stdlib-only, deterministic, byte-reproducible)

## Which of the freeze's 5 premises this violates

The frozen spin-fluctuation / phase-stiffness verdict (Emery-Kivelson; T_BKT=(pi/2)D_s,
~134-164 K ambient ceiling) was measured on **Q=0 / single-particle-flat / crystalline /
quasiparticle-coherent / equilibrium** hosts where the pairing root and the magnetic-
stiffness root are the **same root** (cuprate J and rho_s share one root). This card
attacks the **quasiparticle-coherent / shared-root** premise: it posits a spin-group-
symmetry band texture (altermagnet d-wave spin splitting) whose pairing vertex is claimed
to be sourced by the *static* anisotropic inter-sublattice hopping t_AM, decoupled from
the Neel moment ⟨S⟩ / stiffness rho_s. None of the wave-1 escapes (H_032 multiband /
H_033 z=2 Goldstone / H_034 eta / H_035 Amperean) touch the altermagnet / spin-group axis.

## Hypothesis (frozen pre-register)

A d-wave altermagnet has a momentum-dependent spin splitting `eps_pm(k) = -2t(cos kx +
cos ky) ± t_AM(cos kx - cos ky)` that flips sign under a C4 rotation (spin-group symmetry),
giving zero net moment but a static d-wave (B1g) band texture. The seed CLAIMS the spin-
fluctuation pairing eigenvalue `lambda_pair` on this split Fermi surface stays finite
(**> 0.3**) as the Neel stiffness `rho_s -> 0` at **FIXED t_AM**, because the splitting is
set by the crystal-field/hopping term, not by ⟨S⟩ — so pairing strength and magnetic
phase stiffness become **separate roots** (unlike Emery-Kivelson). A decoupled host could
then carry a strong glue AND a high charge superfluid stiffness, letting T_BKT clear 164 K.

## Why (mechanism + literature grounding)

The altermagnet SC literature is unambiguous that a spin-**FLUCTUATION**-mediated pairing
vertex is the standard RPA kernel `V ~ U·chi_RPA·U`, `chi_RPA = chi0/(1 - U·chi0)`, whose
leading attractive eigenvalue is governed by the **Stoner factor S = U·chi0 → 1** (the
magnetic instability) — it GROWS toward the instability and COLLAPSES away from it:

- **arXiv:2509.09959** ("Possible Spin Triplet Pairing due to Altermagnetic Spin
  Fluctuation"): pairing interaction ∝ `U^S·chi^S(q)·U^S`, chi^S RPA; lambda is computed
  only in `Uc1 ≤ U < Uc2` where fluctuations peak; strongest approaching magnetic ordering.
- **arXiv:2510.19083** ("Inter-orbital spin-triplet superconductivity from altermagnetic
  fluctuations"): fluctuation-mediated; proximity to the magnetic instability *enhances*
  pairing.
- **arXiv:2308.08606** ("Two-dimensional altermagnets: SC in a minimal model").

The "static-splitting sources the glue independent of ⟨S⟩" route the seed needs is NOT the
SF mechanism the freeze concerns — that would be a weak-coupling BCS instability of the bare
altermagnet bands (`lambda ~ U·N0`, room-T-cold, no enhanced glue). **Key identity:** the
mean-field AFM/altermagnetic stiffness scales `rho_s ~ (1 - S)` (massless paramagnon at the
instability). So the glue (S/(1-S)) and the stiffness (1-S) are **two readouts of the same
Stoner factor** — the shared root. The seed must break this; the SF kernel does not.

## The probe (closed-form / small-lattice, deterministic)

2-band altermagnet tight-binding at half-filling, L=24×24 k-grid (in-process, <1 s):
bare q=0 susceptibility chi0 (Lindhard/DOS proxy), d-wave form factor ⟨g⟩ on the split FS,
RPA pairing eigenvalue `lambda_pair = ⟨g⟩·(S/(1-S))/NORM`, Neel stiffness `rho_s = (1-S)`,
charge `D_s = 7.4 meV · min(1,lambda) · n_factor`, `T_BKT = (pi/2)D_s`. The rho_s SWEEP is
realized by moving S at **FIXED t_AM** (the seed's exact protocol). NORM=8 is a fixed
documented weak-coupling normalization — **not tuned to green** (a more generous NORM only
raises every lambda uniformly; it cannot make lambda decouple from rho_s, which is the
load-bearing test).

## Falsifiers (pre-registered; PASS = NOT triggered)

1. **F1_honest_null_disguised_magnon** (DECISIVE / the honest-null) — TRIGGERS when
   `lambda_pair` at a **stiff** Neel order (rho_s=0.5) is `≤ 0.3`, i.e. the vertex is NOT
   decoupled and only grows as the order softens → disguised magnon, re-confirming the
   carded magnon-family closure (H_033/H_034). **PASS only if pairing is genuinely finite
   while the Neel order is stiff.**
2. **F2_lambda_anticorrelates_with_rho_s** — TRIGGERS when corr(lambda_pair, rho_s) < −0.5
   across the sweep (lambda large only as rho_s→0 → same Stoner root).
3. **F3_no_escape_point** — TRIGGERS when no sweep point has lambda>0.3 AND rho_s>0.2
   (genuinely ordered, not at the QCP) AND charge T_BKT>164 K simultaneously.
4. **F4_tbkt_below_wall** — TRIGGERS when the best achievable charge T_BKT ≤ 164 K.
5. **F5_no_dwave_projection** — TRIGGERS when ⟨g⟩ ≤ 0.01 (degenerate model, result
   meaningless; guards against a trivial pass).

ESCAPE requires ALL five to PASS **including** the honest-null F1.

## Verbatim run verdict (no LLM self-judge)

```
chi0 (bare)            = 0.127169
d-wave form factor <g> = 0.277617
rho_s sweep at FIXED t_AM (Stoner S = U*chi0; rho_s ~ (1-S)):
      S    rho_s  lambda_pair   Ds(meV)  T_BKT(K)
   0.10   0.9000       0.0039    0.0445      0.81
   0.30   0.7000       0.0149    0.1717      3.13
   0.50   0.5000       0.0347    0.4007      7.30
   0.70   0.3000       0.0810    0.9350     17.04
   0.85   0.1500       0.1966    2.2707     41.39
   0.95   0.0500       0.6593    7.6135    138.78
   0.99   0.0100       3.4355   11.5472    210.49
lambda_pair at STIFF order (rho_s=0.5)  = 0.0347  (need >0.3 for decoupling)
corr(lambda_pair, rho_s)                = -0.5847  (<<0 => disguised magnon / shared root)
best charge T_BKT on sweep              = 210.49 K  (wall 134-164 K)
escape point (lam>0.3 & rho_s>0.2 & T_BKT>164K) exists = False
  [FAIL] F1_honest_null_disguised_magnon
  [FAIL] F2_lambda_anticorrelates_with_rho_s
  [FAIL] F3_no_escape_point
  [PASS] F4_tbkt_below_wall
  [PASS] F5_no_dwave_projection
honest_null (F1) PASS = False
falsifiers_pass = 2/5
VERDICT: confirms-wall
```

The honest-null F1 **FAILS**: lambda_pair at a stiff Neel order (rho_s=0.5) is 0.035, far
below the 0.3 decoupling threshold. lambda only clears 0.3 at S≥0.95 (rho_s≤0.05 — order
essentially gone). corr(lambda, rho_s) = −0.585. The pairing vertex tracks rho_s: it is a
disguised magnon, exactly the carded magnon-family closure. No genuinely-ordered escape
point exists (F3 fails). The two PASSes (F4/F5) are sanity gates, not an escape.

## Honest limits

1. **Scalar RPA proxy, not the full matrix kernel.** lambda_pair uses the canonical
   S/(1-S) RPA enhancement times a d-wave FS projection, not a diagonalized multi-orbital
   pairing matrix. The qualitative shared-root conclusion is robust (it follows from the
   chi_RPA pole structure that ALL SF kernels share), but the exact lambda magnitudes are
   proxy-level, not ab-initio.
2. **chi0 is a DOS/Lorentzian-broadened q=0 proxy**, not a full q-resolved Lindhard
   function; a peaked finite-Q nesting structure could shift the instability filling but
   not decouple lambda from S.
3. **NORM and t_AM are fixed model inputs.** A different t_AM rescales chi0/⟨g⟩ but does not
   change the rho_s~(1-S) vs lambda~S/(1-S) anti-correlation — the load-bearing physics is
   parameter-independent. Not swept exhaustively here.
4. **The charge-D_s ceiling (7.4 meV cap, n_factor=1) encodes the freeze's measured
   doped-Mott-scarcity root**, not an independently recomputed Kubo weight for the
   altermagnet. The decoupling failure (F1) is upstream of and independent of this cap, so
   the verdict does not rest on it; a high-n compensated-metal escape (n_factor≫1) is the
   SEPARATE H_041 zero-moment-stiffness-ladder lever, not this card.
5. **Mean-field rho_s ~ (1-S).** Beyond mean field the stiffness-vs-Stoner relation
   acquires corrections, but the sign (soft order at the instability) is universal; the
   correction cannot flip the anti-correlation that kills the decoupling claim.
6. **In-silico only.** No altermagnet is synthesized/measured here; absorbed=false. This is
   a computational closed-negative on the *decoupling mechanism*, a hand-off boundary, not
   a claim that altermagnets cannot superconduct (they can — at low Tc, coupled to ⟨S⟩).

## Verdict

**confirms-wall.** The d-wave altermagnet spin-fluctuation pairing vertex does NOT decouple
from the Neel stiffness: lambda_pair and rho_s are two readouts of the one Stoner factor
(lambda ~ S/(1-S), rho_s ~ 1-S), so the vertex only becomes strong as the magnetic order
softens — a disguised magnon, re-confirming the carded magnon-family closure. The frozen
~134-164 K phase-stiffness ceiling stands; a valuable closed-negative tightening the wall
toward a universal no-go on the spin-group-symmetry/decoupled-root escape axis. is_green=false,
absorbed=false.