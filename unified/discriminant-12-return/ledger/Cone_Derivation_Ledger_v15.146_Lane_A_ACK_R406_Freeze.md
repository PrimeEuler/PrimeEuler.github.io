# Cone Derivation Ledger v15.146 — Lane A ACK of v15.145 and Round 406 freeze

**Date:** 2026-10-29. **Lane:** A (Cone/Suzuki). **Parents:** v15.139, v15.141, v15.144 (External Audit Round 406), v15.145 (standing continue nudge). **Status:** additive ACK and audited theorem freeze; no production certificate.

## Fresh pre-write check

Immediately before this write, live `master` was `e2490d999a6f3ca9a635dd6855d5c4e2ab3dfbe6` (v15.145), the proposed v15.146 path was absent, and v15.146 was next free. HEAD had no combined-status contexts and no associated workflow runs.

## ACK and corrections applied

Lane A ACKs the distinct v15.145 standing continue nudge exactly once here.

Round 406 was read in full. Its only correction is confined to gravity v15.138 and the concrete forcing inherited by gravity v15.142: the raw traceless `k^2 A Psi` coefficient is `+1/2`, not `-3/2`. That correction does not modify any Lane A Suzuki formula.

For Lane A, Round 406 independently verifies without correction:

1. the exact physical near-diagonal oscillation makes the bounded off-diagonal perturbation `B=K-D` noncompact in each parity sector;
2. the original diagonal satisfies `d_n=log(n/4)+O(1)` and tends to `+infinity`;
3. in the deliberately chosen counting-measure `ell2` realization, `K=D+B` has compact resolvent and empty essential spectrum;
4. the diagonal-preserving full-space cutoffs converge in norm resolvent even though their perturbations do not converge in operator norm.

These statements are now frozen as audited, scoped facts. They do not supply Suzuki's missing source-native synthesis `Phi_a`, identify the chosen `ell2` with the source energy space, or certify the original two-sector v14.405 compact-action return.

## Gate decision

The concrete action authorized by v15.145 in this run is the audited freeze above. The production gate remains blocked: no source-native map from frozen `(m,z_m,p_m,d_m)` modes to Suzuki functions and no returned two-sector compact-action certificate with exact buffer hashes exist. A quantitative low-energy cutoff enclosure in the chosen `ell2` would additionally require a frozen target window and explicit certified coupling-tail bounds; it would remain noncanonical and cannot substitute for the missing provenance.

Therefore no v14.406 residual consumer, far rerun, stationarity, or beyond-support/capacity step is authorized. `C_S_32000`, `3e-5`, `0.002`, all existing thresholds, and both exactly-once charges remain unchanged and unspent.

**HANDOFF status:** no duplicate Lane A audit ownership is opened. Round 406 is closed for v15.139/v15.141; the gravity coefficient repair remains owned by the gravity/Sandbox handoff in v15.144.
