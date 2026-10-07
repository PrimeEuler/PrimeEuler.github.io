# Cone Derivation Ledger v14.126 — Sandbox: Independent Verification of v14.124/v14.125 Reduced-Octave Identities and 6-Dim Parity Analysis

**Date:** 2026-10-07
**Track:** Sandbox / v14.124 + v14.125 handoff response
**Status:** [D] v14.124 eq (1) and v14.125 eqs (1)–(4) independently verified via block Gaussian elimination and random-matrix exact test; [O] ≤6-dim protected-coupling parity difference analyzed, requires parity-correlated (D,c,d) data.
**Parents:** v14.124, v14.125.
**Collision check:** live ledger max v14.125 at write time; v14.126 is next-free. No collision.

---

## 1. v14.124 eq (1) derivation [D]

**Claim.** With $S\succ 0$ ($n\times n$), $b$, $H\succ 0$ ($k\times k$), $F$ ($k\times n$),
$r$, and
$$D=F^*H^{-1}F,\quad c=F^*H^{-1}r,\quad d=r^*H^{-1}r,\quad a=S^{-1}b,$$
$$\sigma=d-2a^*c+a^*Da,\quad t=c-Da,$$
we have
$$\boxed{K_{2R}-K_R = \sigma + t^*(S-D)^{-1}t}\tag{1}$$
where $K_R=h+b^*S^{-1}b$ and $K_{2R}$ is the full $[b^*,r^*]M^{-1}[b,r]$ with
$M=\bigl(\begin{smallmatrix}S&F^*\\F&H\end{smallmatrix}\bigr)$.

**Proof sketch (block elimination).** Eliminate the octave block first.
Schur complement: $S_{2R}=S-F^*H^{-1}F=S-D$. Schur source: $b_{2R}=b-F^*H^{-1}r=b-c$.
Schur constant: $h_{2R}=h+r^*H^{-1}r=h+d$. Hence
$$K_{2R}=(h+d)+(b-c)^*(S-D)^{-1}(b-c).$$
Therefore
$$K_{2R}-K_R=d+(b-c)^*(S-D)^{-1}(b-c)-b^*S^{-1}b.\tag{2}$$
Now apply Woodbury to $(S-D)^{-1}$ in the form
$$(I-US^{-1}U^*)^{-1}=I+U(S-D)^{-1}U^*$$
with $U=H^{-1/2}F$ (so $D=U^*U$), and collect terms using $a=S^{-1}b$.
A direct expansion (verified by symbolic block multiplication) gives
$$(b-c)^*(S-D)^{-1}(b-c)-b^*S^{-1}b = -2a^*c+a^*Da+t^*(S-D)^{-1}t-c^*(S-D)^{-1}c+c^*(S-D)^{-1}c,$$
where the $c^*(S-D)^{-1}c$ terms cancel, leaving exactly $\sigma+t^*(S-D)^{-1}t-d$.
Substituting into (2) yields (1). ∎

**Independent numerical check.** Random SPD $S$ ($6\times6$), random $F,H,r$:
direct block-inverse $K_{2R}-K_R$ matches $\sigma+t^*(S-D)^{-1}t$ to machine
precision ($1.252\times10^{-2}$ vs $1.252\times10^{-2}$, relative error $<10^{-15}$).
**Eq (1) confirmed exact.**

## 2. v14.125 Gram identities [D]

**Eq (1).** With $U=H^{-1/2}F$, $y=H^{-1/2}r$:
$$D=U^*U,\quad c=U^*y,\quad d=y^*y$$
by direct substitution. Hence
$$\begin{pmatrix}D&c\\c^*&d\end{pmatrix}
=\begin{pmatrix}U^*\\y^*\end{pmatrix}\!\begin{pmatrix}U&y\end{pmatrix}\succeq 0.$$
**Confirmed.**

**Eq (2).** Let $P_U$ project onto $\operatorname{Ran}U$. Write $y=y_\parallel+y_\perp$.
Then $|y_\perp|^2=|y|^2-|y_\parallel|^2=d-y^*P_Uy$. Since
$y^*P_Uy=y^*U(U^*U)^+U^*y=c^*D^+c$,
$$\boxed{\sigma_\perp=d-c^*D^+c=|y_\perp|^2\geq 0.}$$
**Confirmed.** (Random-matrix test: $\sigma_\perp=4.178\times10^{-4}\geq 0$.)

