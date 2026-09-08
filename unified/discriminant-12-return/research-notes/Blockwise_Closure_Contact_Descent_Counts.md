# Blockwise Closure, Contact, and Descent Counts

## Scope

This note continues the shell-defect dynamics of v13.313 by counting the three defect strata exactly inside each quotient block.

For fixed \(n\), let

\[
B_q=\{k:L_q\le k\le R_q\},
\qquad
L_q=\left\lfloor\frac{n}{q+1}\right\rfloor+1,
\qquad
R_q=\left\lfloor\frac nq\right\rfloor,
\]

with block length

\[
m_q=R_q-L_q+1.
\]

On this block,

\[
\Delta_k=n-kq.
\]

Write the endpoint remainder

\[
s_q:=n-qR_q=n\bmod q,
\qquad 0\le s_q<q.
\]

Then for \(k=R_q-j\), \(j=0,1,\dots,m_q-1\),

\[
\boxed{\Delta_{R_q-j}=s_q+jq.}
\]

Thus each quotient block is an arithmetic defect ladder descending by exactly \(q\) toward its right endpoint.

## Exact blockwise stratum counts

The v13.313 strata are:

- contact: \(\Delta_k=0\),
- stable off-shell closure: \(0<\Delta_k<q\),
- strict descent: \(\Delta_k\ge q\).

Because \(\Delta_{R_q-j}=s_q+jq\), only the endpoint \(j=0\) can satisfy \(\Delta_k<q\).

Hence:

### If \(q\mid n\)

Then \(s_q=0\). The right endpoint is the unique contact:

\[
\boxed{C_q=1},
\qquad
\boxed{S_q=0},
\qquad
\boxed{D_q=m_q-1}.
\]

Here \(C_q,S_q,D_q\) denote the contact, stable-closure, and strict-descent counts in block \(B_q\).

### If \(q\nmid n\)

Then \(0<s_q<q\). The right endpoint is the unique stable off-shell closure point:

\[
\boxed{C_q=0},
\qquad
\boxed{S_q=1},
\qquad
\boxed{D_q=m_q-1}.
\]

Therefore, for every distinct quotient block,

\[
\boxed{C_q=\mathbf 1_{q\mid n}},
\]

\[
\boxed{S_q=\mathbf 1_{q\nmid n}},
\]

and universally

\[
\boxed{D_q=m_q-1}.
\]

Equivalently,

\[
\boxed{C_q+S_q=1}
\]

for every quotient block: each horizontal run has exactly one terminal non-descending point, which is either a true shell contact or a positive-defect stable closure.

## Global counts

Let \(Q(n)\) be the set of distinct quotients \(\lfloor n/k\rfloor\), and let

\[
Q_n:=|Q(n)|.
\]

Since the quotient blocks partition \(\{1,\dots,n\}\),

\[
\sum_{q\in Q(n)}m_q=n.
\]

Summing the blockwise formulas gives

\[
\boxed{C(n)=\sum_{q\in Q(n)}\mathbf 1_{q\mid n}=\tau(n)},
\]

because every divisor \(q\mid n\) occurs as a distinct quotient and contributes one shell-contact endpoint.

The stable-closure count is

\[
\boxed{S(n)=Q_n-\tau(n)}.
\]

The strict-descent count is

\[
\boxed{D_{\mathrm{desc}}(n)=n-Q_n}.
\]

Thus the full set of \(n\) staircase columns decomposes exactly as

\[
\boxed{
n=\tau(n)+\bigl(Q_n-\tau(n)\bigr)+\bigl(n-Q_n\bigr).
}
\]

In words:

\[
\boxed{
\text{all columns}
=
\text{contacts}
+\text{stable closures}
+\text{strict descents}.
}
\]

This is a new exact counting organization of the same staircase data.

## Distinct quotient count

The classical distinct-quotient count satisfies

\[
Q_n=\left|\left\{\left\lfloor\frac nk\right\rfloor:1\le k\le n\right\}\right|.
\]

Writing \(m=\lfloor\sqrt n\rfloor\),

\[
\boxed{
Q_n=
\begin{cases}
2m-1, & \lfloor n/m\rfloor=m,\\
2m, & \lfloor n/m\rfloor>m.
\end{cases}}
\]

Equivalently,

\[
\boxed{Q_n=2\lfloor\sqrt n\rfloor-\mathbf 1_{\,n<\lfloor\sqrt n\rfloor(\lfloor\sqrt n\rfloor+1)}}
\]

with the first piecewise form preferred for clarity.

Hence

\[
\boxed{S(n)=Q_n-\tau(n)}
\]

is automatically \(O(\sqrt n)\), while

\[
\boxed{D_{\mathrm{desc}}(n)=n-Q_n}
\]

contains the bulk of columns.

## Prime specialization

For a prime \(p\),

\[
\tau(p)=2.
\]

Therefore

\[
\boxed{C(p)=2},
\]

\[
\boxed{S(p)=Q_p-2},
\]

\[
\boxed{D_{\mathrm{desc}}(p)=p-Q_p}.
\]

Primality still appears only through the minimal contact count; the stable-closure count depends additionally on the classical distinct-quotient count.

## Relation to support count

Earlier work defined the positive-defect support

\[
\mathcal S_0(n)=n-\tau(n).
\]

The present decomposition refines it exactly:

\[
\boxed{
\mathcal S_0(n)
=
S(n)+D_{\mathrm{desc}}(n)
=
\bigl(Q_n-\tau(n)\bigr)+\bigl(n-Q_n\bigr).
}
\]

Thus positive shell defect splits into:

1. one stable positive endpoint for each nondividing quotient block;
2. all remaining interior points of quotient ramps, which undergo strict Euclidean descent.

This is an exact refinement of the zeroth defect moment/support theorem.

## Geometry

Every horizontal quotient run has the form

\[
s_q+(m_q-1)q,\;s_q+(m_q-2)q,\;\dots,\;s_q+q,\;s_q.
\]

Therefore the right endpoint is structurally distinguished:

\[
\boxed{
\text{endpoint defect }s_q=n\bmod q
}
\]

and it alone decides whether the run terminates on the shell or in stable off-shell closure.

All earlier vertices in the same run have defect at least \(q\) and hence belong to the strict-descent stratum.

## Guardrails

- \(S(n)=Q_n-\tau(n)\) is a stable-closure count, not a new primality criterion.
- The contact count remains exactly \(\tau(n)\).
- The strict-descent count \(n-Q_n\) is determined by quotient-block multiplicities, not by divisor structure alone.
- No new factoring algorithm is implied.
- This refines the zeroth-moment support decomposition; it does not alter the first-moment identity \(nH_n-D(n)\).
