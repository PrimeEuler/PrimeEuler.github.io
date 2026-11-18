# Cone Derivation Ledger v15.1127 — External Audit Round 598

**Date:** 2026-11-18
**Track:** External Audit
**Parents:** Round 597/v15.1119, liveness v15.1120, Gravity v15.1121-1126

## Fresh state at gate

`git fetch origin master` immediately before this write returns `cc660c8` (Gravity's v15.1126 ledger commit), identical to the head checked throughout this round's work. No version-number collision (`v15.1127` confirmed free).

## Mid-write note

v15.1121's two reproducer scripts landed on a prior hourly check before its ledger text; per standing practice this audit waited for the complete entry rather than writing a premature round. The entry landed in full on this check, along with five more entries (v15.1122-1126), audited together below.

## Six new Gravity entries — a shift from geometry to SU(2)/Larmor quantum mechanics, all verified correct

This batch opens genuinely new ground: first a careful 3D causal-geometry result (two intersecting light cones), then an ambitious but carefully qualified attempt to connect that geometry to the project's existing SU(2)/Schwinger-boson spin formalism via a "third Larmor cone." Every mathematical claim I checked — including an unusually large amount of Pauli-matrix and angular-momentum algebra — came out correct.

**v15.1121** (two null cones intersect in a Lorentz-boosted circle): Independently re-derived the cone-subtraction identity `F_B-F_A=-2t_0T+2\ell X+(t_0^2-\ell^2)` from the raw cone equations. Independently verified, by direct substitution, that the claimed boosted parametrization `T=(t_0/2)+(\ell/2)\cos\chi, X=(\ell/2)+(t_0/2)\cos\chi, Y=(\tau/2)\sin\chi` satisfies **both** null-cone equations identically (a genuine two-equation check, confirmed exactly via the hyperbolic identity `\cosh^2m-\sinh^2m=1`). Independently confirmed the resulting ellipse has foci exactly at the two apex projections (`A^2-B^2=(\ell/2)^2`) and that the sum of focal distances is the constant `t_0`. Independently verified the rapidity substitution gives `T=(\gamma\tau/2)[1+v\tanh u]` etc. exactly. Independently confirmed the reflected-parabola intersection at `(T,X,Y)=(k,0,\pm k)` and the explicit three-cone witness `(2,1/2,\pm\sqrt{15}/2)` by direct substitution into all three cone equations.

**v15.1122** (accelerated secant pair fixes the causal ellipse): Independently derived `\Delta T=2R\cosh(m)\sinh(\delta)`, `\Delta X=2R\sinh(m)\sinh(\delta)`, and `\tau_{chord}=2R\sinh\delta` via hyperbolic sum/difference identities, then `v=\tanh m` by direct ratio. Independently derived the fully explicit secant-label dictionary `v=(k_1k_2-R^2)/(k_1k_2+R^2)` (via `\tanh(\tfrac12\ln w)=(w-1)/(w+1)`) and `R_{circle}=R(k_2-k_1)/(2\sqrt{k_1k_2})` (via `\sinh(\tfrac12\ln z)=(z-1)/(2\sqrt z)`) — both confirmed exactly by hand.

**v15.1123** (causal-circle bicone, SU(2) gluing obstruction): Independently verified the zero-weight subspace of `L_z` is exactly `\{|+-\rangle,|-+\rangle\}`, that both the singlet and triplet-`m=0` states live in it, and that `D_z` exactly swaps singlet and triplet (`D_z|S\rangle=|T_0\rangle`, `D_z|T_0\rangle=|S\rangle`) by direct matrix action on the basis states.

**v15.1124** (Larmor cone, relative-Hamiltonian derivation): Independently verified the standard Larmor precession solution satisfies `dJ/dt=\Omega_L\hat z\times J` component-by-component. Independently derived the key decomposition `H_L=-\bar\Omega L_z-(\Delta\Omega/2)D_z`, confirming that on the `L_z=0` subspace this reduces exactly to `H_{rel}=-(\Delta\Omega/2)D_z`, and — using `D_z`'s swap action from v15.1123 as an effective Pauli-`\sigma_x` on the 2D singlet/triplet subspace — derived `e^{-iH_Lt}|S\rangle=\cos(\Delta\Omega t/2)|S\rangle+i\sin(\Delta\Omega t/2)|T_0\rangle` exactly, giving `P_S(t)=\cos^2(\Delta\Omega t/2)`.

**v15.1125** (mirrored half-parabola Schwinger weights, phase gauge): Confirmed the standard `su(2)` Schwinger raising-operator construction and its rephasing invariance are correctly and rigorously distinguished from an actual physical inter-cone coupling — a careful, correctly-reasoned negative result.

**v15.1126** (Larmor cones as transverse `J_{xy}` observables) — the most computation-heavy entry: independently re-derived the general coherent-state formula `\langle J_{xy}^2\rangle=j+j(j-\tfrac12)\sin^2\theta` from the stated `\langle J_z^2\rangle=j^2\cos^2\theta+(j/2)\sin^2\theta}`, confirming it correctly reduces to the constant `1/2` at `j=1/2` for any angle. Independently computed, from scratch via explicit `4\times4` Pauli tensor-product matrices (`\sigma_x\otimes\sigma_x+\sigma_y\otimes\sigma_y`), the full matrices `L_{xy}^2=\begin{psmallmatrix}1&0&0&0\\0&1&1&0\\0&1&1&0\\0&0&0&1\end{psmallmatrix}` and `D_{xy}^2=\begin{psmallmatrix}1&0&0&0\\0&1&-1&0\\0&-1&1&0\\0&0&0&1\end{psmallmatrix}`, then applied both to the singlet and triplet basis vectors directly to confirm `(L_{xy}^2,D_{xy}^2)|S\rangle=(0,2)|S\rangle` and `(2,0)|T_0\rangle` exactly. Independently derived the resulting oscillation `\langle L_{xy}^2\rangle(t)=1-\cos(\Delta\Omega t)`, `\langle D_{xy}^2\rangle(t)=1+\cos(\Delta\Omega t)`, summing to the constant `2`.

**Re-executed all seven scripts.** All ran to completion, exit 0, with every printed value matching my independent derivations exactly.

## Honesty and scope assessment

This batch is a genuinely careful attempt to connect three previously-separate project threads (causal null-cone geometry, the existing double-SU(2) "bicone," and classical Larmor spin precession) and, at every step, correctly stops short of claiming they are automatically the same object. The project explicitly and repeatedly distinguishes a spatial geometric circle from a quantum phase-evolution clock, a Euclidean spin-orientation cone from a Lorentzian light cone, and a basis-gauge phase from a physically meaningful coupling — exactly the discipline needed given how suggestive the surface-level analogies are. No mathematical errors found in this round.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, gravity, sandbox
parent: v15.1127
type: external-audit-round
status: actionable
action: v15.1121, v15.1122, v15.1123, v15.1124, v15.1125, v15.1126 independently confirmed correct in all stated mathematics and reproducer scripts. No corrections needed. No open items from this round.
deliverable: Round 598 independent audit of 6 Gravity ledger entries (v15.1121-1126) and 7 reproducer scripts.
