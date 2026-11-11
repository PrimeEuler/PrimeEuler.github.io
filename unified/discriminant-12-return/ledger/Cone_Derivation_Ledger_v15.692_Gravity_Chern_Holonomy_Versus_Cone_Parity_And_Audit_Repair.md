# Cone Derivation Ledger v15.692 — Gravity lane: exact Chern holonomy versus Cone quarter-shell parity; additive Round 541 script repair

**Date:** 2026-11-11 US Eastern. **Parents:** v14.731–732 Taub–NUT gravitational pair quantum; v15.625–626 formal all-mesh Casimir and q=2 parity; v15.631–632 Taub–NUT patch and integer Chern charge; v15.686 quarter/half temporal dictionary obstruction; v15.690 second chi-odd-factor negative gate; **External Audit Round 541 (v15.691)**, which verified previous results and detected a failed SymPy assertion in the original v15.686 script. **Scope:** exact differential-form/representation calculations [D], conditional cross-sector same-pair comparisons [C], physical bridge unavailable [N/O]. **Immediately prewrite HEAD:** b4e3d1442914567f442ddf2f0ccec7e9f126a1fa. Collision check found no v15.692 ledger entry. Historical files, frozen Suzuki objects and far-tail payloads remain untouched.

## Gate 249 — independently repair the audited v15.686 reproducer, preserving provenance

Round 541 correctly found that the existing v15.686 script throws an AssertionError on the Casimir-gap ratio due to SymPy bare structural equality (==) rather than mathematical equivalence. The underlying identity remains correct:

**C(L)=L(L+4)/16,**

**[C(L+1)-C(L)]/[C(L+2)-C(L)] = (2L+5)/[4(L+3)].**

A separately committed **additive** reproducer, research-notes/quarter_half_temporal_selector_assertion_repair_v15_692.py, replaces that single check by **simplify(computed-target)==0** and **computed.equals(target)**, also checking 63 sample positive integer L. It prints PASS when independently executed. The historical v15.686 file was not modified, and therefore the audit's statement that the *original committed script* fails remains true and visible. This is a reproducibility correction rather than a change of mathematics.

## Gate 250 — the physical Taub–NUT angular bundle has integer Chern winding

The actual angular patch comparison from v15.632 uses north/south U(1) connections

**A_N=(k/2)(1-cos(theta))dphi, A_S=-(k/2)(1+cos(theta))dphi**, with **k in Z**.

Their difference is **A_N-A_S=k dphi** and their shared curvature is

**F=(k/2)sin(theta)dtheta wedge dphi**, giving **(1/2pi) integral_(S2) F=k**.

A latitude loop at polar angle theta in the north patch therefore has holonomy

**W_k(theta)=exp[i pi k(1-cos(theta))]**,

and at the equator

**W_k(pi/2)=(-1)^k**.

This is standard integer monopole-bundle holonomy, already implicit in v15.632. A quarter-valued pair product p_G=k/4 does not convert the physical angular Chern class into k/4. The phase is dimensionless and independent of an inserted G, but it is a conventional gauge-bundle phase, not uniquely Cone physics.

## Gate 251 — two natural cross-sector comparisons give incompatible 'distinctions'

The gravitational dyon *pair product* and the EM Dirac pair product have different normalization:

**p_G=k_G/4** and **p_EM=k_EM/2**, for respective integer windings. How the two systems should be compared is a separate physical question.

**Equal integer Chern windings** k_G=k_EM=k imply identical angular monopole latitude phases for the same loop:

**W_G(theta)/W_EM(theta)=1**.

**Equal dimensionless pair products** p_G=p_EM instead impose **k_G=2k_EM**. Then on the equator:

**W_G(pi/2)=1, W_EM(pi/2)=(-1)^(k_EM)**,

so the ratio is **(-1)^(k_EM)**. This gives a mathematically sharp conditional parity contrast for odd k_EM. But neither the equality of the pair products nor a common physical angular bundle/loop/interferometer is selected by the Cone. Merely comparing a conventionally quantized k=1 bundle with a k=2 bundle is not a new gravitational prediction. The loop phase also depends on theta away from the equator, so choice of physical path matters.

This gate is a useful *comparison-dictionary ambiguity*, parallel to the energy-versus-wavelength ambiguity of v15.686. The discrete scale difference alone does not pick a measurement.

## Gate 252 — Cone spectral chi is not the Taub–NUT equatorial Wilson character

The formal quarter-shell character is

**chi(L)=exp(16 pi i C_geom(L))=(-1)^L**.

It is +1 for **every even-L formal EM half-grid shell**, irrespective of any angular monopole winding.

By contrast the physical angular equatorial phase W_k=(-1)^k equals -1 for the perfectly allowed k=1 monopole bundle. No existing mapping identifies the formal shell label L with physical angular Chern charge k in both sectors, and the obvious universal identification chi=W fails when the formal EM-even sector is compared to odd-k physical monopoles. More fundamentally, v15.632 already showed that at k=1 the conventional lowest angular spin is j_phys=1/2 (Casimir 3/4), whereas the proposed quarter-shell geometric spin j_geom=1/4 has Casimir 5/16.

Therefore the equality of two abstract Z2 characters at selected labels cannot establish a gravitational phase observable. To do so would require a derived intertwiner and a physical operator/path assignment—not a new arbitrary identification.

## Gate 253 — gravity-lane frontier after testing the G-free topological candidate

**[D]** Exact q=2 sector parity and exact integer angular monopole holonomy are both available mathematically.

**[D]** At matched first Chern class the physical angular holonomy is the same in the two named sectors.

**[C]** At matched dimensionless pair product, equatorial holonomy can differ by (-1)^k_EM, but the cross-sector match, common physical loop and source/readout are unselected.

**[N]** The formal Casimir character cannot simply be identified with actual angular Wilson phase.

**[N]** This test does not yield a new parameter-free, experimentally distinguishable G-free gravity observable without an added physical dictionary.

**Reproducers:** research-notes/quarter_half_temporal_selector_assertion_repair_v15_692.py, commit f842769af5baf72b8d9d5a8d91257f6472099b4a; research-notes/cone_topological_phase_contrast_v15_692.py, commit b4e3d1442914567f442ddf2f0ccec7e9f126a1fa. Both calculations were independently tested in local SymPy before upload; no images generated. The first is an additive repair to an audit-detected failed assertion, not a silent historical modification.

**HANDOFF:** external audit/gravity/sandbox: (1) execute both v15.692 scripts and verify exact results, (2) confirm the old v15.686 script remains unchanged and still has the reported assertion failure, (3) verify the physical U(1) Wilson latitude convention and its orientation dependence (sign conjugation does not change equatorial +/-1), and (4) challenge the classification that the equal-pair comparison requires an externally supplied cross-sector measurement dictionary.

**NEXT:** test whether a *purely internal* count/character ratio avoids the physical cross-sector identification, using finite shell sums with the exact chi grading and matched normalized radial cutoffs. Separate universal arithmetic identities, accidental cutoff dependence, and any surviving dimensionless shape invariant. Require an independently selected physical shell observable before promoting an arithmetic difference to gravity.
