# Cone Derivation Ledger v13.513 — A3 Tetrahedral Edges, S4 Transpositions, and the QR χ12 Axis

**Status:** exact finite algebra / A3 geometry. The QR comparison uses the exact v13.512 checkpoint. No Suzuki spectral consequence is asserted.

## 1. Tetrahedral minuscule vertices

Use the four minuscule weights
\[
\mu_1=\frac12(1,1,1),\quad
\mu_5=\frac12(1,-1,-1),\quad
\mu_7=\frac12(-1,1,-1),\quad
\mu_{11}=\frac12(-1,-1,1).
\]
They form the Weyl orbit
\[
\{\mu_r\}=W(A_3)\cdot\omega_1,
\]
and every oriented difference
\[
\alpha_{r,s}:=\mu_r-\mu_s
\]
for \(r\ne s\) is an A3 root.

Thus the six unoriented tetrahedral edges are the six root pairs \(\{\pm\alpha\}\), while the twelve edge orientations are the twelve roots.

## 2. Complete edge/root table

Direct subtraction gives
\[
\boxed{
\begin{array}{c|c|c}
\text{edge}&\alpha_{r,s}=\mu_r-\mu_s&\text{opposite orientation}\\ \hline
1-5&(0,1,1)&(0,-1,-1)\\
1-7&(1,0,1)&(-1,0,-1)\\
1-11&(1,1,0)&(-1,-1,0)\\
5-7&(1,-1,0)&(-1,1,0)\\
5-11&(1,0,-1)&(-1,0,1)\\
7-11&(0,1,-1)&(0,-1,1)
\end{array}}
\]
This is exactly
\[
\Phi(A_3)=\{(\pm1,\pm1,0),(\pm1,0,\pm1),(0,\pm1,\pm1)\}.
\]

## 3. Root reflections are tetrahedral transpositions

For every edge root \(\alpha_{r,s}=\mu_r-\mu_s\), define
\[
s_{r,s}(x)=x-(x\cdot\alpha_{r,s})\alpha_{r,s},
\]
since \(\|\alpha_{r,s}\|^2=2\).

Using
\[
\mu_r\cdot\mu_r=\frac34,
\qquad
\mu_r\cdot\mu_s=-\frac14\quad(r\ne s),
\]
one obtains
\[
\mu_r\cdot\alpha_{r,s}=1,
\qquad
\mu_s\cdot\alpha_{r,s}=-1,
\]
while the other two tetrahedral vertices are orthogonal to \(\alpha_{r,s}\).
Therefore
\[
\boxed{s_{r,s}(\mu_r)=\mu_s,\qquad s_{r,s}(\mu_s)=\mu_r,}
\]
and
\[
\boxed{s_{r,s}(\mu_t)=\mu_t\quad(t\notin\{r,s\}).}
\]
Hence each root reflection is literally the transposition \((r\ s)\) on the four tetrahedral labels.

So the six unoriented edges, six root-reflection hyperplanes, and six transpositions in \(S_4\) are the same combinatorial set:
\[
\boxed{
\binom42=6
\quad\leftrightarrow\quad
\Phi/\{\pm1\}
\quad\leftrightarrow\quad
\{\text{transpositions in }S_4\}.
}
\]

## 4. Dynkin chain as a Hamilton path through the tetrahedron

With the established simple roots
\[
\alpha_1=(0,1,1),\quad
\alpha_2=(1,-1,0),\quad
\alpha_3=(0,1,-1),
\]
the edge table identifies them as
\[
\boxed{
\alpha_1=\mu_1-\mu_5,\qquad
\alpha_2=\mu_5-\mu_7,\qquad
\alpha_3=\mu_7-\mu_{11}.
}
\]
Thus the chosen A3 simple system is exactly the oriented path
\[
\boxed{1\longrightarrow5\longrightarrow7\longrightarrow11}
\]
through all four tetrahedral vertices.

The simple reflections are consequently
\[
\boxed{s_1=(1\ 5),\qquad s_2=(5\ 7),\qquad s_3=(7\ 11).}
\]
Adjacent transpositions satisfy the A3 braid relations,
\[
(s_1s_2)^3=(s_2s_3)^3=1,
\]
while the disjoint endpoint transpositions commute,
\[
(s_1s_3)^2=1.
\]
This is the Coxeter presentation of \(S_4=W(A_3)\).

## 5. Remaining positive roots are path sums

The three nonsimple positive roots are the chords of the same ordered tetrahedron:
\[
\alpha_1+\alpha_2=\mu_1-\mu_7=(1,0,1),
\]
\[
\alpha_2+\alpha_3=\mu_5-\mu_{11}=(1,0,-1),
\]
\[
\alpha_1+\alpha_2+\alpha_3=\mu_1-\mu_{11}=(1,1,0).
\]
Thus root addition along the Dynkin chain is literally telescoping of tetrahedral vertex differences.

## 6. Character-axis classification of the six edges

