# Cone Derivation Ledger v15.683 — Gravity lane: degenerate-mode dispersion slope versus overlap tradeoff

**Date:** 2026-11-11 US Eastern. **Parent:** v15.682 same-center degenerate PEC Maxwell dispersion discriminator. **Status:** [D] exact swapped-mode family and quadratic dispersion coefficient; [D] asymptotic large-coefficient/vanishing-reference-overlap tradeoff; [S] finite odd-index geometry scan and simple overlap-weighted proxy; [N] no free sensitivity amplification from ratio poles; [O] detector-noise/Q/readout Fisher calculation and K4-consistent wall dynamics. **Immediately prewrite live HEAD:** 252ae6d7b56a5a0ef99cd0c10d3645b61740c20a. Collision searches found no v15.683 ledger or prior “dispersion slope” ledger entry. Frozen Suzuki certificates and prior audited objects untouched.

**Literature context:** multimode cavity readout is already conventional HFGW engineering rather than a Cone-specific construction. Blas, Chen, Liu, Shang and Shu (2026), arXiv:2601.03341, use many nearly-degenerate modes of one cavity as an effective detector array to recover wave properties. Navarro et al., arXiv:2312.02270, study simultaneous degenerate modes of cubic microwave cavities. Fischer, Hillert, Krokotsch and Moortgat-Pick (2026), arXiv:2608.29293, explicitly optimize cavity geometry and show that geometry choice materially changes HFGW signal-to-noise. The result below is therefore a conditional dispersion application of established multimode/geometry ideas, not a claim of a new cavity-detection principle.

## Gate 219 — every swapped odd-index pair gives an exact degenerate discriminator family

Continue the centered PEC cube and cross-polarized magnetostatic TT source from v15.682. For odd positive integers m,n, use

**E_mn = 2 zhat cos(mx) cos(ny)**

with

**omega_mn^2 = N = m^2+n^2.**

The swapped mode **E_nm** is exactly degenerate in the same cavity. At the ordinary massless point K^2=N, the exact geometry overlap from v15.682 has magnitude

**g_mn = |G_mn| = [8m/(pi^2 n^3)] |cos(pi sqrt(N)/2)|.**

Therefore the massless overlap ratio for the ordered pair (m,n)/(n,m) is simply

**R0 = g_mn/g_nm = (m/n)^4.**

Let a timelike prescribed tensor have

**K^2=N(1-u), u=m_T^2/omega^2.**

Normalize the overlap ratio to its massless value. Exact cancellation of the common plane-wave and cavity factors gives

**D_mn(u) = [1-(N/m^2)u]/[1-(N/n^2)u].**

Hence

**D_mn(u)=1+alpha_mn u+O(u^2),**

with the exact quadratic-dispersion coefficient

**alpha_mn = N(1/n^2-1/m^2)
          = (m^2+n^2)(m^2-n^2)/(m^2 n^2).**

For m>n this is positive. Unlike the special v15.681 two-length ratio, there is no symmetry forcing alpha to vanish.

## Gate 220 — the coefficient is algebraically unbounded, but the reference overlap collapses

At first sight alpha_mn can be made arbitrarily large by taking m>>n. That is not a free experimental enhancement.

Fix odd n and let odd m become large. Since

**sqrt(m^2+n^2)-m = n^2/[sqrt(m^2+n^2)+m] ~ n^2/(2m),**

and m is odd,

**|cos(pi sqrt(N)/2)| ~ pi n^2/(4m).**

Therefore the two massless overlaps have sharply different limits:

**g_mn -> 2/(pi n),**

**g_nm ~ 2 n^3/(pi m^4).**

Meanwhile

**alpha_mn ~ m^2/n^2.**

Thus

**alpha_mn g_nm ~ 2n/(pi m^2) -> 0.**

So the formal dispersion coefficient can grow without bound only while one member of the ratio becomes a vanishingly weak reference channel. Any practical requirement that both massless overlaps stay above a fixed nonzero floor cuts off this large-alpha limit. The ratio pole is therefore an engineering ill-conditioning, not a free physical gain.

## Gate 221 — low-order tradeoff examples

The exact/numerical reproducer scans odd indices below 100. Representative swapped pairs are:

- **(3,1)/(1,3):** alpha=80/9=8.888888889, g_strong=0.613164095, g_weak=0.00756992710, R0=81.
- **(5,3)/(3,5):** alpha=544/225=2.417777778, g_strong=0.144844395, g_weak=0.0187718336, R0=625/81=7.71604938.
- **(5,1)/(1,5):** alpha=24.96, g_weak=0.00100454262, R0=625.
- **(7,1)/(1,7):** alpha=48.97959184, g_weak=0.000263261010, R0=2401.

As a deliberately crude geometry-only diagnostic, define **alpha min(g_a,g_b)**. This is **not** a detector SNR or statistical sensitivity; it only penalizes large ratio slope by the weaker overlap. In the scan m,n<100, the low-order (3,1)/(1,3) pair gives the largest value of this simple proxy among the swapped family. The result warns against choosing extreme indices solely to maximize alpha.

## Gate 222 — novelty and design verdict

The positive v15.682 result survives: same-center multimode geometry can give a translation-invariant O(m_T^2/omega^2) dispersion discriminator. Gate 220 adds the missing engineering constraint: **the coefficient alone is the wrong optimization target**.

This also sharpens the novelty classification. Multimode HFGW reconstruction, degenerate cubic-cavity modes and geometry optimization already exist in the literature. What is specific to the present Cone/K4 lane is only the conditional question “how would a non-null K4 tensor dispersion deform calibrated multimode overlaps?” That remains useful, but it is not a new detector mechanism and it does not derive the K4 dispersion scale from the Cone quarter/half mesh.

For the conditional K4 substitution **u=(8 eta/3)(H/omega)^2**, the swapped-pair leading shift is

**D_mn-1 = (8 eta/3) alpha_mn (H/omega)^2 + O[(H/omega)^4].**

The ability to make alpha_mn large does not remove the fundamental (H/omega)^2 suppression because the weak reference mode becomes correspondingly difficult to measure.

**Reproducibility:** research-notes/degenerate_mode_sensitivity_tradeoff_v15_683.py, commit 252ae6d7b56a5a0ef99cd0c10d3645b61740c20a. It verifies the exact alpha formula, low-order rational examples, scans odd swapped pairs below 100, and numerically checks the fixed-n large-m asymptotics with m=9999. No figures and no protected Suzuki modifications.

**HANDOFF:** independent audit/sandbox/gravity should verify the swapped-family exact ratio, the large-m overlap asymptotics, and the interpretation that a divergent normalized slope is ill-conditioned because one baseline coupling vanishes. The alpha*min(g) scan is explicitly a heuristic geometry proxy and must not be promoted to an experimental sensitivity.

**NEXT:** replace the heuristic proxy by a measurement model. Starting from the calibrated powers **C_n=P_n Q_n^ext/(omega_n Q_n^2)**, derive the uncertainty/Fisher information for **u=m_T^2/omega^2** from two-mode power or complex-voltage readout, including independent versus common-mode calibration noise. This will determine the correct dependence on g_weak, Q, integration time and amplifier noise, and will tell whether any low-order pair is genuinely useful before investing in a full K4 elastic-boundary calculation.
