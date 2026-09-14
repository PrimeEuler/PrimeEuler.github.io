# Cone Derivation Ledger v13.473 — Even Index-3 Seven-Plane Cross-Block Guardrail

Date: 2026-09-14

Status labels: **[D]** exact derived, **[N]** numerical diagnostic, **[N-cert]** previously certified input, **[Audit]** guardrail.

## 0. Synchronization [Audit]

The live ledger was checked at the beginning of this continuation and again immediately before this numbered write.  During the work, `v13.472` (External Audit Round 36) landed.  The newest numbered entry at the final check was therefore `v13.472`, so `v13.473` was free.

Relevant predecessors:

- `v13.399-v13.402`: frozen M3999 six-plane and certified even-sector index bound;
- `v13.451-v13.452`: restored odd theorem and full `ind_{<=0}(A_{a=1})<=6`;
- `v13.467`: signed near-rank-one tail self-energy on the stabilized even four-plane;
- `v13.471`: theorem-cutoff M3999 unresolved four-plane residual-Gram replay;
- unnumbered helper `suzuki_M3999_even_index3_directional_certificate_budget.py`: conditional scalar budget for one unresolved direction;
- `v13.472`: independent audit of v13.471 and that conditional scalar budget.

The new reproducible guardrail helper is

`research-notes/suzuki_M3999_even_index3_sevenplane_guard.py`

(commit `6d7b3a5ae0b7501da08fdc5feedc679e06d260a6`).

## 1. The logical gap in a scalar-only index-3 argument [D]

Let `Q` be the already-certified six-dimensional positive low-core subspace and let `v_*` be one additional unresolved direction.

To improve the even-sector nonpositive-index bound from four to three, it is not enough to prove separately

\[
Q^T S_\infty Q>0
\]

and

\[
v_*^T S_\infty v_*>0.
\]

One needs positivity on the full seven-dimensional span

\[
\operatorname{span}(Q,v_*).
\]

Equivalently, after writing

\[
\begin{pmatrix}
A&b\\
b^T&a
\end{pmatrix},
\]

with `A=Q^T S_\infty Q`, one must control the cross vector `b` and prove

\[
\boxed{a-b^T A^{-1}b>0.}
\]

Therefore the two scalar nominal targets in the earlier directional budget are necessary ingredients but are not by themselves sufficient for an index-3 theorem.

## 2. M3999 finite midpoint cross [N]

Regenerating the source-faithful M3999 finite Schur complement gives the largest unresolved finite direction

\[
v_*^T S_F v_*\approx1.34626944\times10^{-12}.
\]

Its finite coupling to the frozen six-plane is tiny in raw coordinates:

\[
\boxed{\|Q^T S_Fv_*\|_2\approx8.0\times10^{-16}.}
\]

However the first frozen normalization scale is small.  With the exact-dyadic `L_0`,

\[
\boxed{
\|L_0^{-1}Q^T S_Fv_*\|_2
\approx6.50\times10^{-13}.
}
\]

Thus even the finite-side cross cannot simply be dropped when targeting a `10^{-12}` directional margin.

## 3. Tail residual cross [N]

The v13.471 residual machinery was rerun on the combined basis `[Q,N]`, where `N` is a numerical orthonormal basis of the unresolved four-plane.

For the specific largest finite unresolved direction `v_*`, through two million modes,

\[
\boxed{
\|L_0^{-1}Q^TR^*Rv_*\|_2
\approx1.47\times10^{-7}.
}
\]

Using only the certified effective-tail floor

\[
T_{\rm eff}\succeq\delta_T I,
\qquad
\delta_T>0.18225976374175623,
\]

the conservative cross contribution can therefore be of order

\[
\delta_T^{-1}\times1.47\times10^{-7}
\sim8\times10^{-7}
\]

in the normalized six-plane coordinates.

This is the dominant obstruction missed by the scalar-only budget.

## 4. Proper seven-dimensional coercivity-floor lower bound [N/N-cert]

Using the certified coercivity floor, form the midpoint lower-bound matrix

\[
S_{\rm low}
:=S_F-\delta_T^{-1}R^*R.
\]

Normalize the six-plane by `L_0`, then Schur-eliminate it.

The certified-six-plane normalized block in this midpoint residual payload has eigenvalues approximately

