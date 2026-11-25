# Cone Derivation Ledger v15.1470 — Fully nonlinear Einstein–H² homogeneous harmonic-time benchmark with independently evolved lapse and H

**Date:** 2026-11-25. **Lane:** Gravity/Cone main numerical-relativity thread. **Status:** [EXACT] homogeneous massless curved-H² kinetic sigma in 3+1 flat FLRW has explicit harmonic-coordinate time a³(s)=exp(Bs), lapse α(s)=a³(s), B=sqrt(3κC/(2f²)); [NUMERICAL PASS] evolve *independently* seven real degrees (a,α,H,φu,φv,pu,pv) with Raychaudhuri and curved target Hamilton equations, and independently monitor the lapse harmonic relation, Friedmann constraint, exact a³, and sigma invariant. [SCOPE] nonlinear homogeneous gauge-and-matter benchmark, NOT yet the desired inhomogeneous 3D generalized-harmonic Einstein–H² evolution; Weyl–Maxwell still omitted and κ is input. Parent v15.1454 standard proper-time FLRW, v15.1456 independent acceleration, v15.1466 linear GH wave, v15.1468 initial GH gauge. Independent Audit pending.

## Gate 1396 — exact harmonic-time cosmology

The FRW spatial metric γij=a²δij and Kij=−(a_τ/a)γij have K=−3H, where τ denotes proper cosmic time. Introduce harmonic time s with ds=dτ/a³. In harmonic coordinates α=dτ/ds=a³, β=0, so dot_s α=−α²K=3α²H. The curved H² target metric is GAB=δAB−φAφB/(1+φ²), inverse G^AB=δAB+φAφB. With comoving conjugate pA=a³ f² GAB dφB/dτ, the conserved internal kinetic invariant is C=p²+(φ·p)². Thus ρ=C/(2f² a⁶) and H²=κρ/3, with the independent Raychaudhuri evolution dH/dτ=−κρ.

The full independent ODE system in harmonic s is
da/ds=α a H; dα/ds=3α² H; dH/ds=−α κρ;
dφA/ds=α[pA+φA(φ·p)]/(a³ f²);
dpA/ds=−α(φ·p)pA/(a³ f²).

Initial values a=α=1, φ=(.15,−.08), p=(.12,.07), H(0)=sqrt(κ C0/(6f²)). The independent exact comparator follows from proper-time a³(τ)=1+Bτ and ds=dτ/a³: a³(s)=exp(Bs), α=a³(s), H(s)=B/[3a³(s)], where B=sqrt(3κ C0/(2f²)). The numerical integration DOES NOT impose α=a³ or the Friedmann relation inside its RHS, and checks both afterward. This is a useful nonlinear harmonic-gauge *benchmark* that the future 3+1 GH code should reproduce in its homogeneous sector.

## Actual independent numerical tests

**Executed locally** \`/mnt/data/cone_gate/gh_h2_flrw_harmonic_time_v15_1470.py\` via DOP853 (rtol=1e−12 atol=2e−14) on s∈[0,65], sampling 201 points:

| κ | final a | max |α/a³−1| | max normalized Friedmann residual | max relative a³−exp(Bs) | max relative sigma C drift |
|---:|---:|---:|---:|---:|---:|
| .003 | 1.2247315186566787 | 3.66373598e−15 | 7.10760585e−12 | 2.75099499e−13 | 1.36293485e−11 |
| .0015 | 1.1541288933100953 | 9.99200722e−16 | 8.38294592e−12 | 1.26815343e−13 | 1.35637182e−11 |

These checks establish that the *homogeneous nonlinear* Einstein–H² harmonic lapse and matter dynamics are implemented consistently for this benchmark, whereas the previous v15.1466 checked only linear metric waves and v15.1468 only harmonic initial gauge derivatives. This is **not** the same as evolving all 3D γij/Kij plus nonlinear GH gauge. In homogeneous flat FLRW Weyl=0; this model cannot test the local full-Weyl transverse characteristic anomaly v15.1420.

**Additive committed equivalent reproducer:** \`research-notes/k4_h2_gh_flrw_harmonic_time_v15_1470.py\`, SHA **8c28ed8703b20c2e35513fe2172723282d243090**. Exact committed-byte independent Audit pending.

**NEXT MAIN MILESTONE (unchanged):** import the actual v15.1453 nonlinear constrained inhomogeneous 3D Cauchy slice into a *nonlinear generalized-harmonic evolution system* with a hyperbolic metric principal part, Einstein–H² stress and covariant gauge constraints, initialize α and β derivatives by the exact formula v15.1468 and monitor full ADM plus GH constraints and convergence at T=.04 and beyond. Use v15.1463 oversampled Ricci/consistent dealiasing. Only after that restore the complete Weyl–F–H² metric variation under EFT order reduction, returning to causal characteristics and physical observables. v15.1469 quarter-variance susceptibility is an independent Sandbox comparator, NOT a new parameter inserted into Einstein equations. κ is not derived.