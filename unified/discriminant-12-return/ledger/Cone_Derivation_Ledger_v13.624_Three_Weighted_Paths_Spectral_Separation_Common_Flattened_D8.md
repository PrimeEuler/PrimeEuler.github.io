# Cone Derivation Ledger v13.624 — Three Weighted Paths: Spectral Separation and Common Flattened D8 Carrier

Date: 2026-09-21

Status labels: [D] exact derived, [Audit] checked against prior exact low-spin results, [G] structural theorem, [Guardrail] scope restriction.

## 0. Mandatory collision / relevance check

Immediately before this write the live ledger was re-fetched. The current tip is v13.623, so v13.624 is free.

Relevant intervening entries are v13.620-v13.623: chi_-4 carrier/Galerkin work and magnetic-driver endpoint certification. None contains the three-path spectral comparison or flattened-carrier theorem below. v13.618 remains the direct predecessor for the Racah/volume path relation.

This entry records both halves of the result:
1. the raw weighted-path operators are generically spectrally inequivalent, so no invertible physical-operator intertwiner exists;
2. after orientation flattening, all three carry the same real D8 representation.

---

## 1. [D] The three finite weighted paths

Let

[
N=2j+1.
]

### SU(2) / magnetic ladder path

Relabel the J_z chain by (r=0,ldots,2j) and define

[
Y_r=sqrt{(2j-r)(r+1)}.
]

The zero-diagonal symmetric path is

[
L_Y=
egin{pmatrix}
0&Y_0&&\\
Y_0&0&Y_1&\\
&ddots&ddots&ddots\\
&&Y_{2j-1}&0
end{pmatrix}.
]

Exactly,

[
oxed{L_Y=2J_x.}
]

### Crossed-Casimir Racah path

From v13.618,

[
c_k=
rac{k[(2j+1)^2-k^2]}
{2sqrt{4k^2-1}},
qquad k=1,ldots,2j.
]

Define the zero-diagonal symmetric path

[
L_c=
egin{pmatrix}
0&c_1&&\\
c_1&0&c_2&\\
&ddots&ddots&ddots\\
&&c_{2j}&0
end{pmatrix}.
]

This is the off-diagonal path part of (K_{23}^2), not the full crossed Casimir; the full operator also has diagonal
[
d_k=2j(j+1)-rac{k(k+1)}2.
]

### Tetrahedral oriented-volume path

From v13.618,

[
a_k=rac{k}{2}c_k
=
rac{k^2[(2j+1)^2-k^2]}
{4sqrt{4k^2-1}}.
]

The Hermitian volume operator is

[
Q_a=
i
egin{pmatrix}
0&-a_1&&\\
a_1&0&-a_2&\\
&ddots&ddots&ddots\\
&&a_{2j}&0
end{pmatrix}.
]

All interior edge weights are strictly positive.

---

## 2. [D] Common bipartite invariants

Let

[
H=operatorname{diag}(1,-1,1,-1,ldots).
]

For each path,

[
oxed{HAH=-A.}
]

Hence every spectrum is symmetric under (lambdamapsto-lambda), and

[
oxed{operatorname{tr}A=0.}
]

Because every edge is nonzero, each is a connected bipartite path. Therefore

[
oxed{
dimker A=
egin{cases}
1,&jinmathbb Z,\\
0,&jinmathbb Z+rac12.
end{cases}}
]

For integer j the unique kernel vector lies in the H=+1 parity sector.

These shared invariants follow from path bipartiteness and do not imply operator similarity.

---

## 3. [D] Exact SU(2) path spectrum

Since (L_Y=2J_x) and (J_x) is unitarily equivalent to (J_z),

[
oxed{
operatorname{spec}L_Y=
{-2j,-2j+2,ldots,2j-2,2j}.
}
]

Thus

[
oxed{
operatorname{tr}L_Y^2
=
rac43j(j+1)(2j+1).
}
]

For integer j,

[
oxed{det L_Y=0.}
]

For (j=n+rac12),

