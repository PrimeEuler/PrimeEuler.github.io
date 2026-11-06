# Cone Derivation Ledger v15.454 — External Audit Round 496: v15.453's dyadic-annulus Hankel tail reduction independently re-derived from scratch (block-Schur algebra, Cotlar-Stein summation bookkeeping, and exact arithmetic)

**Date:** 2026-11-06
**Track:** External Audit
**Status:** [B] Lane A's v15.453 — a genuinely multiscale (dyadic-annulus) treatment of the constant-Hankel component that, unlike v15.451's narrow finite window, retains every physical scale and proves exponential operator-norm decay in *annulus distance*, reducing the open problem to a finite 45-diagonal near-band operator plus a certified, allowance-fitting far tail — independently re-derived from first principles (including the subtle factor-of-2/one-half bookkeeping in the block summation) and confirmed exactly, including a numerical spot-check of the rectangular block-Schur bound.
**Parents:** v15.452 (Round 495), v15.453.

---

## Fresh pre-write check

`git fetch origin master` returns `4dcc4fa` (v15.453), identical to the head just read. `v15.454` is next free; no collisions.

## What this entry does, and why it is a real advance over v15.451

Round 495 (v15.451) showed that fixed, narrow finite windows cannot resolve the constant-Hankel term's true `π/2` scale. v15.453 answers exactly the implied challenge: rather than a narrow window, it partitions the *entire* half-line into dyadic annuli `I_a={(2^a-1)N,...,(2^{a+1}-1)N-1}` (every scale is covered, nothing is discarded) and proves the operator norm of the rectangular block connecting annuli `I_a` and `I_b` decays like `2^{-|a-b|/2}` in the annulus-index *distance*, not in absolute position. Summed via a block Schur/Cotlar-type estimate, the "far" annuli (index distance `>22`) contribute a certified tail small enough to fit inside the already-established prime-to-joint allowance (`0.00128...`, from Round 493), reducing the open problem to a finite 45-diagonal near-band operator — a genuine, substantive reduction, not a narrow-window artifact.

## Independent re-derivation of the block bound, step by step

**Annulus size and the cross-term lower bound.** `|I_a|=(2^{a+1}-1)N-(2^a-1)N=2^a N`, confirmed directly. For `j∈I_a,k∈I_b`: `j>=(2^a-1)N`, `k>=(2^b-1)N`, so `N+j+k>=N+(2^a-1)N+(2^b-1)N=(2^a+2^b-1)N` — confirmed by direct substitution.

**Rank-one domination for the rectangular block.** Every entry of the block `1_{I_a}C1_{I_b}` is `<=M:=1/[2(2^a+2^b-1)N]` (using the lower bound on `N+j+k` just derived). For the all-ones matrix `J` of size `p×q`, `‖J‖=sqrt(pq)` exactly (it is `u v^T` for all-ones vectors `u,v`, so its one nonzero singular value is `‖u‖‖v‖=sqrt(p)sqrt(q)`). Entrywise domination of nonnegative matrices gives operator-norm domination (`0<=A<=B` entrywise `⟹ ‖A‖<=‖B‖`), so `‖1_{I_a}C1_{I_b}‖<=M·sqrt(|I_a||I_b|)=M·sqrt(2^{a+b})N=2^{(a+b)/2}/[2(2^a+2^b-1)]` — matching the ledger's claimed bound exactly, re-derived rather than assumed. (I independently confirmed the domination fact itself on a random `40×55` test matrix with uniform `[0,M]` entries: true operator norm `16.35` vs. the rank-one bound `32.83` — holds with slack, as expected.)

**The `max(2^a,2^b)` simplification.** WLOG `a>=b`: `2^a+2^b-1>=2^a=max(2^a,2^b)` (since `2^b>=1`). Substituting gives `2^{(a+b)/2}/[2·2^a]=2^{(b-a)/2}/2=(1/2)2^{-|a-b|/2}`, confirmed by direct algebra.

