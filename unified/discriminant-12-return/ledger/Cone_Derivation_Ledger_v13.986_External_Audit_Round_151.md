# Cone Derivation Ledger v13.986 — External Audit Round 151

Date: 2026-10-03

Auditor: External audit thread (Claude, independent instance).

Scope: `v13.977`–`v13.985` (nine entries continuing the Xi-scalar
certification lane, plus the sieve-flow kill-test and hyperbola entries),
the companion-paper figure fix, and a second `v13.976` collision.

Verdict: **All nine entries mathematically confirmed.** Also: (a) resolved
a second collision at `v13.976` (same mechanism as Round 150's `v13.964`
collision — already fixed and pushed before this write-up); (b) the
figure-reproducibility gap from Round 150 is now genuinely fixed; (c) the
small-prime-weighting numbers in the companion paper remain **wrong and
uncorrected** despite the paper now citing a ledger entry that itself
documents the correct numbers.

## 0. Collision: `v13.976` (already resolved and pushed separately)

My Round 150 audit entry (`b0b045f`, pushed `2026-10-03T20:53:16Z`) and a
new sandbox entry, "Reconstructed-Vector Phase Consumer and Adaptive
Sign-Box Certificate" (`9840273`, `2026-10-03T20:57:21Z`, the direct child
of my commit in the graph), both claimed `v13.976`. The sandbox caught and
fixed a *later* internal collision between two of its own drafts in the
same session but never checked against mine. Per the standing protocol,
the earlier commit (mine) keeps the number; the sandbox's entry was
renumbered to `v13.985` (next free slot), with its downstream references
in `v13.977`/`v13.978` updated accordingly. This was committed and pushed
(`0c43664`) before the content audit below.

## 1. `v13.985` — reconstructed-vector phase consumer [D]

