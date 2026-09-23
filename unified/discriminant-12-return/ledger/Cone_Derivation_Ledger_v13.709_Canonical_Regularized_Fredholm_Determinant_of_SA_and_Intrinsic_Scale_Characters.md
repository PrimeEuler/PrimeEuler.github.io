# Cone Derivation Ledger v13.709 — Canonical Regularized Fredholm Determinant of S_A and Intrinsic Scale Characters

Date: 2026-09-23

Status: exact operator-ideal/character gate following v13.708. The goal is to construct the strongest canonical Fredholm determinant justified directly by Suzuki's continuous-kernel operator \(S_A\), without reviving the invalid local Dirichlet-Laplacian bulk comparison.

## 0. Synchronization

Immediately before this write the live head was v13.708, commit \`88967aa3e0424cc2ba8ca3cd5de99ac4b1b3193e\`. No v13.709 collision was present.

Use Suzuki Section 8 as recorded in v13.282 and corrected in v13.662:
\[
S_A=G_A-\lambda K_A,
\qquad
K_A=(-\Delta_N)^{-1},
\]
acting on
\[
L_0^2(-A,A),
\]
with continuous integral kernel
\[
k_A(x,y)=g_A(x-y)-\lambda N_A(x,y).
\]

The exact energy-space transfer is
\[
\bar D:\mathcal H(T_A)\overset{\sim}{\longrightarrow}\mathcal H(S_A).
\]

## 1. Operator ideal forced by the continuous kernel

Because \([-A,A]^2\) is compact and \(k_A\) is continuous,
\[
k_A\in L^2([-A,A]^2).
\]
Therefore the integral operator \(S_A\) is Hilbert--Schmidt:
\[
\boxed{S_A\in\mathfrak S_2.}
\]

Its Hilbert--Schmidt norm is
\[
\|S_A\|_{\mathfrak S_2}^2
=
\int_{-A}^{A}\int_{-A}^{A}
|k_A(x,y)|^2\,dx\,dy.
\]

Continuity of the kernel alone does **not** prove
\[
S_A\in\mathfrak S_1
\]
(trace class). Therefore an ordinary operator determinant
\[
\det(I-zS_A)
\]
must not be asserted from the current hypotheses.

The canonical determinant available at the proved ideal level is the second regularized Fredholm determinant.

## 2. Canonical determinant [D]

Define
\[
\boxed{
D_A(z):=\det{}_2(I-zS_A).
}
\]

For \(S_A\in\mathfrak S_2\), this is a canonical entire function of \(z\).

In terms of the eigenvalues \(\{\mu_n\}\) of the compact self-adjoint \(S_A\), counted with multiplicity,
\[
\boxed{
D_A(z)
=
\prod_n
(1-z\mu_n)e^{z\mu_n}.
}
\]

The product converges because
\[
\sum_n|\mu_n|^2<\infty.
\]

Equivalently, near \(z=0\),
\[
\boxed{
\log D_A(z)
=
-\sum_{m=2}^{\infty}
\frac{z^m}{m}\operatorname{Tr}(S_A^m),
}
\]
where \(S_A^m\in\mathfrak S_1\) for every \(m\ge2\).

Normalization is intrinsic:
\[
\boxed{D_A(0)=1,\qquad D_A'(0)=0.}
\]

No arbitrary nonvanishing entire characteristic gauge is present.

## 3. Deficiency reflection [D]

Let
\[
(Rf)(x)=f(-x).
\]
Suzuki's reflection relation exchanges the deficiency vectors \(u_+\leftrightarrow u_-\).

For the Section-8 kernel,
\[
k_A(-x,-y)=k_A(x,y),
\]
because both \(g_A(x-y)\) and the Neumann kernel \(N_A(x,y)\) are invariant under simultaneous reflection. Hence
\[
\boxed{RS_AR=S_A.}
\]

Therefore
\[
R(I-zS_A)R=I-zS_A.
\]

The regularized determinant is invariant under unitary conjugation:
\[
\boxed{
D_A(z)\xmapsto{\mathscr R}D_A(z).
}
\]

Thus any local logarithm
\[
\tau_A(z):=\log D_A(z)
\]
is deficiency-reflection even:
\[
\boxed{
\mathscr R:\tau_A\mapsto\tau_A.
}
\]

This supplies the required \(F=+\) parity intrinsically.

## 4. Complex conjugation [D]

The Section-8 kernel is real for the real finite-\(A\) problem:
\[
\overline{k_A(x,y)}=k_A(x,y).
\]
Let \(C\) be coefficient conjugation. Then
\[
CS_AC=S_A.
\]

Consequently
\[
\overline{D_A(z)}
=
D_A(\bar z).
\]

For a local logarithm chosen compatibly with \(D_A(0)=1\),
\[
\boxed{
\tau_A(\bar z)=\overline{\tau_A(z)}
}
\]
away from zeros/branch cuts.

Write
\[
\tau_A=p_A+iq_A.
\]
Then under conjugation:
\[
p_A\mapsto p_A,
\qquad
q_A\mapsto-q_A.
\]

Together with reflection evenness:
\[
\boxed{
\Re\tau_A:(F,C)=(+,+),
}
\]
\[
\boxed{
\Im\tau_A:(F,C)=(+,-).
}
\]

These are exactly the cone scale characters
\[
\Re\tau:(+,+),\qquad
\Im\tau:(+,-).
\]

## 5. Intrinsic scale-pair result [D]

Define the continuous-kernel Fredholm scale logarithm
\[
\boxed{
\tau_A^{Fred}(z)
:=
\log\det{}_2(I-zS_A).
}
\]

Then
\[
\boxed{
\Re\tau_A^{Fred}\leftrightarrow\Re\tau
}
\]
and
\[
\boxed{
\Im\tau_A^{Fred}\leftrightarrow\Im\tau
}
\]
are now proved at the exact \(C_2^2\)-character/equivariance level.

Unlike the common characteristic gauge of v13.708, \(\tau_A^{Fred}\) is intrinsic to the specified continuous-kernel operator \(S_A\): it is fixed by the spectrum of \(S_A\) and the canonical \(\det_2\) normalization.

Therefore the previous statement
\[
\text{“only the boost half is canonical”}
\]
can be sharpened:

\[
\boxed{
\text{both character pairs now have canonical operator representatives,}
}
\]
namely
\[
\boxed{
\tau_A^{Fred}=\log\det{}_2(I-zS_A)
}
\]
for the scale pair and
\[
\boxed{
\ell_A^{Cayley}=\log s_A
}
\]
for the boost pair.

## 6. Full four-character table [D]

\[
\boxed{
\begin{array}{c|c|c|c}
\text{cone direction}&(F,C)&\text{Suzuki operator representative}&\text{status}\\ \hline
\Re\tau&(+,+)&
\Re\log\det_2(I-zS_A)&
\text{intrinsic character match}\\
\Im\tau&(+,-)&
\Im\log\det_2(I-zS_A)&
\text{intrinsic character match}\\
\Re\ell&(-,+)&
\Re\log s_A&
\text{intrinsic Cayley character match}\\
\Im\ell&(-,-)&
\Im\log s_A&
\text{intrinsic Cayley character match}
\end{array}
}
\]

The extension phase \(\theta\) remains a second representative of the \((-,-)\) boundary character sector.

Thus the complete regular \(C_2^2\) character pattern now occurs in canonical operator quantities.

## 7. Important non-identification [G]

The character match does **not** prove the literal equality
\[
\tau_A^{Fred}=\tau_{\rm cone}.
\]

Nor does it prove
\[
\det_2(I-zS_A)=G_A(z)
\]
for the common factor in Suzuki's printed characteristic.

The two objects have the same required \(F/C\) character type, but equality would require an additional determinant/characteristic theorem.

Likewise this does not repair the v13.689 Friedrichs-vs-Zeeman numerical discrepancy.

The exact claim is:
\[
\boxed{
\log\det_2(I-zS_A)
\text{ is an intrinsic Suzuki continuous-kernel representative of the }
(+,+)\oplus(+,-)
\text{ scale-character sector.}
}
\]

## 8. Why det_2 rather than det [G]

If a future argument proves
\[
S_A\in\mathfrak S_1,
\]
then the ordinary Fredholm determinant exists and
\[
\det_2(I-zS_A)
=
\det(I-zS_A)e^{z\operatorname{Tr}S_A}.
\]

The difference in logarithms is the linear term
\[
z\operatorname{Tr}S_A.
\]

Until trace class is established, \(\det_2\) is the canonical rigorous choice. It removes precisely the unproved trace term while retaining all spectral zeros \(z=\mu_n^{-1}\) for nonzero eigenvalues.

## 9. Relation to generalized eigenvalues [G]

Suzuki's Section-8 spectral problem is naturally the pencil
\[
G_Au=\lambda K_Au,
\]
while \(S_A=G_A-\lambda K_A\) is formed after choosing a lower-bound parameter \(\lambda\).

Therefore \(D_A(z)=\det_2(I-zS_A)\) is intrinsic **for the fixed operator \(S_A\)**, but it is not yet a canonical determinant of the generalized pencil as a function of the physical spectral parameter.

This is a second guardrail:
\[
\boxed{
\text{canonical for fixed }S_A
\neq
\text{canonical spectral determinant of the pencil }(G_A,K_A).
}
\]

A stronger scale bridge would construct a determinant directly for the pencil or show that the fixed-\(S_A\) determinant is independent of the admissible auxiliary \(\lambda\) after normalization.

## 10. Candidate pencil determinant and obstruction [O]

Formally one would like
\[
\det(I-\zeta K_A^{-1}G_A),
\]
but \(K_A^{-1}\) is unbounded, so this is not presently justified on \(L_0^2\).

The energy-space transfer may permit a symmetrized compact operator such as
\[
K_A^{-1/2}G_AK_A^{-1/2},
\]
but compactness/Schatten class and domain control must be proved before assigning a determinant.

Therefore no generalized-pencil Fredholm determinant is promoted here.

## 11. Result

\[
\boxed{
S_A\in\mathfrak S_2
}
\]
from the continuous kernel.

\[
\boxed{
D_A(z)=\det_2(I-zS_A)
}
\]
is a canonical entire regularized Fredholm determinant.

\[
\boxed{
RS_AR=S_A,\qquad CS_AC=S_A.
}
\]

Hence
\[
\boxed{
\Re\log D_A:(+,+),
\qquad
\Im\log D_A:(+,-).
}
\]

Therefore:
\[
\boxed{
\textbf{PASS: the continuous-kernel representation has an intrinsic canonical scale-character pair.}
}
\]

But:
\[
\boxed{
\textbf{OPEN: equality with Suzuki's common characteristic factor }G_A.
}
\]

And:
\[
\boxed{
\textbf{OPEN: a canonical determinant of the generalized pencil }(G_A,K_A).
}
\]

## 12. Next gate

There are now two canonical logarithmic operator coordinates:
\[
\tau_A^{Fred}=\log\det_2(I-zS_A),
\qquad
\ell_A^{Cayley}=\log s_A.
\]

The next high-value test is whether they are independent in the precise differential sense expected from the cone \((\mathbb C^\times)^2\) structure. Compute their logarithmic derivatives,
\[
\partial_z\tau_A^{Fred},
\qquad
\partial_z\ell_A^{Cayley},
\]
express them through resolvent traces/Weyl data, and test whether one can be algebraically recovered from the other. Independence would support a genuine two-coordinate operator torus; dependence would collapse the proposed bridge.
