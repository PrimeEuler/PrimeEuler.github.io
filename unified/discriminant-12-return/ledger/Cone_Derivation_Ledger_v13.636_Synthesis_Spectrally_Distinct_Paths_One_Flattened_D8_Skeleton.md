# Cone Derivation Ledger v13.636 — Synthesis: Spectrally Distinct Paths, One Flattened D8 Skeleton

Date: 2026-09-21

Status: synthesis of the independently audited closed result in v13.624 and v13.631. No new physical equivalence is asserted.

## 0. Coordination and audit checkpoint

The live ledger was re-fetched immediately before this write. Tip is v13.635, the External Audit Checkpoint: Thread Status and Recommendations, so v13.636 is free.

Section 3 of v13.635 explicitly recommends a synthesis note for the LQG/tetrahedron thread. It records that v13.624 and v13.631 were independently re-derived from scratch in External Audit Rounds 66/67 and that every boxed claim checked exactly.

This entry acts on that recommendation and closes this sub-result.

---

## 1. The three carriers

For fixed spin j, all three carriers have dimension

[
N=2j+1.
]

### SU(2) / magnetic ladder path

[
L_Y=2J_x,
]

with edge weights

[
Y_r=sqrt{(2j-r)(r+1)},
qquad r=0,ldots,2j-1.
]

### Zero-diagonal Racah path

[
(L_c)_{k-1,k}=(L_c)_{k,k-1}=c_k,
]

with

[
c_k=
rac{k[(2j+1)^2-k^2]}
{2sqrt{4k^2-1}},
qquad k=1,ldots,2j.
]

This is the off-diagonal path extracted from (K_{23}^2), not the full crossed Casimir.

### Tetrahedral oriented-volume path

[
Q_a=i
egin{pmatrix}
0&-a_1&&\\
a_1&0&-a_2&\\
&ddots&ddots&ddots\\
&&a_{2j}&0
end{pmatrix},
]

with

[
a_k=rac{k}{2}c_k.
]

All interior weights are nonzero.

---

## 2. What is common before flattening

With

[
H=operatorname{diag}(1,-1,1,-1,ldots),
]

each carrier satisfies

[
oxed{HAH=-A.}
]

Thus each is bipartite, each has spectrum symmetric about zero, and

[
operatorname{tr}A=0.
]

The connected-path parity imbalance gives

[
oxed{
dimker A=
egin{cases}
1,&jinmathbb Z,\\
0,&jinmathbb Z+rac12.
end{cases}}
]

For integer j the unique zero mode is reflection-even.

These common facts are structural consequences of bipartiteness. They do not imply similarity.

---

## 3. The negative half of the theorem: the raw operators are different

v13.624 compares exact spectra, traces, determinants, kernel dimensions, and characteristic polynomials.

The SU(2) path has the exact uniformly spaced spectrum

[
oxed{
operatorname{spec}L_Y
=
{-2j,-2j+2,ldots,2j}.
}
]

At j=1/2 and j=1, low dimension forces accidental scalar-normalized spectral coincidences among connected paths.

The first genuine separation occurs at j=3/2:

[
operatorname{spec}L_Y={-3,-1,1,3},
]

while

[
chi_c(lambda)
=
lambda^4-rac{63}{2}lambda^2+rac{945}{16},
]

and

[
chi_a(lambda)
=
left(lambda^2-rac{315}{16}ight)
left(lambda^2-rac{27}{16}ight).
]

Therefore the positive spectral-magnitude ratio of (L_Y) is 3, whereas for (Q_a) it is

[
sqrt{rac{35}{3}},
]

and the Racah path has a third ratio.

Consequently, generically from j=3/2 onward,

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

No unitary equivalence exists, and no invertible raw-operator intertwiner exists. Scalar-rescaled similarity is also generically ruled out by scale-free spectral ratios.

This spectral inequivalence is essential: the later unification is not a disguised raw-operator equivalence.

---

## 4. Orientation flattening

For the real symmetric paths define on the nonzero sector

[
oxed{
R_Y=H,operatorname{sgn}(L_Y),
qquad
R_c=H,operatorname{sgn}(L_c).
}
]

For the Hermitian imaginary-antisymmetric volume path define

[
oxed{
R_a=-i,operatorname{sgn}(Q_a).
}
]

Each satisfies

[
R^2=-I,qquad
R^4=I,
]

and

[
HRH=R^{-1}=-R.
]

Thus each pair ((R,H)) is a real D8 representation on the nonzero sector.

The parity factor H in the symmetric cases is essential: (operatorname{sgn}(L_Y)) and (operatorname{sgn}(L_c)) are involutions, not quarter-turns.

---

## 5. Explicit parity-adapted normal form

Let (E_+) be the reflection-even part of the nonzero sector and choose any orthonormal basis

[
e_1,ldots,e_{N_j},
]

where

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

Then

[
Ho_r=-o_r,qquad
Ro_r=-e_r.
]

Therefore each plane

[
Pi_r=operatorname{span}{e_r,o_r}
]

carries exactly

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

Hence every nonzero carrier is

