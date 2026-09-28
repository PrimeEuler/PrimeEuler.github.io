# Cone Derivation Ledger v13.843 — External Audit Round 116

Date: 2026-09-28

Auditor: External audit thread (Claude, independent instance).

Scope: v13.842 — the pre-registered Horn A/Horn B falsification test, run against my own Round 115 chat recommendation (Horn A, on a specific boundary-layer mechanism) and reported as a falsification of that mechanism.

Verdict: **PASS on every independently checkable claim, including two I could verify entirely by hand (not just by re-reading a script's printed output). The core numerical falsification (the actual computed ratios and endpoint values from the pivoted (8.5)-least-squares method) remains sandbox-side and unverified by direct execution, same limitation as Rounds 114–115.**

## 0. Disclosure: this entry tests my own prior claim

In chat, prior to this round, I recommended Horn A on a specific mechanistic story: `H^1_0`'s forced `v(±A)=0` fighting an exponentially large source `e^{±x}` manufactures a spurious `O(e^A)`-scale artifact in the ratios. The project owner and the sandbox thread turned that into a pre-registered falsification test. §0 of v13.842 quotes the decision rule verbatim, and the outcome — same growth, same constant, under natural (unconstrained) boundary conditions — falsifies it. I'm auditing this like any other entry, including the parts that go against what I said, and updating accordingly at the end.

## 1. Hand-verified: the load-bearing "constants are exactly annihilated" claim

§2.1 of v13.842 asserts that at `λ=0` in the natural (non-Dirichlet) trial space, constants satisfy `a(c,·)=0` exactly (making the weak-form linear system have an exact kernel there) while `⟨e^{±x},1⟩=±2\sinh(A)≠0` (so the right-hand side has nonzero component along that exact kernel), making the discrete system **inconsistent**, not merely ill-conditioned. I checked this without touching any script:

- `a(u,v)=∬g(x-y)u'(y)v'(x)\,dy\,dx`. For `u=1` (constant), `u'≡0`, so `a(1,v)=0` for every `v` — trivially, by inspection of the formula, no numerics required. This exactly matches the reported `‖S\mathbf1‖/‖S‖=2.5×10^{-16}` floating-point check (which is really just confirming correct matrix assembly of an identity that's already exact in the continuum).
- `∫_{-A}^{A}e^{x}dx = e^A-e^{-A}=2\sinh(A)`, confirmed numerically for `A=2,3,4,5` (`7.254, 20.036, 54.580, 148.406`) — nonzero for every `A>0`, matching the entry's claim exactly.

Combined, this is textbook Fredholm alternative: a symmetric singular operator's equation `Su=f` has no solution when `f` has nonzero overlap with `\ker S`. This is the correct, rigorous reason the "just enlarge the trial space to include constants" version of the weak-form route is dead at `λ=0` — not a numerical instability to be tuned away, a genuine non-existence result for that formulation. Good catch, and reported as exactly what it is (an honest negative) rather than smoothed over.

## 2. Hand-verified: the Neumann Green's-function kernel and its second derivative

§1 cites `N(x,y)=\frac{x^2+y^2}{4a}-\frac{|x-y|}{2}+\frac{a}{6}` from Suzuki §8.2 and claims `∂_x^2N=\frac{1}{2a}-\delta(x-y)`. I pulled page 28 of the PDF directly: "Its inverse `(-\Delta_N)^{-1}:L_0^2(-a,a)\to L^2(-a,a)` is a compact, self-adjoint, and positive integral operator with kernel `N(x,y)=\frac{x^2+y^2}{4a}-\frac{|x-y|}{2}+\frac{a}{6}`" — reproduces verbatim. I then differentiated it myself rather than trusting the entry's finite-difference check: `∂_xN=\frac{x}{2a}-\frac12\mathrm{sgn}(x-y)`, and `∂_x^2N=\frac{1}{2a}-\delta(x-y)` (since `\frac{d}{dx}\mathrm{sgn}(x-y)=2\delta(x-y)`). Matches the entry's claim exactly — their reported `10^{-4}}`-level finite-difference check was confirming something that's exactly true analytically.

## 3. PDF citation check: the `\mathfrak D(A_a)` domain claim

§1's quote — "the domain `\mathfrak D(A_a)` is strictly larger than `\mathfrak D(B_a)=H_0^1(-a,a)` and contains functions such as constants" — I pulled page 4 directly: reproduces **verbatim**, including the specific wording "contains functions such as constants." This is the same fact I originally verified myself in Round 101 and re-confirmed in Round 115; seeing it re-cited correctly a third time across two different audit rounds and two different sandbox entries is a good sign of citation discipline in this track.

## 4. Assessment of the falsification design and the honest-negative reporting

The test itself is well-designed: pre-registered before the result was known, with the decision rule stated in advance and quoted verbatim rather than paraphrased after the fact (which would invite motivated reasoning). The method actually used (regularized least-squares directly on Suzuki's own (8.5), after the originally-planned enlarged-trial-space weak form was found genuinely inconsistent per §1 above) is not a quiet substitution — it's disclosed as a pivot, with the reason for the pivot given and mathematically justified, and it happens to be the exact numerical method Suzuki's own paper recommends ("One may compute `v_\pm(a,x)` by solving this Fredholm equation numerically," p.30 — the same passage I confirmed verbatim in Round 114). Two structurally different discretizations (v13.840's `H^1_0` Galerkin weak form, and this entry's (8.5)-least-squares on the full trial space) agreeing to 1–2% at every tested `A` is meaningful cross-validation precisely because they're different numerical methods, not two runs of the same code.

The mechanism check in §3 (the `v(±A)` endpoint-value table) directly tests my proposed mechanism rather than just reporting the aggregate ratio outcome: it shows the *natural*, unconstrained solution is itself genuinely `O(e^A)` at the right endpoint (`v(+A)\sim0.65\,e^A`, and I confirmed `2\sinh(A)\approx e^A` for the tested range) — meaning the large boundary value isn't a Dirichlet-constraint artifact at all, it's what the equation wants to do given an `e^{\pm x}`-scale source. That's a direct, targeted refutation of the specific mechanism I proposed, not just an aggregate correlation.

## 5. What I still could not verify

The actual falsifying numbers — the `r_1^+,r_0^+` values in the natural-vs-Dirichlet table, the endpoint values, the gate-convergence rates for the pivoted (8.5)-LS method — come from scripts outside this repo, same limitation as Rounds 114–115. I have not re-executed them and I'm not certifying them the way I certify a re-run Bucket 3 script. What I can say is that every piece of this entry I *could* check independently — two hand-derivable mathematical facts and two PDF citations — checks out exactly, and the falsification's logical structure (pre-registered rule, disclosed method pivot with a correct justification, a mechanism-level check rather than just an outcome-level one) is sound.

## 6. Updating my own position

I called Horn A in Round 115's chat exchange, with a specific stated mechanism. That mechanism is directly checked here (§3's endpoint-value table) and doesn't survive the check: the unconstrained solution is large at the boundary anyway, so forcing it to be small can't be what's producing the `Θ(e^A)` ratio growth. I said in Round 115 that a natural-BC rerun reproducing the same growth and constant would flip me toward Horn B, and that's what happened, cross-validated by an independent method rather than a single rerun. I'm updating: Horn B — the edge criteria as stated in v13.743 onward are misformulated for a solution whose natural scale is `Θ(e^A)` — is now the better-supported reading, pending the actual analytic question the entry poses (what the criteria *should* say, given that scale is intrinsic).

## Self-audit note

No error of my own found in this entry. My own prior prediction (Round 115 chat) did not hold up against this round's evidence, recorded above.

## Result

\[
\boxed{\textbf{PASS: v13.842 confirmed on every independently checkable claim.} \textbf{Two mathematical facts verified entirely by hand (exact annihilation of constants by the weak form; the exact second-derivative structure of Suzuki's Neumann Green's function }N\textbf{), and two PDF citations (the }\mathfrak D(A_a)\textbf{ domain fact, re-confirmed a third time; the }N(x,y)\textbf{ kernel formula) both reproduce verbatim. The falsification test was pre-registered, honestly executed including a disclosed method pivot for a genuine mathematical reason, and cross-validated by an independent numerical method. The core falsifying numbers remain sandbox-side and unverified by direct execution. My own Round 115 Horn A prediction does not survive this round's mechanism-level check and is retracted in favor of Horn B.}}
\]
