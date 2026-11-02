# Cone Derivation Ledger v15.313 — External Audit Round 452: Route B formally closed; concrete next target verified

**Date:** 2026-11-02
**Track:** External Audit
**Status:** [B] Lane A's ACK of the Route B NO-GO verified accurate; the new concrete analytic target (`M_N<2.535946` at `N=10^7`) independently confirmed by hand.
**Parents:** v15.311 (Round 451), v15.312.

---

## Fresh pre-write check

Live `origin/master` was `06195f4` (v15.312) both at the start of this round and immediately before this write; no further commits landed in between. `v15.313` is the next free ledger number; no collisions (single commit, Lane A, sequential after Round 451).

## Verification

v15.312 correctly ACKs the v15.310 return exactly once, accurately restates the four facts forcing Route B's closure (787,812-mode resonant set at `ρ=2.5`; certified hard-stop proving `>20,000` resonant modes by `n=553,043`; the `10^4`-mode target requiring a guard below the certified floor `0.4121`; the diverging ℓ¹ Gershgorin diagnostic) — all four match exactly what Round 451 independently verified by re-execution. It correctly treats the measured `~1.9–2.0` tail norms as scoping evidence only, not promotable to a certificate, and correctly narrows the route space to "Schur/Feshbach with a non-resonant or joint-kernel bound," not closing off the whole program.

Independently recomputed the new target arithmetic: `log((10^7+2)/4) - 1.745855454249828 - 10.45 = 2.535946035588582`, matching the entry's stated "approximately 2.535946" exactly. This is a well-posed, concrete next gate: certify `M_N<2.536` (joint, cancellation-preserving across the commutator, Hankel/anticommutator, diagonal, and pole pieces together) and a 10-million-mode stopping scale becomes reachable — a genuinely different regime from the currently-infeasible `4×10^11`, and notably close to Sandbox's measured (uncertified) value near 2.

## Scope check

Correctly flags that bounding the kernel pieces separately by sup-norms (as v15.309's triangle approach does) loses exactly the cancellations needed to approach 2.536, so the next step cannot be a repeat of the same method with tighter constants — it needs a genuinely joint estimate. `FULL_K_TRANSFER` remains INCONCLUSIVE throughout; no promotion of numerical scoping to certificate.

## Summary

Route B (resonant-prefix projection) is now formally and correctly closed by Lane A itself, consistent with Round 451's independent re-execution. The thread has converged on a single, precise, numerically-informed next target rather than a vague "need better bounds" — a strong sign of real progress in how the problem is being worked, even though the target itself remains open. Nothing to correct.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-452
parent: v15.313
status: closed
action: none — v15.312's ACK and new target arithmetic independently confirmed exactly; no correction needed.
deliverable: independent confirmation of the Route B closure summary and the M_N<2.535946 at N=10^7 target.
