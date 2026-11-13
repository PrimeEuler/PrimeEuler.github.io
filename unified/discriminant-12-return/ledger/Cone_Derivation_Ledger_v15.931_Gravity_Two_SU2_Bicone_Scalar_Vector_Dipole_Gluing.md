# Cone Derivation Ledger v15.931 — Glued two-SU(2) bicone: scalar/vector pair operators and hydrogen cross-shell branches

**Date:** 2026-11-13 US Eastern. **Track:** Gravity/EM bicone. **Parent:** staged `arxiv/note-bicone-dipole-alpha/Note_BiconeDipole_FineStructure_v1.0.tex`, Gravity v15.919–920 E1 lifetime benchmark, quarter-refined boundary v15.930. **Live master HEAD immediately prewrite:** bf32191153e20112c8984de755a9c18caddbf415, and ledger target checked absent; additive only, existing staged work and certified lanes unchanged.

**Owner question:** Does gluing two Schwinger SU(2) cone/parabola factor-pair systems into the bicone supply a true dipole operator rather than the one-cone defective quarter-grid shift?

**Status:** [D] standard two-spin coupled SO(4) representation; [C] explicit auxiliary 4-boson pair-operator model; [D] rotational triplet and scalar commutation, conditional on canonical boson model; [N] raw matrix amplitudes alone do not reproduce physical Coulomb radial ratios; [O] physical SO(4,2)/KS normalized dipole and relation to the quarter G carrier.

## Gate 674 — physical angular-momentum content from bicone gluing

Take the **already-staged** pair of ordinary Schwinger spins J,K with equal j=(n−1)/2 on the hydrogen Coulomb principal shell n. The product space H_n=V_j⊗V_j has n² states, and under L=J+K decomposes as the physical orbital irreps l=0,1,...,n−1. The second combination A=J−K supplies the properly normalized hydrogen Runge–Lenz symmetry, and [L,L], [L,A], [A,A] generate SO(4). This is standard hydrogen dynamical symmetry, recorded in the staged paper. This is NOT identical to gluing the *defective*, open q=2 quarter-grid fragments: their representations and Casimir structures differ.

## Gate 675 — a rotational scalar in addition to the staged dipole triplet

Use a concrete canonical four-boson realization (a1,a2) and (b1,b2). The coupled rotational generators are L+=a1†a2+b1†b2, Lz=(Na1−Na2+Nb1−Nb2)/2. Form triplet annihilators

**R_- = a1 b1, R_0=(a1 b2+a2 b1)/sqrt2, R_+=a2 b2**

and scalar singlet annihilator

**S=(a1 b2−a2 b1)/sqrt2**.

Under the *specific* total L conventions in this realization, [Lz,R_q]=q R_q, [L+,R_-]=−sqrt2 R_0, [L+,R_0]=−sqrt2 R_+, [L+,R_+]=0, while [Lz,S]=[L+,S]=0; lowering relations follow by rotation and direct computation. The minus signs are associated with annihilation/dual-spinor conventions and are not automatically standard physical spherical-tensor phase conventions. The staged note already has R and a warning about naive spinor-bilinear identification as a physical position vector; preserve that caution. Neither R nor S has the correct *physical* length normalization by itself.

Each pair annihilator removes one quantum from each copy, j→j−1/2, corresponding to **hydrogen n→n−1** inside this chosen Fock dictionary. Hence R_0 can give angularly allowed n→n−1 vector branches. The composite **S R_0**, which lowers both spins twice, transforms as a vector under total L and permits n→n−2 branches. This is a constructive family of ordinary angular operators, not a unique physical dipole; higher shell differences require further singlet factors or SO(4,2).

## Gate 676 — three lifetime-benchmark channels have auxiliary nonzero amplitudes

In the normalized standard Clebsch–Gordan coupled states in this model, the elementary boson matrix elements are (phase conventions fixed by standard real CG coefficients)

**<1s|R_0|2p,m=0>=1**,

**<2s|R_0|3p,m=0>=sqrt2**,

**<1s|S R_0|3p,m=0>=sqrt2**.

These are dimensionless **bosonic amplitudes**, not electric dipole lengths. Under their respective matrix-element conventions, the physical nonrelativistic radial Coulomb integrals in units of a0 from v15.920 are

**r_21=128sqrt6/243**, **r_31=27sqrt6/128**, **r_32=27648sqrt3/15625**.

After dividing the raw amplitudes above, a common normalization calibrated only at 2p→1s would require **channel-dependent** further coefficients. Taking r21 as the common initial scale, the relative multipliers for r31 and r32, after dividing the respective auxiliary sqrt2 amplitudes, are

**C31/C21 = 6561sqrt2/32768**, **C32/C21 =26244/15625**.

They are different. Angular symmetry/AM–GM geometry alone does **not** determine their ratio; the physical SO(4,2) radial representation, n-dependent Coulomb widths, KS measure and actual parity are independent indispensable inputs. Putting those coefficients in by hand would fit, not derive, the measured hydrogen lifetimes.

## Gate 677 — quarter-grid scope and experimental path

The successful ordinary-SU2×SU2 bicone packaging resolves an algebraic problem of shell content and angularly allowed vector pathways that a single SU2 or defective quarter fragment cannot supply. It does **not** repair the defective quarter-grid's commutator itself nor derive the cross-sector EM↔G operator or a universal physical frequency. The 3p total lifetime benchmark is reproduced only with the already-known radial dipoles and ω³ factors; these are conventional Coulomb/quantum electrodynamics comparator facts.

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_bicone_dipole_pair_triplet_scalar_v15_931.py`, commit **bf32191153e20112c8984de755a9c18caddbf415**. It constructs CG coupled states n=1..4, pair annihilator blocks, verifies triplet/scalar covariance and nonzero channel elements, and checks the distinct radial-factor ratios. **External Audit pending**, especially checking phases and the staged paper's caution about physical tensor interpretation.

**Next:** Place the q=2 quarter-grid *observable lattice* relative to the two ordinary Schwinger cones' transition parabolas, distinguishing geometric interleaving of factor rows, formal Casimir offsets, and actual EM physical vector measurement. Do not conflate the quarter Casimir with ordinary spin-j Casimir or claim observed gravity coupling merely from geometric coincidence.