\[
\boxed{
(0.0222169,\,0.9999982,\,1,\,1,\,1,\,1).
}
\]

For `v_*` alone, before accounting for its six-plane cross,

\[
\boxed{
a\approx6.85\times10^{-13}>0.}
\]

But after the proper six-plane Schur penalty,

\[
\boxed{
a-b^TA^{-1}b\approx-2.84\times10^{-11}.}
\]

Correspondingly, the seven-dimensional lower-bound matrix has

\[
\boxed{
\lambda_{\min}\approx-2.84\times10^{-11}.
}
\]

Therefore the scalar positivity target does not close a seven-plane theorem under the present coercivity-only tail treatment.

## 5. Optimization over the whole unresolved four-plane [N]

The same calculation was then performed before choosing `v_*`: after eliminating the certified six-plane, the effective four-dimensional coercivity-floor lower-bound matrix on the unresolved complement has spectrum approximately

\[
\boxed{
(-2.84\times10^{-11},\,
6.7\times10^{-16},\,
3.47\times10^{-15},\,
8.32\times10^{-15}).
}
\]

This gives two useful facts.

First, the largest-finite-eigenvalue direction `v_*` is not the best seventh direction once the six-plane tail cross is included.

Second, three other nominal directions remain positive in this conservative midpoint lower-bound model, but only at `10^{-15}` scale.  The existing exact-vs-nominal source uncertainty

\[
\boxed{\|A_{\rm exact}-A_{\rm nominal}\|\lesssim2\times10^{-13}}
\]

is much larger than those positive margins.

Thus the present source-certification architecture cannot promote any of those three directions either.

## 6. Consequence for the index-3 program [Audit]

The unnumbered directional budget remains a useful scalar sensitivity calculation, but its concluding conditional sentence must not be read as a sufficient theorem criterion.

The correct seven-dimensional target is one of the following equivalent forms:

1. outward-certify the full `7x7` block on `span(Q,v)` as positive;
2. outward-certify the six-plane block and its cross vector, then prove the scalar Schur complement
   \[
   a-b^TA^{-1}b>0;
   \]
3. choose a corrected seventh vector obtained by eliminating the six-plane cross and certify positivity of the resulting reduced scalar.

With the current coercivity-floor replacement `T_eff^{-1}<=delta_T^{-1}I`, the best nominal residual directions have only `10^{-15}`-scale positive margins, so the existing `2e-13` source envelope is the immediate limiting scale.

## 7. What would be needed next [Audit]

A plausible future index-3 route must improve at least one of two ingredients:

- **tail anisotropy:** replace the crude scalar inverse bound `delta_T^{-1}I` by a source-faithful directional/low-rank enclosure of `T_eff^{-1}` on the residual channels, thereby reducing the six-plane/unresolved cross penalty;
- **source anisotropy:** replace the global `2e-13` operator source error by a much sharper outward directional error on the best cross-corrected candidate vector.

Because v13.467/v13.471 show that the residual tail is extremely low rank, the first route is structurally promising: the coarse coercivity floor may be losing far more than necessary in the cross block.

## 8. Theorem status [Audit]

No theorem is weakened or strengthened by this checkpoint.

The certified bounds remain

\[
\boxed{\operatorname{ind}_{\le0}(A_{\rm even}(1))\le4,}
\]

\[
\boxed{\operatorname{ind}_{\le0}(A_{\rm odd}(1))\le2,}
\]

and hence

\[
\boxed{\operatorname{ind}_{\le0}(A_{a=1})\le6.}
\]

No exact-kernel, RH, or GRH claim follows.

---

**Checkpoint conclusion.** The M3999 scalar directional budget does not by itself suffice for an even-sector index-3 theorem because positivity must hold on a seven-dimensional subspace, not on the six-plane and one extra vector separately.  The missing six-plane/unresolved cross block is negligible in raw finite coordinates but becomes significant after normalization and tail elimination.  Under the current certified coercivity-floor replacement, the proper seven-plane Schur complement for the largest finite unresolved direction is negative at about `-2.84e-11`; optimizing over the whole four-plane leaves only `10^-15`-scale positive candidates, below the existing source uncertainty.  The index-3 frontier therefore moves to anisotropic tail-inverse and directional source certification, not the two scalar targets alone.
