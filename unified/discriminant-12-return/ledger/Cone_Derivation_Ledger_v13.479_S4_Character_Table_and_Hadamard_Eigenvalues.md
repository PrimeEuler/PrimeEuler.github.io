# Cone Derivation Ledger v13.479 — S4 Character Table and Hadamard Eigenvalues

## Purpose

Compute the character and eigenvalue data of the four-dimensional Hadamard/Fourier realization of the affine group

\[
AGL_2(\mathbf F_2)=V_4\rtimes S_3\cong S_4,
\]

using the decomposition

\[
\mathbf 4_{\rm perm}\cong \mathbf 1\oplus \mathbf 3_{\rm std}.
\]

The Hadamard basis is

\[
(1,\chi_{-4},\chi_{-3},\chi_{12}),
\]

with the first line invariant and the remaining three-dimensional subspace carrying the standard representation of \(S_4\).

---

## 1. Conjugacy classes of S4

The five conjugacy classes are indexed by cycle type:

\[
1^4,\qquad 2\,1^2,\qquad 2^2,\qquad 3\,1,\qquad 4,
\]

with class sizes

\[
1,\qquad 6,\qquad 3,\qquad 8,\qquad 6.
\]

For the four-point permutation representation, the character equals the number of fixed points. Hence

\[
\boxed{\chi_{1\oplus3}=(4,2,0,1,0).}
\]

Since the trivial constituent contributes \(1\) on every class,

\[
\boxed{\chi_3=\chi_{1\oplus3}-1=(3,1,-1,0,-1).}
\]

---

## 2. Eigenvalues in the four-dimensional representation

Let \(\omega=e^{2\pi i/3}\). For a permutation matrix, each cycle of length \(m\) contributes the \(m\)-th roots of unity as eigenvalues.

### Identity \(1^4\)

\[
\operatorname{Spec}_{4}=(1,1,1,1),
\qquad \operatorname{tr}_{4}=4.
\]

After removing the invariant line:

\[
\operatorname{Spec}_{3}=(1,1,1),
\qquad \operatorname{tr}_{3}=3.
\]

### Transposition \(2\,1^2\)

\[
\operatorname{Spec}_{4}=(1,1,1,-1),
\qquad \operatorname{tr}_{4}=2.
\]

Thus

\[
\operatorname{Spec}_{3}=(1,1,-1),
\qquad \operatorname{tr}_{3}=1.
\]

### Double transposition \(2^2\)

\[
\operatorname{Spec}_{4}=(1,1,-1,-1),
\qquad \operatorname{tr}_{4}=0.
\]

Thus

\[
\operatorname{Spec}_{3}=(1,-1,-1),
\qquad \operatorname{tr}_{3}=-1.
\]

### Three-cycle \(3\,1\)

\[
\operatorname{Spec}_{4}=(1,1,\omega,\omega^2),
\qquad \operatorname{tr}_{4}=1,
\]

because \(1+\omega+\omega^2=0\). Hence

\[
\operatorname{Spec}_{3}=(1,\omega,\omega^2),
\qquad \operatorname{tr}_{3}=0.
\]

### Four-cycle \(4\)

\[
\operatorname{Spec}_{4}=(1,i,-1,-i),
\qquad \operatorname{tr}_{4}=0.
\]

Removing the invariant eigenvalue \(1\):

\[
\operatorname{Spec}_{3}=(i,-1,-i),
\qquad \operatorname{tr}_{3}=-1.
\]

---

## 3. Character/eigenvalue table

