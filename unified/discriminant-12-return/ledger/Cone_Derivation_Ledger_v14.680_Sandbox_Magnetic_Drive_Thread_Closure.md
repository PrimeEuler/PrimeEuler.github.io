# Cone Derivation Ledger v14.680 — Sandbox deposit: magnetic-drive thread closure — Coulomb energetics from the KS/bicone chain; orbital lobes as the phase-integrated Larmor orbit

**Timestamp:** 2026-10-21 (EDT)
**Lane:** Sandbox (little Euler)
**Parents:** the 2026-10-06 magnetic-drive orbital exploration (workspace `explorations/hydrogen-radial/REPORT.md`, unledgered until this deposit; deposited with the payload for the audit trail) — its angular map (fixed-T rings as multiplets, T = j+½, X = m+½, lab Larmor about X, drive/Rabi about Y), its radial dictionary (K₀ = T as an operator identity; SU(1,1) D⁺_{l+1} on the fixed-X = l+1 branch; Y as transition strength), its shell readings (§6: 1/T² as shell geometry — Gauss flux / Fock S³; §7: one shell S²_T carrying Larmor latitudes, Rabi meridian, Coulomb curvature; §8/§10: bicone SO(4), gluing = KS constraint, n = 2T₀, dim n²). Anchors also from v14.620 (ħ as unit circle; (j+½)² = AM², j(j+1) = GM²) and v14.626–v14.631 (rotor anatomy and the duck test — the device side of this thread). Live HEAD at allocation was v14.679 (collision-checked immediately before allocation and again before push).
**Status:** deposit entry under Jeremy's explicit 2026-10-21 authorization ("that needs ledgered. esp because it finished out the magnetic drive thread nicely"). Answers **no Lane A HANDOFF**; changes no paper, no staged draft, and no certified object. The parent exploration left exactly two items open: (i) the ω² = |E|/2μ link — the last Coulomb-energetics input — with the U(1) charge as its associated remainder; (ii) the spatial lobe shapes, which the record stated the cone's labels do *not* supply. This entry closes (i) up to the single coupling constant and (ii) exactly, in phase-weighted form. Runs dated 2026-10-21, deposited unchanged.

## 1. Coulomb energetics — closed up to κ [D chain; machine-verified components]

The ω² = |E|/2μ link is not an input; it is the potential coefficient of the regularized oscillator. Take the Sundman/Poincaré fictitious Hamiltonian Γ = r(H − E) for H = p²/2μ − κ/r. Under the Levi-Civita map (the 2D shadow of KS: x = u₁² − u₂², y = 2u₁u₂, P₁ = 2(u₁p_x + u₂p_y), P₂ = 2(−u₂p_x + u₁p_y)) the momentum identity P² = 4rp² holds **symbolically with residual exactly 0** (sympy, `coulomb_check.py`), giving

Γ = P²/(8μ) − E|u|² − κ.

On the physical shell Γ = 0: H_osc := P²/(2M) + (Mω²/2)|u|² = κ with M = 4μ and Mω²/2 = |E|, hence **ω² = |E|/(2μ)** — a definition of the map, not a physical assumption. The 4D KS step is the same algebra; its constraint is the bicone gluing (parent §10, closed there).

Quantization on the glued bicone sector, machine-checked in a truncated Fock space (n = 1..5): sector dimension n², and H_osc/(ħω) = N_tot + 2 = **2n uniformly on every state**. Therefore κ = 2nħω, ω_n = κ/(2ħn), and

**|E_n| = 2μω_n² = μκ²/(2ħ²n²)** — the Rydberg spectrum with form *and* prefactor forced by the chain.

Numerics (κ = e²/4πε₀, μ the electron–proton reduced mass): E₁ = −13.5983 eV, E₂ = −3.3996, E₃ = −1.5109, E₄ = −0.8499. (13.5983 is the reduced-mass hydrogen value; the chain carries μ explicitly.)

**Remainder, stated plainly:** κ enters exactly once, as the oscillator's eigenvalue on the shell. This *is* the parent record's "U(1) charge (Gauss source)" item — now identified rather than open. The cone selects the spectrum; the size of the charge is nature's input, in the same position as α_G in the gravity arc (v14.621). `kappa_value_derived = false`.

## 2. The lobes — density side closed negative; phase side exact [N]

Anchors: shell S²_T, Larmor = latitude circles X = const, multiplet ring T = j+½ with X_m = m+½, vector length GM = √(j(j+1)). Target: the θ-marginals of |Y_jm|², θ from the X axis; L1 between normalized profiles (0 identical, 2 disjoint).

