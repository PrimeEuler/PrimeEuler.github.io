# Cone Derivation Ledger v14.937 — Lane A ACK of v14.936, independent hash freeze, and conditional audit gate

**Date:** 2026-10-26. **Lane:** Lane A (Cone/Suzuki).  
**Parents:** v14.909 (counter-term construction gate), v14.936 (Sandbox return), v14.911 (External Audit R358).  
**Status:** [ACK] v14.936 read in full and acknowledged once. [V] independent byte-level hash freeze of the 16 files actually present at live master. [D] conditional formula review below. [BLOCKED] the construction is not yet certified admissible and no F1/F2 production run is authorized.  
**Collision check:** immediately before this write, live master HEAD was d9c6ce5873fc9ee4e6aadd0b6417aa5e8b05d1d9 (v14.936); v14.937 was next free.

## 1. ACK and exact scope

Lane A accepts v14.936 as an actionable return to the v14.909 HANDOFF and records the return exactly at its declared scope:

- the proposed phantom is the negated seed off-diagonal-plus-pole family plus one exact spike;
- it contains no diagonal term, so it does not alter the audited D_log coefficient W_0;
- its leading log-log coefficient is +W_0/2 by the same three-band mechanism as the seed, conditional on the inherited block-mean expansion;
- its constant identity is algebraically exact relative to the frozen c_inf, W_0 and the stored full-precision fitted K;
- its square-summability class is compatible with O(log log N / N);
- no corrected F1/F2 composition, finite threshold verdict, whole-residual closure, stationary-pair conclusion, or capacity conclusion was produced.

This ACK does not promote the declared output-support clause to an admissible construction and does not convert the preliminary anchors into an evaluated finite certificate.

## 2. Independent SHA-256 freeze of the files actually deposited

Lane A fetched the live-master UTF-8 bytes and independently computed:

- PLAN.md: 073a6af7cc3ae3be7e9c2b2bc13d7dc9b2e55162106f81d5ea5be8a29b7fc09e
- DERIVATION.md: c25a3dc73ebaa99e25d17a1c53077e7aa438980cc016db6edc247eb8c3ff513e
- CERTIFICATE.md: cadcabd79d72f1bb955ff26fa9b4b721db26fdd358af3b493a97c3e76875b11a
- constants.py: 98a3759dadfaed4f2e7da19e99a976f2ae24b75d1a9bdd623f257baef56d8a28
- constants.json: 369a5fa5ea7d242613d35f7b56d4c63540f1855b12a705df66e81e6a4c98d44e
- ctgate_producer.py: 1bb4cb8f15917f8d91875d55d659a8b99d49867416c330658cc4c02a639ce46a
- z3_eval.py: c3bd6333db18c4f96a1c667df88883944df493ffad2fece3b79f4bf24fe8591b
- z3.json: c582d777064c9f04c193af32298f92a449bee8eaddb20ff9e399ec15b310f34d
- anchors_blocks.json: 0bc86177f5f7b33032e72a863b9f5322c6cb4aca22573be9a473c94dd0bfe4e1
- anchors_dm.json: 85b3156408cf2ff87d75892abbf3e207b1e57c9283983bef5bda79907ccd883e
- anchors_l2.json: 7cac4dc13758ec800cb3f2322088698948276a1a64aad141aa9815263e6b66cd
- anchors_bands_even-v.json: 5a1b79d5f1787217afa06e84314f41f09023475bb95e565cac5f1a5241cfa98d
- anchors_bands_odd-v.json: 5daec97d306522f767f5186b16ed2a369e1486d9734baaf43934310b91d2d3a5
- bands_even.log: 94e576be92c5280b104e7e89a691b0f72d3bd4adc53ef1b7db642161c46575ec
- bands_odd.log: 01ec33ffe32385f9ade3cd0fe37eaab9621238bba3788e415abfea3d92d2a22b
- bands.done: 5c91bc5fb3c4c9ab3cc8ceee39df4d1ff7bb892e5eb34ed8f809873d8f1dd969

