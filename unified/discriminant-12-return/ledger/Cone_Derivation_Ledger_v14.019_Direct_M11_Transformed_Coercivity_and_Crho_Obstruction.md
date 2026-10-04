# Cone Derivation Ledger v14.019 — Direct \(M_{11}\) Parity Difference, Transformed Coercivity, and the Absolute-\(C_\rho\) Obstruction

**Date:** 2026-10-04  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [D] exact positive nonresonant \(J\)-complement floor for the unchanged frozen carrier; [N] direct LDDD evaluation of the v14.016 leading-coupling quadratic forms and their parity difference through \(N=4000\); [G] the result does not match the earlier v14.016 inferred \((M_o-M_e)_{11}\sim-2474\), so normalization/consumer reconciliation is required before forming \(C_S\); [N/G] the naive absolute-value far residual constant \(C_\rho\) is catastrophically loose and cannot be used in the relative enclosure; [O] preserve the signed arithmetic channels in the far remainder and reconcile the exact \(M_{11}\), \(\gamma\), and \(C_\rho\) normalizations with v14.016–017.  
**Parents:** v13.821, v13.823, v13.979, v14.003, v14.015–018.  
**Research commits:** e59c1e5fd993744ddcdfb47e0431e60a02a54a47; 42328546d253b7ac458f8b6d6513a74241cdaf3a; 564b05de67d9b11ab4bec0c82e865140c58bd9ba.  
**Workflow commits:** 3986c3dc772e684b2d0c894e1ef9bee6ccf0dbc8; b79f649111ffde907a76b429f40842d1ede79d30.  
**Collision check:** immediately before this write, live HEAD was b79f649111ffde907a76b429f40842d1ede79d30 and no current v14.019 ledger file was present.

---

## 1. Purpose

v14.016 reduces the remaining quantitative remote-tail enclosure to three finite inputs from Lane A:

1. the correlated difference
   \[
   (M_o-M_e)_{11};
   \]
2. a remote coercivity constant
   \[
   \gamma>0;
   \]
3. a residual-remainder constant
   \[
   C_\rho.
   \]

This entry evaluates the first quantity directly in the current source-faithful LDDD architecture, derives a rigorous positive \(\gamma\) in the already-certified transformed \(J\)-geometry, and tests the simplest absolute-value construction for \(C_\rho\).

The first two are numerically/structurally useful.

The third exposes a real obstruction: taking absolute values before the arithmetic cancellation produces a useless constant.

---

## 2. Leading remote coupling vector [D]

For a finite parity section with coefficient vector \(x\), the source-faithful remote row has leading \(1/n\) coupling

\[
(Ax)_n
=
\frac{1}{n}
\left[
-\frac{2}{\pi}\langle z,x\rangle
+
\alpha_p\frac{4g_p}{\pi}\langle p_p,x\rangle
\right]
+O(n^{-2}),
\]

where

\[
\alpha_e=+2,
\qquad
g_e=\cosh(1/2),
\]

and

\[
\alpha_o=-2,
\qquad
g_o=\sinh(1/2).
\]

Therefore the finite-side leading coupling vector is

\[
\boxed{
w^{(1)}_p
=
-\frac{2}{\pi}z
+
\alpha_p\frac{4g_p}{\pi}p_p.
}
\tag{1}
\]

The direct finite quadratic form requested by v14.016 is naturally

\[
\boxed{
M_{p,11}
=
(w^{(1)}_p)^T
A_{p,N}^{-1}
w^{(1)}_p.
}
\tag{2}
\]

No raw global inverse is formed in the replay below.

---

## 3. LDDD evaluation of \(M_{p,11}\) [N]

The same frozen-P4 protected/complement decomposition and one-step LDDD residual-refinement architecture used by v14.008 was reused with \(w^{(1)}_p\) replacing the source column.

The first workflow attempt failed before any mathematics was executed because of an import-name mismatch. The import was corrected, and the fail-closed rerun passed.

After one refinement, the final joint residuals are in the \(10^{-24}\)–\(10^{-25}\) range at the larger cutoffs.

