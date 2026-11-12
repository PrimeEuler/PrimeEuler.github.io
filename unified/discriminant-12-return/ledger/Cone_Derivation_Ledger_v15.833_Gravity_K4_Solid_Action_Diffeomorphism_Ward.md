# Cone Derivation Ledger v15.833 — Gravity: frozen K4 solid action, material-coordinate gauge transformation and full linear Einstein–solid pure-gauge Ward

**Date:** 2026-11-12 US Eastern. **Parents:** v14.935 exact K4 Einstein–Hilbert plus relativistic elastic-solid action and coasting solution; v15.815–818 independently audited five-helicity matter-to-optical chain; v15.821–822 event-anchored photon/clock; v15.830–831 generalized 3D optical pure-gauge null; v15.832 canonical spectator gauge-order control. **Live HEAD immediately prewrite:** 7a7c111a859ce8bc66df202fa1a0573b7b0a6aeb; destination absent. Strict additive-only; certified Suzuki objects preserved.

**Status:** [D] action-level and stress-tensor gauge Ward for K4 **solid background** in arbitrary 3D infinitesimal coordinate shifts with nontrivial time dependence, including all ten covariant stress entries; [D] pure-gauge solution of the full linearized Einstein+solid field equations by diffeomorphism covariance on the exact coasting background; [N] no new Cone-specific force or mass gap; [O] componentwise off-shell ADM constraint/intertwiner, complete all-gauge optical source-to-detector with transformed dynamical initial data and remote receiver.

## Gate 456 — take the actual archived solid action seriously

The exact frozen action, in the original v14.935 (+---) signature, is

**S=∫sqrt(-g)[R/(2κ)−C b^(2/3)(1+η_s J)]d⁴x**,

**B^IJ=−g^μν ∂μφ^I∂νφ^J**, **b=sqrt(det B)**,
**J=tr(B²)/(tr B)²−1/3**.

In an equivalent (−+++) conformal metric convention the minus sign defining B is absent, with the action matter density otherwise unchanged. Background **φ^I=x^I**, **a(τ)=τ/sqrt3**, **κC=1**. In conformal time **a(η)=a0 exp(ℋη)**, with **ℋ=1/sqrt3**, **3ℋ²=κC**, background ρ=C/a², p=−ρ/3. The isotropic elastic J vanishes on the background, and the local physical sound-speed parameter η_s is distinct from conformal time η.

For an arbitrary infinitesimal *passive* coordinate shift

**η_new=η+T(η,x)**, **x_new^i=x^i+U^i(η,x)**,

the background solid's physical scalar material labels must transform:

**π^I=δφ^I=−U^I**.

The gauge-generated metric in the conformal (−+++) notation is

**Φ=−T'−ℋT**, **V_i=U_i'−∂_iT**,
**h_ij=−2ℋTδij−∂_iU_j−∂_jU_i**,

where g00=−a²(1+2Φ), g0i=−a² V_i and gij=a²(δij+hij). Spatial shear must be kept; it is not a new source.

## Gate 457 — tracefree internal elastic strain cancels exactly

For the material metric B evaluated to first perturbative order on the background, define the dimensionless matrix **E^IJ=a² δB^IJ**. Directly from the solid material gradients,

**E_ij=−h_ij+∂_iπ_j+∂_jπ_i**.

Substitute π=−U and the full gauge-generated h:

**E_ij=+2ℋTδij**.

Therefore **E_TF=E−(trE/3)I=0** exactly for arbitrary T and U. The initial isotropic state does change under time slicing, as it must: **δb/b=(tr E)/2=3ℋT**, **δρ/ρ=(2/3)δb/b=2ℋT**. This is a shift in the coordinate description of the evolving background density, not a new elastic deformation.

A direct expansion of the frozen invariant gives

**J^(2)=tr(E_TF²)/9**,

so **J^(2)=0** along the entire pure-diffeomorphism direction. A pure coordinate shear cannot create an actual elastic anisotropy if the solid material coordinates transform together with the metric.

