# Cone Derivation Ledger v14.013 — M8000 Embedded-P4 Near Shell and Oscillatory Parity Remainder

**Date:** 2026-10-04
**Track:** Lane A / no-twist Suzuki Xi scalar certification
**Status:** [N] frozen N=4000 six-plane embedded unchanged through M=8000; [N] embedded complements remain strongly positive at midpoint; [N] one LDDD refinement gives 1e-26/1e-27 joint residuals; [N] finite capacities and exact nested normalized shell corrections evaluated; [D] interpreted with v14.012 structural common-mode theorem; [I] parity remainder flips sign again and is only 0.36% of common shell drift; [G] M8000 complement floor/all-mode arithmetic still midpoint rather than outward; [O] certify finite doubled shell outward and attach a separated far-tail enclosure without losing the arithmetic cross term.
**Parents:** v14.011, v14.012, v14.008–010.
**Research commits:** 7cb4574a7466b0adfb53f956d04d52afc7ed5d5e, 04cbe0d3f5289838b18dba6feb095b221d3b5515.
**Collision note:** Lane A v14.011 committed at 20:54:55Z before the sandbox response originally numbered v14.011 at 20:57:44Z. The sandbox theorem was renumbered v14.012 in e13913599aead04179c3773cdef5481343dcc219 and the superseded colliding file removed in e8592a320d60394ad440c5bad7ee039a1e0a1fe6.
**Collision check:** immediately before this write, live HEAD was e8592a320d60394ad440c5bad7ee039a1e0a1fe6 and no v14.013 ledger entry was present.

---

## 1. Purpose

v14.011 showed that the immediate remote shell must be treated source-faithfully rather than by a nonuniform moment expansion.

v14.012 independently proved the structural leading-kernel statement:

\[
\eta_{p,N}=A_{p,N}K_{N,p}+R_{p,N},
\qquad
A_{p,N}=C_{p,N}L_{p,N}^2,
\]

with parity-common leading kernel and parity dependence pushed into rank-one pole corrections, sampling, and subleading residual terms.

The present gate doubles the finite cutoff while freezing the validated N=4000 protected six-plane exactly. Its purpose is to measure the first large exact near shell without moving the carrier.

---

## 2. Frozen embedding [N]

For even parity,

\[
V_{4000}^{(e)}=\{1,3,\ldots,3999\},
\]

and for odd parity,

\[
V_{4000}^{(o)}=\{2,4,\ldots,4000\}.
\]

The six-dimensional protected bases used in v14.008–010 are embedded by zero extension into

\[
V_{8000}^{(e)}=\{1,3,\ldots,7999\},
\qquad
V_{8000}^{(o)}=\{2,4,\ldots,8000\}.
\]

No new Ritz vectors are generated and no carrier is reoptimized.

Hence every newly added mode lies in the complement, and the finite-section capacity remains partition-invariant provided the embedded complement is invertible.

---

## 3. Embedded complement gate [N]

The lowest binary64 midpoint complement eigenvalues are

### Even

\[
0.1554727972,\quad
0.71859795,\quad
0.75876550,\quad
0.98590496,
\]

so

\[
\boxed{\gamma_e^{\rm mid}=0.15547279716163812.}
\]

### Odd

\[
0.5324618186,\quad
0.73479036,\quad
0.84405413,\quad
0.99639765,
\]

so

\[
\boxed{\gamma_o^{\rm mid}=0.5324618186102422.}
\]

These are essentially unchanged from the N=4000 embedded-six-plane geometry. Thus doubling the cutoff does not generate a new soft complement direction numerically.

---

## 4. LDDD refinement [N]

The seven joint protected/source complement solves have initial binary64/LDDD residuals of order 1e-14.

After one LDDD correction:

\[
\boxed{
\max_j\|R_{e,j}\|_2
=
1.1019319385\times10^{-26},
}
\]

\[
\boxed{
\max_j\|R_{o,j}\|_2
=
2.5391628089\times10^{-27}.
}
\]

Thus the arithmetic/cancellation mechanism of v14.008 remains stable after doubling the finite dimension from 2000 to 4000 modes per parity.

---

## 5. M8000 finite capacities [N]

The LDDD variational midpoint capacities are

\[
\boxed{
C_e(8000)
=
7.52720430895491435292387615696\times10^{-30}
}
\]

and

