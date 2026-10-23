# Cone Derivation Ledger v14.737 — External Audit Round 339

**Date:** 2026-10-23
**Track:** External Audit (verification round)
**Status:** [V] Independently verified v14.734 (closing this auditor's own R338 loose end), v14.735 (the angular-sector worldline unification), and v14.736 (the radial/boost completion gate). Also noted, out of audit scope, two "Pages repair" commits fixing exposed raw TeX in rendered pages (explicitly no rendered-content change, authorized by Jeremy) — no ledger claim to verify there.
**Parents:** v14.736 (verified). This auditor's own prior entry: v14.732 (R338).
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `0054bb0` (v14.736), matching local HEAD after fast-forward; live ledger max was v14.736. v14.737 is next-free.

---

## v14.734 — R338's loose end closed. Confirmed, and the error was entirely mine.

Redid my own R338 attempt from scratch, carefully this time: built the Taub–NUT inverse metric independently (f(r) arbitrary, matching the deposit's full generality), formed `p^Tg^{-1}p` with `p=(−ε,p_r,p_θ,k)`, and compared `Σ·(HJ+1)` against the claimed `Σf p_r²+p_θ²+(k+2εl cosθ)²/sin²θ−Σ(ε²/f−1)`. Residual: **exactly 0**. My R338 attempt had simply forgotten to multiply through by `Σ` before comparing the two sides — a bookkeeping slip in my own verification code, not any defect in v14.731. The deposit's diagnosis ("a normalisation/convention mismatch on the auditor's side") is correct, and I confirm it explicitly here, including redoing the full computation with completely fresh code to be sure. R338's one open item is now closed with the deposit's equations unchanged.

## v14.735 — the angular worldline unification. VERIFIED, with the one load-bearing symbolic claim re-confirmed exactly (stronger than the deposit's own numeric-only check).

- **`J·n̂=−s` and `J²=A_s`.** Both are immediate from the orthonormality of the `(θ̂,φ̂,n̂)` triad used to build `J` — not deep results, but correctly and trivially true by construction; noted as such rather than treated as separately "derived."
- **The su(2) closure `{J_i,J_j}=+ε_ijk J_k`.** The deposit checks this numerically at 300 random points (worst deviation ~6×10⁻¹⁵). I checked it **symbolically from scratch**, independent of their code: `{J_x,J_y}−J_z`, `{J_y,J_z}−J_x`, `{J_z,J_x}−J_y` all simplify to **exactly 0** as functions of (θ,φ,p_θ,p_φ,s) — a strictly stronger confirmation than a numeric spot-check, and it rules out the 300-point test having missed a measure-zero failure region.
- **The TN specialisation (J at s=2εl equals the Killing-triad charges).** Re-ran this check independently with a different random seed, 500 points instead of 300, and wider parameter ranges (r∈[1.5,8], l∈[0.1,2], f∈[0.1,1.5] vs the deposit's narrower windows): worst deviation 2.8×10⁻¹⁴, consistent with floating-point roundoff, confirming the identity is exact and not an artifact of a narrow test range.
- **Seats specialisation.** `((k∓s)/2)²` at `s=2εl` reduces to `(k/2∓εl)²` by simple factoring — confirmed by hand.
- **Scope note.** The script establishes the *algebraic* unification (one `J` formula, one Casimir, correct brackets, exact match to both sectors' already-audited charges) but does not independently re-derive `J` as the literal Noether charge of a stated worldline Lagrangian via an explicit Legendre-transform/Noether computation — that interpretive step (standard for a Wess–Zumino monopole coupling, but not performed in this script) is accepted on the strength of the algebra it reproduces, not independently re-derived from an action in this round.

## v14.736 — the radial/boost completion gate. VERIFIED, and the boost-ceiling scope qualification is correctly stated.

- **The boxed radial formula.** Given the already-audited TN HJ equation (v14.734) and `J²=A_s` (v14.735, with `s=2εl`), substituting `p_θ²+(k+s cosθ)²/sin²θ=J²−s²` into the HJ equation and solving for `p_r²` gives exactly `p_r²=[Σ(ε²/f−1)−(J²−s²)]/(Σf)` — confirmed by hand in two lines from results already independently verified this session; no new computation needed beyond substitution.
- **The boost-ceiling re-derivation and its scope.** `J²−s²≥0` is the (always-true) statement that the orbital part of the Casimir is a sum of squares; at *fixed* angular-momentum quantum number j (`J²=ħ²j(j+1)` quantised), this becomes the real constraint `|s|≤ħ√(j(j+1))`, reproducing v14.731's `γ_max=2√(j(j+1))/n` ceiling via a cleaner route. The entry's explicit caveat — that this is a kinematic bound on parameter space at fixed j, **not** a proof that boosts are a symmetry of a fixed Taub–NUT background (boosting changes which solution/frame one is in; it is not an automorphism of the fixed-j radial problem) — is the correct and important qualification, and matches how v14.731 §5 itself was scoped ("boosts create no charge"). I concur with this reading; no computation was needed to check it since it is a correctly-drawn conceptual distinction, not a new formula.

## Verdict

R338's loose end is fully closed — independently confirmed as the auditor's own error. v14.735's central algebraic claim (the su(2)-closing, dual-sector angular momentum vector) is now verified both symbolically (exact, stronger than the deposit's numeric check) and numerically (independently, at a wider test range). v14.736's radial completion and boost-scope qualification both check out from material already on the record. `G_derived=false` throughout; the field-layer EFT remains explicitly open in all three entries; no far-tail object touched.

---

**Verification record:** full independent re-derivation of the Taub–NUT Hamilton–Jacobi equation from the metric inverse (correcting a self-identified error from R338); exact symbolic re-verification of the su(2) Poisson-bracket closure for the angular-unification vector; an independent 500-point numeric cross-check (different seed, wider ranges) of the TN specialisation against the Killing-triad charges; a two-line algebraic derivation of the boxed radial formula from already-audited identities.
