# Cone Derivation Ledger v15.919 — Empirical EM spectral lifetimes as a physical clock for diameter–secant ladders

**Date:** 2026-11-13 US Eastern. **Track:** Gravity/EM physical bridge. **Parents:** v14.550 original diameter–secant machine, v15.905–918 Schwinger and actual velocity readout gates, `arxiv/note-bicone-dipole-alpha/Note_BiconeDipole_FineStructure_v1.0.tex` staged hydrogen lifetimes and SO(4,2) dipole derivation. **Live HEAD immediately before ledger write:** 394ee35311e4acb216e565561fc43ba1f3be07b8. Ledger target checked absent; strictly additive; no changes to prior certified, Audit, Sandbox or Suzuki objects.

**Owner insight:** Real EM spectroscopy gives transition lifetimes as well as line frequencies. Can these measurements close the physical clock/acceleration selector for the Cone (n+k)/(n−k) transitions and nested sqrt(nk) circles?

**Scientific status:** [D] exact fixed-sum Schwinger geometry and rate-matrix-element algebra, NIST lifetime/branching relations, and conditional lifetime-ratio proposal; [N] numerical real lifetime examples from the existing bicone paper; [N] no direct identification of within-shell J+ transitions with radiative spectral lines because the comparator has zero energy gap; [O] field-derived cross-shell physical dipole intertwiner, angular/radial factors, actual independent lifetime ratios.

## Gate 632 — the actual bridge: spontaneous emission measures a clock

A spectroscopic upper-level total radiative lifetime obeys **tau_i^{-1}=sum_{f lower} A_if**, not generally 1/A_if for an arbitrarily chosen line. If branching ratio b_if=A_if/sum A_if is measured, **A_if=b_if/tau_i**. Natural homogeneous Lorentzian full width (ordinary frequency, absent extra broadening) is **Delta nu=1/(2pi tau_i)** for a level decaying exponentially in population. Linewidth data also require distinguishing lower-state width, collisions, Doppler/instrument and dephasing.

For an electric dipole E1 branch, **A_if=omega_if³ |d_if|²/(3pi epsilon0 hbar c³)**, with suitable magnetic-sublevel average/sum when treating unresolved multiplets. Thus measured omega, branching fractions and independent lifetimes give absolute dipole strengths in C·m and remove arbitrary *rate* normalization in the physical system. This is exactly the kind of dimensional observation the owner was seeking, although converting an amplitude into a literal velocity-space acceleration still needs a physically justified observable map.

NIST confirms both tau_i^{-1}=sum A_if and the use of transition line strengths/oscillator strengths; it cautions that spectral database A values may be critically evaluated theory rather than independent experimental measurements. For parameter-independent tests, prefer experimentally measured lifetimes plus branching ratios, with provenance and uncertainty, not a theoretical A table as if it were independent confirmation.

## Gate 633 — a concrete conditional diameter–secant lifetime ratio

For normalized inner product-shell chord `Y/u=sqrt(nk)` and Paper C's fixed-D Schwinger operator `J_+|n−1,k>=sqrt(nk)|n,k−1>`, imagine a **physically justified** dipole transition `d_if=d_* C_if sqrt(nk)`. Here `d_*` is a common physical length×charge, and `C_if` contains necessary angular polarization, cross-shell map, spin and reduced/radial matrix-element factors. THEN an E1 decay branch follows

**A_if=(omega_if³ d_*²/(3pi epsilon0 hbar c³)) |C_if|² nk**.

If two lines share the same `d_*` and the independently derived `C_if`, their corrected lifetime-rate ratio would satisfy

**[A_1/omega_1³]/[A_2/omega_2³] = (n_1k_1|C_1|²)/(n_2k_2|C_2|²).**

If also equal C factors, the pure Cone ladder ratio reduces to **n_1k_1/(n_2k_2)**. At fixed D=5, the (4,1) right and left Schwinger squared strengths are 4 and 6, ratio **2/3**. This is an exact **operator** ratio; it does NOT yet constitute a prediction for measured EM spectral lifetimes. Opposite directions have different final states and energy gaps; selection rules and population branching must be worked out. For unequal transition frequencies the omega³ factor must not be omitted.

## Gate 634 — radiative no-go for a fixed-D equal-frequency Hamiltonian

In the existing Paper C comparator **H0=hbar omega_* (N+1)**, the pair (n,k) and its J_+ destination (n+1,k−1) have identical **N=n+k−1**, hence **Delta E=0 and omega_if=0**. An ordinary spontaneous E1 radiative transition between those degenerate states therefore has zero omega³ radiation rate in this approximation. The Schwinger coefficient sqrt(nk) by itself cannot be equated with a measured line's decay rate, natural lifetime, or gamma parameter.

