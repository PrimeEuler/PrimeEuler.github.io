# Cone Derivation Ledger v13.404 — Odd-Sector Nonpositive Index At Most Two

Date: 2026-09-12

Status labels: **[D]** exact derived, **[N]** numerical, **[N-cert]** validated computational, **[O]** open.

## 1. Purpose

Close the independent odd-v parity sector at `a=1` to a finite-index theorem, using the same source-faithful post-IBP matrix as the even-sector proof but with the parity-specific sinh pole channel.

Odd functions about `x=0` correspond to even Dirichlet mode number.  Use

\[
C_{\rm odd}=\{2,4,\ldots,20\},
\qquad
F=\{22,24,\ldots,4000\},
\qquad
T=\{4002,4004,\ldots\}.
\]

The exact frozen eight-dimensional low-core subspace is the dyadic matrix `Q8` stored in

`research-notes/suzuki_odd_M4000_frozen_dyadic_Q8_L0.py`.

After an initial stale-row scratch commit, that file was corrected from the actual `M=4000` midpoint eigenspace before this theorem was promoted.  Its exact-Fraction minor check proves

\[
\boxed{\operatorname{rank}Q_8=8}
\]

and the frozen lower-triangular `L0` is exactly invertible.

## 2. Finite high block

**[N-cert]** The source-faithful midpoint finite block has

\[
\lambda_{\min}(A_{FF})\approx0.53374499902694.
\]

For the shifted matrix

\[
B_F=A_{FF}-0.53I,
\]

a direct Cholesky replay gives

\[
\|B_F-LL^T\|_F\approx4.11\times10^{-14},
\]

and

\[
\|L^{-1}\|_2\approx16.3409.
\]

Hence the positive factor floor is approximately

\[
\|L^{-1}\|_2^{-2}\approx3.745\times10^{-3},
\]

vastly larger than the exact-vs-nominal source uncertainty and arithmetic replay charges.  Retain the rounded certified statement

\[
\boxed{A_{FF}\succeq0.53I}.
\]

## 3. Conservative raw remote-tail floor

To avoid depending on the sharper cusp-tail localization, use the global cusp remainder bound `0.706` together with

\[
\|H_{\rm odd}\|\le\pi/2,
\qquad
\|B_{\rm prime}\|<2.05,
\]

and the surviving analytic arch tail bound

\[
\beta_{\rm arch}(4002)<4.077\times10^{-4}.
\]

Ignoring the positive pole term,

\[
\alpha_{4002}
=
\log(4002/4)-\frac\pi2-2.05-0.706-\beta_{\rm arch}(4002)
>
\boxed{2.58105}.
\]

This is intentionally much weaker than the available localized cusp estimate, but it is sufficient.

## 4. Finite-high / remote-tail coupling

The adjacent cross block `4002..16000` was decomposed into an explicit rank-12 approximation plus a directly measured Frobenius residual.  The explicit rank-12 + remote-low-rank part has norm

\[
0.9772519211743,
\]

while the near-block residual obeys

\[
\|E_{\rm near}\|_F<0.002308.
\]

The exact rank-two inverse-power expansion handles `16002..2,000,000`.  Beyond two million, the exact leading `1/n` channel contributes at most about

\[
0.035112
\]

in operator norm; the `Z_n/n^2` channel with `|Z_n|<8`, the denominator geometric remainder, and the pole correction raise the analytic tail envelope only to

\[
<0.03519.
\]

After outward arithmetic/source padding retain the simple fail-closed bound

\[
\boxed{\|A_{FT}\|<1.015}.
\]

## 5. Effective tail Schur floor

Using the finite-high floor and the cross bound,

\[
A_{TT}-A_{TF}A_{FF}^{-1}A_{FT}
\succeq
\left(
\alpha_{4002}-\frac{1.015^2}{0.53}
\right)I.
\]

Thus

\[
\boxed{\delta_{\rm odd}>0.6372304048}. 
\]

For a rounded theorem input one may use

\[
\boxed{\delta_{\rm odd}>0.637}.
\]

## 6. Frozen eight-dimensional finite matrix

The `M=4000` odd Schur spectrum begins numerically

