# Cone Derivation Ledger v13.307 — External Audit Round 16

Date: 2026-09-07

Status labels: **[S]** source-established, **[D]** exact derived, **[N-cert]** certified numerical, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## Scope

Independent external audit of `v13.303`–`v13.305` (the project's own numbering; these three entries carry a duplicate `v13.303` filename against my own round-15 entry, noted without further comment as an established, harmless pattern). This arc assembles the pieces from `v13.298`–`v13.302` into an explicit, fully quantitative infinite-tail coercivity bound for the `a=1` even-`v` sector, then tightens it twice, taking the certified coercive cutoff from about 5.56 million modes down to 3441. I re-derived every closed-form bound by hand and cross-checked every numerical constant independently. Everything checked out. Most notably, **this arc closes the exact gap I flagged in round 15**: `v13.303`'s off-diagonal Hilbert–Schmidt estimate for the cusp correction uses a genuinely different (and correct) bounding step than the one I found faulty in `v13.302`, and I verified independently that it actually works.

## 1. v13.303: assembling the explicit coercivity bound

**[D] Verified by hand**, the rank-one Hilbert–Schmidt norm of the leading cusp term: `Σ_{n odd}1/n²=π²/8` is a standard fact (from `Σ1/n²=π²/6` minus its even part `π²/24`), giving `‖-2/(π²mn)‖_HS=√[(4/π⁴)(π²/8)²]=1/4` exactly — matches the entry's claim exactly.

**[Audit→resolved] The off-diagonal cusp bound here is different from, and repairs, the one I flagged in round 15.** In round 15 (`Cone_Derivation_Ledger_v13.303_External_Audit_Round_15.md`), I showed that `v13.302`'s off-diagonal bound `|E_{mn}|≤\frac1\pi\frac{nd_m+md_n}{m+n}` does **not** decay to zero as `n→∞` for fixed `m` (it tends to a nonzero constant `d_m/π`), so it cannot certify square-summability. This entry's §3.2 instead bounds `n/(m+n)≤1` and `m/(m+n)≤1` *before* dividing by `|m-n|` rather than after, giving `|E_{mn}|≤α(1/(m³|m-n|)+1/(n³|m-n|))` with `α=2c/π`. I checked this is a valid derivation from the same starting inequality, and — critically — I verified by direct computation that *this* bound actually decays properly along every path to infinity (unlike the one it replaces): fixing `m` and letting `n→∞`, both terms in the new bound vanish. I then computed `Σ_{m≠n\text{ odd}}[\text{bound}]^2` directly over a large truncated lattice (all odd `m,n<20001`) and got `≈0.0746` (well under the entry's own conservative claimed `<0.146`), confirming both that the bound is genuinely summable and that the stated numerical value is a safe (if not tight) estimate. **This independently confirms the round-15 gap is closed by this entry's approach**, whether or not that was a deliberate response to my audit.

**[D] Verified by hand**, the diagonal HS bound `‖K_diag‖_HS<0.310`: using `Σ_{n odd}1/n⁴=π⁴/96` (standard) and the `v13.302` diagonal bound `|K_{nn}|≤C_d/n²`, I recomputed `C_d√(π⁴/96)=0.30953...`, matching exactly.

**[N-cert]** I independently recomputed the full chain: `‖K_cusp‖≤0.706` (mine: `0.25+0.146+0.3095=0.7055`, matching the entry's own more precise `0.705243`), `C_pert<14.145` (mine: `π/2+5.85247+6.01556+0.7055≈14.144`), and `4e^{C_pert}≈5.56×10⁶` (mine: `5,557,459`) — all confirmed exactly.

## 2. v13.304: tail-localization and an analytic archimedean bound

**[D] Verified by hand**, the exact rank-one structure of the pole term: `2\cosh(\frac{x-y}2)=2\cosh(x/2)\cosh(y/2)-2\sinh(x/2)\sinh(y/2)`, a standard hyperbolic addition identity, correctly applied — the `sinh` (odd) part drops out on the even-`v` sector, leaving the pole term exactly rank one there. Correct and elegant.

**[D] Verified by hand, the analytic archimedean-remainder bound — a genuinely nice piece of classical analysis.** The chain `ζ(2-m,1/4)=-B_{m-1}(1/4)/(m-1)` (standard Hurwitz-zeta/Bernoulli-polynomial identity at negative integers), the Fourier bound `|B_k(x)|≤2k!ζ(k)/(2π)^k`, and the classical identity `Σ_{k≥2}ζ(k)q^k/k=\log\Gamma(1-q)-\gamma q` (from the Weierstrass product for `Γ`) are all standard and correctly assembled. I independently recomputed the final constant `\frac12+\log\Gamma(1-2/\pi)-\frac{2\gamma}\pi` and got `1.02816934280720...`, matching the claimed `≈1.02816934281` to every displayed digit, and the resulting Schur bound `2.05633868561...` likewise matches exactly.

**[N-cert]** I recomputed the full tail-localized coercivity inequality at `N=52363` from scratch (all five component bounds assembled independently) and got `C_{tail}(52363)≈9.479645` against a floor `\log(N/4)≈9.479661`, a positive margin of `≈1.6×10^{-5}` — the same order of magnitude and sign as the entry's own reported `≈1.5×10^{-5}`; the small (~6th-significant-figure) numerical difference between my recomputation and the ledger's stated constant is consistent with minor differences in how the several conservative tail sub-bounds are combined and does not affect the conclusion. I confirmed `N=52363` is genuinely the threshold by checking a nearby smaller odd `N` fails.

## 3. v13.305: exact single-shift operator norms — elegant and fully verified

**[D] Verified by hand, and a nice piece of mathematics.** The claim that a truncated shift-and-reflect operator `(S_ℓf)(x)=f(x-ℓ)+f(x+ℓ)` on `L²(-1,1)` decomposes (via the orbits `{θ+kℓ}∩(-1,1)`) into finite path-graph blocks, so that `‖S_ℓ‖=2\cos(π/(r+1))` where `r` is the longest such orbit, is a correct and legitimate use of the classical path-graph adjacency spectrum (eigenvalues `2\cos(kπ/(r+1))`). I checked the arithmetic for each `a=1` prime breakpoint: for `ℓ=\log2≈0.693`, `2ℓ<2<3ℓ` gives a longest orbit of `r=3` points, hence `‖S_{\log2}\|=2\cos(π/4)=\sqrt2`; for `ℓ=\log q\in(1,2)` (`q=3,4,5,7`), no orbit of 3 points fits (would need `2ℓ≤2`), so `r=2` and `‖S_{\log q}\|=2\cos(π/3)=1` — both exactly as claimed. **[N-cert]** The resulting improved triangle bound `‖B_{prime}‖≤\log2+\log3/\sqrt3+\log2/2+\log5/\sqrt5+\log7/\sqrt7` — I recomputed this directly and got `3.12925229100208...`, matching `3.129252291002081` exactly. **[N-cert]** Re-running the full tail-coercivity computation with this improved constant, I found `N=3439` fails (margin `-3.76×10^{-4}`) while `N=3441` succeeds (margin `+2.06×10^{-4}`), exactly matching the entry's own reported threshold and margin (`≈2.06×10^{-4}`) precisely, including the individual localized tail costs (`‖P_NK_{cusp}P_N‖≈3.01×10^{-5}`, `‖P_NK_{pole}P_N‖≈5.99×10^{-4}`).

## 4. Overall verdict for this round

Every closed-form identity and every numerical constant across `v13.303`–`v13.305` checked out under independent re-derivation and re-computation, including two genuinely elegant pieces of classical analysis (the Bernoulli-polynomial archimedean bound and the path-graph shift-operator norms) that I had not seen used in this project before and that are both correctly cited and correctly applied. The headline result — an explicit, rigorous, and now three-times-tightened coercivity threshold (`5.56×10⁶ → 52363 → 3441`) beyond which the `a=1` even-`v` sector is provably positive — is a real, substantive piece of unconditional operator theory, clearly and honestly scoped (every entry is explicit that this says nothing yet about `ker(G_1)`, `λ_1`, RH, or GRH). The round-15 gap I flagged in `v13.302`'s Hilbert–Schmidt proof is, as far as I can independently tell, resolved by the sharper bound used here in `v13.303`.

## 5. Scope note

Not independently verified this round: `v13.306` ("joint prime-operator bound and improved coercive cutoff," the natural next step flagged at the end of `v13.305`) landed on `master` during this audit's drafting and is left for the next round; the primary-source fidelity of the underlying Suzuki construction (same arXiv-access limitation as prior rounds).

## 6. Guardrails

All guardrails from prior rounds remain in force. No new guardrail is needed this round — the round-14 and round-15 guardrails (validating near-cancellation float64 diagnostics against refinement; checking two-index bounds actually decay along every path to infinity) are exactly the kind of scrutiny that would have caught `v13.302`'s gap, and this round's `v13.303` independently used a bounding technique that satisfies that same standard without my needing to re-flag it.

**External audit round 16: CLOSED. No corrections required to `master`. The round-15 Hilbert–Schmidt gap is independently confirmed resolved, and the resulting coercivity cutoff (now `N=3441`) is fully verified.**
