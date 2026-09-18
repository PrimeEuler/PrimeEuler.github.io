# Cone Derivation Ledger v13.576 — Foliation Swap, A3 Transverse Intertwiner, and Projective T5 Shadow

## Status

**Exact finite-dimensional matrix and permutation calculation, conditional only on the already-established basis/generator conventions of v13.535, v13.545, v13.549, v13.557, and v13.574.**

This entry records the relation between the arithmetic-incidence foliation exchange
\[
J_{\rm fol}(X,Y,T)=(Y,X,T)
\]
and the transverse \(A_3\) character representation. It does **not** identify \(J_{\rm fol}\) with the arithmetic factor exchange \(F\), and it does **not** identify the v13.547 semilinear cyclic-order reversal with either the antipode or \(J_{\rm fol}\).

## 1. Incidence D8 on the cone transverse plane

Use
\[
F=\begin{pmatrix}-1&0\\0&1\end{pmatrix},\quad
S=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
J_{\rm fol}=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Here \(F\) is factor exchange, \(S\) is root-sheet exchange, and \(J_{\rm fol}\) exchanges the complementary fixed-\(X\) and fixed-\(Y\) foliations.

Set
\[
R=FJ_{\rm fol}=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
Then \(R^4=J_{\rm fol}^2=I\) and \(J_{\rm fol}RJ_{\rm fol}=R^{-1}\), so
\[
\langle F,S,J_{\rm fol}\rangle\cong D_8.
\]

## 2. Exact transport through the v13.535/v13.549 intertwiner

Use
\[
P=\begin{pmatrix}1&-1\\1&1\end{pmatrix},\qquad
P^{-1}=\frac12\begin{pmatrix}1&1\\-1&1\end{pmatrix}.
\]
Direct multiplication gives
\[
\boxed{PFP^{-1}=\begin{pmatrix}0&-1\\-1&0\end{pmatrix}=-F_\perp,}
\]
\[
\boxed{PSP^{-1}=\begin{pmatrix}0&1\\1&0\end{pmatrix}=F_\perp,}
\]
and
\[
\boxed{PJ_{\rm fol}P^{-1}=\begin{pmatrix}-1&0\\0&1\end{pmatrix}.}
\]

The exact v13.535 transverse-character ordering is
\[
\boxed{(\chi_{-4},\chi_{-3}).}
\]
Therefore
\[
PJ_{\rm fol}P^{-1}:(\chi_{-4},\chi_{-3})\mapsto(-\chi_{-4},\chi_{-3}).
\]
Also
\[
P(FJ_{\rm fol})P^{-1}=\begin{pmatrix}0&-1\\1&0\end{pmatrix}=R_\perp,
\]
recovering the established \(A_3\) transverse quarter-turn.

## 3. Full A3 lift and the two tetrahedra

Extend the transverse image by fixing the \(\chi_{12}\) axis:
\[
\boxed{J_{A_3}=\operatorname{diag}(-1,1,1)}
\]
in the ordered basis
\[
\boxed{(\chi_{-4},\chi_{-3},\chi_{12}).}
\]

For
\[
v_1=(1,1,1),\quad v_2=(1,-1,-1),\quad
v_3=(-1,1,-1),\quad v_4=(-1,-1,1),
\]
one finds
\[
J_{A_3}v_1=-v_2,\quad J_{A_3}v_2=-v_1,\quad
J_{A_3}v_3=-v_4,\quad J_{A_3}v_4=-v_3.
\]
Thus \(J_{A_3}\) exchanges the selected tetrahedron with its antipodal tetrahedron. The eight sign vertices \((\pm1,\pm1,\pm1)\) are the usual two interpenetrating tetrahedra (stella-octangula vertex configuration).

Projectively,
\[
[v_1]\leftrightarrow[v_2],\qquad [v_3]\leftrightarrow[v_4],
\]
so
\[
\boxed{[J_{A_3}]=(12)(34).}
\]

## 4. Identification of the double transposition

The character-evaluation vectors in the same ordered basis are
\[
\begin{array}{c|ccc}
r&\chi_{-4}(r)&\chi_{-3}(r)&\chi_{12}(r)\\ \hline
1&+1&+1&+1\\
5&+1&-1&-1\\
7&-1&+1&-1\\
11&-1&-1&+1
\end{array}
\]
and hence
\[
v_1\leftrightarrow1,\quad v_2\leftrightarrow5,\quad
v_3\leftrightarrow7,\quad v_4\leftrightarrow11.
\]
Therefore
\[
(12)(34)=(1\,5)(7\,11).
\]
Multiplication by \(5\) on \(\{1,5,7,11\}\) is exactly
\[
T_5=(1\,5)(7\,11).
\]
Hence
\[
\boxed{[J_{A_3}]=T_5}
\]
in this projective tetrahedral/residue action.

Equivalently, define
\[
D_5=\operatorname{diag}(1,-1,-1).
\]
Then \(D_5\) preserves the selected tetrahedron and induces \(T_5\), while
\[
\boxed{J_{A_3}=-D_5.}
\]
Thus \(J_{A_3}\) and \(D_5\) have the same projective action.

## 5. Relation to the certified incidence V4

v13.557/v13.574 certify, in the cone incidence representation,
\[
T_5\leftrightarrow F,\qquad
T_{11}\leftrightarrow S,\qquad
T_7\leftrightarrow FS
\]
projectively.

The present result is a statement in the transported \(A_3\) representation:
\[
[J_{A_3}]=T_5.
\]
These statements must **not** be collapsed to \(J_{\rm fol}=F\). The matrices are different:
\[
F=\operatorname{diag}(-1,1),\qquad
J_{\rm fol}=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
The correct statement is that, after transport by the v13.535/v13.549 \(P\)-intertwiner and extension along the fixed \(\chi_{12}\) axis, the foliation swap has the same **projective tetrahedral residue permutation** as \(T_5\).

## 6. Separation from the v13.547 reversal

v13.546/v13.547 realize cyclic-order reversal on the six null rays by
\[
\mathcal R=\operatorname{diag}(1,1,-1)\,\kappa,
\]
with
\[
\mathcal R|_{\mathcal N_6}=(a\,b)(c\,d)(e\,f).
\]
This is not the antipode \(-I_3\), which is projectively trivial, and it is not \(J_{A_3}\), which is linear and has projective tetrahedral action \(T_5\).

Therefore
\[
\boxed{-I_3,\qquad J_{A_3}=\operatorname{diag}(-1,1,1),\qquad
\mathcal R=\operatorname{diag}(1,1,-1)\kappa}
\]
are distinct operations.

## 7. Certified conclusion

The exact chain established here is
\[
\boxed{J_{\rm fol}:X\leftrightarrow Y
\ \xrightarrow{\ P\ }\
\operatorname{diag}(-1,1)}
\]
on the transverse character plane, and after fixing the \(\chi_{12}\) axis,
\[
\boxed{J_{A_3}=\operatorname{diag}(-1,1,1)=-D_5.}
\]
Consequently,
\[
\boxed{[J_{A_3}]=[D_5]=T_5=(1\,5)(7\,11).}
\]

This is a projective-shadow identification in the \(A_3\) tetrahedral/residue representation, not an equality of the original cone incidence generators.

## Guardrails

1. Do not identify \(J_{\rm fol}\) with factor exchange \(F\).
2. Do not identify cone \((X,Y,T)\) coordinates with character \((\chi_{-4},\chi_{-3},\chi_{12})\) coordinates; the relation here passes through the explicit \(P\)-intertwiner.
3. Do not identify \(J_{A_3}\) with the v13.547 semilinear reversal \(\mathcal R\).
4. The antipode \(-I_3\) exchanges the two tetrahedra linearly but is projectively trivial.
5. The label \(T_5\) here is inherited from the exact residue evaluation ordering \(1,5,7,11\) and the established v13.545/v13.535 conventions.
