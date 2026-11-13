# Cone Derivation Ledger v15.918 — Coherent-state velocity measurement bridge: exact parity obstruction

**Date:** 2026-11-13 US Eastern. **Track:** Gravity. **Parents:** Gravity v15.884 physical velocity-axis declaration, v15.906–914 two-circle Schwinger operators and Fermi detector, and External Audit Round 572/573 (v15.915/917); Gravity v15.916 audit repair. **Master HEAD immediately before this ledger write:** 61fc07c92c86e4e8938de190510125ea7956b008. Target confirmed absent. Additive only; historical Audit, Suzuki, Sandbox and certified files unchanged.

**Versioning note:** External Audit Round 573 landed its own `v15.917_External_Audit_Round_573.md` at c0898a29e135c161ea755b81469d3ec1ab4d7beb, during preparation of this coherent measurement gate. Thus this gate takes next-free ledger **v15.918** to prevent a sixth collision. Its already committed and unambiguous reproducer filename contains `v15_917` (commit 61fc07c92c86e4e8938de190510125ea7956b008), but it belongs to **ledger v15.918**. The Audit has verified and closed both v15.916 repairs.

**Question:** Can a physical measurement of signed oscillator velocity (m/s) be recovered from the Cone velocity-coordinate operator X_Cone=u(J_z+1/2), even for coherent states that have nonzero mean physical momentum? Test the *full distribution*, not just stationary fixed-shell expectation values, and retain actual Fermi tidal dynamics.

**Status:** [D] exact parity-based no-go for all time and all X spectral outcomes within the two-mode quadratic detector model; [N] numerical propagation, energy conservation and opposite physical velocities; [O] different physical Hilbert-space embedding or an independently sourced velocity-sensitive phase operator.

## Gate 628 — two physical states share every X outcome but have opposite velocity

For the physical isotropic oscillator with dimensionful M, omega0, hbar and quadratures q_i,p_i, coherent state |alpha1,alpha2> has mean momentum **<p_i>=sqrt(2M hbar omega0) Im(alpha_i)**, while the Paper C Cone operator is **X_Cone=u[(N1−N2)/2+1/2]**, with u in m/s by the owner's calibration hypothesis. Choose two coherent states **|psi_+>=|+i b,0>**, **|psi_->=|−i b,0>**, for b>0. Their physical velocity expectations are equal and opposite:

**<v_1>_±=±sqrt(2hbar omega0/M)b, <v_2>_±=0**.

But both have *identical* number occupation probabilities on every pair (N1,N2), hence exactly identical **X_Cone probability distributions** and **<X_Cone> =u(1+b²)/2**. In particular, for b=1, <X_Cone>=u while <v_1>_±=±sqrt(2hbar omega0/M). A universal monotonic or even arbitrary function of a measured X spectral outcome therefore cannot reconstruct the sign of v_1 for both states.

## Gate 629 — the distinction survives arbitrary quadratic tidal evolution

Let physical joint parity Π=exp[i pi(N1+N2)]. Then Π|psi_+>=|psi_-> and **Π X_Cone Π†=X_Cone**, while **Π p_i Π†=−p_i**. Under the full leading Fermi tidal detector Hamiltonian of v15.914,

**H=(p_1²+p_2²)/(2M)+(M/2)[omega0²(q_1²+q_2²)+A(q_1²−q_2²)+2B q_1q_2]**,

one has **[Π,H]=0** for every time-dependent or constant physical A,B. Therefore, at every time t,

**Pr_+(X_Cone=x;t)=Pr_−(X_Cone=x;t)** for *every* spectral value x, and **<p_i/M>_−(t)=−<p_i/M>_+(t)**.

The equality of the full distribution follows at once from parity commuting with every spectral projector of X_Cone. It is independent of a finite Fock cutoff, the RWA, or the particular SU(2) dark-node pattern. Actual velocity, unlike the occupation imbalance X_Cone, is odd under parity. An additional parity-odd reference such as a measured quadrature/phase readout could distinguish the pair, but that is new physical information beyond the Cone X label.

## Gate 630 — independent exact-Gaussian propagation benchmark

For numerical test hbar=M=omega0=1, b=1, A=0.04, B=0.08, use the positive 2×2 stiffness matrix **K=[[1.04,0.08],[0.08,0.96]]**. Each coherent state has initial q=(0,0), p=(±sqrt2,0), covariance (1/2)I_4. The full quadratic Hamiltonian evolves their means exactly through the symplectic normal-mode propagator. Their covariance matrices are identical at every time (opposite means), and the complete distributions of X are equal by the parity proof. The mean and exact total energy in dimensionless units are:

| t | <v1>_+ | <v1>_- | <X_Cone>/u (both) | E (both) |
|---:|---:|---:|---:|---:|
| 0 | 1.41421356 | −1.41421356 | 1.00000000 | 2.00000000 |
| 2 | −0.63506165 | +0.63506165 | 0.97935155 | 2.00000000 |
| 8 | −0.40178034 | +0.40178034 | 0.88688262 | 2.00000000 |
| 16 | −0.91316606 | +0.91316606 | 0.64434398 | 2.00000000 |
| 24 | +0.78008500 | −0.78008500 | 0.37739035 | 2.00000000 |

This is conventional quantum harmonic and Fermi tidal physics, with imposed dimensionless detector parameters. The velocity values can be converted into SI only after M, hbar, omega0 are physically supplied. The arbitrary u conversion can give X measured units m/s but cannot make it the particle's true signed momentum/velocity.

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_coherent_velocity_measurement_bridge_v15_917.py`, commit **61fc07c92c86e4e8938de190510125ea7956b008** (number in filename allocated before Audit secured ledger v15.917). Independently executed in local Python/NumPy/SciPy: PASS of both opposite physical velocity readouts, equal X expectation, conserved energy, symplectic normal-mode dynamics, initial Poisson number distribution and all-time parity proof. Independent external Audit of THIS gate pending.

## Gate 631 — interpretation and physical research boundary

**Positive:** The Cone's fixed sum/difference factor lattice remains a correct and useful physical **pseudospin/occupation imbalance** coordinate in the ordinary two-mode detector; its off-diagonal `sqrt(nk)` factors match physical exchange amplitudes exactly and kinetic quadratic observables project to it. A complete physically sourced tidal detector can carry the nested circles and their normal modes.

**Negative:** For this detector, *no state-independent calibration of X alone, whether constant u or nonlinear map f(X), yields literal signed physical velocity for all coherent states*. The no-go holds even if u is assigned SI m/s, at every time under the full quadratic tidal Hamiltonian. Thus the prior conditional claims that d<X>/dt is actual physical acceleration are disallowed for this detector, absent a new velocity-sensitive measurement operator. The geometry fixes velocity-labelled station intervals but not physical particle speed, acceleration, clock, G or a new dimensionless gravity observable. This result does not rule out a different independently derived physical realization of the Cone's velocity-axis hypothesis.

**NEXT:** Test an explicitly phase-sensitive two-observable readout (p_i and X, or J_y plus independent reference), with physical detector resolution and source phase; determine whether any coupling-independent response remains after conventional oscillator tomography. Alternatively seek a physical dynamical embedding whose intrinsic X operator is momentum-like and whose symmetry/selection rules match measured velocity, but do not relabel a number operator as velocity by units alone.

**HANDOFF Audit/Muse:** verify parity argument for all X spectral projectors, coherent-state physical velocity formula, baseline squeezed-vacuum covariance contribution, exact energy E=2 and sample table. Acknowledge Audit Round 573 closed v15.916 reissue/repair; no continuing process correction from that round.
