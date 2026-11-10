# Cone Derivation Ledger v15.602 — Lane A: every rational mesh refinement, residue-chain topology, Casimir defects and generalized cross-shell maps

**Date:** 2026-11-10. **Parents:** Paper C Quantum Realizations v1.1, Casimir Null Diamond v2.1, v15.135/140/180, v15.572–574, v15.595–601. **Status:** [D] exact general theorem, [C] chosen family of geometric cross-shell witnesses, [O] physical sector selector, energy Hamiltonian and interaction normalization. **Prewrite live HEAD:** f960187bae7b2505f2e618547af38760614efba1; no v15.602 collision or prior duplicate. Additive only. Suzuki frozen/production untouched.

## 1. Exact refinement conventions and odd/even N caveat

For integer q≥1 define mesh spacing h=1/q and half-step vertex offset ±h/2=±1/(2q). q=1 is original ±1/2, q=2 is the ±1/4 interlay; q=3,4,... gives infinite extensions, not necessarily a new physically identified sector. The user's alternative shorthand ±1/N corresponds to N=2q **even** if interpreted as a half-cell offset. Geometry can put a vertex at ±1/N for *odd* N as well, but the corresponding h=2/N does not divide an original Δm=1 transition. If N is odd, Δm=1 does not connect nodes of one such uniform mesh; a second staggered coset or a different step/generator is required. Do not use the same symbol N for both vertex denominator and shell-index L.

## 2. General q,L theorem [D]

Let L≥1 integer, j=L/(2q), dimension L+1 with states m_i=-j+i/q for 0≤i≤L. Retain the *original* unit-step AM–GM raising law J+|m> = sqrt((j-m)(j+m+1))|m+1> only if m+1 appears in the refined shell (equivalently i+q≤L); J-=J+† and M=diag(m_i). Define Jx=(J++J-)/2, Jy=(J+-J-)/(2i). Let
D=[J+,J-]-2M,
E=j(j+1)I-[Jx²+Jy²+M²].

These operators are diagonal, with entries
D_ii = U_i - V_i,
E_ii = (U_i+V_i)/2,
U_i = (j-m_i)(j+m_i+1) if i+q>L, else 0;
V_i = (j+m_i)(j-m_i+1) if i-q<0, else 0.
These are nonnegative, so E≥0. Reflection R|i>=|L-i> obeys RDR=-D and RER=E. The exact 'Casimir' of the **defective** original unit-step ladder is j(j+1)I−E, NOT an assumed SU(2) Casimir for fractional j.

The transition graph consists of c=min(q,L+1) chains indexed by index residues mod q (singleton chains allowed). There is exactly one fully closed chain if and only if L is divisible by q, since only then the ±j endpoints share a residue class; all other chains are open. Thus for L≥q, (q | L) implies one closed and q−1 open, otherwise zero closed and q open. For L<q all L+1 chains are isolated/open. This recovers q=1 fully closed, q=2 even/odd shell-index dichotomy, and general odd/even q without inventing a universal parity-only selector.

Each side has a=min(q−1,L) nonzero omitted **directed** transitions with squared weights
w_r = r(L+q−r)/q², r=1,...,a,
mirrored at the opposite end. There are 2a directed omissions, but several can share a source for small shells. E is supported on the union of those sources; for q>1,L≥1 its rank is min(L+1,2(q−1)), which need not equal 2a. The sum of the Casimir deficits is
tr E = Σ_{r=1}^a w_r =
[a(a+1)(3(L+q)−(2a+1))]/(6q²).
If L≥q−1, this becomes (q−1)(3L+q+1)/(6q). q=2 produces precisely the earlier missing-edge c=j+1/4 when L odd; q>2 generally yields more than two nonzero missing legs and different strengths.

## 3. Every-q cross-shell witness [D/C]

Define j' = j+(q−1)/q. For r=1,...,a define the upper leg from source m=j−r/q to target m'=j+1−r/q with amplitude sqrt(w_r), and its mirror lower leg from m=−j+r/q to m'=−j−1+r/q with the same amplitude. All targets lie on the refined j' shell. Targets are mutually orthogonal within each branch and the upper/lower images are disjoint (positive vs negative m'); where a source has two omitted directions, they land on orthogonal target states. Their sum defines a *chosen* geometric T_{q,L}:H_j→H_{j'} and exactly

T†T = 2E.

At q=1, T=0. At q=2 this is the rank-two v15.595 map. At higher q it has generally larger rank. With shell-label operators R_shell=(j+1/2)I and C_shell=j(j+1)I on a direct-sum tower, put d=(q−1)/q. Then [R_shell,T]=dT, [C_shell,T]=d(2j+d+1)T. Splitting T into upper and lower legs gives [M,T_up]=T_up and [M,T_down]=−T_down. These are geometric eigenoperator relations, **not** a physically selected energy Hamiltonian or radiative emission law.

## 4. Native Paper C dictionary and the choice of generator

Paper C uses integer n1,n2≥0, Schwinger J+=a1†a2, physical spin j_phys=(n1+n2)/2, magnetic m_phys=(n1−n2)/2, and SU(1,1) squeeze K+=a1†a2†. The quarter refined shell m=±1/4 is not a conventional physical Schwinger weight. The auxiliary embedding n1=i,n2=L−i gives physical spin L/2=qj and m_phys=q m, making a **different closed nearest-neighbor representation**. More generally define B+ with refined nearest-neighbor step h=1/q and weights sqrt((j-m)(j+m+h)); then Kz=qM, K+=qB+ obey exact standard SU(2) commutators as spin L/2, with no E or D boundary defect. The **defective** unit-step J and the **closed** refined-step B must not be equated. Neither the native dictionary nor refinements alone selects the physical gravity q=2 or a new G value.

## 5. Exact validation, scope and handoff

An independent SymPy reproducer tested all q=1,...,6 and L=1,...,13: **78/78** exact matrix tests of D/E, support, graph topology, mirror and trace; **78/78** exact rectangular T†T=2E tests. Includes short-shell/source-overlap exceptions, q=1 normal SU(2), q=2 parity cases and q=3+ novel multiple missing legs. Conversation artifact: `cone_general_refinement_gates_64_66.zip` containing REPORT.md and reproduce.py.

**Next gates:** (1) audit generalized rank/trace and T construction independently; (2) study refinement compatibility q→kq and whether T_{q,L} respects power-map weld / lattice inclusion; (3) check whether any source-selected Hamiltonian, not the chosen auxiliary Schwinger embedding, distinguishes q=2 experimentally.

**HANDOFF** target external-audit, sandbox, gravity; status open; type all-q rational mesh boundary theorem; verify q,L residue classification, rank and trace, q=1/q=2 limits, generalized T orthogonality and T†T=2E, native Paper C mismatch, and odd N vertex offset obstruction. No Suzuki production/frozen change.
