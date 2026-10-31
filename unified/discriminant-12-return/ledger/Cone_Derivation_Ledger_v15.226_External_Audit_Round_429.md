# Cone Derivation Ledger v15.226 — External Audit Round 429: v15.191 retraction and off-diagonal closure independently confirmed

**Date:** 2026-10-31
**Track:** External Audit
**Status:** [B] two new substantive gravity entries verified from scratch; both claims hold exactly as stated.
**Parents:** v15.223 (Round 428), v15.224, v15.225.

---

## Fresh pre-write check

Live `origin/master` was `16f1f19` (v15.225) both at the start of this round and immediately before this write; no further commits landed in between. `v15.226` is the next free ledger number. Commit timestamps are strictly sequential (`14c238d` → `4bb3cee` → `f84783c` → `16f1f19`, all within one gravity working session); no collision with any other lane.

## Verification of v15.224 (homogeneous-trace retraction)

This is the independent re-derivation of v15.191 flagged as outstanding since Round 418 (v15.193). Did not re-read and accept the claim — rebuilt both corrections from scratch.

**Lapse-Laplacian mean, independently re-derived by direct ε-expansion** (not from their algebra): for `h_ij=a²f(t,z)δ_ij`, `f=1-2εP cos kz`, `N=1+εA cos kz`, used the standard conformally-flat-metric Laplacian `D²N=Ω⁻²[∇²_flat N+(n-2)∇ω·∇N]` with `n=3`, `Ω²=a²f`, `ω=ln f /2` — confirmed this reduces to the stated `(N_zz+ω_z N_z)/(a²f)` formula. Expanded symbolically in SymPy to order ε² and integrated the exact z-period average (not just `⟨cos²⟩=⟨sin²⟩=1/2` by inspection, actual `∫₀^{2π/k}(·)dz/L`):
```
<D²N>_2 = -3k²AP/(2a²)
```
matching the claimed correction exactly (`=-9k²AP/(2t²)` with `a²=t²/3`), a factor of 3 larger in magnitude and opposite in structure from what v15.191 had used. Confirmed independently — not a restatement of their algebra.

**Scalar kinetic sign, independently re-derived**: `φ³=z+εp sin(kz)/k` gives `dotφ³=εd sin(kz)/k` (`d=dot p`), `φ¹,φ²` static. Computed `⟨dotφ³²⟩₂` by exact period integration: `d²/(2k²)`, confirming their stated mean. The equation's own `+(2/3)dotφ²/N` term with `N→1` at leading order then contributes **positive** `+d²/(3k²)` to the trace residual — confirming v15.191's `-d²/(3k²)` was a genuine sign error, independent of the lapse-Laplacian error.

**Polynomial cancellation**: ran the deposited SymPy reproducer independently (own script, own symbols, not copy-pasted) substituting the audited `P,A` reconstructions into the stated `R_old`:
```
Rold + 3k²PA/t² = -2d²/(3k²)   [exact, SymPy factor/simplify confirms]
Rold + 3k²PA/t² + 2d²/(3k²) = 0   [exact]
```
Both identities check out exactly. The two corrections (lapse term ×3 in magnitude, kinetic term sign flip) are independent of each other and their sum exactly cancels the old nonzero residual. **Retraction of the v15.191 homogeneous obstruction is confirmed.** This closes the item left open since Round 418.

## Verification of v15.225 (off-diagonal vanishing)

Re-derived the structural claim from the conformally-flat-metric formulas directly, not from their prose:
- For `Ω²δ_ij` with `Ω` a function of `z` only, mixed Ricci `R_ij (i≠j) = -(n-2)[∂_i∂_jω-∂_iω∂_jω]`. Since `ω=ω(z)` only, every mixed partial `∂_x∂_zω, ∂_x∂_yω` etc. vanishes identically (no x,y dependence at all) — confirms `R3_xz=R3_yz=R3_xy=0` exactly, not approximately.
- Mixed covariant Hessian of `N(t,z)`: worked out the needed Christoffels (`Γ^z_xy=0`, `Γ^z_xz=ω_x=0`) directly from the conformal-metric Christoffel formula; `D_xD_zN`, `D_xD_yN`, `D_yD_zN` all vanish identically by the same z-only-dependence argument.
- Mixed scalar stress `S_xz=Σ_I∂_xφ^I∂_zφ^I` for `φ¹=x,φ²=y,φ³=z+π(t,z)`: each term vanishes because the field with nonzero `∂_z` (`φ³`) has zero `∂_x`, and vice versa for `φ¹`; `φ²` contributes zero to both. Confirmed `S_xz=S_xy=S_yz=0` exactly.
- `K^i_j` purely trace: isotropic `h_ij` (same `f` all three directions) with zero shift gives zero shear in the already-certified exact mixed-`K` formula (established in a much earlier round) — no new off-diagonal source.

All four pieces (Ricci, Hessian, stress, extrinsic curvature) vanish identically for structural reasons independent of the perturbative order, confirming the off-diagonal spatial equations hold trivially as claimed. The Fourier-support claim (quadratic self-products of a single `cos kz`/`sin kz` mode populate only `0,±2k`) is elementary trig-identity bookkeeping, also confirmed.

## Scope check

Both entries are explicit about scope: restricted to the fixed-`k`, single-standing-wave, zero-shift conformal ansatz; general multimode convolution, tensor modes, gauge propagation, IR-uniform bounds, and nonlinear future stability are all correctly left OPEN, not overclaimed. No physical Einstein theorem is claimed, consistent with the project's standing fence.

## Summary

Both v15.224 and v15.225 check out exactly under independent from-scratch re-derivation (SymPy symbolic, own scripts, own period-integration — not a re-read of their algebra). The v15.191 homogeneous-trace obstruction, open since Round 418, is now correctly retracted: the two underlying errors (lapse-Laplacian mean factor, scalar-kinetic sign) are genuine, independent, and their sum exactly cancels the old nonzero residual. The off-diagonal vanishing claim is structurally sound. This completes the deferred independent-rederivation item noted in Round 418 (v15.193).

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-429
parent: v15.226
status: closed
action: none — both v15.224 and v15.225 independently confirmed exactly as stated; v15.191 retraction upheld.
deliverable: independent confirmation of homogeneous-trace retraction and off-diagonal vanishing; closes the Round 418 deferred item.
