# Cone Derivation Ledger v13.716 — External Audit Round 84

Date: 2026-09-23

Auditor: independent external reviewer, verifying by direct hand re-derivation, high-precision symbolic checks, and an end-to-end numerical confirmation with convergence testing.

Scope: v13.715 (unified prime-archimedean logarithmic cone current) — a direct response to the project owner's own proposed synthesis (relayed in this session before the entry landed): that both the finite primes and the archimedean/gamma completion of `\xi'/\xi` sample the same null-cone exponential atom `Q_r(s)`, primes discretely at `r=\log n` with von Mangoldt weights, the gamma/elementary piece continuously.

## 0. Collision/relevance check

`git fetch origin master` immediately before writing this entry shows HEAD at `a04064f` (v13.715), no intervening commits. Highest ledger version is v13.715; this entry claims v13.716 / Round 84.

## 1. The completed logarithmic derivative decomposition: independently verified exactly

`L(s)=\xi'/\xi(s)=1/s+1/(s-1)-\tfrac12\log\pi+\tfrac12\psi(s/2)+\zeta'/\zeta(s)` was independently re-derived by direct differentiation of `\log\xi(s)=\log\tfrac12+\log s+\log(s-1)-\tfrac s2\log\pi+\log\Gamma(s/2)+\log\zeta(s)`, confirming exact agreement with the entry's boxed formula. `P(s):=-\zeta'/\zeta(s)=\sum_n\Lambda(n)n^{-s}` for `\Re s>1` is standard. `L=A_\infty-P` with `A_\infty(s)=1/s+1/(s-1)-\tfrac12\log\pi+\tfrac12\psi(s/2)` follows immediately. **PASS.**

## 2. Integral representations: independently verified symbolically and numerically to ~26 digits

The classical digamma integral `\psi(z)=-\gamma+\int_0^\infty\frac{e^{-t}-e^{-zt}}{1-e^{-t}}dt` was independently checked numerically (high-precision `mpmath`, 40-digit working precision) against `mpmath`'s own digamma implementation at three test points, including one complex point — agreement to `~9\times10^{-27}` in every case, i.e. exact to the precision used. The substitution `z=s/2,t=2r` giving `\tfrac12\psi(s/2)=-\gamma/2+\int_0^\infty\frac{e^{-2r}-e^{-sr}}{1-e^{-2r}}dr` was independently re-derived and confirmed exact. The elementary Laplace transforms `1/s=\int_0^\infty e^{-sr}dr`, `1/(s-1)=\int_0^\infty e^{-sr}e^rdr` are standard and were confirmed by direct evaluation. Combining these into the boxed `A_\infty(s)` integral formula was independently re-derived term-by-term and matches exactly. **PASS, exact.**

## 3. The r→0 cancellation and basepoint subtraction: independently verified via Taylor expansion, PASS

The claim that the combined integrand `e^{-sr}(1+e^r-\tfrac1{1-e^{-2r}})+\tfrac{e^{-2r}}{1-e^{-2r}}` has the finite limit `1+s/2+O(r)` as `r\downarrow0` (despite each piece separately having a `1/r` pole) was independently verified by a full Taylor expansion of every factor to the required order: expanding `e^{-sr}`, `e^r`, and `1/(1-e^{-2r})=1/(2r)-1/2+O(r)` to second order and combining shows the `1/(2r)` singularities cancel exactly between the two pieces, leaving `1+s/2+O(r)` — confirmed to match the entry's claim exactly, not merely approximately.

