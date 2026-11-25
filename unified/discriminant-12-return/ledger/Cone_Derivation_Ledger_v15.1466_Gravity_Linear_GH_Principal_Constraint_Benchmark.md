# Cone Derivation Ledger v15.1466 — Generalized-harmonic linear 3+1 Einstein principal-symbol benchmark, gauge and energy controls

**Date:** 2026-11-25 Eastern. **Track:** Gravity/Cone. **Parents:** v15.1453 exact nonlinear Einstein–H² initial-data constraints, v15.1459 first nonlinear inhomogeneous short-time raw ADM evolution, v15.1463 spatial oversampling improvement, v15.1464 longitudinal zero-speed ADM Jordan obstruction. **Status:** [EXACT PASS] harmonic-gauge linearized Einstein equations reduce to diagonalizable wave propagation for the trace-reversed four-dimensional metric perturbation; [N PASS] TT physical and pure-gauge on-shell null modes satisfy the harmonic gauge constraint, and periodic TT Fourier wave energy is constant to rounding; [NEGATIVE] this does NOT construct, test or certify the full nonlinear 3+1 generalized-harmonic Einstein–H² gauge evolution, nor does it treat the higher-derivative Weyl–F–H² operator. **Audit Round 648** committed v15.1461 independently confirmed v15.1459–1460. Additive; Sandbox v15.1465 preserved.

## Gate 1390 — replace raw ADM's longitudinal Jordan block with wave-like gauge propagation

Use signature `η=diag(-1,1,1,1)`, trace-reversed metric perturbation `bar h_{μν}=h_{μν}−η_{μν}h/2`, and harmonic gauge constraint `C_ν=∂^μ bar h_{μν}=0`. In linearized vacuum general relativity, the gauge-fixed metric field equations are `□bar h_{μν}=0`. With a prescribed **conserved** first-order matter stress tensor T_{μν}, the linear sourced form is `□bar h_{μν}=−2κT_{μν}`, and divergence gives `□C_ν=−2κ∂^μT_{μν}=0`. Thus zero initial C and its compatible first time derivative propagate as zero at this order; generic *off-shell* sigma stress violates the condition, as established v15.1451, so the nonlinear sigma equations must be solved to supply a consistent matter source.

At spatial Fourier wave number k>0, introduce a pseudo-differential first-order state (k bar h, ∂t bar h) for each metric component. The principal generator is `P(k)=[[0,k],[-k,0]]`, an exactly skew-symmetric 2×2 matrix with semisimple eigenvalues ±ik and conserved positive quadratic norm `|∂t bar h|²+k²|bar h|²`. This avoids the **non-diagonalizable** raw unit-lapse ADM principal block recorded v15.1464. This is a standard **linear generalized-harmonic** hyperbolicity property, not a theorem for a particular nonlinear numerical formulation with arbitrary gauge source/constraint damping. Matter H² fields themselves have standard wave principal part and may be appended to the hyperbolic matter system at the level of the Einstein–sigma two-derivative action, but the complete nonlinear constraints and source dynamics remain separate tasks.

## Gate 1391 — symbolic gauge Ward and independent Fourier wave

A plane wave with covector `p_μ=(-ω,0,0,k)` and a pure-gauge vector amplitude ξ_ν generates a trace-reversed metric perturbation proportional to `p_μξ_ν+p_νξ_μ−η_μν (p·ξ)`. Its harmonic gauge divergence satisfies the *exact algebraic identity* `p^μ bar h_μν = (p²) ξ_ν`; for an on-shell null wave ω=k this vanishes even though ξ may be nonzero. Independent physical TT polarization with `bar h_xx=−bar h_yy` also satisfies C=0. Symbolic SymPy checked all four components and the skew principal generator, not just a numeric example.

For an illustrative periodic TT wave traveling in z, set `f(z)=sin z +0.32 cos(3z)` at t=0; evolve exactly by FFT phase `f(z−t)`. Its time/spatial gradient energy norm (spatial mean `f_t²+f_z²`) equals `1+9×0.32²=1.9216` for all times. Local independently executed script `/mnt/data/cone_gate/gh_linear_constraint_wave_v15_1466.py` generated:

| t | Fourier energy | max |f_t+f_z| |
|---:|---:|---:|
| 0 | 1.921599999999999 | <2×10^-14 |
| .3 | 1.921599999999999 | <2×10^-14 |
| 1.7 | 1.9215999999999989 | <2×10^-14 |
| 3 | 1.921599999999999 | <2×10^-14 |

**Additive committed equivalent source:** `research-notes/k4_gh_linear_constraint_wave_v15_1466.py`, SHA **3d0e70b3cc5b26944201b9b1a4912ee31e913bc9**. Local code and committed equivalent are independently authored and the exact committed bytes await independent Audit execution.

**AUDIT:** independently derive the trace-reversal gauge Ward identity and physical TT transversality, verify skew first-order wave symbol, check treatment of four residual coordinates/pure-gauge modes and the conserved Fourier wave norm. Confirm that the principal-symbol result is *linear* and does not establish nonlinear matter Einstein constraints or eliminate the separate v15.1420 Weyl–F–H² characteristic warning.

**NEXT:** build a full **nonlinear 3+1 generalized-harmonic Einstein–H²** time step with prescribed gauge source, stable hyperbolic gauge constraint damping and actual nonlinear initial data v15.1453, then repeat N24/32/40 spatial and RK4 timestep convergence, including longer T=.04. Complete higher-derivative Weyl–Maxwell metric variation and EFT order reduction are subsequent gates, not silently incorporated here. G remains an input.