[
oxed{
mathcal H_{m nz}congho^{oplus N_j},
}
]

with (ho) the standard real two-dimensional D8 representation.

---

## 6. Explicit orthogonal intertwiner

For two flattened carriers A and B, choose parity-adapted bases and define

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

Then

[
U_{Bleftarrow A}^TU_{Bleftarrow A}=I,
]

and

[
oxed{
U_{Bleftarrow A}R_A=R_BU_{Bleftarrow A},
}
]

[
oxed{
U_{Bleftarrow A}H=HU_{Bleftarrow A}.
}
]

Thus

[
oxed{
(R_Y,H)simeq(R_c,H)simeq(R_a,H)
}
]

as real D8 representations after flattening.

---

## 7. Integer-j zero-line extension

For integer j, let (z_A) be the normalized reflection-even kernel vector:

[
Az_A=0,qquad Hz_A=z_A.
]

Let

[
P_{0,A}=|z_Aanglelangle z_A|.
]

Extend the quarter-turn by

[
oxed{
widetilde R_A=R_A+P_{0,A},
}
]

where (R_A) is zero on the kernel before the extension.

Then the zero line carries

[
widetilde R_Az_A=z_A,qquad Hz_A=z_A,
]

so it is the trivial D8 representation.

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

Therefore

[
oxed{
mathcal H_jcong
egin{cases}
mathbf1_{m zero}oplusho^{oplus j},
&jinmathbb Z,\\
ho^{oplus(j+1/2)},
&jinmathbb Z+rac12.
end{cases}}
]

The weight-dependent zero vectors differ, but they do not obstruct representation equivalence.

---

## 8. Nonuniqueness

The intertwiner is not a canonical physical identification.

If

[
Oin O(N_j),
]

rotate the reflection-even multiplicity basis by

[
e_r'=sum_sO_{sr}e_s.
]

Then automatically

[
Re_r'=sum_sO_{sr}Re_s.
]

The induced transformation is

[
Ootimes I_2,
]

which commutes with the canonical R and H blocks.

Thus, once the integer-j zero-line sign is fixed, the family of orthogonal D8 intertwiners has

[
oxed{O(N_j)}
]

multiplicity-space freedom.

For integer j, allowing reversal of the normalized zero vector adds an independent

[
O(1)={pm1}.
]

So the representation type is canonical; the cross-carrier physical map is not.

---

## 9. The synthesis theorem

### Theorem

For every equal spin j, the SU(2)/magnetic ladder path (L_Y), zero-diagonal crossed-Casimir Racah path (L_c), and tetrahedral oriented-volume path (Q_a) are three physically and spectrally distinct finite operators.

Generically from j=3/2 onward they are not similar, not unitarily equivalent, and admit no invertible raw-operator intertwiner.

Nevertheless, after orientation flattening, their parity pairs are orthogonally equivalent real D8 representations:

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

An explicit orthogonal intertwiner is obtained by choosing orthonormal bases of the reflection-even nonzero sectors, generating their odd partners by (o_r=Re_r), and mapping corresponding parity-adapted planes. For integer j, map the normalized even zero line separately.

The resulting intertwiner is unique only up to (O(N_j)) on the multiplicity space, together with an optional (O(1)) sign on the integer-j trivial zero line.

### Proof

The spectral-inequivalence statement is v13.624. The flattened D8 relations, parity-adapted basis construction, explicit orthogonal intertwiner, integer-j zero-line extension, and multiplicity-space nonuniqueness are v13.624 and v13.631. Combining those independently audited results gives the theorem. (square)

---

## 10. Interpretation

The result is a representation-theoretic unification:

[
oxed{
	ext{three distinct metric operators}
longrightarrow
	ext{one common flattened D8 skeleton}.
}
]

Spectral flattening removes the nonzero metric magnitudes that distinguish the operators while preserving the bipartite parity/orientation structure.

This is precisely why the positive result does not contradict the negative spectral comparison.

---

## 11. Required guardrails from the external audit checkpoint

1. This is not a claim of physical equivalence between spin-drive dynamics, Racah recoupling, and LQG tetrahedral-volume dynamics.
2. The spectral inequivalence of v13.624 explicitly rules out that stronger reading.
3. (L_c) is the zero-diagonal path extracted from (K_{23}^2), not the full crossed Casimir.
4. The flattened D8 intertwiner does not intertwine the raw physical operators.
5. The (O(N_j)) freedom means the theorem does not supply a canonical physical identification between the three carriers.
6. There is currently no established link between this result and the chi_-4/L-function thread.
7. There is currently no derived link between this closed result and the separate higher-order magnetic-driver perturbative thread.
8. In particular, any comparison to the E8 golden-ratio spin-chain physics associated with Coldea et al. remains an outside observation, not a result derived in this ledger.

## Closure status

Per the recommendation of v13.635, this synthesis note closes the present LQG/tetrahedron weighted-path/D8 sub-result.

Future work may use the theorem as a proved representation-theoretic input, but any stronger cross-thread or physical identification requires a new derivation rather than extrapolation from the common D8 skeleton.
