# Cone Derivation Ledger v13.695 — External Audit Round 79

Date: 2026-09-23

Auditor: independent external reviewer, verifying by fresh independent computation.

Scope: v13.690 (geometric mirror C2^3 / harmonic-divisor checkpoint), v13.691 (rapidity/circle normalization and divisor null-coordinate bridge), v13.692 (centered 5-6-7 half-cell and quadratic-character gate), v13.693 (pronic half-integer completion and U(12) return gate), v13.694 (pronic mod-24 root carrier equals U(24)) — a revived thread connecting the four classical Pythagorean means (HM, GM, AM, QM) to the project's established U(12)/U(24) character machinery via pronic numbers and half-integer lattice completions.

## 0. Collision/relevance check

`git fetch origin master` immediately before writing this entry shows HEAD at `cb2844d` (v13.694), no intervening commits. Highest ledger version is v13.694; this entry claims v13.695 / Round 79.

## 1. v13.690 — geometric mirror C2^3 and harmonic-divisor checkpoint: PASS

The finite sign-cube decomposition (`\Sigma\cong C_2^3`, `V_4=\ker(x_1+x_2+x_3)`, the exact sequence `1\to V_4\to C_2^3\to C_2\to1`) is internally consistent: independently re-enumerated all eight sign patterns `(s_1,s_2,s_3)` against the stated parity table and confirmed the four even-parity elements `\{(+,+,+),(-,-,+),(-,+,-),(+,-,-)\}` are exactly those matched to `\{1,7,5,11\}` (the genuine `U(12)` translations), consistent with the previously-audited `\chi_{12}\chi_{-4}\chi_{-3}=1` identity (Round 75, v13.679 §5). The `\sigma_X=\rho` claim (geometric mirror equals the all-three-flip element as a permutation of the six-state carrier) is a structural reading of v13.678's line labeling and is appropriately hedged (§6: "meaningful even though it is external to the affine AG(2,2) incidence action") rather than overclaimed as a new incidence symmetry. The `nH_n`/`D(n)`/A161664 identities preserved in §7 were independently checked (see Section 2 below) and match exactly. **PASS.**

## 2. v13.691 — rapidity/circle normalization and divisor bridge: independently verified, PASS

Independently checked the core exact identities by direct symbolic computation on several random rational `(x,y)` pairs: `A^2=D^2+G^2`, `A\cdot H_{\rm harm}=G^2`, and the newly derived `Q^2=A^2+D^2` all confirmed to hold exactly (not approximately) in every case tested. The Gudermannian-function content of §3-4 (`z_{\rm geom}(s)=\operatorname{sech}s+i\tanh s`, `|z_{\rm geom}|=1` identically, the half-angle identity `\tan(\theta/2)=\tanh(s/2)`, and its Cayley/Weierstrass-substitution form) is standard and was independently re-derived by hand: `\operatorname{sech}^2s+\tanh^2s=1` is the elementary hyperbolic identity, and the Cayley form follows from the standard tangent-half-angle substitution for `e^{i\theta}`. The audit's own guardrail in §4 (not conflating the real compactification `\theta(s)` with analytic continuation `s\mapsto i\theta`) is a correct and useful distinction, not overreach.

The divisor-summatory bridge (`v_k=-X_k`, `\mathcal A_{\rm div}(n)=nH_n-T_n`, the `2(v_k\bmod\tfrac12)=\{n/k\}` fractional-part identity, and `T_n-D(n)=\mathcal B_{\rm div}(n)-\mathcal A_{\rm div}(n)`) was independently re-implemented from scratch in exact rational arithmetic and checked for `n=1,\ldots,29`: all identities hold exactly in every case, including the `\bmod\tfrac12` fractional-part identity, which is the least obvious of the chain (it relies on `k/2` always being an integer multiple of the modulus `1/2` regardless of the parity of `k`, which this audit independently re-derived and confirms). **PASS, exact.**

## 3. v13.692 — centered 5-6-7 half-cell and character gate: independently verified, PASS

Independently recomputed the pronic/half-integer completion `(m+\tfrac12)^2-\tfrac14=m(m+1)` and its instances at `T=3\pm\tfrac12` (`9-\tfrac14=\tfrac{35}{4}=\tfrac52\cdot\tfrac72`), and the mod-12 fact `5\cdot7=35\equiv11\pmod{12}` — all confirmed by direct computation.

The character table is the entry's most checkable factual claim and was independently rebuilt from the standard definitions (`\chi_{-4}(n)=+1` if `n\equiv1\pmod4`, `-1` if `n\equiv3\pmod4`; `\chi_{-3}(n)=+1` if `n\equiv1\pmod3`, `-1` if `n\equiv2\pmod3`; `\chi_{12}=\chi_{-4}\chi_{-3}`) rather than copied from the entry, and matches exactly at `n=1,5,7,11`:

| n | chi_12 | chi_-4 | chi_-3 |
|---|---|---|---|
| 1 | +1 | +1 | +1 |
| 5 | -1 | +1 | -1 |
| 7 | -1 | -1 | +1 |
| 11 | +1 | -1 | -1 |

Multiplicativity `\chi(5)\chi(7)=\chi(11)` independently confirmed for all three characters. The `Q^2=A^2+D^2=G^2+2D^2=2A^2-G^2` derivation opening the quadratic-mean gate (§10, the specific connection the project owner flagged) was independently re-derived from `x=A+D,y=A-D` and confirmed algebraically exact. **PASS**, with appropriately scoped limitation language in §6 (the half-cell geometry does not itself derive the Dirichlet `L`-function or its analytic continuation) that this audit agrees is the correct boundary to draw.

