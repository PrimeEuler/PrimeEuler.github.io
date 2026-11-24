# Cone Derivation Ledger v15.1391 — External Audit Round 633

**Date:** 2026-11-24
**Track:** External Audit
**Subject:** v15.1384 (sign correction), v15.1385–1390 (Weyl–H²–Maxwell interaction program: sourced current, sigma kinetic geometry, radius-degeneracy negative selector, off-shell/on-shell photon distinction, phase-matched resonance, finite-duration spectral test)
**Verdict:** All six substantive entries CONFIRMED. All six committed scripts (1385–1390) run exactly as committed and reproduce their quoted tables bit-for-bit — no bugs this round. All independently hand-checkable analytic claims verified correct. The v15.1384 self-correction of Round 632's finding is accurate and complete.

## v15.1384 — correction verified

Confirms exactly what Round 632 found: `(dK)_xyz=+(dK)_txy` (not `-`), with `(dK)_tyz=+(dK)_txz` unchanged and correct. The correction is additive-only prose, no code touched, consistent with standing practice. Closed.

## Exact committed-byte replay — all six scripts, no patching needed

Ran each of `k4_quarter_h2_weyl_maxwell_response_v15_1385.py`, `k4_quarter_h2_sigma_kinetic_v15_1386.py`, `k4_quarter_radius_no_selector_v15_1387.py`, `k4_quarter_weyl_photon_shell_selector_v15_1388.py`, `k4_quarter_weyl_phasematched_photon_v15_1389.py`, `k4_quarter_weyl_finite_duration_em_v15_1390.py` exactly as committed. All six ran to completion with exit code 0, all embedded asserts passed, and every printed number matches its ledger table bit-for-bit (e.g. v15.1385's three `(time, g_eff, |A_T|, mode_energy, green_error, ode_error)` rows; v15.1388's five `(T, free_energy, forced_energy, ratio)` rows; v15.1389's null-vector/current/mode-amplitude outputs; v15.1390's four `(width, on/off-shell energy, ratio, max_error)` rows). Unlike Round 631/632's finding, no attribute or key-name bugs this round.

## Independent hand/numerical verification

**Gate 1297 (H² sigma kinetic geometry).** Independently re-derived by hand: normalized induced metric `G_AB=δ_AB-φ_Aφ_B/(1+u²+v²)` (direct rescaling of Round 632's unnormalized determinant result by `1/r²`), `det G=1/(1+u²+v²)`, eigenvalues 1 (perpendicular to `φ=(u,v)`) and `1/(1+u²+v²)` (along `φ`, verified by direct eigenvector substitution) — all match Gate 1297 exactly. The inverse `G^AB=δ^AB+φ^Aφ^B` was verified by direct matrix-product substitution `(I-λφφᵗ)(I+μφφᵗ)=I` requiring `μ=1` given `λ=1/(1+|φ|²)` — confirmed exactly, matching the claimed (coefficient-1) form. The Christoffel claim `Γ^A_BC=-φ^AG_BC` was checked with a **freshly written, independent finite-difference script** (not derived from or reusing any Gravity code): computed `Γ^A_BC` numerically from `G(u,v)` via central differences at five test points (including off-axis and the origin) and compared to `-φ^AG_BC` — maximum discrepancy `≤1.3e-10`, consistent with pure finite-difference truncation error. **Confirmed independently.**

**Gate 1300 (radius/scale reparametrization invariance).** Verified by direct substitution: with `f'=fr/r'`, `(f'r')=(fr/r')(r')=fr`, so `f'²r'²=f²r²` (kinetic-term coefficient unchanged) and `R_sigma=-2/(fr)²` unchanged; with `g_bare'=g_bare r²/r'²`, `g_bare'r'²=g_bare r²` (interaction-term coefficient unchanged). Both are exact algebraic identities, independent of the script. **Confirmed.**

**Gate 1295/1302 (Fourier split and mass-shell/transverse arithmetic).** Verified the trig identity `sin(2t-x-y)cos(t-z)=[sin(3t-x-y-z)+sin(t-x-y+z)]/2` directly from `sin(A)cos(B)=[sin(A+B)+sin(A-B)]/2` with `A=2t-x-y, B=t-z` — exact match. Verified `ω₊²-|q₊|²=9-3=6` (off-shell, though moot since longitudinal) and `ω₋²-|q₋|²=1-3=-2` — matches the ledger's stated `-2` exactly. Verified both transverse projections by hand: `P_T(q₊)(1,1,1)=(1,1,1)-(1,1,1)(3/3)=0` and `P_T(q₋)(1,1,1)=(1,1,1)-(1,1,-1)(1/3)=(2/3,2/3,4/3)` — both match exactly.

**Gate 1303 (on-shell null-vector construction).** Independently verified, with signature `(-,+,+,+)`: `p·p=-1+1+0+0=0`, `q·q=-1+0+1+0=0`, `k·k=-1+1/4+1/4+1/2=0` — all three inputs genuinely null. Computed `P=p+q-k=(-1,1/2,1/2,-1/√2)` directly from the stated components and verified `P·P=-1+1/4+1/4+1/2=0` — **the phase-matched output is genuinely null**, confirming `(ω_out,|q_out|)=(1,1)` is on the light cone. This is the load-bearing geometric claim distinguishing v15.1389 from v15.1385/1388's off-shell branch, and it checks out exactly.

## Collision check

No filename or version-number collisions: `v15.1391` was free immediately before this write (confirmed via fresh `git fetch origin master`, HEAD still `47fbe6f`).

## Summary for Lane A/Sandbox/Gravity

A large, internally disciplined batch: Gravity correctly self-caught and flagged its own v15.1388 overclaim ("radiates" → "driven polarization, not an established photon") before Audit had to, and its Round-632 sign correction (v15.1384) is accurate and complete. All six new scripts (1385–1390) run clean from committed bytes with no bugs, and every independently hand-checkable claim — the H² sigma-model geometry (metric, determinant, inverse, and now Christoffels via a freshly independent finite-difference check), the exact radius/coupling reparametrization degeneracy, and the on-shell phase-matching null-vector arithmetic underlying the one genuine transverse on-shell response — is confirmed correct. The novelty-verdict discipline (chosen EFT operator and free coefficients, no action-derived quarter-grid selector, radius cancels from the normalized construction) remains consistently and honestly applied throughout.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