Write character coordinates as
\[
(x_4,x_3,x_{12})
\]
for the basis
\[
(\chi_{-4},\chi_{-3},\chi_{12}).
\]
Every root has exactly one zero coordinate. Therefore the six unoriented edges split into three opposite-edge pairs according to which character coordinate vanishes:
\[
\boxed{
\begin{array}{c|c|c}
\text{zero coordinate}&\text{root pairs}&\text{tetrahedral edges}\\ \hline
\chi_{-4}&\pm(0,1,1),\ \pm(0,1,-1)&\{1,5\},\ \{7,11\}\\
\chi_{-3}&\pm(1,0,1),\ \pm(1,0,-1)&\{1,7\},\ \{5,11\}\\
\chi_{12}&\pm(1,1,0),\ \pm(1,-1,0)&\{1,11\},\ \{5,7\}
\end{array}}
\]
These are precisely the three perfect matchings of the tetrahedron \(K_4\).

Thus the three nonprincipal quadratic characters label the three perfect matchings of the four minuscule vertices.

## 7. Relation to the corrected S3 reflection axes

The exact linear S3 action on character coordinates has the corrected fixed-axis convention
\[
F\text{ fixes }\chi_{-4},\qquad
AF\text{ fixes }\chi_{-3},\qquad
A^2F\text{ fixes }\chi_{12}.
\]
The edge decomposition above gives the dual geometric statement: each character axis is paired with the perfect matching whose roots have zero component along that axis.

So the three S3 reflection axes and the three tetrahedral perfect matchings form an exact axis/matching correspondence.

## 8. Import from v13.512: QR quotient singles out chi12

The concurrent v13.512 QR/Fourier checkpoint starts from the signed carrier
\[
G=\mathbf F_2^3\cong U(24)
\]
and the QR-kernel quotient
\[
P:G\to\mathbf F_2^2,
\qquad
\ker P=\langle111\rangle.
\]
Its annihilator is
\[
K^\perp=\{000,110,101,011\}.
\]
The original mod-12 character plane is
\[
P_0=\{1,\chi_{-3},\chi_{-4},\chi_{12}\},
\]
and v13.512 proves
\[
\boxed{P_0\cap K^\perp=\{1,\chi_{12}\}.}
\]
Hence \(\chi_{12}\) is the unique nonprincipal original character surviving unchanged under that QR quotient; \(\chi_{-3}\) and \(\chi_{-4}\) descend only after sheet-character twists.

Combining this with the A3 edge decomposition yields an exact finite-geometric statement:

\[
\boxed{
\text{the unique unchanged nonprincipal QR/Fourier axis }\chi_{12}
\text{ corresponds in the A3 tetrahedron to the perfect matching }
\{1,11\}\sqcup\{5,7\}.
}
\]
Equivalently, the roots perpendicular to the \(\chi_{12}\) coordinate axis are
\[
\boxed{
\pm(1,1,0),\qquad\pm(1,-1,0),
}
\]
coming from the two opposite tetrahedral edges
\[
\boxed{
1-11,\qquad5-7.
}
\]

## 9. Compatibility with Pell time orientation

Independently, the exact Pell Galois law is
\[
\sigma_r(\lambda^n)=\lambda^{\chi_{12}(r)n}.
\]
Thus \(\chi_{12}\) already carries Pell time orientation.

The new QR checkpoint gives a second exact finite-algebraic characterization of the same character: it is the unique nonprincipal member of the original H4 character plane that survives unchanged in the QR quotient dual plane.

Therefore two independently established structures single out the same axis:
\[
\boxed{
\chi_{12}
=\text{Pell time-orientation character}
=\text{unique unchanged nonprincipal QR/Fourier character}.
}
\]
In the A3 tetrahedron this axis is geometrically dual to the opposite-edge matching
\[
\boxed{\{1,11\}\sqcup\{5,7\}.}
\]

This coincidence is exact at the character/finite-algebra level. It does not prove that Pell dynamics induces the QR quotient.

## 10. Complete tetrahedral dictionary

\[
\boxed{
\begin{array}{c|c}
\text{A3 / tetrahedral object}&\text{S4 / character object}\\ \hline
4\text{ vertices }\mu_r&W\cdot\omega_1\\
12\text{ oriented edges}&12\text{ roots}\\
6\text{ unoriented edges}&6\text{ root pairs}=6\text{ transpositions}\\
3\text{ opposite-edge matchings}&3\text{ nonprincipal character axes}\\
1\to5\to7\to11&\text{chosen A3 Dynkin path}\\
\{1,11\}\sqcup\{5,7\}&\chi_{12}\text{-perpendicular matching}
\end{array}}
\]

## 11. Guardrails

1. The tetrahedral/A3/S4 dictionary is exact and independent of the prime-2 tangent affine-frame ambiguity audited in v13.497.
2. The v13.512 QR quotient is exact finite algebra, but no claim is made that it is induced by Pell dynamics or occurs inside the Suzuki operator.
3. The fact that Pell orientation and QR Fourier survival both single out \(\chi_{12}\) is an exact coincidence of two independently defined character selections; any deeper dynamical or spectral bridge requires a separate proof.
4. No moonshine/Monster connection follows from the A3/S4/minuscule structure.