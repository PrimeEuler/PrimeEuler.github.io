# Cone Derivation Ledger v15.1104 — External Audit Round 594

**Date:** 2026-11-17
**Track:** External Audit
**Parents:** Round 593/v15.1099, Gravity v15.1100-1103

## Fresh state at gate

`git fetch origin master` immediately before this write returns `4d257dd` (Gravity's v15.1103 ledger commit), identical to the head checked throughout this round's work. No version-number collision (`v15.1104` confirmed free).

## Four new Gravity entries, all verified correct through substantial independent derivation

This batch moves the project from the abstract Rindler/Compton-scale question (Rounds 593's conclusion: still unselected) toward genuinely physical radiation and tidal-wave calculations. All four entries check out.

**v15.1100** (confocal secant exactly traces a uniformly accelerated worldline): Independently confirmed the confocal parabola `Y²=k²-2kX` has vertex `(k/2,0)` and focus `(0,0)`, and that intersecting it with the secant `Y=R` gives `T_k=R\cosh u, X_k=R\sinh u` under `u=\log(k/R)` (confirmed `T_k²-X_k²=R²`, `T_k\pm X_k` identities directly). Confirmed this matches the standard relativistic hyperbolic-motion trajectory `ct=R\sinh(a\tau/c), x=R[\cosh(a\tau/c)-1]` exactly under `u=a\tau/c`. Independently re-derived `d\theta/du=\operatorname{sech}u` by direct differentiation of `\theta=\arctan(\sinh u)`, and confirmed the involution `k\leftrightarrow R^2/k` sends `X_k\to-X_k` while leaving `T_k` fixed, by direct substitution.

**v15.1101** (retarded null wavefront circles): Independently derived the transverse lightfront radius at the observation point `(0,0)`: starting from `r_\perp^2=(ct_e)^2-(x_e)^2|_{\text{appropriately signed}}`, i.e. `R^2\sinh^2u-R^2(\cosh u-1)^2`, I confirmed by direct hyperbolic-identity algebra that this equals `2R^2(\cosh u-1)=4R^2\sinh^2(u/2)`, then re-expressed in terms of `k=Re^u` to get `r_\perp^2=R(R-k)^2/k` exactly — matching the script's printed `R(R²+k(-2R+k))/k` (confirmed algebraically identical: `R²-2Rk+k²=(R-k)²`). Independently confirmed the collinear-null-wave TT-cancellation proof: with `T_{ij}=\rho\,n_in_j` for a locally plane radiation field (confirmed via the orthonormal decomposition of `\delta_{ij}` into `n,e_\theta,e_\phi`), the TT projector `P=I-nn^T` annihilates `n_in_j` exactly, giving `T^{TT}_{ij}=0` — a standard and correctly-drawn fact that an EM wave can't source a gravitational wave traveling in the *same* direction.

**v15.1102** (finite accelerated two-body pulse, EM dipole vs. GW quadrupole): Independently derived `g''(s)=8(1-s^2)^2(7s^2-1)` from `g(s)=(1-s^2)^4` by direct differentiation, confirming the sign reversal at `s=\pm1/\sqrt7`. Independently recomputed `\int_{-1}^1[g''(s)]^2ds=196608/5005` from scratch via full binomial expansion and term-by-term rational summation. Propagated this into the radiated EM energy, confirming `U_{EM}=131072q^2\epsilon^2/(5005\pi\epsilon_0c^3T^3)` exactly by the same method. Independently derived the quadrupole identity `\ddot(Q_{xx}-Q_{yy})=4m(\dot x^2+x\ddot x)` and, most substantially, carried the full chain through to the stated peak values at the pulse center: `E_{rad,x}(0)=-4q\epsilon/(\pi\epsilon_0c^2DT^2)`, `h_+(0)=-32Gm\epsilon(x_0+\epsilon)/(c^4DT^2)`, and the tidal acceleration `(\ddot\xi_x/\xi_x)(0)=96Gm\epsilon(3x_0+7\epsilon)/(c^4DT^4)` — the last of these required computing `g''''(0)=144` and `(g^2)''''(0)=672` independently (via direct symbolic differentiation and binomial expansion respectively) and combining them through the `d^2h_+/dt^2` chain rule; all three match exactly.

**v15.1103** (finite tidal pulse drives a seeded transverse Maxwell cavity): Independently re-derived the parametrically-coupled mode equation `(1+h)\ddot Q+\dot hQ\dot{}+\omega_0^2Q=0` from the stated Lagrangian via the Euler-Lagrange equation, and the energy-transfer identity `dE/dt=-\tfrac12\dot hQ\dot{}^2` by direct substitution of the equation of motion — a clean, correct derivation. Independently derived the fractional energy-transfer formula `\Delta E/E_0=\omega_0\sin(2\phi)H_{\cos}(2\omega_0)` via integration by parts and the double-angle expansion of `\sin(2\omega_0t+2\phi)`. Independently derived the exact closed form `H_{\cos}(2\omega_0)=-[4Gm/(c^4DT)]\xi^2[x_0\epsilon F_4(\xi)+(\epsilon^2/2)F_8(\xi)]` via **two** integrations by parts of `\int g''(s)\cos(\xi s)ds=-\xi^2F_4(\xi)` (boundary terms vanish since `g,g'` vanish at `s=\pm1`) — confirming the general rule `\int h''(s)\cos(\xi s)ds=-\xi^2\int h(s)\cos(\xi s)ds` for compactly-supported `h`. Independently recomputed both shape-transform constants from scratch via binomial expansion: `F_4(0)=256/315` and `F_8(0)=65536/109395` (the latter via an 8-term rational sum over a common denominator `765765`) — both match exactly.

**Re-executed all four scripts.** All ran to completion, exit 0, with every printed value — including the numerically-evaluated (non-closed-form) `F_4(\pi)=0.5102410680256` and `F_4(2\pi)=0.09162140342465` — matching my independent derivations and the ledger's stated values exactly.

## Honesty and scope assessment

This is a substantively correct, carefully-scoped batch of real electrodynamics and weak-field general relativity: finite accelerated sources genuinely radiate both electromagnetically and gravitationally, and a tidal wave genuinely does parametric work on a correctly-oriented EM cavity mode — all standard, correctly imported physics with `G` and other physical constants left as external inputs, never derived from the Cone's arithmetic structure. Each entry is explicit about what it has *not* shown (a fully conserved covariant source, the frozen K4 solid's constrained ADM response, any Cone-specific selector for the pulse's own temporal spectrum). No mathematical errors found in this round.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, gravity, sandbox
parent: v15.1104
type: external-audit-round
status: actionable
action: v15.1100, v15.1101, v15.1102, v15.1103 independently confirmed correct in all stated mathematics and reproducer scripts. No corrections needed. No open items from this round.
deliverable: Round 594 independent audit of 4 Gravity ledger entries (v15.1100-1103) and their reproducer scripts.
