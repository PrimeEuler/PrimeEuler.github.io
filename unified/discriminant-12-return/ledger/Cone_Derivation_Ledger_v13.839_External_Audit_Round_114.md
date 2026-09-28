# Cone Derivation Ledger v13.839 — External Audit Round 114

Date: 2026-09-28

Auditor: External audit thread (Claude, independent instance).

Scope: v13.838 — the sandbox Bucket 2 gap characterization ("Suzuki's text provides no two linear nullspace-fixing conditions"). This is the first ledger contribution from the project owner's sandbox track working the boundary-constant gate identified in v13.833.

Verdict: **PASS on the [D] textual catalog and the [C]/[D] logical structure. The [N] sandbox numerics could not be independently re-executed (scripts live outside this repo) and are correctly tagged as exploratory, not certified — I did not treat them as proven and neither does the entry. One small citation-fidelity finding in an exact quote, substance unaffected.**

## 0. Method note

This entry makes no finite-section numerical certification claims of the kind Rounds 99–113 have been verifying by re-running committed scripts. Its load-bearing content is (a) a textual catalog of what Suzuki's arXiv v2 actually contains, and (b) a retraction of an earlier sandbox claim. So this round's audit method is different: direct, independent extraction and cross-reading of the source PDF (`research-notes/2606.09096v2.pdf`) against every quoted passage, rather than script execution. The `[N]` sandbox numerics (§2) reference scripts and run directories outside this repo (`~/workspace/d12/lane_b/sandbox/runs/...`); I cannot execute what isn't committed here, and the entry itself does not ask me to — it tags them `[N]`, explicitly not `[N-cert]`, which is the honest classification.

## 1. Independent verification of the §1 textual catalog against the primary source

I extracted the PDF's text directly (all 32 pages) and checked every quoted passage character-by-character rather than trusting the ledger's transcription.

- **§1.1, Theorem 1.5 statement and normalization (p.6) and proof restatement (p.22).** Both quotes — "normalized so that `‖v+(a,·)‖_Ta = ‖v-(a,·)‖_Ta`" (Theorem 1.5, p.6) and "with the normalization `‖v+‖_Ta=‖v-‖_Ta`" (p.22 proof) — reproduce **verbatim**. The entry's assessment (one real, quadratic, cross-channel scale condition; irrelevant to the scale-invariant ratios `r_j=I_j/C`) is a correct reading — Theorem 1.5 fixes `|C_+|/|C_-|`, nothing about `I_0,I_1` individually.
- **§1.2, equation (8.4) (p.30).** `∫_{-a}^a (-k_xx(x,y))v_±(y)dy = C_± e^{±x}, x∈(-a,a)` reproduces **verbatim**. Confirmed this is the actual defining (differentiated) equation, and that Lemma 6.2's invertibility of `T_a` is what would make it determine `v_±` given `λ<λ_a`.
- **§1.3, equation (8.5) and the `A_±,B_±` formulas (p.30).** Reproduces verbatim, including the exact formulas `A_± = ∫k_x(0,y)(-v_±(y))dy ∓ C_±`, `B_± = ∫k(0,y)(-v_±(y))dy - C_±`. This directly confirms the entry's central technical point: `A_±,B_±` (the ledger's `I_1,I_0`) are defined as **functionals of the solution `v_±`**, i.e. outputs, not free inputs — which is exactly what makes §3's retraction correct (see below).
- **§1.2/1.3, "ignores domain issues" (p.30).** "Here we avoid expressing these equations in terms of the operators `T_a` or `S_a`, since the above argument ignores domain issues" reproduces verbatim.
- **§1.2/§2.1, `g'` kink structure (p.8).** "The kernel function `g` is continuous, and its first derivative is piecewise continuous with only a discrete set of discontinuities at which finite one-sided limits exist" reproduces verbatim. This is a real, correctly-cited structural fact about `g`, independently supporting the entry's claim that spline/smoothing discretizations of (8.4)/(8.5) throw away load-bearing content.
- **§1.5, minimal domain (1.10) (p.6).** `D(D_a):=C_c^∞(-a,a)` reproduces verbatim, correctly on the same page as Theorem 1.5.
- **§1.6, `θ=π` (p.30).** "Our numerical experiments provide evidence supporting (1.12) for the choice `θ=π`" reproduces verbatim.
- **§1.8, "(8.5) is different from..." disclaimer (p.30) — one finding.** The PDF's actual text is `S_a u_± = C_± D̄e_{±i}` (the bar is over the operator `D̄` applied to `e_{±i}` — this exact pattern, `S_a u_z = D̄e_z`, is spelled out one line earlier on the same page as a general rule before being specialized to `z=±i`). The entry's §1.8 quotes this as `S_a u_± = C_± \bar{e}_{±i}` (bar over `e`, no `D̄` operator at all). This is a transcription slip, not a misreading of the mathematics: the entry's point — that (8.5) is explicitly *not* the same as a naive inverse-source-style equation — is the correct substance of the disclaimer either way, and it's consistent with what v13.742/757/779 already established about the retracted `u_{A,±}=S_A^{-1}D̄e_{±i}` ansatz. Flagging it because exact-quote fidelity is the entire point of a `[D]` textual claim; it doesn't change the entry's conclusion.

