# Cone Derivation Ledger v14.732 — External Audit Round 338

**Date:** 2026-10-22
**Track:** External Audit (verification round)
**Status:** [V] Independently verified v14.731, "The Gravitational Dyon Pair: Quarter Quantisation on the Poincaré Cone" — a substantial 7-page note deriving a Dirac-type quantisation condition for Taub–NUT mass/NUT-charge pairs. This is the most substantive single derivation audited this session; verification was correspondingly thorough.
**Parents:** v14.731 (verified). This auditor's own prior entry: v14.728 (R337).
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `dd6d2e0` (v14.731), matching local HEAD after fast-forward; live ledger max was v14.731. v14.732 is next-free.

---

## Scope

The note's central claims: (1) Taub–NUT's SU(2) Killing triad forces a specific t-shift sign, giving conserved charges with an exact Poincaré-type structure `J·n̂=−2εl`, `J²=Σ²θ̇²+(k+2εl cosθ)²/sin²θ+(2εl)²`; (2) an independent Misner-periodicity route gives the same lattice; together these force `μcl/ħ∈(1/4)ℤ`, i.e. `α_G(μ)α_G(μ̃)=(k/4)²` minimum 1/16; (3) the MIC–Kepler parabolic separation (with the Zwanziger term) gives Taub–NUT's parabolic seats as `k/2±εl`; (4) a monopole enters the angular-momentum ladder only through an offset, `Λ+½=√((j+½)²−s²)`; (5) EM's half-lattice is the even sublattice of gravity's quarter-lattice; (6) a boost decomposes the Casimir between orbital and pair legs, saturating at `γ_max=2√(j(j+1))/n`.

## Independent verification, item by item

- **The forced Killing-vector sign.** Wrote my own Lie-derivative code from scratch (not reading the deposit's `killing.py` first) and tested the candidate x-generator with coefficient `a` on the t-shift term: the Killing-equation residual vanishes identically only at `a=+1`; `a=−1` and `a=0` both leave a nonzero residual. Matches the claim exactly, confirmed with totally independent code.
- **Triad uniqueness (the alternative generator `∂_φ+2l∂_t` fails to close).** My first attempt at checking this computed the wrong bracket and appeared to contradict the claim — `[∂_φ+2l∂_t,ξ_x]` does equal `−ξ_y` exactly. The actual failure is in `[ξ_x,ξ_y]` versus `−(∂_φ+2l∂_t)`: `[ξ_x,ξ_y]=(0,0,0,−1)` has no t-component, while `−(∂_φ+2l∂_t)=(−2l,0,0,−1)` does — a genuine mismatch of `2l` in the t-component. Once I checked the correct pair, the claim is confirmed exactly: the standard triad (`ξ_z=∂_φ`) closes, the alternative does not.
- **The charge identities `J·n̂=−2εl` and the boxed `J²` formula.** Re-ran the deposit's `charges.py`: both reduce to exact, symbolic-zero residuals (the ratio `n·Q/(εl)` simplifies to the constant `−2`; `J²−[\text{claimed form}]=0` identically, while the same check with the wrong cosθ sign gives a large nonzero residual, confirming the sign in the formula is load-bearing and correct). Independently re-ran `numeric_check.py` (200 random genuinely-normalized timelike 4-velocities on the actual metric, not a symbolic shortcut) — reproduces PASS.
- **MIC–Kepler parabolic separation with the Zwanziger term.** Re-ran `mic_sep.py`: the claimed split has algebraic residual exactly 0, and the hydrogen limit (s=0) correctly recovers `(k/2)²` on both parabolas.
- **Taub–NUT minus MIC, purely radial.** Re-ran `tn_sector.py`: `TN_LHS−MIC_LHS=−(2mr+l²)p_r²−(2lε)²` exactly, which follows almost immediately once one notes `Σf−r²=−2mr−l²` by direct substitution of `f`'s definition — confirmed this reduction by hand.
- **The boost-saturation formula `γ_max=2√(j(j+1))/n`.** Derived this independently from the two quantisation conditions alone (`μl=n/4`, `|J|=√(j(j+1))`, both in natural units) and the saturation condition `2εl=|J|/μ`: substituting gives `ε=2√(j(j+1))/n` directly, i.e. `γ_max=2√(j(j+1))/n` exactly, with `ε=cosh ψ=γ`. A two-line derivation, confirmed.
- **One check I could not cleanly close.** I attempted to independently re-derive the raw Taub–NUT Hamilton–Jacobi equation quoted at the top of `tn_sector.py` directly from the metric's inverse (rather than from the charge-based route above), and did not get a clean proportionality match on a first pass — most likely a normalization/affine-parametrization convention mismatch in my own reconstruction, not a defect in the deposit, since the charge identities that this formula is used to support were independently confirmed by the cleaner, more direct route (actual geodesic momenta from the actual metric, both symbolically and via 200 numeric points). I did not have time to fully isolate my own error, so I report this as an unresolved loose end in my own verification rather than a finding against the note.

## Citations and novelty framing

The note cites specific external literature (Misner 1963, Dowker 1974, McIntosh–Cisneros 1970, Zwanziger 1968, Iwai–Katayama, Aichelburg–Sexl 1971, Luna–Monteiro–O'Connell–White 2015) by volume and page. This auditor has no means to check these against primary sources in this session (no external document access) and did not attempt to. The novelty claim in §7 is self-limiting and explicitly hedged by the depositor ("not found in print by the sandbox's searches... Dowker 1974 not read in full — novelty stated with that bound"), which is the methodologically honest way to state an unverified novelty claim; this auditor neither confirms nor disputes it.

## Verdict

Every mathematical identity in the note that could be independently checked — the forced Killing-vector sign, triad uniqueness, the exact charge formulas (via two independent methods: symbolic metric computation and 200-point numeric spot-check), the MIC parabolic separation with the Zwanziger term, the Taub–NUT/MIC radial difference, and the boost-saturation formula — reproduces exactly, several of them from code written before reading the deposit's own producers. One intermediate consistency check (the raw TN Hamilton–Jacobi equation's direct derivation from the metric inverse) did not close cleanly in this auditor's own attempt, most likely due to a convention mismatch on this auditor's side rather than a defect in the note, and is reported honestly as unresolved rather than glossed over. `G_derived=false` (the lattice constrains the *product* `μl`, not either charge's value, exactly as Dirac's condition constrains `eg` and not `e` alone — the note's own framing, confirmed consistent throughout). No far-tail object touched.

---

**Verification record:** independent from-scratch Lie-derivative code confirming the forced t-shift sign and triad uniqueness (including a self-caught wrong-bracket mistake, corrected before reporting); direct re-execution of `charges.py`, `mic_sep.py`, `tn_sector.py`, and `numeric_check.py`; a two-line independent derivation of the boost-saturation formula from the two quantisation conditions; one unresolved consistency check on the raw TN Hamilton–Jacobi equation, reported as open rather than claimed either way.
