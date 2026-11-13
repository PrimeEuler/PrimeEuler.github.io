# Cone Derivation Ledger v15.933 — Bicone / interleaved quarter-sector phase response against ordinary Rabi and E1 mixing

**Date:** 2026-11-13 US Eastern. **Track:** Gravity/EM physical realization. **Parents:** v15.140/v15.180 sector-relative phase observations, v15.602/v15.627 q=2 sector grading and candidate shifts, Gravity v15.930 boundary-Jacobi obstruction, v15.931 ordinary glued SU(2) bicone E1 pathways, v15.932 quarter-grid interleaved GM-height surplus. **Immediately prewrite live HEAD:** 79ee473229d569e5c1e0d4f53b52fe53b17150cf; ledger target checked absent. Additive-only; protected Audit, Sandbox, Suzuki and existing ledger artifacts unchanged.

**Mission:** Check whether a physically specified *candidate* parity-odd phase probe between a bicone EM transition sector and the interleaved q=2 quarter sector predicts an experimentally distinguishable dimensionless phase/amplitude observable without inserting measured G or an unconstrained model coupling. Comparison must be with an ordinary two-mode Rabi/optical/Stark mixing system, not with a model lacking phase coherence.

**Status:** [D] exact algebra and conditional phase response; [N] no new dynamics or scale selector from quarter mesh; [N] standard two-mode comparator exactly reproduces every signal; [O] actual field-derived interaction, physically accessible sector states, normalization, phase reference and independent cross-system signal.

## Gate 682 — minimal sector-parity interferometer

Let |E> denote an ordinary EM bicone state and |Q> denote one proposed interleaved quarter-sector state. This is a **chosen two-state truncation**, not a previously proved isometry between hydrogen's physical Hilbert space and the defective quarter representation. Put sector grading χ=σ_z and candidate off-diagonal Hermitian phase readouts U_x=σ_x and U_y=σ_y. Then **{χ,U_x}={χ,U_y}=0**, so a χ eigenstate has zero expectation of these observables. A coherent superposition (|E>+e^{iφ}|Q>)/sqrt2 has <U_x>=cosφ and <U_y>=sinφ, with the chosen phase convention. This agrees with the old phase-relative quarter-grid model in v15.180; no physical gravity observable is obtained by calling U a detector.

Postulate a parity-changing interaction and detuning in angular-frequency units (ℏ=1):

**H=(Δ/2)σ_z+g(cosφ σ_x+sinφ σ_y)**.

Here Δ, g, φ are **all external model inputs**. Starting at t=0 in |E> and taking Δ=0, the solution is

**<U_x(t)>=sinφ sin(2gt)** and **P_Q(t)=sin²(gt)**.

The phase dependence of U_x is a genuine mathematical difference from population detection, and signals relative coherence. It is not a new electromagnetic or gravitational response: it is the standard two-level Bloch/Rabi equation. With Δ≠0, Ω=sqrt[g²+(Δ/2)²], and **P_Q(t)=(g/Ω)² sin²(Ωt)**. This is exactly the conventional detuned Rabi probability, checked independently by matrix exponential for multiple g, Δ and times.

A sector basis rephasing **V=diag(e^{-iα/2},e^{iα/2})** takes H(φ)→H(φ+α). Co-transforming the readout U_x and all preparations leaves probabilities unchanged. Accordingly φ is not an absolute physical phase selected by the parabola vertex at ±1/4: one needs an actual phase reference, and measurable statements concern phase *differences*.

## Gate 683 — compare with ordinary E1 line-strength borrowing

To connect the proposed measurement to the v15.920 spectroscopic lifetime result, consider a **three-state conditional comparator** (ground |g0> and bright excited |e> even under χ; candidate dark quarter state |q> odd). Take the ordinary EM dipole **D=d(|g0><e|+|e><g0|)**, where d is the physical dipole from the actual SO(4,2)/KS theory; D is sector-even. Add a supplied parity-odd interaction λ(|e><q|+|q><e|) and an independently supplied energy separation δ=E_e−E_q. Its excited eigenvectors rotate by a mixing angle θ with tan(2θ)=2λ/δ (up to ordering and phase conventions).

The resulting E1 matrix amplitudes are **d_bright=d cosθ** and **d_dark=−d sinθ**. Thus the *frequency-corrected* Einstein-A strengths obey

**(A_bright/ω_bright³):(A_dark/ω_dark³)=cos²θ:sin²θ**,

and their sum after division by their respective ω³ has the **standard oscillator-strength conservation** proportional to d². The borrowed-strength ratio **tan²θ** is dimensionless and potentially measurable, but it is not an independently predicted Cone ratio because θ (or λ and δ) remains free. This is identical to ordinary field-induced level mixing/oscillator strength borrowing. An observed sideband or phase beating alone would not distinguish the proposed interleaved quarter-sector from standard Stark/Zeeman/optical coupling.

**Critical symmetry caveat:** the formal grading χ of the refined q=2 geometric module has not been shown to equal physical spatial parity, magnetic polarization, or a conserved charge of the hydrogen bicone. There is no identified physically accessible dark |q> state nor derived microscopic λ. Therefore the model is explicitly a conditional analog—not an experimentally validated q=2 sector or gravitational E1 transition.

## Gate 684 — exact test and negative selector result

The quarter-grid parabola identity of v15.932 gives a *geometric* midpoint `Y_{k+1/2}² - (Y_k²+Y_{k+1}²)/2=1/4` (or u²/4 under physical scaling); it constrains no independently normalized coefficient λ, detuning Δ, or relative phase φ in the Hamiltonian above. For every chosen λ, Δ, φ one can construct an otherwise ordinary two-mode EM system with the same H and U and exactly the same probabilities; no dimensionless residual survives the comparator. Hence **new gravitational phase response not derived**. The prior v15.930 boundary-Jacobi anomaly is not removed by this two-state truncation; it is simply omitted. A claimed physical q=2 tensor must separately address the defective ladder, bicone-to-quarter Hilbert-space map and gauge/parity selection.

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_interleaved_phase_response_v15_933.py`, commit **79ee473229d569e5c1e0d4f53b52fe53b17150cf**. Exact SymPy checks of χ-odd readouts, phase-dependent signal, sector population, basis rephasing invariance and E1 mixing matrix strengths; numerical SciPy matrix-exponential checks for Δ/g=(0,.1),(.5,.1),(.5,.02) and t=(0,1,3,8), all PASS. Independent external Audit pending.

**Scientific decision / next nonredundant gate:** Stop treating a formal off-diagonal phase measurement as itself a novel physical prediction. Require one concrete, field-derived term linking physical bicone electric dipole and quarter-grid carrier (including correct SI units and gauge/rotation behavior), or identify a rigorous no-go for such a term under parity and angular momentum. As a modest, falsifiable alternative, specify an independent gravitational tidal drive g(t) from the Fermi-normal field action and calculate a response **normalized against the identical ordinary parametric oscillator**; if response coincides identically, close the novelty claim and retain the geometric representation result. Do not infer electron stability or G from the geometric 1/4 position.

**HANDOFF Audit:** Verify the σx phase sign, U(1) co-transformation, detuned Rabi probabilities, frequency-corrected E1 borrowed-strength identity, and the non-identification of geometric quarter χ with physical spatial parity.
