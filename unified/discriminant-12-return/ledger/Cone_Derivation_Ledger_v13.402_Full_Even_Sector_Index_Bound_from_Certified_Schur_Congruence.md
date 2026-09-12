# Cone Derivation Ledger v13.402 — Full Even-Sector Index Bound from Certified Schur Congruence

Date: 2026-09-12

Status labels: **[D]** exact derived, **[N-cert]** validated computational, **[O]** open.

## 1. Scope

v13.401 certified positivity of the exact infinite ten-mode Schur complement on an exact six-dimensional frozen subspace. Since the low core has dimension ten, this yields

\[
\operatorname{ind}_{\le0}(S_{10})\le 4.
\]

This checkpoint transfers that finite Schur statement to the full source-faithful Suzuki operator in the **even-v parity sector at a=1**.

No statement about the odd-v parity sector is made here.

## 2. Block decomposition

Use the orthogonal decomposition of the even-v sector

\[
\mathcal H_{\rm even}=C\oplus D,
\]

with

\[
C=\operatorname{span}\{\psi_1,\psi_3,\ldots,\psi_{19}\},
\qquad
D=\overline{\operatorname{span}}\{\psi_n:n\ge21,\ n\text{ odd}\}.
\]

The source-faithful quadratic form/operator has block representation

\[
A_{\rm even}=
\begin{pmatrix}
A_{CC} & A_{CD}\\
A_{DC} & A_{DD}
\end{pmatrix}.
\]

The restored source-faithful high-complement chain certifies

\[
A_{DD}\succeq \gamma_D I
\]

for some explicit \(\gamma_D>0\). Hence \(A_{DD}^{-1}\) exists and is bounded on \(D\).

Define the exact Schur complement

\[
S_{10}=A_{CC}-A_{CD}A_{DD}^{-1}A_{DC}.
\]

## 3. Exact triangular congruence

Set

\[
T=
\begin{pmatrix}
I_C & 0\\
- A_{DD}^{-1}A_{DC} & I_D
\end{pmatrix}.
\]

Because \(C\) is finite dimensional, \(A_{DC}:C\to D\) is bounded, and because \(A_{DD}^{-1}\) is bounded, \(T\) is bounded and boundedly invertible with

\[
T^{-1}=
\begin{pmatrix}
I_C & 0\\
A_{DD}^{-1}A_{DC} & I_D
\end{pmatrix}.
\]

A direct block calculation gives the exact form congruence

\[
\boxed{
T^*A_{\rm even}T=S_{10}\oplus A_{DD}.
}
\]

Equivalently, for \(u\in C\), \(v\in D\),

\[
\langle A_{\rm even}(u,v),(u,v)\rangle
=
\langle S_{10}u,u\rangle
+
\left\langle
A_{DD}\bigl(v+A_{DD}^{-1}A_{DC}u\bigr),
 v+A_{DD}^{-1}A_{DC}u
\right\rangle.
\]

Since the second term is strictly positive unless its argument vanishes, all nonpositive directions of the full even-sector form are carried entirely by \(S_{10}\).

## 4. Inertia identity

Bounded invertible congruence preserves maximal dimensions of positive, negative, and null subspaces. Because \(A_{DD}>0\),

\[
\boxed{
\operatorname{ind}_{\le0}(A_{\rm even})
=
\operatorname{ind}_{\le0}(S_{10}).
}
\]

Likewise,

\[
\operatorname{ind}_{<0}(A_{\rm even})
=
\operatorname{ind}_{<0}(S_{10}),
\]

and

\[
\dim\ker A_{\rm even}=\dim\ker S_{10}.
\]

The kernel correspondence, if a kernel exists, is explicit:

\[
u\in\ker S_{10}
\quad\Longleftrightarrow\quad
\left(u,-A_{DD}^{-1}A_{DC}u\right)\in\ker A_{\rm even}.
\]

This is only a correspondence; it does **not** assert that any nonzero kernel exists.

## 5. Certified consequence of v13.401

v13.401 proved positivity of \(S_{10}\) on an exact six-dimensional subspace of the ten-dimensional core. Therefore

\[
\boxed{
\operatorname{ind}_{\le0}(S_{10})\le4.
}
\]

By the exact congruence,

\[
\boxed{
\operatorname{ind}_{\le0}(A_{\rm even}(a=1))\le4.
}
\]

This is the first theorem-level finite-index statement for the full infinite-dimensional source-faithful **even-v sector** in this chain.

Because Suzuki's \(A_a\) has discrete spectrum bounded below, the same statement may be phrased spectrally: counting multiplicity within the even-v sector, the fifth eigenvalue satisfies

\[
\boxed{\lambda^{\rm even}_5(a=1)>0.}
\]

This does not determine the signs or exact values of the first four even-sector eigenvalues.

## 6. What this does not prove

- It does not prove \(A_{\rm even}\ge0\).
- It does not show any of the first four directions are zero modes.
- It does not prove \(\lambda_1(a=1)=0\).
- It says nothing yet about the odd-v parity sector.
- It does not establish RH or GRH.
- It does not convert the numerical near-zero pattern into exact kernel multiplicity.

## 7. Next target

The remaining source-faithful problem has split cleanly:

1. **even sector:** at most four nonpositive eigenvalues remain unresolved;
2. **odd sector:** audit/certify its lower spectrum independently;
3. within the four-dimensional even terminal sector, seek exact structural identities or higher-precision validated signs without assuming exact zeros.

The highest-leverage next step is to inspect the four unresolved even directions for exact algebraic/moment constraints and, separately, verify whether the odd sector has any nonpositive spectrum at all.
