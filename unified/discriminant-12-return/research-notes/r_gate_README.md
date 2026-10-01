# r-gate code — odd-sector invertibility probe (ledger v13.912)

Sandbox code posted for the audit thread at the project owner's direction (2026-10-01),
to reproduce the numerical claims of
`Cone_Derivation_Ledger_v13.912_Sandbox_deBranges_Odd_Sector_Invertibility_Question.md`
directly instead of rebuilding from the ledger's equations. Sandbox-only provenance;
nothing here is a new claim.

## Files

- `r_gate.py` — kernel assembly + solve. Builds Suzuki's finite operator L_A on (−A,A)
  with kernel k(x,y) = g(x−y) − λN(x,y), λ = −1, P1 Galerkin; evaluates the boundary
  functionals ℓ_0(v) = ∫k(0,y)v(y)dy, ℓ_1(v) = ∫k_x(0,y)v(y)dy on R_A applied to the
  four sources {1, x, cosh−1, sinh−x} (parity-split); returns moments
  M00, M1x, M0e, M1e, ratios r0, r1, Schur denominators d0, d1, residuals and parity
  canaries. Includes the [D] self-check that the N-kernel Galerkin matrix inverts
  −d²/dx² on the first Neumann mode to 1.5e−15.
- `sweep_r.py` — A-sweep driver (A = 0.5…4, N = 800/1600, q = 8); reproduces the §2 table.
- `diag_r.py` — N-refinement (400→3200), small-eigenspace, and λ-dependence diagnostics;
  reproduces the §4 divergence table and the λ ∈ {−2,−1,−0.5,−0.2} spot-checks.
- `fem_screw.py` — the only local dependency: `make_g('lambda', tmax)` builds Suzuki's
  g(t) per formula (1.3) (pole + Λ-weighted prime sum + archimedean terms), vectorized.
  Prime sieve capped at 100000 — this is what caps the sweep at A ≲ 5.7 (needs e^{2A}).
  (The audit thread's own independently validated g(t) from (1.3) can be substituted.)
- `r_ratios_sweep.json` — the 21 sweep records behind the §2 table.
- `r_ratios_vs_A.png`, `r_schur_denominators.png` — the report's plots.

## Conventions that must be preserved

- **Sign: k = g − λN** (Suzuki v2 §8.3, re-verified [D] against the v2 PDF directly).
  v3's flipped sign (g + λN) contradicts v3's own S_a definition — rejected.
- **λ = −1 only.** The λ = 0 solve is untrustworthy (γ-pinning canary: cond ~1e8
  hallucinates minima pinned at zeta-zero ordinates). The odd-sector ill-posedness in
  §4 is *not* this canary — it persists at λ ∈ {−2,−1,−0.5,−0.2} with modest cond.
- **N(x,y) = (x²+y²)/(4A) − |x−y|/2 + A/6** (Suzuki v2 §8.2); k_x(0,y) = −g′(y) − λ·sign(y)/2.

## Reproducing the §4 claim

Run `diag_r.py`-style refinement at A = 2, N = 400→3200: M_{1x} should read
28.5 → 45.6 → 74.3 → 123.6 (analytic prediction under bounded odd-sector
invertibility: exactly 1). The small-eigenspace diagnostic shows near-null modes at
~1.6e−8 in both parities, the odd ones overlapping the x-source at ~1e−3.

Original sandbox paths (run dir `runs/20260930-divisor-tension/`): filenames kept
identical to the provenance citations in `r_ratios_gate.md` §7.
