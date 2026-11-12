# Cone Derivation Ledger v15.815 — Gravity: complete five-helicity local and finite-arm optical tomography

**Date:** 2026-11-12 US Eastern. **Parents:** audited v15.760 local Fermi/Weyl projector and matched-EH+solid null; v15.787–788 full electric Riemann and detector; audited v15.810–812 coasting photon, free-mirror, clock source-to-optical detector. **Live HEAD immediately prewrite:** ec9d2256213131133f07accec43e6e44bd2fb61b. Target checked absent; strict additive-only. **Status:** [D] exact local 5×5 polarization projector, [N] finite-arm harmonic metric transfer numerically full rank with independently quadrature-verified photon/mirror/clock, [N] finite-wavelength cross-coupling invalidates naive diagonal local reading, [O] source histories for both extra helicities, full FLRW gauge-covariant initial-value control, physical remote source and new Cone interaction.

## Gate 424 — full five-dimensional polarization basis

Fix n=(2,0,1)/sqrt5, e=(1,0,-2)/sqrt5, b=(0,1,0). Define the five symmetric tracefree spatial curvature polarization tensors:

**Q_S=nn^T−I/3**,
**Q_Ve=ne^T+en^T**,
**Q_Vb=nb^T+bn^T**,
**Q_T+=ee^T−bb^T**,
**Q_T×=eb^T+be^T**.

The historical K4 v15.750–812 calculations retained only Q_S, Q_Ve, Q_T+ because of the chosen source and coordinate symmetry, *not* because the general physical metric has only three polarizations.

Use nine available free-fall arm directions **n,e,b,(n±e)/sqrt2,(n±b)/sqrt2,(e±b)/sqrt2**. Take five pairwise equal-arm differential outputs

**D1=n−e, D2=e−b, D3=(n+e)−(n−e), D4=(n+b)−(n−b), D5=(e+b)−(e−b)**,

where arm differences mean uu^T−vv^T.

Direct exact rank-two contractions give the five-by-five local Fermi projector matrix, with columns ordered (S,Ve,Vb,T+,T×):

**M_local = [[1,0,0,−1,0],[0,0,0,2,0],[0,2,0,0,0],[0,0,2,0,0],[0,0,0,0,2]]**.

Its exact **determinant is +16**. The exact inverse is

**S=D1+D2/2, Ve=D3/2, Vb=D4/2, T+=D2/2, T×=D5/2**.

This is a local *five-helicity curvature tomography* identity, not a claim of observing five gravitational quantum polarizations or five independent new Cone fields; a measurement must determine full local Fermi curvature with Ricci completion rather than electric Weyl alone, as v15.760/787 established.

## Gate 425 — test real finite-arm photon, mirror and clock mixing

Reuse the audited v15.811 conformal metric response for harmonic input exp(−iωη+iK·x), on coasting a(η)=a0 exp(ℋη), ℋ=1/sqrt3, a0=1/sqrt3. Keep all three ingredients in each arm's return proper-time response: outbound and inbound null-ray integrals, the endpoint displacement from freely falling mirror geodesics with Hubble friction, and the emitting observer's proper clock.

For a reproducible matrix test set **ω=1.2, |K|=sqrt5, comoving arm d=0.13**. Supply one metric basis perturbation at a time:

**scalar (Φ,Ψ)=(1,0.4)**,
**Ve or Vb transverse shift amplitude=1**,
**T+ or T× conformal spatial TT amplitude=1**.

This scalar (Φ,Ψ) normalization is only a test of the metric-to-detector linear map, not a claimed on-shell solution of the K4 field constraints; the five columns have arbitrary and different source normalizations. Free mirror initial perturbation displacement and velocity are set zero in the chosen coordinate gauge at conformal η=0, consistent with the audited v15.811 transfer setup. These data must transform with the gauge; this gate is not a full cosmological diffeomorphism test.

Independent *numerical quadrature* of all photon paths, mirror Green convolutions and proper-clock integrals for **9 arms × 5 sectors** agrees with the closed-form harmonic transfer to **1.36×10^-16** maximum absolute error. After taking five arm differences, the 5×5 finite-arm complex response matrix has nonzero singular values

**(0.19457675, 0.17392863, 0.01350801, 0.00400719, 0.00383034)**,

with numerical **det M≈(−4.2177253−5.6075377 i)×10^-9 ≠0**. Thus this particular finite-arm metric test is *full rank*. It is not a general theorem that all frequencies, arm lengths and geometries yield full rank: v15.793/794 already established response zeros at selected wavelengths.

## Gate 426 — exact selection rules versus finite-arm mixing

For the chosen symmetric arm geometry and this harmonic model, D3 continues to isolate Ve, D4 to isolate Vb, and D5 carries T× plus a Vb mirror/contact contribution; D2 is **not** purely tensor because both transverse vector displacements contribute to the moving-mirror observable at the finite measuring frequency. In the specific calculated basis D2 has vector coefficients approximately **−0.00607527** for Ve and **+0.00607527** for Vb, besides the tensor-plus coefficient approximately **0.17160745−0.02699006i**.

The matrix stays invertible so those effects can be de-mixed by its *frequency-dependent inverse*, but replacing it with the simple M_local inverse at finite wavelength would misidentify polarization amplitudes. The detector is a standard metric/geodesic/null-ray construction; no additional independent Cone coupling has entered. The existing source-driven v15.812 result remains a three-polarization restricted example whose other two metric helicities were absent by source preparation; this five-helicity detector test uses supplied harmonic metric modes, not yet new source-driven complete fields.

**Reproducer:** research-notes/k4_five_helicity_optical_tomography_v15_815.py, commit **e438c166ba159e6c1902ec82196b8caa8c015492**. The independent local reproduction passed exact SymPy local matrix, 45 independent numerical optical quadratures, complex determinant, singular values, exact symmetry zeros and finite-arm vector mixing. The committed source was written additively; external post-commit audit is pending. No image generator or frozen-object edit.

**HANDOFF — external audit:** verify all five polarizations and the exact M_local determinant/inverse; independently evaluate the 9×5 harmonic FLRW optical matrix and its free-mirror/worldline dependence, complex determinant and smallest singular value. Check the finite-arm D2 and D5 vector mixing and the fact that the harmonic basis is *not* a five-polarization on-shell K4 source. Preserve the exact action-level no-novelty GR+solid comparator from v15.760.

**NEXT:** derive both previously missing vector and tensor-cross source projections from an actual common positive-energy canonical field (v15.816), and then construct the full five-helicity sourced K4 field evolution and optical readout. A nonzero **Cone-minus-matched-GR+solid** observable still requires an independently selected physical Cone operator.
