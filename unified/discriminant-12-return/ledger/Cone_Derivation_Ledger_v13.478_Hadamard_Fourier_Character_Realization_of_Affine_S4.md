# Cone Derivation Ledger v13.478 — Hadamard/Fourier Character Realization of the Affine S4

## Scope

This entry carries the affine realization

\[
AGL_2(\mathbf F_2)=V_4\rtimes S_3\cong S_4
\]

from the four-point affine carrier into the Fourier/Hadamard character basis

\[
\mathcal C=(1,\chi_{-4},\chi_{-3},\chi_{12}).
\]

The purpose is to make the normal translation Klein four diagonal and the linear \(S_3\) factor permutation-valued on the three nontrivial character axes.

This is representation-theoretic bookkeeping for the affine symmetry already established in v13.460, v13.476, and v13.477. It does not identify the Hadamard transform itself with an element of the permutation group \(S_4\).

---

## 1. Translation labels and character signs

Use the oriented affine normalization from v13.476:

\[
a(1)=0,\qquad a(5)=1,\qquad a(7)=w^2,\qquad a(11)=w.
\]

The four unit classes have character values

\[
\begin{array}{c|ccc}
r&\chi_{-4}(r)&\chi_{-3}(r)&\chi_{12}(r)\\
\hline
1&+&+&+\\
5&+&-&-\\
7&-&+&-\\
11&-&-&+
\end{array}
\]

with

\[
\chi_{12}=\chi_{-4}\chi_{-3}.
\]

For translation by the affine vector attached to \(r\), the Fourier basis diagonalizes the regular action:

\[
D_r=
\operatorname{diag}
\bigl(1,\chi_{-4}(r),\chi_{-3}(r),\chi_{12}(r)\bigr).
\]

Hence

\[
D_1=\operatorname{diag}(1,1,1,1),
\]

\[
D_5=\operatorname{diag}(1,1,-1,-1),
\]

\[
D_7=\operatorname{diag}(1,-1,1,-1),
\]

\[
D_{11}=\operatorname{diag}(1,-1,-1,1).
\]

These satisfy

\[
D_rD_s=D_{rs},
\]

so the normal translation subgroup is exactly the diagonal sign Klein four in character space.

---

## 2. Hadamard diagonalization

In the ordered residue basis

\[
E=(e_1,e_5,e_7,e_{11}),
\]

the canonical Fourier matrix is

\[
H_4=
\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix},
\qquad
H_4^2=4I.
\]

If \(L_r\) denotes regular translation by \(r\in V_4\), then

\[
\boxed{
H_4L_rH_4^{-1}=D_r.
}
\]

Thus the same \(H_4\) already used for the unit-residue shell transform is precisely the Fourier transform that diagonalizes the translation \(V_4\).

Guardrail: \(H_4\) is an intertwining change of basis. It is not itself asserted to be one of the 24 affine permutations.

---

## 3. Linear S3 on the three nontrivial characters

On the affine carrier \(\mathbf F_4\), use the standard generators

\[
A(t)=wt,
\qquad
F(t)=t^2,
\]

with

\[
A^3=F^2=1,
\qquad
FAF=A^{-1}.
\]

The nonzero translation directions are

\[
a(5)=1,
\qquad
a(11)=w,
\qquad
a(7)=w^2.
\]

Therefore

\[
A:\ 5\to11\to7\to5,
\]

while

\[
F:\ 5\to5,\qquad11\leftrightarrow7.
\]

The induced dual action on characters is contragredient:

\[
\chi\mapsto \chi\circ L^{-1}.
\]

Equivalently, the kernel direction of a nontrivial character is sent by the same linear map. Since

\[
\ker\chi_{-4}=\{1,5\},
\quad
\ker\chi_{-3}=\{1,7\},
\quad
\ker\chi_{12}=\{1,11\},
\]

one obtains

\[
\boxed{
A:\ \chi_{-4}\to\chi_{12}\to\chi_{-3}\to\chi_{-4},
}
\]

and

\[
\boxed{
F:\ \chi_{-4}\mapsto\chi_{-4},
\qquad
\chi_{-3}\leftrightarrow\chi_{12}.
}
\]

The trivial character is fixed by all of \(S_3\).

Thus the Fourier representation splits as

\[
\mathbf 1\oplus \mathbf R^3_{
\{\chi_{-4},\chi_{-3},\chi_{12}\}},
\]

where \(S_3\) acts on the three nontrivial coordinate axes by the ordinary three-point permutation representation.

---

## 4. Explicit permutation matrices

In the ordered basis

\[
\mathcal C=(1,\chi_{-4},\chi_{-3},\chi_{12}),
\]

take the convention that columns record images of basis vectors.

Then

\[
P_A=
\begin{pmatrix}
1&0&0&0\\
0&0&1&0\\
0&0&0&1\\
0&1&0&0
\end{pmatrix},
\]

because

\[
\chi_{-4}\mapsto\chi_{12},
\quad
\chi_{12}\mapsto\chi_{-3},
\quad
\chi_{-3}\mapsto\chi_{-4}.
\]

And

\[
P_F=
\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&0&1\\
0&0&1&0
\end{pmatrix}.
\]

