# Cone Derivation Ledger v13.488 — Explicit 24 Affine Maps and S4 Cycle Verification

**Renumbering note:** originally filed as `v13.477`, which collided with the concurrently-created `Cone_Derivation_Ledger_v13.477_Shifted_Nominal_M16001_Index3_Target.md` (created 34 seconds earlier by commit timestamp). Renumbered to `v13.488`, the next free slot at the time of the External Audit Round 37 collision sweep; content unchanged.

## Status

Exact finite-field / finite-group calculation. No Suzuki or shell theorem claim.

This entry expands the v13.476 affine completion into all 24 concrete maps, verifies the semidirect-product law, and checks the exact S4 cycle census.

---

## 1. Oriented affine normalization

Work on the four-point carrier

\[
\mathbf F_4=\{0,1,w,w^2\},\qquad w^2+w+1=0.
\]

Fix the positive Pell orientation/frame

\[
b=w.
\]

For \(r\in U(12)=\{1,5,7,11\}\), define

\[
p(r)=\frac{1-\chi_{12}(r)}2,\qquad
f(r)=\frac{1-\chi_{-3}(r)}2,
\]

and the translation coordinate

\[
\boxed{a(r)=p(r)w^2+f(r)w.}
\]

Thus

\[
\begin{array}{c|ccc|c}
r&\chi_{12}&\chi_{-3}&\chi_{-4}&a(r)\\
\hline
1&+&+&+&0\\
5&-&-&+&1\\
7&-&+&-&w^2\\
11&+&-&-&w
\end{array}
\]

where \(\chi_{-4}=\chi_{12}\chi_{-3}\).

The six linear maps are

\[
L_{k,\varepsilon}(t)=w^k t^{2^\varepsilon},
\qquad k\in\mathbf F_3,\ \varepsilon\in\mathbf F_2.
\]

Use the labels

\[
I=L_{0,0},\quad A=L_{1,0},\quad A^2=L_{2,0},
\]

\[
F=L_{0,1},\quad AF=L_{1,1},\quad A^2F=L_{2,1}.
\]

Every affine symmetry is

\[
\boxed{\Phi_{r;k,\varepsilon}(t)=a(r)+w^k t^{2^\varepsilon}.}
\]

---

## 2. Ramified phase action

On the three-state phase coordinate \(j\in\mathbf F_3\),

\[
\boxed{j\longmapsto k+(-1)^\varepsilon j.}
\]

For the positive Pell phase \(j=1\), use the reduced representatives

\[
j=0\leftrightarrow 1,\qquad
j=1\leftrightarrow \lambda,\qquad
j=2=-1\leftrightarrow \lambda^{-1}.
\]

Important guardrail: this is the projective ramified Pell phase carrier. The full S3 does not act as field automorphisms of the infinite Pell unit group. Only the reflection/time-reversal C2 has the literal global action \(\lambda\leftrightarrow\lambda^{-1}\).

For \(j=1\):

\[
\begin{array}{c|c|c}
L&j'&\text{reduced Pell-phase image}\\
\hline
I&1&\lambda\\
A&2&\lambda^{-1}\\
A^2&0&1\\
F&2&\lambda^{-1}\\
AF&0&1\\
A^2F&1&\lambda
\end{array}
\]

Translations do not alter \(j\); only the S3 quotient does.

---

## 3. Complete 24-element table

The frame column is

\[
b'=\Phi(w).
\]

Cycle notation is on the ordered carrier \(\{0,1,w,w^2\}\).