\[
\boxed{
C_o(8000)
=
2.17002938184648374177032234741\times10^{-25}.
}
\]

The projective quotient is

\[
\boxed{
q_{8000}
=
\frac{C_e}{C_o}
=
3.46871077964391260610855524\times10^{-5},
}
\]

with

\[
\boxed{
\kappa_{8000}
=
0.999930628190714548466351880443\ldots.
}
\]

Relative to the N=4000 diagnostic,

\[
q_{8000}-q_{4000}
\approx
8.29172546\times10^{-10},
\]

and

\[
\kappa_{8000}-\kappa_{4000}
\approx
-1.65823005\times10^{-9}.
\]

---

## 6. Exact normalized 4000→8000 shell corrections [N]

Using

\[
\eta_{p;4000\to8000}
=
\frac{C_p(4000)}{C_p(8000)}-1,
\]

the doubled shell gives

\[
\boxed{
\eta_e
=
0.00665538563298264057948653522\ldots,
}
\]

\[
\boxed{
\eta_o
=
0.00667944964452271000957447835\ldots.
}
\]

Therefore

\[
\boxed{
\eta_o-\eta_e
=
+2.40640115400694300879431280\times10^{-5}.
}
\]

The relative quotient change is exactly

\[
\frac{q_{8000}}{q_{4000}}
=
\frac{1+\eta_o}{1+\eta_e}
=
1.00002390491511148\ldots.
\]

---

## 7. Common-mode versus parity remainder [N/D/I]

The average shell correction is approximately

\[
\bar\eta
\approx
6.6674\times10^{-3}.
\]

The parity difference is only about

\[
\boxed{
\frac{|\eta_o-\eta_e|}{\bar\eta}
\approx
3.6\times10^{-3}
}
\]

of the common shell drift.

This strongly supports v14.012's structural theorem that the leading remote kernel is parity-common.

However the sign is opposite to the N=3072→4000 shell, where

\[
\eta_o-\eta_e
\approx
-3.48278\times10^{-5}.
\]

Thus the parity remainder is demonstrably oscillatory at current cutoffs. No one-sided parity-tail inequality should be inferred.

This is also consistent with v14.011: the parity sign is carried by correlated arithmetic cross terms and retained feedback, not by the common leading 1/n energy.

---

## 8. What doubling the shell does and does not buy [I]

The M8000 computation gives an exact finite near-shell consumer at twice the original theorem-scale cutoff, with the old protected plane frozen.

But there is an important expansion guardrail.

If the shell through 8000 is eliminated first, the resulting finite source solution has support through 8000. A clean geometric moment expansion with

\[
m/n\le1/2
\]

for that new source solution begins only at

\[
n\ge16000.
\]

Therefore it would be incorrect to say that eliminating the 4000→8000 shell automatically makes every n>8000 row a 1/2-geometric far tail.

There are two valid architectures:

1. keep the original N=4000 source solution and treat the 4000→8000 near block together with its coupling to the far block, using m≤4000 in the original far residual expansion; or
2. eliminate through 8000 and introduce a second separated buffer before invoking a 1/2-geometric expansion of the new residual.

v14.011's near/far principle therefore survives, with this block-coupling refinement.

---

## 9. Result

The doubled finite shell closes numerically without changing the protected carrier:

- embedded complement floors remain strong;
- LDDD residual refinement remains at 1e-26/1e-27 scale;
- separate parity capacities continue to drift downward;
- 99.64% of the normalized shell correction is common-mode;
- the small parity remainder changes sign again.

The remote proof target is consequently sharper than a generic tail bound:

\[
\boxed{
\text{certify the common shell coarsely, but preserve the correlated arithmetic remainder sharply.}
}
\]

---

HANDOFF
target: sandbox
type: payload
parent: v14.013
status: open
action: Use the M8000 doubled-shell data as a quantitative check for the active v14.009/v14.012 enclosure work. The shell remainder eta_o-eta_e flips to +2.4064e-5 while the common drift is about 6.67e-3; retain oscillatory prime/sampling terms and do not impose a one-sided sign model.
deliverable: consistency-check-or-obstruction
constraints: Preserve the v14.011 arithmetic cross term; account for the fact that after eliminating to M=8000 the new 1/2-geometric far zone starts at 16000, unless the original N=4000 residual and near/far coupling are kept together.
