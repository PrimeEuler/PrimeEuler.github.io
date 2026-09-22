# Cone Derivation Ledger v13.650 — Exact Endpoint-Free Local Quadratic Synthesis of the j=3/2 Tetrahedral Orientation Carrier

Date: 2026-09-22

Status: exact constructive refinement of v13.643. Promotes a finite local-control sequence using only J_x, J_y, and J_z^2 that realizes the flattened tetrahedral orientation carrier R_a up to global phase, with no direct endpoint Hamiltonian coupling.

## 0. Collision, relevance, and audit check

The live ledger was fetched before this write. The highest occupied version is v13.649 and v13.650 is free.

Relevant entries since v13.643 were checked:

- v13.646, External Audit Round 68, independently verified the load-bearing v13.643 no-go, pulse synthesis, intertwiner, transported protocol, and O(2) endpoint lower bound. It also found one isolated transcription error in the displayed static K_a^(0) matrix: coefficients 7 in the (1,2)/(2,1) and (2,3)/(3,2) entries must be 5. The companion note and v13.643 have now been corrected. The audited transported identity and endpoint lower bound are unaffected.
- v13.645 and v13.649 advance the separate higher-order magnetic-driver Floquet thread.
- v13.647 advances the separate Friedrichs/Krein thread.
- v13.648 is External Audit Round 69 and does not supersede the present control question.

The standalone note
`research-notes/Driven_Spin_Analog_Simulation_of_Flattened_Tetrahedral_Orientation_j3_2.md`
has been extended with the complete derivation below.

## 1. Local control primitives

Define

[
X(a)=e^{-iaJ_x},qquad
Y(a)=e^{-iaJ_y},qquad
Q(a)=e^{-iaJ_z^2}.
]

For j=3/2,

[
J_z^2=operatorname{diag}(9/4,1/4,1/4,9/4),
]

so

[
Q(a)=e^{-ia/4}operatorname{diag}(e^{-2ia},1,1,e^{-2ia}).
]

Every instantaneous generator J_x, J_y, or J_z^2 is nearest-neighbor or diagonal in the tetrahedral k-basis. In particular, none has a direct 0<->3 matrix element.

## 2. Structured product and exact angle elimination

Consider

[
U=
Q(alpha_9)Y(-pi/2)X(-pi/2)
Q(alpha_6)Y(alpha_5)X(-pi/2)
Q(alpha_3)Y(pi/2)X(alpha_1).
]

Impose

[
oxed{alpha_5=alpha_1-pi.}
]

After removing the scalar phases of the Q factors, exact multiplication shows that the full projective product is independent of alpha_1.

Let

[
z_3=e^{-2ialpha_3},qquad
z_6=e^{-2ialpha_6},qquad
z_9=e^{-2ialpha_9}.
]

Then

[
oxed{
overline U=
rac18
egin{pmatrix}
0&sqrt3z_9(z_3z_6-3z_3+z_6+1)&0&z_9(z_3z_6-3z_3-3z_6-3)\
sqrt3(z_3z_6+z_3-3z_6+1)&0&3z_3z_6+3z_3+3z_6-1&0\
0&-3z_3z_6-3z_3-3z_6+1&0&sqrt3(-z_3z_6-z_3+3z_6-1)\
z_9(-z_3z_6+3z_3+3z_6+3)&0&sqrt3z_9(-z_3z_6+3z_3-z_6-1)&0
end{pmatrix}.
}
]

Thus the checkerboard support of R_a is exact before any numerical fitting.

## 3. Exact algebraic phases

Recall

[
R_a=
egin{pmatrix}
0&-p&0&-q\
p&0&-q&0\
0&q&0&-p\
q&0&p&0
end{pmatrix},
]

with

[
p=sqrt{rac{11+sqrt{105}}{30}},
qquad
q=sqrt{rac{19-sqrt{105}}{30}}.
]

Set

[
oxed{z_9=-z_3.}
]

The required sign relations collapse to

[
z_3^2z_6-3z_3^2+3z_6-1=0,
]

hence

[
oxed{
z_6=rac{3z_3^2+1}{z_3^2+3}.
}
]

Define

[
r=rac qp=
sqrt{rac{19-sqrt{105}}{11+sqrt{105}}}.
]

The remaining amplitude-ratio equation becomes

[
oxed{
-sqrt3(3z^2+2z+3)=3r(z-1)^2,
qquad z=z_3.
}
]

Choose

[
oxed{
z=
rac{
r-rac1{sqrt3}
-rac{2i}{3}sqrt{6(sqrt3r+1)}
}
{r+sqrt3}.
}
]

Direct algebra gives

