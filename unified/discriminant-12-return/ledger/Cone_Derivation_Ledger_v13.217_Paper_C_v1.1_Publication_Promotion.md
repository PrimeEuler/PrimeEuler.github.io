# Cone Derivation Ledger v13.217 — Paper C v1.1 Publication Promotion

Date: 2026-09-04

Status labels: [S] source-established, [D] exact derived, [Audit] correction/reconciliation, [Pub] publication/pipeline status.

## Scope

This checkpoint closes the Paper-C audit/promotion cycle begun in v13.215 and implemented in v13.216. It records the successful CI build and the resulting change in authoritative foundation status.

## 1. [S] Corrected source

The corrected Paper-C source is `foundations/PaperC_QuantumRealizations_v1.1.tex`. It supersedes `foundations/PaperC_QuantumRealizations.tex` as the live theorem source. The old TeX/PDF pair remains historical provenance rather than a competing authoritative copy.

## 2. [Audit] Mathematical corrections carried into v1.1

For `d=n1-n2`, the two-mode `SU(1,1)` Casimir is `C=(d^2-1)/4=k(k-1)` with the standard positive-discrete-series label `k=(|d|+1)/2`. Thus `k=X` only in the oriented `d>=0` sector. The signed operator `X=(D+1)/2`, with `D=n1-n2`, remains exactly conserved, but a superposition of different `d` sectors does not have one Bargmann index.

The `SU(2)` publication proof now uses exact total-number conservation `[N,J_i]=0`, with `T=(N+1)/2`, rather than inferring arbitrary-state `T` conservation from a Casimir expectation.

The squeezing comparison is corrected to

`T_q(r)-T_cl(2r)=Y_0 sinh(2r)(sqrt(1-1/x_0)-1)`.

The asymptotic discussion distinguishes the bracket factor, absolute residual, and relative error under joint scaling.

The `B_X` section no longer presents a universal Gaussian no-go theorem without a general symplectic proof. It records a scoped structural obstruction; non-Gaussian realizations remain open.

The quantum mixed generator is notated separately from Paper B's normalized classical generator. Its Heisenberg matrix satisfies the exact identity `A^2=-ab I_4`. For `ab>0`, with `T_cl=pi/sqrt(ab)`, this gives `exp(T_cl A)=-I_4` and `exp(2 T_cl A)=I_4`, hence `U(T_cl)=e^{i alpha}(-1)^N` and `U(2T_cl)=e^{2i alpha}I`. The publication statement is therefore: parity eigenstates revive up to phase at one classical period; arbitrary states are guaranteed to revive up to phase by two classical periods. No universal minimal-period claim is made.

The Paper-C state dictionary `x=n1+1`, `y=n2` is retained with the null-diamond guardrail that this state point is a transition vertex, not the four-corner cell center.

The opening framing is synchronized with Paper B v2.1: intrinsic projective powers are distinguished from chosen-equation level-raising lifts, and the parabolic boundary is not described as carrying the same diagonal eigen-coordinate construction.

## 3. [Pub] Build and CI pipeline

Canonical build entry point: `foundations/build_paper_c.sh`.

Canonical workflow: `.github/workflows/build-paper-c.yml`.

Canonical source/output pair:

- `PaperC_QuantumRealizations_v1.1.tex`
- `PaperC_QuantumRealizations_v1.1.pdf`

The workflow successfully compiled and committed the PDF in GitHub Actions commit `edf120b01daf520c86d00adbc6a7fe179a536767`, message `Build Paper C v1.1 PDF`. This is direct evidence that the publication source compiles in the repository CI environment.

## 4. [Audit] README handoff contract reconciled

The project README now states explicitly that Paper C v1.1 is the current audited source and records the active mapping `build-paper-c.yml -> foundations/build_paper_c.sh -> PaperC_QuantumRealizations_v1.1.tex`. It also records the principal v1.1 guardrails so future sessions do not regress to the old Bargmann-index, power-map, `B_X`, or revival formulations.

README promotion commit: `b6fc931633d2c8f859056787be2eb514667e21d8`.

## 5. [Audit] Foundations inventory reconciled

`foundations/FOUNDATIONS_INVENTORY.md` now classifies `PaperC_QuantumRealizations_v1.1.tex/.pdf` as **ACTIVE / AUDITED BASELINE**, and the former unversioned Paper-C source/PDF as historical.

The dependency chain is now explicitly:

1. Paper A v2.4 — audited geometric/conic foundation;
2. Area note v1.1 — one-sided measure companion;
3. Paper B v2.1 — audited continuous Lorentz/projective foundation;
4. Paper C v1.1 — audited quantum-realization foundation;
5. Casimir / Null-Diamond v2.1 — audited discrete/oscillator bridge.

Inventory promotion commit: `7964c3013190bec8cdf61a78406c37806c7c473c`.

## 6. [Audit] Workflow-email distinction

During verification, the repository's GitHub Pages deployment workflow was observed failing on an earlier human-authored commit. That Pages workflow is separate from the Paper-C publication build. The Paper-C publication build itself demonstrably succeeded because it produced and committed `PaperC_QuantumRealizations_v1.1.pdf` in commit `edf120b...`.

Do not conflate generic Pages deployment failures with dedicated paper-build workflows when diagnosing future notification emails.

## 7. [Pub] Foundation status after this checkpoint

Paper C v1.1 is promoted to **ACTIVE / AUDITED BASELINE**.

The A/B/C foundation sequence and the null-diamond bridge are now all on audited, versioned project-local baselines. The next mathematically useful operation is a downstream dependency audit of `papers/Discriminant_12_Return_v0.3.3.tex` against these current foundations before deciding whether a new principal-paper version is warranted.

## Final classification

- [D] Paper-C operator algebra retained with the v13.215 corrections.
- [Audit] stale universal/canonical power-map and global Bargmann-index language removed.
- [Audit] `B_X` claim scoped to the proof actually supplied.
- [D] revival strengthened by `A^2=-ab I_4` and weakened only where minimal-period language was unjustified.
- [Pub] v1.1 compiled successfully in CI and produced a committed PDF.
- [Pub] README and foundations inventory now point to v1.1 as authoritative.

**Paper C audit/promotion cycle: CLOSED.**
