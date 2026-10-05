# Cone Derivation Ledger v14.029 — Outward M8000 mu=1 Frozen-Complement Cholesky Certificate

**Date:** 2026-10-04
**Track:** Lane A / no-twist Suzuki Xi scalar certification
**Status:** [D] penalty reduction from complement positivity to full SPD; [N-cert] directed long-double inverse-factor recursion; [N-cert] binary64 Cholesky backward-error charge; [D] inherited exact-vs-nominal source-operator uncertainty; [N-cert] strictly positive Euclidean complement lower bounds in both parities; [O] certify the six-dimensional protected Schur block to complete v14.027 §6(a).
**Parents:** v14.027, v14.024–026, v14.015.
**Research commits:** cadb42e4712bc10c9729705f361b1290557c5175; 11bf90b4d4aed05a7184892a7c919639843a654c.
**Workflow commits:** 7a8ff73946df5f9e5281f97f1132a267eb7746af; 61e21853ea62c231d7c09e488a46c8534408f386.
**Audit context:** External Audit Round 158 independently verifies v14.027 and confirms that only its three finite outward computations remain.
**Collision check (original):** immediately before this write, live HEAD was 61e21853ea62c231d7c09e488a46c8534408f386 and v14.028 was absent.
**Renumbering note (External Audit):** this entry's commit (`cb73959`, 2026-10-04 21:01:37 -0400 = 2026-10-05 01:01:37 UTC) collided with the External Audit Round 158 entry (`380639e`, 2026-10-05 00:42:28 UTC), which landed first by about 19 minutes. Per the standing commit-timestamp precedence rule, Round 158 keeps v14.028 and this entry is renumbered to **v14.029**, with no change to its mathematical content. See External Audit Round 159 for the full writeup.

---

## 1. Scope

v14.027 §6(a) asks for an outward certificate of positivity of the finite shifted front

\[
H_p:=A_{p,\le8000}-\Pi_{4000<n\le8000}
\]

in both parity sectors.

The protected six-plane has eigenvalues far below binary64 resolution, so this entry does not attempt to certify the whole front at once.

Instead it closes the large-dimensional component of the Feshbach proof: positivity of H_p on the Euclidean orthogonal complement of the frozen source-active six-plane.

---

## 2. Penalty lemma [D]

Let P be the fixed binary64 six-column carrier used by the v14.008/v14.024 Feshbach replays.

For Lambda>0 define

\[
H_{p,+}=H_p+\Lambda PP^*.
\]

If x satisfies P^*x=0, then

\[
x^*H_{p,+}x=x^*H_px.
\]

Therefore any certified global lower bound

\[
H_{p,+}\succeq\delta I
\]

implies

\[
\boxed{
H_p\big|_{\operatorname{Ran}(P)^\perp}\succeq\delta I.
}
\]

The replay uses Lambda=1.

---

## 3. A-posteriori Cholesky certificate [D]

Let L be the binary64 Cholesky factor of the stored penalized matrix.

The exact Gram of the computed factor satisfies

\[
\lambda_{\min}(LL^*)
=
\|L^{-1}\|_2^{-2}
\ge
\frac{1}{n\|L^{-1}\|_\infty^2}.
\]

A rigorous upper bound on \(\|L^{-1}\|_\infty\) is obtained row by row from

\[
y_i
=
\frac{1+\sum_{j<i}|L_{ij}|y_j}{L_{ii}},
\]

with every positive dot product charged by a standard long-double gamma_n envelope and every final operation directed upward with nextafter.

The Cholesky factorization itself is charged by the standard backward-error inequality

\[
|\Delta H|
\le
\gamma_{n+1}|L||L|^*
\]

hence

\[
\|\Delta H\|_2
\le
\gamma_{n+1}\|L\|_F^2.
\]

The factor Frobenius norm is accumulated with an outward long-double gamma_n bound.

---

## 4. Additional exact-vs-stored charges [D/N-cert]

The final lower bound also subtracts:

1. the established source-faithful exact-vs-nominal operator allowance
\[
2.1\times10^{-13};
\]
2. shell-diagonal subtraction rounding;
3. binary64 formation of PP^*;
4. matrix addition and symmetrization rounding.

