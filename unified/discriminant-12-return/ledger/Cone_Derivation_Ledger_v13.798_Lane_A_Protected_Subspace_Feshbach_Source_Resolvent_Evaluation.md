# Cone Derivation Ledger v13.798 — Lane A Protected-Subspace/Feshbach Source-Resolvent Evaluation at \(a=1,\lambda=0\)

Date: 2026-09-25

Lane: A.

Status: [N] protected numerical gate through \(N=16\); [D] exact finite-dimensional Feshbach identity; [G] source/domain guardrails preserved.

Audit correction: External Audit Round 102 (v13.802) reran the committed script on the identical SHA-256 frozen payload. The relative Feshbach/full-spectral energy differences are
\[
\boxed{
9.059467616\times10^{-56}\ \text{(even-v)},\qquad
9.145195157\times10^{-58}\ \text{(odd-v)}.
}
\]
The original \(1.5\times10^{-65}\) and \(1.8\times10^{-67}\) values were erroneous transcription/computation figures. This correction does not change any substantive conclusion. This file was also re-rendered to restore the LaTeX backslashes corrupted in the original write.

Parents: v13.795–797. Research artifact: suzuki_form_core_protected_resolvent.py, commit da767855076603870705d65f4795fe9e2fadf81a.

## 1. Source-faithful finite problem

At
\[
a=1,\qquad \lambda=0,
\]
use the audited direct Dirichlet form matrix and analytic source overlaps. For each parity block \(B\),
\[
E=f^TB^{-1}f.
\]
No endpoint condition is imposed on the deficiency vector, no raw first-kind Fredholm inverse is used, and no identification \(\bar Dv=iv'\) is assumed.

## 2. Frozen payload

A maximum cutoff \(N=16\) was assembled at 70 decimal digits and serialized at 60 significant digits.

\[
\mathrm{SHA256}(A_{16})
=
\texttt{d48c064ba483dc79225764be0be7ba4aa6102640e9a05eedd0c9f5549a8b9839},
\]
\[
\mathrm{SHA256}(f_{16})
=
\texttt{1be3f5f7ed32a38e26028dafed44e25cae920f0f983a335ea50671544203f03d}.
\]

Even-v:
\[
\mathrm{SHA256}(A_{16}^{(+)})
=
\texttt{de2bde77f9359b7221beb52d46b1c1ef66dc52b80b938bb269bb45a66c0157d2},
\]
\[
\mathrm{SHA256}(f_{16}^{(+)})
=
\texttt{65acc73c73598a62f98e8ba036fe9e3a84d68359e913f572fe5fe2d8334e50df}.
\]

Odd-v:
\[
\mathrm{SHA256}(A_{16}^{(-)})
=
\texttt{f870cfca7b37583c65d4f70cb057735eb8ae6fb5daa35af6772041910e7a390b},
\]
\[
\mathrm{SHA256}(f_{16}^{(-)})
=
\texttt{e2b3afe3303ca1386e96c6aea18c0db9151cecbbcab18c64267d5e8788527e38}.
\]

An independent 80-digit \(N=12\) assembly and the upper-left \(N=12\) block of the 70-digit \(N=16\) assembly agree to about
\[
2.04\times10^{-71}
\]
entrywise.

## 3. Protected spectral anatomy

At \(N=16\), even-v begins
\[
8.3158\times10^{-19},\
1.2131\times10^{-13},\
2.5194\times10^{-9},\
6.9481\times10^{-6},\
4.3566\times10^{-3},\
1.0066,\ldots
\]
and odd-v begins
\[
1.2111\times10^{-16},\
7.3738\times10^{-12},\
4.7080\times10^{-8},\
6.6578\times10^{-5},\
4.4992\times10^{-2},\
1.5500,\ldots
\]

Thus both parity blocks have a four-level near-null ladder at this cutoff.

## 4. Exact finite-dimensional Feshbach identity

Let \(P\) be the first \(r\) eigenvectors of the \(N=12\) parity block embedded into \(N=16\), and let \(Q\) be the orthogonal complement. Define
\[
S=P^TBP-P^TBQ(Q^TBQ)^{-1}Q^TBP,
\]
\[
g=P^Tf-P^TBQ(Q^TBQ)^{-1}Q^Tf.
\]
Then
\[
\boxed{
f^TB^{-1}f
=
f_Q^T(Q^TBQ)^{-1}f_Q+g^TS^{-1}g.
}
\]

For \(r=4\), the complement gaps are approximately
\[
\gamma_C^{(+)}\approx3.93\times10^{-3},
\qquad
\gamma_C^{(-)}\approx4.20\times10^{-2},
\]
while the protected-to-complement Frobenius couplings are
\[
\|A_{PC}^{(+)}\|_F\approx2.60\times10^{-2},
\qquad
\|A_{PC}^{(-)}\|_F\approx3.19\times10^{-2}.
\]

The corrected relative Feshbach/full-spectral energy differences are
\[
\boxed{
9.059467616\times10^{-56}\ \text{(even-v)},\qquad
9.145195157\times10^{-58}\ \text{(odd-v)}.
}
\]

## 5. Source quadratic forms

At \(N=16\),
\[
E_{e,16}\approx9.88105202101156878\times10^{17},
\]
\[
E_{o,16}\approx6.64502527901586881\times10^{14}.
\]

The lowest protected direction contributes approximately \(99.999567\%\) of the even-v energy and \(99.997165\%\) of the odd-v energy.

The first Schur parameter is
\[
\boxed{
\kappa_{0,16}
=
0.9986559003076436730382\ldots
}
\]
with cutoff sequence
\[
\begin{array}{c|c}
N & \kappa_{0,N}\\
\hline
4 & 0.99820062872003903161\\
6 & 0.99954753083354612292\\
8 & 0.99734803602012615745\\
10 & 0.96783862780471321268\\
12 & 0.99389585322145076917\\
14 & 0.99769745662762483588\\
16 & 0.99865590030764367304
\end{array}
\]
so no cutoff-convergence claim is made.

## 6. Precision dependence and diagnosis

The \(N=16\) value stabilizes by roughly 35 significant payload digits despite condition numbers of about
\[
2.55\times10^{18}\quad\text{(even-v)},
\qquad
2.07\times10^{16}\quad\text{(odd-v)}.
\]

Thus fixed-cutoff linear algebra is not the obstruction. The active issue is cutoff evolution of the near-null structure.

Later checkpoints v13.799–801 refine the interpretation: correct the odd pole sign, use a fixed low Feshbach core with growing buffer, and then subtract the smooth bulk \(B_{\rm sm}=D_{\log}-H\). The raw four-dimensional \(N=16\) protected picture is therefore a valid local diagnostic, not an asymptotic multiplicity theorem.

## Result

\[
\boxed{
\textbf{At }N=16\textbf{, four protected directions isolate a stiff complement in both parity channels.}
}
\]

\[
\boxed{
\textbf{The corrected relative agreement is about }9.06\times10^{-56}\textbf{ (even) and }9.15\times10^{-58}\textbf{ (odd).}
}
\]

\[
\boxed{
\textbf{The unresolved issue is cutoff evolution, not fixed-cutoff numerical instability.}
}
