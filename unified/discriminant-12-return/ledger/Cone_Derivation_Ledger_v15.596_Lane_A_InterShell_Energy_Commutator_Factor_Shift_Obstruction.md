# Cone Derivation Ledger v15.596 — Lane A: inter-shell energy-commutator gate and native factor-shift obstruction

**Date:** 2026-11-10. **Parents:** v13.583, v13.595, v15.180, v15.274, v15.572–580, v15.595; v15.581 independent audit of v15.578–580. **Status:** [D] exact shell-operator and factor-coordinate identities; [C] Hamiltonian choices conditional; [O] actual field-coupled creation/annihilation operator. **Live HEAD checked:** dd48f4652d0559363910448c4a1fc1bd8f846876; no v15.596 collision. Additive only; frozen Suzuki/far-tail untouched.

## 1. Boundary witness and energy commutators [D/C]

For odd-quarter j=(2n−1)/4 and j'=j+1/2 define the *candidate* (v15.595)

T_j=sqrt(c)(|j',j'><j,j−1/2| + |j',−j'><j,−j+1/2|), c=j+1/4.

Its source norm T_j†T_j=c(P_++P_-)=2E_j is the exact v15.572 boundary Casimir deficit. On a **direct sum of shell state spaces**, define the diagonal geometric shell radius \(\mathcal R|j,m\rangle=(j+1/2)|j,m\rangle\) and scalar Casimir-label observable \(\mathcal C|j,m\rangle=j(j+1)|j,m\rangle\). Then

[mathcal R,T_j]=(1/2)T_j,
[mathcal C,T_j]=(j+3/4)T_j.

In particular for a Hamiltonian **assumed** of form H=f(mathcal R) or H=f(mathcal C), T_j is an energy-eigenoperator and its energy gap is the corresponding spectral difference. But the cone has not *selected either Hamiltonian as its physical shell energy*, and neither Casimir label nor geometric AM radius can be called an emitted photon energy simply from this identity.

Split T_j=T_+ + T_- according to upward and downward target. With the magnetic label M|j,m>=m|j,m>, [M,T_+]=+T_+, [M,T_-]=−T_-; **T_j itself is not a single eigenoperator of M**. Under the *conditional* H=alpha mathcal R+beta mathcal C+omega M, each leg has a distinct energy:
[H,T_±]=(alpha/2+beta(j+3/4)±omega)T_±.
For the already-verified transverse magnetic-driver H0=-g Jx (v13.595 / v15.580), \(J_{x,j'}T_j-T_jJ_{x,j}\) is not proportional to T_j. Thus the recorded driver does not make T_j a fixed-frequency absorption/emission transition.

## 2. Native factor-coordinate obstacle to source-defined creation [D/O]

Use the cone's factor/occupancy coordinates u=j+m, v=j−m on a refined shell (coordinate labels; **odd-quarter values are not an established physical integer Schwinger Fock occupation**). The upper outgoing state m=j−1/2 has (u,v)=(2j−1/2,1/2). Its proposed next-shell extreme target j'=j+1/2, m'=j' has (u',v')=(2j+1,0). The required coordinate change is:

(Δu,Δv)=(+3/2,−1/2).

The lower outgoing branch requires the factor-exchanged change (−1/2,+3/2). Under a native **positive** row/column-creation-only semigroup, both coordinates are nondecreasing, so neither transition is reachable. If both raising and lowering moves by 1/2 are permitted, the address is reachable as *three* raises in one factor and *one* lowering in the other. That composite path is not unique as an operator: ordering, coupling strengths, normalization, and phases need a new rule. The observed sqrt(c) coefficient of T_j cannot be inferred from destination coordinates or monotone shifts alone.

This obstruction is consistent with the earlier ladder's loss of fixed-shell SU(2): a source-defined shell-changing coupling would need more than the geometric presence of next-shell nodes. The shift-composite does not establish a physical electromagnetic interaction or flux.

## 3. Reproducer, status, audit handoff

Independent SymPy reconstruction of shell Jx and boundary maps checked j=1/4,3/4,5/4,7/4,9/4,13/4: T†T=2E, both scalar commutators, the ±M commutators, non-proportional transverse-driver commutator, and factor-coordinate changes. Script and report in local archive cone_energy_shell_shift_gates_54_55.zip.

**HANDOFF** target external-audit; type inter-shell energy-operator and monotone-shift obstruction; status open; check all commutators and verify 'no monotone factor growth' without overclaiming no possible composite shift; compare the physical Hamiltonians (KS/Coulomb and Schwinger) with any claimed shell energy law. No changes to production or frozen Suzuki.

**Next gate:** derive a factor-changing *non-monotone* operator with source-defined amplitudes from an existing oscillator algebra, or certify an obstruction from integrality / selection / conservation. The rank-two witness map is a target for matching, not an already physical energy carrier.
