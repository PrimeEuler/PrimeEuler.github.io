# Cone Derivation Ledger v13.296 — Coefficient-Tail Decay and H1 Tail-Control Audit

**Status:** NUMERICAL TAIL-DECAY AUDIT — OBSERVED FINITE H1 TAIL SMALL AND RAPIDLY DECREASING, BUT NO RIGOROUS INFINITE-TAIL BOUND — `ker(G_1) != {0}`, `lambda_1=0`, RH, AND GRH NOT PROVED.

## 1. Purpose

v13.295 extended the parity-reduced even-`v` Ritz sequence to `M=20` and found renewed decay of the nested `H^1` differences.  v13.296 asks whether the stabilized odd-mode coefficients themselves show enough tail decay to make an `H^1` limit plausible.

At `a=1`, even `v` uses odd Dirichlet modes

\[
\psi_n(x)=\sin\!\left(\frac{n\pi(x+1)}2\right),\qquad n=1,3,5,\ldots,
\]

and

\[
\|Dv\|_2^2=\sum_{n\ \mathrm{odd}}\left(\frac{n\pi}{2}\right)^2|c_n|^2.
\]

Thus a useful numerical compactness diagnostic is the cumulative weighted tail

\[
T_{H^1}(N)=\left[\sum_{n\ge N}\left(\frac{n\pi}{2}\right)^2|c_n|^2\right]^{1/2}.
\]

This is only the tail contained in the finite Ritz vector; it is not an a priori bound on coefficients beyond the truncation.

## 2. M=20 coefficient profile

The high-precision parity-reduced `M=20` candidate has lowest Ritz value

\[
\lambda_{20}^{\mathrm{Ritz}}\approx1.1238941579916523\times10^{-20},
\]

with odd-index Dirichlet coefficients approximately

| n | c_n | |c_n| |
|---:|---:|---:|
| 1 | +8.26511259235e-1 | 8.26511259235e-1 |
| 3 | -5.24960899651e-1 | 5.24960899651e-1 |
| 5 | +1.99786910855e-1 | 1.99786910855e-1 |
| 7 | -3.71423701896e-2 | 3.71423701896e-2 |
| 9 | -6.45471029575e-6 | 6.45471029575e-6 |
| 11 | +9.08711168419e-4 | 9.08711168419e-4 |
| 13 | -3.08000405158e-5 | 3.08000405158e-5 |
| 15 | -6.00392833896e-6 | 6.00392833896e-6 |
| 17 | -8.23824816334e-7 | 8.23824816334e-7 |
| 19 | +1.68758873839e-8 | 1.68758873839e-8 |

The profile is not monotone globally.  There is a pronounced near-zero notch at `n=9`, followed by a secondary `n=11` shoulder.  Therefore a single global power-law fit would be misleading.

## 3. Observed cumulative finite-vector tails

For the `M=20` vector, the observed cumulative tails are:

| cutoff N | observed L2 tail | observed H1 tail |
|---:|---:|---:|
| 9 | 9.09276096418e-4 | 1.57149106724e-2 |
| 11 | 9.09253185990e-4 | 1.57146457369e-2 |
| 13 | 3.13905817627e-5 | 6.45036060391e-4 |
| 15 | 6.06020854616e-6 | 1.43165426373e-4 |
| 17 | 8.23997647802e-7 | 2.20048017936e-5 |

The `n=11` shoulder dominates the finite observed tail.  Once that mode is passed, the weighted derivative tail collapses quickly: the finite contribution from `n>=13` is about `6.45e-4`, and from `n>=17` about `2.20e-5`.

This is consistent with the bounded derivative norms and shrinking nested `H^1` differences in v13.295.

## 4. Descriptive tail-law fits

Using only the observed points `n=11,13,15,17,19`, a log-linear fit

\[
\log |c_n|\approx \alpha+\beta n
\]

gives

\[
\beta\approx-1.27046,
\]

corresponding to an average amplitude ratio of about

\[
e^{2\beta}\approx0.0788
\]

for an increment of two in the odd mode number, with log-scale

\[
R^2\approx0.978.
\]

A log-log power fit over the same five points gives an apparent exponent around `p≈18.5` with log-scale `R^2≈0.966`.

These fits are **descriptive only**.  Five finite-section points cannot establish either exponential or algebraic decay of the infinite coefficient sequence.  The power exponent in particular should not be interpreted literally because the fit window is short and includes the anomalously large `n=11` shoulder.

## 5. Interpretation

The useful conclusion is not “the tail is exponential.”  It is narrower:

1. The candidate remains overwhelmingly low-frequency.
2. There is no evidence of a growing high-mode derivative tail through `M=20`.
3. The directly observed weighted tail beyond `n=13` is already small compared with the total derivative norm `||Dv_{20}||_2≈3.23`.
4. The finite observed tail is consistent with the strong-`H^1` stabilization trend seen in v13.295.

Numerically this makes a genuine `H_0^1` limiting candidate increasingly plausible.

## 6. What remains open

The central gap is now very specific.  To turn the numerical picture into an actual limiting argument one would need a bound valid beyond the finite truncation, for example a demonstrable inequality of the form

\[
|c_n|\le C n^{-p},\qquad p>3/2,
\]

or any stronger summable envelope sufficient to imply

\[
\sum_n n^2|c_n|^2<\infty.
\]

Even better would be an operator-level estimate deriving coefficient decay from regularity of a limiting solution of

\[
P_1G_1u=0,
\]

rather than extrapolating from finite Ritz vectors.

No such rigorous infinite-tail estimate has been established here.

## 7. Proof-status guardrail

v13.296 does **not** prove:

- strong `H^1` convergence of the Ritz sequence,
- existence of a nonzero element of `ker(G_1)`,
- `lambda_1=0`,
- admissibility of the earlier `lambda=-5` Fredholm choice,
- RH or GRH.

The correct status is:

\[
\boxed{\text{observed finite }H^1\text{ tail is very small and rapidly decaying; infinite-tail control remains open.}}
\]

## 8. New reproducibility file

`research-notes/suzuki_tail_decay_audit.py`

The script rebuilds the parity-reduced `M=20` candidate, reports the coefficient sequence, cumulative observed `L^2/H^1` tails, and descriptive exponential/power fits with explicit non-proof warnings.

## 9. Next audit target

The next productive step is not simply another fit.  v13.297 should probe the **operator regularity mechanism** behind the coefficient decay: project `P_1G_1u=0` onto high odd modes and study the asymptotics of the matrix row acting on the stabilized low-mode candidate.  If the high-mode equation itself forces rapid coefficient decay, that could provide a route toward an analytic tail estimate rather than a finite-section extrapolation.
