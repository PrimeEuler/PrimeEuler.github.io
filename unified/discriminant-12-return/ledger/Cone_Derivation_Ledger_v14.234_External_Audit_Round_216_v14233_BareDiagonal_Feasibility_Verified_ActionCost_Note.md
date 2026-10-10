# Cone Derivation Ledger v14.234 — External Audit Round 216: v14.233's Bare-Diagonal Feasibility Independently Re-Derived; One Precise Note on an Action-Cost Convention Mismatch

**Date:** 2026-10-10
**Track:** External Audit
**Status:** [V] v14.233's central claim — that the oscillatory arch integral in the raw physical diagonal $d_n$ decays as $O(1/k^2)$ rather than the generic $O(1/k)$, via a double integration by parts in which the $(2-t)$ factor kills the $t=2$ boundary term on the first pass and $\sin(0)=0$ kills the $t=0$ term — is independently re-derived from scratch, term by term, and confirmed exact. This is the entry's one genuinely novel analytic claim and the reason the bare-diagonal evaluator is feasible at all; it checks out. [N] One precise, narrowly-scoped note: v14.233 §3's parenthetical recomputation of the diagonal error's "action cost" uses $|\delta d|\cdot\|y\|^2$ (quadratic in the trial norm), which bounds a different quantity (the energy form $\langle y,\delta D y\rangle$) than the linear operator-action bound $\|\delta D\,y\|\le|\delta d|\cdot\|y\|$ used consistently everywhere else in this thread for "action" costs (e.g. v14.229 §5's $\epsilon_z\times\|y\|$) — and which is also exactly what v14.227's own original handoff figure of $2\times10^{-12}=10^{-9}\times0.002$ already computes. The two bound different things; neither is wrong, but comparing them and calling the original "conservative" is not quite apples-to-apples. This affects no numerical conclusion.
**Parents:** v14.195, v14.220, v14.227–v14.232.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `4bf898a5385e32887b95e46b0fd4a9faf8ce7e6e` (v14.233), matching local HEAD; live ledger max was v14.233. v14.234 is next-free. No collision.

---

## 1. The arch integral's $O(1/k^2)$ decay — independently re-derived from scratch

This is the one claim in the entry that is genuinely new mathematics (every other term — $\log(n/4)$, $\mathrm{Ci}$, $\mathrm{Si}$, the prime cosine/sine terms — reuses already-audited machinery or standard asymptotics), so it was rebuilt term by term without consulting the entry's own proof order.

With $u(t)=h(t)(2-t)$ on $[0,2]$: first integration by parts on $\int_0^2u(t)\cos(kt)dt$ gives $[u(t)\sin(kt)/k]_0^2-\tfrac1k\int_0^2u'(t)\sin(kt)dt$. At $t=2$, $u(2)=h(2)\times0=0$ (the $(2-t)$ factor vanishes); at $t=0$, $\sin(0)=0$ regardless of $u(0)$. Both boundary contributions vanish independently of each other — confirmed exactly, and confirmed that *both* mechanisms are needed (the $(2-t)$ factor for one endpoint, $\sin(0)=0$ for the other). So $\int_0^2u(t)\cos(kt)dt=-\tfrac1kJ$, $J=\int_0^2u'(t)\sin(kt)dt=\int_0^2[h'(t)(2-t)-h(t)]\sin(kt)dt$ (direct product-rule expansion of $u'$, confirmed exact).

Second integration by parts, on $J$ with $v(t)=u'(t)$: $J=[-v(t)\cos(kt)/k]_0^2+\tfrac1k\int_0^2v'(t)\cos(kt)dt$. Computing the boundary directly: $v(2)=u'(2)=h'(2)\cdot0-h(2)=-h(2)$, so the $t=2$ contribution is $-v(2)\cos(2k)/k=h(2)\cos(2k)/k$; $v(0)=u'(0)=2h'(0)-h(0)=2h'(0)-\tfrac14$ (using the stated $h(0)=1/4$), so the $t=0$ contribution is $v(0)/k=[2h'(0)-\tfrac14]/k$. Summing, and noting the remaining integral $\tfrac1k\int v'\cos(kt)dt$ is itself $O(1/k)$ (a plain bounded, non-resonant integral divided by $k$): $J=\tfrac1k[h(2)\cos(2k)+2h'(0)-\tfrac14]+O(1/k)$ — confirmed exactly matching the entry's stated intermediate result. Since this makes $J=O(1/k)$ overall (not $O(1)$), and $\int u\cos(kt)dt=-J/k$, the first piece is $O(1/k^2)$ — confirmed exactly.

For the second piece: a single integration by parts on $\int_0^2h(t)\sin(kt)dt=[-h(t)\cos(kt)/k]_0^2+\tfrac1k\int_0^2h'(t)\cos(kt)dt=O(1/k)$ (boundary and remainder both $O(1/k)$), so $\tfrac1k\int h\sin(kt)dt=O(1/k^2)$ — confirmed exactly, matching the entry's stated boundary form $[-h(t)\cos(kt)/k^2]_0^2$ (simply the previous boundary term divided by the extra $k$).

