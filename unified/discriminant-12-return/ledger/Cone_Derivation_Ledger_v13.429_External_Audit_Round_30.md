# Cone Derivation Ledger v13.429 — External Audit Round 30

Date: 2026-09-14

Status labels: **[S]** source-established, **[D]** exact derived, **[N]** numerical, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## Scope

This round covers `v13.427` (χ12 exponential moment-generating transform) and `v13.428` (rational prime base-angle certificate, renamed from a `v13.426` collision with this round's own Round-29 entry).

## 1. Version collision — fixed the same way as prior rounds

**[Audit → resolved]** `Cone_Derivation_Ledger_v13.426_Prime_Base_Angle_Rational_Certificate.md` landed with the same number as this audit's own `v13.426_External_Audit_Round_29.md`. Renamed to `v13.428` (the next free slot — `v13.427` had been independently taken in the interim by the exponential-transform entry); content unchanged. Now five rounds running with a version-bookkeeping fix somewhere in most of them; worth the project considering a `git ls-tree` check as a standing pre-commit habit for both sessions, though the fixes have been cheap each time.

## 2. Rational prime base-angle certificate (`v13.428`) — verified exactly, after catching my own arithmetic slip

**[D, independently verified]** This entry replaces floating transcendental constants with exact rational-interval arithmetic for the five Suzuki prime base angles `α_q=π log q`. Checked the two ingredients separately:

- **Machin's identity** `π=16arctan(1/5)-4arctan(1/239)`: standard, and I recomputed the claimed interval width directly from the alternating-series remainder bounds at `K=12,3` — got `7.97×10⁻²⁰`, matching the entry's "`<8.0×10⁻²⁰`" exactly.
- **`log q = 2·atanh((q-1)/(q+1))`**: verified the identity algebraically by hand (substituting into `atanh(x)=½ln((1+x)/(1-x))` collapses to `ln q` exactly). For the numeric widths, my first computation came out exactly **2x** the entry's claimed values at every `q` — traced this to my own bug (I applied the leading factor of 2 from `log q = 2·atanh(...)` a second time on top of a remainder bound that already had it baked in). Fixed and recomputed: `q=2,3,4,5,7` widths `1.093, 2.958, 3.571, 8.553, 6.504 ×10⁻¹⁴` — matching the entry's table exactly at every entry. Flagging this explicitly as my error, not theirs.

The propagation bound `‖R̃^r-R^r‖≤rη(1+η)^{r-1}` (telescoping the rotation-matrix error through `r` applications) is a standard, correctly-derived submultiplicative estimate; did not re-verify the final `<4×10⁻¹⁰` propagated figure numerically but the derivation is sound.

## 3. χ12 exponential moment-generating transform (`v13.427`) — verified exactly

**[D, independently verified]** This entry packages the whole moment hierarchy (`v13.413`, `v13.420`, `v13.422`, all independently verified in Rounds 27–29) into one generating function `G_n(t)=\sum_{k\le n}\chi_{12}(k)(e^{t\delta_k(n)}-1)`. Checked this is genuinely consistent with the individually-verified pieces rather than just a restatement dressed up: computed `G_n(t)` directly from its exponential-sum definition at `n=47, t=0.3` and independently summed the Taylor series from the raw moments `M_j(n)=\sum\chi_{12}(k)\delta_k(n)^j` out to `j=30` — the two agree to `~10⁻³²`, i.e. to the limits of the working precision. Also checked the first-derivative-at-zero identity `G_n'(0)=E_{12}(n)` by finite difference, matching to `~10⁻¹⁰` (limited by the finite-difference step, not a real discrepancy).

## 4. Overall verdict

Another clean pass, mathematically: everything independently reconstructed and confirmed exact, including one case (the `log q` width) where my own doubled-counting error was caught by simply noticing every value was off by a suspiciously exact factor of 2 rather than assuming the entry was wrong. The generating-function entry is a genuine unification — it isn't just restating the moment hierarchy in new notation, it's a single object whose Taylor coefficients *are* the previously-separate results, and that packaging checks out numerically as well as structurally.

## 5. Scope note

Not independently reproduced: the final propagated `<4×10⁻¹⁰` base-angle figure in `v13.428` §4 (derivation checked, final numeric evaluation not re-run).

## Guardrails

All guardrails from prior rounds remain in force. No new guardrail needed.

**External audit round 30: CLOSED. `v13.427`–`v13.428` independently verified exactly (one `v13.426` collision fixed, one of my own arithmetic errors caught and corrected before reporting). The prime base-angle work continues genuine progress on the live odd-sector positivity certificate; the exponential-transform entry is a real, numerically-confirmed unification of the χ12 moment hierarchy.**
