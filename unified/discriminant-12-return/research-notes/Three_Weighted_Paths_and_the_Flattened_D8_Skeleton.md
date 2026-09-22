# Three Weighted Paths and One Flattened D8 Skeleton

## Companion synthesis note

**Status.** Standalone synthesis companion to the closed and independently audited ledger result recorded in v13.624, v13.631, and the closure entry v13.636. This note reorganizes that result as a readable body-of-work statement. It does not add a physical equivalence claim.

## 1. The question

Three finite operators arise from different parts of the project:

1. the SU(2)/magnetic ladder path,
2. the zero-diagonal path extracted from crossed-pair Racah recoupling,
3. the oriented-volume operator of the equal-spin four-valent quantum tetrahedron.

Their edge weights are visibly related, but the operators do not have the same physical meaning. The exact result has two complementary halves:

- **negative:** their raw spectra are generically different, so the three operators are not the same dynamics in different bases;
- **positive:** after discarding nonzero spectral magnitudes while retaining parity and orientation, all three carry the same real dihedral D8 representation.

That distinction is the central point of this note.

## 2. The three weighted paths

Fix spin (j). All three carrier spaces have dimension

[
N=2j+1.
]

### 2.1 SU(2)/magnetic ladder

Relabel the (J_z) chain by (r=0,ldots,2j). Define

[
Y_r=sqrt{(2j-r)(r+1)}
]

and

[
L_Y=
egin{pmatrix}
0&Y_0&&\
Y_0&0&Y_1&\
&ddots&ddots&ddots\
&&Y_{2j-1}&0
end{pmatrix}.
]

Exactly,

[
oxed{L_Y=2J_x.}
]

Hence

[
operatorname{spec}L_Y={-2j,-2j+2,ldots,2j-2,2j}.
]

### 2.2 Zero-diagonal Racah path

For (k=1,ldots,2j), define

[
c_k=
rac{k[(2j+1)^2-k^2]}
{2sqrt{4k^2-1}}.
]

The symmetric zero-diagonal path is

[
L_c=
egin{pmatrix}
0&c_1&&\
c_1&0&c_2&\
&ddots&ddots&ddots\
&&c_{2j}&0
end{pmatrix}.
]

This point matters:

[
oxed{L_c
eq K_{23}^2.}
]

It is only the off-diagonal path extracted from the crossed Casimir. The full crossed Casimir also has diagonal entries

[
d_k=2j(j+1)-rac{k(k+1)}2.
]

### 2.3 Tetrahedral oriented-volume path

Let

[
Q_a=mathbf J_1cdot(mathbf J_2	imesmathbf J_3).
]

In the equal-spin recoupling basis,

[
Q_a=i
egin{pmatrix}
0&-a_1&&\
a_1&0&-a_2&\
&ddots&ddots&ddots\
&&a_{2j}&0
end{pmatrix},
]

where

[
a_k=
rac{k^2[(2j+1)^2-k^2]}
{4sqrt{4k^2-1}}.
]

The Racah and volume weights obey the exact factorization

[
oxed{a_k=rac{k}{2}c_k.}
]

Equivalently, the volume edge weight is the crossed-pair Racah edge weight multiplied by one quarter of the adjacent (K_{12}^2) spectral difference. This follows from

[
Q_a=rac{i}{4}[K_{12}^2,K_{23}^2].
]

## 3. Common bipartite structure

Define the parity/reflection operator

[
H=operatorname{diag}(1,-1,1,-1,ldots).
]

For every one of the three paths,

[
oxed{HAH=-A.}
]

Therefore the spectrum is symmetric under (lambdamapsto-lambda), and each operator has trace zero.

Because all interior path weights are nonzero, the only possible kernel comes from the even/odd vertex imbalance of the connected bipartite chain. Thus

[
oxed{
dimker A=
egin{cases}
1,&jinmathbb Z,\
0,&jinmathbb Z+rac12.
end{cases}}
]

For integer (j), the unique zero vector lies in the (H=+1) sector.

This common parity law is already nontrivial, but it does **not** imply similarity of the raw operators.

## 4. Raw spectral inequivalence

At (j=	frac12) there is only one path edge, so every nonzero two-dimensional zero-diagonal path is a scalar multiple of every other. At (j=1), every connected three-vertex zero-diagonal path has spectrum

[
{0,pmsqrt{w_1^2+w_2^2}},
]

