# Cone Derivation Ledger v13.476 — Complete 24-Element Affine S4 Character Table

## Scope

This entry combines the character-coordinate Klein four from v13.474 with the canonical affine completion

\[
S_4\cong V_4\rtimes S_3\cong AGL_2(\mathbf F_2)
\]

on the prime-2 tangent carrier \(\mathbf F_4\).

The crucial guardrail is that the full affine \(S_4\) does **not** act on Pell time as a 24-element group. The quotient

\[
S_4/V_4\cong S_3
\]

controls the three-state ramified phase carrier. The translation factor \(V_4\) acts only on the four-point affine \(\mathbf F_4\) carrier.

Thus in the table below:

- \((\lambda,j)\) depend only on the \(S_3\) factor;
- the selected affine-frame point \(b=w\) and the full \(\mathbf F_4\) map depend on both the translation and linear factors.

## 1. Character coordinates on the translation factor

For \(r\in U(12)=\{1,5,7,11\}\), define

\[
p(r)=\frac{1-\chi_{12}(r)}2,\qquad
f(r)=\frac{1-\chi_{-3}(r)}2.
\]

Then

\[
\chi_{-4}=\chi_{12}\chi_{-3},
\]

and the four character triples are

\[
\begin{array}{c|ccc|cc}
r&\chi_{12}&\chi_{-3}&\chi_{-4}&p&f\\
\hline
1&+&+&+&0&0\\
5&-&-&+&1&1\\
7&-&+&-&1&0\\
11&+&-&-&0&1
\end{array}
\]

After fixing the positive Pell orientation and hence the affine frame \(b=w\), choose the oriented affine coordinate identification

\[
\boxed{a(r)=p(r)w^2+f(r)w.}
\]

Therefore

\[
\boxed{
1\mapsto0,\qquad
5\mapsto1,\qquad
7\mapsto w^2,\qquad
11\mapsto w.
}
\]

This respects the previously distinguished \(7\)-direction \(w^2\) and uses the oriented frame \(w\) as the second basis vector.

## 2. The six linear S3 maps

Write

\[
A(t)=wt,\qquad F(t)=t^2,
\]

so

\[
A^3=F^2=1,\qquad FAF=A^{-1}.
\]

Every linear element is

\[
L_{k,\varepsilon}(t)=w^k t^{2^\varepsilon},
\qquad
k\in\{0,1,2\},\ \varepsilon\in\{0,1\}.
\]

On nonzero phase states \(t=w^j\), \(j\in\mathbf F_3\),

\[
\boxed{j\mapsto k+(-1)^\varepsilon j.}
\]

Take the positive Pell state as \(j=1\). Define the reduced phase representative

\[
\Lambda_0=1,\qquad \Lambda_1=\lambda,\qquad \Lambda_2=\lambda^{-1}.
\]

Then the six linear elements act on the base state \(j=1\) by

\[
\begin{array}{c|c|c|c}
S_3\text{ element}&(k,\varepsilon)&j'&\Lambda_{j'}\\
\hline
I&(0,0)&1&\lambda\\
A&(1,0)&2&\lambda^{-1}\\
A^2&(2,0)&0&1\\
F&(0,1)&2&\lambda^{-1}\\
AF&(1,1)&0&1\\
A^2F&(2,1)&1&\lambda
\end{array}
\]

Guardrail: the \(C_3\) rotations here are actions on the **projective mod-3 phase carrier**, not automorphisms of the infinite real Pell unit group. Only the reflection/time-reversal component has the literal global action \(\lambda\leftrightarrow\lambda^{-1}\).

## 3. General affine element

For translation label \(r\) and linear element \(L_{k,\varepsilon}\), define

\[
\boxed{
\Phi_{r;k,\varepsilon}(t)
=
a(r)+w^k t^{2^\varepsilon}.
}
\]

These are all 24 elements of

\[
\boxed{AGL_2(\mathbf F_2)\cong S_4.}
\]

Their action on the selected frame point \(b=w\) is

