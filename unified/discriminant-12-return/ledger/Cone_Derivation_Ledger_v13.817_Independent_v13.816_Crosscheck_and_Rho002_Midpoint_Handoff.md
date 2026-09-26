# Cone Derivation Ledger v13.817 — Independent Cross-Check of v13.816 and Fresh \(\rho=0.02\) M3999 Endpoint Midpoint Handoff

Date: 2026-09-25 local / 2026-09-26 UTC.

Lane: A.

Status: [A] source-thread independent numerical cross-check of v13.816 plus-tail certificate targets; [N] fresh theorem-scale \(\rho=0.02\) M3999/4000 midpoint pair; [G] no \(\rho=0.02\) infinite endpoint theorem promoted yet.

Parents: v13.815–816.

Research artifacts:

- research-notes/suzuki_endpoint_M3999_midpoint_effective_core.py
  - commit f4e2df8972d87f8453b5553e1f0d0cfbd73bdc7e
  - endpoint radius parameterized as an explicit argument with \(\rho=0.10\) preserved as the default;

- research-notes/suzuki_endpoint_M3999_rho002_midpoint.py
  - commit 916c30b79a7ab102616e9184be2d1dd0ff635784.

No GitHub workflow/status run is attached.

## 1. Collision/provenance check

Before writing this entry, the live ledger was re-read.

A parallel source commit had already landed as v13.816 and certified the \(\rho=0.10\) plus tail endpoint, so no duplicate plus-endpoint ledger was created here.

Instead, the source thread independently reconstructed the v13.816 midpoint and remote-Gram targets in a separate numerical notebook before proceeding to \(\rho=0.02\).

## 2. Independent cross-check of the \(\rho=0.10\) plus midpoint

Using the same source-faithful formulas but a separate reconstruction path, the \(M=3999/4000\) plus effective cores give

even-v:
\[
\lambda_{\min}(S^+_{0.10,e})
=
0.0107446191592416\ldots,
\]

odd-v:
\[
\lambda_{\min}(S^+_{0.10,o})
=
0.0306633761341358\ldots.
\]

The reconstructed full ten-dimensional inertias are

\[
\boxed{
\operatorname{inertia}(S^+_{0.10,e})=(0,0,10),
}
\]

\[
\boxed{
\operatorname{inertia}(S^+_{0.10,o})=(0,0,10).
}
\]

The corresponding pole-free minimum LDL pivots are

\[
0.861456802259748\ldots
\quad\text{(even-v)},
\]

\[
0.980178259102018\ldots
\quad\text{(odd-v)},
\]

and the pole-update denominators are

\[
1.051985718261438\ldots,
\]

\[
0.991048190948541\ldots.
\]

These independently reproduce v13.816.

## 3. Independent cross-check of the \(\rho=0.10\) plus remote Gram

Using a freshly computed Cholesky factor of the independently reconstructed plus effective core, rather than the frozen v13.816 Cholesky payload, the normalized remote-Gram maxima through two million are

\[
\boxed{
0.03639456413953569
\quad\text{(even-v)},
}
\]

\[
\boxed{
0.01908829473217616
\quad\text{(odd-v)}.
}
\]

The corresponding analytic far envelopes are

\[
\boxed{
7.79019798869\times10^{-5}
\quad\text{(even-v)},
}
\]

\[
\boxed{
4.07402612173\times10^{-5}
\quad\text{(odd-v)}.
}
\]

These agree with the v13.816 verifier targets and remain comfortably inside its widened caps

\[
0.0365,\ 10^{-4}
\]

and

\[
0.0192,\ 6\times10^{-5}.
\]

Thus the plus-tail result is not an artifact of the frozen Cholesky payload.

## 4. Independent plus-tail floor reconstruction

A separate high-precision evaluation of the v13.816 plus-tail lower-bound formulas gives

\[
\gamma_e^+(4001)
=
3.82049621074658040548\ldots,
\]

\[
\gamma_o^+(4002)
=
3.82066116500621993386\ldots.
\]

These reproduce the safe v13.816 bounds

\[
3.82049621074657,
\qquad
3.82066116500621.
\]

Using the widened v13.816 remote-Gram caps, the terminal safe margins are reproduced as

\[
\boxed{
3.7838955512877932
\quad\text{(even-v)},
}
\]

\[
\boxed{
3.8014007953093420
\quad\text{(odd-v)}.
}
\]

Therefore v13.816's conclusion is independently corroborated numerically before the tighter endpoint work begins.

## 5. Radius parameterization

The common midpoint builder is now parameterized by both endpoint sign and endpoint radius:

\[
F_\rho^{(s)}
=
A+s\rho B_{\rm sm},
\]

\[
Z_n^{(s)}
=
Z_n+\frac{s\rho\pi}{2}.
\]

The defaults remain

\[
\rho=0.10,
\qquad
s=-1,
\]

so all previously audited minus-endpoint scripts retain their old call semantics.

