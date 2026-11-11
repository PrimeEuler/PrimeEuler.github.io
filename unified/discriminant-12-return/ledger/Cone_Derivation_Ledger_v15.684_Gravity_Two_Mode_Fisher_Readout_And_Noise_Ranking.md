# Cone Derivation Ledger v15.684 — Gravity lane: two-mode Fisher limit, readout noise, and geometry ranking

**Date:** 2026-11-11 US Eastern. **Parents:** v15.682 same-center degenerate Maxwell dispersion discriminator; v15.683 exact swapped-mode slope/overlap tradeoff. **Status:** [D] exact two-mode Gaussian Fisher matrix with unknown common source amplitude marginalized; [D] coherent-amplitude and absolute-power weak-mode limits; [D] correlated log-calibration cancellation; [S] odd-index swapped-family ranking under equal absolute voltage or power noise; [N] the largest algebraic dispersion slope is not the largest statistical information; [O] complete quantum/thermal/amplifier noise model, finite integration bandwidth, K4-consistent elastic walls and source normalization. **Immediately prewrite live HEAD:** f0fbc1cc33e16a96e7e739f611d25fffcd2329f8. Collision searches found no v15.684 ledger entry or prior two-mode Fisher ledger result. Frozen Suzuki certificates and prior audited objects untouched.

**Comparator context:** recent HFGW cavity work already treats multimode cavities as detector arrays and explicitly optimizes geometry for signal-to-noise, so the statistics below are an application of standard estimation logic to the conditional K4 dispersion parameter, not a new readout principle.

## Gate 223 — exact coherent two-mode Fisher information after marginalizing unknown GW amplitude

Let the two calibrated complex-voltage or coherent-amplitude observables be

**y_i = A g_i(u) + n_i,  i=1,2,**

where **u=m_T^2/omega^2** is the small tensor-dispersion parameter, A is an unknown common source amplitude containing the incident strain and other common factors, and independent Gaussian noise has variance sigma_i^2. Around the massless point u=0 write

**g_i(u)=g_i[1+a_i u+O(u^2)].**

The Fisher matrix for theta=(A,u) is

**F_AA = sum_i g_i^2/sigma_i^2,**

**F_Au = A sum_i g_i^2 a_i/sigma_i^2,**

**F_uu = A^2 sum_i g_i^2 a_i^2/sigma_i^2.**

The exact Schur complement after marginalizing the nuisance amplitude A is

**F_u^marg = A^2 g_1^2 g_2^2 (a_1-a_2)^2 /
             (g_1^2 sigma_2^2 + g_2^2 sigma_1^2).**

Define the individual coherent SNRs

**rho_i = A |g_i|/sigma_i**

and the logarithmic ratio slope

**alpha = a_1-a_2.**

Then

**F_u^marg = alpha^2 rho_1^2 rho_2^2/(rho_1^2+rho_2^2),**

so the Cramer-Rao uncertainty is

**sigma_u = (1/|alpha|) sqrt(rho_1^(-2)+rho_2^(-2)).**

This is the statistically correct version of the v15.683 tradeoff. If one mode is much weaker,

**rho_weak << rho_strong  =>  sigma_u ~= 1/(|alpha| rho_weak).**

Therefore a divergent normalized ratio slope is useless if it is achieved by driving the reference-mode SNR to zero.

For equal absolute coherent-voltage noise and otherwise equal readout factors, **rho_weak proportional to g_weak**, so the leading geometry figure of merit scales as

**|alpha| g_weak.**

This validates the scaling of the deliberately heuristic v15.683 proxy in the coherent-readout limit.

## Gate 224 — direct power readout penalizes the weak overlap more strongly

For an incoherent/direct power measurement write

**p_i = P0 g_i(u)^2 + epsilon_i,**

with unknown common power scale P0 and independent absolute power-noise standard deviation tau_i. The logarithmic response slope is **2a_i**. Define each mode's power SNR

**varrho_i = P0 g_i^2/tau_i.**

Repeating the same nuisance-amplitude marginalization gives

**sigma_u^(P) = (1/(2|alpha|))
                sqrt(varrho_1^(-2)+varrho_2^(-2)).**

In the weak-mode limit,

**sigma_u^(P) ~= 1/(2|alpha| varrho_weak).**