\[
\boxed{b'=\Phi_{r;k,\varepsilon}(w).}
\]

## 4. Complete 24-element table

\[
\begin{array}{c|ccc|c|c|c|c|c}
r&\chi_{12}&\chi_{-3}&\chi_{-4}&S_3&j'&\Lambda_{j'}&b'&\Phi(t)\\
\hline
1&+&+&+&I&1&\lambda&w&t\\
1&+&+&+&A&2&\lambda^{-1}&w^2&wt\\
1&+&+&+&A^2&0&1&1&w^2t\\
1&+&+&+&F&2&\lambda^{-1}&w^2&t^2\\
1&+&+&+&AF&0&1&1&wt^2\\
1&+&+&+&A^2F&1&\lambda&w&w^2t^2\\
\hline
5&-&-&+&I&1&\lambda&w^2&1+t\\
5&-&-&+&A&2&\lambda^{-1}&w&1+wt\\
5&-&-&+&A^2&0&1&0&1+w^2t\\
5&-&-&+&F&2&\lambda^{-1}&w&1+t^2\\
5&-&-&+&AF&0&1&0&1+wt^2\\
5&-&-&+&A^2F&1&\lambda&w^2&1+w^2t^2\\
\hline
7&-&+&-&I&1&\lambda&1&w^2+t\\
7&-&+&-&A&2&\lambda^{-1}&0&w^2+wt\\
7&-&+&-&A^2&0&1&w&w^2+w^2t\\
7&-&+&-&F&2&\lambda^{-1}&0&w^2+t^2\\
7&-&+&-&AF&0&1&w&w^2+wt^2\\
7&-&+&-&A^2F&1&\lambda&1&w^2+w^2t^2\\
\hline
11&+&-&-&I&1&\lambda&0&w+t\\
11&+&-&-&A&2&\lambda^{-1}&1&w+wt\\
11&+&-&-&A^2&0&1&w^2&w+w^2t\\
11&+&-&-&F&2&\lambda^{-1}&1&w+t^2\\
11&+&-&-&AF&0&1&w^2&w+wt^2\\
11&+&-&-&A^2F&1&\lambda&0&w+w^2t^2
\end{array}
\]

## 5. Semidirect-product law

Write an affine element as \((a,L)\), with \(a\in\mathbf F_4^+\) and \(L\in S_3=GL_2(\mathbf F_2)\). Then

\[
\boxed{
(a,L)(a',L')=(a+L(a'),LL').
}
\]

Equivalently, in the \((r;k,\varepsilon)\) labels,

\[
\Phi_{r;k,\varepsilon}\circ \Phi_{r';k',\varepsilon'}(t)
=
a(r)+w^k a(r')^{2^\varepsilon}
+w^{k+(-1)^\varepsilon k'}t^{2^{\varepsilon+\varepsilon'}},
\]

with the exponent data reduced modulo \(3\) for \(k\) and modulo \(2\) for \(\varepsilon\).

This is the explicit semidirect-product structure behind the 24-row table.

## 6. How the arithmetic pieces sit inside S4

The translation label \(r\) carries the full character coordinates

\[
(\chi_{12},\chi_{-3},\chi_{-4}).
\]

Their meanings remain:

\[
\boxed{\chi_{12}=\text{Pell time-orientation bit},}
\]

\[
\boxed{\chi_{-3}=\text{prime-2 residue/Frobenius bit},}
\]

\[
\boxed{\chi_{-4}=\chi_{12}\chi_{-3}=\text{lift/derivation parity bit}.}
\]

The linear \(S_3\) factor permutes the three nonzero tangent directions. The affine translations then move the distinguished zero state as well, producing the full four-point symmetry group \(S_4\).

Hence the exact structural picture is

\[
\boxed{
\text{character }V_4
\;\rtimes\;
\text{ramified phase }S_3
\;=\;
\text{affine }S_4.
}
\]

## 7. Final guardrail

The concrete map

\[
r\mapsto a(r)=p(r)w^2+f(r)w
\]

uses the **oriented affine frame normalization** selected by the positive Pell direction. Without that frame choice, the abstract affine \(S_4\) is canonical but the pointwise arithmetic labeling of its translation vectors retains the previously identified frame ambiguity.

Thus the 24-row table is an exact table in the oriented coordinate system, not a claim that the unoriented arithmetic alone canonically labels every translation vector.