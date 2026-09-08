# Cone Derivation Ledger v13.314 — Blockwise Closure, Contact, and Descent Counts

## Scope

This checkpoint refines v13.313 by counting the three defect-dynamical strata exactly inside each quotient block.

Companion note:

`research-notes/Blockwise_Closure_Contact_Descent_Counts.md`

No new primality theorem, factoring algorithm, RH/GRH, spectral, positivity, or Fredholm claim is made.

---

## 1. Quotient-block defect ladder

For fixed \(n\), let

\[
B_q=\{k:L_q\le k\le R_q\},
\]

with

\[
L_q=\left\lfloor\frac{n}{q+1}\right\rfloor+1,
\qquad
R_q=\left\lfloor\frac nq\right\rfloor,
\qquad
m_q=R_q-L_q+1.
\]

On this block,

\[
\Delta_k=n-kq.
\]

Let

\[
s_q=n-qR_q=n\bmod q.
\]

Then for \(j=0,1,\dots,m_q-1\),

\[
\boxed{\Delta_{R_q-j}=s_q+jq.}
\]

Thus every horizontal quotient run is an exact arithmetic defect ladder whose right endpoint carries the reduced remainder \(s_q\).

---

## 2. Exact count in one block

The v13.313 strata are:

- contact: \(\Delta=0\),
- stable off-shell closure: \(0<\Delta<q\),
- strict descent: \(\Delta\ge q\).

Because

\[
\Delta_{R_q-j}=s_q+jq,
\qquad 0\le s_q<q,
\]

only the right endpoint \(j=0\) can be non-descending.

If \(q\mid n\), then \(s_q=0\), so

\[
\boxed{C_q=1,\qquad S_q=0,\qquad D_q=m_q-1.}
\]

If \(q\nmid n\), then \(0<s_q<q\), so

\[
\boxed{C_q=0,\qquad S_q=1,\qquad D_q=m_q-1.}
\]

Hence universally

\[
\boxed{C_q=\mathbf1_{q\mid n}},
\]

\[
\boxed{S_q=\mathbf1_{q\nmid n}},
\]

\[
\boxed{D_q=m_q-1},
\]

and therefore

\[
\boxed{C_q+S_q=1}.
\]

Every quotient block has exactly one terminal non-descending point: either a true shell contact or a stable positive-defect closure.

---

## 3. Global counts

Let

\[
Q(n)=\left\{\left\lfloor\frac nk\right\rfloor:1\le k\le n\right\},
\qquad
Q_n=|Q(n)|.
\]

Since the quotient blocks partition the \(n\) columns,

\[
\sum_{q\in Q(n)}m_q=n.
\]

Summing the blockwise formulas gives

\[
\boxed{C(n)=\tau(n)},
\]

\[
\boxed{S(n)=Q_n-\tau(n)},
\]

\[
\boxed{D_{\rm desc}(n)=n-Q_n}.
\]

Thus

\[
\boxed{
n=\tau(n)+\bigl(Q_n-\tau(n)\bigr)+\bigl(n-Q_n\bigr).
}
\]

This is the exact global decomposition

\[
\boxed{
\text{all staircase columns}
=
\text{contacts}
+\text{stable closures}
+\text{strict descents}.
}
\]

---

## 4. Refinement of zeroth defect support

Earlier work established

\[
\mathcal S_0(n)=n-\tau(n).
\]

The present count refines this exactly:

\[
\boxed{
\mathcal S_0(n)
=
\bigl(Q_n-\tau(n)\bigr)
+
\bigl(n-Q_n\bigr).
}
\]

Equivalently,

\[
\boxed{
\mathcal S_0(n)=S(n)+D_{\rm desc}(n).
}
\]

So the positive-defect support splits into:

1. one stable positive endpoint for every nondividing quotient block;
2. all interior quotient-ramp points, which lie in the strict Euclidean-descent stratum.

This is an exact refinement of the zeroth-moment theorem, not a replacement for it.

---

## 5. Distinct quotient scale

With \(m=\lfloor\sqrt n\rfloor\), the classical distinct-quotient count satisfies

\[
Q_n=
\begin{cases}
2m-1, & \lfloor n/m\rfloor=m,\\
2m, & \lfloor n/m\rfloor>m.
\end{cases}
\]

Therefore

\[
S(n)=Q_n-\tau(n)=O(\sqrt n),
\]

while

\[
D_{\rm desc}(n)=n-Q_n
\]

contains the bulk of columns.

This makes precise that only O(\sqrt n) staircase columns are terminal points of quotient runs; all remaining columns are interior descent points.

---

## 6. Prime specialization

For prime \(p\),

\[
\tau(p)=2.
\]

Hence

\[
\boxed{C(p)=2},
\]

\[
\boxed{S(p)=Q_p-2},
\]

\[
\boxed{D_{\rm desc}(p)=p-Q_p}.
\]

Primality still appears through the minimal contact count only. The new stable-closure count combines the distinct-quotient geometry with divisor structure.

---

## 7. Relation to v13.312-v13.313

- v13.312: the block endpoint is the Euclidean reduction of shell defect.
- v13.313: columns split dynamically into contact, stable closure, and strict descent.
- v13.314: each quotient block contains exactly one non-descending terminal point, yielding exact global counts.

The resulting hierarchy is

\[
\boxed{
\text{defect support}
\to
\text{quotient blocks}
\to
\text{terminal contact/stable endpoint}
+\text{interior descent points}.
}
\]

---

## Guardrails

- \(S(n)=Q_n-\tau(n)\) is not a new prime criterion.
- Contact count remains exactly \(\tau(n)\).
- \(n-Q_n\) measures quotient-block interior multiplicity, not divisor multiplicity.
- No factoring algorithm is implied.
- The first-moment identity \(nH_n-D(n)\) and V4 character decomposition remain unchanged.

## Interpretation

The Euclidean defect dynamics now has an exact counting law. Every horizontal quotient run contributes one distinguished endpoint: divisibility decides whether that endpoint lies exactly on the shell or closes stably off-shell. All earlier vertices in the run are strict Euclidean-descent points. Globally, the zeroth shell-defect support therefore splits canonically into an O(\sqrt n) endpoint layer and a bulk interior-descent layer.