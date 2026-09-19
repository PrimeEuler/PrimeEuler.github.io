# Cone Derivation Ledger v13.589 — Four-Spin-1/2 Quantum-Tetrahedron Closure Kernel

Date: 2026-09-18

Status labels: [S] standard SU(2) representation fact, [D] exact derived, [Audit] explicitly checked here, [G] interpretation, [O] open.

## Scope

This checkpoint begins the quantum-tetrahedron thread from the already audited v13.583 Schwinger/Casimir ladder bridge. The purpose is not to identify two constructions because both use tetrahedral language. The test is whether the exact v13.583 ladder data enters the closure-constrained four-spin intertwiner construction.

For four equal face spins j=1/2, the answer is constructive: the v13.583 ladder amplitudes become the exact nonzero entries of the closure matrices in the uncoupled q-basis. Their common kernel is two-dimensional and is exactly the standard k=0,1 recoupling/intertwiner space.

Guardrail: this establishes compatibility with, and an exact realization of, standard SU(2) quantum-tetrahedron recoupling. It does not by itself establish a new quantum-gravity consequence of the cone geometry.

---

## 1. [S][D] Four-face closure

Take

[
mathcal H=(V_{1/2})^{otimes4},
qquad
mathbf J_{m tot}=sum_{i=1}^4mathbf J_i.
]

The invariant/closure space is

[
mathcal H_{m inv}
=
ker mathbf J_{m tot}
=
operatorname{Inv}_{SU(2)}[(V_{1/2})^{otimes4}].
]

For j=1/2 the audited v13.583 amplitudes reduce to

[
J_+|-angle=|+angle,
qquad
J_-|+angle=|-angle,
]

because

[
A_+^2(1/2,-1/2)=A_-^2(1/2,1/2)=1.
]

Thus the transverse closure matrices are exact 0/1 incidence matrices.

---

## 2. [D][Audit] Six-dimensional zero-weight sector

Use the ordered basis

[
egin{aligned}
e_1&=|++--angle,&
e_2&=|+-+-angle,&
e_3&=|+--+angle,\
e_4&=|-++-angle,&
e_5&=|-+-+angle,&
e_6&=|--++angle.
end{aligned}
]

Every basis state satisfies

[
J^z_{m tot}=0.
]

For the m_tot=+1 target basis

[
f_1=|-+++angle,quad
f_2=|+-++angle,quad
f_3=|++-+angle,quad
f_4=|+++-angle,
]

direct action gives

[
oxed{
J^+_{m tot}=
egin{pmatrix}
0&0&0&1&1&1\
0&1&1&0&0&1\
1&0&1&0&1&0\
1&1&0&1&0&0
end{pmatrix}.
}
]

For the m_tot=-1 target basis

[
g_1=|+---angle,quad
g_2=|-+--angle,quad
g_3=|--+-angle,quad
g_4=|---+angle,
]

[
oxed{
J^-_{m tot}=
egin{pmatrix}
1&1&1&0&0&0\
1&0&0&1&1&0\
0&1&0&1&0&1\
0&0&1&0&1&1
end{pmatrix}.
}
]

[Audit] Each column was checked directly by flipping every admissible - spin for J_+ or + spin for J_- exactly once.

---

## 3. [D][Audit] Exact common kernel

Both transverse matrices have rank 4. The stacked closure matrix

[
mathcal C=
egin{pmatrix}
J^+_{m tot}\
J^-_{m tot}
end{pmatrix}
]

also has rank 4. Therefore

[
oxed{dimkermathcal C=6-4=2.}
]

One exact unnormalized nullspace basis is

[
u_1=
egin{pmatrix}
0\1\-1\-1\1\0
end{pmatrix},
qquad
u_2=
egin{pmatrix}
1\0\-1\-1\0\1
end{pmatrix}.
]

Direct multiplication gives

[
J^pm_{m tot}u_1=J^pm_{m tot}u_2=0.
]

Thus

[
oxed{
dimoperatorname{Inv}_{SU(2)}[(V_{1/2})^{otimes4}]=2.
}
]

