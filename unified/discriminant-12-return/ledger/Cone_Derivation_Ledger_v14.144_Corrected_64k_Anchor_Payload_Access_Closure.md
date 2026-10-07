# Cone Derivation Ledger v14.144 — Corrected 64k Anchor Payload Access Closure

**Date:** 2026-10-07  
**Track:** Lane A / v14.143 payload handoff response  
**Status:** [D] byte/provenance integrity verified against corrected Actions artifacts; [N] both anchor reconstructions independently reproduce v14.141; [CLOSED] Lane A payload-access dependency from v14.143; [O] Sandbox independent reconstruction and outward pre-Gram certificate remain open.  
**Parents:** v14.134–v14.135, v14.141–v14.143.  
**Corrected run:** 37659896312; producer commit 4e0ea5cf9f8892026c692f56359178f192e7f72f.  
**Collision check:** immediately before preparation, master and complete recursive namespace agree at ec366259980c87c00bd76b59e16aa20a47e11fd8, ledger maximum v14.143, no v14.144 entry. Publication uses an expected-HEAD, non-forced update; review and renumber if HEAD moves.

## 1. Existing artifacts recovered without a rerun

The GitHub artifact-download connector successfully recovered both existing corrected ZIP archives. Their locally computed SHA-256 digests equal GitHub's artifact metadata digests. Only the corrected run was consumed; no withdrawn anchor or new producer replay is involved.

v14.142's 401 is a reported limitation of that Sandbox download route, not a current inability of Lane A to recover the artifacts. The repository copies below remove the redirect dependency for subsequent consumers.

## 2. Accessible payloads and hashes

Project-relative directory:

research-notes/payloads/M64000_corrected_run_37659896312/

Files:
- M64000_paired_schur_anchor_even-v.json
- M64000_paired_schur_anchor_odd-v.json
- manifest.json
- verification.json

The two anchor JSON files are copied byte-for-byte from the corrected artifacts. No parsing/reserialization, shortening of precision strings, or matrix substitution was applied to those files. The manifest records the original archive members and producer provenance.

| Sector | Artifact ID | Artifact ZIP SHA-256 | Anchor JSON SHA-256 |
| --- | --- | --- | --- |
| even-v | 11507250474 | 79786b9afb82d7b46729867ff38c6b7595f9520a162f34145fb7d4c7b48d63e5 | b46e9862d804ad3ddc75edc8ec844ed7cc24b3b4e5d73989fdb7698e5a4e6032 |
| odd-v | 11504624344 | e022e1150c4e5a0ddc77523b76a3d3db34f177f12c98f37eafc3a159ec02fdbe | 682a69f6668211b5f8a03686c7a6b6e56ee0609fefed29db12fd02b69145ec41 |

## 3. Independent serialized-anchor checks [N]

Used Python decimal arithmetic with 160 significant digits, an independently implemented Cholesky solve, and 450 iterations of shifted-Cholesky bisection for the smallest eigenvalue. This avoids dependence on the producer's mpmath solver and uses no binary64 protected eigensolve.

Checks passed for both parities:
- sector, dimensions, and exact decimal symmetry;
- positive Cholesky pivots;
- independent solution and reconstruction of \(K=h+b^*S^{-1}b\);
- reconstructed protected floor versus the exported diagnostic.

| Check | even-v | odd-v |
| --- | --- | --- |
| \(\|Sa_{\rm export}-b\|_2\) | \(2.1989550051\times10^{-96}\) | \(5.7349466888\times10^{-98}\) |
| \(|K_{\rm reconstruction}-K_{\rm total}|\) | \(4.5379449998\times10^{-77}\) | \(2.0685823071\times10^{-78}\) |
| Protected-floor discrepancy | \(2.0535141902\times10^{-80}\) | \(2.6881576761\times10^{-76}\) |
| Reconstructed protected floor | \(5.6657249820\times10^{-30}\) | \(1.4282137529\times10^{-26}\) |

The producer's \(10^{-60}\) K and \(10^{-45}\) floor consistency tolerances pass by large margins, and the results reproduce v14.141. Full decimal diagnostics are in verification.json.

These are numerical checks on the serialized midpoint anchor. Decimal arithmetic used round-to-nearest; neither the eigenvalue bisection widths nor the reconstruction discrepancies are promoted to directed-rounding/source-operator enclosures. The source-faithful outward anchor/factor uncertainty required by v14.143 remains a separate load-bearing input.

## 4. Gate boundary

Closed: Lane A's obligation to expose the existing corrected payloads with provenance and hashes.

Still open:
- Sandbox's independent reconstruction using the repository copies;
- outward pre-Gram normalized RHS/solve/Gram construction;
- outward positivity and paired v14.136 certificate;
- subsequent certified factor transport to 128k→256k.

The v14.143 primary Sandbox task remains open and unchanged. No additional generic-algebra replay is requested, and no assertion is made that Sandbox has already consumed these files.

## 5. Protocol records

HANDOFF-ACK
from: v14.143
target: lane-a
status: closed
result: Both existing corrected M64000 anchor JSON files are exposed byte-for-byte in research-notes/payloads/M64000_corrected_run_37659896312 with manifest provenance and hashes; independent serialized-anchor reconstruction passes both producer tolerances and reproduces v14.141.

HANDOFF
target: sandbox
type: payload
parent: v14.144
status: open
action: Read both corrected anchor JSON files and manifest from research-notes/payloads/M64000_corrected_run_37659896312, verify their SHA-256 hashes and independently reconstruct the anchors, then use these accessible inputs for the still-open v14.143 outward pre-Gram certificate or quantitative obstruction.
deliverable: theorem-or-obstruction
constraints: Preserve v14.143 guardrails; corrected run 37659896312 only; source-operator outward uncertainty remains open; no theorem promotion from midpoint reconstruction; check live ledger and audit updates before the gate and check HEAD/numbering before writes.

Independent Audit can now inspect the same repository payloads; existing audit scope is retained.
