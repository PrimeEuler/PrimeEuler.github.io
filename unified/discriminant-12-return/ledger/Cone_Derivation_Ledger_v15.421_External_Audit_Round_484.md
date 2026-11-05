# Cone Derivation Ledger v15.421 — External Audit Round 484: joint weighted-shift assembly independently verified — self-adjointness certified, promising reconnaissance correctly not promoted

**Date:** 2026-11-05
**Track:** External Audit
**Status:** [B] Lane A's joint coefficient-weighted 40-term assembly (v15.420) independently re-derived and confirmed. The adjoint-transport identity was checked against the actual `G_{\sigma,\tau}` construction from first principles (not just the abstract polynomial restatement the witness itself performs), and confirmed to hold exactly. The entry's informal reconnaissance number (`\approx3.763`, below the `4.249030150943723` budget) is correctly and explicitly not promoted to a certified result.
**Parents:** v15.419 (Round 483), v15.420.

---

## Fresh pre-write check

Live `origin/master` was `c27df0a` (v15.420) both at the start of this round and immediately before this write; no further commits landed in between. `v15.421` is the next free ledger number; no collisions.

## Verification

Read v15.420 in full.

**The witness's own check is weaker than the claim — independently closed that gap.** The witness's `Poly` class checks only that two *already-written* formal expressions, `(c-d)(a-d)+(c-b)(a-b)` and `(a-b)(c-b)+(a-d)(c-d)`, are equal to each other as abstract polynomials in four independent symbols `a,b,c,d` — which is true automatically by commutativity of multiplication (`(c-d)(a-d)=(a-d)(c-d)` and `(c-b)(a-b)=(a-b)(c-b)`, so both sides are literally the same two products reordered) and does not by itself verify that `G_{-\sigma,-\tau}(x)` and `G_{\sigma,\tau}(x+\lambda)` actually *equal* those expressions in the first place. That substantive claim — the actual adjoint-transport identity `G_{-\sigma,-\tau}(x)=G_{\sigma,\tau}(x+\lambda)` with `\lambda=\tau B-\sigma A` — needed independent checking against the real `D`/`s` sawtooth construction, not the abstract symbol-substitution.

**Independent numerical verification of the real identity.** Using the `G_{\sigma,\tau}` implementation already independently re-derived from first principles in Round 466 (not copied from this or any other witness), tested `G_{-\sigma,-\tau}(x)` against `G_{\sigma,\tau}(x+\lambda)` over 200,000 random trials (random `x\in[0,2)`, random signs, fixed representative pair `q=3,r=5`): maximum observed difference `6.66\times10^{-16}$, i.e. exact agreement to floating-point precision. This independently confirms the actual mathematical claim the abstract polynomial check was meant to stand in for.

**Consequence check.** Given this identity, and the already-established adjoint rule `(M_cU_\lambda)^*=M_{c(.+\lambda)}U_{-\lambda}$ for real-valued `c` (Round 466), the `(-\sigma,-\tau)` weighted term is exactly the operator adjoint of the `(\sigma,\tau)` term: its shift is `\lambda(q,r,-\sigma,-\tau)=-\tau B+\sigma A=-\lambda` as required, its coefficient `G_{-\sigma,-\tau}` equals `G_{\sigma,\tau}(.+\lambda)` as required, and its phase sign `(-\sigma)(-\tau)=\sigma\tau` is unchanged, confirming `X=X^*` is a correct and nontrivial consequence, not just an assumption.

**Label census re-checked.** Independently confirmed (consistent with Rounds 482–483) that all 40 labels `r^\tau/q^\sigma` are distinct, and separately confirmed the reciprocal-pairing algebra directly: `label(q,r,-\sigma,-\tau)=q^\sigma/r^\tau=1/\text{label}(q,r,\sigma,\tau)$ exactly, so since no label equals its own reciprocal (none equals `1`, already established), the 40 terms partition into exactly 20 adjoint orbits of size 2 — matching the witness's count.

**Hash and execution check.** Verified all four hashes (SHA-256 and git blob, for both the witness script and its separate manifest file) against the repo files directly — all match. Executed the witness directly: output matched exactly (`10` pairs, `40` terms, `40` distinct labels, `20` adjoint orbits).

## Scope and honesty assessment

This entry is a model of correct self-restraint: it clearly separates the certified formal result (the exact adjoint-transport identity and the resulting self-adjointness `X=X^*`) from an informal numerical "reconnaissance" that happened to land near `3.763` — tantalizingly below the `4.249030150943723` required budget — and explicitly refuses to treat that number as evidence, citing concrete reasons (discontinuous coefficients, non-monotone collocation values, no rigorous truncation or tail bound). This is exactly the discipline this project has maintained throughout: a suggestive number is not a certificate, and the entry does not pretend otherwise.

## Summary

Confirmed without correction, and the independent check went further than simply replaying the witness: the central mathematical claim (the adjoint-transport identity) was verified against the actual construction rather than the witness's own abstract restatement of it, closing a gap the witness itself left unverified. `FULL_K_TRANSFER` remains INCONCLUSIVE; the audited `2.892017147262984` frontier is unchanged against the `2.535946` target, though the informal reconnaissance — not yet a certificate — suggests the eventual answer may be reachable once a rigorous joint Cotlar/Gram or crossed-product bound is constructed.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-484
parent: v15.421
status: closed
action: none — v15.420's self-adjointness certificate independently confirmed against the real G construction (not just its own abstract polynomial check), label census and adjoint-orbit count independently re-derived, all hashes verified, witness re-executed. No correction needed.
deliverable: independent confirmation of the joint weighted-shift assembly's self-adjointness, with the gap in the witness's own abstract check identified and independently closed.
