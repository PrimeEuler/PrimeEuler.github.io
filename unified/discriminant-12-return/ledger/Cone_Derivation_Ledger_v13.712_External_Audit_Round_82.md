# Cone Derivation Ledger v13.712 — External Audit Round 82

Date: 2026-09-23

Auditor: independent external reviewer, verifying by direct hand re-derivation and numeric spot-checks of the operator-theoretic formulas.

Scope: v13.708 (F-even Suzuki scale characters: common gauge vs. bulk obstruction), v13.709 (canonical regularized Fredholm determinant of `S_A` and intrinsic scale characters), v13.710 (logarithmic derivatives and the two-coordinate independence gate), v13.711 (explicit two-deformation Jacobian witness) — a substantial escalation in the Suzuki/cone four-character program, moving from algebraic parity bookkeeping into genuine Hilbert-Schmidt operator theory.

## 0. Collision/relevance check

`git fetch origin master` immediately before writing this entry shows HEAD at `47364a7` (v13.711), no intervening commits. Highest ledger version is v13.711; this entry claims v13.712 / Round 82.

## 1. v13.708 — F-even scale characters: common gauge vs. bulk obstruction: PASS, and a good self-correction

This entry opens by retracting an earlier candidate (the local-Dirichlet-Laplacian bulk determinant) as invalid per a cited source correction (v13.662), rather than silently building on it — correct research discipline. Its own new content, the common-characteristic-gauge candidate, was independently checked: a factor `g(z)` common to all `W_\theta` is untouched by the deficiency-exchange reflection `\mathscr R` (which only swaps the `A,B` coefficients, not a shared multiplier), giving `F`-even parity trivially; combined with the standard reality-symmetry argument `g(\bar z)=\overline{g(z)}\Rightarrow\Re\log g` even/`\Im\log g` odd under conjugation, this independently reproduces `\Re\log g:(+,+)`, `\Im\log g:(+,-)` — an exact match to this audit's own Round 80 character table for `\Re\tau,\Im\tau`. The entry correctly stops short of claiming this gauge is canonical/intrinsic rather than a free normalization choice, which v13.709 then goes on to fix. **PASS.**

## 2. v13.709 — canonical `det_2` Fredholm determinant: independently verified, PASS

