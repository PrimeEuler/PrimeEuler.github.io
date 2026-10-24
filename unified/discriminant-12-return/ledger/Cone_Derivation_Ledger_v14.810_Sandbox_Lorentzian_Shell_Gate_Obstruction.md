# Cone Derivation Ledger v14.810 — Lorentzian fixed-shell gate: support obstruction at every n≥3

**Date:** 2026-10-24 EDT.
**Lane:** sandbox (combinatorics signature gate).
**Parents:** v14.807 (gate), v14.784–785, v14.809.
**Research note:** `research-notes/Sandbox_Lorentzian_Shell_Gate_Test.md` (commit `866fdde477ff9acb2163e76224f9acf7c06017e0`).
**Collision check:** immediately before this write, live master HEAD is `866fdde477ff9acb2163e76224f9acf7c06017e0`; v14.810 verified unoccupied. Additive only; Suzuki production payloads, far-tail work and prior certificates untouched.

## 1. The gate and the canonical choice [D]

v14.807's next falsifiable gate: choose a canonical homogeneous fixed-product-shell generating polynomial, test support M-convexity and every quadratic derivative's Hessian inertia, and record a minimal obstruction if it fails. Canonical choice: for shell \(n\), factor pairs \((a,b)\) with \(ab=n\), homogenized at the shell's maximal degree \(d=\max(a+b)\):

\[
F_n(x,y,z)=\sum_{ab=n} x^a y^b z^{d-a-b},
\qquad
S_n=\{(a,\ b,\ d-a-b): ab=n\}.
\]

M-convexity of the support is a necessary condition for a polynomial to be Lorentzian (Brändén–Huh), and it depends only on the support, not the coefficients.

## 2. Obstruction theorem [D]

Every shell contains the extreme points \(\alpha=(1,n,0)\) and \(\beta=(n,1,0)\) (with \(d=n+1\)). Since \(\alpha_y=n>1=\beta_y\), M-convexity requires an exchange \(\alpha-e_y+e_j \in S_n\) for some \(j\) with \(\alpha_j<\beta_j\). The only candidates are \(j=x\), giving \((2,n-1,0)\), which lies in \(S_n\) only if \(2(n-1)=n\), i.e. \(n=2\); and \(j=z\), giving \((1,n-1,1)\), which would require \(n-1=n\). Hence for **every \(n\ge 3\)**, \(S_n\) is not M-convex, and **no polynomial with support exactly \(S_n\) — with any nonzero coefficients — is Lorentzian**. The obstruction is at support level, coefficient-independent.

Minimal instance: \(n=3\), \(S_3=\{(1,3,0),(3,1,0)\}\); the required intermediate point \((2,2,0)\) belongs to shell 4. Structural reason: a fixed-product shell is a hyperbola arc in the \((a,b)\) plane, and M-convexity demands unit-exchange chain-connectedness that a hyperbola arc has only in the adjacent case. Corroboration: full M-convexity tests for \(n=1\)–\(24\) (fail for all \(n\ge3\)) and the extreme-pair exchange checked unsatisfiable for \(n=3\)–\(500\).

## 3. The surviving shells [D]

\(n=1\) is trivially M-convex. For \(n=2\), \(F_2=xy^2+x^2y=xy(x+y)\) (the homogenizing \(z\) is inert); the support \(\{(1,2,0),(2,1,0)\}\) is M-convex and the first-derivative quadratics \(y^2+2xy\), \(x^2+2xy\) have Hessians with eigenvalues \(1\pm\sqrt5\) — exactly one positive. \(F_2\) is Lorentzian in its effective variables. Since M-convexity already fails for \(n\ge3\), the Hessian-derivative test is moot there.

## 4. Independent spot-verification of v14.807 [D]

Sandbox-recomputed before Audit R344 was seen: \(\det\nabla^2(x^ay^b)=ab(1-d)x^{2a-2}y^{2b-2}\), via \(ab[(a-1)(b-1)-ab]=ab(1-a-b)\); and the divisor counterexample \(d(3)^2=4<d(2)d(4)=6\) from \(d(2)=d(3)=2\), \(d(4)=3\). Both agree with v14.807.

## 5. Scope [D/O]

This closes v14.807's gate for the canonical max-degree homogenization. Other normalizations (different homogenizing degree, weighted or cumulative supports) are new choices not covered here; any Lorentzian object in this family must mix shells, which re-enters v14.807's addition-closure guardrail. Nothing here bears on the open hyperbolicity-cone-to-causal-cone intertwiner, and no GR or \(G\) claim is made; v13.770's carrier distinction remains in force.

**Flags:** `fixed_shell_M_convexity=n_le_2_only`; `minimal_obstruction=n3_extreme_pair`; `obstruction_level=SUPPORT_coefficient_independent`; `v14.807_spot_checks=CONFIRMED_independent`; `shell_mixing=OPEN_new_choice`; `GR_geometry_intertwiner=OPEN`; `G_derived=false`; `Suzuki_payloads_touched=false`; `far_tail_touched=false`.

HANDOFF
target: external-audit
type: sandbox-gate-verification
parent: v14.810
status: open
action: Independently verify the extreme-pair obstruction argument for all n≥3, the n=2 derivative Hessian eigenvalues \(1\pm\sqrt5\), and the support-level (coefficient-independent) scoping; confirm the v14.807 gate is closed for the canonical max-degree homogenization only.
deliverable: scoped audit verdict; do not modify Suzuki or far-tail files.
