# Cone Derivation Ledger v13.451 — Odd Normalized Closure and Index ≤ 2 Theorem

Date: 2026-09-14

Status labels: **[D]** exact derived; **[N-cert]** outward-certified numerical inequality; **[Audit]** guardrail.

## 0. Synchronization [Audit]

A live-head check immediately before this write found `v13.450` as the newest numbered ledger entry. The normalized-C and normalized-H research-note verifiers had already landed as unnumbered commits, so `v13.451` was free at write time.

This checkpoint closes the final theorem-level obligations identified in v13.449 and External Audit Round 32.

The previously closed odd-sector inputs are

\[
A_{FF}\succeq0.53I,
\qquad
\|A_{FT}\|<1.015,
\qquad
\delta_{\rm odd}>0.637.
\]

The first two odd Schur directions remain unresolved throughout this checkpoint.

## 1. Frozen eight-dimensional finite normalization [N-cert]

The artifact

`research-notes/suzuki_odd_M4000_normalized_C_outward_verifier.py`

uses the immutable exact-dyadic `Q8,L0` payload together with the high-precision point nominal

`research-notes/suzuki_odd_M4000_frozen8_highprecision_nominal.py`.

Instead of reproducing the historical normalized midpoint to its final digits, it proves the relaxed point-nominal inequality

\[
Q_8^TS_{F,\rm nom}Q_8\succeq0.998\,L_0L_0^T.
\]

The shifted raw `8x8` matrix is certified positive by a posteriori Cholesky plus verified-inverse bounds.

The exact-dyadic Gershgorin floor is

\[
\lambda_{\min}(L_0L_0^T)>1.6689\times10^{-10}.
\]

Using the audited source envelope

\[
\varepsilon_A=2\times10^{-13},
\]

the certified finite-high floor

\[
\mu=0.53,
\]

the conservative coupling bound

\[
\|A_{CF}\|<5.15,
\]

and the outward finite-solve residual target `1e-12`, the total normalized loss is less than `0.196`.

Hence

\[
\boxed{C_{\rm odd}>0.802I>0.80I.}
\]

This removes the historical transcript-only `C_odd >= 0.80 I` input.

## 2. Exact-vs-point residual-map perturbation [N-cert]

The artifact

`research-notes/suzuki_odd_M4000_normalized_residual_error_bound.py`

starts from

\[
R=A_{TC}-A_{TF}A_{FF}^{-1}A_{FC},
\qquad
Y=RQ_8L_0^{-T}.
\]

It uses the already-certified inputs

\[
\|\Delta A\|\le2\times10^{-13},
\qquad
A_{FF}\succeq0.53I,
\qquad
\|A_{TF}\|<1.015,
\qquad
\|A_{FC}\|<5.15,
\]

and the exact-dyadic inverse of `L0`.

Exact Fraction arithmetic gives the conservative proxy

\[
\|L_0^{-1}\|_2\le\|L_0^{-1}\|_F<77409.
\]

Resolvent propagation, finite-solve residual propagation, and a separate formation allowance then give

\[
\boxed{\|\Delta Y\|<7\times10^{-7}.}
\]

Thus the historical residual-map perturbation scale is no longer an unexplained transcript constant.

## 3. Relaxed nominal residual-Gram certificate [N-cert]

The new artifact

`research-notes/suzuki_odd_M4000_normalized_H_relaxed_outward_verifier.py`

uses a deliberately relaxed proof architecture.

There is no need to reproduce the historical far-tail target `0.000482`. Once

\[
\|\Delta Y\|<7\times10^{-7}
\]

is available, the final theorem only requires the nominal point Gram to stay sufficiently below `0.225`.

### 3.1 Explicit normalized residual Gram through `2M`

The point replay gives

\[
\lambda_{\max}(H_{\le2M,\rm point})
=0.2244148487009\ldots .
\]

The verifier uses the rounded target

\[
\boxed{H_{\le2M,\rm point}<0.22442I.}
\]

The shifted `8x8` Gram

\[
0.22442I-H_{\le2M,\rm point}
\]

has an a-posteriori Cholesky factor-floor proxy above

\[
5.15\times10^{-6},
\]

while the deliberately loose Gram-formation allowance is only

