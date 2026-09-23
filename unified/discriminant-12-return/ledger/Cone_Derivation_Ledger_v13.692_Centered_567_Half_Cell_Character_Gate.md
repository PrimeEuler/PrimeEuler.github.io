# Cone Derivation Ledger v13.692 — Centered 5–6–7 Half-Cell and Quadratic-Character Gate

Date: 2026-09-23

Status labels: **[S]** source-established, **[D]** exact derived, **[I]** interpretation, **[N]** negative/no stronger implication, **[Audit]** guardrail.

## 1. Live synchronization and source chain

[S] Immediately before this write the live ledger head was v13.691, commit \`e6f164102277fe72b8c631ff148c115986ed70a5\`; no v13.692 collision was present.

[S] The test was checked against:

- \`papers/Discriminant_12_Return_v0.3.5.tex\`, which explicitly uses the half-step fixed-\(T\) family through \(x+y=12\), emphasizes \(u=5,6,7\), and then introduces \(U(12)=\{1,5,7,11\}\);
- \`foundations/Casimir_Null_Diamond_Standalone_v2.1.tex\`, which proves that the factor-cell/null-diamond centering has native half-step \(\delta/2\), quarter \(\delta^2/4\), and exact transition-cell coordinates;
- v13.678, which identifies the three nontrivial character quotients \(\chi_{12},\chi_{-4},\chi_{-3}\) on the \(U(12)\cong V_4\) carrier;
- v13.691, which identifies divisor reduction mod \(1/2\) with reduction by the native spacing of the centered \(X=(x-y)/2\) coordinate.

## 2. The apparent 5–6–7 “integer” centering is a half-step in cone \(T\)

[D] The Paper-A additive-shell label is
\[
K=x+y=2T.
\]
Therefore the consecutive shells
\[
K=5,\quad6,\quad7
\]
are located at
\[
\boxed{T=\frac52,\quad3,\quad\frac72.}
\]
Thus \(5,6,7\) are not separated by unit steps in the cone time/radius coordinate. They form the exact centered half-cell
\[
\boxed{T=3-\frac12,\quad3,\quad3+\frac12.}
\]

This resolves the scale issue in the observed identity
\[
36-1=35=5\cdot7.
\]
Dividing by \(4\),
\[
\boxed{
3^2-\left(\frac12\right)^2
=
\frac{35}{4}
=
\frac52\frac72.
}
\]
Equivalently,
\[
\boxed{
(2T)^2-1
=
(2T-1)(2T+1)
}
\]
and at \(T=3\),
\[
6^2-1=5\cdot7.
\]

Hence the familiar pronic/Casimir completion is present at exactly the native cone scale:
\[
\boxed{
\left(m+\frac12\right)^2-\frac14=m(m+1).
}
\]
Taking \(m=2\) gives
\[
\left(\frac52\right)^2-\frac14=6,
\]
and taking the centered pair \(T=3\pm1/2\) gives the product \(35/4\).

## 3. Why this is the same half-cell mechanism as the null-diamond/Casimir source

[S/D] The Casimir foundation attaches to a unit factor cell the center
\[
(u_c,v_c)=\left(p+\frac12,q+\frac12\right)
\]
and maps it to
\[
X_c=\frac{p-q}{2},\qquad
T_c=\frac{p+q+1}{2}.
\]
Its four transition vertices are cardinal displacements
\[
(\Delta X,\Delta T)
=
(\pm\tfrac12,0),(0,\pm\tfrac12).
\]

Therefore the \(T=3\pm1/2\) placement of the \(K=5,7\) shells is exactly one of the native cardinal half-cell displacements of the already-established transition lattice. Squaring the displacement produces
\[
\boxed{\left(\frac12\right)^2=\frac14,}
\]
the same centered quadratic invariant used in the Casimir completion and primitive null-edge midpoint theorem.

[I] This is stronger than observing repeated factors of \(2\): the \(5,6,7\) shell triple and the Casimir/null-diamond cell use the same affine coordinate \(T=(x+y)/2\) and the same half-step.

## 4. The centered product lands on the fourth \(U(12)\) label

[D] Modulo \(12\),
\[
5\cdot7=35\equiv11\pmod{12}.
\]
Equivalently,
\[
\boxed{
(6-1)(6+1)
=6^2-1
\equiv-1
\equiv11\pmod{12}.
}
\]
Thus in the \(U(12)\) group law,
\[
\boxed{5\cdot7=11.}
\]

The geometric center \(6\) is not a unit mod \(12\), but its two adjacent unit shells \(5\) and \(7\) multiply to the outer involution \(11=-1\pmod{12}\).

The same statement in the cone half-coordinate is
\[
\boxed{
4\left[\left(3-\frac12\right)\left(3+\frac12\right)\right]
=35\equiv11\pmod{12}.
}
\]

## 5. Exact character test

[S/D] From v13.678 the three nontrivial character fibers are
\[
\begin{array}{c|cc}
\chi&+1&-1\\ \hline
\chi_{12}&\{1,11\}&\{5,7\}\\
\chi_{-4}&\{1,5\}&\{7,11\}\\
\chi_{-3}&\{1,7\}&\{5,11\}.
\end{array}
\]

Therefore on the centered pair \(5,7\),
\[
\boxed{
\chi_{12}(5)=\chi_{12}(7)=-1,
}
\]
whereas
\[
\boxed{
\chi_{-4}(5)=+1,\quad\chi_{-4}(7)=-1,
}
\]
and
\[
\boxed{
\chi_{-3}(5)=-1,\quad\chi_{-3}(7)=+1.
}
\]

So the centered \(5\leftrightarrow7\) reflection has a distinguished character signature:

- \(\chi_{12}\) is **even/constant** on the centered pair;
- \(\chi_{-4}\) and \(\chi_{-3}\) are **odd/exchanged** on the centered pair.

Because characters are multiplicative,
\[
\chi(5)\chi(7)=\chi(11).
\]
Explicitly,
\[
\boxed{
\begin{array}{c|ccc}
&\chi_{12}&\chi_{-4}&\chi_{-3}\\ \hline
5&-1&+1&-1\\
7&-1&-1&+1\\
11&+1&-1&-1
\end{array}}
\]
and each \(11\)-value is exactly the product of the \(5\)- and \(7\)-values.

This is the finite character content of the centered product \(5\cdot7=11\).

## 6. Relation to quadratic Dirichlet \(L\)-functions: exact but limited

[D] Each quadratic character \(\chi\) defines its Dirichlet \(L\)-function
\[
L(s,\chi)=\sum_{n\ge1}\frac{\chi(n)}{n^s}
=\prod_p(1-\chi(p)p^{-s})^{-1}
\]
in its usual convergence domain/continuation framework. Thus the same character signs carried by the centered residues \(5,7,11\) are indeed the local sign data entering the corresponding Euler factors.

For an unramified prime \(p\equiv5\) or \(7\pmod{12}\),
\[
\chi_{12}(p)=-1,
\]
so its \(\chi_{12}\)-Euler factor has the common sign
\[
(1+p^{-s})^{-1}.
\]
This agrees with the previously audited observation that the \(q=5,7\) source atoms are indistinguishable by \(\chi_{12}\) sign alone.

[N/Audit] The half-cell identity does **not** by itself derive the Dirichlet \(L\)-function, its Euler product, or analytic properties. The exact implication established here is narrower:
\[
\boxed{
\text{centered half-cell }(5,6,7)
\longrightarrow
5\cdot7=11\text{ in }U(12)
\longrightarrow
\text{the verified three-character sign table}.
}
\]
The \(L\)-functions use those characters globally, but the analytic \(L\)-function layer is not generated by the half-cell geometry alone.

## 7. A useful parity decomposition of the centered pair

[D] Let \(R\) exchange the two centered shell labels:
\[
R:5\leftrightarrow7.
\]
On the restricted character data:
\[
\chi_{12}|_{\{5,7\}}=(-1,-1),
\]
\[
\chi_{-4}|_{\{5,7\}}=(+1,-1),
\qquad
\chi_{-3}|_{\{5,7\}}=(-1,+1).
\]

Hence the symmetric line is the \(\chi_{12}\) restriction, while the two other character restrictions differ only by overall sign and span the same antisymmetric line:
\[
\boxed{
\chi_{-3}|_{\{5,7\}}
=
-\chi_{-4}|_{\{5,7\}}.
}
\]

[I] On this two-point centered cell, the three-character system therefore collapses to one even and one odd mode. This is compatible with the project's earlier \(\chi_{12}\)-fixed-axis results, but no new global intertwiner is asserted from this two-point restriction.

## 8. Connection to the divisor mod-\(1/2\) result

[D] v13.691 established
\[
2\left((-X_k)\bmod\frac12\right)=\left\{\frac nk\right\}.
\]
The Casimir/null-diamond foundation establishes native cardinal cell displacement \(1/2\), and the present test shows that the central D12 shells \(K=5,6,7\) become the same
\[
T=3-\frac12,\ 3,\ 3+\frac12
\]
half-cell.

Thus three formerly separate constructions now use the same factor-cone affine half-lattice:
\[
\boxed{
\begin{array}{c}
T=\frac{x+y}{2},\quad X=\frac{x-y}{2}\\[1mm]
\Downarrow\\
(T,X)\text{ carry native }\frac12\text{-steps}\\[1mm]
\Downarrow\\
\begin{cases}
X\bmod\frac12 & \text{divisor fractional remainder},\\
\Delta X,\Delta T=\pm\frac12 & \text{transition/null-diamond cell},\\
(\frac12)^2=\frac14 & \text{Casimir completion},\\
K=5,6,7\leftrightarrow T=\frac52,3,\frac72 & \text{D12 centered shell triple}.
\end{cases}
\end{array}}
\]

The cyclotomic half-element \(\mathcal Z=(H+iI)/2\) remains a fourth dyadic-quarter construction in a distinct relative norm, exactly as the foundation warns.

## 9. Gate result

\[
\boxed{\textbf{PASS: the centered 5–6–7 geometry is genuinely the native cone half-cell.}}
\]

\[
\boxed{\textbf{PASS: its adjacent unit labels multiply to }11\textbf{ and reproduce the exact V4 character signatures.}}
\]

\[
\boxed{\textbf{LIMITED: the corresponding Dirichlet }L\textbf{-functions use these characters, but are not derived from the half-cell alone.}}
\]

This is sufficient to promote the half-lattice connection as an exact geometric/arithmetic compatibility while keeping the analytic \(L\)-function claim properly scoped.

## 10. Next controlled branch: the quadratic/RMS mean

The project owner requested that after this gate we examine the remaining classical Pythagorean mean, the quadratic mean / RMS
\[
Q=\sqrt{\frac{x^2+y^2}{2}}.
\]

The immediate exact cone identity to test is
\[
x=A+D,\qquad y=A-D,
\]
so
\[
\frac{x^2+y^2}{2}
=
A^2+D^2.
\]
Therefore
\[
\boxed{Q^2=A^2+D^2.}
\]
Using the cone relation \(A^2=G^2+D^2\),
\[
\boxed{Q^2=G^2+2D^2=2A^2-G^2.}
\]

This places the RMS mean naturally one quadratic level above the existing \(A,G,D\) right triangle and opens the next gate:
determine its exact normalized circle/hyperbola/parabola/cone interpretations, its rapidity form, and whether the half-lattice/Casimir centering produces a comparably canonical RMS identity.
