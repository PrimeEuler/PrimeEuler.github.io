# Cone Derivation Ledger v13.475 — M16001 Anisotropic Tail Split Restores an Even Index-3 Target

Date: 2026-09-14

Status labels: **[D]** exact derived, **[N]** numerical diagnostic, **[N-cert]** previously certified input, **[Audit]** guardrail.

## 0. Synchronization [Audit]

The live ledger was checked at the beginning of this continuation and again immediately before this numbered write.  After `v13.473`, a concurrent arithmetic entry landed as `v13.474` (`Full V4 Character Action across Pell Residue and Mod-4 Lift`).  Therefore `v13.475` was free at creation time.

Relevant Suzuki predecessors:

- `v13.402`: certified even-sector bound `ind_{<=0}(A_even(1))<=4`;
- `v13.452`: full-parity theorem `ind_{<=0}(A_{a=1})<=6`;
- `v13.467`: signed near-rank-one tail self-energy on the stabilized even four-plane;
- `v13.471`: M3999 unresolved four-plane residual-Gram replay;
- `v13.473`: correction showing that the M3999 scalar directional budget is not sufficient for index `<=3` because the six-plane/unresolved cross block must also be controlled.

The new reproducible helper is

`research-notes/suzuki_M16001_even_index3_anisotropic_tail_split.py`

(commit `59479d50386aa9da6691e20dfdcd879aaccd0cf9`).

## 1. Why the split is moved [D/I]

At the M3999 split

\[
F=\{21,23,\ldots,3999\},
\qquad
T=\{4001,4003,\ldots\},
\]

replacing the entire tail inverse by

\[
T_{\rm eff}^{-1}\preceq\delta_T^{-1}I
\]

creates a large artificial six-plane/unresolved cross penalty.  v13.473 showed that the proper seven-plane Schur lower bound then acquires a negative level of about

\[
-2.84\times10^{-11}.
\]

The new idea is to eliminate the moderate band explicitly and move the split to

\[
\boxed{
F=\{21,23,\ldots,16001\},
\qquad
T=\{16003,16005,\ldots\}.
}
\]

Thus the modes `4001..16001`, which generate most of the troublesome anisotropic cross, are treated by the actual source-faithful Schur elimination rather than by a scalar inverse bound.

## 2. Source-faithful M16001 finite elimination [N]

The canonical even source matrix is regenerated from

- cusp diagonal/off-diagonal terms;
- prime-power channels `q=2,3,4,5,7`;
- the source-faithful post-integration-by-parts archimedean rank-two term;
- the full even PSD pole.

The exact displacement-generator LDL recurrence eliminates the pole-free high block through `16001`, followed by the rank-one pole Woodbury update.

The resulting low-core Schur spectrum begins, at ordinary midpoint precision,

\[
\boxed{
(6.8\times10^{-16},
3.2\times10^{-15},
8.3\times10^{-15},
1.333\times10^{-12},
3.8259\times10^{-8},
2.1447\times10^{-4},\ldots).
}
\]

The first four signs remain diagnostic only.

## 3. Actual moderate-tail correction [N]

Comparing the M3999 and M16001 low-core Schur complements shows that the explicitly eliminated band is highly anisotropic.

On the unresolved four-plane, the signed correction has largest scale only

\[
\boxed{1.31\times10^{-14}},
\]

while the raw low-core correction contains much larger directions outside that plane.

The six-plane/unresolved cross from this band is therefore treated explicitly rather than through a worst-case coercivity bound.

This is the mechanism that removes the false `-2.84e-11` obstruction of the M3999 scalar-tail treatment.

## 4. Remote residual through two million [N]

After eliminating through `16001`, the residual operator is regenerated on the normalized certified six-plane together with the unresolved four-plane for

\[
16003\le n\le2,000,000.
\]

The unresolved remote Gram has

\[
\boxed{
\lambda_{\max}(G_{NN})
\approx3.72\times10^{-14}.
}
\]

The normalized six-plane/unresolved residual cross is also much smaller than at the M3999 split.

The certified remote effective-tail floor used for the remaining inverse is

\[
\boxed{
\delta_{\rm remote}
=4.6732-\frac{0.994^2}{0.22}
\approx0.1821272727.
}
\]

## 5. Blockwise far-tail envelopes beyond two million [N/D]

