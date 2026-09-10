# Cone Derivation Ledger v13.387 — External Audit Round 20 Resolution and Rank-2 Restoration

Date: 2026-09-10

Status labels: **[S]** source-established, **[D]** exact derived, **[N]** numerical, **[N-cert]** validated computational, **[Audit]** correction/limitation, **[O]** open.

## 1. Executive correction

**[Audit → resolved]** External Audit Round 20 (`v13.370`) incorrectly concluded that the project's legacy archimedean off-diagonal formula was wrong. The audit's product-to-sum computation was algebraically correct for the overlap it evaluated, but it evaluated `h=g''` against the **derivative-basis overlap** after the quadratic form had already been reduced by integration by parts.

For Dirichlet test functions `v,w`,

\[
Q_g(v,w)=\iint g(x-y)v'(x)w'(y)\,dx\,dy.
\]

After integration by parts in both variables, the smooth second-derivative contribution is

\[
Q_h(v,w)=-\iint h(|x-y|)v(x)w(y)\,dx\,dy,
\qquad h=g''\ \text{(smooth remainder)}.
\]

Thus `h` must be paired with the overlap of the **Dirichlet sine modes themselves**, not with the overlap of their derivatives.

## 2. Restored exact arch formula

Let

\[
\psi_n(x)=\sin\frac{n\pi(x+1)}2,\qquad
H_n=\int_0^2h(t)\sin\frac{n\pi t}{2}\,dt,
\]

for odd modes. Direct reduction of the sine-overlap gives, for `m != n`,

\[
\boxed{
K_{\rm arch}(m,n)
=-\frac4\pi\frac{nH_m-mH_n}{n^2-m^2}.
}
\]

This is exactly the legacy formula used in the pre-audit rank-two construction.

The Round-20 alternative

\[
\frac{2ab}{a^2-b^2}(bH_n-aH_m),\qquad a=m\pi/2,\ b=n\pi/2,
\]

is the value obtained by integrating `h` against the derivative overlap. It is not the post-integration-by-parts archimedean matrix element.

## 3. Independent numerical checks

**[N, high-confidence control]** Direct quadrature of `-h` against the sine-mode overlap agrees with the restored legacy closed form to numerical precision:

| `(m,n)` | direct `-∫h S_psi` | legacy formula | derivative-overlap formula |
|---|---:|---:|---:|
| `(1,3)` | `-0.1081045366838740` | `-0.1081045366838740` | `+0.0153046032370141` |
| `(1,21)` | `-0.0153470463946085` | `-0.0153470463946085` | `+0.0021730484457013` |
| `(21,29)` | `-0.000498872051576313` | `-0.000498872051576249` | `+0.0000677238563052651` |
| `(21,101)` | `-0.000143231891397458` | `-0.000143231891397457` | `+0.0000194379508652697` |

A second, more important end-to-end control evaluates Suzuki's source screw function `g(t)` directly against the derivative overlap, before any integration-by-parts decomposition. It agrees with the **legacy full matrix** and strongly disagrees with the rank-four audit branch. For example,

\[
A_{1,3}^{\rm source}=0.000387069325955204,
\]

\[
A_{1,3}^{\rm legacy}=0.000387069325951339,
\qquad
A_{1,3}^{\rm rank4}=0.123796209246839,
\]

and

\[
A_{1,21}^{\rm source}=-0.00104951791952813,
\]

\[
A_{1,21}^{\rm legacy}=-0.00104951791953675,
\qquad
A_{1,21}^{\rm rank4}=+0.0164705769207731.
\]

This source-form control is decisive because it bypasses the disputed arch decomposition completely.

## 4. Consequences for the ledger

**[Audit]** The rank-four repair branch `v13.373` through `v13.386` is superseded as an audit detour. In particular:

- the corrected-rank4 finite LDL is not the intended Suzuki matrix;
- the five-negative finite `S10` pattern found immediately after `v13.386` belongs to that wrong matrix and must not be interpreted as evidence about Suzuki's form;
- the centered arch generator gauge is algebraically valid for that alternate rank-four representation, but it is no longer needed for the source-faithful matrix;
- rank-four cross-transfer and high-complement claims are superseded.

**[D]** The original rank-two identity is restored:

\[
Z_n=2A_n+\operatorname{Si}(n\pi)+2H_n,
\]

\[
\boxed{
(A_0)_{mn}
=-\frac2\pi\frac{nZ_m-mZ_n}{n^2-m^2},\qquad m\ne n.
}
\]

Hence

\[
\boxed{\operatorname{rank}(XA_0-A_0X)\le2},
\qquad X=\operatorname{diag}(n^2).
\]

## 5. Restored proof chain and guardrails

The pre-audit validated-computational checkpoints may again be used for the matrix they were actually built from, subject to their original arithmetic-model qualifications:

- `v13.362`: finite high block `A0_[21,16001] >= 0.22 I` under the stated validated-computation model;
- `v13.363`: `||B_prime||<2.05` under its validated breakpoint/power-Schur model;
- `v13.365`: legacy/source-faithful cross architecture, subject to the exact status recorded there and subsequent audit qualifications;
- `v13.366`: ten-mode Schur reduction conditional on the high-complement positivity premise.

The immediate next task is to re-audit the **legacy/source-faithful** high-complement closure and `S10` chain with the new source-form control included as a regression invariant. No result from the rank-four detour should be imported merely because it is numerically favorable.

## 6. New regression invariant

Every future matrix assembly must satisfy both:

1. component-level closed-form checks; and
2. direct source-form checks
   \[
   \iint g(x-y)\psi_m'(x)\psi_n'(y)\,dx\,dy
   \]
   on a fixed set of low/high mode pairs.

A formula-level audit is not accepted if it disagrees with this end-to-end source invariant.

## 7. Scope guardrail

This correction **does not prove RH, disprove RH, establish an exact zero, or certify the final low-core inertia**. It resolves which archimedean matrix formula represents Suzuki's source quadratic form and removes the spurious five-negative rank-four branch from consideration.
