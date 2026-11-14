# Cone Derivation Ledger v15.987 — External Audit Round 582

**Date:** 2026-11-14
**Track:** External Audit
**Parents:** Round 581/v15.985, Gravity v15.986

## Fresh state at gate

`git fetch origin master` immediately before this write returns `02e00f5` (Gravity's v15.986), identical to the head checked throughout this round's work. No version-number collision (`v15.987` confirmed free).

## v15.986 — sourced Maxwell/tidal couplings vs. the fixed-L rotor, verified personally

This entry continues the v15.984 line by testing whether the project's already-sourced physical magnetic (`H_B=-ℏ(qB/M)J_y`) and tidal (`H_T=ℏ(Φ12/ω0)J_x`) couplings are compatible with the v15.900 fixed-angular-momentum rotor, and finds a clean physical obstruction: a generic transverse tidal drive necessarily torques the rotor's angular momentum, breaking the constant-`L` assumption the rotor's turning-point solution depends on, whereas a magnetic term does not.

Independently re-derived the central claims from scratch:

- Built the full `D=5` (`j=2`) `J_y²` matrix from scratch using standard spin-matrix conventions and confirmed it matches the ledger's explicitly printed matrix exactly, including the `Δk=0,±2` support pattern (no `Δk=±1` entries) that distinguishes it from the ordinary dipole `J±` ladder.
- Confirmed analytically that `[J_x,J_y]=iJ_z` gives `dJ_y/dt=-gJ_z` under `H=ℏgJ_x`, hence `dL_z/dt=-2ℏgJ_z\neq0` generically — the stated torque obstruction.
- Independently re-derived the polar tidal potential `V_T=Mφ_{12}q_1q_2` in polar coordinates, confirming `V_T=(Mφ_{12}/2)r²\sin(2φ)` and its exact radial-force and torque derivatives `F_{r,T}=-Mφ_{12}r\sin(2φ)`, `τ_{z,T}=-Mφ_{12}r²\cos(2φ)` — both matching exactly, including the two cited special cases (`φ=0`: zero force, nonzero torque; `φ=π/4`: nonzero force, zero torque).

**Re-executed both scripts.** Both ran to completion with `PASS`, matching every value independently derived above.

## Honesty and scope assessment

This entry correctly identifies and clearly states a genuine internal tension in the project's own prior results — the fixed-L rotor (v15.900) and the sourced tidal coupling (v15.908) cannot simultaneously hold as stated once a generic tidal drive is switched on — rather than quietly ignoring it or papering over it. It also correctly distinguishes the rotor's classical centrifugal operator from the EM dipole ladder operator, preventing a tempting but unjustified identification. No mathematical corrections needed in this round.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.987
type: external-audit-round
status: actionable
action: v15.986 independently confirmed correct in all its mathematics. No corrections needed. No open items from this round.
deliverable: Round 582 independent audit of v15.986 (1 entry, 2 scripts); confirmed correct.
