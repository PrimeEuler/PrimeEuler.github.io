# Cone Derivation Ledger v13.406 — Odd Certificate Provenance Reconciliation

Date: 2026-09-13

Status labels: **[D]** exact derived, **[N]** numerical/transcript, **[V]** previously validated reusable bound, **[O]** open.

## 1. Purpose

Reconcile the fail-closed v13.405 odd-sector freeze with the older v13.404/v13.405 theorem-language files before any further promotion.  This checkpoint deliberately separates exact frozen data, reusable analytic bounds, and stored numerical transcript constants from independently replayable odd-sector certificates.

The authoritative continuation state remains fail-closed: no odd-sector inertia theorem is promoted here.

## 2. Exact frozen payload is in fact present on the current branch

The current repository contains

`research-notes/suzuki_odd_M4000_frozen_dyadic_Q8_L0.py`.

It stores a complete 10x8 hexadecimal `Q_HEX` payload and an 8x8 lower-triangular hexadecimal `L0_HEX` payload.  Its exact-`Fraction` minor test uses rows `(0,3,4,5,6,7,8,9)` and proves

\[
\boxed{\operatorname{rank}Q_8=8}
\]

exactly; the eight diagonal entries of `L0` are nonzero exact dyadics, so `L0` is exactly invertible.

The file history shows that the payload was frozen and then corrected on 2026-09-12 before the later v13.405 local-freeze checkpoint.  Therefore the v13.405 statement that the full payload was not stored in the repository is now superseded as a repository-status statement.  The fail-closed theorem status is **not** superseded by this observation.

## 3. Existing odd verifier is a transcript, not a generator replay

The repository also contains

`research-notes/suzuki_odd_M4000_index2_fail_closed_verifier.py`.

That file stores the following odd-sector numerical constants:

- shifted finite-high factor residual midpoint `4.107015804953941e-14`;
- shifted factor inverse norm midpoint `16.34083126127326`;
- combined low-rank cross value `0.9772519211742844`;
- near Frobenius remainder `0.0023073371285179897`;
- explicit-to-two-million cross upper `0.97957`;
- analytic tail beyond two million `0.03519`;
- residual-Gram explicit value `0.22441479153402388`;
- residual-Gram tail charge `0.000482`.

The script checks the final scalar inequalities, but it does not reconstruct the finite high block, rerun the shifted Cholesky, regenerate the cross decomposition, or recompute the residual Gram from the source-faithful matrix.  Those stored constants therefore remain **[N] transcript inputs** until their generating calculations are reproduced by an audited replay artifact.

This is the proof-critical distinction missed by the earlier theorem-language checkpoint.

## 4. Reusable analytic raw-tail bound

Several ingredients entering the raw tail floor already have independent project-level certificates, in particular the symbolic/interval prime estimate

\[
\|B_{\rm prime}\|<2.05.
\]

Using the conservative global bounds retained by the odd transcript,

\[
\|H_{\rm odd}\|\le\frac\pi2,
\qquad
\|K_{\rm cusp}\|\le0.706,
\qquad
\beta_{\rm arch}(4002)\le 0.00040766761547103477,
\]

and dropping the positive odd pole term gives

\[
\alpha_{4002}
=
\log(4002/4)-\frac\pi2-2.05-0.706-0.00040766761547103477
\]

with numerical value

\[
\boxed{\alpha_{4002}=2.5810511596134207\ldots>2.58}.
\]

Thus the raw-tail target itself has substantial visible margin and is not the delicate part of the remaining audit.

## 5. Correct relaxed cross target

The earlier v13.404 target used

\[
\|A_{FT}\|<1.013
\]

in order to obtain the cosmetically rounded floor `delta_odd>0.64`.

The stored odd transcript instead uses the deliberately looser outward target

\[
\boxed{\|A_{FT}\|<1.015}.
\]

If the finite-high floor

\[
A_{FF}\succeq0.53I
\]

and this `1.015` cross bound are independently replayed, then the effective tail Schur floor is already

\[
\delta_{\rm odd}
>
2.5810511596134207-
\frac{1.015^2}{0.53}
=
\boxed{0.6372304048964401\ldots}.
\]

Therefore the old `1.013` / `0.64` target is unnecessarily strong.  The certification target is henceforth relaxed to

\[
\boxed{
A_{FF}\succeq0.53I,
\qquad
A_{TT}\succeq2.58I,
\qquad
\|A_{FT}\|<1.015,
\qquad
\delta_{\rm odd}>0.637.
}
\]

This relaxation is algebraically sufficient for the intended eight-dimensional terminal comparison.

## 6. Terminal margin if the transcript inputs replay

The stored normalized targets are

\[
C_{\rm odd}\succeq0.80I,
\qquad
H_{\rm odd}\prec0.225I.
\]

Together with the relaxed tail floor they would give

\[
\delta_{\rm odd}\,0.80
>
0.5097843239,
\]

hence a normalized margin above

\[
0.5097843239-0.225>0.2847.
\]

So there remains very large terminal headroom.  The unresolved issue is not numerical closeness; it is independent outward provenance for the finite-high, cross, and residual-Gram constants.

## 7. Audit status of earlier theorem-language files

The earlier files

- `Cone_Derivation_Ledger_v13.404_Odd_Sector_Index_At_Most_Two.md`, and
- `Cone_Derivation_Ledger_v13.405_Quantitative_Positive_Schur_Gaps_After_Parity_Closure.md`

contain the desired odd-sector theorem conclusion.  For the continuing audit they are treated as historical candidate-certificate transcripts, not as the current promoted theorem, because the stored odd verifier does not independently regenerate its proof-critical large-block constants.

The later fail-closed v13.405 checkpoint and this reconciliation control the current status.

## 8. Remaining proof-critical replay tasks

The next certification work is now sharply localized:

1. independently rebuild the source-faithful odd finite block `F={22,24,...,4000}` and replay positivity of `A_FF-0.53I` with an outward residual/error budget;
2. independently regenerate the `F`-to-tail low-rank decomposition and prove `||A_FT||<1.015`, including the `n>2,000,000` analytic remainder;
3. independently regenerate the frozen-`Q8,L0` finite normalized matrix and residual Gram through two million, with outward source/solve/arithmetic charges proving `C_odd>=0.80I` and `H_odd<0.225I`;
4. only then restore the min-max / Schur-congruence conclusion `ind_{<=0}(A_odd)<=2`.

## 9. Guardrails

- Exact `rank(Q8)=8` and exact invertibility of `L0` are retained.
- The complete frozen dyadic payload is present in the repository.
- `delta_odd>0.637` is a valid algebraic consequence **conditional on** the still-to-be-replayed `0.53` finite-high and `1.015` cross bounds.
- Stored large-block decimal constants are not promoted merely because a transcript script asserts them.
- The first two tiny odd-sector directions are not exact kernels.
- No RH, GRH, exact-zero, or lowest-eigenvalue-zero conclusion follows.
