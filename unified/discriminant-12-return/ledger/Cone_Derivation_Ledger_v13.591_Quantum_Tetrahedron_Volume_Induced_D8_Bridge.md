# Cone Derivation Ledger v13.591 — Quantum-Tetrahedron Volume-Induced D8 Bridge

Date: 2026-09-18

Status labels: [S] standard SU(2) representation fact, [D] exact derived, [Audit] explicitly checked here, [G] geometric/representation interpretation, [O] open.

## Scope

This checkpoint extends the exact four-spin-1/2 closure kernel of v13.589 and compares its oriented triple-product / tetrahedral volume structure with the already audited transverse-phase D8 representation of v13.587.

The objective is an explicit marked-representation comparison, not a superficial analogy.

Guardrail: the physical oriented-volume operator itself is not identified with the D8 quarter-turn. Rather, after removing its nonzero spectral scale and multiplying by -i, it canonically induces the real quarter-turn generator on the two-dimensional intertwiner space.

---

## 1. [S][D] Four-spin-1/2 intertwiner basis

From v13.589, use the ordered orthonormal recoupling basis

[
mathcal B_k=(v_0,v_1),
]

where

[
v_0=
rac12
egin{pmatrix}
0\1\-1\-1\1\0
end{pmatrix}
]

is the k=0 intertwiner and

[
v_1=
rac1{2sqrt3}
egin{pmatrix}
2\-1\-1\-1\-1\2
end{pmatrix}
]

is the k=1 intertwiner.

Thus

[
mathcal H_{m inv}
=
operatorname{span}{v_0,v_1}.
]

---

## 2. [S][D][Audit] Oriented triple-product operator

Define

[
Q_{m vol}
=
mathbf J_1cdot(mathbf J_2	imesmathbf J_3)
=
epsilon_{abc}J_1^aJ_2^bJ_3^c.
]

In the six-dimensional m_tot=0 basis of v13.589,

[
(e_1,ldots,e_6)
=
(++--,+-+-,+--+,-++-,-+-+,--++),
]

direct Pauli-matrix evaluation gives

[
Q_{m vol}^{(6)}
=
rac{i}{4}
egin{pmatrix}
0&1&0&-1&0&0\
-1&0&0&1&0&0\
0&0&0&0&-1&1\
1&-1&0&0&0&0\
0&0&1&0&0&-1\
0&0&-1&0&1&0
end{pmatrix}.
]

Projecting onto the invariant basis (mathcal B_k=(v_0,v_1)) yields

[
oxed{
Q_{m vol}^{m inv}
=
egin{pmatrix}
0&-rac{isqrt3}{4}\
rac{isqrt3}{4}&0
end{pmatrix}
=
rac{sqrt3}{4}sigma_y.
}
]

Therefore

[
oxed{
left(Q_{m vol}^{m inv}ight)^2
=
rac{3}{16}I_2.
}
]

The oriented-volume eigenvalues are

[
oxed{
q_pm=pmrac{sqrt3}{4}.
}
]

A normalized eigenbasis is

[
oxed{
|pmangle_Q
=
rac1{sqrt2}(v_0pm i v_1).
}
]

---

## 3. [D][Audit] Volume-induced quarter-turn

Remove the nonzero spectral scale and multiply by -i:

[
widehat Q_{m tet}
equiv
-irac{4}{sqrt3}Q_{m vol}^{m inv}.
]

Then

[
oxed{
widehat Q_{m tet}
=
egin{pmatrix}
0&-1\
1&0
end{pmatrix}.
}
]

Hence

[
widehat Q_{m tet}^2=-I_2,
qquad
widehat Q_{m tet}^4=I_2.
]

This is the standard real quarter-turn matrix.

Important guardrail:

[
oxed{
Q_{m vol}^{m inv}
eq widehat Q_{m tet}.
}
]

The first is Hermitian and carries the physical oriented-volume spectrum; the second is the normalized anti-Hermitian/unitary-derived real quarter-turn induced from it.

---

## 4. [D][Audit] Natural reflection on the intertwiner space

Define the parity-in-k involution

[
H_{m tet}|kangle=(-1)^k|kangle.
]

In the ordered basis ((v_0,v_1)),

[
oxed{
H_{m tet}
=
egin{pmatrix}
1&0\
0&-1
end{pmatrix}.
}
]

For j=1/2, exchange of faces 1 and 2 acts by

[
P_{12}|kangle=(-1)^{2j-k}|kangle
=
(-1)^{1-k}|kangle,
]

so on the invariant space

[
oxed{
P_{12}=-H_{m tet}.
}
]

