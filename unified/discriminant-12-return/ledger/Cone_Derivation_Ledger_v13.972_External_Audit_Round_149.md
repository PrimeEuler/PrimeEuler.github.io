# Cone Derivation Ledger v13.972 — External Audit Round 149

Date: 2026-10-02

Auditor: External audit thread (Claude, independent instance).

Scope: `v13.971` (exact six-dimensional source and Fourier-functional
reduction for the Xi phase certificate) — a single, substantial entry
continuing the Xi-scalar certification lane.

Verdict: **Confirmed.** No errors found. This is a standard but lengthy
Feshbach-reduction argument, and I re-derived its two central results —
the quadratic-form reduction and the Fourier-functional reduction — fully
from scratch via direct substitution into the block system, rather than
merely checking them against the stated conclusion.

## 1. Setup and the 6×6 Feshbach matrix [D]

The three-block structure (core `C`, protected 4-dim `P`, tail complement
`Q`, with the `P`–`Q` cross block zero because `P_4,Q_4` are complementary
spectral projections of `J_T`) and the Schur complement
`H_C(0)=F_{CC}(0)-C_Q(0)^*J_Q^{-1}C_Q(0)` (eq 3) are the same Feshbach
mechanics already verified in `v13.954` and `v13.968` — standard and
correctly instantiated here.

## 2. Exact transformed source reduction — re-derived from scratch [D]

From the block system
`[[F_CC,C_P^*,C_Q^*],[C_P,J_P,0],[C_Q,0,J_Q]]\cdot(u,p,q)=(f_C,g_P,g_Q)`,
I solved the `Q`-equation for `q=J_Q^{-1}(g_Q-C_Qu)` (eq 5, trivial) and
substituted into the `C`-equation directly:
`F_{CC}u+C_P^*p+C_Q^*J_Q^{-1}(g_Q-C_Qu)=f_C` rearranges to exactly
`H_C(0)u+C_P^*p=f_C-C_Q^*J_Q^{-1}g_Q`, matching eq 6–7 exactly.

## 3. Exact source-resolvent scalar — re-derived from scratch [D]

This is the most substantial check. Starting from
`\langle f,A^{-1}f\rangle=\langle f_C,u\rangle+\langle g,y\rangle` (valid
because the congruence `y=B_T^{1/2}v_T`, `g=B_T^{-1/2}f_T` gives
`\langle f_T,v_T\rangle=\langle g,y\rangle` exactly, since
`B_T^{-1/2}` is self-adjoint), I split `\langle g,y\rangle=\langle
g_P,p\rangle+\langle g_Q,q\rangle`, substituted `q` from eq 5, and used
self-adjointness of `J_Q^{-1}` to move `C_Q` across the inner product
(`\langle g_Q,J_Q^{-1}C_Qu\rangle=\langle C_Q^*J_Q^{-1}g_Q,u\rangle`). The
result collects exactly into
`\langle g_Q,J_Q^{-1}g_Q\rangle+\langle f_C-C_Q^*J_Q^{-1}g_Q,u\rangle+
\langle g_P,p\rangle=h_{\rm reg}+\langle f_6,\mathcal M_6(0)^{-1}f_6
\rangle`, matching eq 8 exactly, term for term.

## 4. Fourier-functional reduction — re-derived from scratch [D]

Substituting the same `q=J_Q^{-1}(g_Q-C_Qu)` into
`F_a(t)=h_C(t)^*u+h_P(t)^*p+h_Q(t)^*q` and using the adjoint identity
`h_Q(t)^*J_Q^{-1}C_Qu=[C_Q^*J_Q^{-1}h_Q(t)]^*u` (same self-adjointness
move as §3) collects the `u`-coefficient into exactly
`h_C(t)-C_Q^*J_Q^{-1}h_Q(t)=h_{C,\rm red}(t)` (eq 11) and leaves a residual
term `h_Q(t)^*J_Q^{-1}g_Q=r_a(t)` (eq 13) — giving
`F_a(t)=r_a(t)+h_6(t)^*\mathcal M_6(0)^{-1}f_6` exactly as claimed in
eq 14. Both reductions use the identical algebraic move (eliminate `q`,
move `C_Q` across via self-adjoint `J_Q^{-1}`), and both check out exactly
when carried through independently.

## 5. Background bounds and bookkeeping [D]

The four uniform bounds (eq 15–18) are direct Cauchy–Schwarz/operator-norm
applications of `\|J_Q^{-1}\|<10` (eq 1, cited from the certified tail
moat) — confirmed each by hand: `|h_{\rm reg}|\le\|J_Q^{-1}\|\|g_Q\|^2`,
etc. The numeric corollaries `\sqrt{0.0256}=0.16` and
`\sqrt{0.0416}\approx0.20396<0.204` (eq 19) check out exactly. The
coordinate-reduction identity `\widehat Y^*g=\widehat Q^*f_T` (eq 20,
using `\widehat Y=B_T^{1/2}\widehat Q` and `g=B_T^{-1/2}f_T`, so the two
square-root factors cancel under the self-adjoint pairing) is a clean,
correct observation that avoids ever forming `B_T^{\pm1/2}` numerically.
The subspace-error propagation (eq 22–25) is a trivial operator-norm
bound, correctly applied.

## What remains open

- The specific numeric inputs cited as "certified" (`\|J_Q^{-1}\|<10`,
  `\|C_e\|^2<0.0256`, `\|C_o\|^2<0.0416`, the projector-refinement bounds
  in eq 22–23) are accepted as established facts from the referenced
  `v13.823`–`836` lineage, not re-derived from first principles this
  round.
- This entry is explicitly architectural — it reduces the certification
  problem to "a finite numerical payload, not a missing operator
  theorem," and correctly stops there. The actual `a=1` six-dimensional
  interval solve and the resulting scalar enclosure are still future work
  (`[O]`), per the entry's own §9.
- Unchanged from prior rounds: `G_-\ge0` (RH-hard, Round 136); the
  odd-sector Picard-divergence bounds (Round 135); the source-RG absolute
  location question (Round 147); `v13.963`'s `\chi_{12}`-twist and
  fold-recursion-table pipeline (Round 148).

## Result

\[
\boxed{\textbf{v13.971 confirmed.} \textbf{The exact six-dimensional
Feshbach reduction of both the source-resolvent quadratic form and the
Fourier evaluation functional was independently re-derived from scratch
--- not merely checked against the stated conclusion --- by eliminating
the tail-complement block } q \textbf{ via its own equation and moving
the coupling operator } C_Q \textbf{ across the inner product using
self-adjointness of } J_Q^{-1}\textbf{; both reductions (eq 8 and eq 14)
matched the ledger's claimed formulas term for term.} \textbf{The
resulting architecture is correct and honestly scoped: the Xi-scalar
phase certificate is now reduced to a six-dimensional interval solve plus
four explicit, correctly-bounded analytic backgrounds, with no further
operator-theoretic gap remaining before a first proof-grade numerical
instantiation.}}
\]
