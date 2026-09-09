# Cone Derivation Ledger v13.363 — Validated \(\|B_{\rm prime}\|<2.05\)

## Result

The robust target introduced in v13.346 is now closed under the same validated-computational standard used for the finite high block:

\[
\boxed{\|B_{\rm prime}\|<2.05}.
\]

Let

\[
A=-B_{\rm prime}.
\]

The kernel of \(A\) is nonnegative and symmetric, so for every positive integer \(k\),

\[
\|A\|\le \sup_x(A^k1)(x)^{1/k}.
\]

Piecewise-constant functions remain piecewise constant under \(A\), hence the \(k=16\) estimate reduces to a finite breakpoint sweep.

## Deliberately coarse validation envelopes

The exact logarithm shifts were enclosed by the rational atanh series. Their actual radii are at the \(10^{-50}\) scale, but the combinatorial certification deliberately allows

\[
\boxed{r_{\rm shift}=10^{-8}}.
\]

Similarly, exact prime weights were enclosed using rational log bounds and integer-square-root bracketing. The final positive-kernel sweep deliberately inflates every weight by

\[
\boxed{10^{-6}}.
\]

These envelopes are vastly larger than the actual transcendental enclosure widths.

At depth 16 the finite geometry has

\[
3345
\]

constant intervals. The minimum point-geometry source-boundary lookup clearance is

\[
\boxed{4.759731185477456\times10^{-5}},
\]

and the minimum breakpoint spacing is

\[
\boxed{9.519462370954912\times10^{-5}}.
\]

A coarse depth-16 uncertainty envelope is only

\[
33\,r_{\rm shift}=3.3\times10^{-7},
\]

so neither breakpoint order nor any source-cell lookup can change under the certified shift intervals.

## Positive-kernel upper sweep

With all five prime weights inflated upward by \(10^{-6}\), the depth-16 positive recurrence gives

\[
\boxed{\sup_x(A^{16}1)(x)<93390.833}.
\]

On the other hand,

\[
2.05^{16}=97288.5603556106\ldots
\]

so the absolute slack exceeds

\[
\boxed{3897.7}.
\]

Therefore

\[
\sup_x(A^{16}1)(x)<2.05^{16},
\]

hence

\[
\boxed{\|A\|<2.05},
\]

and since \(A=-B_{\rm prime}\),

\[
\boxed{\|B_{\rm prime}\|<2.05}.
\]

## Consequence for the \(N=16003\) tail gap

The previously derived cusp and archimedean tail-localization bounds may now be combined with the certified prime constant rather than the old noninterval decimal. Thus the robust analytic tail lower bound at the working interface is available:

\[
\boxed{\alpha_{16003}>4.6732}.
\]

The remaining high-complement bottleneck is now solely the rigorous cross estimate

\[
\boxed{\|A_{0,[21,16001],[16003,\infty)}\|<1}.
\]

Together with v13.362,

\[
A_{0,[21,16001]}\succeq0.22I,
\]

this cross bound would imply

\[
A_0|_{\mathcal D}\succeq
\left(0.22-\frac{1}{\alpha_{16003}}\right)I
>0.006I.
\]

## Guardrail

This checkpoint closes the prime-operator norm target only. It does not by itself prove positivity of the full high complement, a global inertia bound, an exact zero, RH, or GRH.