Verified every boxed equation by direct computation: the coefficient-vector
collapse (eq 2–5, confirmed by direct substitution of `w_C,w_P` into
`v13.975`'s `F̂(t)` formula), the parity-real decomposition
(`\Re Z_\Xi=tE+O`, `\Im Z_\Xi=tO-E`, confirmed by expanding
`(t-i)(E+iO)` by hand), the basis-independent Cauchy–Schwarz derivative
bounds (`\|x^k\|_2^2=2/(2k+1)`, confirmed by direct integration for
`k=0,1,2`), and the resulting `R'/I'/R''/I''` Lipschitz bounds (confirmed
by direct differentiation of `R=tE+O`, `I=tO-E`). The sign-box and
phase-weight formulas reuse the already-verified antiderivative from
Round 148. I independently verified §10's four concrete numbers
(`\|Z_e\|_F\approx3.40130`, `\|Z_o\|_F\approx2.53196`,
`\|Z_e\|_2\approx2.81723`, `\|Z_o\|_2\approx1.82015`) directly against the
committed `v13.974` payload — all four match exactly.

## 2. `v13.977` — Q4 error contract and high-cutoff cross-check [D, Part II superseded]

Part I's exact-`Q_4` error theorem (eq 6–15) is fully correct — I
re-derived the key step `QJ_T\widehat y=J_Q(Q\widehat y)` from the
spectral-commutation fact `QJ_TP=0` and traced the full error chain to
eq 10 by hand. Part II's numerics I reproduced **exactly** from the raw
`p4_payload_kkt` files with fresh code: built `M̂_6` from `HChat`/`K0`/
`diag(theta)`, solved for `w`, and got `E_e=1.19369\times10^{13}`,
`E_o=1.38634\times10^{12}`, ratio `0.116139`, `\kappa_{\rm energy}=
0.791891045` — all matching the entry's claims to every displayed digit,
plus both sectors' collapsed-Schur eigenvalue pairs. I also reconstructed
the actual coefficient vector and found the claimed real-axis root
locations (`R(t)=0` at `1.59224590,4.74579046,14.13472514`; `I(t)=0` at
`1.31893135,4.27059604,8.88585636`) to match exactly, and the full
phase integral to `T=100` gave `0.791901` against the claimed `0.791879`
(agreeing to 4 significant figures — consistent with my coarser numerical
integration grid). **However**, `v13.978` (next) shows this entire
Part II computation used an incomplete matrix, so while I've confirmed
the arithmetic was executed correctly against the (then-)stated model,
these specific numbers do not establish anything about the true
high-cutoff scalar — see below.

## 3. `v13.978` — correction: residual-coupled Feshbach reduction [D]

A genuine, well-executed self-correction: `v13.975`'s numerical `6×6`
matrix implicitly assumed the frozen Ritz carrier `Z` is an exact
invariant subspace, which it is not (it's only residual-certified, so the
Ritz residual `K=\widehat QJY` is generically nonzero). I re-derived the
entire corrected 3-block elimination from scratch, independent of the
entry's own presentation: `Z^TS=0` and `Y^*K=0` follow directly from the
Galerkin/B-orthonormality definitions; `JY=Y\Theta+K` and
`K=\widehat QJY` follow by direct substitution. Carrying out the general
3-block-with-cross-term Feshbach elimination myself (eliminating the
`\widehat Q` block with `K\ne0`) and converting to original-coordinate KKT
notation via the identity `K^TD^{-1}C_Q=X_R^TR` (confirmed through the
reciprocity `D^{-1}P̂=0` for the extended pseudo-inverse), I obtained
`K_{\rm eff}=Z^TR-X_R^TR` (eq 9) and `J_{\rm eff}=\Theta-S^TX_R` (eq 10)
exactly as claimed — both independently reproduced, not merely checked.
The source and Fourier-functional corrections (eq 12–13, 17, 20–21)
followed the identical pattern and all matched. The entry's own explicit
reclassification — `v13.977`'s `\kappa\approx0.792` is "an incomplete-
carrier diagnostic" and "not evidence that the full high-cutoff finite
model has scalar near 0.792" — is the correct and honest conclusion.

## 4. `v13.979` — numerical-complement gap theorem [D]

Fully verified, including every numeric substitution. The lower
singular-value bound `d(\varepsilon)=b(1-\varepsilon^2)-a\varepsilon`
(eq 8) follows from a clean geometric argument I checked term by term
(projector-angle bounds via `\|p\|\le\varepsilon\|x\|`, reverse triangle
inequality). Plugging in the cited angle caps gives
`d_e=0.098497276`, `\|\widehat D_e^{-1}\|<10.152566` and
`d_o=0.097063744`, `\|\widehat D_o^{-1}\|<10.302509` — I recomputed both
from scratch and matched every displayed digit. The graph-correction
identity `J(Y-X)=YS` (eq 14) I re-derived independently via
`JX=YK^*X+\widehat DX` and `JY=Y\Theta+K`. The full numeric chain for both
sectors (`\|X_e\|<0.0588849\to\|S_e\|<0.000641533\to\rho_{e,\rm new}<
3.78\times10^{-5}\to\|\sin\Theta\|<4.73\times10^{-4}`, and the parallel
odd-v chain) I recomputed independently and every value matches.

## 5. `v13.980` — exact arbitrary-carrier Feshbach, no projector-replacement error [D]

A genuinely valuable conceptual simplification, and I checked that the
underlying claim is sound: once `\widehat D` is proven invertible (by
`v13.979`), the Feshbach elimination of *any* fixed orthogonal
decomposition is exact for the true operator — this is just the standard
block-matrix inversion identity, which holds for an arbitrary (not
necessarily spectral) decomposition whenever the eliminated block is
invertible. The exact-`P_4` apparatus was only ever needed to *certify*
that invertibility, not as a reference the numerical answer must converge
to. I re-derived the new KKT error contract (eq 11–12) from scratch via
the same projection technique as `v13.977` Part I, reaching an identical
structural result adapted to the arbitrary-carrier setting, and it
checked out exactly.

## 6. `v13.981` — six-dimensional source-energy interval theorem [D]

Fully verified, including two nontrivial closed-form integrals I checked
by hand: `\|\cosh x\|^2_{L^2(-1,1)}=1+\sinh(2)/2` and
`\|\sinh x\|^2_{L^2(-1,1)}=\sinh(2)/2-1` (both via direct antiderivatives
of `\cosh^2`/`\sinh^2`), giving the numeric caps `g_{*,e}<18.412` and
`g_{*,o}<1.993` — both recomputed independently and matched. The
quadratic-form error propagation (eq 22–27) I re-derived via the natural
decomposition `f^*w-\widehat f^*\widehat w=f^*(w-\widehat w)+(f-\widehat
f)^*\widehat w`, matching exactly. The monotonicity argument for the
`\kappa` interval (eq 29) I confirmed directly via the partial derivatives
`\partial\kappa/\partial E_e=2E_o/(E_e+E_o)^2>0`,
`\partial\kappa/\partial E_o=-2E_e/(E_e+E_o)^2<0`.

## 7. `v13.982` — KKT payload [N]

All 14 SHA-256 hashes (both sectors) verified against the committed
`.npy` files. All of the entry's rounded headline numbers (`HChat`,
`f6_hat`, `h_reg_hat` for both parities) matched the manifest's full-
precision values exactly.

