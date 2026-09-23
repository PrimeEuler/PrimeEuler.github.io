# Cone Derivation Ledger v13.732 — Exact Compensated Suzuki Edge Wiener–Hopf Equation

Date: 2026-09-23

Status: exact transform-level Wiener–Hopf reduction of the compensated edge form, with the \(-\delta_0\) boundary term and the rank-one Green moment \(Q(0)\) kept explicitly.

Synchronization: live head before this write was v13.731, commit \`f319a942e234e1c8f6685ffebe00fbb30eb0e71e\`. Entries v13.729--731 are a separate Tate/adelic lane and do not collide with the Suzuki edge calculation.

## 1. Conventions and compensated edge problem

Let
\[
q_+(\xi)=H(\xi)q(\xi),
\qquad
Q_+(k)=\int_0^\infty e^{-ik\xi}q(\xi)\,d\xi,
\]
with \(H\) the half-line indicator and Fourier convention
\[
\widehat f(k)=\int_{\mathbb R}e^{-ikx}f(x)\,dx.
\]

Let
\[
h(\xi)=\int_0^\infty\min(\xi,\eta)q(\eta)\,d\eta,
\qquad \xi\ge0.
\]
Then
\[
-h''=q,\qquad h(0)=0,\qquad h'(0)=Q_+(0).
\]

The source-faithful weak edge equation from v13.725 is
\[
\mathfrak s_{\rm edge}[q,\varphi]
=
\int_0^\infty e^{-\xi}\overline{\varphi(\xi)}\,d\xi
-\overline{\varphi(0)}.
\]

Its interior kernel is
\[
S_{\rm edge}=G_+-\lambda K_{\rm edge},
\qquad
(G_+q)(\xi)=\int_0^\infty g(\xi-\eta)q(\eta)d\eta.
\]

## 2. Exact distributional extension of the Green potential

Extend \(h\) by zero:
\[
h_+(x)=H(x)h(x).
\]

Because \(h(0)=0\),
\[
(h_+)'
=
Hh',
\]
and
\[
(h_+)''=Hh''+\delta_0h'(0).
\]

Using \(h''=-q\),
\[
\boxed{
(h_+)''=-q_+ + Q_+(0)\delta_0.
}
\]

Fourier transformation gives
\[
-k^2\widehat h_+(k)
=
-Q_+(k)+Q_+(0),
\]
hence
\[
\boxed{
\widehat h_+(k)
=
\frac{Q_+(k)-Q_+(0)}{k^2}.
}
\]

This is the Fourier counterpart of the exact Laplace identity from v13.728,
\[
H(p)=\frac{Q(0)-Q(p)}{p^2}.
\]

The numerator subtraction is essential: it is the rank-one boundary/moment contribution inherited from the half-line Green kernel.

## 3. Exact full-line Wiener–Hopf completion

For \(x>0\),
\[
G_+q=(g*q_+)(x).
\]

To turn the positive-half-line equation into a full-line distributional identity introduce an unknown residual \(r_-\) supported in
\[
\operatorname{supp}r_-\subset(-\infty,0].
\]

Then the compensated problem has the Wiener--Hopf completion
\[
\boxed{
g*q_+
-\lambda h_+
=
e^{-x}H(x)-\delta_0+r_-.
}
\]

This equation is exact as a distributional completion of the weak half-line problem: the negative-support residual contains whatever is required on \(x\le0\), including any boundary-supported component needed because the regular integral expression cannot itself create the explicit \(-\delta_0\).

The decomposition is not unique until the boundary/gauge normalization of \(r_-\) is fixed. The explicit \(-\delta_0\) is retained to display the Suzuki core compensation.

## 4. Exact transformed Wiener–Hopf equation

The transforms are
\[
\widehat{e^{-x}H(x)}(k)=\frac1{1+ik},
\qquad
\widehat{\delta_0}=1.
\]

Let
\[
R_-(k)=\widehat r_-(k).
\]

Since
\[
\widehat{g*q_+}(k)=\widehat g(k)Q_+(k),
\]
and
\[
\widehat h_+(k)=\frac{Q_+(k)-Q_+(0)}{k^2},
\]
we obtain
\[
\boxed{
\widehat g(k)Q_+(k)
-\lambda\frac{Q_+(k)-Q_+(0)}{k^2}
=
\frac1{1+ik}-1+R_-(k).
}
\]

Equivalently,
\[
\boxed{
\left(\widehat g(k)-\frac{\lambda}{k^2}\right)Q_+(k)
+
\frac{\lambda Q_+(0)}{k^2}
=
-\frac{ik}{1+ik}+R_-(k).
}
\]

This is the exact compensated Wiener--Hopf equation, with both requested nonstandard pieces visible:

1. boundary compensation:
   \[
   \boxed{-1=\widehat{-\delta_0}};
   \]

2. rank-one Green contribution:
   \[
   \boxed{\frac{\lambda Q_+(0)}{k^2}}.
   \]

## 5. Pole-free form

The \(k^{-2}\) notation should not be interpreted by separating singular pieces at \(k=0\); the difference
\[
\frac{Q_+(k)-Q_+(0)}{k^2}
\]
is the object fixed by the Green potential and its boundary conditions.

Multiplying the exact equation by \(k^2\) gives the safer pole-free form
\[
\boxed{
\left[k^2\widehat g(k)-\lambda\right]Q_+(k)
+\lambda Q_+(0)
=
k^2\left[
-\frac{ik}{1+ik}+R_-(k)
\right].
}
\]

Define the edge Wiener--Hopf symbol
\[
\boxed{
\mathcal D(k)=k^2\widehat g(k)-\lambda.
}
\]

Then
\[
\boxed{
\mathcal D(k)Q_+(k)+\lambda Q_+(0)
=
-\frac{i k^3}{1+ik}
+k^2R_-(k).
}
\]

The scalar \(Q_+(0)\) is therefore an explicit rank-one unknown coupled to the factorization problem.

## 6. Analytic half-plane structure

Under the usual decay/tempered hypotheses:

- \(Q_+(k)\) is the boundary value of a function analytic in the lower half-plane for the convention \(e^{-ikx}\), because \(q_+\) is supported on \(x\ge0\).
- \(R_-(k)\) is the boundary value of a function analytic in the upper half-plane, because \(r_-\) is supported on \(x\le0\).

Thus the factorization problem is genuinely of Wiener--Hopf type:
\[
\boxed{
\text{lower-half-plane unknown }Q_+
\quad\leftrightarrow\quad
\text{upper-half-plane unknown }R_-.
}
\]

The source pole
\[
\frac1{1+ik}
\]
lies at
\[
k=i,
\]
consistent with the positive-half-line exponential source and the chosen Fourier convention.

## 7. Boundary delta versus residual boundary mass

Because the left-hand side is regular at the level discussed in v13.727, the full-line residual must contain a compensating boundary-supported component if the identity is represented with an explicit \(-\delta_0\).

Write
\[
r_-=a\,\delta_0+\widetilde r_-,
\qquad
\operatorname{supp}\widetilde r_-\subset(-\infty,0].
\]

Then
\[
R_-(k)=a+\widetilde R_-(k).
\]

For a regular left-hand side the net atomic coefficient on the right must vanish, forcing
\[
\boxed{a=1}
\]
at the purely distributional full-line-completion level.

This does **not** erase the Suzuki boundary functional. It shows that if one insists on representing the weak boundary problem as an equality of full-line distributions with a regular left side, the boundary functional migrates into the splitting convention for the Wiener--Hopf residual.

Therefore the invariant source-faithful datum is the weak trace term
\[
-\varphi(0),
\]
not the arbitrary allocation of a \(\delta_0\) between the displayed source and \(r_-\).

## 8. Rank-one structure made explicit

Let
\[
M:=Q_+(0)=\int_0^\infty q(\xi)d\xi.
\]

Then the pole-free equation is
\[
\boxed{
\mathcal D(k)Q_+(k)
=
-\frac{i k^3}{1+ik}
-\lambda M
+k^2R_-(k).
}
\]

For a fixed \(M\), this is an ordinary scalar Wiener--Hopf equation. The moment \(M\) must then be determined self-consistently by
\[
\boxed{
M=Q_+(0).
}
\]

Thus the Green term is a genuine rank-one perturbation of the scalar Wiener--Hopf problem.

Formally, after a factorization
\[
\mathcal D(k)=\mathcal D_+(k)\mathcal D_-(k),
\]
the solution has the structure
\[
Q_+(k)
=
\frac{1}{\mathcal D_-(k)}
\left[
\text{lower-half-plane projection of }
\frac{-ik^3/(1+ik)-\lambda M}
{\mathcal D_+(k)}
\right],
\]
up to the standard polynomial/index terms required by the factorization.

The self-consistency condition at \(k=0\) then fixes \(M\), provided the factorization is nondegenerate there.

No explicit factorization is asserted until Suzuki's exact \(\widehat g(k)\) is inserted.

## 9. Relation to the edge transfer function

On the Laplace line \(p=ik\),
\[
Q(p)=Q_+(k).
\]

The edge transfer introduced in v13.728 is
\[
\mathcal T_{\rm edge}(p)=(p+1)Q(p).
\]

Hence the exact Wiener--Hopf equation determines the nonconstant transfer through
\[
\boxed{
\mathcal T_{\rm edge}(ik)
=
(1+ik)Q_+(k).
}
\]

The source pole \(1/(1+ik)\) is removed by this definition; all remaining nontrivial analytic structure comes from

1. the factorization of
   \[
   \mathcal D(k)=k^2\widehat g(k)-\lambda;
   \]
2. the self-consistent rank-one moment \(M=Q_+(0)\);
3. the boundary/gauge normalization encoded by \(R_-\).

This is now the precise analytic object that must be compared with the Xi/theta channel.

## 10. Result

\[
\boxed{\textbf{PASS: exact compensated Wiener--Hopf equation}}
\]

\[
\boxed{
\left(\widehat g(k)-\frac{\lambda}{k^2}\right)Q_+(k)
+
\frac{\lambda Q_+(0)}{k^2}
=
-\frac{ik}{1+ik}+R_-(k).
}
\]

Equivalent pole-free form:
\[
\boxed{
[k^2\widehat g(k)-\lambda]Q_+(k)
+\lambda Q_+(0)
=
-\frac{ik^3}{1+ik}+k^2R_-(k).
}
\]

The \(-\delta_0\) boundary compensation appears exactly as the \(-1\) in
\[
(1+ik)^{-1}-1,
\]
while the half-line Green operator contributes the rank-one term
\[
\lambda Q_+(0)/k^2.
\]

Next gate: extract or reconstruct Suzuki's exact transform \(\widehat g(k)\), then factor
\[
\mathcal D(k)=k^2\widehat g(k)-\lambda
\]
and solve the scalar-plus-rank-one Wiener--Hopf system.
