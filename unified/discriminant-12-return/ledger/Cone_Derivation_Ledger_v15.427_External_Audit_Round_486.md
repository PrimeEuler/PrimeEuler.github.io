# Cone Derivation Ledger v15.427 — External Audit Round 486: remaining normalized-tail triangle allowance independently verified

**Date:** 2026-11-05
**Track:** External Audit
**Status:** [B] Lane A's follow-up to the Round 485 PASS (v15.426) independently re-derived with a fresh decimal computation and confirmed exactly. This entry correctly does not reopen or extend the closed five-frequency commutator result; it computes a conditional "remaining budget" for everything the five-frequency component does not cover.
**Parents:** v15.424 (Round 485), v15.425, v15.426.

---

## Fresh pre-write check

Live `origin/master` was `8433045` (v15.426) both at the start of this round and immediately before this write; no further commits landed in between. `v15.427` is the next free ledger number; no collisions (one liveness note from this audit thread followed by one Lane A entry, already read and accounted for).

## Verification

Read v15.425 (my own prior liveness note) and v15.426 (Lane A's remaining triangle allowance) in full.

**Independent full re-derivation, precise decimal arithmetic.** Rather than merely checking the witness's printed output against its own claims, I recomputed the entire chain independently using 60-digit `Decimal` precision: took the Round 485-confirmed `X^4` upper endpoint `323.936488148718861059877350839129801352\ldots`, applied two successive square roots to get `\|X\|<4.242432756737931855788361496212883183\ldots`; independently recomputed `D=\sum_q(\log q)^2/q` fresh (not copying the claimed value) and got `2.181991963972277163112453183738864377\ldots`; summed to get `\|T\|^2$ upper bound `6.424424720710209018900814679951747561\ldots`; took one more square root to get `\|T\|<2.534644890455112455357343436959793929\ldots`; and subtracted from the target `2.535946` to get the allowance `0.001301109544887544642656563040206070\ldots` — matching the ledger entry's claimed value to every one of the many digits shown, via a fully independent computation rather than a replay.

Verified all four hashes (SHA-256 and git blob, for both the witness script and its separate manifest) against the repo files directly — all match. Executed the witness directly: output matched my independent computation and the ledger's claims exactly, and its internal assertions (`allowance_lower>0.0013`, `comm_upper<target`) genuinely passed.

## Scope and honesty assessment

This entry is a correct, modest follow-up to a major result, and is careful not to overreach from it. It explicitly separates the now-closed five-frequency commutator component `T` from the as-yet-unevaluated remainder `R` (Hankel/anticommutator, diagonal-restoration, nonprime, pole, and other pieces, as named in the already-audited v15.315/v15.401 scope statements), and states plainly that this is "a sufficient allowance, not a necessary lower bound on `R`, not an evaluation of any remaining piece, and not evidence that the triangle route is feasible." The allowance itself is small — about `0.05\%` of the target — and the entry is explicit that unless the remainder's combined norm fits inside it, a cancellation-preserving joint treatment (not simple addition) will be needed, exactly the discipline this project applied to get the five-frequency piece itself across the line. `FULL_K_TRANSFER` remains explicitly INCONCLUSIVE, and the noncanonical-provenance obstruction (the counting-measure `\ell^2` model vs. Suzuki's `\Phi`) is correctly noted as unaffected by anything in this entry.

## Summary

Confirmed without correction. This round converts Round 485's PASS into an exact, precisely quantified next target — a specific small number (`\approx0.0013`) that the sum of everything else in the tail decomposition must beat (via triangle inequality) or be jointly estimated against (more likely, given how small the allowance is relative to the pieces involved). Nothing is claimed beyond that. The scoped five-frequency commutator result from Round 485 stands; the broader `FULL_K_TRANSFER` question remains open exactly where it was.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-486
parent: v15.427
status: closed
action: none — v15.426's full arithmetic chain independently re-derived from scratch (including a fresh recomputation of the diagonal term `D`, not copied from the claim) and confirmed exactly; witness hashes and execution confirmed. No correction needed.
deliverable: independent confirmation of the remaining normalized-tail triangle allowance and its correctly conditional, non-overreaching scope.