so scalar-normalized spectral coincidences persist for another dimension.

The first genuine separation occurs at

[
j=rac32.
]

For the SU(2) path,

[
operatorname{spec}L_Y={-3,-1,1,3}.
]

For the Racah path,

[
chi_c(lambda)
=
lambda^4-rac{63}{2}lambda^2+rac{945}{16}.
]

For the volume path,

[
chi_a(lambda)
=
left(lambda^2-rac{315}{16}ight)
left(lambda^2-rac{27}{16}ight),
]

so

[
operatorname{spec}Q_a
=
left{
pmrac{3sqrt3}{4},
pmrac{3sqrt{35}}4
ight}.
]

The positive-magnitude ratio of (L_Y) is (3), whereas that of (Q_a) is

[
sqrt{rac{35}{3}},
]

and the Racah path gives a third value. Hence even scalar-rescaled similarity fails.

Therefore, generically from (j=	frac32),

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

In particular, there is no unitary equivalence and no invertible raw-operator intertwiner among the three.

This negative theorem is essential. The unification below is not physical equivalence in disguise.

## 5. Orientation flattening

Restrict first to the nonzero sector.

For the two real symmetric paths define

[
R_Y=H,operatorname{sgn}(L_Y),
qquad
R_c=H,operatorname{sgn}(L_c).
]

For the Hermitian imaginary-antisymmetric volume operator define

[
R_a=-i,operatorname{sgn}(Q_a).
]

The parity factor (H) in the first two definitions is essential: (operatorname{sgn}(L)) itself is an involution, not a quarter-turn.

Using (HAH=-A), functional calculus gives

[
H,operatorname{sgn}(A),H=-operatorname{sgn}(A).
]

Consequently each flattened carrier satisfies

[
oxed{R^2=-I,qquad R^4=I,}
]

and

[
oxed{HRH=R^{-1}=-R.}
]

Thus ((R,H)) realizes the defining real (D_8) relations.

Flattening has discarded the nonzero metric magnitudes that distinguish the three operators while retaining the orientation/parity skeleton.

## 6. Parity-adapted normal form

Let (E_+) denote the (H=+1) part of the nonzero sector and choose an orthonormal basis

[
e_1,ldots,e_{N_j},
]

where

[
N_j=
egin{cases}
j,&jinmathbb Z,\
j+rac12,&jinmathbb Z+rac12.
end{cases}
]

Define

[
o_r=Re_r.
]

Since (HR=-RH),

[
Ho_r=-o_r.
]

Orthogonality of (R) gives

[
langle o_r,o_sangle=delta_{rs},
qquad
langle e_r,o_sangle=0.
]

Furthermore,

[
Ro_r=R^2e_r=-e_r.
]

Therefore every plane

[
Pi_r=operatorname{span}{e_r,o_r}
]

has the canonical matrices

[
R|_{Pi_r}=
egin{pmatrix}
0&-1\
1&0
end{pmatrix},
qquad
H|_{Pi_r}=
egin{pmatrix}
1&0\
0&-1
end{pmatrix}.
]

Hence

[
oxed{mathcal H_{m nz}congho^{oplus N_j},}
]

where (ho) is the standard real two-dimensional representation of (D_8).

## 7. Explicit orthogonal intertwiner

For two flattened carriers (A) and (B), choose parity-adapted bases as above. Define

[
oxed{
U_{Bleftarrow A}
=
sum_{r=1}^{N_j}
left(
|e_r^{(B)}anglelangle e_r^{(A)}|
+
|R_Be_r^{(B)}angle
langle R_Ae_r^{(A)}|
ight).
}
]

This map is orthogonal and satisfies

[
oxed{
U_{Bleftarrow A}R_A=R_BU_{Bleftarrow A},
}
]

and

[
oxed{
U_{Bleftarrow A}H=HU_{Bleftarrow A}.
}
]

Therefore

[
oxed{
(R_Y,H)simeq(R_c,H)simeq(R_a,H)
}
]

on the nonzero sectors.

This is a genuine representation intertwiner. It is **not** an intertwiner of the original raw operators.

## 8. Integer-spin zero line

For (jinmathbb Z), let (z_A) be the normalized zero vector:

[
Az_A=0,qquad Hz_A=z_A.
]

Let

[
P_{0,A}=|z_Aanglelangle z_A|.
]

