# Cone Derivation Ledger v13.832 — Full \(\rho=0.02\) Endpoint Inertia Theorem

Date: 2026-09-28.

Lane: A.

Status: [C] full minus-endpoint negative index \(4\) and zero kernel in both parity sectors; [C] full plus-endpoint negative index \(2\) and zero kernel in both parity sectors; [C] signed Pontryagin endpoint spectral flow \(4-2=2\); [G] ordinary six-root multiplicity remains a separate low-core meromorphic/Krein problem.

Parents: v13.821, v13.824–831.

Research artifacts:

- research-notes/suzuki_full_endpoint_rho002_frozen_carriers.py
  - commit c33f8e3770430014e091fe38810d01d8008e1154

- research-notes/suzuki_full_endpoint_rho002_inertia_certificate.py
  - initial theorem commit f0b39b593b9274d9ce4359077e5c90dcc6a1afb5
  - 12-core reference-envelope correction c6d95c38b23c6f1fcebbf0ec3117c90e714870c6

External Audit Round 111, v13.831, independently confirmed the exact full smooth-bulk Pontryagin index two and the M3999/4000 low-core endpoint sign pattern used as the handoff into this theorem.

No GitHub workflow/status run is attached to the present full-endpoint certificate.

## 1. Why the direct remote-correction estimate is unnecessary

The finite low-core Schur margins of v13.830 suggested bounding

\[
S_C^{(\infty)}-S_C^{(M)}
\]

directly.

That is not the most stable proof architecture because the minus tail endpoint is indefinite with exactly four negative directions.

Instead use sign-subspace geometry:

- at the minus endpoint, construct an infinite positive subspace of codimension four;
- at the plus endpoint, use the already certified positive tail together with a compactly supported two-dimensional negative trial space.

This avoids any large norm of the full indefinite tail inverse.

## 2. Frozen theorem carriers

### Minus endpoint

After eliminating the positive finite buffer

even-v:
\[
25,27,\ldots,3999,
\]

odd-v:
\[
26,28,\ldots,4000,
\]

retain the first twelve parity coordinates:

even-v:
\[
1,3,\ldots,23,
\]

odd-v:
\[
2,4,\ldots,24.
\]

The eight positive directions of the resulting \(12\times12\) effective core are frozen as exact binary64 dyadics.

Payload SHA-256:

even-v:
\[
\boxed{
\texttt{99d84bde14147780b80d5b2de4b9b9c71778e7a9b8ec508cc819be8875b61ce6}
}
\]

odd-v:
\[
\boxed{
\texttt{2b252375df5805127acb66dcfd9bdb21bb9530c95f062c8bb8fc11bbcec7b224}
}
\]

The runtime verifier checks exact nonzero \(8\times8\) dyadic minors and positive Cholesky diagonals.

The first-minor diagnostics are approximately

\[
-1.26576\times10^{-10}
\quad\text{even-v},
\]

\[
2.03395\times10^{-8}
\quad\text{odd-v}.
\]

Thus both frozen positive carriers have rank eight exactly.

### Plus endpoint

A compactly supported two-dimensional negative subspace is frozen directly.

even-v support:
\[
\{1,3\},
\]

with identity basis and SHA-256

\[
\boxed{
\texttt{eb8ddbe867b8bd63a582111adee047ff59ef3103c373d6c23553e0df43ee92d3}.
}
\]

odd-v support:
\[
\{2,4,6,8\},
\]

with frozen two-plane SHA-256

\[
\boxed{
\texttt{8dc6e0eb24b62fb553d179fd5796d1c7de5acbc936d7d8f6311c673151a46039}.
}
\]

The exact first \(2\times2\) dyadic minors are nonzero.

## 3. Minus endpoint finite twelve-core anatomy

For

\[
F^-_{0.02}=A-0.02B_{\rm sm},
\]

the finite-buffer-eliminated \(12\times12\) effective spectra are

### even-v

\[
\begin{aligned}
&-0.02838296,\ -0.02020899,\ -0.01060547,\ -0.00328207,\\
&\phantom{-}0.00835922,\ 0.03871923,\ 0.24675858,\ 1.05009521,\\
&1.67787288,\ 1.98569249,\ 2.42836371,\ 2.58130499.
\end{aligned}
\]

### odd-v

\[
\begin{aligned}
&-0.02737665,\ -0.02023841,\ -0.01177076,\ -0.00584476,\\
&\phantom{-}0.00294877,\ 0.02062276,\ 0.81800651,\ 1.47941918,\\
&1.79244949,\ 2.09286769,\ 2.43639786,\ 2.60681186.
\end{aligned}
\]

