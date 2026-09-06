# Cone Derivation Ledger v13.273 — Exact Single-Prime Form Variation and Fredholm Linearity No-Go

Date: 2026-09-06

Status: EXACT SINGLE-PRIME FORM DERIVATION + EXACT ADDITIVE-FREDHOLM NO-GO — RH/GRH NOT PROVED

## 0. Synchronization and source audit

Immediately before this write, the authoritative project README, current `master` tip, and highest ledger state were re-fetched.

The current tip remained

`a42239a345f99d79623af7db0d17811bb6c6e90e`,

with v13.272 the highest project checkpoint. The external auditor's v13.271 round-10 audit remains immediately upstream and verified v13.262–v13.270 with no mathematical errors.

No v13.273 file existed at synchronization time.

This entry executes the one-prime diagnostic proposed at the end of v13.272 using Suzuki's actual screw-kernel structure.

Source check:

Masatoshi Suzuki, “Aspects of the screw function corresponding to the Riemann zeta-function,” *J. London Math. Soc.* 108 (2023), 1448–1487, DOI `10.1112/jlms.12785`.

Suzuki decomposes the zeta screw function as

\[
g=g_0+g_1+g_\infty,
\]

with prime part

\[
\boxed{
 g_1(t)
 =
 \sum_{n\le e^{|t|}}
 \frac{\Lambda(n)}{\sqrt n}
 (|t|-\log n)
 }
\]

and screw kernel

\[
G_g(t,u)=g(t-u)-g(t)-g(-u)+g(0).
\]

Suzuki's 2026 operator paper identifies the localized Weil operator as the Friedrichs extension of a symmetric operator of the form

\[
B_a=D^*G_aD
\]

on `H_0^1(-a,a)`.

The purpose here is to compute exactly what one single prime-power ramp contributes to that form.

---

## 1. One ramp and its screw kernel

Fix

\[
0<v<2a
\]

and define the elementary ramp

\[
\boxed{
r_v(t):=(|t|-v)_+.
}
\]

For a real coefficient `c`, define

\[
g_{v,c}(t):=c\,r_v(t).
\]

Its screw kernel is

\[
\boxed{
G_{v,c}(t,u)
=
c\,[r_v(t-u)-r_v(t)-r_v(-u)+r_v(0)].
}
\]

Since `v>0`,

\[
r_v(0)=0,
\]

and because `r_v` is even,

\[
G_{v,c}(t,u)
=
c\,[r_v(t-u)-r_v(t)-r_v(u)].
\]

Distributionally,

\[
\boxed{
r_v''(x)=\delta(x-v)+\delta(x+v).
}
\]

Therefore the mixed derivative of the screw kernel is

\[
\boxed{
\partial_t\partial_uG_{v,c}(t,u)
=-c\,[\delta(t-u-v)+\delta(t-u+v)].
}
\]

The anchored subtraction terms `-r_v(t)` and `-r_v(u)` disappear under the mixed derivative.

This fact is important: at the `D^*GD` form level, the screw anchoring does **not** itself introduce an overlap normalization.

---

## 2. Exact form variation on `H_0^1(-a,a)`

Let

\[
I_a=[-a,a],
\qquad
f\in H_0^1(I_a).
\]

The one-ramp contribution to Suzuki's form is

\[
q_{v,c}[f]
:=
\int_{I_a}\!\int_{I_a}
G_{v,c}(t,u)
 f'(u)\overline{f'(t)}\,du\,dt.
\]

Because `f` vanishes at the endpoints, integration by parts in `u` and `t` produces no boundary terms. Hence

\[
q_{v,c}[f]
=
\int_{I_a}\!\int_{I_a}
\partial_t\partial_uG_{v,c}(t,u)
 f(u)\overline{f(t)}\,du\,dt.
\]

Substituting the distributional derivative gives

\[
\boxed{
q_{v,c}[f]
=
-c
\int_{-a+v}^{a}
f(x-v)\overline{f(x)}\,dx
-c
\int_{-a}^{a-v}
f(x+v)\overline{f(x)}\,dx.
}
\]

Define the truncated shift

\[
(S_{a,v}f)(x)
=
\mathbf1_{I_a}(x)\mathbf1_{I_a}(x-v)f(x-v).
\]