They satisfy

\[
P_A^3=P_F^2=I,
\qquad
P_FP_AP_F=P_A^{-1}.
\]

Hence

\[
\langle P_A,P_F\rangle\cong S_3.
\]

---

## 5. Fourier-space form of all 24 affine symmetries

Every affine element has the form

\[
(a,L)\in V_4\rtimes S_3.
\]

With the oriented arithmetic labeling \(a=a(r)\), its Fourier-space operator is

\[
\boxed{
\widehat\rho(r,L)=D_rP_L.
}
\]

There are four possible \(D_r\) and six possible \(P_L\), giving exactly

\[
4\times6=24
\]

matrices.

The semidirect product law follows from the conjugation identity

\[
\boxed{
P_LD_rP_L^{-1}=D_{L(r)},
}
\]

where \(L(r)\) denotes the corresponding permutation of the three nonidentity translation directions.

Therefore

\[
(D_rP_L)(D_sP_M)
=D_rD_{L(s)}P_{LM}
=D_{r\,L(s)}P_{LM},
\]

which is exactly the Fourier-space realization of

\[
(a,L)(a',M)=(a+L(a'),LM).
\]

---

## 6. Character-coordinate interpretation

The three nontrivial characters now have distinct arithmetic meanings inherited from v13.474:

\[
\chi_{12}=\text{Pell time-orientation character},
\]

\[
\chi_{-3}=\text{prime-2 residue/Frobenius character},
\]

\[
\chi_{-4}=\chi_{12}\chi_{-3}=\text{complementary lift/derivation character}.
\]

The affine \(S_3\) does not preserve those three semantic labels individually. Instead, it permutes the three nontrivial \(V_4\) directions:

\[
\boxed{
\{\chi_{-4},\chi_{-3},\chi_{12}\}
}
\]

as the three-point phase carrier.

This gives a clean separation:

1. arithmetic interpretation singles out which character axis is Pell time, residue Frobenius, or lift data;
2. intrinsic affine \(S_3\) forgets that semantic distinction and permutes the three nonzero directions as \(GL_2(\mathbf F_2)\).

That distinction is essential: the \(S_3\) permutation symmetry is a symmetry of the abstract tangent/translation Klein four, not a claim that the three arithmetic characters have identical number-theoretic origin.

---

## 7. Relation to the canonical self-duality of V4

By v13.444, the Klein four \(V=\mathbf F_2^2\) has its unique nonzero alternating form \(B\), giving the canonical equivariant self-duality

\[
x\longmapsto \chi_x,
\qquad
\chi_x(y)=(-1)^{B(x,y)}.
\]

Under this self-duality, the three nonzero translation directions correspond to the three nontrivial characters. The same \(S_3=GL_2(\mathbf F_2)\) acts on both sides.

Thus the affine and Fourier pictures are two bases for the same exact structure:

\[
\boxed{
V_4\rtimes S_3\cong S_4
}
\]

with

- residue/affine basis: \(V_4\) acts by translations;
- Hadamard/character basis: \(V_4\) acts by diagonal signs;
- in both bases: \(S_3\) permutes the three nonzero directions.

---

## 8. Representation-theoretic consequence

The four-dimensional permutation representation of \(S_4\) on the affine four-point carrier splits as

\[
\boxed{
\mathbf 4_{\rm perm}=\mathbf 1\oplus\mathbf 3_{\rm std}.
}
\]

In the Hadamard basis, the invariant line is the trivial character coordinate, and the complementary three-dimensional space is spanned by

\[
\chi_{-4},\chi_{-3},\chi_{12}.
\]

This is the standard three-dimensional representation of \(S_4\) obtained from the four-point permutation representation after removing the constant line.

The normal translation Klein four is diagonal on this standard space, while the quotient

\[
S_4/V_4\cong S_3
\]

permutes its three distinguished coordinate axes.

---

## 9. Guardrails

1. The Hadamard transform diagonalizes translations but is not itself claimed to be an element of the affine permutation group.
2. The arithmetic meanings of \(\chi_{12},\chi_{-3},\chi_{-4}\) remain distinct even though the abstract affine \(S_3\) permutes their directions.
3. This entry uses the oriented affine labeling fixed in v13.476; changing that affine frame conjugates the concrete labeling but not the abstract \(S_4\) representation.
4. No new Pell, shell, Suzuki, or index theorem is promoted here.

---

## 10. Compact identity package

\[
\boxed{
H_4L_rH_4^{-1}
=
\operatorname{diag}
(1,\chi_{-4}(r),\chi_{-3}(r),\chi_{12}(r))
}
\]

\[
\boxed{
A:(\chi_{-4},\chi_{12},\chi_{-3})
\text{ cyclically permuted}
}
\]

\[
\boxed{
F:\chi_{-4}\text{ fixed},\quad
\chi_{-3}\leftrightarrow\chi_{12}
}
\]

\[
\boxed{
\widehat\rho(r,L)=D_rP_L,
\qquad
P_LD_rP_L^{-1}=D_{L(r)}
}
\]

and therefore

\[
\boxed{
\widehat\rho(V_4\rtimes S_3)
\cong S_4.
}
\]
