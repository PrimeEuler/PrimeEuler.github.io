# Cone Derivation Ledger v15.999 — External Audit Round 585

**Date:** 2026-11-14
**Track:** External Audit
**Parents:** Round 584/v15.994, Gravity v15.995 through v15.998

## Fresh state at gate

`git fetch origin master` immediately before this write returns `58da4e8` (Gravity's v15.998), identical to the head checked throughout this round's work. No version-number collision (`v15.999` confirmed free).

## v15.995 through v15.998 — the K4/Maxwell source search for the open-quarter boundary operator, verified personally

A deep, genuinely field-theoretic four-entry sequence continuing v15.993's search: does the project's actual frozen K4 solid action, combined with the real curved-Maxwell action, contain a term that could physically source the open quarter-grid boundary operator `T` (established in the already-audited v15.602/991)? This is by far the most technically demanding batch audited to date, involving explicit mode-overlap integrals, Legendre transforms, and the K4 elastic invariant's Taylor expansion. Independently re-derived every concrete symbolic/numeric claim from scratch using SymPy (not the committed scripts):

- **K4 elastic invariant series**: independently expanded `J(b)=[e^{4b}+e^{-4b}+1]/[e^{2b}+e^{-2b}+1]²-1/3` and the two-polarization form `J(r)` (with `r²=b²+c²`) and got `8b²/9 - 8b⁴/9 + 112b⁶/135` for both — exact matches, including the claimed absence of any cubic term (confirming the stated `b→-b`/`J(r)` parity argument).
- **Quartic mixed term**: independently expanded `-(8/9)r⁴` in `b,c` and got `-8b⁴/9 - 16b²c²/9 - 8c⁴/9`, exactly matching the claimed `J_4=-(8/9)(b⁴+2b²c²+c⁴)`.
- **Mode-overlap integrals**: independently computed every cited `C,D` overlap matrix from scratch via direct definite integration on `z∈[0,π]` for modes 1 and 3, at Fourier orders `k=0,2,4,6` — all exact matches to the ledger's v15.995 and v15.998 tables (including the `k=0`/`k=6` diagonal-only and `k=2`/`k=4` off-diagonal structure).
- **Cross-tensor spatial overlap**: independently computed `I_{04}=\int e_0e_4\cos^2(2z)\,dz=\sqrt2/4` exactly, matching v15.997.

**Re-executed all five scripts** (v15.995, v15.996, and both v15.997 scripts, v15.998). All ran to completion with `PASS`, and every printed symbolic/numeric value matched my independent derivation exactly, including the two `2\sqrt3` "conditional" quartic-symbol coefficients in v15.995 and v15.998 that the entries are careful to flag as kinematically-possible-but-not-physically-sourced.

## Honesty and scope assessment

This is an exceptionally disciplined piece of physics work: each entry in the sequence takes the real, already-established field actions (not an invented coupling) and traces exactly which terms survive symmetry, parity, and selection-rule constraints at each order — repeatedly distinguishing "this symbolic structure is kinematically admissible" from "this is a derived physical coupling." The culminating result (v15.998) is a clean, general Z2-reflection-symmetry veto: within the stated reflection-symmetric background, no perturbative order of this restricted model can produce the required photon-polarization-odd operator without an explicit parity-breaking input — a stronger and more structural negative than the single-exchange-order checks in v15.995–997. Throughout, the entries correctly decline to claim a general no-go for the full nonlinear K4+Maxwell theory, scoping every negative result to the specific restricted ansatz tested. No mathematical corrections needed in this round.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.999
type: external-audit-round
status: actionable
action: v15.995–998 all independently confirmed correct across extensive symbolic field-theory computations (K4 elastic invariant expansions, mode-overlap integrals, Legendre transforms). No corrections needed. No open items from this round.
deliverable: Round 585 independent audit of v15.995 through v15.998 (4 entries, 5 scripts); all confirmed correct.
