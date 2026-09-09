# Cone Derivation Ledger v13.369 — Shell Contact as Joint Zero of Remainder and Curvature Coordinates

**Date:** 2026-09-09

## Purpose
Continue v13.362--v13.368 by isolating the exact two-coordinate condition for a quotient-block staircase vertex to lie on the product shell.

## Exact coordinates
For
\[
q=\lfloor n/k\rfloor,
\qquad
R_q=\lfloor n/q\rfloor,
\]
define
\[
\boxed{s_q=n-qR_q=n\bmod q}
\]
and
\[
\boxed{C_{k,q}=q(R_q-k)}.
\]
Then
\[
\boxed{\Delta_k=n-kq=s_q+C_{k,q}}.
\]
Both terms are nonnegative.

## Exact zero loci
\[
\boxed{s_q=0\iff q\mid n}
\]
while
\[
\boxed{C_{k,q}=0\iff k=R_q}.
\]
Thus remainder and transport detect distinct structures: arithmetic divisibility of the quotient label versus geometric terminality in the horizontal block.

## Joint-zero shell criterion
Because both terms are nonnegative,
\[
\boxed{\Delta_k=0\iff s_q=0\text{ and }C_{k,q}=0.}
\]
Equivalently,
\[
\boxed{kq=n\iff q\mid n\text{ and }k=R_q.}
\]
At the joint zero,
\[
(k,q)=\left(\frac nq,q\right),
\]
a true divisor-lattice shell contact.

## Strata
- Contact: \((s_q,C_{k,q})=(0,0)\).
- Stable off-shell terminal: \(s_q>0,C_{k,q}=0\).
- Strict descent/interior: \(C_{k,q}>0\), regardless of whether \(s_q=0\) or \(s_q>0\).

Important: \(s_q=0,C_{k,q}>0\) is allowed; it is an interior point of a block whose terminal endpoint is a divisor contact.

## Quarter-mode form
From the mixed-curvature checkpoint,
\[
C_{k,q}=4\sum M_F^2
\]
over the endpoint strip. Hence
\[
\boxed{
\Delta_k
=s_q+4\sum M_F^2.
}
\]
Shell contact requires both terminal remainder and accumulated quarter-mode transport to vanish.

## Relation to v13.368
The product-field mixed invariant gives only the product
\[
q(R_q-k).
\]
The quotient decomposition supplies \(q\) separately, thereby resolving the reciprocal-scale ambiguity for these arithmetic strips. This resolution is carrier-specific to the divisor quotient geometry.

## Counting consequence
The number of joint-zero quotient-block endpoints is exactly
\[
\boxed{\tau(n)}.
\]
For \(n>1\),
\[
\boxed{\tau(n)=2\iff n\text{ prime}.}
\]
This is the classical divisor-count criterion in the new two-coordinate geometry, not a new factoring test.

## Guardrails
1. Zero transport alone means terminality, not divisibility.
2. Zero remainder alone means \(q\mid n\), not current-column shell contact.
3. Shell contact is the simultaneous zero.
4. Quarter-mode transport does not replace the arithmetic remainder coordinate.
5. No new primality or asymptotic theorem is asserted.

## Companion note
`research-notes/Shell_Contact_as_Joint_Zero_of_Remainder_and_Curvature_Coordinates.md`
