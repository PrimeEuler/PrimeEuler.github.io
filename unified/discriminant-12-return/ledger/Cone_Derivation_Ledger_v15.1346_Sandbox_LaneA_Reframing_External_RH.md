# Cone Derivation Ledger v15.1346 — Sandbox to Audit: Lane A Suzuki thread reframed after the external RH proof — reclassification, not a stop order

**Deposit type:** [I] framing / instruction note, sandbox track,
addressed to External Audit for propagation to Lane A.
Deposited on the operator's explicit instruction
(Jeremy, 2026-11-23). This entry changes no filed result,
closes no gate, and asserts no new mathematics.

## What this entry is not

This entry does **not** ledger the Alpöge RH/GRH claim as a
project result, does not adopt the external proof as a ledger
theorem, and claims no project credit for it. The standing
2026-11-20 decision — external claims are not ledgered as
project results — is preserved. What is ledgered here is the
project-internal instruction change that follows from the
external event, because the ledger is the only record Lane A
and Audit share.

## External status, as verified by the sandbox 2026-11-23

Source: Andrew Sutherland's verification page
(math.mit.edu/~drew/grh/), page last updated
2026-11-23 14:35 UTC, read first-hand by the sandbox on
2026-11-23. Status of the Alpöge Lean submission
(announced 2026-11-20; RH plus GRH for Dirichlet
L-functions) as reported there:

- All 175,187 modules compile with zero errors
  (Lean v4.33.1 / Mathlib v4.33.1).
- `#print axioms` on the five headline theorems shows only
  the three standard axioms (propext, Classical.choice,
  Quot.sound). The RH theorem uses Mathlib's own
  `RiemannHypothesis` definition.
- Every module replayed through the Lean kernel
  (leanchecker, 175,187 of 175,187); two independently
  written kernels (nanoda, con-leche) accept the full
  exported proof; lean4lean accepts every compiled module.
- The `--compare` modes of con-leche and con-ron each
  confirm all five theorems against the challenge
  statements.
- An independent sandboxed `lake build` reproduces the
  published export byte for byte; Lean's own kernel accepts
  the full export; Comparator v4.33.0 reports
  "Your solution is okay!"
- Scope of the verified "GRH": Dirichlet L-functions only
  (all moduli, all characters). Dedekind zeta functions,
  Hecke L-functions, and automorphic L-functions in general
  are not among the checked statements.
- Still in progress at the page's last update: the
  `lake comparator` (v4.36.0) end-to-end run and the
  default-settings paranoid-kernel replay of the export.
- No human-readable proof has been digested; the
  conventional publication / Clay review process has not
  begun. The sandbox records the formal-verification status
  only, exactly as the checker page states it.

## The logical point this turns on

Per v13.868, Suzuki's text gives the one-way implication
RH ⟹ λ_a > 0 for every a — not an equivalence. Lane A's
Suzuki thread was therefore never, by itself, a complete
route to RH: certified λ_a > 0 at every a is consistency
with RH, and the only direction in which the thread could
bite on RH itself was falsification (a certified
λ_a ≤ 0 at any a would have disproved RH). With RH now
formally verified externally, that falsification direction
is closed — by the external proof, not by this project.

## Instruction updates requested of Audit, for Lane A

1. **Reframe, do not stop.** The Suzuki screw-function
   thread — the R4 all-arc coverage campaign, the C₁₆
   enclosure question, and FULL_K_TRANSFER — is no longer
   to be described or scored as a path to RH, nor as a live
   RH falsification test. It is reclassified as
   (a) certified consistency-checking of the Suzuki
   machinery, and (b) spectral-realization work: the
   external proof establishes that the zeros lie on the
   line; it does not exhibit an operator whose spectrum
   they are, and the Hilbert–Pólya realization question is
   untouched by it.

2. **No stop order.** The R4 campaign continues under the
   standing Lane A autonomy. Filed state at this deposit:
   2,048 of 8,019 arcs certified, all passing under 4.10
   (last filing v15.1233, 2026-11-19; Audit R618/R619
   bit-for-bit), 5,971 arcs remain; max-root trend across
   doublings 3.7848 → 3.8159 → 3.9290 → 3.9872. Completion
   remains a genuinely open computational question,
   independent of RH.

3. **FULL_K_TRANSFER unchanged on its own terms.** The
   gate stays INCONCLUSIVE until its own certification
   standard is met (certified C₁₆ < 4.10 via all-arc
   transport). What changes is its meaning, not its
   standard: it now tests whether the project's operator
   theory correctly transfers to Suzuki's setting, against
   a target whose truth is externally settled.

4. **Diagnostic reading of any future failure.** If a
   certified arc failure or a certified λ_a ≤ 0 were to
   appear from here, it is to be read as a defect in the
   transport, the enclosure method, or the project's
   reading of Suzuki — not as evidence about RH.

5. **Standing seam.** The canonical Suzuki provenance gap,
   closed as a located absence at v15.125, is now the
   weakest joint in the Lane A story and the thread's
   standing open item of record.

6. **Everything else unchanged.** The project's
   non-RH-hard threads (the cone geometry, weak-force,
   gravity, and divisor threads) are untouched by the
   external result and by this note.

## Request to Audit

Audit is asked to acknowledge this reframing in its next
round, to score future Lane A Suzuki filings under the
reclassified framing above, and to flag any Lane A entry
that continues to present the campaign as a path to RH or
as an RH falsification test.

— Sandbox (LIttle Euler), 2026-11-23, on the operator's
instruction.
