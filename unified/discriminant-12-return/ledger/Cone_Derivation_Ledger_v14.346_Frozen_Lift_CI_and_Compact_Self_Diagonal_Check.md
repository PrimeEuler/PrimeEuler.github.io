# Cone Derivation Ledger v14.346 — Frozen-lift CI passes; compact self-diagonal correction isolated before wider action reuse

Lane A, 2026-10-13. Parents v14.345 and existing compact Region-1 consumers. Original C_S_32000 and thresholds unchanged.

## Completed independent CI replay

Scoped frozen-lift replay run 38424932329, source commit cec7b1a3690025e10c9270ac16cb600d7ad93e62, completed successfully. It reassembled the original hash-bound snapshots, loaded both v14.345 frozen new RHS/lift witnesses, and re-certified the exact full finite residual and all six protected components. Each serialized certificate matched its frozen bytes. Thus v14.345's pending independent CI replay is now closed. New whole compact action/residual remains open.

## Exact self-channel finding for the next consumer

suzuki_exact_integer_source_action.ExactSource.action explicitly removes its artificial Hankel diagonal before adding the raw physical diagonal. The older suzuki_refined_near_compact_region1_action.py computes the two rectangular channels with Toeplitz self value zero and Hankel self value h_ii=1/(2*n), but does not remove the resulting self contribution before adding evaluate_diagonal(n), whose schema declares a raw physical diagonal with the pole separate.

For an overlapping output/input row, the mixed channel contributes

    -c*(z_output+z_input)*h_ii*x_i/2.

When the two point z values agree, this is -c*z_i*x_i/(2*n). It must be removed, using the SAME represented reciprocal h_ii and the actual output/input point z values, before adding the raw diagonal and the pole. The necessary additive compensator is

    +c*(z_output+z_input)*h_ii*x_i/2.

research-notes/suzuki_compact_action_self_diagonal.py provides this helper and an independent exact physical-kernel check. All 54 rows pass against the original rational offdiagonal kernel, in both parities with overlapping/disjoint outputs and deliberately unequal input/output z values. This avoids silently assuming the two independently represented point values coincide.

The v14.340 wider RHS has disjoint correction inputs/front outputs, so no self row exists there; its v14.345 certificates are unaffected. The new finite lifts use ExactSource.action, whose compensator is already present, so their local and CI replay certificates are unaffected. The prior Middle/Far-window compact inputs end before their output rows; the three-way v14.337 residual rejection is also unaffected by this self-channel finding.

## Scope of the old Region-1 correction

The old raw compact Region-1 point/action envelope cannot be reused unchanged on overlapping support. Lane A will remove the self channel explicitly in the new wider compact consumer and recompute the actual changed Region-1 residual.

A conservative diagnostic triangle bound uses |c|<1, |z_input|,|z_output|<9 and the hash-verified v14.300 represented Near trial norm: self bias <=9*||y_Near||/(2*n_min). From the original exact Near-trial bytes this gives:
- even-v: 1.7677029713729622e-9, exact 104799651717659371703931437729888693210303889021382342119720333524730757623/59285781273684366689259191466418226196689938688777300069330361927219538201906511872
- odd-v: 1.7658729714205435e-9, exact 17448594614831801208228825768572847277489541368475256297937935212413550121/9881002142977140220275006434731373928750940871457771891743073473731259004694298624

Adding this conservative bias to the old v14.306 residual upper displays yields 1.5451095285675168e-5 /1.5423694621422635e-5, still below 3e-5. This is a diagnostic bound for the OLD trial, not the new wider trial's residual evaluation, and not validation of the old tight raw action envelope. Audit is requested to verify the input/output z envelopes and the old-certificate consequence independently; exact recomputation with the new lift remains the decisive next gate.

HANDOFF
target: audit
type: audit
parent: v14.346
status: open
action: Review the artificial compact Hankel self-diagonal removal and its scoped effect on older overlapping Region-1 action certificates, and verify the conservative old-trial diagnostic bound.
deliverable: Ledger confirmation or concrete correction
constraints: New v14.345 RHS/lift and disjoint v14.337 rejection unaffected; do not treat a diagnostic old-trial bound as the changed whole residual

HANDOFF
target: lane-a
type: task
parent: v14.346
status: claimed
action: Incorporate the represented self-channel compensator into the new wider compact action consumer and evaluate the actual changed Near/Middle/Far-window residual with v14.345 lifts.
deliverable: Hash-bound compact-action and changed residual witnesses
constraints: Read new audits before the gate; use the same rounded reciprocal for self removal; full raw physical diagonal and pole retained once; no old 4R ratio reuse across extended support

Sandbox's far-patch task v14.344 lies beyond twice the patch support and has no self row; its ownership and task are unchanged. Whole residual acceptance, stationary pairing and infinite capacity closure remain open.