## Gate 458 — the full K4 solid action density changes only by a boundary divergence

At the coasting conformal background the matter Lagrangian density is **ℒ0=−Ca²**. Its metric-volume perturbation is **δsqrt(−g)/sqrt(−g)=Φ+trh/2**. Its material density perturbation obeys **δ(b^(2/3))/b^(2/3)=tr E/3=2ℋT**. Therefore

**δℒ_m/ℒ0=Φ+trh/2+trE/3=−T'−div U−2ℋT**.

Because **ℒ0'/ℒ0=2ℋ**, this is

**δℒ_m=−∂_μ(ξ^μ ℒ0)**, with ξ=(T,U).

Hence the actual K4 solid action is invariant up to the standard coordinate-boundary term. No freely chosen extra elastic/coupling term is needed. The Einstein–Hilbert part shares ordinary diffeomorphism invariance.

## Gate 459 — ten stress components and the linearized on-shell Einstein–solid Ward

At this background, the covariant solid stress tensor, in the same (−+++) convention, simplifies to the **constant** conformal-coordinate matrix

**T^(0)_μν=diag(C,−C/3,−C/3,−C/3)**.

The pure-gauge stress first-order variation calculated from the solid fluid limit and the phonon is

**δT00=−2C T'**,

**δT0i=−C∂iT+(C/3)U_i'**,

**δTij=(C/3)(∂i U_j+∂j U_i)**,

exactly the ten components of **δT_μν=−ℒ_ξ T^(0)_μν**. These identities include the solid's momentum response; omitting π=−U would spoil them.

The background Einstein tensor is **G^(0)_μν=diag(3ℋ²,−ℋ²,−ℋ²,−ℋ²)** and the exact coasting Einstein equation says **3ℋ²=κC**, giving **G^(0)_μν=κT^(0)_μν**.

Diffeomorphism covariance of the original Einstein–solid field equations therefore implies for the *full gauge-generated metric and solid field perturbations*

**δ(G_μν−κT_μν)=−ℒ_ξ (G^(0)_μν−κT^(0)_μν)=0**.

This proves the full linearized equations admit arbitrary pure-gauge solutions on the exact background. It is a covariance/Noether Ward result, **not** a separate componentwise direct integration of all gauge-dependent ADM scalar/vector constraints or a gauge-invariance proof for arbitrary physical source solutions and gauge-preparation choices. Crucially, a solid-background perturbation of the same order as the metric is required; unlike the zero-background spectator stress in v15.832, the solid cannot be frozen in the gauge overlay.

## Gate 460 — reproducibility, limitation, and novel-physics null

The new additive symbolic reproducer checks arbitrary three-component U and arbitrary T as symbolic 3D+time functions: exact E matrix, tracefree J zero, full action-density divergence, ten stress Lie-derivative entries, the linearized Einstein–solid pure-gauge Ward and a concrete nonzero false shear when π is improperly held zero.

**Reproducer:** research-notes/k4_solid_gauge_action_v15_833.py, commit **1e62f92fadb3a4c78a7177444f2cf8438661cee1**. Equivalent local SymPy implementation executed PASS; the committed file has not yet been independently externally reexecuted. The distinct false elastic gradient energy is recorded in v15.834. No historical files modified, no images generated.

**HANDOFF — external audit:** reexecute the exact committed SymPy v15.833 and independently confirm the original v14.935 B, b, J action/signature translation; scalar material-field transformation π=−U; matter stress Lie derivative including δT0i; on-shell Einstein normalization and that the original full scalar/vector/TT constraints accept pure-gauge modes. Audit the conditional scope of the covariance identity and avoid promoting it to a new physics detection.

**NEXT:** use the material-coordinates gauge-invariant strain and a fully event-anchored optical observable to test explicit nontrivial physical source solutions under arbitrary full metric/solid gauge transformations; then investigate remote detector geometry. The independently audited exact matched ordinary GR+relativistic elastic solid result remains **no Cone-specific residual**.