| r | character triple \((\chi_{12},\chi_{-3},\chi_{-4})\) | linear part | affine map \(\Phi(t)\) | \(j'\) | reduced image of \(\lambda\) from \(j=1\) | \(b'=\Phi(w)\) | permutation |
|---|---|---|---|---|---|---|---|
| 1 | \((+,+,+)\) | \(I\) | \(t\) | \(j\) | \(\lambda\) | \(w\) | id |
| 1 | \((+,+,+)\) | \(A\) | \(wt\) | \(j+1\) | \(\lambda^{-1}\) | \(w^2\) | \((1\ w\ w^2)\) |
| 1 | \((+,+,+)\) | \(A^2\) | \(w^2t\) | \(j+2\) | \(1\) | \(1\) | \((1\ w^2\ w)\) |
| 1 | \((+,+,+)\) | \(F\) | \(t^2\) | \(-j\) | \(\lambda^{-1}\) | \(w^2\) | \((w\ w^2)\) |
| 1 | \((+,+,+)\) | \(AF\) | \(wt^2\) | \(1-j\) | \(1\) | \(1\) | \((1\ w)\) |
| 1 | \((+,+,+)\) | \(A^2F\) | \(w^2t^2\) | \(2-j\) | \(\lambda\) | \(w\) | \((1\ w^2)\) |
| 5 | \((-,-,+)\) | \(I\) | \(1+t\) | \(j\) | \(\lambda\) | \(w^2\) | \((0\ 1)(w\ w^2)\) |
| 5 | \((-,-,+)\) | \(A\) | \(1+wt\) | \(j+1\) | \(\lambda^{-1}\) | \(w\) | \((0\ 1\ w^2)\) |
| 5 | \((-,-,+)\) | \(A^2\) | \(1+w^2t\) | \(j+2\) | \(1\) | \(0\) | \((0\ 1\ w)\) |
| 5 | \((-,-,+)\) | \(F\) | \(1+t^2\) | \(-j\) | \(\lambda^{-1}\) | \(w\) | \((0\ 1)\) |
| 5 | \((-,-,+)\) | \(AF\) | \(1+wt^2\) | \(1-j\) | \(1\) | \(0\) | \((0\ 1\ w^2\ w)\) |
| 5 | \((-,-,+)\) | \(A^2F\) | \(1+w^2t^2\) | \(2-j\) | \(\lambda\) | \(w^2\) | \((0\ 1\ w\ w^2)\) |
| 7 | \((-,+,-)\) | \(I\) | \(w^2+t\) | \(j\) | \(\lambda\) | \(1\) | \((0\ w^2)(1\ w)\) |
| 7 | \((-,+,-)\) | \(A\) | \(w^2+wt\) | \(j+1\) | \(\lambda^{-1}\) | \(0\) | \((0\ w^2\ w)\) |
| 7 | \((-,+,-)\) | \(A^2\) | \(w^2+w^2t\) | \(j+2\) | \(1\) | \(w\) | \((0\ w^2\ 1)\) |
| 7 | \((-,+,-)\) | \(F\) | \(w^2+t^2\) | \(-j\) | \(\lambda^{-1}\) | \(0\) | \((0\ w^2\ 1\ w)\) |
| 7 | \((-,+,-)\) | \(AF\) | \(w^2+wt^2\) | \(1-j\) | \(1\) | \(w\) | \((0\ w^2)\) |
| 7 | \((-,+,-)\) | \(A^2F\) | \(w^2+w^2t^2\) | \(2-j\) | \(\lambda\) | \(1\) | \((0\ w^2\ w\ 1)\) |
| 11 | \((+,-,-)\) | \(I\) | \(w+t\) | \(j\) | \(\lambda\) | \(0\) | \((0\ w)(1\ w^2)\) |
| 11 | \((+,-,-)\) | \(A\) | \(w+wt\) | \(j+1\) | \(\lambda^{-1}\) | \(1\) | \((0\ w\ 1)\) |
| 11 | \((+,-,-)\) | \(A^2\) | \(w+w^2t\) | \(j+2\) | \(1\) | \(w^2\) | \((0\ w\ w^2)\) |
| 11 | \((+,-,-)\) | \(F\) | \(w+t^2\) | \(-j\) | \(\lambda^{-1}\) | \(1\) | \((0\ w\ 1\ w^2)\) |
| 11 | \((+,-,-)\) | \(AF\) | \(w+wt^2\) | \(1-j\) | \(1\) | \(w^2\) | \((0\ w\ w^2\ 1)\) |
| 11 | \((+,-,-)\) | \(A^2F\) | \(w+w^2t^2\) | \(2-j\) | \(\lambda\) | \(0\) | \((0\ w)\) |

---

## 4. Semidirect-product multiplication law

Write an affine element as \((a,L)\), acting by

\[
t\mapsto a+L(t).
\]

Then

\[
(a,L)(a',L')t
=a+L(a'+L'(t))
=a+L(a')+(LL')(t).
\]

Hence

\[
\boxed{(a,L)(a',L')=(a+L(a'),LL').}
\]

The inverse is

\[
\boxed{(a,L)^{-1}=(-L^{-1}a,L^{-1}).}
\]

Since the field has characteristic 2, \(-x=x\), so here

\[
(a,L)^{-1}=(L^{-1}a,L^{-1}).
\]

Conjugation gives

\[
(0,L)(a,I)(0,L)^{-1}=(L(a),I),
\]

showing that the translation subgroup is normal and the linear S3 acts on its three nonzero directions exactly as \(GL_2(\mathbf F_2)\).

Therefore

\[
\boxed{AGL_2(\mathbf F_2)=\mathbf F_4^+\rtimes GL_2(\mathbf F_2)\cong V_4\rtimes S_3.}
\]

---

## 5. Exact S4 cycle census

From the 24 explicit permutations:

- identity: 1;
- transpositions: 6;
- double transpositions: 3;
- 3-cycles: 8;
- 4-cycles: 6.

Thus the cycle census is

\[
\boxed{1+6+3+8+6=24,}
\]

exactly the conjugacy-class census of \(S_4\).

Hence the affine action is not merely abstractly order 24: its concrete permutation action on \(\mathbf F_4\) realizes the standard four-point \(S_4\) action.

---

## 6. Arithmetic interpretation

The normal translation factor is labeled by the character coordinates

\[
(\chi_{12},\chi_{-3},\chi_{-4}),
\qquad \chi_{-4}=\chi_{12}\chi_{-3}.
\]

The two independent arithmetic bits are:

\[
\chi_{12}: \text{Pell time orientation},
\]

\[
\chi_{-3}: \text{prime-2 residue Frobenius action}.
\]

After fixing the positive oriented frame \(b=w\), these two bits give the affine translation coordinate \(a(r)\). The S3 factor acts on the three nonzero character/tangent directions and on the three-state ramified phase coordinate.

The resulting hierarchy is

\[
\boxed{
V_4^{\rm character}\rtimes S_3^{\rm phase}
\cong AGL_2(\mathbf F_2)
\cong S_4.
}
\]

Guardrail: the concrete identification of the arithmetic V4 labels with affine translations uses the chosen positive Pell/cyclotomic frame normalization. The canonical object without that orientation choice is the abstract affine four-state carrier together with its S4 symmetry.
