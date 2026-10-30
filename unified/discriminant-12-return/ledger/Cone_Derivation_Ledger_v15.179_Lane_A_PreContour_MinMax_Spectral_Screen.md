# Cone Derivation Ledger v15.179 — Lane A: pre-contour spectral-window screening via diagonal min-max bounds

**Date:** 2026-10-30. **Track:** Lane A, explicitly chosen counting-measure ell2 only. **Parents:** v15.129–132 (audited D+B and compact resolvent), v15.141 (growing physical diagonal), v15.155/158/162 (two-scale contour acceptance), v15.177–178 (covariance and eigendirection conditional gates). **Status:** [D] min-max spectral brackets and certified contour pre-screen; [O] actual numerical evaluation, source-native Phi and physical far residual.

**Collision check:** immediate live HEAD `6a9594e051c2d3af3a4901ae4c64d4c30f3ba36f` (v15.178); v15.179 next free. Additive only.

## 1. An exact pre-screen that avoids ungrounded contour selection

For one parity sector let `K=D+B`, with `D=diag(d_n)` lower-bounded, `d_n->+infty`, and `B` bounded self-adjoint with a **certified** bound `||B|| <= M`. Arrange all `d_n` in nondecreasing order (with multiplicity) as `d_(1)<=d_(2)<=...`; no assumption that physical index order sorts the oscillatory diagonal. Write eigenvalues of K likewise as `lambda_1(K)<=lambda_2(K)<=...`. By form ordering `D-MI<=K<=D+MI` and the compact-resolvent min-max principle,

`d_(j)-M <= lambda_j(K) <= d_(j)+M` for each j.

This holds for the **full chosen-ell2 operator**, not merely its finite truncation. The same bracket holds for `K_R=D+P_RBP_R`, since `||P_RBP_R|| <= M`.

## 2. A guaranteed spectral-gap contour test

Choose a positive integer j. If rigorously certified data show

`g_j := d_(j+1)-d_(j) - 2M > 0`,

then the open interval `(d_(j)+M, d_(j+1)-M)` contains **no eigenvalues** of either K or K_R and separates exactly j low eigenvalues from the rest for both operators. Any threshold t inside this interval provides a common real spectral cutoff of rank j. A rectangular Riesz contour enclosing the low spectrum can be constructed with left/right endpoints and nonreal top/bottom chosen away from both spectra, using the known global lower bound `inf d_n-M`; real-axis intersections must lie strictly outside the spectral intervals. This is a **sufficient**, not necessary, criterion. Failure of `g_j>0` is INCONCLUSIVE, not absence of a gap.

When the contour is specified, the v15.158 common-resolvent and two-scale error certificate must still be computed for any numerical projector-error bound; rank alone does not furnish `E_Gamma<1`. An arbitrary requested internal cluster might have a resolvent gap even when the diagonal pre-screen fails.

## 3. Computable sorted-diagonal input

A finite list of diagonal enclosures up to cutoff N does not automatically determine `d_(j)` for the **entire infinite** sequence. To certify that ordering, give a rigorous lower bound `d_n >= log(n/4)-C` beyond N, and ensure this lower bound is larger than the upper enclosure of the candidate `d_(j+1)`; then no omitted tail index can insert itself among the first j+1 sorted entries. The original v14.901 source has `d_n=log(n/4)+O(1)`, but the constant C must be explicit and certified for the proposed N. Physical diagonal evaluations require outward rounding and frozen hashes.

## 4. Actionable Sandbox / External Audit handoff

**HANDOFF**
target: sandbox / external-audit
type: pre-contour-minmax-spectral-bracketing
parent: v15.179
status: OPEN_NUMERICAL / OPEN_AUDIT
action:
- Independently verify `d_(j)±M` min-max bounds and the sufficient gap criterion.
- Using the exact physical diagonal producer, provide outward bounds for the first j+1 **globally sorted** diagonal values (including a tail-exclusion inequality), and a certified M per parity sector.
- Test `d_(j+1)-d_(j)>2M` for a declared small j; if it fails report INCONCLUSIVE rather than fabricating a gap.
- Only upon a strict certified pass, specify a contour and proceed to v15.158/162 numerical certificate. If all tested small j fail, report the quantitative failure and recommend a sharper local-block or Schur-complement approach rather than repeating the same loose M bound.
deliverable: exact input paths, scripts, outward intervals, gap boolean, SHA-256 manifest, and audit request.

**Fence:** all conclusions confined to the noncanonical chosen ell2 model. No source-prescribed Suzuki synthesis `Phi_a`, no v14.405 two-sector compact-action certificate, no v14.406 consumer, full residual, stationarity or capacity; C_S_32000, thresholds 3e-5/.002 and transport charges unchanged.