Then `S_{a,v}^*=S_{a,-v}`, and the exact operator-form identity is

\[
\boxed{
q_{v,c}[f]
=
-c\,
\langle (S_{a,v}+S_{a,v}^*)f,f\rangle.
}
\]

Thus the elementary prime-power perturbation of `D^*GD` is not merely “schematically shift-like.” It is exactly the symmetric truncated translation pair on the form core.

For the D12 Dedekind field channel,

\[
c_n=
\frac{b_K(n)}{\sqrt n},
\qquad
b_K(n)=\Lambda(n)(1+\chi_{12}(n))\ge0,
\]

and

\[
v_n=\log n.
\]

Hence the finite arithmetic perturbation on the common form core is

\[
\boxed{
V_{K,a}
=
-\sum_{\log n\le2a}
\frac{b_K(n)}{\sqrt n}
\bigl(S_{a,\log n}+S_{a,\log n}^*\bigr).
}
\]

This removes the coefficient-normalization ambiguity left in v13.272.

---

## 3. Consequence for the one-prime first variation

Let `A_{\infty,a}` denote an archimedean reference realization, and suppose for the present calculation that

\[
R_{\infty,a}(w)
:=(A_{\infty,a}+w)^{-1}
\]

is trace class.

Turn on one prime-power ramp with coupling parameter `epsilon`:

\[
A_{a}^{(v)}(\epsilon)
=
A_{\infty,a}
+\epsilon V_{v,c},
\]

where

\[
V_{v,c}
=-c(S_{a,v}+S_{a,v}^*).
\]

The relative Fredholm determinant is

\[
\Delta_{a,v}(w;\epsilon)
=
\det\!\left(
I+\epsilon
R_{\infty,a}(w)^{1/2}
V_{v,c}
R_{\infty,a}(w)^{1/2}
\right).
\]

Its first variation at zero is

\[
\boxed{
\frac{\partial}{\partial\epsilon}
\log\Delta_{a,v}(w;\epsilon)
\Big|_{\epsilon=0}
=
\operatorname{Tr}
\bigl(R_{\infty,a}(w)V_{v,c}\bigr).
}
\]

Therefore

\[
\boxed{
\frac{\partial}{\partial\epsilon}
\log\Delta_{a,v}(w;\epsilon)
\Big|_{0}
=
-c\,
\operatorname{Tr}
\left[R_{\infty,a}(w)(S_{a,v}+S_{a,v}^*)\right].
}
\]

If the reference resolvent has integral kernel `R_{\infty,a}(x,y;w)`, then

\[
\boxed{
\operatorname{Tr}
\left[R_{\infty,a}(w)(S_{a,v}+S_{a,v}^*)\right]
=
2\,\Re
\int_{-a+v}^{a}
R_{\infty,a}(x,x-v;w)\,dx.
}
\]

Thus the exact one-prime diagnostic is an off-diagonal resolvent sum rule.

---

## 4. Exact Euler coefficient demanded by D12

Set

\[
w=\kappa^2,
\qquad \kappa>\frac12.
\]

The D12 finite Euler relative trace from v13.270 is

\[
\mathcal R_{K,a}^{E}(\kappa^2)
=
-\frac1\kappa
\sum_{\log n\le2a}
\frac{b_K(n)}{n^{1/2+\kappa}}.
\]

For one prime power with

\[
v=\log n,
\qquad
c=\frac{b_K(n)}{\sqrt n},
\]

the desired first-order contribution is

\[
\boxed{
-\frac{c}{\kappa}e^{-\kappa v}.
}
\]

Comparing with the exact form variation above, a Fredholm realization would therefore require

\[
\boxed{
\operatorname{Tr}
\left[R_{\infty,a}(\kappa^2)
(S_{a,v}+S_{a,v}^*)\right]
=
\frac1\kappa e^{-\kappa v}.
}
\]

Equivalently,

\[
\boxed{
\Re
\int_{-a+v}^{a}
R_{\infty,a}(x,x-v;\kappa^2)\,dx
=
\frac{1}{2\kappa}e^{-\kappa v}.
}
\]

