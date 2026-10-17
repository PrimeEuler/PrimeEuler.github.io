# Cone Derivation Ledger v14.540 — External Audit Round 306: v14.539 Complete-RHS Return — Cross-Checks Pass, New Output Bytes Not Yet Repository-Accessible

**Date:** 2026-10-17
**Track:** External Audit
**Status:** [V] v14.539 is read in full. It is the first substantive numerical return since the v14.510 producer handoff (eight intervening ACKs, v14.506 through v14.536). It reports both-sector completion of `suzuki_direct_middle_delta_rhs.py`, with a new complete-RHS certificate/buffer per sector, and opens a fresh-lift request to Lane A. Every claim this auditor can check without the as-yet-untransferred output bytes checks out exactly: pinned hash constants, buffer byte-count arithmetic, the whole-trial-norm triangle-sum reproduction (independently computed in Round 296), and an order-of-magnitude derivation showing the new "complete physical-RHS error upper" figures are expected to — and do — match the v14.403 base RHS certificates' own pre-existing error field to the displayed precision. The new certificate/buffer hashes themselves are not yet independently verifiable: no payload bytes have been transferred to the repository, exactly as v14.539 itself discloses ("the payload transfer ... awaits Jeremy's explicit line"). This is reported as a scope limitation, not a defect.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–500, v14.500–539.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `ecabd2b...` (v14.539), matching local HEAD; live ledger max was v14.539. v14.540 is next-free. No collision.

---

## 1. Pinned hash constants — cross-checked exact against the already-reviewed producer

v14.539 cites six hashes as the exact inputs the producer run consumed: two snapshot SHA-256 (even `da718974...eb5`, odd `6ba7a15a...453`), two v14.500 candidate-point SHA-256 (even `c5b68453...2bb2`, odd `e9efaf91...2776`), and two v14.403 base-RHS-certificate SHA-256 (even `42c71d7e...075`, odd `1309bec0...0b3`). All six were grepped directly out of `research-notes/suzuki_direct_middle_delta_rhs.py`'s own hardcoded `SNAPSHOT_SHA256`/`CANDIDATE_SHA256`/`BASE_CERT_SHA256` dicts — the same script this auditor read in full and partially re-executed in Round 297 — and match character-for-character. No substitution of inputs occurred.

## 2. Buffer byte-count arithmetic — exact

```
even/odd lift-RHS:      128,000 rows x 30 bytes = 3,840,000  -- claimed 3,840,000, exact
even/odd correction-z:  1,040,383 rows x 21 bytes = 21,848,043 -- claimed 21,848,043, exact
```

Row counts (128,000 front / 1,040,383 direct-middle) match the producer's own `N`/`M` constants exactly.

## 3. Whole-trial norm upper — independently reproduced from Round 296's own exact arithmetic

v14.539's table gives whole-trial norm upper even `1.720328e-04`, odd `1.719923e-04`. This auditor already computed these exact sums in Round 296 (Fraction arithmetic, base v14.403 upper + v14.500 correction upper):

```
even: 0.0001720327820072869  -> rounds to 1.720328e-04  (exact match)
odd:  0.0001719923297163405  -> rounds to 1.719923e-04  (exact match)
```

Both match to full displayed precision. The delta correction norm uppers in v14.539's table (even `3.7520048128694792e-06`, odd `3.7451276392601123e-06`) are copied character-for-character from the v14.500 certificates this auditor byte-verified in Round 296.

## 4. New "complete physical-RHS error upper" — order-of-magnitude derivation confirms plausibility

v14.539 reports complete physical-RHS error upper even `3.213e-30`, odd `3.210e-30` (cap `<4e-30`). Reading the cited v14.403 base RHS certificates directly (`research-notes/payloads/gap_correction_rhs_and_lift_v14_403/gap-correction-RHS-{even,odd}-v.json`), their own pre-existing `display_approximate/RHS_error` fields are even `3.2131128292548455e-30`, odd `3.2100986315445134e-30` — matching v14.539's "complete" figures to all four displayed significant digits.

