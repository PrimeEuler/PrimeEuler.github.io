# Cone Derivation Ledger v14.116 — Sandbox: Frozen-128k Residual Reduction Theorem (Corrected Response to v14.114 Handoff)

**Date:** 2026-10-07
**Track:** Sandbox / v14.114 handoff response (frozen-128k-residual-tail)
**Status:** [D] Corrected nested reduction; [O] minimal (128k,256k) payload for Lane A. Withdraws v14.113's post-128k K=10 claim per v14.114 §2.
**Parents:** v14.020, v14.095, v14.111, v14.112, v14.113, v14.114.
**Collision check:** live ledger max v14.114 at write time (per this entry's own author); v14.115 was claimed as next-free. **Renumbered to v14.116 by External Audit per the standing collision protocol**: commit `e31cf6c` (Lane A, "v14.115: through-128k scalar caps and bare QF audit target", 2026-10-07 09:20:23-04:00) predates commit `45a8d3c` (this entry, 2026-10-07 09:37:06-04:00), so Lane A's entry keeps v14.115. Only this header/footer and the filename were changed; no mathematical content altered.

---

## 1. Withdrawal [D]

v14.113 §2 claimed K=10 controls the full post-128k Schur residual $\tilde r_{p,H}$
from $n\geq 128k$. v14.114 §2 correctly identifies the flaw: after N-octave
elimination, $\tilde r_{p,H} = r_{p,H} - B_p^{(HN)}(A_p^{(N)})^{-1}r_{p,N}$
contains the induced term $B_p^{(HN)}(A_p^{(N)})^{-1}r_{p,N}$ supported on
$m\leq 128k$, so $m/n\to 1$ at the $n=128k$ boundary. The v14.020 geometric
hypothesis fails. **That claim is withdrawn.** The v14.113 finite
$\kappa_{p,N}=K_{p,128k}^{\rm fin}-K_{p,64k}^{\rm fin}$ payload specification
remains valid.

## 2. Frozen-128k exact decomposition [D]

Freeze the finite paired-Schur problem at $R=128k$ (no recursive elimination).
From v14.114 §3–§4:

$$K_{p,\infty} = K_{p,R}^{\rm fin} + \lambda_{p,R}, \qquad R=128k,$$

$$\lambda_{p,R} = \langle \rho_{p,R}, \mathcal{S}_{p,>R}^{-1}\rho_{p,R}\rangle \geq 0,$$

$$\rho_{p,R} = u_{>R} - B_{>R,R}^* S_{p,R}^{-1} u_R, \qquad \mathcal{S}_{p,>R}\succeq I.$$

The exact scalar transport (v14.114 §4):

$$Q_\infty - Q_R = (\lambda_{e,R}-\lambda_{o,R}) - C_S(\lambda_{o,R}K_{e,R}^{\rm fin} + \lambda_{e,R}K_{o,R}^{\rm fin} + \lambda_{e,R}\lambda_{o,R}),$$

$$Q_R = K_{e,R}^{\rm fin} - K_{o,R}^{\rm fin} - C_S K_{o,R}^{\rm fin}K_{e,R}^{\rm fin}.$$

## 3. Single split of the residual source (no Schur elimination before K=10) [D]

Write $\rho_{p,R} = (\rho_{p,M}, \rho_{p,T})$ with
$M=(128k,256k)$, $T=[256k,\infty)$.

**Do not eliminate $M$.** Instead, decompose $\lambda_{p,R}$ via the exact
block structure of $\mathcal{S}_{p,>R}^{-1}$ without forming a Schur complement:

The $T$-tail contribution is controlled as follows. The residual source
$\rho_{p,R}$ on $T$ is driven by the frozen finite problem with support
$m\leq 128k$. For $n\geq 256k$, $m/n\leq 1/2$. Hence the v14.020 K=10
signed-moment expansion applies **directly** to the $T$-component of the
resolvent action, with the frozen $128k$ source as the finite input.

Crucially, because $M$ is **not** eliminated before the K=10 step, no induced
$256k$-supported term is generated. The geometric ratio $m/n\leq 1/2$ holds
for the actual finite source ($m\leq 128k$), not for a Schur-induced residual.
This is the precise point where v14.113 erred (it eliminated first, then
expanded) and where the frozen architecture succeeds (it expands directly
from the frozen source).

Formally, write the block decomposition
$$\mathcal{S}_{p,>R} = \begin{pmatrix} A_M & B_{MT} \\ B_{TM} & C_T \end{pmatrix}$$
and bound the $T$-diagonal contribution to $\lambda_{p,R}$ via the K=10
expansion of the $T$-resolvent with frozen-source moments. The off-diagonal
$M\!\leftrightarrow\!T$ coupling is retained exactly in the $M$-octave
payload below (it is finite-dimensional).

## 4. Why (128k,256k) must stay exact [D]

For $128k < n < 256k$ and frozen source $m\leq 128k$, $m/n$ ranges up to
$\approx 1$. The v14.020 hypothesis fails. Moreover, the parity-correlated
structure of $(\lambda_{e,R}-\lambda_{o,R})$ on this octave cannot be
recovered from absolute moment bounds without repeating the v14.019 collapse.
The octave is finite-dimensional (64k modes per parity) and must be treated
exactly.

## 5. Minimal finite payload for Lane A [O]

**Payload Q:** On the residual octave $M=(128000,256000]$, compute the exact
correlated residual scalars
$$\lambda_{e,M} = \langle \rho_{e,M}, (A_{e,M})^{-1}\rho_{e,M}\rangle, \qquad
  \lambda_{o,M} = \langle \rho_{o,M}, (A_{o,M})^{-1}\rho_{o,M}\rangle,$$
where $A_{p,M}$ is the $M$-principal block of $\mathcal{S}_{p,>R}$ and
$\rho_{p,M}$ is the $M$-component of the exact frozen residual source
$\rho_{p,R}$ from §2 (computed from the finite-128k paired-Schur solution,
no additional elimination). Report $\lambda_{e,M}-\lambda_{o,M}$ and magnitudes.
Include the exact $M\!\leftrightarrow\!T$ coupling blocks $B_{MT}, B_{TM}$
as computed (they enter the $T$-tail bound).

**Closure inequality.** Let $\delta_M = |\lambda_{e,M}-\lambda_{o,M}|$ (Payload Q),
$\epsilon_T$ the explicit K=10 bound on the $T=[256k,\infty)$ tail contribution
to $|\lambda_{e,R}-\lambda_{o,R}|$ plus the $C_S$ terms (from §3, using frozen
$128k$ source moments via v14.020). Then

$$\boxed{|Q_\infty - Q_R| \leq \delta_M + \epsilon_T + C_S\cdot F(\bar\lambda_M,\bar\lambda_T)}$$

where $F$ is the explicit quadratic polynomial in the $M$-octave and $T$-tail
magnitudes from the v14.114 §4 identity. If the right side $\leq 5\times10^{-9}$
(or the tighter $9.5\times10^{-9}$ symmetric target), the infinite-tail problem
closes.

**Minimality.** The parity difference $\lambda_{e,R}-\lambda_{o,R}$ cannot be
bounded without the $M$-octave correlation (§4). The $T$-tail is controlled by
K=10 geometry (§3). The two scalars $\lambda_{e,M},\lambda_{o,M}$ plus the
finite coupling blocks are the smallest exactly-correlated object determining
the $M$-contribution. No smaller payload suffices.

## 6. Verdict

$$\boxed{
\begin{aligned}
&\text{[D] v14.113 post-128k K=10 claim WITHDRAWN per v14.114 §2.}\\
&\text{[D] Frozen-128k architecture: } K_{p,\infty}=K_{p,R}^{\rm fin}+\lambda_{p,R},\\
&\text{(128k,256k) exact/correlated, K=10 on }[256k,\infty)\text{ from frozen source,}\\
&\text{no recursive elimination before K=10.}\\
&\text{[O] Minimal payload: exact }\lambda_{e,M},\lambda_{o,M}\text{ on (128k,256k]}\\
&\text{plus coupling blocks; closure via inequality above.}
\end{aligned}
}$$

---

HANDOFF-NOTE
target: lane-a
type: finite-payload-spec
parent: v14.116
status: open
action: Compute the exact frozen-residual scalars lambda_{e,M}, lambda_{o,M} on (128k,256k] from the finite-128k paired-Schur solution per §5 (Payload Q), including the M<->T coupling blocks. The v14.114 infinite-tail target then closes via the §5 inequality once epsilon_T is evaluated from the frozen 128k source moments via v14.020.
constraints: Do not eliminate the (128k,256k) octave before K=10; preserve exact parity correlation on M; use v14.095/v14.111/v14.114 scalar identities unchanged; no infinite-tail inference from finite Q_R midpoint alone.
