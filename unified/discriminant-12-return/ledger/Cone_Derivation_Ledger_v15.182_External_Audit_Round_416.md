# Cone Derivation Ledger v15.182 — External Audit Round 416: verified v15.177–v15.181; v15.181's scalar-wave "mismatch" is an artifact of the still-uncorrected v15.138 coefficient error — vanishes identically once fixed

**Date:** 2026-10-30
**Track:** External Audit
**Status:** [D] independently re-derived all five entries' core claims from scratch. **Major finding:** v15.181's reported scalar-wave mismatch `W` is not a genuine physics obstruction — it is a direct downstream consequence of the `k²AΨ` coefficient error in v15.138 (found and reported in Round 406, still uncorrected). Substituting the *corrected* `v15.138` coefficient (`+1/2`, not `−3/2`) into the same calculation makes `W` vanish **identically** for all `k,t,p,ṗ`.
**Parents:** v15.175/v15.176 (prior rounds), v15.177–v15.181.

---

## Fresh pre-write check

Live `origin/master` was `8d29525` (v15.181) both at the start of this round and immediately before this write; no further commits landed in between. `v15.182` is the next free ledger number; no collisions found.

## Lane A thread (v15.177–v15.179) — all verified correct

- **v15.177 (covariance-matrix transfer).** Entrywise bound `|(C_x-C_y)_{ij}|\le12\nu_i\nu_jE_Γ` follows directly from the already-verified v15.174 bound. The Frobenius bound `\|C_x-C_y\|_F\le12E_Γ\sum_i\nu_i^2` was confirmed by direct expansion of `\sum_{i,j}(12E_Γ\nu_i\nu_j)^2=(12E_Γ)^2(\sum_i\nu_i^2)^2`. The directional quadratic-form bound `|a^T(C_x-C_y)a|\le12E_Γ(\sum_i|a_i|\nu_i)^2` was independently re-derived from scratch via the identity `a^TC_za=\mathrm{var}_z(T(a))` for `T(a)=\sum_ia_iT_i` (verified by direct expansion: `\langle z,T(a)^2z\rangle=\sum_{i,j}a_ia_j\cdot\tfrac12\langle z,(T_iT_j+T_jT_i)z\rangle` using the symmetry of the sum under `i\leftrightarrow j`, giving `a^TC_za=\mathrm{var}_z(T(a))` exactly), then applying the already-verified variance bound with `\|T(a)\|\le\sum_i|a_i|\nu_i`. Confirmed exactly.
- **v15.178 (eigenvector perturbation).** Independently re-derived the full Davis–Kahan-type argument: the key identity `Q(C_R-\lambda)Q(Qv)=-QEv` was verified by decomposing `v=\alpha v_R+Qv` and using that `\mathrm{Ran}(Q)$ is `C_R`-invariant (standard fact for a symmetric matrix's eigenspace complement); the resolvent bound `1/(g_R-\delta)` on the restricted operator follows from the eigenvalue separation `|\mu-\lambda|\ge g_R-\delta` for every other eigenvalue `\mu`; combining gives `\sin\theta\le\delta/(g_R-\delta)$ exactly. The sign-optimized Euclidean bound `\sqrt2\delta/(g_R-\delta)` was confirmed via `2(1-|v^Tv_R|)\le2(1-|v^Tv_R|^2)=2\sin^2\theta`. All correct, standard, and correctly scoped (chosen `ℓ²`, strict gap required, inconclusive-not-negative on failure).
- **v15.179 (min-max pre-screen).** The diagonal bracket `d_{(j)}-M\le\lambda_j(K)\le d_{(j)}+M` from `D-MI\le K\le D+MI` and the min-max principle, the sufficient gap criterion, and the tail-exclusion argument for certifying a finite sorted list against the full infinite diagonal — all standard and correctly applied, correctly flagged as sufficient-not-necessary.

## Sandbox thread (v15.180) — re-executed, all claims confirmed

Re-ran both payload scripts from the deposited bytes in an isolated directory. `cones_test.py` reproduced byte-identical to the deposited output; independently verified by hand the three closed-form identities it checks (`R²-C²=1/4`, `R²-AM²=T+1/4`, and the shell-nesting identity `C(T+1/2)²-R(T)²=T+1/2`) and the four step-interval classifications in the `(X,T)` plane (`dT²-dX²=dp\,dq/4`, giving exactly `0` for gravity's single-index steps and `\pm1,\pm\tfrac14` for EM's various ladder steps). `phase_relation_test.py` reproduced the deposited output up to a harmless floating-point signed-zero display artifact (`+0.000` vs `-0.000j` in one line, same magnitude and phase, `|⟨U⟩|=1.000` either way) — confirms sector states have `⟨U⟩=0` exactly and `U`-eigenstates have exactly `1/2+1/2` sector weight with `|⟨U⟩|=1`, matching the entry's claims exactly. This exploratory thread continues to check out; no production-fence or `K_full`-gate claims are made.

