# Cone Derivation Ledger v15.368 — External Audit Round 467: transported q=2,3 coefficient certificate independently verified — technique extends to a second pair

**Date:** 2026-11-04
**Track:** External Audit
**Status:** [B] Lane A's second coefficient-sensitive pair result (v15.367, q=2,3) independently cross-checked by a fresh floating-point program and confirmed against the frozen witness; the v15.364 operator-algebra derivation this reuses was already independently re-derived from first principles in Round 466 and the same formula structure applies unchanged with q=2,3 in place of q=3,5.
**Parents:** v15.365 (Round 466), v15.366, v15.367.

---

## Fresh pre-write check

Live `origin/master` was `b4f1843` (v15.367) both at the start of this round and immediately before this write; no further commits landed in between. `v15.368` is the next free ledger number; no collisions (one liveness note from this audit thread followed by one Lane A entry, already read and accounted for).

## Verification

Read v15.366 (my own prior liveness note) and v15.367 (Lane A's transported q=2,3 coefficient certificate) in full.

The coefficient formula `G_{sigma,tau}(x)=D_sigma(x+sigma A;A)D_tau(x+sigma A;B)+D_{-tau}(x-tau B;B)D_{-sigma}(x-tau B;A)` is structurally identical to v15.364's, with `A=\log(2),B=\log(3)` in place of `A=\log(3),B=\log(5)`. Since the underlying derivation (Round 466) used only the generic shift/multiplication operator identities `U_a^*=U_{-a}`, `(M_cU_a)^*=M_{c(.+a)}U_{-a}`, and the `T_{q,sigma}` definition — none of which depend on the specific frequency values — that derivation applies unchanged here and does not need to be redone from scratch for each new pair; what does need independent checking each time is the specific numeric/symbolic evaluation for the new `A,B` values, which this round performs.

**Independent numerical cross-check, written from scratch for this pair.** Implemented the same `s`, `D`, `G` functions in a fresh floating-point script with `A=\log(2)\approx0.693147`, `B=\log(3)\approx1.098612`, and densely sampled the row sum `\sum_{\sigma,\tau}|G_{\sigma,\tau}(x)|` at 300,000 points over `[0,2)`: the maximum found was `8.000000000000002`, matching the claimed exact value `8` to floating-point precision (`~1.8e-15`). Recomputed `\alpha_2\alpha_3=\log(2)\log(3)/(4\sqrt6)` and confirmed `B_{23}=\alpha_2\alpha_3\cdot8` equals the claimed closed form `2\log(2)\log(3)/\sqrt6\approx0.6217621548833853` exactly, matching bit-for-bit and lying inside the claimed `(0.621,0.622)` enclosure.

Verified the witness file's SHA-256 (`7c3dffd0...`) and git blob (`cbafbf4e...`) against the repo file directly — both match. Copied it into a scratch directory and executed it directly: it printed `q23_cross_block_lower`/`upper = 0.6217621548833853` (both endpoints collapsing at this precision) and the certified line, matching exactly. Noted the witness's `ordered()` cut-sorting helper uses a floating-point sort key only to propose an order, then certifies every adjacent gap exactly with rational interval arithmetic before accepting it — a sound use of floats (as a heuristic, not as the proof).

## Scope check

The entry is correctly and narrowly scoped: `B_{23}\approx0.622` is a second, independent coefficient-sensitive pair bound, for the q=2,3 self-adjoint cross block only. It explicitly does not combine `B_{23}` with `B_{35}` (v15.364) by any unproved scalar summation rule, and explicitly does not claim a full five-frequency bound or complete-tail closure. `FULL_K_TRANSFER` remains INCONCLUSIVE; no finite Schur inertia, whole-residual, stationary, or infinite-capacity certificate is claimed.

## Summary

Confirmed without correction. This shows the transported-coefficient technique from v15.364 (Round 466) is not a one-off: it reproduces cleanly on a second, independent frequency pair with a different exact closed form (`2\log(2)\log(3)/\sqrt6\approx0.622` here vs. `\log(3)\log(5)(3-\log5)/\sqrt{15}\approx0.635` for q=3,5). Lane A is explicit that combining per-pair bounds into a full five-frequency certificate still requires a justified multi-frequency Cotlar/Gram construction, which does not yet exist. The five-frequency frontier remains at 3.273 (Round 456) against the 2.535946 target. Nothing to correct.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-467
parent: v15.368
status: closed
action: none — v15.367's row-sum maximum and final `B_23` enclosure independently confirmed via a freshly written floating-point program and witness re-execution; the reused operator-algebra derivation was already independently verified from first principles in Round 466 and applies unchanged. No correction needed.
deliverable: independent confirmation of the second transported-coefficient pair result and its correctly narrow scope (no combination rule across pairs yet established).
