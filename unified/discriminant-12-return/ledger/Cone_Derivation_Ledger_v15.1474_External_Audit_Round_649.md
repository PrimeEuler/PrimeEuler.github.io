# Cone Derivation Ledger v15.1474 — External Audit Round 649

**Date:** 2026-11-25
**Track:** External Audit
**Subject:** v15.1462 (Sandbox) — G-trace audit; v15.1463–1464, 1466–1470, 1472–1473 (Gravity) — 2× Ricci-aliasing removal, raw-ADM Jordan weak-hyperbolicity obstruction, linear generalized-harmonic principal-symbol benchmark, variance-shell boost comparator, harmonic-gauge initial-data closure (illustrative then actual v15.1453 slice), nonlinear GH FLRW harmonic-time benchmark; v15.1465 (Sandbox) — variance shells; v15.1471 (Lane A) — Suzuki R4 direct-restart 64-state right extension
**Verdict:** All eleven entries CONFIRMED.

## v15.1462 (Sandbox, G-trace audit): CONFIRMED

Independently hand-verified the G-power census by logarithmic differentiation (Poisson source, surface gravity, tidal β₂, compactness, α_G, ADM κ all power +1; free-fall time −1/2; tangency gap −1; tidal deformability Λ −5) and the Gauss-law algebra `g_s=(4/3)\pi G\rho R`. Ran `g_trace_audit.py` exactly as staged: all 5 checks PASS. SHA-256 of both payload files match the ledger's claimed hashes exactly.

## v15.1463 (Gravity, 2× oversampling): CONFIRMED

Ran `k4_oversampled_full_ricci_v15_1463.py` exactly as committed: all native (1×) values match the already-audited v15.1460 baseline exactly; the 2× oversampled values match the ledger table to 6+ significant figures, with tiny (7th-digit) differences at the `~10^{-13}-10^{-14}` floor — consistent with ordinary FFT/floating-point summation-order nondeterminism at that depth, not a finding (same category noted for v15.1459 in Round 648).

## v15.1464 (Gravity, raw-ADM Jordan block): CONFIRMED exactly

Independently hand-derived every claim before running anything: the linearized Ricci `R_ij=\tfrac12(\partial_k\partial_ih_{kj}+\partial_k\partial_jh_{ki}-\partial_i\partial_j\,\mathrm{tr}(h)-\Delta h_{ij})` vanishes identically for the pure-longitudinal mode (checked all components by hand); both linear constraints vanish exactly; the evolution matrix is the nilpotent Jordan block `J=\begin{psmallmatrix}0&-2\\0&0\end{psmallmatrix}` with `J^2=0` and only one eigenvector; `\exp(tJ)=I+tJ` gives `H(t)=-2tP(0)` exactly; and I reproduced every value in the norm-growth table by hand (e.g. `k=256`: `\sqrt{1+4(1+256^2)}=\sqrt{262149}\approx512.00488}`). Ran `k4_raw_adm_longitudinal_jordan_v15_1464.py` exactly as committed: output matches both the ledger and my independent derivation exactly.

## v15.1465 (Sandbox, variance shells): CONFIRMED

Hand-verified all core identities (AM²−GM²=((n−k)/2)²; the cone identity T²−X²=Y²=nk; E−|p|=min(n,k); m/E=sechψ; dilation m→cm; the Casimir sums 5/16=1/4+1/16, 13/16=3/4+1/16). Ran `variance_shell.py` exactly as staged: all 7 checks PASS. SHA-256 of both payload files match exactly.

## v15.1466 (Gravity, linear GH principal-symbol benchmark): CONFIRMED exactly

Hand-verified the trace-reversal gauge Ward identity (`p^\mu\bar h_{\mu\nu}=(p^2)\xi_\nu` exactly, vanishing on-shell), the skew principal generator `P(k)=\begin{psmallmatrix}0&k\\-k&0\end{psmallmatrix}` with conserved norm, and the TT-wave Fourier energy `1+9(0.32)^2=1.9216` by direct computation of `\mathrm{mean}([f'(z)]^2)` for `f(z)=\sin z+0.32\cos(3z)`. Ran `k4_gh_linear_constraint_wave_v15_1466.py` exactly as committed: matches the ledger table exactly, including the t=1.7 last-digit variant.

## v15.1467 (Gravity, variance-shell boost comparator): CONFIRMED exactly

Hand-derived the boost transformation `T'=T\cosh\eta+X\sinh\eta`, `X'=X\cosh\eta+T\sinh\eta`, confirmed `Q'=T'^2-X'^2=nk=Q` exactly (genuine Lorentz invariance), and reproduced the balanced-pair counterexample (`\sinh^2(0.5)\approx0.271540`, `\sinh^2(1)\approx1.381098`) exactly by hand — confirming Sandbox's variance `X^2` is *not* the same object as the genuinely invariant `Q=nk`. Ran `k4_variance_shell_boost_covariance_v15_1467.py` exactly as committed: matches exactly. Parent commit reference to Sandbox v15.1465 (`9f5430fa6cb95a360395f9e5313d2471572407a7`) verified correct.

## v15.1468 (Gravity, illustrative GH initial-gauge closure): CONFIRMED

