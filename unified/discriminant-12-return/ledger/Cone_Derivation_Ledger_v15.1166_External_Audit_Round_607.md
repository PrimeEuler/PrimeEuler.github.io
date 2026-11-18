# Cone Derivation Ledger v15.1166 — External Audit Round 607

**Date:** 2026-11-18
**Track:** External Audit

## Scope

Four new Sandbox entries landed since Round 606/v15.1161 (`3596921`),
completing Jeremy's 2026-11-18 gravity-thread tasking queue:

- v15.1162 (`...Sandbox_Spin_Transfer_Source.md`, `ef76b58`,
  payload `payloads/spin_transfer_source_v15_1162/`)
- v15.1163 (`...Sandbox_Rho_Well_Definedness.md`, `96bf042`,
  payload `payloads/rho_well_definedness_v15_1163/`)
- v15.1164 (`...Sandbox_Sciama_Apex.md`, `9116729`,
  payload `payloads/sciama_apex_v15_1164/`)
- v15.1165 (`...Sandbox_Trapz_Repair.md`, `f2ca6a0`,
  payload `payloads/trapz_repair_v15_1165/`)

No filename or version-number collisions found.

## v15.1162 — independent verification

- **Biot-Savart field (W1).** Hand-derived div B=0 and curl B=0 for a
  single infinite wire directly from the stated field
  B=(μ₀I_w/2π)(z,0,−ξ)/(ξ²+z²): both derivatives cancel exactly
  (∂Bx/∂x=−μ₀I_wzξ/(π(ξ²+z²)²)=−∂Bz/∂z, and ∂Bx/∂z=∂Bz/∂x), confirming
  both identities away from the wire for each wire, hence for the sum.
- **Linear coefficient G (W2).** By hand (binomial expansion of the
  two-wire sum to linear order in x,z around the origin): the two wires'
  contributions to ∂Bz/∂x add constructively to give
  G=μ₀I/(πa²) exactly, matching the script; the z-linear term in Bz
  vanishes identically (Bz depends on z only through z², an exact
  symmetry); Bx's z-linear coefficient also equals G exactly — all
  confirmed by direct series expansion.
- **Exact splitting (W3).** By hand: Bz on-axis (z=0) sums to
  μ₀I·x/(π(a²−x²)) (odd in x), so ΔΩ_exact=2γ·Bz(d/2 cosθ)=
  γGd cosθ/(1−(d cosθ/2a)²) exactly — matching the ledger — and its
  geometric-series expansion in d gives leading term 1 and first
  correction cos²θ/(4a²), both confirmed by hand.
- **Helmholtz evenness (W4).** By hand: B_axis(−z)=B_axis(z) follows
  directly from swapping which loop is nearer/farther, confirming the
  on-axis field is even and its gradient vanishes at the center.
- SHA-256 of both payload files matched; script re-executed: exit 0,
  8/8 PASS.

## v15.1163 — independent verification

Hand-derived all five closed-form ratios from the stated definitions
(λ_C=ħ/mc, τ_C=ħ/mc², a*=mc³/ħ, a(ρ)=a*/ρ):
- Δτ/(2πτ_C)=ρ (direct substitution).
- T_U=mc²/(2πk_Bρ) (direct substitution).
- a_ZB/a(ρ)=2ρ (direct substitution).
- E_rest·τ_C=ħ (trivial).
- Bouncer ratio reduces algebraically to exactly 2^(−1/3)ρ^(−2/3)
  (confirmed by cubing both sides by hand).
All five matched the ledger exactly. The wedge-count step-function claim
(R6) is a numerical/combinatorial check, not independently re-derivable
in closed form; re-ran the script fresh and reproduced the stated
"278/300 sampled steps" figure exactly. SHA-256 of both payload files
matched; script re-executed: exit 0, 6/6 PASS.

## v15.1164 — independent verification

- **Apex-pair geometry (A1).** By hand, solving row=col (n²−2nX=k²+2kX)
  gives X_c=(n−k)/2 exactly; vertex midpoint (n/2−k/2)/2=(n−k)/4 exactly;
  curvatures d²X_row/dY²=−1/n and d²X_col/dY²=1/k sum to 1/k−1/n,
  vanishing iff n=k — all confirmed by direct differentiation. At n=k=1:
  crossing Y²=1 at X=0 (state (0,1)), curvatures −1/+1 — confirmed.
- **Cosmic B in flat FLRW (A2).** By hand: substituting ρ_c=3H²Ω/(8πG)
  and R_H=c/H into B=GM_H/(R_Hc²) with M_H=(4/3)πρ_cR_H³, every factor of
  H cancels exactly, leaving B=Ω/2 identically — confirmed by direct
  algebraic substitution, independent of the script.
- **Measurement margins (A3).** With B_meas=0.4996±0.0009: by hand,
  z(n=1)=0.0004/0.0009=0.444 (rounds to the ledger's stated 0.44σ — note
  the script's own docstring comment says "0.45σ", a harmless wording
  slip that does not appear in any assertion or in the printed/ledgered
  value, which is correctly 0.44); z(n=2)=0.5004/0.0009≈556σ;
  z(n=0)=0.4996/0.0009≈555σ — both confirmed by hand and matching the
  ledger exactly.
- SHA-256 of both payload files matched; script re-executed: exit 0,
  6/6 PASS, printed z-values (0.44/556/555) match the ledger exactly.

## v15.1165 — independent verification (repair entry)

This entry repairs v15.857's producer for NumPy ≥2.0 (where `np.trapz`
was removed in favor of `np.trapezoid`). Verified more directly than the
ledger's own method, since this session's actual NumPy is 2.4.6 (checked:
has `trapezoid`, lacks `trapz`) rather than simulated:
- **Diff check.** `diff`'d the repaired producer against the original
  filed `payloads/hj_inversion_v15_857/hj_inversion.py` directly: the
  only differences are the claimed 6-line portability shim
  (`_trapz = np.trapezoid if hasattr(np, "trapezoid") else np.trapz`,
  plus comments) and the three renamed call sites — no other hunks,
  exactly as the ledger states.
- **Real failure confirmed.** Ran the original, unrepaired
  `hj_inversion.py` directly in this environment: it crashes with
  `AttributeError: module 'numpy' has no attribute 'trapz'`, confirming
  the claimed portability defect is real, not hypothetical.
- **Repaired version runs clean.** Ran the repaired producer directly:
  exit 0, full output produced.
- **Byte-identical output, independently confirmed.** Ran the *original*
  producer with a one-line `np.trapz = np.trapezoid` monkeypatch
  (restoring the removed name under genuine NumPy 2.4.6, rather than the
  ledger's own simulated-removal approach) and diffed its stdout against
  the repaired producer's stdout: **identical, zero diff**.
- SHA-256 of both payload files matched.

No discrepancy of any kind found. All four entries are correctly scoped
and the repair entry's claim of a purely mechanical, output-preserving
fix is confirmed to a higher standard than the entry's own self-check
(since this audit had access to a real, rather than simulated, NumPy 2.0
environment).

## Verdict

All four new entries PASS independent verification, completing Jeremy's
2026-11-18 gravity-thread tasking queue (v15.1153-v15.1165) with no
mathematical, numerical, or reproducibility error found anywhere in it.

`git fetch origin master` immediately before this commit returns
`f2ca6a0`, unchanged since the pushes verified above. Gravity/Sandbox/
Lane A should continue.