\[
(\sim10^{-15},\sim10^{-15},1.66895\times10^{-10},3.34239\times10^{-6},8.22118\times10^{-3},0.6514,\ldots).
\]

The frozen `Q8` spans directions `3..10`; no statement is made about the first two.

The global component bounds give the fully analytic coupling estimate

\[
\|A_{CF}\|<5.15.
\]

With

\[
\varepsilon_A<2\times10^{-13},
\qquad
A_{FF}\succeq0.53I,
\]

the exact-vs-nominal finite Schur perturbation is below

\[
2.30\times10^{-11}.
\]

The ordinary point solve has residual at the `10^{-16}` scale; the verifier only requires and charges the much looser outward target

\[
\|R_F\|<10^{-12},
\]

which contributes less than

\[
9.72\times10^{-12}
\]

to the Schur matrix.

After the exact frozen `L0` normalization and a generous midpoint-coordinate padding, the raw normalized lower bound remains above `0.804`.  Retain

\[
\boxed{C_{\rm odd}\succeq0.80I}.
\]

## 7. Eight-direction residual Gram

The normalized residual Gram on the frozen eight-dimensional subspace was accumulated explicitly through mode two million.  Its midpoint maximum is

\[
\boxed{h_{\le2\times10^6}=0.2244147915340}.
\]

For the remaining infinite tail, the exact leading residual channel contributes

\[
<4.8063\times10^{-4}
\]

to the Gram.  The `Z_n/n^2`, higher denominator powers, and pole corrections raise the analytic tail charge only slightly; retain

\[
\boxed{\Delta H_{>2\times10^6}<4.82\times10^{-4}}.
\]

A conservative exact-vs-point normalized residual-operator enclosure

\[
\|\Delta Y\|<7\times10^{-7}
\]

covers source-operator uncertainty, finite solve uncertainty, scalar reconstruction and arithmetic.  Consequently

\[
\boxed{H_{\rm odd}\prec0.225I}.
\]

## 8. Terminal inequality

Combine

\[
C_{\rm odd}\succeq0.80I,
\qquad
H_{\rm odd}\prec0.225I,
\qquad
\delta_{\rm odd}>0.6372304048.
\]

Then

\[
\delta_{\rm odd}\lambda_{\min}(C_{\rm odd})
>
0.6372304048\times0.80
=
0.5097843238,
\]

so

\[
\boxed{H_{\rm odd}<\delta_{\rm odd}C_{\rm odd}}
\]

with normalized margin exceeding

\[
\boxed{0.2847}.
\]

Therefore the exact infinite odd-sector Schur complement is positive on the exact eight-dimensional subspace `ran(Q8)`.

## 9. Odd-sector index theorem

Since the low core has dimension ten and contains an exact eight-dimensional positive subspace,

\[
\operatorname{ind}_{\le0}(S_{10}^{\rm odd})\le2.
\]

The high complement is strictly positive, so exact Schur-congruence inertia gives

\[
\boxed{
\operatorname{ind}_{\le0}(A_{\rm odd}(a=1))\le2.
}
\]

Equivalently, counting multiplicity in the odd-v sector,

\[
\boxed{\lambda^{\rm odd}_3(a=1)>0.}
\]

## 10. Combined parity picture

Together with v13.402,

\[
\operatorname{ind}_{\le0}(A_{\rm even})\le4,
\qquad
\operatorname{ind}_{\le0}(A_{\rm odd})\le2.
\]

Thus for the full parity decomposition at `a=1`,

\[
\boxed{\operatorname{ind}_{\le0}(A_{a=1})\le6}
\]

provided the even and odd parity sectors are combined in the standard orthogonal decomposition.

This does **not** say that six nonpositive directions exist; it is only an upper bound.

## 11. Guardrails

- The first two odd-sector tiny directions remain unresolved and are not called exact kernels.
- The first four even-sector directions from v13.402 remain unresolved.
- The full index bound `<=6` is an upper bound, not an equality.
- No exact zero, RH, GRH, or `lambda_1=0` conclusion follows.
- The numerical/computational parts are certified under the same explicit floating-point/outward-error model used in the v13.401 terminal replay; this is not a machine-checked formal proof.
