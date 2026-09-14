# Cone Derivation Ledger v13.452 — Full Parity Index Bound ≤ 6

Date: 2026-09-14

Status labels: **[D]** exact derived; **[N-cert]** validated computational input; **[Audit]** guardrail.

## 0. Synchronization [Audit]

A fresh live-head check immediately before this write found `v13.451` as the newest numbered ledger entry, so `v13.452` was free.

This checkpoint contains no new large numerical certificate. It combines the two independently certified parity-sector inertia bounds through the exact orthogonal parity decomposition used throughout the source-faithful Suzuki construction.

## 1. Certified parity-sector inputs

The even-v sector theorem from v13.402 is

\[
\boxed{
\operatorname{ind}_{\le0}(A_{\rm even}(a=1))\le4.
}
\]

The odd-v sector theorem restored in v13.451 is

\[
\boxed{
\operatorname{ind}_{\le0}(A_{\rm odd}(a=1))\le2.
}
\]

Both are theorem-level statements for the full infinite-dimensional source-faithful parity sectors, not merely finite truncations.

## 2. Exact parity decomposition [D]

The Fourier basis splits orthogonally into the two invariant parity sectors used in the separate audits:

\[
\mathcal H=\mathcal H_{\rm even}\oplus\mathcal H_{\rm odd}.
\]

In the source-faithful same-parity matrix representation, odd Fourier indices and even Fourier indices do not couple. Therefore

\[
\boxed{
A_{a=1}=A_{\rm even}(a=1)\oplus A_{\rm odd}(a=1).
}
\]

For orthogonal direct sums, the nonpositive index is additive:

\[
\operatorname{ind}_{\le0}(A\oplus B)
=
\operatorname{ind}_{\le0}(A)
+
\operatorname{ind}_{\le0}(B).
\]

Hence

\[
\begin{aligned}
\operatorname{ind}_{\le0}(A_{a=1})
&=
\operatorname{ind}_{\le0}(A_{\rm even}(1))
+
\operatorname{ind}_{\le0}(A_{\rm odd}(1))\\
&\le4+2.
\end{aligned}
\]

Therefore

\[
\boxed{
\operatorname{ind}_{\le0}(A_{a=1})\le6.
}
\]

## 3. Equivalent spectral statement

Because the source-faithful Suzuki operator at `a=1` has discrete spectrum bounded below, counting multiplicity across both parity sectors, the seventh eigenvalue is strictly positive:

\[
\boxed{
\lambda_7(a=1)>0.
}
\]

This statement uses only the certified finite-index bounds and the exact parity direct sum.

## 4. What remains unresolved [Audit]

This theorem does **not** determine the signs or exact values of the first six full-spectrum eigenvalues.

In particular:

- the first four even-sector directions remain unresolved;
- the first two odd-sector directions remain unresolved;
- none of those six directions is proved to be an exact zero mode;
- no kernel multiplicity is asserted;
- no statement such as `lambda_1(a=1)=0` is proved;
- no RH or GRH conclusion follows.

The near-zero numerical patterns remain diagnostics only until exact structure or further validated sign information is obtained.

## 5. Provenance chain

The full bound rests on two independently audited sector chains:

1. **even sector** — v13.401/v13.402 and External Audit Round 26;
2. **odd sector** — exact frozen `Q8,L0`, finite-high closure v13.434, cross closure v13.443, normalized provenance v13.449, and normalized closure v13.451.

No historical transcript-only odd constant remains necessary for the v13.451 theorem.

---

**Checkpoint conclusion.** The source-faithful Suzuki operator at `a=1` now has the theorem-level full-parity bound

\[
\boxed{\operatorname{ind}_{\le0}(A_{a=1})\le6},
\]

equivalently

\[
\boxed{\lambda_7(a=1)>0}.
\]

The six lower directions remain unresolved, and no exact-zero, kernel, RH, or GRH claim is made.