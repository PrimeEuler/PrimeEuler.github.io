# Cone Derivation Ledger v15.810 — Gravity: gauge-controlled local scalar/vector/tensor round-trip photon, free-mirror and clock transfer

**Date:** 2026-11-12 US Eastern. **Parents:** v15.760 and v15.787–788 full Fermi geodesic curvature, v15.792 audit-confirmed repair, v15.793 finite-arm spatial proxy, v15.794 independently audited conventional TT photon transfer. **Status:** [D] exact first-order round-trip light time with free mirror endpoints and emitter proper clock on a locally flat background for arbitrary Fourier scalar/vector/tensor metric perturbations; [D] pure-diffeomorphism zero test, tensor-only v15.794 recovery and independent numeric photon-path quadratures; [N] any new Cone gravitational interaction or finite-distance K4 sourced waveform; [O] FLRW propagation and plugging in physical matter-driven metric source histories. **Live HEAD immediately prewrite:** adeaba7262ef4ac2aa43a8ddae2e6b3eefc4c5a9. Target path absent; additive-only; frozen Suzuki assets untouched.

## Gate 413 — include all three operational terms, not only a null-ray metric integral

In local Minkowski (−+++) with prescribed small plane Fourier metric perturbations exp[−iωt+i k·x], choose one freely falling arm of coordinate length L in unit direction u and define λ=k·u, H=u^i u^j h^TT_ij, V=u^i V_i:

**h00=−2Φ**, **h0u=−V**, **huu=−2Ψ+H**.

For a photon emitted at t_e at the beam splitter, transmitted to a freely falling mirror, and returned to the same freely falling beam splitter, the first-order emitter-proper round-trip time change requires (i) outgoing and returning *causal photon* null-ray integrals, (ii) endpoint position changes of both beam splitter and mirror, and (iii) the emitter-clock lapse integral. Any one term alone is coordinate-dependent and not an operational signal.

Let **F(z)=exp(i z/2)sinc(z/2)**, **x=ωL**, **y=λL**. The photon integrals evaluated on unperturbed paths are

**O=L exp(−iωt_e)(−Φ−Ψ−V+H/2)F(y−x)**,

**I=L exp(−iωt_e)exp[i(y−x)](−Φ−Ψ+V+H/2)F(−y−x)**.

The beam splitter proper-time correction is

**C=2L exp(−iωt_e)Φ F(−2x)**.

The mirror and beam splitter are geodesic, NOT coordinate-static for arbitrary Φ,V. In this Newtonian/vector metric gauge the linear longitudinal acceleration is

**δx_u''=−∂u Φ+∂t V**.

For a harmonic source its coefficient is **A=−i(λΦ+ωV)**; with initial coordinate displacements and velocities zero at t=0 in this gauge, define **J(t)=[1−exp(−iωt)−iωt]/ω²**. The round-trip endpoint correction is

**M=A[2 exp(iy)J(t_e+L)−J(t_e)−J(t_e+2L)]**.

The complete emitter-clock result is **δT_RT=O+I+C+M**. Initial mirror preparation (the choice at t=0) is a physical part of the instrument setup; its coordinate values transform under a change of gauge.

## Gate 414 — exact pure-coordinate-wave null and conventional TT recovery

A pure linear coordinate transformation of flat spacetime, with vector field **ξ^0=T exp(−iωt+iλu·x)** and **ξ^u=U exp(−iωt+iλu·x)**, produces a nonzero apparent metric **hμν=−∂μ ξν−∂ν ξμ**. Because the underlying spacetime is still flat, the physical round-trip proper-time perturbation must be zero when the mirror and beam splitter worldlines transform with ξ, rather than being falsely reset to zero coordinate displacement.

Write **E=exp[i(λ−ω)L]**, **R=exp(−2iωL)**. Direct exact integration gives the pure-gauge photon term, worldline correction and clock term, with a common exp(−iωt_e) factor:

**O+I=(T−U)(E−1)+(T+U)(R−E)**,

**M=U(2E−1−R)**,

**C=T(1−R)**.

Their sum vanishes **identically** for arbitrary T,U,E,R. This is a strong gauge null: no phantom gravitational signal is created by coordinate transformations if endpoint worldlines and clocks are consistently included. In the generic wave implementation, setting Φ=Ψ=V=0 returns the v15.794 conventional TT transfer exactly; the first-order static transverse-shift limit also vanishes for a local flat-space reciprocal arm.

## Gate 415 — independent numeric integrals, limitations and originality

The committed reproducer evaluates three nontrivial complex scalar/vector/tensor Fourier input configurations. For each, the analytic F-phase result is compared with **independently numerically quadrature-integrated** outbound/inbound null-ray paths and clock term plus exact mirror Green-solution endpoint motion; the difference is <2×10⁻¹². This is independent of the pure-gauge symbolic identity and the TT-only control.

**Reproducer:** research-notes/k4_local_scalar_vector_tensor_photon_mirror_clock_v15_810.py, additive commit **8dfbc88abdc3e00184f1710958cfe0eb114f0e9d**. Locally executed with SymPy/Numpy/SciPy to PASS for the exact pure-diffeomorphism cancellation, numerical quadratures, TT reduction and static vector check. Original K4 and Suzuki objects preserved.

**Important limitation:** This is a *locally Minkowski* harmonic metric **transfer functional**, not a waveform sourced by K4 matter, nor an FLRW long-arm detector. The pure-gauge cancellation applies when the *same physical mirror worldlines* are transformed with the coordinate change. Assigning zero coordinate mirror perturbations again in the transformed gauge would describe a different physical preparation. Complex Fourier coefficients must be paired with their conjugates to form real observations.

**HANDOFF — independent audit:** verify the null-ray sign, each arm endpoint time, beam splitter proper clock factor, geodesic acceleration −∂uΦ+V', exact pure-diffeomorphism cancellation and gauge-compatible mirror Cauchy data, TT control and independent numeric quadratures. No G calibration or physical amplitude claim.

**NEXT:** repeat on exact coasting FLRW conformal metric with Hubble-damped mirror geodesics and expanding-emitter clock, then insert the *same* evolving compact canonical source's metric histories into a finite-distance two-arm time-domain calculation. Matched EH+solid detector residual remains exactly zero if no additional Cone operator is independently derived.
