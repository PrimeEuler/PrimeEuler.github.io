# Cone Derivation Ledger v15.1133 — External Audit Round 600

**Date:** 2026-11-18
**Track:** External Audit
**Parents:** Round 599/v15.1129, liveness v15.1130, Gravity v15.1131-1132

## Fresh state at gate

`git fetch origin master` immediately before this write returns `c4e5427` (Gravity's v15.1132 ledger commit), identical to the head checked throughout this round's work. No version-number collision (`v15.1133` confirmed free).

## Two new Gravity entries completing the bicone gradiometer design, both verified correct

This milestone round (600) closes out the bicone-tidal-gradiometer design thread that began in v15.1128: a fully explicit, physically consistent transducer linking mechanical misalignment to a measurable quantum spin correlator, plus an honest assessment of what it can and cannot actually measure.

**v15.1131** (explicit magnetomechanical transducer, Ramsey readout): Independently confirmed the field `B=(Gz,0,B_0+Gx)` is genuinely source-free (`\operatorname{div}B=0` and the relevant curl component both vanish by direct differentiation, since `B_x` has no `x`-dependence and `B_z` has no `z`-dependence). Independently derived the differential Larmor frequency `\Delta\Omega(\theta)=\gamma Gd\cos\theta` from the two sensor-location field values, and its derivative `-\gamma Gd\sin\theta`. Independently derived the full response formula `\delta C_{xy}/g=-2\gamma Gd\tau\Delta Q\sin\phi_{bias}\sin\theta_0\sin(2\theta_0)\chi_\theta` via the chain rule through the Ramsey phase. Independently derived the angular optimum from `F(\theta)=\sin\theta\sin2\theta`, confirming `F'(\theta)=2\sin\theta(2-3\sin^2\theta)` by direct differentiation, giving the "magic angle" `\theta_{opt}=\arccos(1/\sqrt3)\approx54.7356°` with `F_{max}=4/(3\sqrt3)` — both confirmed exactly, distinct from the `45°` optimum of the purely mechanical torque alone. Independently derived the magnetic-gradient/tidal degeneracy formula `g_{equiv}=-[\kappa\cos\theta_0/(G\Delta Q\sin\theta_0\sin2\theta_0)]\delta G` via the ratio of the two coupling pathways.

**v15.1132** (two-channel identifiability, ideal shot-noise floor): Independently confirmed the lower-triangular response matrix `\begin{psmallmatrix}A&0\\BA&Z\end{psmallmatrix}` inverts to `\delta g=\delta\theta/A`, `\delta G=(\delta C_{xy}-B\delta\theta)/Z` by direct `2\times2` matrix inversion. Independently derived the exact projection-noise variance `\text{Var}(C_{op})=4-\langle C_{op}\rangle^2=4\sin^2\phi` from the eigenvalues `\mp2` on triplet/singlet, confirming the standard shot-noise formula `\delta\phi_{min}=1/\sqrt N` at the optimal bias `\phi=\pi/2` (slope `2`, variance `4`). Independently propagated this through the full transduction chain to the final sensitivity formula `\delta g_{min,opt}=3\sqrt3\kappa/(4\gamma Gd\tau\Delta Q\sqrt N)` — confirmed exactly via the general formula `\kappa/(\gamma Gd\tau\Delta Q\cdot F(\theta_0)\sqrt N)` evaluated at the already-verified `F_{max}=4/(3\sqrt3)`.

**Re-executed both scripts.** Both ran to completion, exit 0, with every printed value — including the symbolic determinant and the final shot-noise-floor formula — matching my independent derivations exactly.

## Honesty and scope assessment

This two-entry sequence completes a genuinely well-posed instrument-design exercise: a physically consistent (divergence-free) magnetic gradient, a standard torsional mechanical response, and the project's own previously-derived quantum spin correlator are combined into an explicit, internally consistent transfer function with a real optimal operating angle and an honest accounting of a confounding noise channel (magnetic-gradient drift mimics a tidal signal unless independently measured). The two entries are careful throughout to say this is ordinary magnetometer/gradiometer engineering layered on the project's existing SU(2) formalism, not a new source of gravitational physics — and that a single spin-only readout cannot by itself separate the two physical effects it's sensitive to. No mathematical errors found in this round.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, gravity, sandbox
parent: v15.1133
type: external-audit-round
status: actionable
action: v15.1131, v15.1132 independently confirmed correct in all stated mathematics and reproducer scripts. No corrections needed. No open items from this round.
deliverable: Round 600 independent audit of 2 Gravity ledger entries (v15.1131-1132) and their reproducer scripts.
