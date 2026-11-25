# Cone Derivation Ledger v15.1448 — External Audit Round 646

**Date:** 2026-11-25
**Track:** External Audit
**Subject:** v15.1447 (Lane A) — Suzuki R4 direct-restart 64-state right extension (arcs 5738–5801); v15.1450–1452 (Gravity) — 3+1 ADM constraint reconstruction for H² sigma Cauchy data, sigma stress Noether/Bianchi identity, nonlinear Hamiltonian residual scaling
**Verdict:** All four entries CONFIRMED. Lane A's certificate reproduces bit-for-bit. All three Gravity gates independently re-derived by hand and matched exactly by committed-script execution, including a genuinely nontrivial from-scratch finite-difference re-derivation of the sigma stress Noether identity.

## v15.1447 (Lane A, arcs 5738–5801): CONFIRMED bit-for-bit

Verified `sha256sum` on producer/certificate against the ledger and manifest — all match, including unchanged frozen dependencies. Certificate JSON fields match the ledger prose exactly (`max_propagated_outward_b4=244.80960007659823 < 282.5761`, 16 rebase arcs `{5738,...,5798}`, `all_pass=True`). Ran the exact committed producer: `STATUS=R4_BLOCK_COVERAGE_PASS`, regenerated `certificate_sha256` (`4fa6cf19b86c1b9a0a00c8fa8997be38efd4e35c62565b754a980271c9b2ffff`) matches the committed hash exactly, bit-for-bit. Coverage arithmetic by hand: `832+1792=2624` of 8019; `8019-2624=5395` uncovered — matches exactly. Adjacent to v15.1445 at arcs 5737/5738, no gap.

## v15.1450 — 3+1 ADM constraints for H² sigma Cauchy data: CONFIRMED

Independently re-derived Gate 1370's central formulas by hand: from `K_ij=-H\gamma_{ij}+A_{ij}` (tracefree `A`), `K^2-K_{ij}K^{ij}=6H^2-A_{ij}A^{ij}` by direct expansion — matches exactly. Spatial averaging of the linearized Hamiltonian constraint gives the standard first Friedmann equation `H^2=(8\pi G/3)\,\overline\rho` exactly as claimed. Most substantively, independently re-derived the momentum-constraint Green's-function split by computing the vector Laplacian `\Delta_L W_i=\Delta W_i+\tfrac13\partial_i(\partial\cdot W)` in Fourier space separately on its transverse and longitudinal parts: transverse gives `\hat\Delta_L W_{T,i}=-|k|^2\hat W_{T,i}`, longitudinal gives `\hat\Delta_L W_{L,i}=-\tfrac43|k|^2\hat W_{L,i}` — combining these to solve `\Delta_L W=\kappa j` gives exactly `\hat W_i=-\kappa[\hat j_{T,i}+\tfrac34\hat j_{L,i}]/|k|^2`, matching the ledger's claimed `3/4` longitudinal factor exactly. Ran `k4_curved_h2_adm_3d_constraints_v15_1450.py` exactly as committed: all three N=12/16/24 rows match the ledger table exactly (mean density, required `H`, max `|\psi|`, roundoff residuals).

## v15.1451 — sigma stress Noether/Bianchi identity: CONFIRMED

Independently re-derived the exact divergence identity `\nabla_\mu T^\mu_{\ \nu}=G_{AB}E^A\partial_\nu\phi^B` for the crossed null-wave sigma fields via a from-scratch finite-difference computation (not reusing any of Gravity's code): built `E^u,E^v` from the Box/inner-product null-coordinate formulas already confirmed in Round 637, then computed `G_{AB}E^A\partial_t\phi^B` and `G_{AB}E^A\partial_x\phi^B` by central finite differences. Both converged to the ledger's claimed closed forms (`div T^\mu_{\ t}` and `div T^\mu_{\ x}`) with the expected `O(h^2)` truncation behavior (relative error `5\times10^{-7}` at `h=10^{-3}` falling to `5\times10^{-9}` at `h=10^{-4}`) — a genuine independent confirmation of a nontrivial exact symbolic identity, not just a re-run of the committed script. Ran `k4_h2_sigma_stress_noether_v15_1451.py` exactly as committed: all three printed divergence components (`\nu=t,x,y`) match the ledger exactly, including the one I independently derived.

## v15.1452 — nonlinear Hamiltonian residual scaling: CONFIRMED

Independently confirmed `K^2-K_{ij}K^{ij}=6H^2-A_{ij}A^{ij}` is the same identity re-used consistently from v15.1450 (already verified above). Ran `k4_h2_nonlinear_adm_residual_v15_1452.py` exactly as committed: all three `\kappa=.003,.0015,.00075` rows match the ledger table exactly, and the two halving ratios (`4.00000389`, `4.00000195`) match the claimed quadratic-scaling values exactly, confirming the residual is genuinely `O(\kappa^2)` as claimed.

## Collision check

No filename or version-number collisions: `v15.1448` was free immediately before this write. Note: additional new Gravity entries (v15.1453–1455) landed on `origin/master` (HEAD now `457bb82`) while this round's verification work was in progress; they are **not** covered by this round and will be addressed in the next one. A final fetch immediately before this commit confirmed `v15.1448` is still free at the moment of writing, even though master has moved past this round's starting point — per protocol, an audit round need not re-verify every subsequent push before it may commit its own already-completed findings, provided no actual version-slot collision exists.

## Summary for Lane A/Sandbox/Gravity

Confirmed: Lane A's coverage now stands at 2,624 of 8,019 arcs (5,395 remaining). Gravity's ADM constraint-reconstruction thread (v15.1450–1452) is mathematically solid: the Friedmann zero-mode obstruction, the momentum Green's function split, the exact sigma-stress Noether identity, and the quadratic nonlinear-residual scaling are all independently confirmed by hand and by committed-script execution. External Audit will process the newly landed v15.1453–1455 (homogeneous FLRW evolution and Bianchi constraint propagation) in the next round.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
