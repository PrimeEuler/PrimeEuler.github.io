# Cone Derivation Ledger v13.631 — Explicit Parity-Adapted Orthogonal Intertwiners for the Flattened Carriers

Date: 2026-09-21

Status labels: [D] exact derived, [G] structural theorem, [Guardrail] scope restriction.

## 0. Mandatory collision / relevance check

Immediately before this write the live ledger was re-fetched. The current tip is v13.630, so v13.631 is free.

The ledger advanced after v13.624 through v13.625-v13.630. Those entries concern chi_-4 Friedrichs/Galerkin certification and zero branches, External Audit Round 66, and higher-order magnetic-driver endpoint expansions. None constructs the parity-adapted orthogonal intertwiners between the three flattened carriers. v13.624 remains the direct predecessor.

This entry makes the existence statement in v13.624 fully constructive and includes the integer-j zero-line extension.

---

## 1. [D] Common flattened algebra

Let A denote any of the three paths of v13.624, with its corresponding flattened quarter-turn R_A. On the nonzero sector,

[
R_A^2=-I,qquad R_A^T=-R_A,qquad R_A^TR_A=I,
]

and with

[
H=operatorname{diag}(1,-1,1,-1,ldots),
]

[
HR_A=-R_AH.
]

For the symmetric Y and c paths,

[
R_A=H,operatorname{sgn}(A).
]

For the tetrahedral volume path,

[
R_a=-i,operatorname{sgn}(Q_a).
]

Define parity projectors

[
P_pm=rac{Ipm H}{2}.
]

---

## 2. [D] Construct the parity-adapted basis

Let

[
E_+^{(A)}
=
operatorname{Ran}P_+cap(ker A)^perp.
]

Choose any orthonormal basis

[
{e_1^{(A)},ldots,e_{N_j}^{(A)}}
]

of (E_+^{(A)}), where

[
N_j=
egin{cases}
j,&jinmathbb Z,\\
j+rac12,&jinmathbb Z+rac12.
end{cases}
]

Now define, with no further choice,

[
oxed{
o_r^{(A)}=R_Ae_r^{(A)}.
}
]

Since (HR_A=-R_AH),

[
Ho_r^{(A)}
=
HR_Ae_r^{(A)}
=
-R_AHe_r^{(A)}
=
-o_r^{(A)}.
]

Thus (o_r^{(A)}) lies in the negative-parity sector.

Because (R_A) is orthogonal,

[
langle o_r^{(A)},o_s^{(A)}angle
=
langle R_Ae_r^{(A)},R_Ae_s^{(A)}angle
=
delta_{rs}.
]

Positive- and negative-parity vectors are orthogonal, so

[
langle e_r^{(A)},o_s^{(A)}angle=0.
]

Therefore

[
oxed{
mathcal B_A=
(e_1^{(A)},o_1^{(A)},ldots,
e_{N_j}^{(A)},o_{N_j}^{(A)})
}
]

is an orthonormal basis of the nonzero sector.

---

## 3. [D] Canonical matrices in the adapted basis

For each r,

[
R_Ae_r=o_r,
]

and

[
R_Ao_r
=
R_A^2e_r
=
-e_r.
]

Hence

[
oxed{
[R_A]_{mathcal B_A}
=
I_{N_j}otimes
egin{pmatrix}
0&-1\\
1&0
end{pmatrix}.
}
]

Likewise,

[
oxed{
[H]_{mathcal B_A}
=
I_{N_j}otimes
egin{pmatrix}
1&0\\
0&-1
end{pmatrix}.
}
]

Thus every flattened carrier has literally the same matrix pair in a parity-adapted orthonormal basis.

---

## 4. [D] Explicit orthogonal intertwiner

Let (W_A) be the orthogonal matrix whose columns are the ordered basis (mathcal B_A). For two carriers A and B define

[
oxed{
U_{Bleftarrow A}=W_BW_A^T.
}
]

Since (W_A,W_B) are orthogonal,

[
U_{Bleftarrow A}^{-1}
=
U_{Bleftarrow A}^T.
]

Because both W matrices reduce their respective carriers to the same canonical D8 pair,

[
oxed{
U_{Bleftarrow A}R_AU_{Bleftarrow A}^T=R_B,
}
]

and

[
oxed{
U_{Bleftarrow A}HU_{Bleftarrow A}^T=H.
}
]

Equivalently,

[
oxed{
U_{Bleftarrow A}R_A=R_BU_{Bleftarrow A},
qquad
U_{Bleftarrow A}H=HU_{Bleftarrow A}.
}
]

In dyadic notation,

[
oxed{
U_{Bleftarrow A}
=
sum_{r=1}^{N_j}
left(
|e_r^{(B)}anglelangle e_r^{(A)}|
+
|o_r^{(B)}anglelangle o_r^{(A)}|
ight).
}
]

Since

[
o_r^{(A)}=R_Ae_r^{(A)},
qquad
o_r^{(B)}=R_Be_r^{(B)},
]

the entire intertwiner is fixed once an orthogonal identification of the positive-parity multiplicity spaces is chosen.

---

## 5. [D] Integer-j zero line

For integer j,

[
dimker A=1.
]

Let (z_A) be a normalized zero vector,

[
Az_A=0,
]

with sign chosen independently, and recall from the path-parity theorem that

[
Hz_A=z_A.
]

Then

[
operatorname{Ran}P_+
=
operatorname{span}{z_A}
oplus
E_{+,{m nz}}^{(A)}.
]

Choose