[
oxed{
det L_Y=(-1)^{n+1}[(2n+1)!!]^2.
}
]

---

## 4. [D] General determinant formula for a weighted path

For an even-dimensional zero-diagonal path (A) of dimension (2m), with edge weights (w_1,ldots,w_{2m-1}),

[
oxed{
det A=(-1)^m(w_1w_3cdots w_{2m-1})^2.
}
]

For odd dimension,

[
oxed{det A=0.}
]

Also, for every Hermitian zero-diagonal weighted path,

[
oxed{operatorname{tr}A^2=2sum_k w_k^2.}
]

These invariants already separate the three raw operators.

---

## 5. [D][Audit] Low-spin exact separation

### j=1/2

[
operatorname{spec}L_Y={-1,+1},
]

[
operatorname{spec}L_c=
left{-rac{sqrt3}{2},+rac{sqrt3}{2}ight},
]

[
operatorname{spec}Q_a=
left{-rac{sqrt3}{4},+rac{sqrt3}{4}ight}.
]

All three are scalar multiples in dimension two. This is the one-edge accident.

### j=1

[
operatorname{spec}L_Y={-2,0,+2},
]

[
operatorname{spec}L_c={-sqrt7,0,+sqrt7},
]

[
operatorname{spec}Q_a={-sqrt3,0,+sqrt3}.
]

Any connected three-vertex zero-diagonal path has spectrum
[
{0,pmsqrt{w_1^2+w_2^2}},
]
so the three are still spectrally equivalent after individual scalar normalization. This is another low-dimensional accident.

### j=3/2: first genuine separation

[
operatorname{spec}L_Y={-3,-1,+1,+3}.
]

For the Racah path,

[
oxed{
chi_c(lambda)
=
lambda^4-rac{63}{2}lambda^2+rac{945}{16}.
}
]

For the volume path,

[
oxed{
chi_a(lambda)
=
left(lambda^2-rac{315}{16}ight)
left(lambda^2-rac{27}{16}ight).
}
]

Hence

[
operatorname{spec}Q_a=
left{
pmrac{3sqrt3}{4},
pmrac{3sqrt{35}}4
ight}.
]

The positive-magnitude ratio for (L_Y) is 3, whereas for (Q_a) it is

[
sqrt{rac{35}{3}},
]

so even scalar-rescaled similarity fails. The Racah polynomial gives a third scale-free spectral ratio.

Thus from j=3/2 onward there is no generic scalar normalization that makes the raw paths similar.

---

## 6. [D] Determinant and moment checks

Representative exact determinants:

At j=1/2,

[
det L_Y=-1,qquad
det L_c=-rac34,qquad
det Q_a=-rac3{16}.
]

At j=3/2,

[
oxed{
det L_Y=9,qquad
det L_c=rac{945}{16},qquad
det Q_a=rac{8505}{256}.
}
]

At j=5/2,

[
oxed{
det L_Y=-225,
}
]

[
oxed{
det L_c=-rac{2338875}{64},
}
]

[
oxed{
det Q_a=-rac{526246875}{4096}.
}
]

At j=2 there is an instructive second-moment coincidence:

[
operatorname{tr}L_c^2
=
operatorname{tr}Q_a^2
=
198.
]

But the characteristic polynomials separate them:

[
oxed{
chi_c(lambda)=
lambda(lambda^4-99lambda^2+1188),
}
]

whereas

[
oxed{
chi_a(lambda)=
lambda(lambda^4-99lambda^2+1296).
}
]

So the equal second moment is not an intertwiner signal.

---

## 7. [G] Raw similarities and invertible intertwiners ruled out

A similarity

[
B=SAS^{-1}
]

preserves the complete characteristic polynomial. Therefore the differing spectra above rule out, generically from j=3/2 onward,

[
oxed{
L_Y
otsim L_c,qquad
L_Y
otsim Q_a,qquad
L_c
otsim Q_a.
}
]

Unitary equivalence is ruled out a fortiori.

