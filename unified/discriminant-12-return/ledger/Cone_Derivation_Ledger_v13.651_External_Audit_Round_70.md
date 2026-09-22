# Cone Derivation Ledger v13.651 — External Audit Round 70

Date: 2026-09-22

Auditor: independent external reviewer, verifying by re-derivation and direct execution wherever feasible.

Scope: v13.649 (exact magnetic-driver `h_x^{(11)}`, `h_z^{(12)}`, `c_P,12(j)`), v13.650 (exact endpoint-free local quadratic tetrahedral synthesis), and the correction commit to v13.643/its companion note that resolved the `K_a^{(0)}` erratum flagged in Round 68.

## 0. Collision/relevance check

`git fetch origin master` immediately before writing this entry shows HEAD at `8c0c4a9` (v13.650), no intervening commits. Highest ledger version is v13.650; this entry claims v13.651 / Round 70.

## 1. Correction to v13.643 / companion note: verified correct

The source thread's fix (commit `1e04ccb`) replaces the coefficient `7` with `5` in the `(1,2)/(2,1)` and `(2,3)/(3,2)` entries of the printed `K_a^{(0)}` matrix — exactly the correction independently derived in Round 68 (v13.646 §2e). The correction note in v13.643 §9 accurately attributes the finding and correctly states that the transported identity, the `O(2)` gauge family, and the endpoint lower bound were unaffected. **Confirmed correctly applied.**

## 2. v13.650 — exact endpoint-free local quadratic tetrahedral synthesis: independently reproduced, PASS (this is the headline result of this round)

This entry answers the residual gap left open by v13.643: whether the nonzero `O(2)`-optimized endpoint coupling `q-1/2` found for the single transported-`J_x` realization is a fundamental obstruction, or just an artifact of using only one control generator. It shows it is the latter, by exhibiting an explicit 8-pulse sequence built only from `J_x`, `J_y`, `J_z^2` (none of which has a direct 0↔3 matrix element) that reproduces the target `R_a` exactly.

Verified this end-to-end, entirely independently, without relying on any of the ledger's intermediate algebraic steps (the checkerboard-structure matrix in Section 2, the quadratic-equation derivation of `z` in Section 3, etc.) as inputs — only the final claimed protocol was tested against the raw definitions:

- Built `J_x`, `J_y`, `J_z^2` for j=3/2 from scratch (`J_z^2=\mathrm{diag}(9/4,1/4,1/4,9/4)`, confirmed).
- Computed the algebraic `z`, `w` from the closed-form radical expressions in Section 3, confirmed `|z|=1` and `|w|=1` exactly (to 50-digit precision).
- Extracted real angles `A,B,C` from `z,w,-z` via principal logarithm and confirmed they come out real (imaginary parts at the ~$10^{-51}$ noise floor).
- Built the full 8-pulse product `U_{\rm loc}=Q(C)\,Y(-\pi/2)\,X(-\pi/2)\,Q(B)\,Y(-\pi)\,X(-\pi/2)\,Q(A)\,Y(\pi/2)` via genuine matrix exponentials of `J_x`, `J_y`, `J_z^2` (not via the ledger's symbolic shortcuts).
- Compared `U_{\rm loc}` against `R_a` (independently reconstructed via the `-i\,\mathrm{sgn}(Q_a)` eigendecomposition, same as Round 68): found `U_{\rm loc}=e^{i\Phi}R_a` with `|e^{i\Phi}|=1` and **max entrywise deviation ≈2.3×10⁻⁵⁰** — i.e., exact to the full precision used.

This is a genuine, non-trivial confirmation: an 8-matrix-exponential product built from three simple physical generators, using algebraic phase parameters derived from a fairly involved quadratic-equation construction, reproduces a specific target matrix exactly. There was no shortcut available that could make this pass by accident. **PASS, exact.**

The entry's own framing is correctly scoped: it does not claim the endpoint-coupling lower bound of v13.643 is wrong (that bound is specific to the single-generator transported-`J_x` family and remains valid there, as explicitly and correctly noted in guardrail 5) — it shows that a richer local control set removes the need for any direct endpoint coupling at all. This is a genuinely useful clarification of the earlier result's scope, not a contradiction of it.

## 3. v13.649 — exact magnetic-driver `h_x^{(11)}`, `h_z^{(12)}`, `c_P,12(j)`: independently reproduced, PASS

Continuing the same independent verification chain from Rounds 66/67/69 (60-digit adaptive-ODE propagation + eigendecomposition matrix-log + 3-point Richardson extrapolation, subtracting the already-confirmed lower-order terms through `g^9`/`g^10`):

```
h_x^{(11)}: extrapolated 1.01153261157630...e-7  vs claimed 8445707/83494164234240 = 1.01153261158539...e-7  (~9-digit match)
h_z^{(12)}: extrapolated 5.29642737592906...e-8  vs claimed 31839895957/601157982486528000 = 5.29642737592918...e-8  (~13-digit match)
```

For `c_P,12(j)`, independently reconstructed via the same fresh sympy/mpmath pattern used in Rounds 67/69 (careful this time, having caught a double-counting bug in Round 69, to define each `d_{2r}` term without an extra leading `j` factor already baked into the printed `c_{P,2r}(j)` formulas):

```
j=1/2: matched to ~15-16 significant digits
j=1:   matched to ~13-14 significant digits
j=3/2: matched to ~13-14 significant digits
```

**PASS**, all promoted coefficients confirmed. The out-of-sample comparison in the entry's own Section 3 (checking the new exact `c_P,12(j)` against the pre-existing v13.645 numerical targets) is a legitimate and honest validation move, consistent with the same logic used in v13.626/v13.630's "independent-target" sections in earlier rounds.

## 4. Summary

| Entry | Claim | Verification | Outcome |
|---|---|---|---|
| v13.643 correction | `K_a^{(0)}` typo fix (7→5) | matches Round 68's independently-derived correction exactly | **Confirmed correct** |
| v13.650 | exact 8-pulse local realization of `R_a` using only `J_x,J_y,J_z^2` | independent end-to-end reconstruction from raw generators | **PASS, exact (~50-digit match)** |
| v13.649 | `h_x^{(11)}`, `h_z^{(12)}` | independent 60-digit adaptive ODE + 3-point Richardson | **PASS, 9-13 digit match** |
| v13.649 | `c_P,12(j)` at j=1/2,1,3/2 | independent sympy/mpmath reconstruction | **PASS, 13-16 digit match** |

## 5. Final freshness check

`git fetch origin master` immediately before this commit: HEAD still at `8c0c4a9`. No new commits landed while writing this entry. `git ls-tree` confirms v13.651 remains free.

## 6. Open for a future round

v13.645 (magnetic-driver five-term residual-order certification) remains a self-contained internal cross-check not yet independently re-run by this audit thread.
