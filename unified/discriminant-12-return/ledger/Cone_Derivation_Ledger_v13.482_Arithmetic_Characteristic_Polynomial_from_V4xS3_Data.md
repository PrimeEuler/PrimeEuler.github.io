# Cone Derivation Ledger v13.482 — Arithmetic Characteristic Polynomial from V4 x S3 Data

## Scope

Continue v13.476–v13.481 by deriving the characteristic polynomial, order, and Hadamard spectrum of an affine element directly from its arithmetic pair

\[
(r,L)\in V_4\rtimes S_3,
\]

without first expanding its permutation on the four affine points.

This is an exact finite-group calculation. It introduces no shell/Suzuki theorem.

---

## 1. Character coordinates for the translation part

For
\[
r\in U(12)=\{1,5,7,11\},
\]
write
\[
(c_4,c_3,c_{12})=
(\chi_{-4}(r),\chi_{-3}(r),\chi_{12}(r)).
\]

The four possibilities are

\[
\begin{array}{c|ccc}
r&c_4&c_3&c_{12}\\ \hline
1&+1&+1&+1\\
5&+1&-1&-1\\
7&-1&+1&-1\\
11&-1&-1&+1
\end{array}
\]

and always
\[
c_4c_3c_{12}=1.
\]

In the Hadamard basis
\[
(1,\chi_{-4},\chi_{-3},\chi_{12}),
\]
translation by \(r\) is
\[
D_r=\operatorname{diag}(1,c_4,c_3,c_{12}).
\]

For a linear phase element \(L\in S_3\), let \(P_L\) be its permutation matrix on the three nontrivial character axes. Then
\[
\boxed{\rho(r,L)=D_rP_L.}
\]

Thus the full spectral problem is a signed permutation problem on three axes, plus the invariant trivial line.

---

## 2. Identity linear sector

For \(L=I\),
\[
\rho(r,I)=\operatorname{diag}(1,c_4,c_3,c_{12}),
\]
so
\[
\boxed{p_{r,I}(x)=(x-1)(x-c_4)(x-c_3)(x-c_{12}).}
\]

Hence:

- \(r=1\):
  \[
  p(x)=(x-1)^4,
  \]
  class \(1^4\), order 1.

- \(r\ne1\): exactly one of \(c_4,c_3,c_{12}\) is \(+1\) and two are \(-1\), so
  \[
  \boxed{p(x)=(x-1)^2(x+1)^2,}
  \]
  class \(2^2\), order 2.

This recovers the identity plus the three double transpositions.

---

## 3. Rotation sector: \(L=A,A^2\)

The linear rotation cyclically permutes the three nontrivial character axes. The signed 3-cycle block has characteristic polynomial
\[
x^3-c_4c_3c_{12}.
\]
Since
\[
c_4c_3c_{12}=1,
\]
we obtain for every \(r\in V_4\):
\[
\boxed{p_{r,A}(x)=p_{r,A^2}(x)=(x-1)(x^3-1).}
\]
Equivalently,
\[
\boxed{p(x)=(x-1)^2(x^2+x+1).}
\]

Therefore all eight elements in the two rotation cosets have eigenvalues
\[
\boxed{\{1,1,\omega,\omega^2\}},
\]
trace 1, class \(3\,1\), and order 3.

This gives an arithmetic explanation for the entire eight-element 3-cycle class: the only sign invariant around the 3-cycle is the product
\[
\chi_{-4}(r)\chi_{-3}(r)\chi_{12}(r)=1.
\]

---

## 4. Reflection sector

Let \(L\) be one of the three reflections in \(S_3\). It fixes one nontrivial character axis, call its character \(\chi_f\), and swaps the other two.

Write
\[
c_f=\chi_f(r)\in\{\pm1\}.
\]
Because the product of all three signs is 1, the product of the two swapped signs is also
\[
c_sc_t=c_f.
\]

On the fixed character axis the eigenvalue is \(c_f\). On the swapped two-plane, the signed transposition block squares to \(c_fI\), hence has characteristic polynomial
\[
x^2-c_f.
\]
Therefore the full characteristic polynomial is
\[
\boxed{p_{r,L}(x)=(x-1)(x-c_f)(x^2-c_f).}
\]

This single formula separates the two reflection-sector conjugacy classes.

### Case 4a: \(c_f=+1\)

Then
\[
\boxed{p(x)=(x-1)^3(x+1),}
\]
with eigenvalues
\[
\{1,1,1,-1\}.
\]
Hence the element is a transposition, trace 2, order 2.

### Case 4b: \(c_f=-1\)

