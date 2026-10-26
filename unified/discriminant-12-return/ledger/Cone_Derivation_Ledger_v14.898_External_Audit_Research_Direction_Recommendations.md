# Cone Derivation Ledger v14.898 — External Audit: research-direction recommendations for the gravity lane

**Date:** 2026-10-26
**Track:** External Audit (auditor opinion, requested by project owner — not a verification round, not a mathematical claim)

This entry is different in kind from every other External Audit entry to date. Rounds 341–355 (and the liveness notes between them) verify specific mathematical/numerical claims already deposited by Lane A, Sandbox, and the gravity lane. **This entry contains no such verification.** It is this auditor's own assessment of the gravity lane's research *direction*, written at the explicit request of the project owner, to be read by the gravity lane before its next round of work. Nothing below should be read as [D], [V], or [N] — treat every claim in this entry as **[OPINION]**.

## Summary assessment

Across roughly thirty gravity-lane entries audited in Rounds 349–355 (v14.831 through v14.896), this auditor found the *mathematics* to be consistently correct: every nontrivial identity, integral, commutator, and numerical root-find that was independently re-derived or re-computed matched the deposit's claims, including several results (the retarded Maxwell kernel's closed form, the finite-Larmor pole sweep, the support-sensitivity analysis) that required genuine independent analytical or numerical work to check, not mere inspection. The lane's epistemic discipline is also unusually good: claims are consistently tagged [D]/[I]/[O], new physical couplings are explicitly flagged as postulated rather than derived, and negative results (seat softening instead of stiffening, dilation covariance instead of a selected scale, "Higgs identification NOT derived") are reported plainly rather than buried.

The reservation is about direction, not correctness, and is offered in that spirit.

## Recommendation 1 — name the free-parameter bottleneck explicitly

Every physical model introduced so far carries at least one free parameter with no mechanism, inside the Cone/bicone/SU(2) structure itself, that fixes it: the exchange coupling `λ` (v14.862), the charge-geometry coupling `g=2qR/u` (v14.871 onward), the drive frequency `Ω` and regulator width `a`, and now the external support stiffness `κ_s` and bare inertia `μ_s` (v14.896, itself explicitly flagged as "NOT supplied by SU(2), Coulomb, or the reflected-circle source model"). A model with an unfixed free parameter can always be tuned to match any single target value; that by itself is not evidence of a physical connection. Before adding further kernel complexity (more harmonics, finite-rotation supports, additional couplings), the lane would gain more by asking directly: **is there any argument — a symmetry, a locality constraint, a uniqueness theorem — that *forces* a specific value for one of these parameters, rather than merely *permitting* a range of them?** If the honest answer is "no, this structure genuinely underdetermines the coupling," that negative result is itself worth a ledger entry, and would be more valuable than another free-parameter extension of the existing kernel.

## Recommendation 2 — apply a "second independent prediction" test

The signature that distinguishes physics from numerology is that fixing a model's free parameters against *one* known quantity lets it correctly predict a *second*, independent one that was not used in the fit. Nothing in the thirty-entry sequence audited so far has been checked against this bar — every gate stops at "under this choice of parameters, the sign/magnitude is consistent with such-and-such," never "I fixed this against known quantity X, and it now correctly predicts independent known quantity Y." This auditor recommends the lane adopt this explicitly as the closing criterion for any future claim that a specific coupling or scale has been *selected* (as opposed to merely shown compatible). Absent that, the honest label for the program's output remains "an internally consistent family of toy models," not "evidence for a coupling."

## Recommendation 3 — reconnect to the arithmetic side of the project

This project is named for a discriminant-12 arithmetic structure, and the strongest content this auditor has verified across all rounds sits on the number-theoretic side: the divisor-weighted Casimir sums (`w(a,b)=ab-(a+b)/2`), the Schwinger relabeling of divisor contacts, and especially Sandbox's Suzuki/Weil far-residual work (still open as of v14.882's handoff — see below). The gravity lane's recent entries (rotating dipoles, retarded Maxwell kernels, Bessel harmonic sweeps, mechanical support sensitivity) are correctly executed, but they are standard classical electrodynamics in bicone notation; nothing in them uses the arithmetic structure itself. A direction this auditor would find more promising: investigate whether the divisor-weight function or the so(4) Casimir structure admits a genuine *spectral* interpretation connecting to the Suzuki/Weil explicit-formula zeros — in the spirit of a Hilbert–Pólya-type correspondence — rather than treating the bicone purely as a classical mechanical system to which electromagnetism is separately attached.

## Recommendation 4 — seek one real empirical anchor

Across everything audited so far, no entry has been checked against an actual measured physical quantity — not an electron mass, not a known spectral line or resonance, not Newton's `G` itself, not even approximately. Even a single rough, order-of-magnitude point of contact with something measured would do more for establishing this program's physical content than another exact closed-form kernel computed for a model with unfixed parameters.

## Note on the still-open Suzuki handoff

Separately from the above: v14.882 (Lane A) handed Sandbox a concrete, scoped task — read the exact rational `W_0` for the far-seed diagonal coefficient, bound the remainder, and derive a three-band offdiagonal/pole asymptotic. As of this entry that handoff remains open; Sandbox's most recent return (v14.884) answered a different, earlier handoff (the finite-Larmor Maxwell pole, from v14.880/881) instead. This auditor flags no error here — both handoffs are legitimately open and it is Sandbox's call which to prioritize — but notes it for completeness since the project owner has separately indicated the Suzuki lane is intended to be active again.

---

**No flags, no verification record.** This entry makes no mathematical claim and should not be cited as a parent for any [D]/[V]/[N] result. It is advisory only, offered at the project owner's request to inform the gravity lane's next steps.
