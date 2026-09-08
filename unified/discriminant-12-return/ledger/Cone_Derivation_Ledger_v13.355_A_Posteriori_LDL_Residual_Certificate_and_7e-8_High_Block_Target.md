# Cone Derivation Ledger v13.355

## A posteriori LDL residual certificate and the 7e-8 high-block target

### Purpose

The naive interval implementation of the exact generator LDL recurrence from
v13.354 suffers severe dependency inflation: repeated reuse of the same
uncertain generator entries widens interval pivots rapidly even when the
midpoint recurrence is numerically stable.

This checkpoint replaces forward interval propagation by an a posteriori
factor certificate.

---

## 1. Shifted finite high block

Let

\[
B:=A_{0,[21,16001]}-0.22I.
\]

The midpoint diagnostics are

\[
\lambda_{\min}(A_{0,[21,16001]})\approx0.227114802018,
\]

and the exact generator LDL recurrence gives

\[
\min_j d_j^{LDL}\approx0.25429962365.
\]

---

## 2. Residual certificate

Let a point factorization provide a unit lower triangular \(L\) and diagonal
\(D\), and define

\[
E:=B-LDL^T.
\]

Then

\[
L^{-1}BL^{-T}=D+L^{-1}EL^{-T}.
\]

Hence

\[
\lambda_{\min}(L^{-1}BL^{-T})
\ge d_{\min}-\|L^{-1}EL^{-T}\|_2.
\]

A sufficient condition for \(B\succ0\) is therefore

\[
\boxed{
\|E\|_2<\frac{d_{\min}}{\|L^{-1}\|_2^2}.
}
\]

This converts positivity into two independent a posteriori checks:

1. a lower bound for \(d_{\min}\);
2. a norm bound for \(L^{-1}\);
3. a global factor residual bound \(\|E\|_2\).

No interval Schur recursion is required.

---

## 3. Cheap inverse-factor bound

For unit lower triangular \(L\), define recursively

\[
y_i=1+\sum_{j<i}|L_{ij}|y_j.
\]

Forward-substitution induction gives

\[
\|L^{-1}\|_\infty\le\max_i y_i.
\]

The midpoint structured factorization gives

\[
\boxed{
\max_i y_i\approx21.22011808.
}
\]

Using only the crude dimension inequality

\[
\|L^{-1}\|_2
\le\sqrt{7991}\,\|L^{-1}\|_\infty,
\]

one obtains

\[
\boxed{
\|L^{-1}\|_2\lesssim1.897\times10^3.
}
\]

This is intentionally very loose.

---

## 4. Explicit residual target

With

\[
d_{\min}\approx0.25429962365,
\]

and the crude inverse bound above,

\[
\frac{d_{\min}}{\|L^{-1}\|_2^2}
\approx
\boxed{7.07\times10^{-8}}.
\]

Therefore the finite high-block proof can close if the completed point factor
satisfies the outward-rounded residual estimate

\[
\boxed{\|B-LDL^T\|_2<7\times10^{-8}}.
\]

This tolerance is very loose compared with the rational/transcendental entry
precision already available from the v13.339-v13.343 construction.  The prime,
cusp, archimedean, and pole-free finite entries can be enclosed at scales far
below \(10^{-10}\), and the scalar series can be extended arbitrarily if more
margin is desired.

---

## 5. Why this is preferable to naive interval LDL

A direct interval generator recurrence couples the same uncertain generator
variables through thousands of Schur steps and therefore suffers dependency
blow-up.  That widening does not reflect actual numerical instability.

The a posteriori route instead:

1. computes a high-precision point structured factorization;
2. treats \(L,D\) as a fixed proof object;
3. verifies only the final factor residual and inverse-factor norm.

This separates numerical construction from rigorous validation and avoids the
main dependency mechanism.

---

## 6. Global consequence if closed

If the v13.355 residual certificate proves

\[
A_{0,[21,16001]}\succeq0.22I,
\]

then together with the current rounded global targets

\[
\|G_{[21,16001],[16003,\infty)}\|<1,
\]

and

\[
A_{0,[16003,\infty)}\succeq4.67326749I,
\]

one obtains

\[
A_0|_{\mathcal D}
\succeq
\left(0.22-\frac1{4.67326749}\right)I
>6\times10^{-3}I.
\]

That would finally prove the entire pole-free high complement positive and
reduce the infinite inertia problem rigorously to the ten low modes.  The PSD
pole may then be restored without harming positivity.

---

## Guardrails

- The current \(d_{\min}\) and inverse-factor bound are midpoint diagnostics.
- The \(7\times10^{-8}\) target is a sufficient-condition design value, not yet
  a completed residual certificate.
- No high-complement positivity theorem is claimed until the residual and
  inverse-factor estimates are outward certified.
- No exact-zero, \(\lambda_1=0\), RH, or GRH conclusion follows.
