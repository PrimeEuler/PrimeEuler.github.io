# Cone Derivation Ledger v14.774 — Hbar unit-circle action-to-length selection test

Date: 2026-10-23. Gravity lane. Parents: v14.620, v14.622, v14.773, unit-circle pair-encoding note. Prewrite HEAD: b75ca53a808187f10ece1bf950463fd49ac0c701. Research: research-notes/Gravity_Hbar_Unit_Circle_Common_Length_Test.md (commit b75ca53). Additive only; Suzuki and far-tail untouched.

## Exact mathematical anchors [D]

The circle point \(z_{n,k}=(n-k+2i\sqrt{nk})/(n+k)\) satisfies \(|z_{n,k}|=1\) and \(z_{\lambda n,\lambda k}=z_{n,k}\). Its consecutive AM–GM identity
\[
(j+\tfrac12)^2-\tfrac14=j(j+1)
\]
fixes ratios, halves and quarters, not an absolute length. v14.620's established interpretation identifies \(\hbar\) as action per radian of quantum phase \(e^{iS/\hbar}\). A complete winding changes S by \(2\pi\hbar\).

## Conditional loop calibration [D/O]

For an ungauged circular proper loop of radius R and constant physical tangential momentum p, the independent model input \(S_{\rm loop}=2\pi pR\), together with phase single-valuedness, implies
\[
\boxed{pR=m\hbar},\qquad m\in\mathbb Z.
\]
Thus the circle can supply a physical length unit \(\ell_p=\hbar/p\) if p is separately measured or selected. Taking p=μc gives a reduced-Compton scale only as another input. In gauge/gravity holonomy backgrounds, the phase quantization law requires the appropriate connection contributions and can differ; none is derived here.

## Remaining common-length no-go [D]

At fixed winding, \((R,p)\mapsto(\lambda R,p/\lambda)\) preserves the phase; the unit circle cannot independently select R. Dimensional analysis likewise shows ħ and c alone do not yield a length; a mass, momentum or other dimensionful physical datum is required. The Planck length \(\sqrt{\hbar G/c^3}\) is circular as an input if seeking to derive G.

Hence the unit circle may eliminate independent **action** normalization freedom but does not force half-grid **physical length** spacing or EM/G coupling equality. The quarter coordinate vertices are not by themselves quarter-phase holonomy. The missing test is a common dynamical phase/holonomy boundary condition that derives the two sector embeddings, not assumes them.

Status: exact arithmetic and conditional winding law; universal length selector OPEN; G NOT derived; external audit requested. v13.770 carrier guardrail retained.

HANDOFF
target: external-audit
type: gravity-only-math-audit
parent: v14.774
status: open
action: Verify circle scaling invariance, the 2π winding normalization, the conditional momentum-loop result and scaling freedom; ensure quarter vertex is not mistaken for holonomy or a derived coupling.
deliverable: scoped verdict, additive only, no Suzuki/far-tail modifications.
