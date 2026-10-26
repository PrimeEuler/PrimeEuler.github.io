# v14.819 / v14.882 sandbox return - package manifest

Assembled 2026-10-26. Status: READY, awaiting Jeremy's ledger
line. Closes v14.819 tasks 1-4 and the v14.882 sandbox handoff
(items i-iv) in one entry. Verdict: s_inf and B_seed do not
exist for the frozen pair; the combined far coefficient drifts
like +(W_0/2) ln ln(n/4); no compact or input-side correction
can cancel it; smallest admissible shape is an action-level
counter-term with far support (TASK4.md sec.3).

## Deliverables (sha256)

- SEED_FORMULA.md - task 1: the seed's full physical action
  ac5799748e8b78b02f256c18e239412452320bd2895498393b6ac47d6fade873
- TASK3.md + task3-{even,odd}-v.json + mz-{even,odd}-v.json +
  remainder-{even,odd}-v.json - task 3: c_inf both sectors
  from exact five-component M_z and P; signed-moment remainder
  bound; R346-verified.
  TASK3.md 6d81c33d4c4709955a8ffe50cbb087eb6330b1f2d3b60fc32bfd715b69a83b97
- TASK2.md + blocks_{even,odd}-v.json - task 2: s_inf does not
  exist; beta = W_0/2 exact; block means 6.2e6..2e8 both
  sectors; F2 [S, 2S) band defect (sec.4).
  TASK2.md cf3ddff847a2d6891e3e4d3fd2f1759e6f17057812b38398cf7cb43ee88048e7
  blocks_even 9605186b4136ae0413f370292fe2c94301731ece65bad79e4601329d1bd0dea0
  blocks_odd  31c526dd684657774c79c2d1257b1da36e0c3c6b278be9c7a396f21e2e5ad903
- TASK2B_THREEBAND.md + w0_exact.json - v14.882 Gate-3 reply:
  exact rational W_0, Phi remainder envelope, E_diag bound,
  three-band uniform asymptotic, B_seed non-existence.
  TASK2B 8aa040325641a2f3cbe296d3ebfbb89e624dfb1a8ca5e4993b80caee1a84efea
  w0_exact 89f6968de12c6a3bc3ca6ffd908c939c934158d5dec21cb2ea491c1528b459ab
- TASK4.md - task 4: no-compact / no-input-rescaling proofs,
  counter-term target expansion both sectors, recertification
  impact; sec.4 restates the verdict in v14.882's B_seed frame.
  a3f215f8c776fdbd47146787b418156ef34e9ec1af046d23406c3f6e132f6a6a

## Producer / verification code (rerunnable)

- eval_seed_blocks.py f4e98923b795119474b86426508a9362498549c8d8732eb577624840fe92a9b6
- fit_blocks.py       b4c7ec6c495cbf33ec0c0c974de68bb242357134da6ebfb8fb8d8bdaad23c2a9
- task3_validate.py   4fc7f0d8b9b99a0a7f2d98a0e2e63702721996af4ce897d44db46311b82a94cd
- mz_eval.py          d44c26488b6e49f07e80cdfdcda0b4bc6780d8918e228cccfd87688b13954dc7
- zbar_moments.py     9ba644d4191507583131efe8518b63a6c37ee71697c03e12e1bdf3faaeb272da
(depends on ../sandbox_region23_evaluator.py and the pinned
payloads/whole-source-affine.json, hashes asserted at runtime)

## Excluded scratch (not part of the return)

- check_f2_coverage.py + bank_float_even-v.npz + agg_even-v.json
  + coverage_even.log: the superseded coverage attempt whose
  bank sums returned NaN (self-term not excluded); the block
  comparison in TASK2.md sec.4 is the coverage measurement.
- eval_seed_large.py, fit_large_n.py, large_n_even.log:
  superseded single-row ladder (D_osc oscillation +-0.13).
- ODD_CONFIRMATION_DRAFT.md: superseded by TASK2.md as folded
  in on 2026-10-25. PLAN.md: working plan.
