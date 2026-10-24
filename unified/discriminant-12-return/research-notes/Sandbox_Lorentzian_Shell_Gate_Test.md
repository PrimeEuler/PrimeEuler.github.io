# Sandbox Research Note — Lorentzian fixed-shell gate test

**Date:** 2026-10-24. **Lane:** sandbox. **Gate source:** v14.807
(Lorentzian polynomials and the factor-Cone signature), whose next
falsifiable gate reads: choose a canonical homogeneous
fixed-product-shell generating polynomial, test support M-convexity
and every quadratic derivative's Hessian inertia; if this fails,
record a minimal obstruction.

## Canonical choice

For a fixed product shell \(n\), take the factor pairs \((a,b)\) with
\(ab=n\) and homogenize at the shell's maximal degree
\(d = \max(a+b)\):

\[
F_n(x,y,z) = \sum_{ab=n} x^a y^b z^{d-a-b}.
\]

The support is the lattice set
\(S_n = \{(a, b, d-a-b) : ab = n\}\).

## Necessary condition

By the Brändén–Huh theory, the support of a Lorentzian polynomial is
M-convex: for any \(\alpha, \beta\) in the support and any coordinate
\(i\) with \(\alpha_i > \beta_i\), there must exist a coordinate \(j\)
with \(\alpha_j < \beta_j\) and \(\alpha - e_i + e_j\) again in the
support. M-convexity depends only on the support, not on the
coefficients.

## Obstruction theorem (all \(n \ge 3\))

Every shell contains the extreme points
\(\alpha = (1, n, 0)\) and \(\beta = (n, 1, 0)\) (here \(d = n+1\)).
Since \(\alpha_y = n > 1 = \beta_y\), M-convexity requires an exchange
in coordinate \(y\): some \(j\) with \(\alpha_j < \beta_j\) and
\(\alpha - e_y + e_j \in S_n\). The only candidates are

- \(j = x\): \((2, n-1, 0)\), which lies in \(S_n\) only if
  \(2(n-1) = n\), i.e. \(n = 2\);
- \(j = z\): \((1, n-1, 1)\), which would require \(1 \cdot (n-1) = n\),
  impossible.

Hence for every \(n \ge 3\) the exchange fails and \(S_n\) is not
M-convex. Therefore **no polynomial whose support is exactly \(S_n\)
— with any nonzero coefficients whatsoever — is Lorentzian for
\(n \ge 3\)**. The obstruction is at support level.

Corroboration: the full M-convexity test was run for shells
\(n = 1\) to \(24\) (all fail for \(n \ge 3\)), and the extreme-pair
exchange was checked unsatisfiable for all \(n = 3\) to \(500\).

Minimal instance: \(n = 3\), support \(\{(1,3,0), (3,1,0)\}\); the
required intermediate point \((2,2,0)\) belongs to shell \(4\), not
shell \(3\).

Structural reason: a fixed-product shell is a hyperbola arc in the
\((a,b)\) plane; M-convexity demands unit-exchange chain-connectedness
along the simplex, which a hyperbola arc possesses only in the
adjacent case.

## The surviving shells

- \(n = 1\): single point, trivially M-convex.
- \(n = 2\): \(F_2 = xy^2 + x^2 y = xy(x+y)\) (the homogenizing \(z\)
  is inert). Support \(\{(1,2,0), (2,1,0)\}\) is M-convex, and the
  first derivatives are the quadratics \(y^2 + 2xy\) and
  \(x^2 + 2xy\), whose Hessians \(\begin{pmatrix}0&2\\2&2\end{pmatrix}\)
  and \(\begin{pmatrix}2&2\\2&0\end{pmatrix}\) have eigenvalues
  \(1 \pm \sqrt 5\) — exactly one positive. \(F_2\) is Lorentzian in
  its effective variables.

## Independent spot-verification of v14.807

- \(\det \nabla^2 (x^a y^b) = ab(1-d)\, x^{2a-2} y^{2b-2}\) with
  \(d = a+b\): recomputed,
  \(ab[(a-1)(b-1) - ab] = ab(1 - a - b)\). Agrees.
- \(d(3)^2 = 4 < d(2)\, d(4) = 6\): recomputed from
  \(d(2) = d(3) = 2\), \(d(4) = 3\). Agrees; the divisor function is
  not globally log-concave.

## Scope

This closes v14.807's gate for the canonical max-degree
homogenization above. Other normalizations (different homogenizing
degree, weighted or cumulative supports) are new choices, not covered
here; any Lorentzian object in this family must mix shells, which
re-enters v14.807's addition-closure guardrail. Nothing here bears on
the open hyperbolicity-cone-to-causal-cone intertwiner, and no GR or
\(G\) claim is made. Sandbox scripts: `shell_test.py`,
`proof_check.py` (run folder `20261024-lorentzian-shell-test`).