Thus the finite effective core already has the desired

\[
4^-+8^+
\]

split.

The eight positive reference minima are

\[
\boxed{
0.0083592175546\ldots
\quad\text{even-v},
}
\]

\[
\boxed{
0.0029487721567\ldots
\quad\text{odd-v}.
}
\]

## 4. Self-audit correction: 12-core rounding envelope

The reusable v13.820 reference-defect helper used a hard-coded ten-coordinate dot-product length because its original target core had dimension ten.

The present full problem has dimension twelve.

The new theorem wrapper therefore implements a dimension-generic reference-defect envelope with

\[
n_c=12.
\]

After this correction the outward reference-defect values remain tiny:

\[
\boxed{
7.51\times10^{-16}
\quad\text{even-v},
}
\]

\[
\boxed{
6.99\times10^{-16}
\quad\text{odd-v}.
}
\]

The public cap in both sectors is

\[
1.40\times10^{-15}.
\]

This correction changes no displayed theorem margin but removes a small proof-engineering undercount.

## 5. Minus finite-side outward caps

The frozen eight-planes give coupling norms

\[
\|F_{FC}Q_{8,e}\|_F
\approx1.03318,
\]

\[
\|F_{FC}Q_{8,o}\|_F
\approx0.77466.
\]

The fail-closed caps are

\[
1.08,\qquad0.82.
\]

The outward long-double solve residuals are approximately

\[
1.17\times10^{-15},
\qquad
1.00\times10^{-15},
\]

against caps

\[
1.55\times10^{-15},
\qquad
1.45\times10^{-15}.
\]

The inherited exact buffer floors are the already audited \(\rho=0.02\) values

\[
\mu^-_e>0.0065707609,
\qquad
\mu^-_o>0.0051455413.
\]

After the inherited source/operator uncertainty, solve residual, and reference-defect budgets, the normalized finite eight-plane lower bounds are safely

\[
\boxed{
C_{8,e}>0.99999931\,I,
}
\]

\[
\boxed{
C_{8,o}>0.99999816\,I.
}
\]

## 6. Minus infinite remote replay

The eight-plane dressed residual Gram is accumulated directly through \(16001/16000\), by the eight-level inverse-power replay through \(2,000,000\), and analytically beyond.

Observed explicit normalized Gram maxima are

\[
\boxed{
0.04664598567
\quad\text{even-v},
}
\]

\[
\boxed{
0.02390665275
\quad\text{odd-v}.
}
\]

The widened caps are

\[
0.0490,
\qquad
0.0250.
\]

The analytic far envelopes are approximately

\[
\boxed{
9.9941\times10^{-5}
\quad\text{even-v},
}
\]

\[
\boxed{
5.1076\times10^{-5}
\quad\text{odd-v},
}
\]

against caps

\[
1.20\times10^{-4},
\qquad
7.00\times10^{-5}.
\]

Frozen-coordinate conditioning satisfies

\[
\|L_e^{-1}\|_2\approx10.9375<11.2,
\]

\[
\|L_o^{-1}\|_2\approx18.4154<18.8.
\]

The corresponding dressed-plane norms are

\[
10.9461<11.2,
\qquad
18.4317<18.8.
\]

The residual-operator perturbation caps remain comfortably above the derived values.

## 7. Minus terminal positivity

Use the audited remote floors

\[
\gamma^-_e(4001)>3.18003114023348,
\]

\[
\gamma^-_o(4002)>3.18016610573875.
\]

With the deliberately widened Gram and residual-operator caps, the full terminal lower bounds are

\[
\boxed{
\gamma^-_e C_{8,e}-H_{8,e}
>
3.1308\,I,
}
\]

\[
\boxed{
\gamma^-_o C_{8,o}-H_{8,o}
>
3.1550\,I.
}
\]

The associated normalized post-tail lower bounds are

\[
\boxed{
>0.9845\,I
\quad\text{even-v},
}
\]

\[
\boxed{
>0.9920\,I
\quad\text{odd-v}.
}
\]

Thus the full minus endpoint possesses an infinite-dimensional strict positive subspace of codimension four.

## 8. Exact minus endpoint inertia

The certified tail theorem v13.821 supplies a four-dimensional strict negative tail subspace.

Embedding it with zero low-core coordinates gives

\[
\operatorname{ind}_{-}(F^-_{0.02,\rm full})\ge4.
\]

Section 7 constructs a strict positive subspace of codimension four, hence

