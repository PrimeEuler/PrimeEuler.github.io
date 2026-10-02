# Cone Derivation Ledger v13.933 — Sandbox Erratum to v13.926: the "Positive Spectral Gap" Was a Quadrature Artifact

**Date:** 2026-10-01
**Track:** Sandbox / exploratory lane (little Euler)
**Status:** [D] exact artifact mechanism; [N] independent reproduction; [O] reopened: v13.910's "continuum if"
**Authorization:** Jeremy, 2026-10-01 ("yep" — authorizing the v13.926 erratum)
**Parents:** v13.926 (the entry under correction), v13.910 (the conditional whose status is restored), v13.915 (the prior result v13.926 failed to cross-check), v13.928 (External Audit Round 139 — the finding), v13.932 (companion entry whose numbers were re-verified under the corrected protocol)
**Collision check:** live head v13.932; v13.933 absent.

---

## 0. What is withdrawn

v13.926 claimed, as its central result [N]:

\[
\inf_{H^1_0(-2,2)} RQ_{\rm full} = 1.83\times10^{-8} > 0,
\]

"N-stable, O(h²)-converged," thereby **refuting** the v13.910 §7 conditional ("if inf RQ_full = 0 then the continuum V-shape is exact").

**This claim is withdrawn.** The "converged positive gap" was a discretization artifact, not a continuum fact. The v13.910 conditional is **reopened**, not refuted; the available evidence now leans toward the "if" being true.

Nothing in v13.910's conditional logic [D] is affected — only v13.926's verdict on its hypothesis.

---

## 1. The artifact [D/N]

External Audit Round 139 (v13.928) identified the mechanism, independently reproduced here (§2):

- `fem_screw.py`'s `build_G2(g, a, ngrid=40001)` approximates the exact double antiderivative G2 (G2″ = g) by cumulative trapezoid on a **fixed** grid, then a cubic spline.
- `assemble_Q` builds the stiffness-like matrix from **second differences of G2 at mesh spacing h = 2a/N, divided by h²**.
- Hence any residual G2 quadrature error is amplified by **1/h²**: the quadrature grid (ngrid) and the FEM mesh (N) are not independent discretization parameters. v13.926 varied only N, holding ngrid at the hardcoded default 40001 throughout — its "N-convergence" study was converging to an artifact of the fixed, unrefined grid.

Scale signature, confirmed by direct test: at N = 20, λ_1 is stable across ngrid (7.325e−6 → 7.295e−6); at N = 100 it drifts; at N = 200 it is clearly unstable — exactly the 1/h² amplification onset.

---

## 2. Independent reproduction [N]

Re-ran the v13.926 pipeline at a = 2, N = 800, varying only ngrid:

| ngrid | λ_1(Q_full) |
|-------|-------------|
| 40,001 | 1.839754e−08 |
| 160,001 | 1.488960e−09 |
| 640,001 | 1.271454e−10 |

This matches Round 139's numbers to 4 digits at every point, and reproduces v13.926's own table entry (1.8398e−08) to 5 digits at the default ngrid — confirming both that v13.926's observation was real and that it was converging to the artifact. λ_1 shrinks ~3–4× per ngrid doubling with no plateau: the textbook signature of an O(δ²) quadrature error converging to zero, not of a positive eigenvalue being resolved.

---

## 3. Two misses, recorded

1. **ngrid was never varied.** The entry's reproducibility note lists only N-refinement. A second discretization parameter with a known 1/h² coupling went unexamined.
2. **No cross-check against v13.915.** That entry's `selector_principle_exploration.md` (Test A) already reports, for the same object, "Full form: λ_1 = 0.000000 in both sectors (**numerical floor, as expected** at a = 2)" — the established expectation, consistent with the entire Λ-rigidity arc's knife-edge premise (λ_1(Q_full) at the boundary of the positivity cone). v13.926 contradicted it without noticing.

---

## 4. What survives, what is unconfirmed

- **Survives [D]:** the v13.910 §7 conditional itself — its logic never depended on the hypothesis being true.
- **Unconfirmed:** v13.926 §§3–4 (frequency-response high-pass profile, two-bump Ritz plateau at 1.07e−07). These may use computational paths not implicated by this specific bug, but the entry's interpretive framing leaned on §2's floor being real; treat them as unconfirmed pending re-computation with controlled quadrature, not as independently safe.
- **Survives [N]:** the m=7 slope measurements of v13.932. Those are O(1) secant differences (Δλ_1 ~ 7e−3 at ε = 0.01, five orders above the ~1e−8 floor), and were re-verified under 32× ngrid refinement with a clean plateau (1.21104 → 1.21321 → 1.21326). Different measurement regime; unaffected.

---

## 5. Corrected protocol for this pipeline

Until `build_G2` is replaced by a quadrature scheme whose error is controlled independently of N (adaptive quadrature per Toeplitz entry, or the analytically exact piecewise antiderivative between the known kink locations log n), every FEM number from this pipeline must be checked under **joint** refinement — e.g. ngrid ≳ 100N at every N — never N alone.

---

## 6. Result

\[
\boxed{
\text{v13.926's "REFUTED" verdict on the v13.910 conditional is withdrawn.}
}
\]

\[
\boxed{
\text{v13.910's "if" (}\inf RQ_{\rm full} = 0\text{) is reopened [O], with the evidence leaning true.}
}
\]

The exact continuum V-shape question is back where v13.910 left it: a proved conditional awaiting its hypothesis.
