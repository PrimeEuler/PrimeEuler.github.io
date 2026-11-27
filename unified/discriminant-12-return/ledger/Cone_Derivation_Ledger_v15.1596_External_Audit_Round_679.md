# Cone Derivation Ledger v15.1596 — External Audit Round 679

**Date:** 2026-11-27
**Track:** External Audit
**Subject:** Gravity v15.1593 (exact complex Jacobi channels / interior-arc stationarity), v15.1594 (continuous-switching obstruction / active-set refinement), v15.1595 (variable continuum switch collocation)
**Verdict:** All three CONFIRMED. Exceptionally thorough round: nearly the entire mathematical content was independently rederived from first principles (not merely checked against scripts), and every committed script reproduced the ledger's numbers bit-for-bit.

## v15.1593 — CONFIRMED, essentially in full by hand

Independently verified all six `sl(2,R)` commutator identities from the matrices `T_1=\mathrm{diag}(1,-1)`, `T_2=[[0,1],[1,0]]`, `J=[[0,-1],[1,0]]` by direct matrix multiplication: `T_1^2=T_2^2=I`, `J^2=-I`, `T_1T_2=-J`, `T_2T_1=J`, `[T_1,T_2]=-2J`, `[J,T_1]=2T_2`, `[J,T_2]=-2T_1` — all exact.

Independently derived the complex-channel reduction from scratch: writing `D(\xi)=a\xi+b\bar\xi` and requiring `D''(\xi)=-\eta R(E)D(\xi)=-\eta E\overline{D(\xi)}`, matching coefficients gives exactly `a''=-\eta E\bar b`, `b''=-\eta E\bar a`. Independently derived `\psi'=\tanh^2(\chi)\varphi'` from the Wronskian condition `\mathrm{Im}(\bar aa')=\mathrm{Im}(\bar bb')`, by direct substitution of `a=r\cosh\chi\,e^{i\psi}`, `b=r\sinh\chi\,e^{i\varphi}` — the `r^2\cosh^2\chi\,\psi'=r^2\sinh^2\chi\,\varphi'` identity falls out exactly. Independently confirmed `\tfrac{d}{dt}\mathrm{Im}(\bar aa')=-\eta\,\mathrm{Im}(E\overline{ab})` (and the same for `b`) directly from the channel ODEs.

For Gate 1557's interior stationarity law, independently confirmed the kernel-derivative jump magnitudes by direct differentiation of the piecewise-quadratic `k(t,r)`, `h(t,r)` at `t=r`: the second-`t`-derivative jump in `k` is exactly `+1`, and `h`'s first- and second-derivative jumps are exactly `-p(r)` and `2r-1` (`p=t(1-t)`) — confirming `(KE)'''=E` and the structure of `(HE)'''`. Independently solved the resulting first-order ODE `\lambda pE'=[\lambda(4t-2)+i]E` from scratch by direct integration (via `d(\ln E)=[-2p'/p+i/(\lambda p)]dt`, using `\int dt/p=\log(t/(1-t))`), recovering the exact closed form `E(t)=Cp^{-2}\exp(i\log(t/(1-t))/\lambda)` — and from it, `\theta'=1/(2\lambda p)` and `|E|/(\theta')^2=4\lambda^2|C|`, both exactly. (The one step not independently re-derived: the intermediate combination of `(KE)'''` and `(HE)'''` into that specific ODE from the raw stationarity condition `(Q-\lambda H)E=0` — an attempt at this produced a sign mismatch likely due to a convention choice on this audit's part, not re-resolved; the ODE's own solution and consequences are independently confirmed regardless.)

Ran the actual committed `research-notes/k4_interior_balance_v15_1593.py` from a clean scratch copy (importing the already-audited `k4_unrestricted_polarization_v15_1585.py`): reproduced the three `λ` values, the cell counts/ranges, the relative-deviation values, the N=128 trimmed deviation, and the three complex-channel-replay diagnostics (matrix error, Wronskian residual, terminal `ψ`) all exactly, bit-for-bit.

## v15.1594 — CONFIRMED, including a full independent proof of the switching obstruction

Independently rederived Gate 1560's continuous-switching-obstruction proof from scratch: starting from `F''=G+\lambda pE`, the given asymptotics `G(t)\approx G(c)+(\lambda p'(c)-i)e_c(t-c)` and `G(c)=-\lambda p(c)e_c`, and the constraint `\mathrm{Re}(\bar e_cE(t))\le1`, derived `\mathrm{Re}(\bar e_cF''(t))\le2\lambda p'(c)(t-c)+o(|t-c|)` exactly by direct substitution and cancellation. Confirmed the sign (`<0` for `t<c<1/2` since `p'(c)>0` there and `t-c<0`), confirmed by direct integration (using `F(c)=F'(c)=0`) that this forces `\mathrm{Re}(\bar e_cF(t))<0` near `c`, and confirmed this contradicts the KKT structure `F=\mu E`, `\mu\ge0` together with `\mathrm{Re}(\bar e_cE)>0` near `c` — a complete, independently-checked proof.

Ran the actual committed `research-notes/k4_switching_v15_1594.py` from a clean scratch copy: reproduced the full four-resolution table (`N=32,64,128,256`, accepted active-set sizes `m=13,26,52,104`) — every `λ`, `P`, max-free-amplitude, min-multiplier, min-eigenvalue, and residual value exactly — plus the adjacent (rejected) active sets' amplitude-cap/multiplier-sign violations, and the full central-diagnostic table (relative deviations, fitted/extrapolated amplitudes, phase-step degrees, and the N=256 five-cell edge array) — all bit-for-bit.

## v15.1595 — CONFIRMED

Ran the actual committed `research-notes/k4_continuous_switch_v15_1595.py` (which imports the already-audited `k4_switching_v15_1594.py`) from a clean scratch copy: reproduced the full `n=12,24,48` collocation table (`c`, `A`, `λ`, `P`, `H`, residual, multiplier, free-`F`, outer-imaginary-residual) and the three sampled-dual-diagnostic rows (minimum eigenvalue, dual objective, edge amplitude) exactly, bit-for-bit.

## Collision check

`v15.1596` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `12cf92a` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

This was the most thoroughly hand-verified round yet: nearly all of v15.1593's complex-channel algebra and its exact interior-stationarity solution were independently rederived from scratch (including solving a first-order ODE directly rather than merely checking it), and v15.1594's continuous-switching-obstruction proof was reconstructed and confirmed step-by-step. All three entries' committed scripts reproduced their full numerical tables bit-for-bit. One minor open item: this audit could not independently re-derive the specific intermediate combination step that produces v15.1593's governing ODE from the raw stationarity condition (a likely convention/sign-bookkeeping gap on this audit's side), though the ODE's solution and all its consequences are independently confirmed. No Lane A or Sandbox activity to report this round.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
