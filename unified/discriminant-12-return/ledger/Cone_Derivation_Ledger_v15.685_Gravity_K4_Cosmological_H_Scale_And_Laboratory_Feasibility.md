# Cone Derivation Ledger v15.685 — Gravity lane: certified cosmological-H scale and present-laboratory K4 dispersion feasibility

**Date:** 2026-11-11 US Eastern. **Parents:** v14.928 K4 coupled tensor gate; v14.930 exact K4 tensor evolution; v14.935 full SVT stability return; v15.682 same-center multimode dispersion discriminator; v15.684 two-mode Fisher/readout limit. **Status:** [D] H in m_T^2=(8 eta/3)H^2 is the FLRW cosmological expansion rate of the K4 background, not a free laboratory pump parameter; [D] present-epoch dimensionless dispersion scale across laboratory GW frequencies; [D] Fisher SNR requirement inherited from v15.684; [N] heterodyne/difference-frequency lowering does not produce a plausible present-laboratory K4 window; [C] use of an observed present-day H0 to set the scale because the exact K4 coasting cosmology is itself observationally disfavored; [O] early-universe/astrophysical regime and any independent Cone selector that generates a non-cosmological local scale. **Immediately prewrite live HEAD:** edf15b9d73fe2a9ca8c55ac36f0bfb56137c3f4b. Collision searches found no v15.685 ledger entry. Frozen Suzuki certificates and prior audited objects untouched.

**External scale references:** the 2026 Particle Data Group astrophysical constants table states H0=100 h km s^-1 Mpc^-1, with representative h=0.674(5) from Planck and 0.730(10) from the distance ladder. The April 2026 H0 Distance Network direct result reports H0=73.50 +/- 0.81 km s^-1 Mpc^-1. The numerical reproducer below uses 73.50 only as a present-epoch scale exemplar; it is not a fit of the K4 coasting cosmology. Coupled/heterodyne microwave-cavity GW detectors conventionally resonate when the GW frequency matches a difference between electromagnetic modes, so a difference-frequency route can lower omega_g relative to the microwave carrier but does not change which frequency belongs in the GW dispersion relation.

## Gate 227 — certified meaning of H: cosmological expansion, not local pump rate

Re-read the certified K4 tensor chain rather than inferring H from the later cavity shorthand.

v14.928 begins from the Einstein-Hilbert metric plus the four-factor elastic solid on flat FLRW. It derives

**rho=C/a^2, kappa rho=3H^2, H=dot a/a,**

and for the TT tensor sector

**m_T^2=(8/9) kappa rho eta = (8 eta/3) H^2.**

The same ledger explicitly calls this a **cosmological solid-modified TT mode**, not an empirical graviton mass.

v14.930 then specializes to the exact K4 coasting background

**a=tau/sqrt(3), H=1/tau,**

hence

**m_T^2=8 eta/(3 tau^2).**

External Audit v14.931 independently substituted a=tau/sqrt(3), re-derived H=dot a/a=1/tau, and verified the tensor equation exactly. v14.935 independently recovered the same common gap in the full SVT system,

**m^2=(8 eta/3)H^2.**

Therefore the H appearing in the cavity/K4 conditional substitutions of v15.679-v15.684 is **not** an adjustable local gravitational pump amplitude or an apparatus-dependent H. It is the cosmological FLRW expansion rate of that K4 background.

This closes an ambiguity that mattered enormously for experimental interpretation.

## Gate 228 — present-epoch K4 dispersion is extremely small at laboratory frequencies

For a present-epoch scale estimate only, take the 2026 direct central value

**H0=73.50 km s^-1 Mpc^-1 = 2.38197278e-18 s^-1.**

The stable/sub-luminal K4 window remains

**3/8 < eta <= 3/2.**

Thus

**1 < m_T^2/H^2 <= 4,**

or

**1 < (m_T/H)^2 <= 4**, equivalently **1 < m_T/H <= 2** at the open lower edge.

For a GW angular frequency omega_g=2 pi f_g, define

**u=m_T^2/omega_g^2.**

Then throughout the certified eta window

**(H/omega_g)^2 < u <= 4(H/omega_g)^2.**

Using the observed present-epoch H0 scale gives:

- **f_g=1 mHz:** 1.44e-31 < u <= 5.75e-31;
- **f_g=1 Hz:** 1.44e-37 < u <= 5.75e-37;
- **f_g=1 kHz:** 1.44e-43 < u <= 5.75e-43;
- **f_g=1 MHz:** 1.44e-49 < u <= 5.75e-49;
- **f_g=100 MHz:** 1.44e-53 < u <= 5.75e-53;
- **f_g=1 GHz:** 1.44e-55 < u <= 5.75e-55.

These numbers contain no measured Newton G. Their smallness comes solely from the enormous separation between a cosmological inverse-time scale H0 and any laboratory oscillation frequency.

## Gate 229 — the v15.684 Fisher bound turns the scale separation into an experimental no-go for this route

For the best coherent-voltage swapped pair found in the restricted v15.684 scan, (3,1)/(1,3),

**|alpha|=80/9.**

The favorable weak-mode limit is

**sigma_u ~= 1/(|alpha| rho_weak).**

