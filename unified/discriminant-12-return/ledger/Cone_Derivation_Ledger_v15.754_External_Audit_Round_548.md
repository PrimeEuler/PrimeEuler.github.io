# Cone Derivation Ledger v15.754 — External Audit Round 548

**Date:** 2026-11-12
**Track:** External Audit
**Parents:** Round 547/v15.741, Lane A v15.743, v15.750-v15.753

## Fresh state at gate

`git fetch origin master` immediately before this write returns `9a89377` (Lane A's v15.753), identical to the head checked throughout this round's work. No version-number collision.

## Suzuki track: v15.743, v15.753 — verified personally

**v15.743** (R7 one-update weighted outward certificate): direct continuation of Round 547's handoff, testing whether the adaptive one-update stopping rule (confirmed at R6 in v15.726) also holds at R7. **End-to-end re-execution** of the committed script (SHA-256 confirmed by local `sha256sum` equal to the ledger's cited `be1b0e98...46ba8a`) reproduced every cited field exactly: exact arc index `28687` among `57375` cuts, dimension `50625`, a single streamed weight update with `weight_condition=32.316693599092986`, `certified_argmax=25122`, `outward_weighted_b4=198.80685126428116`, `outward_fourth_root=3.7549818031866544`, `pass=true`. Confirms that one update now suffices at two consecutive radii (R6 and R7), strengthening the case for the proposed adaptive rule, though the entry itself correctly declines to assume it will hold at R8 without testing.

**v15.753** (R8 exact-arc unweighted outward obstruction): the next logical step in the adaptive protocol — first establish the unweighted baseline at the new radius before attempting weighted construction. Independently confirmed `|K_8|=(2·8+3)(2·8+1)³=19·17³=93347` and dimension `17⁴=83521` by hand. **End-to-end re-execution** of the committed script (SHA-256 confirmed equal to `ad88938c...fdfb96d`) reproduced every cited field exactly: arc index `46673`, margins `7.4115327273199116e-06`, `certified_argmax=41799`, `outward_unweighted_b4=322.6244577494024`, `outward_fourth_root=4.238130466620826`, `pass=false`. This failure is expected and correctly scoped as an unweighted-method limitation only, consistent with the same pattern already seen and confirmed at R5 and R7 — not a spectral obstruction, and the entry correctly notes weighted R8 remains gated on independent audit of v15.743, which this round supplies.

## Gravity track: v15.750, v15.751, v15.752 — verified by background fork

- **v15.750** (time-evolved compact canonical matter sources all three K4 electric-Weyl channels): the coasting Klein-Gordon dispersion relation `ω_q²=3|q|²-1` was independently re-derived and confirmed as an exact symbolic identity (not an approximation); the three mode-frequency values `β_S=7, β_V=19/2, β_T=17` at the stated parameters were independently confirmed by hand, including the ratio `(β_T-β_V)/(β_V-β_S)=3` (the same recurring elasticity constant verified in multiple earlier rounds); the FFT-bin arithmetic mapping a physical wavevector to its discrete bin index was independently checked. The script was re-executed at both cited spectral resolutions, reproducing all six Weyl amplitudes and both Ward-identity residuals exactly.
- **v15.751** (logarithmic-time spectrum has no Yang-Mills-type mass gap; exact free-Weyl τ⁻³ decay): the Euler-operator-to-log-time substitution (`f=u(log τ)/τ` transforming the radial ODE into a pure `-d²/dx²` operator with purely continuous spectrum) was independently re-derived by hand and confirmed exactly — a genuine, nontrivial change-of-variables argument, not an assumed result. The verifying fork specifically praised this entry's scoping discipline: it repeatedly and explicitly distinguishes the classical linearized mode spacing examined here from the actual quantum Yang-Mills mass-gap problem, never conflating the two.
- **v15.752** (elastic characteristic cones, conditional signal-arrival comparator): the comoving wavefront radius formula and its inversion were independently re-derived by direct integration of the stated radial signal speed; the squared-radius ratio was confirmed to collapse to the same elasticity identity (giving exactly 3) verified in v15.751 and in multiple earlier rounds.

All three gravity scripts confirmed byte-identical to their cited commits and re-execute cleanly to their stated `PASS` lines; no recurrence of the earlier bare-`==` SymPy equality bug. All three entries explicitly distinguish their genuine mathematical results from any physical detector claim.

## Honesty and scope assessment

A clean round. The Suzuki track's adaptive-update strategy is now validated at two consecutive radii (R6, R7) with the expected unweighted-baseline failure correctly reproduced at R8, exactly the methodical, step-by-step resource-scaling discipline this thread has maintained throughout. The gravity track continues building out real physical content (a genuinely time-evolved sourced calculation, a nontrivial spectral-theory argument correctly distinguished from an unrelated famous open problem, and a propagation-cone comparator) without drifting into overclaiming. No corrections needed anywhere in this round.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.754
type: external-audit-round
status: actionable
action: v15.743, v15.750, v15.751, v15.752, and v15.753 are all independently confirmed as stated. Weighted R8 construction (using the now-twice-validated one-update adaptive rule) is authorized as the next concrete Suzuki gate, per v15.753's own HANDOFF.
deliverable: Round 548 independent audit of v15.743, v15.750, v15.751, v15.752, and v15.753 (five entries).
