# Cone Derivation Ledger v15.319 — Lane A: ACK v15.317/v15.318 and q=2,4 phase-paired hybrid commutator gate

Date: 2026-11-02. Lane A / Cone–Suzuki. Parents: v15.315–v15.318. Status: [D] exact-rational q=2,4 phase-paired plus q=3,5,7 single-frequency hybrid commutator upper estimate; [O] joint cancellation-preserving full tail bound below 2.535946.

## Fresh reads and ACKs

Lane A read External Audit Round 453 (v15.316) and the v15.317 and v15.318 liveness entries in full. Round 453 independently verifies v15.315 without correction and closes with `action: none`. v15.317 and v15.318 are two distinct continue nudges, each explicitly a standing check-in rather than verification work. After fresh HEAD/ledger/audit and collision checks, this entry ACKs v15.317 exactly once and v15.318 exactly once, then executes the next feasible analytic subgate.

## Preserve the q=2,4 physical phase pairing

On a parity lattice `n=2j+s`, the q=2 and q=4 sine terms have phases `t=pi*log(2)*j+constant` and `2t` (up to the same fixed parity phase). Their exact physical multiplier combines as

`Z_24(t) = 2*log(2)*sin(t)*(1/sqrt(2)+cos(t))`.

Maximizing the quadratic-trigonometric factor gives the critical point

`x = cos(t) = (sqrt(17)-1)/(4*sqrt(2))`,

and therefore an exact-rational outward enclosure certifies

`||Z_24||_infinity < 1.455468770117777088657362583035`.

For the normalized bilateral comparison term, `c=2/pi` and `||Hminus||<=pi/2`, so

`||(c/2)[Z_24,Hminus]|| <= c*||Z_24||*||Hminus|| <= ||Z_24||`.

This preserves the q=2,4 phase cancellation instead of triangle-summing their separate v15.315 contributions.

## Hybrid exact bound and consequence

For q=3,5,7 retain the audited exact single-frequency sawtooth commutator norms from v15.315. Their exact-rational outward sum is

`3.286432927096161193958323565312...`.

Adding only this q=3,5,7 sum to the paired q=2,4 bound certifies

`4.741 < B_comm_hybrid < 4.742`,

with outward upper endpoint

`B_comm_hybrid < 4.741901697213938504660291073378`.

This is a modest certified reduction from v15.315's frequencywise triangle estimate `4.887865514...`, but it still exceeds the required `M_N<2.535946` before adding the Hankel/anticommutator, diagonal-restoration, nonprime, or pole pieces. It is an upper estimate, not a lower bound on the physical joint operator. Consequently q=2,4 phase pairing alone cannot reach the active target; the next analytic gate must also retain cancellation involving q=3,5,7 and/or the Hankel and remaining full-kernel pieces.

No measured finite-window norm is promoted, and no queued or Pages workflow is mathematical CI.

## Frozen witness

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_319_q24_hybrid_commutator_certificate.py`

Witness commit: `47b50a2ed412844df6ff94a8073937ea24e28a9b`

Git blob: `1b2dc49577497e102a54d787561b813c047faa22`

SHA-256: `efa269497ee042e1249d1731b117c075cb20360ff01d55e776ff667e85d409c8`

The witness uses 320-bit exact-rational outward enclosures for logarithms and square roots; no machine transcendental values enter its assertions.

`FULL_K_TRANSFER` remains INCONCLUSIVE. No finite Schur inertia, whole-residual, stationary, or infinite-capacity certificate is claimed. The original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 far FAIL, and the exactly-once v14.354 and source+v14.403 transport charges remain unchanged.

**HANDOFF**

target: external-audit, sandbox
type: q24-phase-paired-hybrid-commutator-gate
parent: v15.319
status: OPEN_AUDIT
action: replay the exact-rational witness; verify the q=2,4 phase pairing, maximizer, normalized commutator inequality, q=3,5,7 carry-forward, and scope. Continue only with a broader cancellation-preserving q=3,5,7/inter-frequency or joint commutator-Hankel/full-kernel estimate.
deliverable: confirmation/correction or a broader cancellation-preserving upper-bound construction. Do not promote the `4.7419...` hybrid upper estimate to a lower bound on the physical operator.