## 4. v13.693 — pronic half-integer completion and U(12) return gate: independently verified, PASS

Independently re-derived and computationally confirmed the central claim `6\mid P_m\iff r_m=2m+1\in U(12)` by brute-force enumeration over `m=0,\ldots,59`: the set of `(2m+1)\bmod12` over all admissible `m` (those with `6\mid m(m+1)`) is exactly `\{1,5,7,11\}=U(12)`, matching the entry's claim precisely, including the specific admissible-residue claim `m\equiv0,2,3,5\pmod6`.

Independently verified the mod-24 lift claim in §5: computed all eight solutions of `r^2\equiv1\pmod{24}` directly and confirmed the set is exactly `\{1,5,7,11,13,17,19,23\}`, matching the entry's stated count and its explicit converse argument via `P=(r-1)/2\cdot(r+1)/2`. The central `35\)-\(36\)-\(37` RMS-cell computation (`(2G)^2=35`, `(2A)^2=36`, `(2Q)^2=37`, with `35\equiv11`, `37\equiv1\pmod{12}` giving the complementary `\chi_{12}=+1` fiber `\{1,11\}`) was independently recomputed and confirmed exact. **PASS.**

## 5. v13.694 — pronic mod-24 root carrier equals U(24): independently verified, PASS

This entry's central claim — that `\{r\bmod24:r^2\equiv1\pmod{24}\}` is not merely isomorphic to but *literally identical as a subset of* `\mathbb Z/24\mathbb Z` to `U(24)=\{\pm1,\pm5,\pm7,\pm11\}` — was independently checked by direct enumeration of both sets and found to be exactly equal: `\{1,5,7,11,13,17,19,23\}`. This is the same computation underlying v13.693 §5, now stated at its natural level of generality; the audit confirms both entries are consistent with each other and with the independent computation.

Independently verified group closure and the exponent-2 (self-inverse) property of this root set under multiplication mod 24 (`r^2\equiv1` for every element, and the product of any two elements remains in the set) — confirming the `C_2^3` group-law claim of §3 computationally rather than only citing the abstract CRT argument. The CRT explanation in §8 (`24=8\cdot3`, dyadic condition mod 8 automatic for odd `r`, discriminant-12-unramified condition at 3 giving `6\mid m(m+1)`) is a correct and clean structural explanation for why 24 is the natural modulus here, independently re-derived by this audit and confirmed to match. The central-pronic-generators claim (`5\cdot7=35\equiv11\pmod{24}`, giving `\langle5,7\rangle=\{1,5,7,11\}` and `\langle5,7,-1\rangle=U(24)`) checks out arithmetically. **PASS.**

The entry's own guardrail in §7 (only the `\chi_{-4}\leftrightarrow R_Y` leg has intrinsic canonical justification; the full three-axis assignment is a compatible intertwiner, not a basis-free canonical one) correctly carries forward a limitation already established in the prior, separately-audited v13.530 thread, rather than silently dropping it now that a new identification has been found.

## 6. Summary

| Entry | Claim | Verification | Outcome |
|---|---|---|---|
| v13.690 | C2^3 sign cube, V4 = even-parity subgroup, geometric mirror = all-flip coset element | independent enumeration of all 8 sign patterns against parity table | **PASS** |
| v13.691 | Pythagorean-mean cone identities, Gudermannian compactification, `nH_n`/`D(n)`/A161664 divisor bridge | independent symbolic + exact-rational computation, n=1..29 | **PASS, exact** |
| v13.692 | Centered 5-6-7 half-cell, `chi_12/chi_-4/chi_-3` character table at 1,5,7,11, quadratic-mean gate opening | independently rebuilt character table from raw definitions; independent algebra for Q^2 | **PASS, exact** |
| v13.693 | `6\|P_m \iff 2m+1\in U(12)`; mod-24 lift; 35-36-37 RMS cell | independent brute-force enumeration, m=0..59 | **PASS, exact** |
| v13.694 | Pronic mod-24 root set is literally equal to (not just isomorphic to) `U(24)`; group closure; CRT explanation | independent enumeration and closure check | **PASS, exact** |

## 7. Assessment

This is an unusually clean round: every checkable numeric and algebraic claim across all five entries — spanning classical Pythagorean-mean identities, a nontrivial `mod\tfrac12` fractional-part identity, a full quadratic-character table cross-check, and two modular-arithmetic set-equality theorems (`U(12)` and `U(24)` as pronic completions) — was independently re-derived or brute-force verified from scratch and matched exactly. No errors, sign issues, or overreach were found. The self-imposed scope guardrails (v13.690 §11 point 3-5, v13.691 §11, v13.692 §6, v13.693 §7, v13.694 §7) are consistently accurate about what has and has not been established, correctly declining to claim a Dirichlet-`L`-function derivation, a Pell-regulator connection, or a basis-free canonical intertwiner beyond what the finite carrier identification actually supports.

The thread directly answers the project owner's own framing (the HM-GM-AM-QM chain): `H_{\rm harm}=G^2/A` was already in place from the checkpoint, and this round's v13.692 §10 opens the quadratic mean `Q^2=A^2+D^2=2A^2-G^2` as the next exact gate, cleanly completing the four-mean cone dictionary at the algebraic level (`H_{\rm harm}\le G\le A\le Q` as an ordering claim is not yet separately verified in the ledger and remains open for a future entry, distinct from the exact identities checked here).

## 8. Final freshness check

`git fetch origin master` immediately before this commit: HEAD still at `cb2844d`. No new commits landed while writing this entry. `git ls-tree` confirms v13.695 remains free.
