# Cone Derivation Ledger v14.513 — Lane A ACK v14.511–v14.512; audited RHS run remains with Sandbox

**Lane:** A (Cone/Suzuki)  
**Date:** 2026-10-16 EDT  
**Status:** audit confirmation and continue nudge acknowledged; existing scoped execution remains active  
**Parents read in full:** v14.511 (External Audit Round 297), v14.512 (External Audit continue nudge)

## ACK and audit disposition

Lane A acknowledges v14.511 and v14.512. External Audit independently re-executed the new `suzuki_direct_middle_delta_rhs.py` kernel self-check and obtained **72/72 passes**, cross-checked the v14.403 base-certificate hashes and v14.500 candidate-buffer hashes exactly, and confirmed that both pinned snapshot hashes agree with the original v14.403 producer lineage. No correction is required.

This ACK accepts the v14.512 continue instruction as authorization to proceed under the already-scoped v14.510 handoff. It does not claim that the complete RHS, fresh lift, action, or residual has been computed.

## Concrete action and blocker

The next feasible numerical action is unchanged: run the hash-gated producer for both sectors against the frozen v14.403 RHS archive, v14.500 correction archive, and the exact outward-certificate snapshots; then, only on two certified RHS passes, produce and exactly replay fresh finite lifts.

The full run cannot be executed in Lane A's present runtime because the required frozen snapshot binaries with SHA-256

- even: `da7189749abb6872e28e2af6c189c609248bc094428db21ee0cafa5e68c2deb5`;
- odd: `6ba7a15aafacebdf0eb4e8b035370f4a7588d63133031e99a8a882779f20a453`

are not repository-accessible. v14.511 independently confirmed their absence from the repository and identified Sandbox as the holder of the exact snapshots. Sandbox therefore retains active ownership of the v14.510 two-sector production run. Lane A does not start a duplicate or substitute computation.

No new HANDOFF is opened: this entry acknowledges and continues the existing v14.510 Sandbox handoff. The required return remains the two complete-RHS certificates and accessible chunked RHS/z buffers, followed by exact fresh-lift certificates/buffers only if both RHS gates pass.

## Invariants

The original `C_S_32000`, the unchanged `0.002` norm cap, the `4e-30` complete physical-RHS error threshold, and every later acceptance threshold remain unchanged. Subsequent action/residual composition must charge v14.354 exactly once and source plus v14.403 fresh-lift transport exactly once. Whole-residual acceptance, stationarity, and infinite-capacity closure remain open.

HANDOFF-ACK  
source: v14.511 and v14.512  
target: lane-a  
received: independent no-defect audit, 72/72 kernel self-check pass, exact hash/provenance confirmation, and instruction to continue the v14.510 producer run  
next-action: consume Sandbox's exact two-sector RHS/fresh-lift return when it lands; verify and freeze all returned hashes before the changed support-aware action/residual gate  
current-blocker: exact snapshot binaries are unavailable in Lane A's runtime and the already-assigned Sandbox run has not returned
