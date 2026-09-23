# Cone Derivation Ledger v13.728 — Suzuki Edge Laplace/Wiener–Hopf Transfer and Domain Gate

Date: 2026-09-23

Status: several consecutive gates after v13.727. Exact Laplace reduction of the Green component; exact Wiener–Hopf formulation of the screw component; identification of the boundary-delta transform; and a domain obstruction showing that the compensated equation cannot be treated as an ordinary pointwise Fredholm equation on regular half-line functions.

Synchronization: live head before this work was v13.727, commit \`e422b4a2efae0cd0c31a464341fd540523e5bc41\`. v13.726 is a separate representation-theory lane.

## Gate 1. Exact Laplace transform of the edge Green component [D]

Let
\[
Q(p)=\int_0^\infty e^{-p\xi}q(\xi)\,d\xi,\qquad \Re p>p_0,
\]
and
\[
h(\xi)=\int_0^\infty\min(\xi,\eta)q(\eta)\,d\eta.
\]
Then
\[
h(0)=0,\qquad h'(\xi)=\int_\xi^\infty q(\eta)\,d\eta,
\qquad h'(0)=Q(0),
\qquad -h''=q.
\]
Therefore
\[
p^2H(p)-h'(0)=-Q(p),
\]
so
\[
\boxed{
H(p)=\frac{Q(0)-Q(p)}{p^2}.
}
\]
The apparent singularity at \(p=0\) is removable under the corresponding moment hypotheses because \(Q(0)-Q(p)=O(p)\); a finite \(H(0)\) additionally requires the first moment/compatibility needed by the Green potential.

Thus the inverse-Laplacian edge term contributes
\[
\boxed{
-\lambda H(p)
=
-\lambda\frac{Q(0)-Q(p)}{p^2}.
}
\]

## Gate 2. Exact half-line transform of the screw component [D]

Define
\[
(G_+q)(\xi)=\int_0^\infty g(\xi-\eta)q(\eta)\,d\eta.
\]

A one-sided Laplace transform does not diagonalize this operator. Directly,
\[
\mathcal L_+[G_+q](p)
=
\int_0^\infty q(\eta)e^{-p\eta}
\left[
\int_{-\eta}^{\infty}e^{-pr}g(r)\,dr
\right]d\eta.
\]

Hence
\[
\boxed{
\mathcal L_+[G_+q](p)
\ne \widehat g(p)Q(p)
}
\]
in general. The missing lower-half contribution is the Wiener–Hopf edge correction.

Equivalently extend
\[
q_+(\xi)=
\begin{cases}
q(\xi),&\xi\ge0,\\
0,&\xi<0.
\end{cases}
\]
Then on the full line
\[
G_+q=(g*q_+)|_{\xi>0}.
\]

Let \(r_-\) denote the unknown negative-support residual required to turn the half-line equation into a full-line distributional identity. The screw equation is therefore naturally Wiener–Hopf, not a scalar Laplace-multiplier equation.

## Gate 3. The compensated source in Laplace space [D]

On the closed half-line,
\[
f_{\rm comp}=e^{-\xi}-\delta_0.
\]
Its one-sided Laplace transform is
\[
\boxed{
F_{\rm comp}(p)
=
\frac1{p+1}-1
=
-\frac{p}{p+1}.
}
\]

In particular
\[
\boxed{F_{\rm comp}(0)=0,}
\]
which is exactly the transform statement of the zero-total-mass compensation inherited from Suzuki's derivative core.

This zero at \(p=0\) is structural and must be retained by any edge transfer function.

## Gate 4. Formal transformed edge equation [D/G]

If
\[
\mathcal G_+[q](p)
:=
\mathcal L_+[G_+q](p),
\]
then the weak compensated equation, ignoring only the constant-output gauge, has the exact transform form
\[
\boxed{
\mathcal G_+[q](p)
-
\lambda\frac{Q(0)-Q(p)}{p^2}
=
-\frac{p}{p+1}.
}
\]

With a constant gauge \(C\), add \(C/p\) on the right.

This is exact wherever the one-sided transforms exist, but it is not yet algebraic in \(Q\), because \(\mathcal G_+\) is a Wiener–Hopf operator.

## Gate 5. Full Wiener–Hopf representation [D/G]

Let \(\mathcal F\) denote the full-line Fourier transform, and write the full-line screw symbol
\[
\widehat g(k)=\int_{\mathbb R}g(r)e^{-ikr}\,dr
\]
in the ordinary or distributional sense appropriate to Suzuki's screw function.

The half-line equation can be written schematically as
\[
P_+\left[
g*q_+ -\lambda K_{\rm edge}q
\right]
=
e^{-\xi}
\]
for \(\xi>0\), while the boundary atom is retained as a boundary functional.

After extension to the line one introduces a negative-support residual \(r_-\) and obtains the Wiener–Hopf identity
\[
\boxed{
g*q_+
-\lambda h_+
=
e^{-\xi}1_{\xi>0}
-\delta_0
+r_-,
}
\]
where \(r_-\) is supported in \((-\infty,0]\) and also absorbs the chosen constant-output normalization.

In transform variables this becomes
\[
\boxed{
\widehat g(k)\,\widehat q_+(k)
-\lambda\,\widehat h_+(k)
=
\frac1{1+ik}-1+\widehat r_-(k).
}
\]

The exact Green transform on the positive side is governed by
\[
H(p)=\frac{Q(0)-Q(p)}{p^2},
\]
so the Wiener–Hopf problem contains both a multiplicative screw symbol and a rank-one/moment coupling through \(Q(0)\).

This \(Q(0)\) coupling is the half-line remnant of the zero-frequency Neumann/mean-zero structure.

## Gate 6. Domain obstruction: the delta cannot be an ordinary Fredholm forcing [D]

For regular \(q\), both
\[
G_+q
\quad\text{and}\quad
K_{\rm edge}q
\]
are regular distributions under the hypotheses used in v13.727. Therefore the integral expression for \(S_{\rm edge}q\) cannot itself create \(-\delta_0\).

Consequently the equation
\[
S_{\rm edge}q=e^{-\xi}-\delta_0
\]
cannot be interpreted as an ordinary equality of locally integrable functions with a singular right-hand side.

There are only two source-faithful possibilities:

1. the operator domain is enlarged so \(q\) itself has a singular boundary component whose image supplies the atom; or
2. the \(-\delta_0\) term is encoded as a boundary condition/boundary functional in the closed edge form rather than as an interior forcing term.

Suzuki's warning that \(H(S_A)\not\subset L^2\) makes the second interpretation especially natural.

Thus the next rigorous object should be a closed half-line **form plus boundary functional**, not merely the naive integral operator on \(L^2(0,\infty)\).

## Gate 7. Weak form and boundary trace [D/G]

Define the edge form
\[
\mathfrak s_{\rm edge}[q,\varphi]
=
\int_0^\infty\!\!\int_0^\infty
\overline{\varphi(\xi)}
\left[g(\xi-\eta)-\lambda\min(\xi,\eta)\right]
q(\eta)\,d\eta\,d\xi.
\]

The compensated source acts by
\[
\boxed{
\mathfrak f_{\rm comp}[\varphi]
=
\int_0^\infty e^{-\xi}\overline{\varphi(\xi)}\,d\xi
-
\overline{\varphi(0)}.
}
\]

The source-faithful edge problem is therefore
\[
\boxed{
\mathfrak s_{\rm edge}[q,\varphi]
=
\mathfrak f_{\rm comp}[\varphi]
}
\]
for all test/form-domain vectors for which the boundary trace \(\varphi(0)\) is continuous.

This formulation retains the delta without demanding that a regular integral kernel literally output a delta distribution.

The unresolved theorem is construction of the precise limiting form domain from Suzuki's \(H(S_A)\) completions and proof that the trace functional survives continuously.

## Gate 8. Edge transfer function [D/C]

The raw exponential channel has Laplace transform
\[
Q_0(p)=\frac1{p+1}.
\]

For the actual edge solution define
\[
\boxed{
\mathcal T_{\rm edge}(p)
:=
(p+1)Q(p).
}
\]

Then
\[
\boxed{
Q(p)=\frac{\mathcal T_{\rm edge}(p)}{p+1}.
}
\]

The scalar-profile hypothesis rejected in v13.727 is exactly the claim
\[
\mathcal T_{\rm edge}(p)\equiv c.
\]

Therefore v13.727 implies, in any source-faithful solution retaining the boundary trace,
\[
\boxed{
\mathcal T_{\rm edge}(p)\text{ is nonconstant}
}
\]
unless \(Q\) fails to exist in the ordinary Laplace sense.

This is the precise nontrivial transfer factor that must intervene between Suzuki's deficiency channel and the raw Xi/Mellin exponential channel.

## Gate 9. What this does to the Xi bridge [D/C]

The v13.720 raw channel reconstruction works because the edge source/profile is \(e^{-\xi}\), whose transform is \(1/(p+1)\).

The source-faithful Suzuki profile replaces this by
\[
Q(p)=\frac{\mathcal T_{\rm edge}(p)}{p+1}.
\]

Therefore a direct Suzuki-to-Xi identification can survive only if the paired deficiency construction either

1. cancels \(\mathcal T_{\rm edge}\) between the reflected channels,
2. admits a canonical deconvolution by \(\mathcal T_{\rm edge}\), or
3. identifies the Xi kernel itself with the transferred profile rather than the raw exponential.

The scalar-normalization route is closed.

## Gate 10. Next exact computation [O]

The decisive missing input is now the explicit full-line transform/spectral representation of Suzuki's screw kernel \(g\). Once \(\widehat g\) is inserted, the Wiener–Hopf symbol can be factorized into plus/minus analytic factors and the boundary/moment condition can determine \(Q(0)\).

The target is an explicit formula
\[
\boxed{
Q(p)
=
\frac{\mathcal N_+(p)}
{\mathcal D_+(p)}
}
\]
for the positive-half-plane factor, from which
\[
\mathcal T_{\rm edge}(p)=(p+1)Q(p)
\]
can be compared directly with the theta/Xi Mellin symbol.

## Result

\[
\boxed{\textbf{PASS: exact Green-component Laplace reduction}}
\]
\[
\boxed{H(p)=\frac{Q(0)-Q(p)}{p^2}.}
\]

\[
\boxed{\textbf{PASS: compensated source transform}}
\]
\[
\boxed{F_{\rm comp}(p)=-\frac{p}{p+1}.}
\]

\[
\boxed{\textbf{PASS: nonconstant edge transfer is the correct next invariant}}
\]
\[
\boxed{\mathcal T_{\rm edge}(p)=(p+1)Q(p).}
\]

\[
\boxed{\textbf{OPEN: explicit Wiener--Hopf factorization after inserting Suzuki's exact screw symbol.}}
\]