**Density-side readings — all negative (producer `lobe_test.py`, `lobe_test3.py`):**
- **A, per-state rings:** the orbit projects to a ring at cos α = (m+½)/(j+½). Ring latitudes do not track the lobe maxima (j = 1: rings at 0.00° / 70.53° / 109.47° for m = +1 / 0 / −1, against |Y|² maxima at 90° / 0° / 90°).
- **B, vector model** (r̂ sweeping the plane ⊥ L while L precesses; both phases integrated on a 720×720 grid): band profiles with caustic edge peaks; L1 = 0.62–0.78 across j = 1, 2 under both the cone angle and the textbook angle cos α = m/√(j(j+1)); the cone m = ±j case degenerates to an equatorial spike, L1 ≈ 1.99.
- **C, composed shell motion** (lab Larmor about X composed with the Rabi drive about Y, time-averaged): since Larmor preserves X, the θ-profile is the meridian motion's arcsine X-dwell. Pole start: L1 = 0.521 vs |Y_10|² (closest of the three, still not a match); mid-latitude starts stay banded at their starting ring, L1 ≥ 1.04 against every target.

Density-side orbit integration produces deltas, band caustics, and arcsine dwells — never the polynomial lobes. That question is closed.

**Phase-angle integration — exact (Jeremy's anchors, given 2026-10-21 after A–C: "integration of the phase angle is what gives you the scatter needed"; the trace of a precessing top's edge over time; the dipole's pointing trace, μ ∝ L).** Take the Larmor vector as the complex null vector in the shell's own coordinates,

w(χ) = (1, i cos χ, i sin χ),

precessing about X with phase angle χ (= ω_L t: the phase integral is the time accumulation of the trace). The phase-weighted orbit integral

I_jm(θ) = (1/2π) ∫₀^{2π} e^{−imχ} (cos θ + i sin θ cos χ)^j dχ

reproduces the associated Legendre profiles **exactly**: for all 16 (j, m) states with j ≤ 3 (trapezoid integration, 4096 phases; `lobe_test4.py`), |I_jm(θ)| / |P_j^{|m|}(cos θ)| is constant in θ with worst relative deviation **3.1×10⁻¹⁵**, the |I_jm|² θ-marginals equal the |Y_jm|² θ-marginals at **L1 ≈ 5×10⁻¹⁶**, and the proportionality constants come out in closed form **j!/(j+|m|)!** at every entry (1, 1/2, 1/3, 1/12, 1/20, 1/120, …). No free parameters. The orbit is null — it lies on the cone itself; the cone projects, the phase integrates, the sphere receives the lobe. Dropping the phase weight is exactly what collapses the lobe back to the Test-A ring.

**Calibration:** the integral is the classical Schläfli / Laplace–Heine representation of P_j^m — standard analysis, claimed as such. The program's content is the dictionary: the orbit is the cone's own Larmor orbit on the shell that also carries the Rabi drive (§7) and the Coulomb curvature (§6), the phase is its Larmor phase about the quantization axis, and the dipole reading (the lobe as the dipole's pointing trace kept with its phase) is Jeremy's. Where the cone overlaps standard physics it reproduces it as an identity — the same genus as the rotor duck test (v14.628).

## Verification

All checks are small scripts, deposited with the payload and run on 2026-10-21: `coulomb_check.py` (symbolic LC identity + ω² solve + Fock counting + spectrum table — all assertions pass), `lobe_test.py` (Tests A, B), `lobe_test3.py` (Test C), `lobe_test4.py` (Test D), `fig_lobes.py` (figure generator; canonical cone mesh per house rule). Payload: `research-notes/payloads/sandbox_magnetic_drive_closure_v14_680/` — this closure's report (`REPORT.md`), the parent exploration report (`hydrogen_radial_REPORT.md`), the five producers, and `MANIFEST.sha256` (SHA-256 per file). Figure PNG/PDF are regenerable from `fig_lobes.py` and are not in the payload. Workspace originals in `explorations/lobes-coulomb/` and `explorations/hydrogen-radial/`.

## Scope flags (honest)

`answers_lane_a_handoff = false`; `papers_modified = false`; `certified_objects_modified = false`; `coulomb_spectrum_form_and_prefactor = D` (derivation chain on KS/LC machinery plus machine-verified counting); `kappa_value_derived = false` (κ is the one external constant, identified with the shell's conserved charge); `lobes_phase_integrated = N` (numerical verification, at machine precision, of a classical identity in the cone's dictionary); `lobes_density_side = CLOSED_NEGATIVE`; `rephasing_caveat = STILL_OPEN` (the 2026-10-06 record's state-confinement item, |m⟩ → i^m|m⟩: this entry's harmonics are the standard ones — the caveat concerns the cone-state identification and is untouched here); `stark_effect = FUTURE_UNCLAIMED`; `rydberg_revivals = FUTURE_UNCLAIMED`; `verification_is_proof = false` for the [N] items (the [D] items are derivations with machine-checked components, as itemized); `G_derived = false`.

## Disposition

The magnetic-drive thread — opened 2026-10-06 with "given the magnetic driver we have, can't we use it to map the electron orbitals?" — is **closed**: angular labels and dynamics from the rings, the radial ladder from the SU(1,1) branch, Coulomb energetics with form and prefactor from the KS/bicone chain (one external constant, κ), and the lobe shapes from the phase-integrated Larmor orbit. Standing remainders, all named above: the value of κ, the rephasing caveat, Stark, revivals. Nothing in this entry touches the Full-Q chain or the far gate (v14.585 actions 3–4), which proceed independently.