| cycle type | class size | order | eigenvalues on \(1\oplus3\) | \(\chi_{1\oplus3}\) | eigenvalues on \(3_{\rm std}\) | \(\chi_3\) |
|---|---:|---:|---|---:|---|---:|
| \(1^4\) | 1 | 1 | \(1,1,1,1\) | 4 | \(1,1,1\) | 3 |
| \(2\,1^2\) | 6 | 2 | \(1,1,1,-1\) | 2 | \(1,1,-1\) | 1 |
| \(2^2\) | 3 | 2 | \(1,1,-1,-1\) | 0 | \(1,-1,-1\) | -1 |
| \(3\,1\) | 8 | 3 | \(1,1,\omega,\omega^2\) | 1 | \(1,\omega,\omega^2\) | 0 |
| \(4\) | 6 | 4 | \(1,i,-1,-i\) | 0 | \(i,-1,-i\) | -1 |

---

## 4. Full irreducible S4 character table for context

Using the same class order

\[
(1^4,\ 2\,1^2,\ 2^2,\ 3\,1,\ 4),
\]

the irreducible character table is

| irrep | dim | \(1^4\) | \(2\,1^2\) | \(2^2\) | \(3\,1\) | \(4\) |
|---|---:|---:|---:|---:|---:|---:|
| trivial \([4]\) | 1 | 1 | 1 | 1 | 1 | 1 |
| standard \([31]\) | 3 | 3 | 1 | -1 | 0 | -1 |
| \([22]\) | 2 | 2 | 0 | 2 | -1 | 0 |
| standard\(\otimes\)sign \([211]\) | 3 | 3 | -1 | -1 | 0 | 1 |
| sign \([1111]\) | 1 | 1 | -1 | 1 | 1 | -1 |

Therefore the Hadamard representation has character

\[
\chi_H=\chi_{[4]}+\chi_{[31]},
\]

namely

\[
\boxed{\chi_H=(4,2,0,1,0).}
\]

---

## 5. Determinants on the standard three-space

The determinant on \(3_{\rm std}\) equals the sign character:

\[
\det \rho_3(g)=\operatorname{sgn}(g).
\]

Indeed:

- identity: \(+1\),
- transposition: \(-1\),
- double transposition: \(+1\),
- three-cycle: \(+1\),
- four-cycle: \(-1\).

This follows immediately from the listed eigenvalues.

---

## 6. Character-polynomial relation

If \(X_1(g)\) denotes the number of fixed points of \(g\) in its natural action on four letters, then

\[
\boxed{\chi_H(g)=X_1(g)}
\]

and

\[
\boxed{\chi_3(g)=X_1(g)-1.}
\]

This gives the class values without choosing coordinates.

---

## 7. Relation to the discriminant-12 Hadamard basis

In the character basis

\[
(1,\chi_{-4},\chi_{-3},\chi_{12}),
\]

the invariant line \(\mathbf C\cdot 1\) is the trivial representation, while

\[
W=\operatorname{span}\{\chi_{-4},\chi_{-3},\chi_{12}\}
\]

carries \(3_{\rm std}\).

Thus the three arithmetic directions

\[
\chi_{-4},\qquad \chi_{-3},\qquad \chi_{12}
\]

are not three separate one-dimensional \(S_4\)-subrepresentations. They are the three distinguished Hadamard axes inside one irreducible three-dimensional standard module. The affine \(S_3\) permutes these axes, while translations contribute the diagonal character signs from v13.478.

This preserves the arithmetic guardrail: the meanings

\[
\chi_{12}=\text{Pell time},\qquad
\chi_{-3}=\text{residue Frobenius},\qquad
\chi_{-4}=\text{mod-4 lift/derivation}
\]

remain distinct even though the abstract affine symmetry permutes the three corresponding directions.

---

## 8. Exact conclusion

The discriminant-12 affine/Hadamard realization of \(S_4\) is the natural four-point permutation representation, decomposed by Hadamard transform as

\[
\boxed{\mathbf4_{\rm perm}=\mathbf1\oplus\mathbf3_{\rm std}.}
\]

Its class character is

\[
\boxed{(4,2,0,1,0),}
\]

and the nontrivial Hadamard three-space has character

\[
\boxed{(3,1,-1,0,-1).}
\]

The complete eigenvalue data are exactly those listed in Section 3.
