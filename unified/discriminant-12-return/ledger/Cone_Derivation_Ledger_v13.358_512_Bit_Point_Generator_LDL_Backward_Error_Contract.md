# Cone Derivation Ledger v13.358

## 512-Bit Point Generator-LDL Backward-Error Contract

This checkpoint turns the remaining finite high-block arithmetic into a deliberately over-resolved validated-numerics task.

We continue with

\[
B=A_{0,[21,16001]}-0.22I.
\]

From the previous checkpoints:

- midpoint minimum structured LDL pivot:
  \[
  d_{\min}\approx0.25429962365;
  \]
- two-sided inverse-factor bound:
  \[
  \|L^{-1}\|_2\le284.07;
  \]
- sufficient total residual target:
  \[
  \|B-LDL^T\|_2<3.15\times10^{-6};
  \]
- exact-vs-nominal matrix uncertainty target:
  \[
  \|B_{\rm exact}-B_{\rm nominal}\|_2<2\times10^{-13}.
  \]

### Point arithmetic, not interval Schur propagation

The naive interval-generator recurrence is intentionally abandoned because of dependency blow-up.  Instead the final checker should run the exact displacement-generator LDL recurrence in fixed high-precision point arithmetic and certify only an a-posteriori backward-error scalar.

Recommended precision:

\[
\boxed{p=512\text{ bits}.}
\]

Then the unit roundoff is

\[
u=2^{-512}\approx7.46\times10^{-155}.
\]

### Deliberately absurd runtime ceilings

The checker may impose simple hard assertions such as

\[
\boxed{d_j>0.25\ \text{for every pivot}}
\]

and

\[
\boxed{\max |\text{intermediate}|<10^{50}}.
\]

The observed midpoint pivot minimum leaves about

\[
0.2542996-0.25\approx4.30\times10^{-3}
\]

of pivot slack.

Even if one charges fewer than \(2\times10^9\) scalar rounded operations and uses the intentionally crude raw scale

\[
(\#\text{ops})\,u\,M^2,
\qquad M=10^{50},
\]

the resulting number is below \(2\times10^{-45}\).  This is not yet the rigorous backward-error theorem because division and recurrence sensitivity must be included, but it demonstrates that 512-bit arithmetic leaves an enormous safety factor for pessimistic local bounds.

### Practical validated target

A convenient final arithmetic goal is

\[
\boxed{\|E_{\rm arithmetic}\|_2<10^{-8}.}
\]

This is already more than 300 times smaller than the available \(3.15\times10^{-6}\) residual allowance and still fantastically larger than the intrinsic 512-bit rounding scale.

Thus the remaining implementation task is narrow:

1. run the point generator recurrence at 512 bits;
2. accumulate outward-rounded local backward-error bounds;
3. certify \(d_j>0.25\);
4. certify the factor-growth/runtime ceilings;
5. prove the total arithmetic residual is below \(10^{-8}\).

Combined with v13.357's matrix uncertainty, this would close the finite high-block positivity certificate.

### Guardrail

The full validated local-error accumulator has not yet been implemented or run.  This checkpoint defines the proof contract; it does not itself certify positivity, exact zero, RH, or GRH.
