# Cone Derivation Ledger v13.749 — External Audit Round 89

Date: 2026-09-24

Auditor: independent external LLM session (Claude Sonnet 5), auditing via shared git ledger only.

Scope: v13.742–748, the seven entries pushed since Round 88 (v13.741, commit `11d6648`). This includes the source thread's correction of the Round 88 finding, several follow-on gates, and a substantial new "multiple helix" lane the user specifically asked to be checked.

## 0. Coordination note

No collision this round. `git fetch` immediately before this write confirms `origin/master` unchanged at `bb507c3` since v13.748 landed. This entry is pushed as v13.749.

## 1. v13.742–743 — Round 88 correction, verified

v13.742 retracts the invalid `S_A u_± = D̄e_{±i}` identity exactly as required and rebuilds the finite deficiency pair from Suzuki's actual equation (8.5), keeping the affine boundary terms `A_{A,±}x+B_{A,±}` as genuine unknowns rather than discarding them. This is the correct fix — it does not merely patch the symptom but re-derives the finite pairing, Weyl relation, and convergence criteria from the source-faithful construction, and correctly notes that the pure compensated edge source is now conditional on a new open estimate (whether `α_A, β_A → 0`).

v13.743 derives the reflection relations `A_{A,-}=-A_{A,+}`, `B_{A,-}=B_{A,+}`, `C_{A,-}=C_{A,+}`. I independently re-derived the needed kernel parities from Suzuki's explicit formula `k(x,y)=g(x-y)-λN(x,y)` with `N(x,y)=(x²+y²)/(4a)-|x-y|/2+a/6` (PDF p.29): direct computation gives `k(0,-y)=k(0,y)` (even) and `k_x(0,-y)=-k_x(0,y)` (odd), using `g` even. From these I re-derived the reflection identities for `A_{A,±}`, `B_{A,±}` by substitution and confirmed they match exactly. The resulting edge-scaling analysis (§4–§10, defining `α_A, β_A` and the affine contamination `b_A(ξ)=β_A-α_Aξ`) is correct algebra throughout, and appropriately leaves `α_A,β_A→0` as open rather than assuming it.

No errors in either entry.

## 2. v13.744 — self-correction, verified

Retracts an earlier overstrong claim that the full centered Weil multiplier equals `2Re L(1/2+0⁺+it)` as an ordinary real-axis object encoding all zeros. The retraction's own argument — `Re L(1/2+it)=0` away from critical-line poles — I re-derived independently from two already-established facts: the functional equation `L(s)=-L(1-s)` and the reflection property `L(s̄)=conj(L(s))` (since `ξ` has real Taylor coefficients). Combining these at `s=1/2+it` forces `L(1/2+it)=-conj(L(1/2+it))`, i.e. purely imaginary, i.e. `Re L=0`. This is a standard, correct fact and the retraction is well-founded: a real-axis delta decomposition of `L` can only ever see critical-line zeros directly, so identifying it with the full (possibly off-line) zero side would silently assume what is not proved. Good self-correction, no errors.

## 3. v13.745 — closed scalar moment system, verified

Derives a full linear-algebraic reduction of the corrected (8.5)-based deficiency equation to three scalars `(C_A, I_{0,A}, I_{1,A})`. I independently re-derived the entire chain by hand: the equation in canonical form (1), the response-function decomposition (2), the two moment equations (3)–(4) obtained by applying the boundary functionals, the Cramer's-rule solution (5)–(6), the resulting `α_A,β_A` closed forms (7)–(8), and — most substantively — the parity simplification `M_{0x}=M_{10}=0` in §8, which I re-derived from first principles (odd integrand over a symmetric interval vanishes, using the same kernel parities confirmed in §1 above applied to `u_{1,A}` even / `u_{x,A}` odd, themselves following because `L_A` commutes with reflection). Every step checks out exactly. No errors.

## 4. v13.746 — archimedean/origin match, verified

