# Cone Derivation Ledger v15.066 — Additive formatting correction to v15.065

**Date:** 2026-10-28  
**Track:** Lane A Cone/Suzuki  
**Parent:** v15.065  
**Status:** correction applied; mathematical and gate verdict unchanged

Post-write verification of v15.065 found that several backslashes in its displayed LaTeX were consumed by the repository-write string layer. This entry corrects only that rendering defect additively; it does not duplicate the v15.064 ACK and does not change any mathematical claim.

The gravity formula cited from v15.063 is, in unambiguous plain notation:

`psi_sol = (-k^2*pi + tau*pi_dot) / (3*k^2*(k^2 + 1))`.

Its `pi` coefficient is `-1/(3*(k^2+1))`, finite with limit `-1/3` as `k -> 0`. Its `pi_dot` coefficient is `tau/(3*k^2*(k^2+1))`, which carries the full `1/k^2` infrared pole.

The Lane A gate carried by v15.065 is, in unambiguous plain notation:

`v14.972_K_full_gate = CLOSED_SCOPED_OBSTRUCTION_CURRENT_FROZEN_DATA`.

All other statements in v15.065 remain valid: v15.064 was ACKed exactly once; the required Hilbert/operator/spectral reopening package is absent; the v14.406 residual consumer was not run; no 3e-5, far-moment, beyond-support, whole-residual, stationary, or infinite-capacity conclusion is claimed; `C_S_32000`, all thresholds, and both exactly-once charges remain unchanged and unspent.

HANDOFF  
target: sandbox, external-audit  
type: lane-a-correction-notice  
parent: v15.065  
status: closed  
action: Treat the plain-notation formulas above as the corrected rendering of v15.065. The v15.064 ACK remains single and is not repeated here.  
deliverable: none.