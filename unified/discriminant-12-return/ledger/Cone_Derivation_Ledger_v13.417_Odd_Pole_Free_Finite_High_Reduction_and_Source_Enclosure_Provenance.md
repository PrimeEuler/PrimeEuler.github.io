# Cone Derivation Ledger v13.417 — Odd Pole-Free Finite-High Reduction and Source-Enclosure Provenance

Date: 2026-09-14

Status labels: **[D]** exact derived, **[N]** numerical midpoint diagnostic, **[N-cert]** outward/certified numerical statement, **[Audit]** limitation/guardrail.

## 0. Synchronization

This checkpoint follows the concurrent v13.415 Suzuki mod-12 source-channel audit and v13.416 F4/character-splitting entry.  Those entries remain structurally relevant but do not replace the direct Suzuki positivity estimates.

The current odd-sector target remains the finite-high block

\[
F=\{22,24,\ldots,4000\}.
\]

The full source-faithful odd finite-high matrix has the form

\[
A_{FF}=A_{FF}^{(0)}+2dd^T,
\]

where

\[
d_n=\frac{2k_n\sinh(1/2)}{k_n^2+1/4},
\qquad k_n=\frac{n\pi}{2}.
\]

## 1. Positive-pole reduction [D]

Because

\[
2dd^T\succeq0,
\]

we have the exact Loewner inequality

\[
A_{FF}\succeq A_{FF}^{(0)}.
\]

Therefore it is sufficient to prove

\[
\boxed{A_{FF}^{(0)}\succeq0.53I.}
\]

No outward enclosure of the odd sinh-pole channel is required for this particular finite-high lower bound.

This removes one proof-critical source from the finite-high certificate.

## 2. Independent pole-free midpoint replay [N]

A new replay artifact was added:

`research-notes/suzuki_odd_M4000_pole_free_finite_high_replay.py`.

It uses the same independently reconstructed source-faithful scalar formulas as v13.407 but records the pole-free and full matrices separately.

For the pole-free block,

\[
\boxed{
\lambda_{\min}(A_{FF}^{(0)})
\approx0.5328423837861.
}
\]

For comparison, including the positive rank-one pole gives

\[
\lambda_{\min}(A_{FF})
\approx0.5337449990275.
\]

Thus the pole raises the bottom eigenvalue by roughly

\[
9.03\times10^{-4},
\]

but is not needed to remain above the working floor 0.53.

The shifted pole-free matrix

\[
B_0=A_{FF}^{(0)}-0.53I
\]

has midpoint minimum

\[
\boxed{
\lambda_{\min}(B_0)
\approx0.0028423837861.
}
\]

A binary64 Cholesky replay gives approximately

\[
\|B_0-LL^T\|_F\approx3.89\times10^{-14},
\]

\[
\|B_0-LL^T\|_2\approx2.70\times10^{-15},
\]

and

\[
\frac1{\sqrt{\lambda_{\min}(B_0)}}
\approx18.75679541.
\]

These are midpoint/regression diagnostics only.

## 3. Provenance of the dimension-free source enclosure [D/Audit]

The previously used even-sector exact-vs-nominal budget

\[
\varepsilon_A=2\times10^{-13}
\]

was traced to ledger v13.357 rather than merely accepted from the later final replay.

The key analytic input is the degree-64 polynomial approximation to the archimedean kernel scalar function \(h\), with uniform certified remainder

\[
\boxed{
\|h-h_{32}\|_\infty<6.1\times10^{-14}
\quad\text{on }[0,2].
}
\]

Schur's test on the induced integral kernel gives the dimension-free operator estimate

\[
\boxed{
\|\Delta K_{\rm arch}\|_2
\le 2(6.1\times10^{-14})
=1.22\times10^{-13}.
}
\]

This is an operator statement before compression.  Hence it applies to every orthogonal finite Fourier compression, including the present even-index odd-sector block \(F=\{22,24,\dots,4000\}\).

The polynomial tail certificate itself is present in

`research-notes/suzuki_arch_polynomial_certificate.py`.

It derives the \(6.1\times10^{-14}\) remainder from explicit Euler/Bernoulli tail estimates.

## 4. Parity caveat for the archived recurrence [Audit]

The helper

`research-notes/suzuki_arch_polynomial_recurrence.py`