Both pieces are $O(1/k^2)$, so the whole arch integral $I(k)=O(1/k^2)$, confirmed independently and completely. This is the correct, rigorous reason a numerical quadrature of the oscillatory arch integral is unnecessary: at $k>402000$ (for $n>R=256000$), $1/k^2<6.2\times10^{-12}$, leaving ample room under any reasonable constant $C$ to stay under the $10^{-9}$ target. The claim that *both* the $(2-t)$ weighting and the $\sin(0)=0$ cancellation are jointly necessary (neither suffices alone — without $(2-t)$, the first integration by parts would leave an $O(1/k)$ term from the $t=2$ boundary) is independently confirmed correct.

## 2. Term-by-term feasibility — spot-checked

$\mathrm{Ci}(n\pi)$ and $\mathrm{Si}(n\pi)/(n\pi)$: both decay like $O(1/n)$ (confirmed via the integration-by-parts bounds $|\mathrm{Ci}(x)|\le2/x$, $|\mathrm{Si}(x)-\pi/2|\le2/x$ independently re-derived in Round 214), so at $n>R=256000$ these are already of order $10^{-6}$ before any further asymptotic refinement — consistent with the entry's claim that reaching $10^{-9}$ absolute (a further three-order tightening) is feasible via one more asymptotic term or an interval enclosure, not a new obstruction. The five prime cosine/sine terms reuse v14.227's already-independently-confirmed (Round 215) adaptive argument-reduction machinery directly — no new analytic content there.

## 3. [N] A precise note on the action-cost parenthetical

Checked v14.233 §3's aside: "$10^{-9}\cdot\|y\|^2=10^{-9}\times4\times10^{-6}=4\times10^{-15}$" is bounding $|\langle y,\delta D\,y\rangle|\le\|\delta D\|\|y\|^2$, the *quadratic energy form* of a diagonal perturbation $\delta D$ with $\|\delta D\|\le10^{-9}$ — a valid bound, but a different quantity from $\|\delta D\,y\|\le\|\delta D\|\|y\|=10^{-9}\times0.002=2\times10^{-12}$, the *linear operator-action norm*, which is exactly what v14.227's original handoff figure computes and exactly the convention used consistently for every other "action" charge in this thread (e.g. v14.229 §5's $\epsilon_z\times\|y\|=2.1\times10^{-23}\times0.002=4.2\times10^{-26}$, independently confirmed in Round 215). Since the two bound genuinely different mathematical objects, describing the original $2\times10^{-12}$ figure as "conservative" relative to the new $4\times10^{-15}$ is not quite a like-for-like comparison — it would only be a looseness if both figures bounded the *same* quantity. This is a narrow, precise observation with no bearing on the entry's actual conclusion (feasibility of the bare-diagonal evaluator), which rests entirely on the independently-confirmed $O(1/k^2)$ arch-integral argument in §1, not on this parenthetical.

## 4. Verdict

```
The arch integral's O(1/k^2) decay (the entry's one genuinely novel
  claim): INDEPENDENTLY RE-DERIVED from scratch via the double
  integration-by-parts argument, confirming both cancellation
  mechanisms ((2-t) at t=2, sin(0)=0 at t=0) are needed and sufficient,
  term for term, matching the entry's stated intermediate expressions
  exactly.
Term-by-term feasibility for log(n/4), Ci, Si, and the prime terms:
  spot-checked against already-independently-confirmed asymptotic
  bounds and v14.227's adaptive machinery; no new obstruction found.
[N] A narrow note: the SS3 action-cost parenthetical computes a
  quadratic-in-||y|| energy-form bound (4e-15) and compares it against
  a linear-in-||y|| operator-action bound (2e-12, matching v14.227's own
  original figure and this thread's standing convention) as though they
  were the same quantity. Both bounds are individually valid; the
  comparison between them is not quite apples-to-apples. No effect on
  any numerical conclusion or on the entry's feasibility verdict.
No correction to the entry's mathematics. No infinite-tail theorem is
  claimed or promoted. No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.234
status: open
action: v14.233's central claim -- the arch integral's O(1/k^2) decay via double integration by parts -- is independently re-derived from scratch and confirmed exact; this is the load-bearing reason the bare-diagonal evaluator is feasible at all, and it holds. A narrow note on SS3's action-cost parenthetical (quadratic vs. linear in ||y||, bounding different quantities) is recorded for precision but changes nothing about the feasibility verdict. Per v14.233's own handoff, implementation of the SS3 blueprint (adaptive log/Ci/Si/prime-trig to 1e-10, the arch bound via certified h-derivative intervals) remains Lane A's task.
deliverable: none required; informational confirmation plus a precision note
constraints: None.
