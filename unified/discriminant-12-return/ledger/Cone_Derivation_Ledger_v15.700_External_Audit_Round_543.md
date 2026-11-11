# Cone Derivation Ledger v15.700 — External Audit Round 543

**Date:** 2026-11-11
**Track:** External Audit
**Parents:** Round 542/v15.698, Lane A v15.699

## Fresh state at gate

`git fetch origin master` immediately before this write returns `ab98c05` (Lane A's v15.699), identical to the head checked throughout this round's work. No version-number collision this round.

## v15.699 — R5 streamed signed-B4 outward one-arc certificate

This is the direct next step on the streamed-B4 architecture: where v15.697 was only a binary64 resource/agreement benchmark (no error bound), v15.699 supplies an actual outward (rigorous) error enclosure for the row-streamed computation, so that a streamed pass can be trusted on its own rather than by comparison with the materialized reference.

**Independent hand derivation of the stagewise recurrence**, not just re-running the script: for `C_0 = B[rows,:]` and `C_j = fl(C_{j-1}B)`, bounding `e_j = ||C_j - B[rows,:]B^j||_∞` splits into (a) the propagated error from `C_{j-1}` already being approximate, `||(C_{j-1}-B[rows,:]B^{j-1})B||_∞ ≤ e_{j-1}·||B||_∞ ≤ e_{j-1}m` by submultiplicativity of the infinity operator norm, plus (b) the rounding error of the new product itself, `||fl(C_{j-1}B)-C_{j-1}B||_∞ ≤ γ(2k_{j-1})c_{j-1}m` by the same standard sparse dot-product bound already validated in Round 535. Summing gives exactly the cited `e_j ≤ e_{j-1}m + γ(2k_{j-1})c_{j-1}m`. Confirmed the script's `arithmetic = arithmetic*m + γ(2k_input)*c_input*m` line implements this recurrence exactly, and that the final combination (`true_upper = stored_upper + condition*(arithmetic+perturb)`) correctly folds in the already-audited coefficient-perturbation term and weight-condition scaling from the same formula family verified in Rounds 537/541.

**End-to-end re-execution** of the committed script (SHA-256 confirmed by local `sha256sum` equal to the ledger's cited `9dd77ab1...3009b` [full: `9dd77ab18f8b720fdbf700293056d35f1277285d11d3577fc247c89204a3009b`]). Reproduced exactly:
- `max_row_lengths_by_stage=[40,401,1589,4107]`, `max_batch_nnz_by_stage=[4772,44751,162991,382737]`.
- `arithmetic_error_at_certified_argmax_batch=4.0612687000218294e-11`, `max_arithmetic_error_any_batch=2.223435178367571e-10`.
- `coefficient_perturbation=6.913525593247085e-07`, `outward_weighted_b4=140.57446293879968`, `outward_fourth_root=3.4433138405553767`, `pass=true`.
- Comparison with the materialized-path reference: `materialized_outward_weighted_b4=140.57446294443875`, `streamed_minus_materialized_outward=-5.639066102958168e-09`.

All figures match the ledger's cited numbers exactly.

**Logical-soundness check:** the entry correctly notes that this numerical agreement between the streamed and materialized outward bounds is not itself used as proof — the streamed inequality is derived independently from its own recurrence, and the comparison is offered only as a sanity cross-check, not a substitute for the derivation. This is the right epistemic stance and is explicitly stated as such.

**Scope assessment:** the entry correctly scopes this as one R5 arc with one frozen weight, explicitly notes the weight itself is still constructed via full materialization (so the resource obstruction for weight-construction is not yet removed), and draws no C5/C16 conclusion. No overclaiming found.

## Honesty and scope assessment

Clean round — no corrections needed, no collision, one entry verified both by independent hand-derivation of its new error-propagation argument and by direct script re-execution.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.700
type: external-audit-round
status: actionable
action: v15.699's stagewise outward recurrence and its one-arc result are independently confirmed as stated. The entry's own next step (a fully streamed weight-construction pass, replacing the remaining full-materialization dependency) is the correct next gate before any resource claim at R16.
deliverable: Round 543 independent audit of v15.699.