Even taking the largest K4 mass in the certified eta interval, eta=3/2, a one-sigma measurement of the present-epoch effect would require approximately

**rho_weak >= 1/(|alpha| u_max).**

This gives:

- **1 mHz:** rho_weak >= 1.96e29;
- **1 Hz:** rho_weak >= 1.96e35;
- **1 kHz:** rho_weak >= 1.96e41;
- **1 MHz:** rho_weak >= 1.96e47;
- **100 MHz:** rho_weak >= 1.96e51;
- **1 GHz:** rho_weak >= 1.96e53.

These are already the optimistic coherent-amplitude limits with the strong channel treated as effectively perfect. Direct power readout is more demanding because the weak overlap enters quadratically. Calibration cancellation, higher Q and integration time can improve actual rho, but cannot remove the required inverse-u scaling after the common source amplitude has been marginalized.

Thus the v15.682 G-free dispersion ratio is mathematically clean but **not a plausible present-day laboratory observable of the certified K4 cosmological tensor mass**.

## Gate 230 — heterodyne difference frequency helps algebraically but does not rescue the K4 scale

A two-mode heterodyne detector can use a GW frequency equal to the small difference of two much higher electromagnetic carrier frequencies. This is an important distinction: in the K4 dispersion parameter,

**u=m_T^2/omega_g^2,**

the relevant denominator is the **GW/difference frequency omega_g**, not the microwave carrier frequency.

Therefore heterodyne operation can indeed enlarge u by lowering omega_g. But the cosmological H0 scale is so small that the improvement remains insufficient. Even an extreme illustrative **1 mHz** difference frequency leaves

**u_max ~= 5.75e-31**

and requires the optimistic coherent weak-mode SNR above **1e29**.

Conversely, at the favorable eta=3/2 edge, to obtain:

- **u=1e-24** requires f_g ~= 7.58e-7 Hz, period about 15.3 days;
- **u=1e-18** requires f_g ~= 7.58e-10 Hz, period about 41.8 years;
- **u=1e-12** requires f_g ~= 7.58e-13 Hz, period about 4.18e4 years;
- **u=1e-6** requires f_g ~= 7.58e-16 Hz, period about 4.18e7 years.

The lower-frequency strategy therefore trades an already tiny dispersion shift for increasingly impractical observation/coherence times and ultrafine mode splitting. It does not expose a reasonable laboratory window for the certified present-epoch K4 mass term.

## Verdict — close the present-laboratory K4-mass cavity branch, not cavity GW physics in general

The finite-cavity program produced several real results:

1. a seeded static-B cavity response at omega_g=omega_c;
2. an exact first-order traveling massless 2:1 parametric null in the fixed-wall single-mode toy;
3. a conditional K4 opening of that null;
4. a same-center multimode ratio that cancels unknown strain and retains O(m_T^2/omega_g^2) sensitivity;
5. the correct Fisher/noise tradeoff for measuring that ratio.

Gate 227 now fixes the missing physical scale: **m_T is of order the cosmological Hubble rate.** Once that certified meaning is restored, the present-epoch K4 dispersion shift is many tens of orders below any plausible laboratory cavity ratio measurement.

Accordingly, mark the specific route

**“present-day laboratory cavity detection of the K4 cosmological tensor mass through dispersion”**

as **NEGATIVE / CLOSED ON SCALE**, unless a future gate derives a different local gravitational scale from the theory itself.

This does **not** close:
- ordinary GR/inverse-Gertsenshtein cavity detection;
- multimode HFGW engineering;
- an early-universe or astrophysical K4 propagation test where H was much larger;
- a genuinely new Cone observable if the quarter/half mesh independently derives a local frequency/scale selector.

It specifically prevents us from treating H as an adjustable pump just to make the cavity effect measurable.

**Reproducibility:** research-notes/k4_present_epoch_dispersion_feasibility_v15_685.py, commit edf15b9d73fe2a9ca8c55ac36f0bfb56137c3f4b. It converts the 2026 H0 Distance Network central value to s^-1, evaluates u over 1 mHz–1 GHz, propagates the v15.684 coherent Fisher limit for alpha=80/9, and solves the inverse problem for the GW period needed to reach target u values. No figures and no protected Suzuki modifications.

**HANDOFF:** external audit/gravity should verify (i) the chain v14.928 -> v14.930 -> v14.935 really fixes H as FLRW H; (ii) the H0 unit conversion; (iii) the u and SNR tables; and (iv) the distinction between heterodyne carrier frequency and GW difference frequency. Reject any attempt to replace H by an apparatus rate without a new derivation.

**NEXT:** return to the original Cone question rather than squeezing the cosmological K4 mass. Search for a mechanism in which the quarter-grid/half-grid structure produces a **dimensionless local modulation or mode-selection rule independent of H0**, especially a symmetry/selection rule rather than a tiny mass dispersion. The strongest surviving cavity clue is the exact difference between the seeded omega_g=omega_c conversion channel and the unseeded 2 omega_c parametric channel. Test whether the 1/4 versus 1/2 Cone sectors can derive a temporal or mode-parity selection rule from their existing rotor/ladder operators; if no such derivation exists, record that the attractive “gravity grid pumps EM at the peaks” picture remains analogy rather than physics.
