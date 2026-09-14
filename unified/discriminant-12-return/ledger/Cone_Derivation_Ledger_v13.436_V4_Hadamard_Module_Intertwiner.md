# Cone Derivation Ledger v13.436 — V4 Hadamard Module Intertwiner

Date: 2026-09-14

Status labels: **[D]** exact derived; **[I]** interpretation; **[Audit]** guardrail.

## 0. Synchronization [Audit]

This checkpoint was assigned only after checking the live ledger through `v13.435` (External Audit Round 31). That audit independently verified the recent `v13.430`–`v13.434` chain, including the cyclotomic zeta intertwiner graph and the all-character `H_4` transform. The same audit also independently re-executed and confirmed the certified finite-high positivity closure recorded in `v13.434`.

## 1. Regular V4 residue module and Hadamard diagonalization [D]

Let

\[
G=U(12)=\{1,5,7,11\}\cong V_4,
\]

and let

\[
E=(e_1,e_5,e_7,e_{11})
\]

be the standard basis of the rational regular module \(\mathbf Q[G]\). For \(s\in G\), let \(L_s\) denote left translation,

\[
L_s e_r=e_{sr}.
\]

Order the four real characters as

\[
(\mathbf 1,\chi_{-4},\chi_{-3},\chi_{12}),
\]

and define the character table

\[
H_4=
\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix},
\qquad H_4^2=4I.
\]

If \(x\) is a residue-coordinate column and

\[
c=H_4x,
\]

then for every \(s\in G\),

\[
\boxed{
H_4L_sH_4^{-1}
=
\operatorname{diag}
\bigl(
1,\chi_{-4}(s),\chi_{-3}(s),\chi_{12}(s)
\bigr).
}
\]

Thus the same `H_4` already used in the shell-displacement Fourier transform is exactly the diagonalizing matrix for the regular \(V_4\) action.

## 2. Cyclotomic field as the same rational V4-module [D]

Let

\[
K=\mathbf Q(\zeta_{12})=\mathbf Q(\sqrt3,i),
\]

with Galois action

\[
\sigma_s(\zeta_{12})=\zeta_{12}^s.
\]

From `v13.421`, the four one-dimensional character lines are

\[
L_{\mathbf1}=\mathbf Q\cdot1,
\qquad
L_{-4}=\mathbf Q\cdot i,
\qquad
L_{-3}=\mathbf Q\cdot i\sqrt3,
\qquad
L_{12}=\mathbf Q\cdot\sqrt3.
\]

In the ordered character basis

\[
B_\chi=(1,i,i\sqrt3,\sqrt3),
\]

one has

\[
[\sigma_s]_{B_\chi}
=
\operatorname{diag}
\bigl(
1,\chi_{-4}(s),\chi_{-3}(s),\chi_{12}(s)
\bigr).
\]

Therefore

\[
\boxed{
K\cong_{\mathbf Q[V_4]} \mathbf Q[V_4]
}
\]

as rational \(V_4\)-modules: both contain each of the four rational characters exactly once.

An explicit intertwiner is obtained by first applying the Hadamard transform to residue coordinates and then interpreting the four character coordinates along the four cyclotomic character lines:

\[
\boxed{
\mathcal T(x_1,x_5,x_7,x_{11})^T
=
 c_{\mathbf1}\,1
+c_{-4}\,i
+c_{-3}\,i\sqrt3
+c_{12}\,\sqrt3,
\qquad
c=H_4x.
}
\]

It satisfies

\[
\boxed{
\mathcal T\,L_s
=
\sigma_s\,\mathcal T
\qquad(s\in V_4).
}
\]

This is an exact representation-theoretic bridge between residue-sector Fourier coordinates and the cyclotomic Galois module.

## 3. Guardrail: module isomorphism, not ring or geometric identification [Audit]

The map \(\mathcal T\) is a \(\mathbf Q[V_4]\)-module isomorphism after choosing the displayed scalings of the four character lines. It is **not** asserted to be

- a ring isomorphism \(\mathbf Q[V_4]\to K\),
- an integral isomorphism \(\mathbf Z[V_4]\to\mathcal O_K\),
- a map from the four geometric Cone shells into field elements,
- or an action of the Pell matrix on divisor-sector coordinates.

The exact common object is the semisimple rational \(V_4\)-representation and its character decomposition.

## 4. Zeta multiplication in the character basis [D]

From `v13.431`, for

\[
\mathcal Z=\times\zeta_{12},
\qquad
\zeta_{12}=\frac{\sqrt3+i}{2},
\]

one has in \(B_\chi\)

\[
[\mathcal Z]_{B_\chi}
=
\begin{pmatrix}
0&-\frac12&0&\frac32\\
\frac12&0&\frac32&0\\
0&\frac12&0&\frac12\\
\frac12&0&-\frac12&0
\end{pmatrix}.
\]

Reorder the character basis by \(\chi_{-3}\)-parity:

\[
B_{\rm par}
=(1,i\sqrt3\mid i,\sqrt3)
=(\mathbf1,\chi_{-3}\mid\chi_{-4},\chi_{12}).
\]

Then