This is the precise single-prime sum rule that the actual archimedean reference resolvent would need to satisfy.

For the compressed free resolvent of v13.272,

\[
R_{a,\kappa}(x,y)
=
\frac1{2\kappa}e^{-\kappa|x-y|},
\]

the left side is

\[
\frac{2a-v}{2\kappa}e^{-\kappa v},
\]

so the required identity fails by the exact overlap factor `2a-v`, recovering v13.272.

The new point is that the criterion is now exact for Suzuki's actual form normalization: any cancellation must come from the nontrivial archimedean reference resolvent itself, not from the prime ramp, not from the screw anchoring, and not from hidden endpoint terms on `H_0^1`.

---

## 5. A stronger obstruction: additive Fredholm determinants are nonlinear in prime couplings

The one-prime test reveals a second, more structural issue.

Let

\[
K:=R_0(w)^{1/2}VR_0(w)^{1/2}
\in\mathfrak S_1
\]

be self-adjoint and nonzero. For sufficiently small real `epsilon`,

\[
\log\det(I+\epsilon K)
=
\sum_{m\ge1}
\frac{(-1)^{m+1}}{m}
\epsilon^m\operatorname{Tr}(K^m).
\]

Hence

\[
\boxed{
\frac{d}{d\epsilon}\log\det(I+\epsilon K)\Big|_0
=\operatorname{Tr}K,
}
\]

but also

\[
\boxed{
\frac{d^2}{d\epsilon^2}\log\det(I+\epsilon K)\Big|_0
=-\operatorname{Tr}(K^2).
}
\]

Because `K` is self-adjoint,

\[
\operatorname{Tr}(K^2)=\|K\|_2^2\ge0,
\]

with equality iff `K=0`.

Therefore any nontrivial additive self-adjoint perturbation has strictly negative second logarithmic variation:

\[
\boxed{
K\ne0
\Longrightarrow
\frac{d^2}{d\epsilon^2}\log\det(I+\epsilon K)\Big|_0<0.
}
\]

---

## 6. Why this conflicts with a literal Euler-log coupling model

The finite Euler logarithm is additive over prime powers:

\[
L_{K,2a}(s)
=
\sum_{\log n\le2a}
\frac{b_K(n)}{\log n}\,n^{-s}.
\]

Introduce independent formal amplitudes `epsilon_n`:

\[
L_{K,2a}(s;\epsilon)
=
\sum_{\log n\le2a}
\epsilon_n
\frac{b_K(n)}{\log n}\,n^{-s}.
\]

Then the target relative determinant is

\[
\boxed{
\mathcal Z_E(s;\epsilon)
=
\exp\bigl(2L_{K,2a}(s;\epsilon)\bigr).
}
\]

Its logarithm is exactly linear in every independent coupling:

\[
\boxed{
\frac{\partial^2}{\partial\epsilon_n^2}
\log\mathcal Z_E(s;\epsilon)
=0,
}
\]

and for distinct `m,n`,

\[
\boxed{
\frac{\partial^2}{\partial\epsilon_m\partial\epsilon_n}
\log\mathcal Z_E(s;\epsilon)
=0.
}
\]

By contrast, an additive operator model

\[
A(\epsilon)
=
A_0+\sum_n\epsilon_nV_n
\]

produces

\[
\frac{\partial^2}{\partial\epsilon_m\partial\epsilon_n}
\log\Delta(\epsilon;w)\Big|_0
=
-\operatorname{Tr}(K_mK_n),
\]

where

\[
K_n=R_0(w)^{1/2}V_nR_0(w)^{1/2}.
\]

In particular,

\[
\boxed{
\frac{\partial^2}{\partial\epsilon_n^2}
\log\Delta(\epsilon;w)\Big|_0
=-\|K_n\|_2^2<0
}
\]

for every nonzero self-adjoint prime perturbation.

Therefore:

\[
\boxed{
\text{a literal Euler determinant cannot be exactly the Fredholm determinant of a linearly additive, independently coupled self-adjoint prime-ramp perturbation.}
}
\]

This is an exact local no-go theorem.

It is stronger than the overlap-factor obstruction because it does not depend on the free model or on the detailed form of the reference resolvent.

---

## 7. Scope of the no-go

