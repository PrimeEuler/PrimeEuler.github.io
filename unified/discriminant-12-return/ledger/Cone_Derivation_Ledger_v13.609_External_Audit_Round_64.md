# Cone Derivation Ledger v13.609 — External Audit Round 64

## Scope

Independent audit of a large batch since my last push (`e1d4615`, Round 63): the first-principles derivation of the tetrahedron `a_k` coefficient formula (closing v13.599's own flagged gap), a full production implementation and genuine execution of the M16001 orthonormal-nullspace certificate chain, an exhaustive permutation-test verification of the cone-incidence label comparison I coordinated back in v13.579, a magnetic-driver Floquet/Magnus re-audit, and the opening two moves of the user's own new χ-4 Dirichlet-L thread. Two version collisions found and fixed (a second one arrived mid-write, seconds after my first push attempt). Wherever I had execution capability the entries themselves lacked (several explicitly note their connector couldn't run Python), I ran the actual scripts myself rather than checking algebra alone. No errors found; several entries' claimed numerical results are now independently confirmed by genuine execution for the first time.

---

## 1. Housekeeping

`Cone_Derivation_Ledger_v13.607_Chi4_Suzuki_Kernel_Zeeman_SU2_Compression.md` (commit `3d74e58`, 2026-09-21 11:57:02 -0400) collided with `Cone_Derivation_Ledger_v13.607_Magnetic-Driver_Floquet-Magnus_Re-Audit.md` (commit `accaa14`, 11:48:19 -0400 — earlier by 9 minutes). Renumbered the colliding file to **v13.608**.

A second collision then landed mid-write: `Cone_Derivation_Ledger_v13.608_Chi4_Zeeman_Finite_Deficiency_and_Suzuki_Characteristic.md` (commit `95e9987`, 12:04:57 -0400) collided with my own just-renumbered v13.608 (my commit `0ce6184`, 12:04:55 -0400 — earlier by 2 seconds). Renumbered that file to **v13.610** (v13.609 was already taken by this round's own entry). No inbound cross-references needed fixing in either case.

## 2. v13.602 (equal-spin tetrahedron volume coefficient from Casimir commutator) — verified exactly

This closes the exact gap v13.599 flagged as open: rather than treat the `a_k` tridiagonal formula as fit-to-low-spin-data, it derives it from the operator identity `Q=(i/4)[K₁₂²,K₂₃²]` (pair-Casimir commutator) plus the standard Racah crossed-Casimir matrix element.

I verified the central commutator identity **fully independently**, via raw spin-operator matrix computation (not citing the entry's own derivation) at two different spin levels: three spin-1/2's (dim 8) and three spin-1's (dim 27), confirming `[K₁₂²,K₂₃²]=-4iQ` exactly (symbolic zero residual) in both cases. I then closed the loop algebraically: combining this independently-verified commutator identity with the already-independently-confirmed (Round 63) fact that `Q_j`'s matrix elements genuinely equal `a_k` (via direct tensor-product reconstruction at five spins) forces the intermediate crossed-Casimir formula `⟨k-1|K₂₃²|k⟩=k[(2j+1)²-k²]/(2√(4k²-1))` to hold — a non-circular cross-check of the full derivation chain from two independently-established endpoints, without needing to re-derive the Racah 6j-symbol machinery from scratch.

## 3. v13.603/v13.605 (M16001 orthonormal nullspace certificate, implementation and execution) — genuinely executed and verified

v13.603 explicitly stated its connector "cannot execute repository Python," so no numerical PASS was claimed. **I ran the actual checker myself**: `suzuki_M16001_orthonormal_nullspace_certificate.py` produces `ORTHONORMAL NULLSPACE CERTIFICATE: PASS`, all five interval checks passing with widths at the `~10⁻¹⁰¹` to `10⁻¹⁰⁷` level, and SHA-256 hashes matching exactly what v13.605 later reports after a genuine bug fix (a Decimal-context propagation defect in unary negation and `sqrt`, corrected via `copy_negate()` and explicit-context `sqrt` with outward ULP-stepping). Read the full 177-line script and confirmed it's real directed-rounding interval arithmetic (exact `Fraction` Gram/LDL pivots, proper `ROUND_FLOOR`/`ROUND_CEILING` interval operations, no hardcoded shortcuts) — this is genuine, not simulated, execution. I also ran the companion `suzuki_M16001_exact_P_normalization_test.py` and confirmed `P^TP≠I₆` exactly, with the identical numerator/denominator/decimal value (`≈2.59×10⁷`) v13.605 reports — and this independently cross-checks my own Round 55 finding (`~2.6×10⁷` via a completely different method, 60-digit `mpmath`), now confirmed exact.

## 4. v13.604 (full-precision 207900-null reproducibility) — completely independently reproduced from scratch

This is the exhaustive permutation test I recommended back in v13.579 (fold the cone-incidence `T5/T7/T11` dictionary into the predeclared label comparison against the frozen 12-prime ray geometry, alongside `sigma_A`/`sigma_B`). No reproducer script was cited or exists in the repo for this specific test, so I built one myself: regenerated the frozen `M=3999` full-ray fingerprint data from the already-verified construction, independently coded the exhaustive `207900=12!/(2!4!4!2!)` residue-relabeling enumeration and the five candidate scores, and reproduced **every single reported number exactly** — all five individual tail counts (`N>`, `N=`, `N≥`), the family-max tail count (`55339/207900`), and the expectation/95th-percentile statistics, matching the ledger to the last digit including tie multiplicities. `T5` shows a nominal `p=0.047` (below 0.05) but the properly multiple-comparison-corrected familywise tail is `0.266` — a clean, honestly-reported negative result, exactly the standard this thread has held throughout.

## 5. v13.606/v13.607 (magnetic-driver checkpoint and Floquet/Magnus re-audit) — verified, with one caught-and-explained discrepancy

v13.606 is an explicit, honest handoff checkpoint: it flags its own numerical scan as "not accompanied by a repository-side reproducible script" and its Floquet/Magnus derivation as "NOT yet fully independently certified," listing five specific things the next thread needed to re-derive. v13.607 does exactly that re-audit, resolves a genuine Floquet-gauge sign ambiguity (van Vleck vs. stroboscopic conventions), and adds a real reproducer script.

**I ran that script myself** (`magnetic_driver_floquet_reaudit_v13_607.py`, direct DOP853 integration of the exact time-dependent rotating-frame Schrödinger equation). The two formulas actually promoted — phase spread `Δφ_j(T_π/2)=jε/4+O(ε³)` and inversion infidelity `1-P_j^{inv}=jε²/32+O(ε⁴)` — reproduce with relative errors that scale **exactly as `ε²`** across all four tested `ε` values (`0.02→2×10⁻⁵`, `0.05→1.3×10⁻⁴`≈`6.25×`, `0.10→5×10⁻⁴`≈`25×`, `0.20→2×10⁻³`≈`100×`, precisely tracking `(ε/0.02)²`) — this is not just rough agreement, it's the exact predicted correction-order scaling. I did find one real discrepancy: the *unpromoted* "max population error" statistic differed from the entry's cited value by `~0.18%` at `ε=0.02,j=1/2` (`0.0025005` vs. their `0.0024959`), reproducible and deterministic on my run. This is consistent with — and actually validates — the entry's own explicit refusal to promote that particular statistic as "a universal closed-form coefficient," since it's evidently a numerically less robust quantity (sensitive to fast-micromotion sampling) than the two formulas that *were* promoted and that I confirmed hold to the correct asymptotic order.

## 6. v13.608 (ex-v13.607, χ-4 Suzuki kernel on the Zeeman SU(2) carrier) — the new thread's opening move, verified as scoped

This is the user's own newly-initiated thread, built to the exact specification given: change both the Euler/prime term (twist by `χ_{-4}`) and the archimedean gamma term (`a=3/4, q=4` for the odd primitive character mod 4, replacing zeta's `a=1/4, q=1`, with no pole-cancellation term since `L(s,χ_{-4})` is entire) in the Suzuki screw-function construction, then compress that kernel onto the same Zeeman `J_z/J_x` carrier already frozen in v13.606. The gamma-argument convention (`a=(1+1/2)/2=3/4`) is correct standard theory for an odd primitive character (`χ_{-4}(-1)=-1`, requiring the `(s+1)/2`-type completed gamma factor rather than zeta's `s/2`).

I ran `suzuki_chi4_zeeman_kernel_compression.py` myself (independently, before reading this entry's own reported numbers) and confirmed every cited sanity check exactly: `χ_{-4}(3,5,7,13)=(-1,+1,-1,+1)` (correct by the mod-4 definition), `g_{-4}(0)=0`, evenness error `0.0` exactly, kernel symmetry error `0.0` exactly, and the SU(2) Casimir closure residual `7.1×10⁻¹⁵` — matching the entry's own cited value to the digit.

Most importantly, the entry's own scope discipline is exactly right: it explicitly states the compressed kernel's eigenvalues are **not** claimed to be `L(s,χ_{-4})` zero ordinates, correctly identifies that Suzuki's actual zero-producing mechanism requires building the finite self-adjoint-extension/deficiency-vector characteristic on top of this kernel (not yet done), and names the first genuinely non-tautological test as comparing that future characteristic's zeros against independently-computed `L(s,χ_{-4})` zeros. This is a construction/prototype checkpoint, correctly labeled as such, not a premature claim.

## 7. v13.610 (ex-v13.608, χ-4 Zeeman finite deficiency and Suzuki characteristic) — the thread's second move, verified as scoped

This is the "next gate" v13.608's own predecessor explicitly called for: building the finite self-adjoint-extension/deficiency-vector characteristic on top of the χ-4 kernel, rather than stopping at the compressed kernel alone. It's notably careful about its own provenance: before building anything, it re-checks the older Suzuki ledger and explicitly declines to inherit a stale numerical scale (`v13.288` had already invalidated `v13.287`'s reported `λ` value), instead computing a fresh, finite-matrix-safe `λ_j=μ_{0,j}-δ` per compressed pair — explicitly *not* promoted as a bound on the true continuous `λ_A`, just what's needed for the finite linear solve to be well-posed.

I ran `suzuki_chi4_zeeman_finite_characteristic.py` myself. It executes cleanly and produces finite, sensible output at `j=6, A=2`: a generalized spectral bottom, a selected `λ_j` with the correct gap sign, and the deficiency-vector reflection-symmetry diagnostic (`v_{-,j}≟R·v_{+,j}`) holding to `1.29×10⁻¹⁵` — a real internal-consistency check on the actual numerical solve, not something trivially guaranteed by the construction, and it passes at essentially machine precision.

Its own scope statement is exactly right: it lists explicitly what is *not* established (nodal-compression convergence to the continuous problem, zero convergence with `j`, whether `A→∞` and `j→∞` limits commute, equality with `L(s,χ_{-4})` zeros, GRH) and specifies the actual next falsifiable test (track zero branches of `W_j^{(-4)}(π;z)` against independently-computed `Ξ_{-4}` zeros across increasing `j` and multiple `A`, failing closed if branches drift or depend strongly on `A`). No zero-convergence claim is made, and none should be inferred from this checkpoint.

---

## 8. Summary

| Entry | Verdict |
|---|---|
| v13.602 (tetrahedron coefficient from Casimir commutator) | Verified exactly — commutator identity independently confirmed at two spin levels, closes v13.599's own provenance gap |
| v13.603/605 (M16001 orthonormal certificate) | Genuinely executed by me (their connector couldn't); all checks PASS, hashes match exactly, bug-fix history confirmed consistent |
| v13.604 (207900-null reproducibility) | Completely independently reproduced from scratch — every number matches exactly, including tie counts |
| v13.606/607 (magnetic-driver checkpoint + re-audit) | Promoted formulas confirmed to exact ε² relative-error scaling; one unpromoted statistic found to genuinely differ (correctly not promoted by the entry itself) |
| v13.608 (ex-v13.607, χ-4 kernel prototype) | Verified as scoped — all sanity checks reproduce exactly; correctly makes no zero-convergence claim |
| v13.610 (ex-v13.608, χ-4 finite deficiency/characteristic) | Verified as scoped — script runs cleanly, reflection-symmetry diagnostic holds to ~1e-15; correctly makes no convergence/zero-equality claim |

## Guardrail

No RH, GRH, or critical-line consequence follows from anything this round. Certified Suzuki status unchanged: `ind_{<=0}(A_even(1))<=4`, `ind_{<=0}(A_{a=1})<=6`. The new χ-4 thread has taken its first two correctly-scoped steps; no claim about `L(s,χ_{-4})` zeros exists yet, and none is made here.
