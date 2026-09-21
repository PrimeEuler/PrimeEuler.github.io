# Cone Derivation Ledger v13.637 — chi_-4 Closed-Avenues Consolidation and Renormalization Handoff

Date: 2026-09-21

Status: consolidation / scope control. No new theorem or numerical certificate is asserted here.

## 0. Live collision and relevance check

The live ledger was read through v13.636 immediately before this write. The controlling audit checkpoint is v13.635. Its chi_-4 recommendation is adopted here: consolidate the two failed direct-zero lanes, freeze them as closed avenues, and move the thread to the renormalization/source-normalization question rather than another ordered-zero repair. v13.636 is the LQG/tetrahedron synthesis and does not collide with this lane.

## 1. What is now closed

### 1.1 Bare J_z nodal carrier as a direct arithmetic-zero model

v13.616/v13.620 tested the Zeeman/J_z nodal compression against the breakpoint construction under independent j- and breakpoint-refinement. The normalized characteristic mismatch did not converge away and the zero branch exhibited strong A dependence.

Decision retained:
[
\boxed{\text{bare }J_z\text{ nodal sampling is rejected as the direct finite carrier.}}
]

This does not reject SU(2) as an abstract finite carrier.

### 1.2 Domain-faithful Friedrichs-Galerkin carrier as a direct ordered-zero model

v13.621 repaired the domain issue with endpoint-adapted parity bases. v13.623 assembled and solved the Galerkin equations independently rather than projecting the breakpoint solution. v13.625 found the finite operator blocks quadrature-stable, with the expected first-kind inverse sensitivity.

Nevertheless v13.627 found
[
r_1(A)\simeq \pi/A
]
and large cross-A drift in the ordered zero list. Thus the repaired carrier also fails the direct ordered-zero-versus-beta-zero test.

Decision retained:
[
\boxed{\text{the repaired Galerkin discretization is numerically sound, but its raw ordered finite-}A\text{ zeros are not an }A\text{-robust arithmetic spectrum.}}
]

## 2. Why another direct-zero repair is not the next gate

v13.629 deleted the arithmetic screw term while retaining the interval, Friedrichs bases, nuisance equations, finite lambda, Neumann inverse term, and characteristic. The free roots already satisfy
[
r_n^0(A)\approx n\pi/A.
]
Therefore the dominant box branch is present before g_{-4} is turned on.

v13.633 then introduced
[
k_\tau=\tau g_{-4}-\lambda N_A,qquad0\le\tau\le1,
]
and continuously tracked the first ten roots. No order exchanges occurred over the sampled homotopy. The shifts in v13.629 are therefore genuine continuous deformations of the free box modes, not an ordered-root relabeling artifact.

Together:
[
\boxed{\text{the }1/A\text{ branch is an endpoint/free branch continuously deformed by the arithmetic kernel.}}
]

Hence further changes of finite carrier or root sorting, without changing the object being compared, would repeat a closed test.

## 3. The open mathematical object

The next question is not whether the first finite-A roots equal Dirichlet-beta zeros. It is which relative or limit-aware object removes the endpoint box contribution while retaining the arithmetic kernel.

A natural candidate to derive, not assume, is a relative characteristic such as
[
\mathcal R_A(z)=\frac{W_A^{\rm full}(z)}{W_A^{0}(z)},
]
with analytic treatment at zeros of the denominator, or an equivalent Fredholm/determinant quotient.

Required before interpreting such an object:
1. derive the exact free/endpoint factor from the finite Friedrichs problem rather than numerically dividing two oscillatory functions;
2. determine whether the quotient is the correct invariant under the nuisance-scalar normalization and phase convention;
3. test A-stability only after that derivation;
4. distinguish a fixed-A quotient from the actual A->infinity object in Suzuki's theorem.

No claim is made here that this quotient is the correct answer.

## 4. Source-normalization blocker

The chi_-4 screw function used throughout this lane remains a direct primitive-character analogue:
[
g_{-4}(t)=
\sum_{n\le e^{|t|}}\frac{\chi_{-4}(n)\Lambda(n)}{\sqrt n}(|t|-\log n)
-\frac{|t|}{2}\left[\psi(3/4)+\log(4/\pi)\right]
-\frac14\left[\Phi(1,2,3/4)-e^{-3|t|/2}\Phi(e^{-2|t|},2,3/4)\right].
]

Its conductor/gamma linear coefficient, signs, and Lerch exponential have not yet been independently derived from the twice-integrated explicit formula at theorem level.

The audit checkpoint v13.635 correctly elevates this from a background caveat to a sequencing constraint:
[
\boxed{\text{source normalization should be certified before another arithmetic A-robustness claim.}}
]

A wrong normalization would not explain away the independently confirmed free n*pi/A branch, but it could materially alter the kernel-dependent remainder that a renormalized characteristic is intended to isolate.

## 5. Handoff / next gate

The chi_-4 lane is therefore frozen at the following boundary:

- CLOSED: bare-J_z direct ordered-zero identification.
- CLOSED: Friedrichs-Galerkin raw ordered finite-A zero identification.
- ESTABLISHED NUMERICALLY: the free endpoint problem carries the n*pi/A branch.
- ESTABLISHED NUMERICALLY: g_-4 continuously deforms those branches without the sampled crossings.
- OPEN: exact source normalization from the primitive chi_-4 completed-L explicit formula.
- OPEN: derivation of the correct free-factor/relative characteristic.
- OPEN: A->infinity behavior of that derived relative object.
- NOT ESTABLISHED: any beta-zero identification or GRH consequence.

Next gate: rederive g_-4 from the completed Dirichlet-beta explicit formula, coefficient by coefficient, and compare that derivation against the frozen implementation before constructing or testing a renormalized characteristic.
