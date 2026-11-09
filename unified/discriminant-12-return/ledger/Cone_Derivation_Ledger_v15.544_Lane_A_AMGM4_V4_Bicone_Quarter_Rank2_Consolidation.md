# Cone Derivation Ledger v15.544 — Lane A: AM–GM(4)/V4, bicone, quarter-Casimir and rank-two transport consolidation

Date: 2026-11-09. Status: [D] exact finite-dimensional identities; [C] conditional identifications across carriers; [O] physical and infinite-spectral intertwiner missing. Disclosure for independent audit, not a promotion of any Standard Model generation/mass result or gravity coupling. Live prewrite HEAD e31aaa004ffb3b512b256b84343bc290d0668a5c, checked with no v15.544 collision. Additive only; Suzuki and far-tail production untouched.

## 1. Already established background, not newly claimed

- v13.436, v13.460, v13.556–557: arithmetic V4 regular module, Hadamard character transform, affine completion V4 semidirect S3 = S4 and its three nontrivial character axes. Generator-level cone correspondence has projective/sign qualifications.
- v14.865–867 and KS bicone note: two SU(2) oscillators, KS equal-number glue, diagonal scalar/triplet channels, relative generators.
- v15.135/CASIMIR, v15.140, v15.143, v15.279: EM half-grid and gravity-only quarter-grid Casimir classes, open-ladder boundary defects, and extreme transition parabolas.
- v15.524–525: rank-two tidal angular matrix elements, independent external audit.
- v13.501–502: arithmetic U(24)->U(12) cover on cone, and **negative** Suzuki mod-24 unit-stratum correspondence.
- v15.461, v15.466–467: separate conditional flat-9 generation-fold mechanism, divisor convolution, and mod-18 bookkeeping. Nothing in the present calculation resolves its H1/H2.

## 2. AM–GM(4) one-plus-three space [D]

For F(u)=log[(sum_{i=1}^4 exp(u_i))/4] - (sum_i u_i)/4, at the equality seat
Hess F=(I-11^T/4)/4. Hence a canonical rank-one collective projector P0=11^T/4 and a rank-three relative projector P3=I-P0. The four-entry permutation action of S4 decomposes as 1+3. This is compatible at the representation level with the old V4 Hadamard split (trivial and three nontrivial characters). Full S4 invariance forces a triple-degenerate relative eigenvalue at the seat. Generic off-seat splitting does not determine SM masses. The arithmetic V4, geometric AM–GM entries, and canonical Suzuki modes are different carriers absent a new intertwiner.

## 3. Bicone scalar/triplet is NOT the same 1+3 [D/C]

On C^2 tensor C^2 let J_i^(1)=sigma_i tensor I/2, J_i^(2)=I tensor sigma_i/2; L_i=J_i^(1)+J_i^(2), A_i=J_i^(1)-J_i^(2). The diagonal SU(2) gives a spin-1 triplet and spin-0 singlet. Under the **chosen** four-entry/tensor-product coordinate identification, the AM–GM mean lies inside the rotational triplet and the rotational singlet inside the AM–GM relative 3-space, with a 2-dimensional intersection between the two triplets. The map is not physically canonical merely because dimensions agree.

## 4. Critical correction: half and quarter are different Casimir/transition structures [D]

EM extreme-transition vertices are +/-1/2, gravity-only refined vertices +/-1/4; not simply an h^2 rescaling of one fixed operator. On refined shells j in (1/4)Z with m=-j,-j+1/2,...,j, use J_+ transition weights squared (j-m)(j+m+1) for m->m+1 when the target is present. Even j in (1/2)Z have one closed SU(2) table chain and one open fragment; odd quarters have two open conjugate fragments. C=j(j+1) mod1 lies in {0,3/4} for even half-grid, versus {5/16,13/16} for odd quarters. Open-end squared escape weight is j+1/4; thus neither the representations nor their quadratic forms are related by a uniform geometric dilation.

Test BOTH D=[J_+,J_-]-2J_z and E=j(j+1)I-(J_x^2+J_y^2+J_z^2). A zero commutator defect need not imply correct Casimir on an isolated fragment (j=1/2 exception). On first four-state odd-quarter shell j=3/4, ordered m=(-3/4,-1/4,1/4,3/4), E_quarter=diag(0,1/2,1/2,0). This is an operator on an incomplete ladder, NOT a unitary SU(2) irrep.

## 5. Conditional axial match and exact rank-two commutator transport [D/C]

In the standard ordered bicone basis |++>,|+->,|-+>,|-->, A_z=(sigma_z tensor I - I tensor sigma_z)/2. Thus E_bicone=A_z^2/2=diag(0,1/2,1/2,0), numerically identical to E_quarter in the **chosen** ordering. With L_+=L_x+iL_y, L_-=L_x-iL_y, A_+=A_x+iA_y, A_-=A_x-iA_y, and Q_c=A_x^2-A_y^2, exact 4x4 Pauli matrices satisfy

[L_+,[L_+,E_bicone]]=A_+^2,
[L_-,[L_-,E_bicone]]=A_-^2,
Q_c=([L_+,[L_+,E_bicone]]+[L_-,[L_-,E_bicone]])/2,
E_bicone=(I-Q_c^2)/2,
E_bicone Q_c=Q_c E_bicone=0.

Independent symbolic reconstruction confirmed zero entries in the residual matrices. This is exact tensor algebra, **not** an established Hilbert-space intertwiner between the quarter-shell fragment and bicone. In particular the quarter-shell J± boundary leakage cannot be removed by a unitary identification.

## 6. Rotor rank-two comparison [D/C]

In the spin-1 rotational triplet and the common angular basis/phase convention, the projected rotor transverse rank-two factor sin^2(theta)cos(2phi) has m=-1 to m=+1 entry -4/5, versus -1 for Q_c. Thus Q_c=(5/4)P_{j=1}[sin^2(theta)cos(2phi)]P_{j=1} as 3x3 matrices with that normalization. This factor is representation-dependent and is NOT G, a tidal coupling constant, a universal higher-j factor, or a physical mass selector.

## 7. Findings and guardrails

[D] The four-entry relative module, V4/S4 character structure, bicone diagonal scalar/triplet, distinct quarter-shell Casimirs, finite axial matching, and rank-two internal transport identities are mathematically precise but occupy distinct spaces. [O] No source-defined factor-to-mode/quarter-fragment-to-bicone/Suzuki spectral intertwiner; no compatible unitary SU(2) representation on odd-quarter open fragments; no transverse dynamical coefficient, mass hierarchy, three-generation derivation, or G. The two covers Spin(4)->SO(4) and U(24)->U(12), and the divisor identity d2*d2=d4, must NOT be conflated.

**Next gate:** construct or obstruct a boundary-preserving partial-isometry/quadratic-form map from j=3/4 open quarter module to the bicone four-carrier, checking J_z, raising/lowering, Casimir, commutator defect, and higher j=5/4. A genuine bridge must preserve operator actions with explicit residual norms, not just align 4x4 matrices.

**HANDOFF** target: external-audit; type: symbolic-source and carrier-separation; status: open; action: independently verify j=3/4 E, nested commutator identities, rotor j=1 normalization, and the failure of a naive SU(2) intertwiner; compare j=5/4. No change to frozen Suzuki, far-tail, or physical classification.