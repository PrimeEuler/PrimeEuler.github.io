# Lemma G/W Attack for the q=7-Dominated Oscillatory Quadratic Form

**Task:** Sandbox CONSTRUCTION handoff v14.083 (type: analytic-lemma).
**Date:** 2026-10-06
**Status:** Complete — SHARPENED QUANTIFIED OBSTRUCTION (no theorem Lemma G/W;
exact obstruction factor and precise sub-lemma identified).
**Scope:** One-sided 32k framework, margin M = 1.37456583285676e-5.
Lane A owns μ_{32k} (not touched). No repo/ledger writes. No theorem promotion.

**Conventions:** [D]=derived, [N]=numerical, [I]=inference, [O]=open/gap.
**Producer:** `lemma_gw_producer.py` (deterministic, numpy only, SHA-256 verified).
All [N] vector norms are bare-operator, finite-window (J=300); the analytic
constants are [D].

**Parents:** v14.079 (exact R_osc decomposition, Lemma G/W statements),
v14.081 (one-sided 32k framework), v14.083 (handoff, 64k payload).

---

## 0. Verdict

**SHARPENED QUANTIFIED OBSTRUCTION.** Neither Lemma G nor Lemma W is proved.
The best rigorous bound is

$$
\boxed{
|\langle w_o, R_{osc}^b w_e \rangle|
\;\le\;
12.40 \cdot \|w_o\|\,\|w_e\|
\quad\text{[D]}
}
$$

which at N=32k evaluates (with [N] vector norms) to
A·bound = 2.71× the one-sided margin M. The obstruction factor is **2.71×**,
down from v14.079's 7× (symmetric) because the one-sided margin is ~40×
looser — but the bound still does not fit.

The three attack angles were attempted in order (§§1–3); each hits a
precise, named sub-obstruction. The exact sub-lemma that would close the
gap is stated in §4: a joint constant ≤ 4.1 (3× improvement over 12.40).

This does **not** close the one-sided 32k R_osc gap — it sharpens v14.079's
obstruction from "7× over (symmetric)" to "2.71× over (one-sided)" and
locates the remaining looseness exactly.

---

## 1. Attack 1: Sharpened Toeplitz/Hankel [D/N]

### 1.1 Exact q=7 slow-phase structure [D]

From v14.079 §1.3, the q=7 off-diagonal leading term (sum-of-products +
paired difference + δ_7 reduction) is exactly

$$
(R_7^{\mathrm{off,lead}})_{jk}
= -C_7 \cos\big((N+\tfrac32+j+k)\delta_7\big)\,(T^{(\delta_7)})_{jk},
$$

where C_7 = 4c\,w_7\sin(\phi_7/2) ≈ 1.8706 (c=2/π),
δ_7 = π(1−log7/2) ≈ 0.0849641392, and
$(T^{(\delta)})_{jk} = \sin((j-k)\delta)/(2(j-k))$ is the sinc-Toeplitz.

*Derivation.* The paired difference gives
$[K^{(m)}-K^{(n)}]^{\mathrm{lead}}_{jk}
= -2\sin(\phi_7/2)\sin((N+\tfrac32+j+k)\phi_7)\sin((j-k)\phi_7)/(2(j-k))$.
Using φ_7 = π−δ_7:
- $\sin((j-k)\phi_7) = -(-1)^{j-k}\sin((j-k)\delta_7)$,
- $\sin((N+\tfrac32+j+k)\phi_7) = -(-1)^{j+k}\cos((N+\tfrac32+j+k)\delta_7)$
  (N even).
The $(-1)^{2j}=1$ cancellation leaves the stated form. ∎

### 1.2 Toeplitz symbol lemma is sharp [D]

**Lemma T** (v14.079 §6): $\|T^{(\delta)}\|_2 \le \pi/2$, with equality in
the bi-infinite limit (the symbol is $(\pi/2)\cdot\mathbf{1}_{|\omega|<\delta}$,
a projection). **This bound cannot be improved via operator norm** — π/2 is
exact, not an estimate.

The (j+k)-oscillation is removed by unitary diagonal modulation:
$\cos((N+\tfrac32+j+k)\delta_7) = \mathrm{Re}[e^{i(N+3/2)\delta_7}
e^{ij\delta_7}e^{ik\delta_7}]$, and $\tilde w_p[j]=e^{ij\delta_7}w_p[j]$
satisfies $\|\tilde w_p\|=\|w_p\|$. Hence [D]:

$$
|\langle w_o, R_7^{\mathrm{off,lead}} w_e\rangle|
\le C_7 \cdot \tfrac{\pi}{2}\cdot \|w_o\|\|w_e\|
= 2.940 \cdot \|w_o\|\|w_e\|.
$$

The constant 2.940 = $c\cdot 2w_7\cdot\pi\cdot\sin(\phi_7/2)$ is **exact**
given the symbol lemma; no sharpening is available at the operator-norm level.

### 1.3 Quantification vs one-sided 32k margin [D/N]

At N=32k (bare, J=300): $\|w_o\|\|w_e\| = 3.7281\times10^{-9}$ [N].
- Bound: $2.940 \times 3.7281\mathrm{e}{-9} = 1.0968\mathrm{e}{-8}$.
- A·bound = $804 \times 1.0968\mathrm{e}{-8} = 8.8182\times10^{-6}$.
- **A·bound / M = 0.6415** (64% of the one-sided margin).

The existing lemma "fits" (< M) for the q=7 off-diagonal leading term
alone, but consumes 64%, leaving only 36% for: four other q-channels'
off-diagonals, all five diagonals, second identity terms, smooth remainders,
and the Schur oscillatory remainder. **Quantified: the lemma fits the
channel but the channel budget is exhausted.**

For Lemma G's target constant 0.35 (8.4× improvement): would give
64%/8.4 = 7.6% of M. For "comfortable" (≤20% of M): need 3.2×
improvement (constant ≤ 0.92).

### 1.4 Other q-channels: same symbol lemma, no resonance [D]

For q∈{2,3,4,5}, the identical derivation (without δ-reduction) gives

$$
|\langle w_o, R_q^{\mathrm{off,lead}} w_e\rangle|
\le C_q \|w_o\|\|w_e\|,\quad
C_q = 4\,w_q\,|\sin(\phi_q/2)|,
$$

with C_2=1.015, C_3=1.928, C_4=1.228, C_5=2.745 [D].
Sum: $\sum_q C_q = 9.855$.

**The q-dependent (j+k) modulations $e^{ij\phi_q}$ prevent a joint
Toeplitz bound**: the modulated vectors $\tilde w^{(q)}_p[j]=e^{ij\phi_q}w_p[j]$
differ by q, so the five Toeplitz operators cannot be combined before
taking norms. Summing absolute channel bounds is the only available
rigorous route, giving $9.855\|w_o\|\|w_e\|$.

### 1.5 Second identity terms: negligible [D/N]

The second sum-of-products term carries an extra $1/(\nu_j+\nu_k)$.
For the paired difference, $|[K^{(m)}-K^{(n)}]^{2\mathrm{nd}}_{jk}|
\le 1/(2N^2) + \phi_q/(2N)$ [D]. Numerically (J=300), the q=7
second-term operator norm is $3.13\times10^{-3}$ [N], ~1000× below the
leading constant 2.94. All-q total ≤ 0.02·‖w_o‖‖w_e‖ [D/N], contributing
< 0.1% of M. **Negligible; not the obstruction.**

### 1.6 Diagonal channels: crude max bound [D]

$(R_q^{\mathrm{diag,cos}})_{jj}
= -2w_q(2-\log q)\sin(\phi_q/2)\sin(A_q+j\theta_q)$ [D, v14.079 §1.2].
Hence [D]:

$$
|\langle w_o,R_q^{\mathrm{diag,cos}}w_e\rangle|
\le D_q\|w_o\|\|w_e\|,\quad
D_q = 2w_q|2-\log q|\,|\sin(\phi_q/2)|,
$$

D_2=0.664, D_3=0.869, D_4=0.377, D_5=0.536, D_7=0.080. Sum: 2.525.
The $R_q^{\mathrm{diag,sin}}$ pieces are O(1/n) and bounded similarly;
total diagonal ≤ 2.6·‖w_o‖‖w_e‖ [D].

**This bound discards the diagonal oscillation entirely** (uses
$|\sin|\le1$). The true diagonal values are ~2500× smaller [N].
Improving it requires SBP, which needs w-smoothness (§2).

---

## 2. Attack 2: Self-consistent w equation [D/O]