This is not a coincidence to wave away; the producer's own formula (`suzuki_direct_middle_delta_rhs.py`, read in full in Round 297) is `error = sqrt_upper(N,256)*row_error + physical_lift_rhs_error_upper(base)`, where `row_error` is driven by the new delta correction's ℓ¹ norm (`correction_l1 ≈ 0.00325`) at coefficients of order `1e-38`. Estimating: `row_error ≈ 21e-38 × 0.00325 ≈ 6.8e-40`; multiplying by `sqrt_upper(128000,256) ≈ 357.8` gives an added term of order `2.4e-37` — about seven orders of magnitude below the `~3.21e-30` base error, hence invisible at the displayed precision. (The `abs(P)` term is smaller still: bounding `pole[j]` by `~2/mode·2^256` for `mode` up to `~4.16e6` and `delta[j]` by the correction's own per-row scale gives `P ≈ 2×10⁻⁹`, so `2e-38·|P| ≈ 4×10⁻⁴⁷`, negligible.) The claim that adding the direct-middle delta correction leaves the complete physical-RHS error essentially unchanged from the v14.403 base value is therefore independently predicted by the producer's own stated formula, not merely asserted — and the prediction matches the reported figures exactly. This is a genuine, non-trivial cross-check, though it stops short of a full exact replay (which would require the raw per-row z/pole values this auditor does not have).

## 5. Scope limitation — disclosed, not a defect

No file matching the new certificate hashes (`d56eaf3a...`, `19c67577...`) or buffer hashes (`2fb4363f...`, `e8d1e795...`, `0e9e889c...`, `4ba2d312...`) exists anywhere in the repository; the only occurrence of these strings is in v14.539's own ledger prose. This matches v14.539's own disclosure that the chunked payload transfer "awaits Jeremy's explicit line." This auditor therefore cannot independently byte-verify the new certificates/buffers this round, for the same reason the v14.500 payload could not be verified between its announcement (v14.500) and its eventual repository transfer (confirmed in Round 296) — a precedent this project has already worked through once. The max-correction-input-z-error figures (`7.15e-42`, both sectors, cap `<1e-39`) are plausible in magnitude (far below both the cap and the `2^-160` quantization grain) but likewise not independently recomputable without the raw snapshot.

## 6. Run narrative and fresh-lift request — informational, no numerical claim

The reported operational narrative (two failed launches on a staging manifest-shape mismatch, a mid-run VM replacement that killed the odd sector at row 560,000, a restart from row 0, independent re-verification after both sectors completed) is operational detail, not a mathematical claim, and is consistent with the producer's own documented single-shot-per-sector design (Round 297 read). The fresh-lift request to Lane A (asking for a direct-middle analogue of the v14.403 finite-lift producer, hash-gated to the new RHS hashes) is a reasonable, scoped ask, mirroring the same proportionate-request pattern this auditor already endorsed for the v14.503 payload-transfer request in Round 294. All closure flags (`new_finite_lift_certified`, `new_residual_evaluated`, `whole_residual_acceptance_certified`, `infinite_capacity_tail_closed`) remain correctly false; no v14.403 lift is reused.

## 7. Verdict

```
Pinned hash constants: exact match to the already-reviewed producer.
Buffer byte-count arithmetic: exact.
Whole-trial norm upper: reproduces this auditor's own Round 296 exact
  Fraction sums to full displayed precision.
Complete physical-RHS error upper: independently predicted via the
  producer's own error formula to be indistinguishable from the
  v14.403 base error at this precision -- and it is, exactly.
New certificate/buffer hashes: not independently verifiable this
  round -- no payload bytes are yet repository-accessible, matching
  v14.539's own disclosure. Scope limitation, not a defect.
No defect found in anything checkable. Awaiting the payload transfer
  for full byte-level replay, and Lane A's response to the fresh-lift
  producer request.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.540
status: open
action: this auditor independently cross-checked every claim in v14.539 that does not require the untransferred output bytes (hash provenance, buffer arithmetic, triangle-sum reproduction, and an order-of-magnitude derivation of the new physical-RHS error figure from the producer's own formula) -- all exact or exactly as predicted. No correction needed. The new certificate/buffer bytes remain outside the repository; full byte-level replay awaits that transfer, as it did for v14.500.
deliverable: none required; informational confirmation
constraints: None.
