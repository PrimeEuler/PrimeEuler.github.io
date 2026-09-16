# Cone Derivation Ledger v13.496 — chi12 Level-1b q=5/q=7 Propagated-Axis Stability Audit

Date: 2026-09-16

Status labels: **[N]** numerical diagnostic, **[Audit]** guardrail/fail-closed interpretation.

## 0. Synchronization

Live ledger checked immediately before this write. Parallel work had advanced through v13.495, so v13.496 was the next free slot.

## 1. Pre-registered question

Continue v13.494 without inspecting or fitting the frozen v13.471 terminal direction. Test whether

\[
C_{5,7}=\frac{\langle B_5,B_7\rangle_F}{\|B_5\|_F\|B_7\|_F}
=0.9873520060523864
\]

persists under the pre-registered Level-1b stability checks: finite-difference step size, cancellation-free derivative evaluation / alternate stable solve, finite cutoff M, and compatible canonical source-support cutoff Q.

Here

\[
B_q=N^T(dS_q)N
\]

uses the same frozen unresolved four-plane N from v13.494.

## 2. M-cutoff stability [N]

Recomputed the analytic Frechet derivative using the same canonical source formula and frozen low-core/four-plane basis while truncating the finite F block at several odd-mode cutoffs:

| M | ||B5||_F | ||B7||_F | C(5,7) |
|---:|---:|---:|---:|
| 499 | 0.10561127228039455 | 1.505443532986095e-8 | 0.9873525528298092 |
| 999 | 0.10561127492930068 | 1.5091301813363863e-8 | 0.9873522297085451 |
| 1999 | 0.10561127648155129 | 1.5112890767623148e-8 | 0.9873520783404802 |
| 3999 | 0.10561127728338410 | 1.5124031893163728e-8 | 0.9873520060547859 |

Thus the v13.494 value is extremely stable under M. The total cosine drift from M=499 to M=3999 is only about 5.47e-7.

## 3. Finite-difference h sweep [N]

Central finite differences of the complete nonlinear Schur map were run for h=2^-8,...,2^-16. The resulting projected pair cosine was:

| exponent e in h=2^-e | C_FD(5,7) |
|---:|---:|
| 8 | 0.9873521921092788 |
| 9 | 0.9873518499996760 |
| 10 | 0.9873513537852898 |
| 11 | 0.9873533461970386 |
| 12 | 0.9873520642097268 |
| 13 | 0.9873505264136884 |
| 14 | 0.9873434397719049 |
| 15 | 0.9873566331866731 |
| 16 | 0.9873923411759224 |

The expected cancellation floor appears at the smallest h because B7 itself is only ~1.5e-8. The stable window h=2^-8 through 2^-13 remains within about 1.5e-6 of the analytic cosine. At the preregistered h=2^-12 it gives 0.9873520642097268.

## 4. Cancellation-free complex-step / alternate solve audit [N]

As a higher-accuracy derivative check, the entire Schur map was evaluated at a complex source perturbation alpha=i h and Im(S(alpha))/h was projected to the four-plane. This avoids the subtraction cancellation of central finite differences. For h from 1e-8 down through 1e-24 the pair cosine remained

\[
0.9873520058\ldots\text{ to }0.98735200605\ldots,
\]

with representative h=1e-20 value

\[
\boxed{0.9873520060231898}.
\]

The complex-step B5 and B7 matrices agree with the analytic Frechet matrices at roughly 1e-16 and 3e-17 absolute Frobenius scale respectively at h=1e-20.

An independent symmetric-matrix solve (`scipy.linalg.solve(...,assume_a='sym')`) at M=3999 gave

\[
\|B_5\|_F=0.10561127728338411,
\quad
\|B_7\|_F=1.512403190129351\times10^{-8},
\]

and

\[
C(5,7)=0.9873520060798747.
\]

The B7 difference from the general dense solve was below 1e-17 in Frobenius norm. A full arbitrary-precision M=3999 factorization was not performed; the relevant numerical-conditioning check here is the cancellation-free complex-step derivative plus independent symmetric solve. Do not describe this checkpoint as an outward or arbitrary-precision certificate.

## 5. Canonical source-support Q cutoff: failure of full stability [N, Audit]

The important negative result appears when the *baseline Suzuki source* is truncated to the canonical support q<=Q while the same q=5 and q=7 infinitesimal derivative probes are evaluated. This is a legitimate nonlinear-background sensitivity test: because the Schur map is nonlinear, dS_q can depend on which other source channels are already present in the baseline operator.

| baseline Q cutoff | ||B5||_F | ||B7||_F | signed C(5,7) |
|---:|---:|---:|---:|
| 3 | 0.11649941135747867 | 9.53487385012754e-3 | -0.3266429552105951 |
| 4 | 0.12039412166735827 | 1.0168202377593468e-2 | -0.48527228576700965 |
| 5 | 0.10559446009166633 | 1.6953238255728356e-7 | -0.9884710872671137 |
| 7 | 0.10561127728338410 | 1.5124031893163728e-8 | +0.9873520060547859 |

Therefore the literal v13.494 signed alignment **does not persist across Q/source-background cutoffs**. In particular, for Q=3 and Q=4 the axes are not close to collinear even up to sign; at Q=5 the normalized matrices become nearly anti-collinear, and only after the q=7 channel is included in the baseline does the sign become positive with the published 0.987352 value.

This is strong evidence that the v13.494 coherence is sensitive to nonlinear source-background interactions rather than being an intrinsic two-channel chi12 orientation law by itself.

## 6. Verdict [Audit]

The pre-registered stability test is **mixed and therefore fails the promotion gate**:

- PASS: M cutoff stability is excellent.
- PASS: finite-difference h sweep has a clear stable window.
- PASS: cancellation-free complex-step differentiation and an alternate symmetric solve reproduce the M3999 value.
- FAIL: the normalized q=5/q=7 relation is not stable under compatible canonical source-support Q cutoffs.

Hence

\[
\boxed{C_{5,7}\approx0.987352\text{ is a robust property of the full canonical }Q=7\text{ baseline, but not a baseline-independent chi12 bridge signal.}}
\]

Per the preregistration in v13.494, this failure means we do **not** proceed to terminal-direction alignment as if Level-1b had passed. The next useful question is instead to explain the Q=5 -> Q=7 sign/amplitude transition analytically by mixed Schur derivatives (especially the interaction of the q=7 perturbation with the q=5-containing baseline), and to determine whether any invariant chi12-sensitive quantity survives after separating those nonlinear cross terms.

## 7. Guardrail

No Pell/Euler/Suzuki bridge is promoted by this checkpoint. No exact kernel, critical-line, RH, GRH, or stronger Suzuki inertia theorem follows. Certified Suzuki inertia bounds are unchanged.
