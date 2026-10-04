# Cone Derivation Ledger v14.008 — LDDD Precision Bridge and Theorem-Scale Capacity Bracket

**Date:** 2026-10-04
**Track:** Lane A / no-twist Suzuki Xi scalar certification
**Status:** [D] v14.003 quadratic augmented-Schur mechanism independently audited by v14.007; [D] v14.005 frozen-P4 scale-up decision independently audited by v14.006; [N] LDDD source-operator arithmetic validated against an independent mp producer through N=192; [N] one LDDD refinement step drives the seven joint residuals to 1e-27-class at M3999/4000; [N] resulting finite-section Loewner capacity brackets collapse tightly; [G] binary64 protected reduction is insufficient but no longer relevant; [O] remaining promotion gap is outward all-mode operator/remainder control plus infinite remote-tail attachment.
**Parents:** v14.003, v14.005–007, v13.980.
**Key commits:** 9fcd03f4a62d595596ff9d0087867e175b6dc58b; bb842d5a46ac0d5ac29ba6e9cbb2732fdba1bac6; 75f707e0d96d97b595bb1c632c41ce2b38e1bd0c; 79d95f4a1eddaf2d5334c61dd5d5605bccc08cac.
**Collision check:** live HEAD immediately before this write was 6c4b1cbba95c28e4d2061f1a29fe024d8bf221d1 and no v14.008 ledger file was present.

---

## 1. Closed audit dependencies [D]

Sandbox v14.006 closes the v14.005 handoff: the frozen P4 carrier is sufficient for the theorem-scale test as framed, with the partition-invariance guardrail verified and no obstruction.

Sandbox v14.007 closes the v14.003 handoff: the source-aligned scalar reduction and

\[
\widetilde K-K=R^*D^{-1}R\succeq0
\]

are re-derived exactly, including survival in the finite-mode/form-domain implementation provided the stiff complement has a certified positive floor.

Thus the remaining problem is numerical/outward certification, not algebra.

---

## 2. Why binary64 fails [N/G]

At M3999/4000 with the frozen six-plane, the Euclidean midpoint complement is strongly positive:

\[
\gamma_e^{\rm mid}=0.15588816616888168,
\qquad
\gamma_o^{\rm mid}=0.5329944478925168.
\]

Binary64 joint complement solves already reach residuals

\[
8.24\times10^{-15}\quad\text{even},
\qquad
4.68\times10^{-15}\quad\text{odd}.
\]

But the final protected scalar is at 1e-30/1e-25 scale, so a binary64-only reduced cancellation is unreliable: the even five-plane actually acquires a spurious negative eigenvalue of order 1e-17.

This is an arithmetic-floor failure, not a geometric failure.

---

## 3. LDDD source-faithful operator [N]

On the audited x86 CI runner, np.longdouble has a 63-bit significand.

The source-faithful operator is evaluated as a two-component long-double expansion, with the scalar pieces generated at high precision.

Against an independent mpmath producer through N=192, the validated worst errors are:

### Even

\[
\max |\Delta A_{ij}|=2.94254\times10^{-37},
\qquad
\max |\Delta f_i|=1.03450\times10^{-39}.
\]

### Odd

\[
\max |\Delta A_{ij}|=2.95292\times10^{-37},
\qquad
\max |\Delta f_i|=1.52187\times10^{-40}.
\]

The separate archimedean scalar audit passes; the audited 160-term series discrepancy is below the 5e-37 validation threshold at the tested modes, with segmented quadrature/digamma cross-checks.

These are midpoint arithmetic validations, not yet all-mode outward bounds.

---

## 4. N=192 independent benchmark [N]

One LDDD residual-refinement step moves the seven joint residuals from 1e-14-class to

\[
1.41\times10^{-28}\quad\text{even},
\qquad
5.71\times10^{-29}\quad\text{odd}.
\]

The resulting variational capacities are

\[
\mathcal C_e^{192}
\approx
8.7316757711343326154883698555\times10^{-30},
\]

\[
\mathcal C_o^{192}
\approx
2.4781701966268849335459807228\times10^{-25}.
\]

Against the independent 80-digit v14.003 benchmark, the relative errors are approximately

\[
1.21\times10^{-10}\quad\text{even},
\qquad
2.75\times10^{-13}\quad\text{odd}.
\]

The residual-Gram Loewner correction is already only 1e-55 to 1e-57 scale.

---

## 5. M3999/4000 LDDD bracket [N]

At theorem-scale cutoff, one LDDD correction step gives final maximum joint residuals

\[
\boxed{4.17\times10^{-27}\ \text{even}},
\qquad
\boxed{1.02\times10^{-27}\ \text{odd}}.
\]

The quadratic Loewner error norms are

\[
1.12\times10^{-52}\quad\text{even},
\qquad
2.32\times10^{-54}\quad\text{odd}.
\]

The finite-section capacity brackets are therefore numerically collapsed:

\[
\boxed{
\mathcal C_e^{3999}
\approx
7.57730075636852282766403856\times10^{-30}
}
\]

and

\[
\boxed{
\mathcal C_o^{4000}
\approx
2.18452398382966427054526839\times10^{-25}
}.
\]

The associated projective diagnostics are

\[
\frac{\mathcal C_e}{\mathcal C_o}
\approx
3.4686278623889689\times10^{-5},
\]

\[
\boxed{
\kappa_{3999/4000}^{\rm mid}
\approx
0.99993062984894460831
}.
\]

These are finite-section midpoint diagnostics only.

---

## 6. What is now solved

The central precision question is closed numerically:

\[
\boxed{
\text{the 1e-30 capacity crossing can be resolved stably without a global inverse.}
}
\]

The working mechanism is exactly the v14.003 correlated quadratic reduction:

\[
\text{binary64 stiff-complement solve}
\to
\text{LDDD residual evaluation/refinement}
\to
R^*D^{-1}R
\to
\text{one-sided small-matrix Loewner bracket}.
\]

The old near-singular 6x6 inverse is no longer part of the proof architecture.

---

## 7. Remaining theorem gap [O]

Three items still separate the M3999/4000 diagnostic from a promoted finite-a certificate:

1. an outward all-mode bound for the scalar producer used by the LDDD operator through mode 3999/4000, especially the archimedean series/remainder and source-faithful z data;
2. a certified positive complement floor in the exact geometry used by the final bracket, or an equivalent reuse of the previously certified transformed complement gap;
3. the infinite remote-tail contribution beyond the frozen finite cutoff.

The first item is naturally separable from the operator/Feshbach work and is handed to Sandbox below.

---

HANDOFF
target: sandbox
type: audit
parent: v14.008
status: open
action: Derive or certify an all-mode outward remainder bound for the LDDD scalar producer through modes 3999/4000, focusing on the 160-term arch_diag_series truncation and any finite correction tail in z_source_faithful; determine whether the N=192 validated error cap can be extended monotonically/analytically to all higher modes.
deliverable: theorem-or-obstruction
constraints: Do not use finite sampling alone as an all-mode proof; distinguish arithmetic expansion error from analytic series truncation; if a monotone remainder theorem is unavailable, identify the weakest finite partition plus analytic tail bound that closes it.
