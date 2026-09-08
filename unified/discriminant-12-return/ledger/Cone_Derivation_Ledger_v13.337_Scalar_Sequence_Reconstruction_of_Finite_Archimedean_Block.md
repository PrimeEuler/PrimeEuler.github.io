# Cone Derivation Ledger v13.337 — Scalar-Sequence Reconstruction of the Finite Archimedean Block

## Main reduction

The finite archimedean matrix does not require an independent quadrature for every pair of modes.

For odd \(m\ne n\), v13.321 gives

\[
\boxed{
(K_{\rm arch})_{mn}
=-\frac4\pi\frac{nH_m-mH_n}{n^2-m^2},
}
\]

where

\[
H_j=\int_0^2h(t)\sin\!\left(\frac{j\pi t}{2}\right)dt.
\]

Thus every off-diagonal entry is algebraically reconstructed from the scalar sequence \(\{H_j\}\).

For the diagonal define

\[
D_n
=-\int_0^2h(t)
\left[
(2-t)\cos\!\left(\frac{n\pi t}{2}\right)
+
\frac{\sin(n\pi t/2)}{n\pi/2}
\right]dt.
\]

Then \((K_{\rm arch})_{nn}=D_n\).

## Finite N=155 count

The finite modes are

\[
1,3,\ldots,153,
\]

so there are exactly 77 odd modes.

Therefore the entire symmetric \(77\times77\) smooth archimedean block is determined by only

\[
\boxed{77\ H_n\text{ values}+77\ D_n\text{ values}=154\text{ scalar integrals}.}
\]

This replaces roughly three thousand independent pairwise matrix integrals.

## Pole term also closes analytically

For the even-v odd-Dirichlet sector the pole vector is

\[
c_n=\langle\psi_n,\cosh(x/2)\rangle
=\frac{2k_n\cosh(1/2)}{k_n^2+1/4},
\qquad k_n=\frac{n\pi}{2},
\]

and

\[
P_{\rm pole}=2cc^T\ge0.
\]

Thus no numerical integration is needed for the pole contribution either.

## Certification consequence

At N=155 the full finite assembly now decomposes into:

1. cusp: explicit Si/Ci formulas;
2. prime: explicit five-frequency trigonometric formulas;
3. archimedean: 154 outward-rounded scalar integrals followed by exact algebraic reconstruction;
4. pole: exact closed-form rank one, or omit entirely for lower-bound work.

The continuous verification workload is therefore one-dimensional and sequence-based.

This is especially useful for the high-accuracy residual-certified solve of v13.335: the same verified scalar sequences can be reused in every matrix-vector product and residual evaluation.

## Guardrails

The scalar integrals still require rigorous outward enclosure.  Reconstructing the matrix algebraically does not by itself make the numerical values rigorous.  No exact zero, positivity theorem, lambda_1=0, RH, or GRH conclusion follows.

## Next target

Exploit the scalar-sequence representation in the residual computation itself.  Instead of assembling a high-precision dense 77x77 matrix, evaluate the ten residual columns using verified H_n and D_n sequences plus the explicit prime/cusp formulas.  Combine this with the v13.336 Weyl criterion to target a total 10x10 operator enclosure below 2e-8, sufficient to certify the four-dimensional terminal obstruction.