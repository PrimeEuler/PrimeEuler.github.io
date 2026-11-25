# Cone Derivation Ledger v15.1481 — First unrestricted nonlinear 3+1 generalized-harmonic Einstein–H² evolution on actual constrained torus data

**Date:** 2026-11-25 Eastern. **Track:** Gravity/Cone. **Status:** [ACTUAL NUMERICAL PASS, short-time] all TEN independent 4D metric components gμν and their ten coordinate-time derivatives, both real curved-H² sigma fields and their two coordinate-time derivatives are freely advanced using the full nonlinear 4D generalized-harmonic wave-reduced Einstein–H² sigma equations, with *spatial FFT derivatives obtained from the evolving fields*. Initial data are the nontrivial spatially inhomogeneous curved-H² torus initial slice from v15.1453/1473, which solves the full nonlinear ADM Hamiltonian/momentum constraints and simultaneously the 4D harmonic gauge constraints. Both independent physical ADM H/M constraints and all four harmonic gauge constraints are re-evaluated on the evolved metric. [STRICT NEGATIVE/OPEN] Short time t=.016 only; high-frequency/low-N aliasing dominates, long-time strong stability/constraint convergence, full dealiasing and gauge damping not certified; the Weyl–F–B coupling remains OFF, κ=8πG=.003 prescribed rather than selected. This is the first **unrestricted** metric-and-sigma nonlinear GH method-of-lines evolution in this lane, moving beyond the v15.1480 *restricted exact pp-wave sector*. [AUDIT] pending independent exact-byte replay; Audit Round 649 (v15.1474, commit 60ddd5f6eadb9088d32eefbfbcbfce662eff86db) independently confirmed prior v15.1463–1473.

## Gate 1407 — solve the full nonlinear GH wave equations on a 3D periodic field grid

