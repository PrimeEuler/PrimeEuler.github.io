# V4 Four-Channel Transform of the Divisor Shell-Defect Field

## Scope

This note continues the exact overlay recorded in ledger v13.309.  The divisor shell-defect field

\[
\delta_k(n)=\left\{\frac nk\right\}=\frac{n-Y_k^2}{k}
\]

is decomposed against the four real Dirichlet characters modulo 12,

\[
\{1,\chi_{-4},\chi_{-3},\chi_{12}\},
\qquad \chi_{12}=\chi_{-4}\chi_{-3}.
\]

The result is a four-channel arithmetic Fourier transform of the same geometric defect field.  No identification is made between local factor-cell vertices and literal residue classes modulo 12.

---

## 1. Four shell-defect channels

For each character \(\chi\), define

\[
E_\chi(n)=\sum_{k=1}^n \chi(k)\delta_k(n)
=\sum_{k=1}^n \chi(k)\frac{n-Y_k^2}{k}.
\]

The trivial channel is

\[
\boxed{E_1(n)=nH_n-D(n).}
\]

The three nontrivial channels are

\[
E_{-4}(n),\qquad E_{-3}(n),\qquad E_{12}(n).
\]

The existing discriminant-12 note already studies \(E_{12}(n)\); the present point is that it belongs naturally to the full four-character transform of the shell-defect field.

---

## 2. Residue-class reconstruction on U(12)

For the unit residue classes \(r\in\{1,5,7,11\}\), define the class-restricted defect sums

\[
R_r(n)=\sum_{\substack{k\le n\\k\equiv r\ (12)}}\delta_k(n).
\]

On \(U(12)\), use the character table

\[
\begin{array}{c|rrrr}
 &1&5&7&11\\\hline
1&1&1&1&1\\
\chi_{-4}&1&1&-1&-1\\
\chi_{-3}&1&-1&1&-1\\
\chi_{12}&1&-1&-1&1
\end{array}
\]

so that, writing \(E_\chi^{\times}\) for the sums restricted to \(\gcd(k,12)=1\),

\[
\begin{pmatrix}
E_1^{\times}\\E_{-4}^{\times}\\E_{-3}^{\times}\\E_{12}^{\times}
\end{pmatrix}
=
H_4
\begin{pmatrix}
R_1\\R_5\\R_7\\R_{11}
\end{pmatrix},
\]

with \(H_4\) the order-four Hadamard matrix above.  Since \(H_4^2=4I\), inversion is exact:

\[
\boxed{
\begin{pmatrix}
R_1\\R_5\\R_7\\R_{11}
\end{pmatrix}
=
\frac14 H_4
\begin{pmatrix}
E_1^{\times}\\E_{-4}^{\times}\\E_{-3}^{\times}\\E_{12}^{\times}
\end{pmatrix}.}
\]

Thus the four V4 character channels and the four unit-residue defect totals contain exactly the same information.

Guardrail: the full untwisted discrepancy \(E_1(n)\) also receives contributions from nonunit residue classes modulo 12.  The Hadamard inversion above applies to the unit-supported part \(E_1^{\times}\), not to the full \(E_1(n)\).

---

## 3. Two generator directions and the mixed channel

Using the Boolean identification

\[
1\leftrightarrow(0,0),\quad 5\leftrightarrow(1,0),\quad
7\leftrightarrow(0,1),\quad 11\leftrightarrow(1,1),
\]

the two one-generator characters are the two independent sign directions, while

\[
\chi_{12}=\chi_{-4}\chi_{-3}
\]

is the mixed/checkerboard mode.

Hence the unit-supported shell defect decomposes into:

- mean channel,
- 5-direction imbalance,
- 7-direction imbalance,
- 5x7 checkerboard imbalance.

This is exactly the same four-mode Walsh algebra carried locally by one four-vertex factor cell in v13.309.

---

## 4. Quotient-block compression of all channels

For a constant quotient block

\[
q=\left\lfloor\frac nk\right\rfloor,
\qquad L_q\le k\le R_q,
\]

we have

\[
\delta_k(n)=\frac nk-q.
\]

For each character define

\[
H_\chi(N)=\sum_{k\le N}\frac{\chi(k)}{k},
\qquad
C_\chi(N)=\sum_{k\le N}\chi(k).
\]

Then exactly

\[
\boxed{
E_{\chi,q}(n)=
 n\bigl(H_\chi(R_q)-H_\chi(L_q-1)\bigr)
-q\bigl(C_\chi(R_q)-C_\chi(L_q-1)\bigr).}
\]

Therefore

\[
\boxed{E_\chi(n)=\sum_{q\in Q(n)}E_{\chi,q}(n)}
\]

for all four characters, with \(|Q(n)|=O(\sqrt n)\).

So the quotient-block/hyperbola compression acts channel-by-channel on the V4 transform.

---

## 5. Local/global parallel

The local factor-cell Walsh transform from v13.309 gives

\[
\left(
Y_c^2,
-\frac{\delta v_c}{2},
-\frac{\delta u_c}{2},
\frac{\delta^2}{4}
\right).
\]

The global shell-defect transform gives

\[
\left(
E_1^{\times},E_{-4},E_{-3},E_{12}
\right).
\]

The exact common structure is the character algebra, not equality of observables or carriers.  In both cases the mixed/checkerboard channel is distinguished:

\[
\text{local: }\frac{\delta^2}{4},
\qquad
\text{global: }E_{12}(n).
\]

---

## 6. Prime-contact information remains a support statistic

The V4 transform reorganizes amplitudes but does not replace the exact prime contact criterion.  The shell-contact zero set remains

\[
\delta_k(n)=0\iff k\mid n,
\]

and

\[
\tau(n)=\#\{k:\delta_k(n)=0\}.
\]

For \(n>1\),

\[
\boxed{n\text{ prime}\iff \tau(n)=2.}
\]

Thus the character channels measure signed defect amplitudes, while primality itself remains encoded in the zero-set/support geometry.

---

## Interpretation

The divisor-shell framework now has two compatible decompositions:

1. quotient blocks compress the staircase geometrically to O(sqrt n) horizontal runs;
2. V4 characters decompose the shell-defect amplitudes arithmetically into four orthogonal sign channels.

These operations commute at the level of finite sums: one may first split into quotient blocks and then project by character, or first project the defect field and then sum blockwise.  This gives a clean two-axis organization of the same arithmetic data without identifying the local four-vertex cell with the global mod-12 residue lattice.
