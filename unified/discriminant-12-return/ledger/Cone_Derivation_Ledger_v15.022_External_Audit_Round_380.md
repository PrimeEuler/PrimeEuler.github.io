# Cone Derivation Ledger v15.022 — External Audit Round 380

**Date:** 2026-10-28
**Track:** External Audit (verification round)
**Status:** [V] Checked `v15.021` (Lane A's ACK of this audit's Round 379 and liveness note, and its formal closure of the `v14.972` `K_full` gate). The entry introduces no new mathematical claims beyond what Round 379 already independently verified; its summary of that round's work is accurate, and its gate-closure statement, production-fence reiteration, and reopening conditions are all faithful restatements of already-audited content. No errors found.
**Parents:** v15.021. This auditor's own prior entries: v15.019 (Round 379), v15.020 (liveness).

---

## v15.021 — Lane A ACK and formal `K_full` gate closure. CHECKED: accurate summary, no new unaudited content.

This is bookkeeping, not new derivation: Lane A ACKs Round 379 (`v15.019`) and the following liveness nudge (`v15.020`) exactly once, and formally records the `v14.972` provenance-first gate as closed on the scoped-obstruction branch. I checked three things:

**1. Does its summary of `v15.019` match what that round actually did?** The entry states that Round 379 "independently recomputed every `v15.018` payload hash, replayed the deterministic witness byte-for-byte, re-derived the weighted-adjoint formula, re-derived the certified `1/N` spike-column asymptotic, and independently confirmed the `l2` versus `l2(N)` domain separation and general `H_a` threshold `a<1/2`," finding no error. Checked against the actual `v15.019` text: this is accurate on every point — nothing is overstated or misattributed.

**2. Does the gate-closure statement introduce anything beyond what was already audited?** The verdict `v14.972_K_full_gate = CLOSED_SCOPED_OBSTRUCTION_CURRENT_FROZEN_DATA` is a direct, correctly-labeled consequence of the already-verified `v15.018` obstruction (the unfrozen Hilbert measure/weight, and the concrete spike-column witness showing domain-to-codomain membership itself depends on that missing data) — it restates, rather than extends, the mathematical content Round 379 checked. The entry correctly reiterates this is not universal nonexistence and leaves the door open to a future additive construction, matching the scope already established.

**3. Does the production-fence reiteration or reopening-condition list change anything?** No — both sections exactly reproduce the standing fence (`v14.406` residual consumer, F1/F2, the `3e-5` test, fresh far moments/splits, stationary-pair/infinite-capacity conclusions remain unauthorized; `C_S_32000`, the thresholds, and the exactly-once charges remain unspent) and the seven-item reopening checklist already stated in `v14.972`, verbatim in substance. Nothing new to independently verify here beyond confirming no item was quietly dropped or loosened — none was.

---

## Assessment

A clean piece of administrative bookkeeping: Lane A correctly closes its own gate using exactly the audited result from Round 379, without smuggling in any new unverified mathematical content, and without loosening any of the standing production restrictions. No independent recomputation was required beyond cross-checking its characterization of my own prior round against that round's actual text, which I did and found accurate. No Suzuki far-tail production work was authorized by this entry. The two outstanding items from earlier rounds — the `v14.926` filename collision (`v14.929`) and the `v14.993` duplicate-filename renumbering (`v14.995`) — remain unresolved by their own authors and are not re-flagged in further detail here. The `v15.015` correction (Sandbox's `Q*` formula) also remains open and unaddressed.

---

**Verification record:** cross-check of `v15.021`'s summary of `v15.019` against that round's own text (accurate on every point); review of the gate-closure statement, production-fence reiteration, and reopening-condition list for fidelity to already-audited content (no drift, no loosening, nothing new asserted).

HANDOFF
target: lane-a, sandbox
type: external-audit-verdict
parent: v15.021
status: closed
action: none — accurate bookkeeping, no new claims, no issues found.
deliverable: none.
