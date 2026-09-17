# Cone Derivation Ledger v13.554 — Transported complex structure on the A3 character plane

## Scope

This entry transports the intrinsic fixed-shell cone complex coordinate

\[
z=X+iY
\]

through the exact intertwiner from v13.549

\[
P=\begin{pmatrix}1&-1\\1&1\end{pmatrix},
\]

into the A3 transverse character plane with ordered coordinate basis
\((\chi_{-4},\chi_{-3})\).  This is an exact linear-algebra statement on the transverse two-plane; it does not identify the third A3 coordinate \(\chi_{12}\) with a complex coordinate.

## Transported coordinates

Write

\[
\binom{u}{v}=P\binom{X}{Y}.
\]

Then

\[
u=X-Y,\qquad v=X+Y.
\]

Thus a cone vector \(X e_X+Y e_Y\) is represented on the A3 transverse plane as

\[
u\,\chi_{-4}+v\,\chi_{-3}
=(X-Y)\chi_{-4}+(X+Y)\chi_{-3}.
\]

Introduce the transported complex coordinate

\[
w=u+iv.
\]

Directly,

\[
w=(X-Y)+i(X+Y)=(1+i)(X+iY)=(1+i)z.
\]

Hence the intertwiner is, in complex notation, simply multiplication by \(1+i=\sqrt2e^{i\pi/4}\): a scale by \(\sqrt2\) and rotation by \(\pi/4\).

## Multiplication by i

On cone coordinates, multiplication by \(i\) is

\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
J\binom{X}{Y}=\binom{-Y}{X}.
\]

The transported operator is

\[
J_{A_3}=PJP^{-1}.
\]

Since

\[
P^{-1}=\frac12\begin{pmatrix}1&1\\-1&1\end{pmatrix},
\]

a direct multiplication gives

\[
\boxed{
J_{A_3}=\begin{pmatrix}0&-1\\1&0\end{pmatrix}=J.
}
\]

Therefore multiplication by \(i\) on the A3 transverse character coordinates is exactly

\[
\boxed{(u,v)\mapsto(-v,u).}
\]

Equivalently,

\[
\boxed{
u\chi_{-4}+v\chi_{-3}
\longmapsto
-v\chi_{-4}+u\chi_{-3}.}
\]

In particular the transported complex structure satisfies

\[
J_{A_3}^2=-I,
\]

and the quarter-turn states are

\[
I,\quad J_{A_3},\quad -I,\quad -J_{A_3}.
\]

## Basis-vector action

The exact action on the two character axes is

\[
\boxed{
J_{A_3}:\chi_{-4}\mapsto\chi_{-3},
\qquad
\chi_{-3}\mapsto-\chi_{-4}.
}
\]

This is the concrete character-plane meaning of the cone operation \(z\mapsto iz\).

## Consistency with the transported complex coordinate

Because \(w=(1+i)z\),

\[
z\mapsto iz
\]

gives

\[
w\mapsto(1+i)iz=i(1+i)z=iw.
\]

Thus the transported coordinate itself has the standard complex action:

\[
\boxed{w\mapsto iw.}
\]

No extra phase appears in the multiplication-by-i operator because \(P\) commutes with \(J\).

## Conjugation comparison

For later use, cone conjugation is

\[
C=\operatorname{diag}(1,-1).
\]

v13.549 established

\[
PCP^{-1}=F_\perp=
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Hence in \((u,v)\) coordinates cone conjugation acts by

\[
(u,v)\mapsto(v,u).
\]

In terms of \(w=u+iv\), this is

\[
\boxed{w\mapsto i\bar w.}
\]

This is consistent with \(w=(1+i)z\):

\[
(1+i)\bar z=i\,\overline{(1+i)z}=i\bar w.
\]

Thus the transported complex structure is standard, while the transported cone conjugation is reflection across the diagonal character axis rather than ordinary \(w\mapsto\bar w\).

## Exact conclusion

On the A3 transverse plane \(\operatorname{span}(\chi_{-4},\chi_{-3})\), the cone complex coordinate transports as

\[
\boxed{w=(X-Y)+i(X+Y)=(1+i)z,}
\]

and multiplication by \(i\) is represented exactly by

\[
\boxed{
J_{A_3}=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
}
\]

Therefore the cone complex quarter-turn is not merely abstractly compatible with the A3 transverse action: under the v13.549 intertwiner it is literally the same standard complex-structure matrix.

## Guardrail

This result is confined to the two-dimensional A3 transverse character plane.  The full three-dimensional A3 generator from v13.535 also acts on the \(\chi_{12}\) axis; no claim is made here that the entire three-dimensional A3 representation is a complex one-dimensional representation.