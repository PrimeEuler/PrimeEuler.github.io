# Cone Derivation Ledger v15.722 — Gravity: exact source-conditioned retarded K4 vector and tensor Weyl transients

**Date:** 2026-11-11 US Eastern. **Parents:** v14.928 EH+K4 sourced TT tensor action, v14.935 original constrained vector action, v15.716–717 conserved tilted FLRW stress, v15.720 source-history scalar Weyl, v15.721 common-source vector and tensor particular Weyl. **Classification:** [D] exact coasting source-driven vector/tensor Euler solutions with zero dynamical initial data; [D] nonzero electric vector and tensor Weyl for transient solutions; [N] v15.721 electric-vector null is not a universal selection rule; [O] smooth physically localized source, finite-bandwidth detector, canonical source normalization, full coupled three-mode measurement. **Immediately prewrite HEAD:** 22fffe7e497550ff2412574b08abed83bc492fa9; v15.722 ledger target absent, additive-only; protected Suzuki and existing certificates untouched.

## Gate 338 — general retarded coasting vector Green function

With the original v14.935 vector action sourced *before* eliminating B_v (v15.710 and v15.721), define **D=4+3k²** and the conserved-source shear component **Q=Q0_zy** for comoving k>0. The forced coasting vector displacement equation is

**f_ddot+(3/tau)f_dot + beta_V f/tau² = -2 i Q/(k tau²)**,

**beta_V=2eta D/3**, **nu_V²=beta_V-1>0** on eta>3/8 and k>0.

The Euler operator retarded Green kernel is the same general geometric form as the scalar result v15.714 but with its own frequency **nu_V**:

**G_V(tau,sigma)= sigma² sin[nu_V log(tau/sigma)]/(nu_V tau)** for tau>sigma, zero before. The source-specific constant particular displacement is

**f_part=-3 i Q/(eta k D)**.

When the source is present from an initial slice tau0 and the *dynamical displacement* satisfies **f(tau0)=f_dot(tau0)=0**, the exact source-conditioned solution is

**f(tau)=f_part {1-(tau0/tau)[cos(nu_V log(tau/tau0))+(1/nu_V)sin(nu_V log(tau/tau0))]}**.

Direct symbolic differentiation checks the ODE and both initial conditions. The time dependence is logarithmic with a tau^-1 homogeneous envelope. The associated nondynamical shift is

**B_v(tau)=b_v(tau) f_dot(tau)-J_v(tau)/A_v(tau)**,

**b_v=4tau/[sqrt(3)D]**, **J_v=i k tau Q/6**, **A_v=tau D/(6sqrt(3))**.

The latter source-contact contribution is constant in conformal time, whereas the f_dot term is transient and generically time-dependent.

## Gate 339 — electric Weyl reappears for the transient vector response

v15.721 independently computed the local orthonormal electric and magnetic Weyl tensor from the conformal vector metric perturbation h_(chi y)=-B_v:

**E^(Weyl,V)_(yz)=-i k B_v_dot/(4a)**,

**C_(0z yz)^(orth)=-k² B_v/(4a²)**,

with a=tau/sqrt(3). Therefore electric Weyl vanishes only if **B_v_dot=0**, as for the steady particular source response. It is **not generally zero** for the retarded vector solution.

For the specified zero-displacement/velocity initial slice, exact substitution of the vector dispersion relation gives the finite one-sided post-onset value

**E^(Weyl,V)_(yz)(tau0+)=-2Q/[D tau0²]**,

provided the source is treated as present on tau>=tau0. This is nonzero for a generic tilted source component Q, and proportional to the same undetermined stress amplitude; a real field uses conjugate Fourier pairs.

**Sharp switch-on caveat:** the algebraic source-to-shift contact term may jump across an ideal abrupt source-on boundary. The formula above is the finite post-onset transient, not the distributional impulse at tau0. A truly physical source must be smoothly prepared and covariantly conserved through the switch-on, which was not modeled here. Smoothing changes the early transient amplitudes without changing the conclusion that time-dependent vector motion supports electric Weyl.

## Gate 340 — matching zero-data tensor retarded response

For the same conserved source's TT stress component Q_T and the sourced tensor action of v14.928,

**gamma_ddot+3 gamma_dot/tau + beta_T gamma/tau²=-2kappa Q_T/tau²**,

**beta_T=3k²+8eta/3**, **nu_T²=beta_T-1>0** in the examined interval.

The particular tensor amplitude is **gamma_part=-2kappa Q_T/beta_T**. The exact solution with gamma(tau0)=gamma_dot(tau0)=0 is

**gamma(tau)=gamma_part {1-(tau0/tau)[cos(nu_T log(tau/tau0))+(1/nu_T)sin(nu_T log(tau/tau0))]}**.

Direct substitution reproduces the sourced ODE, zero initial data and the conformal TT electric Weyl:

**E^(Weyl,T)_(xx)=[tau² gamma_ddot+tau gamma_dot-3k² gamma]/(12a²)**

for plus polarization in the stated curvature convention, with the yy component of opposite sign and corresponding cross term. At the same one-sided initial slice,

**E^(Weyl,T)_(xx)(tau0+)=-kappa Q_T/[6a(tau0)²]**, generically nonzero.

## Gate 341 — corrected scope of the three-mode detector discussion

**[D]** The scalar source-to-curvature transfer was derived in v15.719–720; source-driven tensor and vector particular transfers were derived in v15.721; this gate now confirms their *retarded transient* electric-Weyl responses are generically nonzero in both vector and tensor channels. Consequently, the previous vector-electric null is **specific to the time-independent conformal-shift particular solution**, not a permanent representation or gauge-invariance selection rule.

**[N]** None of this makes the v15.706 pole-gap ratio 3 a source-independent *measured* three-peak signal. Three spectral responses may have orientation-dependent residues, different preparation histories, different damping and potentially inaccessible detectors. Moreover the exact ratio 3 comes from standard coasting isotropic relativistic elasticity (Carter comparator), rather than a distinct Cone quarter-grid coupling. The scalar/tensor/vector source templates still lack a specified positive-energy localized matter action and experimentally calibrated detector.

**Reproducibility:** research-notes/k4_vector_retarded_electric_v15_722.py, additive commit 22fffe7e497550ff2412574b08abed83bc492fa9. Independently executed locally to PASS on vector and tensor Euler ODEs, zero displacement/velocity initial conditions, source-frequency compatibility, nonzero post-onset electric-Weyl components and tensor conformal Weyl sign/normalization. No images, no protected file changes.

**HANDOFF:** independent audit/gravity: inspect v15.721–722 and the audited v14.928/v14.935 source actions; verify the transverse momentum source phase, shift contact, conformal Weyl component conversion, tensor sourcing sign, initial-slice one-sided limits and distinction between electric and magnetic Weyl. Do not treat discontinuous source switch-on as a physical compact matter model.

**NEXT:** require a smooth covariantly conserved finite-duration source (including stress density and momentum continuity) before inferring experimentally usable spectral residues; next compare actual **source-to-curvature Green functions** for all T/V/S modes at a common k, including angular nulls. Demand an observable that distinguishes Cone from ordinary relativistic elasticity, rather than relabeling the same three-wave-speed relation.