\[
\operatorname{ind}_{\le0}(F^-_{0.02,\rm full})\le4.
\]

Therefore

\[
\boxed{
\operatorname{ind}_{-}
(F^-_{0.02,e,\rm full})
=
4,
}
\]

\[
\boxed{
\operatorname{ind}_{-}
(F^-_{0.02,o,\rm full})
=
4.
}
\]

The same inequalities exclude a zero mode, so

\[
\boxed{
\ker F^-_{0.02,e,\rm full}
=
\ker F^-_{0.02,o,\rm full}
=
\{0\}.
}
\]

## 9. Plus compact negative trial spaces

The plus tail is already strictly positive by v13.821.

### even-v

On the first two modes \(\{1,3\}\), the exact-dyadic frozen restriction has nominal negative eigenvalues

\[
-0.03830031,\qquad -0.00719170.
\]

After the full source/operator and arithmetic reserve,

\[
\boxed{
-F^+_{0.02,e}
>
0.0071916\,I
}
\]

on this fixed two-plane.

### odd-v

On the frozen two-plane supported in

\[
\{2,4,6,8\},
\]

the nominal restricted eigenvalues are

\[
-0.01862602,\qquad -0.000616646.
\]

After the same exact-vs-nominal reserve,

\[
\boxed{
-F^+_{0.02,o}
>
0.0006165\,I
}
\]

on the frozen two-plane.

These are compactly supported vectors; no infinite remote correction enters their quadratic forms.

## 10. Exact plus endpoint inertia

The full tail subspace itself is strictly positive and has codimension two in the full parity space.

Therefore

\[
\operatorname{ind}_{\le0}(F^+_{0.02,\rm full})\le2.
\]

Section 9 supplies a two-dimensional strict negative subspace, hence

\[
\operatorname{ind}_{-}(F^+_{0.02,\rm full})\ge2.
\]

Consequently

\[
\boxed{
\operatorname{ind}_{-}
(F^+_{0.02,e,\rm full})
=
2,
}
\]

\[
\boxed{
\operatorname{ind}_{-}
(F^+_{0.02,o,\rm full})
=
2.
}
\]

Again the nonpositive-index upper bound is already exhausted by strict negative directions, so

\[
\boxed{
\ker F^+_{0.02,e,\rm full}
=
\ker F^+_{0.02,o,\rm full}
=
\{0\}.
}
\]

## 11. Full signed endpoint spectral flow

The exact full endpoint inertias are therefore

\[
\boxed{
\operatorname{ind}_{-}(F^-_{0.02})=4,
\qquad
\operatorname{ind}_{-}(F^+_{0.02})=2
}
\]

in each parity sector.

Hence the full endpoint inertia difference is

\[
\boxed{
4-2=2.
}
\]

Because the full smooth bulk has Pontryagin index two, this is a signed Krein/Pontryagin spectral-flow invariant.

It is not, by itself, an ordinary multiplicity count.

## 12. Relation to the finite six-root diagnostic

At N=96, v13.830 observed six real inner generalized roots with invariant bulk signature

\[
2^-+4^+.
\]

The exact full endpoint theorem is perfectly consistent with that finite picture:

\[
4^+-2^-=2.
\]

However the present theorem does not promote the ordinary infinite root count from six finite roots to six exact roots.

That requires a separate argument for the two negative-metric low-core channels, for example through the meromorphic \(2\times2\) Feshbach map and a Krein-aware zero count.

## Guardrails

This theorem does not assert:

- exactly six ordinary full generalized roots in \(|\delta|<0.02\);
- simplicity or reality of two infinite low-core roots;
- individual signatures of nearly degenerate machine-zero Ritz vectors;
- convergence of \(\kappa_0\);
- promotion of \(\kappa_1\);
- RH or GRH.

The platform-dependent decimal eigenvalues of the N=96 restricted \(B\) matrix noted by External Audit Round 111 are not used anywhere in this theorem.

## Result

For each parity sector,

\[
\boxed{
\operatorname{ind}_{-}(F^-_{0.02,\rm full})=4,
\qquad
\ker F^-_{0.02,\rm full}=\{0\},
}
\]

\[
\boxed{
\operatorname{ind}_{-}(F^+_{0.02,\rm full})=2,
\qquad
\ker F^+_{0.02,\rm full}=\{0\}.
}
\]

Therefore the full signed endpoint spectral flow across the certified inner window is

\[
\boxed{2}.
\]

The next unresolved theorem is the ordinary low-core root multiplicity, not endpoint inertia.