was written explicitly for odd Fourier mode numbers and uses

\[
\cos(n\pi)=-1.
\]

The current odd Suzuki finite-high block uses even mode numbers, for which

\[
\cos(n\pi)=+1.
\]

Therefore that recurrence implementation cannot be copied verbatim into the odd-sector outward generator.

This does **not** invalidate the uniform-kernel/Schur source enclosure above, which is basis-independent.  It only means that the exact finite polynomial antiderivative recurrence must be re-derived with the even-mode endpoint signs before a proof-grade nominal matrix generator is frozen.

## 5. Prime/cusp source arithmetic [Audit]

v13.357's remaining source budget treats the prime and cusp scalar constants by over-resolving certified logarithmic, trigonometric, Si, and Ci values so tightly that their matrix-level contribution is negligible relative to the archimedean \(1.22\times10^{-13}\) term.

That strategy is compatible with the odd block, but a source-faithful even-mode generator must still explicitly implement outward enclosures for these scalars rather than importing midpoint SciPy values.

Consequently the finite-high result is **not yet promoted** to

\[
A_{FF}^{(0)}\succeq0.53I
\]

as an [N-cert] statement.

## 6. Margin available for the outward arithmetic [N]

The midpoint shifted pole-free gap is

\[
0.0028423837861\ldots
\]

whereas the inherited analytic archimedean source envelope is at the \(10^{-13}\) scale.

Therefore the proof does not require an ultra-tight floating arithmetic certificate: any validated nominal-factorization/operator arithmetic enclosure comfortably below approximately

\[
2.8\times10^{-3}
\]

would suffice after source charges.

In practice a target at the \(10^{-6}\) or \(10^{-7}\) level would leave orders of magnitude of safety margin.

This is substantially easier than the older 7991-dimensional even high-block certificate that motivated v13.357.

## 7. Cross-thread ledger relevance

The concurrent cone/Q(sqrt3) entries remain monitored.

- v13.415's chi12 Suzuki source audit showed no useful finite-high or cross cancellation in the active q-support.
- the other v13.415 entry gives an exact chi12 residue-tail/digamma profile; this may still be useful when the remote Suzuki cross tail is regenerated, but no direct operator bound has yet been obtained from it.
- v13.416 separates the three mod-12 character roles and confirms that chi12 is specifically the real/Pell-time sign, while the ramified F4 quotient is chi_{-3}.  This supports keeping the carriers distinct in the positivity proof.

No cone/V4/Pell identity is presently being used as a substitute for the direct finite-high certificate.

## 8. Next certification step

The remaining finite-high task is now sharply defined:

1. derive the even-mode version of the exact polynomial antiderivative recurrence;
2. generate the pole-free nominal \(A_{FF}^{(0)}\) with outward-rounded pi, logarithms, prime phases, Si/Ci/cusp values, and polynomial arithmetic;
3. perform a validated shifted Cholesky/LDL backward-error estimate for
   \(A_{FF}^{(0)}-0.53I\);
4. combine that arithmetic residual with the dimension-free source enclosure.

If the combined perturbation is below the midpoint shifted margin, promote

\[
\boxed{A_{FF}^{(0)}\succeq0.53I}
\]

and hence, by \(2dd^T\succeq0\),

\[
\boxed{A_{FF}\succeq0.53I}.
\]

## Guardrails

- The pole-free eigenvalue and Cholesky residual are midpoint diagnostics, not outward proof statements.
- The odd sinh pole is dropped only because it is positive semidefinite; no approximation of it is being used.
- The odd-sector theorem `ind_{<=0}(A_odd(1))<=2` remains unpromoted.
- The combined full-parity bound `ind_{<=0}(A_{a=1})<=6` remains unpromoted.
- No exact-zero, RH, or GRH conclusion follows.

---

**Checkpoint conclusion.** The finite-high odd-sector certification can be reduced exactly to the pole-free block.  That harder block still has a midpoint floor about \(0.53284238\), leaving a \(2.842\times10^{-3}\) shifted margin.  The formerly opaque \(2\times10^{-13}\) source budget has been traced to an explicit uniform polynomial-kernel certificate and dimension-free Schur estimate, though the proof-grade even-mode nominal generator and outward arithmetic replay remain to be built.  This materially simplifies the next certificate without changing theorem status.