\[
\boxed{
[\mathcal Z]_{B_{\rm par}}
=
\begin{pmatrix}
0&A\\
B&0
\end{pmatrix},
}
\]

with

\[
A=
\begin{pmatrix}
-\frac12&\frac32\\
\frac12&\frac12
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
\frac12&\frac32\\
\frac12&-\frac12
\end{pmatrix}.
\]

Thus \(\mathcal Z\) is exactly off-diagonal with respect to the parity splitting

\[
\boxed{
K
=
(L_{\mathbf1}\oplus L_{-3})
\oplus
(L_{-4}\oplus L_{12}).
}
\]

Equivalently,

\[
\boxed{
\mathcal Z:
K_+\leftrightarrow K_-,
\qquad
K_+=L_{\mathbf1}\oplus L_{-3},
\quad
K_-=L_{-4}\oplus L_{12}.
}
\]

This is the operator-level version of the `K_{2,2}` support graph recorded in `v13.431`.

## 5. Even and odd powers [D]

Squaring the block matrix gives

\[
[\mathcal Z^2]_{B_{\rm par}}
=
\begin{pmatrix}
AB&0\\
0&BA
\end{pmatrix}
=
\begin{pmatrix}
\frac12&-\frac32&0&0\\
\frac12&\frac12&0&0\\
0&0&\frac12&\frac32\\
0&0&-\frac12&\frac12
\end{pmatrix}.
\]

Hence every even power preserves the two \(\chi_{-3}\)-parity halves, while every odd power exchanges them.

At the cubic step,

\[
\mathcal Z^3=\times i,
\]

and in the parity basis

\[
\boxed{
[\mathcal Z^3]_{B_{\rm par}}
=
\begin{pmatrix}
0&0&-1&0\\
0&0&0&1\\
1&0&0&0\\
0&-1&0&0
\end{pmatrix},
}
\]

a signed permutation matrix. Finally,

\[
\boxed{\mathcal Z^6=-I,\qquad \mathcal Z^{12}=I.}
\]

## 6. One exact diagram joining the two Hadamard appearances [D/I]

There are now two rigorously distinct but representation-theoretically equivalent appearances of the same character table:

\[
\boxed{
\begin{array}{ccc}
\text{residue / unit-core coordinates}
&\xrightarrow{\ H_4\ }&
\text{character coordinates}\\[1mm]
\Big\downarrow L_s&&\Big\downarrow \operatorname{diag}(\chi(s))\\[1mm]
\text{residue / unit-core coordinates}
&\xrightarrow{\ H_4\ }&
\text{character coordinates}
\end{array}}
\]

and

\[
\boxed{
\begin{array}{ccc}
\mathbf Q[V_4]
&\xrightarrow{\ \mathcal T\ }&
\mathbf Q(\zeta_{12})\\[1mm]
\Big\downarrow L_s&&\Big\downarrow\sigma_s\\[1mm]
\mathbf Q[V_4]
&\xrightarrow{\ \mathcal T\ }&
\mathbf Q(\zeta_{12}).
\end{array}}
\]

The shell-displacement `H_4` transform of `v13.430` is therefore not merely numerically the same Hadamard matrix as the cyclotomic character decomposition: both are instances of the Fourier transform of the same finite group \(V_4\).

The new ingredient supplied by the cyclotomic carrier is the non-Galois operator \(\mathcal Z\), which is off-diagonal in the Galois-character basis and intertwines the two \(\chi_{-3}\)-parity halves.

## 7. Relation to the finite-field layer [I/Audit]

The parity character singled out by the off-diagonal decomposition is \(\chi_{-3}\), exactly the character that survives as the identity/Frobenius dichotomy on the ramified residue field \(\mathbf F_4\) in `v13.416`.

This gives the exact chain of compatible labels

\[
\boxed{
\chi_{-3}
:\quad
\text{cyclotomic zeta parity}
\longleftrightarrow
\text{residue-field Galois/Frobenius parity}.
}
\]

**[Audit]** This is compatibility of character labels and operator parity. It does not identify \(\mathcal Z\) over characteristic zero with Frobenius in characteristic two.

## 8. Next exact target

The next natural calculation is to reduce the off-diagonal \(\mathcal Z\) structure modulo the ramified prime and determine exactly how its two-block characteristic-zero action collapses to literal multiplication by \(\omega\) on \(\mathbf F_4\), while the Galois \(\chi_{-3}\) parity becomes Frobenius. The target is a commuting/semilinear diagram that simultaneously displays

\[
\times\zeta_{12}\to\times\omega,
\qquad
\sigma_{5,11}\to\mathrm{Fr},
\]

without conflating multiplication with Galois action.

---

**Checkpoint conclusion.** The shell/residue Hadamard transform and the cyclotomic Galois character decomposition are exactly the same rational \(V_4\) Fourier decomposition on two different carriers. The explicit intertwiner \(\mathcal T\) makes that equivalence precise. In the resulting character basis, cyclotomic multiplication by \(\zeta_{12}\) is an exact off-diagonal operator exchanging the two \(\chi_{-3}\)-parity halves; even powers preserve the halves, odd powers exchange them, \(\mathcal Z^3\) is a signed permutation, and \(\mathcal Z^6=-I\).