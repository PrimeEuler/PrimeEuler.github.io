# Cone Derivation Ledger v15.702 — Gravity: invariant Kaluza–Klein minimal coupling preserves fiber winding

**Date:** 2026-11-11 US Eastern. **Parents:** v15.647 actual invariant Taub–NUT Dirac/KY operators preserve fiber charge; v15.696 charge-one source selection and global bundle caveat; v15.701 Hopf two-component unit-Chern carrier and audited v15.695 script repair. **Status:** [D] exact scalar local invariant KK wave-operator reduction and selection rule; [C] relevance as a local model for invariant Taub–NUT geometry; [N] no source-selected charge-one transition or amplitude; [O] complete globally patched, physical, non-invariant Taub–NUT spinor/metric interaction. **Immediately prewrite live HEAD:** ca193e760a873ec291011c5d8c196012e38d9402. Target v15.702 ledger path not present. Additive-only; Suzuki/far-tail objects untouched.

## Gate 274 — metric-derived minimal connection carries gauge charge but does not raise it

Take a standard local Kaluza–Klein base/fiber metric

**ds²=dx²+R²(dpsi+A(x)dx)²**, with R>0, periodic psi, and psi-independent A.

In (x,psi) coordinates its exact metric and inverse are

**g=[[1+R² A², R² A],[R² A,R²]], det g=R²**,

**g^(-1)=[[1,-A],[-A,A²+R^(-2)]].**

The natural scalar Laplace–Beltrami operator with this constant R is

**Delta phi = partial_x(g^xx partial_x phi+g^(x psi) partial_psi phi)
            + partial_psi(g^(psi x) partial_x phi+g^(psi psi) partial_psi phi)**.

For a fiber Fourier mode **phi=f_k(x) exp(i k psi)** it reduces exactly to

**Delta phi = exp(i k psi)[(partial_x-i k A)^2 f_k-(k²/R²) f_k]**,

where the square includes the derivative of A. This is conventional U(1) minimal coupling of the k-th *fixed* Fourier sector to a gauge potential A, with no transition between k sectors. The KK gauge-charge coefficient k is fixed by Fourier geometry; it is not a transition amplitude.

## Gate 275 — conserved Fourier winding is a symmetry selection rule of the covariant operator

Because all metric coefficients are independent of psi, the Killing generator **P=-i partial_psi** commutes with the natural scalar operator: **[P,Delta]=0**. Fourier orthogonality

**integral_0^(2pi) exp[i(k-k')psi] dpsi=2pi delta_(k,k')**

makes all off-diagonal k→k' matrix elements vanish. The exact reproducer checks k,k' from -6 to 6 along with the symbolic metric and Laplacian.

This reproduces in a strictly source-derived, rather than postulated, geometric setting the k-preservation conclusion of v15.647 for actual invariant Dirac/KY symmetries. It does not claim to have derived the full four-dimensional Taub–NUT Dirac equation, Euclidean-to-Lorentzian continuation or spin connection; those require separate global analysis. The common symmetry mechanism is already decisive for this restricted invariant background.

## Gate 276 — distinction between ordinary gauge coupling and a physical quarter-rung source

In a fiber-invariant metric, the connection A gives a physically meaningful gauge covariant derivative **D_x=partial_x-i k A**. Its nonzero coupling to the k-th mode must not be confused with a charge-raising interaction. It has charge zero under the fiber generator, rather than q=+1.

To obtain **k→k+1**, the interaction must have a genuine psi-dependent Fourier component of charge +1, as v15.696 showed. A globally valid field realizing that component must transform as a degree-one bundle coefficient on patch overlaps, for which v15.701 provides a two-component geometrical example. Neither the invariant KK metric nor its natural wave operator forces such a non-invariant field to exist, become excited or couple with a chosen magnitude.

Thus standard minimal coupling is not the missing Cone charge-changing source.

## Gate 277 — close the automatic Hopf-to-dynamics shortcut

The combined source-first chain establishes:

**[D]** A compatible global unit-Chern charged *carrier* is available (v15.701).

**[D]** An invariant metric-derived KK wave operator acts diagonally in fiber winding (this gate).

**[D]** A k→k+1 perturbation needs a degree-one charged source, and its amplitude is not set by the topological integer (v15.696).

**[N]** The Hopf carrier does not automatically generate a k-changing term in the actual invariant geometric dynamics. No unique Cone gravitational coupling, observed gravitational spinor transition or G-free tidal observable follows from it.

**NEXT:** preserve the topological charged-carrier construction as a conditional lead. Before pursuing a spinor-source extension, require a concrete independent physical action and field matter content that explicitly breaks or transfers fiber charge with globally correct patching, together with a normalization sourced from its kinetic and interaction terms. If no existing independently motivated action supplies that input, do not manufacture arbitrary Yukawa couplings to claim success. Resume the separately standing rank-1/rank-2 rotor-to-tidal response program, where any proposed dimensionless observable must first pass angular-momentum and standard GR symmetry controls.

**Reproducibility:** research-notes/invariant_kk_minimal_source_v15_702.py, additive commit ca193e760a873ec291011c5d8c196012e38d9402. It independently verifies the metric inverse/determinant, complete scalar Laplacian with the derivative-of-A term, and Fourier orthogonality for integer charges. Locally executed PASS; no image generation, no certified/Suzuki modifications.

**HANDOFF:** external audit/gravity/sandbox: confirm the exact KK inverse and scalar Laplacian, no overlooked k-changing term for a psi-independent metric, and the stated limitation that this is a local invariant scalar example rather than a complete Taub–NUT spinor computation. Check whether an independent physically specified non-invariant source in older papers already exists before authorizing any new sourced-field gate.
