# Cone Derivation Ledger v13.761 — Lane A Basepoint Trace Reduction and Nonresonance Obstruction

Date: 2026-09-24

Lane: A — Screw/Helix–Weil–Hermite–Biehler Program.

Status: [D] exact basepoint-trace reduction; [N] exact obstruction to closing Schur nonresonance from presently established coercivity alone; [C] minimal sufficient nonresonance criterion.

Parents: v13.742, v13.745, v13.758–760. Relevant exact finite transport: v13.667.

## 0. Synchronization and checkpoint instructions

The live ledger was checked immediately before this write: v13.760 is current head, so there is no numbering collision.

v13.760 assigns Lane A first to:
1. derive \(\ell_{0,A},\ell_{1,A}\) as trace/Riesz functionals from the actual finite kernel;
2. obtain their \(A\)-dependence and lower bounds on
\[
|1+M_{00}|,\qquad |1+M_{1x}|.
\]

This entry closes the exact trace-identification half and determines precisely why the desired lower bound does not follow from the currently established bulk coercivity alone.

## 1. Exact basepoint trace realization [D]

Let the finite kernel operator be
\[
(K_Av)(x):=\int_{-A}^{A}k(x,y)v(y)\,dy,
\]
with Suzuki's finite kernel
\[
k(x,y)=g(x-y)-\lambda N(x,y).
\]

The corrected boundary functionals from v13.745 are
\[
\ell_{0,A}(v)
=
\int_{-A}^{A}k(0,y)v(y)\,dy,
\]
\[
\ell_{1,A}(v)
=
\int_{-A}^{A}k_x(0,y)v(y)\,dy.
\]