Any physical spectroscopic mapping must add a Hamiltonian that gives independently predicted nonzero line energies and derive the **physical electric dipole operator** between their upper/lower atomic states. In hydrogen, the physical E1 dipole changes the principal-energy shell; fixed-N SU(2) transitions merely rearrange state amplitudes in the same ideal shell. The staged bicone note uses a larger **SO(4,2)** construction and the KS physical measure to supply a nontrivial radial dipole coefficient, rather than treating bare J_+ as the electric dipole. This is a key distinction, not an obstacle to using the lifetime data.

## Gate 635 — existing independently sourced lifetime precedent

The staged note `arxiv/note-bicone-dipole-alpha/Note_BiconeDipole_FineStructure_v1.0.tex` already computes hydrogen 2p→1s's dimensionless radial dipole coefficient **Y_geom=768/(243 sqrt6)** using the hydrogen SO(4,2)/bicone representation and physical KS weighting. It then uses the **reported experimentally measured** hydrogen 2p lifetime **tau_H=(1.592±0.025) ns** to infer **alpha^{-1}≈137.4±2.2**, explicitly with a measured spectral frequency and electron Compton length. This is not an alpha-from-geometry-alone derivation and does not fix a new physical time unit without empirical input.

That staged note also cites a He+ 2p measured lifetime **tau_He=(0.9992±0.0026)×10^-10 s**, or 99.92±0.26 ps. A leading nonrelativistic hydrogenic dipole scaling A(Z)~Z^4 implies tau_He≈tau_H/16=99.5±1.56 ps, consistent with the He+ measurement within reported uncertainty. More precise comparison needs reduced-mass and relativistic effects and proper transition frequency for He II. Hydrogen's reported lifetime yields A≈6.2814×10^8/s and natural FWHM Δν≈99.97 MHz in the single-dominant-channel approximation. The numerical input is **from the staged project's cited experimental papers, not a fresh independent remeasurement**.

The key implication is methodological: the bicone paper's SO(4,2) cross-shell dipole plus independent lifetime is a valid route to testing dimensionless geometry against spectroscopy, whereas bare within-shell Schwinger ladder alone is not. Data provide the dimensional electromagnetic clock. This precedent does NOT fix Newton G nor a new EM→G timing mechanism.

## Gate 636 — falsifiable experimental protocol and scope

Construct for each candidate measured spectral transition an explicit mapping **(physical upper state, lower state, polarization/multipole, observed omega_if, independent upper lifetime tau_i, measured branching fraction b_if) ↔ (Cone transition coordinates and physical dipole coefficient)**. Then compute **Q_if=3pi epsilon0 hbar c³ [b_if/tau_i]/(omega_if³ |d_geom,if|²)**, with d_geom a properly dimensioned dipole coefficient from the independent physical operator/geometry. If all geometry factors and external scales are fixed by **one** calibration line, predict at least two additional independent lines **before** using their measured lifetimes, and compare residuals with uncertainty and the ordinary hydrogenic SO(4,2)/QED comparator. Matching well-known hydrogen symmetry alone is a **standard-physics reproduction**, not a new Cone-specific prediction. For a truly dimensionless test one can compare corrected A/omega³ ratios after eliminating any shared dipole scale.

**Next gate:** start with physically independent H 2p and He+ 2p lifetime and frequency measurements, reproduce the staged bicone calibration with correct experimental errors and reduced mass, then identify two additional lines with measured independent branching/lifetime data and genuinely derived SO(4,2) matrix elements. Require a cross-shell intertwiner to convert the simple (n+k)/(n−k) secant steps into actual E1 transitions; report missing derivation explicitly.

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_spectral_lifetime_diameter_secant_v15_919.py`, commit **394ee35311e4acb216e565561fc43ba1f3be07b8**. Executable Python/SymPy; exact operator and rate-ratio identity, fixed-D ΔE=0 negative control, staged measured H/He+ lifetime values, 2/3 operator ratio. Independent Audit pending.

**Sources:** NIST Atomic Spectroscopy Compendium, Atomic Lifetimes (tau_k inverse = sum_i A_ki); NIST ASD transition-strength definitions; staged bicone note's references G. Tielert et al. (1973) and G.W.F. Drake et al. (1983). These are public/external context, not independent new measurements in this gate.

**HANDOFF Audit/Muse:** verify the distinction between lifetime and branch A, E1 omega³ and angular statistical weights, the fixed-D zero-gap no-go, and whether the staged SO(4,2) Y_geom length can be linked to a full (n,k) spectral family without inserting measured dipoles. In particular independent audits should examine source independence of input A, the He+ reduced-mass and Z^4 correction, and the meaning of the 2/3 at D=5.
