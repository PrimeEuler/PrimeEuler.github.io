# Cone Derivation Ledger v15.942 — Physical Taub–NUT U(1) monopole angular spectrum versus the odd-quarter geometric Casimir

**Date:** 2026-11-13 Eastern; Gravity lane. **Question:** Does the existing *actual* Taub–NUT U(1) fiber/monopole connection induce the odd-quarter geometric shell Casimir rather than merely the quarter-valued gravitational pair? **Parents and redundancy check:** audited gravitational worldline pair v14.731/732; v15.630 genuine SU2 obstruction; v15.631 explicitly distinguished p=k/4, physical angular s=k/2 and geometric quarter j=k/4; v15.632–633 true monopole patch and fourth-root obstruction; v15.639 bicone-swap distinction; v15.940–941 auxiliary 8π phase and global descent; External Audit Round 575 v15.939 confirmed Gravity v15.930–938. Existing monopole-harmonic formula is **not new**. New exact comparator here: shell-by-shell dimension correspondence, covariant angular kinetic spectrum and an all-level no-affine-Casimir-bridge theorem with exact residual. **Live master HEAD immediately before ledger write:** 079a4dead69d8444b61081521c2529c30e1d8eec (v15.942 reproducer), target absent. Additive only; no collisions, no certified or Suzuki changes.

**Status:** [D/recall] physical monopole SU2 and quarter-pair relation; [D] dimension/Casimir comparison and affine-no-bridge theorem; [N] no induced odd-quarter physical Casimir or connection-selected interaction; [O] actual sourced gravitational field dynamics and non-SU2 carrier.

## Gate 710 — identify the physical U1 connection representation accurately

Under the *stated regular-periodic Taub–NUT assumptions*, normalized Misner fiber angle has integer Fourier winding k and gravitational pair **p=μcl/ℏ=k/4**. The associated angular monopole line bundle has integer first Chern charge k and monopole angular parameter **s=k/2=2p**. For positive k, ordinary covariant monopole harmonics on S² carry total rotation spin

**j_phys=s+r=k/2+r**, with r nonnegative integer, dimensions **d_phys=2j_phys+1=k+2r+1**. Its genuine total SU2 Casimir is **C_phys=j_phys(j_phys+1)**; the standard gauge-covariant (unit-radius) monopole kinetic angular Laplacian has spectral value **λ_cov=j_phys(j_phys+1)−s²=s(2r+1)+r(r+1)**. This is the standard angular spectrum of the actual U1 monopole connection, not a new field hypothesis, and does not require confusing the time Fourier generator with angular spin.

## Gate 711 — dimensions match the corresponding refined quarter shell but Casimirs do not

Set **L=k+2r**, so every physical monopole multiplet has **L+1** states, exactly the count of *nodes* in the corresponding q=2 quarter shell `m_i=−L/4+i/2`. This is a natural numerical/dimensional match for all k and r. The genuine physical angular SU2 spin equals **j_phys=L/2**, precisely the **closed refined-step SU2** representation with spin L/2 when its generators are normalized to step 1. It is not the original projected step-one, boundary-defective q=2 ladder.

The physical and formal geometric Casimirs are, respectively,

**C_phys=L(L+2)/4** and **C_geom=L(L+4)/16**,

with exact difference **C_phys−C_geom=L(3L+4)/16>0** at L>0. For the fundamental k=1 series r=0,1,2, the (dimension, C_phys, λ_cov, C_geom) records are **(2,3/4,1/2,5/16)**, **(4,15/4,7/2,21/16)**, **(6,35/4,17/2,45/16)**. In particular, the minimal angular physical Casimir **3/4** is not the quarter geometric **5/16**, even though the carrier has two states in either description. The equality of dimensions is not a unitary *Lie algebra* intertwiner because the generators are structurally different.

## Gate 712 — no single scalar+constant calibration fits the full tower

Could a common change of units and Casimir zero point rescue the identification? Fix winding k and suppose a single **C_phys(r)=a C_geom(r)+b** for every r≥0. Matching r=0 and r=1 uniquely fixes

**a=4(k+2)/(k+3)**, **b=−k(k+2)/[4(k+3)]**.

Then the exact residual over the full sequence is

**C_phys(r)−[a C_geom(r)+b]=r(r−1)/(k+3).**

At r=2 the residual is **2/(k+3)>0** for every positive k; hence no fixed affine renormalization can identify even the first three multiplets. (A *nonlinear* map or the original label relation C_phys=4 C_geom−L/2 trivially relates the eigenvalues, but that requires the separate linear label L and is **not equality of physical Casimir operators** or a field-derived observable.) This exact spectral discriminator makes the mismatch stronger than one low-lying example. The no-affine obstruction is a mathematical comparison, not an experimentally new gravitational frequency: treating C_geom as an energy would import a Hamiltonian scale.

## Gate 713 — explicit generator check and scope

Independent exact SU2 matrices for the corresponding L/2 physical multiplet satisfy [J+,J−]=2Jz with ordinary nearest-neighbor step; the original q2 projected step-one ladder on m_i=−L/4+i/2 does not, and its defective quadratic differs from formal C_geom by a rank-two boundary E on tested odd L=1,3,5,7. Thus physical bundle-induced angular SU2 matches the known closed refinement, not the formal original-step q2 Casimir. Tensoring with the ordinary two-SU2 bicone does not change that: the second physical SU2 factor is not a quarter-character by itself (v15.639/941).

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_taub_nut_u1_covariant_casimir_bridge_v15_942.py`, commit **079a4dead69d8444b61081521c2529c30e1d8eec**. Executed locally in SymPy: general k,r polynomial identities, symbolic affine fit and nonzero residual; exact k=1..8/r=0..5 checks, and representative 2/4/6/8-dimensional matrices distinguishing genuine SU2 from original defective quarter J. PASS. External Audit pending.

**Scientific verdict:** The *actual* gravitational U1 fibration does supply the quarter dimensionless pair p=k/4 and an angular monopole bundle. Its covariant angular Casimir is **not** the odd-quarter geometric Casimir. The dimensional correspondence is exact and interesting but is naturally explained by the already-known closed refined-step SU2 realization, not a new gravity-specific spin, Casimir or 8π phase character. No parameter-free measurable G-free contrast or physical EM/G odd-sector coupling follows.

**NEXT:** Instead of adding another arbitrary U1 holonomy, derive from a specified Lorentzian Taub–NUT/Kaluza–Klein field action an operator whose symmetry is genuinely different from the standard monopole angular SU2 and whose spectral response is independent of fitted couplings; otherwise close this angular identification route as a negative result and redirect to physically sourced rank1/rank2 tidal measurements. Do not reopen parked Suzuki quarter physical weld.

**HANDOFF Audit/Muse:** Independently verify covariant angular eigenvalues, dimensional equality with L=k+2r, no-affine-fit residual r(r−1)/(k+3), and physical-closed-SU2 versus defective quarter-original-step distinction.
