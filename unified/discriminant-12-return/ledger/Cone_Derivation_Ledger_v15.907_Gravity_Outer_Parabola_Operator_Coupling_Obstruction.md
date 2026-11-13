# Cone Derivation Ledger v15.907 — Outer acceleration parabola and Schwinger coupling obstruction

**Date:** 2026-11-13 US Eastern. **Track:** Gravity. **Parents:** Paper C Schwinger dictionary, Sandbox diameter–secant machine v14.550, transition-parabola v15.869, Gravity v15.895–906. **Live HEAD checked immediately before this ledger write:** 50db55e4f14753d8c8a6dbdf2b0ed0c52ace213f. Target confirmed absent. Strict additive-only; leave Suzuki, Audit, Sandbox and prior certified objects unchanged.

**Question:** Does the outer n+k circle's geometric acceleration parabola, plus the inner sqrt(n) turning chord, generate the Schwinger J_+-driven transitions dynamically without inserting a coupling?

**Status:** [D] exact operator-valued chord and circle identity; [N] geometric diagonal operators do not create the off-diagonal ladder; [D] explicit two-sided drive matrix-element check; [O] field-derived coupling, time law and physical phase locking.

## Gate 598 — exact chord as a squared transition operator

On an outer circle of fixed pair diameter D=n+k, the standard Paper C basis is |a,b> with a=n−1, b=k, a+b=D−1. Define J_+=a_1^dagger a_2 and J_-=a_2^dagger a_1, J_z=(N_a−N_b)/2. The exact geometry in the factor-grid unit u is

X=u(J_z+1/2), T=u D/2, Y²=u²(N_a+1)N_b.

Thus the **operator identity** on the fixed-D sector is

**Y²=u² J_- J_+ =T²−X²**,

with **<a,b|J_-J_+|a,b>=nk**, and the raising matrix element is **<n,k−1|J_+|n−1,k>=sqrt(nk)**. This is exact and generalizes the sqrt(n) chord at k=1. It is the squared chord (positive diagonal operator) that equals the squared ladder coefficient; Y itself is not identical to J_+.

The outer circle's crown-osculating parabola Y≈T−X²/(2T) is likewise a function of diagonal T,X. The original factor-row parabola Y²=u²+2uX is valid only on the k=1 row and not as a global operator identity across all k.

## Gate 599 — geometrical parabola does not select a transverse drive

Any self-adjoint Hamiltonian constructed solely as a function of the commuting outer-circle geometry operators H_geom=f(X,Y²,T), even with a coordinate-dependent potential suggested by the outer crown parabola, obeys **[H_geom,J_z]=0** and is diagonal in the fixed-D basis. Consequently it cannot generate transitions between distinct (n,k) states. Its diagonal energies could yield phase differences if a physical energy assignment f were independently supplied, but cannot by themselves produce the J_+ changes in secant ratio.

An explicit transverse term H_int=hbar g J_x, J_x=(J_++J_-)/2, does induce transitions with matrix elements (hbar g/2)sqrt(nk); the coupling g has dimensions inverse seconds and is a separate input. A geometric parabola's curvature fixes no such g, operator orientation, or time law. The exact oscillator/Rindler/Cone clocks remain underdetermined.

## Gate 600 — second-neighbor leakage at (n,k)=(4,1)

At fixed D=5, the state (4,1) corresponds to Fock |3,1>. J_+ leads to |4,0> with coefficient **sqrt4=2**, but J_- also leads to |2,2> with coefficient **sqrt6**. Thus a symmetric J_x drive is not a two-state model: to lowest nontrivial time order, the total population leakage is

**P_out(t)=(g t)²(4+6)/4+O((g t)^4)=5(g t)²/2+O((g t)^4).**

The right-endpoint channel alone contributes (g t)², and the lower neighbor contributes (3/2)(g t)². Isolating one direction requires an additional selection rule, boundary, polarization, spectral detuning or engineered coupling; the diameter/secant geometry does not do so.

The global n+1 quantum phase cycles of the isotropic H0=hbar omega_*(N+1) are common-phase winding, not an explanation for transitions: H0 commutes with J_±. With any diagonal gap H_geom, a J_x term can cause off-resonant/rabi exchange, but its strength and energy splitting need physical specification.

## Gate 601 — what remains of the outer acceleration parabola

Retain three distinct objects: (i) the full outer (X,Y) action circle and its local geometric osculating parabola, (ii) the factor-row k=1 parabola connecting sqrt(n) to the n+1 boundary, and (iii) the physical acceleration-versus-time parabola associated with a specified radial force, as in the conditional v15.900 rotor. Neither (i) nor (ii) automatically yields the physical transition generator (iii). An actual coupling could arise from an off-diagonal term in the K4+Maxwell matter stress/action, but must be derived, with its power and dimensions checked, rather than equated with a curvature.

**Reproducer:** research-notes/k4_outer_parabola_schwinger_coupling_v15_907.py, commit 50db55e4f14753d8c8a6dbdf2b0ed0c52ace213f. Executed locally with SymPy: PASS for D=2..9 on x²+y²=T² matrix identity, J_-J_+ diagonal chord, commutators, sqrt(nk) ladder coefficient and D=5 two-way leakage. Independent Audit pending.

**NEXT:** (1) test explicit candidate off-diagonal interactions motivated by genuine physical acceleration/matter fields and compare them with ordinary polarization-driven Schwinger SU(2), (2) compute whether any dimensionless and model-independent ratio of transition amplitudes survives changing unknown g, and (3) compare with independently calibrated outer-circle parabola curvature and inner sqrt(n) turning point, without identifying geometrical action-circle radii with SI length, velocity or action by fiat.

**HANDOFF Audit/Muse:** independently check orientation of J_+ and J_- under Paper C's x=N_a+1 dictionary; J_-J_+ versus J_+J_- ordering, completeness of the diagonal obstruction, and whether any real field-derived coupling can break it. Existing Audit Round 571 process gaps v15.888,890,895,897 standalone reproducers remain open.
