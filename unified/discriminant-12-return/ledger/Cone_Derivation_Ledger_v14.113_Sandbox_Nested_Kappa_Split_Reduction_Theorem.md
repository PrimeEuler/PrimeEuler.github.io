# Cone Derivation Ledger v14.113 — Sandbox: Nested 64k/128k κ-Split Reduction Theorem (Response to v14.112 Handoff)

**Date:** 2026-10-07
**Track:** Sandbox / v14.112 handoff response (nested-kappa-tail-reduction)
**Status:** [D] Exact nested-split reduction theorem; [O] minimal finite payload identified for Lane A. No direct 5e-9 bound claimed — the 64k–128k octave must be computed exactly/correlated by Lane A.
**Parents:** v14.020, v14.095, v14.111, v14.112.
**Collision check:** live ledger max v14.112 at write time; v14.113 is next-free. No collision.

---

## 1. Exact nested decomposition [D]

From v14.112 §2, with F=(32k,64k], G=(64k,∞), N=(64k,128k), H=[128k,∞):

$$\kappa_p = \kappa_{p,N} + \kappa_{p,H}, \qquad p\in\{e,o\},$$

where
$$\kappa_{p,N} = \langle r_{p,N}, (A_p^{(N)})^{-1} r_{p,N}\rangle \geq 0,$$
$$\kappa_{p,H} = \langle \tilde r_{p,H}, \mathcal{S}_{p,H}^{-1} \tilde r_{p,H}\rangle \geq 0,$$
$$\mathcal{S}_{p,H} \succeq I.$$

The nonnegativity follows from $A_p^{(N)} \succ 0$ (finite principal block of the
positive far Schur operator) and $\mathcal{S}_{p,H} \succeq I$ (promoted remote floor).

## 2. K=10 legality on H [D]

For every retained source mode $m \leq 64000$ and every $n \geq 128000$:

$$\frac{m}{n} \leq \frac{1}{2}.$$

Hence the v14.020 signed-moment geometric expansion (Eqs 1–2) applies verbatim
on H with $N=64000$. The remainder after $K=10$ signed channels satisfies

$$|\tilde R_{10}(n)| \leq \frac{A_{10}}{n^{23}} + \frac{B_{10}}{n^{24}},$$

with $A_{10}, B_{10}$ the explicit source-moment constants from v14.020 §3
(computed from the finite $m\leq 64k$ source moments $S^z_{22}, S_{23}$).

In particular, the $H$-tail is a genuine geometric series with ratio $\leq 1/2$;
no low-order absolute $C_\rho$ is used.

## 3. Reduction of the scalar target [D]

From v14.095/v14.111:

$$Q_\infty - Q_F = (\kappa_e-\kappa_o) - C_S(\kappa_o K_{e,F} + \kappa_e K_{o,F} + \kappa_e\kappa_o).$$

Insert $\kappa_p = \kappa_{p,N}+\kappa_{p,H}$:

$$\begin{aligned}
Q_\infty-Q_F &= (\kappa_{e,N}-\kappa_{o,N}) + (\kappa_{e,H}-\kappa_{o,H}) \\
&\quad - C_S\big[(\kappa_{o,N}+\kappa_{o,H})K_{e,F} + (\kappa_{e,N}+\kappa_{e,H})K_{o,F} \\
&\qquad\qquad + (\kappa_{e,N}+\kappa_{e,H})(\kappa_{o,N}+\kappa_{o,H})\big].
\end{aligned}$$

Let $\bar\kappa = \max_{p,N/H} \kappa$. Since all $\kappa \geq 0$ and
$K_{e,F},K_{o,F} \approx 8.8\times 10^{-7}$ (v14.111), $C_S \approx 639.83$:

$$|Q_\infty-Q_F| \leq |\kappa_{e,N}-\kappa_{o,N}| + |\kappa_{e,H}-\kappa_{o,H}| + C_S\cdot E(\bar\kappa),$$

where $E(\bar\kappa) = 2\bar\kappa(K_{e,F}+K_{o,F}) + \bar\kappa^2$ bounds the
parenthesized $C_S$ terms.

