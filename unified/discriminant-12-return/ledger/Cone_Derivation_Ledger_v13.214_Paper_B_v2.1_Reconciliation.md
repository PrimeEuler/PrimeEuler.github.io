# Cone Derivation Ledger v13.214 — Paper B v2.1 Reconciliation

Date: 2026-09-04

Status labels: [S] source-established, [D] exact derived, [Audit] correction/reconciliation, [I] interpretation.

## Scope

This checkpoint closes the ground-up Paper B v2 audit recorded in v13.213 by promoting a corrected source:

`foundations/PaperB_EigenCoordinates_v2.1.tex`

The v2 source remains in `foundations/` as historical provenance. The active build target and GitHub Actions workflow are advanced to v2.1 in the same change set, in accordance with the project CI/publication invariant.

## [D] Core Lorentz geometry retained

The v2 audit confirmed the following exact structure.

For
\[
G_{a,b}=(a+b)L+(a-b)B_Y,
\]
we have
\[
\chi_G(\lambda)=\lambda(\lambda^2+4ab).
\]
The cutting plane
\[
(a-b)X+(a+b)T=c
\]
is invariant under the flow, and every connected nondegenerate signed section is a full orbit of the associated one-parameter subgroup.

The elliptic, parabolic and hyperbolic trichotomy therefore agrees exactly with the sign of `ab`.

## [Audit] Paper A two-sided synchronization

Paper B v2 still described Paper A as though its factor geometry were intrinsically the upper sheet `Y>=0`.

Paper A v2.4 instead uses the two-sided lift
\[
Y=\pm\sqrt{xy},
\]
while retaining `Y=+sqrt(xy)` as the principal one-sided lift when needed for discrete figures or one-sided measure statements.

Paper B v2.1 now adopts this distinction explicitly. The full Lorentz orbit lives on the signed future cone; restricting to `Y>=0` is a one-sided presentation choice, not the fundamental geometry.

This correction also preserves the distinction between factor exchange and cone-side reflection.

## [Audit] Single metric-dual cutting normal

The invariant cutting functional is represented by the Lorentz metric-dual vector
\[
m=(a-b,0,-(a+b)).
\]
It obeys
\[
G_{a,b}m=0
\]
and
\[
\langle m,(X,Y,T)\rangle_\eta=(a-b)X+(a+b)T.
\]
Its squared Lorentz norm is
\[
\boxed{m^2=-4ab.}
\]

v2 unnecessarily introduced a second vector with the opposite third component when stating the classification. That vector happened to have the same squared norm, so the sign classification was numerically unaffected, but it obscured which vector is actually the metric-dual normal of the invariant plane. v2.1 uses `m` consistently throughout.

## [D] Projectively normalized Lorentz generator

For `ab != 0`, define
\[
\boxed{\widehat G_{a,b}=\frac{G_{a,b}}{2\sqrt{|ab|}}.}
\]
Then the nonzero spectrum is
\[
\pm i\qquad(ab>0),
\]
and
\[
\pm1\qquad(ab<0).
\]

A positive common rescaling of `(a,b,c)` leaves `\widehat G` unchanged. A negative common rescaling reverses its sign and therefore only reverses flow orientation.

This cleanly separates the intrinsic projective orbit type from arbitrary time normalization of the unnormalized matrix generator.

## [D] Intrinsic elliptic projective coordinate

For `ab>0`, the unnormalized eigen-coordinate remains
\[
\zeta=(a+b)X+(a-b)T+2i\sqrt{ab}\,Y,
\]
with
\[
|\zeta|^2=c^2.
\]
For a nondegenerate cut, orient the representative so that `c>0` and define
\[
\boxed{z=\frac{\zeta}{c}.}
\]
Then
\[
\boxed{|z|=1.}
\]

The normalized coordinate is invariant under positive common rescaling of the oriented equation. It therefore gives the intrinsic unit-circle coordinate of the projective cut.

## [D] Intrinsic hyperbolic projective coordinates

For `ab<0`, with `r=sqrt(-ab)`, retain
\[
\eta_\pm=(a+b)X+(a-b)T\pm2rY,
\]
with
\[
\eta_+\eta_-=c^2.
\]
After orienting the representative by `c>0`, define
\[
\boxed{\xi_\pm=\frac{\eta_\pm}{c}.}
\]
Then
\[
\boxed{\xi_+\xi_-=1.}
\]

On each connected future branch the signs of `xi_+` and `xi_-` are fixed. The normalized split flow is multiplicative with opposite exponents.

