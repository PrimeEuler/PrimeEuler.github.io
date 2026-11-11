# Cone Derivation Ledger v15.695 — Gravity: observable closure matrix and fixed Maxwell source versus unselected Cone interaction

**Date:** 2026-11-11, US Eastern. **Parent gravity chain:** v14.767/774/904/914 factor-grid, action-length, weld and audit; v14.928/930/935 K4 tensor and stability; v15.625–628 shell parity; v15.631–632 Taub–NUT phase/patch; v15.646–647 charge-changing comparator; v15.676–680 cavity source and two resonances; v15.681–690 multimode dispersion/no-go tests; v15.692–694 holonomy, signed-count and quarter-phase negative gates. **External Audit Round 541:** v15.691 detected v15.686 script defect; v15.692 preserved original and added the separate corrected reproducer. **Status:** [D] direct Maxwell action derivation and source-normalization control; [D] exact sector-odd zero and arbitrary coupling magnitude; [N] no new Cone metric/source normalization from existing factor and Casimir identities; [O] independently sourced spacetime field/intertwiner. **Immediately prewrite HEAD:** dc8977f64c17218d77fc44c8dc58208e9a36a082. Search found no v15.695 ledger; commits additive only, no Suzuki/far-tail/certified modifications.

## Gate 261 — closure matrix: what survives and what is missing

| Candidate | Certified exact content | Requires new physical input | Observable verdict |
|---|---|---|---|
| q=2 quarter-only Casimir shells | C_geom=L(L+4)/16 and chi=(-1)^L; sector projectors | Physical realization of geometric shell C and an actual charge-changing interaction | Representation selector, not independently observable gravity |
| EM/G weld and power map | q_G=1/4, q_EM=1/2; h_G=1/2, h_EM=1; normalized shell/divisor covariance | Common physical coordinate calibration and propagation dynamics | Dimensionless count resolution, not a clock/force |
| Taub–NUT dyon pair | p_G=k/4; integer angular first Chern k; fixed-l Fourier quarter characters | Physical TN geometry/source, non-CTC realization, interferometer and selected length l | Conventional winding phases; no independently forced gravity/EM contrast |
| K4 elastic tensor | Conditional m_T²=(8 eta/3)H² with H=FLRW expansion; stability window | Cosmology, eta selection, source and detection; existing coasting background observationally disfavored | Dimensionless dispersion discriminator but present-lab mass route scale-closed |
| Finite EM cavity | Exact seeded conversion at omega_g=omega_c, conventional multimode overlap and Fisher ratios | Physical GW source/strain, detector material boundaries and Q | Real standard Maxwell–gravity engineering, not unique Cone |
| q=2 odd-rung carrier | chi-odd W flips parity; chosen W² can match a reference even shift | Physical source of W and its matrix element, globally correct bundle/representation | Algebraic witness only; ordinary EM-to-EM direct odd matrix element vanishes |
| Signed divisor counts | Exact D(N) and chosen parity-weighted combinations | Physical shell-pair pullback, source/readout | Nonunique arithmetic ratios, not gravity predictions |

No entry in this matrix currently supplies a dimensionless, parameter-free and experimentally distinguishable *new Cone gravity observable* without an externally added physical map or source. This is a documented frontier assessment, not a theorem prohibiting all future Cone dynamics.

## Gate 262 — universal metric–EM interaction source is already fixed by Maxwell, without an extra quarter coefficient

Work in the same explicitly restricted prescribed metric and fixed-wall model as v15.680:

**ds²=-dt²+exp(2b)dx²+exp(-2b)dy²+dz²**,

**A_y=B0 z+a(t,z)**, all other dynamical potentials suppressed, natural Maxwell normalization c=1.

Reducing the standard curved Maxwell action **S_EM=-(1/4) integral sqrt(-g) F_(mu nu)F^(mu nu)** per unit transverse area gives

**L_EM=(1/2) exp(2b)[(partial_t A_y)²-(partial_z A_y)²].**