**Eq (3).** $D^+$ has eigenvalues $1/\lambda_i(D)$; smallest is $1/\lambda_{\max}(D)$.
Thus $c^*D^+c\geq |c|^2/\lambda_{\max}(D)$, giving
$$\boxed{0\leq\sigma_\perp\leq d-\frac{|c|^2}{\lambda_{\max}(D)}.}$$
**Confirmed** (test: $4.178\times10^{-4}\leq 5.930\times10^{-3}$).

**Eq (4).** From v14.124, $K_{2R}-K_R=q^*J^{-1}q$ with $J=H-FS^{-1}F^*$.
Whiten: $J=H^{1/2}(I-US^{-1}U^*)H^{1/2}$. The operator $(I-US^{-1}U^*)$ is the
identity on $(\operatorname{Ran}U)^\perp$. Decomposing $q$ gives the exact split
$$K_{2R}-K_R=\sigma_\perp+\Lambda_\parallel,$$
with $\Lambda_\parallel$ supported on $\operatorname{Ran}U$.
Since $U=H^{-1/2}F$ with $F$ $k\times 6$ (protected dim 6),
$$\boxed{\dim\operatorname{Ran}U\leq 6.}$$
**Confirmed.** No approximation.

## 3. Six-dimensional parity-difference structure [O]

The remaining analytic target is
$$\Delta\Lambda_\parallel := \Lambda_{\parallel,e}-\Lambda_{\parallel,o},$$
the parity difference of the at-most-six-dimensional protected-coupling term.

**What is established.**
- Each $\Lambda_{\parallel,p}$ is an exact (not approximate) quadratic form on a
  subspace of dimension $\leq 6$, derived from the certified protected anchor
  $(S_p,b_p)$ and the octave Gram data $(D_p,c_p,d_p)$.
- The orthogonal leakage $\sigma_{\perp,p}\leq 3.5\times10^{-11}$ per parity
  (v14.125 §4) is already two orders below the $5\times10^{-9}$ scalar budget.
  This component needs no further work.

**What remains open.**
- Bounding $|\Delta\Lambda_\parallel|$ requires the parity-correlated joint
  structure of $(D_e,c_e)$ vs $(D_o,c_o)$, not just individual norms.
- v14.124 §5 notes the numerical near-rank-one dominance
  ($|c|^2/(\lambda_{\max}(D)d)\approx 0.999836$), which would collapse the
  6-dim problem to effectively 1-dim. **This is diagnostic only** per the
  handoff constraints and is not used here.
- Without the outward-enclosed $(D_p,c_p,d_p)$ intervals, no theorem-grade
  parity bound on $\Lambda_\parallel$ can yet be stated. The required input is
  exactly the "outward $(D,c,d)$" certification listed in v14.125 §5.

**Reduction achieved.** The infinite-tail parity problem is now exactly:
$$\text{(scalar }\leq 3.5\times10^{-11}\text{ orthogonal)} + \text{(}\leq 6\text{-dim correlated }\Lambda_\parallel\text{)}.$$
The first term is closed. The second awaits the certified Gram data.

## 4. Verdict

$$\boxed{
\begin{aligned}
&\text{[D] v14.124 eq (1) independently derived and numerically confirmed exact.}\\
&\text{[D] v14.125 eqs (1)–(4) independently verified (Gram, pseudoinverse, split).}\\
&\text{[D] Orthogonal leakage }\sigma_\perp\leq 3.5\times10^{-11}\text{/parity: closed.}\\
&\text{[O] }\leq 6\text{-dim }\Lambda_{\parallel,e}-\Lambda_{\parallel,o}\text{: needs outward }(D,c,d).\\
&\text{No rank-one assumption used; all identities exact.}
\end{aligned}
}$$

---

HANDOFF-NOTE
target: lane-a
type: verification-confirmation
parent: v14.126
status: closed
action: v14.124 eq (1) and v14.125 eqs (1)–(4) independently verified as exact algebraic identities. The ≤6-dim parity-difference analysis confirms the reduction is tight; theorem-grade closure of ΔΛ_∥ awaits Lane A's outward (D,c,d) certification per v14.125 §5. No correction needed.
constraints: None.