[
oxed{|z|=1.}
]

Now define

[
oxed{
w=rac{3z^2+1}{z^2+3}.
}
]

Then

[
oxed{|w|=1.}
]

Choose real A,B,C with

[
e^{-2iA}=z,qquad
e^{-2iB}=w,qquad
e^{-2iC}=-z.
]

## 4. Exact matrix certificate

Substitute

[
z_3=z,qquad z_6=w,qquad z_9=-z.
]

The complete projective product reduces identically to

[
oxed{overline U=sR_a,}
]

where

[
oxed{
s=
rac{sqrt3,z(z-1)^2}{2p(z^2+3)}.
}
]

The quadratic defining equation for z and |z|=1 imply

[
oxed{|s|=1.}
]

Equivalently,

[
oxed{R_a^daggeroverline U=sI_4.}
]

The sixteen component residual identities are

[
egin{aligned}
U_{00}=U_{02}=U_{11}=U_{13}
=U_{20}=U_{22}=U_{31}=U_{33}&=0,\
U_{01}=U_{23}&=-sp,\
U_{10}=U_{32}&=sp,\
U_{03}=U_{12}&=-sq,\
U_{21}=U_{30}&=sq.
end{aligned}
]

These are exact algebraic identities.

Restoring the physical scalar phases of Q(A), Q(B), Q(C),

[
oxed{
U_{m phys}=e^{iPhi}R_a,
}
]

where

[
oxed{
e^{iPhi}=e^{-i(A+B+C)/4}s.
}
]

## 5. Exact eight-pulse sequence

Because alpha_1 is redundant once alpha_5=alpha_1-pi, choose alpha_1=0. Then alpha_5=-pi and the first X pulse is the identity.

The exact local sequence becomes

[
oxed{
U_{m loc}
=
Q(C),
Y(-pi/2),
X(-pi/2),
Q(B),
Y(-pi),
X(-pi/2),
Q(A),
Y(pi/2)
=
e^{iPhi}R_a.
}
]

Only the three control generators

[
oxed{J_x,qquad J_y,qquad J_z^2}
]

are used.

At no stage does the instantaneous Hamiltonian contain a direct 0<->3 matrix element.

## 6. Refined endpoint theorem

v13.643 established, and v13.646 independently audited, that for the transported one-generator family

[
K_a=U_{aleftarrow Y}J_xU_{aleftarrow Y}^T
]

the full O(2) gauge freedom obeys

[
oxed{
min_{O(2)}|(K_a)_{03}|
=
sqrt{rac{19-sqrt{105}}{30}}-rac12>0.
}
]

The present exact local sequence proves that this nonzero lower bound is **not** a fundamental requirement of the target R_a.

Instead,

[
oxed{
	ext{endpoint coupling is intrinsic to the single transported-}J_x	ext{ realization,}
}
]

while

[
oxed{
	ext{direct endpoint coupling is unnecessary for general time-ordered local quadratic control.}
}
]

The endpoint amplitude of R_a is generated dynamically by the ordered product of nearest-neighbor/diagonal pulses.

## 7. Promoted theorem

For j=3/2, the flattened tetrahedral orientation carrier R_a admits an exact finite realization using only the local quadratic-control set {J_x,J_y,J_z^2}. One explicit realization has eight nontrivial pulses and satisfies

[
U_{m loc}=e^{iPhi}R_a
]

with the algebraic phases specified in Sections 3-5.

Therefore the residual endpoint coupling found in the O(2)-optimized transported generator is a genuine obstruction to that **particular one-generator construction**, but is not an obstruction to exact analog simulation of R_a itself.

## 8. Guardrails

1. The target is the flattened orientation carrier R_a=-i sign(Q_a), not the raw volume operator Q_a or its spectral magnitudes.
2. No physical equivalence between magnetic-spin and tetrahedral-volume dynamics is asserted.
3. The eight-pulse sequence proves exact finite realizability; it is not claimed to be globally pulse-count minimal or time-optimal.
4. The local statement refers to instantaneous matrix support in the tetrahedral k-basis: J_x and J_y are nearest-neighbor and J_z^2 is diagonal. Effective longer-range terms may arise through time ordering/commutators.
5. The v13.643 O(2) lower bound remains valid for the transported-J_x family and is not weakened.
6. The Section-5 static K_a matrix typo identified by v13.646 has been corrected in v13.643 and the standalone note; no promoted downstream identity depended on the incorrect coefficients.
7. No chi_-4/L-function consequence is asserted.
8. The separate magnetic-driver Floquet thread remains logically distinct.
9. No E8/golden-ratio spin-chain conclusion is asserted.
