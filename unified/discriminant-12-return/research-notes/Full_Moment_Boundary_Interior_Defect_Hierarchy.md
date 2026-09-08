# Full Defect-Moment Boundary/Interior Hierarchy

## Scope

This note extends the quotient-block boundary/interior split from the zeroth and first shell-defect moments to the full positive moment family

\[
\mathcal S_\alpha(n)=\sum_{k:r_k\ne0}\left(\frac{r_k}{k}\right)^\alpha,
\qquad \alpha>0,
\]

where

\[
r_k=n-k\left\lfloor\frac nk\right\rfloor=n-Y_k^2.
\]

The result is an exact decomposition by the same carriers identified in v13.314-v13.316: one terminal state per quotient block and the strict-descent interior of that block. No new divisor-problem asymptotic, primality theorem, or factorization algorithm is claimed.

---

## 1. Quotient-block defect ladder

For each distinct quotient value \(q\), define

\[
L_q=\left\lfloor\frac{n}{q+1}\right\rfloor+1,
\qquad
R_q=\left\lfloor\frac nq\right\rfloor,
\qquad
m_q=R_q-L_q+1,
\]

and the terminal remainder

\[
s_q=n-qR_q=n\bmod q.
\]

For \(k\in[L_q,R_q]\),

\[
\Delta_k=n-kq=s_q+q(R_q-k),
\]

and therefore

\[
\delta_k(n)=\frac{\Delta_k}{k}=\frac nk-q.
\]

The endpoint \(k=R_q\) is the unique non-descending terminal state of the block. Every \(k<R_q\) is a strict-descent state.

---

## 2. Exact split for every positive real moment

For \(\alpha>0\), define the block moment

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

## 3. Zeroth-moment limit recovers the exact support split

For every positive defect \(x\in(0,1)\), \(x^\alpha\to1\) as \(\alpha\to0^+\), whereas zero defects contribute zero for every \(\alpha>0\). Therefore

\[
\boxed{\lim_{\alpha\to0^+}B_\alpha(n)=Q_n-\tau(n)},
\]

because exactly the nondividing quotient blocks have \(s_q>0\).

Every interior point has positive defect, so

\[
\boxed{
\lim_{\alpha\to0^+}I_\alpha(n)
=\sum_{q\in Q(n)}(m_q-1)
=n-Q_n.
}
\]

Thus

\[
\boxed{
\lim_{\alpha\to0^+}\mathcal S_\alpha(n)
=(Q_n-\tau(n))+(n-Q_n)
=n-\tau(n).
}
\]

The v13.315 support decomposition is therefore the exact \(\alpha\to0^+\) boundary/interior limit of the full positive moment family.

---

## 4. First moment as the v13.316 specialization

At \(\alpha=1\),

\[
B_1(n)=\sum_{q\in Q(n)}\frac{n\bmod q}{\lfloor n/q\rfloor},
\]

and

\[
I_1(n)=\sum_{q\in Q(n)}\left[n(H_{R_q-1}-H_{L_q-1})-q(m_q-1)\right].
\]

Hence

\[
\boxed{\mathcal S_1(n)=nH_n-D(n)=B_1(n)+I_1(n)},
\]

recovering v13.316 exactly.

---

## 5. Positive integer moments and generalized harmonic sums

Let \(m\ge1\) be an integer and define

\[
H_N^{(j)}=\sum_{k=1}^N k^{-j},
\qquad H_N^{(0)}=N.
\]

Since

\[
\left(\frac nk-q\right)^m
=\sum_{j=0}^m {m\choose j}n^j(-q)^{m-j}k^{-j},
\]

we obtain

\[
\boxed{
I_{m,q}(n)
=\sum_{j=0}^m {m\choose j}n^j(-q)^{m-j}
\left(H_{R_q-1}^{(j)}-H_{L_q-1}^{(j)}\right).
}
\]

The boundary term is

\[
\boxed{B_{m,q}(n)=\left(\frac{s_q}{R_q}\right)^m}.
\]

Therefore

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

This is the boundary/interior refinement of the earlier quotient-block generalized-harmonic moment hierarchy.

---

## 6. Logarithmic derivative at the support limit

The previously established derivative

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

## 7. Structural summary

The same quotient-block carriers organize the entire hierarchy:

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

Thus the zeroth support theorem and harmonic first-moment theorem are two members of one exact boundary/interior defect-moment hierarchy.

---

## Guardrails

- The moment family and generalized-harmonic expansions reorganize classical floor/remainder data.
- No new asymptotic estimate for the Dirichlet divisor problem is inferred.
- An \(O(\sqrt n)\) boundary term count alone does not imply a sharp magnitude bound.
- The \(\alpha\to0^+\) limit is a support-count limit, not evaluation at an independently defined \(\alpha=0\) power.
- Contact endpoints remain zero in every positive moment.
- No new primality criterion or factorization algorithm is claimed.
