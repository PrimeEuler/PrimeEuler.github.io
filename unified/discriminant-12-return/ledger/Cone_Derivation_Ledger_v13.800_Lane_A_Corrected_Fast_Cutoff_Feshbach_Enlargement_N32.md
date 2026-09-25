# Cone Derivation Ledger v13.800 — Lane A Corrected Fast-Cutoff Feshbach Enlargement Through \(N=32\)

Date: 2026-09-25

Lane: A.

Status: [N] corrected high-precision finite-section enlargement; [D] parity/sign convention inherited from v13.799; [G] protected dimension shown cutoff-dependent; [O] \(\kappa_0\) convergence and \(\kappa_1\) promotion remain open.

Formatting note: re-rendered after External Audit Round 102 (v13.802) to restore corrupted LaTeX backslashes. Mathematical content is unchanged.

Parents: v13.797–799.

Research artifact: suzuki_form_core_corrected_fast_cutoff.py, commit 7d32cb07ad8400cb99f715e2198aeceaffd4fcad.

## 1. Corrected parity builders

The even-v block uses odd Dirichlet indices and
\[
A_{\rm pole}^{(+)}=+2cc^T.
\]

The odd-v block uses even Dirichlet indices and the corrected sign
\[
A_{\rm pole}^{(-)}=-2dd^T.
\]

The corrected odd fast builder agrees with the direct source-faithful form through \(N=16\) at about
\[
8.7\times10^{-23}
\]
entrywise; the analogous even-v comparison is about
\[
8\times10^{-23}.
\]

## 2. First Schur parameter through \(N=32\)

Define
\[
E_{e,N}=f_e^T(A_N^{(+)})^{-1}f_e,
\qquad
E_{o,N}=f_o^T(A_N^{(-)})^{-1}f_o,
\]
and
\[
\kappa_{0,N}
=
\frac{E_{e,N}-E_{o,N}}
{E_{e,N}+E_{o,N}}.
\]

The corrected continuation gives
\[
\begin{array}{c|c}
N & \kappa_{0,N}\\
\hline
18 & 0.9981634258231784889223\\
20 & 0.9959431212804212882113\\
22 & 0.9971160610440417681680\\
24 & 0.9987372793730411261293\\
26 & 0.9990349070278660678051\\
28 & 0.9991646953989737916482\\
30 & 0.9994186427865947104573\\
32 & 0.9992230376149196805584
\end{array}
\]

For comparison,
\[
\kappa_{0,\infty}
\approx
0.9968019520324009035289.
\]

Thus
\[
\boxed{
\kappa_{0,N}\text{ is not cutoff-stable through }N=32.
}
\]

## 3. Lowest parity eigenvalues

At \(N=32\),
\[
\lambda_{\min}(A_{32}^{(+)})
\approx
7.1762110931\times10^{-26},
\]
\[
\lambda_{\min}(A_{32}^{(-)})
\approx
1.6285192018\times10^{-23}.
\]

The source-resolvent energies are approximately
\[
E_{e,32}
\approx
1.06931\times10^{25},
\qquad
E_{o,32}
\approx
4.15569\times10^{21}.
\]

## 4. Feshbach effective 10-core

Use a ten-dimensional low core in each parity sector and eliminate the remaining \(N=32\) modes by exact finite Schur complementation.

Even-v effective-core spectrum begins
\[
\begin{aligned}
&7.17621109312\times10^{-26},\\
&4.68282357060\times10^{-20},\\
&4.39883945855\times10^{-15},\\
&1.03931963248\times10^{-10},\\
&6.71959735666\times10^{-7},\\
&1.06872063732\times10^{-3},\\
&1.15999955256,\ldots
\end{aligned}
\]

Odd-v effective-core spectrum begins
\[
\begin{aligned}
&1.62851920175\times10^{-23},\\
&4.55540018216\times10^{-18},\\
&3.98939265910\times10^{-13},\\
&3.32725909787\times10^{-9},\\
&1.71474727214\times10^{-5},\\
&1.72676901707\times10^{-2},\\
&1.51646824479,\ldots
\end{aligned}
\]

The buffer is therefore eliminated cleanly while the near-null ladder remains visible in a fixed finite core.

## 5. Raw four-dimensional protection is not cutoff-stable

At \(N=16\), v13.798 showed a four-level ladder followed by gaps of approximately
\[
4.36\times10^{-3}\quad\text{(even-v)}
\]
and
\[
4.50\times10^{-2}\quad\text{(odd-v)}.
\]

At \(N=32\), the effective core has a fifth small level,
\[
6.72\times10^{-7}\quad\text{(even-v)},
\]
\[
1.71\times10^{-5}\quad\text{(odd-v)},
\]
before the next levels reach approximately
\[
1.07\times10^{-3}
\quad\text{and}\quad
1.73\times10^{-2}.
\]

Therefore
\[
\boxed{
\text{the protected dimension inferred directly from the raw }N=16\text{ spectrum is not cutoff-invariant.}
}
\]

## 6. Updated strategy

The correct continuation is:

1. keep a fixed low Feshbach core;
2. enlarge only the buffer;
3. recompute the effective core;
4. identify the low cluster by a gap criterion rather than hard-coding rank four;
5. transport source coordinates through the same elimination;
6. track \(E_e,E_o,\kappa_0\) and principal angles.

v13.801 subsequently improves this further by subtracting the common smooth bulk
\[
B_{\rm sm}=D_{\log}-H
\]
and recasting the problem as a compact relative resonance problem.

## 7. \(\kappa_1\) remains blocked

Since \(\kappa_{0,N}\) is still cutoff-sensitive,
\[
\boxed{
\text{do not promote a new }\kappa_{1,1}\text{ value yet.}
}
\]

## Result

\[
\boxed{
\kappa_{0,32}
\approx
0.9992230376149196805584,
}
\]
with no cutoff-convergence claim.

\[
\boxed{
\textbf{A fifth raw near-null effective-core direction has entered by }N=32\textbf{ in both parity sectors.}
}
\]

\[
\boxed{
\textbf{The correct continuation is fixed-core/growing-buffer Feshbach, refined in v13.801 by smooth-bulk subtraction.}
}
