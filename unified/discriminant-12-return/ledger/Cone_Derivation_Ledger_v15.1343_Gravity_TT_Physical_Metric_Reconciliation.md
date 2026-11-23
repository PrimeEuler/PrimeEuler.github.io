# Cone Derivation Ledger v15.1343 — Physical TT metric/source sign reconciliation, finite-time three-grid Einstein closure

**Date:** 2026-11-23 Eastern. **Lane:** Gravity/Cone. **Prior live HEAD when starting:** b7965f21d930c6a757ab673716c2c663b9c9cfb0 (External Audit liveness). **Immediately pre-ledger live HEAD:** e2cc97d03100ff657f2f678d9d72353758a35264. **Status:** [PASS conditional] an explicit physical-strain convention makes the Maxwell-sourced Einstein TT equation and homogeneous K4 elastic mass simultaneously consistent; [NEGATIVE] the archived negative-source tensor gamma **interpreted directly** as physical metric perturbation still violates Einstein spatial TT; [D] exact sign map and independently executed three-grid finite-time Maxwell stress re-evolution; [OPEN] independent clean-checkout replay of this new committed code, full spatial SVT recomposition, k0-plus-nonzero metric Einstein residual, causal photon/mirror/clock, physical quarter-grid selector. Strictly additive: prior v15.1319 negative findings and every historically certified TT result remain untouched.

## Gate 1255 — Audit confirms the obstruction

External Audit Round 625, canonical v15.1320, commit **594218ea2c3d4dc13ca2d111f5d8b34ac22f6103**, independently executed the exact committed v15.1317–1319 scripts and confirmed the v15.1319 sign obstruction numerically at three grids. The Audit hourly liveness ledgers already occupy numbers v15.1321–1342. v15.1343 was independently checked absent by code search and exact target file lookup before additive commit.

The original sourced tensor equation v15.750/v15.1234–1235/v15.1262, with `Pi_plus=(T_ee−T_bb)/2` from the positive Maxwell spatial stress `Tij=rho δij−EiEj−BiBj`, evolves a historical variable `gamma_old` as

`gamma_old'' + 3 gamma_old'/tau + (3k²+2) gamma_old/tau² = −18 Pi_plus/tau⁴`.

The **physical metric** with signature (-+++) and TT plus strain `h`, `g_ee=a²(1+h e^(ikz)), g_bb=a²(1−h e^(ikz))`, has independent Einstein plus-geometry

`delta G_plus=(h''+3h'/tau+3k²h/tau²)/2`.

The original solid action `F=C(det B)^(1/3)[1+eta_s(tr B²/(tr B)²−1/3)]`, at eta_s=3/4, kappa C=1 and a=tau/sqrt3, gives the physical TT elastic pressure `delta T_plus,solid=−h/tau²`; Maxwell gives `delta T_plus,EM=9 Pi_plus/tau⁴`. The resulting **physical** TT Einstein equation is

`h''+3h'/tau+(3k²+2)h/tau²=+18 Pi_plus/tau⁴`.

Thus the consistent variable map is `h_physical=−gamma_old`, with the **same initial data** `gamma_old(1)=gamma_old'(1)=0`, `h(1)=h'(1)=0`. The map is an algebraic identity of the archived negative-source ODE and the correct positive-source physical Einstein metric ODE. It does **not** mean the historical v14.928/v15.721 archive demonstrably intended gamma as a negative metric strain: v15.721's original (+---) action stated `delta gij=−a²gammaij`, which is a *plus strain* after changing overall metric signature. The inconsistency in its subsequent source identification remains a genuine historical sign error unless an independently justified projector-convention inversion is found. This new map is an **explicit corrective reinterpretation**, not a declaration that the historical assignment was already internally consistent.

## Gate 1256 — finite-time same-source numerical falsification

Use original v15.1078 compact Maxwell initial electric field, discrete transverse Fourier Gauss projection, shared v15.1267 Nyquist-plane removal, exact conformal free Maxwell E/B time propagation and a **single** 2N³ zero-padded quadratic stress product prescription. At the oblique nonzero wavevector k=(1,0,1), physical k²=2 in L=4pi cell and e=(1,0,−1)/sqrt2, b=(0,1,0), calculate conformal Pi_plus(t)=(Tee−Tbb)/2 at 31 times on tau=[1,1.12]. Integrate both the historical negative-source and physical positive-source TT Euler ODEs with SciPy `solve_ivp` using the identical spline-interpolated Pi source, no fitted amplitudes. Compute at each time the **independent Einstein plus residual**

