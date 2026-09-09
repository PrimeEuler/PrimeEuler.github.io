# Cone Derivation Ledger v13.373 — Audit Reconciliation: Corrected Arch Formula and Rank-4 Restart

Date: 2026-09-09

Status labels: **[D]** exact derived, **[N]** numerical, **[N-cert]** validated numerical, **[Audit]** correction/limitation, **[O]** open.

## 1. Audit finding accepted

**[Audit] External Audit Rounds 20–21 found a genuine formula error in the archimedean off-diagonal term used by the v13.349–v13.366 Suzuki chain.**

The legacy formula was

\[
K_{\rm arch}^{\rm old}(m,n)
=-\frac4\pi\frac{nH_m-mH_n}{n^2-m^2},
\qquad
H_j=\int_0^2h(t)\sin(j\pi t/2)\,dt.
\]

Direct product-to-sum reduction of the verified overlap kernel instead gives, for
\(a=m\pi/2\), \(b=n\pi/2\),

\[
\boxed{
K_{\rm arch}(m,n)
=\frac{2ab}{a^2-b^2}\bigl(bH_n-aH_m\bigr)
}
\]

or equivalently

\[
\boxed{
K_{\rm arch}(m,n)
=\pi mn\frac{nH_n-mH_m}{m^2-n^2}.
}
\]

This agrees with the audit's independent direct quadrature at the tested pairs.  For example, at \((m,n)=(21,29)\), the corrected expression gives approximately

\[
6.77238563\times10^{-5},
\]

whereas the legacy expression gives approximately

\[
-4.98872052\times10^{-4}.
\]

Therefore the old unified scalar identity

\[
(A_0)_{mn}=-\frac2\pi\frac{nZ_m-mZ_n}{n^2-m^2}
\]

with \(Z_n=2A_n+\operatorname{Si}(n\pi)+2H_n\) does **not** represent the intended full pole-free matrix.

## 2. Canonical end-to-end reconstruction

A canonical assembler has now been added:

`research-notes/suzuki_canonical_A0_matrix_assembly.py`

It constructs the actual pole-free matrix from the cusp, prime, corrected archimedean diagonal, and corrected archimedean off-diagonal definitions in one executable path.  It also retains the legacy arch switch solely to reproduce historical checkpoints.

**[N] Legacy reconstruction cross-check.** On odd modes \(21\le n\le399\), the canonical assembler with the legacy arch expression gives

\[
\lambda_{\min}\approx0.231953166254,
\]

which reproduces the project's historical v13.348 value

\[
0.231953166244
\]

to about \(10^{-11}\).  This strongly identifies the old certificate's matrix and shows that the remaining round-20 discrepancy was not caused by a hidden difference in the project's other component formulas.

**[N] Corrected reconstruction.** Replacing only the arch off-diagonal term by the audited/correct expression gives

\[
\boxed{
\lambda_{\min}(A_{0,[21,399]}^{\rm corrected})
\approx0.234501398756.
}
\]

Thus the correction modestly raises this finite-block minimum.  The audit's separate value near \(0.2767\) is **not reproduced** by the canonical assembly.  The audit was correct about the arch formula; its residual ~19% eigenvalue discrepancy appears to arise elsewhere in that independent reconstruction and is no longer evidence of a second project formula error.

This numerical finite-block result is not an infinite positivity certificate.

## 3. Structural salvage: displacement rank four

The corrected formula destroys the old single rank-two \(Z_n\) generator, but it does **not** destroy Cauchy-like structure.

Let

\[
Y_n=nH_n.
\]

Then

\[
(m^2-n^2)K_{\rm arch}(m,n)
=\pi mn(Y_n-Y_m)
=\pi\bigl[m(nY_n)-(mY_m)n\bigr].
\]

Hence the corrected arch block has displacement rank at most two.

The already-established cusp-plus-prime off-diagonal block is

\[
K_{cp}(m,n)
=\frac{2}{\pi}\frac{nU_m-mU_n}{m^2-n^2},
\qquad
U_n=\operatorname{Si}(n\pi)+2A_n,
\]

which is also displacement rank at most two.

Therefore the corrected full pole-free matrix satisfies a displacement equation of rank at most four:

\[
\boxed{
\operatorname{rank}(XA_0-A_0X)\le4,
\qquad X=\operatorname{diag}(n^2).
}
\]

This salvages the structured no-pivot LDL architecture: the generator state must be enlarged from two scalar generator vectors to four, while the diagonal update and scalar Schur-complement logic remain available.

## 4. Status rollback

**[Audit] v13.362 is superseded as a certificate for the intended operator.** Its validated arithmetic transcript certifies positivity of the legacy rank-two matrix, not the corrected Suzuki matrix.

**[Audit] v13.365 is superseded.** Its six-plane cross certificate and claimed global high-complement closure use the same legacy rank-two off-diagonal identity.  Therefore the statements

\[
\|A_{0,[21,16001],[16003,\infty)}\|<0.994
\]

and

\[
A_0|_{\mathcal D}>0
\]

are reopened for the corrected matrix.

**[Audit] v13.366 returns to conditional status.** The Haynsworth/Schur inertia theorem stated there is correct, but the premise \(A_{DD}>0\) has not yet been re-certified for the corrected matrix.  No theorem-level work on the final \(S_{10}\) should proceed until that premise is restored.

**[N-cert / surviving] v13.363's separate prime-operator target \(\|B_{\rm prime}\|<2.05\) is unaffected by this archimedean correction.**

The analytic one-sided/tail bounds that do not use the erroneous off-diagonal identity remain candidates for reuse, but any cross-operator or structured-matrix number derived from the legacy \(Z_n\) generator must be recomputed.

## 5. Restart target

The corrected Suzuki route is now:

1. use the canonical assembler as the ground-truth end-to-end regression test;
2. implement the exact rank-four displacement generators and verify them entry-by-entry against the canonical matrix;
3. rerun the structured LDL on \([21,16001]\) for the corrected matrix and establish a new finite lower bound;
4. rebuild the finite-to-tail cross norm with the corrected two-channel (cusp+prime plus arch) Cauchy structure;
5. combine with the surviving analytic tail coercivity to restore \(A_0|_{\mathcal D}>0\);
6. only then resume the full ten-mode Schur complement.

## Guardrail

No RH/GRH or exact-zero claim follows.  The corrected \(21..399\) positive numerical minimum is encouraging but is not a certificate for the infinite high complement.
