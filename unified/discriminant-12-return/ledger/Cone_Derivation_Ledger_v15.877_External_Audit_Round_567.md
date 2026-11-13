# Cone Derivation Ledger v15.877 — External Audit Round 567

**Date:** 2026-11-13
**Track:** External Audit
**Parents:** Round 566/v15.868, Sandbox v15.869, Gravity v15.870, v15.871, v15.872, v15.873, v15.874, v15.875, v15.876

## Fresh state at gate

`git fetch origin master` immediately before this write returns `6a62f4a` (Gravity's v15.876), identical to the head checked throughout this round's work. No version-number collision (`v15.877` confirmed free).

## v15.870 — the Round 566 repair, verified personally: both findings correctly fixed

Read the committed repair script in full before running it. It makes exactly the two changes I identified in Round 566 — the disclosed structural-equality assertion fix, plus my own exact fix for the `v=s.Function('v')(tau)` callable-collision bug (`v=s.Function('v')(tau)` → `v=s.Function('v')`) — and explicitly asserts the unsupported "Minkowski tensor oscillator benchmark" phrase is absent from the replayed text. **Re-executed the committed script**: it now runs to completion, reproducing the exact same Gate 491 table I obtained from my own scratch fix in Round 566 (`lever=8.27921561087423` at all three orientations, with the identical plus/cross values). Both of my findings are correctly and fully remediated; nothing further needed here.

## v15.869 — the transition-parabola connection, verified personally

**End-to-end re-execution** reproduced every claim exactly: the osculating-parabola/no-quadratic-term distinction between `cos` at its vertex and `sin` at its node, the node/antinode quarter-turn offset, and the Airy-equation reduction with zero-asymptotic ratios `1.0077`, `1.0015`, `1.0006` at the first three Airy zeros, matching the ledger's cited values exactly.

## v15.871, v15.872 — EM/gravity phase-rate dictionary and K4 tensor Green response, verified personally

Independently re-derived the Green's-function solution to the forced oscillator equation `u_ss+ν²u=-2sin(Ωs+φ)` with zero initial data from scratch (fresh SymPy session, not importing the committed script): confirmed the stated closed form satisfies the ODE and initial conditions exactly (`simplify` to zero on all three checks). Independently recomputed the numeric case `β_T=14, Ω=2` (`ν²=13`): gain `2/9`, and the zero-data transient values at `s=1` for sine-phase (`φ=0`) and cosine-phase (`φ=π/2`) sources: `-0.257226931022372` and `-0.106253604891363`, matching the ledger's cited `-0.2572269310` / `-0.1062536049` exactly. **Re-executed both committed scripts**: both reproduce every value exactly.

## v15.873, v15.874 — Casimir offset vs. parametric pump work, verified personally

Independently re-derived both central identities from scratch with direct symbolic computation: the on-shell energy-transfer law `dE/dt=(1/2)k̇(t)x(t)²` (substituting the true equation of motion `mẍ=-k(t)x` into `d/dt[mẋ²/2+k(t)x²/2]`, confirmed exactly), and the first-order pump-work integral `ΔE^(1)=πA²δk·cosφ/2` (direct symbolic integration over one period, confirmed exactly — not just checked consistent with the claim). **Re-executed both committed scripts**: v15.873 reproduces the exact symbolic identities and phase-sign table; v15.874's numeric table (`ε=0.01`: exact `ΔE` of `+0.0159570945861`/`+0.000248149132821`/`-0.015463570308` at `φ=0,π/2,π`) matches the ledger's cited `+0.01595709459`/`+0.00024814913`/`-0.01546357031` exactly.

## v15.875 — conservative EM/gravity-like toy Hamiltonian, verified personally

Independently re-derived all four Hamilton equations and the on-shell `Ḣ=0` identity from the stated Hamiltonian via direct symbolic differentiation (fresh SymPy session), confirming every claimed equation of motion and the exact opposite energy-exchange identities `Ė_EM=+λq̇x²/2=-Ė_G` exactly. **Re-executed the committed script**: the numeric table (`ΔE_EM` at `φ=0,π/2,π`: `+0.03027997992078979`/`-0.0009732985174774056`/`-0.03226015480385902`) matches the ledger's cited values exactly, with the 25-period conservation residual (`8.21e-11`/`7.57e-11`/`1.34e-10`) consistent with the cited `1.34×10⁻¹⁰` bound.

## v15.876 — GR Fermi tidal comparator and atomic-scale hierarchy, verified personally

Independently recomputed the gravitational-to-Coulomb force ratio from `scipy.constants` (`4πε₀Gm_pm_e/e²`) and got `4.407885575703484e-40`, matching the ledger's cited `4.40788557570×10⁻⁴⁰` exactly, and independently matched the Bohr-radius/frequency and illustrative gravitational-wave fractional-stiffness estimates. **Re-executed the committed script**: every displayed value (Bohr radius, `ω_e`, force ratio, illustrative `ε_tidal` at 100 Hz and at resonance) matches exactly.

## Honesty and scope assessment

An unusually large, fully-confirmed round across eight entries spanning both tracks, with zero new defects found. The v15.870 repair exactly and completely resolves both findings from Round 566, down to the identical fix I independently derived — a clean remediation. The Gravity sequence (v15.871→876) is a careful, honest chain of "is this hypothesis correct" investigations prompted directly by the project owner's own questions (EM/gravity phase dictionaries, Casimir-offset causation, atomic stability via gravitational pumping): every entry correctly concludes the proposed mechanism is either not novel to Cone, or many orders of magnitude too weak, or both — with no overclaiming anywhere, and the quantitative force-hierarchy comparison (`~10⁻⁴⁰`) is presented honestly as a decisive negative result rather than downplayed.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.877
type: external-audit-round
status: actionable
action: v15.869 through v15.876 are all independently confirmed as stated with no corrections needed, including full remediation of both Round 566 findings via v15.870. No further action required on the force-agent entry; both prior issues are closed.
deliverable: Round 567 independent audit of v15.869 through v15.876 (8 entries, 2 tracks).
