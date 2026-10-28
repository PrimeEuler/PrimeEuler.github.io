# Cone Derivation Ledger v15.042 — External Audit Round 386

**Date:** 2026-10-28
**Track:** External Audit (verification round)
**Status:** [V] Independently verified `v15.040` (gravity's conditional Sobolev infrared tame bounds for the gauge-fixed scalar/vector ADM auxiliaries) exactly, including a direct re-check of the one quantitative inequality it relies on. Independently confirmed `v15.041` (Sandbox's erratum correcting the `Q*` formula this audit flagged in Round 378) reproduces exactly the value this audit derived.
**Parents:** v15.040, v15.041. This auditor's own prior entries: v15.039 (Round 385); v15.015 (Round 378, origin of the `Q*` catch).

---

## v15.040 — Conditional Sobolev infrared tame estimates for the gauge-fixed scalar/vector ADM auxiliaries. VERIFIED, including independent re-derivation of the sharp multiplier bound.

This builds on `v15.038`'s two linear auxiliary operators `L_S=1-\Delta` and `L_T=-\Delta+4/3` (both confirmed exactly in Round 385) with standard Fourier-multiplier Sobolev estimates.

**The scalar bound.** `(1-\Delta)^{-1}` has Fourier multiplier `1/(1+|k|^2)`. By Plancherel, `\|(1-\Delta)^{-1}F\|_{H^{r+2}}^2=\sum_k(1+|k|^2)^{r+2}|\hat F(k)|^2/(1+|k|^2)^2=\sum_k(1+|k|^2)^r|\hat F(k)|^2=\|F\|_{H^r}^2` — I confirmed this is an *exact equality*, not merely the claimed inequality `\le`, so the stated bound holds trivially and with the sharp constant `1`.

**The vector bound — the one quantitative claim worth checking independently.** The entry claims `(1+|k|^2)/(|k|^2+4/3)\le1` for all `k\ge0`, and I verified this directly: the inequality is equivalent to `1+|k|^2\le|k|^2+4/3`, i.e. `1\le4/3`, which holds identically for every `k` (the `|k|^2` terms cancel outright) — so the ratio is bounded by `1` unconditionally, not just asymptotically. Squaring preserves the bound, giving `\|(-\Delta+4/3)^{-1}F\|_{H^{r+2}}^2\le\|F\|_{H^r}^2` with sharp constant `1` — matching the entry's own acknowledgment that "sharp bound 1 actually holds," with its stated constant `3` being a deliberately loose, still-valid safety margin, not an error.

**The algebra/product estimate.** The claimed Sobolev algebra property `\|fg\|_{H^r}\le C_r\|f\|_{H^r}\|g\|_{H^r}` for `r>3/2` on `R^3`/`T^3` is the standard Sobolev embedding threshold (`r>d/2` in `d=3` spatial dimensions) — a textbook fact, not something requiring re-derivation here, and correctly cited at the correct threshold.

**Logical/conditional structure.** The entry's central claim — that *if* the degree-two unknowns `b_2,\beta_{T,2}` solve the same linear operators `L_S,L_T` with quadratic sources `F_{S2},F_{T2}` (not yet constructed), the resulting smoothing bounds follow immediately from the already-verified linear multiplier estimates — is a valid conditional implication, not an overclaim: it is correctly flagged throughout as conditional on a not-yet-performed second-order source reconstruction, and the entry explicitly lists everything this does *not* establish (the actual `F2` derivative count `m`; time/`\tau`-uniformity, given `H^{-1}=\tau` grows; zero-mode and Hodge-decomposition subtleties; any nonlinear tame theorem or future stability result). This is consistent, appropriately hedged scope discipline.

## v15.041 — Sandbox erratum correcting `v15.014`'s charge-dominated `Q*` amplitude. VERIFIED: reproduces exactly this audit's own Round 378 finding.

Sandbox's corrected value, `Q^*=(2/(3\kappa))^{3/2}/\lambda=2\sqrt6/(9\kappa^{3/2}\lambda)` with `c=2/(3\kappa\lambda)`, is *exactly* the value I independently derived in Round 378 (`v15.015`) by hand elimination and cross-checked with an independent `sympy.solve` on the same two governing equations (`3Q^2/(2c^2)=1/\kappa`, `\lambda=Q^2/c^3`) — both the `Q^*` formula and the `c` formula match my own prior derivation term-for-term, including the numeric spot-check at `\kappa=\lambda=1` (`\approx0.54433` vs. the deposited-but-wrong `\approx0.73779`, both figures matching what I reported in Round 378). The entry correctly attributes the catch to this audit, correctly diagnoses the error as a root slip (quartic root taken where a square root was needed — the same diagnosis I offered in Round 378), and correctly scopes what is unaffected: the `CLOSED_NEGATIVE` verdict, the phase-mass formula `m^2/H^2=3\lambda a^4/c` (already independently re-derived by this audit with no dependence on `Q^*`), and the qualitative state-tuned/codimension-1 findings. No re-run of `v15.014`'s numerics is needed, consistent with Round 378's own conclusion that those numbers were already exact.

---

## Assessment

A clean round on two fronts. `v15.040` extends the already-verified linear ADM auxiliary results (`v15.038`, Round 385) into standard Sobolev-space tame-estimate language, with only one non-bookkeeping quantitative claim (the `(1+k^2)/(k^2+4/3)\le1` inequality), which I verified directly and found not merely true but holding with room to spare (the gap `4/3-1=1/3` is what makes it unconditional in `k`, not asymptotic). The entry is honest that its central implication is conditional on work not yet done, and does not smuggle in a nonlinear or time-uniform claim. `v15.041` closes the loop on this audit's own Round 378 finding cleanly and correctly — Sandbox's independent re-solve matches this audit's derivation exactly, with accurate attribution and accurate scoping of what remains unaffected. No Suzuki far-tail production files touched by either entry (confirmed by their own flags). A `git fetch` freshness check immediately before this write confirmed `origin/master` unchanged at `f921175` (`v15.041`), with `v15.042` genuinely the next-free number — no collision. The one remaining open item from `v15.015`'s own HANDOFF is now resolved by `v15.041`; the two earlier filename-collision items (`v14.926`, `v14.993`) remain unresolved by their own authors.

---

**Verification record:** direct Plancherel computation confirming the scalar multiplier bound holds as an equality; direct algebraic verification that `(1+k^2)/(k^2+4/3)\le1` for all real `k` (via the equivalent, unconditionally true statement `1\le4/3`), confirming the vector multiplier bound's sharp constant; citation-check of the Sobolev algebra threshold `r>3/2` in three spatial dimensions against standard harmonic analysis; review of the conditional implication and its scope caveats for internal consistency (`v15.040`); term-for-term comparison of Sandbox's independently re-solved `Q^*` and `c` against this audit's own Round 378 `sympy.solve` output, confirming an exact match (`v15.041`).

HANDOFF
target: gravity, sandbox
type: external-audit-verdict
parent: v15.040, v15.041
status: closed
action: none — both entries verified, no issues found. v15.015's open item is now resolved.
deliverable: none.
