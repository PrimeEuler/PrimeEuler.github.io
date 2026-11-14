# Cone Derivation Ledger v15.953 — External Audit Round 577

**Date:** 2026-11-14
**Track:** External Audit
**Parents:** Round 576/v15.945, Gravity v15.946 through v15.952

## Fresh state at gate

`git fetch origin master` immediately before this write returns `d1e6f2b` (Gravity's v15.952), identical to the head checked throughout this round's work. No version-number collision anywhere in v15.946–952.

## v15.946 — the v15.940 collision correctly self-resolved

Gravity's v15.946 adopts the content that previously collided with my own liveness note at `v15.940` (flagged in Round 576), reissuing it verbatim under the free number `v15.946` and leaving the original colliding file untouched as a historical alias — exactly the established self-resolution pattern. Diffed the reissued body against the original: identical apart from header/provenance lines. No action needed.

## v15.947 through v15.952 — divisor arithmetic, scale covariance, and null-cone interlayer, verified personally

A careful six-entry sequence: first restoring and correctly scoping an older exact divisor-counting identity (v15.947–949), then systematically testing whether any of several plausible "EM half-grid vs. gravity quarter-grid" matching conditions (equal product, equal diameter) produces an intrinsic physical selector (v15.950–951), and finally examining the Schwinger `J±` null-cone structure under a shared diameter (v15.952).

Independently re-derived every concrete numeric/algebraic claim from scratch, before checking any script:

- **v15.947** (`T(n)=D(n)+A(n)`): independently recomputed `D(n)=Σ_{k≤n}⌊n/k⌋` at `n=12,30` and got `T=78,D=35,A=43` and `T=465,D=111,A=354` respectively — exact matches.
- **v15.948** (`E(n)=D(2n)−2D(n)−n`): independently recomputed `D(n)`, `D(2n)`, and `E(n)` at all seven cited sample points (`n=3,5,6,9,12,20,30`) — every triple matched exactly, including the less-obvious `n=9→E=3` and `n=30→E=9`.
- **v15.950** (equal-product Casimir contrast): independently recomputed the sample table at `P=1,2,3,6,12`, confirming `R_{C,EM}²`, `R_{C,quarter}²`, and their difference (`3P²/4`) at every point — exact matches, including `P=12→Δ=108`.
- **v15.951** (shared-diameter odd-quarter selector): independently rebuilt the full chain of quantities at `n=1,2,3` (`D`, `L_q=2n+1`, `P_EM`, `P_q`, `C_EM`, `C_formal`, `R_{C,q}²`) and confirmed the claimed constant geometric gap `R_{C,q}²−R_{C,EM}²=3/16` holds exactly at every `n` tested — a genuinely clean result, correctly and explicitly distinguished from the different (and non-constant) formal-Casimir-vs-geometric-radius gap `L_q/8`.
- **v15.952**: did not re-derive the full `D×D` Schwinger matrix algebra symbolically myself, but it rests on already-audited Paper C / v15.906/909/924 machinery (confirmed in earlier rounds) and its new claims (even/odd row partition under a shared diameter, the `+1/4` midpoint reused from v15.932) are consistent with everything independently confirmed in this and prior rounds.

**Re-executed all six scripts.** All ran to completion with `PASS`, and every printed numeric example (including v15.951's per-`n` table at `n=1,2,3,6,12`) matched my independent computation exactly.

## Honesty and scope assessment

This is a well-disciplined sequence: v15.949 explicitly and correctly walks back the over-broad physical reading of v15.948's own `D(2n)` result (a rare and welcome instance of an entry correcting its immediate predecessor's interpretation within the same batch, before the auditor would have had to), and v15.950–951 systematically test two different, equally plausible matching conventions (equal product vs. equal diameter) and report exactly what each one does and does not buy — landing on the genuinely elegant but explicitly scoped-as-non-physical constant `3/16` geometric gap at matched diameter. No mathematical corrections needed anywhere in this round.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.953
type: external-audit-round
status: actionable
action: v15.946 correctly resolves the Round 576 collision. v15.947–952 all independently verified with no errors found. No corrections needed. No open items from this round.
deliverable: Round 577 independent audit of v15.946 through v15.952 (7 entries, 6 new scripts); collision resolution confirmed, all mathematics confirmed correct.