If the absolute power noise is equal between modes, **varrho_weak proportional to g_weak^2**, so the geometry figure of merit becomes

**|alpha| g_weak^2.**

Thus readout architecture changes the preferred cavity geometry. One must not optimize the overlap ratio or alpha in isolation.

## Gate 225 — common multiplicative calibration noise cancels in the ratio

Let the measured logarithmic amplitudes have calibration/noise standard deviations s_1,s_2 and correlation coefficient c. For the log ratio

**q = ln s_1^(meas) - ln s_2^(meas),**

the variance is

**Var(q)=s_1^2+s_2^2-2c s_1 s_2.**

The amplitude-ratio signal is **delta q = alpha u**, so

**sigma_u = sqrt[Var(q)]/|alpha|.**

For power ratios the slope is **2alpha**, hence the denominator is **2|alpha|**. Exactly common multiplicative calibration errors, c=1 and s_1=s_2, cancel. Differential mode calibration, amplifier-chain mismatch, detuning, Q drift and independent noise do not.

This identifies the practical attraction of same-cavity degenerate modes: they can share substantial environmental and calibration systematics while retaining different geometry slopes.

## Gate 226 — the statistically preferred swapped pair depends on readout

Use the exact v15.683 odd swapped family below index 100. With equal absolute coherent-voltage noise, rank by **|alpha| g_weak**. The leading entries are:

- **(3,1)/(1,3):** 6.72882409e-2;
- **(5,3)/(3,5):** 4.53861221e-2;
- **(7,3)/(3,7):** 3.07072487e-2;
- **(5,1)/(1,5):** 2.50733837e-2.

So the low-order **(3,1)/(1,3)** pair is best within this restricted family for coherent readout.

With equal absolute power noise, rank instead by **|alpha| g_weak^2**. The leading entries are:

- **(5,3)/(3,5):** 8.51980730e-4;
- **(3,1)/(1,3):** 5.09367078e-4;
- **(7,3)/(3,7):** 1.79238961e-4.

The optimum changes to **(5,3)/(3,5)** because the very weak (1,3) reference channel of the (3,1) pair is penalized quadratically in direct power SNR.

This scan is not a detector optimization: it omits mode-dependent Q, coupling port efficiency, system noise temperature, bandwidth/integration time, near-degenerate mode mixing, elastic-wall contamination and amplifier correlations. Its role is to replace the misleading “maximize alpha” rule by the correct first statistical criterion.

## Verdict

The same-center multimode dispersion observable from v15.682 survives a proper nuisance-amplitude treatment. The useful information is controlled by the **difference of logarithmic dispersion slopes times the SNR of the weaker channel**, not by the raw ratio coefficient alone.

This is a positive engineering result and a negative novelty result. It shows how one could measure a generic non-null tensor dispersion without knowing the absolute incident strain, but it still does not derive a Cone-specific strength, eta, source frequency or quarter-grid temporal selector. For the conditional K4 identification

**u=(8 eta/3)(H/omega)^2,**

the experiment would measure u first; interpreting it as eta/H/K4 remains a separate gravitational-model step.

**Reproducibility:** research-notes/degenerate_mode_fisher_readout_v15_684.py, additive commit f0fbc1cc33e16a96e7e739f611d25fffcd2329f8. The script symbolically verifies the Fisher Schur complement, coherent and power uncertainty formulas, correlated log-calibration cancellation, and the readout-dependent ranking of odd swapped modes below 100. No figures and no protected Suzuki modifications.

**HANDOFF:** independent audit/sandbox/gravity should verify the Fisher marginalization, especially the distinction between coherent-amplitude SNR rho and absolute-power SNR varrho; confirm the correlated-log ratio variance; and independently reproduce the mode ranking. Do not treat the equal-noise scan as an experimental sensitivity forecast.

**NEXT:** test the actual scale of the conditional K4 parameter. First verify from the certified K4 tensor ledger that the H appearing in **m_T^2=(8 eta/3)H^2** is the cosmological background Hubble rate in the local-WKB derivation rather than a free local pump rate. If yes, quantify u across realistic cavity and heterodyne GW frequencies and ask whether difference-frequency/near-degenerate readout can reduce the relevant omega without violating the propagating-WKB assumptions. This decides whether the G-free discriminator is merely formal or has any plausible laboratory window.
