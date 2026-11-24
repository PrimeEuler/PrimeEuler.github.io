# Cone Derivation Ledger v15.1403 — External Audit Round 636

**Date:** 2026-11-24
**Track:** External Audit
**Subject:** v15.1401 (nested EM/q2/null hyperboloid shell volumes), v15.1402 (natural state-count/orbit-area comparison)
**Verdict:** Both entries CONFIRMED. Both committed scripts run exactly as committed with no patching and reproduce every quoted number exactly. All analytically tractable claims verified correct by hand, including a from-scratch Jacobian derivation and precise numerical recomputation of the 3+1 ball-volume ratio at all three quoted T values.

## v15.1401 — nested hyperboloid shell volumes: CONFIRMED

**Gate 1325 (fixed-T annular areas).** With `a=√(1/4)=1/2`, `b=√(1/16)=1/4`: `A_{EM-q2}=π(a²-b²)=π(1/4-1/16)=3π/16`, `A_{q2-null}=πb²=π/16`, `A_{EM-null}=πa²=π/4`. Ratios `3`, `3/4`, `1/4` all follow by direct substitution — confirmed exactly.

**Gate 1326 (Jacobian and regulated volumes).** Independently re-derived the Jacobian of `T=s cosh χ, X=s sinh χ cos θ, Y=s sinh χ sin θ` from the full 3×3 determinant by hand: expanding along the first row gives `s² sinh χ cosh²χ − s² sinh³χ = s² sinh χ(cosh²χ−sinh²χ) = s² sinh χ` — matches the claimed Jacobian exactly. Integrating this over `b≤s≤a`, `0≤χ≤H`, `0≤θ≤2π` by hand gives `V_shell(H)=(2π/3)(a³-b³)(cosh H-1)` and `V_inner(H)=(2π/3)b³(cosh H-1)` — both match exactly, and their ratio `(a³-b³)/b³=(a/b)³-1=2³-1=7` for `a/b=2` — confirmed exactly, a clean closed-form check. Independently recomputed the 3+1 ball-volume ratio `[(T²-b²)^{3/2}-(T²-a²)^{3/2}]/[T³-(T²-b²)^{3/2}]` numerically at `T=1/2,1,4`, getting `1.8532221454500828`, `2.7984473734168533`, `2.9882313661617776` — matching the ledger's quoted `≈1.85322214545`, `≈2.79844737342`, `≈2.98823136616` to the full quoted precision.

Ran `k4_nested_observability_hyperboloid_volumes_v15_1401.py` exactly as committed: all five PASS lines print, and the five printed `(T, shell/inner)` rows (including two, `T=3/5` and `T=2`, beyond what the ledger text quotes) are internally consistent with the same formula and confirm the monotonic trend toward 3 as `T→∞`.

## v15.1402 — state-count vs. shell-volume comparison: CONFIRMED

Independently verified `dim(H_q)/dim(H_EM)=2D/D=2` for every `D` (trivial from `dim=2J_Q+1=2D` vs. `dim=2j_E+1=D`). Independently verified the SU(2) orbit-area ratio `A_q/A_EM=J_Q/j_E=(2D-1)/(D-1)=2+1/(D-1)` by direct substitution of `J_Q=(2D-1)/2`, `j_E=(D-1)/2` — confirmed `=3` at `D=2`, `=5/2` at `D=3`, `=7/3` at `D=4`, and `→2` as `D→∞`, exactly as claimed. Ran `k4_quarter_orbit_count_vs_shell_volume_v15_1402.py` exactly as committed: all six printed `(D, EM_states, q2_states, orbit_ratio)` rows (`D=2,3,4,5,10,100`) match this formula exactly (`q2_states` is always exactly double `EM_states`; `orbit_ratio` at `D=5,10,100` gives `9/4, 19/9, 199/99`, all consistent with `(2D-1)/(D-1)`), and both PASS/NEGATIVE lines print as quoted.

## Collision check

No filename or version-number collisions: `v15.1403` was free immediately before this write (confirmed via fresh `git fetch origin master`, HEAD still `6aee2a9`).

## Summary for Lane A/Sandbox/Gravity

Another clean round. The 3:1 fixed-time annular partition (v15.1401) is exact and elegant geometry, independently reconfirmed by hand including a from-scratch Jacobian derivation for the regulated 7:1 comparison and precise numerical recomputation of the T-dependent 3+1 ratio. v15.1402 correctly shows this 3:1 figure does not survive contact with either of the two most natural alternative measures (finite Hilbert-dimension counting gives 2:1 always; SU(2) coadjoint-orbit symplectic area gives 3:1 only as an isolated D=2 coincidence, tending to 2:1 at large D) — a well-disclosed negative result consistent with the project's standing novelty-verdict discipline. No action-derived physical measure has been identified that would make any of these ratios a genuine Cone-specific prediction, which both entries state plainly.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