Then
\[
\boxed{p(x)=(x-1)(x+1)(x^2+1)=x^4-1,}
\]
with eigenvalues
\[
\{1,-1,i,-i\}.
\]
Hence the element is a 4-cycle, trace 0, order 4.

So:
\[
\boxed{\text{reflection coset class is decided by one character sign }\chi_f(r).}
\]

This is the desired arithmetic class test.

---

## 5. Which character is fixed by each reflection?

Using the v13.478 convention
\[
A:\chi_{-4}\to\chi_{12}\to\chi_{-3}\to\chi_{-4},
\]
\[
F:\chi_{-4}\mapsto\chi_{-4},\qquad
\chi_{-3}\leftrightarrow\chi_{12},
\]
we have:

\[
\begin{array}{c|c|c}
L&\text{fixed character}&\text{class test}\\ \hline
F&\chi_{-4}&\chi_{-4}(r)=+1\Rightarrow 2\,1^2;\ -1\Rightarrow4\\
AF&\chi_{12}&\chi_{12}(r)=+1\Rightarrow 2\,1^2;\ -1\Rightarrow4\\
A^2F&\chi_{-3}&\chi_{-3}(r)=+1\Rightarrow 2\,1^2;\ -1\Rightarrow4
\end{array}
\]

Each nontrivial character has two \(+1\) and two \(-1\) values on \(V_4\). Consequently each reflection coset contains exactly two transpositions and two 4-cycles. Across three reflection cosets this gives
\[
6+6.
\]

---

## 6. Complete arithmetic classifier

For \((r,L)\in V_4\rtimes S_3\):

\[
\boxed{
\begin{array}{c|c|c|c}
L&\text{condition}&\text{S4 class}&p_{r,L}(x)\\ \hline
I&r=1&1^4&(x-1)^4\\
I&r\ne1&2^2&(x-1)^2(x+1)^2\\
A,A^2&\text{all }r&3\,1&(x-1)^2(x^2+x+1)\\
\text{reflection}&\chi_f(r)=+1&2\,1^2&(x-1)^3(x+1)\\
\text{reflection}&\chi_f(r)=-1&4&(x-1)(x+1)(x^2+1)
\end{array}}
\]

Thus the conjugacy class, order, trace, and complete Hadamard spectrum are recoverable directly from:

1. the \(S_3\) type of \(L\), and
2. for reflections only, the single arithmetic character value on the character axis fixed by \(L\).

No four-point permutation expansion is required.

---

## 7. Trace formula

The preceding formulas give a compact trace rule:

\[
\boxed{
\operatorname{tr}\rho(r,L)=
\begin{cases}
1+c_4+c_3+c_{12},&L=I,\\
1,&L=A,A^2,\\
1+c_f,&L\text{ a reflection fixing }\chi_f.
\end{cases}}
\]

Hence:

- identity: trace 4;
- nonzero translation: trace 0;
- rotation: trace 1;
- reflection with \(\chi_f(r)=+1\): trace 2;
- reflection with \(\chi_f(r)=-1\): trace 0.

These are exactly the v13.479 character values
\[
(4,2,0,1,0)
\]
on \(1^4,2\,1^2,2^2,3\,1,4\).

---

## 8. Standard three-dimensional factor

Removing the invariant trivial eigenvalue \(1\) gives the standard factor characteristic polynomials:

\[
\begin{array}{c|c}
\text{class}&p_3(x)\\ \hline
1^4&(x-1)^3\\
2\,1^2&(x-1)^2(x+1)\\
2^2&(x-1)(x+1)^2\\
3\,1&(x-1)(x^2+x+1)=x^3-1\\
4&(x+1)(x^2+1)
\end{array}
\]

and traces
\[
\boxed{(3,1,-1,0,-1).}
\]

---

## 9. Interpretation

The Hadamard basis converts the affine \(S_4\) problem into a signed permutation representation on the three arithmetic character directions
\[
\{\chi_{-4},\chi_{-3},\chi_{12}\}.
\]

The class structure is then controlled by elementary cycle products of the signs:

- identity sector sees all three signs separately;
- a 3-cycle sees only their product, forced to \(+1\);
- a reflection sees only the sign on its fixed character direction.

Therefore the full five-class \(S_4\) spectrum is encoded directly in the three discriminant-12 character coordinates plus the local \(S_3\) phase permutation.

This is a representation-theoretic/arithmetic identification. It does not erase the distinct arithmetic meanings of the three character axes: \(\chi_{12}\) remains Pell-time orientation, \(\chi_{-3}\) the prime-2 residue/Frobenius bit, and \(\chi_{-4}\) the mod-4 lift/derivation bit.