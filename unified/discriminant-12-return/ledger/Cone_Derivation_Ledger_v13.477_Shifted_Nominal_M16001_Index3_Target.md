# Cone Derivation Ledger v13.477 — Shifted-Nominal M16001 Even Index-3 Target

Date: 2026-09-14

Status labels: **[D]** exact derived, **[N]** numerical diagnostic, **[N-cert]** previously certified input, **[Audit]** guardrail.

## 0. Synchronization [Audit]

The live ledger was checked immediately before this numbered write.  The newest numbered entry was `v13.476` (affine `S4` character table), so `v13.477` was free.

Relevant Suzuki predecessors:

- `v13.401-v13.402`: certified even-sector six-plane theorem and exact-vs-nominal source enclosure;
- `v13.473`: seven-plane cross-block guardrail showing the M3999 scalar-only route is insufficient;
- `v13.475`: M16001 anisotropic tail split restoring a proper seven-plane midpoint target above `1e-12`.

New reproducible helpers:

- `research-notes/suzuki_M16001_even_index3_shifted_nominal_target.py`
  (commit `3632aa38aeea460309a248a6f16a61a741246a58`),
- `research-notes/suzuki_M16001_shifted_nominal_longdouble_crosscheck.py`
  (commit `12ecb8364fa795eecaf1be53471803e111866112`).

## 1. Why shift the nominal operator [D]

v13.401 certifies a dimension-free exact-vs-nominal source-operator enclosure

\[
\boxed{\|A_{\rm exact}-A_{\rm nom}\|<2\times10^{-13}.}
\]

Hence, in operator order,

\[
\boxed{
A_{\rm exact}
\succeq
A_{\rm nom}-\varepsilon I,
\qquad
\varepsilon=2\times10^{-13}.
}
\]

Therefore a clean sufficient route to an even-sector index-3 theorem is:

1. define the shifted nominal operator
   \[
   B:=A_{\rm nom}-\varepsilon I;
   \]
2. certify that `B` has a seven-dimensional positive subspace;
3. conclude the same index upper bound for `A_exact` by monotonicity.

This avoids propagating the source perturbation separately through each finite-Schur, residual, and cross term.

## 2. Shifted M16001 finite solve [N]

The v13.475 source-faithful M16001 split is rerun with the diagonal shifted by

\[
-\varepsilon=-2\times10^{-13}.
\]

The shifted low-core finite Schur spectrum begins

\[
\boxed{
(-1.99\times10^{-13},
-1.97\times10^{-13},
-1.92\times10^{-13},
1.133\times10^{-12},
3.8259\times10^{-8},
2.1447\times10^{-4},\ldots).
}
\]

This is exactly the qualitative behavior expected from the high-precision tiny-spectrum diagnostics: the first three levels are below the global source uncertainty scale, while the fourth remains positive on the shifted nominal branch.

## 3. Shifted remote coercivity [D/N-cert]

The remote finite/tail floor is shifted consistently.  Using the already-certified raw inputs conservatively gives

\[
\boxed{
\delta_{\rm remote,shift}
=(4.6732-\varepsilon)
-\frac{0.994^2}{0.22-\varepsilon}.
}
\]

Numerically this differs negligibly from the unshifted

\[
0.1821272727\ldots
\]

but keeps the lower-bound logic fail-closed on the shifted operator.

## 4. Shifted seven-plane anisotropic target [N]

The same normalized basis

\[
P=Q L_0^{-T}
\]

and unresolved four-plane are used.

After

- explicit finite elimination through `16001`,
- explicit remote residual-Gram accumulation through `2,000,000`,
- blockwise far-tail inverse-power envelopes,
- the shifted remote coercivity floor,

the midpoint targets are

\[
\boxed{\lambda_{\min}(A_Q)>0.67773,}
\]

\[
\boxed{\|B_{Q,N}\|_2<2.68\times10^{-7},}
\]

\[
\boxed{\lambda_{\max}(F_N)>9.22\times10^{-13}.}
\]

The corresponding six-plane Schur penalty remains only

\[
\boxed{<1.06\times10^{-13}.}
\]

Hence the shifted nominal anisotropic lower target is

\[
\boxed{
9.22\times10^{-13}-1.06\times10^{-13}
>8.16\times10^{-13}>0.
}
\]

Thus the global `2e-13` source uncertainty can be absorbed at operator level while leaving a substantial midpoint seven-plane margin.

## 5. Structured-solve arithmetic cross-check [N]

To isolate linear-algebra rounding from source-model uncertainty, the same shifted source scalar payload was replayed with `numpy.longdouble` structured LDL arithmetic.

The maximum finite-solve coefficient difference between the ordinary binary64 and long-double structured solves is

\[
\boxed{<4\times10^{-15}.}
\]

For the largest shifted unresolved finite Rayleigh direction, the scalar difference is only

\[
\boxed{1.36\times10^{-16}.}
\]

This is almost two orders of magnitude below the `~1e-14` local scalar slack and many orders below the final `8e-13` shifted anisotropic target.

Therefore the structured finite solve itself is not the limiting uncertainty.

## 6. What remains open [Audit]

The shifted-operator architecture removes the main conceptual source-perturbation obstacle, but the current helper is still a midpoint target rather than a complete outward certificate.

The remaining obligations are:

1. outward-certify the shifted nominal finite Schur block at M16001;
2. outward-certify the normalized six-plane/unresolved cross block;
3. outward-certify the remote residual Gram through two million;
4. outward-certify the blockwise far-tail envelopes;
5. freeze a fixed seventh coordinate direction, or directly certify a positive eigenvalue/Schur complement of the resulting `7x7` lower matrix.

The existing v13.401 arithmetic machinery is highly relevant: it already supplies long-double `gamma_n` residual accounting, source-independent structured-solve verification, and fail-closed tail-generation techniques.  The new margins are large enough that the arithmetic replay should not require the extreme delicacy of the original six-plane proof.

## 7. Theorem status [Audit]

No theorem is promoted yet.

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

**Checkpoint conclusion.** The global source uncertainty from v13.401 has the exact operator-order form needed for a shifted-nominal proof strategy.  Replaying the anisotropic M16001 split on `A_nom-2e-13 I` leaves a proper seven-plane midpoint lower target above `8.1e-13`.  Independent long-double structured-solve arithmetic changes the relevant finite scalar by only `1.4e-16`, so the remaining frontier is a conventional outward numerical replay of the shifted M16001 blocks and remote Gram—not a new conceptual source-perturbation problem.