Linearization around B0 and small a,b yields

**(partial_t²-partial_z²)a=2B0 partial_z b**.

At second order in independent perturbation bookkeeping epsilon with a->epsilon a, b->epsilon b, the mixed action term is exactly

**L_mixed=-2 B0 b partial_z a**.

Integrating by parts in z gives the same bulk source, with an additional boundary term that matters outside the fixed-wall comparator. Hence, *given* a prescribed metric perturbation b and magnetic bias B0, ordinary Maxwell theory fixes the numerical interaction coefficient 2. It is not supplied by the quarter grid and not an independent new source. The absolute response remains proportional to the physically sourced b amplitude, static magnetic bias, and boundary/readout transfer.

For real cavities the literature requires proper-detector-frame fields and mechanical boundaries, not arbitrary fixed-wall TT interpretations: Berlin et al., Phys. Rev. D 105 (2022) 116011, DOI 10.1103/PhysRevD.105.116011; Gué, Krokotsch, Moortgat-Pick, JCAP 08 (2026) 058, DOI 10.1088/1475-7516/2026/08/058.

## Gate 263 — exact symmetry does not fix any new coupling normalization

On a direct sum H=H_+ plus H_- with chi=+1 on ordinary EM and chi=-1 on odd-quarter shells, for any chi-odd W:

**{chi,W}=0**, hence **P_+ W P_+=0**.

Its second-order composite is chi-even,

**[chi,W²]=0**,

and may yield nonzero EM-to-EM matrix elements if a suitable physical intermediate sector exists. But for every nonzero scalar g,

**{chi,gW}=0** and **P_+ (gW)² P_+=g² P_+W²P_+**.

The grading fixes whether an interaction is *permitted*, not g or the amplitude of the composite. Even fixing a chosen reference even shift W² algebraically (as in v15.628) does not identify W with a metric perturbation, a physical Yang–Mills charge or the Maxwell stress tensor, nor fix its absolute spacetime source normalization. Without independent field dynamics, assigning g from the desired signal would be circular.

## Gate 264 — no replacement of missing gravity dynamics by a conventional coupling identity

The standard EM metric source offers an exact normalization **conditional on b**; the q=2 mathematical grading offers an exact selection rule **conditional on a realized state carrier**. Their juxtaposition does not derive the physical relation

**b_(mu nu) = functional[quarter-grid matter/fields]**,

nor a globally defined odd charge-changing intertwiner whose observable matrix elements and normalization are fixed. Those are logically separate unsupplied inputs. Accordingly the current gravity lane cannot claim a unique G-free new gravitational wave coupling from the standard seeded cavity formula.

**Result:** conventional field coupling derivation [D]; exact grading/normalization freedom [D]; novel Cone gravitational coupling and prediction [N/O].

**Reproducibility:** research-notes/maxwell_sector_source_normalization_v15_695.py committed at dc8977f64c17218d77fc44c8dc58208e9a36a082 and independently executed locally to PASS. It derives the Euler–Lagrange source from the metric-reduced action, isolates the mixed action coefficient rather than confounding it with the quadratic background term, and verifies parity matrix identities and arbitrary composite magnitude. No figures generated.

**HANDOFF:** external audit/gravity/sandbox: verify signs and boundary scope of L_mixed, compare actual Maxwell source with v15.680, check that no independent gravity-sector operator in older ledgers fixes the normalization g, and challenge closure classifications against any sourced physical intertwiner.

**NEXT:** targeted *source-first* gate. Among available source-derived geometric structures, test the standard Taub–NUT fiber KK connection and actual charge/current conservation against the proposed odd quarter-sector W. Explicitly compute whether minimally coupled gauge/metric interactions preserve fiber winding k or can source k→k+1 on a fixed invariant background. If they preserve k, state the symmetry obstruction precisely; if a non-invariant source breaks it, write that source, its required bundle charge and its free amplitude rather than relabeling a toy transition as a prediction.