Likewise an invertible intertwiner satisfying

[
SB=AS
]

would imply similarity, so no bijective physical-operator intertwiner exists between the generic raw paths.

Scale-free spectral ratios also rule out generic scalar-rescaled similarities

[
B=alpha SAS^{-1}.
]

The j=1/2 and j=1 scalar-normalized coincidences are low-dimensional exceptions, not a general bridge.

---

## 8. [D][G] Orientation flattening of the symmetric paths

For either real symmetric path (Ain{L_Y,L_c}), restrict to its nonzero sector and define

[
S_A=operatorname{sgn}(A).
]

Then

[
S_A^2=I,qquad S_A^T=S_A.
]

Since (HAH=-A), functional calculus gives

[
HS_AH=-S_A.
]

Define

[
oxed{R_A=HS_A.}
]

Then

[
R_A^2
=
HS_AHS_A
=
-S_A^2
=
-I,
]

so

[
oxed{R_A^4=I.}
]

Also

[
HR_AH=-R_A=R_A^{-1}.
]

Thus

[
oxed{
R_A^4=I,qquad H^2=I,qquad HR_AH=R_A^{-1}.
}
]

Moreover,

[
R_A^T=-R_A,qquad R_A^TR_A=I.
]

So orientation flattening converts each real symmetric bipartite path into a real orthogonal complex structure.

The parity factor H is essential: (operatorname{sgn}(A)) itself is an involution, not a quarter-turn.

---

## 9. [D][G] Tetrahedral flattening

For the Hermitian imaginary-antisymmetric volume path, v13.599 gives

[
oxed{
R_a=-i,operatorname{sgn}(Q_a)
}
]

on the nonzero sector.

Again,

[
R_a^2=-I,qquad
R_a^4=I,qquad
HR_aH=R_a^{-1}.
]

Thus the three prescriptions

[
oxed{
R_Y=H,operatorname{sgn}(L_Y),
}
]

[
oxed{
R_c=H,operatorname{sgn}(L_c),
}
]

and

[
oxed{
R_a=-i,operatorname{sgn}(Q_a)
}
]

produce the same abstract real D8 carrier type.

---

## 10. [D] Explicit standard-plane decomposition

Let (E_+) be the H=+1 subspace inside the nonzero sector. Choose an orthonormal basis

[
e_1,ldots,e_{N_j}
]

of (E_+), with

[
N_j=
egin{cases}
j,&jinmathbb Z,\\
j+rac12,&jinmathbb Z+rac12.
end{cases}
]

Set

[
o_r=Re_r.
]

Because (HR=-RH),

[
Ho_r=-o_r.
]

Because (R^2=-I),

[
Ro_r=-e_r.
]

Therefore each

[
Pi_r=operatorname{span}{e_r,o_r}
]

is invariant and carries

[
R|_{Pi_r}
=
egin{pmatrix}
0&-1\\
1&0
end{pmatrix},
qquad
H|_{Pi_r}
=
egin{pmatrix}
1&0\\
0&-1
end{pmatrix}.
]

Hence

[
oxed{
mathcal H_{m nz}congho^{oplus N_j},
}
]

where (ho) is the standard real two-dimensional D8 representation.

---

## 11. [D] Explicit orthogonal intertwiner after flattening

For two paths A and B, choose parity-adapted plane bases

[
{e_r^{(A)},R_Ae_r^{(A)}},
qquad
{e_r^{(B)},R_Be_r^{(B)}}.
]

Define (U_{BA}) by

[
U_{BA}e_r^{(A)}=e_r^{(B)},
]

[
U_{BA}R_Ae_r^{(A)}
=
R_Be_r^{(B)}.
]

Then (U_{BA}) is orthogonal and

[
oxed{
U_{BA}R_A=R_BU_{BA},
}
]

[
oxed{
U_{BA}H=HU_{BA}.
}
]

Therefore

[
oxed{
(R_Y,H)simeq(R_c,H)simeq(R_a,H)
}
]

