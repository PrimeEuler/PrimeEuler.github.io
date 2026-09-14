# Cone Derivation Ledger v13.463 — High-Precision Even Terminal Four-Plane Cutoff Stability

Date: 2026-09-14

Status labels: **[N]** numerical diagnostic, **[I]** interpretation, **[Audit]** guardrail.

## 0. Synchronization [Audit]

The live ledger was checked at the start of this continuation and again immediately before this numbered write. The newest numbered entry remained `v13.462`, so `v13.463` was free.

Relevant predecessors:

- `v13.459`: leave-one-channel Schur sensitivity of the unresolved even four-plane;
- `v13.461`: high-precision finite-cutoff spectrum, resolving the four binary64 zero-scale levels into positive tiny eigenvalues;
- `v13.462`: obstruction to canonically identifying the Galois `V4` with the tangent translation `V4`.

The present checkpoint asks whether the unresolved four-dimensional low-core geometry itself is stable under high-precision cutoff evolution, independently of the frozen `M=3999` verifier basis.

## 1. Source-faithful high-precision ladder [N]

Use the full even-v finite source-faithful Suzuki matrix with modes

\[
1,3,\ldots,M,
\]

including:

- cusp contribution,
- the five prime-power channels `q=2,3,4,5,7`,
- the restored source-faithful archimedean term,
- the full PSD even-sector cosh pole.

The matrix is assembled in `mpmath` high precision using

`research-notes/suzuki_even_small_cutoff_highprecision_spectrum.py`.

For

\[
M\in\{29,39,49,59,69\},
\]

diagonalize the full finite matrix at 70 decimal digits and retain the first four eigenvectors.

The new reproducible diagnostic is

`research-notes/suzuki_even_highprecision_eigenvector_evolution.py`.

## 2. The first four eigenvectors are low-core objects [N]

Restrict each of the first four normalized full eigenvectors to the ten-mode low core

\[
C=\{1,3,5,7,9,11,13,15,17,19\}.
\]

Across the entire cutoff ladder, the norm of this ten-coordinate restriction is greater than

\[
\boxed{0.99999}
\]

for all four eigenvectors.

The first three are closer still to unit low-core norm, at effectively all displayed digits.

Thus the tiny spectral directions are already overwhelmingly low-core localized at these cutoffs.

## 3. Successive four-plane convergence [N]

Let `U_M` be an orthonormal basis of the four-dimensional low-core span of the first four high-precision eigenvectors at cutoff `M`.

The principal cosines between successive four-planes converge rapidly toward one.

The smallest principal cosine is approximately

\[
\begin{array}{c|c}
\text{pair}&\text{smallest principal cosine}\\\hline
29\to39&0.9995946\\
39\to49&0.9999936\\
49\to59&0.99999958\\
59\to69&0.99999990
\end{array}
\]

while the other three principal cosines are numerically indistinguishable from one on this scale.

Therefore

\[
\boxed{
U_M\text{ stabilizes extremely rapidly as }M\text{ grows.}
}
\]

This is a subspace statement and does not depend on arbitrary signs of individual eigenvectors.

## 4. Direct comparison with the frozen M=3999 unresolved complement [N]

The certified even-sector verifier freezes an exact-dyadic six-dimensional positive subspace

\[
Q\subset\mathbf R^{10}
\]

at `M=3999`.

Let

\[
N_{3999}:=\ker(Q^T),
\]

which is the four-dimensional unresolved low-core complement used in the later terminal diagnostics.

Comparing the high-precision `M=69` four-plane with this frozen complement gives principal cosines

\[
\boxed{
1,\quad1,\quad1,\quad0.99999884.
}
\]

Hence

\[
\boxed{
U_{69}\approx N_{3999}
}
\]

at extremely high subspace overlap.

This is strong evidence that the frozen terminal four-plane is not a late-cutoff or eigenvector-freezing artifact. The same four-plane is already essentially present in the much smaller high-precision matrices.

## 5. Mod-12 unit-residue profile is cutoff-stable [N/I]

On the ten-mode low core, let `R_unit` be the span of the four residue-indicator vectors for

\[
1,5,7,11\pmod{12}.
\]

The principal cosines between `U_M` and `R_unit` stabilize to

\[
\boxed{
0.936,\quad0.713,\quad0.702,\quad0.235
}
\]

by the upper end of the high-precision ladder.

These are the same values previously observed from the frozen `M=3999` unresolved complement in `v13.455`.

Therefore the qualitative split

\[
\boxed{
\text{three substantially residue-aligned directions}
+\text{ one poorly residue-aligned direction}
}
\]

is itself cutoff-stable.

This remains a geometric overlap diagnostic, not an invariant decomposition of the Suzuki operator into character blocks.

## 6. Exceptional residue-orthogonal direction [N]

Inside `U_M`, choose the unit vector having the smallest principal cosine with the four-dimensional unit-residue span.

This is the same diagnostic exceptional direction used in the preceding terminal analysis.

Its overlap stabilizes extremely quickly:

\[
|\langle x_{39},x_{49}\rangle|>0.999998,
\]

and by the last two cutoffs the overlap is above

\[
0.99999998.
\]

At `M=69`, its overlap with the corresponding exceptional vector extracted from the frozen `M=3999` unresolved complement is

\[
\boxed{0.99999981}.
\]

The exceptional vector remains strongly concentrated on the `n=3` coordinate, with amplitude

\[
\boxed{|x_3|\approx0.943}.
\]

Thus the `n=3`-dominated exceptional direction is not an artifact of the frozen basis either.

## 7. Relation to v13.460-v13.462 [I/Audit]

The stabilized numerical pattern

\[
3+1
\]

is suggestive when placed next to the exact four-state tangent `S_4` architecture of `v13.460`.

However `v13.462` proves that the presently available arithmetic data do **not** canonically identify the Galois `V4` with the tangent translation `V4`.

Therefore no canonical `S_4` action on the Suzuki terminal four-plane is claimed here.

The safe conclusion is only that the Suzuki four-plane itself has a stable internal geometry consisting of three substantial unit-residue directions plus one exceptional ramified-cancellation direction.

## 8. Consequence for the next search [I]

The next structural target should no longer be "does the terminal four-plane stabilize?" It does.

The more relevant question is whether the rapidly shrinking high-precision eigenvalues have a systematic cutoff law and whether the stabilized four-plane supports four distinct asymptotic scales.

In particular, track

\[
\lambda_j(M),\qquad j=1,2,3,4,
\]

at high precision over a longer cutoff ladder and test candidate asymptotics such as

\[
M^{-p},\qquad e^{-cM},\qquad e^{-c\sqrt M},
\]

without assuming an exact kernel.

## 9. Guardrails [Audit]

- The four finite-cutoff eigenvalues are not declared exact zeros.
- The stabilized four-plane is not declared a canonical V4/S4 representation.
- Residue overlap does not imply operator block-diagonalization; v13.459 already showed strong channel mixing.
- The high-precision computations are numerical diagnostics, not outward spectral certificates for the infinite operator.
- No RH or GRH conclusion follows.

---

**Checkpoint conclusion.** The unresolved even-sector four-plane is a robust source-faithful feature of the finite matrices. High-precision eigenvectors at cutoffs as small as `M=39-69` already reproduce the frozen `M=3999` unresolved complement to near-unit principal-angle overlap. Its mod-12 unit-residue profile and its `n=3`-dominated exceptional direction are equally stable. The structural frontier therefore moves from subspace identification to the asymptotic law of the four tiny positive eigenvalue scales.