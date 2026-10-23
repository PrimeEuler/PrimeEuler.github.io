# Selector v14.761 research note — action normalization obstruction and causal-fermion-system candidate

2026-10-23. Parents v14.696, v14.731–760. Independent gravity research; Suzuki sandbox reserved.

## 1. Standard field actions cannot select their own normalization [D]

Write in one consistent unit system
\[
S_{\rm EM}=-\frac{1}{4g_{\rm EM}^2}\int F_{\mu\nu}F^{\mu\nu}\sqrt{-g}\,d^4x,
\quad
S_{\rm EH}=\frac{c^3}{16\pi G}\int R\sqrt{-g}\,d^4x+S_{\rm boundary}.
\]
The EM coefficient can be moved by a field rescaling unless charge normalization / compact U(1) bundle and matter coupling are specified. The gravitational inverse coefficient already contains G. So merely evaluating these actions and calling their quadratic coefficients a,b in \(U=a\alpha_1^2+b\alpha_2^2\) is circular. For point monopoles the field energies are also UV-singular without a physical core/renormalization prescription; TN's Misner time periodicity/causality and radial boundary terms obstruct identifying a finite and universally positive gravimagnetic susceptibility by assertion.

At a finite radial cutoff r0, classical static Maxwell energy scales as \(E_{\rm field}\propto q^2/r_0\); no fixed r0 follows from the shared angular charge-monopole worldline algebra. The gravity action of the NUT sector is not a second positive Maxwell energy with a known universal matching coefficient. Thus **the requested a,b have not been determined from Maxwell + Einstein–Hilbert alone**. This is a structural non-identifiability result, not a failure of the angular unification.

## 2. Causal fermion systems (CFS): possible upstream coefficient generator [literature-based model]

The CFS causal action is variational in an operator-valued measure. In suitable continuum limits its effective field equations include gauge interactions and gravity. Finster's monograph states gauge coupling constants depend on regularization choices; related CFS analyses explain gravitational weakness via Newton's constant scaling quadratically with a microscopic regularization length, unlike corresponding gauge couplings. A 2026 continuum-limit paper extends Einstein–Dirac recovery to globally hyperbolic curved spacetimes. Sources:
- https://causal-fermion-system.com/cfs.pdf
- https://epub.uni-regensburg.de/53613/1/Finster_2022_Class._Quantum_Grav._39_165005.pdf
- https://link.springer.com/article/10.1007/s11005-026-02168-3
- https://causal-fermion-system.com/faq/

A **toy dimensional matching**, not a derived CFS formula, is
\[
G_{\rm eff}=c_g\,\frac{c^3\ell_{\rm reg}^2}{\hbar},\qquad
\alpha_{\rm EM}=c_e,
\]
with positive dimensionless effective coefficients \(c_g,c_e\) that may depend on microscopic regularization, fermionic sector and chosen minimizer. Then for particle mass \(\mu\),
\[
\alpha_G(\mu)=\frac{G_{\rm eff}\mu^2}{\hbar c}
=c_g\big(\frac{\mu c\ell_{\rm reg}}{\hbar}\big)^2,\quad
\frac{\alpha_{\rm EM}}{\alpha_G(\mu)}
=\frac{c_e}{c_g}\big(\frac{\hbar}{\mu c\ell_{\rm reg}}\big)^2.
\]
This cleanly identifies a hierarchy-generating dimensionless scale ratio *if* a separate causal-action minimization predicts \(\ell_{\rm reg}\) and \(c_e/c_g\). Otherwise it just rewrites the observed hierarchy in microscopic parameters. Different \(\mu\) give different \(\alpha_G\), so an elemental reference species must be stated.

The potential \(U(\psi)=A e^{2\psi}+B e^{-2\psi}\) of v14.760 is **not derived by CFS**. One would need to construct a CFS family \(\rho_\psi\) respecting the monopole pair lattice, compute the regularized causal action \(S_{\rm CFS}[\rho_\psi]\), and show the second variation produces finite, regulator-independent, non-circular \(A,B\). No map from a Taub–NUT (typically non-globally-hyperbolic with periodic time) spacetime to a CFS minimizer is currently supplied by the cited globally hyperbolic construction.

## 3. Selector test contract

- Specify an admissible CFS vacuum measure or family parameterized by \(\psi\) and an EM/NUT bundle embedding, without inserting measured G or alpha into the target.
- Derive both response coefficients from the *same* causal action and the same UV regularization; check dependence on scheme and constraints.
- If coefficients vary with \(\ell_{\rm reg}\), supply a separate dynamical or boundary equation fixing that length/ratio; a free UV scale is not a prediction.
- Establish a well-posed causal domain or explicitly avoid periodic-time TN background by using a local weak-field gravitomagnetic approximation before claiming an actual global NUT sector.
- Predict one independent observable (e.g. angular scattering response or RG flow) with stated input count.

**Outcome:** standard field actions alone = selector NOT obtained, normalization circular; CFS = promising conditional mechanism for a relative coupling scale, with a currently missing minimizer/regularization matching calculation. Quantized dyon pair product is intact and G-free; no G derived, no field unification, no new Suzuki sandbox work.
