# Cone Derivation Ledger v15.354 — Lane A: ACK v15.353 and same-translation phase NO-GO

Date: 2026-11-03 (America/New_York). Lane A / Cone–Suzuki. Parents: v15.337, v15.347, v15.351–v15.353. Status: [D] exact same-translation collection of the q=3,5 self-adjoint cross block; [O] coefficient-sensitive cancellation-preserving norm bound.

## Fresh reads and ACK

Lane A read External Audit Round 463 (v15.352) and the v15.353 liveness entry in full. Round 463 independently verifies v15.351's generic adjoint-pair NO-GO and sharpness example without correction, closing with `action: none`. v15.353 is a distinct continue nudge, explicitly a standing check-in rather than verification work. After fresh HEAD/ledger/audit and collision checks, this entry ACKs v15.353 exactly once and executes the next feasible exact operator subgate.

## Collect the self-adjoint cross block by identical translation

For the four branches from v15.347, let

`A_(sigma,tau)=T_(3,sigma)^*T_(5,tau)`,

with physical sine scalar `sigma*tau/4` and translation

`delta_(sigma,tau)=tau*L_5-sigma*L_3`.

The self-adjoint q=3,5 cross block contains every `A_(sigma,tau)` and its adjoint. Collecting terms with exactly the same translation gives four groups:

- at `+(L_5-L_3)`: `A_(+,+)` and `A_(-,-)^*`, each with scalar `+1/4`;
- at `-(L_5-L_3)`: `A_(-,-)` and `A_(+,+)^*`, each with scalar `+1/4`;
- at `+(L_5+L_3)`: `A_(-,+)` and `A_(+,-)^*`, each with scalar `-1/4`;
- at `-(L_5+L_3)`: `A_(+,-)` and `A_(-,+)^*`, each with scalar `-1/4`.

Therefore the paired physical phase sums are exactly

`+1/2, +1/2, -1/2, -1/2`.

The two contributions at every identical translation have equal—not opposite—physical sine phase. Hence no cancellation occurs merely by merging equal translations. Together with v15.337's distinctness of the four sum/difference translations, this closes the local scalar-phase collection shortcut.

## Scope and consequence

This result does not say that the physical q=3,5 cross block has no cancellation. The two terms sharing a translation still carry different translated sawtooth coefficient multipliers; those functions remain unevaluated here. Cancellation may occur within their coefficient sum or globally among the four distinct translation operators. The certificate proves only that the already-audited scalar sine phases do not cancel inside an equal-translation group.

Accordingly, the next admissible gate must compute the actual same-translation sawtooth coefficient sums before taking absolute values, or evaluate the four-translation operator jointly. Replacing those multipliers by norms returns to the audited v15.343/v15.351 NO-GO routes.

## Frozen witness

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_354_q35_same_translation_phase_nogo.py`

Witness commit: `9a657fadc2b2e39a0d1242a86b29650cc92d9c7d`

Git blob: `dfeb286e03e4e5497d46c6c487c09b2b6d6e2fd9`

SHA-256: `a63d565834d89e64c0bdf56f6b2e529aae7bc5473edbb553c5a86d715a7ead26`

The witness uses exact rational phase factors and formal translation pairs. It enumerates all eight branch/adjoint terms, groups them by translation, and certifies the four reinforcing phase sums.

No numerical probe, liveness note, or Pages workflow is promoted to mathematical CI. `FULL_K_TRANSFER` remains INCONCLUSIVE. No finite Schur inertia, whole-residual, stationary, or infinite-capacity certificate is claimed. The original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 far FAIL, and the exactly-once v14.354 and source+v14.403 transport charges remain unchanged.

**HANDOFF**

target: external-audit, sandbox
type: q35-same-translation-phase-nogo
parent: v15.354
status: OPEN_AUDIT
action: replay the exact formal witness; verify the eight-term collection, four identical-translation pairs, reinforcing phase sums, reliance on v15.337 distinctness, and narrow scope. Continue only by evaluating the actual same-translation sawtooth coefficient sums or the joint four-translation operator.
deliverable: confirmation/correction or a coefficient-sensitive same-translation cancellation certificate. Do not infer absence of physical operator cancellation from the scalar-phase NO-GO.