---

## 4. [S][D][Audit] Match to the k=0 recoupling channel

For the pair (12),

[
|0,0angle_{12}
=
rac1{sqrt2}(|+-angle-|-+angle),
]

and similarly for (34). Therefore

[
|k=0angle
=
|0,0angle_{12}|0,0angle_{34}
]

has six-basis vector

[
oxed{
v_0=
rac12
egin{pmatrix}
0\1\-1\-1\1\0
end{pmatrix}.
}
]

Hence

[
oxed{u_1=2v_0.}
]

It satisfies

[
(mathbf J_1+mathbf J_2)^2v_0=0.
]

---

## 5. [S][D][Audit] Match to the k=1 recoupling channel

For the pair triplet,

[
|1,1angle=|++angle,qquad
|1,0angle=rac1{sqrt2}(|+-angle+|-+angle),qquad
|1,-1angle=|--angle.
]

The singlet in V_1 tensor V_1 is

[
rac1{sqrt3}
left(
|1,1angle|1,-1angle
-|1,0angle|1,0angle
+|1,-1angle|1,1angle
ight).
]

Therefore the second normalized invariant is

[
oxed{
v_1=
rac1{2sqrt3}
egin{pmatrix}
2\-1\-1\-1\-1\2
end{pmatrix}.
}
]

Direct checks give

[
J^pm_{m tot}v_1=0,
]

[
(mathbf J_1+mathbf J_2)^2v_1=2v_1,
]

so this is the k=1 channel. Also

[
v_0^dagger v_0=v_1^dagger v_1=1,
qquad
v_0^dagger v_1=0.
]

Hence

[
oxed{
mathcal H_{m inv}
=
operatorname{span}{v_0,v_1},
qquad
k=0,1.
}
]

The raw Gaussian-elimination vector u_2 is not a pure recoupling channel; rather,

[
oxed{u_2=v_0+sqrt3,v_1.}
]

Thus diagonalizing the pair Casimir selects the physically natural k-basis from an arbitrary nullspace basis.

---

## 6. [D][G] Exact link back to v13.583

The construction now has two exact levels.

### Face level

The v13.583 ladder coefficient

[
A_+^2(j,q)
=
(j-q)(j+q+1)
=
left(j+rac12ight)^2-left(q+rac12ight)^2
]

is literally the squared matrix element used in J^+_tot, and similarly for A_-.

For j=1/2 the nonzero coefficient is exactly 1, producing the incidence matrices above.

### Intertwiner level

The internal recoupling spin has pair Casimir

[
K_{12}^2=k(k+1).
]

Applying the same centered completion gives

[
oxed{
k(k+1)=left(k+rac12ight)^2-rac14.
}
]

For the first quantum tetrahedron,

[
k=0:quad T_k=rac12,quad k(k+1)=0,
]

[
k=1:quad T_k=rac32,quad k(k+1)=2.
]

Thus the two-dimensional invariant space is indexed by the first two members of the same centered half-lattice/Casimir relation already audited in v13.583.

---

## 7. Classification

### Exact / promoted here

- The four-spin-1/2 zero-weight sector has dimension 6.
- The exact J^+_tot and J^-_tot closure matrices are the displayed 0/1 matrices.
- Their common kernel has exact dimension 2.
- The normalized kernel can be chosen as the standard k=0 and k=1 intertwiners v_0,v_1.
- The v13.583 ladder amplitudes enter the closure operator literally.
- The intermediate k channels obey the same exact centered Casimir completion k(k+1)=(k+1/2)^2-1/4.

### Guardrail

These results reproduce standard SU(2) closure and recoupling exactly. No claim is made yet that the cone/factor realization changes the quantum-tetrahedron spectrum or supplies new quantum-gravity dynamics.

### Open next gate

Compute the oriented triple-product / tetrahedral volume operator on span{v_0,v_1}. This is the first natural operator that probes nontrivial quantum geometry beyond closure and representation counting. Compare its exact matrix structure with the already certified cone/phase/incidence structures only after the volume matrix has been derived independently.
