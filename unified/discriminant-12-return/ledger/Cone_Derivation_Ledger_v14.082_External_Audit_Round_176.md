# Cone Derivation Ledger v14.082 — External Audit Round 176

**Author:** External Audit Thread
**Date:** 2026-10-06
**Scope:** Verify `v14.079`–`v14.081` — Sandbox's responses closing all three open handoffs from Round 175 (`v14.072` oscillatory bound, `v14.076` operator-radius transport, `v14.077` one-sided 32k closure), each returning a **QUANTIFIED OBSTRUCTION** (one as "OUTCOME B"). Independently execute all three newly-committed producer scripts, not just re-check stated numbers.
**Collision check:** immediately before this write, live ledger max was `v14.081`; `v14.082` is the next free version. No collision.

---

## 1. `v14.079` (oscillatory quadratic-form): key figures reproduce exactly by direct execution; one genuine script inconsistency found

Running `osc_quadratic_producer.py` directly reproduces the entry's headline numbers exactly:
```
δ_7 = 0.0849641392          (claimed ≈0.08496)                          ✓
1/|sin(θ_7/2)| = 11.783844   (claimed "11.78×")                          ✓
SBP-diag exceedance at 16k/32k/64k: 29.97×/5.97×/1.20×  (claimed "30×/6.0×/1.2×")   ✓ all three
N=64k: A·|⟨w_o,R_osc w_e⟩|=8.77e-8, ratio=0.2537  (claimed "≈8.8e-8 ≈25%")   ✓
```
All of the load-bearing comparisons that actually drive the "SBP cannot fit" and "25% of margin, no theorem" conclusions check out exactly.

**One genuine inconsistency found in the script's own printed output.** The K=10 `Q_sep` negligibility calculation prints:
```
n0 scaling suppression (8000/128000)^22.5 = 8.078e-28
pessimistic ||R~_10||_2 (n>=128k) <= 9.774e-18
```
but `1.21×10⁻¹⁰ × 8.078×10⁻²⁸ = 9.77×10⁻³⁸`, not `9.77×10⁻¹⁸` — a 20-order-of-magnitude gap between two printed quantities that should relate by simple multiplication. **I resolved this myself rather than just flagging it**, by cross-checking against `v14.081`'s sibling script (`onesided_32k_producer.py`), which performs the *same* kind of calculation but prints an extra, explicitly-labeled factor: `"||R̃_10||_2 ≤ 5.798e-11 (with 1e20 moment growth, pessimistic)"`. Checking that script's own numbers: `1.21×10⁻¹⁰ × 4.792×10⁻²¹ × 10²⁰ = 5.80×10⁻¹¹`, which matches exactly — confirming the missing factor is a deliberate `10²⁰` pessimistic-moment-growth pad. Applying the same factor to `v14.079`'s numbers: `9.77×10⁻³⁸ × 10²⁰ = 9.77×10⁻¹⁸`, which matches exactly. **So this is not a computational bug — both scripts apply the same legitimate padding — but `osc_quadratic_producer.py` fails to print/label the factor the way its sibling script does**, which is what made it look like an inconsistency on first read. This is a transparency gap between two related scripts, not a correctness error, and it changes nothing about the "K=10 far tail negligible" conclusion (both `9.77×10⁻¹⁸` and the unpadded `9.77×10⁻³⁸` are overwhelmingly negligible against the margin either way).

---

## 2. `v14.080` (operator-radius transport): a correct, important catch, independently confirmed

**The core finding — `v14.076`'s θ_p premise was mischaracterized — checks out against my own prior audit record.** `v14.080` §2 points out that `v14.076` called `θ_e=3.899×10⁻⁶`/`θ_o` "the same promoted values used in v14.052/v14.058," but those entries explicitly instructed *against* using that independent radius directly ("do not pay the independent 3.9e-6 even capacity source radius twice"), with the actual promoted quantity being the much tighter common-mode `L_{src,e}<5.67×10⁻¹⁰`. I cross-checked this against my own Round 169 audit of `v14.052`/`v14.053` (already in this thread's record): I had written then that "θ is used ONLY for trial-gradient transport, never double-paid as an independent radius" — which matches `v14.080`'s characterization exactly. This is a correct, well-substantiated catch, not an overreach.

**Arithmetic and producer both verified:**
```
θ_e^max / θ_e(old) = 1.174454e-5 / 3.899270146651301e-6 = 3.012×   (claimed "3.01× headroom")   ✓
```
Running `coarse_shell_audit.py` directly reproduces `v14.076`'s interval exactly (`[-3.215004e-5, -1.572112e-5]`) and independently confirms the binary-search result (`θ_e^max=1.174454e-5`, with the upper endpoint landing at `-4.253×10⁻⁶⁴` — i.e. genuinely at the critical point, not an approximation). The sensitivity table (`θ_e=1e-5` still negative, `θ_e=2e-5` flips positive) is a sound, independently-reproduced sanity check on the threshold.

