# Cone Derivation Ledger v13.494 — chi12 Prime-Phase Bridge Level-1 Schur Propagation

Date: 2026-09-16

Status labels: **[D]** exact algebra, **[N]** numerical diagnostic, **[Audit]** guardrail.

## 0. Synchronization

Live ledger checked immediately before this write. Parallel work had advanced through v13.493, so v13.494 was the next free slot. External Audit Round 37 already resolved the earlier v13.485 collision and retained the chi12 Level-0 gate as the earlier-created v13.485 entry.

## 1. Purpose

Continue the v13.485 source-faithful phase-bridge lane past the tautological local clock identity. For each canonical Suzuki prime-power source channel

\[
q\in\{2,3,4,5,7\},
\]

scale that channel infinitesimally and differentiate the full M=3999 finite Schur complement

\[
S=A_{CC}-A_{CF}A_{FF}^{-1}A_{FC}.
\]

The exact Frechet formula is

\[
\begin{aligned}
dS={}&dA_{CC}-dA_{CF}A_{FF}^{-1}A_{FC}
-A_{CF}A_{FF}^{-1}dA_{FC}\\
&+A_{CF}A_{FF}^{-1}dA_{FF}A_{FF}^{-1}A_{FC}.
\end{aligned}
\]

This is the first non-tautological downstream observable in this lane.

## 2. Frozen four-plane

Use the exact-dyadic 10x6 positive basis Q already frozen in the canonical M3999 replay and construct a numerical orthonormal basis

\[
N=\ker(Q^T).
\]

The replay gave

\[
\boxed{\|Q^TN\|_2=4.58\times10^{-16}}.
\]

For each channel define

\[
\boxed{B_q=N^T(dS_q)N}.
\]

The entries of B_q depend on the orthonormal coordinates chosen inside the four-plane, while its eigenvalues, Frobenius norm, rank profile, and pairwise Frobenius inner products are invariant under a common orthogonal change of N.

## 3. Independent derivative regression [N]

The analytic derivative was compared against a central finite difference of the complete nonlinear Schur map with step h=2^-12. Relative full-Schur Frobenius discrepancies were:

| q | ||dS_q||_F | relative analytic/FD discrepancy |
|---:|---:|---:|
| 2 | 2.1876947705563374 | 8.85e-8 |
| 3 | 2.0607091486550240 | 9.09e-8 |
| 4 | 0.8884698318033449 | 6.72e-9 |
| 5 | 1.8011775134528105 | 9.12e-8 |
| 7 | 1.2059156866013396 | 7.57e-8 |

All five channels pass the preregistered 2e-6 regression threshold by more than an order of magnitude.

The projected B_q analytic/FD discrepancies are also small. For q=2,3,4 they are about 1e-9 relative, for q=5 about 5.1e-8 relative, and for q=7 about 3.8e-5 relative. The larger *relative* q=7 value is caused by the extremely small projected signal itself; its absolute projected discrepancy is only about 5.8e-13.

## 4. Four-plane responses [N]

The invariant Frobenius norms are

\[
\begin{array}{c|c}
q&\|B_q\|_F\\\hline
2&1.069404182085463\\
3&0.9404428008802309\\
4&0.2865821998018114\\
5&0.10561127728338408\\
7&1.51240318876159\times10^{-8}.
\end{array}
\]

The B_q eigenvalues are approximately

\[
\begin{array}{c|rrrr}
2&-0.68235887&-0.48732840&-0.29342488&+0.59533566\\
3&-0.63401440&-0.57034989&+0.00161487&+0.39643006\\
4&-0.271401387&-2.70581\!\times10^{-4}&3.90022\!\times10^{-8}&+0.092035707\\
5&-0.105610050&-1.19772\!\times10^{-7}&2.68209\!\times10^{-12}&+5.09145\!\times10^{-4}\\
7&-1.51240319\!\times10^{-8}&-7.94\!\times10^{-17}&2.11\!\times10^{-17}&9.21\!\times10^{-14}.
\end{array}
\]

Thus the two unramified chi12=-1 channels are both extremely close to rank one on the unresolved four-plane, with q=7 almost annihilated in amplitude there.

## 5. Unexpected directional coherence [N]

Normalize the four-plane matrices by Frobenius norm and use the invariant matrix cosine

\[
C(q,q')=\frac{\langle B_q,B_{q'}\rangle_F}{\|B_q\|_F\|B_{q'}\|_F}.
\]

The unramified pair gives

\[
\boxed{C(5,7)=0.9873520060523864}.
\]

For comparison, the ramified/control cross-cosines with q=5 or 7 are

\[
\begin{aligned}
C(2,5)&=0.331554,&C(2,7)&=0.342850,\\
C(3,5)&=0.269802,&C(3,7)&=0.316167,\\
C(4,5)&=0.568044,&C(4,7)&=0.433807.
\end{aligned}
\]

This is the first genuinely downstream numerical pattern in the phase-bridge lane: the two canonical unramified chi12 channels, which share the same chi12=-1 orientation, produce nearly collinear four-plane Schur derivatives even though their projected amplitudes differ by about seven orders of magnitude.

## 6. Interpretation boundary [Audit]

This is **not yet evidence sufficient to call a Pell/Euler/Suzuki bridge**. The canonical source contains only two unramified channels, both have chi12=-1, and q=7 is extremely small after projection. In particular:

- there is no positive-chi12 unramified control in the present compact source support;
- there is no unramified m>=2 exponent-parity test;
- a normalized direction attached to an almost-annihilated channel requires higher-precision/stability checks;
- no terminal direction was fitted or inspected in obtaining C(5,7).

Therefore the correct status is: **interesting Level-1 propagation signal, requiring a stability/control stage before any bridge promotion.**

## 7. Next target

Before looking at the frozen v13.471 terminal direction, perform a Level-1b stability audit:

1. h-sweep the finite-difference regression for q=5,7;
2. recompute B_5 and B_7 under higher precision / alternate stable linear algebra where practical;
3. verify the near-rank-one axes and C(5,7) are stable under cutoff changes compatible with the existing source pipeline;
4. only then compare those independently frozen axes with the v13.471 terminal tail direction.

This ordering prevents fitting the terminal direction to the observed q=5,7 coherence.

## 8. Guardrail

No exact kernel, critical-line, RH, GRH, or stronger Suzuki inertia theorem follows. Certified Suzuki inertia bounds are unchanged.

Implementation artifact begun in commit `b22afb3534f6e7163ae271b496c7b79531741e21`; this checkpoint records the independently executed structured-solve replay and its numerical output.