# Cone Cross-Lane Handoff Protocol

Purpose: let Lane A and Sandbox hand off narrowly scoped research tasks through the repository without Jeremy having to relay the request manually.

## Structured handoff block

Use this exact compact block in a ledger entry or dedicated research note:

HANDOFF
target: lane-a | sandbox
type: task | payload | audit | question | blocker
parent: v13.xxx
status: open | claimed | closed
action: one explicit sentence describing the requested next action
deliverable: research-note | ledger-if-warranted | diagnostic | theorem-or-obstruction
constraints: optional semicolon-separated guardrails

## Acting rule

A lane may act autonomously only when:
- target names that lane explicitly;
- status is open;
- action is concrete enough to execute without inferring among several possible next gates;
- the task is confined to the Cone research repository/workflow.

Do not treat a generic "next gates", "open items", or "future work" section as a handoff.

## Repository discipline

Before acting:
1. read live HEAD;
2. read the latest relevant ledger/audit entries;
3. check for overlapping work in the other lane;
4. preserve source-faithful guardrails.

Before any write:
1. re-read live HEAD;
2. collision-check the intended ledger number if a ledger entry is warranted;
3. avoid rewriting or superseding another lane's live result unless explicitly marked as an audit/correction.

## Acknowledgement

A lane may acknowledge a claimed handoff in the next result it commits by including:

HANDOFF-ACK
from: <parent entry>
target: <lane>
status: claimed | closed
result: <commit or concise result>

No acknowledgement commit is required merely to say "claimed"; avoid repo noise.

## Standing scope

Autonomous handoffs are limited to mathematical derivation, numerical replay/certification, repository research notes, CI reproducer work, and ledger entries warranted by a completed theorem/obstruction.

Anything outside that scope requires Jeremy's explicit instruction.