## 6. Fresh \(\rho=0.02\) minus endpoint midpoint

Use the same theorem-scale cores and buffers.

Even-v:
\[
C_e=\{5,7,\ldots,23\},
\qquad
F_e=\{25,27,\ldots,3999\}.
\]

Odd-v:
\[
C_o=\{6,8,\ldots,24\},
\qquad
F_o=\{26,28,\ldots,4000\}.
\]

For

\[
F^-_{0.02}=A-0.02B_{\rm sm},
\]

the even-v effective-core eigenvalues begin

\[
\boxed{
-0.028353188898810,
-0.020179901674853,
-0.010474181546635,
-0.002661799708406,
0.245976602526821,
1.049819338534858,\ldots
}
\]

and the odd-v spectrum begins

\[
\boxed{
-0.027367219923063,
-0.020214857627285,
-0.011458487752410,
-0.003985706539651,
0.816378454801791,
1.475890226388034,\ldots
}
\]

Therefore

\[
\boxed{
\operatorname{inertia}(S^-_{0.02,e})=(4,0,6),
}
\]

\[
\boxed{
\operatorname{inertia}(S^-_{0.02,o})=(4,0,6).
}
\]

The pole-free minimum pivots are

\[
0.624381973268005
\quad\text{(even-v)},
\]

\[
0.699374957660604
\quad\text{(odd-v)},
\]

with pole-update denominators

\[
1.063338676824682,
\]

\[
0.989143722012079.
\]

The smallest-magnitude negative levels are still separated from zero by

\[
2.66\times10^{-3}
\quad\text{and}\quad
3.99\times10^{-3},
\]

so the midpoint sign split is not a binary64 ambiguity.

## 7. Fresh \(\rho=0.02\) plus endpoint midpoint

For

\[
F^+_{0.02}=A+0.02B_{\rm sm},
\]

the even-v effective-core spectrum begins

\[
\boxed{
0.002423439244832,
0.010369949733561,
0.020121273709251,
0.028234238735820,
0.354195071095960,
1.111027957748426,\ldots
}
\]

and odd-v begins

\[
\boxed{
0.006832063813425,
0.014806116128875,
0.022167249010987,
0.035233677338956,
0.891052177968709,
1.528048943412799,\ldots
}
\]

Thus

\[
\boxed{
\operatorname{inertia}(S^+_{0.02,e})=(0,0,10),
}
\]

\[
\boxed{
\operatorname{inertia}(S^+_{0.02,o})=(0,0,10).
}
\]

The pole-free minimum pivots are

\[
0.703450233625058
\quad\text{(even-v)},
\]

\[
0.793150530082642
\quad\text{(odd-v)},
\]

with pole-update denominators

\[
1.058946289028944,
\]

\[
0.989893805932665.
\]

The smallest plus levels

\[
2.4234\times10^{-3},
\qquad
6.8321\times10^{-3}
\]

remain comfortably above floating-point noise, but are much tighter than at radius \(0.10\). The \(\rho=0.02\) outward certificate must therefore retain the hardened proof discipline developed in v13.814–816.

## 8. Certification architecture for \(\rho=0.02\)

The midpoint anatomy is exactly the desired one:

\[
\boxed{
F^-_{0.02}: 4\text{ negative}+6\text{ positive},
}
\]

\[
\boxed{
F^+_{0.02}: 10\text{ positive},
}
\]

in both parity sectors.

The next gates should mirror the now-audited \(\rho=0.10\) architecture:

1. freeze exact-dyadic negative four-planes and positive six-plane preconditioners for the minus endpoint;
2. freeze standard-core Cholesky preconditioners for the plus endpoint;
3. independently audit hashes, exact ranks, coupling/residual/reference caps before theorem use;
4. certify the \(\rho=0.02\) remote tail floors;
5. replay the remote residual Grams with the shifted generators
   \[
   Z_n\mapsto Z_n\pm0.01\pi;
   \]
6. prove
   \[
   \operatorname{ind}_{-}(F^-_{0.02,\rm tail})=4,
   \qquad
   \operatorname{ind}_{-}(F^+_{0.02,\rm tail})=0
   \]
   in each parity;
7. conclude
   \[
   N_{\rm tail}^{(e)}(0.02)
   =
   N_{\rm tail}^{(o)}(0.02)
   =
   4.
   \]

The separate two-mode low-core Feshbach problem remains outside this tail theorem.

## Result

The \(\rho=0.10\) plus endpoint of v13.816 has been independently reproduced on a separate numerical path.

The next theorem-scale radius already has the correct midpoint anatomy:

\[
\boxed{
\operatorname{inertia}(S^-_{0.02})=(4,0,6),
\qquad
\operatorname{inertia}(S^+_{0.02})=(0,0,10)
}
\]

in both parity sectors.

No \(\rho=0.02\) infinite endpoint theorem is promoted yet.
