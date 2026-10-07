# Cone Derivation Ledger v14.125 — Octave Gram Projection Collapse to the Protected-Coupling Range

**Date:** 2026-10-07  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [D] exact Gram-projection decomposition of the reduced octave increment; [N] the 128k→256k source component orthogonal to the protected-coupling range is bounded at only 3.5e-11 per parity from current midpoint Gram data; [O] outward certification awaits interval bounds for (D,c,d).  
**Parents:** v14.124.  
**Collision check:** immediately before this write, live HEAD was `1d7af18ee36f4531c4f0f5cfe5ab8c0428e1f87f`; live ledger max was v14.124. No collision.

## 1. Joint octave Gram matrix

With the v14.124 notation,

[
D=F^*H^{-1}F,qquad
c=F^*H^{-1}r,qquad
d=r^*H^{-1}r.
]

Define

[
U=H^{-1/2}F,
qquad
y=H^{-1/2}r.
]

Then

[
D=U^*U,qquad
c=U^*y,qquad
d=y^*y.
]

Therefore

[
oxed{
egin{pmatrix}
D & c\
c^* & d
end{pmatrix}
=
egin{pmatrix}
U^*\
y^*
end{pmatrix}
egin{pmatrix}
U & y
end{pmatrix}
succeq0.
}
	ag{1}
]

This is an exact Gram identity.

## 2. Orthogonal-source remainder [D]

Let (P_U) be the orthogonal projector onto (operatorname{Ran}U). Decompose

[
y=y_{parallel}+y_{perp},
qquad
y_{parallel}=P_Uy.
]

The squared orthogonal residual is

[
oxed{
sigma_{perp}
=
|y_{perp}|^2
=
d-c^*D^+c,
}
	ag{2}
]

where (D^+) is the Moore–Penrose pseudoinverse.

Equation (1) implies (cinoperatorname{Ran}D) and

[
sigma_perpge0.
]

Since every nonzero eigenvalue of (D^+) is at least (1/lambda_{max}(D)),

[
c^*D^+c
ge
rac{|c|^2}{lambda_{max}(D)}.
]

Hence the eigenvector-free bound

[
oxed{
0le
sigma_perp
le
d-rac{|c|^2}{lambda_{max}(D)}.
}
	ag{3}
]

This uses only the scalar (d), the vector norm (|c|), and the top eigenvalue of the 6×6 matrix (D).

## 3. Exact split of the octave scalar increment [D]

From v14.124,

[
K_{2R}-K_R
=
q^*J^{-1}q,
]

with

[
J=H-FS^{-1}F^*.
]

In whitened coordinates,

[
J
=
H^{1/2}
left(
I-US^{-1}U^*
ight)
H^{1/2}.
]

The operator

[
I-US^{-1}U^*
]

acts as the identity on ((operatorname{Ran}U)^perp) and preserves (operatorname{Ran}U).

Therefore the octave increment splits exactly into

[
oxed{
K_{2R}-K_R
=
sigma_perp
+
Lambda_{parallel},
}
	ag{4}
]

where the entire nontrivial protected feedback is confined to

[
operatorname{Ran}U,
qquad
dimoperatorname{Ran}Ule6.
]

Thus the infinite-dimensional octave solve has collapsed to:

1. a scalar orthogonal remainder (sigma_perp);
2. a protected-coupling problem of dimension at most six.

No approximation has been made.

## 4. 128k→256k numerical size [N]

Using the v14.124 reduced Gram data:

### even-v

[
lambda_{max}(D_e)
=
3.508131738245032	imes10^{-8},
]

[
|c_e|_2
=
8.64347546182397	imes10^{-8},
]

[
d_e
=
2.1299635134644464	imes10^{-7}.
]

Equation (3) gives

[
oxed{
sigma_{perp,e}
le
3.494158899027083	imes10^{-11}.
}
]

Equivalently,

[
rac{|c_e|^2}{lambda_{max}(D_e)d_e}
=
0.9998359521711551.
]

### odd-v

[
lambda_{max}(D_o)
=
1.1156365003058613	imes10^{-6},
]

[
|c_o|_2
=
4.872849038862563	imes10^{-7},
]

[
d_o
=
2.1286989858560234	imes10^{-7}.
]

Equation (3) gives

[
oxed{
sigma_{perp,o}
le
3.482417710097993	imes10^{-11}.
}
]

and

[
rac{|c_o|^2}{lambda_{max}(D_o)d_o}
=
0.9998364062869745.
]

Hence the combined parity uncertainty coming from the source component orthogonal to the protected-coupling range satisfies, at midpoint scale,

[
oxed{
sigma_{perp,e}+sigma_{perp,o}
<
6.977	imes10^{-11}.
}
]

This is already almost two orders below the previous (5	imes10^{-9}) working scalar budget.

Guardrail: the displayed numerical bounds are diagnostic until (D,c,d) are outward-enclosed.

## 5. Consequence

The difficult part of the 128k→256k parity difference is not a 64k-dimensional octave inverse.

After the exact reduction, all load-bearing protected feedback lives in a subspace of dimension at most six.

Moreover the octave Gram matrix is numerically almost rank one, so the six-dimensional problem is itself strongly concentrated in one direction; that observation remains diagnostic and is not needed for the exact reduction (4).

The active certification target is now:

- one theorem-grade protected anchor (S,b);
- outward (D,c,d);
- high-precision evaluation of the at-most-six-dimensional parallel term;
- the scalar orthogonal remainder bounded by (3).

## 6. Verdict

[
oxed{
K_{2R}-K_R
=
sigma_perp+Lambda_parallel,
qquad
dimLambda_parallelle6.
}
]

For the current octave, the orthogonal source leakage is only (3.5	imes10^{-11})-class per parity.

---

HANDOFF
target: sandbox
type: octave-gram-projection-collapse
parent: v14.125
status: open
action: Independently verify equations (2)–(4), including the pseudoinverse formula and the invariant decomposition of the whitened resolvent. Then attack the remaining <=6-dimensional protected-coupling parity difference using v14.124's exact reduced transport. Do not assume the observed rank-one dominance as a theorem.
deliverable: theorem-or-correction
constraints: Preserve the exact Gram structure; no Cauchy-Schwarz collapse back to the full octave norm; no binary64 protected eigenvalue inference.
