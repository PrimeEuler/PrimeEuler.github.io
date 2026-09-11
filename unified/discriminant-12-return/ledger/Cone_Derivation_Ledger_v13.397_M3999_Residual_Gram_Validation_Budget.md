# Cone Derivation Ledger v13.397 — M3999 Residual-Gram Validation Budget

Date: 2026-09-11

Status labels: **[D]** exact derived, **[N]** numerical, **[N-cert]** validated computational, **[O]** open.

## 1. Context

v13.396 reduced the finite-side fixed-preconditioner uncertainty to a normalized distortion below about 0.43%, provided the source-faithful M=3999 finite solve is replayed with residual

\[
\|R_F\|<10^{-12}.
\]

The corresponding normalized finite matrix satisfies the design target

\[
C_{\rm pre}\succeq c_{\rm low}I,
\qquad c_{\rm low}>0.9958.
\]

The certified source-faithful Schur-tail floor remains

\[
\delta_T>0.18225976374175623.
\]

Hence the residual-Gram side may occupy at most

\[
H_{\max}=\delta_T c_{\rm low}>0.18149.
\]

## 2. Current hybrid residual value

From v13.393,

\[
h_{\rm hybrid}=0.17910434985544155,
\]

where this already includes:

1. explicit source-faithful generalized residual-Gram accumulation from mode 4001 through 2,000,000;
2. the analytic beyond-two-million envelope
   \[
   8.938359453827081\times10^{-4}.
   \]

Therefore the raw outward-validation room after the finite-side budget is still greater than

\[
\boxed{2.39\times10^{-3}}.
\]

## 3. Normalize at the residual-operator level

Let

\[
Y=R_WL_0^{-T},\qquad H=Y^*Y.
\]

If an outward replay proves

\[
\|Y-Y_0\|\le\varepsilon_Y,
\]

then

\[
\|H-H_0\|
\le
2\|Y_0\|\varepsilon_Y+\varepsilon_Y^2.
\]

Because

\[
\|Y_0\|\le\sqrt{0.17910435}<0.424,
\]

the deliberately loose target

\[
\boxed{\varepsilon_Y<10^{-3}}
\]

costs less than

\[
\boxed{8.5\times10^{-4}}
\]

in normalized Gram norm.

This tolerance is many orders larger than the source-constant uncertainty and is intentionally chosen to make the final replay simple and auditable.

## 4. Reserve for analytic-tail constant validation

The current analytic tail envelope beyond two million is

\[
8.93836\times10^{-4}.
\]

Even allowing a very conservative 25% outward inflation during interval reconstruction consumes only

\[
\boxed{2.24\times10^{-4}}.
\]

Thus the combined residual-side validation reserve is below roughly

\[
8.5\times10^{-4}+2.24\times10^{-4}
<1.08\times10^{-3},
\]

less than half the available normalized room.

## 5. Fail-closed terminal target

A convenient final residual-side target is

\[
\boxed{\lambda_{\max}(H_{\rm exact})<0.18025}.
\]

This is deliberately looser than the midpoint/hybrid estimate but remains comfortably below

\[
H_{\max}>0.18149.
\]

Therefore the terminal six-direction proof can be organized around two independent verifier outputs:

\[
\boxed{C_{\rm pre}\succeq0.9958I},
\]

and

\[
\boxed{H_{\rm exact}\prec0.18025I}.
\]

These imply

\[
H_{\rm exact}<\delta_T C_{\rm pre}
\]

with visible normalized margin.

## 6. Consequence

The six candidate-positive directions no longer require uniform \(10^{-11}\)-scale infinite solve certification. The final outward checker may work at the normalized residual-operator scale \(10^{-3}\), provided the finite M=3999 solve itself is certified to the v13.396 residual target.

This sharply separates the problem into:

1. a high-precision but finite M=3999 solve certification;
2. a coarse normalized residual replay with large outward room;
3. the unresolved four-dimensional near-zero terminal sector.

## 7. Guardrails

This checkpoint is a verifier budget, not a completed validated-computational run. The first four low-core directions are not exact kernels. No final inertia, exact-zero, RH, or GRH conclusion follows.
