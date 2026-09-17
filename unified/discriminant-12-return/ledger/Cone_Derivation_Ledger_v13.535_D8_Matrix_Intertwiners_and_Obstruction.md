# Cone Derivation Ledger v13.535 — Three D8 Matrix Realizations, Explicit Intertwiners, and the Generator Obstruction

## Status

Exact finite-dimensional matrix calculation. This checkpoint corrects an over-strong interpretation suggested after v13.534: the three groups are abstractly D8, but the previously established intrinsic cone/cyclotomic identification `R_Y = complex-conjugation parity` is **not** compatible with identifying the complexified arithmetic-negation lift with the cyclotomic quarter-turn. The obstruction is the square relation.

---

## 1. Cyclotomic complex-plane D8

On the real basis `(1,i)` of `Q(i) tensor R`, multiplication by `i` is

\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad J^2=-I_2,
\]

and complex conjugation is

\[
C=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

They satisfy

\[
J^4=C^2=I_2,
\qquad CJC=J^{-1},
\]

so

\[
\boxed{\langle J,C\rangle\cong D_8.}
\]

In the previously established cyclotomic operator notation,

\[
\boxed{J=\mathcal Z^3=\times i.}
\]

---

## 2. Complexified cone lift

Use coordinates `(X,Y,T)` and the affine-normalized arithmetic-negation lift

\[
A=\widetilde\sigma_+:
(X,Y,T)\mapsto(-T,iY,-X).
\]

Its matrix is

\[
A=
\begin{pmatrix}
0&0&-1\\
0&i&0\\
-1&0&0
\end{pmatrix}.
\]

The native reflections are

\[
R_X=B=
\begin{pmatrix}
-1&0&0\\
0&1&0\\
0&0&1
\end{pmatrix},
\]

\[
R_Y=
\begin{pmatrix}
1&0&0\\
0&-1&0\\
0&0&1
\end{pmatrix},
\]

and sheet reversal is

\[
S_T=
\begin{pmatrix}
1&0&0\\
0&1&0\\
0&0&-1
\end{pmatrix}.
\]

Direct multiplication gives

\[
\boxed{A^2=R_Y},
\qquad A^4=I_3.
\]

The full antipode is

\[
\Omega=-I_3=R_XR_YS_T.
\]

As established in v13.534,

\[
G_{\rm lift}=\langle A,B\rangle,
\qquad |G_{\rm lift}|=16,
\]

and

\[
\overline G_{\rm cone}=G_{\rm lift}/\langle\Omega\rangle\cong D_8.
\]

Writing projective classes with bars,

\[
\bar A^4=\bar B^2=1,
\qquad
\bar B\bar A\bar B=\bar A^{-1}.
\]

Thus the abstract presentation identifies

\[
\boxed{\bar A\leftrightarrow J,\qquad \bar B\leftrightarrow C}
\]

as one D8 isomorphism. Under this isomorphism,

\[
\boxed{\bar R_Y=\bar A^2\leftrightarrow J^2=-I_2.}
\]

This last equation is the crucial constraint.

---

## 3. A3 / tetrahedral chi_12-axis stabilizer

Use the character-coordinate basis

\[
(e_1,e_2,e_3)=(\chi_{-4},\chi_{-3},\chi_{12}).
\]

The tetrahedral vertices are

\[
(1,1,1),\ (1,-1,-1),\ (-1,1,-1),\ (-1,-1,1).
\]

An order-four tetrahedral symmetry preserving the unoriented `chi_12` axis is

\[
R=
\begin{pmatrix}
0&-1&0\\
1&0&0\\
0&0&-1
\end{pmatrix}.
\]

Its square is

\[
R^2=
\begin{pmatrix}
-1&0&0\\
0&-1&0\\
0&0&1
\end{pmatrix}
=D_{11},
\]

exactly the previously established action of carrier element `11`: the 180-degree rotation about the `chi_12` axis.

Take the reflection

\[
F=
\begin{pmatrix}
0&1&0\\
1&0&0\\
0&0&1
\end{pmatrix}.
\]

It exchanges `chi_-4` and `chi_-3`, fixes `chi_12`, preserves the tetrahedral vertex set, and satisfies

\[
F^2=I_3,
\qquad FRF=R^{-1}.
\]

Hence

\[
\boxed{\langle R,F\rangle\cong D_8.}
\]

---

## 4. Explicit cyclotomic-to-A3 intertwiner

On the transverse `(chi_-4,chi_-3)` plane, the A3 matrices reduce to

\[
R_\perp=
\begin{pmatrix}0&-1\\1&0\end{pmatrix}=J,
\]

and

\[
F_\perp=
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

We seek `P` satisfying

\[
PJ=R_\perp P,
\qquad
PC=F_\perp P.
\]

A solution is

\[
\boxed{
P=\begin{pmatrix}1&-1\\1&1\end{pmatrix}.
}
\]

Indeed,

\[
PJ=JP,
\]

and

\[
PCP^{-1}=F_\perp.
\]

Up to a nonzero scalar this is the 45-degree change of reflection axis. Therefore the cyclotomic complex-plane D8 and the transverse A3 D8 are explicitly intertwined:

\[
\boxed{
J=\mathcal Z^3\longleftrightarrow R,
\qquad
C\longleftrightarrow F.
}
\]

Moreover

\[
J^2=-I_2
\longleftrightarrow
R^2=D_{11}|_{\perp}=-I_2.
\]

Thus the cyclotomic quarter-turn has a rigid A3 interpretation: it is the order-four tetrahedral symmetry whose square is the known `11` half-turn about the `chi_12` axis.

---

## 5. Abstract projective-cone-to-cyclotomic D8 isomorphism

Because

\[
\bar A^4=\bar B^2=1,
\qquad
\bar B\bar A\bar B=\bar A^{-1},
\]

there is an abstract D8 isomorphism

\[
\Theta:\overline G_{\rm cone}\to\langle J,C\rangle
\]

specified by

\[
\boxed{
\Theta(\bar A)=J=\mathcal Z^3,
\qquad
\Theta(\bar R_X)=C.
}
\]

Consequently

\[
\boxed{
\Theta(\bar R_Y)
=\Theta(\bar A^2)
=J^2
=-I_2.
}
\]

Composing with the A3 intertwiner gives

\[
\boxed{
\bar A
\longleftrightarrow
\mathcal Z^3=\times i
\longleftrightarrow
R,
}
\]

and

\[
\boxed{
\bar R_Y
\longleftrightarrow
- I_2
\longleftrightarrow
D_{11}|_{\perp}.
}
\]

So, **within this D8 presentation**, the cone generator corresponding to the cyclotomic quarter-turn is the projective class of the complexified arithmetic-negation lift `A`, not either native reflection.

---

## 6. Exact obstruction to compatibility with the earlier intrinsic complex identification

Earlier checkpoints established a different, intrinsically motivated correspondence. Since

\[
z=X+iY,
\]

we have

\[
R_Y:z\mapsto\bar z.
\]

Under the compatible cyclotomic embedding `i_cone=ζ_12^3`, this gives

\[
\boxed{R_Y\longleftrightarrow C}
\]

as complex-conjugation parity.

Now ask whether an intertwiner can simultaneously satisfy

\[
A\longleftrightarrow J
\]

and

\[
R_Y\longleftrightarrow C.
\]

It cannot. Since

\[
A^2=R_Y,
\]

any homomorphism with `A -> J` must send

\[
R_Y=A^2\mapsto J^2=-I_2.
\]

But complex conjugation is

\[
C=\operatorname{diag}(1,-1)\neq-I_2.
\]

Therefore

\[
\boxed{
\text{no D8 intertwiner can simultaneously realize }
A\mapsto\mathcal Z^3
\text{ and }
R_Y\mapsto C.
}
\]

This is a structural obstruction, not a basis artifact: an order-four generator's square is the central order-two element of D8, whereas a reflection is noncentral.

---

## 7. Consequence for the claimed three-way D8 correspondence

The following two statements are separately exact:

1. Intrinsic complex cone:
   \[
   R_Y\leftrightarrow C
   \]
   because both are complex conjugation after `i_cone=ζ_12^3`.

2. Projective complexified signed-factor D8:
   \[
   \bar A\leftrightarrow J=\mathcal Z^3
   \]
   under the standard D8 generator matching.

But they do **not** belong to one generator-preserving D8 intertwiner, because `A^2=R_Y` while `J^2=-I`.

Hence the three D8 occurrences

\[
\langle J,C\rangle,
\qquad
\overline G_{\rm cone},
\qquad
\operatorname{Stab}_{S_4}(\mathbf R\chi_{12})
\]

are abstractly isomorphic, and the first and third admit the explicit matrix intertwiner above, but the projective-cone identification cannot simultaneously preserve the previously established `R_Y/C` semantic labeling.

This prevents an accidental conflation of two distinct uses of the same cone reflection.

---

## 8. Certified correspondence table

The strongest currently justified table is therefore

\[
\begin{array}{c|c|c|c}
\text{role}&\text{projective cone}&\text{cyclotomic plane}&A_3\text{ transverse plane}\\ \hline
\text{order-4 rotation}&\bar A&J=\mathcal Z^3&R\\
\text{central half-turn}&\bar R_Y&-I_2&D_{11}|_\perp\\
\text{chosen D8 reflection}&\bar R_X&C&F_\perp
\end{array}
\]

This table is an exact D8 generator intertwining.

Separately, the intrinsic complex-semantic correspondence remains

\[
\boxed{R_Y\leftrightarrow C}
\]

and must not be merged with the table above.

---

## 9. Guardrail and next target

The key result is therefore both positive and negative:

\[
\boxed{
\bar{\widetilde\sigma}_+
\leftrightarrow
\mathcal Z^3=\times i
\leftrightarrow
R
}
\]

is the explicit order-four D8 generator matching, **but only after adopting the projective signed-factor D8 presentation**.

At the same time,

\[
\boxed{
\bar R_Y\leftrightarrow-1
}
\]

inside that presentation, so this matching does not preserve the independently motivated `R_Y <-> complex conjugation` interpretation.

The next structural question is whether both actions embed into a larger Clifford/split-quaternion or semilinear group in which `R_Y` can appear in the two different roles through different quotients/subgroups, rather than trying to identify the two D8 actions directly. That is now the mathematically precise place where the split-quaternion/Penrose side branch may become useful.
