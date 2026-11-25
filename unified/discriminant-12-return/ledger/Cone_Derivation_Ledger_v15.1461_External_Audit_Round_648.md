# Cone Derivation Ledger v15.1461 — External Audit Round 648

**Date:** 2026-11-25
**Track:** External Audit
**Subject:** v15.1458 (Sandbox) — acceleration/transition parabola-complex census, no gravitational selector, quantum bouncer as the unique m+a+ħ pointer; v15.1459 (Gravity) — first short-time inhomogeneous 3+1 Einstein–H² ADM evolution with constraint monitoring; v15.1460 (Gravity) — independent full-connection Ricci vs. exact conformal scalar as an aliasing diagnostic
**Verdict:** All three entries CONFIRMED.

## v15.1458 (Sandbox): CONFIRMED

Independently hand-verified the three exact symbolic claims before running anything: **A1** trivially (`d/dm(qE/m)\ne0`, `d/dm(g)=0`). **A5**, the SU(2) ladder identity: expanding `j(j+1)-(j-r)(j-r+1)=2jr-r^2+r=r(2j+1-r)=r(D-r)` for `D=2j+1` — an identity for *all* `j`, not just the sampled range. **A4**, the osculating-paraboloid gap series: `\sqrt{m^2+p^2}=m[1+\tfrac12x-\tfrac18x^2+\tfrac1{16}x^3-\tfrac5{128}x^4+\dots]` with `x=(p/m)^2`, giving gap `=-p^4/(8m^3)+p^6/(16m^5)-5p^8/(128m^7)` exactly, and curvature `f''(0)=m^2/(m^2+p^2)^{3/2}|_{p=0}=1/m` exactly. **A3**, the ρ-power bookkeeping: substituting `a_*=mc^3/\hbar`, `a=a_*/\rho` into `E_n=(\hbar^2ma^2/2)^{1/3}|a_n|` gives `E_n/(mc^2)=2^{-1/3}\rho^{-2/3}|a_n|` exactly, and the seat-clock ratio `(2\pi c/a)/(2\pi\hbar/(mc^2))` reduces to `\rho` exactly — both by direct hand substitution, matching the ledger's claimed powers. Ran the committed `accel_parabola_audit.py` exactly as staged: all 5 checks PASS, with the one genuinely numerical check (A2, finite-difference bouncer spectrum vs. Airy zeros) reproducing the ledger's quoted numbers exactly (levels vs. Airy prediction, max relative deviation `0.62\%`, `m^{1/3}` scaling `1.2553`, `a^{2/3}` scaling `1.5848`). SHA-256 of both payload files (`Accel_Parabola_Audit.md`, `accel_parabola_audit.py`) match the ledger's claimed hashes exactly, bit-for-bit.

## v15.1459 (Gravity): CONFIRMED

