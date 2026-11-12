# Cone Derivation Ledger v15.751 — Gravity: logarithmic-time classical K4 spectrum, no Yang–Mills-type mass gap, and exact free tidal decay

**Date:** 2026-11-11 US Eastern. **Parents:** v14.935 K4 Einstein–Hilbert plus elastic-solid action; v15.706 exact three-sector squared-frequency-gap ratio 3 and conventional isotropic relativistic-elasticity comparator; v15.714 scalar retarded Green function; v15.720 scalar Weyl transfer; v15.721–722 vector/tensor Weyl transfer; v15.750 one compact canonical source driving three time-evolving electric-Weyl responses. **Fresh live HEAD immediately prewrite:** 3c5c67ac19d053f869928a3565f658eacf707c40; target path absent; additive only, Suzuki/far-tail protected files untouched. External Audit Round 547/v15.741 independently covered through v15.740; newest v15.750 is not yet independently audited.

**Categories:** [D] exact coasting Euler/logarithmic-time operator equivalence, continuous-spectrum no-gap property of a particular auxiliary classical Sturm–Liouville operator, exact free-mode electric-Weyl late-time envelopes; [N] correspondence between classical mode-frequency spacing and Yang–Mills quantum mass gap, as well as a universal source-independent Cone tidal observable; [O] experimentally discriminating full source-to-detector result under realistic background.

## Gate 380 — the actual logarithmic-time operator and its spectrum

For a free K4 scalar/vector/tensor Fourier mode of the coasting source-free dynamics (comoving k>0), write

**f_X''(τ)+(3/τ)f_X'(τ)+(β_X/τ²)f_X(τ)=0**,

**β_S=[8η(1+k²)-3k²]/3**,

**β_V=2η(4+3k²)/3**,

**β_T=3k²+8η/3**.

Define **x=log(τ/τ0)** and **u_X(x)=τ f_X(τ)**. By exact differentiation,

**f_X''+3f_X'/τ+β_X f_X/τ² = τ^(-3)[u_X,xx+(β_X-1)u_X]**.

Hence **ν_X²=β_X-1**, and for ν_X>0 the classical mode is

**f_X(τ)=τ^(-1)[A cos(ν_X log(τ/τ0))+B sin(ν_X log(τ/τ0))]**.

There is an exact natural weighted Hilbert-space transformation **U:L²((0,∞), τ dτ)→L²(R,dx)**, **(Uf)(x)=τ f(τ)**. On smooth compactly supported functions, the self-adjoint closure of the differential operator

**A_f=−[τ² d²/dτ²+3τ d/dτ+1]**

satisfies **U A_f U^(-1)=−d²/dx²**, the standard free one-dimensional Laplacian, with **pure continuous spectrum [0,∞)**. Thus *this explicitly defined auxiliary classical operator* has no positive spectral gap above zero. The numbers ν_X² are mode parameters/eigenvalues in a generalized spectral sense, not a discrete set of quantum particle masses. The log-time map is mathematical; no interacting quantum Hamiltonian, physical vacuum, or Wightman/Osterwalder–Schrader construction is supplied.

**Yang–Mills caution:** Nothing here constructs the interacting four-dimensional quantum Yang–Mills theory, or establishes (or rules out) a strictly positive energy gap above its quantum vacuum. The Clay Yang–Mills mass gap is a fundamentally different problem. An apparent 1/4 Casimir or a classical mesh spacing likewise cannot be identified as such a quantum gap without a Hamiltonian and spectral proof.

## Gate 381 — exact three-sector frequency relation is conventional relativistic elasticity

The mode parameters obey the already independently audited identity

**(ν_T²−ν_V²)/(ν_V²−ν_S²)=3**

whenever the denominator is nonzero. Because all ν_X²=β_X−1, this is identical to the squared-frequency relation from v15.706, not an extra log-time discovery. In particular, the transverse and longitudinal wave-speed squares in the coasting isotropic relativistic-solid comparator are

**c_V²=2η/3**, **c_L²=−1/3+8η/9**,

so exactly

**1−c_V² = 3(c_V²−c_L²)**.

It is a standard elasticity identity for that background and equation of state; it does not distinguish Cone from a conventional GR+elastic-solid treatment. Example **η=3/4,k=2** gives **ν_S²=5,ν_V²=7,ν_T²=13**, the same values used in v15.725's mathematical pulse spectral-notch gate.

