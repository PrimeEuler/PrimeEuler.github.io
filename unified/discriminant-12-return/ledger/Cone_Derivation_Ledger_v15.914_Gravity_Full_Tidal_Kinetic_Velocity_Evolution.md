# Cone Derivation Ledger v15.914 — Full sourced-form tidal oscillator: kinetic imbalance, true velocity, and inter-circle leakage

**Date:** 2026-11-13 US Eastern. **Gravity track.** Parents: Paper C two-mode Schwinger realization; Gravity v15.876 conventional Fermi gravitational oscillator; v15.905–913 outer fixed-D/secant ladder, Fermi tidal interaction and kinetic-imbalance physical operator. **Live master HEAD immediately before write:** 8fefff9830cadf50bec7d73959f78b3e34e24252. Target checked absent. Additive only; preserve protected Suzuki, historical, Audit and Sandbox files.

**Goal:** Evolve a real physical two-dimensional test oscillator under the *full* leading local Fermi-normal tidal interaction (including number-changing terms) and compare the measured velocity and kinetic observables with the Cone's proposed m/s coordinate X=u(J_z+1/2). Do not insert any novel Cone force or arbitrary curvature-weighted ladder Hamiltonian.

**Status:** [D] exact parity no-go for physical mean velocity and exact normal modes; [N] converged explicit full-Fock evolution and nonzero shell leakage; [D] full versus fixed-shell kinetic projection; [N] no independently selected n+1 velocity clock, G-free Cone correction or sourced field amplitude.

## Gate 624 — physical model and exact parity

Take a physical planar isotropic detector coordinate vector q=(q1,q2) in meters, momentum p=(p1,p2), mass M, and baseline angular frequency omega0. The leading local freely falling tidal Hamiltonian is

**H = [p1²+p2²]/(2M) + [M omega0²/2](q1²+q2²) + [M/2][A(q1²−q2²)+2B q1q2]**,

with the physical electric tidal curvature components A,B in s^-2, and with a prescribed time-independent tracefree tidal matrix E=[[A,B],[B,−A]]. This is ordinary Fermi-normal gravitational physics, *not* a new gravitational source obtained from the Cone/K4 action. Time dependence is possible but not required for the present comparator. Stability demands **sqrt(A²+B²)<omega0²**.

The Hamiltonian is even under q_i→−q_i, p_i→−p_i; it commutes with joint oscillator excitation parity (−1)^(N1+N2). A literal physical Cartesian velocity v_i=p_i/M is odd under this parity. Therefore any initial definite-parity Fock state (including |3,1>, representing pair (4,1) on outer D=5) obeys the **exact all-time result <v1>(t)=<v2>(t)=0** even with complete N→N±2 coupling. This does not mean zero velocity variance, kinetic activity or probability currents: it is a symmetry statement about first moments. An odd-parity admixture, parity-breaking driving force, or coherent displaced state is needed for nonzero mean physical velocity.

## Gate 625 — physical kinetic observables and complete Fock benchmark

Define **Kdiff=(p1²−p2²)/(2M)** and **C=p1p2/M**. The fixed-D projection from v15.913 is **P_N Kdiff P_N=hbar omega0 J_z**, **P_N C P_N=hbar omega0 J_x**, whereas **P_N p_i P_N=0**. Full H contains number-changing terms ΔN=±2 in addition to fixed-D **P_N H_tidal P_N=(hbar/omega0)(A J_z+B J_x)**. Consequently the total time-evolved state can populate multiple outer D=N+1 circles. The projected kinetic relations are exact on each individual shell but the *full* kinetic expectation also includes the ±2 coherence; full <Kdiff> is not generally <Jz> of just the initial D=5 sector.

Dimensionless numerical benchmark: hbar=M=omega0=1, A=.04, B=.08, initial |3,1>. Complete Hamiltonian in total Fock occupation cutoff Nmax=13, 105 states. Units for time are 1/omega0; A and B are in omega0². Reproducible full evolution gives:

| t | <Kdiff> | <C> | P(N=4) |
|---:|---:|---:|---:|
| 0 | 1.000000 | 0.000000 | 1.000000 |
| 2 | 1.065685 | 0.169925 | 0.983440 |
| 8 | 0.885347 | 0.269041 | 0.983175 |
| 16 | 0.360191 | 0.441848 | 0.991414 |
| 24 | −0.211271 | 0.670651 | 0.995264 |

