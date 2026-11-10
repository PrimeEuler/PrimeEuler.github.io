# Cone Derivation Ledger v15.612 — Lane A: quarter-mesh complement signal survives Paper C shift and positive measures

**Date:** 2026-11-10. **Parents:** v13.197 (circle pushforward), Paper C Quantum Realizations, v14.767 (mesh scaling), v15.602 (all-q ladder), v15.608–609 (boundary support and shifted origin), v15.610 (External Audit Round 522 *and* separately named concurrent Lane A file; version collision), v15.611 (additive canonical numbering correction for Lane A Gates 81–82). **Status:** [D] positive-support theorem and numerical independently recomputed integrals; [O] physically selected coordinate dictionary, probability measure, gravity coupling. **Immediately checked live HEAD:** c35b47b02010b49c27dc27b8f71bd7717594e85f; next version v15.612 search clear. Additive only, prior conflicting v15.610 files untouched; Suzuki frozen/production untouched.

## Gate 83 — the complement signal survives shifted occupation-factor origin

The continuum interpolation of the fixed-step original AM–GM Casimir deficit at normalized transition ratio r=s/u is

E_r(x,y)=1/2 [y(x+r) 1_(y<r)+x(y+r) 1_(x<r)].

The v13.197 staircase regions are formed in original column coordinates X∈[k−1,k], 0≤Y≤n+1−k (triangle), 0≤Y≤floor(n/k) (divisor), and their difference A. Apply the Paper C-like factor-origin translation **x=X+1, y=Y**, while retaining the same function E_r in the translated factor coordinates. This is a *coordinate-domain comparison*, not a claim that Paper C's actual Fock J± equals the original defective ladder.

For co-scaled r=1, the entire complementary staircase A satisfies X≥1,Y≥1 almost everywhere, hence translated x≥2,y≥1, and E_1=0 throughout A. For original physical step retained on the u=1/2 grid (r=2), column k=2 of A for each integer n≥3 includes a positive-area subset where old X∈(1,2), y=Y∈(1,2), x=X+1≥2. Here E_2(x,y)=y(x+2)/2>0. So **F_{A,2,shift=1}(n)>0 for all n≥3**, whereas **F_{A,1,shift=1}(n)=0**.

## Gate 84 — positive-measure robustness versus magnitude nonuniversality

The preceding proof rests on open-set support and positivity, not the Jacobian's numerical formula. Any positive locally integrable area weight that assigns positive measure to that open complement patch gives a strictly positive fixed-step A response, while co-scaled r=1 contributes zero. Two independent choices were tested: (i) flat factor-area measure dX dY and (ii) the exact circle pushforward J_F(x,y) dX dY, J_F=(x+y)/(4sqrt(xy)), including its translation x=X+1.

At n=11 the dimensionless **F** integrals are:

| shift c | weight | r | F_T | F_D | F_A |
|---|---|---|---:|---:|---:|
| 0 | flat | 1 | 35.750000 | 35.750000 | 0 |
| 0 | flat | 2 | 146.250000 | 75.000000 | 71.250000 |
| 0 | circle | 1 | 33.903275634744 | 33.903275634744 | 0 |
| 0 | circle | 2 | 105.723774794453 | 57.613393686346 | 48.110381108107 |
| 1 | flat | 1 | 20.625000 | 20.625000 | 0 |
| 1 | flat | 2 | 145.250000 | 105.875000 | 39.375000 |
| 1 | circle | 1 | 20.446917414766 | 20.446917414766 | 0 |
| 1 | circle | 2 | 102.842395046821 | 75.142463203350 | 27.699931843471 |

All rows independently satisfy F_T=F_D+F_A within integration tolerance; r=1 reproduces previously certified unshifted and shifted circle v15.608–609 numbers, and r=2 unshifted reproduces the canonical v15.611 values. All r=2 values are strictly positive on A. At n=11 the scale-free complement share F_A/F_T is 0.4871795 unshifted-flat, 0.4550574 unshifted-circle, 0.2710843 shifted-flat, 0.2693435 shifted-circle. Hence *presence* is stable but magnitude is origin/measure-dependent; there is no universal selected quotient.

For the u=1/2 physical factor scaling, the circle F integrals acquire the u^4 factor 1/16 if the translation c=1 is made in **normalized** coordinates before scaling. Under other translation conventions the comparison needs to be recalculated. Keeping a fixed normalized n is not the same as matching physical hyperbola product X, which changes n as u^-2 (v14.767). Do not identify factor area, circle area, operator matrix element, or physical energy.

## Independent verification and handoff

Reproducer `cone_gate83_84/reproduce.py` computes all 24 integrals with SciPy quadrature, splits at indicator discontinuities, transforms away the integrable circle-axis singularity, checks the T=D+A identity, and asserts strict A positivity/zero as appropriate. `cone_gate83_84/REPORT.md` and the downloadable `cone_gate83_84.zip` archive include calculations. No new image generated.

**Next gate:** assess fixed-physical-product comparisons and alternate sources of the transition ratio r=s/u; determine whether any physically justified dynamical symmetry selects fixed s instead of co-scaled s, and do not promote the algebraic contrast to a gravitational prediction prematurely.

**HANDOFF** target external-audit, gravity, sandbox; status open; type origin-shift and positive-measure boundary support; independently confirm n≥3 positive patch, co-scaled null complement, each n=11 integral, and distinguish geometrical translation from Paper C operator equivalence. Frozen Suzuki untouched.
