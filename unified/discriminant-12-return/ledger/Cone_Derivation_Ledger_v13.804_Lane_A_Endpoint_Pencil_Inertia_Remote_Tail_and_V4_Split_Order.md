# Cone Derivation Ledger v13.804 — Lane A Endpoint-Pencil Inertia Gate, Analytic Remote-Tail Floors, and Correct Placement of the V4 Rank-4 Split

Date: 2026-09-25

Lane: A.

Status: [D] endpoint-inertia identity; [D] endpoint Cauchy-generator shift; [D] analytic parity-aware remote-tail lower bounds; [N] finite endpoint inertias through N=256; [N] V4 class-average split improves finite conditioning but does not reduce remote-band coupling; [C] corrected certification order fixed.

Parents: v13.363, v13.801–803.

Research artifact:

- research-notes/suzuki_endpoint_v4_inertia_certificate_diagnostic.py
- commit 39c371c9a4053da3690807938726146f29bdb6af.

No GitHub workflow/status run is attached to this research commit. The reported finite numbers below were independently recomputed in-session from the same source-faithful formulas at 40–50 decimal digit assembly precision.

## 1. Endpoint-inertia formulation [D]

On the positive smooth-bulk tail let
\[
B:=B_{\rm sm}=D_{\log}-H,
\]
and
\[
J=B^{-1/2}AB^{-1/2}=I+K.
\]

For \(0<\rho<1\), define
\[
F_\rho^-:=A-\rho B,
\qquad
F_\rho^+:=A+\rho B.
\]

Under congruence by \(B^{-1/2}\),
\[
F_\rho^-\sim J-\rho I,
\qquad
F_\rho^+\sim J+\rho I.
\]

Hence, provided the endpoint operators are nonsingular,
\[
\boxed{
N(\rho)
=
\#\{\delta\in\sigma(J):|\delta|<\rho\}
=
\operatorname{ind}_-(F_\rho^-)
-
\operatorname{ind}_-(F_\rho^+).
}
\]

Because \(\delta=1+\mu(K)\), this is equivalently
\[
N(\rho)
=
\#\{\mu\in\sigma(K):|1+\mu|<\rho\}.
\]

Thus the target
\[
N(0.02)=N(0.10)=4
\]
certifies a four-dimensional resonance cluster within \(0.02\) of \(-1\) and excludes a fifth resonance within \(0.10\).

## 2. Endpoint shifts preserve the rank-two Cauchy structure [D]

For either same-parity pole-free source-faithful block, the off-diagonal matrix has the form
\[
A_{0,mn}
=
-\frac{2}{\pi}
\frac{nZ_m-mZ_n}{n^2-m^2},
\qquad m\ne n.
\]

For the smooth bulk,
\[
B_{mn}
=
-\frac1{m+n}
=
-\frac{m-n}{m^2-n^2}.
\]

Therefore
\[
F_{\rho,mn}^{(s)}
=
A_{0,mn}
-
\frac{s\rho}{m+n},
\qquad s=\pm1,
\]
is exactly
\[
\boxed{
F_{\rho,mn}^{(s)}
=
-\frac{2}{\pi}
\frac{nZ_m^{(s)}-mZ_n^{(s)}}{n^2-m^2},
}
\]
with
\[
\boxed{
Z_n^{(s)}
=
Z_n+\frac{s\rho\pi}{2}.
}
\]

The diagonal is shifted separately by
\[
s\rho\left(\log(n/4)-\frac1{2n}\right).
\]

Thus the endpoint pencils preserve the source-faithful displacement-rank / Cauchy machinery. Existing streaming LDL, cross-expansion, and residual-certificate infrastructure can be adapted by a constant generator shift rather than re-derived from scratch.

The parity pole terms remain separate rank-one pieces:
\[
+2cc^T\quad\text{(even-v)},
\]
\[
-2dd^T\quad\text{(odd-v)}.
\]

## 3. Analytic endpoint remote-tail floor [D]

For the worst endpoint
\[
F_\rho^-=A-\rho B,
\]
write
\[
F_\rho^-
=
(1-\rho)(D_{\log}-H)
+
B_{\rm prime}
+
K_{\rm cusp}
+
K_{\rm arch}
+
K_{\rm pole}.
\]

Use the already validated full operator bound
\[
\boxed{\|B_{\rm prime}\|<2.05}
\]
from v13.363. This is a full positive-kernel operator certificate, not an even-v-only estimate.

For a parity tail supported on \(n\ge N\), define
\[
s_2(N)=N^{-2}+(2N)^{-1}.
\]

