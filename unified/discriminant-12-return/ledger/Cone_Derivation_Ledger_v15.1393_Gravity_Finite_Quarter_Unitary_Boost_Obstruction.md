# Cone Derivation Ledger v15.1393 — Finite quarter-grid SU(2) carrier cannot realize a nontrivial unitary continuous SO+(2,1) hyperboloid boost symmetry

**Date:** 2026-11-24 Eastern. **Gravity/Cone.** **Status:** [D exact structural no-go] the finite-dimensional closed q=2 refined carrier of archived v15.972–973 is an ordinary finite SU(2) representation and does **not** admit a nontrivial *unitary finite-dimensional* representation of the noncompact SO+(2,1) hyperboloid boost group; [N PASS] explicit exact SymPy finite-carrier tests D=2..6 and the general Hilbert–Schmidt trace proof; [NEGATIVE] the continuous H² nonlinear sigma field of v15.1380–1392 cannot be identified with the physical dynamics of that **same** finite quarter Hilbert carrier simply by rescaling the ladder or assigning a Casimir; [OPEN] separate infinite-dimensional unitary target carrier, effective classical sigma coordinates, physically broken boost lattice, independent action and measurable parameter. **Immediately preledger latest source SHA:** da58a6e73c18e21009fcbe7f387ed712757303fb. Strictly additive.

## Gate 1313 — general finite-dimensional unitary noncompact boost no-go

Write the Lie algebra `so(2,1)` in the Hermitian-observable convention as three hypothetical Hermitian generators `K0,K1,K2` obeying

`[K0,K1]=i K2`, `[K0,K2]=−i K1`, `[K1,K2]=−i K0`.

Trace cyclicity gives `Tr(K0[K1,K2])=Tr([K0,K1]K2)`. Using the brackets, the left side equals `−i Tr(K0²)` and the right side equals `+i Tr(K2²)`. Thus

`Tr(K0²)+Tr(K2²)=0`.

On a finite-dimensional **positive-definite Hilbert space**, any Hermitian K has nonnegative `Tr(K²)=sum eigenvalues²`, so both K0 and K2 must vanish. Then the commutators force K1 to vanish. Therefore the **only finite-dimensional unitary representation of the connected noncompact SO+(2,1) algebra is trivial**. This proof is independent of numerical truncation, the chosen quarter radius and any free sigma coefficient. It is NOT a no-go for an infinite-dimensional unitary principal/complementary/discrete-series representation, a nonunitary finite-dimensional mathematical representation, or a classical nonlinear sigma target. It is a direct constraint on equating the old finite q2 quantum carrier with exact continuous unitary hyperboloid boosts.

## Gate 1314 — reproduce on the exact closed q2 SU2 carrier and identify the nonunitary continuation

The archive's **true closed refined-step Schwinger carrier** at fixed integer D≥2 has spin `J=(2D−1)/2` and dimension 2D (not the incompatible formal geometric spin `(2D−1)/4`). Its Hermitian ordinary unit-step generators Jx,Jy,Jz obey SU2. Co-scaled q2 generators `J_i/2` instead obey `[J_x/2,J_y/2]=i(J_z/2)/2`; they do not magically acquire the sign flip of a boost group.

For an explicit algebraic, **nonunitary** finite-dimensional so(2,1) continuation define `K0=Jz`, `K1=i Jx`, `K2=i Jy`. These satisfy the three so(2,1) brackets exactly but K1,K2 are **anti-Hermitian**, violating the physical Hermitian-generator convention for unitary real-parameter boost transformations. The trace identity becomes `Tr(K0²)=−Tr(K2²)>0`, perfectly consistent because K2 is non-Hermitian; it does not establish physical unitary boosts.

Actual executed Python SymPy examples (D,dimension,spin,Tr K0²,Tr K2²):

| D | dimension | J | Tr(K0²) | Tr(K2²) |
|---:|---:|---:|---:|---:|
| 2 | 4 | 3/2 | 5 | −5 |
| 3 | 6 | 5/2 | 35/2 | −35/2 |
| 4 | 8 | 7/2 | 42 | −42 |
| 5 | 10 | 9/2 | 165/2 | −165/2 |
| 6 | 12 | 11/2 | 143 | −143 |

Every SU2 bracket, continued so(2,1) bracket, adjoint test, trace cyclicity and sign relation passed exactly without numerical tolerance.

**Executed file:** `/mnt/data/cone_gate/k4_quarter_finite_unitary_boost_no_go_v15_1393.py`, exact SymPy source. New additive GitHub equivalent `research-notes/k4_quarter_finite_unitary_boost_no_go_v15_1393.py`, SHA **da58a6e73c18e21009fcbe7f387ed712757303fb**, pending independent Audit replay.

## Gate 1315 — implications for the physics selector

This independently strengthens v15.1185's **finite-lattice set preservation** obstruction: the finite shell does not admit nontrivial common boosts preserving every discrete factor pair, and now no finite positive-Hilbert-space closed q2 representation could support a faithful noncompact boost algebra either. These are two distinct obstructions: one about exactly preserving a finite geometric node set and one about unitary quantum representation theory.

The continuous H² sigma interaction v15.1380–1392 remains a legitimate *chosen* generally covariant additional classical field theory and gives a leading Maxwell source, but its continuous SO+(2,1) target symmetry and finite q2 archived SU2 state Hilbert space **cannot be identified one-to-one without adding extra physical structure**. The sigma model could have continuous classical coordinates with ordinary canonical quantum field Hilbert space (typically infinite-dimensional) without violating this no-go. A genuinely finite quarter-grid Hamiltonian can instead have only discrete boost-symmetry remnants or select a different noncompact infinite-dimensional carrier. None of these alternatives is selected by the arithmetic grid itself.

**AUDIT:** independently verify the Hermitian-generator sign convention and trace-cyclicity proof, the exact q2 physical carrier dimension/spin, and explicit nonunitary continuation. Distinguish classic SO+(2,1) target covariance from having an SO+(2,1) representation on one finite q2 Hilbert space. Do not present this as a no-go for curvature-dependent wave interactions or infinite-dimensional quantum gravity.

**NEXT:** physical half-grid–quarter-grid bridge must choose either (i) a discrete unitary intertwiner with a finite q2 carrier and explicit symmetry breaking, or (ii) an independently defined infinite-dimensional boost carrier/quantization and an action coupling to EM/curvature. Test either option against the radius/free-coupling degeneracy of v15.1387 and the precisely matched same-enlarged-EFT comparator. The current attractive continuous H² interaction alone does **not** fix an intrinsically quarter-grid gravitational coupling.
