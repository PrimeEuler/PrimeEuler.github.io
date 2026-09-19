# Cone Derivation Ledger v13.596 — Spin-1 Tetrahedron Zero-Volume Mode and Nonzero-Sector D8

Date: 2026-09-19

Status labels: [S] standard representation fact, [D] exact derived, [Audit] explicitly checked algebraically in this checkpoint, [G] structural interpretation, [O] open.

## Coordination / collision check

Immediately before this write, the live ledger reached v13.595, occupied by the resonant magnetic-driver weighted-multiplet checkpoint. v13.596 was free.

The parallel magnetic lane is now directly relevant at the structural level: v13.595 found a three-state j=1 weighted path with a coherent zero/dark state, while this checkpoint finds a three-dimensional j=1 tetrahedral intertwiner path with a zero-volume mode. These are not the same operators or the same zero vector, and no intertwiner between them is claimed here. The shared path-plus-kernel pattern is recorded only as a comparison target.

---

## 1. [S] Equal-spin j=1 intertwiner space

For four equal face spins

[
j_1=j_2=j_3=j_4=1,
]

the gauge-invariant recoupling space has basis

[
mathcal B_k=(|0angle,|1angle,|2angle)
]

and dimension

[
oxed{dimmathcal H_{m inv}^{(1)}=3.}
]

Use the same oriented triple-product convention as v13.591 and v13.593,

[
Q_{m vol}=mathbf J_1cdot(mathbf J_2	imesmathbf J_3).
]

---

## 2. [D] Exact j=1 volume matrix

Projection into the recoupling basis gives

[
oxed{
Q_{m vol}^{(1)}
=
i
egin{pmatrix}
0&-rac{2sqrt3}{3}&0\\
rac{2sqrt3}{3}&0&-rac{sqrt{15}}3\\
0&rac{sqrt{15}}3&0
end{pmatrix}.
}
]

Thus the physical volume operator is again strictly nearest-neighbor in k:

[
oxed{0leftrightarrow1leftrightarrow2.}
]

Set

[
a=rac{2sqrt3}{3},
qquad
b=rac{sqrt{15}}3.
]

Then

[
a^2+b^2=rac43+rac53=3.
]

The characteristic polynomial is

[
oxed{chi_Q(lambda)=lambda(lambda^2-3)}
]

and hence

[
oxed{operatorname{spec}(Q_{m vol}^{(1)})={-sqrt3,0,+sqrt3}.}
]

---

## 3. [D][Audit] Exact zero-volume mode

Solving

[
Q_{m vol}^{(1)}z=0
]

gives the even-k vector

[
zpropto
egin{pmatrix}
sqrt5/2\\
0\\
1
end{pmatrix}.
]

The normalized zero mode is

[
oxed{
|Zangle
=
rac{sqrt5}{3}|0angle
+
rac23|2angle.
}
]

Therefore

[
oxed{Q_{m vol}|Zangle=0.}
]

Choose the orthogonal normalized even-k state

[
oxed{
|Eangle
=
rac23|0angle
-
rac{sqrt5}{3}|2angle
}
]

and the odd state

[
oxed{|Oangle=|1angle.}
]

Then

[
oxed{
mathcal H_{m inv}^{(1)}
=
operatorname{span}{|Zangle}
oplus
mathcal H_{m nz},
}
]

where

[
oxed{
mathcal H_{m nz}
=
operatorname{span}{|Eangle,|Oangle}.
}
]

---

## 4. [D][Audit] Nonzero-volume block

In the ordered basis

[
mathcal B_{m nz}=(|Eangle,|Oangle),
]

the projected operator is, with the displayed phase/sign convention,

[
oxed{
Q_{m vol}ig|_{mathcal H_{m nz}}
=
sqrt3
egin{pmatrix}
0&-i\\
i&0
end{pmatrix}
=
sqrt3,sigma_y.
}
]

Consequently,

[
oxed{
Q_{m vol}^2ig|_{mathcal H_{m nz}}=3I_2.
}
]

Thus ordinary scalar normalization suffices on the nonzero sector. Define

[
oxed{
R_{m nz}
=
-irac{Q_{m vol}}{sqrt3}
Big|_{mathcal H_{m nz}}.
}
]

After choosing the orientation of |E> consistently with the v13.587/v13.591 marked convention,

[
oxed{
R_{m nz}
=
egin{pmatrix}
0&-1\\
1&0
end{pmatrix}.
}
]

Therefore

[
oxed{R_{m nz}^2=-I_2},
qquad
oxed{R_{m nz}^4=I_2}.
]

---

## 5. [D][Audit] Reflection and D8

The natural k-parity involution on the full recoupling space is

[
oxed{
H=operatorname{diag}(1,-1,1).
}
]

It acts by

