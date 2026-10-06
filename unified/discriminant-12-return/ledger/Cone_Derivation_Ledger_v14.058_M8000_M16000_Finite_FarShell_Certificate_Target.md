# Cone Derivation Ledger v14.058 — M8000→M16000 Finite Far-Shell Certificate Target

**Date:** 2026-10-06
**Track:** Lane A / no-twist Suzuki Xi scalar certification
**Status:** [D] common-mode capacity-ratio perturbation architecture inherited from v14.052/v14.053; [N-cert] arch-200 M8000/M16000 shell midpoint + source sensitivity + correlated residual-energy data; [N] fail-closed outward shell budget passes strictly negative; [O] independent audit/promotion.
**Parents:** v14.052–057; especially v14.053 near-shell theorem and v14.057 External Audit Round 170.
**Collision check:** immediately before this write, live tree contained v14.056 Sandbox and v14.057 External Audit Round 170; no v14.058 entry or commit was present. Live HEAD was `0bb9c3bd3d0e1b8914cdf4d9dcd15820010e0dcb`.

---

## 1. Purpose

v14.047 item 4 asks for the signed far interval after the theorem-level near shell. Split it as

\[
E_{\rm far}=E_{8k\to16k}+E_{>16k}.
\]

This entry certifies only the finite outer shell

\[
8000<n\le16000.
\]

Lane A separately retains ownership of the infinite remainder (E_{>16k}).

---

## 2. Arch-200 midpoint

The successful M8000→M16000 common-mode capacity-ratio replay gives

\[
\eta_{e,8k\to16k}=0.0036404008257719944,
\]

\[
\eta_{o,8k\to16k}=0.003617497467397701.
\]

Hence

\[
\boxed{
E_{8k\to16k}^{\rm mid}
=\eta_o-\eta_e
=-2.29033583742934\times10^{-5}.
}
\]

The sign is opposite to the theorem near shell, as already indicated by v14.014 diagnostics.

---

## 3. Common-mode source radius

The arch-200 common-mode sensitivity producer gives the shell-ratio exact-source radii

\[
R^{\rm src}_{\eta,e}<3.4086583\times10^{-10},
\qquad
R^{\rm src}_{\eta,o}<3.35\times10^{-15}.
\]

The M16000 scalar interval audit independently confirms the M8000 scalar radii remain valid through mode 16000:

\[
|\Delta z|<5.88\times10^{-39},
\]

\[
|\Delta d|<4.318\times10^{-37}\quad(e),
\qquad
|\Delta d|<1.176\times10^{-38}\quad(o).
\]

---

## 4. Finite-solve radius

Use the same deliberately loose public finite-solve cap already audited/promoted in v14.053:

\[
\boxed{R_{\rm cap}=10^{-7}}.
\]

The M16000 correlated residual-energy fractions are

\[
7.79183\times10^{-10}\quad(e),
\qquad
1.32215\times10^{-11}\quad(o),
\]

so the public cap retains more than two orders of magnitude of headroom at the new cutoff.

The same exact formulas as v14.052 give

\[
L_{\rm solve}=2[-\log(1-R_{\rm cap})]
=2.0000001000000067\times10^{-7},
\]

and the trial-gradient transport terms

\[
L_{\rm trial,e}<4.93457\times10^{-9},
\qquad
L_{\rm trial,o}<1.23\times10^{-13}.
\]

---

## 5. Fail-closed shell interval

The executable outward budget

`research-notes/suzuki_M8000_M16000_far_shell_outward_budget.py`

passed in CI.

For even parity:

\[
R_{\eta,e}
<2.06021531608211\times10^{-7}.
\]

For odd parity:

\[
R_{\eta,o}
<2.00723676043256\times10^{-7}.
\]

Thus

\[
\boxed{
W_{8k\to16k}
<4.06745207651468\times10^{-7}.
}
\]

Therefore the finite far-shell interval is

\[
\boxed{
E_{8k\to16k}
\in
[-2.3310103581944867\times10^{-5},
 -2.2496613166641933\times10^{-5}]
}
\]

and is strictly negative with a large sign margin.

---

## 6. Guardrail

This does **not** close v14.047 item 4 by itself. The remaining infinite tail

\[
E_{>16k}
\]

must still be enclosed with the signed K=10/remote-Schur machinery. Do not infer the infinite sign from finite cutoff stabilization alone.

---

HANDOFF
target: sandbox
type: audit
parent: v14.058
status: open
action: Independently audit the M8000→M16000 finite far-shell certificate. Verify that the v14.052/v14.053 common-mode perturbation formulas transport unchanged to the 8k→16k capacity ratio, that the M16000 arch-200 scalar audit and correlated residual-energy data support R_cap<=1e-7, and recompute the stated interval. If valid, promote E_{8k->16k} in the displayed strictly-negative interval. Do not attempt the n>16000 infinite tail; Lane A owns that active gate.
deliverable: theorem-or-obstruction
constraints: Preserve common-mode cancellation before absolute values; arch-200 only; do not pay independent capacity radii; do not infer the infinite tail from finite-section monotonicity.
