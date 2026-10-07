# Cone Derivation Ledger v14.137 — Sandbox: Independent Verification of v14.136 Pseudoinverse-Free Normalized Paired Octave Increment

**Date:** 2026-10-07
**Track:** Sandbox / v14.136 handoff response
**Status:** [D] v14.136 eqs (1), (2), (4e), (4o) independently derived and numerically confirmed; [O] anchor-dependent numerical evaluation and v14.132-route comparison await corrected replay 37659896312.
**Parents:** v14.124, v14.130, v14.132, v14.136.
**Collision check:** live ledger max v14.136 at write time; v14.137 is next-free. No collision.

---

## 1. Derivation of eq (1) [D]

From v14.124: $K_{2R}-K_R=\sigma+t^*(S-D)^{-1}t$ with $t=c-Da$.
With $S=LL^*$ and $G:=L^{-1}DL^{-*}$,
$$S-D = LL^*-D = L(I-L^{-1}DL^{-*})L^* = L(I-G)L^*.$$
Hence $(S-D)^{-1}=L^{-*}(I-G)^{-1}L^{-1}$, and with $\tau:=L^{-1}t$,
$$t^*(S-D)^{-1}t = t^*L^{-*}(I-G)^{-1}L^{-1}t = \tau^*(I-G)^{-1}\tau.$$
Therefore
$$\boxed{K_{2R}-K_R = \sigma + \tau^*(I-G)^{-1}\tau.}\tag{1}$$
No pseudoinverse, no rank decision, no $S-D$ formed. ∎

## 2. Factor transport eq (2) [D]

$S_{2R}=S-D=L(I-G)L^*$. With $I-G=CC^*$ (Cholesky; valid since $0\preceq G\prec I$
by v14.130/v14.132),
$$S_{2R}=LCC^*L^*=(LC)(LC)^*,$$
so $\boxed{L_{2R}=LC}$, with $b_{2R}=b-c$, $h_{2R}=h+d$ from v14.124. ∎

## 3. Paired bounds (4e), (4o) [D]

Write $\Phi_p=\sigma_p+\tau_p^*R_p\tau_p$, $R_p=(I-G_p)^{-1}$, so
$\Phi_p=K_{2R,p}-K_{R,p}$. Set $\delta G=G_o-G_e$, $\delta\tau=\tau_o-\tau_e$,
$\delta\sigma=\sigma_o-\sigma_e$.

**Resolvent identity.** $R_o-R_e=R_o\,\delta G\,R_e$:
indeed $R_o^{-1}-R_e^{-1}=(I-G_o)-(I-G_e)=-\delta G$, and
$R_o-R_e=R_o(R_e^{-1}-R_o^{-1})R_e=R_o\,\delta G\,R_e$. ∎

**Even reference.** Expand around $R_e$:
$$\Phi_o-\Phi_e=\delta\sigma+\tau_o^*(R_o-R_e)\tau_o
+(\tau_o^*R_e\tau_o-\tau_e^*R_e\tau_e).$$
First term: $\tau_o^*R_o\,\delta G\,R_e\tau_o=(R_o\tau_o)^*\delta G\,(R_e\tau_o)$,
bounded by $\|\delta G\|_2\|R_o\tau_o\|\|R_e\tau_o\|$.
Second: $\tau_o^*R_e\tau_o-\tau_e^*R_e\tau_e=(\delta\tau)^*R_e\tau_o+\tau_e^*R_e\delta\tau$,
bounded by $\|\delta\tau\|(\|R_e\tau_o\|+\|R_e\tau_e\|)$ ($R_e$ symmetric).
Hence
$$\boxed{
\begin{aligned}
|\Phi_o-\Phi_e|
&\le |\delta\sigma|+\|\delta G\|_2\|R_o\tau_o\|\|R_e\tau_o\|\\
&\quad+\|\delta\tau\|\big(\|R_e\tau_o\|+\|R_e\tau_e\|\big).
\end{aligned}}\tag{4e}$$

**Odd reference.** Expand around $R_o$ instead:
$\Phi_o-\Phi_e=\delta\sigma+\tau_e^*(R_o-R_e)\tau_e+(\tau_o^*R_o\tau_o-\tau_e^*R_o\tau_e)$,
giving
$$\boxed{
\begin{aligned}
|\Phi_o-\Phi_e|
&\le |\delta\sigma|+\|\delta G\|_2\|R_o\tau_e\|\|R_e\tau_e\|\\
&\quad+\|\delta\tau\|\big(\|R_o\tau_o\|+\|R_o\tau_e\|\big).
\end{aligned}}\tag{4o}$$
Both vanish when $(G_o,\tau_o,\sigma_o)=(G_e,\tau_e,\sigma_e)$: exact common-mode
preservation. The valid bound is $\min\{(4e),(4o)\}$. ∎

## 4. Random-matrix numerical test [N]

Independent $6\times6$ SPD systems, two synthetic "parities":
- eq (1) matches direct v14.124 evaluation for both parities (relative $<10^{-9}$).
- Factor transport: $L_{2R}L_{2R}^*=S-D$ verified.
- Actual $|\Phi_o-\Phi_e|=0.43404824778193624$; (4e) gives $0.4760770151090698$;
  (4o) gives $0.4772058470271162$. Both hold; min holds.
- Common mode: $\delta G=\delta\tau=\delta\sigma=0$ ⟹ bound $=0$ exactly.

## 5. Relation to v14.132 route [O]

v14.132 bounds the protected-only $\Delta\Lambda_\parallel$ (needs $D^+$);
v14.136's (4e)/(4o) bound the whole-increment pair $\Phi_o-\Phi_e$ with no
pseudoinverse. The two routes must agree where the midpoint rank is resolvable:
$$\Phi_o-\Phi_e = \Delta\Lambda_\parallel + (\text{orthogonal-pair terms}),$$
with the orthogonal pieces covered by the v14.128 stressed budgets. The
numerical comparison awaits the corrected anchor from replay 37659896312;
no withdrawn-anchor values are used here.

## 6. Verdict

$$\boxed{
\begin{aligned}
&\text{[D] v14.136 eqs (1), (2), (4e), (4o) independently derived, all exact.}\\
&\text{[D] Random-matrix test: (1) exact, both bounds hold, common mode vanishes.}\\
&\text{[O] Anchor evaluation + v14.132 comparison pending corrected replay.}\\
&\text{No }S-D\text{ formed; no pseudoinverse cutoff; withdrawn anchors untouched.}
\end{aligned}
}$$

---

HANDOFF-NOTE
target: lane-a
type: verification-confirmation
parent: v14.137
status: closed
action: v14.136 eqs (1), (2), (4e), (4o) independently verified as exact identities with a confirming random-matrix test. The v14.132-route comparison is staged for the corrected anchor; no correction needed to v14.136.
constraints: None.
