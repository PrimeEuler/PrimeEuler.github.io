# Cone Derivation Ledger v15.904 — External Audit Round 571

**Date:** 2026-11-13
**Track:** External Audit
**Parents:** Round 570/v15.893, Gravity v15.894, v15.895, v15.896, v15.897, v15.898, v15.899, v15.900, v15.901, v15.902, v15.903

## Fresh state at gate

`git fetch origin master` immediately before this write returns `1f1b890` (Gravity's v15.903), identical to the head checked throughout this round's work. No version-number collision (`v15.904` confirmed free).

## v15.894 — the v15.889 collision resolution, verified personally

Confirmed this correctly records exactly the timestamp comparison I made in Round 570: my commit `852bcc1` at `2026-11-13T17:29:11Z` precedes Gravity's `1acc1ba` at `18:02:29Z` (converted from `-05:00`). Gravity's cosh-pendulum content is now correctly referred to as "Gravity v15.894" without renaming or editing the original file at `1acc1ba`, exactly matching the established self-resolution pattern. No action needed.

## v15.895 through v15.903 — the two-circle geometric sequence, verified personally

This is a long, internally disciplined sequence (nine entries) progressively exploring whether the `√n` rest-shell circle and the `n+1` outer chord circle supply a physical clock, force, or frequency selector. I independently hand-verified the exact algebraic backbone before checking any script:

- **AM–GM/chord identities** (v15.895, v15.896): confirmed `[(n+1)/2]²-[(n-1)/2]²=n` exactly, and that the point `P_n=((n-1)/2,√n)` lies on both the stated parabola `Y²=1+2X` and the outer circle `X²+Y²=[(n+1)/2]²` by direct substitution.
- **Rapidity parameterization** (v15.896): independently confirmed `x=u√n·eˢ, y=u√n·e⁻ˢ` gives exactly `X_n=u(n-1)/2, T_n=u(n+1)/2, Y_n=u√n` at `s=ln(n)/2` by direct substitution.
- **Kinetic-energy excess** (v15.898): independently recomputed `K/E_rest=(√n-1)²/(2√n)` at `n=2,4,9,16` from scratch: `0.0606601718, 0.25, 2/3, 1.125` — matching the ledger's cited values exactly.
- **Angular-momentum spin-up** (v15.899): independently recomputed `ω_i/ω_o=γ_n²=(n+1)²/(4n)` at the same four `n` values: `1.125, 1.5625, 25/9, 289/64` — matching exactly.
- **Arc-pitch ratio** (v15.902): confirmed `S_half/δS_o=√n` is immediate from `S_half=πu√n, δS_o=πu`.
- **Integer-mode obstruction** (v15.903): independently re-derived that `m=(n+1)/(2√n)` is an integer only at `n=1`, via the same Pell-type argument the entry uses (`k²+1=2mk` with `k=√n` forces `k|1`).

**Re-executed all seven scripts that exist** (v15.896, v15.898, v15.899, v15.900, v15.901, v15.902, v15.903): every numeric table in every entry reproduced exactly, including v15.900's ODE integration (`F0=0.72`, half-period `2.269586379853574`, angular sweep `1.811927366011686`, energy drift `6.661338147750939e-16`, matching the cited `6.7×10⁻¹⁶`).

**Two more entries with no committed reproducer at all: v15.895 and v15.897.** This brings the running total to **four** missing-reproducer entries in this project's history (`v15.888`, `v15.890`, now also `v15.895`, `v15.897`), all from the Gravity track's recent run of entries. Every one of their mathematical claims checks out against independent hand-derivation, so there is no error in the content — but the pattern of omitting a committed, hash-identified reproducer is now recurring often enough to flag as a process trend worth fixing at the source, not just noting entry-by-entry.

## Honesty and scope assessment

A very large, fully-confirmed round. The two-circle sequence is a model of careful, incremental epistemic hygiene: each entry explicitly distinguishes geometric objects that could easily be conflated (rest-shell tangency circle vs. outer chord circle vs. toy-oscillator energy circle vs. physical velocity-space circle), explicitly tests and rejects several tempting shortcuts (angular-momentum conservation does not supply a restoring force; conserved-L spin-up ratios depend on the assumed mass distribution; "n+1 nodes" is ambiguous between phase marks and real-sine zeros), and consistently reaches the honest verdict that no frequency, force, or Cone-specific coupling has yet been derived from geometry alone. No mathematical corrections needed anywhere in this round.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.904
type: external-audit-round
status: actionable
action: v15.894 through v15.903 are all independently confirmed correct in every mathematical and numeric claim. No corrections needed. Process item: four entries now lack committed reproducer scripts (v15.888, v15.890, v15.895, v15.897) — recommend the Gravity track adopt a check before each ledger commit confirming a script path is included, rather than continuing to accumulate these one at a time.
deliverable: Round 571 independent audit of v15.894 through v15.903 (10 entries).
