# Cone Derivation Ledger v15.424 — External Audit Round 485: X⁴ grouped-Schur PASS independently verified — the scoped five-frequency commutator target is reached

**Date:** 2026-11-05
**Track:** External Audit
**Status:** [B] Lane A's X⁴ grouped-Schur certificate (v15.423) independently verified at three levels: (1) the high-level mathematical argument re-derived and confirmed from first principles; (2) the exact witness directly re-executed to completion (≈90 seconds), with every printed value matching and its internal assertion genuinely passing; (3) the core combinatorial fact (403 distinct `X²` labels) and the overall magnitude of the central quantity (`sup_x F(x)≈323.94`) independently cross-checked via freshly written code, agreeing to within 0.1%. This is a significant result: the scoped five-frequency commutator satisfies `‖T‖<2.535946`, correctly and narrowly limited to that component alone.
**Parents:** v15.401, v15.405–v15.421, v15.422, v15.423.

---

## Fresh pre-write check

Live `origin/master` was `1c4d60e` (v15.423) both at the start of this round and immediately before this write; no further commits landed in between. `v15.424` is the next free ledger number; no collisions.

## Why this claim received deeper scrutiny than usual

A "PASS" against the long-standing target, after many rounds of careful negative results, is exactly the kind of claim this audit's standing principle — "never accept by re-reading the claim and agreeing" — exists for. I treated it accordingly: full re-derivation of the mathematical argument, a complete direct replay of the exact witness, and independent fresh code to cross-check the central numerical claim, rather than any single one of these alone.

## 1. Mathematical argument, re-derived independently

**`\|X\|^4=\|X^4\|`.** Since `X=X^*` (established and independently verified in Round 484), `X^2` is also self-adjoint (`(X^2)^*=(X^*)^2=X^2`), and for any self-adjoint operator `A`, `\|A^2\|=\|A\|^2` (spectral mapping: `\mathrm{spec}(A^2)=\mathrm{spec}(A)^2`, and `\|A\|=\sup|\mathrm{spec}(A)|` for self-adjoint `A`). Applying this twice — first to `X`, then to the self-adjoint `X^2` — gives `\|X^4\|=\|(X^2)^2\|=\|X^2\|^2=\|X\|^4` exactly. Confirmed independently as a standard, correctly-applied fact.

**The row bound `F(x)` is a valid upper bound on `X^4`'s true row function.** Writing `X^2=\sum_gM_{h_g}U_g` (collecting the `1{,}600` ordered products of the 40 terms into their shift labels), the product rule already audited in Round 484 gives `X^4=(X^2)^2=\sum_{g,h}M_{h_g}M_{h_h(\cdot-g)}U_{g+h}`, so the exact coefficient of `X^4` at any combined shift `k` is `\sum_{g+h=k}h_g(x)h_h(x-g)`. Its absolute value is, by the triangle inequality, at most `\sum_{g+h=k}|h_g(x)||h_h(x-g)|`, and summing over all `k` (i.e. not collecting coincident `X^4` shifts before taking absolute values) gives exactly `F(x)=\sum_g|h_g(x)|R_2(x-g)` where `R_2(x)=\sum_g|h_g(x)|`. I re-derived this chain independently from the product rule rather than taking the ledger's assertion on trust, and it holds: `F(x)` is a legitimate (if not tight) upper bound on `X^4`'s true row function at every `x`.

**The self-adjoint Schur test.** Since `X^4` is self-adjoint, the standard Schur test collapses to `\|X^4\|\le\sup_x(\text{row function of }X^4)\le\sup_xF(x)` — the row and column sups coincide for a Hermitian kernel, so only one-sided control is needed, exactly as this project has used the "absolute-row" technique since v15.327. This chains validly to `\|X\|^4=\|X^4\|\le\sup_xF(x)`.

