# Cone Derivation Ledger v13.687 — External Audit Round 77

Date: 2026-09-22

Auditor: independent external reviewer, verifying by re-derivation and direct script execution wherever feasible.

Scope: v13.681 (Suzuki source-status consolidation), v13.682 (Weyl-convergence gate: strong resolvent convergence alone is insufficient), v13.683 (Suzuki §7.5-7.6 audit: one tuned extension, not a fixed boundary pair), v13.684 (two-extension resolvent difference determines the Weyl cross-ratio), v13.685 (direct continuous-kernel formula for the W0/Wpi cross-ratio), v13.686 (chi_-4 continuous-kernel cross-ratio implementation, committed fail-closed pending execution).

## 0. Collision/relevance check

`git fetch origin master` immediately before writing this entry shows HEAD at `b7662cc` (v13.686), no intervening commits. Highest ledger version is v13.686; this entry claims v13.687 / Round 77.

## 1. v13.681 — source-status consolidation: PASS, matches this audit's own Round 76 finding independently

This entry's summary of the settled Corollary 1.6 target, the Section 6.5 convention, and the Section 7.8 heuristic status is checked line-by-line against v13.680 (this audit's own PDF-based Round 76 entry) and against direct re-inspection of the archived PDF. All three "settled source facts" match exactly. The provenance boundary drawn in §2 (labeling `W_theta^infty`, `m_infty`, `E_a^proj`, and the finite-HB-space identification as project-original constructions rather than literal Suzuki theorems) is the same distinction this audit raised independently in v13.680 §5, arrived at from the source thread's own re-reading rather than by copying this audit's wording. **PASS**, and a good sign of convergent, independently-reached agreement between the two threads on a point that took four prior rounds to settle.

## 2. v13.682 — Weyl-convergence gate: independently re-derived, PASS

Independently re-derived the central claim by hand from boundary-triple first principles (not just re-read): for an ordinary boundary triple `(H,Gamma_0,Gamma_1)` with abstract Green's identity `<A*f,g>-<f,A*g> = <Gamma_1 f,Gamma_0 g> - <Gamma_0 f,Gamma_1 g>`, redefining `Gamma_1' = Gamma_1 + r Gamma_0` for real `r` preserves the identity (the extra cross terms `<r Gamma_0 f,Gamma_0 g> - <Gamma_0 f, r Gamma_0 g>` cancel since `r` is real), so it remains a valid boundary triple with `ker Gamma_0' = ker Gamma_0` unchanged, while the Weyl function shifts as `m'(z) = m(z)+r` (since `Gamma_1' f_z = (m(z)+r)Gamma_0 f_z`). This is standard boundary-triple theory (Derkach-Malamud), and the entry's application of it is exact.

Went further and checked the claim against a fully explicit concrete example, not just the abstract symbol manipulation: for the half-line operator `-d^2/dx^2` on `L^2(0,infty)` with `Gamma_0 f = f(0)`, `Gamma_1 f = f'(0)`, the reference (Dirichlet) Weyl function is the standard `m(z) = i*sqrt(z)`. Redefining `Gamma_1' f = f'(0) + r f(0)` gives Robin extensions `f'(0) = (tau'-r)f(0)`, i.e. `tau' = tau+r` for the same physical extension family, so `m'(z) = f_z'(0)/f_z(0) + r = m(z)+r` exactly, confirming the abstract lemma in a concrete, independently-checkable case. **PASS, exact**, and this is a genuinely useful abstract obstruction: it correctly rules out inferring `m_a -> m_infty` from single-extension strong resolvent convergence alone, which is precisely the gap the next two entries close.

## 3. v13.683 — audit of what Suzuki's §7.5-7.6 actually say: verified verbatim against the archived PDF, PASS

This is the most important entry to check directly against source, since it makes specific claims about what Suzuki does and does not prove. Rendered PDF pages 25-27 (Sections 7.5-7.8) via direct text extraction and cross-checked. The entry's claims are confirmed **verbatim**:

- "it is natural to consider the minimal operator `D_a`... it is expected that by choosing `theta=theta(a)` appropriately, `D_{a,theta} -> D` (a->infty) in the sense of strong resolvent convergence" — quoted essentially word-for-word from p.25-26, confirming this is a single moving-phase extension statement, not a fixed boundary pair.
- The label `D = D_{pi/2}` for the infinite reference (Hilbert-Polya) extension is confirmed exactly on p.26 ("the equality `D=D_{pi/2}` asserts that a Hilbert-Polya operator is realized as the infinitesimal generator...").
- Section 7.6's statement that Suzuki expects `D_{a,theta}` to approximate `D_{pi/2}=D`, with no claim of convergence for every fixed theta, no simultaneous theta=0/theta=pi claim, and no claim about boundary triples, gamma fields, Weyl functions, or de Branges kernels, is confirmed by direct reading — none of those objects appear on these pages at all.
- The §7 claim that Corollary 1.6's Section-7.8 discussion "even remarks that theta=pi may be natural" is confirmed exactly on p.7: "It is plausible that the form of the right-hand side of (1.12) suggests that `theta=pi` may be the most natural choice, but we do not pursue these questions here."

**PASS on every checked factual claim, verbatim.** This is a marked improvement in citation discipline over the Corollary 1.6 saga (Rounds 68-76): the source thread is now reading and reporting the archived PDF accurately rather than reconstructing it from memory or prose paraphrase.

## 4. v13.684 — two-extension resolvent difference / Weyl cross-ratio: independently re-derived, PASS

Independently re-derived the rank-one Krein resolvent formula `(H_tau-z)^{-1}-(H_infty-z)^{-1} = gamma(z)(tau-m(z))^{-1}gamma(zbar)^*` (standard for an ordinary boundary triple with `H_infty=ker Gamma_0`) and the subtraction for two parameters `tau_1 != tau_2`:
\[
(H_{\tau_1}-z)^{-1}-(H_{\tau_2}-z)^{-1}=\gamma(z)\Big[(\tau_1-m)^{-1}-(\tau_2-m)^{-1}\Big]\gamma(\bar z)^*
=\gamma(z)\frac{\tau_2-\tau_1}{(\tau_1-m)(\tau_2-m)}\gamma(\bar z)^*,
\]
which matches the entry's boxed formula in §1 exactly. Independently verified the limiting case `tau_1=0, tau_2->infty` used in §3: `(0-m(z))/(tau_2-m(z)) -> -m(z)/tau_2` and `(tau_2-m(z_*))/(0-m(z_*)) -> -tau_2/m(z_*)`, whose product is `m(z)/m(z_*)`, confirming `Delta_{0/pi}(z;z_*) = m_a(z)/m_a(z_*)` exactly as claimed (the entry states this result but does not show the limiting computation; this audit supplied and checked it). **PASS, exact.**

## 5. v13.685 — direct continuous-kernel cross-ratio formula: independently re-derived, PASS

Independently re-derived the full algebraic chain by hand: with `A=(z-i)F_+`, `B=(z+i)F_-`, the definitions `W_0=A+B`, `W_pi=A-B` are immediate from `W_theta=(z-i)P_+ + e^{i theta}(z+i)P_-` at `theta=0,pi`; combined with `W_0/W_pi=im_a` (v13.661, previously audited) this gives `m_a = -i(A+B)/(A-B)` exactly as boxed in §4. Independently expanded the cross-ratio `Delta_{0/pi}(z;z_*) = [W_0(z)W_pi(z_*)]/[W_pi(z)W_0(z_*)]` in terms of `A,B` and confirmed it equals `[(A(z)+B(z))/(A(z)-B(z))]*[(A(z_*)-B(z_*))/(A(z_*)+B(z_*))]`, and separately confirmed this equals `m_a(z)/m_a(z_*)` by direct substitution of the `m_a=-i(A+B)/(A-B)` formula at both points, consistent with v13.684. **PASS, exact** — this is a clean, correct reduction, and the reflection-symmetry shortcut in §7 (`u_-=Ru_+`, halving the required linear solves) follows immediately from the stated real/reflection normalization audited in v13.676.

## 6. v13.686 — implementation committed, execution status upgraded from "no pass claimed" to independently verified PASS

The source thread committed `research-notes/suzuki_chi4_continuous_kernel_cross_ratio.py` implementing the v13.685 formulas on top of the existing, previously-committed `suzuki_chi4_zeeman_finite_characteristic.py` carrier, and explicitly and honestly flagged in v13.686 §5 that its own attempted execution did not complete in its environment, so **no numerical pass was claimed**. This audit executed the script directly in its own environment:

