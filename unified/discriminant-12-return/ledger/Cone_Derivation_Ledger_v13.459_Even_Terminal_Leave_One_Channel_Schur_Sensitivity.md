# Cone Derivation Ledger v13.459 — Even Terminal Leave-One-Channel Schur Sensitivity

Date: 2026-09-14

Status labels: **[N]** midpoint numerical diagnostic; **[D]** exact structural setup; **[Audit]** guardrail.

## 0. Synchronization [Audit]

A live-head check immediately before this write found `v13.458` as the newest numbered ledger entry, so `v13.459` was free.  No theorem-level inertia statement is strengthened here.

The full source-faithful parity theorem already stands at

\[
\operatorname{ind}_{\le0}(A_{a=1})\le6.
\]

The purpose here is structural: identify which source channels control the unresolved four-dimensional even-v terminal sector.

## 1. Canonical source-faithful setup [D/N]

Use the canonical restored even-v Suzuki matrix formulas of

`research-notes/suzuki_canonical_A0_matrix_assembly.py`,

with low core

\[
C=\{1,3,\ldots,19\}
\]

and finite block

\[
F_M=\{21,23,\ldots,M\}.
\]

The full even PSD pole is retained.  Let `Q` be the frozen exact-dyadic 10x6 positive subspace from v13.399, and let

\[
N_4=\ker(Q^T)
\]

be its numerical four-dimensional orthogonal complement.

For each arithmetic prime-power source channel

\[
q\in\{2,3,4,5,7\},
\]

remove that channel from the **entire finite matrix before inversion**, then recompute the finite Schur complement.  Thus this is a nonlinear Schur sensitivity, not an additive attribution.

The reproducible helper is

`research-notes/suzuki_even_terminal_leave_one_prime_schur_sensitivity.py`.

## 2. Cutoff stability [N]

The calculation was run at

\[
M=399,799,1599,3999.
\]

The base first four Schur eigenvalues remain at numerical zero scale throughout, while the fifth and sixth converge toward the known M3999 positive values.  The leave-one-channel sensitivities stabilize rapidly across the ladder.

This rules out the observed hierarchy being an artifact of one finite cutoff.

## 3. Exceptional non-V4 direction [N]

From v13.455, the unit-residue span has principal cosines with the unresolved four-plane

\[
0.9357,\ 0.7127,\ 0.7024,\ 0.2351.
\]

The least V4-aligned unresolved direction is approximately 94.3% concentrated on the low-core coordinate `n=3`.

At M=3999, its raw low-core prime Rayleigh pieces are approximately

\[
\begin{array}{c|r}
q&v^TP_qv\\\hline
2&+0.5833983961\\
3&-0.2956044377\\
4&-0.1150868653\\
5&-0.0166984825\\
7&-1.13\times10^{-7}
\end{array}
\]

The **nonlinear leave-one-prime Schur responses** on the same direction are

\[
\boxed{
\begin{array}{c|r}
\text{channel removed}&v^T(S_{-q}-S)v\\\hline
q=2&-0.5837733497\\
q=3&+0.2773058643\\
q=4&+0.1138870933\\
q=5&-0.0057570708\\
q=7&-9.30\times10^{-9}
\end{array}}
\]

The sign pattern and magnitudes are already nearly stable by M=399.

Therefore the exceptional direction is not a pure q=3 defect.  It is a robust cancellation dominated by

\[
\boxed{q=2\text{ versus }q=3,4,}
\]

with q=5 secondary and q=7 negligible.

## 4. Whole unresolved four-plane hierarchy [N]

Project the Schur change to `N_4`.  At M=3999 the operator norms are approximately

\[
\boxed{
\begin{array}{c|c}
\text{channel removed}&\|N_4^T(S_{-q}-S)N_4\|_2\\\hline
q=2&0.6823393\\
q=3&0.6340103\\
q=4&0.2697328\\
q=5&0.1048639\\
q=7&8.4\times10^{-8}
\end{array}}
\]

Thus the same hierarchy is a property of the whole unresolved four-plane, not merely the exceptional vector.

## 5. Grouped source sensitivity [N]

The second helper

`research-notes/suzuki_even_terminal_grouped_component_schur_sensitivity.py`

removes the entire cusp, archimedean, PSD-pole, or aggregate-prime block before Schur elimination.

At M=3999:

### Remove cusp

The first four Schur eigenvalues become approximately

\[
(-1.3410,-0.9862,-0.5028,-0.1275).
\]

### Remove archimedean block

The first four become

\[
\boxed{
(1.2448\times10^{-4},
 2.4286\times10^{-4},
 4.4882\times10^{-4},
 1.0016\times10^{-3})
}
\]

and this positive pattern is stable from M=399 through M=3999.

### Remove PSD pole

One direction falls to roughly

\[
-5.35,
\]

while the remaining three stay at numerical zero scale.

### Remove all prime channels

The first four become approximately

\[
(-0.5896,\ 0.0761,\ 0.4640,\ 0.7412).
\]

## 6. Structural interpretation [I]

The unresolved even four-plane is therefore not controlled by one isolated arithmetic source.

A more faithful working picture is

\[
\boxed{
\text{near-zero terminal sector}
=
\text{multi-source cancellation among cusp, pole, primes, and archimedean terms}.
}
\]

Inside the prime sector, the ramified-prime hierarchy is nevertheless very strong:

\[
q=2\sim q=3 \gg q=4 > q=5 \gg q=7.
\]

This is compatible with the discriminant-12 local arithmetic developed in v13.448-v13.458, where primes 2 and 3 are the ramified primes and the full V4 character data is recovered only after combining quotient and lift information.

However, no operator-level identification with the mod-4 derivation `D_7`, the prime-3 tangent phase, or the intrinsic S3 quotient has been proved.

## 7. Main new diagnostic conclusion [N/I]

Two earlier simplistic hypotheses are now ruled out numerically:

1. the four terminal directions are not missing low polynomial moments;
2. the exceptional fourth even direction is not a pure q=3 mode.

The strongest current structural statement is instead:

\[
\boxed{
\text{three directions carry substantial V4 residue content, while the fourth is a ramified multi-source cancellation mode.}
}
\]

The latter is anchored near `n=3` but depends strongly and oppositely on the q=2 and q=3/4 source channels after full finite-high elimination.

## 8. Next target [O]

The highest-leverage next test is to build a basis adapted to this decomposition:

1. three projected V4/lift directions, organized by `chi_-3`, `chi_-4`, and their product `chi_12`;
2. one exceptional ramified cancellation direction;
3. form the exact/midpoint 4x4 terminal Schur matrix in that adapted basis;
4. test whether it becomes approximately block diagonal or reveals a rank-one/rank-two coupling law.

If such a reduction appears, then derive it from the source-faithful Cauchy structure before making any theorem claim.

## 9. Guardrails [Audit]

- All present sensitivities are midpoint diagnostics.
- Leave-one-channel Schur responses are nonlinear and must not be interpreted as additive source decomposition.
- The first four even directions are not asserted exact kernels.
- The first two odd directions remain unresolved individually.
- No stronger inertia, exact-zero, RH, or GRH claim follows.

---

**Checkpoint conclusion.**  The leave-one-channel audit shows that high-mode Schur elimination preserves a stable arithmetic hierarchy rather than generating it.  The unresolved even terminal four-plane is a multi-source cancellation object, with q=2 and q=3 dominant, q=4 important, q=5 secondary, and q=7 negligible.  Three directions remain strongly residue/V4-like; the exceptional fourth direction is instead a robust ramified cancellation mode centered near n=3.