Therefore, whenever differentiation under the integral is valid,
\[
\boxed{\ell_{0,A}(v)=(K_Av)(0),}
\]
\[
\boxed{\ell_{1,A}(v)=(K_Av)'(0).}
\]

Thus the pair is exactly the two-component basepoint trace
\[
\boxed{
\operatorname{Tr}_0K_A:v\longmapsto
\begin{pmatrix}
(K_Av)(0)\\
(K_Av)'(0)
\end{pmatrix}.
}
\]

No Riesz theorem is needed for this identification.

## 2. Ambient \(L^2\) Riesz representatives [D]

On \(L^2(-A,A)\), define
\[
h_{0,A}(y):=\overline{k(0,y)},
\qquad
h_{1,A}(y):=\overline{k_x(0,y)}
\]
for the convention linear in the first slot (conjugations reverse under the opposite convention).

Then
\[
\boxed{
\ell_{0,A}(v)=\langle v,h_{0,A}\rangle_{L^2},
\qquad
\ell_{1,A}(v)=\langle v,h_{1,A}\rangle_{L^2}.
}
\]

Hence
\[
\boxed{
\|\ell_{0,A}\|_{(L^2)^*}
=
\|k(0,\cdot)\|_{L^2(-A,A)},
}
\]
\[
\boxed{
\|\ell_{1,A}\|_{(L^2)^*}
=
\|k_x(0,\cdot)\|_{L^2(-A,A)}.
}
\]

If the finite energy space \(X_A\) has a continuous embedding
\[
\|v\|_{L^2}\le C_A^{\rm emb}\|v\|_{X_A},
\]
then
\[
\boxed{
\|\ell_{0,A}\|_{X_A^*}
\le
C_A^{\rm emb}\|k(0,\cdot)\|_2,
}
\]
\[
\boxed{
\|\ell_{1,A}\|_{X_A^*}
\le
C_A^{\rm emb}\|k_x(0,\cdot)\|_2.
}
\]

This is the exact finite-energy trace estimate available without identifying the energy-space Riesz representers themselves.

## 3. Reflection diagonalizes the trace map [D]

Under the reflection symmetry already used in v13.745/758, \(K_A\) preserves parity.

For even \(v_+\),
\[
(K_Av_+)'(0)=0.
\]
For odd \(v_-\),
\[
(K_Av_-)(0)=0.
\]

Thus
\[
\boxed{
\operatorname{Tr}_0K_A
=
\ell_{0,A}\oplus\ell_{1,A}
}
\]
is parity diagonal: value trace on the even channel, derivative trace on the odd channel.

With
\[
f_+=\cosh x-1,\qquad f_-=\sinh x-x,
\]
the exact feedback ratios become
\[
\boxed{
r_{0,A}
=
\frac{(K_AR_A^{(+)}f_+)(0)}
{1+(K_AR_A^{(+)}1)(0)},
}
\]
\[
\boxed{
r_{1,A}
=
\frac{(K_AR_A^{(-)}f_-)'(0)}
{1+(K_AR_A^{(-)}x)'(0)}.
}
\]

This is a sharper realization of v13.758's Banach-duality formulas.

## 4. Schur denominators are basepoint boundary-transfer denominators [D]

Define
\[
\mathcal B_{+,A}:=(K_AR_A^{(+)}1)(0),
\]
\[
\mathcal B_{-,A}:=(K_AR_A^{(-)}x)'(0).
\]

Then
\[
\boxed{
d_{0,A}=|1+\mathcal B_{+,A}|=|1+M_{00}|,
}
\]
\[
\boxed{
d_{1,A}=|1+\mathcal B_{-,A}|=|1+M_{1x}|.
}
\]

Therefore the singular cases from v13.745 have an exact trace interpretation:
\[
\boxed{
\mathcal B_{+,A}=-1
\quad\text{or}\quad
\mathcal B_{-,A}=-1.
}
\]

These are finite-\(A\) boundary-feedback resonances.

## 5. What bulk coercivity actually gives [D]

Suppose the corrected finite operator \(\mathcal L_A\) is coercive/invertible on a channel \(X_{A,\pm}\):
\[
\|\mathcal L_A^{-1}\|=\|R_A^{(\pm)}\|\le c_{A,\pm}^{-1}.
\]

Then
\[
|\mathcal B_{+,A}|
\le
\|\ell_{0,A}\|\,\|R_A^{(+)}1\|,
\]
\[
|\mathcal B_{-,A}|
\le
\|\ell_{1,A}\|\,\|R_A^{(-)}x\|.
\]

Consequently the reverse triangle inequality gives the rigorous lower bounds
\[
\boxed{
|1+M_{00}|
\ge
1-
\|\ell_{0,A}\|\,\|R_A^{(+)}1\|,
}
\]
\[
\boxed{
|1+M_{1x}|
\ge
1-
\|\ell_{1,A}\|\,\|R_A^{(-)}x\|.
}
\]

A sufficient quantitative nonresonance condition is therefore
\[
\boxed{
\|\ell_{0,A}\|\,\|R_A^{(+)}1\|\le1-\delta_{0,A},
}
\]
\[
\boxed{
\|\ell_{1,A}\|\,\|R_A^{(-)}x\|\le1-\delta_{1,A},
}
\]
with \(\delta_{j,A}>0\). Then
\[
\boxed{
|1+M_{00}|\ge\delta_{0,A},
\qquad
|1+M_{1x}|\ge\delta_{1,A}.
}
\]

If the \(\delta_{j,A}^{-1}\) grow only subexponentially, this is sufficient for the denominator side of the v13.758 edge criterion.

## 6. Exact obstruction: coercivity alone does not force the needed sign [N]

The presently established coercivity/invertibility of the bulk finite operator controls the size of \(R_A\). It does not determine the sign or phase of the boundary transfers
\[
\ell_{0,A}(R_A^{(+)}1),
\qquad
\ell_{1,A}(R_A^{(-)}x).
\]

In particular, from
\[
\|R_A\|<\infty
\]
alone one cannot conclude
\[
M_{00}\ge0,\qquad M_{1x}\ge0,
\]
nor
\[
M_{00}>-1,\qquad M_{1x}>-1.
\]

Therefore the hoped-for unconditional statement
\[
|1+M_{00}|,\ |1+M_{1x}|\ge c>0
\]
does NOT follow from the currently established bulk coercivity alone.

This is the precise obstruction:
\[
\boxed{
\text{bulk coercivity controls response size but not the boundary-feedback sign.}
}
\]

A positivity conclusion would require an additional theorem identifying the boundary functionals with positive-compatible energy-space Riesz representatives or an independent monotonicity/sign identity for the basepoint traces.

## 7. Why the helix/Weil carrier cannot repair this by itself [N]

v13.753–754 transport the bulk form and boundary triple without changing the Weyl data. But v13.742 already showed that twice differentiating loses the affine boundary constants.

The present trace formulas make this concrete:
\[
\mathcal B_{+,A}=(K_AR_A^{(+)}1)(0),
\qquad
\mathcal B_{-,A}=(K_AR_A^{(-)}x)'(0).
\]

These are point/derivative traces after the finite response solve. They are not determined by the full-line spectral current alone.

Hence:
\[
\boxed{
\text{helix/Weil bulk spectral control}
\not\Rightarrow
\text{Schur nonresonance}.
}
\]

The boundary trace must be controlled separately.

## 8. Relation to the exact finite continuous-kernel transport [I/G]

v13.667 established the exact finite continuous-kernel transport and Weyl-function invariance. However, the later source correction v13.742 warns against replacing Suzuki's actual Section-8 deficiency vectors by a naive specialization of the generic inverse-source solve.

Accordingly, the present entry uses \(R_A=\mathcal L_A^{-1}\) only in the corrected v13.745 moment system and does NOT infer a new deficiency-source identity.

This keeps the trace reduction source-faithful.

## 9. Consequence for Lane A gate A.3.1

The first half of A.3.1 is closed exactly:
\[
\boxed{
\ell_{0,A}=\operatorname{ev}_0\circ K_A,
\qquad
\ell_{1,A}=\operatorname{ev}_0\circ\partial_xK_A,
}
\]
with explicit ambient \(L^2\) Riesz representatives \(k(0,\cdot)\) and \(k_x(0,\cdot)\).

The denominator half is reduced to a sharp conditional criterion:
\[
\boxed{
\|\ell_{0,A}\|\,\|R_A^{(+)}1\|<1,
\qquad
\|\ell_{1,A}\|\,\|R_A^{(-)}x\|<1
}
\]
(or any independent sign/monotonicity theorem excluding \(-1\)).

But it is NOT unconditionally closed from present data.

Thus A.3.1 has moved from an undefined trace problem to the concrete task of estimating two explicit basepoint boundary transfers.

## 10. Next gate

Compute or bound, from Suzuki's actual finite kernel,
\[
\|k(0,\cdot)\|_2,\qquad
\|k_x(0,\cdot)\|_2,
\]
together with coercivity/resolvent estimates for
\[
R_A^{(+)}1,\qquad R_A^{(-)}x.
\]

In parallel, search the finite boundary-triple characteristic for an identity that identifies
\[
1+M_{00},\qquad1+M_{1x}
\]
with nonvanishing characteristic values or derivatives. Such an identity would be stronger than the norm criterion and could prove nonresonance without requiring the products above to be \(<1\).

Until one of these two routes closes, the correct status is:
\[
\boxed{
\text{trace realization proved; quantitative Schur nonresonance remains open.}
}