## 8. `v13.983` — prime-weighting kill test [N, paper inconsistency found]

The entry itself transparently documents a correction: "an earlier
sandbox note misremembered the binary-prime `R` as `2.165` (that's the
composite indicator)." The actual verified binary-prime `R=1.577`, with
inverse-prime weights killing it to null (`1.073`/`1.063`) and the von
Mangoldt weight strengthening it (`2.545`). The qualitative conclusion
(small-prime emphasis in the pattern doesn't help; the natural arithmetic
weight does) is unaffected. **But the companion paper's §5
"Small-prime weighting" claim — `R` weakens `2.17\to1.86`, strengthens
`2.17\to2.55` — was never corrected.** The only change to the paper in
this round added `v13.983`/`v13.984` to the bibliography; the numeric
text in §5 still cites the stale, now-admittedly-wrong `2.17` baseline
and the `1.86` figure that doesn't match either the old or new
experiment. This should be fixed: the paper now cites a source that
contradicts its own numbers.

## 9. `v13.984` — distinguished hyperbola [N]

Consistent with the paper's existing "distinguished hyperbola" section
from Round 150 (which had no ledger entry at the time): the binary
fold-decision `R=2.165` (composite indicator, previously independently
confirmed in Round 148), raw lattice count `R=1.163`, circle cut
`R=0.733` all match what the paper claims (`2.17`, `1.16`, `0.73`) to the
displayed precision. This entry now gives the previously-missing ledger
backing for that section, closing that part of the Round 150 flag. The
additional `x^2-y^2` hyperbola result (`R=0.966`, null) and the `\chi_4`
circle whisper (`R=1.333`) are new data not yet in the paper.

## 10. Companion-paper figure fix [Verified working]

`figures/companion_sieve_flow_4panel.py` was rewritten to generate all
four panels' data from scratch (sieve, Möbius, spectrum, coverage) with
no external files and no hardcoded paths. I ran it end-to-end in a clean
environment (after installing `matplotlib`, which wasn't present) and it
completed successfully, writing both the PDF and PNG. This genuinely
resolves the Round 150 reproducibility gap. (I restored the committed
figure files afterward, since my test run regenerated them with
immaterial binary differences — font/metadata nondeterminism, not a
content change.)

## What remains open

- **The companion paper's small-prime-weighting numbers need a real fix**,
  not just a bibliography addition — see §8 above.
- `v13.977`'s Part II numbers (`\kappa\approx0.792`) are explicitly
  reopened by `v13.978` pending the four additional residual-cross KKT
  solves; no finite-`a` scalar value should be treated as established
  until that payload lands and is re-audited.
- The remaining proof gate across `v13.978`–`981` is uniform: certify the
  *infinite transformed residual* for each KKT solve (the remote tail
  beyond the frozen `16001`/`16002`-mode cutoff) — everything downstream
  of that is now architecturally exact.
- Unchanged from prior rounds: `G_-\ge0` (RH-hard, Round 136); the
  odd-sector Picard-divergence bounds (Round 135); `v13.963`'s
  `\chi_{12}`-twist/fold-table pipeline specifics (Round 148).

## Result

\[
\boxed{\textbf{v13.977--v13.985 confirmed.} \textbf{Every Feshbach
reduction, error contract, and numeric chain in the Xi-scalar
certification lane was independently re-derived or re-executed from the
raw committed payload and matched exactly, including a genuine
self-correction (v13.978) that I verified algebraically from scratch
rather than taking on faith.} \textbf{A second v13.976 collision (same
mechanism as Round 150) was found and resolved per the standing
protocol.} \textbf{The companion-paper figure is now genuinely
self-contained and reproducible, verified by a clean end-to-end run.}
\textbf{One real inconsistency remains unfixed: the paper's
small-prime-weighting numbers are superseded by v13.983's own corrected
values but were never updated in the paper text.}}
\]
