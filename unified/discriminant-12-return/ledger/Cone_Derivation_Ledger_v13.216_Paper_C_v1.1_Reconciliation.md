# Cone Derivation Ledger v13.216 — Paper C v1.1 Reconciliation

Date: 2026-09-04

Status labels: [S] source-established, [D] exact derived, [Audit] correction/reconciliation, [O] open.

## Scope

This checkpoint promotes the mathematical corrections from v13.215 into a new source:

`foundations/PaperC_QuantumRealizations_v1.1.tex`

The historical predecessor `PaperC_QuantumRealizations.tex` is retained for provenance but is no longer the intended build target.

## [Audit] Paper-B dependency corrected

Paper C v1.1 no longer assumes that every cone generator carries one canonical orbit-enlarging power map. It imports the audited Paper-B v2.1 hierarchy:

1. intrinsic powers of normalized nonparabolic orbit coordinates;
2. exact chosen-equation-dependent level-raising powers in unnormalized eigen-coordinates;
3. failure of the diagonal eigen-coordinate construction at the parabolic boundary, without denying coordinatewise factor powers.

## [D] SU(2) statement strengthened

With `N=n1+n2`, every Schwinger `su(2)` generator commutes with `N`. Therefore

`T=(N+1)/2`

is conserved as an operator, including its full spectral distribution. This is stronger and cleaner than inferring only an expectation-value statement from Casimir centrality.

## [Audit] SU(1,1) sector label corrected

For `D=n1-n2`,

`C=(D^2-1)/4`

and fixed-`d` sectors carry positive-discrete-series index

`k=(|d|+1)/2`.

Only for the oriented sector `d>=0` is `k=X=(d+1)/2`. A superposition across different `d` sectors has no single Bargmann index, although the signed operator `X=(D+1)/2` is exactly conserved.

## [D] residual parameter corrected

The exact coherent-state comparison is

`T_q(r)-T_cl(2r) = Y0 sinh(2r)(sqrt(1-1/x0)-1)`.

The previous argument-label mismatch `T_q(2r)-T_cl(2r)` is removed. The asymptotic discussion now distinguishes the bracket factor, absolute residual, and relative error under joint scaling.

## [Audit] B_X theorem strength reduced

The manuscript now records a scoped obstruction for the natural passive and standard active Gaussian families. It does not claim a universal Gaussian no-go theorem without a general symplectic/Bogoliubov normal-form proof. Non-Gaussian realizations remain open.

## [D] generic elliptic revival strengthened

The quantum generator is renamed

`Gq_{a,b}` / `\mathcal G^{(q)}_{a,b}`

to avoid collision with Paper B's normalized classical `\widehat G_{a,b}`.

For the Heisenberg matrix,

`A^2=-ab I4`.

Thus for `ab>0` and `T_cl=pi/sqrt(ab)`,

`exp(T_cl A)=-I4`,

`exp(2 T_cl A)=I4`.

On Fock space,

`U(T_cl)=e^{i alpha}(-1)^N`,

`U(2T_cl)=e^{2i alpha}I`.

Correct revival language is therefore:

- parity eigenstates revive up to phase at one classical period;
- arbitrary states are guaranteed to revive up to phase at two classical periods;
- no minimal-period claim is made for every individual state.

## [Audit] transition-cell guardrail

The dictionary `x=n1+1, y=n2` is retained, but the corresponding state point is explicitly identified as a transition vertex rather than the center of the four-corner null-diamond cell.

## Publication pipeline

Added:

- `foundations/build_paper_c.sh`
- `.github/workflows/build-paper-c.yml`

The workflow targets `PaperC_QuantumRealizations_v1.1.tex` and commits `PaperC_QuantumRealizations_v1.1.pdf` after a successful build.

## Classification

Paper C v1.1 is the corrected theorem source produced from the v13.215 audit. Its mathematical promotion is complete at source level. Publication-authoritative status additionally requires a successful CI compile of the new PDF. The old `PaperC_QuantumRealizations.tex/.pdf` remain historical provenance artifacts.