## Gate 382 — physical-frequency scales do not stay separated from zero

The effective cosmic-time mode term is **β_X/τ²**, and the physical spatial Fourier scale is **k/a=√3 k/τ**. For any fixed η,k and finite β_X≥0,

**√β_X/τ → 0 as τ→∞**.

It is therefore invalid to interpret the constant log-time ν_X as a constant nonzero rest-mass energy in physical time. K4's positive log-time oscillation frequencies at fixed parameters are not evidence of a uniform positive physical energy gap over arbitrarily late coasting time.

This statement is about the classical linearized K4 mode coefficients, not an interacting quantum spectrum and not a general no-go for other possible K4 quantizations.

## Gate 383 — exact late-time electric tidal curvature for free waves

For a single source-free Fourier mode in each sector take the normalized homogeneous solution **f=τ^(-1)cos[ν log(τ/τ0)]**, **ν²=β_X−1**, and coasting **a=τ/√3**. Reinsert it independently into the *already audited* source-free Bardeen/linearized-Weyl formulas (v15.720–722) with source contact terms J=0. Let **c=cos(ν log(τ/τ0))**, **s=sin(ν log(τ/τ0))**. The exact electric-Weyl amplitudes are

**W_S(τ)=τ^(-3) [k²/(2(1+k²))][(1+k²−ν_S²)c+2ν_S s]**,

**W_V(τ)=τ^(-3) [i k/(4+3k²)][(ν_V²−1)c−2ν_V s]**,

**W_T(τ)=τ^(-3) [1/4][(1−3k²−ν_T²)c+2ν_T s]**,

where W_V is the complex Fourier coefficient of the transverse vector electric shear and W_T the plus-polarization transverse tensor component, in their respective earlier conventions. The phase factor **i** for the complex vector Fourier coefficient cancels into a real spacetime field after pairing ±k.

All three share an exact, bounded **τ^(-3)** free electric-Weyl amplitude envelope. Consequently their squared individual curvature amplitudes have envelopes proportional to **τ^(-6)**. For scalar pure STF Weyl curvature, the exact total norm remains **E_ij E_ij=(2/3)W_S²**, so the geometric 2/3 persists as a *shape factor* even while the physical curvature decays; it does not prevent late-time amplitude suppression.

These are **free homogeneous solutions** after removing source contacts, not a claim that the evolving positive-energy canonical matter source of v15.750 turns off after a finite global time. Its source history and constrained metric potentials may continue contributing. A fully retarded source-and-instrument signal requires those contributions and detector calibration.

## Gate 384 — originality boundary, negative result and reproducibility

**Positive mathematical outcome:** exact unitary transformation for a natural classical K4 differential operator, exact clarification of spectral type, and exact source-free scalar/vector/tensor Weyl late-time decay formulas.

**Negative novelty result:** (i) the mode-gap ratio 3 is already standard isotropic relativistic elasticity; (ii) the log-time frequencies are not a positive quantum vacuum mass gap; (iii) at fixed comoving k all physical effective frequency scales tend to zero with coasting expansion; (iv) source-independent 2/3 STF norm does not fix a finite signal.

**Reproducer:** research-notes/k4_log_time_spectral_gap_and_weyl_decay_v15_751.py, additive commit **3c5c67ac19d053f869928a3565f658eacf707c40**. Independently executed locally with SymPy to PASS on Euler-to-log-time operator equality, transformed Sturm–Liouville operator, 3-ratio/elasticity identity, all three exact Weyl formulas and limiting vanishing effective physical frequencies. No image generation; no historical or frozen file overwrite.

**HANDOFF — external audit:** independently re-derive the weighted Hilbert-space measure and self-adjoint transformed Laplacian, classical-vs-quantum mass-gap boundary, all three Weyl curvature late-time transfer formulas and the role of source contact terms. Do **not** extrapolate the time-dependent coasting model to a Yang–Mills quantum energy-gap statement. Continue independent verification of v15.750 compact canonical evolving source.

**NEXT:** test source-to-curvature transfer under a realistic finite-distance retarded detector construction and an explicit ordinary GR+relativistic-elasticity comparator. Accept a Cone-specific dimensionless gravitational observable only if it survives that comparator and no measured G or fitted source normalization is inserted.
