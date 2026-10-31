# Cone Derivation Ledger v15.192 — Lane A: actual coarse v15.179 pre-screen probe returns INCONCLUSIVE

**Date:** 2026-10-30. **Lane:** A. **Parents:** v15.129, v15.139/141, v15.155, v15.179, v15.184/v15.186, External Audit v15.187; collision repair v15.192; Round 418 v15.193; ACK v15.195. **Status:** [N] concrete first-100-diagonal source-formula probe; [D] coarse global bound cannot establish a low-index spectral gap; [O] rigorously sorted infinite diagonal and sharp local-block spectral contour.\n\n**Canonical rename provenance:** This is the mechanically corrected canonical path requested by External Audit Round 418. It preserves the substantive content of legacy commit `20216773fb68184f2980296d7676b17fbf658cc2`, blob `555bbfc46ab25588729269d442e52ca66dfa5e89`. Gravity retains v15.189; this Lane A result is v15.192. The historical pre-write paragraph below is retained as provenance and is not a new collision claim.

**Live collision check:** pre-write master HEAD `e8535b9785a0eb1bfe47dae2bb04be038240d550`, gravity source commit after v15.188; v15.189 is proposed additive next ledger entry. No protected sources modified.

## What was actually tested

On each parity lattice starting b=512001 (odd physical n) and b=512002 (even physical n), evaluate the **leading displayed physical diagonal formula** in `payloads/far_coefficient_attribution_v14_901/SEED_FORMULA.md` at 100 modes n=b+2j, j=0,...,99:

`d_approx(n)=log(n/4)-1/(2n)+2*(-1)^n/(n*pi)^2 - sum_(q=2,3,4,5,7) w_q (2-log q)[cos(theta_q*n)+2/(n*pi) sin(theta_q*n)]`,

with `theta_q=pi*log(q)/2`, `w_q=log(q)/sqrt(q)` except `w_4=log(2)/2`. Ordinary double precision was used for this **screening probe only**; the stated source formula has an omitted O(1/n²) correction and is not an interval evaluation of the exact diagonal.

The five lowest sampled approximate values on lattice b=512001 are 10.44022730 (n=512035), 10.44437691 (512151), 10.54281672 (512191), 10.61627262 (512053), 10.64189646 (512013). First sampled gap 0.00414962.

The five lowest sampled approximate values on lattice b=512002 are 10.28559769 (n=512082), 10.29855466 (512122), 10.32751192 (512174), 10.40179968 (512024), 10.43555101 (512064). First sampled gap 0.01295697.

These are **sample-sorted, not globally sorted**, and have no certified interval radius or tail exclusion. Neither a global gap nor a contour is claimed.

## Global norm-bound comparison

The already audited v15.129 inequality gives for non-pole B0

`||B0|| <= |c|*pi*Zbar + |c|*Zbar/(2*n_min)`

with `c=2/pi`, `Zbar<7.4233`, `n_min>=512001`, hence `||B0||<14.84661`. For exact-floor pole `0<=p_n<=L/n`, `L<2`, `sum_(n in parity)1/n²<=1/(2*(n_min-2))`, the rank-one pole norm `2||p||²<4/(n_min-2)<0.000007813`. Thus a safe global `M=15` is a valid **analytic upper bound** on ||B|| in each sector (subject to the already certified z and source constants), without evaluating a finite matrix norm. The pre-screen requires sampled/global gaps to **exceed 2M=30**, whereas the observed first gaps are <0.013. This is a very loose global comparison. It shows the proposed first-100 probe does not produce a positive witness, not that a tight local-block or actual operator spectral gap fails.

A source-level all-tail screening shortcut is also available: the displayed physical diagonal has bounded oscillatory correction, with absolute amplitude <2 in the source formula and negligible O(n^-2), so an outward bound `|d_n-log(n/4)|<3` is conservative on the remote lattice, pending independent confirmation from the exact diagonal producer. For every j<=99, min-max and 100 first-mode competitors give `d_(j+1)-d_(j) <= log((b+2j)/b)+6 < 6.001 <30`; **if** this uniform exact bound is independently verified, it rigorously rules out a strict v15.179 gap PASS for j<=99 at M=15, even with infinite-tail ordering. No global sorted list is asserted.

## Gate decision and next feasible work

**Outcome:** `COARSE_MINMAX_PRESCREEN_INCONCLUSIVE` in both parity sectors. The v15.179 sufficient condition is far too conservative for the sampled low-diagonal spacing. Do not label this as 'no spectral gap'. The next useful computation is an audited finite **local-block/Schur-complement** comparison that treats near-diagonal coupling nonperturbatively and bounds the far block and cross-block leakage, or a direct interval inertia test on a certified contour. Source-native Suzuki synthesis Phi_a remains absent; any resulting spectral certificate is for the chosen ell2 model only.

**HANDOFF** target: Sandbox/External Audit. type: coarse-screen-negative-sharper-block. status: OPEN. action: replay sampled calculation with the exact diagonal interval evaluator, verify M<=15 and uniform |d_n-log(n/4)|<3 against the source; then design a finite-block gap/inertia and Schur-tail calculation. deliverable: replay code/hashes, outward-certified values, actual cutoff/contour or precise failure certificate.

**Fence:** no v14.406 residual consumer, no far F1/F2 refresh, no spectral-source equivalence, stationary pair, capacity or altered C_S_32000 / 3e-5 / .002 thresholds.
