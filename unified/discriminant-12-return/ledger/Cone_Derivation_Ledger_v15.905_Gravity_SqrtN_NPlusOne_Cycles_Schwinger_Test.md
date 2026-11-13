# Cone Derivation Ledger v15.905 — n+1 cycles associated with sqrt(n): actual Schwinger/Casimir test

**Date:** 2026-11-13 US Eastern. **Gravity lane.** Parents: Paper C Quantum Realizations v1.1, gravity v15.895–904, External Audit Round 571. **Live master HEAD immediately before write:** 0a365a0c9086b7aa66217c5d38f49680f21fb497. Target checked absent; additive-only; Audit/Sandbox/Suzuki/certified artifacts unchanged.

**User clarification:** test *n+1 cycles of the sqrt(n) circle*, not an imposed n+1 standing-wave zero count on the outer boundary.

**Status:** [D] exact embedding of pair (n,1) in the existing Schwinger shell with dimension n+1, and exact conditional equal-frequency oscillator phase accumulation; [N] the existing SU(2) Casimir is not n(n+1), quantum global phase is not mechanical orbit, and existing ladder does not force a physical sqrt(n) circle angular velocity.

## Gate 590 — recover exact extant Paper C operator labels

Paper C uses x=n_1+1, y=n_2, N=n_1+n_2, j=N/2, T=(N+1)/2, J_z=(n_1−n_2)/2, with fixed-T SU(2) shell. At the geometric point (x,y)=(n,1) for integer n>=1, the Fock state is (n_1,n_2)=(n−1,1), so N=n and j=n/2. Thus the full SU(2) irrep has exactly **2j+1=n+1 basis states** while its outer Cone transition-circle radius is **T=(n+1)/2**. The exact chord at this state is Y=sqrt(xy)=sqrt(n), and its X=(n−1)/2; hence T²−X²=Y²=n. This recovers all the user's three labels in one existing exact object, without assigning nodes.

The standard SU(2) Casimir here is **j(j+1)=n(n+2)/4** and the completed-square identity is **T²=j(j+1)+1/4**; it is **not** n(n+1). Moreover the individual chord sqrt(n) is not itself the SU(2) Casimir radius. Paper C fixed-T SU(2) ladder motions preserve N; its J_± operators connect different states within the same n+1 dimensional shell, but do not change the shell radius.

## Gate 591 — genuine n+1 temporal quantum phase cycles from a specified Hamiltonian

For **two identical, noninteracting quantum harmonic oscillators** with Hamiltonian H0=hbar omega_* (N+1), the full fixed-N=n shell has E_n=(n+1)hbar omega_*. Consequently every state in that eigenspace has Schrödinger phase exp[−i(n+1)omega_* t], and over one base period T_*=2pi/omega_* the state vector accumulates exactly **n+1 cycles** (phase 2pi(n+1)). This is an exact well-known zero-point + occupation identity under this explicitly chosen Hamiltonian. It is a faithful possible reading of the user's n+1 cycles associated with sqrt(n).

However it is a **global phase** common to all states of the shell and therefore unobservable by itself. The energy gap between neighboring N shells is E_(n+1)−E_n=hbar omega_*, a **single** base frequency; all within-shell J_± transitions are degenerate under H0 and have zero Bohr gap. Thus n+1 phase windings cannot be identified with an emitted n+1 omega_* transition frequency without supplying a reference/interaction that makes the relative phase observable. Nor does this Hamiltonian rotate the point around the circle at angular velocity (n+1)omega_*: H0 commutes with J_i and produces only common phase in a fixed shell.

## Gate 592 — first-transition arc and skater rotor remain distinct

The inner geometric half-arc pi u sqrt(n) is still the half-turn arc of a **one-winding** geometric phase if one is assigned. Schrödinger global phase, by contrast, advances by pi after time pi/[(n+1)omega_*], while spatial state and physical chord need not move. For the thin-ring mechanical skater interpretation of v15.899/904, imposing a physical inner angular rate (n+1)omega_* requires **L_n=M (ell_*u)² n(n+1)omega_*** across n, which is not the ordinary SU(2) angular-momentum eigenvalue hbar sqrt[j(j+1)]=hbar sqrt[n(n+2)]/2. Indeed a fixed-j irrep's eigenvalues carry explicit hbar and mechanical inertia mapping; no derived equality to L_n exists. The Casimir difference is an exact negative discriminator, not a minor normalization correction.

If n+1 denotes m=n+1 **spatial mode winding** rather than temporal phase, a sin(m theta) field on the inner circle has its first zero at arc pi u sqrt(n)/(n+1), not pi u sqrt(n). This is a different hypothesis; the user's latest phrasing motivates testing both but does not make them equal.

## Gate 593 — scope, verification, next experiment

**Reproducer:** research-notes/k4_sqrt_n_nplus1_cycles_schwinger_v15_905.py, commit 0a365a0c9086b7aa66217c5d38f49680f21fb497. SymPy + explicit integer shell enumeration: Paper C mapping, dimensionality, chord/outer radius, Casimir completed square, n+1 phase per base period, and within-shell H0 degeneracy all pass locally; independent Audit pending.

**Positive:** The already-recorded Schwinger construction unifies (n+1) as irrep dimension/outer diameter and sqrt(n) as specific chord, and the ordinary isotropic two-boson H0 supports an n+1-cycle quantum-phase reading.

**Negative:** Geometry alone supplies no frequency in Hz, H0 is a chosen Hamiltonian, global phase alone is not an observable, SU(2) Casimir does not provide the needed n(n+1) mechanical rotor angular momentum, and no restoring/contraction force or EM→G frequency selection follows.

**NEXT:** test observable relative phase of *two shells* with an explicitly named probe that changes N (not fixed-shell SU(2) J_±), and compare with within-shell anisotropic or interaction-split transitions; calculate whether the physical wave first-transition arc is half a spatial circle or half a temporal phase cycle. Then compare coupling to the outer acceleration parabola against a matched ordinary two-oscillator comparator. Avoid identifying energy eigenphase with measurable wave frequency.

**HANDOFF Audit/Muse:** check Paper C (n−1,1) embedding, precise n+1 representation dimension, n(n+2)/4 Casimir vs n(n+1), n+1 global phase, and actual physical transition gaps. Audit Round 571 flagged missing standalone reproducers at v15.895/v15.897, in addition to prior v15.888/v15.890: these process gaps remain open.