No other discrepancies found. §1.7's "searched and absent" claim (no endpoint conditions, no decay conditions, no second normalization, no linear functional prescribed) is consistent with everything else on pages 6–31 that I read in the course of checking the other citations — I did not find a competing candidate condition anywhere in §§6–8.

## 2. The retraction (§3), checked for soundness

The withdrawn earlier headline solved `-K_A v = e^x + i`, i.e. plugged in `A_1=1, B_1=1+i` as the right-hand side. Per the verified formulas above, `A_±,B_±` are defined *from* `v_±` — they are outputs of a self-consistency condition, not free parameters one may assign and then solve forward from. Treating them as given inputs and solving is circular: whatever `v` comes out will trivially satisfy the equation with those `A,B` by construction, without that being the equation's actual (self-consistent) solution. This is a correct and precisely-stated diagnosis of the error, and the entry discloses it plainly rather than quietly dropping the earlier claim. I independently checked the second part of the retraction — that the earlier run's justifying citation ("a purported §8 equation `S_a v_± = e^{±x} ± i`") does not appear anywhere in §8 (pages 29–31) of the PDF — and confirmed it: no such equation exists there. The "fictitious citation" characterization is accurate.

## 3. The [N] numerics (§2) — not independently verified, correctly not treated as proof

These scripts are not committed to this repo, so I could not re-run them the way I have for every Bucket 3 finite-section result in Rounds 99–113. I have not treated any of §2's reported figures (nullspace residuals, `r_1`/`r_0` drift, collocation sensitivity, spline-(8.4)-vs-(8.5) inconsistency) as verified in the sense the rest of this audit log uses that word. What I *can* say: the entry itself never asks for that status — it tags the whole section `[N]`, states explicitly "the ledger's [N-cert] pipeline has not touched them," and the qualitative picture it reports (a genuine, `λ`-independent 2D near-nullspace; wild sensitivity to arbitrary linear fixers; smoothing-destroys-the-kink inconsistency between (8.4) and (8.5) discretizations) is exactly what the §1 textual analysis alone would predict, which is a reasonable consistency check even without my being able to rerun it.

## 4. Assessment of the "precise gap statement" (§4) and recommendation (§5)

Given §1's verified catalog, the boxed gap statement is a fair and accurate synthesis: Suzuki's text supplies the defining equation (8.4)/(8.5) itself plus one quadratic scale condition (Theorem 1.5) that is irrelevant to the linear ratios `r_j`, and nothing else in §§6–8 touches `(I_0,I_1)`. This sharpens v13.833's Bucket 2 entry correctly — the prior framing ("use Suzuki's actual domain normalization to determine `I_0/C,I_1/C`," v13.773 §7) could be misread as claiming the text hands you two usable linear equations; §1's exhaustive search shows it doesn't, and §5's recommended rewording is warranted.

## 5. Minor note

§2 describes its numerics as confirming "v13.773 §5 **verbatim**." v13.773 §5 is a structural/algebraic claim (no numerics), so nothing there is literally verified "verbatim" by a numerical run; the sandbox numerics support the same underlying fact by a different (numerical) route. A wording nitpick, not a substantive issue.

## Self-audit note

No error of my own found this round, beyond the initial PDF-tooling friction in this environment (a broken `cryptography`/`cffi` binding blocked `pypdf`/`pdfminer`; fixed with `pip install --force-reinstall cffi` before any extraction was attempted) — noted here only because it's the kind of environment issue a future audit round might hit again.

## Result

\[
\boxed{\textbf{PASS on the verifiable content of v13.838.} \textbf{Every checked [D] textual claim against the primary Suzuki source (arXiv 2606.09096v2) reproduces correctly, with one minor quote-fidelity slip (bar placement in the (8.5)-disclaimer quote) that does not affect the argument. The retraction of the earlier circular "}r_1=-1\textbf{" headline is technically sound and its "fictitious citation" claim is independently confirmed absent from the source. The [N] sandbox numerics are honestly scoped as exploratory and were not independently re-executed by this audit. Bucket 2 is genuinely sharpened: the missing piece is a distributional (kink-faithful) realization of }T_a\textbf{, not a pair of linear conditions the text was merely overlooked as providing.}}
\]