The audited cusp tail majorant is
\[
\beta_{\rm cusp}(N)
=
\frac{2}{\pi^2}s_2(N)
+
2\alpha
\sqrt{\frac{\pi^2}{12}
\left(N^{-6}+\frac1{10N^5}\right)}
+
C_{\rm diag}
\sqrt{N^{-4}+\frac1{6N^3}},
\]
where
\[
\alpha
=
\frac2\pi
\left(\frac2{\pi^3}+\frac6{\pi^4}\right),
\]
\[
C_{\rm diag}
=
\frac2{\pi^2}
+\frac2{\pi^3}
+\frac2{\pi^4}
+\frac6{\pi^5}.
\]

The same norm bound applies in the corrected odd-v sector: the leading cusp rank-one term changes sign with parity, but its Hilbert-Schmidt norm does not, and the sine-integral remainder estimates are parity-independent in absolute value.

The smooth archimedean tail bound is
\[
\beta_{\rm arch}(N)
=
\frac{4C_r}{\pi^2}s_2(N),
\]
with
\[
C_r
=
\frac{19}{12}
+
4\frac{\zeta(3)(2/\pi)^3}{4(1-2/\pi)^3}.
\]

The integration-by-parts estimate uses only the antiderivative magnitude and endpoint magnitude \(1/k_n\), so the same absolute bound applies to both parity subsequences.

For corrected odd-v, the adverse pole is
\[
-2dd^T,
\]
with
\[
|d_n|
\le
\frac{4\sinh(1/2)}{\pi n},
\]
hence
\[
\boxed{
\beta_{\rm pole}^{(-)}(N)
\le
\frac{32\sinh^2(1/2)}{\pi^2}s_2(N).
}
\]

The even-v pole is positive and may be dropped in a lower bound.

Therefore
\[
\boxed{
\gamma_{\rho,+}(N)
=
(1-\rho)
\left[\log(N/4)-\frac\pi2\right]
-2.05
-\beta_{\rm cusp}(N)
-\beta_{\rm arch}(N)
}
\]
for even-v, and
\[
\boxed{
\gamma_{\rho,-}(N)
=
\gamma_{\rho,+}(N)
-\beta_{\rm pole}^{(-)}(N)
}
\]
for odd-v.

These are analytic/validated-input lower bounds for \(F_\rho^-\). Once \(B>0\), \(F_\rho^+\) is the easier endpoint.

## 4. Concrete remote-tail scales [D/N]

For \(\rho=0.02\), a common conservative positivity threshold is
\[
N\ge159.
\]

At \(N=159\),
\[
\gamma_{0.02,+}\approx8.48\times10^{-3},
\qquad
\gamma_{0.02,-}\approx5.68\times10^{-3}.
\]

For \(\rho=0.10\), a common conservative threshold is
\[
N\ge191,
\]
with
\[
\gamma_{0.10,+}(191)\approx6.45\times10^{-3},
\]
\[
\gamma_{0.10,-}(191)\approx4.12\times10^{-3}.
\]

These margins are positive but too small for a comfortable Schur-cross certificate.

A much better working interface is
\[
\boxed{N_R=257.}
\]

There,
\[
\boxed{
\gamma_{0.10,+}(257)\approx0.275964,
\qquad
\gamma_{0.10,-}(257)\approx0.274238,
}
\]
and
\[
\gamma_{0.02,+}(257)\approx0.483323,
\qquad
\gamma_{0.02,-}(257)\approx0.481597.
\]

Thus the remote endpoint tail itself is not the difficult part once the interface is moved modestly upward.

## 5. Finite endpoint inertia through N=256 [N]

Retain the first two parity modes as the low core, exactly as in v13.801, and examine the finite tail through \(N=96,192,256\).

At every tested cutoff, in both parity sectors and both radii,
\[
\boxed{
\operatorname{ind}_-(F_\rho^-)=4,
\qquad
\operatorname{ind}_-(F_\rho^+)=0.
}
\]

In particular at \(N=256\):

even-v:
\[
\begin{array}{c|cc}
\rho & \operatorname{ind}_-(F_\rho^-)
& \operatorname{ind}_-(F_\rho^+)\\
\hline
0.02&4&0\\
0.10&4&0
\end{array}
\]

odd-v:
\[
\begin{array}{c|cc}
\rho & \operatorname{ind}_-(F_\rho^-)
& \operatorname{ind}_-(F_\rho^+)\\
\hline
0.02&4&0\\
0.10&4&0.
\end{array}
\]

This is strong cutoff-stable finite evidence for
\[
N(0.02)=N(0.10)=4,
\]
but it is not yet the infinite certificate because finite-to-remote coupling remains to be enclosed.

## 6. V4/unit-core class block at the endpoints [N]

On the finite \(N=256\) tail, let \(U\) be the four normalized unit-core class-average directions.

For each endpoint write
\[
F=
\begin{pmatrix}
C&K^T\\
K&D
\end{pmatrix}
\]
relative to
\[
\operatorname{Ran}U\oplus(\operatorname{Ran}U)^\perp.
\]

The class block is very safe.

