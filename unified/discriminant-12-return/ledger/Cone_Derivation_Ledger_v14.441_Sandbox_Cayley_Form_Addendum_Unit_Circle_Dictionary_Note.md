# Cone Derivation Ledger — v14.441

## Sandbox Deposit: Cayley-Form Addendum (§8) to the Unit-Circle Dictionary Note

**Track:** sandbox ("our Lane B" — the exploratory track; not the
ledger's Lane B). **Authorization:** Jeremy, 2026-10-15, in the main
chat: the Cayley repackaging was proposed by Jeremy and the addendum
approved in the same message ("worth a short addendum to the
dictionary note if you want it in the record — yes").

**Object amended:** `research-notes/Unit_Circle_Encoding_and_Hyperbolic_Cone_Form.md`
(the v14.366–v14.368 note), §8 appended. New note SHA-256
`68940c78678694c4befb6a20bb87289239d3fb00a65d0d5cdee505462e8935d9`
(10,325 bytes; commit `3c9632d3138737ef31a94aaf4392633f744e8090`;
fetch-back byte-verified). No paper edited.

## Content of the addendum [D throughout, except the final reading marked [I]]

Jeremy's readings of the components:

- Re z_n = 1 − 2/(n+1).
- Im z_n = √n / ((n+1)/2) = GM/AM.

The point as a Cayley transform (verified symbolically in-session,
sympy: both differences from the §1/§6 forms simplify to 0):

- z_n = (√n + i)/(√n − i);
- z_{n,k} = (√n + i√k)/(√n − i√k) = (1 + i e^{−ψ_{n,k}})/(1 − i e^{−ψ_{n,k}}).

Consequences recorded:

- |z_{n,k}| = 1 manifest (a number over its conjugate);
- z_{n,k} is the square of the normalized (√n, √k) direction;
  φ_{n,k} = 2 arctan √(k/n); inverse Cayley gives
  (1 + z_{n,k})/(1 − z_{n,k}) = i√(n/k) = i e^{ψ_{n,k}},
  i.e. cot(φ_{n,k}/2) = e^{ψ_{n,k}}; chains multiply the real Cayley
  arguments (= rapidities add); φ = π/2 − gd ψ is the Cayley angle
  law (the transposed Gudermannian of the v14.414 literature scan).
- The full pair ratio: (n+k)/(n−k) = coth ψ_{n,k} = 1/Re z_{n,k}
  = sec φ_{n,k} = |w|²/Re(w²), w = √n + i√k — no separate point;
  in Cayley language it is the real transform (1+x)/(1−x) at
  x = k/n where z_{n,k} is the imaginary transform at √x [I for
  the "one ratio, two readings" gloss].

## Scope

Presentation-layer identity for the existing encoding; no new
numerical claim, no change to §§1–7, no paper action. The note's
status is unchanged (Jeremy's later call on any paper use).