Thus H_tet is, up to the central sign -I, the face-exchange involution.

Directly,

[
H_{m tet}Q_{m vol}^{m inv}H_{m tet}
=
-Q_{m vol}^{m inv}.
]

Therefore the reflection reverses oriented volume.

Equivalently, on the volume eigenstates,

[
oxed{
H_{m tet}|+angle_Q=|-angle_Q,
qquad
H_{m tet}|-angle_Q=|+angle_Q.
}
]

---

## 5. [D][Audit] Exact D8 relations

The pair

[
widehat Q_{m tet}
=
egin{pmatrix}
0&-1\
1&0
end{pmatrix},
qquad
H_{m tet}
=
egin{pmatrix}
1&0\
0&-1
end{pmatrix}
]

satisfies

[
oxed{
widehat Q_{m tet}^4=I_2,
qquad
H_{m tet}^2=I_2,
qquad
H_{m tet}widehat Q_{m tet}H_{m tet}
=
widehat Q_{m tet}^{-1}.
}
]

Hence

[
oxed{
langle widehat Q_{m tet},H_{m tet}angle
cong D_8
}
]

using the project's order-8 convention.

---

## 6. [D][Audit] Exact marked comparison with v13.587

v13.587 audited the transverse-phase generators

[
R=
egin{pmatrix}
0&-1\
1&0
end{pmatrix},
qquad
S=
egin{pmatrix}
1&0\
0&-1
end{pmatrix}.
]

Therefore, in the ordered tetrahedral recoupling basis ((v_0,v_1)),

[
oxed{
widehat Q_{m tet}=R,
qquad
H_{m tet}=S.
}
]

The marked intertwiner is literally

[
oxed{U=I_2.}
]

Explicitly,

[
U^{-1}widehat Q_{m tet}U=R,
qquad
U^{-1}H_{m tet}U=S.
]

Thus the tetrahedral and transverse-phase D8 realizations are not merely abstractly isomorphic; after the stated basis convention they are the same marked real two-dimensional representation.

---

## 7. [D][G] Extension of the existing marked chain

v13.587 certified

[
R^2=-I_2=FS
]

and the safe marked correspondence

[
T_7leftrightarrow FS.
]

Since

[
widehat Q_{m tet}=R,
]

we obtain

[
oxed{
widehat Q_{m tet}^{,2}
=
R^2
=
-I_2
=
FS.
}
]

Therefore the safe enlarged chain is

[
oxed{
T_7
leftrightarrow
FS
=
R^2
=
Q_{m phase}^2
=
widehat Q_{m tet}^{,2}.
}
]

Guardrail: correspondence symbols across arithmetic, electromagnetic, and tetrahedral realizations are not operator equalities between those physical/mathematical domains.

---

## 8. [G] What is genuinely new in this checkpoint

v13.589 established only closure and recoupling:

[
	ext{ledger ladder}
	o
kermathbf J_{m tot}
	o
{k=0,1}.
]

The present checkpoint adds a nontrivial quantum-geometric operator on that kernel:

[
Q_{m vol}^{m inv}
=
rac{sqrt3}{4}sigma_y.
]

Its normalized orientation action produces exactly the already audited quarter-turn generator, while the natural k-parity involution produces exactly the audited reflection generator.

Thus the bridge is now operator-level and marked:

[
oxed{
	ext{tetrahedral oriented volume}
Longrightarrow
widehat Q_{m tet}=R,
qquad
H_{m tet}=S.
}
]

This is materially stronger than a dimension match or a generic statement that both constructions use SU(2).

---

## 9. Classification

### Exact / promoted here

- The projected four-spin-1/2 oriented triple-product matrix is ((sqrt3/4)sigma_y).
- Its eigenvalues are (pmsqrt3/4).
- The normalized induced quarter-turn is exactly (R).
- The k-parity reflection is exactly (S).
- The two generators satisfy the D8 relations exactly.
- The marked intertwiner with v13.587 is (I_2).
- Reflection exchanges the two opposite oriented-volume eigenstates.

### Guardrails

- The physical Hermitian volume operator is not itself the D8 quarter-turn.
- The quarter-turn arises only after removing the nonzero spectral scale and multiplying by -i.
- The arithmetic translation T7 remains related only through the previously certified marked correspondence; no cross-domain operator equality is claimed.

### Open next gate

Generalize the volume calculation from j=1/2 to equal spins j=1 and j=3/2. Determine whether the projected triple-product remains a nearest-neighbor/tridiagonal operator in the recoupling label k and whether any exact normalized D8 substructure survives beyond the two-dimensional intertwiner space. Do not assume the two-dimensional result generalizes.
