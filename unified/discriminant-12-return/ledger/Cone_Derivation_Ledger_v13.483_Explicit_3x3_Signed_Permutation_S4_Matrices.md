# Cone Derivation Ledger v13.483 — Explicit 3x3 Signed-Permutation S4 Matrices

## Scope

Write the v13.478–v13.482 Hadamard action explicitly on the nontrivial character space
\[
W=\operatorname{span}\{e_4,e_3,e_{12}\}
=\operatorname{span}\{\chi_{-4},\chi_{-3},\chi_{12}\},
\]
verify the semidirect-product/S4 relations, and recover the characteristic polynomials for all five S4 conjugacy classes directly from 3x3 matrices.

All statements below are exact finite-dimensional linear algebra.

---

## 1. V4 sign matrices

In the ordered basis
\[
(e_4,e_3,e_{12})=(\chi_{-4},\chi_{-3},\chi_{12}),
\]
translation by \(r\in\{1,5,7,11\}\) acts as
\[
D_r=\operatorname{diag}(\chi_{-4}(r),\chi_{-3}(r),\chi_{12}(r)).
\]
Thus
\[
D_1=I_3,
\]
\[
\boxed{D_5=\begin{pmatrix}1&0&0\\0&-1&0\\0&0&-1\end{pmatrix}},
\]
\[
\boxed{D_7=\begin{pmatrix}-1&0&0\\0&1&0\\0&0&-1\end{pmatrix}},
\]
\[
\boxed{D_{11}=\begin{pmatrix}-1&0&0\\0&-1&0\\0&0&1\end{pmatrix}}.
\]

They satisfy
\[
D_5^2=D_7^2=D_{11}^2=I,
\]
\[
D_5D_7=D_{11},\qquad D_7D_{11}=D_5,\qquad D_{11}D_5=D_7,
\]
and commute pairwise. Hence
\[
\boxed{\langle D_5,D_7\rangle\cong V_4.}
\]
All have determinant +1.

---

## 2. S3 generator matrices

Use the v13.478 convention
\[
A:e_4\mapsto e_{12}\mapsto e_3\mapsto e_4,
\]
and
\[
F:e_4\mapsto e_4,\qquad e_3\leftrightarrow e_{12}.
\]
With columns equal to images of basis vectors,
\[
\boxed{P_A=
\begin{pmatrix}
0&1&0\\
0&0&1\\
1&0&0
\end{pmatrix}},
\]
\[
\boxed{P_F=
\begin{pmatrix}
1&0&0\\
0&0&1\\
0&1&0
\end{pmatrix}}.
\]

Then
\[
P_A^3=I,
\qquad
P_F^2=I,
\qquad
\boxed{P_FP_AP_F=P_A^{-1}=P_A^2}.
\]
Therefore
\[
\boxed{\langle P_A,P_F\rangle\cong S_3.}
\]

The other reflections are
\[
P_{AF}=P_AP_F,
\qquad
P_{A^2F}=P_A^2P_F.
\]
They fix respectively
\[
e_{12},\qquad e_3,
\]
while \(F\) fixes \(e_4\).

---

## 3. Semidirect conjugation action

Conjugation by \(P_A\) cycles the three nonidentity V4 matrices:
\[
\boxed{P_AD_5P_A^{-1}=D_7,\quad
P_AD_7P_A^{-1}=D_{11},\quad
P_AD_{11}P_A^{-1}=D_5.}
\]

Conjugation by \(P_F\) fixes the sign flip whose +1 axis is \(e_4\), and swaps the other two:
\[
\boxed{P_FD_5P_F^{-1}=D_5,\quad
P_FD_7P_F^{-1}=D_{11},\quad
P_FD_{11}P_F^{-1}=D_7.}
\]

Thus the S3 factor acts faithfully as
\[
\operatorname{Aut}(V_4)\cong S_3,
\]
and
\[
\boxed{\langle D_5,D_7,P_A,P_F\rangle\cong V_4\rtimes S_3\cong S_4.}
\]
The resulting 3-dimensional representation is the standard irreducible representation of S4.

---

## 4. Useful S4 presentation inside the matrices

Take
\[
s=P_F,
\qquad
t=D_7P_F.
\]
Because \(F\) swaps \(D_7\leftrightarrow D_{11}\),
\[
t^2=D_7D_{11}=D_5\ne I,
\]
and
\[
t^4=I.
\]
Thus \(t\) is a 4-cycle class element, whereas \(s\) is a transposition class element.

A standard Coxeter realization is obtained by selecting three transposition-class signed permutation matrices corresponding to adjacent transpositions in the tetrahedral S4 action; equivalently the full generated group has order 24 and satisfies the semidirect relations above. The semidirect presentation is the most transparent one for the arithmetic character coordinates.

---

## 5. General 3x3 matrix

For
\[
(r,L)\in V_4\rtimes S_3,
\]
the nontrivial Hadamard block is simply
\[
\boxed{M(r,L)=D_rP_L.}
\]
The full 1+3 representation is
\[
\rho(r,L)=1\oplus M(r,L).
\]
Hence
\[
p_{1\oplus3}(x)=(x-1)p_3(x),
\qquad
p_3(x)=\det(xI_3-M(r,L)).
\]

