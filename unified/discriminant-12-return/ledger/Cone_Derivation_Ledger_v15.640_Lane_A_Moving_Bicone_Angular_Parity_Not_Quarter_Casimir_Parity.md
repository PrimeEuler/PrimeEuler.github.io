# Cone Derivation Ledger v15.640 — Lane A: source-faithful moving-bicone angular parity is not yet the EM/odd-quarter Casimir grading

**Date:** 2026-11-10. **Parents:** original two-body moving-bicone payload `payloads/two_body_bicone_v15_428/REPORT.md` and `two_body_bicone.py`; v14.862–869 bicone/exchange; v14.872 actual Larmor Floquet current; v15.544 and **v15.572** audited earlier two-spin quarter-ladder encoding (Audit Round 517 v15.575); v15.625–628 q=2 Casimir grading; v15.639 bicone swap-parity no-identification (External Audit Round 528 at HEAD 9ccab34 confirms v15.639). **Status:** [D] classical harmonic identity and discrete planar rotor selection rule *if canonically quantized*; [C] quantization of existing classical angular model, not yet experimentally sourced; [O] any worldline/phase-space intertwiner to odd-quarter shell Casimir. **Prewrite live HEAD:** 521ea945fd22109fe8ee08b23927a9cdc94a72ea; collision search v15.640 empty. Additive, frozen Suzuki untouched.

## Redundancy and model identity

The earlier v15.572 already exactly constructed a **j=3/4 quarter-defective ladder** in the full two-spin algebra, and Audit Round 517 independently verified it; it is not rediscovered here. v15.639 already distinguished bicone *singlet/triplet swap* grading (trace 2 on four states) from geometric *quarter-shell Casimir* grading (scalar ±I at a fixed shell). This gate tests a **third parity** that is genuinely implied by the original moving-bicone *classical two-body dipole angular potential* and is not to be conflated with either.

The original moving-bicone v15.428 model is a **classical planar** system with headed dipole axes n_i=(cosθ_i,sinθ_i), position separation direction e=(cosα,sinα), interaction U_dd=(C_dd/r³)[n1·n2−3(n1·e)(n2·e)], and otherwise central -K/r, kinetic translation and rotation. The spin-1/2×spin-1/2 quantum KS bicone of v14.869 is a **different** model/carrier from these planar angular rotors. No equality of their states/charges is assumed.

## Gate 152 — exact angular Fourier reduction and classical symmetry

Direct trigonometric identity:

U_dd=(C_dd/r³){−(1/2)cos(θ1−θ2)−(3/2)cos(θ1+θ2−2α)}.

A simultaneous half-turn θ1→θ1+π and θ2→θ2+π leaves U_dd unchanged, whereas reversing **only one headed dipole** changes the sign of U_dd and is not a symmetry at fixed C_dd. Identical-body interchange θ1↔θ2 together with r→−r (α→α+π) also preserves U_dd. These are exact statements about original classical dynamics, not newly postulated phase locks. The physically headless *shape* identification n∼−n noted in v15.428 must carry a compensating dipole polarity/phase variable; the original simulation used headed dipoles and **did not** implement that headless quotient. Do not silently quotient θ_i by π.

## Gate 153 — conditional quantum-rotor angular selection and total J

If each headed planar orientation is quantized with 2π-periodic wavefunction, each p_{θ_i}/ℏ eigenvalue m_i is an integer. The first Fourier harmonic has angular shifts (Δm1,Δm2)=(±1,∓1) with Δℓ=0. The second harmonic has (±1,±1) with Δℓ=∓2 when α is the dynamical orbital angle. All terms preserve total orbital-plus-rotor angular momentum J=ℓ+m1+m2 and, separately, the **parity Π=exp[iπ(m1+m2)]=(-1)^{m1+m2}**. Because only angular Fourier charges are used here, this is a selection rule for **the specified quantum quantization of the classical angular interaction**. Classical dynamics preserves angular momentum but Π as an operator belongs to the chosen quantum rotor carrier.

At fixed α=0, direct finite 25×25 matrix for m1,m2∈{-2,-1,0,1,2}, Fourier coefficients −1/4 on shifts (±1,∓1) and −3/4 on (±1,±1), satisfies H=H†, [Π,H]=0 and [S,H]=0 for swap S|(m1,m2)⟩=|(m2,m1)⟩, [Π,S]=0. On this finite symmetric cutoff Π has + multiplicity 13 and − multiplicity 12. This is a diagnostic cutoff, not a claim about full dynamics or physical spin-statistics.

## Gate 154 — the three Z2 gradings have different carriers and no established intertwiner

The existing quarter Casimir sector character is χ_G=exp(16πi C_geom)=(-1)^L for j_geom=L/4. The full source-faithful moving-bicone interaction's Π=(-1)^(m1+m2) is a **rotor angular-momentum parity**. It is a well-defined conservation rule without a Casimir identification, but nothing in the kinetic phase space, dipole coupling or force law gives a map L≡m1+m2 (mod 2), or any equivalence between χ_G and Π. Likewise the two-spin KS swap S of v15.639 acts on spin 1/2×spin 1/2 and is not automatically this planar-rotor permutation. The old v15.572 4×4 algebraic encoding does not provide that absent physical map.

Adding a conventional Fourier perturbation odd in a single rotor angle would break Π, but it must be **new physical interaction data**; original symmetric dipole-dipole term cannot force one-rung quarter-sector mixing. The imported C_dd/r³ and -K/r in the original simulation are conventional forces, not new Cone-predicted couplings.

## Verdict and audit request

**Positive:** an independently source-faithful simultaneous-dipole-rotation Z2 symmetry of the original moving-bicone dynamics, with an exact rotor-quantized parity selection rule and a conserved total angular momentum operator in the fully rotationally covariant quantum model. **Negative:** no already supplied canonical map from that parity to the EM/odd-quarter geometric Casimir label, no odd-quarter gravitational excitation/interaction, and no parameter-free G-free novelty. The natural original-worldline phase model remains a classical headed-dipole simulation with no discrete Casimir carrier attached.

**Reproducer:** `research-notes/bicone_moving_phase_selection_v15_640.py`, committed at 521ea945fd22109fe8ee08b23927a9cdc94a72ea and executed with exact SymPy output PASS. Verifies harmonic identity, simultaneous π-turn, individual reversal sign, Fourier selection, full J increments and 25×25 operator parity/exchange. The first exploratory local test exposed an *implementation-only* float/integer mixing issue in negative integer powers; resolved by exact SymPy integer powers before commit. No images generated.

**HANDOFF:** external-audit, gravity, sandbox; verify the Fourier decomposition, headed versus headless polarity caveat, quantization hypothesis, rotor parity and angular momentum selection with orbital α, and absence of a derived map between Π, S, χ_G. This is not new EM/G sector mixing. Frozen Suzuki and far-tail production untouched.

**Next gate:** inspect potential physically motivated headless axis/polarity-phase completion in the original moving bicone and compare its required discrete gauge redundancy with the geometric Z2 Casimir grading; alternatively test a physical dimensionless response in full moving-bicone dynamics against standard dipole multipole theory. Prefer a falsifiable dynamical observable over further auxiliary four-component constructions.