The result does **not** rule out all spectral realizations of the Euler product.

It rules out the specific ansatz

\[
A(\epsilon)
=
A_0+\sum_n\epsilon_nV_n
\]

combined with an exact identity

\[
\det_{\rm rel}A(\epsilon)
=
\exp\left(\sum_n\epsilon_n\ell_n\right)
\]

for independently variable amplitudes.

Possible escapes include:

1. a nonlinear dependence of the operator/boundary condition on the arithmetic couplings;
2. a multiplicative transfer/scattering construction in which Euler factors are primitive objects;
3. a boundary characteristic function rather than a bulk Fredholm determinant;
4. a limit in which higher connected Fredholm traces vanish asymptotically, rather than identically;
5. a de Branges/canonical-system realization where the arithmetic enters the Hamiltonian nonlinearly.

The no-go therefore tells us where **not** to spend effort: trying to force the fixed prime ramps into an exact independent additive Fredholm-Euler dictionary.

---

## 8. Strategic consequence: pivot from bulk relative determinant to boundary characteristic data

The previous chain was

\[
\text{prime ramps}
\to
D^*GD
\to
\text{bounded shifts}
\to
\text{trace-class sandwich}
\to
\det(I+K_a).
\]

The first three arrows are now exact.

But the fourth/fifth combination encounters two independent obstructions:

\[
\boxed{
\text{bulk overlap factor}
}
\]

and

\[
\boxed{
\text{nonzero quadratic Fredholm cumulants}.
}
\]

Therefore the bulk relative-Fredholm route should be downgraded from the primary path.

The better target is Suzuki's boundary characteristic-entire-function / de Branges side, where self-adjoint extension eigenvalues are zeros of a scalar entire boundary function and the arithmetic dependence need not be linearly additive at operator level.

This aligns with v13.268–v13.269, where the exact arithmetic target was already identified as

\[
\boxed{
\Psi_K(w)=\xi_K\!\left(\frac12+\sqrt w\right),
}
\]

an order-`1/2`, genus-zero entire function.

The revised frontier is therefore

\[
\boxed{
\text{localized D12 screw form}
\to
\text{boundary/de Branges characteristic function}
\stackrel{?}{\longrightarrow}
\Psi_K(w)
}
\]

rather than

\[
\text{additive prime ramps}
\to
\text{exact Euler Fredholm determinant}.
\]

---

## 9. Next concrete calculation

The next high-value step is to source-audit Suzuki's finite characteristic entire function `W(a,theta;z)` and its relation to the nonlocal self-adjoint first-order extension.

The exact question is:

\[
\boxed{
\text{what is the first variation of the boundary characteristic function itself under one prime ramp?}
}
\]

Unlike the bulk Fredholm determinant, a boundary characteristic function can absorb nonlinear dependence through the extension parameter / transfer matrix.

We should derive:

1. the exact finite D12 analog of Suzuki's `W(a,theta;z)`;
2. its Hadamard/H4 covariance in the principal/quadratic pair;
3. its fold
   \[
   \mathcal W_{K,a}(w)=W_{K,a}(i\sqrt w)W_{K,a}(-i\sqrt w);
   \]
4. the one-prime variation of `log W`, not `log det(I+K)`;
5. whether the large-`a` boundary characteristic ratio can converge to
   \[
   \Psi_K(w)^2
   \]
   without violating the Fredholm cumulant no-go.

If this works, the Laguerre–Pólya closure from v13.269 becomes the main RH/GRH frontier again.

---

## 10. Guardrails

No RH/GRH conclusion is proved.

The exact new results are:

\[
\boxed{
q_{v,c}[f]
=-c\langle(S_{a,v}+S_{a,v}^*)f,f\rangle
}
\]

for one Suzuki prime ramp on `H_0^1`, and

\[
\boxed{
K\ne0
\Longrightarrow
\partial_\epsilon^2\log\det(I+\epsilon K)|_0
=-\operatorname{Tr}(K^2)<0.
}
\]

Therefore a literal independently linear Euler log cannot equal the logarithm of an additive self-adjoint Fredholm determinant in a neighborhood of zero coupling.

The boundary/de Branges characteristic-function route remains open and is now the preferred continuation.