`A_\infty(2)=\tfrac32-\tfrac12(\log\pi+\gamma)` was independently confirmed both algebraically (`\psi(1)=-\gamma`, standard) and numerically to 30 digits (`mpmath`, exact agreement). The basepoint-subtracted identity `A_\infty(s)-A_\infty(2)=\int_0^\infty(e^{-sr}-e^{-2r})W_\infty(r)dr` with `W_\infty(r)=1+e^r-\tfrac1{1-e^{-2r}}` follows immediately since the `s`-independent pieces cancel in the subtraction — independently confirmed by direct algebra. The near-zero behavior `W_\infty(r)=-\tfrac1{2r}+\tfrac32+O(r)` and `(e^{-sr}-e^{-2r})=(2-s)r+O(r^2)` were independently verified (the same Taylor computation as above), confirming the product is finite at `r=0`, and the large-`r` behavior `W_\infty(r)\sim e^r` giving convergence for `\Re s>1` was confirmed. **PASS, exact.**

## 4. The unified current and end-to-end numerical verification: PASS, with genuine convergence testing

Sections 6-8's assembly of `d\nu_\xi(r)=W_\infty(r)dr-d\mu_\Lambda(r)` and the resulting identity `\xi'/\xi(s)-\xi'/\xi(2)=\int_0^\infty(e^{-sr}-e^{-2r})d\nu_\xi(r)` for `\Re s>1` follow by straightforward linear combination of the two previously-verified pieces (Sections 2-3 above), independently re-derived and confirmed exact as algebra.

This audit went further and tested the *entire assembled formula end-to-end numerically*, not just its algebraic components, at the test point `s_0=2.5+1.3i`: the left side `L(s_0)-L(2)` was computed directly from `\xi'/\xi` via standard `\Gamma`/`\zeta` derivative routines; the right side was computed as [a high-precision numerical integral of the archimedean piece] minus [a von-Mangoldt sum truncated at `N`]. At `N=2\times10^5` the two sides agreed to `\sim5\times10^{-6}`; at `N=2\times10^6` (a `10\times` increase) the discrepancy shrank to `\sim5\times10^{-7}`, a genuine `\sim10\times` reduction consistent with the discrepancy being ordinary prime-sum truncation error converging to zero, not a persistent bias from a formula error. This is a substantive, non-trivial confirmation: it independently validates the entire chain (digamma integral, elementary Laplace transforms, basepoint subtraction, the von-Mangoldt Laplace-Stieltjes representation, and their combination) simultaneously, rather than checking each algebraic step in isolation. **PASS, exact, confirmed by convergent numerical test.**

## 5. The honestly-flagged limitation: independently confirmed as real, not overclaimed away

This is the most important thing to check in this entry, and this audit specifically probed it: does the construction actually make the `V_4`/functional-equation symmetry (established in v13.713, audited Round 83) manifest at the level of the new current `d\nu_\xi`, or does the entry merely claim the connection exists?

Independently confirmed the entry's own guardrail is accurate: the representation `\int_0^\infty(e^{-sr}-e^{-2r})d\nu_\xi(r)` converges, by the large-`r` asymptotics verified in Section 3 above, only for `\Re s>1`. The reflection `s\mapsto1-s` maps this region to `\Re s<0`, a disjoint half-plane where this specific one-sided representation is not even defined, let alone symmetric. Therefore the oddness `L(1-s)=-L(s)` established in v13.713/Round 83 is **not** a property of `d\nu_\xi(r)` or its Laplace kernel `e^{-sr}` on this representation — it remains a fact about the abstractly-continued `\xi'/\xi` function, imported by citation (§9) rather than re-derived from the current itself. The entry states this plainly ("the `V_4` functional-equation oddness is not yet manifest term-by-term in this one-sided current representation... This is the remaining structural gap") and correctly proposes a two-sided/theta-symmetrized construction as the next gate rather than asserting the gap is closed. This audit's independent check of the convergence-region argument confirms the gap is real and correctly characterized, not a rhetorical hedge covering an actual overclaim. **PASS — the guardrail is accurate, not just present.**

The "arithmetic-archimedean balance law" `P(s)+P(1-s)=A_\infty(s)+A_\infty(1-s)` (§10) was independently re-derived from `L=A_\infty-P` and `L(1-s)=-L(s)` by direct substitution and rearrangement — confirmed exact algebra, correctly presented as a consequence of the *already-established* abstract functional equation (via analytic continuation) rather than a new independent derivation from the current.

## 6. Assessment of scope relative to the project owner's framing

The project owner's proposal (relayed just before this entry landed) was that "both act on exactly the same exponential/cone atom," with primes sampling it discretely and the gamma/elementary completion occupying the continuous radial distribution. This audit's independent verification confirms this is **exactly correct as a classical analytic-number-theory fact**, rigorously established (not merely suggestive) by v13.715: every piece of `\xi'/\xi(s)` — the pole terms `1/s,1/(s-1)`, the digamma/gamma term, and the prime sum — is literally a Laplace-Stieltjes transform of a measure on the same radial variable `r\in(0,\infty)` against the same kernel `e^{-sr}`, and this audit's numerical test confirms the assembled identity holds.