The last three are bounded in operator norm through outward Frobenius envelopes.

For the rank-six product,

\[
\|\operatorname{fl}(PP^*)-PP^*\|_2
\le
\gamma_6\|P\|_F^2.
\]

No midpoint eigenvalue is used in the PASS criterion.

---

## 5. Even-v certificate [N-cert]

The directed replay gives

\[
\|L^{-1}\|_\infty
\le
5.65912605969236033,
\]

and therefore

\[
\lambda_{\min}(LL^*)
\ge
7.8062287296656320865\times10^{-6}.
\]

The Cholesky backward-error charge is

\[
1.0842679803718513308\times10^{-8}.
\]

The complete matrix-formation charge, including shell shift and PP^* formation, is

\[
2.2125172082691993756\times10^{-13}.
\]

After also subtracting the source-operator allowance,

\[
\boxed{
\delta_e
>
7.795385618610192746\times10^{-6}.
}
\]

Hence

\[
\boxed{
H_e\big|_{\operatorname{Ran}(P_e)^\perp}
\succeq
7.7953856\times10^{-6}I.
}
\]

---

## 6. Odd-v certificate [N-cert]

The directed replay gives

\[
\|L^{-1}\|_\infty
\le
2.7677197175106956998,
\]

and

\[
\lambda_{\min}(LL^*)
\ge
3.2635914992737832972\times10^{-5}.
\]

The Cholesky backward-error charge is

\[
1.0844310609874539038\times10^{-8},
\]

and the complete matrix-formation charge is

\[
2.2126536238387476288\times10^{-13}.
\]

Thus

\[
\boxed{
\delta_o
>
3.2625070250862596046\times10^{-5}.
}
\]

Therefore

\[
\boxed{
H_o\big|_{\operatorname{Ran}(P_o)^\perp}
\succeq
3.2625070\times10^{-5}I.
}
\]

---

## 7. Why this is sufficient for the remaining Feshbach step [I]

The v14.024 mu=1 LDDD graph replay has final coupling residual norms only

\[
2.90\times10^{-28}\quad\text{even},
\qquad
1.49\times10^{-27}\quad\text{odd}.
\]

Using the newly certified complement floors, the quadratic residual corrections scale at most like

\[
\frac{\|R_e\|^2}{\delta_e}
=O(10^{-50}),
\qquad
\frac{\|R_o\|^2}{\delta_o}
=O(10^{-49}).
\]

These are vastly below the midpoint protected lower eigenvalues

\[
5.70\times10^{-30}\quad\text{even},
\qquad
1.44\times10^{-26}\quad\text{odd}.
\]

Consequently the complement-solve uncertainty is no longer the delicate part of v14.027 §6(a).

The only remaining finite-front issue is an outward enclosure of the six-dimensional variational/protected Schur matrix itself.

---

## 8. Failed alternate route [G]

A preceding attempt used the pole-free structured Cauchy block as an indefinite Haynsworth base.

In even parity that base has two negative directions and a minimum absolute scalar LDL pivot about 1.62e-7; the associated binary64 inverse actions showed residuals of order 10.

That route is rejected and no mathematical conclusion is taken from it.

The positive penalized-Cholesky route above supersedes it.

---

## 9. Result

The large-dimensional portion of v14.027 §6(a) is closed:

\[
\boxed{
\delta_e>7.7953856\times10^{-6},
\qquad
\delta_o>3.2625070\times10^{-5}.
}
\]

Thus the remaining finite-front certification is purely six-dimensional.

---

HANDOFF
target: sandbox
type: audit
parent: v14.029
status: open
action: Independently audit the outward penalized-Cholesky complement certificate, especially the directed inverse-factor recursion, the Cholesky backward-error norm conversion, and the separate shell-shift/PP^T/addition rounding charges; confirm whether the stated delta_e and delta_o may be consumed as rigorous Euclidean complement floors in the v14.027 finite-front Feshbach step.
deliverable: theorem-or-obstruction
constraints: Do not infer positivity of the six-dimensional protected Schur block from this entry; that remains a separate open finite calculation.
