# Cone Derivation Ledger v15.787 — Gravity: full scalar/vector/tensor local Fermi electric Riemann from the original sourced metric

**Date:** 2026-11-12 US Eastern. **Parents:** original K4 Einstein–Hilbert+ordinary isotropic relativistic solid v14.928/935; traceful-source Bardeen potentials v15.727–729; v15.730 independently audited on-shell canonical spectator; v15.750 independently audited compact evolving positive-energy matter; v15.760 Weyl-only three-arm reconstruction, Ricci obstruction and exact matched-action GR+solid null; v15.761 independently audited nonzero spectator Ricci shear. **Audit:** External Audit Round 549 verified v15.760–761 and their no-novelty comparator, while later audits through Round 556 focused on Suzuki. **Immediately prewrite HEAD:** 0746838a80ac4e9b816b397213e95eeed2ed3bb9, and proposed v15.787 ledger target did not exist. Additive only, preserved Suzuki/far-tail assets.

**Status:** [D] exact linear full scalar/vector/tensor electric Riemann tensor on coasting FLRW by direct independent Christoffel-to-curvature calculation, rather than Weyl-only substitution; [D] exact tracefree Ricci completion for scalar, nonzero local full electric vector tide even if electric Weyl vanishes for constant conformal shift; [D] exact canonical matter source benchmark with full-versus-Weyl numerical difference; [N] novelty under matched Einstein–Hilbert+solid comparator; [O] real finite-distance retarded metric/geodesic/laser interferometry and independently selected new Cone operator.

## Gate 397 — actual local freely falling Fermi geodesic deviation from the metric

For the coasting background **ds²=−dτ²+a(τ)² δ_ij dx^i dx^j**, **a(τ)=τ/√3**, we have **a''=0**. Therefore the background local electric Riemann components **R^(i)_(0j0)=0** in a comoving orthonormal frame. Perturbatively, at linear order in the metric mode, tetrad and basis corrections to this particular electric background component vanish; the full metric perturbation's local **R^(i)_(0j0)** is obtained directly from the first-order Christoffels/Riemann, not inferred from a Weyl-only detector approximation. At leading order in small Fermi arm separation L, **d²ξ^i/dT²=−R^(i)_(0j0) ξ^j**, and differential arm acceleration is **−L D^(ij)R_(0i0j)** for tracefree D=uu^T−vv^T. Large-arm light propagation and finite-separation corrections are not included.

Take scalar Newtonian-gauge perturbations **g00=−1−2Φ_N(τ)e^(ikz)**, **gij=a²[1−2Ψ_N(τ)e^(ikz)]δij**. Define

**A(τ)=Ψ_N''+(2/τ)Ψ_N'+Φ_N'/τ**.

Direct four-dimensional perturbed Riemann calculation yields the exact linear electric matrix in a local (x,y,z) frame:

**R^(i)_(0j0)=A δ_ij−[k² Φ_N/a²] zhat_i zhat_j**.

Its tracefree piece is

**R^(electric,STF)_ij=−[k² Φ_N/a²]Q_ij**,

**Q_ij=zhat_i zhat_j−δij/3**, **Q:Q=2/3**.

Thus the measured tracefree *full tidal* coefficient depends directly on **Φ_N**, not just on the Weyl combination **Φ_N+Ψ_N**. The isotropic part A−k²Φ_N/(3a²) is also present in individual-arm accelerations and does not cancel unless the detector arrangement is tracefree.

## Gate 398 — exact algebraic Weyl/Ricci completion

The already audited scalar electric Weyl curvature is

**E^W_ij=W Q_ij**, **W=k²(Φ_N+Ψ_N)/(2a²)**.

In four-dimensional signature (−+++) the tracefree local electric Riemann is related to Weyl and Ricci by

**R^(electric,STF)_ij=E^W_ij−(1/2)R^(spatial,STF)_ij**.

For these scalar metric modes, computing directly from the *same metric* gives the equivalent spatial Ricci tracefree coefficient

**R^(spatial,STF)_ij=[k²(3Φ_N+Ψ_N)/(a²)]Q_ij**,

so that

**−k²Φ_N Q/a² = [k²(Φ_N+Ψ_N)/(2a²)]Q − [k²(3Φ_N+Ψ_N)/(2a²)]Q**.

This explicitly completes the v15.760–761 anisotropic Ricci warning at the **total metric curvature level**, without separately postulating a spectator-only Ricci correction. Under Einstein's equations it implicitly contains all consistent matter and K4-solid stress at this order. This does NOT amount to an independently reconstructed matter-plus-solid constitutive stress tensor: that remains a separate audit/control.

## Gate 399 — vector and tensor full electric Riemann differ from Weyl-only readouts

For the transverse vector shift mode **g0y=−a B_V(τ)e^(ikz)**, with other vector metric perturbations set to zero in the archived gauge, direct linear Riemann gives

