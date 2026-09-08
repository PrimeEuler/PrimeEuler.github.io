# Cone Derivation Ledger v13.315 — Hyperbola Boundary Form of Defect-Strata Counts

## Scope

This checkpoint continues v13.314 by rewriting the global contact/stable/descent counts in the classical square-root hyperbola parameter

\[
m=\lfloor\sqrt n\rfloor.
\]

Companion note:

`research-notes/Hyperbola_Boundary_Form_of_Defect_Strata_Counts.md`

The distinct-quotient count itself is classical. The exact addition here is its role as the terminal boundary layer of the shell-defect dynamics.

No new primality, factorization, RH/GRH, spectral, positivity, or Fredholm claim is made.

---

## 1. Classical distinct-quotient count

Let

\[
Q(n)=\left\{\left\lfloor\frac nk\right\rfloor:1\le k\le n\right\},
\qquad Q_n=|Q(n)|,
\]

and

\[
m=\lfloor\sqrt n\rfloor.
\]

The small quotient values are

\[
1,2,\dots,m,
\]

while the large values are

\[
\left\lfloor\frac n1\right\rfloor,
\left\lfloor\frac n2\right\rfloor,
\dots,
\left\lfloor\frac nm\right\rfloor.
\]

There is one overlap precisely when

\[
\left\lfloor\frac nm\right\rfloor=m,
\]

which is equivalent to

\[
n<m(m+1).
\]

Therefore

\[
\boxed{
Q_n=
\begin{cases}
2m-1,&m^2\le n<m(m+1),\\
2m,&m(m+1)\le n<(m+1)^2.
\end{cases}}
\]

This formula is classical hyperbola/distinct-quotient structure and is not claimed as new.

---

## 2. Defect-strata counts in closed form

From v13.314,

\[
C(n)=\tau(n),
\qquad
S(n)=Q_n-\tau(n),
\qquad
D_{\rm desc}(n)=n-Q_n.
\]

Thus

\[
\boxed{
S(n)=
\begin{cases}
2m-1-\tau(n),&m^2\le n<m(m+1),\\
2m-\tau(n),&m(m+1)\le n<(m+1)^2,
\end{cases}}
\]

and

\[
\boxed{
D_{\rm desc}(n)=
\begin{cases}
n-2m+1,&m^2\le n<m(m+1),\\
n-2m,&m(m+1)\le n<(m+1)^2.
\end{cases}}
\]

Hence the strict-descent count depends only on the square-root hyperbola boundary, while the terminal endpoint layer is split arithmetically by \(\tau(n)\).

---

## 3. Endpoint boundary layer

Every quotient block contains exactly one terminal non-descending state. Therefore the terminal layer has cardinality

\[
\boxed{Q_n=O(\sqrt n)}.
\]

Its exact occupancy is

\[
\boxed{
Q_n
=
\tau(n)
+
\bigl(Q_n-\tau(n)\bigr),
}
\]

where

- \(\tau(n)\) terminal states are exact shell contacts;
- \(Q_n-\tau(n)\) terminal states are stable positive-defect closures.

The complementary interior has cardinality

\[
\boxed{n-Q_n}
\]

and consists entirely of strict Euclidean-descent states.

---

## 4. Refined zeroth defect support

The earlier zeroth-moment/support identity is

\[
\mathcal S_0(n)=n-\tau(n).
\]

Combining it with the hyperbola boundary gives

\[
\boxed{
\mathcal S_0(n)
=
\underbrace{Q_n-\tau(n)}_{\text{stable endpoint boundary}}
+
\underbrace{n-Q_n}_{\text{strict-descent interior}}.
}
\]

Thus the positive-defect support has an exact two-scale decomposition into an \(O(\sqrt n)\) terminal boundary and a bulk interior.

---

## 5. Hyperbola-method interpretation

The classical distinct-quotient set is precisely the set of terminal columns of the horizontal quotient runs.

Hence the usual hyperbola compression admits the exact dynamical reading

\[
\boxed{
\text{one terminal state per quotient block}
\quad+\quad
\text{all remaining states are interior descent states}.
}
\]

Divisibility acts only on the terminal layer:

\[
\boxed{
q\mid n
\iff
\text{the terminal state of }B_q\text{ is a shell contact}.
}
\]

Otherwise the terminal state is stable off-shell.

---

## 6. Prime specialization

For prime \(p\),

\[
\tau(p)=2,
\]

so

\[
\boxed{C(p)=2},
\qquad
\boxed{S(p)=Q_p-2},
\qquad
\boxed{D_{\rm desc}(p)=p-Q_p}.
\]

Primality still enters only through the minimal contact occupancy of the terminal boundary layer.

---

## Relation to v13.314

- v13.314: one non-descending terminal state per quotient block and exact global counts.
- v13.315: the terminal layer is identified explicitly with the classical square-root hyperbola boundary count \(Q_n\), while the bulk interior is \(n-Q_n\).

The new content is therefore interpretive/exactly organizational, not a new formula for the classical distinct-quotient count.

---

## Guardrails

- Do not claim the formula for \(Q_n\) as new.
- The new contribution is the exact defect-dynamical occupancy of the hyperbola boundary/interior split.
- \(n-Q_n\) is geometric/combinatorial, not a divisor multiplicity.
- The endpoint arithmetic is entirely in the split \(\tau(n)+(Q_n-\tau(n))\).
- No new primality theorem or factoring algorithm is claimed.

## Interpretation

The shell-defect staircase now has a clean two-scale structure. The classical square-root hyperbola boundary contributes one terminal state per quotient block; arithmetic determines which terminals are genuine divisor contacts. Every nonterminal column belongs to the strict Euclidean-descent interior.