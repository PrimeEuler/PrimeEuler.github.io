# Cone Derivation Ledger v15.981 — Why 9/5 reappears: EM/quarter node rapidity versus axial and TT rank-two responses

**Date:** 2026-11-14 US Eastern. **Gravity lane.** **Owner:** recognized 9/5 elsewhere and requested check and continue. **Status:** [D] exact three-way rational identity at D=4 with the stated choices; [C] a natural-looking but *unselected* outward-edge map from Schwinger magnetic state to physical speed fraction; [N] general-D tensor extension fails, alternative geometric coordinate gives a different ratio, speed pairs are nonunique, and physical EM↔G coupling remains absent.

**Parents/redundancy:** Gravity v15.888 (+ Audit Round 569/v15.889) already found atanh(1/2)−atanh(1/4)=ln(9/5)/2 from assumed velocity fractions. v15.906 Schwinger diameter/secant has example (7,2) giving 9/5. v15.761 has a 9/5 *different Ricci stress contraction*, no connection assumed. v15.975/976 find allowed tensor ranks for matched-D closed EM/quarter oscillator spin representations. v15.979 (Audit Round 580 at canonical v15.980 independently verified) finds axial rank-2 CG inner/outer ratio 9/5 at D=4. No existing ledger result deriving an SU(2)-to-Lorentz dynamical map is identified. **Immediately prewrite live HEAD:** 81ba489e444b1387fcce9a6401f0c0a36cd58ac1 (this gate's script). Target absent; additive-only; no modification to certified, Suzuki, Audit, Muse or Sandbox objects.

## Gate 778 — three exact formulas use the same 9/5 number

At the special allowed **D=4**, the conventional closed Schwinger pair is j_e=(D−1)/2=3/2, j_q=(2D−1)/2=7/2. Consider a **rank-two** spherical tensor and normalized Clebsch–Gordan squares W_q(m)=|<3/2,m;2,q|7/2,m+q>|², with m=(-3/2,-1/2,+1/2,+3/2).

The axial q=0 profile, already in v15.979, is **W_0=(2/7,18/35,18/35,2/7)**, so **W_0(|m|=1/2)/W_0(|m|=3/2)=9/5**.

The rank-two **helicity** q=+2 profile is **W_+2=(1/35,1/7,3/7,1)**; q=−2 is **W_−2=(1,3/7,1/7,1/35)**. Summing the two orthogonal final-state helicity channels (unpolarized/equal-intensity TT comparator, NOT a generic coherent polarization input) yields **W_TT=(36/35,4/7,4/7,36/35)**. The **outer/inner** helicity-summed ratio is **W_TT(|m|=3/2)/W_TT(|m|=1/2)=(36/35)/(4/7)=9/5**: the inverse orientation of the axial comparison. These are exact standard Clebsch–Gordan coefficients; q=0 is NOT a propagating TT gravitational wave's helicity along its propagation axis. Equal-weight +2/−2 is only a polarimetric control. Actual rates need source power, state preparation, resonance and a physical mapping of oscillator pseudospin to detector angular momentum.

Independently, the assumed velocity nodes β_inner=1/4, β_outer=1/2 have rapidity Δeta=atanh(1/2)−atanh(1/4)=ln(9/5)/2, so **exp(2Δeta)=9/5** (v15.888). Thus the 3-way numeric match is exact, now including transverse-helicity summed response.

## Gate 779 — a candidate magnetic-edge speed dictionary exists, but its physical meaning is missing

At D=4 the positive magnitudes of magnetic states are |m|=1/2,3/2. Define a *chosen* outward-side edge fraction **β_m=(|m|+1/2)/D**. The +1/2 reflects the same edge-versus-state-center shift used in v15.955/968, and the normalization by the outer physical diameter D is geometrically plausible. It gives **β_(1/2)=1/4** and **β_(3/2)=1/2**. The associated Cayley/rapidity ratio is

**[(1+β_outer)/(1−β_outer)]/[(1+β_inner)/(1−β_inner)]=9/5**.

However it chooses the **outward** edge (the opposite offset or center coordinates are also well-defined), takes |m| instead of signed m, and asserts without dynamics that an *algebraic factor-grid coordinate* equals a physical speed fraction. The outermost state maps to the **boundary** half-step where one outward Schwinger J+ coefficient vanishes, so this is especially NOT an identification of two nonzero J+ transition edges. No field theory makes that interpretation mandatory. In a contrasting state-centered rule β_m=|m|/D, the corresponding Cayley ratio is **77/45**, not 9/5. Both are geometrically plausible without a sourced velocity map.

The boost group SO(1,1) / noncompact SU(1,1) and the finite SU(2) angular-momentum carrier are not made the same unitary representation by equality of one real number. A physically meaningful bridge would require a nontrivial dynamical map of states/operators, not a scalar ratio equality.

## Gate 780 — D=4 is exceptional: rank-minimal higher shells kill a universal identity

For even D≥4 with closed q2 and EM ordinary-spin carriers, the smallest tensor rank permitted by the triangle rule is k=D/2 (v15.975). The two positive magnetic magnitudes selected for comparison are **m_inner=1/2**, **m_outer=j_e=(D−1)/2**. The outward-coordinate speed rule gives β_inner=1/D and β_outer=1/2; hence the generalized Cayley ratio is **R_boost(D)=3(D−1)/(D+1)**.

Direct exact CG evaluation with **rank k=D/2** gives:

| D | Rank | q=0 inner/outer CG squared ratio | candidate Cayley ratio |
| 4 | 2 | 9/5 | 9/5 |
| 6 | 3 | 25/7 | 15/7 |
| 8 | 4 | 245/33 | 7/3 |
| 10 | 5 | 2268/143 | 27/11 |
| 12 | 6 | 7623/221 | 33/13 |

Thus the equality already fails at D=6, and physical **rank-two** gravity/EM intersector transitions would be symmetry-forbidden at D≥6 anyway under the common-SU2 premise. There is no universal D-dependent identity linking these group-theoretic ratios via the suggested speed map. The D=4 match is an exact low-shell special-case numerical alignment, not an established all-shell operator correspondence.

Moreover **9/5 does not select the speed nodes uniquely**. For any β_i∈[0,1), imposing Cayley(β_o)/Cayley(β_i)=9/5 gives

**β_o=[(9/5)(1+β_i)−(1−β_i)]/[(9/5)(1+β_i)+(1−β_i)]**.

At β_i=1/4 this gives β_o=1/2; at β_i=0 it gives β_o=2/7. Hence the rapidity ratio alone underdetermines both speeds, the acceleration and the action-circle clock.

## Gate 781 — verdict and next physical selector

**[D]** The repeated 9/5 is real in three exact algebraic contexts. The new *TT-summed* 9/5 is not an arithmetic mistake, and does add a useful polarization comparator to the earlier axial CG result.

**[N]** Nothing yet identifies the proposed 1/2,1/4 factor-grid offsets with massive particle physical velocities. The chosen edge rule is not a physical law and does not generalize to D≥6 under rank-minimal angular coupling. SU2 CG and SR rapidity are well-known standalone formulas; a shared 9/5 cannot be promoted to a new G-independent gravitational effect, phase lock or EM↔G transition.

**[O]** To turn this into a physical test, identify a *specific* Lorentz-covariant field/detector action mapping velocity or rapidity to the oscillator magnetic labels, including the half-step edge and its orientation and the actual rank-two TT mode. Then derive a measurable polarization ratio or phase against conventional GR+electrodynamics, with no freely tuned amplitude or kinematic map. If the map must be imposed, stop this branch as a validated coincidence.

**Reproducer:** `research-notes/k4_rapidity_tidal_9over5_bridge_v15_981.py`, commit **81ba489e444b1387fcce9a6401f0c0a36cd58ac1**. Actually executed equivalent exact local SymPy script with PASS: q0/TT strengths, both 9/5 ratios, β edge dictionary, ln(9/5)/2, alternative 77/45, D=4..12 rank-minimal mismatch, and continuous family of speed-node pairs. Independent Audit pending.

**HANDOFF Audit/Muse:** independently verify q±2 normalized CG profiles and polarization-sum sign/ordering, confirm q0 not itself physical TT helicity, pressure-test proposed β_m outward-edge assignment and boundary zero, and check the D6 ratio 25/7 vs 15/7. Do not infer source-derived G or velocity from dimensionless arithmetic.
