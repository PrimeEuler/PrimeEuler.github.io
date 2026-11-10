# Cone Derivation Ledger v15.631 — Lane A: Taub–NUT gravitational quarter pair versus quarter-shell holonomy Casimir carrier

**Date:** 2026-11-10. **Parents:** v14.731 gravitational dyon pair and independent Audit Round 338 v14.732, v14.913 correction of weld framing, v15.135 EM/odd-quarter sector parity, v15.602 all-q mesh shell, v15.625–628 Casimir functional-calculus grading and odd-rung construction, v15.630 ordinary rotor SU2 obstruction. **Status:** [D] exact Taub–NUT-derived pair/angular normalization comparisons and exact candidate holonomy-carrier algebra; [C] chosen twisted-holonomy sector construction; [O] physical geometry-to-quantum spin intertwiner, independently sourced EM↔G interaction/coupling and observable. **Immediate prewrite live HEAD:** 4069b47210d0eefb98134f18c066d5fe3bc09187, v15.631 filename collision and overlap searches negative. Additive-only; Suzuki quarter physical weld stays parked and all frozen Suzuki production untouched.

## Gate 128 — restore the actual gravitational quarter already independently derived, but distinguish its carrier

v14.731 (independently verified by v14.732) derives from the Taub–NUT Killing triad and the periodic Misner-time condition the dimensionless gravitational test-mass/NUT pair

**p:=μ c l/ℏ=k/4, k∈Z,** under the stated Taub–NUT worldline conventions and regularity assumptions. The angular-monopole Poincaré term is **s=2p=k/2**. Standard monopole angular harmonics have **j=|s|+n**, n∈Z≥0, hence j∈(1/2)Z and their genuine SU2 Casimir is j(j+1). For k=1 and n=0, s=j=1/2 and **C_phys=3/4**; the square of the gravitational *pair product* is **p²=1/16**; the *independently assigned geometric odd-quarter shell* at j_geom=p=1/4 has **C_geom=5/16**. These are different carriers and three different quantities, and none can be silently substituted for another.

For k>0 and minimal physical monopole angular j=k/2: **C_phys=k(k+2)/4**, whereas the proposed identification j_geom=p=k/4 gives **C_geom=k(k+4)/16**, with exact difference **k(3k+4)/16>0**. The algebraic map j_geom=p is precisely an extra node=state/period-to-spin identification; its physical validity is NOT proved by either existing Taub–NUT route. This does not retract the independently derived quarter-pair quantum or the formal all-mesh Casimir formula. The mechanical separation parameter Λ defined by Λ(Λ+1)=j(j+1)−s² is yet a third label; at minimal angular j=s>0 it satisfies Λ(Λ+1)=s=k/2, not generally Λ=k/4.

## Gate 129 — explicit quarter-sector holonomy carrier exists outside SU2

On the angular universal cover θ∈R, a twisted boundary condition **f(θ+2π)=e^(2πiβ) f(θ)** gives generator K=−i∂θ with eigenvalues n+β, n∈Z. Holonomy β∈R/Z is free unless a specified gauge bundle or boundary law fixes it. Choose four different twisted sectors β_σ=σ/4, σ∈{0,1,2,3}, and restrict to nonnegative n (the positive-frequency/Hardy subspaces, an additional chosen restriction). On the direct sum, label |n,σ⟩ with **j=n+σ/4=(4n+σ)/4**, and assign C_geom=j(j+1). The entire formal quarter-shell spectrum C_{2,L}=L(L+4)/16 is exactly realized. The 2π holonomies are 1,i,−1,−i; the grading χ=e^(16πi C_geom)=(-1)^σ recovers EM vs odd-quarter. The four twist values and Hardy restriction are structural inputs, not derived Taub–NUT requirements. This model is an **axial/flat-holonomy carrier**, not an ordinary SO3/SU2 angular-momentum irrep.

## Gate 130 — isometric quarter-rung shift, boundary obstruction, and free interaction strength

Define W|n,σ⟩=|n,σ+1⟩ for σ<3 and W|n,3⟩=|n+1,0⟩. Then **[J,W]=W/4**, **{χ,W}=0**, and **W⁴** advances the integer n on each β sector. On the complete nonnegative tower, W†W=1 but WW†=1−|0,0⟩⟨0,0|: W is an isometry and not a unitary. No unitary global shift by +1/4 can conjugate a bounded-below J to J+1/4 while preserving its spectrum; the deficiency at the lowest state is necessary. A bilateral n∈Z construction admits a unitary shift but loses positive-j-only carrier, still does not become ordinary SU2. Hermitian H_int=gW+g*W† exists with **arbitrary g**. Operator shift normalization 1 does not fix an interaction coupling, energy splitting, G or any force law.

## Gate 131 — the normalized actual Misner circle has *integer* Fourier mode, despite quarter pair quantum

Taub–NUT periodicity as in v14.731 is **T_t=8π l/c**. With normalized angle θ=ct/(4l), the period is 2π. The ordinary physical time phase is

**exp(-iEt/ℏ)=exp[-i (4lE/(ℏc)) θ].**

Single-valuedness enforces **k=4lE/(ℏc)∈Z** and therefore **El/(ℏc)=k/4**, or μcl/ℏ=k/4 for E=μc². The *natural Fourier momentum on the actual normalized Misner time circle* is k, an integer. It is not automatically the odd-quarter **angular** spin j_geom=k/4, nor does the time-periodicity argument give the spatial/rotational line-bundle holonomy i. Identifying them requires a new geometrically derived intertwiner or gauge patching law. A bare spin structure offers only periodic/antiperiodic signs, whereas ±i twists would require additional flat U1/Z4 holonomy or a nonstandard cover. The time-circle topology therefore supplies the quarter *pair* without automatically selecting our four angular holonomy sectors.

## Reproducibility and next gate

Conversation artifact `cone_holonomy_gates_128_131.zip` contains `reproduce.py` and `REPORT.md`, independently executed and passing exact SymPy tests of Taub–NUT pair versus SU2 spin values, all four holonomy sectors/Casimir/parity, truncated 24-state quarter shift and isometry boundary, and 4π SU2 identity failure at odd quarters. The analytic proofs above are independent of truncation.

**Verdict:** positive: gravitational pair quarter is independently derived (not an arbitrary imported 1/4) and a quarter-Casimir holonomy carrier plus odd-rung shift can be built. Negative: the existing Taub–NUT Killing angular SU2 and Misner time periodicity do NOT by themselves identify that pair quarter with odd-quarter angular spin Casimirs or select the holonomy carrier's interaction strength. The missing condition is an **intertwiner between time-fiber quantization and angular-shell representation** with a specified gauge connection and physical observable.

**HANDOFF** target external-audit, gravity, sandbox; status open. Verify normalized Misner-time Fourier labels, the standard charge-monopole j=|s|+n rule and the three k=1 numerical invariants, direct-sum Hardy holonomy/quarter-rung shift, 4π SU2 obstruction, and nonidentification of time-circle momentum with spin. Preserve v14.731/v14.732's successful independent derivation and v14.913 framing correction. Suzuki physical-quarter weld stays parked; certified frozen far-tail unchanged.

**Next gate:** test Taub–NUT patch overlap transition t_N−t_S=4lφ and its induced energy-eigenmode line-bundle transition (Chern/winding number). Determine whether global patching forces a quarter angular twist or instead exactly reproduces ordinary charge-monopole j half-integer selection; do not assume extra Z4 flat holonomy.