At all displayed times both literal physical <p_i/M> are exactly zero by parity (numerically zero to precision). Full probability normalization holds. The nonzero and time-varying probability outside N=4 exhibits ordinary *inter-circle transitions*: the original fixed n+k circle is not a conserved exact subsystem of the full spatial quadratic tidal dynamics, only of its number-conserving/RWA projection. This is not itself a Cone gravity signature.

Fock truncation sensitivity: at t=24, the kinetic imbalance is −0.21114681238 for Nmax=9, −0.21127016480 for 11, −0.21127096604 for 13, and −0.21127097019 for 15. The N=4 probability converges near .9952641441. This excludes a numerical cutoff artifact at the reported precision.

## Gate 626 — exact physical normal modes and fixed-shell comparator

The canonical frequency-squared matrix is **omega0² I + E**. Its eigenvalues are **omega0² ± sqrt(A²+B²)**. Therefore the exact stable physical normal-mode angular frequencies are

**omega_±=sqrt[omega0² ± sqrt(A²+B²)]**.

For the benchmark, **omega_+=1.04376372762**, **omega_−=0.95423125127**, and **omega_+−omega_−=0.08953247635**, all in units of omega0. This beat rate is a physically meaningful relative time scale of the conventional oscillator, but explicitly depends on the tidal amplitude; it is *not* n+1 and does not follow solely from the velocity-axis node spacing.

The conventional fixed-N effective Hamiltonian is **H_RWA/hbar = (A/omega0)J_z + (B/omega0)J_x**, with angular precession **g_RWA=sqrt(A²+B²)/omega0=0.0894427191** in this benchmark. Full and projected kinetics agree in the weak-tidal limit to leading order but differ because of counter-rotating shell-changing contributions. The observed finite differences do not constitute a new geometric force or frequency.

## Gate 627 — scientific verdict and next physical gate

**Positive:** The physical Fermi tidal Hamiltonian provides an actual field-origin transverse interaction, a mathematically complete dynamical network of inner sqrt(nk) amplitudes, and a physical measured kinetic-imbalance/cross-momentum observable. It allows population to redistribute both along the original diameter–secant ladder and across nearby diameter shells. This is a rigorous conventional physical comparator.

**Negative:** Literal physical mean velocity remains zero for the parity-eigenstate test while the Cone X coordinate's projected expectation can change. Their direct identification remains invalid within this oscillator realization. The m/s normalization of X alone cannot turn a kinetic-imbalance readout into a particle velocity or acceleration. The tidal source magnitude, detector mass, mode frequency and conversion between geometry and actual velocity are not fixed by the Cone; the entire test is reproducible with ordinary GR/quantum mechanics. No Cone-specific dimensionless gravitational observable survived the matched conventional-control subtraction.

**Reproducer:** research-notes/k4_full_tidal_kinetic_velocity_v15_914.py, additive commit **8fefff9830cadf50bec7d73959f78b3e34e24252**. Independent local Python/NumPy/SciPy execution, parity and covariance checks, exact quadratic operator projection, shell occupancy and norm, convergence scan Nmax=9,11,13,15, and exact normal-mode frequencies. External independent Audit pending.

**NEXT:** The meaningful bridge test is *measurement theory*: construct an explicit operational protocol for reading a signed velocity m/s from the Cone X shell label, and determine whether it measures particle momentum, velocity variance, energy imbalance, phase-group velocity or an auxiliary state-space coordinate. Test a coherent displaced physical oscillator (nonzero <p_i>) against the Cone spectrum; see whether any state-independent, dimensionful calibration u maps both classical and quantum transition dynamics without violating canonical commutators or parity. In parallel retain the existing K4 five-helicity sourced model and explicitly match its detector tidal response to the conventional Fermi baseline before claiming nonstandard physics.

**HANDOFF Audit/Muse:** independently confirm parity argument, full ±2 shell transitions and cutoff convergence, factor in `P_N p1p2/M P_N=hbar omega0 J_x`, exact frequency splitting, and that this conventional physical Hamiltonian has no separately derived Cone-only coupling.
