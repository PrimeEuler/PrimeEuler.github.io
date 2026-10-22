# Gravity self-executed remaining gates: exact jump/killing identity, conditioned law, Xi non-bridge

**Date:** 2026-10-22. Parents: v14.705–722, notably the deposited EFT v3.4 (bound-survivor and killed-moment BPS corrections), v14.716 (joint process). Dedicated gravity lane, no sandbox handoffs.

## I. Source-faithful hard collision operator [D]

At instantaneous Kepler phase x=(r,v), let the physical postcollision velocity v' be distributed by the positive Rutherford/Boltzmann jump rate measure \(\nu_x(dv')\), already accounted for by the EFT's matching prescription. Define \(h'(r,v')=|v'|^2/2-\mu/r\). Let \(\mathcal B=\{h'<0\}\), \(\mathcal E=\{h'\ge0\}\), and define bounded jump-safe shape \(s'(r,v')=1-|\mathbf r\times\mathbf v'|\sqrt{-2h'}/\mu\) on \(\mathcal B\).

The **exact killed** generator, applied to any test function \(f\) with cemetery value \(f(\dagger)=0\), is
\[
(J_{\rm kill} f)(x)=\int_{\mathcal B}[f(x')-f(x)]\nu_x(dx')
-\lambda(x) f(x),\quad
\lambda(x)=\nu_x(\mathcal E).
\]
This follows algebraically from \(\int(f(x')-f(x))\nu\) with f(\dagger)=0 on escaped outcomes.

By contrast, the **censor/reject-escape, bound-preserving** jump generator is
\[
(J_{\rm cens} f)(x)=\int_{\mathcal B}[f(x')-f(x)]\nu_x(dx').
\]
Thus \(J_{\rm kill}=J_{\rm cens}-\lambda\) as multiplication operators on any test f. This is an exact Markov-generator identity, independent of the particular Rutherford kernel.

The matched generator must keep the original EFT subtraction:
\[
L_{\rm matched}=L_{\rm soft}^{\rm BPS-FP}
+J_{\rm hard}^{\rm exact}
\quad\text{(equivalently the full BPS-FP plus hard exact-minus-hard FP residual)}.
\]
Adding a full hard process to the *full* BPS-FP would double-count the hard sector. The EFT v3.4 gives **fold-local** numerical correction values, not the full tabulated \(x\mapsto \nu_x\) needed for a forward solver. The exact operator is therefore specified structurally but not implemented as a global numerical collision kernel from those local values alone.

## II. Survival normalization is an exact nonlinear selection equation [D]

Let \(p_t(x)\) be the subprobability density under the killed forward generator, \(S(t)=\int p_t\), \(\pi_t=p_t/S(t)\), and \(\bar\lambda_t=\int \lambda(x)\pi_t(x)dx\). Assume the nonkilling part L_cens is mass-preserving. Then
\[
\partial_t p=L_{\rm cens}^*p-\lambda p,\quad
S'=-S\bar\lambda,\quad
\boxed{\partial_t\pi=L_{\rm cens}^*\pi-(\lambda-\bar\lambda)\pi.}
\]
For any bounded test f,
\[
\boxed{\frac{d}{dt}\mathbb E_\pi[f]
=\mathbb E_\pi[L_{\rm cens} f]-\operatorname{Cov}_\pi(f,\lambda).}
\]
In particular for jump-safe s, the survivor drift is **not** the censored local shape drift alone: hazard-shape covariance enters. A fold-local escape hazard (EFT's \(\lambda/\mathcal K_0=0.41027\pm0.00088\) at one point) cannot yield the covariance across an ensemble or a QSD.

A QSD with decay exponent \(\kappa\) must solve \(L_{\rm kill}^*\pi=-\kappa\pi\), \(\int\pi=1\), \(\kappa=\langle\lambda\rangle_\pi\). There is no uniquely specified QSD from the current finite collection of fold coefficients; existence depends on global operator, boundary and confining properties. The high-speed joint process of v14.716 has no joint QSD, despite a survival-conditioned shape marginal; no finite-temperature BPS QSD is established.

## III. Why this does not alter Xi [D / explicit modeling boundary]

In v14.700, \(\Xi=\frac13[1-R\Phi''(R)/\Phi'(R)]\) is a ratio of derivatives of a deterministic central potential inferred from calibrated rank-1 and rank-2 torques. The bath operator above acts on Kepler orbital phase-space distributions. Neither its jump rate \(\nu_x\) nor its escape selection supplies a new \(\Phi(R)\), a rotor–bath Hamiltonian or a response kernel that changes \(\beta_1,\beta_2\). Therefore it yields **no derived correction** to Xi. Identifying the Gram witness with a torque, or using a numerical fold to alter \(\Phi\), would be an unsupported physics postulate.

A real conditional gravitational signal would require a specified source mass density/noise law, a rotor coupling Hamiltonian, and a detector estimator with a derived expectation and uncertainties. Dynamic stochastic backgrounds may enter **noise and selection**, not an automatic renormalization of the central-field slope.

## IV. Remaining obstruction, with exact requirements

The structural killed/bound-preserving operator, survival-selection identity, and the no-bridge result are resolved here. A global **numerical** BPS survivor density remains uncomputed: the archived EFT reports endpoint coefficients and local Monte Carlo estimates, not the global collision-rate kernel plus the BPS matched soft coefficient tables needed for a controlled forward evolution over energy, eccentricity and bath temperature. A high-speed/fake-diffusion absorber cannot replace them. No claim of a certified QSD or new gravity law.

No measured G is inserted. The gravity lane handles all remaining work itself. Suzuki sandbox untouched.
