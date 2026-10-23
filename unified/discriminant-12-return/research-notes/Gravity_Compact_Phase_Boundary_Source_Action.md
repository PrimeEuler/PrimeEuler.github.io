# Gravity common-circle boundary-response action: explicit variational test

Date 2026-10-23. Gravity lane. Parents v14.620, v14.760–761, v14.773–778. [D] exact conditional model statements; [O] physical EM/gravity embedding not derived. Suzuki/far-tail artifacts untouched.

## Compact circle field and physical wall [D]

Fix a physical one-dimensional interval s∈[0,L] of independently measured proper length L>0, and a dimensionless phase field θ(s)∈R/(2πZ). Pin θ(0)=0. Define a *static effective energy* (not relativistic gauge/gravity field action)
\[
E_{\kappa,j}[\theta]=\frac{\kappa}{2}\int_0^L(\theta'(s))^2ds-j\sin\theta(L),\qquad\kappa>0.
\]
The bounded source potential is genuinely 2π periodic and has a fixed physical source parameter j (energy units). κ has energy×length dimensions. Thus the unit-circle period cannot be freely rescaled while retaining the same phase coordinate, but κ is not fixed by compactness or ħ.

Stationarity under variations δθ(0)=0 yields θ''=0 and the natural boundary condition
\[
\boxed{\kappa\theta'(L)=j\cos\theta(L)}.
\]
Write Θ=θ(L). The unique linear interior extremal is θ(s)=sΘ/L; local extrema therefore solve
\[
\boxed{(\kappa/L)\Theta=j\cos\Theta}.
\]
For sufficiently small |j|, the local branch through Θ=0 exists by the implicit function theorem. Its zero-source response is
\[
\boxed{\chi=\left.\frac{\partial\Theta}{\partial j}\right|_{j=0}=\frac{L}{\kappa}}.
\]
The on-shell second derivative of the minimized energy is \(\partial_j^2 E_{\min}|_0=-L/\kappa\). These are physical candidate source responses *within the stated effective model*, contingent on independently measured j and L.

## Invariant spectral/geometric interpretation [D]

The harmonic bulk equation with pinned end has a boundary Dirichlet-to-Neumann stiffness K_DN=κ/L. It is measurable by force/angle response. If a pair of sectors shares the same θ period, same proper L and the same source calibration j, yet has independent κ_EM,κ_G>0, then
\[
\boxed{\chi_G/\chi_{\rm EM}=\kappa_{\rm EM}/\kappa_G}.
\]
No constraint from circle topology or a common ħ fixes this ratio. Assigning κ_G=κ_EM/4 would generate 4 by assumption; it would not derive that ratio from the Cone half-grid or a physical field action.

## Winding and same quantization, different dynamics [D]

For a circle-valued field on a *closed* spatial ring of circumference L, \(\theta(L)-\theta(0)=2\pi m\) on a lift, m∈Z. With no source, the minimum static energy in that sector is
\[
\boxed{E_m=\frac{\kappa}{2L}(2\pi m)^2=\frac{2\pi^2\kappa m^2}{L}}.
\]
Thus integer winding is universally fixed, while the energy cost of winding depends on free κ. This closed-ring example is a distinct boundary-value problem from the pinned-interval response above; they share the same compact target but must not be conflated.

## Rescaling and calibration checks [D/O]

Changing the unit used to describe s changes the numerical κ and L together; the measured ratio L/κ (angle per energy) stays invariant. A reparametrization of θ that alters its period is *not* an admissible relabeling of the same fixed U(1) representation. Even after fixing this representation, κ remains an unconstrained dynamical modulus. A source j with different physical calibration in each sector destroys comparability; assuming shared j is a hypothesis demanding an actual common coupling to the probe.

No claim that this 1D effective action equals Maxwell, Einstein-Hilbert, a CFS limit, or a Suzuki operator. No Newton constant determined.

## Falsifiable next contract [O]

Derive κ_EM and κ_G as coefficients of the boundary Dirichlet-to-Neumann action from a *single* independently specified microscopic or bulk theory, with common source calibration, a common proper-length wall, and a controlled regulator. Check that the same topological phase normalization plus the Cone h=1/2 embedding truly forces κ ratio instead of taking it as input. Vary boundaries and physical probes. This is the missing dynamical selector.
