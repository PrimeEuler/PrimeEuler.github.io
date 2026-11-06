# Cone Derivation Ledger v15.465 — External Audit Round 500: v15.464's doubling-endomorphism architecture correction independently verified

**Date:** 2026-11-06
**Track:** External Audit
**Status:** [B] Lane A's v15.464 — catching that the affine-doubling map `F` from Round 499 (v15.462) is conjugate to coordinatewise squaring on `T^4`, hence a 16-to-1 *noninvertible* endomorphism, not an automorphism, so the "obvious" ordinary `C(T^4)×_F Z` crossed-product construction implicitly invited by the earlier framing is simply unavailable — independently re-derived and confirmed both algebraically and numerically. A genuine, useful architecture correction that heads off an invalid construction before it's attempted.
**Parents:** v15.463 (Round 499), v15.464.

---

## Fresh pre-write check

`git fetch origin master` returns `330d22f` (v15.464), identical to the head just read. `v15.465` is next free; no collisions.

## What this entry catches, and why it matters

Round 499 confirmed `F(η)_p=ρ_pη_p^2` on `T^4` as the exact recursion linking the dyadic annulus scale to the four-torus phase hull. The natural next instinct — stated explicitly as the thing being headed off here — would be to build a `Z`-crossed-product `C(T^4)×_F Z` to get a covariant operator framework for the signed near-band gate. v15.464 shows this doesn't work: a group crossed product requires `F` to be a *homeomorphism* (invertible), but `F` is conjugate to pure coordinatewise squaring, a `16`-to-`1` map, so it is nowhere near invertible. Catching this now, before any operator construction is attempted on top of it, avoids wasted effort on a framework that was never going to be valid.

## Independent re-derivation of the conjugacy

Setting `w_p=ρ_pη_p`: `ρ_p F(η)_p=ρ_p(ρ_pη_p^2)=ρ_p^2η_p^2=(ρ_pη_p)^2=w_p^2`. So the "new" `w` (defined the same way from the updated `η`) equals the square of the "old" `w` — confirmed by direct substitution, exactly as claimed, showing `F` is conjugate via the affine shift `w=ρη` to `D(w)=w^2`.

## Independent re-derivation and numerical confirmation of the 16-fold covering

Each circle coordinate of `D(w)=w^2` is the standard 2-to-1 squaring map on the circle (every nonzero point has exactly two square roots, differing by a sign/half-turn), so on the product `T^4` the map has exactly `2^4=16` preimages per generic point — confirmed both algebraically (elementary) and with a fresh, independent numerical check: picked a random point on `T^4`, computed both square roots of each of its four circle coordinates directly, verified each one actually squares back to the target (`<1e-9` error), and confirmed all `16` sign-combinations give `16` genuinely distinct preimage points (no accidental coincidences). Also independently verified the conjugacy identity itself numerically for all four primes `p∈{2,3,5,7}` with an arbitrary test phase, matching to `<1e-9`.

## Assessment of the architectural conclusion

The claim that an ordinary `Z`-crossed product requires an automorphism (invertible dynamics), and that a genuinely noninvertible endomorphism instead needs either the natural-extension/inverse-limit solenoid construction or an endomorphism-correspondence framework (Cuntz–Pimsner/Exel-type crossed products by endomorphisms), is standard, well-established operator-algebra and topological-dynamics theory — these are exactly the recognized tools in the literature for covariant constructions over noninvertible maps, not an ad hoc or questionable substitution. The entry correctly identifies which of the two prior approaches (v15.462's framing) would have been invalid and why, without yet attempting either of the two valid alternatives.

## Hash and execution verification

Witness `lane_a_v15_464_doubling_endomorphism_certificate.py` (commit `072f3d9`, blob `5144c95`, SHA-256 `a1635c73...`) and manifest `lane_a_v15_464_doubling_endomorphism_certificate.sha256` (commit `c9b6f5b`, blob `62ba7f6`, SHA-256 `2b28d145...`) both verified directly — exact match. Executed the witness directly: ran clean, output matches the ledger exactly, including `joint_norm_gate=UNEVALUATED`.

## Scope and honesty assessment

Correctly scoped: explicitly labeled "this corrects the proof architecture only" and states plainly it "does not construct the lifted block operator or evaluate" the still-open gate. It also warns against a specific shortcut temptation — "discarding the inverse branches or pretending successive annulus phases are independently invertible" — naming exactly the kind of silent approximation that would need to be avoided in whatever construction comes next. This is a healthy, self-correcting step within Lane A's own chain, not an externally-forced correction.

## Summary

Confirmed. The conjugacy to coordinatewise squaring and the resulting 16-fold, noninvertible covering structure are both independently re-derived algebraically and confirmed numerically. This correctly rules out the "obvious" ordinary crossed-product approach before any operator construction was built on it, and correctly redirects toward the two standard valid frameworks for noninvertible dynamics, without claiming to have built either yet.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-500
parent: v15.465
status: closed
action: none — v15.464's conjugacy derivation, 16-fold covering-degree claim, and architectural conclusion are all correct and independently re-derived/confirmed. No correction needed.
deliverable: independent confirmation that the annulus/phase-hull doubling map is a noninvertible 16-to-1 endomorphism, correctly ruling out an ordinary Z-crossed-product construction before it is attempted, and correctly redirecting toward the natural-extension solenoid or an endomorphism correspondence.
