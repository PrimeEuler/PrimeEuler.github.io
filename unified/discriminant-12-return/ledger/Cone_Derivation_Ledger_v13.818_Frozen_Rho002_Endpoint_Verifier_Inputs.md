# Cone Derivation Ledger v13.818 — Frozen Exact-Dyadic \(\rho=0.02\) Endpoint Verifier Inputs

Date: 2026-09-26

Lane: A.

Status: [D] exact-dyadic \(\rho=0.02\) minus negative four-planes, minus positive six-planes, their Cholesky preconditioners, and plus ten-core Cholesky factors frozen in both parity sectors; [D] runtime SHA-256 and exact rank checks embedded in the frozen modules; [G] no outward \(\rho=0.02\) endpoint theorem promoted yet.

Parents: v13.817.

Research artifacts:

- research-notes/suzuki_endpoint_M3999_rho002_minus_frozen_inputs.py
  - commit 74a2b224962f27532598c496011757687abb5443

- research-notes/suzuki_endpoint_M3999_rho002_plus_frozen_L0.py
  - commit 41da44b70ebef0bb44b17752eaab5ee3e11a6e46

No GitHub workflow/status run is attached.

## 1. Freeze construction

The payloads were regenerated from a fresh source-faithful \(M=3999/4000\) reconstruction at

\[
\rho=0.02.
\]

For the minus endpoint,

\[
F^-_{0.02}=A-0.02B_{\rm sm},
\]

the four negative and six positive midpoint eigendirections were separated in each parity sector.

Column signs were canonicalized by requiring the largest-magnitude component of each eigenvector to be positive.

The frozen preconditioners are

\[
L_{\rm neg}L_{\rm neg}^T
=
-Q_{\rm neg}^TS^-Q_{\rm neg},
\]

\[
L_{\rm pos}L_{\rm pos}^T
=
Q_{\rm pos}^TS^-Q_{\rm pos}.
\]

For the plus endpoint,

\[
F^+_{0.02}=A+0.02B_{\rm sm},
\]

the standard ten-coordinate core is retained and only the midpoint Cholesky factor

\[
L_0L_0^T=S^+_{0.02}
\]

is frozen.

Every stored scalar is an exact IEEE-754 binary64 hexadecimal dyadic.

## 2. Minus endpoint payload hashes

Each parity payload hash covers all four frozen arrays

\[
(Q_{\rm neg},L_{\rm neg},Q_{\rm pos},L_{\rm pos})
\]

using canonical JSON serialization with sorted keys and compact separators.

Even-v:

\[
\boxed{
\texttt{f42f62b50fbd8ebd8e40a692450915ed4f6b4bcb9b5a2822f55f103c6f4bb5b3}
}
\]

Odd-v:

\[
\boxed{
\texttt{550fc794249e79ebb943ac1771542f7c2940827bfe8dfe71c84acc9d477fed9f}
}
\]

The verifier recomputes these hashes at runtime and fails closed on mismatch.

## 3. Exact minus rank checks

The negative four-planes are checked by exact rational evaluation of the first \(4\times4\) dyadic minors.

Even-v:

\[
\det Q_{{\rm neg},e}[1:4]
\approx
4.229675411445356\times10^{-4}\ne0.
\]

Odd-v:

\[
\det Q_{{\rm neg},o}[1:4]
\approx
9.18745847606495\times10^{-2}\ne0.
\]

Therefore both negative payloads have rank four exactly.

The positive six-planes are checked by exact rational evaluation of their first \(6\times6\) dyadic minors.

Even-v:

\[
\det Q_{{\rm pos},e}[1:6]
\approx
8.54925792559225\times10^{-10}\ne0.
\]

Odd-v:

\[
\det Q_{{\rm pos},o}[1:6]
\approx
-3.807883816357752\times10^{-8}\ne0.
\]

Thus both positive payloads have rank six exactly.

These exact rank tests are executed at runtime; no floating numerical-rank threshold is used.

## 4. Minus orthogonality diagnostics

Binary64 diagnostics give

\[
\|Q_{{\rm neg},e}^TQ_{{\rm neg},e}-I\|_2
\approx1.3680\times10^{-15},
\]

\[
\|Q_{{\rm pos},e}^TQ_{{\rm pos},e}-I\|_2
\approx1.2517\times10^{-15},
\]

\[
\|Q_{{\rm neg},o}^TQ_{{\rm neg},o}-I\|_2
\approx8.3473\times10^{-16},
\]

