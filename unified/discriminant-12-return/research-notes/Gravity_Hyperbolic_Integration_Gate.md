# Cone gravity: the hyperbolic integration gate

Date: 2026-10-23. Parents v14.592, v14.696, v14.731–761. This is a testable **proposed integration dictionary**, not yet the unique integration of the established Cone phase state. No Suzuki sandbox use.

## 1. Circular versus hyperbolic integral [D, classical]

On a compact circle the Fourier kernel obeys
\[
i^m J_m(z)=\frac1{2\pi}\int_0^{2\pi}e^{iz\cos\theta-im\theta}\,d\theta
\quad(m\in\mathbb Z).
\]
On a boost orbit \((X,Y)=(a\cosh u,a\sinh u)\) the invariant rapidity measure is du and the convergent even kernel is
\[
\boxed{K_\nu(z)=\int_0^\infty e^{-z\cosh u}\cosh(\nu u)\,du},\quad z>0
\]
with the usual restrictions on branches/order. The noncompact transform is of modified Bessel K type, not an automatically quantized circular Fourier mode. Physically z requires an action, scale or regulator; it cannot be fixed by replacing cos with cosh in an integral.

At order 0,
\[
K_0(z)=-\log(z/2)-\gamma+O(z^2|\log z|).
\]
Its logarithm has the same broad separatrix type as the elliptic-period K(e)~(1/2)log(16/(1−e²)) but is **not equal to that elliptic integral** without an explicitly derived z(e) dictionary. Picking z by solving K0(z)=the target hierarchy is fitting a free variable, not selection.

## 2. Hyperbolic base and compact monopole fiber [D]

On the hyperbolic plane of curvature −1/a², with spatial metric
\[
ds_{H^2}^2=a^2(du^2+\sinh^2u\,d\phi^2),
\]
the area form is \(\omega=a^2\sinh u\,du\wedge d\phi\). A natural local U(1) connection is
\[
\mathcal A=p(\cosh u-1)\,d\phi,\qquad
\mathcal F=d\mathcal A=p\sinh u\,du\wedge d\phi.
\]
Its flux through a hyperbolic disk of radius U is
\[
\int_{D_U}\mathcal F=2\pi p(\cosh U-1).
\]
This depends on U continuously. A disk is not a nontrivial closed 2-cycle: **there is no Dirac-type integer flux condition on a single disk**. Quantized first Chern class requires a compact cycle/global bundle, e.g. a closed quotient of H² with specified topology and \(\int\mathcal F/(2\pi)\in\mathbb Z\). Whether such a quotient is the user's physical Cone geometry is unknown.

A causal extension with noncompact τ and spacelike compact fiber ϑ is
\[
ds^2=-N^2d\tau^2+a^2(du^2+\sinh^2u\,d\phi^2)+L^2(d\vartheta+\mathcal A)^2.
\]
With N>0, a,L positive and time-independent complete spatial metric, the product-static spacetime is globally hyperbolic under standard completeness assumptions; this is **not** the original periodically identified timelike Taub–NUT. The fiber holonomy and field equations require their own derivation.

## 3. Selector test [OPEN]

One may define a regularized boost kernel \(Z(z,\psi)\) from an actual causal/worldline action and derive \(V_{\mathrm eff}(\psi)=-\log Z\) or a causal-action Hessian. But the free boost rapidity integration by itself does not produce a physical \(\psi_*\): convergence scale z, fiber curvature p, geometry a,L, measure and admissible cycles are still external parameters. To claim selection, derive all these from the same action plus independently specified constraints, show stationarity/positive Hessian and regulator/gauge robustness, and obtain a non-circular observable independent of measured alpha/G.

**Next exact calculation:** integrate a physically sourced \(\psi\)-dependent hyperbolic kernel and compute the resulting first/second derivatives; test whether reflection symmetry inevitably gives ψ=0 or whether global fiber holonomy provides noninserted asymmetry. Keep compact angular period and noncompact hyperbolic heat kernel distinct.

Verdict: hyperbolic integration transform + flux geometry **constructed**; identification with Cone state and coupling selector **open**. G_derived=false; no new EM-gravity field law; Suzuki sandbox reserved.