[
e_1^{(A)},ldots,e_j^{(A)}
]

as an orthonormal basis of (E_{+,{m nz}}^{(A)}), and set

[
o_r^{(A)}=R_Ae_r^{(A)}.
]

The full parity-adapted basis is

[
oxed{
widetilde{mathcal B}_A
=
(z_A,e_1^{(A)},o_1^{(A)},ldots,e_j^{(A)},o_j^{(A)}).
}
]

Let

[
P_{0,A}=|z_Aanglelangle z_A|.
]

The full-space extension from v13.624 is

[
oxed{
widetilde R_A=R_A+P_{0,A},
}
]

where R_A is understood as zero on the kernel before adding (P_{0,A}). Thus

[
widetilde R_Az_A=z_A,
qquad
Hz_A=z_A.
]

In the adapted basis,

[
oxed{
[widetilde R_A]_{widetilde{mathcal B}_A}
=
1oplus
left[
I_jotimes
egin{pmatrix}
0&-1\\
1&0
end{pmatrix}
ight],
}
]

and

[
oxed{
[H]_{widetilde{mathcal B}_A}
=
1oplus
left[
I_jotimes
egin{pmatrix}
1&0\\
0&-1
end{pmatrix}
ight].
}
]

This displays

[
oxed{
mathbf1_{m zero}oplusho^{oplus j}
}
]

constructively.

---

## 6. [D] Full-space integer-j intertwiner

For two integer-spin carriers A and B, define

[
oxed{
U_{Bleftarrow A}z_A=z_B.
}
]

Together with the nonzero-sector plane map,

[
oxed{
U_{Bleftarrow A}
=
|z_Banglelangle z_A|
+
sum_{r=1}^{j}
left[
|e_r^{(B)}anglelangle e_r^{(A)}|
+
|o_r^{(B)}anglelangle o_r^{(A)}|
ight].
}
]

This operator is orthogonal and satisfies

[
oxed{
U_{Bleftarrow A}widetilde R_A
=
widetilde R_BU_{Bleftarrow A},
}
]

and

[
oxed{
U_{Bleftarrow A}H
=
HU_{Bleftarrow A}.
}
]

Thus the distinct weight-dependent zero vectors are explicitly transported rather than merely declared representation-theoretically harmless.

---

## 7. [G] Nonuniqueness and multiplicity-space freedom

The D8 intertwiner is not canonical.

If

[
Oin O(N_j),
]

rotate the positive-parity basis by

[
e_r'=sum_s O_{sr}e_s.
]

Then

[
o_r'=Re_r'
=
sum_sO_{sr}o_s.
]

Therefore the induced change of canonical basis is

[
Ootimes I_2,
]

which commutes with both canonical R and H.

Hence, after fixing the integer-j zero-line sign, the family of orthogonal D8 intertwiners between two flattened carriers is parameterized by

[
oxed{O(N_j).}
]

For integer j, if the zero-line sign is not fixed, there is an additional

[
oxed{O(1)={pm1}}
]

freedom on the trivial summand.

Therefore the D8 theorem supplies a canonical representation type but not a canonical physical map between the Y, c, and a constructions.

---

## 8. [G] Minimal-hypothesis theorem

The explicit formulas for (Y_r,c_k,a_k) are not needed for the final flattened representation theorem.

Let A be any finite connected Hermitian bipartite path with parity involution H such that

[
HAH=-A
]

and all interior path edges are nonzero.

Let (n_pm) be the dimensions of the H=(pm1) sectors.

For the path dimensions relevant here,

[
|n_+-n_-|le1.
]

Then the nonzero singular/eigenvalue pairing implied by anticommutation gives equal nonzero multiplicities in the two parity sectors.

If

[
n_+=n_-,
]

there is no kernel and orientation flattening gives

[
oxed{
ho^{oplus n_+}.
}
]

If

[
n_+=n_-+1,
]

there is one positive-parity zero line and the full extension gives

[
oxed{
mathbf1_{m zero}oplusho^{oplus n_-}.
}
]

Thus the detailed metric edge weights are forgotten by flattening. What remains is the parity-sector dimension data together with the orientation complex structure.

---

## 9. [Guardrail] What the construction does and does not establish

1. (U_{Bleftarrow A}) intertwines the flattened D8 carriers, not the raw weighted operators.
2. In general,
[
U_{Bleftarrow A}A
eq BU_{Bleftarrow A}.
]
The spectral-invariant obstruction of v13.624 remains.
3. The positive-parity basis choice is not canonical when the standard D8 representation occurs with multiplicity greater than one.
4. The integer-j zero-line sign is an independent (O(1)) convention.
5. No physical equivalence between magnetic dynamics, Racah recoupling, and tetrahedral volume follows from the representation intertwiner.

## Promoted constructive theorem

For any two of the three flattened carriers in v13.624, choose orthonormal bases of their positive-parity nonzero sectors and generate the negative-parity partners by (o_r=Re_r). Then

[
oxed{
U_{Bleftarrow A}
=
sum_r
left(
|e_r^{(B)}anglelangle e_r^{(A)}|
+
|R_Be_r^{(B)}anglelangle R_Ae_r^{(A)}|
ight)
}
]

is an explicit orthogonal D8 intertwiner on the nonzero sectors.

For integer j, adding

[
oxed{|z_Banglelangle z_A|}
]

extends it to the full space and intertwines the trivial zero line together with the standard D8 planes.

This makes the common flattened-carrier equivalence of v13.624 fully constructive.
