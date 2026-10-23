# Gravity common symplectic and response-selector test

Date 2026-10-23. Gravity lane. Parents v14.620, v14.760-761, v14.773-777. Exact toy-model deductions, not a derived physical EM/gravity action.

## Gate A: common symplectic normalization does not fix Hamiltonian [D]

On canonical phase space with \(\omega=dq\wedge dp\), consider \(H_{a,b}=\frac12(ap^2+bq^2)\), \(a,b>0\). Hamilton's equations are \(\dot q=ap,\ \dot p=-bq\), giving \(\ddot q+abq=0\) and \(\Omega=\sqrt{ab}\). The symplectic form and hence canonical \([q,p]=i\hbar\) are identical for all a,b, while the frequency and physical energy gap \(\hbar\Omega\) change. Therefore a common action quantum and common symplectic manifold do not select a unique dynamical response.

The rescaling \(q\mapsto\lambda q,\ p\mapsto p/\lambda\) is canonical; a and b transform reciprocally under re-expression while their product \(\Omega^2\) is invariant. It cannot alter the physically measurable frequency. This prevents confusing a coordinate normalization choice with a coupling determination.

## Gate B: two-sector oscillator and susceptibility [D]

Let sectors i=EM,G have \(H_i=\frac12(a_ip_i^2+b_iq_i^2)-J_iq_i\), with independently specified force source \(J_i\). For static equilibrium \(p_i=0,\ q_i=J_i/b_i\), the static susceptibility is \(\chi_i=\partial q_i/\partial J_i=1/b_i\). Common symplectic quantization fixes neither \(b_{\rm EM}/b_{\rm G}\) nor \(\chi_{\rm G}/\chi_{\rm EM}\).

The numerical values of cross-sector susceptibility ratios are meaningful only after the source variables J_i and measured q_i are independently calibrated and assigned compatible units. A shared \(\hbar\) by itself supplies neither calibration.

## Gate C: quantization integrality and the action metric [D/O]

For a compact phase space, prequantization requires the symplectic flux class \([\omega/(2\pi\hbar)]\) to have integer periods. On a compact 2-sphere, a class of area \(2\pi N\hbar\) has integral Chern number N. This topologically restricts a symplectic class but does not uniquely fix a compatible metric, Hamiltonian, propagation speed, or separate gauge/Einstein-Hilbert kinetic coefficient. The Cone pair-circle identity yields dimensionless coordinates and half/quarter offsets, but gives no derivation of an action metric coupling them to physical source response.

## Next discriminating gate [O]

Construct a concrete action-derived quadratic source-response operator, with one independently calibrated source normalization and boundary condition, and show whether the unit-circle/symplectic integrality forces its coefficients. A proposed relative EM/G response must be invariant under canonical reparameterization, gauge rescaling, and reference-length changes and must not insert measured G as input. The known factor-four divisor density is not automatically a force ratio.

No Suzuki/Weil carrier equivalence and no G derivation claimed; Suzuki and far-tail files reserved.