At the worst \(\rho=0.10\) minus endpoint:
\[
\lambda_{\min}(C)
\approx2.3694
\quad\text{(even-v)},
\]
\[
\lambda_{\min}(C)
\approx2.2949
\quad\text{(odd-v)}.
\]

Across all four endpoint pencils at \(N=256\),
\[
\boxed{
\lambda_{\min}(C)>2.29.
}
\]

The solve amplification
\[
\frac{\|K\|_2}{\lambda_{\min}(C)}
\]
is below
\[
0.72\quad\text{(even-v)},
\qquad
0.66\quad\text{(odd-v)}.
\]

Thus four residual-certified right-hand sides suffice to eliminate the unit-core class block with a mild error amplification.

## 7. Finite gap improvement from the rank-4 Schur split [N]

Let
\[
S=D-KC^{-1}K^T.
\]

At \(N=256\), the class elimination preserves the endpoint inertias exactly and increases the smallest absolute endpoint eigenvalue modestly.

Representative ratios
\[
\frac{\min|\lambda(S)|}{\min|\lambda(F)|}
\]
are:

even-v:
\[
1.031\text{--}1.042,
\]

odd-v:
\[
1.024\text{--}1.068.
\]

For example, at \(\rho=0.02\):
\[
\min|\lambda(S_-^{\rm even})|
\approx2.730\times10^{-3},
\]
\[
\min|\lambda(S_+^{\rm even})|
\approx2.531\times10^{-3},
\]
\[
\min|\lambda(S_-^{\rm odd})|
\approx3.938\times10^{-3},
\]
\[
\min|\lambda(S_+^{\rm odd})|
\approx7.073\times10^{-3}.
\]

Thus the V4/unit-core split is a useful finite conditioning device, although the improvement is modest rather than dramatic.

## 8. Crucial negative result: V4 elimination does not decouple the remote band [N]

To test whether the unit-core split should be applied before the remote-tail Feshbach step, assemble through \(N=256\), use the finite window through \(N=192\), and regard modes \(>192\) as a next-band proxy.

Compare the fluctuation-to-band cross norm before and after eliminating the four class averages.

Across the four endpoint pencils:

even-v:
\[
\frac{\|G_{\rm after}\|}{\|G_{\rm before}\|}
\approx
1.015\text{--}1.032,
\]

odd-v:
\[
\frac{\|G_{\rm after}\|}{\|G_{\rm before}\|}
\approx
0.992\text{--}0.998.
\]

In particular, in even-v the rank-4 elimination slightly increases the next-band cross norm.

Therefore
\[
\boxed{
\text{the unit-core/V4 split is not a remote-tail decoupling mechanism.}
}
\]

This rules out using it as a substitute for the source-faithful cross/residual certificate.

## 9. Correct certification order [C]

The order from v13.803 is now sharpened:

1. choose an endpoint radius \(\rho\);
2. exploit the exact generator shift
   \[
   Z_n\mapsto Z_n\pm\rho\pi/2
   \]
   to adapt the source-faithful Cauchy/streaming machinery to \(F_\rho^\pm\);
3. certify the remote tail and finite-to-remote Schur correction first;
4. obtain a finite effective endpoint block;
5. only then split off the four unit-core class-average directions;
6. eliminate that \(4\times4\) block with four residual-certified solves;
7. certify the inertia of the remaining fluctuation Schur matrix;
8. verify
   \[
   N(0.02)=N(0.10)=4.
   \]

The V4 structure therefore survives as a **finite low-rank certificate organizer**, not as an infinite symmetry and not as a tail preconditioner.

## 10. Next exact gate

The load-bearing open object is now the endpoint finite-to-remote correction.

Because the endpoint shift preserves the Cauchy generator, the next implementation should modify the already source-faithful high-complement/cross machinery by

\[
Z_n\longmapsto Z_n\pm\rho\pi/2
\]
and the corresponding diagonal endpoint shift, while treating the parity pole rank-one terms separately.

The first target should be the worst endpoint
\[
\boxed{\rho=0.10,\quad F^-_{0.10}=A-0.10B_{\rm sm}.}
\]

A successful certificate for that endpoint, with the \(N_R=257\) analytic tail floor or a larger interface if needed for cross control, will determine whether the compact \(N_R\) split is sufficient or whether the older \(M=3999\)/\(16001\) structured machinery should be reused.

## Result

The endpoint-inertia route is now materially sharper:

\[
\boxed{
\textbf{Finite sections through }N=256\textbf{ give exactly four negative }F_\rho^-\textbf{ directions and zero negative }F_\rho^+\textbf{ directions at both certification radii.}
}
\]

\[
\boxed{
\textbf{The endpoint pencils preserve the source-faithful rank-two Cauchy structure by the exact shift }Z_n\to Z_n\pm\rho\pi/2.
}
\]

\[
\boxed{
\textbf{The unit-core/V4 rank-4 split improves finite conditioning but must be applied after, not before, the remote-tail elimination.}
}
