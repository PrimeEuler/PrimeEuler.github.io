# Cone Derivation Ledger v13.316 — First-Moment Boundary/Interior Defect Split

## Scope

This checkpoint lifts the v13.314-v13.315 contact/stable/descent support stratification from the zeroth defect moment to the first moment

\[
\mathcal S_1(n)=nH_n-D(n).
\]

Companion note:

`research-notes/First_Moment_Boundary_Interior_Defect_Split.md`

The result is an exact reorganization of the classical harmonic discrepancy by quotient-block terminal boundary versus strict-descent interior. No new divisor-problem asymptotic, primality theorem, factorization algorithm, RH/GRH, spectral, positivity, or Fredholm claim is made.

---

## 1. Quotient-block ladder

For a distinct quotient value q, let

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

Define the terminal remainder

\[
s_q=n-qR_q=n\bmod q.
\]

Then along the block

\[
\boxed{\Delta_k=s_q+q(R_q-k)}.
\]

The endpoint k=R_q is the unique non-descending terminal state; all k<R_q are strict-descent interior states.

---

## 2. First moment in one block

The block contribution is

\[
E_q(n)=\sum_{k=L_q}^{R_q}\frac{\Delta_k}{k}.
\]

Using \(\Delta_k=n-qk\),

\[
\boxed{
E_q(n)
=n\bigl(H_{R_q}-H_{L_q-1}\bigr)-qm_q.
}
\]

Separating the terminal k=R_q term gives

\[
\boxed{
E_q(n)=B_q^{(1)}(n)+I_q^{(1)}(n),
}
\]

where

\[
\boxed{
B_q^{(1)}(n)=\frac{s_q}{R_q}=\frac{n\bmod q}{\lfloor n/q\rfloor}
}
\]

and

\[
\boxed{
I_q^{(1)}(n)
=n\bigl(H_{R_q-1}-H_{L_q-1}\bigr)-q(m_q-1).
}
\]

Hence

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

---

## 3. Global boundary/interior split

Summing over distinct quotient values,

\[
\boxed{
nH_n-D(n)=E_{\partial}(n)+E_{\mathrm{int}}(n),
}
\]

with

\[
\boxed{
E_{\partial}(n)
=
\sum_{q\in Q(n)}
\frac{n\bmod q}{\lfloor n/q\rfloor}
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

The terminal-boundary sum has exactly \(Q_n=O(\sqrt n)\) potential terms.

---

## 4. Boundary support equals the stable endpoint layer

At a terminal block endpoint,

\[
B_q^{(1)}(n)=\frac{n\bmod q}{\lfloor n/q\rfloor}.
\]

Therefore

\[
\boxed{B_q^{(1)}(n)=0\iff q\mid n.}
\]

Thus

\[
\boxed{
E_{\partial}(n)
=
\sum_{\substack{q\in Q(n)\\q\nmid n}}
\frac{n\bmod q}{\lfloor n/q\rfloor}.
}
\]

So:

- contact terminals contribute zero;
- stable off-shell terminals contribute positive first-moment boundary weight;
- strict-descent points contribute the interior first moment.

---

## 5. Weighted lift of the zeroth-moment support split

From v13.315,

\[
\mathcal S_0(n)
=
\underbrace{Q_n-\tau(n)}_{\text{stable endpoint boundary}}
+
\underbrace{n-Q_n}_{\text{strict-descent interior}}.
\]

The present checkpoint gives the weighted analogue

\[
\boxed{
\mathcal S_1(n)
=
\underbrace{E_{\partial}(n)}_{\text{stable endpoint boundary weight}}
+
\underbrace{E_{\mathrm{int}}(n)}_{\text{strict-descent interior weight}}.
}
\]

The support stratification and first-moment stratification therefore use the same carriers.

---

## 6. Relation to earlier defect moments

Earlier work established

\[
\mathcal S_\alpha(n)=\sum_{k:r_k\ne0}\left(\frac{r_k}{k}\right)^\alpha,
\]

with

\[
\mathcal S_0=n-\tau(n),
\qquad
\mathcal S_1=nH_n-D(n).
\]

v13.316 shows that the boundary/interior support decomposition is not confined to \(\alpha=0\): it lifts exactly to \(\alpha=1\).

This suggests, but does not yet prove in closed form for arbitrary \(\alpha\), a general boundary/interior moment decomposition obtained by splitting each quotient block into its terminal endpoint and its interior ramp.

---

## Guardrails

- This is an exact reorganization of \(nH_n-D(n)\), not a new asymptotic estimate for the Dirichlet divisor problem.
- The boundary sum has O(\sqrt n) summands; no magnitude bound is inferred from that count alone.
- Contact terminals vanish in the first moment because their shell defect is zero.
- The stable-boundary and strict-descent interior carriers remain distinct.
- No new prime criterion or factoring algorithm is implied.

## Interpretation

The defect-dynamical stratification now controls both support and harmonic weight:

\[
\boxed{
\text{harmonic discrepancy}
=
\text{stable terminal-boundary defect}
+
\text{strict-descent interior defect}.
}
\]

So the classical quotient-block formula acquires a sharper cone-geometric reading: each horizontal run contributes one terminal remainder weight plus the accumulated normalized defect along its Euclidean descent interior.