Thus the two intrinsic nonparabolic normal forms are
\[
\boxed{|z|=1}
\qquad\text{and}\qquad
\boxed{\xi_+\xi_-=1}.
\]

## [Audit] Two distinct power-map layers

Paper B v2 correctly recognized that the level-raising power map depended on a chosen equation, but v2.1 makes the hierarchy explicit.

### Intrinsic projective orbit maps

On the normalized coordinates, integer powers give self-maps of the same normalized orbit:
\[
z\mapsto z^n
\]
and
\[
(\xi_+,\xi_-)\mapsto(\xi_+^n,\xi_-^n).
\]
These satisfy exact flow semiconjugacy
\[
\Psi_n\circ\mathrm{flow}_t
=\mathrm{flow}_{nt}\circ\Psi_n.
\]

### Chosen-equation level-raising maps

The older unnormalized construction remains exact:
\[
\zeta\mapsto\zeta^n,
\qquad
\eta_\pm\mapsto\eta_\pm^n,
\]
followed by reconstruction onto the target plane with right-hand side `c^n`.

But this construction is not invariant under arbitrary rescaling
\[
(a,b,c)\mapsto(\kappa a,\kappa b,\kappa c),
\]
because eigen-coordinates scale by `kappa` while their nth powers scale by `kappa^n`.

Therefore the publication-safe distinction is:

- normalized powers = intrinsic projective orbit self-maps;
- unnormalized powers = exact chosen-equation level-raising lifts.

## [D] Parabolic boundary retained

For `ab=0`, the generator is nilpotent and the nonzero diagonal eigen-coordinate construction collapses. This is a failure of diagonalization, not a theorem that no power map exists.

The coordinatewise operation
\[
(x,y)\mapsto(x^n,y^n)
\]
remains exact and maps rows/columns to their nth-power levels.

v2.1 also carries the two-sided sign convention into the cone coordinate:
\[
Y_n=\pm(xy)^{n/2}.
\]

Literal factor-coordinate translation and the Lorentz null-rotation flow remain distinct one-parameter notions.

## [D] Rapidity and discriminant-12 interface retained

The rapidity
\[
s=\frac12\log\frac{x}{y}
\]
obeys
\[
(x,y)\mapsto(x^n,y^n)
\Longrightarrow
s\mapsto ns.
\]

The discriminant-12 arithmetic return remains a separate discrete Lorentz element with
\[
\lambda=2+\sqrt3,
\]
acting by
\[
x\mapsto\lambda x,
\qquad
y\mapsto\lambda^{-1}y,
\]
so
\[
s\mapsto s+\log\lambda.
\]

No claim is made that the generic cutting generator `G_{a,b}` is itself the distinguished arithmetic return.

## [Audit] Publication and repository consequences

The authoritative Paper B source is now:

`foundations/PaperB_EigenCoordinates_v2.1.tex`

The build script is synchronized to that source:

`foundations/build_paper_b.sh`

The GitHub workflow is synchronized in the same change set:

`.github/workflows/build-paper-b.yml`

and commits:

`foundations/PaperB_EigenCoordinates_v2.1.pdf`

when the PDF changes.

`PaperB_EigenCoordinates_v2.tex/.pdf` are historical predecessor artifacts after this promotion and should no longer be treated as the current build target.

## Foundation status after this checkpoint

Paper B v2.1 is promoted to **ACTIVE / AUDITED BASELINE** for the continuous Lorentz/eigen-coordinate layer.

The main foundation dependency chain is now:

1. Paper A v2.4 — audited geometric/conic foundation.
2. Area note v1.1 — exact one-sided measure companion.
3. Paper B v2.1 — audited continuous Lorentz/projective foundation.
4. Paper C — next theorem-reconciliation target, downstream of corrected Paper B.
5. Casimir / Null-Diamond v2.1 — active audited bridge, logically independent of unresolved Paper-C power-map wording.

## Next task

Reconcile Paper C against Paper B v2.1. In particular:

1. remove the inherited claim that every cone symmetry generator has a canonical exact power map;
2. use the intrinsic/projective versus chosen-equation distinction from Paper B v2.1;
3. correct the global two-mode positive-discrete-series parameter to
\[
k=\frac{|n_1-n_2|+1}{2},
\]
with `k=X` only in the oriented `n1>=n2` sector;
4. synchronize Paper C with the transition-cell conventions already fixed in the null-diamond foundation.
