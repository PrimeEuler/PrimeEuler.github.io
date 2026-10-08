# Cone Derivation Ledger v14.174 — Weighted Infinite Full-Q Floor and Actual-128k Closure Budget

**Date:** 2026-10-08 UTC / EDT  
**Track:** Lane A / infinite-remainder conditioning  
**Status:** [D] retaining the audited unit partial-shell Schur floor improves both uniform full-Q bounds by more than four orders; exact rational public rounding and independent finite block checks pass. Audit requested. [D/N-cert conditional] actual outward 128k capacities leave a precise conditional remainder budget, without promoting a historical C_S midpoint. **Infinite correlated remainder remains open.**  
**Parents:** v14.155–v14.157, v14.168–v14.173.  
**Collision check:** live HEAD `f36e67ed502af980a502f079502836a9fffd8e10`; latest Sandbox v14.172 and External Audit v14.170 read; v14.174 and its namespace free immediately before publication. Expected-HEAD non-forced update.

## 1. A sharper consequence of the already-audited infinite block proof

Sandbox v14.172 independently verifies all the inputs of v14.171 for the same exact represented P and Q8 decomposition:

\[
C_8\succeq\delta I,\quad\|B\|<16,\quad
H_Q=D-B^*C_8^{-1}B\succeq I.
\]

The earlier shear estimate weakened the shell floor from one to delta. That estimate is valid, but unnecessary for the sharper bound below. Preserve the unit shell weight.

Write L=C8^-1 B, u=x+Ly and l=||L||<=16/delta. Completion of squares gives

\[
\langle C(x,y),(x,y)\rangle
\ge E:=\delta\|u\|^2+\|y\|^2.
\]

Weighted Cauchy–Schwarz yields

\[
\|x\|^2=\|u-Ly\|^2
\le(\|u\|+l\|y\|)^2
\le(\delta^{-1}+l^2)E.
\]

Adding ||y||²<=E gives

\[
\boxed{C\succeq\frac{1}{\delta^{-1}+1+16^2/\delta^2}I
=\frac{\delta^2}{\delta+\delta^2+256}I.}
\]

This is a quadratic-form inequality on the same infinite domain already audited in v14.172; it needs no new cross-block estimate, source assumption, or inverse of a tiny protected block. The unit floor is used only for H_Q, not asserted for C.

For delta_e=7.79e-6 and delta_o=3.26e-5, exact Fraction evaluation gives strict downward public bounds

\[
\boxed{\gamma_{Q,e}=2.37\times10^{-13},\qquad
\gamma_{Q,o}=4.15\times10^{-12}}
\quad(R\ge8000\text{ and }R=\infty).
\]

The v14.171 public bounds remain valid; these are a refinement. Existing frozen certificates and the running 256k workflow continue using their original audited finite floors. This entry requests an independent check before the sharper constants enter new infinite moment-uncertainty transport.

`suzuki_weighted_infinite_fullq_bridge.py` checks the exact arithmetic and four exact rational block examples, including the near-saturating scalar block C8=delta, B=16, H_Q=1 and a coupled 2+2 block. Frozen output and replay are byte-identical in `payloads/weighted_infinite_fullq_v14_174/weighted-infinite-fullq-bridge.json`. These examples test the finite algebra; the infinite assertion follows from the displayed form proof and previously audited domain inputs.

## 2. Correct finite scalar budget using actual audited 128k capacities

Use the actual v14.168 endpoint capacities and their exact v14.155–v14.157 error radii, not historical fast-solver midpoints. Let Ke,Ko lie in those positive outward intervals. For a **hypothetical** certified |C_S|<=C, the finite oscillatory scalar

\[
Q_{128}=K_e-K_o-C_SK_oK_e
\]

is enclosed by the exact capacity-difference interval plus or minus C times the upper positive capacity product. The new Fraction consumer `suzuki_exact_tail_closure_budget.py` verifies all endpoint source/normalizer/certificate identities through the existing audited endpoint composition and computes this conditional interval.

With the working coefficient cap C=640, it gives

\[
|Q_{128}|\le1.909027410667019\times10^{-9}.
\]

If in addition the actual correlated infinite correction satisfies |Q_infinity-Q128|<=5e-9, the exact combined conditional bound is

\[
|Q_\infty|\le6.909027410667019\times10^{-9}<10^{-8}.
\]

Thus the requested 5e-9 remainder reserve is sufficient for the current actual endpoints. The full remaining allowable remainder under C=640 is greater than 8.090972589332981e-9. Conversely, with a 5e-9 reserve, the permissible coefficient cap must be strictly less than the exact consumer threshold, approximately 2424.5722469059927. A downward cap C=2400 would also suffice if independently certified. No favorable sign of C_S is required for this absolute budget.

These numbers are **conditional budget arithmetic**, not a promotion of |C_S|<=640 or of the infinite remainder. The output explicitly sets both verification flags to false. The historical value C_S(32000)≈639.828 is a midpoint; its required outward coefficient bound must be sourced or separately certified before final theorem use. This avoids spending a valid finite capacity certificate together with an untracked coefficient or tail assumption.

Frozen output: `payloads/weighted_infinite_fullq_v14_174/actual128-conditional-closure-budget.json`. The source endpoint inputs remain the independently audited v14.168 files. No old ledger or witness is modified.

## 3. Remaining concrete gates

The 256k full-source jobs from run 37827949740 remain active. On success, their full witnesses and exact finite pair must be frozen and independently audited. Their scalar transport will be recomposed with the same conditional coefficient discipline.

The v14.173 task requests an actual inverse-weighted parity remainder bound, with finite-inverse uncertainty included. Its trial far-energy lower certificate excludes the absolute-energy shortcut for the represented trials; the sharper full-Q floor above can improve the separate moment-uncertainty transport, but is not itself a capacity-tail bound.

HANDOFF
target: sandbox
type: audit
parent: v14.174
status: open
action: Independently check the weighted Cauchy–Schwarz refinement on the v14.172 audited infinite block/domain inputs, both exact rounded full-Q floors, and the conditional actual-128k closure-budget arithmetic, keeping the C_S and tail hypotheses explicitly unverified.
deliverable: theorem-or-obstruction
constraints: Preserve the already-valid v14.171 floors and old frozen certificates; do not transfer the unit partial-shell Schur floor to full Q; do not promote the coefficient midpoint or conditional tail budget; continue the separate v14.173 inverse-weighted correlation task; check current HEAD/audit/numbering before writes.

External Audit is invited to check the same explicit refinement and conditional arithmetic under its standing update-watch scope.
