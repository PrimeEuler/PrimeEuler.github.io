# Cone Derivation Ledger v15.492 — additive correction to v15.491 common dyadic fiber

**Timestamp:** 2026-11-06 20:34 EST  
**Lane:** A (Cone/Suzuki), chosen-counting-measure five-frequency gate  
**Status:** v15.491 mathematical statement preserved; stripped equation markup corrected additively

## Correction

Post-write verification found that the equation backslashes in v15.491 were stripped by string escaping. This affected presentation, not the witness, hashes, replay, or mathematical claim. The frozen v15.491 ledger is not edited. The exact theorem is restated below using escape-free notation.

## Exact statement

For a ≥ 0, define:

- I_a = {(2^a − 1)N, …, (2^(a+1) − 1)N − 1}.
- n_a = |I_a| = 2^a N.
- E_(a,r) = [1 + r/n_a, 1 + (r+1)/n_a), for 0 ≤ r < n_a.
- V_a = span{sqrt(n_a) times the indicator of E_(a,r)} inside L2([1,2]).
- U_a e_r = sqrt(n_a) times the indicator of E_(a,r).

Then U_a is unitary from the locally reindexed ell2(I_a) onto V_a.

For d ≥ 0, define the refinement isometry by

J_(a,d)e_r = 2^(−d/2) times the sum of e_q over 2^d r ≤ q < 2^d(r+1).

Writing B_(a,d) for the unnormalized duplication matrix gives exactly:

- B_(a,d)^* B_(a,d) = 2^d I.
- J_(a,d)^* J_(a,d) = I.
- J_(a+d,e) J_(a,d) = J_(a,d+e).
- U_(a+d) J_(a,d) = U_a.

Therefore V_a is contained in V_(a+d). The projection J_(a,d)J_(a,d)^* is block averaging on each set of 2^d descendants, with every within-block entry equal to 2^(−d). The union of the V_a is dense in L2([1,2]).

The physical space decomposes exactly as the orthogonal direct sum over a of ell2(I_a). Hence W, the direct sum over a of U_a, is unitary onto the direct sum over a of V_a, viewed inside the direct sum over a of L2([1,2]).

For an arbitrary matrix block A_(a,b), define its step kernel on E_(a,r) times E_(b,s) by

k_(a,b)(x,y) = sqrt(n_a n_b) A_(a,b)(r,s).

Integration against U_b e_s gives exactly U_a(A_(a,b)e_s). Thus the kernel block equals U_a A_(a,b) U_b^*, not an approximation. The signs, prime phases, transported coefficients, and constant-Hankel entries are retained exactly. Consequently the finite 45-diagonal operator has exactly the same norm after this unitary common-fiber embedding.

## Frozen evidence and scope

The authoritative v15.491 witness remains:

- research-notes/lane_a_v15_491_common_dyadic_fiber.py
- witness commit 5f01751aa8e7581d7aff9b385d19291b80c4e1db
- witness blob 9fadebd1695d84ebc0f42d0fb55c481ad573d411
- witness SHA-256 43c915d153fda65b24227b53afda3a25d35e4a2f1db23c19339f92669e4ae788
- manifest commit 2525ec46c7e5b6cd993ca8021b5e3d19b27a470a
- manifest blob 6e09f38f10e48de90c348774880d77e9a328cbed
- manifest SHA-256 00bb74059f78a4b3599a36c79d165eaaba7ba2f6dc7ae009dc4e35d10bf983e8

This correction does not evaluate the signed 45-diagonal norm and does not construct the desired smaller scale-solenoid groupoid or continuous-field compression. It remains only the noncanonical chosen-counting-measure ell2 five-frequency commutator gate, not whole K or source-native Suzuki Phi. All frozen thresholds, charges, and prior certificates remain unchanged.

HANDOFF
target: external-audit, sandbox
type: additive-typesetting-correction
parent: v15.492
status: open
action: audit v15.491 using this escape-free theorem statement and the frozen v15.491 witness; do not infer a signed-gate pass or any full-K conclusion.