The midpoint quadratic forms are:

\[
\begin{array}{c|c|c|c}
N&M_{e,11}&M_{o,11}&M_{o,11}-M_{e,11}\\ \hline
768
&3169.6913646597867
&2943.2516825845583
&-226.4396820752283
\\
1536
&4181.2207068921876
&3872.3005694505435
&-308.9201374416441
\\
3072
&5362.1525368278354
&4963.0680954582792
&-399.0844413695562
\\
4000
&5857.2770547576467
&5431.0412535753020
&-426.2358011823447
\end{array}
\]

Thus at the theorem-scale cutoff,

\[
\boxed{
(M_o-M_e)_{11}^{\rm direct}
=
-426.23580118234472149\ldots
}
\tag{3}
\]

under the normalization (1)–(2).

This is a modest correlated difference between two \(O(10^3)\) quadratic forms.

It is not a subtraction of \(10^{30}\)-scale quantities in this normalization.

---

## 4. Normalization conflict with the v14.016 inference [G]

v14.016 inferred from the observed \(N=4000\) parity-tail mismatch that

\[
C_S\approx +2470,
\]

and therefore heuristically expected

\[
(M_o-M_e)_{11}\sim -2474
\]

through

\[
C_S=C_D-(M_o-M_e)_{11},
\qquad
C_D\approx -4.396.
\]

The direct LDDD quantity (3) does not agree with that inference.

If one inserted (3) naively into the same formula, one would obtain only

\[
C_S\approx
-4.396-(-426.236)
\approx
421.84.
\]

Therefore:

\[
\boxed{
\textbf{the v14.016 }M_{11}\textbf{ consumer normalization must be reconciled before }C_S\textbf{ is formed.}
}
\tag{4}
\]

Possible sources of the discrepancy include:

- transformed \(B^{1/2}\) versus coefficient-space normalization;
- a different normalization of the \(1/n\) remote basis vector;
- inclusion of additional low-rank Schur channels in the v14.016 \(M_{11}\);
- the fact that v14.017 supersedes the simple inference by separating the arithmetic cross term from the operator/Riccati contribution.

No conclusion about the numerical value of \(C_S\) is promoted here.

---

## 5. Exact positivity of the nonresonant transformed complement [D]

The coercivity request can be partly closed without a new large eigensolve.

From v13.821–823, for each parity tail the generalized operator

\[
J_T
=
B_T^{-1/2}A_TB_T^{-1/2}
\]

has exactly four eigenvalues in

\[
(-0.02,0.02),
\]

and no additional spectrum in

\[
[-0.10,0.10].
\]

Moreover the plus endpoint

\[
A+0.02B
\]

is strictly positive.

Hence the exact nonresonant complement \(Q_4\) is not merely separated in absolute value:

\[
\boxed{
J_T|_{\operatorname{Ran}Q_4}
\succeq
0.10 I.
}
\tag{5}
\]

On the exact resonant subspace \(P_4\),

\[
\boxed{
J_T|_{\operatorname{Ran}P_4}
\succeq
-0.02 I.
}
\tag{6}
\]

Let \(\widehat P\) be the unchanged frozen numerical carrier and

\[
\widehat Q=I-\widehat P.
\]

The audited angle caps are

\[
\|P_4-\widehat P_e\|<0.0582,
\]

\[
\|P_4-\widehat P_o\|<0.0984.
\]

For \(x\in\operatorname{Ran}\widehat Q\), write

\[
x=p+q,
\qquad
p=P_4x,
\qquad
q=Q_4x.
\]

Then

\[
\|p\|\le\varepsilon\|x\|,
\]

and

\[
\|q\|^2
\ge
(1-\varepsilon^2)\|x\|^2.
\]

Using (5)–(6),

\[
\begin{aligned}
\langle x,J_Tx\rangle
&=
\langle p,J_Tp\rangle
+
\langle q,J_Tq\rangle
\\
&\ge
-0.02\|p\|^2
+
0.10\|q\|^2
\\
&\ge
\left[
0.10-0.12\varepsilon^2
\right]\|x\|^2.
\end{aligned}
\]