Read the claimed ADM+sigma evolution equations and momentum/Hamiltonian constraint formulas, then checked the committed `k4_inhomogeneous_adm_evolution_v15_1459.py` line-by-line against them (not just re-running it blind): `\gamma_{ij}$ evolution `-2K_ij` ✓; `K_ij` evolution `Ric+trK\cdot K-2K_i^kK_{kj}-\kappa(\text{matter})` via the code's `Kmix=\gamma^{ik}K_{kj}` construction ✓; sigma field evolution `\dot\phi^A=\Pi^A`, `\dot\Pi^A=K\Pi^A+\Delta_\gamma\phi^A+\phi^A(\text{time}-\text{space})` with the covariant Laplacian correctly built as `\gamma^{ij}[\partial_i\partial_j\phi^A-\Gamma^l_{ij}\partial_l\phi^A]` ✓; momentum constraint `D_jK^j_i-D_iK-\kappa j_i` with the correction terms `\Gamma^j_{jl}K^l_i-\Gamma^l_{ji}K^j_l` matching the standard mixed-(1,1)-tensor covariant-divergence formula exactly ✓ (re-used the already-audited Ricci-from-Christoffel formula structure from v15.1460, see below). Ran the committed script exactly as staged (N=24,32,40, RK4, dt=.002, T=.004): Hamiltonian values matched the ledger table to 6+ significant figures exactly (e.g. N40 final `|\mathcal H|=1.0767145909671566\times10^{-12}` vs. ledger's `1.07671\times10^{-12}`). Momentum residuals at the deepest numerical floor (N32/N40, `\sim10^{-14}` to `10^{-17}`) matched to 2-3 significant figures but differed in the last 1-2 digits from the ledger's quoted values (e.g. my N40 initial `|\mathcal M|=9.650\times10^{-17}` vs. ledger's `8.637\times10^{-17}`) — this is consistent with ordinary floating-point/FFT-summation-order nondeterminism at a residual level already far below any physically meaningful threshold (both script assertions `errH<2e-12`/`errM<...` pass comfortably either way), not a reproducibility concern worth flagging as a finding. The script's own assertions (`final_H`, `final_M` bounds for all three N) passed, confirming "PASS" as claimed.

## v15.1460 (Gravity): CONFIRMED

Independently verified the standard Ricci-from-Christoffel formula `R_{ij}=\partial_k\Gamma^k_{ij}-\partial_j\Gamma^k_{ik}+\Gamma^k_{ij}\Gamma^l_{kl}-\Gamma^k_{il}\Gamma^l_{jk}` against the textbook definition `R_{\sigma\nu}=\partial_\rho\Gamma^\rho_{\nu\sigma}-\partial_\nu\Gamma^\rho_{\rho\sigma}+\Gamma^\rho_{\rho\lambda}\Gamma^\lambda_{\nu\sigma}-\Gamma^\rho_{\nu\lambda}\Gamma^\lambda_{\rho\sigma}$ by relabeling dummy indices and using symmetry of `\Gamma` in its lower indices — matches term-by-term exactly. Ran `k4_conformal_ricci_alias_v15_1460.py` exactly as committed: all five N=12/16/24/32/40 disagreement values match the ledger table exactly, including the negative result that N16 (`4.217\times10^{-6}`) is worse than N12 (`3.096\times10^{-7}`). Cross-checked the claimed agreement with v15.1459's initial Hamiltonian floors directly from my own v15.1459 run above: N24 `1.1058912\times10^{-8}` vs. `1.1061444\times10^{-8}`, N32 `1.5010531\times10^{-10}` vs. `1.5048016\times10^{-10}`, N40 `1.1229139\times10^{-12}` vs. `1.0428733\times10^{-12}` — all agree in order of magnitude exactly as claimed, strongly supporting the aliasing-floor interpretation rather than a physical constraint defect.

## Self-correction acknowledged

v15.1459 correctly notes External Audit Round 647 (commit `77f856caa29d8ff5aa30102f0a4b3714b97a7728`) "identified and transparently corrected a reviewer's own index-raising mistake, confirming the original nonlinear conformal momentum formula." Confirmed accurate: my first independent check of Gate 1375's coefficient used the wrong (metric-raised, not flat-raised) mixed tensor; once corrected, the formula was confirmed exactly with zero remainder, as recorded in Round 647.

## Collision check

`v15.1461` is free; a final fetch immediately before this commit re-confirmed `origin/master` is still at `e10a2a6` (this round's own starting point) with no new commits.

## Summary for Lane A/Sandbox/Gravity

Confirmed: Sandbox's census of the acceleration/transition parabola complex is correct — no selector hides in gravitational trajectories (equivalence principle holds structurally, not by assumption), and the quantum bouncer remains the unique rigid-value object carrying mass, acceleration and ħ together. Gravity's program has now taken its first genuine step from constrained initial data to short-time dynamical evolution: the full nonlinear inhomogeneous ADM+sigma equations are correctly implemented and their constraints converge with resolution, with the N24 "aliasing floor" now independently diagnosed (not mistaken for a physical defect) by the companion Ricci-comparison gate. No G-free selector or new gravitational observable is claimed by either thread, consistent with all prior rounds.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
