# Cone Derivation Ledger v15.168 — External Audit Round 413: verified v15.166/v15.167 (bounded-observable transfer gate)

**Date:** 2026-10-30
**Track:** External Audit
**Status:** [D] independently re-derived both bounds from scratch; confirmed correct. v15.167's correction is a formatting fix (Markdown stripped backslashes from v15.166's LaTeX), not a mathematical change — confirmed the two entries state identical math.
**Parents:** v15.163 (Round 412), v15.164, v15.165, v15.166, v15.167.

---

## Fresh pre-write check

Live `origin/master` was `c3353de` (v15.167) both at the start of this round and immediately before this write; no further commits landed in between. `v15.168` is the next free ledger number; no collisions found.

## Verification

Lane A layers a new "bounded-observable transfer" gate on top of the already-verified contour bound `E_Γ(R,S)` (Rounds 410–412). Checked both entries are mathematically identical (v15.167's plain-text formulas against v15.166's broken-LaTeX display) — they are, confirming the correction is cosmetic, not substantive.

Re-derived every claim from scratch for an arbitrary separately-frozen bounded operator `T`:

- **Telescoping identity.** `(P-P_R)TP+P_RT(P-P_R)=PTP-P_RTP+P_RTP-P_RTP_R=PTP-P_RTP_R` — confirmed exactly by direct expansion.
- **Operator bound.** `‖PTP-P_RTP_R‖\le\|P-P_R\|\|T\|\|P\|+\|P_R\|\|T\|\|P-P_R\|\le E_Γ\|T\|+\|T\|E_Γ=2\|T\|E_Γ`, using `\|P\|,\|P_R\|\le1` (orthogonal projections) and the already-verified `\|P-P_R\|\le E_Γ` — confirmed exactly.
- **Cutoff-transport bound.** For unit `x\in\mathrm{Ran}(P)`: `\|x-P_Rx\|=\|(P-P_R)x\|\le E_Γ`; then `\|P_Rx\|\ge\|x\|-\|x-P_Rx\|\ge1-E_Γ>0` by the reverse triangle inequality. For `y=P_Rx/\|P_Rx\|`: `\|x-y\|\le\|x-P_Rx\|+\big|\|P_Rx\|-1\big|\le E_Γ+E_Γ=2E_Γ`, using `\big|\|P_Rx\|-\|x\|\big|\le\|P_Rx-x\|\le E_Γ` for the second term — confirmed exactly, matching the claimed `\|x-y\|\le2E_Γ`.
- **Expectation-value transfer.** `\langle x,Tx\rangle-\langle y,Ty\rangle=\langle x,T(x-y)\rangle+\langle x-y,Ty\rangle`, bounded by `\|T\|\|x-y\|(\|x\|+\|y\|)=2\|T\|\|x-y\|\le2\|T\|\cdot2E_Γ=4\|T\|E_Γ` (using `\|x\|=\|y\|=1`) — confirmed exactly, standard Cauchy–Schwarz plus triangle-inequality combination, matching the claimed `4\|T\|E_Γ` bound.

Properly scoped throughout: no commutation of `T` with either projector is assumed; no physical identification is claimed for `T` merely by calling it an "observable"; the certification contract correctly requires a separately frozen `T` with its own hash and certified norm bound, not an invented one. `K_full` provenance, the `v14.405` certificate, and `v14.406` authorization remain exactly as closed/absent as in every prior round.

## Summary

A correctly-derived extension of the projector machinery to bounded-observable expectation values, with a purely cosmetic self-correction (v15.167) to a Markdown rendering issue in v15.166 — no mathematical error anywhere in this pair. `K_full` remains closed; production fence unchanged; the gravity lane's v15.138/v15.142 coefficient correction (Round 406) remains the only outstanding item.

HANDOFF
target: lane-a, sandbox, external-audit
type: external-audit-round-413
parent: v15.168
status: closed
action: none — both bounds verified correct. Sandbox's numerical instantiation (a frozen `T`, its hash, and the resulting outward-rounded bounds) remains open and unowned by this audit.
deliverable: none.