**R^(y)_(0z0)=R^(z)_(0y0)=−ik[B_V'+B_V/τ]/(2a)**.

The previously audited vector *electric Weyl* is **E^W_yz=−ik B_V'/(4a)**. Hence if B_V is constant in cosmic time (the v15.721 source-conditioned particular example), the vector electric Weyl vanishes but the full Fermi-frame electric Riemann vector component remains **−ikB_V/(2aτ) ≠0** for k B_V≠0. Thus a Weyl-only vector cancellation is emphatically *not* a physical full local tidal null.

For tensor plus polarization with **gxx=a²[1+γ_T(τ)e^(ikz)]**, **gyy=a²[1−γ_T(τ)e^(ikz)]**, the full electric Riemann tracefree components are

**R^(x)_(0x0)=−(γ_T''+2γ_T'/τ)/2**, **R^(y)_(0y0)=+(γ_T''+2γ_T'/τ)/2**.

These have the conventional local geodesic-deviation form and generally differ from electric Weyl-only tensor amplitudes. Their complete physical amplitudes follow when inserting the source-driven γ_T and B_V of v15.750; this gate establishes the curvature transfer **exactly**, but does not yet recompute the entire three-sector wavepacket numerical time history in these new variables.

## Gate 400 — exact positive-energy canonical benchmark, full tide versus Weyl

Use independently audited v15.730 physical on-shell two-plane-wave canonical matter scalar source, at τ=1, |K|²=5, with its constraint-sourced Bardeen values

**Φ_N=191/1800**, **Ψ_N=−1/72**, **a²=1/3**.

The actual scalar full-electric-Riemann STF coefficient is

**R_STF=−k² Φ_N/a²=−191/120≈−1.5916666667**,

while the electric Weyl-only coefficient is

**W=+83/120≈+0.6916666667**.

The difference is large, and their signs even differ, because the **full spatial Ricci STF** is

**R_spatial,STF = (137/30) Q**,

which contributes **−137/60 Q** to full electric Riemann. Exact check:

**−191/120 = +83/120 − 137/60**.

This is the *complete metric-inferred Ricci* coefficient for the given canonical source and K4 action, not the previously isolated **spectator-only** Ricci term of v15.761; subtracting that term from the total would leave the K4 elastic/metric Ricci sector and needs its own further derivation. All quoted coefficients refer to a single complex Fourier component, with the source amplitude and normalization of v15.730. Physical real fields require ±K pairing.

For an equal-arm local tracefree gradiometer **D=zhat zhat^T−xhat xhat^T**, **D:Q=1**, so the leading differential *acceleration per separation* is **−R_STF=+191/120** in the model/Fourier convention, **not** **−W=−83/120**. This is not an SI acceleration measurement or calibrated radiation signal.

## Gate 401 — no-novelty comparator and next falsification criterion

The **exact matched-action null** independently audited at v15.760 remains unchanged: the K4 sector used here was literally derived from Einstein–Hilbert plus an ordinary relativistic isotropic-solid matter action. A conventional GR+same-solid comparator with identical background, coefficients, source, boundary data and Fermi detector functional yields *the same entire metric* and therefore *the same full Riemann tensor*. No parameter-free Cone-only residual is created by the Ricci completion.

The mathematical achievement is to repair a potentially serious observational misidentification: three nonzero Weyl channels at v15.750 are not the complete local tidal readout, and even an electric-Weyl null need not be a full-Riemann null.

**Reproducer:** research-notes/k4_full_fermi_riemann_v15_787.py, additive commit **0746838a80ac4e9b816b397213e95eeed2ed3bb9**; locally executed PASS via explicit first-order matrix-inverse, all Christoffels and Riemann curvature for the scalar, vector and tensor metric perturbations; exact canonical benchmark and Ricci completion. No image generator; no modification of certified content.

**HANDOFF — external audit:** independently derive the full 4D R^i_(0j0) from FLRW scalar/vector/tensor perturbed metrics and verify all signs, spatial orthonormal normalization, Einstein Ricci shear relation and v15.730 canonical source amplitude. Verify the vector nonzero full tide for constant B and check v15.721–722 normalization consistency. Distinguish Fermi local geodesic-deviation **leading arm** from full finite-baseline light propagation and actual detector noise/reception. Avoid claiming the matched-action null as a no-go theorem for all possible future Cone actions.

**NEXT:** feed the **same v15.750 source-driven compact evolving matter** into these full-Riemann scalar/vector/tensor transfer formulas and report time-resolved three-arm *full* tidal accelerations, separating Weyl and Ricci. Then compute a finite-baseline, finite-distance retarded source/detector model and directly compare a candidate *independently selected* Cone-only operator against ordinary GR+isotropic solid; a nonzero source-independent dimensionless residual is required before claiming novelty.