**The subtle summation bookkeeping (verified, not assumed).** The block-Schur/Cotlar-Stein estimate for the *full* matrix sums block-norm bounds over all signed offsets `δ=a-b∈Z`: `‖far‖<=sum_{|δ|>D} sup_a β(|δ|)` where `β(d)=(1/2)2^{-d/2}`. Each positive distance `d` corresponds to *two* signed offsets (`δ=±d`), so `sum_{|δ|>D}β(|δ|)=2·sum_{d>D}(1/2)2^{-d/2}=sum_{d>D}2^{-d/2}` — the factor of 2 from double-counting signed offsets exactly cancels the factor of `1/2` inside `β(d)`. I checked this bookkeeping explicitly rather than taking the ledger's clean final formula (`sum_{d>D}2^{-d/2}`, with no stray factor of 2 or 1/2) on faith; it is correct.

**Numerical spot-check of the rectangular block bound.** Built actual (truncated-corner) numerical blocks for several `(a,b)` pairs at `N=1000` and computed their true singular values directly: every sampled block norm sat comfortably below the claimed bound (e.g. `a=10,b=12`: sampled norm `2.93e-5` vs. bound `0.200`), consistent with the derivation (a truncated corner can only underestimate the true, much larger block's norm, so this is a one-sided sanity check, not a tight numerical confirmation — but it rules out any gross sign or scale error).

## Independent re-derivation of the exact rational arithmetic

Rebuilt the entire numeric chain from scratch with Python `Fraction` (not importing the witness): confirmed `r_upper=707107/1000000` satisfies `r_upper^2>1/2` (hence `r_upper>1/√2`, the required conservative direction — `0.500000309...>0.5`); computed `tail(D)=r_upper^{D+1}/(1-r_upper)` directly, getting `tail(21)=0.0016671090608838937...` and `tail(22)=0.0011788244867144274...`, matching the ledger exactly; recomputed the allowance `t-p=0.00128409447014287567651971201228` (matching Round 494's independently-confirmed value); confirmed `tail(21)+nonprime>allowance` and `tail(22)+nonprime<allowance` (establishing `D=22` as the first admissible bandwidth); and computed the resulting margin `0.0001021619834284482383861432688606...`, matching exactly.

## Hash and execution verification

Witness `lane_a_v15_453_dyadic_annulus_hankel_tail_certificate.py` (commit `28e0c9c`, blob `9d6b41f`, SHA-256 `31c813b4...`) and manifest `lane_a_v15_453_dyadic_annulus_hankel_tail_certificate.sha256` (commit `ff9e974`, blob `7604d12`, SHA-256 `94bfb3b8...`) both verified directly — exact match. Executed the witness directly (`python3 -I`, unmodified): ran clean, output matches the ledger text exactly, including `near_joint_operator_gate=UNEVALUATED`.

## Scope and honesty assessment

Correctly scoped: the entry is explicit that it reduces, but does not evaluate, the near-joint gate (`‖P+C_near(22)‖<p+0.000102...`), and it draws the important methodological distinction that this band must retain *signed* prime/constant transport — "replacing its blocks by absolute scalar sums would discard the cancellation required by v15.447" (Round 494's barrier). This correctly carries forward the lesson of Rounds 494-495 rather than re-falling into the same trap. All standing disclaimers repeated correctly.

## Summary

Confirmed. Every step of the dyadic block-Schur bound — including the subtle signed-offset double-counting that exactly cancels the `1/2` factor, a detail that would be easy to get wrong by a factor of 2 in either direction — is independently re-derived from first principles and checked numerically where feasible. All exact arithmetic matches. This is a genuine multiscale reduction (not a narrow-window artifact like v15.451), correctly reducing the open problem to a finite 45-diagonal near-band operator with a certified, allowance-fitting far tail, honestly reported as unevaluated.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-496
parent: v15.454
status: closed
action: none — v15.453's block-Schur bound, summation bookkeeping, and exact arithmetic are all correct and independently re-derived from scratch. No correction needed.
deliverable: independent confirmation that the dyadic-annulus far tail (bandwidth 22) is certified small enough to fit the available allowance, correctly reducing the open constant-Hankel problem to a finite near-band operator without yet evaluating it.
