# Cone Derivation Ledger v14.490 — Lane A ACK v14.486–v14.489; open direct-middle delta gate

**Lane:** A (Cone/Suzuki)  
**Status:** ACK / certified FAIL incorporated / next scoped gate assigned  
**Parent ledger:** v14.489  
**Source entries read in full:** v14.486, v14.487, v14.488, v14.489; correction lineage v14.399 and audit v14.400

## ACK and correction incorporation

Lane A acknowledges the returned Sandbox handoff in v14.486, the External Audit correction in v14.487, the completed Sandbox residual result in v14.488, and the independent External Audit verification in v14.489.

The v14.487 correction is controlling: the even endpoint ratio is

\[
\frac{17318340263961}{69273377701969}
=0.24999993992596596\ldots < \frac14,
\]

not the displayed approximation in v14.486. The certified inequality and the v14.486 action gate remain unchanged.

This ACK records receipt and acceptance of the scoped computation. It is not a claim of whole-residual, stationary, or infinite-capacity closure.

## Gate result now controlling

The direct-middle finite-plus-gap residual gate fails in both sectors:

| sector | direct-middle point \(\ell^2\) | physical upper | allowance | ratio |
|---|---:|---:|---:|---:|
| even | \(5.05775126250299\times10^{-5}\) | \(5.057751282456339\times10^{-5}\) | \(2.2251541105255456\times10^{-5}\) | \(2.273\ldots\) |
| odd | \(5.048483094718929\times10^{-5}\) | \(5.048483114565176\times10^{-5}\) | \(2.228757296675468\times10^{-5}\) | \(2.265\ldots\) |

The physical squared residual already exceeds the sector allowance before any far charge. Because the far contribution is on disjoint support and enters by nonnegative quadrature, no far block can rescue this gate. Therefore far evaluation is moot at this checkpoint and is not authorized as a substitute for repairing the direct-middle mismatch.

The v14.448 action/residual handoff is answered in full with a certified FAIL. The controlling next step is a fresh correction candidate, not a closure claim.

## Replay scope fence

The following returned hashes remain the identifiers of the exact Sandbox witnesses:

- even seed action: **c29411b698b69dbec9a8d7827c8baddc751db6e01d6df46433d744d9064d3cd1**
- odd seed action: **f4f8a6e576bbc3351d9681073dc06e7012e377294a06a4f9fe37c018a7f5ea2c**
- even residual: **b441468d283c8276b54e637f71f6b8641a936b3126dbba59e2e17a2483db6f5e**
- odd residual: **35d4d104c9f81fb58bb48c46de063b6f0c56cbec0e501e9822287b308ab1394c**

Their arithmetic has been independently checked as reported in v14.487 and v14.489. Byte-for-byte replay outside Sandbox is not claimed because the raw buffers were not deposited in the repository. Existing payload-transfer restrictions remain in force and are not overridden here.

## Next scoped gate: direct-middle delta candidate

Sandbox is authorized to construct a direct-middle correction candidate on the exact v14.488 point-residual supports:

- even: \(2{,}080{,}767,2{,}080{,}769,\ldots,4{,}161{,}531\);
- odd: \(2{,}080{,}768,2{,}080{,}770,\ldots,4{,}161{,}532\);
- \(1{,}040{,}383\) rows per sector.

Use the v14.399 correction convention with the same hash-pinned normalized-log midpoint lineage:

**delta_DM(n) = floor_160(r_DM,point(n) / midpoint(log_normalized(n,128)))**

This is a candidate-generation gate only. It does not authorize silently changing the original \(C_{S,32000}\), the \(3\times10^{-5}\) finite-plus-gap threshold, or any existing acceptance threshold.

### Required Sandbox return

For each sector, return an additive certificate containing:

1. assertions that the consumed v14.488 point-residual buffer hash is exactly the hash recorded above;
2. the exact normalized-log/midpoint dependency hashes and an assertion that the v14.399 convention is used;
3. the 160-bit correction buffer hash, byte length, row count, exact support, exact norm-squared, outward norm upper, and outward \(\ell^1\) upper;
4. the exact one-quantum pointwise enclosure and independently recomputed integer-only sample rows;
5. the correction norm on its stated support and its contribution to the whole trial norm, tested against the unchanged \(0.002\) cap;
6. explicit false flags for action completion, residual acceptance, whole-residual closure, stationary closure, and infinite-capacity closure.

After a clean returned certificate and audit, Lane A will build a new complete RHS, obtain a fresh lift, and evaluate support-aware compact/original-seed action and residual rows with fresh output splits. The v14.471 and v14.478 witnesses must not be silently reused outside their certified scope.

## Charge and provenance invariants

- Preserve the original \(C_{S,32000}\).
- Charge v14.354 exactly once.
- Charge source plus v14.403 fresh-lift transport exactly once.
- Preserve every existing threshold.
- Freeze and replay exact hashes at each subsequent gate.
- Do not treat this candidate construction as an evaluated residual certificate.

## HANDOFF

**Target:** Sandbox, with External Audit review after return.  
**Task:** construct and certify the two-sector direct-middle delta candidate above from the exact v14.488 point residuals.  
**Ownership:** Sandbox owns only this candidate construction and certificate. Lane A retains the post-return RHS/lift/action/residual decision.  
**Current blocker:** the fresh correction certificate has not yet returned.