Extend the flattened quarter-turn by

[
widetilde R_A=R_A+P_{0,A},
]

where (R_A) is taken to vanish on the kernel before the extension. Then

[
widetilde R_Az_A=z_A,qquad Hz_A=z_A,
]

so the zero line carries the trivial (D_8) representation.

The full-space intertwiner is

[
oxed{
widetilde U_{Bleftarrow A}
=
|z_Banglelangle z_A|
+
U_{Bleftarrow A}^{m nz}.
}
]

Thus the full carrier has representation type

[
oxed{
mathcal H_jcong
egin{cases}
mathbf1_{m zero}oplusho^{oplus j},
&jinmathbb Z,\
ho^{oplus(j+1/2)},
&jinmathbb Z+rac12.
end{cases}}
]

The different weight-dependent zero vectors do not obstruct the abstract representation equivalence.

## 9. Nonuniqueness of the intertwiner

The representation type is canonical, but the physical cross-carrier identification is not.

For any

[
Oin O(N_j),
]

rotate the even multiplicity basis by

[
e_r'=sum_sO_{sr}e_s.
]

Then

[
Re_r'=sum_sO_{sr}Re_s,
]

so the same (O) acts simultaneously on the corresponding odd partners. In canonical plane coordinates this is (Ootimes I_2), which commutes with both (R) and (H).

Therefore, after fixing the integer-spin zero-line sign, the family of orthogonal flattened-carrier intertwiners has

[
oxed{O(N_j)}
]

freedom. If the integer-spin zero-vector sign is also left unfixed, there is an additional (O(1)={pm1}).

This nonuniqueness is another reason the theorem should not be read as a canonical physical identification of the three systems.

## 10. Synthesis theorem

**Theorem.** For every equal spin (j), the SU(2)/magnetic ladder path (L_Y), the zero-diagonal crossed-Casimir Racah path (L_c), and the tetrahedral oriented-volume path (Q_a) are physically and spectrally distinct finite operators. Generically from (j=	frac32) onward they are not similar, not unitarily equivalent, and admit no invertible raw-operator intertwiner.

Nevertheless, after orientation flattening their parity pairs are orthogonally equivalent real (D_8) representations:

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
&jinmathbb Z,\
ho^{oplus(j+1/2)},
&jinmathbb Z+rac12.
end{cases}}
]

An explicit intertwiner is obtained by choosing orthonormal bases of the reflection-even nonzero sectors, generating the odd partners with (R), and mapping corresponding parity-adapted planes. For integer (j), the normalized even zero line is mapped separately. The intertwiner is unique only up to (O(N_j)), together with an optional (O(1)) zero-line sign.

## 11. What the theorem does and does not say

The exact content is

[
oxed{
	ext{three distinct metric operators}
longrightarrow
	ext{one common flattened }D_8	ext{ skeleton}.
}
]

It is a representation-theoretic unification.

It is **not** a claim that magnetic spin-drive dynamics, Racah recoupling, and LQG tetrahedral-volume dynamics are physically equivalent. Their raw spectral inequivalence explicitly rules that out.

It does not identify (L_c) with the full crossed Casimir.

It does not turn the flattened (D_8) intertwiner into an intertwiner of the raw physical operators.

The (O(N_j)) freedom means that no canonical physical map between the three carriers follows from the theorem alone.

There is no established consequence here for the (chi_{-4})/L-function thread.

There is likewise no result here identifying this closed theorem with the separate higher-order magnetic-driver Floquet expansion. A later analog-simulation question may use the theorem as an input, but that is a new problem and must be derived separately.

Finally, comparisons with E8/golden-ratio spin-chain phenomenology remain outside observations, not consequences of this theorem.

## 12. Provenance and closure

The raw spectral comparison and common flattened-carrier theorem were established in ledger v13.624. The constructive parity-adapted intertwiner, integer-spin zero-line extension, and (O(N_j)) freedom were established in v13.631. Both were independently reconstructed in External Audit Rounds 66/67.

Ledger v13.635 recommended that the closed result be pulled into a dedicated synthesis note before it became buried under unrelated rounds. Ledger v13.636 recorded the formal closure and guardrails.

This document is the corresponding standalone body-of-work companion. It deliberately stops at that closed theorem. The later analog/digital simulation question opened by v13.638, including any magnetic pulse synthesis or transported controls, belongs to a separate investigation.
