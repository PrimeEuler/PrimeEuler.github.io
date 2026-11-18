# Cone Derivation Ledger v15.1149 — Finite-temperature and mechanical-loss limits of the paired-Jxy torsion revival

**Date:** 2026-11-18 Eastern. **Lane:** Gravity/Cone. **Classification:** [D/C] exact dephasing in an explicitly assumed stationary **Gaussian weak-damping oscillator correlation model**, including lossless thermal limit, positive incomplete finite-Q revival and first-order small-damping expansion; [D/C] nonzero finite-force phase accumulation for an underdamped torsional actuator; [N] no universal perfect thermal revival in an open lossy device, no physically selected frequency or new gravitational response beyond ordinary spin–oscillator theory; [O] fully microscopic thermal bath / noise-qualified field detector and matched K4 tensor-source comparison. **Immediately pre-ledger live HEAD:** c390c1b6160a1dd09b48c07b5926e8bae700f30b. Target v15.1149 collision-free; additive-only; no changes to active Suzuki far-tail/Lane A, Audit, Sandbox, Muse or historical certified objects.

## Parent, audit and scope
Gravity v15.1147 (script 73009c401835906d4b798f0c415775c7cecbd2c3, ledger a781d0242974c9f924abce04808a1ec8b12600f8) found the exact 54.7356103°=arctan√2 magic-angle *numerical/geometric* coincidence and a conventional spin–torsion Hamiltonian. Gravity v15.1148 (script 72cc6d0072345056738984879123a1bc2024bf76, ledger 74724a4dac305602bbd3fa451f3879fffb1dc53f) found a nonzero accumulated gravity-driven spin phase exactly at a perfect **closed** harmonic spin–oscillator recurrence. External Audit Round 600/v15.1133 independently verified previous v15.1131–1132, and latest HEAD before this gate includes active Lane A tiled R4 certification and external Audit Round 603/v15.1145 plus v15.1146 liveness. No intervening Gravity correction was found. This gate tests the central missing realism, with **explicit model assumptions**, not a claim of arbitrary exact quantum Brownian dynamics.

## Gate 1048 — stationary weak-damping Gaussian oscillator model and exact contrast
With the relative Zeeman coupling kΩ q(t) to paired spin phase, take an oscillator of mechanical inertia I, damped oscillation frequency ω, amplitude decay λ>0, and stationary thermal occupancy nbar. Specify, rather than derive from Cone, the **symmetrized** oscillator position autocorrelation of a weakly damped quantum optical/rotating-wave Markov oscillator:
**C_q(u)= ℏ(2nbar+1)/(2Iω) exp(−λ|u|) cos(ωu)**.
This is a valid positive Gaussian stationary correlation in the model, and its classical stochastic phase integral is Gaussian. For a spin relative phase φ=kΩ ∫_0^t q(s)ds, the normalized phase-coherence contrast is
**V(t)=exp[−(kΩ²/2) Var(∫_0^t q(s)ds)]**
=**exp[−kΩ² ℏ(2nbar+1)/(2Iω) J(t)]**,
where
**J(t)=∫_0^t (t−u)e^(−λu) cos(ωu)du**
=**Re[t/(λ−iω)−(1−e^(−(λ−iω)t))/(λ−iω)²]**.
This is a *specified Gaussian covariance influence model*. The same symmetrized thermal correlator is obtainable in the weak-coupling quantum-noise treatment of a damped harmonic mode; a full bath-dependent fluctuation/dissipation kernel and possible extra renormalization must be supplied for arbitrary friction/memory. No assertion is made that one scalar `e^(−λu)cosωu` is the exact correlator of a general damped classical elastic body.

