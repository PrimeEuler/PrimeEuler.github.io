# Cone Derivation Ledger v15.694 — Gravity lane: Taub–NUT quarter-pair Fourier characters and physical-scale obstruction

**Date:** 2026-11-11 US Eastern. **Parents:** v14.731–732 dyon quarter product and audit; v15.631–632 distinct Lorentzian Misner-time Fourier winding versus angular Chern class; v15.646–647 charge-changing ladder obstruction; v15.692 topological phase comparison; v15.693 factor-pair parity-pullback ambiguity. **Status:** [D] exact Fourier circle identities, fractional translation characters, rescaling invariance; [N] no new scale-free gravitational observable beyond integer winding without a physical selection/readout; [O] a physical characteristic length/energy anchor and a sourced interferometric operation. **Immediately prewrite live HEAD:** d6f8ed811b03e858d7d80ea6533488cf3b875cac. Collision search found no v15.694 ledger entry. Suzuki/far-tail/certified objects untouched.

## Gate 258 — quarter gravitational pair quantum is a dimensionless Fourier-winding normalization

In the formal fixed-l Lorentzian Taub–NUT Misner-periodic model of v14.731 and v15.631, the physical-time period is

**T=8 pi l/c**, with **l>0**.

Periodicity of a pure Fourier energy mode gives

**E_k = 2 pi hbar k/T = hbar c k/(4l)**, **k integer**.

The previously derived gravitational pair product is

**p_G = E_k l/(hbar c)=k/4**.

This establishes the quarter-pair arithmetic without measured G. But all of the dimensionless quantities in this minimal one-parameter family are functions of the winding integer k, not independently fixed new dynamical constants. For example, the adjacent energy-gap ratio is

**E_(k+1)/E_k=(k+1)/k** (for nonzero k),

while the absolute energy spacing is

**Delta E=hbar c/(4l)**.

The scale l remains free: **l -> lambda l**, **E -> E/lambda** preserves p_G and every ratio of energies. No independent physical cavity or gravitational energy scale follows from the quarter by itself.

## Gate 259 — fractional-period phases are ordinary circle characters

Under a chosen translation through fraction 1/r of the time period, a mode acquires

**U(T/r)|k> = exp(-2 pi i k/r)|k>**, for any positive integer r.

At r=4 this gives the appealing quarter character

**U(T/4)|k> = exp(-i pi k/2)|k>**,

with eigenvalues 1, -i, -1, i according to k modulo four. The full-period return is

**U(T)|k> = exp(-2 pi i k)|k> = |k>**.

The quarter character is exact but not unique: choosing r=2,3,5,8 produces equally exact roots of unity. The normalized integer winding alone does not select the physical operation T/4, prepare a coherent superposition of k sectors, or furnish a common phase reference/readout. This phase is a **fractional time-translation eigenvalue**, not automatically the angular monopole Wilson holonomy calculated in v15.632 or a new Berry phase. Its real-world use also inherits the known periodic-Lorentzian-time/closed-timelike-curve caveat.

## Gate 260 — strongest conditional route and exact negative result

If an independent physical process were to create a coherent pair of winding states and implement/measurably compare the quarter-period translation to another sourced sector, then their relative phase

**exp[-i pi (k1-k2)/2]**

would be a parameter-free discrete character conditional on that process. This could be an experimentally distinguishable interference datum in such an explicitly supplied model, but it would be a general property of a periodic Fourier system; it is not uniquely Cone merely because its period is divided into quarters.

At present the mathematically certified options are:

- compare k at fixed winding: no angular phase difference (v15.692);
- compare the pair product p across EM and gravity: requires a sector-identification rule (v15.692);
- pull chi onto factor pairs: requires a shell-state dictionary (v15.693);
- use a quarter-period phase: requires selection of a physical fractional translation, coherent source and readout (this gate).

**Verdict:** no new dimensionless, G-free **local gravitational observable** follows solely from the quarter pair quantum and existing Fourier/holonomy identities. This is a scoped negative, not a denial of the exact quantization or its future use if an independently derived source/field map appears.

**Reproducibility:** research-notes/taubnut_fourier_scale_phase_v15_694.py, additive commit d6f8ed811b03e858d7d80ea6533488cf3b875cac. Locally run PASS for the energy/period relation, p_G=k/4, exact rescaling, full-period identity and fractional characters r=2,3,4,5,8. No figures generated.

**HANDOFF:** external audit/gravity/sandbox: rederive the Fourier normalization and carefully distinguish fractional time translation from gauge-invariant angular Wilson holonomy, and assess whether any existing gravity source specifically selects T/4. Respect Euclidean-vs-Lorentzian Taub–NUT distinctions.

**NEXT:** begin a consolidated, reference-backed **gravity observable closure matrix**, distinguishing the surviving exact topology and counting structures from conditional physical mechanisms. Focus new research on source-derived field dynamics and a fixed coupling/intertwiner, not on further re-labellings of quarter phases. Preserve open astrophysical and proper-detector-frame alternatives and request external audit of v15.692–694 before promoting any claims.
