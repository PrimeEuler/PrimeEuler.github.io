# Cone Derivation Ledger v15.936 — Rank-two tidal-tensor comparator on the n=2 glued bicone

**Date:** 2026-11-13 US Eastern. **Track:** Gravity / bicone physical-tensor tests. **Parents:** v15.905 and Gravity v15.931–935; earlier v14.700 spherical-rotor rank-two benchmark; Fermi-normal tidal comparator v15.912–914. **Live master HEAD immediately before ledger write:** b249010ec223f48e712e3e3d37894fe38410c67d. Target verified absent; additive only. No historical, Audit, Sandbox, Suzuki or certified changes.

**Question:** Does a genuinely rank-two tensor acting on the two spin-one cones at the n=2 rest/Casimir crossing isolate the coupled spin-two channel? Does the AM–GM construction yield any nonstandard tidal coupling ratio without new model inputs?

**Status:** [D] exact rotational tensor, exchange symmetry and spin-sector matrix elements in the chosen auxiliary bicone; [N] no unique spin-two selector or new gravity response from n=2 crossing; [O] physical tidal position-operator bridge and normalized Hamiltonian.

## Gate 693 — define a *specified* rank-two operator, not an ad hoc spin-two projector

At factor-pair n=2, each ordinary Schwinger cone is spin j=1, with single-cone Casimir 2 and the geometric rest-circle radius squared 2. Define coupled total angular momentum **L=J+K**, and the relative vector **A=J−K**. Under L, A transforms as a vector, and under cone interchange J↔K it changes sign. Construct a traceless rank-two Cartesian tensor `Q_ij=(A_i A_j+A_j A_i)/2−delta_ij A²/3`; use its q=0 unnormalized component

**Q_20=3 A_z²−A²**.

This is a Hermitian SO3 quadrupole. The exact matrices satisfy **[L_z,Q_20]=0** and the rank-two highest-weight test **ad_(L_+)³(Q_20)=0**, while **ad_(L_+)²(Q_20)≠0**; its trace vanishes in the nine-dimensional product space. Under cone exchange Q_20 is even: **Swap Q_20 Swap=Q_20**. These statements are normal SU2 tensor algebra, not a field-derived graviton coupling.

## Gate 694 — exact projectors and strengths

Using the v15.935 orthogonal spin-projectors `P_0,P_1,P_2`, with dimensions 1,3,5, define projected blocks `P_s Q_20 P_t`.

The exact **block ranks**, rows s=0,1,2 and columns t=0,1,2, are

`[[0,0,1],[0,3,0],[1,0,5]]`.

The Hilbert–Schmidt squared block norms **Tr[(P_s Q P_t)†(P_s Q P_t)]** are

`[[0,0,32],[0,54,0],[32,0,14]]`.

In standard real coupled CG phases the nonzero **singlet→quintet** amplitude is

**<2,0|Q_20|0,0>=4 sqrt(2)** (square 32).

The fixed-m diagonal amplitudes for the spin-one sector m=−1,0,1 are **(−3,6,−3)**, and for the spin-two sector m=−2,−1,0,1,2 are **(−2,1,2,1,−2)**. The spin-zero diagonal element vanishes. The 0↔1 and 1↔2 blocks are identically zero because Q is even under cone interchange whereas spin-one is odd and spin-zero/two are even. The 0↔2 channel is consistent with ordinary rank-two Wigner–Eckart selection rules. The presence of 1→1 and 2→2 matrix elements means Q does **not** uniquely select total spin two.

These integers and root factors are dimensionless **auxiliary bicone** numbers. Their ratios are fixed by the deliberately selected Q=A_i A_j form, not by observed G, or a newly derived physical tidal tensor.

## Gate 695 — physical gravitational comparator and the unproved operator identification

The standard weak-field Fermi-normal local nonrelativistic tidal Hamiltonian for a localized test mass has the form **H_tidal=(m/2) E_ij x^i x^j** (up to Riemann/sign convention), with E_ij=R_(0i0j) and the trace-free vacuum tidal part transforming as a rank-two spatial tensor. If a traceless gravitational field E_ij is supplied, it naturally couples to **physical position quadrupole x_i x_j−delta_ij r²/3**. The auxiliary `A=J−K` here encodes the normalized Runge–Lenz symmetry of the Coulomb shell, not physical position `x`; identifying `x_i x_j` with `A_i A_j` is an **additional, unproved operator bridge**, and it changes radial/selection-rule matrix elements. The actual gravitational interaction carries an independently specified field strength and physical mass/length, and the EM bicone's fixed n=2 geometry fixes neither. The gravity-sector quarter Casimir formal spectrum remains a separate unresolved representation: this gate uses two **ordinary** spin-one SU2 cones only.

The original n=2 identity **R_rest²=R_C²=2I_9**, with R_transition²=9/4 I, remains a scalar on all 0,1,2 channels; hence it does not distinguish which projected block is driven. Simply applying a rank-two field does not turn spin-2 components into massless helicity±2 gravitons, and the 0↔2 transition is ordinary quadrupole spectroscopy, not a new Cone-dependent selection rule.

## Reproduction and next gate

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_bicone_tidal_rank2_gate_v15_936.py`, additive commit **b249010ec223f48e712e3e3d37894fe38410c67d**. Direct exact SymPy computation independently run locally: all nine-by-nine matrices, projector-block ranks and Hilbert–Schmidt squared norms, singlet/quintet matrix element, triplet/quintet diagonals, angular highest-weight commutator, exchange and Hermiticity checks passed. External Audit pending.

**Scientific verdict:** *positive* the two-SU2 glued bicone supports a rank-two tensor with a nonzero singlet→spin-two channel and exact model-specific amplitudes. *negative* the n=2 circle crossing does not select this tensor or the spin-two channel; the tensor also acts within other allowed spin sectors. No novel G-free tidal ratio, massless graviton dynamics or physical source coupling derived.

**Next discriminating gate:** compute the **actual projected hydrogen position quadrupole** `P_n(x_i x_j−δ_ij r²/3)P_n` (with physical Coulomb/KS normalization) and compare its spin-sector blocks to this auxiliary `Q_ij(A)`. Check whether the ratios differ, and if so quantify the missing radial/representation bridge; no fitting to an observed tidal/graviton signal. For a massless graviton claim require Lorentzian helicity and gauge constraints separately, not just SO3 rank-two covariance.

**HANDOFF Audit:** independently reconstruct Q from relative spin generators; check the 0↔2 amplitude 4sqrt2, block-rank/norm matrices, exchange parity, and the physical x-vs-A identification caveat.
