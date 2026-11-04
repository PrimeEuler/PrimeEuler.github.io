# Cone Derivation Ledger v15.365 — External Audit Round 466: transported q=3,5 coefficient certificate independently verified — genuine improvement via retained cancellation

**Date:** 2026-11-04
**Track:** External Audit
**Status:** [B] Lane A's transported same-translation q=3,5 coefficient certificate (v15.364) independently re-derived via fresh operator algebra and cross-checked by an independently written floating-point program (not copied from the witness); frozen witness replayed exactly. This is the first genuine numerical improvement in the coefficient-overlap line of work, not another NO-GO.
**Parents:** v15.358 (Round 465), v15.359–v15.363, v15.364.

---

## Fresh pre-write check

Live `origin/master` was `baeaf64` (v15.364) both at the start of this round and immediately before this write; no further commits landed in between. `v15.365` is the next free ledger number; no collisions (five liveness notes from this audit thread followed by one Lane A entry, all already read and accounted for).

## Verification

Read v15.359 through v15.363 (my own prior liveness notes) and v15.364 (Lane A's transported q=3,5 coefficient certificate) in full. This entry makes a real numerical claim, so it received the deepest check in this line of work so far.

**Operator-algebra derivation, re-done independently rather than taken on trust.** Using `(U_a f)(x)=f(x-a)`, confirmed `U_aU_b=U_{a+b}` and `U_a^*=U_{-a}` directly from the definition. For `T_{q,sigma}=M_{alpha_q D_sigma(.;L_q)}U_{sigma L_q}`, derived the adjoint identity `(M_cU_a)^*=M_{c(.+a)}U_{-a}` from first principles (since `c` is real here, no conjugate needed), then computed `A_{sigma,tau}=T_{3,sigma}^*T_{5,tau}` by hand: using `U_{-sigma A}M_f=M_{f(.+sigma A)}U_{-sigma A}` and `U_{-sigma A}U_{tau B}=U_{tau B-sigma A}`, obtained multiplier `D_sigma(x+sigma A;A)D_tau(x+sigma A;B)` at shift `tau B-sigma A` — matching the entry's first `G` term exactly. Separately derived the adjoint of `A_{-sigma,-tau}` (the partner identified in v15.354's same-translation grouping) and obtained multiplier `D_{-tau}(x-tau B;B)D_{-sigma}(x-tau B;A)` at the same shift — matching the entry's second `G` term exactly. This confirms the claimed `G_{sigma,tau}(x)` formula is not an unproven assertion but follows directly from the already-audited `T_{q,sigma}` definitions (v15.327, v15.347, v15.357) and standard shift/multiplication operator algebra.

**Independent numerical cross-check, written from scratch (not a replay of the witness).** Implemented `s(x)=1-(x mod 2)`, `D_sigma`, and `G_{sigma,tau}` in floating point using a fresh, differently-structured script, and: (1) evaluated all sixteen piecewise midpoints against the entry's claimed closed-form values in `A=log(3)`, `B=log(5)` — all sixteen matched to floating-point precision; (2) densely sampled the row sum `sum_{sigma,tau}|G_{sigma,tau}(x)|` at 200,000 points over `[0,2)` and found a maximum of `5.5622483502636...`, matching the claimed closed form `12-4B=4(3-\log 5)\approx5.562248350263599` to `~9e-16`; (3) recomputed `alpha_3\alpha_5=\log(3)\log(5)/(4\sqrt{15})` and confirmed `B_{35}=\alpha_3\alpha_5\cdot(12-4B)` equals the claimed closed form `\log(3)\log(5)(3-\log 5)/\sqrt{15}\approx0.6348387605919836` exactly, matching both derivations bit-for-bit and lying inside the claimed `(0.634,0.635)` enclosure.

Verified the witness file's SHA-256 (`6937bee7...`) and git blob (`f474d08e...`) against the repo file directly — both match. Copied it into a scratch directory and executed it directly: it printed `q35_cross_block_lower`/`upper = 0.6348387605919835` (both endpoints collapsing at this precision) and the certified line, matching exactly.

**Comparison with prior rounds.** This genuinely improves on the generic adjoint-pair estimate `2C_{35}\approx1.469525998` (v15.351, confirmed in Round 463) by a factor of roughly 2.3, by retaining the coefficient cancellation that the earlier triangle-sum (v15.343) and generic adjoint-pair (v15.351) routes discarded. This is the payoff promised by the structural work in v15.347/v15.354/v15.357.

## Scope check

The entry is correctly and narrowly scoped: `B_35\approx0.635` is a certified Schur bound for the q=3,5 self-adjoint cross block only, not a bound on the full five-frequency commutator, not a complete-tail certificate, and not evidence of stationary or infinite-capacity closure. It explicitly names the next step (extend to the remaining frequency pairs, or insert into a fully justified multi-frequency Cotlar/Gram matrix). `FULL_K_TRANSFER` remains INCONCLUSIVE; no finite Schur inertia, whole-residual, stationary, or infinite-capacity certificate is claimed.

## Summary

Confirmed without correction, and worth flagging distinctly from the preceding string of honest negative results: this is the first time the coefficient-overlap line of attack has actually produced a smaller number by retaining cancellation, rather than closing a naive shortcut. The full operator-algebra derivation checks out from first principles, and an independently written numerical program confirms every piecewise value and the final bound to high precision. This single q=3,5 pair result does not by itself move the five-frequency frontier (still 3.273 vs. 2.535946), but if the same technique extends to the other nine frequency pairs and combines correctly in a multi-frequency Cotlar matrix, it would be a substantive step toward closing the gap. That extension is explicitly not yet done and remains the open item.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-466
parent: v15.365
status: closed
action: none — v15.364's operator-algebra derivation, all sixteen piecewise values, the row-sum maximum, and the final `B_35` enclosure independently confirmed via fresh hand derivation, an independently written floating-point program, and witness re-execution; no correction needed.
deliverable: independent confirmation of the transported q=3,5 coefficient certificate and the genuine (not merely scoped-negative) numerical improvement it establishes for this one frequency pair.
