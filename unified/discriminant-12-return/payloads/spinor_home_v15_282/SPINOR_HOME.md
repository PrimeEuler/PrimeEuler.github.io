# Spinors live only in the doublet channel

Producer: `spinor_home.py` / `spinor_home_output.txt`.

A full 2π rotation acts on a spin-j state as (−1)^{2j} (computed
j = 0…3): integer shells return +1 (tensors, residents of the
scalar even/odd channels of v15.277); half-integer shells return
−1. That −1 is the same sign as T² on the doublet (Kramers,
v15.278) — the spinor is the doublet channel's resident: it has
no scalar exchange parity itself, living on the double cover, in
the pair. The scalar channels see only its bilinears: density
ψ†ψ descends to the EVEN channel; the current ψ†σψ descends as
the ODD generators (verified on an explicit 2-spinor).

By the shell lock, half-integer j ⟺ odd diagonals and integer j
⟺ even diagonals, so: spinors reside only on the odd diagonals,
and even diagonals cannot host them (their exchange sign is +1
by the same computation). This retro-fits v15.140: the odd
sector's only resident form is a conjugate pair of one-ended
fragments — a doublet is exactly a conjugate pair; spinors were
never going to appear as closed chains.