## Gate 1049 — closed thermal limit and first-revival Q law
At λ=0, **J(t)=(1−cosωt)/ω²**, yielding the old spin-coherent contrast multiplied by the thermal factor
**V_closed,thermal(t)=exp[−(2nbar+1) r sin²(ωt/2)]**, with
**r=ℏ kΩ²/(Iω³)**.
Therefore a finite temperature increases the *between-revival* dephasing, but **the closed, exactly harmonic** system still has unit visibility at t=2πn/ω regardless of nbar. This is a special ideal harmonic recurrence, not a generic thermal robust sensor.
For finite weak damping, define the mechanical quality factor **Q=ω/(2λ)** and first near-period T=2π/ω. The exact Gaussian-integral evaluation is
**ω² J(T)= [2πx/(1+x²)] + [(1−e^(−2πx))(1−x²)/(1+x²)²]**, x=λ/ω=1/(2Q).
For x≪1, **J(T)=4πλ/ω³+O(λ²)** and
**−log V(T)=π r(2nbar+1)/Q+O(Q^(−2))**.
This is the precise quantitative obstruction to *perfect* revival once information is lost to the modeled mechanical bath.
For a thermal harmonic oscillator **2nbar+1=coth[ℏω/(2k_B T)]**, which becomes ≈2k_B T/(ℏω) in the high-temperature limit. Thus the first-revival loss scales like thermal occupation divided by Q times the spin–torsion coupling r. This dependence follows standard oscillator noise and is not selected by Cone geometry.

## Gate 1050 — explicit dimensionless numerical controls
For illustration only set ω=1 in normalized units and **r=0.1**. Exact numerical Gaussian integration, independently compared with SciPy quadrature for λ=0,.002,.01,.05,.2 and t=.6,1.3,2π,4π, gave agreement <10^−9 throughout. Values of **V(T=2π)** are:
Q=30: nbar=0 -> 0.989850310; nbar=1 -> 0.969858932; nbar=10 -> 0.807160666.
Q=100: nbar=0 -> 0.996887833; nbar=1 -> 0.990692526; nbar=10 -> 0.936638933.
Q=1000: nbar=0 -> 0.999686137; nbar=1 -> 0.999058705; nbar=10 -> 0.993429515.
These are **not measured noise or real sensor estimates**. They quantify why low mechanical loss and low thermal occupation matter if one wants to use the standard coherent-revival operating point. External spin decoherence would multiply V by an independent visibility factor such as exp(−T/T2) if appropriate under separately specified noise assumptions.

## Gate 1051 — a damped gravitational force still accumulates Ramsey phase
For a constant gravitational tidal force/torque F_g coupled linearly to the torsional coordinate q, use the standard deterministic damped equation
**I q¨+2Iλ q˙+Iω_0² q=F_g**, q(0)=q˙(0)=0, with **ω_d=sqrt(ω_0²−λ²)>0**.
Its exact solution is
**q_g(t)=F_g/(Iω_0²){1−e^(−λt)[cos(ω_d t)+(λ/ω_d)sin(ω_d t)]}**.
The spin phase is **φ_g(t)=kΩ ∫_0^t q_g(s)ds**. For F_g kΩ≠0 and the stated underdamped time range, it remains nonzero at t=2π/ω_d, even though the associated spin coherence visibility is now <1. This is conventional forced-oscillator phase integration; no natural tidal coupling coefficient is fixed by the Cone.

## Verdict and reproducibility
Positive: the ideal periodic backaction cancellation is a valid closed-oscillator limit and survives *purely thermal initial states* if there is no dissipation, but under a concrete stationary damped Gaussian model the visibility is exponentially suppressed by r(2nbar+1)/Q at first revival. A constant tidal torque still writes a nonzero spin phase into a damped apparatus. Negative: these standard spin-oscillator equations do not validate a selected action-circle clock, intrinsic gravitational frequency, new SU(2) generator or G-independent source. They describe a calibration tradeoff in an explicitly assumed material/readout setup.

Canonical locally executed source `research-notes/k4_bicone_thermal_damping_revival_v15_1149.py` uploaded additively as **c390c1b6160a1dd09b48c07b5926e8bae700f30b**; every exact symbolic assertion and independent analytic-vs-numeric quadrature test passed. The complete equivalent local script was executed before GitHub upload. Independent Audit pending.
**AUDIT HANDOFF:** verify Gaussian correlation assumptions/normalization, integral J(t), thermal/zero-loss limit and coefficient π/Q, Q convention Q=ω/(2λ), numeric sample grid, deterministic forced damped response and maintained spin phase, and the difference between a stationary Gaussian dephasing comparator and a fully microscopic FDT-consistent Brownian device. No changes or handoff compute requests to active Suzuki Lane A.
**NEXT:** insert realistic room-temperature oscillator parameters, finite pair T2 and measured mechanical/magnetic noise spectra only when independently available; distinguish between torque readout and intrinsic tidal K4 source. The only decisive new-gravity gate remains a parameter-free residual relative to conventional Einstein–Maxwell+material with an independently justified Cone source operator.
