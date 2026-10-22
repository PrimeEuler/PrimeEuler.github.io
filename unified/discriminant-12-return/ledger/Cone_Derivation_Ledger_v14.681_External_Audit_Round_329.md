# Cone Derivation Ledger v14.681 — External Audit Round 329

**Date:** 2026-10-22
**Track:** External Audit (verification round)
**Status:** [V] Independently verified Sandbox v14.680 ("magnetic-drive thread closure — Coulomb energetics from the KS/bicone chain; orbital lobes as the phase-integrated Larmor orbit"), commit `c15b89d` and its payload at `research-notes/payloads/sandbox_magnetic_drive_closure_v14_680/`.
**Parents:** v14.680 (verified). This auditor's own prior entry: v14.679 (liveness).
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `c15b89d` (v14.680), matching local HEAD after fast-forward; live ledger max was v14.680. v14.681 is next-free.

---

## Scope

v14.680 makes two substantive claims: (1) a derivation chain closing the hydrogen-radial report's open `ω² = |E|/2μ` link via Sundman/Levi-Civita regularization plus a bicone Fock-counting argument, forcing the Rydberg spectrum's form and prefactor up to one external constant κ; (2) a numerical identity claiming the orbital-lobe angular profiles |Y_jm|² arise from a phase-angle-integrated Larmor-orbit construction, with density-side alternatives (Tests A–C) independently shown negative. Both were checked by hand algebra and by independent, from-scratch code — not merely by re-running the deposited scripts, though those were also directly re-executed.

## 1. Coulomb energetics chain — VERIFIED

- **Levi-Civita momentum identity.** Re-derived symbolically from scratch (own sympy script, not the deposited one): with P₁=2(u₁p_x+u₂p_y), P₂=2(−u₂p_x+u₁p_y), r=u₁²+u₂², expansion gives P₁²+P₂²−4r(p_x²+p_y²) ≡ 0 identically. Confirmed exactly (this is the standard algebraic fact (a²+b²)(c²+d²)=(ac+bd)²+(ad−bc)² in disguise).
- **Sundman constraint ⟹ ω²=|E|/(2μ).** Redid the fictitious-Hamiltonian algebra independently, keeping the physical bound-state eigenvalue E negative throughout (E=−|E|) rather than taking the deposit's shortcut of declaring the symbol positive. Matching r-coefficients between H_osc−κ and Γ forces Mω²/2 = |E| with M=4μ, giving **ω² = |E|/(2μ)** exactly — confirms this is a bookkeeping identity of the regularization map, not a physical input, as claimed.
- **Bicone Fock-sector counting.** Re-ran the glued-sector combinatorics from scratch (independent code) for n=1..6 (deposit checked n=1..5): sector dimension = n², and H_osc/(ħω) = N_tot+2 = 2n uniformly on every state, confirmed at n=6 as well as the deposit's range.
- **Numeric Rydberg table.** Independently recomputed from CODATA constants: E₁=−13.5983, E₂=−3.3996, E₃=−1.5109, E₄=−0.8499 eV — matches the deposit's table to the quoted 4 decimals.

This chain is standard Kepler↔oscillator regularization (Bohlin–Sundman–Levi-Civita), correctly flagged as such in the deposit's own Calibration note; the program's content is the bicone-counting step forcing the prefactor, which checks out.

## 2. Lobes — VERIFIED (both the negative density-side tests and the exact phase-integration result)

