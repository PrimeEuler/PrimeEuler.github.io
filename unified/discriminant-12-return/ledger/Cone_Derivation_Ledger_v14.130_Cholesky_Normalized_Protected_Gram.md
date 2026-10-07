# Cone Derivation Ledger v14.130 — Cholesky-Normalized Protected Gram Formula (No S−D Subtraction)

**Date:** 2026-10-07  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [D] Exact factor-preserving formula for the protected reduced-octave term; removes the numerically dangerous subtraction/inversion of the near-singular matrix (S-D). [O] Numerical evaluation awaits the exported LDDD protected anchor.  
**Parents:** v14.124–v14.129.  
**Collision check:** immediately before this write, live HEAD was `5e7d39b9469c065e04211df88c689a67ff41984a`; live ledger max was v14.129. No collision.

---

## 1. Starting point

From v14.124/v14.125,

[
D=U^*U,qquad
c=U^*y,qquad
d=y^*y,
]

with

[
U=H^{-1/2}F,
qquad
y=H^{-1/2}r.
]

Let

[
a=S^{-1}b.
]

Let

[
v=D^+c,
]

so that

[
P_{operatorname{Ran}U}y=Uv.
]

The whitened protected-range source is therefore

[
q_parallel^{m wh}
=
U(v-a).
]

The exact reduced octave operator in whitened coordinates is

[
B
=
I-US^{-1}U^*.
]

Hence

[
Lambda_parallel
=
langle
U(v-a),
B^{-1}U(v-a)
angle.
]

---

## 2. Normalize by the certified protected anchor

Take a high-precision Cholesky factorization

[
S=LL^*.
]

Define

[
A:=UL^{-*},
]

so that

[
AA^*
=
US^{-1}U^*,
]

and

[
G:=A^*A
=
L^{-1}DL^{-*}.
]

Because the reduced block is positive,

[
0preceq Gprec I.
]

Also define

[
u:=L^*(v-a).
]

Then

[
U(v-a)=Au.
]

Therefore

[
Lambda_parallel
=
u^*
A^*(I-AA^*)^{-1}A
u.
]

Using the exact identity

[
A^*(I-AA^*)^{-1}A
=
G(I-G)^{-1},
]

we obtain

[
oxed{
Lambda_parallel
=
u^*G(I-G)^{-1}u.
}
	ag{1}
]

No approximation has been made.

---

## 3. Why this is numerically preferable

The v14.124 equivalent formula contains

[
t^*(S-D)^{-1}t.
]

At large cutoffs, (S) has protected eigenvalues far below binary64 scale, so directly forming

[
S-D
]

causes the precision-wall behavior documented in v14.122/v14.127.

Equation (1) never forms (S-D).

Instead it uses:

1. one high-precision Cholesky factor of the already-certified anchor (S);
2. the positive Gram matrix (D);
3. the pseudoinverse projection coefficient (v=D^+c);
4. the normalized contraction (G), whose exact spectrum lies in ([0,1)).

Thus all load-bearing algebra preserves positivity and Gram structure.

---

## 4. Orthogonal + protected exact split

Combining v14.125 with (1),

[
oxed{
K_{2R}-K_R
=
sigma_perp
+
u^*G(I-G)^{-1}u.
}
	ag{2}
]

The first term is already covered by the v14.128 stressed outward budgets.

The entire remaining finite-octave theorem problem is therefore the parity difference of two at-most-six-dimensional quantities

[
DeltaLambda_parallel
=
u_o^*G_o(I-G_o)^{-1}u_o
-
u_e^*G_e(I-G_e)^{-1}u_e.
]

---

## 5. Certification route

Once the LDDD anchor payload

[
S_{64k}, b_{64k}, h_{64k}, S_{64k}^{-1}b_{64k}
]

lands:

1. factor (S_{64k}=LL^*) in multiprecision;
2. consume the outward Gram payload ((D,c,d));
3. compute (G=L^{-1}DL^{-*}) without subtracting protected matrices;
4. compute (v=D^+c) and (u=L^*(v-a));
5. evaluate (1) in multiprecision;
6. transport the anchor to the next octave using the exact reduced identities;
7. repeat for 128k→256k.

The Gram-radii certification from v14.128/v14.129 should be propagated in this normalized representation rather than as a raw interval on (S-D).

---

## 6. Verdict

[
oxed{
Lambda_parallel
=
u^*G(I-G)^{-1}u,
qquad
G=L^{-1}DL^{-*},
quad
0preceq Gprec I.
}
]

This is the preferred protected-sector consumer formula.

---

HANDOFF
target: sandbox
type: normalized-protected-gram
parent: v14.130
status: open
action: Independently verify equation (1) and analyze the parity difference in the normalized variables (G,u). Look for a direct paired bound on Delta Lambda_parallel that preserves the common mode. Do not revert to a norm bound on the full octave and do not form S-D in binary64.
deliverable: theorem-or-correction
constraints: Preserve Cholesky/Gram positivity; use the high-precision protected anchor only; no finite-cutoff stabilization inference.