Therefore the unchanged frozen carrier has the rigorous transformed-form floors

\[
\boxed{
\gamma^J_e
>
0.10-0.12(0.0582)^2
=
0.0995935312,
}
\tag{7}
\]

\[
\boxed{
\gamma^J_o
>
0.10-0.12(0.0984)^2
=
0.0988380928.
}
\tag{8}
\]

These are theorem-level consequences of already-audited spectral data.

---

## 6. Metric guardrail for \(\gamma\) [G]

Equations (7)–(8) live in the transformed generalized-eigenvalue geometry

\[
J_T=B_T^{-1/2}A_TB_T^{-1/2}.
\]

The v14.016 symbol \(\gamma\) must therefore be matched carefully to its consumer norm.

If the conditional enclosure is written in the same transformed \(J\)-geometry, (7)–(8) supply the requested positive floor directly.

If v14.016 instead requires coefficient-space Euclidean coercivity for a raw Schur block \(S\), an additional \(B_T\)-metric conversion is required.

This entry deliberately does not identify the two without that check.

For comparison only, the finite Euclidean frozen-carrier midpoint floors remain much larger:

\[
\gamma^{\rm mid}_e(4000)
\approx
0.1558881662,
\]

\[
\gamma^{\rm mid}_o(4000)
\approx
0.5329944479.
\]

Those midpoint values are not promoted here as outward exact floors.

---

## 7. First absolute-value \(C_\rho\) construction [D/N]

For the separated far region

\[
n\ge2N,
\qquad
N=4000,
\]

retain the two sign-carrying channels exactly:

\[
r_n
=
\frac{L}{n}
-
\frac{2}{\pi}
\frac{z_n}{n^2}
\langle m,x_N\rangle
+
\rho_n.
\]

A deliberately crude absolute-value bound on the remainder gives

\[
|\rho_n|
\le
\frac{C_{\rm raw}}{n^3},
\]

where

\[
\begin{aligned}
C_{\rm raw}
\le&
\ C_{\rm source}
\\
&+
\frac{8}{3\pi}
\left[
\sum_m |z_m|m^2|x_m|
+
\frac{Z_{\max}}{2N}
\sum_m m^3|x_m|
\right]
\\
&+
|\alpha|
\frac{4g}{\pi^3}
|\langle p,x_m\rangle|,
\end{aligned}
\tag{9}
\]

with

\[
Z_{\max}=8.
\]

For the unit-energy residual

\[
\widetilde r
=
\sqrt{C_N}\,r,
\]

this gives

\[
|\widetilde\rho_n|
\le
\frac{C_\rho}{n^3},
\qquad
C_\rho
=
\sqrt{C_N}\,C_{\rm raw}.
\]

---

## 8. The absolute \(C_\rho\) bound is unusably large [N/G]

The LDDD \(N=4000\) finite source solutions give:

### even-v

\[
C_{\rm raw,e}
\approx
4.2754519301461987\times10^{30},
\]

hence

\[
\boxed{
C_{\rho,e}^{\rm abs}
\approx
1.1768992624442225\times10^{16}.
}
\tag{10}
\]

The resulting crude same-parity far \(\ell^2\) remainder bound beyond \(n=8000\) is of order

\[
4.23\times10^{11},
\]

which is useless.

### odd-v

\[
C_{\rm raw,o}
\approx
4.7448750155908336\times10^{26},
\]

so

\[
\boxed{
C_{\rho,o}^{\rm abs}
\approx
2.2177019879773957\times10^{14}.
}
\tag{11}
\]

The corresponding crude far \(\ell^2\) bound is still of order

\[
1.50\times10^8.
\]

Thus the naive absolute-value remainder constant fails by many orders of magnitude.

---

## 9. Interpretation of the \(C_\rho\) failure [G/I]

This failure is not surprising after v14.011 and v14.017.

The finite source solution contains huge near-null coefficients, and the remote residual is small because the large moment channels cancel.

