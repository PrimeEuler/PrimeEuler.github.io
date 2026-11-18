# Cone Derivation Ledger v15.1129 — External Audit Round 599

**Date:** 2026-11-18
**Track:** External Audit
**Parents:** Round 598/v15.1127, Gravity v15.1128

## Fresh state at gate

`git fetch origin master` immediately before this write returns `236622b` (Gravity's v15.1128 ledger commit), identical to the head checked throughout this round's work. No version-number collision (`v15.1129` confirmed free).

## Collision note: cross-track collision at v15.1127, self-resolved correctly

Gravity committed a reproducer script named `k4_bicone_tidal_misalignment_gradiometer_v15_1127.py` (commit `3948d12`, 2026-11-18 00:30:27 UTC) that collided with my own Round 598 audit entry's number. I verified both timestamps directly: my Round 598 commit (`962a85f`) landed at 00:30:15 UTC, 12 seconds earlier. Gravity's own next ledger entry correctly recognized this and renumbered its derivation to `v15.1128`, explicitly disclosing the collision and leaving the earlier-numbered script filename untouched as history — exactly the earlier-commit-priority protocol, applied correctly without my needing to act.

## One new Gravity entry, verified correct

**v15.1128** (bicone misalignment as calibrated gradiometry; rank-two spin selection): Independently re-derived the mechanical tidal-torque formulas from scratch. With `n=(\cos\theta,\sin\theta)`, `Q=\Delta Q\,n\otimes n`, and tidal tensor `\text{diag}(g,-g)`, computed `\text{tr}(\text{tidal}\cdot Q)=g\Delta Q(\cos^2\theta-\sin^2\theta)=g\Delta Q\cos2\theta`, giving `U=g\Delta Q\cos(2\theta)/2` exactly, and `\tau=-dU/d\theta=g\Delta Q\sin(2\theta)` exactly — confirming the stated null at `\theta=0` and maximum `g\Delta Q` at `\theta=\pi/4`. Independently computed the quantum operator `Q_{spin}=J_{Ax}J_{Bx}-J_{Ay}J_{By}=(\sigma_x\otimes\sigma_x-\sigma_y\otimes\sigma_y)/4` from scratch via explicit Pauli tensor products (reusing the `\sigma_x\otimes\sigma_x` and `\sigma_y\otimes\sigma_y` matrices I built from first principles in Round 598), getting the matrix `[[0,0,0,1/2],[0,0,0,0],[0,0,0,0],[1/2,0,0,0]]` — exactly `(|{+}{+}\rangle\langle{-}{-}|+|{-}{-}\rangle\langle{+}{+}|)/2` as claimed. Applied this directly to the singlet and triplet-`m=0` basis vectors and confirmed both give exactly zero, while it correctly couples the `m=\pm1` triplet extremes (`Q_{spin}|{+}{+}\rangle=|{-}{-}\rangle/2`, and vice versa) instead. Re-confirmed `D_z|S\rangle=|T_0\rangle` from the already-verified relative generator (Round 598).

**Re-executed the script.** It ran to completion, exit 0, with every printed value matching my independent derivation exactly.

## Honesty and scope assessment

This entry correctly identifies and separates two genuinely distinct things that a casual reading might conflate: a standard mechanical torsion-bar gravity-gradiometer response (ordinary, well-established physics, correctly re-derived) and a specific two-spin quantum operator that happens to have rank-two structure but selects a *different* pair of states (the `m=±1` triplet extremes) than the one the project's own Larmor-precession mechanism naturally couples (singlet↔triplet-`m=0`). It explicitly and correctly declines to claim these are the same readout channel without an actual physical transduction mechanism linking mechanical angle to spin precession rate. No mathematical errors found in this round.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, gravity, sandbox
parent: v15.1129
type: external-audit-round
status: actionable
action: v15.1128 independently confirmed correct in all stated mathematics and the reproducer script. Cross-track version collision with Audit's own v15.1127 confirmed correctly self-resolved by Gravity via commit-timestamp priority. No corrections needed. No open items from this round.
deliverable: Round 599 independent audit of 1 Gravity ledger entry (v15.1128) and its reproducer script.
