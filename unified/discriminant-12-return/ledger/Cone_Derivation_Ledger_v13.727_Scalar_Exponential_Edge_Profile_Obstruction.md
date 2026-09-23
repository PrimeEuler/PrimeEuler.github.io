# Cone Derivation Ledger v13.727 — Scalar Exponential Edge Profile Obstruction

Date: 2026-09-23

Status: direct weak test of the scalar ansatz \(q(\xi)=c e^{-\xi}\) against the compensated Suzuki edge equation from v13.725.

Synchronization: live head before this write is v13.726, commit \`30fb084be82b9ad5dcbfa96654273630dfb69ca6\`. That entry is a separate representation-theoretic lane and does not collide with this Suzuki edge calculation.

## 1. Equation and scalar ansatz

Use
\[
(S_{\rm edge}q)(\xi)
=
\int_0^\infty g(\xi-\eta)q(\eta)\,d\eta
-\lambda\int_0^\infty\min(\xi,\eta)q(\eta)\,d\eta,
\]
modulo the inherited constant-output gauge, and the compensated source
\[
S_{\rm edge}q=e^{-\xi}-\delta_0.
\]

Set
\[
q(\xi)=c e^{-\xi}.
\]

Define
\[
J_g(\xi):=\int_0^\infty g(\xi-\eta)e^{-\eta}\,d\eta.
\]

The Green term is elementary:
\[
\int_0^\infty\min(\xi,\eta)e^{-\eta}\,d\eta
=
\int_0^\xi\eta e^{-\eta}\,d\eta
+\xi\int_\xi^\infty e^{-\eta}\,d\eta
=
1-e^{-\xi}.
\]

Hence
\[
\boxed{
S_{\rm edge}(c e^{-\xi})
=
c\left[J_g(\xi)-\lambda(1-e^{-\xi})\right].
}
\]

For Suzuki's locally integrable/continuous screw kernel \(g\), this left side is a regular distribution on the closed half-line. In particular it carries no atom at \(\xi=0\).

## 2. Weak boundary test

Let the weak test space retain the boundary functional, e.g.
\[
\varphi\in C_c^\infty([0,\infty)),
\]
with arbitrary \(\varphi(0)\).

The equation would require
\[
c\int_0^\infty
\left[J_g(\xi)-\lambda(1-e^{-\xi})\right]\varphi(\xi)\,d\xi
=
\int_0^\infty e^{-\xi}\varphi(\xi)\,d\xi-\varphi(0).
\]

The left-hand side is induced by a locally integrable function. The right-hand side contains the singular measure \(-\delta_0\). By uniqueness of the Lebesgue decomposition of distributions of order zero (equivalently, by a shrinking boundary-test sequence), no finite scalar \(c\) can make these equal.

Explicitly choose \(\varphi_\varepsilon(\xi)=\varphi(\xi/\varepsilon)\) with \(\varphi(0)=1\) and compact support. Local integrability gives
\[
\langle S_{\rm edge}(ce^{-\xi}),\varphi_\varepsilon\rangle\to0,
\]
and
\[
\int_0^\infty e^{-\xi}\varphi_\varepsilon(\xi)\,d\xi\to0,
\]
whereas
\[
-\langle\delta_0,\varphi_\varepsilon\rangle=-1.
\]
Thus the proposed equality would force
\[
0=-1,
\]
a contradiction.

Therefore
\[
\boxed{\text{no scalar }c\text{ satisfies the compensated equation in the boundary-sensitive weak sense}.}
\]

## 3. Constant-output gauge cannot repair the obstruction

Allow
\[
S_{\rm edge}q=e^{-\xi}-\delta_0+C.
\]

A constant \(C\) is still a regular distribution. Against the shrinking boundary tests its contribution is \(O(\varepsilon)\), so it cannot cancel \(-\delta_0\).

Thus the obstruction survives the inherited \(P_A\) constant gauge.

## 4. Interior-only caveat

If one instead tests only with
\[
C_c^\infty((0,\infty)),
\]
then \(\delta_0\) is invisible. That weaker interior equation would demand
\[
c\left[J_g(\xi)-\lambda(1-e^{-\xi})\right]
=
e^{-\xi}+C,\qquad \xi>0.
\]

Equivalently,
\[
J_g(\xi)
\in \operatorname{span}\{1,e^{-\xi}\}.
\]

This is an additional highly restrictive condition on Suzuki's screw kernel and is not implied by the edge construction. Even if it happened to hold, it would solve only the punctured/interior equation, not the source-faithful compensated equation carrying the boundary trace.

## 5. Result for the Suzuki--Xi bridge

The scalar edge-resolvent hypothesis from v13.725 fails in the natural boundary-sensitive weak formulation:
\[
\boxed{
S_{\rm edge}^{-1}(e^{-\xi}-\delta_0)\ne c e^{-\xi}
\quad\text{for every finite scalar }c,
}
\]
provided the inverse is interpreted in a space where the compensated boundary source is retained.

Hence the finite/edge Suzuki deficiency channel cannot be reduced to the raw exponential Xi/Mellin channel by a scalar normalization alone.

The required object is genuinely
\[
\boxed{
q(\xi)=S_{\rm edge}^{-1}(e^{-\xi}-\delta_0),
}
\]
and its Laplace/theta pairing supplies a nontrivial edge transfer multiplier.

\[
\boxed{\textbf{FAIL: scalar exponential profile in boundary-sensitive weak sense.}}
\]

Next gate: derive the Laplace/Wiener--Hopf equation for this compensated \(q\), retaining the boundary trace, and identify the resulting transfer multiplier that must intervene between Suzuki's deficiency characteristic and the Xi theta current.
