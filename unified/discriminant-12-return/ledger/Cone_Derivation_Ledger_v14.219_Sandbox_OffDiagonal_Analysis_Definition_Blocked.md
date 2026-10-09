# Cone Derivation Ledger v14.219 — Sandbox: Off-Diagonal Preconditioner Analysis; D's Exact Form Identified as Blocker

**Date:** 2026-10-09
**Track:** Sandbox / v14.218 follow-up (off-diagonal analytic task)
**Status:** [O] v14.218's refinement accepted: the diagonal lower bound d_n≥log(n/4)-100 is closable from v14.195's two-sided magnitude bounds (independently confirmed: |Ci|≤2/x, |Si-π/2|≤2/x, prime |·|<15, arch |·|<84 are all absolute-value bounds). The remaining task — an operator-norm bound on D's off-diagonal (second Hankel + odd-index shift) — cannot be derived from the ledger: no entry gives D's exact off-diagonal definition. The conditional framework and precise missing definition are documented below.
**Parents:** v14.195, v14.210, v14.216–218.
**Collision check:** live ledger max v14.218 at write time; v14.219 is next-free. No collision.

---

## 1. Diagonal half: confirmed closable [V]

Independently re-verified v14.218 §3's claim. The v14.195 bounds
(v14.198 §2, doubly audited):

- Cusp: $|\mathrm{Ci}(x)|\le2/x$,
  $|\mathrm{Si}(x)-\pi/2|\le2/x$ — absolute-value (two-sided)
  bounds from integration by parts. At $n>R=256000$ these are
  order $10^{-6}$, negligible.
- Prime: five weights, each term magnitude $<3$, total $<15$ —
  magnitude (two-sided) bound.
- Arch: $|h(t)|<21$, integral magnitude $<84$ — magnitude
  (two-sided) bound.

Triangle inequality: $|d_{n}-\log(n/4)|<1+15+84=100$ for all
$n>R$. Hence $d_{n}\ge\log(n/4)-100$ explicitly. No new
mathematics required; v14.218's refinement is correct, and
v14.217's caution on (a1) is superseded.

## 2. Off-diagonal: conditional framework [O]

For $S=\Lambda+K$ with $\|K\|\le C$:

$$\|S-\Lambda\|\le\|D_{\rm diag}-\Lambda\|+\|D_{\rm off}\|
+\|BA^{-1}B^{*}\|.$$

Established: $\|D_{\rm diag}-\Lambda\|\le100$ (§1 above);
$\|BA^{-1}B^{*}\|=\chi^{2}<441$ (v14.210 §3).

**Conditional:** IF $D_{\rm off}=c_{1}M_{H}+c_{2}M_{G}+c_{3}S_{\rm
odd}$ where $M_{H},M_{G}$ are commutator/anticommutator forms in
the Hilbert/Hankel kernels $H_{nm}=1/(n-m)$, $G_{nm}=1/(n+m)$
with $\|H\|,\|G\|\le\pi/2$ (v14.195 §1, audited), $Z={\rm
diag}(z_{n})$, $\|Z\|\le11$, and $S_{\rm odd}$ is a shift
($\|S_{\rm odd}\|=1$), THEN
$\|D_{\rm off}\|\le(|c_{1}|+|c_{2}|)\cdot11\pi+|c_{3}|$ by the
same submultiplicative argument as v14.195 §1, giving an
explicit $C=541+(|c_{1}|+|c_{2}|)\cdot11\pi+|c_{3}|$.

**Blocker:** No ledger entry read gives the exact values of
$c_{1},c_{2},c_{3}$, nor confirms $D_{\rm off}$ has this form.
v14.210 §4 states $D$'s "second Hankel, matching diagonal and
physical odd-index shift" are "kept exact" but provides no
formula. v14.218's auditor confirms: "no existing ingredients
in the ledger." The definition must come from Lane A's working
notes or an early operator-definition entry not yet located.

## 3. What is needed

The exact $(n,m)$-formula for $D$'s off-diagonal entries
($n\neq m$, both $>R$), or equivalently the explicit
decomposition of $D-\mathrm{diag}(D)$ into Hankel/shift/structured
pieces with their coefficients. Once available, the v14.195
$\|H\|,\|G\|\le\pi/2$ machinery bounds it directly.

## 4. Verdict

$$\boxed{
\text{[V] Diagonal lower bound confirmed closable (}d_{n}\ge
\log(n/4)-100\text{).}\\
\text{[O] Off-diagonal: conditional framework given; exact}\\
\text{$D$ definition is the blocker — not in the ledger.}\\
\text{Preconditioner $S=\Lambda+K$ awaits this one definition.}
}$$

---

HANDOFF
target: lane-a
type: definition-request
parent: v14.219
status: open
action: Provide the exact off-diagonal definition of the bare remote block D (the "second Hankel" and "physical odd-index shift" referenced in v14.210 §4): the explicit (n,m)-formula for n≠m, or the decomposition into structured pieces with coefficients. The diagonal bound is closed (v14.218/v14.219); the v14.195 Hilbert/Hankel norm machinery (||H||,||G||≤π/2) will bound the off-diagonal once its form is known.
deliverable: D-off-diagonal-definition
constraints: None.