## 4. Why the N-octave cannot be K=10'd [D]

For $64k < n < 128k$ and $m$ up to $64k$, the ratio $m/n$ ranges up to $\approx 1$.
The v14.020 geometric hypothesis $m/n \leq 1/2$ fails. Any attempt to apply
the signed-moment expansion on N would require absolute-bounding the
non-convergent geometric tail — precisely the v14.019 failure mode that v14.020
was built to avoid.

Therefore N must be treated exactly/correlated via the nested Schur formula.
No analytic shortcut exists without losing the parity correlation that the
entire $\eta_o-\eta_e$ program depends on.

## 5. Minimal finite payload for Lane A [O]

The infinite-tail problem reduces exactly to the following finite computation:

**Payload P:** On the octave $N=(64000,128000]$, compute the exact nested-Schur
scalars
$$\kappa_{e,N} = \langle r_{e,N}, (A_e^{(N)})^{-1} r_{e,N}\rangle, \qquad
  \kappa_{o,N} = \langle r_{o,N}, (A_o^{(N)})^{-1} r_{o,N}\rangle,$$
via the v14.112 §2 block Gaussian elimination (eliminate $F$, retain $N$
exactly, form the Schur complement). Report the correlated difference
$\kappa_{e,N}-\kappa_{o,N}$ and the individual magnitudes.

**Closure inequality.** Let $\delta_N = |\kappa_{e,N}-\kappa_{o,N}|$ (from Payload P),
and let $\epsilon_H$ be the explicit K=10 bound on
$|\kappa_{e,H}-\kappa_{o,H}| + C_S\cdot E_H$ from §2 (computable from the
$64k$-source moments via v14.020 Eqs 1–3). Then

$$\boxed{|Q_\infty-Q_F| \leq \delta_N + \epsilon_H + C_S\cdot E_N(\bar\kappa_N)}$$

where $E_N$ uses only the $N$-octave $\kappa$ values from Payload P.
If $\delta_N + \epsilon_H + C_S\cdot E_N \leq 5\times 10^{-9}$, the v14.112
target closes.

**Why this is minimal.** Any bound on $|Q_\infty-Q_F|$ must control the
parity-correlated difference $\kappa_e-\kappa_o$. The $H$-part is controlled
by K=10 geometry (§2). The $N$-part has no convergent geometric expansion
(§4), so it must be computed exactly. The two scalars $\kappa_{e,N},
\kappa_{o,N}$ (32k modes per parity, finite-dimensional, exactly correlated
via the nested Schur complement) are the smallest object carrying the needed
parity information. No smaller payload suffices without reintroducing the
absolute-$C_\rho$ failure.

## 6. Verdict

$$\boxed{
\begin{aligned}
&\text{[D] Nested split } \kappa_p=\kappa_{p,N}+\kappa_{p,H} \text{ is exact;}\\
&\text{K=10 is legal on } H=[128k,\infty) \text{ with } m/n\leq 1/2.\\
&\text{[D] } N=(64k,128k) \text{ cannot use K=10 (ratio up to 1); must stay exact.}\\
&\text{[O] Minimal payload: Lane A computes } \kappa_{e,N},\kappa_{o,N} \text{ exactly}\\
&\text{on the 64k--128k octave via nested Schur; closure via inequality above.}\\
&\text{No 5e-9 bound claimed here — the octave computation is Lane A's.}
\end{aligned}
}$$

---

HANDOFF-NOTE
target: lane-a
type: finite-payload-spec
parent: v14.113
status: open
action: Compute the exact nested-Schur scalars kappa_{e,N}, kappa_{o,N} on the (64k,128k] octave per v14.112 §2 (eliminate F=(32k,64k], retain N exactly, form Schur complement to H). Report kappa_{e,N}-kappa_{o,N} and magnitudes. The v14.112 5e-9 target then closes via the §5 inequality once the K=10 H-tail epsilon_H is evaluated from the 64k source moments.
constraints: Preserve exact parity correlation on N; do not replace N by K=10 or absolute bounds; use the v14.095/v14.111 scalar identities unchanged.
