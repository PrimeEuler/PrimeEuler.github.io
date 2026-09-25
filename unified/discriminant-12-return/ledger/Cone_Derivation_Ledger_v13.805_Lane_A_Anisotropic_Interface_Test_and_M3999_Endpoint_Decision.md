# Cone Derivation Ledger v13.805 — Lane A Anisotropic Interface Test and Decision to Reuse the Structured M=3999 Endpoint Verifier

Date: 2026-09-25

Lane: A.

Status: [N] anisotropic finite-to-band interface diagnostics; [D] endpoint large-n residual-channel shift; [N] compact interfaces 257/401 judged too weak or too tight for a robust common certificate; [C] M=3999 structured endpoint replay selected as the next implementation gate.

Parents: v13.390–400, v13.472, v13.801–804.


Audit correction (External Audit Round 103, v13.808): the N_R=401 even-v V4-reduced band figure is corrected from approximately 0.632637 to the script-reproduced value approximately 0.632306, with remaining room approximately 0.04652 rather than 0.04619. The qualitative M=3999 decision is unchanged.

Research artifact:

- research-notes/suzuki_endpoint_anisotropic_interface_diagnostic.py
- commit 2d8518ebff511910ee60e72117e37b0ca2cff60b.

No CI/status run is attached to this research commit. The midpoint numbers were independently recomputed in-session from the current corrected parity formulas.

## 1. Why a scalar cross norm is not the right test

For a finite endpoint block \(F\) coupled to a positive remote block \(R\), a scalar estimate
\[
\|G\|^2/\gamma_R
\]
throws away the same directional structure that motivated the earlier six-direction residual-Gram machinery.

Let
\[
S_F=W\Lambda W^T
\]
be the finite effective endpoint matrix and let \(W_+\) contain only its positive directions.

For a remote-band coupling \(G\), define
\[
\boxed{
\delta_{\rm crit}^{\rm band}
=
\left\|
\Lambda_+^{-1/2}W_+^TG
\right\|_2^2.
}
\]

If the remote block obeys
\[
R\succeq\gamma I,
\]
then positivity of the finite positive subspace after eliminating that remote block follows from
\[
\delta_{\rm crit}<\gamma.
\]

For orthogonal remote bands, residual Gram matrices add positively. Therefore a finite-band value is a lower contribution to the eventual full-tail residual Gram.

This is the endpoint analogue of the v13.390 anisotropic six-direction criterion.

## 2. Interface \(N_R=257\): even-v fails immediately under the current scalar tail floor [N]

Use the worst endpoint
\[
F^-_{0.10}=A-0.10B_{\rm sm}.
\]

Take the finite tail through mode \(256\) and the next band through \(384\).

The analytic remote-tail floors from v13.804 are
\[
\gamma_{0.10,+}(257)\approx0.275964
\]
for even-v and
\[
\gamma_{0.10,-}(257)\approx0.274238
\]
for odd-v.

### Even-v

Before the four-class unit-core elimination,
\[
\delta_{\rm crit}^{\rm band}
\approx0.533354.
\]

After the V4/unit-core rank-4 Schur elimination,
\[
\boxed{
\delta_{\rm crit,V4}^{\rm band}
\approx0.491393.
}
\]

Thus
\[
0.491393>0.275964.
\]

The next band alone already exceeds the available analytic scalar tail floor.

Therefore
\[
\boxed{
\text{the }N_R=257\text{ even-v certificate cannot close with the current scalar remote-floor architecture.}
}
\]

This does not rule out a stronger matrix-valued remote-tail treatment; it rules out this particular compact scalar-floor closure.

### Odd-v

Before class elimination,
\[
\delta_{\rm crit}^{\rm band}
\approx0.203736.
\]

After class elimination,
\[
\boxed{
\delta_{\rm crit,V4}^{\rm band}
\approx0.174214.
}
\]

Here
\[
0.174214<0.274238.
\]

So \(N_R=257\) remains numerically viable in odd-v, although the uncomputed farther tail must still fit inside the remaining margin.

A mixed proof architecture with different parity interfaces is possible, but it would substantially complicate the final certificate.

## 3. Interface \(N_R=401\): even-v becomes plausible but remains too tight [N]

Increase the finite even-v endpoint window through mode \(399\), so the remote tail starts at mode \(401\).

The analytic endpoint floor is
\[
\boxed{
\gamma_{0.10,+}(401)\approx0.678827.
}
\]

Using only the first next band through mode \(511\), the V4-reduced normalized residual cost is approximately
\[
0.288523,
\]
comfortably below the floor.

However, extending the explicitly assembled band through mode \(1023\) raises the same quantity to
\[
\boxed{
\delta_{\rm crit,V4}^{401:1023}
\approx0.632306.
}
\]

Hence the remaining analytic room is only
\[
\boxed{
0.678827-0.632306
\approx0.04652.
}
\]

The endpoint residual has the same leading \(1/n\) channel as the source-faithful M=3999 tail machinery, so the uncomputed tail beyond \(1023\) is not naturally negligible on this scale.

Therefore \(N_R=401\) is not rejected by the finite-band inequality, but it is too tight to be an attractive robust certification interface.

A dense attempt to extend this direct calculation much farther also hits the expected computational scaling barrier, reinforcing the need to return to the structured Cauchy implementation.

## 4. Endpoint large-n channel is an exact modification of the old residual expansion [D]

For the endpoint pencil
\[
F_\rho^{(s)}=A+s\rho B_{\rm sm},
\qquad s=\pm1,
\]
v13.804 proved
\[
Z_n^{(s)}
=
Z_n+\frac{s\rho\pi}{2}.
\]