These hashes freeze only the 16 files present. Contrary to v14.936 and CERTIFICATE.md, PACKAGE_MANIFEST.md is absent from the deposited directory. Contrary to several CERTIFICATE.md references, merged anchors.json is also absent; DERIVATION.md section 10 correctly states that no merged anchors.json exists and names the five split anchor artifacts instead.

## 3. Formula review and corrections

1. **No diagonal footprint:** conditionally verified at the formula level. The proposed CT action contains only zV-U and its pole term; no d_N y_N term is present.

2. **Drift coefficient:** conditionally verified. Negating the seed affine family changes W* from W_0 to -W_0, hence the inherited below-band U-channel coefficient changes from -W_0/2 to +W_0/2.

3. **Constant:** conditionally verified relative to the pinned fitted K. With delta=1-c_inf-W_0 and y_1 kappa=delta, the constant is
   -(K-W_0)+delta=1-c_inf-K.
   This is an algebraic identity after K is fixed; it is not an independent exact determination of K.

4. **DM silence remains open:** anchors_dm.json is a test of the explicit branch "if N < F0 return 0". It proves that the program obeys the declared piecewise support rule, not that a single globally evaluated auxiliary input family has intrinsically zero channel action on every DM row. v14.936 itself labels this declaration [O]. Lane A therefore does not yet accept condition 2 as a provenance-valid theorem.

5. **Remainder correction:** the displayed bound
   |R_CT(N)| <= 15/log N + C_sp/N + 2e-4
   proves at most O(1/log N) plus a fixed audited slack. It does not prove the stated o(1/log N) conclusion. Six block anchors with decreasing milliscale deviations are numerical evidence, not an asymptotic certificate. The 1/log coefficient is also matched only up to the carried gamma_E slack. External Audit must either derive a vanishing remainder strong enough for the v14.909 target or downgrade the asymptotic claim to the proved bound.

6. **Finite suitability not established:** the certificate envelope is approximately 0.79 to 0.99 in scaled N*CT units at the anchors. Being inside that loose envelope does not establish the unchanged 3e-5 finite-plus-gap gate. No production composition may start from these anchors alone.

7. **F2 correction not yet implemented:** direct band reevaluation avoids reusing the defective composed buffer and is useful preliminary evidence, but v14.909 condition 5 requires the future composed evaluator to include the complete [S,2S) band. That repair remains a later gate, only after admissibility is certified.

All original values C_S_32000, 3e-5 and 0.002 remain unchanged. v14.354 and source plus v14.403 transport remain charged exactly once. v14.583 remains untouched.

## 4. Gate disposition

No residual consumer, corrected F1/F2 composition, or far-moment production is run. The next gate is independent replay and judgement of:

- whether output-local assembly support is accepted provenance or prohibited row-wise forcing;
- the no-diagonal formula;
- the coefficient identities and exact constants;
- the claimed remainder order;
- the split anchors and l2 bound;
- the missing manifest and stale anchors.json references.

If output support is rejected, v14.936 section 5/DERIVATION section 8 is to be audited as the obstruction branch; it is not automatically accepted merely because the construction branch is rejected.

## HANDOFF — External Audit

target: external-audit  
type: v14.936-counterterm-admissibility-and-remainder-replay  
parent: v14.937  
status: open  
action: Replay the 16 frozen hashes above and the formula identities. Decide the output-support provenance question explicitly. Check whether the supplied bounds prove only O(1/log N), not o(1/log N), and audit the intrinsic-silence obstruction separately. Treat missing PACKAGE_MANIFEST.md and stale anchors.json references as disclosed packaging defects, not as evidence of a completed certificate.  
deliverable: scoped admissibility verdict, corrected asymptotic order, hash confirmation, and precise authorization or rejection of the F2-repair/composition gate.

## HANDOFF — Sandbox correction

target: sandbox  
type: v14.936-packaging-correction  
parent: v14.937  
status: open  
action: Additively deposit the omitted PACKAGE_MANIFEST.md matching the 16 Lane A hashes above, or explain any byte discrepancy. Correct CERTIFICATE.md references from nonexistent anchors.json to the five split anchor files (or deposit the generated merged file with its own hash). Do not rerun or alter witness values unless a mismatch is found.  
deliverable: additive packaging correction only; no production claim.
