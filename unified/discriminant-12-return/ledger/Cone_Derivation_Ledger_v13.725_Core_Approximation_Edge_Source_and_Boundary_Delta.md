# Cone Derivation Ledger v13.725 — Core Approximation of Suzuki Transport: Edge Source and Boundary Delta

Date: 2026-09-23

Status: explicit core-approximation computation for the right deficiency source. It identifies the distributional boundary-layer profile forced by the fact that every core derivative has zero mean. Promotion to convergence in the limiting \(H(S_{\rm edge})\) energy topology remains open.

Status labels: **[D]** exact finite-\(A\)/distributional calculation, **[C]** conditional energy-space identification, **[O]** open, **[G]** guardrail.

## 0. Synchronization and source check

Live head before this write is v13.724, commit \`e0a70610bd1180da125da058809e58b3718eb903\`.

Suzuki Section 8.3 defines
\[
H(S_A)
=
\overline{C_c^\infty(-A,A)\cap L_0^2(-A,A)}^{\|\cdot\|_{S_A}},
\]
and proves that
\[
D=i\,d/dx:
C_c^\infty(-A,A)
\to
C_c^\infty(-A,A)\cap L_0^2(-A,A)
\]
is bijective and extends to an isometric isomorphism
\[
\bar D:H(T_A)\overset{\sim}{\to}H(S_A).
\]
Suzuki explicitly warns that \(H(S_A)\not\subset L^2\) and that
\[
\bar D(1_{[-A,A]})\ne0.
\]

Therefore \(\bar D e_{+i}\) must be computed as an \(H(S_A)\)-limit of derivatives of core approximants, not by ordinary differentiation of \(e^x\).

## 1. Explicit core approximants [D]

Fix \(A>0\). Let \(\chi\in C^\infty([0,\infty))\) satisfy
\[
0\le\chi\le1,\qquad
\chi(t)=0\quad(0\le t\le1/2),
\qquad
\chi(t)=1\quad(t\ge1).
\]

For \(\varepsilon>0\), define right and left boundary cutoffs
\[
\chi^R_{\varepsilon,A}(x)
=
\chi\!\left(\frac{A-x}{\varepsilon}\right),
\qquad
\chi^L_{\varepsilon,A}(x)
=
\chi\!\left(\frac{A+x}{\varepsilon}\right),
\]
and
\[
v_{\varepsilon,A}(x)
=
e^x\chi^R_{\varepsilon,A}(x)\chi^L_{\varepsilon,A}(x).
\]

Then
\[
v_{\varepsilon,A}\in C_c^\infty(-A,A).
\]

Because \(e^x\in H(T_A)\) as a Suzuki deficiency/source vector and \(C_c^\infty(-A,A)\) is the defining form core, one may choose a vanishing sequence \(\varepsilon_n\downarrow0\) (or a standard diagonal core sequence with the same boundary profile) such that
\[
v_{\varepsilon_n,A}\to e^x
\quad\text{in }H(T_A).
\]

By definition of the isometric extension,
\[
\boxed{
\bar D e_{+i}
=
\lim_{n\to\infty}
Dv_{\varepsilon_n,A}
\quad\text{in }H(S_A).
}
\]

## 2. Exact derivative of the approximants [D]

Since \(D=i\,d/dx\),
\[
Dv_{\varepsilon,A}
=
i e^x\chi_R\chi_L
+i e^x\chi_R'\chi_L
+i e^x\chi_R\chi_L'.
\]

Here
\[
\chi_R'(x)
=
-\frac1\varepsilon
\chi'\!\left(\frac{A-x}{\varepsilon}\right),
\]
while
\[
\chi_L'(x)
=
\frac1\varepsilon
\chi'\!\left(\frac{A+x}{\varepsilon}\right).
\]

Every such derivative has exactly zero integral:
\[
\boxed{
\int_{-A}^{A}Dv_{\varepsilon,A}(x)\,dx
=
i[v_{\varepsilon,A}(A)-v_{\varepsilon,A}(-A)]
=
0.
}
\]

This zero-mean identity is the mechanism that forces a boundary correction to the naive bulk derivative \(ie^x\).

## 3. Right-edge rescaling [D]

Set
\[
x=A-\xi,
\qquad
(\mathcal E_Af)(\xi)=f(A-\xi),
\qquad
0\le\xi\le2A.
\]

Multiply by \(e^{-A}\). The right cutoff becomes
\[
\chi_R(A-\xi)=\chi(\xi/\varepsilon).
\]

For fixed \(\xi\) and large \(A\), the left cutoff equals \(1\), while its derivative is supported near \(\xi=2A\) and is suppressed after the \(e^{-A}\) normalization.

Thus the right-edge contribution is exactly
\[
\boxed{
e^{-A}\mathcal E_A(Dv_{\varepsilon,A})(\xi)
=
i e^{-\xi}
\left[
\chi(\xi/\varepsilon)
-
\frac1\varepsilon\chi'(\xi/\varepsilon)
\right]
+
R_{A,\varepsilon}(\xi),
}
\]
where \(R_{A,\varepsilon}\) is supported at the remote left edge \(\xi\approx2A\).

For compactly supported edge test functions,
\[
R_{A,\varepsilon}\to0
\qquad(A\to\infty).
\]

## 4. The boundary delta [D]

As \(\varepsilon\downarrow0\),
\[
\chi(\xi/\varepsilon)\to1
\quad(\xi>0),
\]
while
\[
\frac1\varepsilon\chi'(\xi/\varepsilon)
\rightharpoonup\delta_0
\]
on the half-line, because
\[
\int_0^\infty\frac1\varepsilon\chi'(\xi/\varepsilon)\varphi(\xi)\,d\xi
=
\int_0^\infty\chi'(t)\varphi(\varepsilon t)\,dt
\to
\varphi(0)\int_0^\infty\chi'(t)\,dt
=
\varphi(0).
\]

Since \(e^{-\xi}=1\) at the boundary,
\[
e^{-\xi}\frac1\varepsilon\chi'(\xi/\varepsilon)
\rightharpoonup\delta_0.
\]

Therefore the iterated distributional edge limit is
\[
\boxed{
F_{+,{\rm dist}}^{\rm edge}
=
i\left(e^{-\xi}-\delta_0\right).
}
\]

This profile has zero total mass:
\[
\boxed{
\int_0^\infty
\left(e^{-\xi}-\delta_0\right)
=
1-1=0,
}
\]
exactly preserving the mean-zero property of the finite core derivatives.

Thus the delta is not optional: it is the boundary compensation required by Suzuki's target core
\[
C_c^\infty(-A,A)\cap L_0^2(-A,A).
\]

## 5. Independence of cutoff shape [D]

The coefficient of \(\delta_0\) depends only on
\[
\chi(\infty)-\chi(0)=1.
\]

Hence every smooth monotone boundary cutoff with the same endpoint values produces the same distributional edge source
\[
\boxed{i(e^{-\xi}-\delta_0).}
\]

The detailed cutoff profile affects only terms vanishing in the distributional limit.

## 6. Energy-space interpretation [C/G]

The exact definition is
\[
\bar D e_{+i}
=
H(S_A)\!-\!\lim Dv_n.
\]

The calculation above proves that any compatible explicit cutoff sequence has the local right-edge **distributional** profile
\[
i(e^{-\xi}-\delta_0).
\]

To identify
\[
F_+^{\rm edge}
=
\lim_{A\to\infty}
e^{-A}\mathcal E_A(\bar D e_{+i})
\]
as an element of a limiting edge energy space, one still needs:

1. existence of the \(A\to\infty\) edge-energy limit;
2. continuity of local distributional testing under that limit;
3. membership of the boundary functional \(\delta_0\), or its equivalence class, in the dual/completion appropriate to \(S_{\rm edge}\).

Thus the source-faithful conclusion is
\[
\boxed{
F_+^{\rm edge}
=
i(e^{-\xi}-\delta_0)
}
\]
**distributionally and conditionally in the limiting energy space**.

It is not justified to replace it by \(ie^{-\xi}\).

## 7. Reflection and the left deficiency channel [D]

For \(e^{-x}\), use the left-edge coordinate
\[
\xi=A+x.
\]

The same cutoff calculation gives the reflected compensated profile, with the sign from
\[
D e^{-x}=-i e^{-x}
\]
on the interior:
\[
\boxed{
F_-^{\rm edge}
=
-i(e^{-\xi}-\delta_0)
}
\]
distributionally in its own left-edge coordinate.

Thus the two deficiency channels remain reflection partners.

## 8. Corrected edge equation [C]

Using the half-line form from v13.724,
\[
s_{\rm edge}(\xi,\eta)
=
g(\xi-\eta)-\lambda\min(\xi,\eta),
\]
the source-faithful model for the right deficiency profile is no longer
\[
S_{\rm edge}q=e^{-\xi}.
\]

It is
\[
\boxed{
S_{\rm edge}q_+
=
i(e^{-\xi}-\delta_0)
}
\]
in the distributional/energy sense, modulo the inherited constant-output gauge.

After removing the harmless channel phase \(i\), define
\[
q=S_{\rm edge}^{-1}(e^{-\xi}-\delta_0).
\]

Formally,
\[
\boxed{
\int_0^\infty
\left[
g(\xi-\eta)-\lambda\min(\xi,\eta)
\right]q(\eta)\,d\eta
=
e^{-\xi}-\delta_0+c.
}
\]

This equation must be interpreted weakly because of the boundary delta.

## 9. Interaction with the Green component [D]

The edge Neumann Green kernel satisfies
\[
K_{\rm edge}(\xi,\eta)=\min(\xi,\eta).
\]

Its action on the boundary delta is
\[
\boxed{
(K_{\rm edge}\delta_0)(\xi)
=
\min(\xi,0)=0.
}
\]

Thus the \(-\lambda K_{\rm edge}\) part does not see the boundary delta directly.

The convolution/screw part does:
\[
\boxed{
(G_{\rm edge}\delta_0)(\xi)=g(\xi).
}
\]

Therefore if \(S_{\rm edge}q=e^{-\xi}-\delta_0\), the delta enters entirely through the screw-kernel boundary response. This is a concrete, computable correction to the naive exponential forcing.

## 10. Consequence for the Suzuki--Xi identification [D/C]

The transport-source gate from v13.724 is now resolved at the distributional level:
\[
\boxed{
F_+^{\rm edge}\ne i e^{-\xi};
\qquad
F_+^{\rm edge}=i(e^{-\xi}-\delta_0).
}
\]

Hence the scalar-mode test must be replaced by
\[
\boxed{
S_{\rm edge}^{-1}(e^{-\xi}-\delta_0)
\stackrel{?}=c\,e^{-\xi}.
}
\]

If this fails, the exact modification is the edge profile
\[
q(\xi)=S_{\rm edge}^{-1}(e^{-\xi}-\delta_0),
\]
whose Laplace/theta pairings must replace the raw exponential channel factors in v13.720.

This makes the next gate both sharper and more source-faithful.

## 11. Result

\[
\boxed{
\textbf{PASS: explicit core approximants determine the universal compensated edge source}
}
\]
\[
\boxed{
F_{+,{\rm dist}}^{\rm edge}=i(e^{-\xi}-\delta_0).
}
\]

The boundary delta is forced by the exact zero-mean identity for every core derivative and is cutoff-shape independent.

\[
\boxed{
\textbf{OPEN: promotion of this distributional profile to a theorem in the limiting }H(S_{\rm edge})\textbf{ topology.}
}
\]

\[
\boxed{
\textbf{NEXT: solve/factor the weak half-line equation }
S_{\rm edge}q=e^{-\xi}-\delta_0.
}
\]