Evolve state y=(gμν,∂tgμν,φA,∂tφA), where metric is 4×4 symmetric Lorentzian and φ=(u,v) lives on the actual curved H² target. Use Einstein trace-reversed sigma source \`Rμν=κ GAB(φ) ∂μφA ∂νφB\`. Construct from **current evolving** g and ∂g all 4D inverse metrics, Levi-Civita Christoffels and harmonic vector Cμ=gαβ Γμ_αβ, including nonzero g0i once time evolution develops. Compute the lower-order nonlinear generalized-harmonic Ricci term Q(g,∂g) by setting all metric second derivatives to zero in the full Ricci-minus-gauge-derivative expression, as independently established by v15.1478/1479:

\`R^GH_μν = R_μν−∇_(μ C_ν) = −½ gαβ ∂α∂β gμν + Qμν(g,∂g)\`.

Solve ten metric coordinate accelerations explicitly:
\`∂t²gμν = [2(Qμν−κGAB φ^A_,μ φ^B_,ν)−2g^ti ∂t∂i gμν−g^ij∂i∂j gμν]/g^tt\`.
Solve BOTH curved-target scalar accelerations:
\`∂t²φA=[φA GBC gμν∂μφB∂νφC + Cμ∂μφA−2g^ti∂t∂iφA−g^ij∂i∂jφA]/g^tt\`.
All spatial derivatives are 3D FFTs on the periodically identified x,y,z coordinates; fourth-order RK4 advances the unconstrained state without resetting gauge/physical constraints at each timestep. No pp-wave symmetry, fixed conformal shape or frozen metric is imposed during evolution.

From the actual freely evolved g, metric velocities and φ velocities reconstruct α=1/sqrt(−g^tt), β^i=γ^ij g0j, extrinsic Kij=−[∂tγij−Diβj−Djβi]/(2α), normal sigma velocities Π^A=(φ^A_t−β^i∂iφ^A)/α, full spatial Ricci and H/M constraints. This is independent from the GH wave reduced equations. The 4 harmonic gauge constraints Cμ are computed independently from all 4D Christoffels.

## Gate 1408 — actual 3D numerical results, positives and negatives

**Locally actually executed reproducible** \`/mnt/data/cone_gh/gh3d.py\`, pure NumPy periodic FFT, fully general gμν and nonlinear H² target, SHA-256 **087310cf64d4aea64bcc3443a71af2b0d3c2092c0136cb42ac9c91d581efbb60**. **Additive standalone GitHub reproducible** \`research-notes/k4_gh_3d_unrestricted_einstein_h2_v15_1481.py\`, commit **134a3faf7f267cdcbce017c39718f7f112edb1bd**, assembled from the previously Audit-confirmed canonical v15.1472 nonlinear constrained initial-data solver and independently authored 3D GH solver/constraint monitors; mathematical implementation mirrors the executed local source, but **exact committed-byte external replay is pending**. The local prototype initially had two NumPy FFT-array axis-order mistakes in the gradient of a two-field array and its Hessian. These caused immediate Python shape errors before any physical output; fixed by explicit axis swapping and rerun successfully. All results below are from the successfully corrected full code.

| grid | RK4 dt | end t | max 4D harmonic C^μ | max ADM Hamiltonian | max ADM momentum |
|---:|---:|---:|---:|---:|---:|
| 16³ | .004 | .016 | 1.7210143e−8 | 4.2533537e−6 | 7.0081512e−7 |
| 16³ | .002 | .016 | 1.7210142e−8 | 4.2533537e−6 | 7.0081512e−7 |
| 24³ | .004 | .016 | 7.2581202e−11 | 1.1318018e−8 | 4.5671652e−9 |
| 24³ | .002 | .016 | 7.2581768e−11 | 1.1318028e−8 | 4.5671619e−9 |
| **32³** | **.004** | **.016** | **5.8734267e−13** | **1.4772903e−10** | **1.7669805e−11** |

Initial full ADM and 4D GH constraints independently measured:

| grid | t=0 harmonic | t=0 Hamiltonian | t=0 momentum |
|---:|---:|---:|---:|
| 16³ | 9.75793e−12 | 4.21694e−6 | 2.08002e−9 |
| 24³ | 8.65938e−13 | 1.1058912e−8 | 9.72077e−12 |
| 32³ | 1.0508201e−14 | 1.5010531e−10 | 2.90055e−14 |

At N32, the evolved 4D inverse g^tt remains negative (close to −0.999495), so the short interval retains a timelike coordinate-time evolution direction. Large residuals on N16 are expected from already independently audited coarse-grid nonlinear Ricci aliasing and Cauchy sigma initial-source aliasing (v15.1453/1460). N24→N32 improves all final constraint residuals by ~two orders of magnitude, but no asymptotic convergence order or continuum bound is claimed. Halving dt for fixed N16/24 changes residuals negligibly because **the spatial error floor dominates**. A finer-step N32 run exceeded the local execution budget, so N32 time-step refinement remains unclosed. The N16 raw solver does not claim physical fidelity.

## Controls / required work before milestone marked fully certified

This is a genuine **full unrestricted 3D GH Einstein–H² method-of-lines code** executing at short time, not just a strong-hyperbolicity principal-symbol derivation or an exact-wave ansatz. But its PDE formulation has no gauge-constraint damping and uses a raw undealiased pseudospectral nonlinear evaluation; its long-time stability and freely evolved constraint propagation are not certified. Need 2× oversampled products and consistent filtering/projection of *every* GH RHS nonlinear term (the standalone 3D conformal Ricci 2× improvement in v15.1463 is a precedent but does not prove full GH filtering), longer T=.04 and beyond, spatial/timestep convergence with independent monitoring. Gauge sources and initial Cdot compatibility should be checked analytically and independently; no automatic confidence from initial C=0 alone.

**AUDIT:** run committed-byte v15.1481 source at N16/24/32, compare displayed residuals and monitor lorentzian g^tt; inspect full nonlinear Q, mixed g^ti terms and target sigma Christoffel sign, independent ADM Kij reconstruction after g0i !=0, and whether zero-mode/FFT aliasing explains remaining floors. Verify that executable truly does NOT impose exact-wave restriction and preserves symmetric metric. Compare with independently executed local SHA and ask for explicit full GH time-derivative subsidiary constraints. Prior v15.1480 restricted null-sector and v15.1479 analytic-jet RHS remain independent comparators.

**NEXT:** v15.1482 runs this same fully unrestricted 3D solver on the **exact nonlinear harmonic FLRW benchmark**, demonstrating fourth-order time convergence, and should be audited independently. Then use full 2× spectral dealias and longer N24/N32 3D tests. Only after physical GH plus Einstein constraint control should we turn on full Weyl–F–H² higher-derivative Maxwell interaction with full metric variation and physical selector; sector variance V=1/16 alone is not coupling strength.