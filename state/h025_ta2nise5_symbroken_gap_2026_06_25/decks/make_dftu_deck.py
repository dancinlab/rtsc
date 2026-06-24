#!/usr/bin/env python3
# Rung 2 of the H_025 convergence ladder: DFT+U on Ni-3d applied to the MONOCLINIC
# C2/c cell. U on the correlated Ni-3d manifold opens/stabilizes the excitonic-like
# gap and regularizes the near-metallic SCF, cheaper than a hybrid.
#
# U choice: U(Ni-3d) = 3.0 eV — a standard mid-range value for Ni in chalcogenides
# (cf. linear-response U(Ni) ~ 3-4 eV in NiO/Ni-dichalcogenide literature; we use
# the cheap fixed-U DFT+U, NOT a self-consistent cRPA). Reported as a chosen value,
# honestly flagged. QE 7.2 new HUBBARD card syntax (ortho-atomic projectors).
#
# Reads the converged monoclinic deck tanise5.mono.in and emits tanise5.mono.u3.in.
import re

with open("tanise5.mono.in") as f:
    deck = f.read()

# bump electron_maxstep a bit and keep conv_thr; add starting_magnetization? keep nspin=1.
# Insert HUBBARD card at the very end (after K_POINTS block) — QE reads it as a card.
hubbard = "\nHUBBARD {ortho-atomic}\n  U Ni-3d 3.0\n"

deck_u = deck.replace("prefix = 'tanise5m'", "prefix = 'tanise5mu'")
deck_u = deck_u.replace("outdir = './out_mono'", "outdir = './out_mono_u'")
deck_u = deck_u.rstrip() + "\n" + hubbard

with open("tanise5.mono.u3.in", "w") as f:
    f.write(deck_u)
print("wrote tanise5.mono.u3.in (Ni-3d U=3.0 eV, ortho-atomic, monoclinic cell)")
