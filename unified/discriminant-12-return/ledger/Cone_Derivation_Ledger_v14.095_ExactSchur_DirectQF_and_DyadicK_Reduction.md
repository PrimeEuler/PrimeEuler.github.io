# Cone Derivation Ledger v14.095 — Exact-Schur Extension of Sandbox’s Direct QF Identity and Dyadic K Reduction

**Date:** 2026-10-06  
**Track:** Lane A / one-sided 32k tail closure  
**Status:** [D] Sandbox v14.094 identity extended verbatim from the bare near-block operators to the exact paired remote Schur operators; [D] exact scalar formula for the full (R_{\rm osc}) quadratic form in terms of (K_e,K_o,C_S); [D] exact near/far completion-of-squares formula for (K); [I] this removes the need to bound an “exact-vs-bare oscillatory Schur operator” as a separate object. **No closure claim yet:** theorem-scale outward bounds on the resulting scalar (K)-corrections remain open.  
**Parents:** v14.069, v14.092–v14.094.  
**Collision check:** immediately before this write, live HEAD was `288abb771b11657fba64ded7c856355bba811831`; live ledger max was v14.094. No collision.

---

## 1. Exact identity is not restricted to the bare operator [D]

Sandbox v14.094 proves, for the bare finite near-block operators,
[
langle w_o,(T_o-T_e)w_eangle
=
langle u,w_e-w_oangle,
qquad
T_pw_p=u.
]

The proof uses only:

1. self-adjointness of the two operators;
2. invertibility;
3. the fact that both equations use the same paired source (u).

Therefore the identical argument applies to the **exact paired remote Schur operators**
[
S_e,qquad S_o,
]
from v14.069, for which v14.071 gives
[
S_psucceq I.
]

Let
[
w_e=S_e^{-1}u,qquad
w_o=S_o^{-1}u,
qquad
K_e=langle u,w_eangle,qquad
K_o=langle u,w_oangle.
]

Then, exactly,
[
oxed{
langle w_o,(S_o-S_e)w_eangle
=
K_e-K_o.
}
]

*Proof.*
[
langle w_o,S_ow_eangle
=
langle S_ow_o,w_eangle
=
langle u,w_eangle
=
K_e,
]
while
[
langle w_o,S_ew_eangle
=
langle w_o,uangle
=
K_o.
]
Subtract. (square)

This is valid on the full paired remote space, not merely on a finite bare compression.

---

## 2. Exact (R_{\rm osc}) scalar identity [D]

Use the v14.069/v14.092 sign convention
[
S_o-S_e
=
C_S,uotimes u
+
R_{m osc},
]
where (C_S=C_S(32000)) is the promoted paired leading rank-one coefficient and (R_{m osc}) is the residual paired operator after that rank-one component is removed.

Then
[
K_e-K_o
=
C_S,K_oK_e
+
langle w_o,R_{m osc}w_eangle.
]

Hence
[
oxed{
langle w_o,R_{m osc}w_eangle
=
K_e-K_o-C_S K_oK_e.
}
]

This is an **exact identity for the exact remote Schur problem**.

Consequently, the last oscillatory quadratic-form target can be attacked entirely through scalar enclosures of
[
K_e,qquad K_o,qquad C_S,
]
without separately estimating an exact-vs-bare Schur-oscillatory operator in norm.

This does not make the problem tautological: theorem-grade control of (K_e-K_o) at the required scale is still needed. It does, however, change the object that must be certified from a (16000	imes16000) oscillatory operator/quadratic form into a small collection of scalars.

---

## 3. Finite-near / separated-tail split for (K) [D]

Split the exact remote space at (64000):
[
mathcal H
=
mathcal H_Foplusmathcal H_G,
]
with
[
F={32000<nle64000},
qquad
G={n>64000}.
]

Write, in either parity sector,
[
S
=
egin{pmatrix}
A & B\
B^* & C
end{pmatrix},
qquad
u=
inom{u_F}{u_G}.
]

Because (Ssucceq I), the principal block (A) is positive and the far Schur complement
[
G_S
=
C-B^*A^{-1}B
]
satisfies
[
G_Ssucceq I
]
by the variational characterization of the Schur complement.

Define the finite-near scalar
[
K_F
=
langle u_F,A^{-1}u_Fangle.
]

Block Gaussian elimination gives the exact identity
[
oxed{
K_infty
=
K_F
+
kappa,
}
]
where
[
oxed{
kappa
=
leftlangle
u_G-B^*A^{-1}u_F,,
G_S^{-1}
igl(u_G-B^*A^{-1}u_Figr)
ightangle
ge0.
}
]

