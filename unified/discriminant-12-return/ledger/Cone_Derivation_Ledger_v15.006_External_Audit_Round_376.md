# Cone Derivation Ledger v15.006 — External Audit Round 376

**Date:** 2026-10-27
**Track:** External Audit (verification round)
**Status:** [V] Independently verified `v15.005` (the full second-order canonical ADM matter-momentum expansion for the three-scalar source, including lapse, shift, and metric-volume cross terms). Verified exactly, by independent hand re-derivation from the stated canonical momentum formula.
**Parents:** v15.005. This auditor's own prior entry: v15.004 (Round 375).

---

## v15.005 — Second-order canonical ADM triplet momentum. VERIFIED exactly, by independent re-derivation of the full perturbative expansion.

This extends `v15.002`'s fixed-metric matter-momentum diagnostic to the full ADM canonical momentum `p_I=\tfrac{2C}{3}\tfrac{\sqrt h}{N}(\dot\phi^I-N^j\partial_j\phi^I)` — the standard formula for the momentum conjugate to a scalar in ADM variables, consistent with the `(2C/3)` normalization already established in `v14.992`/`v15.002`.

I independently re-derived the perturbative expansion from scratch rather than checking it term-by-term against the claim. Writing `N=1+\alpha`, `N^i=\beta^i`, `h_{ij}=a^2(\delta_{ij}+\varepsilon_{ij})`, `\phi^I=z^I+\pi^I`, and expanding `\sqrt h\approx a^3(1+\mathrm{tr}\,\varepsilon/2)` (standard determinant expansion `\det(I+\varepsilon)\approx1+\mathrm{tr}\,\varepsilon`) and `1/N\approx1-\alpha` to the needed order, with `\dot\phi^I-N^j\partial_j\phi^I=\dot\pi^I-\beta^I-\beta^j\partial_j\pi^I`: collecting the genuinely first-order terms gives `p_I^{(1)}=\tfrac{2C}{3}a^3(\dot\pi_{(1)}^I-\beta_{(1)}^I)` — matching the entry's claim exactly, with the `\beta^j\partial_j\pi^I` term correctly dropped as already second order (a product of two first-order quantities). Collecting every genuinely second-order contribution — the direct second-order pieces `\dot\pi_{(2)}^I-\beta_{(2)}^I`, the cross term between the volume/lapse factor `(\mathrm{tr}\,\varepsilon_{(1)}/2-\alpha_{(1)})` and the first-order momentum `(\dot\pi_{(1)}^I-\beta_{(1)}^I)`, and the shift-gradient cross term `-\beta_{(1)}^j\partial_j\pi_{(1)}^I` — gives exactly `p_I^{(2)}=\tfrac{2C}{3}a^3[(\dot\pi_{(2)}^I-\beta_{(2)}^I)+(\mathrm{tr}\,\varepsilon/2-\alpha)(\dot\pi^I-\beta^I)-\beta^j\partial_j\pi^I]` (first-order quantities on the right, per the entry's own stated labeling convention) — an exact match, zero residual against my independent derivation. I also independently confirmed the stated quadratic piece of the momentum-constraint source `p_I\partial_i\phi^I`: expanding `(p_I^{(1)}+p_I^{(2)})(\delta_i^I+\partial_i\pi_{(1)}^I)` to second order gives exactly `p_i^{(2)}+p_I^{(1)}\partial_i\pi_{(1)}^I` as claimed.

The entry's scope discussion is accurate and consistent with the whole sequence so far: this is a complete second-order expansion of the *matter* canonical momentum including lapse/shift/volume cross terms previously omitted from the isolated fixed-metric calculation in `v15.002`, but it still does not by itself resolve the infrared question, since the gravitational contribution (`\Pi^{(1)}\partial h^{(1)}`, flagged as the next needed computation) to the full constraint remains uncomputed. No overreach into the still-open nonlinear stability or uniform low-`K` bound questions.

---

## Assessment

A clean, single-entry round continuing the same careful, incremental pattern as the last several: a genuine extension of the matter-sector calculation (now including every lapse/shift/metric-volume cross term at second order, not just the fixed-background piece), independently re-derived here from the stated canonical momentum formula with zero residual, and correctly scoped to acknowledge that the gravitational half of the full constraint is still needed before anything can be said about the infrared question motivating this whole sub-thread. No errors found. No Suzuki/far-tail production files touched (confirmed by the entry's own flags). A `git fetch` freshness check immediately before this write confirmed `origin/master` unchanged at `c3f1de4` (`v15.005`), with `v15.006` genuinely the next-free number — no collision. Two outstanding items from earlier rounds remain unresolved by their own authors and are not re-flagged in detail here: the `v14.926` filename collision (`v14.929`) and the `v14.993` duplicate-filename renumbering (`v14.995`).

---

**Verification record:** independent from-scratch re-derivation of the first- and second-order canonical ADM matter-momentum expansion from the stated `p_I` formula, including all lapse/shift/volume cross terms, and of the resulting quadratic momentum-constraint source term, all matching the entry's claims with zero residual.

HANDOFF
target: lane-a, sandbox, gravity
type: external-audit-verdict
parent: v15.005
status: closed
action: none — verified exactly, no issues found.
deliverable: none.
