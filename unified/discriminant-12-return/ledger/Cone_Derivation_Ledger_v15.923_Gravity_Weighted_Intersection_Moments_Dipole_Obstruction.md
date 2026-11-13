# Cone Derivation Ledger v15.923 — Weighted hyperbola/parabola intersection moments and the cross-shell dipole obstruction

**Date:** 2026-11-13 US Eastern. **Gravity/EM geometry lane.** **Parents:** v14.550 diameter–secant machine, v14.767 power-grid scaling, v15.906–923 fixed-sum Schwinger and hyperbola intersections, v15.919–920 EM radiative lifetimes and cross-shell E1 matrix factors; owner's legacy `webgl/index.html` page. **Live HEAD immediately before write:** 7685c85b8a2501e6563810ee0f97719c05b9a10d; ledger target checked absent. Strictly additive; no modifications to old WebGL, certified, Audit/Sandbox or Suzuki files.

**Owner's target:** Determine whether *weighted* (not merely counted) parabola/hyperbola intersections on the AM–GM cone directly reproduce physical transition matrices, particularly independently measured hydrogen dipole strengths, without inserting measured matrix elements.

**Status:** [D] exact divisor-function moment identities and signed cancellation; [N] independent symbolic/arithmetic sweep over products 1..89; [N] no uniquely determined cross-shell E1 operator follows from these geometric moments; [O] derivation of the normalised physical SO(4,2) hydrogen dipole from the geometrical pair variables, including KS measure and dynamical radial scale.

## Gate 647 — all oriented intersections are arithmetic moments

At legacy t=1 and constant product N>0, every ordered positive-integer factor pair ab=N marks a signed point **X=(a−b)/2, Y=sqrt(N), T=(a+b)/2**. The full oriented intersection set includes *both* signs of X (the involution a↔b), with X=0 counted once for square N. Define `d(N)=sum_(k|N)1` and `sigma_p(N)=sum_(k|N)k^p`. Direct exact algebra gives

**sum_pairs 1=d(N)**,

**sum_pairs X=0**,

**sum_pairs X²=[sigma_2(N)−N d(N)]/2**,

**sum_pairs Y²=N d(N)**,

**sum_pairs T=sigma_1(N)**,

**sum_pairs T²=[sigma_2(N)+N d(N)]/2**.

Thus `sum (X²+Y²−T²)=0` holds globally as well as pointwise. All odd X moments vanish because the oriented pair involution reverses X without changing the scalar weight. The leading squared-moment identities are not independent new spectral constants: they are combinations of classical divisor sums.

For N=12, oriented pairs (12,1),(6,2),(4,3),(3,4),(2,6),(1,12), yielding **sum X²=69**, **sum Y²=72**, **sum T²=141**, **sum T=28**. These are exact, parameter-free arithmetic results, positive evidence for the owner's claim that many *geometrical* matrix coefficients share an AM–GM root.

## Gate 648 — scaling in the legacy division parameter

For division t>0, original WebGL uses u=1/t for each integer mesh factor. The physical slice Y²=N then intersects the original integer-factor mesh if ab=N t². Apply the entire moment dictionary with **integer product P=N t²** to the unscaled integer pair (a,b), while the physical coordinates are (X,Y,T)=(X_integer/t,sqrt(P)/t,T_integer/t). Consequently, for example

**sum X²=[sigma_2(P)−P d(P)]/(2t²)** and **sum Y²=N d(P)**.

Do not equate these counts with d(N) except t=1 or when an independently justified renormalization of the slice simultaneously changes N. The mere use of the speed-axis label m/s would require an independently supplied physical velocity unit u in m/s to give the moments SI dimensions.

## Gate 649 — why these moments do not uniquely predict a radiative transition operator

A sum of scalar positions/weights on a shell, or a diagonal operator formed from the fixed-shell geometric quantities X,T,Y², cannot supply a nonzero transition matrix element between **different oscillator shells**. In the Paper C isotropic Schwinger realization, `[N_total,X]=[N_total,T]=[N_total,Y²]=0`, hence for distinct D,D' the operator block **P_D f(X,T,Y²) P_D'=0** for every polynomial/function well defined in the commuting operators.

This is a precise, scoped no-go, not a claim that the full geometry forbids transitions. A *newly specified cross-shell operator* may be introduced (for example the established, physically normalized SO(4,2) dipole acting between hydrogen principal quantum numbers), but the divisor intersection set does not determine its matrix elements: zero and arbitrary nonzero cross-shell blocks are both compatible with all the same fixed-shell moment observations. The physical dipole's parity, Δl=±1, radial wavefunction overlaps, normalization and photon energy ω_if are necessary independent ingredients.

The v15.920 hydrogen data give an exact strong constraint: **2p→1s**, **3p→1s** and **3p→2s** require three distinct radial E1 factors, and the observed 3p total lifetime sums two branches. A proposed raw rule `A∝nk`, or any unspecified sum of unweighted/symmetric divisor intersections, has neither the cross-shell labels nor the angular selection rules to reproduce those three values uniquely. Allowing freely chosen signed weights to fit them would be a parameterization, not a derived prediction.

## Gate 650 — precise constructive next test

Instead of searching all moment combinations after seeing the dipole answers, start with the actual **parabolic hydrogen `|n_1,n_2,m>` states and KS measure** already present in `arxiv/note-bicone-dipole-alpha/Note_BiconeDipole_FineStructure_v1.0.tex`. Map the legacy parabola row and AM–GM pair `(a,b)` to its shell and parabolic quantum numbers with correct state normalizations, *then* write the physical dipole as an operator with explicit shell-changing generators. Check the three v15.920 radial factors without using them as normalization inputs. If such a map yields exactly conventional SO(4,2), report geometric correspondence; only a nonstandard coupling-independent residual counts as a new Cone observable.

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_intersection_moments_dipole_obstruction_v15_923.py`, add-only commit **7685c85b8a2501e6563810ee0f97719c05b9a10d**. Independent SymPy arithmetic run PASS N=1..89 on d, σ1, σ2, odd moments and cone identity; code also encodes a finite two-shell diagonal/off-diagonal underdetermination control. External Audit pending.

**Verdict:** The owner's original AM–GM picture does unify the scalar **shape** of the pair lattice, local circle radii and ordinary Schwinger coefficients. Summing its geometric intersections yields rigorous classical divisor arithmetic. A measured EM **decay time**, however, is a matrix element of the genuine cross-shell electromagnetic dipole, and is not determined by those scalar moments alone. This is a specific underdetermination result, not a rejection of the broader physical realization program.