on the nonzero sectors.

This is a genuine representation intertwiner, in contrast to the ruled-out raw physical-operator intertwiners.

---

## 12. [D][G] Integer-j zero line and full-space extension

For integer j, each path has a unique reflection-even zero mode (|Z_Aangle):

[
A|Z_Aangle=0,qquad
H|Z_Aangle=|Z_Aangle.
]

The zero vectors are weight-dependent and generally distinct, but this does not obstruct abstract full-space D8 equivalence.

Let (P_0) be the orthogonal kernel projector.

For the symmetric paths define

[
oxed{
widetilde R_A
=
H,operatorname{sgn}(A)+P_0.
}
]

For the volume path define

[
oxed{
widetilde R_a
=
-i,operatorname{sgn}(Q_a)+P_0.
}
]

On the kernel line,

[
widetilde R=H=1.
]

On the nonzero sector, (widetilde R=R). Hence

[
widetilde R^4=I,qquad
H^2=I,qquad
Hwidetilde RH=widetilde R^{-1}.
]

Therefore

[
oxed{
mathcal H_jcong
mathbf1_{m zero}oplusho^{oplus j}
qquad(jinmathbb Z),
}
]

while

[
oxed{
mathcal H_jcong
ho^{oplus(j+1/2)}
qquad(jinmathbb Z+	frac12).
}
]

An orthogonal full-space intertwiner may send the normalized zero mode of one path to that of another and intertwine the standard D8 planes on the complement.

Thus the distinct zero vectors are not a representation-theoretic obstruction. What is impossible is demanding (R^2=-I) on the full odd-dimensional real space without splitting/extending the zero line.

---

## 13. [G] Three-layer hierarchy

The comparison now separates three logically distinct layers.

### Metric/operator layer

The weights

[
Y_r,qquad c_k,qquad a_k
]

produce different spectra, determinants, moments, and characteristic polynomials. Generic raw similarity fails.

### Bipartite layer

All three satisfy

[
HAH=-A
]

and share the same integer/half-integer kernel parity law.

### Orientation-flattened layer

After discarding nonzero spectral magnitudes while retaining orientation/parity,

[
oxed{
	ext{SU(2)/magnetic path}
;sim_{D_8};
	ext{Racah path}
;sim_{D_8};
	ext{tetrahedral-volume path}.
}
]

More precisely,

[
oxed{
egin{cases}
mathbf1_{m zero}oplusho^{oplus j},
&jinmathbb Z,\\
ho^{oplus(j+1/2)},
&jinmathbb Z+rac12.
end{cases}}
]

Thus spectral flattening is doing genuine mathematical work: it quotients out exactly the metric spectral information that prevented raw operator equivalence.

---

## 14. Guardrails

1. (L_c) here is the zero-diagonal Racah path extracted from (K_{23}^2), not the full crossed Casimir.
2. Raw operator similarity and flattened D8 representation equivalence are different claims.
3. The j=1/2 and j=1 scalar-normalized spectral coincidences are low-dimensional accidents and must not be promoted as a general intertwiner.
4. The integer-j zero line is not a complex-structure plane; it carries a separate trivial D8 summand in the full-space extension.
5. No physical identification is made between magnetic dynamics, crossed-Casimir recoupling, and tetrahedral volume. The exact bridge is representation-theoretic after orientation flattening.

## Promoted theorem

For every equal spin j, the three connected weighted paths (L_Y,L_c,Q_a) are generically inequivalent as raw operators, but their orientation-flattened parity pairs are orthogonally equivalent D8 representations:

[
oxed{
(R_Y,H)simeq(R_c,H)simeq(R_a,H).
}
]

Their common representation type is

[
oxed{
egin{cases}
mathbf1_{m zero}oplusho^{oplus j},
&jinmathbb Z,\\
ho^{oplus(j+1/2)},
&jinmathbb Z+rac12.
end{cases}}
]

This is the exact bridge that survives after the spectral-invariant comparison rules out a raw weighted-path similarity.
