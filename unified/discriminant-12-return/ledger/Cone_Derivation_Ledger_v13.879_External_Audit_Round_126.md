# Cone Derivation Ledger v13.879 — External Audit Round 126

Date: 2026-09-30

Auditor: External audit thread (Claude, independent instance).

Scope: v13.878 — the D12 Friedrichs-extension lower-bound campaign: a three-part push (the P+H analytic bound, the D12-vs-Riemann positivity-gap decomposition, and the transfer-lemma interval correspondence), including an explicit, prominent self-retraction of overclaims made earlier in the same campaign.

Note on process: this entry was originally numbered `v13.877` by its author before discovering my own simultaneous `v13.877` push (Round 125) and renumbering to `v13.878` — exactly the outcome the standing collision rule calls for, and exactly what I confirmed when the project owner asked me to check twice in the preceding turns. No action needed here beyond noting the protocol worked as designed.

Verdict: **PASS.**

## 1. The self-retraction (§1) — assessed, not just noted

This entry opens by withdrawing four claims made earlier in the same day's campaign: an unsubstantiated value for `A_L`, a "rigorous" `‖K‖_{HS}≤0.26` bound that turns out to rest on floating-point arithmetic and an unproven uniform remainder estimate, the claim that an analytic P+H lower bound was obtained at all, and the derived constants `C^K≥1.777·I`/`A≥0.167·I` that depended on the above. It states plainly that a companion document overclaims and should not be relied on. This is the same self-correcting discipline seen repeatedly across the sandbox arc (the `ψ(1/4)` bug, the `0.955` false plateau, the PAIR-H edge-localization walk-back) — catching your own overclaim before an external check forces it is worth more than getting everything right the first time, and this entry does that cleanly. What survives after the retraction (a lower-boundedness chain, explicitly weaker than a positivity certificate) is the honest residue, and the entry is careful to say so rather than quietly keep the stronger-sounding framing.

## 2. The P+H obstruction (§2) — the Fourier-analytic fact checked independently

The argument that the naive absolute-value majorant `|p_{\rm off}(m,n)|\le\frac{4}{\pi}\frac{W}{|n-m|}` cannot establish boundedness rests on the classical Fourier series `\sum_{k=1}^\infty\frac{\cos k\theta}{k}=-\log(2\sin(\theta/2))` (hence `\sum_{k\ne0}e^{ik\theta}/|k|=-2\log|2\sin(\theta/2)|`), which has a logarithmic singularity at `\theta=0` — the symbol of the Toeplitz matrix with entries `1/|n-m|` is unbounded, so that matrix is not a bounded operator on `\ell^2`. I checked the Fourier identity numerically rather than take it as textbook fact on faith: a partial sum to `N=2\times10^6` terms at `\theta=1.3` gives `-0.19092853...` against the closed form `-\log(2\sin(0.65))=-0.19092842...`, agreeing to the precision expected of a conditionally convergent series at that truncation. The conclusion — that proving `‖P‖` bounded needs genuine oscillatory/singular-integral cancellation, not an absolute-value bound, and that this is correctly left as an open, harder problem rather than pushed through with a wrong tool — is exactly the right diagnosis of why this particular attempt stalls, and the entry reports the stall plainly (`λ_{\min}(P+H)` numerically stabilizing near `-1.50`, status kept at `[N]`, no claim of an analytic bound).

## 3. The interval-correspondence claim (§4) — checked directly against v13.275 §3, not summarized

I pulled v13.275 §3's Transfer Lemma directly rather than accept the "resolved" verdict secondhand. Its three stated assumptions — `H_0^1(-a,a)` a form core compatible with the derivative operator; the energy completion admitting continuous boundary functionals; unique energy-space solvability of `Tv_z=e^{-izx}` for every `z` off the real axis — are exactly the three v13.878 cites. None of the three, as stated, depends on the interval being symmetric about the origin; each is phrased in terms of form-domain/energy-completion properties that translate directly to any bounded interval under the obvious relabeling. The claim that the `(-a,a)` vs. `[0,2]` distinction is a labeling convention rather than a mathematical gap is therefore well-supported by what's actually in the cited lemma, not just asserted.

## 4. The lower-bound chain (§5) — arithmetic checked, components correctly typed by status

The final combination `A\succeq A_{\rm arch}-\|P\|\cdot I\succeq-6.74\cdot I-2.94\cdot I=-9.68\cdot I` is correct arithmetic (`-6.74-2.94=-9.68` exactly) and correct operator-inequality reasoning (a bounded perturbation `P` of a lower-bounded operator `A_{\rm arch}` is lower-bounded by `\inf\sigma(A_{\rm arch})-\|P\|`, standard). I did not re-verify the individual numerical entries (`λ_{\min}` of the low-mode block, the archimedean/cusp bound, the coupling norm) since no script is posted to this repo for this campaign — they remain `[N]`/`[D+N]` as labeled, and the table is honest about which pieces are `[D]` (the prime-norm bound, cited to v13.275 §6 as already established) versus numerically estimated. The conductor-shift arithmetic in §3 (`1.95/2.23≈87\%`) checks out exactly.

## 5. Scope discipline (§7) — correctly calibrated, consistent with this session's whole Bucket 1/2/3 framework

The explicit statement that finite-section/finite-interval lower-boundedness is strictly weaker than infinite-volume positivity, that the latter would be GRH-equivalent via Weil's criterion, and that no circularity is smuggled by proving only the weaker statement, is exactly the distinction this audit thread has maintained since the very first Bucket 1/2/3 triage (v13.833) and the `λ_a>0` strategic note (v13.860): a finite-object spectral-boundedness statement is a different, more tractable kind of claim than the RH/GRH-equivalent global positivity statement, and conflating them would be the error. This entry draws that line correctly and in the right place — finite-`a` self-adjointness and real deficiency-characteristic zeros are established (conditional on the lower bound holding, itself `[D+N]`); the `a\to\infty` convergence and zero-identification are named as the actual remaining wall, untouched.

## Self-audit note

No error of my own found this round.

## Result

\[
\boxed{\textbf{PASS: v13.878 confirmed.} \textbf{Its self-retraction of earlier overclaims is substantively correct and appropriately scoped, not just a disclaimer.} \textbf{The Fourier-analytic obstruction to the P+H bound was checked numerically against the classical series identity it relies on.} \textbf{The interval-correspondence claim was checked directly against v13.275 §3's actual three-assumption statement, which is indeed interval-shape-agnostic.} \textbf{The lower-bound chain's arithmetic is correct, with numerical components appropriately left as [N]/[D+N] rather than upgraded.} \textbf{Scope discipline in §7 — finite lower-boundedness is not infinite positivity, and the latter alone would be GRH-equivalent — matches this session's own Bucket 1/2/3 framework exactly.}}
\]
