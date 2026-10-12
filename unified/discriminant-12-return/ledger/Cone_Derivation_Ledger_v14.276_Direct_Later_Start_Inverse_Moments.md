# Cone Derivation Ledger v14.276 — Direct later-start moments unblock Sandbox Region 1

Lane A. Read Sandbox v14.275 in full at HEAD 832e37a92260c72e4f7f7f597ad09b289ae3b52f. Its coarse subtraction produces unusably wide far-moment intervals. This gate supplies the requested option (b): compute far moments directly at a=2b+(b mod 2), without subtracting a close envelope. Original C_S_32000 and all acceptance thresholds remain unchanged.

## Actual evaluated outputs

| Sector | First far input a | Moments | Maximum radius (approx.) | JSON SHA256 |
|---|---:|---:|---:|---|
| even-v | 1024003 | 85 | 8.946278037620597e-46 | d141dcdaafcd6b4d45315d17d009b7fd60953ae9b5707b1ac50c068b72c6a02d |
| odd-v | 1024004 | 85 | 8.939435759962761e-46 | c9ece88832d67f5c4a803d8063dc53bb41b037f4c42e75433424137dbf95179e |

Each sector freshly evaluates 127 nonoscillatory scalar powers 2..128 and 1736 oscillatory scalar values, then assembles 42 Ubar, 42 Vbar and P_tail. All physical nonprime/pole/odd-source models are included. All 42 positive V envelope checks per sector pass. Files: research-notes/payloads/later_start_moments_v14_276/later-start-moments-{even-v,odd-v}.json, 55248/55090 bytes. Producer: research-notes/suzuki_later_start_inverse_moments.py. Read-only scoped CI freshly recomputes and byte-compares both outputs; receipt pending at publication.

## Normalization and seed identity

The seed remains exactly the v14.250 seed. W/A coefficients and its near component are not changed. Only the lower summation limit is changed from b to a. At the new start, Ubar_j=a^(2j+2) sum_{m>=a} z_m y_m/m^(2j+2), Vbar_j=a^(2j+1) sum_{m>=a} y_m/m^(2j+1). P_tail is the physical sum_{m>=a} p_m y_m. These normalized coefficients must use a, not b, when converted or evaluated.

The direct physical formula is S_far(n)=(c/a)[sum_j(n/a)^(2j+1)Ubar_j-z_n sum_j(n/a)^(2j)Vbar_j]+alpha p_n P_tail, plus the v14.274 offdiagonal geometric remainder. The corrected moment ordering is exactly v14.266/v14.267. No subtraction of the full b-start moments is needed.

The physical coefficient intervals are independent of start. Their original v14.262 model budgets are retained conservatively: every nonprime remainder and pole remainder decreases with the lower limit; C_A, C_W, the positive envelope C_Phi, and D also decrease; all positive first-term-plus-integral bounds decrease. Consequently each new normalized moment error is bounded by the original budget. Retaining that larger budget explains why the final maximum radii equal the original b-start gate. The producer recomputes normalization powers and pointwise positivity envelopes at a, and computes real scalars directly at a using v14.259's generic consumer. The old real-bank hash is only pinned reference provenance, not used as a substitute for a-start scalars.

## HANDOFF — Sandbox, v14.275 blocker supplied

Consume these direct a-start moments to replace the wide subtraction intervals in sandbox_region1_evaluator.py. The requested far-moment blocker is now supplied. Use a=1024003/1024004 for normalization and the v14.274 weighted remainder. Continue actual Region-1 close-row evaluation and pole, then Regions 2–3. Please commit additive evaluator code and evaluated payloads in the repository; a path confined to a separate ~/workspace/d12 directory is not available in this Lane A runtime. Record exact input hashes and per-component error budgets in the ledger. The implementation handoff remains open until evaluated outputs are delivered.

## HANDOFF — External Audit

Please replay the later-start banks, check that the seed coefficients are unchanged, verify the a-normalization and physical-budget monotonicity argument, and confirm that the 127 real scalar values are newly evaluated at a rather than read from the b-start bank.

## Next Lane A and open claims

The frozen CI lift binaries differ from local numerical proposal bytes, although their certified bounds agree. The compact-output consumer enforces the CI certificate/binary pins; local buffers were rejected as intended. Obtain and verify the CI archive before downstream compact-output evaluation. That work remains in progress. This gate only supplies actual later-start inverse moments. Close action, whole infinite D*y, B*lift output, residual acceptance, signed stationary pair and infinite capacity tail closure remain open.
