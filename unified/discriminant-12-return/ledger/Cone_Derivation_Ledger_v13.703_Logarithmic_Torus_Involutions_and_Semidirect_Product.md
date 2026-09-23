# Cone Derivation Ledger v13.703 — Logarithmic Torus Involutions and Semidirect Product

Date: 2026-09-23

Status: exact group-action calculation following v13.702.

## 0. Synchronization

Immediately before this write the live head was v13.702, commit \`30dc8581df973e11b9d25f0a80a86d96edb0548d\`; no v13.703 collision was present.

## 1. Continuous torus and logarithmic coordinates

From v13.702, use the commuting actions
\[
S(\lambda):v\mapsto\lambda v,
\qquad
B(w):(x,y,Y)\mapsto(wx,w^{-1}y,Y),
\]
with
\[
(\lambda,w)\in
T_{\mathbb C}:=
\mathbb C^\times_{\rm scale}\times
\mathbb C^\times_{\rm boost}.
\]

Write
\[
\lambda=e^\tau,\qquad w=e^\ell,
\]
so the universal-cover logarithmic coordinates are
\[
(\tau,\ell)\in\mathbb C^2.
\]

On the positive real factor cone,
\[
\tau=\frac12\log(xy),
\qquad
\ell=s=\frac12\log\frac{x}{y},
\]
and
\[
\log x=\tau+\ell,\qquad
\log y=\tau-\ell.
\]

Modulo logarithm periods,
\[
(\tau,\ell)\sim
(\tau+2\pi i m,\ell+2\pi i n),
\qquad m,n\in\mathbb Z.
\]

## 2. Factor exchange F [D]

Define factor exchange
\[
F:(x,y,Y)\mapsto(y,x,Y).
\]
Equivalently on cone coordinates,
\[
F=R_X:(T,X,Y)\mapsto(T,-X,Y).
\]

Then
\[
xy\mapsto xy,
\qquad
\frac{x}{y}\mapsto\frac{y}{x}
=\left(\frac{x}{y}\right)^{-1}.
\]

Therefore on the real logarithmic slice,
\[
\boxed{
F:(\tau,s)\mapsto(\tau,-s).
}
\]

On the complex torus itself, conjugating the continuous actions gives
\[
F\,S(\lambda)\,F^{-1}=S(\lambda),
\]
and
\[
F\,B(w)\,F^{-1}=B(w^{-1}).
\]

Thus
\[
\boxed{
F:(\lambda,w)\mapsto(\lambda,w^{-1}).
}
\]

On a chosen logarithmic lift,
\[
\boxed{
F:(\tau,\ell)\mapsto(\tau,-\ell)
}
\]
modulo the \(2\pi i\) period lattice.

Relations:
\[
\boxed{F^2=1,}
\]
\[
\boxed{FS(\lambda)F=S(\lambda),}
\]
\[
\boxed{FB(w)F=B(w^{-1}).}
\]

Hence \(F\) acts as the Weyl inversion on the boost torus and trivially on the scale torus.

## 3. Complex conjugation C [D]

Let
\[
C:v\mapsto\bar v
\]
be the semilinear complex-conjugation involution on the complexified cone.

Then
\[
C\,S(\lambda)\,C^{-1}=S(\bar\lambda),
\]
and because the boost matrices have Laurent-polynomial coefficients in \(w\) with real coefficients,
\[
C\,B(w)\,C^{-1}=B(\bar w).
\]

Therefore
\[
\boxed{
C:(\lambda,w)\mapsto(\bar\lambda,\bar w).
}
\]

On logarithmic coordinates,
\[
\boxed{
C:(\tau,\ell)\mapsto(\bar\tau,\bar\ell)
}
\]
modulo logarithm periods.

Writing
\[
\tau=a+i\alpha,\qquad
\ell=s+i\phi,
\]
gives
\[
\boxed{
C:(a,\alpha,s,\phi)
\mapsto
(a,-\alpha,s,-\phi).
}
\]

Thus complex conjugation fixes both real logarithmic generators (scale \(a\) and rapidity \(s\)) and reverses both phase coordinates.

Relations:
\[
\boxed{C^2=1,}
\]
\[
\boxed{CS(\lambda)C=S(\bar\lambda),}
\]
\[
\boxed{CB(w)C=B(\bar w).}
\]

On the positive real cone \(C\) acts trivially.

## 4. F and C commute [D]

Factor exchange is represented by a real matrix, so
\[
FC(v)=F(\bar v)=\overline{F(v)}=CF(v).
\]

Hence
\[
\boxed{FC=CF.}
\]

Therefore
\[
\boxed{
\langle F,C\rangle\cong C_2\times C_2.
}
\]

Their product acts by
\[
FC:(\lambda,w)\mapsto(\bar\lambda,\bar w^{-1}),
\]
and on logarithms
\[
\boxed{
FC:(\tau,\ell)\mapsto(\bar\tau,-\bar\ell).
}
\]

In real coordinates,
\[
FC:(a,\alpha,s,\phi)
\mapsto
(a,-\alpha,-s,\phi).
\]

So \(FC\) reverses real rapidity and scale phase, while preserving boost phase.

## 5. Exact semidirect product [D]

The involution group
\[
V=\langle F,C\rangle\cong C_2^2
\]
acts on
\[
T_{\mathbb C}
=(\mathbb C^\times)^2
\]
by
\[
F:(\lambda,w)\mapsto(\lambda,w^{-1}),
\]
\[
C:(\lambda,w)\mapsto(\bar\lambda,\bar w).
\]

Therefore the generated continuous/semilinear group is
\[
\boxed{
G_{\log}
=
(\mathbb C^\times_{\rm scale}\times
\mathbb C^\times_{\rm boost})
\rtimes
(C_2^{F}\times C_2^{C}).
}
\]

The action homomorphism
\[
\varphi:C_2^2\to\operatorname{Aut}_{\mathbb R}(T_{\mathbb C})
\]
is
\[
\varphi(F)(\lambda,w)=(\lambda,w^{-1}),
\]
\[
\varphi(C)(\lambda,w)=(\bar\lambda,\bar w),
\]
\[
\varphi(FC)(\lambda,w)=(\bar\lambda,\bar w^{-1}).
\]

The action is faithful: \(F,C,FC\) induce three distinct nonidentity automorphisms.

## 6. Presentation [D]

A useful operator presentation is
\[
\boxed{
\begin{aligned}
G_{\log}
=\langle\,
&S(\lambda),B(w),F,C\ :\\
&S(\lambda_1)S(\lambda_2)=S(\lambda_1\lambda_2),\\
&B(w_1)B(w_2)=B(w_1w_2),\\
&[S(\lambda),B(w)]=1,\\
&F^2=C^2=1,\quad [F,C]=1,\\
&FS(\lambda)F=S(\lambda),\\
&FB(w)F=B(w^{-1}),\\
&CS(\lambda)C=S(\bar\lambda),\\
&CB(w)C=B(\bar w)
\,\rangle .
\end{aligned}
}
\]

Here \(C\) is semilinear, so the automorphism category is real/semilinear rather than complex-linear.

## 7. Lie-algebra action [D]

On the logarithmic Lie algebra
\[
\mathfrak t_{\mathbb C}\cong\mathbb C^2
\]
with coordinates \((\tau,\ell)\),

\[
F=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}
\]
as a complex-linear involution.

Complex conjugation is semilinear:
\[
C(\tau,\ell)=(\bar\tau,\bar\ell).
\]

On the underlying real Lie algebra with coordinates
\[
(a,\alpha,s,\phi)
=(\Re\tau,\Im\tau,\Re\ell,\Im\ell),
\]
the two involutions are diagonal:
\[
\boxed{
F=\operatorname{diag}(1,1,-1,-1),
}
\]
\[
\boxed{
C=\operatorname{diag}(1,-1,1,-1),
}
\]
and
\[
\boxed{
FC=\operatorname{diag}(1,-1,-1,1).
}
\]

Thus the four real directions split into simultaneous one-dimensional eigenspaces:

\[
\begin{array}{c|cc}
\text{coordinate}&F&C\\ \hline
a=\Re\tau&+&+\\
\alpha=\Im\tau&+&-\\
s=\Re\ell&-&+\\
\phi=\Im\ell&-&-
\end{array}
\]

This is a canonical \(C_2^2\) character decomposition of the logarithmic tangent space.

## 8. Important distinction from the earlier RY label [G]

On the real fixed-\(T\) \(XY\) plane, the map
\[
z=X+iY\mapsto\bar z
\]
is the real-linear reflection
\[
R_Y:(X,Y,T)\mapsto(X,-Y,T).
\]

The \(C\) used in this entry is instead **coefficient conjugation on the complexified cone**:
\[
(X,Y,T)\mapsto(\bar X,\bar Y,\bar T).
\]

These coincide in their action on a chosen scalar complex phase only after a representation/real-form identification; they are not globally the same \(3\times3\) operation.

This distinction is necessary for the semidirect-product statement above.

## 9. Weyl/dihedral interpretation [D/G]

The subgroup
\[
\mathbb C^\times_{\rm boost}\rtimes\langle F\rangle
\]
has
\[
FB(w)F=B(w^{-1}),
\]
so it is the normalizer of the one-dimensional complex boost torus in this representation, with Weyl group
\[
\boxed{W\cong C_2.}
\]

Restricting \(w\) to the fourth roots of unity gives
\[
\mu_4\rtimes C_2\cong D_8
\]
for the **boost-torus torsion**.

Separately, v13.701 identified the scalar cyclotomic torsion
\[
\langle\mathcal Z^3\rangle=\mu_4\subset\mathbb C^\times_{\rm scale}.
\]
Coefficient conjugation acts there by
\[
C(iI)C^{-1}=-iI=(iI)^{-1},
\]
so
\[
\mu_4^{\rm scale}\rtimes\langle C\rangle\cong D_8.
\]

Thus the two distinct \(D_8\) mechanisms now occupy orthogonal factors:

\[
\boxed{
\begin{array}{c|c|c}
&\text{torus}&\text{inverting involution}\\ \hline
D_8^{\rm boost}&\mu_4\subset\mathbb C^\times_{\rm boost}&F\\
D_8^{\rm cycl}&\mu_4=\langle\mathcal Z^3\rangle\subset\mathbb C^\times_{\rm scale}&C
\end{array}
}
\]

They commute at the level of the product torus/involution action, but they should not be identified.

## 10. Positive-real restriction [D]

Restrict to
\[
\lambda=e^a>0,\qquad w=e^s>0.
\]
Then coefficient conjugation \(C\) is trivial on the torus, while
\[
F:(a,s)\mapsto(a,-s).
\]

Therefore the real positive continuous symmetry is
\[
\boxed{
(\mathbb R_{>0}^{\rm scale}\times
\mathbb R_{>0}^{\rm boost})
\rtimes C_2^F.
}
\]

In additive coordinates:
\[
\boxed{
(\mathbb R_a\oplus\mathbb R_s)\rtimes C_2,
\qquad
F(a,s)=(a,-s).
}
\]

This is the clean continuous group underlying the ordinary positive factor cone.

## 11. Proved relations summary

\[
\boxed{
F^2=C^2=1,\qquad FC=CF.
}
\]

\[
\boxed{
FS(\lambda)F=S(\lambda),\qquad
FB(w)F=B(w^{-1}).
}
\]

\[
\boxed{
CS(\lambda)C=S(\bar\lambda),\qquad
CB(w)C=B(\bar w).
}
\]

\[
\boxed{
G_{\log}
=(\mathbb C^\times)^2\rtimes C_2^2.
}
\]

\[
\boxed{
F:(\tau,\ell)\mapsto(\tau,-\ell),
\qquad
C:(\tau,\ell)\mapsto(\bar\tau,\bar\ell).
}
\]

\[
\boxed{
FC:(\tau,\ell)\mapsto(\bar\tau,-\bar\ell).
}
\]

The underlying real logarithmic tangent space decomposes into the four \(C_2^2\) characters
\[
(++),(+-),(-+),(--)
\]
carried respectively by
\[
\Re\tau,\quad\Im\tau,\quad\Re\ell,\quad\Im\ell.
\]

## 12. Next gate

This exact four-character decomposition is potentially exportable to the Suzuki/operator lane. The next useful test is to identify whether Suzuki's Cayley/log variables naturally split into the same four real directions (scale modulus, scale phase, rapidity modulus, boost phase), rather than forcing a single scalar logarithm. Any such bridge must be constructed from the actual Friedrichs/Kreĭn formulas and not inferred from group-type coincidence.
