# Cone Derivation Ledger v13.538 — Complexified Arithmetic-Negation Lifts

**Renumbering note:** originally filed as v13.530, then briefly v13.537 -- both collided with concurrently-created entries. Renumbered to v13.538 during External Audit Round 45. Mathematical content is unchanged.

## Status

Exact classification under the stated linear/projective signed-factor assumptions. The natural arithmetic-negation lift does not collapse to a real sheet reflection. Instead there are four projectively normalized complexified lifts squaring to `R_Y`, split into two conjugacy classes under the residual geometric `V_4`. On the affine normalization `T-X=1`, only two lifts remain and they are not conjugate by the affine-normalization-preserving residual subgroup.

---

## 1. Signed factor coordinate

For the normalized factor line

\[
X(r)=\frac{r-1}{2},\qquad T(r)=\frac{r+1}{2},
\]

we have

\[
T-X=1,\qquad T+X=r.
\]

Projectively,

\[
r=\frac{T+X}{T-X}.
\]

Arithmetic negation `r -> -r` is induced on the `(X,T)` pair by

\[
A_0(X,T)=(-T,-X).
\]

Indeed

\[
\frac{T'+X'}{T'-X'}
=\frac{-X-T}{-X+T}
=-\frac{T+X}{T-X}=-r.
\]

The negative scalar representative

\[
-A_0(X,T)=(T,X)
\]

induces the same projective map `r -> -r`, but reverses the affine normalization from `T-X=1` to `T'-X'=-1`.

---

## 2. General linear complexified lift

Require a linear lift which:

1. induces `r -> -r` on the signed projective factor coordinate;
2. preserves the complexified cone
   \[
   X^2+Y^2=T^2;
   \]
3. acts diagonally on the transverse `Y` coordinate;
4. squares exactly to
   \[
   R_Y(X,Y,T)=(X,-Y,T).
   \]

Write

\[
L_{\lambda,\delta}(X,Y,T)
=
(-\lambda T,\ \delta i\lambda Y,\ -\lambda X),
\]

where initially `lambda` is a nonzero complex scalar and `delta in {+1,-1}`.

Cone preservation follows because

\[
X'^2+Y'^2
=\lambda^2T^2-\lambda^2Y^2
=\lambda^2X^2
=T'^2.
\]

The square is

\[
L_{\lambda,\delta}^2(X,Y,T)
=(\lambda^2X,-\lambda^2Y,\lambda^2T)
=\lambda^2R_Y(X,Y,T).
\]

Therefore the condition

\[
L^2=R_Y
\]

forces

\[
\lambda^2=1,
\]

hence

\[
\lambda=\pm1.
\]

Thus there are exactly four such lifts:

\[
\boxed{
L_{\lambda,\delta}(X,Y,T)
=(-\lambda T,\delta i\lambda Y,-\lambda X),
\qquad
(\lambda,\delta)\in\{\pm1\}^2.
}
\]

Explicitly,

\[
\begin{array}{c|c}
(\lambda,\delta)&L_{\lambda,\delta}(X,Y,T)\\ \hline
(+,+)&(-T,+iY,-X)\\
(+,-)&(-T,-iY,-X)\\
(-,+)&(T,-iY,X)\\
(-,-)&(T,+iY,X)
\end{array}
\]

Every one satisfies

\[
\boxed{L_{\lambda,\delta}^2=R_Y,\qquad L_{\lambda,\delta}^4=I.}
\]

Thus each lift generates a `C_4` whose unique involution is `R_Y`.

---

## 3. Affine versus projective classification

On the strict affine section

\[
T-X=1,
\]

arithmetic negation uniquely fixes the `(X,T)` representative

\[
(X,T)\mapsto(-T,-X),
\]

so `lambda=+1`. The only two affine lifts are therefore

\[
\boxed{
L_+=L_{+,+}=(-T,+iY,-X),
\qquad
L_-=L_{+,-}=(-T,-iY,-X).
}
\]

Both square to `R_Y`.

If the signed factor coordinate is treated projectively, multiplication of `(X,T)` by `-1` is allowed and all four lifts occur.

---

## 4. Residual geometric V4 conjugation

