# Cone Derivation Ledger v13.602 — Equal-Spin Tetrahedron Volume Coefficient from Casimir Commutator

Date: 2026-09-19

Status labels: [S] standard angular-momentum/recoupling fact, [D] exact derived, [Audit] explicitly cross-checked, [G] structural interpretation, [O] open.

## Coordination / collision and relevance check

Immediately before this write, the live ledger reached v13.601, occupied by External Audit Round 63. v13.602 was free.

Round 63 independently stress-tested the coefficient formula used in v13.599 against fresh tensor-space constructions at j=2 and j=5/2, including spectra and kernel dimensions. It also renumbered the off-resonant magnetic checkpoint to v13.600 and repaired the affected cross-references in v13.599.

The magnetic lane remains structurally relevant through its SU(2) weighted path, but no magnetic/tetrahedral operator equality is used here.

This entry closes the provenance gate left open by v13.599: derive the tetrahedral path coefficient directly from pair Casimirs and recoupling, fixing the factor and orientation sign for the convention

[
Q=mathbf J_1cdot(mathbf J_2	imesmathbf J_3).
]

---

## 1. [D] Pair-Casimir commutator fixes the physical normalization

Define

[
K_{12}^2=(mathbf J_1+mathbf J_2)^2,
qquad
K_{23}^2=(mathbf J_2+mathbf J_3)^2.
]

Since operators on distinct legs commute,

[
K_{12}^2=J_1^2+J_2^2+2J_1^aJ_2^a,
]

[
K_{23}^2=J_2^2+J_3^2+2J_2^bJ_3^b.
]

All one-leg Casimirs commute with the remaining terms, hence

[
[K_{12}^2,K_{23}^2]
=
4[J_1^aJ_2^a,J_2^bJ_3^b].
]

Using

[
[J_2^a,J_2^b]=iepsilon_{abc}J_2^c,
]

we obtain

[
[K_{12}^2,K_{23}^2]
=
4iepsilon_{abc}J_1^aJ_2^cJ_3^b.
]

Interchanging b and c reverses the Levi-Civita sign:

[
epsilon_{abc}J_1^aJ_2^cJ_3^b
=
-epsilon_{abc}J_1^aJ_2^bJ_3^c.
]

Therefore, for

[
Q=epsilon_{abc}J_1^aJ_2^bJ_3^c,
]

the exact identity is

[
oxed{
[K_{12}^2,K_{23}^2]=-4iQ.
}
]

Equivalently,

[
oxed{
Q=rac{i}{4}[K_{12}^2,K_{23}^2].
}
]

This fixes the overall factor for the project's Q convention without importing a separate LQG volume normalization.

Reversing the physical orientation, for example (2leftrightarrow3), sends

[
oxed{Qmapsto-Q.}
]

---

## 2. [S][D] Recoupling basis

For four equal spins j, use the normalized invariant basis

[
|kangle
=
|[(j_1j_2)k,(j_3j_4)k],J=0angle,
qquad
k=0,ldots,2j.
]

It diagonalizes the first pair Casimir:

[
oxed{
K_{12}^2|kangle=k(k+1)|kangle.
}
]

Hence for arbitrary k',k,

[
langle k'|Q|kangle
=
rac{i}{4}
left[k'(k'+1)-k(k+1)ight]
langle k'|K_{23}^2|kangle.
]