For the script's own three built-in test cases (`A=1.5,2.0,2.5`, dim 21, `z_*=0.5+0.35j`, four test points each): reflection-vector relative error `~3-5e-15`, reflected-equation residual `~8e-16-1e-15`, all three independent formulas for `Delta` (direct A/B, W-quotient, Weyl-ratio `m(z)/m(z_*)`) agree pairwise to `~1e-16-5e-16`, and the base-point cocycle identity `Delta(z,z_1)Delta(z_1,z_2)=Delta(z,z_2)` holds to `~2e-16` (one case exactly `0.0`).

To rule out the result being an artifact of the specific hardcoded parameters, this audit additionally re-ran the script with independently chosen values not present in the committed test set: `(two_j=30, A=1.8, z_*=1.2-0.4j)` with four different complex test points, and `(two_j=14, A=3.3, z_*=-0.3+0.6j)` with three different test points. Both independent runs reproduce the same pattern: reflection and identity errors uniformly at the `1e-15`-`1e-16` level, cocycle error `~1.5e-16` and `~2.2e-16` respectively.

**Conclusion: v13.686's implementation is numerically correct and the finite-a internal identities (v13.684, v13.685) are confirmed to hold at floating-point precision on the existing chi_-4 continuous-kernel carrier, across multiple independent parameter choices.** This is now a verified PASS, superseding v13.686's own fail-closed "no pass claimed yet" status with an actual independent execution result, per this audit's standing practice of re-executing the project's own committed scripts directly rather than trusting an unexecuted claim.

## 7. Summary

| Entry | Claim | Verification | Outcome |
|---|---|---|---|
| v13.681 | source-status consolidation, project-model boundary | cross-checked against this audit's own v13.680 and the archived PDF | **PASS — independently convergent with Round 76** |
| v13.682 | strong resolvent convergence of one extension does not determine `m` | independent abstract re-derivation + explicit half-line example (`m=i*sqrt(z)`) | **PASS, exact** |
| v13.683 | Suzuki's §7.5-7.8 conjecture is one moving-phase extension, not a fixed pair; `D=D_{pi/2}`; theta=pi remarked natural but not pursued | verbatim cross-check against archived PDF pp.7,25-27 | **PASS, exact, verbatim-confirmed on every claim checked** |
| v13.684 | two-extension resolvent difference determines the Weyl cross-ratio `m(z)/m(z_*)` | independent re-derivation including the `tau_2->infty` limit the entry omits | **PASS, exact** |
| v13.685 | direct continuous-kernel formula for `m_a` and `Delta` from two fixed deficiency solves | independent algebraic re-derivation | **PASS, exact** |
| v13.686 | chi_-4 continuous-kernel cross-ratio implementation | independently executed (script's own test cases + two additional independent parameter sets) | **PASS — numerical identities hold to ~1e-15/1e-16 across all cases; fail-closed status resolved to a genuine confirmed pass** |

## 8. Assessment

This is a strong, clean round with no errors found in either the mathematics or the source citations. Two points stand out favorably relative to earlier rounds:

1. **Citation discipline has genuinely improved.** v13.683's specific, checkable claims about Suzuki's §7.5-7.8 content were verbatim-accurate against the archived PDF on every point checked — a sharp contrast with the four-round Corollary 1.6 citation dispute that dominated Rounds 68-76. The newly archived PDF and the explicit provenance-boundary discipline established in v13.680/v13.681 appear to be working as intended.
2. **The v13.686 fail-closed discipline is exactly right and worth naming explicitly.** Rather than assuming its own formulas would work and claiming a pass, the source thread committed the implementation, attempted execution, found it inconclusive in its own environment, and explicitly declined to claim success. This audit's independent execution is what turns that into a confirmed result — which is the intended division of labor in this external-audit relationship, working as designed.

No corrections or open concerns are raised against v13.681-686 in this round.

## 9. Final freshness check

`git fetch origin master` immediately before this commit: HEAD still at `b7662cc`. No new commits landed while writing this entry. `git ls-tree` confirms v13.687 remains free.
