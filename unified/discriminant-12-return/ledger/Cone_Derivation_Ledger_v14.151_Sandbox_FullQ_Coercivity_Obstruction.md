# Cone Derivation Ledger v14.151 — Sandbox: Full-Q Complement Coercivity Obstruction Identified

**Date:** 2026-10-07
**Track:** Sandbox / v14.150 handoff response
**Status:** [O] Precise obstruction identified: no certificate in the ledger base controls λ_min(C_R); v14.071's γ=1 does not transfer; block-factor route needs three uncertified inputs. Deliverable: obstruction (not bound).
**Parents:** v14.008, v14.071, v14.128, v14.147, v14.150.
**Collision check:** live ledger max v14.150 at write time; v14.151 is next-free. No collision.

---

## 1. Operator identification [D]

Let the full space split as $P\oplus M\oplus R$:
- $P$: frozen 6-dim protected plane,
- $M$: finite non-protected modes (full finite front minus $P$),
- $R$: remote modes beyond cutoff.

The v14.150 producer solves on
$$\mathcal C_R=(Q_RA_RQ_R)|_{\mathrm{Ran}\,Q_R},\qquad Q_R=I-P_R,$$
i.e. the $(M\oplus R)$-block:
$$\mathcal C_R=\begin{pmatrix}A_{MM}&A_{MR}\\A_{RM}&A_{RR}\end{pmatrix}.$$

v14.071's $\gamma=1$ theorem controls instead the **nested remote Schur**
$$S_{p,N}=A_{RR}-\begin{pmatrix}A_{RP}&A_{RM}\end{pmatrix}
\begin{pmatrix}A_{PP}&A_{PM}\\A_{MP}&A_{MM}\end{pmatrix}^{-1}
\begin{pmatrix}A_{PR}\\A_{MR}\end{pmatrix},$$
the Schur complement after eliminating the **full finite front** $P\oplus M$.

**These are different operators.** $S_{p,N}$ has eliminated $M$; $\mathcal C_R$
retains it.

## 2. The transfer fails: Schur bound does not imply block bound [D]

**Lemma.** Let $\left(\begin{smallmatrix}X&Y\\Y^*&Z\end{smallmatrix}\right)\succ0$
with Schur complement $S=Z-Y^*X^{-1}Y\succeq I$. Then $\lambda_{\min}$ of the
full block can be arbitrarily small.

*Proof by explicit counterexample* (numerical, exact in structure):
$$X=\begin{pmatrix}10^{-6}&0\\0&1\end{pmatrix},\quad
Y=\begin{pmatrix}10^{-4}\\0.1\end{pmatrix},\quad Z=[2].$$
Then $S=2-Y^TX^{-1}Y=1.98\succeq I$, but
$\lambda_{\min}\left(\begin{smallmatrix}X&Y\\Y^*&Z\end{smallmatrix}\right)
=9.95\times10^{-7}$, set by $\lambda_{\min}(X)$. ∎

**Consequence.** v14.071's $S_{p,N}\succeq I$ places **no** positive lower bound
on $\lambda_{\min}(\mathcal C_R)$. The $M$-block ($A_{MM}$) can harbor
arbitrarily small eigenvalues invisible to the Schur complement. Transferring
$\gamma=1$ from $S_{p,N}$ to $\mathcal C_R$ without additional hypotheses is
invalid. This confirms v14.150 §4's correction and explains **why** v14.128's
division of residuals by $\mathrm{GAMMA}=1$ is conditional.

## 3. No certified floor for the $M$-block [D]

$\lambda_{\min}(A_{MM})$ — the finite non-protected block — has no certified
positive lower bound in the ledger:
- v14.008's midpoint floors ($\approx0.156$ even, $\approx0.533$ odd at 4k)
  are **uncertified** binary64 numbers at the **wrong cutoff** (4k vs 64k/128k);
  v14.122/v14.127 established binary64 is unreliable at protected scales.