\[
10^{-8}.
\]

The eight-level inverse-power truncation used on `16002..2,000,000` has residual-map norm below

\[
1.1\times10^{-13},
\]

under a cancellation-free row-norm majorant.

### 3.2 Relaxed far tail beyond `2M`

For even `n>=2,000,002`, write

\[
r_n=\frac{L}{n}+e_n,
\]

with

\[
\|e_n\|\le\frac{B}{n^2}+\frac{C}{n^3}.
\]

The point frozen coefficients satisfy the outward-rounded inequalities

\[
\|L\|<43.847,
\qquad
B<8.898\times10^6,
\qquad
C<5.022\times10^7.
\]

Using

\[
\sum_{n\ge N,\ n\ {m even}} n^{-p}
\le
N^{-p}+\frac12\frac{N^{1-p}}{p-1},
\]

with `N=2,000,002`, the verifier obtains

\[
\boxed{
H_{>2M,\rm point}<5.39\times10^{-4}<5.5\times10^{-4}.
}
\]

This is intentionally weaker than the historical `4.82e-4` target but is fully sufficient.

### 3.3 Final normalized residual-Gram bound

Therefore the rounded point-nominal Gram obeys

\[
\|H_{\rm point}\|
<0.22442+0.00055
=0.22497.
\]

For

\[
Y_{\rm exact}=Y_{\rm point}+\Delta Y,
\]

we have

\[
\|Y_{\rm exact}\|^2
\le
\left(\sqrt{0.22497}+7\times10^{-7}\right)^2
<0.224971.
\]

Hence

\[
\boxed{H_{\rm odd}<0.224971I<0.225I.}
\]

This removes the historical transcript-only `H_odd < 0.225 I` input.

## 4. Positive frozen eight-dimensional subspace [N-cert]

The infinite-tail Schur lower bound is already certified as

\[
\delta_{\rm odd}>0.637.
\]

Together with

\[
C_{\rm odd}>0.80I,
\qquad
H_{\rm odd}<0.225I,
\]

we get the rounded comparison

\[
\delta_{\rm odd}C_{\rm odd}-H_{\rm odd}
>
0.637\cdot0.80-0.225
=0.2846.
\]

Using the sharper certified `delta_odd` value from the cross closure gives a margin above `0.2847`, but the coarse rounded inequality already suffices.

Therefore the exact frozen eight-dimensional candidate-positive subspace remains strictly positive after infinite-tail elimination.

## 5. Odd-sector inertia theorem [D/N-cert]

The low block has dimension ten. An exact rank-eight frozen subspace has now been certified positive for the full odd-sector operator after finite-high and infinite-tail Schur elimination.

By min-max / Schur inertia,

\[
\boxed{
\operatorname{ind}_{\le0}(A_{\rm odd}(1))\le2.
}
\]

This is now restored as a theorem-level odd-sector statement.

## 6. What is not proved [Audit]

- The remaining two odd directions are **not** proved to be exact kernels.
- No claim is made that either unresolved direction has eigenvalue exactly zero.
- No RH, GRH, or zeta-zero theorem is inferred.
- This checkpoint does not by itself change the independently audited even-sector index bound.
- Any full-parity index statement must combine this theorem only with whatever even-sector theorem is currently certified in the live ledger.

## 7. Provenance summary

Closed ingredients now are:

1. exact rank `Q8=8` and exact invertibility of `L0`;
2. `A_FF >= 0.53 I` — v13.434;
3. `||A_FT|| < 1.015` and `delta_odd > 0.637` — v13.443;
4. exact-dyadic normalized denominator and finite-Schur perturbation provenance — v13.449;
5. `C_odd > 0.802 I` — normalized-C outward verifier;
6. `||Delta Y|| < 7e-7` — normalized residual-map perturbation verifier;
7. `H_odd < 0.224971 I < 0.225 I` — relaxed normalized-H outward verifier.

---

**Checkpoint conclusion.** The final normalized frozen-eight-dimensional obligations are closed. The odd-sector theorem

\[
\boxed{\operatorname{ind}_{\le0}(A_{\rm odd}(1))\le2}
\]

is restored, with the first two odd directions explicitly unresolved and with no exact-zero, RH, or GRH claim.