### 2.1 Two-scale split [D]

Write $w_p = a_p + r_p$ with $a_p = D_p^{-1}u_p$ explicit
($a_p[j] = 1/(n_j d_{n_j})$, smooth) and $r_p = w_p-a_p$ the ripple.
From $S_p w_p = u_p$ and $D_p a_p = u_p$ [D]:

$$
S_p r_p = -E_p a_p,\qquad
r_p = -S_p^{-1}E_p a_p,\qquad
\|r_p\| \le \|E_p a_p\|\quad(\gamma_N=1).
$$

Numerically $\|r_p\|/\|w_p\| \approx 0.094$ at 32k [N], but no rigorous
bound on $\|E_p a_p\|$ is established (requires $\|D_p^{-1}E_p\|_2<1$
for Neumann, not proved).

### 2.2 Small-divisor obstruction [D]

To bound $\langle a_o, R_7^{\mathrm{off,lead}} a_e\rangle$ via SBP/Fourier:
$a_p[j] \approx 1/((N+2j)\log((N+2j)/4))$ satisfies $a_p\in\ell^2$ but
$a_p\notin\ell^1$ ($\sum_j 1/(j\log j)$ diverges). Hence the DTFT
$\tilde a_p(\Omega)$ has a non-integrable singularity at Ω=0, and the
SBP bound $|\tilde a_p(\Omega)|\le V(a_p)/|2\sin(\Omega/2)|$ blows up
exactly where the Toeplitz symbol is supported. **The two-scale SBP
route hits a genuine small-divisor obstruction.** This is Lemma W's
content: a usable modulus for $r_p$ (not just $\|r_p\|/\|w_p\|\approx0.1$)
is needed, resolving the ripple's modulated-smooth structure at the
combined frequencies $\theta_q\pm\phi_{q'}$.

### 2.3 Verdict on Attack 2

The w-equation yields the exact identity $S_p r_p = -E_p a_p$ [D], but
converting it into a usable bound requires either (i) a rigorous
$\|D_p^{-1}E_p\|_2 \le \rho<1$ (not established), or (ii) Lemma W's
modulus of continuity for $r_p$. **Attack 2 reduces to Lemma W; not proved.**

---

## 3. Attack 3: q-channel correlation [D/O]

The five q-channels' true values at 32k exhibit sign cancellation [N],
but the signs are J-delicate and N-dependent (v14.079 §8: finite sections
oscillate; conditionally convergent). No sign is provable.

A joint bound would require combining the five modulated Toeplitz
operators $\sum_q C'_q M_{f_q} T^{(\phi_q)}$ before taking norms, but
the q-dependent modulations $M_{f_q}$ (diagonal unitaries $e^{ij\phi_q}$)
do not commute with each other or admit a common diagonalization.
**No joint bound tighter than $\sum_q|\cdot|$ is available without
Lemma G's correlation estimate.** Attack 3 reduces to Lemma G; not proved.

---

## 4. Sharpened obstruction: exact factor and sub-lemma [D/N]

### 4.1 Best rigorous bound

Combining §§1.4–1.6 (all [D]):

$$
\boxed{
|\langle w_o, R_{osc}^b w_e\rangle|
\le \big(\underbrace{9.855}_{\sum C_q}
      + \underbrace{2.525}_{\sum D_q}
      + \underbrace{0.02}_{\text{2nd terms}}\big)
      \|w_o\|\|w_e\|
= 12.40\,\|w_o\|\|w_e\|.
}
$$

(Smooth remainders ≤ 0.1% M [D, v14.079 §7]; Schur oscillatory remainder
[O, Lane A's finite data].)

### 4.2 Obstruction factor [N]

At N=32k, $\|w_o\|\|w_e\| = 3.7281\times10^{-9}$ [N, bare J=300]:

$$
12.40 \times 3.7281\mathrm{e}{-9} = 4.623\mathrm{e}{-8},\quad
A_{\max}\times = 804 \times 4.623\mathrm{e}{-8} = 3.717\mathrm{e}{-5}.
$$

$$
\boxed{
\frac{A_{\max}\cdot\text{bound}}{M}
= \frac{3.717\times10^{-5}}{1.3746\times10^{-5}}
= \mathbf{2.70\times}
}
$$

**The best rigorous bound exceeds the one-sided 32k margin by 2.70×.**
(True value: 0.6% of M [N]; the bound is 450× loose.)

### 4.3 Where the 2.70× lives [D/N]

| Piece | Rigorous constant | A·bound/M | True A·|·|/M [N] | Looseness |
|---|---|---|---|---|
| q=7 offdiag lead | 2.940 | 0.641 | 0.0055 | 116× |
| q=2,3,4,5 offdiag | 6.915 | 1.508 | ~0.0004 | ~4000× |
| Diagonals (all q) | 2.525 | 0.551 | ~0.0001 | ~5000× |
| 2nd identity terms | 0.02 | 0.004 | <0.0001 | — |
| **Total** | **12.40** | **2.70** | **0.006** | **450×** |

The dominant looseness is the off-diagonal $\sum C_q$ (1.51× M for
q≠7 alone) and the diagonal $\sum D_q$ (0.55× M) — both discard
oscillation/w-vector structure that the true values exploit.

### 4.4 Precise sub-lemma that closes it [O]

**Sub-lemma S.** Prove, for the bare paired operators at N=32k,

$$
|\langle w_o, R_{osc}^b w_e\rangle| \le 4.1\,\|w_o\|\|w_e\|.
$$

Then $A_{\max}\cdot 4.1 \cdot 3.7281\mathrm{e}{-9}
= 1.23\times10^{-5} = 0.89\times M$ [D/N]: **fits**.

Sufficient (stronger) form:
- (S-off) $|\langle w_o,\sum_q R_q^{\mathrm{off,lead}} w_e\rangle|
  \le 3.0\,\|w_o\|\|w_e\|$ (vs 9.86; 3.3× improvement), **and**
- (S-diag) $|\langle w_o,\sum_q R_q^{\mathrm{diag}} w_e\rangle|
  \le 1.1\,\|w_o\|\|w_e\|$ (vs 2.53; 2.3× improvement).

Lemma G (constant 0.35 for q=7, 8.4× improvement) would imply (S-off)
for the dominant channel; Lemma W (modulus for $r_p$) would enable
the SBP route to (S-diag) and the two-scale route to (S-off). Either
original lemma suffices; the sub-lemma is the minimal sufficient form.

### 4.5 What was ruled out [D]

- Improving $\|T^{(\delta)}\|_2\le\pi/2$: **impossible** (sharp).
- SBP against $w_p$: **doomed** (v14.079 §4: ripple 54% of variation).
- SBP against $a_p$: **blocked** ($a_p\notin\ell^1$, small divisors).
- Joint q-Toeplitz bound: **blocked** (non-commuting modulations).
- Sign-based cancellation: **unprovable** (J-delicate).

---

## 5. Files

- `~/workspace/d12/lemma_gw_producer.py` — deterministic producer:
  phase constants (φ_q, θ_q, δ_7, denominators), C_q/D_q tables,
  Toeplitz-symbol verification, second-term operator norms,
  [N] vector norms at 32k, the 2.70× obstruction computation,
  sub-lemma target check. SHA-256 of key outputs printed.
- `~/workspace/d12/lemma_gw_bound.md` — this derivation.

No repo/ledger writes. Report to parent with verdict.

---

## 6. Result

$$
\boxed{
\begin{aligned}
&\text{SHARPENED QUANTIFIED OBSTRUCTION for Lemma G/W under the one-sided 32k framework:}\\
&\text{Best rigorous bound } |\langle w_o,R_{osc}^b w_e\rangle| \le 12.40\,\|w_o\|\|w_e\|\ \text{[D]}\\
&\text{exceeds the }1.37\times10^{-5}\text{ margin by exactly } \mathbf{2.70\times}
\text{ [D/N].}\\
&\text{Toeplitz symbol lemma is sharp (no improvement via operator norm);}\\
&\text{q=7 channel alone fits at 64\% of M, but }\sum_q|\cdot|\text{ over all channels does not.}\\
&\text{Two-scale and q-correlation attacks reduce to Lemma W / Lemma G respectively.}\\
&\text{Precise sub-lemma: joint constant }\le 4.1\ (3\times\text{ improvement});\\
&\text{sufficient via (S-off)}\le3.0\text{ and (S-diag)}\le1.1.\\
&\text{Lane A's }\mu_{32k}\text{ and the Schur oscillatory remainder remain open separately.}
\end{aligned}
}
$$