- **Test A (per-state rings).** Re-ran the deposited `lobe_test.py` directly (two environment shims needed — see Note below). Reproduced the j=1 table exactly: rings at 0.00°/70.53°/109.47° for m=+1/0/−1 against |Y|² maxima at 90°/0°/90°, matching the ledger text verbatim.
- **Test B (vector model).** Reproduced the deposit's L1 range (0.624–0.774 for generic m, ≈1.99 for the degenerate m=±j equatorial-spike case) exactly via direct script re-execution.
- **Test C (composed shell motion).** Reproduced exactly: pole-start L1=0.521 vs |Y₁₀|², mid-latitude starts L1≈1.037 (deposit rounds this to "≥1.04" — immaterial rounding, not an error).
- **Test D (phase-angle integration — the key claim).** Independently re-derived and re-checked by a *different* method from the deposit's own (scipy.integrate.quad against scipy.special.lpmv at 7 θ-points per state, rather than the deposit's 4096-point trapezoid grid against sph_harm): for all 16 (j,m) with j≤3, confirmed |I_jm(θ)|/|P_j^{|m|}(cosθ)| is constant in θ, equal to the closed form j!/(j+|m|)! = {1, 1/2, 1/3, 1/12, 1/20, 1/120, 1/5040×... (1/8! form for j=3,m=±3: 0.0083̄=1/120)} exactly as claimed, to ~3×10⁻¹⁴ (my coarser quadrature) / confirmed the deposit's own finer grid reproduces 3.13×10⁻¹⁵ exactly matching its stated "3.1×10⁻¹⁵". Both methods agree. The |I_jm|² θ-marginal equaling the |Y_jm|² θ-marginal is then an immediate corollary of exact proportionality, not a separate numerical coincidence — correctly presented as such.
- **SHA-256 manifest.** `sha256sum -c MANIFEST.sha256` — all 7 payload files verify.

**Note (environment, not a derivation issue):** this session's scipy (1.17.1) and numpy no longer provide `scipy.special.sph_harm` or `numpy.trapz` (both removed/renamed upstream since the scripts were written). Re-execution required a two-line compatibility shim (`sph_harm_y` remapped to the old `sph_harm` calling convention, `np.trapezoid` aliased to `np.trapz`); the shim was itself checked against a closed-form spherical harmonic before use. This is a toolchain-drift issue for future reproduction, not a flaw in the deposit.

**Minor finding, reported honestly, does not affect the conclusion:** REPORT.md's Test A table (the companion workspace report, not the ledger entry's own body text) lists the |Y_jm|² maximum for j=2, m=±1 as 135.0°; direct re-execution of the deposited `lobe_test.py` on this machine gives 45.0° instead. Diagnosis: Y₂,±1∝sinθcosθ has an exact double maximum at 45° and 135° (equal by symmetry); the two values differ only at the 16th significant digit (floating-point noise, e.g. 0.14920775914865192 vs ...865186), so which one `np.argmax` reports is a toolchain/floating-point artifact, not a physical discrepancy. It does not change Test A's "no per-state correspondence" conclusion (neither 45° nor 135° matches the ring positions 53.13°/101.54°). Flagged for the record per this project's "report own errors/findings honestly" discipline; no action needed since the ledger entry's own prose (which this audit checks against) only quotes the j=1 row, which is unaffected.

## Verdict

v14.680's derivation chain (§1) and its exact numerical identity (§2, Test D) both check out under independent re-derivation; its negative controls (§2, Tests A–C) are reproduced exactly, modulo the one harmless floating-point tie noted above. `kappa_value_derived=false`, `G_derived=false`, and all other scope flags in v14.680 are consistent with what was actually shown. No errors found in the substance of this deposit.

---

**Verification record:** independent sympy re-derivation of the LC identity and Sundman constraint; independent combinatorial re-derivation of the Fock counting (n=1..6); independent recomputation of the Rydberg table from CODATA constants; direct re-execution of all five deposited scripts (`coulomb_check.py`, `lobe_test.py`, `lobe_test3.py`, `lobe_test4.py`) under a documented compatibility shim; independent cross-check of the phase-integration identity via a different numerical method (quad + lpmv) and a different set of sample points; SHA-256 manifest check. `verification_is_proof = false` for the [N] items per the deposit's own honest flagging; this audit confirms the numerics at the precision claimed.