---

## 6. Class 1^4: identity

Representative:
\[
M(1,I)=I_3.
\]
Therefore
\[
\boxed{p_3(x)=(x-1)^3},
\]
with eigenvalues
\[
\{1,1,1\},
\]
trace 3.

Full polynomial:
\[
\boxed{p_4(x)=(x-1)^4.}
\]

---

## 7. Class 2^2: nonzero V4 translations

Representative:
\[
D_5=\operatorname{diag}(1,-1,-1).
\]
Hence
\[
\boxed{p_3(x)=(x-1)(x+1)^2},
\]
eigenvalues
\[
\{1,-1,-1\},
\]
trace -1.

Full polynomial:
\[
\boxed{p_4(x)=(x-1)^2(x+1)^2.}
\]

The same holds for \(D_7,D_{11}\).

---

## 8. Class 3 1: rotation sector

Representative:
\[
P_A=
\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix}.
\]
Its characteristic polynomial is
\[
\boxed{p_3(x)=x^3-1=(x-1)(x^2+x+1)}.
\]
Eigenvalues:
\[
\{1,\omega,\omega^2\},
\]
trace 0.

For a signed representative \(D_rP_A\), the product of signs around the 3-cycle is
\[
\chi_{-4}(r)\chi_{-3}(r)\chi_{12}(r)=1,
\]
so the same polynomial holds for all eight elements in the A and A^2 cosets.

Full polynomial:
\[
\boxed{p_4(x)=(x-1)^2(x^2+x+1).}
\]

---

## 9. Class 2 1^2: reflection with positive fixed-axis sign

Representative:
\[
P_F=
\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}.
\]
Then
\[
\boxed{p_3(x)=(x-1)^2(x+1)},
\]
eigenvalues
\[
\{1,1,-1\},
\]
trace 1.

More generally, if reflection \(L\) fixes character axis \(e_f\), and
\[
c_f=\chi_f(r)=+1,
\]
then \(D_rP_L\) has this same polynomial.

Full polynomial:
\[
\boxed{p_4(x)=(x-1)^3(x+1).}
\]

---

## 10. Class 4: reflection with negative fixed-axis sign

Take the F reflection, whose fixed character is \(e_4\), and choose \(r=7\), for which \(\chi_{-4}(7)=-1\):
\[
M(7,F)=D_7P_F
=
\boxed{\begin{pmatrix}
-1&0&0\\
0&0&1\\
0&-1&0
\end{pmatrix}}.
\]

The lower 2x2 block squares to \(-I_2\), so its eigenvalues are \(i,-i\). Therefore
\[
\boxed{p_3(x)=(x+1)(x^2+1)},
\]
eigenvalues
\[
\{-1,i,-i\},
\]
trace -1.

Full polynomial:
\[
\boxed{p_4(x)=(x-1)(x+1)(x^2+1)=x^4-1.}
\]

Also
\[
M(7,F)^4=I,
\qquad
M(7,F)^2=D_5,
\]
so its square is the corresponding double transposition, exactly as for a 4-cycle in S4.

---

## 11. Five-class matrix summary

\[
\boxed{
\begin{array}{c|c|c|c}
S_4\text{ class}&3\times3\text{ representative}&p_3(x)&\operatorname{tr}_3\\ \hline
1^4&I&(x-1)^3&3\\
2\,1^2&P_F&(x-1)^2(x+1)&1\\
2^2&D_5&(x-1)(x+1)^2&-1\\
3\,1&P_A&(x-1)(x^2+x+1)&0\\
4&D_7P_F&(x+1)(x^2+1)&-1
\end{array}}
\]

Multiplying each polynomial by \((x-1)\) recovers the full v13.479/v13.482 1+3 characteristic polynomials.

---

## 12. Determinant and parity

The determinants are
\[
\det D_r=+1
\]
for all translations,
\[
\det P_A=+1,
\qquad
\det P_F=-1.
\]
Thus
\[
\boxed{\det M(r,L)=\operatorname{sgn}(L)=\operatorname{sgn}_{S_4}(r,L),}
\]
since the normal V4 consists entirely of even permutations.

So the standard 3-dimensional determinant is exactly the S4 sign character.

---

## 13. Geometric reading

The matrices are orthogonal signed permutation matrices. The three V4 elements are 180-degree rotations about the three coordinate axes:
\[
D_5=\operatorname{diag}(1,-1,-1),
\]
and cyclic permutations thereof.

The S3 subgroup permutes those three coordinate axes. Therefore this 3x3 realization is the tetrahedral standard representation of S4, written in the arithmetic Hadamard character coordinates
\[
(\chi_{-4},\chi_{-3},\chi_{12}).
\]

This makes the A3/tetrahedral model explicit at the matrix level, while retaining the guardrail that the three axes have distinct arithmetic meanings in discriminant 12.