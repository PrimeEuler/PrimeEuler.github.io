# Cone Derivation Ledger v13.377 — Asymptotically Centered Corrected Arch Generator Gauge

Date: 2026-09-09

Status labels: **[D]** exact derived, **[N]** midpoint numerical, **[Diag]** numerical conditioning diagnostic, **[O]** open.

## 1. Corrected arch generator and an exact gauge freedom

After the Audit-Round-20 correction,

\[
K_{\rm arch}(m,n)
=\pi mn\frac{Y_n-Y_m}{m^2-n^2},
\qquad
Y_n=nH_n.
\]

A displacement pair is

\[
p_n=n,
\qquad
q_n=nY_n.
\]

For any constant `c`, replace

\[
q_n\mapsto q_n-cp_n=n(Y_n-c).
\]

Then

\[
p_m(q_n-cp_n)-(q_m-cp_m)p_n
=p_mq_n-q_mp_n.
\]

Therefore:

\[
\boxed{
q\mapsto q-cp
\text{ is an exact generator gauge transformation.}
}
\]

The represented matrix is unchanged exactly.

## 2. [D] Natural asymptotic center

Put

\[
b=\frac{n\pi}{2},
\qquad
H_n=\int_0^2h(t)\sin(bt)\,dt,
\]

with odd `n`.  Integration by parts gives

\[
H_n
=\frac{h(0)-h(2)\cos(2b)}{b}
+\frac1b\int_0^2h'(t)\cos(bt)\,dt.
\]

Since

\[
\cos(2b)=\cos(n\pi)=-1,
\]

and the sine endpoint term in a second integration by parts vanishes,

\[
H_n=\frac{h(0)+h(2)}{b}+O(b^{-3}).
\]

Hence

\[
Y_n=nH_n
=\frac2\pi\bigl(h(0)+h(2)\bigr)+O(n^{-2}).
\]

Now

\[
h(0)=\frac14,
\]

and

\[
h(2)=\frac{e^{-1}}{1-e^{-4}}-\frac14.
\]

Thus the exact natural center is

\[
\boxed{
c_\infty
=\frac2\pi\frac{e^{-1}}{1-e^{-4}}
}
\]

with midpoint

\[
\boxed{c_\infty\approx0.2385688673212266}.
\]

Define

\[
\widetilde Y_n=Y_n-c_\infty.
\]

Then

\[
\widetilde Y_n=O(n^{-2}),
\]

so the centered generator

\[
\boxed{\widetilde q_n=n\widetilde Y_n}
\]

satisfies

\[
\boxed{\widetilde q_n=O(n^{-1})},
\]

whereas the raw generator `q_n=nY_n` grows like `O(n)`.

## 3. [N] Size reduction on the finite high block

The degree-65 arch scalar reconstruction gives

\[
Y_{16001}^{\rm mid}\approx0.23856886737245636.
\]

Across odd modes `21..16001`, the centered generator satisfies numerically

\[
\boxed{
\max_n|n(Y_n-c_\infty)|\approx6.25\times10^{-4}.
}
\]

The raw generator at the upper end is of order

\[
nY_n\sim3.8\times10^3.
\]

So the gauge removes a huge artificial scale without changing one matrix entry.

## 4. [Diag] Direct replay conditioning test

As a deliberately lower-precision diagnostic, a float64 point factor was replayed with a long-double checker using the corrected v13.375 local-defect formula.

With the raw arch generator gauge,

\[
\sum_k\delta_k^{\rm raw}\approx1.3031\times10^{-4}.
\]

With the exact asymptotic-centered gauge,

\[
\boxed{
\sum_k\delta_k^{\rm centered}\approx1.7932\times10^{-8}.
}
\]

This is a reduction by roughly

\[
\boxed{7.3\times10^3}.
\]

These values are **not** the final long-double/outward-rounded certificate.  Their purpose is to identify and remove the numerical ill-conditioning introduced by the raw rank-four generator representation.

## 5. Structural consequence for the far tail

The same centered gauge is useful beyond LDL.  The corrected arch component no longer needs to be treated through an `O(n)` generator with large cancellation.  Its nontrivial scalar channel is now explicitly decaying:

\[
\widetilde q_n=O(n^{-1}).
\]

This should make the repaired finite-to-tail cross estimate substantially cleaner: the new arch channel behaves as a genuine decaying moment channel, while the constant asymptotic part has been gauged away exactly.

## 6. Next target

Use the centered gauge for the full corrected arithmetic replay:

1. generate high-precision nominal scalar data;
2. cast/store the point factor in the intended long-double model;
3. replay each step with the corrected rank-four local checker;
4. validate `d_min`, `y_max`, factor-growth norms and `sum delta_k`;
5. compare total residual against the fresh v13.376 allowance.

Then carry the same centered generator into the corrected cross/tail certificate.

## Guardrail

The gauge identity and asymptotic center are exact derived facts.  The displayed local-defect reduction is a conditioning diagnostic only.  The corrected finite high-block positivity certificate remains open until the full validated arithmetic transcript is produced.  The infinite high complement and `S_10` remain downstream.  No exact-zero, RH, or GRH claim follows.