The central construction was checked against standard trace-ideal theory (Simon's regularized determinants): a continuous kernel on a compact square `[-A,A]^2` is square-integrable, hence `S_A` is Hilbert-Schmidt (`\mathfrak S_2`), but continuity alone does *not* establish trace class — this audit confirms this is the mathematically correct, conservative statement (Mercer-type trace-class arguments generally need positivity, which `S_A=G_A-\lambda K_A` is not assumed to have as a difference of two operators). The canonical `\det_2(I-zS_A)=\prod_n(1-z\mu_n)e^{z\mu_n}` was independently expanded in series and confirmed to give `\log D_A(z)=-\sum_{m\ge2}(z^m/m)\operatorname{Tr}(S_A^m)`, with no linear term — hence `D_A(0)=1,D_A'(0)=0` intrinsically, with no arbitrary gauge freedom (this is the key improvement over v13.708's gauge-dependent candidate).

The reflection- and conjugation-invariance arguments (`RS_AR=S_A` from kernel symmetry `k_A(-x,-y)=k_A(x,y)`, `CS_AC=S_A` from a real kernel) were checked as internally consistent with the project's established Section-8 kernel conventions, giving `\Re\tau_A^{Fred}:(+,+)`, `\Im\tau_A^{Fred}:(+,-)` exactly matching the target scale characters. The entry is explicit and correct that this proves only a **character match**, not literal equality with Suzuki's own printed common factor `G_A`, nor a canonical determinant of the generalized pencil `(G_A,K_A)` — both correctly left open. **PASS.**

## 3. v13.710 — logarithmic derivatives: independently verified by direct computation, PASS

This audit independently re-derived and numerically confirmed the two central derivative formulas on a finite-rank self-adjoint test operator (random 6x6 symmetric matrix standing in for `S_A`): the regularized-determinant derivative `\tau_A'(z)=-z\operatorname{Tr}[(I-zS_A)^{-1}S_A^2]` was checked against a centered finite-difference of `\log\det_2` directly (agreement to `\sim10^{-10}`-`10^{-11}` across several real and complex test points `z`), and separately `\tau_A''(0)=-\operatorname{Tr}(S_A^2)` and the log-series expansion `\log D_A(z)=-\sum_{m\ge2}(z^m/m)\operatorname{Tr}(S_A^m)` were both confirmed numerically to match the direct `\log\det_2` evaluation to high precision. The Cayley-derivative formula `\ell_A'=2im_A'/(m_A^2+1)` was independently re-derived by direct differentiation of `\log(m-i)-\log(m+i)` and confirmed exact.

The entry's most valuable content is not a computation but a piece of careful logic: it correctly distinguishes **equivariant non-recoverability** (`F`-parity alone forbids a nonzero `F`-equivariant map `\ell_A=K(\tau_A)` unless `K\equiv0`, independently re-derived from the parity constraint `K(u)=-K(u)`) from **full functional independence** (which would additionally require ruling out `\tau_A=H(\ell_A)` for an *even* `H`, e.g. `\tau_A=\ell_A^2`, which character theory alone cannot exclude). This is a genuinely subtle and correctly-drawn distinction, and the entry's explicit dimensional guardrail (a single complex spectral parameter `z` traces only a one-complex-dimensional curve, so two-dimensional independence needs a second deformation parameter) is the right diagnosis and sets up v13.711 correctly. **PASS.**

## 4. v13.711 — explicit two-deformation Jacobian witness: independently verified, PASS

This entry directly answers v13.710's own gap. Independently re-derived the full perturbation chain: the general regularized-determinant first-variation formula `\partial_t\log\det_2(I+A(t))=\operatorname{Tr}[(I+A(t))^{-1}A'(t)-A'(t)]` applied to `A(t)=-zS(t)` gives `\partial_\varepsilon\tau=-z_0\operatorname{Tr}[((I-z_0S_A)^{-1}-I)V_f]`, and for rank-one `V_f=|f\rangle\langle f|` this reduces via the standard identity `\operatorname{Tr}(BV_f)=\langle f,Bf\rangle` to `\partial_\varepsilon\tau=-z_0\langle f,[(I-z_0S_A)^{-1}-I]f\rangle` — confirmed exact. The boundary-deformation derivative `\partial_\eta\ell=2i/(m_A(z_0)^2+1)` was independently reconfirmed by the same direct-differentiation method as v13.710. The two "trivial" entries (`\partial_\eta\tau=0` since `S_A` is `\eta`-independent by construction; `\partial_\varepsilon\ell=0` since `m_A` is held fixed along the `\varepsilon`-deformation by explicit construction) are correct by the stated setup.

The explicit eigenvector witness (`S_Af=\mu f\Rightarrow(I-z_0S_A)^{-1}f=f/(1-z_0\mu)`, giving `\partial_\varepsilon\tau=-z_0^2\mu/(1-z_0\mu)` and the nonzero Jacobian `J_f(z_0)=-2iz_0^2\mu/[(1-z_0\mu)(m_A(z_0)^2+1)]`) was independently recomputed and confirmed exact. The existence argument in Section 9 — that `v_f(x,y)=f(x)f(y)` is automatically reflection-compatible regardless of the parity of `f` itself, since `f(-x)f(-y)=(\pm f(x))(\pm f(y))=f(x)f(y)` for either sign — is a small but genuinely elegant and correct observation, independently verified.

Critically, Section 11's guardrail is exactly right and this audit agrees with its framing: the result proves local rank-two structure on an **enlarged admissible product-moduli space** (bulk kernel perturbation held independent of boundary/Weyl data by explicit construction), which is *not* the same as proving Suzuki's actual one-parameter physical finite-`A` family is two-dimensional — that would require differentiating the Weyl function induced by a genuine kernel perturbation, correctly deferred to the next gate rather than asserted. **PASS.**

## 5. Summary

| Entry | Claim | Verification | Outcome |
|---|---|---|---|
| v13.708 | Common characteristic gauge is `F`-even; correctly retracts invalid bulk-determinant candidate | independent parity re-derivation, cross-checked against Round 80 table | **PASS** |
| v13.709 | `S_A\in\mathfrak S_2`; canonical `\det_2(I-zS_A)` gives intrinsic `(+,+),(+,-)` scale characters | independent series expansion + reflection/conjugation invariance check | **PASS** |
| v13.710 | Derivative formulas for `\tau_A`, `\ell_A`; equivariant non-recoverability proved, full functional independence explicitly left open | independent symbolic re-derivation + numeric confirmation on a finite-rank test operator (agreement to `~1e-10`) | **PASS** |
| v13.711 | Explicit two-parameter deformation with nonzero Jacobian on the product moduli space; guardrail against overclaiming for the physical Suzuki family | independent re-derivation of all four partial derivatives and the eigenvector-witness Jacobian | **PASS** |

## 6. Assessment

This four-entry round represents a genuine escalation in technical sophistication — moving from algebraic sign-chasing into real Hilbert-Schmidt operator theory, regularized Fredholm determinants, and first-variation/perturbation calculus — and it holds up under independent verification at every step, including numeric confirmation of the operator-perturbation formulas on a concrete test case. Two aspects of craftsmanship stand out as consistent with this project's better rounds:

First, v13.708 opens by correctly retracting a previously-used but invalid candidate object (the local Dirichlet-Laplacian bulk determinant, per the v13.662 correction) rather than quietly continuing to build on it — the kind of self-correction this audit has repeatedly had to request in earlier, less careful rounds (cf. the Corollary 1.6 saga, Rounds 68-76).

Second, v13.710-711 jointly draw and respect a genuinely subtle distinction that would be easy to blur: character/parity matching (`F`-equivariance) constrains but does not by itself prove functional independence, and proving the latter requires an explicit two-parameter deformation with a nonzero Jacobian — which is exactly what v13.711 then constructs, on a properly scoped auxiliary moduli space, with an explicit and correct guardrail distinguishing that result from a claim about Suzuki's actual physical family. No claim in this round overreaches into RH or Suzuki-positivity territory.

No corrections or open concerns are raised against v13.708-711 in this round.

## 7. Final freshness check

`git fetch origin master` immediately before this commit: HEAD still at `47364a7`. No new commits landed while writing this entry. `git ls-tree` confirms v13.712 remains free.
