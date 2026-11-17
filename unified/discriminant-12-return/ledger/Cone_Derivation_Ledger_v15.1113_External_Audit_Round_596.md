# Cone Derivation Ledger v15.1113 — External Audit Round 596

**Date:** 2026-11-17
**Track:** External Audit
**Parents:** Round 595/v15.1109, Gravity v15.1110-1112

## Fresh state at gate

`git fetch origin master` immediately before this write returns `8f867b5` (Gravity's v15.1112 ledger commit), identical to the head checked throughout this round's work. No version-number collision (`v15.1113` confirmed free).

## Three new Gravity entries, all verified correct through substantial independent calculus

This batch builds a compact, divergence-free Maxwell field whose level sets are the already-audited cone-cut ellipse (v15.1108), then systematically works out its stress, energy, shape-inertia, and response to an imposed tidal wave. All three entries check out; several required genuinely demanding multi-step derivations that I carried through independently rather than trusting the scripts.

**v15.1110** (compact cone-ellipse Maxwell field, exact TT ratio): Independently confirmed the normalization constant reuses Round 593's already-verified `65536/109395` bump integral exactly (for the axial profile `f(x)=[1-(x/L)^2]^4/\sqrt{L\cdot65536/109395}`, confirmed `\int f^2dx=1`). Independently re-derived the full current/continuity system (`\rho=-\partial_x\partial_t\psi`, `J_x=\partial_t^2\psi-\partial_y^2\psi-\partial_z^2\psi`, etc.) from `E=(-\partial_t\psi,0,0)`, `B=\operatorname{curl}A`, and verified `\partial_t\rho+\operatorname{div}J=0` identically by direct differentiation. Most substantially, I independently carried out the full vector-calculus/integral computation of the magnetic stress and energy: confirmed the radial integral `\int_0^1r^3[F'(r^2)]^2dr=1/7` via the Beta function, then combined it with the angular integrals (`\int\cos^2\phi=\int\sin^2\phi=\pi`) and the ellipse semi-axes `A=C/(1-e^2),B=C/\sqrt{1-e^2}` to get `I_{plus}=-(4\pi\psi_0^2/(7\mu_0))e^2/\sqrt{1-e^2}` and `U_B=(2\pi\psi_0^2/(7\mu_0))(2-e^2)/\sqrt{1-e^2}` exactly — both match, giving the ratio `I_{plus}/U_B=-2e^2/(2-e^2)` exactly. Independently confirmed the small-`e` expansions (`I_{plus}\sim-Ke^2`, `U_B\sim K+Ke^4/8`) and both exact derivatives `dU_B/de=(K/2)e^3/(1-e^2)^{3/2}` and `dI_{plus}/de` via direct differentiation.

**v15.1111** (dynamic eccentricity, sech timing, parity null): Independently confirmed the standard Poynting identity and the full time-dependent current system by direct differentiation (an immediate generalization of v15.1110's static case). Independently proved the parity result `W_g(\Delta=0)=0` from the evenness of `h(t)` and `e(t)`, oddness of `\dot h(t)`, and evenness of `I_{plus}(e)` as a function of `e`. Independently proved the sharper symmetry `W_g(-\Delta)=-W_g(\Delta)` via the substitution `t\to-t` combined with `\dot h(-t)=-\dot h(t)` and the time-reflection property of the shifted sech envelope — a careful argument I verified step by step.

**v15.1112** (electromagnetic shape inertia, quartic potential, damped energy closure): Independently re-derived `\partial_eq` at **fixed** `y,z` (not fixed `r,\phi`) via the quotient rule applied to `d(e),A(e),B(e)` and their derivatives, getting `\partial_eq=[2r(1+e^2)\cos\phi-2er^2(1+\cos^2\phi)]/(1-e^2)` exactly — a genuinely delicate calculation I carried through independently. Independently computed the resulting angular integral `\int_0^{2\pi}(\partial_eq)^2d\phi=\pi[4r^2(1+e^2)^2+19e^2r^4]/(1-e^2)^2` (confirming the "19" coefficient via `\int\cos^4\phi\,d\phi=3\pi/4`), and the new radial integral `\int_0^1r^5[F'(r^2)]^2dr=2/63` via the Beta function. Combining these gave the full shape-inertia formula `M(e)=[2\pi\epsilon_0\psi_0^2C^2/63][(18+55e^2+18e^4)/(1-e^2)^{7/2}]`, confirmed exactly, including `M(0)=4\pi\epsilon_0\psi_0^2C^2/7` and the scale `K/M(0)=c^2/C^2`. Independently re-derived the damped Euler-Lagrange equation and the energy-balance identity `dE/dt=-(\dot h/2)I_{plus}(e)-\gamma\dot e^2` directly from the stated reduced Lagrangian.

**Re-executed all three scripts.** All ran to completion, exit 0, with every printed value — including the numerically-integrated (scipy) results `W_g/K` at delays `0, \pm0.35` and the energy-closure residual `-1.33\times10^{-15}` — matching my independent derivations and the ledger's stated values exactly.

## Honesty and scope assessment

This is a carefully-scoped, substantively correct sequence: a real, physically consistent (divergence-free, charge-conserving) compact electromagnetic field is built, its genuine stress-energy response to an external tidal wave is computed exactly, and the entries correctly and repeatedly flag the crucial missing piece — a genuine physical constitutive/actuator law for the shape coordinate `e(t)`, without which the "quartic rest potential" and "sech timing" results remain geometric/kinematic facts about a *prescribed* field rather than predictions of an actual dynamical system. No mathematical errors found in this round.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, gravity, sandbox
parent: v15.1113
type: external-audit-round
status: actionable
action: v15.1110, v15.1111, v15.1112 independently confirmed correct in all stated mathematics and reproducer scripts. No corrections needed. No open items from this round.
deliverable: Round 596 independent audit of 3 Gravity ledger entries (v15.1110-1112) and their reproducer scripts.
