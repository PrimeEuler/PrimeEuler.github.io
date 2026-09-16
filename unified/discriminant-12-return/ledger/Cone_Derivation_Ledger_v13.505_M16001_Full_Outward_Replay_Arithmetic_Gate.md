# Cone Derivation Ledger v13.505 — M16001 Full Outward Replay: Arithmetic Gate

Date: 2026-09-16

Status labels: **[N-cert]** certified numerical input, **[N]** midpoint diagnostic, **[Audit]** fail-closed guardrail.

## 0. Synchronization [Audit]

Live ledger was checked at the start and immediately before this write. v13.504 was the newest numbered entry; the unnumbered replay-budget helper commit `57935549535e1da3a8b79c2546ccbcf17ea4d015` landed afterward. Thus v13.505 was free.

## 1. Source gates [N-cert]

The M16001 source constructions are now available: prime recurrence through r=8000 (v13.484), cusp Si/Ci through n=16001 (v13.486), and degree-64 archimedean rational reconstruction (v13.493). The established exact-vs-nominal operator shift remains `2e-13`; the arch analytic operator tail is `<=1.22e-13`, while prime/cusp evaluation radii are negligible on this scale.

## 2. Shifted M16001 numerical target [N]

The previously reproduced shifted anisotropic replay gives the conservative midpoint targets

- normalized six-plane lower level `lambda_min(A_Q)>0.6777`;
- Q/N cross norm `<2.68e-7`;
- corrected unresolved scalar before six-plane penalty `>9.22e-13`;
- six-plane Schur penalty `<1.06e-13`;
- final seven-plane midpoint lower target `>8.16e-13`.

The shifted remote coercivity floor is

`(4.6732-2e-13)-0.994^2/(0.22-2e-13)`, approximately `0.18212727`.

The blockwise far unresolved Gram target remains `<1.3e-15`.

## 3. Arithmetic audit [Audit]

The repository contains a binary64/long-double cross-check of the M16001 structured solve. It reports max finite-solve coefficient difference `<4e-15` and relevant shifted unresolved Rayleigh difference about `1.36e-16`. These are strong diagnostics but are not outward interval radii.

Unlike the completed M3999 certificate, the M16001 branch still lacks executable gamma_n-style outward bounds for:

1. the 7991-dimensional structured LDL/Woodbury solve and shifted finite Schur formation;
2. the normalized Q/N cross-block formation;
3. the explicit residual-Gram accumulation for `16003 <= n <= 2,000,000`;
4. the floating evaluation of the blockwise far-tail moments and their Gram envelopes.

Therefore no theorem-level interval endpoints for those four arithmetic quantities can yet be asserted from the committed artifacts. Wrapping the observed long-double differences in an ad hoc safety factor would not constitute the required outward proof.

## 4. Fail-closed result [Audit]

The numerical target remains strongly positive relative to the observed arithmetic sensitivity, but the complete outward replay requested for theorem promotion is not closed. The missing item is now arithmetic certification, not source provenance.

Hence the certified theorem remains

\[
\boxed{\operatorname{ind}_{\le0}(A_{\rm even}(1))\le4}.
\]

In particular `ind_{<=0}(A_even(1))<=3` is **not promoted** in this entry.

New helper: `research-notes/suzuki_M16001_full_outward_replay_budget.py` (commit `57935549535e1da3a8b79c2546ccbcf17ea4d015`).

## 5. Next exact obligation [Audit]

Port the M3999 `gamma_n` residual accounting to the M16001 structured solve and explicit Gram accumulation, with directed/outward charges on the Q/N block and far moments. If those radii consume less than the `>8.16e-13` shifted midpoint margin, the seven-plane positivity certificate and even-sector index<=3 theorem can then be promoted.