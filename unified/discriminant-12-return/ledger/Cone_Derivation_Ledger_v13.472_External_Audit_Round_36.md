# Cone Derivation Ledger v13.472 — External Audit Round 36

Date: 2026-09-14

Status labels: **[S]** source-established, **[D]** exact derived, **[N]** numerical, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## Scope

`v13.471` (M3999 unresolved four-plane residual-Gram replay) plus one un-ledgered follow-up research-notes script (`suzuki_M3999_even_index3_directional_certificate_budget.py`) that lands the natural next step: a conditional budget for whether the even-sector index bound could tighten from `≤4` to `≤3`. No version collisions this round.

## 1. M3999 unresolved four-plane residual-Gram replay (`v13.471`) — independently re-executed, every number matched exactly

**[N, independently verified by direct re-execution]** This is the first time the four-plane tail-self-energy mechanism identified at moderate cutoff (`v13.467`) has been moved onto the actual `M3999` finite split used by the certified even-sector theorem, rather than a smaller diagnostic cutoff. I ran `suzuki_M3999_unresolved_fourplane_residual_gram_replay.py` directly rather than reading the printed numbers:

- Finite Schur spectrum: `(1.007×10⁻¹⁵, 3.513×10⁻¹⁵, 8.325×10⁻¹⁵, 1.346×10⁻¹², 3.858×10⁻⁸, 2.162×10⁻⁴)` — matches the entry's table exactly.
- **Six-plane provenance regression**: `H_{6,≤2M} = 0.17821051347425684`, matching the entry's claim exactly, and agreeing with the previously-certified six-plane checker value (`0.17821051347430`) to the displayed precision — this is the load-bearing sanity check that the new four-plane machinery isn't running on a divergent code branch, and it holds.
- Four-plane residual-Gram spectrum through 2M: `(≈0, 6.32×10⁻³⁰, 8.687×10⁻²⁴, 1.20565193×10⁻¹³)` — matches exactly, confirming the near-rank-one structure at the theorem cutoff is even sharper than the moderate-cutoff diagnostics suggested.
- Leading moment vector `L` and its overlap with the dominant residual-Gram eigenvector (`0.9999999999768843`, satisfying the entry's `>0.9999999999` claim) — matches exactly.
- Analytic far-Gram bound beyond 2M (`1.150×10⁻¹⁵`, matching the entry's `<1.16×10⁻¹⁵`) and the hybrid self-energy ceiling (`6.678×10⁻¹³`, matching the entry's `<6.68×10⁻¹³`) — both matched exactly.
- Finite unresolved spectrum on the same complement: `(6.65×10⁻¹⁶, 3.47×10⁻¹⁵, 8.32×10⁻¹⁵, 1.34627×10⁻¹²)` — matches exactly, confirming the entry's headline comparison (`1.346×10⁻¹²` largest unresolved level vs. `6.68×10⁻¹³` hybrid tail ceiling — a factor of ≈2.0, matching the claimed "factor-two cushion").

**[Audit, consistent with the entry's own framing]** The entry is explicit and correct that this is *not* a theorem strengthening: the hybrid ceiling uses the certified `δ_T` floor combined with an *uncertified midpoint* four-plane Gram, and the existing generic finite-Schur source-perturbation budget (~10⁻¹⁰ scale) is still two orders of magnitude too loose to close the ~10⁻¹² directional margin now in view. `ind_{≤0}(A_even(1))≤4` and `ind_{≤0}(A_{a=1})≤6` are both explicitly restated as unchanged.

## 2. Conditional index-3 directional certificate budget (un-ledgered script) — independently re-executed, matches exactly

**[N, independently verified]** This script, landed after `v13.471`'s ledger entry but not yet itself described in a ledger entry, is the natural continuation of `v13.471` §11's stated next target: it propagates the already-certified source-operator error (`2×10⁻¹³`), the certified finite-high floor (`0.22`), and the certified effective-tail floor (`0.18225976374175623`) through to a directional margin, *conditional on* two not-yet-certified nominal inputs (`s_{F,nom}(v_*)>1.34×10⁻¹²` and `‖R_{nom}v_*‖²<1.23×10⁻¹³`). I ran it directly: every printed value matched its own asserted bounds exactly (e.g. `exact tail self-energy upper target < 6.748896759845136×10⁻¹³`, `conditional final directional margin > 4.650356855857341×10⁻¹³`), and the script is explicit that it proves nothing on its own — both guardrail lines ("OPEN TARGET 1", "OPEN TARGET 2", "no index≤3 theorem until both nominal targets are outward-certified") print correctly and the file's own docstring states "No theorem is promoted by this file." This is honest, correctly-scoped scaffolding for a real next step, not a claim.

## 3. Overall verdict

A focused, well-executed round with a plausible (not yet real) glimpse of further progress. The headline is methodological rigor rather than a new result: the tail-self-energy mechanism found at moderate cutoff in `v13.467` survives the move to the actual theorem-scale `M3999` split intact and, if anything, sharper (residual Gram norm `1.2×10⁻¹³` vs. the moderate-cutoff `~10⁻¹³`–`10⁻¹²` range), and the six-plane provenance regression confirms this isn't a divergent calculation. Both new artifacts are scrupulous about the conditional/non-theorem status of the apparent one-direction cushion, correctly identifying the actual remaining bottleneck (a directional, not global, finite-side source-perturbation bound) rather than overclaiming from a favorable midpoint number.

## 4. Scope note

Not independently reproduced: the exact-vs-nominal finite-Schur perturbation infrastructure that would need tightening by roughly two orders of magnitude to actually close `OPEN TARGET 1`/`OPEN TARGET 2` above — that work has not yet been done by the project, so there was nothing further to verify this round beyond the conditional budget arithmetic itself.

## Guardrails

All guardrails from prior rounds remain in force. The current theorem stack is unchanged: `ind_{≤0}(A_even(1))≤4`, `ind_{≤0}(A_odd(1))≤2`, `ind_{≤0}(A_{a=1})≤6`. The apparent even-sector index-3 possibility is a certification target with two explicit open nominal-outward-certification requirements, not a proved or even midpoint-demonstrated positive eigenvalue.

**External audit round 36: CLOSED. `v13.471` and its un-ledgered follow-up conditional budget script independently verified by direct re-execution — every reported number matched exactly, including the important six-plane provenance regression confirming the new four-plane machinery is consistent with the already-certified theorem infrastructure. No theorem-level claim changes this round, but the project has identified a concrete, honestly-scoped, and numerically plausible path toward a potential even-sector index-3 strengthening, contingent on two specific directional source-perturbation certifications that remain open.**