\[
\|Q_{{\rm pos},o}^TQ_{{\rm pos},o}-I\|_2
\approx1.6497\times10^{-15}.
\]

These are diagnostics only; exact rank is established by the rational minors above.

## 5. Minus preconditioner reference scales

The frozen negative reference minima are

\[
\lambda_{\min}(L_{{\rm neg},e}L_{{\rm neg},e}^T)
=
0.00266179970840637\ldots,
\]

\[
\lambda_{\min}(L_{{\rm neg},o}L_{{\rm neg},o}^T)
=
0.00398570653965055\ldots.
\]

Their midpoint inverse norms are approximately

\[
\|L_{{\rm neg},e}^{-1}\|_2
=
19.3826,
\]

\[
\|L_{{\rm neg},o}^{-1}\|_2
=
15.8397.
\]

The frozen positive six-plane reference minima are

\[
0.245976602526821\ldots
\quad\text{(even-v)},
\]

\[
0.816378454801792\ldots
\quad\text{(odd-v)},
\]

with

\[
\|L_{{\rm pos},e}^{-1}\|_2
\approx2.01629,
\]

\[
\|L_{{\rm pos},o}^{-1}\|_2
\approx1.10676.
\]

All Cholesky diagonals are required positive at runtime.

## 6. Plus endpoint hashes and exact rank

The plus endpoint stores only the ten-core Cholesky factor \(L_0\).

Even-v SHA-256:

\[
\boxed{
\texttt{d2bb5e790023af852e349e001876369e5d9fd43a56a85f7fb3edc687d7d3ef5c}
}
\]

Odd-v SHA-256:

\[
\boxed{
\texttt{7eb101a7138b27a92412c9f381a12d53aacd70af437d86ed478f4dc44a86f8df}
}
\]

The runtime verifier recomputes the hash and then evaluates the triangular determinant exactly as a product of dyadic diagonal entries.

Both determinants are nonzero, so

\[
\boxed{
\operatorname{rank}L_{0,e}
=
\operatorname{rank}L_{0,o}
=
10
}
\]

exactly.

Decimal determinant diagnostics are

\[
\det L_{0,e}
\approx3.588046990194519\times10^{-4},
\]

\[
\det L_{0,o}
\approx1.683656020813781\times10^{-3}.
\]

## 7. Plus reference scales

The frozen plus references reproduce the v13.817 smallest midpoint levels:

\[
\lambda_{\min}(L_{0,e}L_{0,e}^T)
=
0.00242343924483203\ldots,
\]

\[
\lambda_{\min}(L_{0,o}L_{0,o}^T)
=
0.00683206381342420\ldots.
\]

The corresponding midpoint inverse norms are

\[
\boxed{
\|L_{0,e}^{-1}\|_2
\approx20.31346,
}
\]

\[
\boxed{
\|L_{0,o}^{-1}\|_2
\approx12.09829.
}
\]

These larger conditioning factors relative to \(\rho=0.10\) are expected from the tighter endpoint radius and must be included explicitly when designing the outward finite-side caps.

## 8. Runtime fail-closed contract

The committed minus freeze module fails closed if any of the following occurs:

1. even or odd SHA-256 mismatch;
2. exact negative first \(4\times4\) minor vanishes;
3. exact positive first \(6\times6\) minor vanishes;
4. any negative-preconditioner diagonal is nonpositive;
5. any positive-preconditioner diagonal is nonpositive.

The plus freeze module fails closed if:

1. either SHA-256 mismatches;
2. the exact triangular determinant vanishes;
3. any Cholesky diagonal is nonpositive.

Thus subsequent outward verifiers can consume immutable frozen coordinates without regenerating eigenspaces or Cholesky factors.

## 9. Next gate

The next certification gate should not regenerate any frozen object.

It should consume these exact payloads and independently audit all \(\rho=0.02\) coupling, residual, reference-defect, buffer-conditioning, remote-Gram, and far-tail caps with the same headroom discipline used in v13.814–816.

Because the smallest even-v scales are only

\[
2.42\times10^{-3}
\quad\text{(plus)}
\]

and

\[
2.66\times10^{-3}
\quad\text{(minus negative)},
\]

the cap audit must occur before either \(\rho=0.02\) endpoint is promoted.

## Result

\[
\boxed{
\textbf{All }\rho=0.02\textbf{ theorem-scale endpoint coordinates and preconditioners are now frozen as exact dyadic payloads.}
}
\]

The hashes and exact runtime rank checks are embedded in the committed artifacts, and no outward \(\rho=0.02\) theorem has yet been claimed.