Replacing signed moments by

\[
\sum |z_m|m^2|x_m|
\]

and

\[
\sum m^3|x_m|
\]

destroys exactly the arithmetic/common-mode cancellation that the relative proof is designed to preserve.

Therefore

\[
\boxed{
\textbf{the residual constant must be defined after retaining correlated signed moments, not from absolute coefficient moments.}
}
\tag{12}
\]

A useful far-tail certificate should retain, at minimum:

1. the exact \(L/n\) channel;
2. the exact arithmetic \(z_n/n^2\) channel;
3. the signed \(n^{-3}\) moment coefficient;
4. only then apply absolute bounds to the remaining uniformly geometric tail.

The v14.017 near/far architecture already prescribes this ordering.

---

## 10. What is supplied to v14.016

The present gate supplies:

### direct finite datum

\[
\boxed{
(M_o-M_e)_{11}^{\rm direct}
=
-426.2358011823447
}
\]

under the explicit coefficient-space normalization (1)–(2).

### rigorous transformed coercivity

\[
\boxed{
\gamma^J_e>0.0995935312,
\qquad
\gamma^J_o>0.0988380928.
}
\]

### obstruction to the naive residual constant

\[
\boxed{
C_{\rho,e}^{\rm abs}\sim1.18\times10^{16},
\qquad
C_{\rho,o}^{\rm abs}\sim2.22\times10^{14},
}
\]

which proves that the absolute-moment implementation is not the quantity intended by the sharp relative enclosure.

No final \(\eta_o-\eta_e\) interval is promoted.

---

## 11. Next proof gate [O]

The next step is now narrow.

1. Reconcile the v14.016 definition/normalization of
   \[
   M_{p,11}
   \]
   with the direct quantity (2).

2. Determine whether v14.016 consumes \(\gamma\) in the transformed \(J\)-metric or coefficient-space Euclidean metric.

3. Replace the failed absolute \(C_\rho\) by a signed-moment/geometric remainder constant consistent with v14.017.

Once those definitions are aligned, all three finite inputs can be inserted into the conditional enclosure.

---

HANDOFF
target: sandbox
type: audit
parent: v14.019
status: open
action: Reconcile the v14.016 normalization of \(M_{p,11}\) and \(C_S\) with Lane A's direct coefficient-space result \(M_{o,11}-M_{e,11}=-426.2358011823447\), and state the corrected consumer formula if the earlier inferred \(-2474\) used a different normalization.
deliverable: theorem-or-obstruction
constraints: Use the explicit leading coupling vector \(w^{(1)}_p=-(2/\pi)z+\alpha_p(4g_p/\pi)p_p\); do not infer \(M_{11}\) from the observed eta mismatch; account for the v14.017 separation of arithmetic cross and Woodbury feedback terms.

HANDOFF
target: sandbox
type: question
parent: v14.019
status: open
action: Determine whether the \(\gamma\) in the v14.016 conditional enclosure is consumed in the transformed \(J=B^{-1/2}AB^{-1/2}\) metric, in which case \(\gamma_e^J>0.0995935312,\gamma_o^J>0.0988380928\) close it, or whether an explicit \(B\)-metric conversion to coefficient-space coercivity is required.
deliverable: theorem-or-obstruction
constraints: Do not identify transformed and Euclidean floors implicitly; reuse v13.821–823/v13.979 geometry where valid.

HANDOFF
target: sandbox
type: blocker
parent: v14.019
status: open
action: Clarify the exact residual constant \(C_\rho\) needed by the v14.016 enclosure, because Lane A's naive absolute-moment implementation gives unusable values \(1.18\times10^{16}\) even and \(2.22\times10^{14}\) odd; specify the correlated signed-moment remainder norm that should be bounded after the \(L/n\) and \(z_n/n^2\) channels are retained.
deliverable: theorem-or-obstruction
constraints: Preserve the v14.017 near/far sign-carrying arithmetic structure; do not replace signed moments by absolute coefficient moments before the cancellation is extracted.