Computes the Fourier transform of Suzuki's local Pf/contact/remainder package and shows it equals the centered Tate gamma multiplier `Reψ(1/4+it/2)-logπ`. I independently re-derived `𝓕[Pf(1/|r|)](t) = -2γ-2log|t|` from the stated finite-part definition, using the small-argument asymptotic `Ci(x)~γ+ln x`. Combined with `2A+1=log(2π)+γ`, the Euler–Mascheroni constant cancels exactly between the Pf term and the contact delta, and adding the (already source-checked) archimedean remainder transform reproduces `Reψ(1/4+it/2)-logπ` exactly, matching the independently-verified identity `L_∞'/L_∞(1/2+it)+L_∞'/L_∞(1/2-it) = -logπ+Reψ(1/4+it/2)` (itself re-confirmed via the reflection property of `ψ`). No errors.

## 5. v13.747 — sign fix, verified

Fixes the sign relating Suzuki's screw quadratic form to the Weil form: `Q_Suz[DF]=Q_Weil[F]`, no global minus sign. I independently redid the double integration by parts from scratch (`∬g(x-y)F'(x)F̄'(y)dxdy → -∬g'(x-y)F(x)F̄'(y)dxdy → ∬[-g''(x-y)]F(x)F̄(y)dxdy`, tracking each sign through two integrations by parts) and got the identical clean result. Cross-checked independently via Parseval (`|F̂'(t)|²=t²|F̂(t)|²`, combined with the established `Ŵ(t)=t²ĝ(t)`) and via the `D_Suz=id/dx` phase-cancellation argument — both agree with the direct computation. No errors.

## 6. v13.748 — new lane: multiple-helix seed to two-channel Dedekind theta current

This is the entry the user specifically flagged. It is large, so this audit checked it in full rather than sampling.

**Provenance handling:** commendable. The entry explicitly states the original multiple-helix prompt/parametrization is not recoverable from the current repository and does not fabricate one — it records only the structural motifs (scale/boost coexistence, projection merging strands, discrete returns) as inherited themes and clearly labels everything else as the recoverable mathematical development. This is exactly the right epistemic posture for a provenance checkpoint.

**Mathematical content, independently re-derived:**

- The AM–GM cone identity `X²+Y²=T²` for `X=(x-y)/2, Y=√(xy), T=(x+y)/2`, plus the harmonic/RMS companion identities — confirmed by direct algebra.
- The rapidity parametrization `x=e^{r/2+u}, y=e^{r/2-u}`, `(T,X,Y)=e^{r/2}(\cosh u,\sinh u,1)` — confirmed.
- The discriminant-12 matrix `g_12=[[3,1],[2,1]]`: characteristic polynomial `t²-4t+1` (confirmed by direct `det(g_12-tI)` computation), expanding unit `ε=2+√3`, and `N(ε)=(2+√3)(2-√3)=1` (confirmed).
- `U(12)≅V_4`: confirmed each nontrivial element (5, 7, 11) squares to 1 mod 12.
- The boost spectral decomposition `V_τ ≅ 1⊕χ_12`: I directly verified `σ_qφ_τ^+=φ_τ^+` and `σ_qφ_τ^-=χ_12(q)φ_τ^-` by substituting `u↦χ_12(q)u` into `cos(τu)` (even, invariant) and `i\sin(τu)` (odd, picks up the sign) — confirmed exactly.
- The prime-ideal measure decomposition `μ_K=μ_1+μ_{χ_12}` reproducing `ζ_K(s)=ζ(s)L(s,χ_12)`: I checked all three cases by hand — split (`χ_12(p)=1`: two atoms at `log p`), inert (`χ_12(p)=-1`: the odd-`k` terms cancel, surviving even terms reduce to one atom at `2log p` with weight `2log p`, matching the norm of the inert prime ideal), and ramified (`p=2,3`: local `L`-factor is the convention-`1` (not `χ_12(p)=1`, which would be wrong since 2,3 don't lie in `(Z/12Z)^×` — the ledger's phrasing here is correct but easy to misread), leaving only the trivial channel's single atom at `log p`, matching known ramification of `Q(√3)`). All three cases check out against standard algebraic number theory.
- The archimedean recombination `ξ_K(s)=ξ(s)·Λ_χ(s)` with `Λ_χ(s)=12^{s/2}Γ_R(s)L(s,χ_12)`: confirmed by direct multiplication, matching `ξ_K(s)=½s(s-1)·12^{s/2}π^{-s}Γ(s/2)²ζ_K(s)`.
- The explicit logarithmic-derivative formula for the centered `Ξ_K`: I re-derived `d/ds\logξ_K(s)` term by term from the definition of `ξ_K` (the `1/s+1/(s-1)` pole terms, the `½log12-logπ` constant, the `ψ(s/2)` digamma term, and `ζ_K'/ζ_K`), substituted `s=1/2+w`, and reproduced the boxed formula `ℒ_K(w)=2w/(w²-1/4)+½log12-logπ+ψ(1/4+w/2)+ζ_K'/ζ_K(1/2+w)` exactly, including confirming `1/s+1/(s-1)|_{s=1/2+w}=2w/(w²-1/4)` by direct algebra.
- The `χ_12` theta-kernel Mellin transform `∫ϑ_χ(x)x^{s/2}dx/x=2(12/π)^{s/2}Γ(s/2)L(s,χ_12)`: re-derived from scratch via the standard Gamma-integral computation for each `n`, using `χ_12(-1)=1` (even) to fold the `n<0` sum onto `n>0`. Confirmed exactly.
- The theta functional equation `ϑ_χ(x)=x^{-1/2}ϑ_χ(1/x)` is standard for a real primitive even character (root number `+1`) — accepted as standard theory, consistent with everything built on it.
- The fold-at-1 construction of `K_χ(r)=e^{|r|/2}ϑ_χ(e^{2|r|})` and `Λ_χ(1/2+w)=∫_ℝ K_χ(r)e^{wr}dr`: I re-derived this completely from scratch (splitting the Mellin integral at `x=1`, applying the functional equation to fold the `(0,1)` piece onto `(1,∞)`, substituting `x=e^{2r}`) and reproduced the boxed result exactly, mirroring the same method used earlier in the project (v13.722) for the ordinary `Ξ` case.
- The convolution identity `Φ_K=Φ*K_χ`: re-derived via the product-of-transforms argument (a product of two bilateral Laplace-type transforms is the transform of the convolution), and `Φ_K(-r)=Φ_K(r)` re-derived from the evenness of both factors.

**Positivity status:** the entry correctly does NOT claim `Φ_K>0` or `K_χ>0` — it explicitly flags this as open, notes numerical sampling is merely suggestive, and states a guardrail against promoting it. This is the right call; a signed character series is not automatically positive and the entry does not pretend otherwise.

I found no errors anywhere in v13.748. This is a substantial, carefully-hedged piece of work connecting the project's real-quadratic-field/Pell structure to a rigorous two-channel Dedekind zeta and theta-kernel construction for `Q(√3)`.

## 7. Result

\[
\boxed{\textbf{PASS: v13.742--743 correctly and completely fix the Round 88 finding.}}
\]
\[
\boxed{\textbf{PASS: v13.744--747, independently re-derived, no errors.}}
\]
\[
\boxed{\textbf{PASS: v13.748 (multiple-helix/Dedekind lane), independently re-derived in full, no errors. Provenance handling of the unrecoverable original helix prompt is honest and appropriately caveated.}}
\]

No errors were found in this auditor's own work this round.

## 8. Next gates to watch

1. The affine-contamination estimate `α_A,β_A→0` from v13.742–745 remains open and is the decisive question for the corrected finite-edge convergence program.
2. `ϑ_{χ_12}(x)>0` for `x>0` (v13.748 §14) — the sole gap standing between the exact convolution kernel `Φ_K=Φ*K_χ` and a proved-positive Dedekind analogue of `Φ`.
3. The local ramified-geometry cross-check in v13.748 §9 cites "independent ramified analysis" results from earlier project papers not re-verified in this round; flagged for a future pass if those papers are re-examined.
