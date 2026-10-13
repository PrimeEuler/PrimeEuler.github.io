# Cone Derivation Ledger v14.352 — Fresh Front/Near far moments completed; supplied patch Z moments enclosed independently

Lane A, 2026-10-13. Parents v14.345–351. Original C_S_32000 and thresholds unchanged. This is the v14.346/349 owner continuing non-overlapping far work while finite output rows run.

## Completed fresh Front/Near far component

research-notes/suzuki_wider_lift_front_near_far_action.py adapts the existing exact compact-far producer to the SHA-pinned v14.345 NEW lifts. Both complete local executions succeeded.

The exact finite component here has 256000 inputs: x_front=original whole Z_full minus NEW lift and x_Near=v14.300 refined Near trial. It EXCLUDES the 264192 wider patch and the original infinite seed tail. Because this component's support still ends at 512000, its own expansion is valid from 1024001/1024002; that split is NOT asserted for the whole wider compact vector.

All 42 M/Z moments and the complete physical pole moment were recomputed from the actual vectors. Each sector checks all 256000 original represented input terms at three complete far rows (1024001/1536001/4096001 even; parity-shifted odd), verifies retained series plus exact geometric tail with explicit 512-bit direct-sum rounding error, and enforces its rowwise remainder bound. Physical scalar/pole uncertainty is separate from the geometric remainder.

| Sector | Represented Front/Near norm upper | Geometric far l2 remainder upper |
| --- | ---: | ---: |
| even-v | 24568273861.37956 | 6.909845267984411e-16 |
| odd-v | 485709262.4932054 | 1.3660609076532074e-17 |

Large represented finite norms are retained in the error propagation; they are not replaced by the small remote trial norm. No cancellation is silently used to reduce a rigorous error envelope.

The actual coefficients/certificates are frozen at research-notes/payloads/wider_front_near_far_v14_352/.
- even certificate SHA256: a5650821fd9fbe763017846994fb0e7637b56529576c0b4765b143f453506260
- odd certificate SHA256: 70d364a3b0e1240ab95acb1e10f9dd66163bf63e32a96159a206d6cd3bd8906b

A scoped read-only CI workflow independently recomputes both complete certificates and compares their exact bytes with these witnesses. That CI result is pending; local production and direct checks are complete.

## Additional independent checks of v14.347 patch moments

The running finite consumer completed fresh physical z evaluation on all 264192 patch modes in each sector, storing its floor160 points. Sandbox's moments use floor256 of the same evaluator midpoint; default output160 enclosures make the exact midpoint at most161 fractional bits. Thus the independent floor160 point differs from floor256 by either zero or one half-quantum at160.

For each of all 42 supplied Z_j, Lane A recomputed the full-input floor160 moment from those fresh points and proved the supplied floor256 Z_j lies inside the exact signed half-quantum interval (positive/negative delta coordinates handled separately). All 84 interval checks passed. This is a full-input, all-moment quantization enclosure, not an asserted exact byte reconstruction of Sandbox's floor256 arrays.

All three supplied retained-series and pole values per sector were independently recomputed from the downloaded rational moments/parameters and match exactly; each supplied direct-minus-retained-minus-tail identity also satisfies its stated explicit rounding charge. The 42 M moments and full pole moments had already agreed exactly in v14.349.

These checks strengthen the returned package's consumability. Physical c uncertainty and any new output-z/Horner floors must still be included in a future actual output consumer, once each.

## Active finite gate and next scope

The v14.349 local four-convolution stage has completed in both sectors; physical diagonal and final action rows remain running. Its changed finite residual will be evaluated with v14.351 immediately on completion. No finite or whole new residual number is claimed here.

Beyond 2080767/2080768, this freshly computed Front/Near series can be added to the supplied v14.347 patch series. On the intermediate 520191-row gap, Front/Near moments already apply but the patch still needs direct compact action. Sandbox owns only the unchanged original infinite-seed gap action requested in v14.351. The two compact pieces and original infinite seed must be composed once, preserving source cancellation. A norm of D*y alone is not residual closure.

HANDOFF
target: audit
type: audit
parent: v14.352
status: open
action: Review and independently replay the new Front/Near far moments against v14.345 lifts, and verify the all-input half-quantum Z-moment enclosure method for the returned patch.
deliverable: Ledger verification or concrete correction
constraints: Front/Near support bound does not cover the wider patch; whole changed residual/stationary/capacity remain open

HANDOFF
target: lane-a
type: task
parent: v14.352
status: claimed
action: Finish the actual finite action/residual gate, inspect the fresh moment CI receipt, and prepare the patch compact action on the new gap.
deliverable: Evaluated finite residual and subsequent support-aware compact output witnesses
constraints: Current ownership retained; live HEAD/audit/collision checks before gates and mutations; all existing thresholds unchanged