After the previously fixed mod-12 identifications, the relevant geometric Klein four is

\[
V_{XY}=\langle R_X,R_Y\rangle
=\{I,R_X,R_Y,R_XR_Y\},
\]

where

\[
R_X=\operatorname{diag}(-1,1,1),\qquad
R_Y=\operatorname{diag}(1,-1,1)
\]

in coordinates `(X,Y,T)`.

Direct conjugation gives

\[
R_YL_{\lambda,\delta}R_Y=L_{\lambda,\delta},
\]

while

\[
R_XL_{\lambda,\delta}R_X
=L_{-\lambda,-\delta}.
\]

The same nontrivial action is obtained from `R_XR_Y` because `R_Y` centralizes every lift.

Hence the four lifts split into exactly two `V_{XY}`-conjugacy classes:

\[
\boxed{
\mathcal C_+
=\{L_{+,+},L_{-,-}\}
}
\]

and

\[
\boxed{
\mathcal C_-
=\{L_{+,-},L_{-,+}\}.
}
\]

The invariant distinguishing them is the actual multiplier of `Y`:

\[
\mu=\delta\lambda i.
\]

For `C_+`,

\[
Y\mapsto+iY,
\]

whereas for `C_-`,

\[
Y\mapsto-iY.
\]

Thus residual real sign reflections cannot conjugate the `+i` quarter-turn into the `-i` quarter-turn.

---

## 5. Effect of the affine normalization

Conjugation by `R_X` changes `lambda -> -lambda`, so it leaves the strict affine representative class `lambda=+1`.

The subgroup of `V_{XY}` preserving the affine normalization is therefore

\[
\langle R_Y\rangle\cong C_2.
\]

But `R_Y` centralizes both affine lifts. Consequently

\[
\boxed{L_+\text{ and }L_-\text{ are not conjugate under the affine-normalization-preserving residual symmetry}.}
\]

They are the two orientation choices for the complex quarter-turn in the `Y` direction.

---

## 6. Relation to cyclotomic i and complex conjugation

The two classes are exchanged by complex conjugation of coefficients:

\[
\overline{L_+}=L_-,
\]

because `i -> -i`.

This is not conjugation by the real residual `V_4`; it is the Galois/antilinear conjugation of the complexified coefficient field.

Once the compatible orientation

\[
i_{\rm cone}=\zeta_{12}^3
\]

is selected, the `+i` versus `-i` class is selected as well. Reversing the complex orientation exchanges the two classes.

Thus the residual classification has a clean interpretation:

\[
\boxed{
\text{two real-}V_4\text{ conjugacy classes}
\leftrightarrow
\text{the two complex orientations }i\leftrightarrow-i.
}
\]

---

## 7. Consequence for the arithmetic sign bit

Arithmetic negation has order two in `U(24)`, but every natural complexified cone lift above has order four:

\[
\boxed{L^2=R_Y\neq I.}
\]

Therefore these maps are not honest representations of the arithmetic sign generator as an order-two cone symmetry. They form a nontrivial lift/extension in which the square of the lifted sign is the already identified `chi_-4` reflection.

Schematically, if `s` denotes a lifted arithmetic-negation generator,

\[
\boxed{s^2=R_Y,\qquad R_Y^2=1,\qquad s^4=1.}
\]

This is a `C_4` lift of the arithmetic `C_2` sign direction, not the direct-product real `C_2` sheet flip used in the explicit v13.528-v13.529 model.

Accordingly:

- the real `U(24) -> C_2^3` map remains an explicit chosen group intertwiner;
- the signed factor coordinates naturally produce a complexified order-four lift instead;
- the two possible lift classes are distinguished by complex orientation;
- pure sheet reversal is not derived from signed factor negation.

---

## 8. Guardrail

The classification above is complete **under the stated lift ansatz**: linear action, projective signed-factor negation on `(X,T)`, scalar action on `Y`, preservation of the complexified quadratic cone, and exact square `R_Y`.

It does not claim classification of arbitrary nonlinear automorphisms of the complex quadric.

The next structural question is whether adjoining this order-four lift to the already present cone reflections produces a familiar finite extension (and how it compares with the cyclotomic `D_8` generated by multiplication by `i` and complex conjugation).