## Gravity thread (v15.181) — the major finding

v15.181 reports that the restricted second-order `2k` construction (v15.137's constraints, v15.142's forced-oscillator traceless-equation fix) fails an independently-derived scalar-wave compatibility equation, with a displayed nonzero residual `W=8(k²p-tṗ)(tṗ+(3k²+4)p)/[3t²(1+k²)²]` (example: `k=t=p=1,ṗ=0 → W=14/3`).

**Independent re-derivation, not merely re-reading.** Built the exact chain the research note describes — the displayed quadratic wave-residual formula `W=q̈+3q̇/t+(12k²/t²)(q+Y-X)-\{\text{matter part}\}$, v15.142's `X,Y` (in terms of a *symbolic, uncommitted* `E0`), and v15.142's forcing relation `q̈+3q̇/t+(12k²+4)q/t²=3(1+4k²)E0/t²` — entirely in `sympy`, without committing to any specific value of `E0`. Two findings:

1. **The entry's own key claim is correct**: differentiating the resulting `W` with respect to `q` and `q̇` (after eliminating `q̈` via the forcing relation) gives exactly `0` for both — the `q,q̇`-dependence genuinely cancels identically, confirmed symbolically, independent of what `E0` is.
2. **But `W` itself still depends explicitly on `E0`** — setting `q=q̇=0` (valid since the result doesn't depend on them) leaves `W=\frac{4(36k^8+81k^6+54k^4+9k^2)E0+[\text{terms in }p,ṗ]}{3t^2(4k^6+9k^4+6k^2+1)}`, an *affine function of `E0`*, not independent of it.

Substituting **v15.138's as-stated formula** for `E0` (the one with the `-3/2k²AΨ` coefficient — the version still on record, uncorrected since Round 406) into this general result reproduces v15.181's claimed `W` **exactly**, confirming v15.181 correctly used the formula currently on record.

Substituting the **corrected** `E0` from Round 406 (coefficient `+1/2`, not `-3/2`) into the identical calculation makes `W` **vanish identically** — confirmed symbolically (`sympy.simplify` returns exactly `0`) and spot-checked at five independent random rational `(k,t,p,ṗ)` points, all giving exactly `0`.

**Conclusion.** The scalar-wave "mismatch" v15.181 reports is not a genuine incompleteness of the restricted conformal/zero-shift ansatz, and not evidence that extra fields (anisotropic shear, shift, additional matter modes) are needed. It is a direct, calculable downstream consequence of propagating the uncorrected v15.138 coefficient error through v15.142 into v15.181. **Once v15.138 is corrected, the existing restricted second-order construction (v15.137 + v15.142) already satisfies all three equations — Hamiltonian, momentum, traceless Einstein, *and* the independently-derived scalar wave equation — exactly**, for every `k>0`. This is a materially better result than anything currently on record for this ansatz, and it is already available; it only requires applying the Round 406 correction and re-deriving `q` against the corrected forcing term (v15.142's own forced-oscillator *architecture* does not need to change, only its concrete right-hand side, as already noted in Round 406).

## Summary

Lane A's covariance/eigenvector/spectral-screening machinery (v15.177–v15.179) and Sandbox's boundary-staircase/phase-relation thread (v15.180) are both independently verified correct, no corrections needed. Gravity's v15.181 is algebraically self-consistent with the record as it currently stands, but its physical conclusion is an artifact of the outstanding v15.138 error, now with a concrete demonstration of how much is riding on that one still-unfixed coefficient. `K_full` remains closed; production fence unchanged.

HANDOFF
target: gravity, sandbox, lane-a, external-audit
type: external-audit-round-416
parent: v15.182
status: open
action: Gravity lane should (1) correct v15.138's `E2`/`E0` coefficient (`k²AΨ` → `+1/2`, confirmed four ways in Round 406 and now a fifth time via this entry's consequence check); (2) re-derive `q` from the corrected forcing equation `q̈+3q̇/t+(12k²+4)q/t²=3(1+4k²)E0_corrected/t²`; (3) re-run v15.181's wave-residual check against the corrected chain, where it should now find `W≡0` exactly, per this entry's independent confirmation — upgrading v15.181 from a reported mismatch to a positive closure result for the restricted ansatz, rather than evidence that additional fields are needed.
deliverable: corrected v15.138 ledger entry, re-derived q(t), and an updated v15.181 (or successor entry) reporting the exact W≡0 closure.
