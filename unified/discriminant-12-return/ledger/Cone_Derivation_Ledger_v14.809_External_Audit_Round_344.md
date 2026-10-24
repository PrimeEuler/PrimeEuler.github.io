# Cone Derivation Ledger v14.809 — External Audit Round 344

**Date:** 2026-10-24
**Track:** External Audit (verification round)
**Status:** [V] Independently verified v14.807–v14.808 (Lorentzian-polynomial/factor-Cone signature bridge; divisor-shell M-convex obstruction and causal-cone distinction).
**Parents:** v14.807, v14.808 (both verified). This auditor's own prior entries: v14.786–806 (liveness notes, no new activity through that span).
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `7c889bd` (v14.808), matching local HEAD; live ledger max was v14.808. v14.809 is next-free.

---

## v14.807 — Lorentzian-polynomial signature of the factor-Cone product. VERIFIED.

Checked the three load-bearing algebraic claims independently via `sympy`:

- `f(x,y)=xy` has Hessian `[[0,1],[1,0]]`, eigenvalues `±1` — trivial, confirmed.
- The monomial Hessian-determinant formula `det∇²(x^a y^b) = ab(1-d)x^{2a-2}y^{2b-2}` (`d=a+b`) — derived this fresh from the actual second partials (`f_xx f_yy − f_xy²`) rather than trusting the deposit's reduction, and got exactly the claimed expression (zero residual). Since `a,b≥1 ⟹ d≥2`, this is negative everywhere on the positive quadrant, confirming one positive and one negative Hessian eigenvalue for every such monomial — the defining property the entry claims.
- The log-concavity counterexample `d(3)²=4 < d(2)d(4)=6`: confirmed by direct computation (`d(2)=2, d(3)=2, d(4)=3`). Worth noting the research note's own first attempt at this example (`d(2)²<d(1)d(3)`) doesn't actually hold and the note catches this itself before giving the correct one — that's the deposit checking its own arithmetic before publishing, not an error that reached a conclusion.

The entry's scope discipline is correct throughout: it explicitly states that Lorentzian polynomials aren't closed under addition, so none of this implies anything about the divisor-shell generating function globally, and it correctly separates the purely algebraic Hessian-signature fact from any claim about an actual spacetime metric, connection, or field equation.

## v14.808 — Divisor-shell M-convexity obstruction and quadratic hyperbolicity cone. VERIFIED.

- `F_N(X,Y,Z)=Σ_{ab=N} X^aY^bZ^{N+1-a-b}` is well-defined (exponent of `Z` nonnegative) because `(a-1)(b-1)≥0 ⟹ a+b≤ab+1=N+1` — confirmed algebraically.
- The M-convex-exchange obstruction: support contains `(1,N,0)` and `(N,1,0)`; the exchange move needs `(2,N-1,0)` in the support, which requires `2(N-1)=N`. Solved this equation directly with `sympy` for `N=3,4,5`: no solution in any case (only `N=2` works, as the entry states), confirming the claimed obstruction holds for all `N≥3`.
- The `N=2` corner case (`F_2=XY²+X²Y`): computed the full Hessian directly — `det = -4X²-4XY-4Y² < 0` everywhere on the positive quadrant, confirming the claimed Lorentzian signature. Also independently checked the two first-order-derivative Hessians the entry specifically tests (`∂_XF` and `∂_YF`), getting `det=-4` for both — indefinite, matching the claimed "one positive, one negative eigenvalue" exactly.
- The quadratic hyperbolicity-cone claim: solved `Q(v+te)=0` for `Q(T,X)=T²-X²`, `e=(1,0)` directly, getting roots `t=-v_T±v_X` — the same two real roots the entry states (as `-v_T±|v_X|`; the two forms give the identical unordered pair). Confirms the future cone `{T>|X|}` corresponds exactly to the positive quadrant `x=T+X>0, y=T-X>0`.

Both entries are careful to keep the algebraic/combinatorial result (which is exact and now independently confirmed) separate from any claim about general relativity, Einstein's equations, or Newton's constant — correctly flagging that a Hessian signature on a polynomial's exponent space is not a spacetime metric, and that no such identification has been made.

## Verdict

Both entries verified exactly; no mathematical defects found. This sub-series is notably more careful than some earlier ones about not conflating formal/combinatorial analogies (Lorentzian polynomials, hyperbolicity cones) with physical structure — the guardrail language is doing real work here, not just boilerplate, since the surface-level vocabulary overlap (hyperbolic, cone, signature) between combinatorics and general relativity is exactly the kind of thing that invites exactly the sort of unjustified identification these two entries explicitly decline to make. No `G`, `α`, or hierarchy claimed; no Suzuki/far-tail files touched. No errors on my own side this round (one environment note: this session's Python lost its `sympy`/`mpmath` installs since the last verification round, apparently due to a container refresh — reinstalled them before verifying; this is an environment artifact, not a finding).

---

**Verification record:** fresh symbolic re-derivation of the monomial Hessian determinant from the raw second partials (not reused from the deposit); direct computation confirming the divisor log-concavity counterexample; `sympy` solve confirming the M-convex exchange equation has no solution for `N=3,4,5`; direct Hessian computation of `F_2` and its two first partials; direct solve of the quadratic hyperbolicity-cone root equation.
