# Cone Derivation Ledger v15.579 — Lane A: zero-external-field transition-current feedback and mirror cancellation

**Date:** 2026-11-09. **Parents:** v13.595, v15.140, v15.572–578. **Status:** [D] exact finite-dimensional source/symmetry identities; [N] explicitly chosen coupled-mode simulation; [O] physical field/current dictionary, Maxwell coupling, open-boundary-specific effect. **Prewrite HEAD:** eb4cdfc3061196f7d8f68ff5498dd80321ec0e69, collision search no v15.579. Additive only. Frozen Suzuki/far-tail untouched.

## 1. Transition current without an externally applied Zeeman field [D]

At j=3/4, M=Jz=diag(-3/4,-1/4,+1/4,+3/4), original step-one J+ has nonzero edges (0->2),(1->3), both sqrt(3/2), Jx=(J++J-)/2. Let H0=-g Jx, real g. No term omega M is present. Define the *mathematical source candidate* S=i[H0,M] in units hbar=1; S=dM/dt at the operator level under H0. For initial |0>, evolution within its 2-state block yields exactly

<M(t)> = -1/4 - (1/2) cos(g sqrt(3/2) t),
<S(0)>=0, d<S>/dt|0 = 3g²/4.

The reflection R|i>=|3-i> maps RMR=-M, R Jx R=Jx and hence RSR=-S. Mirror-reflected |3> has the opposite current/coordinate profile, whereas the R-even state (|0>+|3>)/sqrt(2) has <M(t)>=<S(t)>=0 throughout free matter-only evolution. The nonzero g is *assumed*: g=0 makes S=0, so this is not a vacuum excitation arising without an interaction.

## 2. Explicit field-oscillator feedback test [D conditional on model; N numeric]

Introduce one oscillator of frequency Omega>0 with Q=(b+bdag)/sqrt(2), number n=bdag b, and the **new test ansatz**

H_total= H0 tensor I + I tensor Omega*n + lambda*S tensor Q,

with real lambda. This does **not** come from a derived Maxwell equation or a physical electromagnetic gauge coupling.

The combined parity P=R tensor (-1)^n obeys P H_total P=H_total and P (I tensor Q) P= -(I tensor Q). Thus for the mirror-even matter state with oscillator vacuum, <Q(t)>=0 **exactly** for all times, even though oscillator excitation can be nonzero. For |0> with initially empty oscillator, Heisenberg oscillator equation and current slope give

<Q(t)>= -(Omega*lambda*g²/8)t³ + O(t⁴).

For uncoupled-oscillator vacuum initial preparation and either |0> or its mirror-even superposition, the initial oscillator occupation has

<n(t)>= (lambda²/2)<S²>_0*t² + O(t³)= (3 lambda²*g²/16)t²+O(t³),

because <S²>_0=3g²/8. Thus **zero mean field is not absence of fluctuations or oscillator quanta**; oscillator excitations are not necessarily radiated photons because the starting vacuum is not generally the dressed ground state and no outgoing continuum or asymptotic radiation is modeled.

SymPy-style exact matrix identities and full finite-dimensional exponentiation were tested with g=1, Omega=2, lambda=0.2, oscillator cutoff 6. At t=1: single-chain initial |0>, <Q>=-0.03755634867 and <n>=0.00500533331; mirror-even (|0>+|3>)/sqrt(2), <Q>=0 (roundoff) and <n>=0.00500533331. The exact P symmetry was verified as a matrix identity. Source built instead from M itself also creates a field, but that example is contaminated by initial static <M> and is less diagnostic of transition-generated motion.

## 3. Scope and genuinely discriminating next step

This proves a possible **mirror-odd transition-current source in an explicitly postulated Hamiltonian**; it does *not* show that the cone selects the physical field oscillator, its frequency or lambda, or its coupling to actual gauge fields. It does not require open-quarter escape at all: a closed SU(2) ladder can likewise generate a time-varying dipole current under an assumed transverse coupling. Nor does it prove net sustained radiation, spontaneous activation g without input, weak chirality, or G.

Next gate: compare open odd-quarter versus closed half-grid spin ladders under matched source/drive normalization, isolating whether the exact boundary-projector defect D=c(P+-P-) generates an observable signature not reproducible by a generic driven magnetic dipole. An honest candidate has to include either an explicit boundary source/inter-shell target from the cone or a measurable, symmetry-protected difference.

**HANDOFF** target external-audit; type finite feedback Hamiltonian, parity and initial-slope verification; status open; action independently verify the S derivative, combined reflection-oscillator parity and <Q> symmetry, short-time current-sourced <Q> and <n> coefficients; challenge the claim of any mechanism special to open quarter shells. Reproducer local archive cone_zero_field_feedback_gates_48_49.zip; no production code changes.
