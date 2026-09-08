# Cone Derivation Ledger v13.318 — Full Defect-Moment Boundary/Interior Hierarchy

## Scope

This checkpoint extends v13.316 from the first shell-defect moment to the entire positive moment family

\[
\mathcal S_\alpha(n)=\sum_{k:r_k\ne0}\left(\frac{r_k}{k}\right)^\alpha,
\qquad \alpha>0,
\]

with

\[
r_k=n-k\left\lfloor\frac nk\right\rfloor=n-Y_k^2.
\]

Companion note:

`research-notes/Full_Moment_Boundary_Interior_Defect_Hierarchy.md`

The main result is that the terminal-boundary / strict-descent-interior split of v13.314-v13.316 persists exactly for every positive real moment. Positive integer moments retain the generalized-harmonic quotient-block expansion. No new divisor-problem asymptotic, primality theorem, factorization algorithm, RH/GRH, spectral, positivity, or Fredholm claim is made.

---

## 1. Quotient-block ladder

For each distinct quotient value \(q\), let

\[
L_q=\left\lfloor\frac{n}{q+1}\right\rfloor+1,
\qquad
R_q=\left\lfloor\frac nq\right\rfloor,
\qquad
m_q=R_q-L_q+1,
\]

and

\[
s_q=n-qR_q=n\bmod q.
\]

For every \(k\in[L_q,R_q]\),

\[
\boxed{\Delta_k=n-kq=s_q+q(R_q-k)}.
\]

Thus the endpoint \(k=R_q\) is the unique non-descending terminal state, while every \(k<R_q\) is a strict Euclidean-descent state.

---

## 2. Positive real moments

Define

\[
\mathcal S_{\alpha,q}(n)
=\sum_{k=L_q}^{R_q}\left(\frac{\Delta_k}{k}\right)^\alpha.
\]

Separating the endpoint gives

\[
\boxed{\mathcal S_{\alpha,q}=B_{\alpha,q}+I_{\alpha,q}},
\]

where

\[
\boxed{
B_{\alpha,q}(n)
=\left(\frac{s_q}{R_q}\right)^\alpha
=\left(\frac{n\bmod q}{\lfloor n/q\rfloor}\right)^\alpha,
}
\]

and

\[
\boxed{
I_{\alpha,q}(n)
=\sum_{k=L_q}^{R_q-1}\left(\frac nk-q\right)^\alpha.
}
\]

Hence globally

\[
\boxed{\mathcal S_\alpha(n)=B_\alpha(n)+I_\alpha(n)},
\]

with

\[
\boxed{
B_\alpha(n)
=\sum_{q\in Q(n)}
\left(\frac{n\bmod q}{\lfloor n/q\rfloor}\right)^\alpha,
}
\]

and

\[
\boxed{
I_\alpha(n)
=\sum_{q\in Q(n)}\sum_{k=L_q}^{R_q-1}
\left(\frac nk-q\right)^\alpha.
}
\]

Contact endpoints vanish automatically because \(s_q=0\) when \(q\mid n\).

---

## 3. Zeroth-moment limit

For positive defects, \(x^\alpha\to1\) as \(\alpha\to0^+\). Zero defects remain zero for every \(\alpha>0\). Therefore

\[
\boxed{\lim_{\alpha\to0^+}B_\alpha(n)=Q_n-\tau(n)},
\]

because the nondividing quotient blocks are exactly the positive-defect terminal states.

Every interior state has positive defect, so

\[
\boxed{
\lim_{\alpha\to0^+}I_\alpha(n)
=\sum_{q\in Q(n)}(m_q-1)
=n-Q_n.
}
\]

Hence

\[
\boxed{
\lim_{\alpha\to0^+}\mathcal S_\alpha(n)
=(Q_n-\tau(n))+(n-Q_n)
=n-\tau(n).
}
\]

Thus the support decomposition of v13.315 is exactly the \(\alpha\to0^+\) limit of the same boundary/interior moment decomposition.

---

## 4. First moment

At \(\alpha=1\),

\[
B_1(n)=\sum_{q\in Q(n)}\frac{n\bmod q}{\lfloor n/q\rfloor},
\]