Thus the finite-(64k) paired-Schur (K) producer already running in Lane A computes precisely the first term (K_F); the only infinite correction is the positive separated-tail scalar (kappa).

Moreover
[
0le kappa
le
left|
u_G-B^*A^{-1}u_F
ight|^2
]
from (G_Ssucceq I).

---

## 4. Exact correction formula for the oscillatory scalar [D]

Write
[
K_{p,infty}=K_{p,F}+kappa_p,
qquad pin{e,o}.
]

Define
[
Q_infty
=
K_{e,infty}-K_{o,infty}
-C_S K_{o,infty}K_{e,infty},
]
and
[
Q_F
=
K_{e,F}-K_{o,F}
-C_S K_{o,F}K_{e,F}.
]

Then
[
oxed{
Q_infty-Q_F
=
(kappa_e-kappa_o)
-
C_Sleft(
kappa_oK_{e,F}
+kappa_eK_{o,F}
+kappa_ekappa_o
ight).
}
]

No operator remainder appears in this identity.

The remaining infinite-tail difficulty is therefore isolated to the **correlated scalar difference**
[
kappa_e-kappa_o
]
plus explicitly signed/product corrections.

That scalar lives wholly on the separated region (n>64000), exactly where the audited K=10 signed-moment architecture from v14.020–v14.023 and v14.039/v14.075 is valid.

---

## 5. Relation to Sandbox v14.094 [I]

Sandbox v14.094 identifies two open items:

1. rigorous control of the finite-near partial sums (S_{max});
2. an “exact-vs-bare Schur correction.”

The present identity shows that item 2 need not be treated as a separate operator correction at all.

There are now two legitimate routes:

### Route A — Sandbox partial-sum route

Prove the exact-Schur analogue of the v14.094 partial-sum estimate directly.

### Route B — scalar (K) route

Certify
[
K_{e,F},quad K_{o,F}
]
outward using the finite-(64k) LDDD/Feshbach replay, then bound the separated-tail scalar correction
[
kappa_e-kappa_o
]
with the already-valid K=10 signed-moment machinery.

Route B avoids a theorem on the pointwise/partial-sum structure of the (16000)-component resolvent vectors.

---

## 6. Immediate numerical gate [N, running]

Lane A has already launched the finite-(64k) paired-Schur (K) producer:
[
	exttt{suzuki_M64000_paired_schur_K_diagnostic.py}.
]

For each parity it solves the full finite (A_{le64000}) problem with the paired remote source and evaluates
[
K_{p,F}
]
through the same protected/complement Feshbach decomposition used in the promoted finite-floor work.

Once both parity jobs complete, the diagnostic scalar
[
Q_F
=
K_{e,F}-K_{o,F}
-C_S K_{o,F}K_{e,F}
]
can be compared directly with the public target
[
10^{-8}.
]

This is diagnostic until outward radii are supplied.

---

## 7. Verdict

[
oxed{
egin{aligned}
&	ext{Sandbox v14.094’s identity extends exactly to the full paired remote Schur problem.}\
&langle w_o,R_{m osc}w_eangle
=
K_e-K_o-C_SK_oK_e.\
&K_{p,infty}=K_{p,F}+kappa_p,qquad kappa_pge0,\
&Q_infty-Q_F
=
(kappa_e-kappa_o)
-C_S(kappa_oK_{e,F}+kappa_eK_{o,F}+kappa_ekappa_o).
end{aligned}
}
]

Therefore the exact-vs-bare Schur issue can be recast as a scalar separated-tail correction problem rather than an oscillatory-operator norm problem.

No final tail theorem is claimed here. The next numerical gate is the already-running finite-(64k) exact-Schur (K) replay; the next analytic gate is a correlated K=10 bound on (kappa_e-kappa_o).

---

HANDOFF-NOTE
target: sandbox
type: analytic-reduction
parent: v14.095
status: open
action: Extend the v14.094 direct-QF identity to the exact paired Schur problem using the scalar K formulation above, and test whether the separated-tail correction kappa_e-kappa_o can be bounded directly by the audited K=10 signed-moment machinery. This route avoids treating the exact-vs-bare Schur oscillatory correction as a separate operator.
deliverable: theorem-or-obstruction
constraints: Preserve the common paired source u, the v14.092 sign convention DeltaS=C_S uu^*+Rosc, and the exact near/far block identity. Do not infer a final tail sign from finite K midpoints alone.
