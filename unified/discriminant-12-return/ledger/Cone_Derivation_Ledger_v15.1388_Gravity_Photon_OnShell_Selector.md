# Cone Derivation Ledger v15.1388 — Off-shell EM response is not automatic on-shell photon production

**Date:** 2026-11-24 Eastern. **Lane:** Gravity/Cone. **Sources:** v15.1385 Weyl–H² Maxwell Fourier response and v15.1386/1387 sigma kinetic and scale negative gate. **Immediately pre-ledger live master HEAD:** af9e6324c40abdf7029a5a9502d41bb99cf1d87c. **Status:** [D/NEGATIVE] a genuine driven transverse Maxwell Fourier response need not describe freely propagating photons; [N PASS] independent adiabatic switching experiment and exact analytic spectral prediction; [OPEN] finite wave-packet radiation, full coupled stress, cone-only coupling selector. Additive, freeze prior archives. Earlier v15.1385 use of the phrase "radiates a transverse Maxwell Fourier mode" should be read as a *driven transverse polarization*, not as independently established outgoing real-photon radiation.

## Gate 1302 — photon mass shell and Fourier branch

The chosen v15.1385 Weyl–Maxwell–H² source at leading amplitude g_eff produces J^mu ∝(1,1,1,1) sin(2t−x−y) cos(t−z). Its exact trig split gives branch (omega+,q+)=(3,(1,1,1)) and branch (omega−,q−)=(1,(1,1,−1)). The first is spatially longitudinal: P_T(q+)(1,1,1)=0. The second has P_T(q−)(1,1,1)=(2/3,2/3,4/3) ≠0, but **omega−²−|q−|²=−2**, whereas a free physical vacuum Maxwell photon must satisfy omega²=|q|². Thus the specific indefinitely monochromatic, spatially infinite branch is a **nonresonant forced electromagnetic polarization**, not automatically a free radiative photon. This refines, not invalidates, v15.1385's correct Green/ODE driven-field result.

## Gate 1302b — switching-generated free modes versus steady forced field

Consider a single transverse Fourier eigenmode A(t) in Lorenz gauge with k=√3, drive frequency omega=1, arbitrary illustrative g_eff=.02 and complex current amplitude J0=i g_eff |P_T j|/4. Turn on its forcing smoothly via s_T(t)=[1+tanh(t/T)]/2, integrate

A''+k² A=−J0 s_T(t)e^(−i omega t)

from near-zero t=−12T to t=+12T, with zero A and A' at start. At the final time, separate off the *persistent forced particular* A_p=−J0e^(−i omega t)/(k²−omega²), and measure the residual free oscillator energy E_free=(|A_free'|²+k²|A_free|²)/2. Independent analytic Fourier transform of s_T'(t)=sech²(t/T)/(2T) yields FT(delta)=[πdelta T/2]/sinh[πdelta T/2]. The free mode energy predicted from positive/negative free frequencies matches the ODE value with relative discrepancy ≤1.5e−8 for these runs, checking the decomposition independently.

Actually executed SciPy/NumPy local Python at `/mnt/data/cone_gate/k4_quarter_weyl_photon_shell_selector_v15_1388.py`:

| switching T | free-mode energy | steady forced-mode energy | ratio |
|---|---:|---:|---:|
| 0.5 | 2.84671592315546e−5 | 3.33333333333333e−5 | .854014776946638 |
| 1 | 2.040777291665417e−5 | 3.33333333333333e−5 | .612233187499625 |
| 2 | 6.751540395555293e−6 | 3.33333333333333e−5 | .202546211866659 |
| 4 | 2.661859081601047e−7 | 3.33333333333333e−5 | .007985577244803 |
| 8 | 1.076430482335932e−10 | 3.33333333333333e−5 | 3.229291447007794e−6 |

The transient free component can be suppressed arbitrarily by sufficiently slow, adiabatic switch-on in this off-resonant ideal oscillator, while the nonzero forced polarization persists. Therefore v15.1385 showed a valid curvature-sourced EM response but not a demonstrated *steady emitted photon flux*. Fast-onset finite pulses can generate free modes from their broad temporal spectra; no assertion they are impossible.

**Reproducer:** additive GitHub `research-notes/k4_quarter_weyl_photon_shell_selector_v15_1388.py` SHA **1a05938a940ad201443746ddb77dbcfe94762308**. The local file above was actually run, and the separately authored committed script uses the same mathematical tests. **Exact GitHub committed-byte Audit replay pending**.

**Audit:** independently check on-shell dispersion, both transverse projectors, analytic tanh-switch FT and negative/positive frequency contributions, energy definition and fixed-background scope; label any discrepancy additively. The absence of on-shell photons in **this one geometry** must not be elevated to a universal no-go for the chosen Weyl–H² interaction.

**NEXT:** search for a kinematically **phase-matched on-shell** 3-wave mixing configuration with genuine transverse current. Then verify analytic retarded resonance, independent ODE, and record unavoidable finite wave packet/backreaction and free coupling caveats. This is implemented separately by v15.1389.