and

\[
I_1(n)=\sum_{q\in Q(n)}\left[n(H_{R_q-1}-H_{L_q-1})-q(m_q-1)\right].
\]

Therefore

\[
\boxed{\mathcal S_1(n)=nH_n-D(n)=B_1(n)+I_1(n)},
\]

recovering v13.316 exactly.

---

## 5. Positive integer moments

For integer \(m\ge1\), define generalized harmonic numbers

\[
H_N^{(j)}=\sum_{k=1}^N k^{-j},
\qquad H_N^{(0)}=N.
\]

Since

\[
\left(\frac nk-q\right)^m
=\sum_{j=0}^m {m\choose j}n^j(-q)^{m-j}k^{-j},
\]

the strict-descent interior contribution is

\[
\boxed{
I_{m,q}(n)
=\sum_{j=0}^m {m\choose j}n^j(-q)^{m-j}
\left(H_{R_q-1}^{(j)}-H_{L_q-1}^{(j)}\right).
}
\]

The terminal-boundary contribution is

\[
\boxed{B_{m,q}(n)=\left(\frac{s_q}{R_q}\right)^m}.
\]

Thus

\[
\boxed{
\mathcal S_m(n)
=\sum_{q\in Q(n)}\left[
\left(\frac{s_q}{R_q}\right)^m
+\sum_{j=0}^m {m\choose j}n^j(-q)^{m-j}
\left(H_{R_q-1}^{(j)}-H_{L_q-1}^{(j)}\right)
\right].
}
\]

This is the terminal/interior refinement of the earlier generalized-harmonic quotient-block moment hierarchy.

---

## 6. Logarithmic derivative at the support limit

The earlier identity

\[
\left.\frac{\partial}{\partial\alpha}\mathcal S_\alpha(n)\right|_{0^+}
=\sum_{k\nmid n}\log\left(\frac{r_k}{k}\right)
\]

splits over the same carriers:

\[
\boxed{
B'_0(n)
=\sum_{\substack{q\in Q(n)\\q\nmid n}}
\log\left(\frac{s_q}{R_q}\right),
}
\]

\[
\boxed{
I'_0(n)
=\sum_{q\in Q(n)}\sum_{k=L_q}^{R_q-1}
\log\left(\frac{n-kq}{k}\right),
}
\]

so

\[
\boxed{\mathcal S'_0(n)=B'_0(n)+I'_0(n)}.
\]

---

## 7. Unified hierarchy

The same quotient-block carriers now organize every level:

\[
\boxed{
\begin{array}{c|c|c}
&\text{terminal boundary}&\text{strict-descent interior}\\
\hline
\alpha\to0^+&Q_n-\tau(n)&n-Q_n\\
\alpha=1&B_1(n)&I_1(n)\\
\alpha=m\in\mathbb N&B_m(n)&I_m(n)\\
\text{all }\alpha>0&B_\alpha(n)&I_\alpha(n)
\end{array}}
\]

Hence the zeroth support theorem and the harmonic first-moment theorem are not isolated identities. They are two slices of one exact boundary/interior defect-moment hierarchy.

---

## Ledger numbering note

A concurrent Suzuki/operator audit created `v13.317` after v13.316. This divisor-shell checkpoint therefore uses v13.318 rather than colliding with that independent branch of the audit sequence.

---

## Guardrails

- The moment family and generalized-harmonic formulas reorganize classical floor/remainder data.
- No new asymptotic estimate for the Dirichlet divisor problem follows from this decomposition alone.
- The boundary has \(O(\sqrt n)\) summands, but cardinality alone does not provide a sharp magnitude bound.
- The \(\alpha\to0^+\) statement is a support-count limit, not evaluation of a separately defined \(0\)-power at zero defects.
- Contact endpoints vanish in every positive moment.
- No new primality criterion or factorization algorithm is claimed.

## Interpretation

The quotient-block terminal/interior geometry is now moment-complete: the same decomposition controls support, harmonic discrepancy, all positive real defect moments, every positive integer generalized-harmonic moment, and the logarithmic derivative at the support limit.