For fixed finite mode \(m\) and remote \(n\to\infty\), the pole-free leading coefficient therefore changes by exactly
\[
\boxed{
-\frac{2}{\pi}Z_m
\longmapsto
-\frac{2}{\pi}Z_m-s\rho.
}
\]

Including the parity pole channel gives

even-v:
\[
\boxed{
L_m^{(s,+)}
=
-\frac{2}{\pi}Z_m
+
\frac{8\cosh(1/2)}{\pi}c_m
-s\rho,
}
\]

odd-v:
\[
\boxed{
L_m^{(s,-)}
=
-\frac{2}{\pi}Z_m
-
\frac{8\sinh(1/2)}{\pi}d_m
-s\rho.
}
\]

Thus
\[
F_{mn}^{(s)}
=
\frac{L_m^{(s)}}{n}
+
O(n^{-2}).
\]

Moreover the endpoint Hilbert contribution has the exact geometric expansion
\[
-\frac{s\rho}{n+m}
=
-\frac{s\rho}{n}
+\frac{s\rho m}{n^2}
-\frac{s\rho m^2}{n^3}
+\cdots.
\]

Therefore the old explicit residual accumulation and analytic inverse-power tail enclosure can be adapted directly. The endpoint modification is not a new asymptotic problem.

## 5. Why M=3999 is now the preferred common interface [C]

The repository already contains a completed outward verifier architecture at the \(M=3999\) scale for the source-faithful even-v problem:

- finite structured solve;
- fixed finite effective core;
- frozen directional coordinates;
- explicit residual-Gram accumulation through two million;
- analytic inverse-power tail beyond two million;
- outward finite-side and residual-side error budgets.

The endpoint pencil preserves the same Cauchy displacement rank and changes the remote asymptotic channels by explicit constants.

The endpoint high buffer also appears numerically healthy. At the currently assembled \(N=256\) diagnostic scale, using a ten-mode tail core and starting the high buffer at

\[
n=25\quad\text{(even-v)}
\]
or
\[
n=26\quad\text{(odd-v)},
\]

the worst \(\rho=0.10\) minus endpoint has midpoint high-buffer minima

\[
\boxed{
\lambda_{\min}\approx0.41590
\quad\text{(even-v)},
}
\]
\[
\boxed{
\lambda_{\min}\approx0.42443
\quad\text{(odd-v)}.
}
\]

This is far above the resonance scale.

Hence the endpoint certification should keep the difficult geometry in a small effective core and treat the high buffer with the existing structured machinery.

## 6. Recommended endpoint M=3999 layout [C]

For each parity tail, retain a ten-dimensional low tail core:

even-v:
\[
C_+=\{5,7,\ldots,23\},
\]

odd-v:
\[
C_-=\{6,8,\ldots,24\}.
\]

Use the finite structured buffers

even-v:
\[
F_+=\{25,27,\ldots,3999\},
\]

odd-v:
\[
F_-=\{26,28,\ldots,4000\}.
\]

The remote tails begin at \(4001\) and \(4002\), respectively.

At \(\rho=0.10\), the raw analytic endpoint tail floors near this interface are already about
\[
2.75
\]
in both parity sectors.

The expected finite effective core for the minus endpoint should have
\[
4\ \text{negative directions}
+
6\ \text{candidate-positive directions},
\]
matching the natural six-direction residual-Gram verifier architecture.

For the plus endpoint all ten effective-core directions should be positive and can be certified by the analogous normalized residual Gram, potentially with a simpler positive-core bound.

No endpoint \(M=3999\) theorem is claimed until these fresh finite cores and residual channels are actually recomputed.

## 7. Role of the V4 class split after this decision

The unit-core/V4 class-average split remains useful, but only after the finite-to-remote endpoint elimination.

It should be applied to the resulting finite effective block as a rank-4 conditioning/reproducibility check, not inserted into the remote-tail residual machinery.

This avoids the observed failure to reduce cross coupling while retaining the well-conditioned four-right-hand-side Schur solve from v13.803–804.

## 8. Next implementation gate

Build an endpoint version of the source-faithful M=3999 midpoint generator with parameters

\[
(\rho,s,\text{parity}),
\]

using

\[
Z_n\mapsto Z_n+\frac{s\rho\pi}{2}
\]
and the endpoint diagonal shift.

First execute only
\[
\boxed{
\rho=0.10,\qquad s=-1
}
\]
for both parity sectors.

Freeze and report:

1. high-buffer minimum eigenvalue / factor pivot margin;
2. ten-dimensional finite effective-core inertia;
3. the six candidate-positive directions for the minus endpoint;
4. their normalized remote residual Gram through a large explicit cutoff;
5. the analytic residual tail;
6. the corrected odd-v rank-one pole contribution separately.

Only if this worst endpoint closes should the \(\rho=0.02\) and plus-endpoint replays be run.

## Result

The compact-interface experiments have served their purpose: they identify where brute-force truncation stops being efficient and where the old structured verifier becomes the correct tool.

\[
\boxed{
\textbf{The }N_R=257\textbf{ scalar-floor endpoint architecture is ruled out for even-v by the next band alone.}
}
\]

\[
\boxed{
\textbf{The }N_R=401\textbf{ interface is numerically plausible but leaves only about }0.046\textbf{ tail-floor room after modes through 1023, so it is not robust.}
}
\]

\[
\boxed{
\textbf{The next Lane A gate is a fresh }M=3999\textbf{ endpoint residual-Gram replay, not a larger dense finite section.}
}
