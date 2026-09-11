# Cone Derivation Ledger v13.392

## Source-Faithful High-Complement Reinstatement After Audit Resolution

### Status
Validated-computational / analytic, under the same explicit models as the constituent certificates. No RH/GRH, exact-zero, or final low-mode inertia claim.

## Why this checkpoint exists
External Audit Round 20 temporarily displaced the original rank-two archimedean matrix formula by pairing the smooth kernel remainder with the derivative-basis overlap. v13.387 resolved that mistake directly against Suzuki's source-level screw-function form: after integration by parts the smooth remainder acts on the Dirichlet sine-mode overlap, and the original formula

\[
K_{\rm arch}(m,n)=-\frac4\pi\frac{nH_m-mH_n}{n^2-m^2}
\]

is source-faithful. Consequently the compressed rank-two \(Z_n\) matrix used by the pre-audit finite-high and cross certificates is again attached to the intended operator.

## Reinstated inputs
Let

\[
F=\operatorname{span}\{\psi_n:21\le n\le16001,\ n\text{ odd}\},
\qquad
T=\overline{\operatorname{span}}\{\psi_n:n\ge16003,\ n\text{ odd}\}.
\]

The following inputs are now mutually source-faithful again:

1. Finite high block:
   \[
   A_F\succeq0.22I.
   \]

2. Raw remote tail coercivity, independently revalidated in v13.391 with the robust prime bound \(\|B_{\rm prime}\|<2.05\):
   \[
   A_T\succeq \alpha_T I,
   \qquad
   \alpha_T>4.673332491014484.
   \]

3. Source-faithful finite-high/tail cross certificate from the original rank-two six-plane reduction:
   \[
   \|G_{F,T}\|<0.994.
   \]

The cross certificate remains subject to its stated validated-computational model; this checkpoint does not strengthen that model, only restores its correct operator provenance.

## Schur-tail floor
Because \(A_F\succeq0.22I\),

\[
G^*A_F^{-1}G\preceq \frac{\|G\|^2}{0.22}I.
\]

Hence the Schur complement of \(F\) inside \(F\oplus T\) obeys

\[
A_T-G^*A_F^{-1}G
\succeq
\left(4.673332491014484-\frac{0.994^2}{0.22}\right)I.
\]

Numerically,

\[
\boxed{\delta_T>0.18225976374175623}.
\]

Therefore the full pole-free high complement

\[
\mathcal D=F\oplus T
\]

is positive under the combined certificate models.

## Consequence for the terminal low-core problem
The exact Feshbach/inertia reduction to the ten low odd modes

\[
C=\{1,3,\ldots,19\}
\]

is again available. The remaining problem is not high-complement positivity; it is certification of the low-core Schur complement, especially the tiny fifth source-faithful direction near \(4\times10^{-8}\) in finite-section diagnostics.

The preferred terminal route remains v13.390's anisotropic six-dimensional residual-Gram test rather than a uniform ten-column residual requirement.

## Guardrails
- The four numerical near-zero low-core directions are not certified exact kernels.
- The fifth finite-section eigenvalue is not yet a certified infinite-dimensional positive eigenvalue.
- No RH, GRH, exact-zero, or final inertia conclusion follows here.
- The earlier rank-four audit-detour branch v13.373--v13.386 remains superseded where it depends on the derivative-overlap arch formula.