For `n>=2,000,001`, use the source-faithful inverse-power form

\[
r_n=\frac{L}{n}+O(n^{-2})+O(n^{-3}).
\]

A single isotropic ten-dimensional far bound is unusable because the normalized six-plane contains the deliberately small first `L_0` scale.  Instead the far envelope is split into

- a normalized-six-plane Gram bound `f_Q`;
- an unresolved-four-plane Gram bound `f_N`;
- a cross bound `f_X<=sqrt(f_Q f_N)`.

The replay gives

\[
\boxed{f_N<1.3\times10^{-15}.}
\]

This is the relevant scale for the potential seventh direction.

## 6. Proper anisotropic seven-plane lower target [N/N-cert]

Work in normalized six-plane coordinates

\[
P=Q L_0^{-T}.
\]

After subtracting the explicit remote Gram through two million, the blockwise far envelopes, and the certified scalar remote inverse floor, the midpoint lower blocks satisfy

\[
\boxed{
\lambda_{\min}(A_Q)>0.6777,
}
\]

\[
\boxed{
\|B_{Q,N}\|_2<2.68\times10^{-7},
}
\]

and the best unresolved scalar level before the six-plane Schur penalty is

\[
\boxed{
\lambda_{\max}(F_N)>1.122\times10^{-12}.
}
\]

The entire six-plane cross penalty is bounded at the midpoint target by

\[
\boxed{
\frac{\|B_{Q,N}\|_2^2}{\lambda_{\min}(A_Q)}
<1.06\times10^{-13}.
}
\]

Therefore the corrected anisotropic seven-plane target is

\[
\boxed{
1.122\times10^{-12}-1.06\times10^{-13}
>1.016\times10^{-12}.
}
\]

This is over an order of magnitude larger than the `10^{-15}` surviving directions in the coarse M3999 coercivity-floor treatment of v13.473.

## 7. Interpretation [I]

The index-3 obstruction seen in v13.473 is therefore largely a **proof-budget artifact** caused by applying `delta^{-1}I` before eliminating the moderate anisotropic tail.

The M16001 split reveals the more faithful geometry:

1. the troublesome near-tail cross is explicitly absorbed into the finite Schur complement;
2. the remaining remote residual is much smaller;
3. the normalized six-plane block is strongly positive (`>0.67` midpoint target);
4. one corrected unresolved direction again has a `~10^-12` positivity target after the proper seven-plane Schur penalty.

This does not yet prove positivity because source and arithmetic uncertainty have not been outward charged on this new split.

## 8. Next certification obligations [Audit]

To turn the M16001 target into an even-sector index-3 theorem, the next work is now sharply defined:

1. freeze one maximizing unresolved coordinate direction for the anisotropic lower block;
2. outward-certify the M16001 finite Schur scalar/cross quantities in that fixed direction;
3. outward-certify the normalized six-plane lower block at the new split;
4. outward-enclose the remote residual Gram and blockwise far bounds;
5. propagate the exact-vs-nominal source operator error through the full **seven-dimensional** block, not a scalar-only surrogate.

Because the nominal corrected margin is now about

\[
\boxed{1.0\times10^{-12}},
\]

while the global source operator uncertainty is `2e-13`, a theorem-level certificate is numerically plausible if the anisotropic source perturbation is not amplified by more than a modest factor.

## 9. Theorem status [Audit]

No theorem is promoted here.

The certified bounds remain

\[
\boxed{\operatorname{ind}_{\le0}(A_{\rm even}(1))\le4,}
\]

\[
\boxed{\operatorname{ind}_{\le0}(A_{\rm odd}(1))\le2,}
\]

and

\[
\boxed{\operatorname{ind}_{\le0}(A_{a=1})\le6.}
\]

No exact-kernel, RH, or GRH conclusion follows.

---

**Checkpoint conclusion.** Moving the finite/tail split from M3999 to M16001 and explicitly eliminating the moderate anisotropic band removes the large false cross penalty created by a premature scalar coercivity bound.  On the normalized certified six-plane plus unresolved four-plane, the remaining remote-tail treatment leaves a proper seven-plane midpoint lower target above `1.0e-12`.  The even index-3 program is therefore viable again, but its frontier is now an outward anisotropic source/arithmetic certificate on the M16001 split rather than a scalar M3999 directional budget.