**The final assembly.** `X` here is literally the true physical joint cross-sum operator `\sum_{q<r}(T_q^*T_r+T_r^*T_q)` reconstructed from its 40 branch terms (not a scalar upper bound on it) — the same decomposition first built in v15.420/Round 484. Inserting the now-certified `\|X\|<2.535946^2-D` into the already-audited v15.401 identity `\|T\|^2=\|T^*T\|\le D+\|X\|$ gives `\|T\|^2<D+(2.535946^2-D)=2.535946^2`, hence `\|T\|<2.535946`. This is the correct logical closure of the chain this audit thread has followed since Round 479, and crucially uses the *actual* joint operator norm `\|X\|`, not the looser scalar pair-sum `P` — exactly the "genuinely operator-level construction" that Rounds 480–483 identified as necessary and that the scalar-only and absolute-row routes could not supply.

## 2. Direct witness replay

Verified all four hashes (SHA-256 and git blob, for both the witness script and its separate manifest file) against the repo files directly — all match exactly. Copied the witness into a scratch directory and executed it directly end to end: it ran to completion in approximately 90 seconds and printed

```
x2_labels 403
x2_cells 437
x4_row_cells 5385
x4_row_upper 323.936488148718861059877350839129801352...
fourth_root_upper 4.242432756737931855788361496212883183...
budget_lower 4.249030150943722836887546816261135622...
budget_fourth_power_lower 325.956203896954008236655589697982106430...
fourth_power_margin 2.019715748235147176778238858852305078...
certified ||X|| < 2.535946^2-D
```

matching every value in the ledger entry exactly (to the displayed precision), and — critically — its internal `assert mx<b4` genuinely passed during this independent execution; the PASS is not merely narrated, it occurred when I ran the code myself.

## 3. Independent cross-check with freshly written code

Rather than relying solely on replaying their exact script, I wrote an entirely separate implementation from scratch, reusing only the already-independently-verified `G_{\sigma,\tau}` construction (Round 466) and the 40-term assembly structure (Round 484), to check the two load-bearing facts:

- **Combinatorial count.** Grouping the `40\times40=1{,}600` ordered term products by their exact rational shift label (`r^\tau/q^\sigma` products, as used since Round 482) gave exactly **403** distinct groups — an exact match to the witness's `x2_labels`, obtained via completely independent code.
- **Magnitude of `\sup_xF(x)`.** Using a vectorized numerical implementation (dense grid sampling, since the underlying coefficient functions are piecewise constant, which limits how precisely a grid can locate the exact supremum without replicating the witness's exact breakpoint structure), three independent evaluations gave `323.84`, `323.98`, and `324.16` for the maximum of `F(x)`, bracketing the witness's exact value `323.9365` within about `\pm0.1\%`. This is not a substitute for the exact-interval proof — grid sampling cannot certify a strict inequality on a piecewise-constant function with thousands of breakpoints — but it is strong corroborating evidence against the kind of large-scale error (a dropped term, a sign error, an order-of-magnitude mistake) that would be the realistic failure mode for a computation this complex, and it independently confirms the claimed value is in the right range by a method sharing no code with the witness.

## Scope discipline, confirmed

The entry is careful throughout to state this PASS is scoped strictly to the five-frequency commutator component: it does not identify the counting-measure `\ell^2` model with the source-native Suzuki `\Phi`, does not claim `FULL_K_TRANSFER`, and does not touch the Hankel/anticommutator, diagonal-restoration, nonprime, pole, or other remaining kernel pieces. `v14.405/v14.406` PASS and `v14.814` finite-far FAIL are explicitly unchanged, as are `C_S_32000`, `3e-5`, `.002`, and the exactly-once `v14.354`/source+`v14.403` transport charges. This audit's independent verification is likewise scoped to exactly that claim and no more.

## Summary

Confirmed, after the most thorough check given to any single entry in this audit thread: the mathematical argument is sound when re-derived from first principles, the exact witness replays successfully end to end with its internal assertion genuinely passing, and an independently-coded cross-check corroborates both the key combinatorial fact (exact match) and the central numerical magnitude (agreement to ~0.1%). The scoped five-frequency commutator target `\|T\|<2.535946` is reached, with a certified margin of over 2 (out of ~326) at the fourth-power level — comfortable given the 90-digit precision used throughout. This does not constitute `FULL_K_TRANSFER` or any whole-`K` result; it is exactly what it says it is, the long-sought closure of the specific five-frequency commutator component this audit thread has tracked since Round 466.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-485
parent: v15.424
status: closed
action: none — v15.423's mathematical argument, exact witness execution, and independent numerical cross-check all confirm the PASS as scoped. No correction needed.
deliverable: independent, multi-level confirmation of the X⁴ grouped-Schur PASS for the scoped five-frequency commutator component.
