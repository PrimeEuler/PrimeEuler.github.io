# First-Moment Boundary/Interior Split of the Divisor Shell Defect

## Scope

This note continues the defect-strata analysis by refining the first moment

\[
E(n)=nH_n-D(n)=\sum_{k=1}^n \frac{\Delta_k}{k},
\qquad
\Delta_k=n\bmod k.
\]

The goal is to separate the contribution of the terminal quotient-block boundary from the strict-descent interior.

No new primality, factorization, RH/GRH, spectral, positivity, or Fredholm claim is made.

---

## 1. Quotient-block defect ladder

Fix a distinct quotient value

\[
q=\left\lfloor\frac nk\right\rfloor
\]

and its block

\[
B_q=\{k:L_q\le k\le R_q\},
\]

where

\[
L_q=\left\lfloor\frac{n}{q+1}\right\rfloor+1,
\qquad
R_q=\left\lfloor\frac nq\right\rfloor,
\qquad
m_q=R_q-L_q+1.
\]

Let

\[
s_q=n-qR_q=n\bmod q.
\]

Then for

\[
k=R_q-j,
\qquad
j=0,1,\dots,m_q-1,
\]

we have

\[
\boxed{\Delta_k=s_q+jq.}
\]

The terminal point is \(j=0\); all \(j\ge1\) are strict-descent interior points.

---

## 2. Exact first-moment split inside one block

The block contribution to the harmonic discrepancy is

\[
E_q(n)
=
\sum_{k=L_q}^{R_q}\frac{\Delta_k}{k}.
\]

Using \(\Delta_k=n-qk\),

\[
E_q(n)
=
n\sum_{k=L_q}^{R_q}\frac1k-qm_q
=
n\bigl(H_{R_q}-H_{L_q-1}\bigr)-qm_q.
\]

Now write

\[
\Delta_k=s_q+q(R_q-k).
\]

Then

\[
\boxed{
E_q(n)
=
B_q^{(1)}(n)+I_q^{(1)}(n),
}
\]

where the terminal-boundary term is

\[
\boxed{
B_q^{(1)}(n)
=
\frac{s_q}{R_q}
=
\frac{n\bmod q}{\lfloor n/q\rfloor},
}
\]

and the strict-descent interior term is

\[
\boxed{
I_q^{(1)}(n)
=
\sum_{k=L_q}^{R_q-1}\frac{s_q+q(R_q-k)}{k}.
}
\]

Equivalently, separating the common terminal remainder from the ramp height,

\[
\boxed{
I_q^{(1)}(n)
=
s_q\bigl(H_{R_q-1}-H_{L_q-1}\bigr)
+q\sum_{k=L_q}^{R_q-1}\frac{R_q-k}{k}.
}
\]

Since

\[
\frac{R_q-k}{k}=\frac{R_q}{k}-1,
\]

we obtain the closed form

\[
\boxed{
I_q^{(1)}(n)
=
\bigl(s_q+qR_q\bigr)
\bigl(H_{R_q-1}-H_{L_q-1}\bigr)
-q(m_q-1).
}
\]

But

\[
s_q+qR_q=n,
\]

so this simplifies to

\[
\boxed{
I_q^{(1)}(n)
=
n\bigl(H_{R_q-1}-H_{L_q-1}\bigr)-q(m_q-1).
}
\]

Therefore

\[
\boxed{
E_q(n)
=
\frac{n\bmod q}{\lfloor n/q\rfloor}
+
n\bigl(H_{R_q-1}-H_{L_q-1}\bigr)
-q(m_q-1).
}
\]

This is exactly the same block first moment, now decomposed by the v13.314-v13.315 boundary/interior stratification.

---

## 3. Global first-moment boundary/interior decomposition

Summing over distinct quotient values gives

\[
\boxed{
E(n)=E_{\partial}(n)+E_{\mathrm{int}}(n),
}
\]

with

\[
\boxed{
E_{\partial}(n)
=
\sum_{q\in Q(n)}
\frac{n\bmod q}{\lfloor n/q\rfloor},
}
\]

and

\[
\boxed{
E_{\mathrm{int}}(n)
=
\sum_{q\in Q(n)}
\left[
 n\bigl(H_{R_q-1}-H_{L_q-1}\bigr)
-q(m_q-1)
\right].
}
\]

Thus

\[
\boxed{
nH_n-D(n)=E_{\partial}(n)+E_{\mathrm{int}}(n).}
\]

The boundary sum has only \(Q_n=O(\sqrt n)\) terms.

---

## 4. Contact/stable endpoint interpretation

At the terminal point of block \(B_q\),

\[
B_q^{(1)}(n)
=
\frac{s_q}{R_q}.
\]

If \(q\mid n\), then

\[
s_q=0,
\]

so the terminal first-moment contribution vanishes.

If \(q\nmid n\), then

\[
0<s_q<q,
\]

and

\[
B_q^{(1)}(n)>0.
\]

Hence the terminal boundary contribution is supported exactly on the stable off-shell endpoint layer:

\[
\boxed{
B_q^{(1)}(n)=0
\iff
q\mid n.
}
\]

Globally,

\[
\boxed{
E_{\partial}(n)
=
\sum_{\substack{q\in Q(n)\\q\nmid n}}
\frac{n\bmod q}{\lfloor n/q\rfloor}.
}
\]

So the first moment inherits the same exact boundary occupancy as the zeroth moment:

- contact terminals contribute zero;
- stable off-shell terminals contribute positive boundary defect;
- strict-descent points contribute the interior term.

---

## 5. Relation to the zeroth-moment split

The zeroth support decomposition is

\[
\mathcal S_0(n)
=
\bigl(Q_n-\tau(n)\bigr)
+
\bigl(n-Q_n\bigr).
\]

The present first-moment decomposition is its weighted analogue:

\[
\boxed{
\mathcal S_1(n)
=
E_{\partial}(n)+E_{\mathrm{int}}(n).
}
\]

The two layers have exactly the same supports as in the zeroth moment, but now weighted by normalized shell-defect amplitudes \(\Delta_k/k\).

This provides a direct bridge between the dynamical strata and the harmonic discrepancy.

---

## Guardrails

- This is an exact reorganization of the classical first-moment identity, not a new asymptotic for the divisor problem.
- The boundary term is O(\sqrt n) in number of summands, not necessarily in total magnitude by this statement alone.
- Contact terminals contribute zero to the first moment because their shell defect is zero.
- Stable terminals and strict-descent interiors remain distinct carriers.
- No new prime criterion or factoring algorithm is implied.

## Interpretation

The v13.314-v13.315 support split lifts exactly from the zeroth moment to the harmonic first moment:

\[
\boxed{
\text{harmonic discrepancy}
=
\text{terminal stable-boundary defect}
+
\text{strict-descent interior defect}.
}
\]

The classical quotient-block formula therefore admits a sharper cone-geometric reading: every block contributes one terminal remainder weight plus the accumulated normalized defect along its Euclidean descent ramp.