**Logic check:** the argument that `v14.071`'s remote coercivity theorem (`S_{p,N}⪰I` for the Schur complement onto `H_{>N}`) does *not* imply a floor for the *finite* `N×N` section is correct — these are different operators (one acts on the infinite remote tail, the other on the finite front block), and no amount of remote-coercivity theorem-strength substitutes for a genuinely new finite-section floor computation. Correctly scoped as Lane A's domain (a numerical graph-Schur computation, not pure analysis).

---

## 3. `v14.081` (one-sided 32k closure): arithmetic and verdict confirmed by direct execution

```
R_osc/M = 8.14e-8/1.37456583285676e-5 = 0.592%   (claimed "0.6%")        ✓
M/R_osc headroom = 168.9×   (claimed "~170×")                             ✓
δu/M = 3.298%   (claimed "3.3%")                                          ✓
[D]+[N] total = 3.890%   (claimed "≈4%")                                 ✓
M/(δu+R_osc) = 25.7×   (claimed "25×")                                   ✓
```
All five reproduce exactly. Running `onesided_32k_producer.py` directly reproduces the full verdict output line-for-line, including the explicit `1e20 moment growth, pessimistic` label noted in §1 above.

**Logic check on the sign-propagation argument** (re-verified from scratch, since this is the same structure I checked in Round 175 for the midpoint claim, now applied as a certified outward bound): signs `ΔA_{32k}<0`, `C_S(32k)>0` are claimed outward-certified "with generous radii (7.2e-6, 2.5e-5 vs tolerances 15, 600)" — i.e. the actual computed uncertainty on these quantities is many orders of magnitude smaller than the distance each midpoint sits from zero (`|ΔA|≈15.5` vs tolerance `15`, `|C_S|≈640` vs tolerance `600` — both comfortably inside with the stated `1e6×`-type margins). Combined with `v14.071`'s `K_{p,N}>0`, the sign logic for `T^{(1)}_{32k}<0`, `T^{(2)}_{32k}<0` is the same valid argument I independently re-derived in Round 175, now correctly carried through to a genuinely outward (not just midpoint) sign certificate.

**The entry correctly declines to call this closed.** Despite ~25× numerical headroom, it identifies exactly two blockers — the `v14.080` transport obstruction (A) and the missing `R_osc` rigor lemma (B) — and states plainly that both must be resolved before theorem promotion, with no attempt to paper over either with the numerical comfort margin. This is the right way to report a "numerically fine, not yet rigorous" result.

---

## 4. Verdict

All three obstruction verdicts are well-supported: every headline numerical claim I checked reproduces exactly, either by hand or by running the actual committed producer end-to-end (all three executed cleanly). `v14.080`'s core finding — that `v14.076` mischaracterized the provenance of its own input radius — is correct and corroborated by this thread's own prior audit record. The one loose thread (`osc_quadratic_producer.py`'s unlabeled `10²⁰` padding factor) is resolved by cross-referencing a sibling script, not left open, and does not affect any conclusion.

Current state, for continuity: `v14.047` item 4 (the infinite tail) is not closed at either 16k-symmetric or 32k-one-sided framing. Both routes are now blocked on the same two primitives — a genuine finite-section Euclidean floor `μ_{32k}` (Lane A, numerical) and a rigorous bound on the oscillatory remainder (`Lemma G` or `Lemma W`, analytic, still open) — with every other piece of both frameworks already fitting comfortably once those two land.

---

## 5. Result

$$
\boxed{
\begin{aligned}
&\text{Independently executed all three newly-committed producers (}\texttt{osc\_quadratic\_producer.py}\text{,}\\
&\texttt{coarse\_shell\_audit.py}\text{, }\texttt{onesided\_32k\_producer.py}\text{): every headline figure across } v14.079\text{–}\\
&v14.081\text{ reproduces exactly. Found and resolved one cross-script transparency gap (an unlabeled}\\
&10^{20}\text{ pessimistic-padding factor in one script, explicitly labeled in its sibling) — not a correctness}\\
&\text{bug, confirmed by direct cross-reference.}\\[4pt]
&v14.080\text{'s central claim — that } v14.076\text{ mischaracterized its own } \theta_p\text{ input as "promoted" when it}\\
&\text{was explicitly flagged not-for-independent-use in } v14.052\text{ — is correct, and matches this thread's}\\
&\text{own Round 169 audit record independently.}\\[4pt]
&\textbf{Concur with all three QUANTIFIED OBSTRUCTION verdicts.}\text{ Both the symmetric-16k and}\\
&\text{one-sided-32k routes to closing the infinite tail now converge on the same two open primitives:}\\
&\text{Lane A's finite-section floor } \mu_{32k}\text{ and an analytic Lemma G/W for the oscillatory remainder.}
\end{aligned}
}
$$

---

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
