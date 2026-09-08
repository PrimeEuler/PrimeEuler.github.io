# Hyperbola Boundary Form of the Defect-Strata Counts

## Scope

This note continues the quotient-block defect dynamics of ledger v13.314 by rewriting the global contact/stable/descent counts in the classical square-root hyperbola parameter

\[
m=\lfloor\sqrt n\rfloor.
\]

The distinct-quotient count itself is classical. The useful addition here is the exact placement of the previously derived defect strata on that boundary count.

No new primality, factorization, RH/GRH, spectral, positivity, or Fredholm claim is made.

---

## 1. Distinct quotient count in square-root form

Let

\[
Q(n)=\left\{\left\lfloor\frac nk\right\rfloor:1\le k\le n\right\},
\qquad Q_n=|Q(n)|,
\]

and let

\[
m=\lfloor\sqrt n\rfloor.
\]

The distinct quotient values consist of the small values

\[
1,2,\dots,m
\]

and the large values

\[
\left\lfloor\frac n1\right\rfloor,
\left\lfloor\frac n2\right\rfloor,
\dots,
\left\lfloor\frac nm\right\rfloor,
\]

with one overlap exactly when

\[
\left\lfloor\frac nm\right\rfloor=m.
\]

Since

\[
\left\lfloor\frac nm\right\rfloor=m
\iff n<m(m+1),
\]

we obtain

\[
\boxed{
Q_n=
\begin{cases}
2m-1,& m^2\le n<m(m+1),\\
2m,& m(m+1)\le n<(m+1)^2.
\end{cases}}
\]

Equivalently,

\[
\boxed{
Q_n=2\lfloor\sqrt n\rfloor-\mathbf 1_{\,n<\lfloor\sqrt n\rfloor(\lfloor\sqrt n\rfloor+1)}.
}
\]

---

## 2. Exact defect-strata counts

From v13.314,

\[
C(n)=\tau(n),
\qquad
S(n)=Q_n-\tau(n),
\qquad
D_{\rm desc}(n)=n-Q_n.
\]

Therefore, with \(m=\lfloor\sqrt n\rfloor\),

\[
\boxed{
S(n)=
\begin{cases}
2m-1-\tau(n),& m^2\le n<m(m+1),\\
2m-\tau(n),& m(m+1)\le n<(m+1)^2,
\end{cases}}
\]

and

\[
\boxed{
D_{\rm desc}(n)=
\begin{cases}
n-2m+1,& m^2\le n<m(m+1),\\
n-2m,& m(m+1)\le n<(m+1)^2.
\end{cases}}
\]

Thus the bulk descent count is completely geometric, depending only on the square-root hyperbola boundary, while the split of the endpoint layer into contacts versus stable closures is arithmetic through \(\tau(n)\).

---

## 3. Boundary layer versus arithmetic occupancy

The quotient-block endpoint layer has size

\[
\boxed{Q_n=O(\sqrt n)}.
\]

Its arithmetic occupancy is

\[
\boxed{
Q_n
=
\underbrace{\tau(n)}_{\text{shell-contact endpoints}}
+
\underbrace{(Q_n-\tau(n))}_{\text{stable off-shell endpoints}}.
}
\]

The complementary interior has size

\[
\boxed{n-Q_n}
\]

and every one of those columns lies in the strict Euclidean-descent stratum.

Hence the positive-defect support

\[
\mathcal S_0(n)=n-\tau(n)
\]

has the exact two-scale decomposition

\[
\boxed{
\mathcal S_0(n)
=
\underbrace{Q_n-\tau(n)}_{O(\sqrt n)\text{ boundary endpoint layer}}
+
\underbrace{n-Q_n}_{\text{bulk descent interior}}.
}
\]

The new information is therefore not a new formula for \(Q_n\), but an exact dynamical interpretation of the classical hyperbola boundary count.

---

## 4. Hyperbola-method reading

The familiar \(O(\sqrt n)\) distinct-quotient set is precisely the set of terminal columns of the horizontal quotient runs.

Thus the classical hyperbola compression now acquires the defect-dynamical interpretation

\[
\boxed{
\text{one terminal state per quotient block}
\quad+\quad
\text{all remaining states are interior Euclidean descent points}.
}
\]

Divisibility then acts only on the terminal layer:

\[
q\mid n
\iff
\text{the }q\text{-block terminal state is a shell contact}.
\]

Otherwise that terminal state is stable off-shell.

---

## 5. Prime specialization

For a prime \(p\),

\[
\tau(p)=2.
\]

Hence

\[
\boxed{S(p)=Q_p-2},
\qquad
\boxed{D_{\rm desc}(p)=p-Q_p}.
\]

The prime condition still enters only through the minimal contact occupancy of the endpoint layer.

---

## Guardrails

- The formula for \(Q_n\) is classical distinct-quotient/hyperbola structure.
- The contribution here is its exact interpretation inside the defect-strata decomposition.
- The bulk count \(n-Q_n\) is geometric/combinatorial, not a divisor statistic.
- The endpoint split \(\tau(n)+(Q_n-\tau(n))\) carries the divisor arithmetic.
- No new primality theorem or factorization algorithm is claimed.

## Interpretation

The staircase now separates naturally into a classical square-root hyperbola boundary and a bulk interior. The boundary has one terminal state per distinct quotient; arithmetic decides which of those terminal states are genuine divisor contacts. Everything away from that boundary is strict Euclidean defect descent.