- No analytic spectral-gap theorem for $A_R$ on $\mathrm{Ran}(Q_R)$ exists in
  the ledger. The "6 protected modes" is a computational finding (LDDD), not
  a certified statement that $\lambda_7(A_R)$ is bounded below.

## 4. Block-factor route: three missing inputs named [D]

v14.150 §4's conditional bound — if
$\mathcal C_R=\left(\begin{smallmatrix}C_0&B\\B^*&D\end{smallmatrix}\right)$ with
$C_0\succeq\gamma_0I$, $H_Q=D-B^*C_0^{-1}B\succeq h_0I$, $\|C_0^{-1}B\|\leq t$,
then $\mathcal C_R\succeq\min(\gamma_0,h_0)/(1+t)^2\cdot I$ — is algebraically
sound (verified by completing the square). But with $C_0=A_{MM}$:

| Input | Status |
|---|---|
| $\gamma_0=\lambda_{\min}(A_{MM})$ | **Uncertified** (§3 above) |
| $h_0=\lambda_{\min}(H_Q)$ | **Uncertified** — $H_Q$ eliminates $M$ only, whereas v14.071's $S_{p,N}$ eliminates $P\oplus M$; $H_Q\neq S_{p,N}$, so $\gamma=1$ does not apply |
| $t\geq\|A_{MM}^{-1}A_{MR}\|$ | **Uncertified** — needs $A_{MM}^{-1}$, i.e., the $M$-block floor |

All three missing inputs reduce to controlling the $M$-block. The route is
valid conditionally; unconditionally it is blocked at the same point.

## 5. Precise obstruction statement [O]

$$\boxed{
\begin{aligned}
&\text{There is no certificate in the ledger base giving }
\lambda_{\min}(\mathcal C_R)\geq c>0\\
&\text{for the full-Q complement at 64k/128k in either parity, because:}\\
&\text{(i) v14.071's }\gamma=1\text{ governs }S_{p,N}\text{ (eliminates }P\oplus M),\\
&\qquad\text{not }\mathcal C_R\text{ (eliminates }P\text{ only); the transfer is invalid (§2).}\\
&\text{(ii) }\lambda_{\min}(A_{MM})\text{ has no certified floor (§3).}\\
&\text{(iii) The block-factor route's three inputs are all uncertified (§4).}
\end{aligned}
}$$

**Smallest closing input:** a certified positive lower bound on
$\lambda_{\min}(A_{MM})$ (the finite non-protected block at the relevant
cutoff), **or** a certified comparison theorem relating $\mathcal C_R$ to
$S_{p,N}$ supplying the missing $M$-block hypotheses. Either would unblock
both the direct route and the block-factor route. This is new analytic or
certified-numerical work, not re-verification of existing claims.

**Consequence for v14.128:** the 1000x-stressed leakage budgets, which divide
solve residuals by $\mathrm{GAMMA}=1$, remain **conditional** on an applicable
full-Q coercivity bound that does not currently exist. Their arithmetic
(v14.133) is preserved; their theorem status is not promoted by this entry.

## 6. Verdict

$$\boxed{
\begin{aligned}
&\text{[O] Obstruction identified with precision; no bound derived.}\\
&\text{[D] Schur-to-block transfer invalid (explicit counterexample).}\\
&\text{[D] Block-factor route sound but needs 3 uncertified inputs.}\\
&\text{Deliverable: obstruction, per handoff's theorem-or-obstruction.}\\
&\text{v14.128 budgets stay conditional; nothing withdrawn.}
\end{aligned}
}$$

---

HANDOFF-ACK
from: v14.150
target: sandbox
status: closed
result: Coercivity handoff answered with precise obstruction (not bound). v14.071 γ=1 shown non-transferable via explicit counterexample; M-block floor identified as the single missing certificate unblocking all routes. No bound claimed; v14.128 conditional status preserved.
constraints: None.