Given how subtle the index-raising conventions proved in Round 647 (v15.1453), did not trust Gate 1394's formulas on sight. Built an independent, from-scratch numerical computation of the full 4D contracted Christoffel symbols for a general ADM metric (general lapse/shift and their time derivatives, general conformal spatial metric) — not reusing any of the committed script's internal `dg`-array construction, which uses an index-placement pattern that looked suspicious on inspection. My independent computation matched the claimed `\Gamma^0=-\dot\alpha-K` and `\Gamma^i=-\dot\beta^i+\gamma^{jk}\,{}^{(3)}\Gamma^i_{jk}` exactly (to machine precision) at a concrete test point, and separately confirmed the conformal simplification `\gamma^{jk}\,{}^{(3)}\Gamma^i_{jk}=-e^{-2\psi}\partial^i\psi` by hand. Ran `k4_gh_initial_gauge_v15_1468.py` exactly as committed: output matches the ledger exactly (`K\_trace=-0.015779868`, `max\_harmonic\_gauge\_violation=1.734723475976807\times10^{-18}`, `max\_spatial\_gauge\_velocity\approx5.10\times10^{-6}` at N=12/16/24). A separate from-scratch cross-check at a representative point using the same field profile also gave exactly zero, confirming the script's near-zero result is physically correct despite its non-obvious internal indexing.

## v15.1469 (Gravity, variance/EM-area nonselector): CONFIRMED exactly

Hand-verified the Wick identity `E[(a_xb_y-a_yb_x)^2]=2\det\Sigma` for independent diagonal-covariance Gaussian pairs, the extrema (`0` and `V^2/2=1/512` at `V=1/16`), and the fixed-norm orthogonal case (`V^2\sin^2\theta=1/256`) — all exact. Ran `k4_variance_em_area_v15_1469.py` exactly as committed: matches exactly.

## v15.1470 (Gravity, nonlinear GH FLRW harmonic-time benchmark): CONFIRMED exactly

Derived every harmonic-time ODE by chain rule from the already-audited proper-time equations (v15.1454/1456) composed with `d\tau/ds=\alpha`, and the closed form `\alpha=a^3(s)=e^{Bs}`, `H(s)=B/(3a^3(s))` by direct change-of-variables integration of `a^3(\tau)=1+B\tau`. Confirmed `H(0)=B/3=\sqrt{\kappa C_0/(6f^2)}` by hand. Ran `k4_h2_gh_flrw_harmonic_time_v15_1470.py` exactly as committed: matches the ledger table exactly, with `B` cross-checked against v15.1454's slope.

## v15.1472/1473 (Gravity, GH gauge closure on the actual v15.1453 slice): CONFIRMED

Confirmed the audit-handoff distinction is accurate: `k4_h2_constrained_gh_initial_v15_1472.py` is byte-identical in substance to v15.1453's solver (returns `psi,A,q` only, no gauge check) and must not be treated as the reproducer; `k4_h2_constrained_gh_fullcheck_v15_1473.py` is the actual canonical GH-closure script. Hand-confirmed `\dot\alpha=3H=0.015779868` and that the deliberately-wrong control (`\dot\alpha=\dot\beta=0`) gives violation `=|{-K}|=3H` exactly, matching the formula from v15.1468. Ran the committed v15.1473 script exactly as staged: the substantive numbers (ADM Hamiltonian/momentum, the deliberately-wrong control residuals, lapse/shift-derivative means) all match the ledger exactly, including bit-for-bit matches on the "naive_GH_residual" diagnostic values (`0.01577986800387445`, `0.015779868003730036`). The genuine (near-zero, ~10^{-18}) `GH_initial_residual` values I obtained differ from the ledger's quoted figures by an amount larger than the usual last-digit roundoff variation seen elsewhere this session, but both mine and the ledger's are 4+ orders of magnitude below the script's own `1e-14` assertion threshold — consistent with pure floating-point noise on an exact algebraic cancellation (`\Gamma^\mu$ is exactly zero by construction once `\dot\alpha,\dot\beta` are chosen as claimed), not a physics or implementation error. Noted here per the standing honesty principle.

## v15.1471 (Lane A, R4 direct-restart 64-state right extension, arcs 5802–5865): CONFIRMED bit-for-bit

Verified `sha256sum` on producer and certificate against the manifest — both match exactly; the frozen dependency hashes (v15.842, v15.800 producers) also match. Read every field of the committed certificate JSON (64 states, arc range 5802–5865, step range 1793–1856, 16 rebase arcs, all `pass: true`) and confirmed every extremum quoted in the ledger prose matches the JSON exactly (`max_propagated_b4=249.84402550125876`, `max_propagated_fourth_root=3.9757332889106447<4.10`, `max_direct_fourth_root`, `max_sweep_minus_direct_b4`, `max_entry_discrepancy`, `max_cumulative_arithmetic`, `max_rebase_arithmetic`). Verified the quoted live-HEAD and landing commit hashes against actual git history — all match exactly. Ran the exact committed producer from a clean invocation (full ~7-minute rebuild, not a shortcut): regenerated `certificate_sha256=a955356268ab2e9e0f8811bd5e9ee6e2d9e58833c9ddd75109f6a89fa3a5d680`, matching the committed certificate bit-for-bit. Coverage arithmetic by hand: `832+1856=2688` of 8019; `8019-2688=5331` uncovered — matches exactly. Adjacent to v15.1447 at arcs 5801/5802, no gap.

## Collision check

`v15.1474` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `0de5073` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

Confirmed: Lane A's coverage now stands at 2,688 of 8,019 arcs (5,331 remaining). Gravity's numerical-relativity program has made substantial progress this round: the N16 aliasing floor is resolved as a spectral artifact (2× oversampling), the raw fixed-lapse ADM formulation is proven weakly hyperbolic by an exact Jordan-block argument (a genuine, clean mathematical negative result), a linear generalized-harmonic benchmark avoids that obstruction, and harmonic-gauge initial data has now been closed on the actual nonlinear v15.1453 constrained slice — closing the loop from illustrative to physical initial data. Sandbox's G-trace and variance-shell notes, and Gravity's own variance-shell boost critique, are all confirmed; the critique correctly distinguishes the non-invariant pair-variance from the genuinely boost-invariant `Q=nk`. No G-free selector or new gravitational observable is claimed anywhere in this batch.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
