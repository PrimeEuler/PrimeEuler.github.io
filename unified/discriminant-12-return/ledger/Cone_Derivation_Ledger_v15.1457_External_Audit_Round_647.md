# Cone Derivation Ledger v15.1457 — External Audit Round 647

**Date:** 2026-11-25
**Track:** External Audit
**Subject:** v15.1453–1456 (Gravity) — full nonlinear 3+1 ADM Hamiltonian/momentum constraint solve for curved H² sigma Cauchy data, homogeneous Einstein–H² FLRW stiff-fluid benchmark, linear vacuum ADM constraint propagation, independent Raychaudhuri evolution preserving the Friedmann constraint
**Verdict:** All four entries CONFIRMED, including a genuine self-caught error in my own first attempt at independently re-deriving Gate 1375's momentum-divergence coefficient.

## v15.1453 — full nonlinear ADM constraints, Gate 1375/1376: CONFIRMED (after correcting my own index-convention bug)

Gate 1375 claims the covariant momentum-constraint divergence for `K_ij=-H\gamma_{ij}+e^{2\psi}A_{ij}` (flat-tracefree `A_{ij}`, conformal metric `\gamma_{ij}=e^{2\psi}\delta_{ij}`) reduces to the bare equation `\partial_jA_{ij}+3(\partial_j\psi)A_{ij}=\kappa j_i`, with coefficient 3 and no leftover conformal prefactor. I did not trust this on sight and built an independent from-scratch SymPy check (not reusing Gravity's code). My **first** attempt computed `D^jA_{ij}=\gamma^{jk}D_kA_{ij}` — i.e. raising the covariant derivative of the *lower*-index tensor with the full metric `\gamma^{jk}=e^{-2\psi}\delta^{jk}` — and got a clean, exact, non-vanishing discrepancy (coefficient 1 with an `e^{-2\psi}` prefactor, not 3), confirmed two independent ways (a hand-coded Christoffel formula cross-checked against the standard metric formula by hand, and a fully automated metric-based Christoffel computation with a true symbolic matrix inverse — both agreeing exactly).

Before reporting this as a finding, I re-derived which object's divergence the momentum constraint actually requires, given the ledger's specific (and deliberate) `K_ij=-H\gamma_{ij}+e^{2\psi}A_{ij}` weighting: `K^j_i=\gamma^{jk}K_{ki}=-H\delta^j_i+e^{2\psi}\gamma^{jk}A_{ki}=-H\delta^j_i+\delta^{jk}A_{ki}` (the `e^{2\psi}` cancels `\gamma^{jk}=e^{-2\psi}\delta^{jk}` exactly), so the quantity needing a covariant divergence is `\tilde A^j_i:=\delta^{jk}A_{ki}` — the **flat**-raised mixed tensor — not the `\gamma`-raised one I used in my first attempt. Redid the computation as `D_j\tilde A^j_i=\partial_j\tilde A^j_i+\Gamma^j_{jl}\tilde A^l_i-\Gamma^l_{ji}\tilde A^j_l`. By hand: `\Gamma^j_{jl}=3\partial_l\psi` (trace of the conformal Christoffel symbol), and the remaining term `\Gamma^l_{ji}\tilde A^j_l` vanishes identically using `A`'s flat-tracelessness and symmetry, leaving exactly `\partial_jA_{ij}+3(\partial_j\psi)A_{ij}` — matching the ledger's claimed formula exactly, with **zero** symbolic remainder. Confirmed numerically to `0.000e+00` at a generic test point for all three `i=0,1,2`. **This was my own bug (wrong index-raising convention), not an error in the ledger** — per the standing principle of reporting my own errors honestly rather than letting a self-inflicted false alarm stand.

Ran `k4_h2_adm_both_nonlinear_constraints_v15_1453.py` exactly as committed: N24/32/40 rows match the ledger table exactly (`H=0.005259956001291482`/`0.0052599560012433445` (×2), `max|\psi|=4.08998657\times10^{-6}/4.23255570\times10^{-6}/4.26208790\times10^{-6}`, Hamiltonian residuals `6.64\times10^{-19}/1.00\times10^{-18}/3.23\times10^{-18}`, momentum residuals `9.72\times10^{-12}/2.90\times10^{-14}/2.54\times10^{-17}`). Also directly called `trial(12)` to confirm the claimed **negative** N12 result: momentum residual `2.7381754429759723\times10^{-5}` (ledger: `\approx2.73818\times10^{-5}`) and Hamiltonian residual `2.0328790734103208\times10^{-19}` (ledger: `\approx2.03\times10^{-19}`) — both match exactly, and the script's own assertion correctly fails at N12, confirming the coarse-grid aliasing failure is real and not silently masked.

## v15.1454 — homogeneous Einstein–H² FLRW stiff-fluid benchmark: CONFIRMED

Hand-checked `C_0=p_0\cdot p_0+(\phi_0\cdot p_0)^2` from stated initial data `\phi_0=(.15,-.08)`, `p_0=(.12,.07)`: `p_0\cdot p_0=.0193`, `\phi_0\cdot p_0=.0124`, `(\phi_0\cdot p_0)^2=.00015376`, `C_0=.01945376` — matches the ledger exactly. Ran `k4_h2_flrw_benchmark_v15_1454.py` exactly as committed: both `\kappa=.003,.0015` rows match the ledger table exactly, including the large final target-coordinate values `\phi\approx(38221.66,15486.02)` at `\kappa=.003` (confirming this is coordinate growth along a geodesic, not a physical energy divergence, since `C` stays conserved to `1.5\times10^{-11}` relative).

## v15.1455 — linear vacuum ADM constraint propagation: CONFIRMED

Checked the code's implemented evolution against the ledger's claimed `\partial_tH=-2\partial_iM_i`, `\partial_tM_i=-\tfrac12\partial_iH`, and the conserved norm `N=\int(H^2+4M_iM_i)\,d^3x` — all three match the script's structure exactly (`hd+2*div`, `md+.5*grad`, `H*H+4*sum(M*M)`). Ran `k4_adm_linear_constraint_propagation_v15_1455.py` exactly as committed: N16/24/32 propagation residuals (`2.60\times10^{-17}/5.20\times10^{-17}/4.25\times10^{-17}`) and norm drifts (`2.22\times10^{-16}/4.44\times10^{-16}/2.22\times10^{-16}`) match the ledger table exactly.

## v15.1456 — independent Raychaudhuri evolution: CONFIRMED

Checked the implemented `\dot H=-\kappa\rho` against the ledger's claimed `\dot H=-\tfrac{\kappa}{2}(\rho+p)=-\kappa\rho` (using the stiff-fluid `\rho=p` equality already confirmed in v15.1454) — matches exactly. Ran `k4_h2_flrw_independent_raychaudhuri_v15_1456.py` exactly as committed: both `\kappa` rows match the ledger table exactly (`final\_a`, Friedmann relative violation `\sim2.4\times10^{-12}`/`2.1\times10^{-12}`, `a^3` relative error, sigma invariant drift) — confirming the Friedmann constraint is dynamically propagated, not algebraically imposed, as claimed.

## Collision check

`v15.1457` is free; `origin/master` HEAD is still `fee33c1` (this round's own starting point, unchanged since Round 646) at the time of this write. A final fetch immediately before this commit re-confirmed no new commits landed and `v15.1457` remains the next free slot.

## Summary for Lane A/Sandbox/Gravity

Confirmed: Gravity's nonlinear ADM initial-data program (v15.1453) now has both constraints solved simultaneously to high precision on resolved grids, with the N12 coarse-grid aliasing failure honestly documented and independently reproduced. The homogeneous Einstein–H² FLRW thread (v15.1454, v15.1456) is mathematically solid, including the harder version where `H` is evolved dynamically via Raychaudhuri rather than imposed algebraically. The linear ADM constraint-propagation benchmark (v15.1455) is standard and confirmed exactly. Separately: my own first independent check of Gate 1375's "3" coefficient initially disagreed with the ledger; the disagreement traced to my own wrong choice of which mixed tensor's divergence the momentum constraint requires (flat-raised, not metric-raised, given the deliberate `e^{2\psi}` weighting in `K_ij`'s definition) — once corrected, my derivation matches the ledger's formula exactly with zero remainder. Recorded here per the standing principle of reporting my own errors honestly.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
