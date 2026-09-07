# Cone Derivation Ledger v13.306 — Joint Prime-Operator Schur Bound and 2809 Coercive Cutoff

**Status:** JOINT FIVE-SHIFT PRIME OPERATOR BOUNDED RIGOROUSLY BY SCHUR GEOMETRY; COERCIVE CUTOFF IMPROVED TO 2809. NUMERICAL GALERKIN SPECTRAL RADIUS ~1.94 IS EXPLORATORY ONLY. RH/GRH NOT PROVED.

## 1. Purpose

v13.305 improved the prime contribution by using exact norms of the five individual truncated shifts on [-1,1], reducing the prime bound from 5.852468... to 3.129252.... v13.306 treats all five shifts as one weighted operator and asks whether the finite-interval support geometry gives a smaller rigorous bound before any cancellation is invoked.

For q in {2,3,4,5,7}, write

\[
\ell_q=\log q,
\qquad
a_q=\frac{\Lambda(q)}{\sqrt q},
\]

and

\[
(S_{\ell}f)(x)=f(x-\ell)+f(x+\ell)
\]

with zero extension outside [-1,1]. Then

\[
B_{\rm prime}=-\sum_q a_q S_{\ell_q}.
\]

## 2. Joint Schur row sum

For fixed x, the total absolute kernel row mass is

\[
R(x)=\sum_q a_q\left(\mathbf 1_{|x-\ell_q|\le1}+\mathbf 1_{|x+\ell_q|\le1}\right).
\]

Since the operator is symmetric, Schur's test gives

\[
\|B_{\rm prime}\|\le \sup_{x\in[-1,1]}R(x).
\]

The indicator pattern changes only at the finitely many breakpoints

\[
x=\pm(\ell_q-1),\ \pm(\ell_q+1)
\]

that lie in [-1,1], so the supremum is found by an exact finite interval sweep.

The maximum occurs in the edge region where exactly one translated copy from each prime-power shift remains inside the interval. Hence

\[
\sup_xR(x)=\sum_q a_q.
\]

Numerically,

\[
\boxed{
\|B_{\rm prime}\|\le
\sum_{q\in\{2,3,4,5,7\}}\frac{\Lambda(q)}{\sqrt q}
\approx2.926234182176409.
}
\]

This is smaller than the separate-shift v13.305 bound

\[
3.129252291002081.
\]

No inter-prime cancellation is assumed in this rigorous estimate.

## 3. Numerical joint spectral edge

A Galerkin audit in the odd Dirichlet basis gives the following exploratory spectral radii for the full weighted five-shift matrix:

- 20 odd modes: ~1.8600,
- 40 odd modes: ~1.9224,
- 80 odd modes: ~1.9324,
- 120 odd modes: ~1.9353.

The minimum eigenvalue is the dominant edge in these sections. This strongly suggests that the true joint operator norm may be near 1.94, substantially below the Schur bound 2.92623.

This is numerical evidence only. The value ~1.94 is **not** used in the rigorous coercivity theorem and is not yet an infinite-dimensional certified norm.

## 4. Updated coercivity bound

Retain the v13.304 pieces:

\[
\|H_{\rm odd}\|=\frac\pi2,
\]

analytic archimedean-remainder bound

\[
\|K_{\rm arch\,rem}\|\le2.056338685\ldots,
\]

and tail-decaying explicit cusp and pole bounds.

With the new joint prime constant,

\[
C_{\rm tail}(N)
=
\frac\pi2
+2.926234182176409
+2.056338685\ldots
+\|P_NK_{\rm cusp}P_N\|
+\|P_NK_{\rm pole}P_N\|.
\]

Thus

\[
\langle A_{\rm even}c,c\rangle
\ge
\bigl[\log(N/4)-C_{\rm tail}(N)\bigr]\|c\|_2^2
\]

for odd-mode vectors supported on n>=N.

The first sufficient odd cutoff from these bounds is

\[
\boxed{N=2809.}
\]

This improves the sequence

\[
5.56\times10^6\to52363\to3441\to\boxed{2809}.
\]

## 5. Interpretation

The important structural point is that the prime contribution is not just a sum of five unrelated worst-case shifts. Its finite-interval support geometry already enforces a smaller joint Schur envelope.

At the same time, the Galerkin data indicate further cancellation/interaction may exist inside that envelope. Proving a joint norm closer to ~1.94 would lower the cutoff toward roughly 10^3, but that remains open.

## 6. Guardrails

Established here:

- exact finite-interval joint Schur row function;
- rigorous prime operator norm upper bound 2.926234182176409;
- rigorous sufficient high-tail coercive cutoff N=2809 within the cumulative v13.302-v13.306 framework.

Not established:

- exact joint five-shift operator norm;
- certified infinite-dimensional value near 1.94;
- positivity of the entire operator from this tail estimate alone;
- ker(G_1)!={0}, lambda_1=0, RH, or GRH.

## 7. Files

- `research-notes/suzuki_joint_prime_operator_audit.py`
- this ledger entry

## 8. Next checkpoint

v13.307 should target a rigorous improvement of the joint prime norm. Natural routes are:

1. analyze B_prime^2 and use the finite overlap graph of translated intervals;
2. derive a block/fiber representation induced by the five incommensurate shifts;
3. construct a certified Galerkin-plus-tail enclosure for the norm;
4. in parallel, sharpen the analytic archimedean remainder constant, now the other large permanent cost.