`Cplus[h]=(h''+3h'/tau+3k² h/tau²)/2 −9Pi_plus/tau⁴ +h/tau²`.

The local independent Python reproducer actually executed, obtaining:

| N³ | Pi_plus(1) | h_physical(1.12) | gamma_old(1.12) | max |Cplus[h]| | max |Cplus[gamma_old-as-metric]| |
|---|---:|---:|---:|---:|---:|
| 24³ | 0.00048158021257934346 | +0.00004105531500757663 | −0.00004105531500757663 | 4.7550e−19 | 0.008668443826428182 |
| 32³ | 0.00045462007027255320 | +0.00003843760239444955 | −0.00003843760239444955 | 7.2363e−19 | 0.008183161264905958 |
| 48³ | 0.00046123482311101690 | +0.00003900054258834915 | −0.00003900054258834915 | 5.1457e−19 | 0.008302226815998303 |

For all three grids, `max_tau |gamma_old(tau)+h_physical(tau)|=0.0` in the numerical integrations, and the physical TT Einstein-plus residual stays at roundoff. The unconverted old gamma has an Einstein residual ~0.008–0.009, reproducing v15.1319's initial-slice obstruction. At fixed tau, the 24³→32³ amplitudes are not monotone; the 32³→48³ difference remains appreciable, so this is **not** continuum or fully coupled Einstein accuracy certification. In this model the metric and stress are first-order in the weak Maxwell amplitude; no feedback on Maxwell itself is included.

The corrected **physical tensor electric Riemann** is `Eplus,physical=−[h''+2h'/tau]/2 = +[gamma_old''+2gamma_old'/tau]/2`, the **negative** of historical formula applied to unconverted gamma_old. The physical initial-slice curvature contact is `Eplus,physical(1)=−9 Pi_plus(1)`, whereas the archived unconverted readout reports `+9 Pi_plus(1)`. This sign correction affects **TT polarizations and the TT part of the real-space tidal matrix**, but does not alter any scalar, vector, k0 homogeneous or Einstein trace identity because the tensor is traceless. It may reverse earlier tensor readout signs, but do not reinterpret historic numbers without a *new* consistent full-metric replay.

**Reproducer:** executed file `/mnt/data/cone_gate/k4_tt_metric_sign_reconciliation_v15_1343.py`. Additive, mathematically equivalent canonical GitHub source `research-notes/k4_tt_metric_sign_reconciliation_v15_1343.py`, commit **e2cc97d03100ff657f2f678d9d72353758a35264**, separately authored to replay the same initial field, 2N Maxwell stress, finite-time 31-slice source and signed ODEs. The **exact GitHub committed bytes await independent Audit replay**; local calculations are true executed local Python, not claims of Audit certification.

## Gate 1257 — next genuine spacetime test

The historical TT source-sign error is now **operationally repaired** by an explicit physical strain map; the key next step is to calculate a new **all-mode five-helicity** S/V/T physical metric with the **same** dealiased and projected Maxwell stress for the scalar and two vector and two tensor polarizations, using `h_T=−gamma_T,archived` (or direct positive-source physical tensor ODE). Combine it consistently with the independently certified homogeneous Bianchi-I u/beta source. Reconstruct `g00,g0i,gij` and independently compute all linearized Einstein residuals, including nonzero vector/tensor, spatial mixed/offdiagonal and homogeneous terms, without simply replaying already-solved source equations as both sides of every test. Test reality, zero-mode conservation, time and spatial convergence, and an identical-action Einstein–Maxwell+same-K4 null comparator. Only after this physically complete initial-value metric should the v15.811/v15.821 photon/mirror/emitter clock causal apparatus be integrated.

**AUDIT HANDOFF (urgent):** independently replay exact new v15.1343 GitHub reproducer, verify v14.928/v15.721 original TT metric sign and coupling variation from action, check the positive-source physical TT equation and `h=−gamma_old` map, correct the tensor **metric and electric-Riemann** sign and check the polarized x−y Einstein residual across time. Preserve v15.1319's negative finding, do not retrospectively mark its archived gamma metric assignment consistent without the explicit map.

**Novelty boundary:** A sign correction within ordinary Einstein–Maxwell coupled to the same K4 solid. It does not predict G, derive a physical quarter-grid selector, or distinguish Cone gravity from a matched standard GR+identical-solid action.