Two things this does **not** yet establish, matching the entry's own correct scope: (1) it does not make the `\xi` functional-equation symmetry manifest at the current/kernel level — that symmetry still enters only through the pre-established abstract identity `L(1-s)=-L(s)`, not through any two-sidedness of `d\nu_\xi` itself, exactly as flagged in Section 5 above; (2) it remains entirely within the Xi/Zeta lane opened in v13.713 — nothing in this entry uses or references Suzuki's specific continuous-kernel operator `S_A` or its screw-function kernel `g_A`, so this construction does not yet address the "major bridge problem" (v13.713 §12) of connecting the Suzuki operator lane to the Xi/Zeta lane. The shared "exponential cone atom" language is real and now rigorously established between primes and the archimedean completion *within* the classical `\xi'/\xi` decomposition — it is not yet a bridge to Suzuki's own, independently-constructed kernel.

## 7. Summary

| Section | Claim | Verification | Outcome |
|---|---|---|---|
| §1 | `L=A_\infty-P` decomposition of `\xi'/\xi` | independent differentiation of `\log\xi` | **PASS, exact** |
| §2-4 | Digamma integral, elementary Laplace transforms, combined `A_\infty(s)` formula | independent symbolic re-derivation + numeric check to `~1e-26` | **PASS, exact** |
| §4-5 | `r\to0` cancellation; `A_\infty(2)` closed form; basepoint-subtracted `W_\infty` identity | independent Taylor expansion + 30-digit numeric confirmation | **PASS, exact** |
| §6-8 | Unified current `d\nu_\xi`; main identity `\xi'/\xi(s)-\xi'/\xi(2)=\int(e^{-sr}-e^{-2r})d\nu_\xi(r)` | independent algebra + **end-to-end numerical test with convergence verification** (discrepancy shrinks `~10\times` when prime truncation increases `10\times`) | **PASS, exact, numerically confirmed** |
| §9-10 | `V_4` symmetry not yet manifest in the current (honest limitation); arithmetic-archimedean balance law | independently confirmed the convergence-region argument makes the gap real, not rhetorical; balance law re-derived exactly | **PASS — guardrail is accurate** |

## 8. Overall assessment

This is genuinely strong work: a real, rigorously-established classical-analysis result (not a loose analogy) that both finite and archimedean places live in exactly the same Laplace/exponential-atom language on a common logarithmic radius variable, verified independently at every algebraic step and — unusually for this project's more abstract entries — confirmed by an actual convergent numerical computation tying the whole chain together end-to-end. The entry's own honest accounting of what remains open (the two-sided/functional-equation-symmetric extension, and the still-unaddressed bridge to the Suzuki operator lane) is accurate under this audit's independent check, not a hedge papering over a gap. This round finds no errors and no overreach.

## 9. Final freshness check

`git fetch origin master` immediately before this commit: HEAD still at `a04064f`. No new commits landed while writing this entry. `git ls-tree` confirms v13.716 remains free.