For the upper neighboring entry (k'=k-1),

[
(k-1)k-k(k+1)=-2k,
]

so

[
oxed{
langle k-1|Q|kangle
=
-rac{ik}{2}
langle k-1|K_{23}^2|kangle.
}
]

Thus the tetrahedral coefficient problem reduces exactly to one crossed-pair Casimir matrix element.

---

## 3. [S] Racah transform for the crossed pair

Let (|ellangle_{23}) be the corresponding invariant basis coupled first through legs 2 and 3. Then

[
K_{23}^2|ellangle_{23}
=
ell(ell+1)|ellangle_{23}.
]

The two recoupling bases are related by the Racah matrix

[
{}_{12}langle k|ellangle_{23}
=
(-1)^eta
sqrt{(2k+1)(2ell+1)}
egin{Bmatrix}
j&j&k\\
j&j&ell
end{Bmatrix},
]

where the common phase convention is chosen consistently with the earlier recoupling basis.

Therefore

[
langle k'|K_{23}^2|kangle
=
sum_{ell=0}^{2j}
ell(ell+1)
,{}_{12}langle k'|ellangle_{23}
,{}_{23}langleell|kangle_{12}.
]

The Racah three-term recurrence for multiplication by (ell(ell+1)) makes this matrix tridiagonal in k.

For equal external spins, its neighboring coefficient simplifies to

[
oxed{
langle k-1|K_{23}^2|kangle
=
rac{
kig[(2j+1)^2-k^2ig]
}{
2sqrt{4k^2-1}
},
qquad
k=1,ldots,2j.
}
]

The quantity is strictly positive throughout the allowed range.

---

## 4. [D] Exact tetrahedral coefficient

Insert the crossed-Casimir coefficient into the commutator result:

[
langle k-1|Q|kangle
=
-rac{ik}{2}
rac{k[(2j+1)^2-k^2]}
{2sqrt{4k^2-1}}.
]

Thus

[
oxed{
langle k-1|Q|kangle=-ia_k,
}
]

with

[
oxed{
a_k=
rac{
k^2[(2j+1)^2-k^2]
}{
4sqrt{4k^2-1}
},
qquad
k=1,ldots,2j.
}
]

Hermiticity gives

[
oxed{
langle k|Q|k-1angle=+ia_k.
}
]

Therefore

[
oxed{
Q_j=
i
egin{pmatrix}
0&-a_1&0&cdots&0\\
a_1&0&-a_2&ddots&dots\\
0&a_2&0&ddots&0\\
dots&ddots&ddots&ddots&-a_{2j}\\
0&cdots&0&a_{2j}&0
end{pmatrix}.
}
]

This is exactly the weighted path used as input in v13.599.

---

## 5. [Audit] Low-spin normalization checks

### j=1/2

For k=1,

[
a_1
=
rac{4-1}{4sqrt3}
=
rac{sqrt3}{4}.
]

Hence

[
Q_{1/2}
=
egin{pmatrix}
0&-isqrt3/4\\
isqrt3/4&0
end{pmatrix},
]

matching v13.591 exactly.

### j=1

[
a_1=rac{2sqrt3}{3},
qquad
a_2=rac{sqrt{15}}3,
]

matching v13.596 exactly.

### Higher-spin audit status

Round 63 independently reconstructed the tensor-space volume spectra at j=2 and j=5/2 and found agreement with the same (a_k) formula to numerical roundoff, while also verifying the general positivity lemma used by v13.599.

Thus the coefficient is now supported both by the recoupling derivation here and by independent low/higher-spin reconstruction checks.

---

## 6. [D] Orientation sign versus basis-phase sign

Two sign operations must not be conflated.

### Physical orientation reversal

Changing

[
Q_{123}
=
mathbf J_1cdot(mathbf J_2	imesmathbf J_3)
]

to the oppositely oriented triple gives

[
oxed{Qmapsto-Q.}
]

This is a physical orientation convention.

### Recoupling basis rephasing

A basis transformation such as

[
|kanglemapsto(-1)^k|kangle
]

also reverses every displayed nearest-neighbor matrix sign. But this is merely a similarity transformation of the matrix representation; it does not reverse physical tetrahedral orientation.

The project's marked convention is fixed by

[
Q=mathbf J_1cdot(mathbf J_2	imesmathbf J_3)
]

together with the recoupling phases used in v13.591, giving

[
oxed{
langle k-1|Q|kangle=-ia_k.
}
]

---

## 7. [D][G] Provenance chain for the general D8 theorem

The load-bearing chain is now

[
oxed{
Q=mathbf J_1cdot(mathbf J_2	imesmathbf J_3)
}
]

[
Downarrow
]

[
oxed{
Q=rac{i}{4}[K_{12}^2,K_{23}^2]
}
]

[
Downarrow
]

[
oxed{
K_{12}^2|kangle=k(k+1)|kangle
}
]

plus the equal-spin Racah recurrence

[
Downarrow
]

[
oxed{
a_k=
rac{k^2[(2j+1)^2-k^2]}
{4sqrt{4k^2-1}}
}
]

[
Downarrow
]

[
oxed{
Q_j=i	imes	ext{real antisymmetric nonvanishing weighted path}
}
]

[
Downarrow
]

the v13.599 kernel-parity and spectral-flattening theorem:

[
oxed{
mathcal H_jcong
egin{cases}
mathbf1_{m zero}oplusho^{oplus j},
&jinmathbb Z,\\
ho^{oplus(j+1/2)},
&jinmathbb Z+rac12.
end{cases}
}
]

Thus the principal coefficient-provenance assumption left open in v13.599 is closed.

---

## 8. Guardrails

1. The operator Q here is the dimensionless oriented triple product. A physical LQG volume operator may include additional regularization, Planck-scale, Immirzi, combinatorial, and square-root factors; none are silently absorbed here.
2. The overall sign depends on physical orientation and on the marked ordering (1,2,3).
3. Matrix-entry signs also depend on recoupling-state phase convention; those basis signs are not physical orientation reversals.
4. The D8 quarter-turn remains the spectral flattening (-i,operatorname{sgn}(Q)) on the nonzero sector, not the raw Q for generic j.
5. The magnetic weighted path is coordinated but logically distinct.

## Promoted conclusion

For the project's convention

[
Q=mathbf J_1cdot(mathbf J_2	imesmathbf J_3),
]

the exact pair-Casimir identity is

[
oxed{
Q=rac{i}{4}[K_{12}^2,K_{23}^2],
}
]

and the equal-spin recoupling-basis entries are

[
oxed{
langle k-1|Q|kangle
=
-i
rac{k^2[(2j+1)^2-k^2]}
{4sqrt{4k^2-1}}.
}
]

This supplies the exact normalization, orientation convention, and coefficient formula required by the general kernel/D8 theorem of v13.599.

## Open next gate

The remaining algebraic refinement is to write the equal-spin Racah three-term recurrence itself in the ledger and derive the crossed-Casimir neighboring coefficient from that recurrence line by line. This would make even the intermediate 6j/Racah reduction explicit rather than citing it as the standard recoupling step.