[
H|Zangle=|Zangle,
qquad
H|Eangle=|Eangle,
qquad
H|Oangle=-|Oangle.
]

Thus the kernel and nonzero-volume sector are separately H-invariant.

On (mathcal H_{m nz}),

[
oxed{
H_{m nz}
=
egin{pmatrix}
1&0\\
0&-1
end{pmatrix}.
}
]

Then

[
H_{m nz}R_{m nz}H_{m nz}
=
-R_{m nz}.
]

Since

[
R_{m nz}^{-1}=-R_{m nz},
]

we have

[
oxed{
H_{m nz}R_{m nz}H_{m nz}
=
R_{m nz}^{-1}.
}
]

Therefore

[
oxed{
R_{m nz}^4=I,qquad
H_{m nz}^2=I,qquad
H_{m nz}R_{m nz}H_{m nz}=R_{m nz}^{-1},
}
]

and hence

[
oxed{
langle R_{m nz},H_{m nz}anglecong D_8.
}
]

So D8 survives exactly on the two-dimensional nonzero-volume subspace.

---

## 6. [D] Full-space obstruction

The full three-dimensional space cannot carry a real operator R satisfying

[
R^2=-I_3.
]

Taking determinants would require

[
(det R)^2=det(-I_3)=-1,
]

which is impossible over the reals.

Equivalently, the odd-dimensional antisymmetric volume structure necessarily has a zero eigenvalue here.

Thus the j=1 result distinguishes

[
oxed{
	ext{full intertwiner space}

eq
	ext{natural D8 carrier}
}
]

while

[
oxed{
	ext{nonzero oriented-volume sector}
=
	ext{exact D8 carrier}.
}
]

---

## 7. [G] Comparison with j=1/2 and j=3/2

The audited low-spin pattern is now:

### j=1/2

[
dimmathcal H_{m inv}=2,
]

with no zero-volume mode. Scalar normalization of Q_vol gives the full-space D8 quarter-turn.

### j=1

[
dimmathcal H_{m inv}=3=1_{m zero}+2_{m nonzero}.
]

The zero-volume mode splits off and the two-dimensional nonzero sector carries D8.

### j=3/2

[
dimmathcal H_{m inv}=4,
]

with no zero-volume mode in the audited spectrum. Because the two nonzero volume magnitudes differ, spectral flattening rather than scalar normalization produces the full-space D8 representation of v13.593.

This supports, but does not yet prove for arbitrary j, the working hypothesis:

[
oxed{
	ext{the natural tetrahedral dihedral carrier is the nonzero oriented-volume sector.}
}
]

---

## 8. [G] Relevance to v13.595 magnetic weighted multiplet

v13.595 independently established for the resonantly driven magnetic j=1 multiplet a connected three-state weighted path and a coherent zero/dark state

[
|Dangle=rac1{sqrt2}(|-1angle-|1angle),
qquad
J_x|Dangle=0.
]

The present tetrahedral j=1 operator likewise has a connected three-state path and an exact kernel vector

[
|Zangle=rac{sqrt5}{3}|0angle+rac23|2angle,
qquad
Q_{m vol}|Zangle=0.
]

The comparison is structurally relevant because both are odd-dimensional nearest-neighbor SU(2)-derived path operators with a one-dimensional kernel.

However:

[
oxed{|Dangle
eq|Zangle}
]

under the displayed native bases and their edge weights differ. No equality, similarity, or physical identification is promoted here.

A legitimate future bridge would require an explicit basis map/intertwiner and a comparison of the weighted path invariants, not merely the shared existence of a dark/zero mode.

---

## 9. Classification and guardrails

### Exact / promoted here

- The displayed j=1 tetrahedral volume matrix and spectrum.
- The exact normalized zero-volume state.
- The orthogonal decomposition into zero and nonzero-volume sectors.
- The nonzero block is a scaled sigma_y.
- Scalar normalization on that block gives the standard 2D quarter-turn.
- k-parity gives the standard reflection.
- The nonzero sector therefore carries exact D8.
- A full-space real complex structure is obstructed in dimension three.

### Guardrails

- The full j=1 intertwiner space does not carry the quarter-turn construction.
- The zero-volume tetrahedral state is not identified with the v13.595 magnetic dark state.
- Shared path-plus-kernel structure is not an operator equality.
- The proposed integer/half-integer pattern remains a hypothesis until higher spins are checked.

### Open next gate

Compute at least j=2 and j=5/2, determine kernel dimensions and nonzero spectra, and test whether spectral sign on the nonzero-volume sector always yields an even-dimensional real complex structure R with k-parity H satisfying

[
R^2=-I,qquad H^2=I,qquad HRH=R^{-1}.
]

In parallel, compare the path invariants of the magnetic driver and tetrahedral volume operators only after rechecking newer magnetic-thread ledger entries.
