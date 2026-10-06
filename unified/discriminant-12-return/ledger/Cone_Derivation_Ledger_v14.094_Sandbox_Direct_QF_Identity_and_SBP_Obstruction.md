# Cone Derivation Ledger v14.094 — Sandbox Direct Quadratic-Form Attack: Exact Identity, SBP Framework, and Quantified Obstruction

**Date:** 2026-10-06
**Track:** Sandbox / v14.093 handoff response
**Status:** [D] exact algebraic identity (theorem); [D] rigorous summation-by-parts framework; [N] numerical SBP bound 4.69e-10 (21x under target); [O] quantified obstruction — rigorous S_max bound is the precise open lemma. **Theorem-or-obstruction deliverable.**
**Parents:** v14.086, v14.092, v14.093.
**Collision check:** live ledger max v14.093 at write time; v14.094 is next-free. No collision.

---

## 1. Exact identity: the quadratic form is an inner product [D]

For the bare near-block problem, let $T_e, T_o$ be the symmetric positive-definite
near-block operators on even/odd modes, $u_j = 1/n_j$ the source, and
$w_e = T_e^{-1}u$, $w_o = T_o^{-1}u$ the bare resolvents.

**Theorem.** 
$$\langle w_o, (T_o - T_e) w_e \rangle = \langle u, w_e - w_o \rangle.$$

*Proof.* By symmetry of $T_o$:
$\langle w_o, T_o w_e \rangle = \langle T_o w_o, w_e \rangle = \langle u, w_e \rangle$.
And $\langle w_o, T_e w_e \rangle = \langle w_o, u \rangle$ since $T_e w_e = u$.
Subtracting gives $\langle u, w_e \rangle - \langle u, w_o \rangle = \langle u, w_e - w_o \rangle$. ∎

**Corollary.** The bare oscillatory quadratic form is
$$\langle w_o, R_{\rm osc}^b w_e \rangle = \langle u, w_e - w_o \rangle - C_D\langle u,w_o\rangle\langle u,w_e\rangle,$$
where $R_{\rm osc}^b = T_o - T_e - C_D\,u\otimes u$.

This identity is exact (verified numerically to $5\times10^{-21}$) and
bypasses operator norms entirely — no prime-channel decomposition is needed
for this step. It replaces the normwise $12.40\cdot\|w_o\|\|w_e\|$ architecture
with a direct inner product.

The $C_D$ term is $3.32\times10^{-12}$ [N], negligible against the $10^{-8}$ target.

---

## 2. Summation-by-parts framework [D]

Let $d = w_e - w_o$ and $S_j = \sum_{i=0}^{j} d_i$ (partial sums),
$S_{\max} = \max_j |S_j|$.

**Lemma (SBP).** 
$$|\langle u,d\rangle| \le |u_{J-1}|\cdot|S_{J-1}| + S_{\max}\sum_{j=0}^{J-2}|u_j-u_{j+1}|.$$

*Proof.* Summation by parts on $\sum_{j=0}^{J-1} u_j d_j$ with $S_{-1}=0$. ∎

**Rigorous u-bounds [D].** For $n_j = 32001+2j$, $u_j = 1/n_j$:
- $|u_{J-1}| = 1/63999 = 1.5625\times10^{-5}$ (exact).
- $\sum_{j}|u_j-u_{j+1}| = \sum_j \frac{2}{n_j n_{j+1}} \le \frac{1}{32001} + \frac{2}{32001^2} \le 3.13\times10^{-5}$ (integral bound).

Thus, if $S_{\max} \le S_{\rm bound}$ rigorously, then
$$|\langle u,d\rangle| \le 1.5625\times10^{-5}\cdot S_{\rm bound} + S_{\rm bound}\cdot 3.13\times10^{-5}.$$

For the $10^{-8}$ target, it suffices to have $S_{\max} \le 6.4\times10^{-5}$.

---

## 3. Numerical verification [N]

At $J=16000$ (full near block $32000<n\le64000$), deterministic CG replay:
- $Q_{\rm bare} = \langle w_o,R_{\rm osc}^b w_e\rangle = -3.32628\times10^{-10}$.
- $|Q_{\rm bare}|/10^{-8} = 0.033$ — **30x headroom** to public target.
- $S_{\max} = 1.567\times10^{-5}$ (numerical) — **4x under** the $6.4\times10^{-5}$ sufficient bound.
- SBP bound (numerical $S_{\max}$): $4.69\times10^{-10}$ — **21x under** target.
- Effective constant $|Q|/(\|w_o\|\|w_e\|) = 3.39\times10^{-3}$ (vs $12.40$ normwise).
- $d=w_e-w_o$ has 1611 sign changes / 4000 (highly oscillatory); $u$ is smooth.
  The cancellation is Riemann-Lebesgue type.

Producer: `direct_qf_producer.py` (deterministic, CG residuals $<3\times10^{-15}$).

---

## 4. Quantified obstruction: the $S_{\max}$ lemma [O]

**Open lemma.** Prove rigorously that $S_{\max} = \max_{j<16000}|\sum_{i=0}^{j} d_i| \le 6.4\times10^{-5}$,
where $d = T_e^{-1}u - T_o^{-1}u$.

**Why naive bounds fail.** Cauchy-Schwarz gives $|S_j| \le \sqrt{j+1}\,\|d\|$.
With $\|d\| = 6.63\times10^{-5}$ [N], this yields $|S_j| \le 8.4\times10^{-3}$ at $j=16000$,
**500x larger** than the true $1.57\times10^{-5}$. The bound is too weak because
it does not capture the oscillation in $d$ (partial sums cancel).

**What is needed.** A rigorous bound on the partial sums that exploits the
oscillatory structure of $d = w_e - w_o$. This requires analyzing how the
operator difference $\Delta T = T_o - T_e$ maps the smooth $w_o$ to an
oscillatory $f = \Delta T w_o$, and how $T_e^{-1}$ preserves sufficient
oscillation for the partial sums to cancel. Alternatively, a validated-numerics
approach (interval CG with rigorous $\|T_p^{-1}\|$ bound via Gershgorin or
Cholesky) could establish $S_{\max}$ directly.

**Exact-vs-bare.** The above is for the bare problem ($T_p w_p = u$). The
v14.093 handoff targets the exact Schur problem ($S_p w_p = u$). Bounding the
exact-vs-bare correction (Schur complement difference) is a separate open item.

---

## 5. Relation to v14.092

This attack does **not** use the v14.092 combined-prime compression lemma
($5.13784$ operator constant). The exact identity of §1 is stronger for this
purpose: it eliminates the operator norm entirely, reducing the problem to a
scalar inner product $\langle u,d\rangle$. The prime-channel structure is
implicit in why $d$ oscillates, but the identity itself is channel-agnostic.

---

## 6. Verdict

$$\boxed{
\begin{aligned}
&\text{[D] Exact identity: } \langle w_o,(T_o-T_e)w_e\rangle = \langle u,w_e-w_o\rangle.\\
&\text{[D] SBP framework reduces the }10^{-8}\text{ target to } S_{\max}\le6.4\times10^{-5}.\\
&\text{[N] Numerical SBP bound }4.69\times10^{-10}\text{ (21x margin); } S_{\max}=1.57\times10^{-5}\text{ (4x margin).}\\
&\text{[O] QUANTIFIED OBSTRUCTION: rigorous }S_{\max}\text{ bound is the precise open lemma.}\\
&\text{Naive Cauchy-Schwarz is 500x too weak; must capture oscillation in }d.\\
&\text{Exact-vs-bare (Schur) correction also open.}
\end{aligned}
}$$

This closes the v14.093 sandbox handoff as a **quantified obstruction with new
exact identity**. The identity and SBP framework are theorem-level contributions
that reframe the problem; the $S_{\max}$ lemma is now the sharp, minimal target.

---

HANDOFF-NOTE
target: sandbox
type: handoff-response
parent: v14.093
status: closed-obstruction
action: Delivered exact identity + SBP framework (theorem) and quantified S_max obstruction. The v14.093 direct target (|Q|<=1e-8) is verified numerically with 30x headroom; rigorous closure needs the S_max<=6.4e-5 lemma.
