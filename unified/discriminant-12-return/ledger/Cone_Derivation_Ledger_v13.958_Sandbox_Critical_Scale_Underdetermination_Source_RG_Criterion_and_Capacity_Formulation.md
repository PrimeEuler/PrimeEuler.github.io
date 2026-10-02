# Cone Derivation Ledger v13.958 — Sandbox: Critical-Scale Underdetermination, Source-RG Fixed-Point Criterion, and Capacity Formulation

**Date:** 2026-10-02  
**Track:** Sandbox / untwisted Suzuki source-spectral selector lane  
**Status:** [D] exact countermodel showing \(N_a\delta_\tau\) is not fixed by the universal matrix state alone; [D] exact scaled-ratio criterion for \(N^{-1}\) critical scaling; [D] exact source-capacity dual formulation; [D] tightness criterion for the rescaled critical matrix state; [G] zero-blind variational exponent does not by itself determine the physical source scale; [O] prove the source-RG ratio limit for Suzuki's operator  
**Authorization:** Jeremy, 2026-10-02 ("perfect hit it!!!!")  
**Parents:** v13.950, v13.956, v13.957 (External Audit Round 146)  
**Collision check:** v13.958 was absent in the live tree immediately before this write.

---

## 0. Gate and verdict

v13.956 defines the exact untwisted source spectral matrix and the intrinsic critical regulator \(\delta_\tau(a)\) by

\[
\kappa_a(\delta_\tau(a))
=
e^{-\tau},
\qquad
\tau>0.
\]

The cone/sieve scale is

\[
N_a=e^{2a}.
\]

The natural question was whether the already-proved universal critical parity weights and the exact zero-blind exponent force

\[
N_a\delta_\tau(a)
\longrightarrow
C_\tau\in(0,\infty).
\]

They do **not**.

The present entry proves this sharply by an explicit positive source-spectral countermodel that preserves:

- the exact raw source masses;
- the exact raw right/left overlap;
- \(\kappa_a(0+)=1\);
- the exact large-\(\delta\) endpoint;
- reflection symmetry and positivity;

while allowing the critical scale to be chosen arbitrarily.

The correct extra hypothesis is a scale limit of the **source resolvent ratio** itself.

---

## 1. Exact parity source masses [D]

From v13.956,

\[
m_a
:=
\rho_a([0,\infty))
=
\frac{1-e^{-4a}}2,
\]

and

\[
c_a^{\rm raw}
:=
\eta_a([0,\infty))
=
2ae^{-2a}.
\]

The even/odd source spectral measures are

\[
d\sigma_{a,+}
=
d\rho_a+d\eta_a,
\]

\[
d\sigma_{a,-}
=
d\rho_a-d\eta_a.
\]

Their total masses are therefore

\[
\boxed{
M_{+,a}
=
m_a+c_a^{\rm raw},
}
\tag{1}
\]

\[
\boxed{
M_{-,a}
=
m_a-c_a^{\rm raw}.
}
\tag{2}
\]

As \(a\to\infty\),

\[
M_{+,a}\to\frac12,
\qquad
M_{-,a}\to\frac12.
\]

---

## 2. Exact critical equation in the parity basis [D]

Define

\[
G_{a,+}(\delta)
=
\int\frac{d\sigma_{a,+}(\lambda)}{\lambda+\delta},
\]

\[
G_{a,-}(\delta)
=
\int\frac{d\sigma_{a,-}(\lambda)}{\lambda+\delta}.
\]

From v13.956,

\[
\kappa_a(\delta)
=
\frac{G_{a,+}(\delta)-G_{a,-}(\delta)}
{G_{a,+}(\delta)+G_{a,-}(\delta)}.
\]

Thus

\[
\kappa_a(\delta_\tau)
=
e^{-\tau}
\]

is equivalent to

\[
\boxed{
\frac{
G_{a,-}(\delta_\tau)
}{
G_{a,+}(\delta_\tau)
}
=
q_\tau,
}
\tag{3}
\]

where

\[
\boxed{
q_\tau
=
\tanh\!\left(\frac\tau2\right)
=
\frac{1-e^{-\tau}}{1+e^{-\tau}}.
}
\tag{4}
\]

The standing first-crossing convention is retained.

---

## 3. Two-atom countermodel [D]

Let

\[
s_a>0
\]

be an arbitrary positive sequence.

Define parity source spectral measures by

\[
\boxed{
d\sigma_{a,+}
=
M_{+,a}\,\delta_0,
}
\tag{5}
\]

\[
\boxed{
d\sigma_{a,-}
=
M_{-,a}\,\delta_{s_a}.
}
\tag{6}
\]

These are positive measures.

Define

\[
d\rho_a
=
\frac12
(d\sigma_{a,+}+d\sigma_{a,-}),
\]

\[
d\eta_a
=
\frac12
(d\sigma_{a,+}-d\sigma_{a,-}).
\]

Then the matrix measure

\[
d\Sigma_a
=
\begin{pmatrix}
d\rho_a&d\eta_a\\
d\eta_a&d\rho_a
\end{pmatrix}
\]

is positive semidefinite, because its parity diagonalization is exactly

\[
\operatorname{diag}
(d\sigma_{a,+},d\sigma_{a,-}).
\]

Its total masses are

\[
\rho_a([0,\infty))
=
\frac{M_{+,a}+M_{-,a}}2
=
m_a,
\]

\[
\eta_a([0,\infty))
=
\frac{M_{+,a}-M_{-,a}}2
=
c_a^{\rm raw}.
\]

Thus the model reproduces **exactly** the source norm and overlap data of v13.956.

---

## 4. Exact endpoint coherences in the countermodel [D]

The parity Stieltjes transforms are

\[
\boxed{
G_{a,+}(\delta)
=
\frac{M_{+,a}}{\delta},
}
\tag{7}
\]

\[
\boxed{
G_{a,-}(\delta)
=
\frac{M_{-,a}}{s_a+\delta}.
}
\tag{8}
\]

As

\[
\delta\downarrow0,
\]

\[
G_{a,+}(\delta)\to\infty,
\]

while \(G_{a,-}\) remains finite, so

\[
\boxed{
\kappa_a(0+)=1.
}
\tag{9}
\]

As

\[
\delta\to\infty,
\]

\[
\frac{G_{a,-}}{G_{a,+}}
\to
\frac{M_{-,a}}{M_{+,a}}.
\]

Therefore

\[
\kappa_a(\infty)
=
\frac{M_{+,a}-M_{-,a}}
{M_{+,a}+M_{-,a}}
=
\frac{c_a^{\rm raw}}{m_a}.
\]

Using the exact masses,

\[
\boxed{
\kappa_a(\infty)
=
\frac{4ae^{-2a}}
{1-e^{-4a}},
}
\tag{10}
\]

which is precisely the exact raw source coherence in v13.956.

So both endpoints are reproduced.

---

## 5. Exact critical regulator in the countermodel [D]

Equation (3) gives

\[
\frac{
M_{-,a}/(s_a+\delta_\tau)
}{
M_{+,a}/\delta_\tau
}
=
q_\tau.
\]

Hence

\[
M_{-,a}\delta_\tau
=
q_\tau M_{+,a}(s_a+\delta_\tau).
\]

Therefore

\[
\boxed{
\delta_\tau(a)
=
K_{a,\tau}\,s_a,
}
\tag{11}
\]

with

\[
\boxed{
K_{a,\tau}
=
\frac{
q_\tau M_{+,a}
}{
M_{-,a}-q_\tau M_{+,a}
}.
}
\tag{12}
\]

For every fixed \(\tau>0\), the denominator is positive for all sufficiently large \(a\), because

\[
\frac{M_{-,a}}{M_{+,a}}\to1
\]

and

\[
q_\tau<1.
\]

Moreover,

\[
\boxed{
K_{a,\tau}
\longrightarrow
\frac{q_\tau}{1-q_\tau}
=
\frac{e^\tau-1}{2}.
}
\tag{13}
\]

This recovers the doublet coefficient from v13.953, but here it appears inside a model whose odd spectral scale \(s_a\) is completely arbitrary.

---

## 6. \(N_a\delta_\tau\) is not fixed by the universal identities [D]

Let

\[
N_a=e^{2a}.
\]

Because

\[
\delta_\tau(a)
=
K_{a,\tau}s_a,
\]

we can choose:

### Subcritical scale

\[
s_a=N_a^{-2}.
\]

Then

\[
\boxed{
N_a\delta_\tau(a)\to0.
}
\tag{14}
\]

### Critical scale

\[
s_a=\frac{C}{N_a},
\qquad
C>0.
\]

Then

\[
\boxed{
N_a\delta_\tau(a)
\to
\frac{e^\tau-1}{2}C.
}
\tag{15}
\]

### Supercritical scale

\[
s_a=N_a^{-1/2}.
\]

Then

\[
\boxed{
N_a\delta_\tau(a)\to+\infty.
}
\tag{16}
\]

All three families have the same exact universal source masses and endpoint coherences.

Therefore:

\[
\boxed{
\textbf{the identities proved through v13.956 do not determine the scale of }\delta_\tau(a).
}
\tag{17}
\]

In particular, the exact zero-blind exponent of v13.950 is not by itself a theorem about the physical source-weighted regulator.

---

## 7. Exact \(N\)-scaled source-ratio function [D]

Define

\[
\boxed{
\Phi_a(c)
=
\frac{
G_{a,-}(c/N_a)
}{
G_{a,+}(c/N_a)
},
\qquad
c>0.
}
\tag{18}
\]

Let

\[
\boxed{
c_{a,\tau}
=
N_a\delta_\tau(a).
}
\tag{19}
\]

Because \(\delta_\tau\) is the first crossing of

\[
G_{a,-}(\delta)
=
q_\tau G_{a,+}(\delta),
\]

we obtain the exact equivalence

\[
\boxed{
c_{a,\tau}
=
\text{first positive crossing of }
\Phi_a(c)=q_\tau.
}
\tag{20}
\]

Thus the \(N^{-1}\) critical-scale question is exactly a scaled source-resolvent-ratio question.

---

## 8. Source-RG fixed-point theorem [D/C]

Assume there exists a continuous function

\[
\Phi:(0,\infty)\to[0,\infty)
\]

such that

\[
\boxed{
\Phi_a\to\Phi
}
\tag{H1}
\]

locally uniformly on \((0,\infty)\).

Assume further that for the chosen \(\tau\):

1. \(\Phi(c)=q_\tau\) has a unique first positive solution
   \[
   C_\tau\in(0,\infty);
   \]

2. the crossing is strict, i.e. there exists \(\varepsilon>0\) such that
   \[
   \Phi(c)<q_\tau
   \quad
   (0<c<C_\tau-\varepsilon),
   \]
   and
   \[
   \Phi(c)>q_\tau
   \quad
   (C_\tau+\varepsilon<c<C_\tau+2\varepsilon)
   \]
   after shrinking the neighborhood if necessary.

Then first-crossing stability under local uniform convergence gives

\[
\boxed{
N_a\delta_\tau(a)
=
c_{a,\tau}
\longrightarrow
C_\tau.
}
\tag{21}
\]

This is the exact source-RG criterion for a finite nonzero \(N^{-1}\) double-scaling law.

No isolated eigenvalue, one-pole approximation, or fixed-rank moat is needed.

---

## 9. Pushed-forward source spectral measures [D]

Define the \(N_a\)-scaled parity source measures

\[
\boxed{
\widehat\sigma_{a,\pm}
=
(\lambda\mapsto N_a\lambda)_*
\sigma_{a,\pm}.
}
\tag{22}
\]

Then

\[
G_{a,\pm}(c/N_a)
=
N_a
\int_0^\infty
\frac{
d\widehat\sigma_{a,\pm}(u)
}{
u+c
}.
\]

Hence

\[
\boxed{
\Phi_a(c)
=
\frac{
\displaystyle
\int (u+c)^{-1}d\widehat\sigma_{a,-}(u)
}{
\displaystyle
\int (u+c)^{-1}d\widehat\sigma_{a,+}(u)
}.
}
\tag{23}
\]

Thus H1 is exactly a statement that the **ratio of the two scaled source Stieltjes transforms** has a cutoff-free limit.

The common overall amount of low-energy source mass may vanish; it cancels in the ratio.

This is why a nonzero limiting total source mass is not required.

---

## 10. Critical matrix-state tightness criterion [D]

At the intrinsic critical regulator

\[
\delta_a:=\delta_\tau(a),
\]

v13.956 defines

\[
d\Pi_{a,\tau}(\lambda)
=
\frac1{R_a(\delta_a)}
\frac{d\Sigma_a(\lambda)}
{\lambda+\delta_a}.
\]

Push this measure to

\[
u=N_a\lambda.
\]

Write the resulting matrix measure as

\[
d\widetilde\Pi_{a,\tau}(u).
\]

Its total matrix is exactly

\[
\begin{pmatrix}
1&e^{-\tau}\\
e^{-\tau}&1
\end{pmatrix}.
\]

Because the matrix measure is positive semidefinite, tightness is equivalent to tightness of either diagonal measure.

Define the diagonal tail

\[
\boxed{
T_{a,\tau}(M)
=
\frac1{R_a(\delta_a)}
\int_{N_a\lambda>M}
\frac{
d\rho_a(\lambda)
}{
\lambda+\delta_a
}.
}
\tag{24}
\]

Then

\[
\boxed{
\{\widetilde\Pi_{a,\tau}\}
\text{ is tight on }[0,\infty)
\iff
\lim_{M\to\infty}
\sup_a
T_{a,\tau}(M)
=
0.
}
\tag{25}
\]

Thus the no-escape condition is an exact resolvent-weighted tail criterion.

---

## 11. Limit matrix measure under source-RG convergence [C]

Suppose:

1. \(c_{a,\tau}\to C_\tau\in(0,\infty)\);
2. the pushed-forward source matrix measures have a Stieltjes-scale limit after any necessary common scalar normalization;
3. the critical weighted family is tight in the sense of (25).

Then every subsequential limit has the form

\[
\boxed{
d\Pi_{\infty,\tau}(u)
=
\frac1{r_\tau}
\frac{
d\Sigma_\infty(u)
}{
u+C_\tau
},
}
\tag{26}
\]

where

\[
r_\tau
=
\int
\frac{
d\rho_\infty(u)
}{
u+C_\tau
},
\]

and the total matrix is

\[
\boxed{
\begin{pmatrix}
1&e^{-\tau}\\
e^{-\tau}&1
\end{pmatrix}.
}
\tag{27}
\]

The limiting measure may be atomic, clustered, or continuous.

The overlap selector itself does not distinguish those cases.

---

## 12. Source-capacity duality [D]

For either parity, let

\[
T_{a,\pm}(\delta)
=
B_a^{(\pm)}+\delta I.
\]

Let \(f_{\pm,a}\) be the parity source vectors of v13.956.

For any strictly positive self-adjoint \(T\),

\[
\langle f,T^{-1}f\rangle
=
\sup_{g\ne0}
\frac{
|\langle f,g\rangle|^2
}{
\langle g,Tg\rangle
}.
\]

Therefore define the source capacity

\[
\boxed{
\mathcal C_{a,\pm}(\delta)
=
\inf_{\langle f_{\pm,a},g\rangle=1}
\left[
\langle g,B_a^{(\pm)}g\rangle
+
\delta\|g\|_2^2
\right].
}
\tag{28}
\]

Then

\[
\boxed{
\mathcal C_{a,\pm}(\delta)
=
\frac1{
G_{a,\pm}(\delta)
}.
}
\tag{29}
\]

Hence the intrinsic critical equation is exactly

\[
\boxed{
\frac{
\mathcal C_{a,+}(\delta_\tau)
}{
\mathcal C_{a,-}(\delta_\tau)
}
=
q_\tau.
}
\tag{30}
\]

This is a useful source-faithful variational formulation.

The selector is therefore a ratio of **source-constrained low-energy capacities**, not a ratio of isolated eigenvalues.

---

## 13. Relation to the zero-blind stopband theorem [G]

v13.950 proves the exact zero-blind variational exponent

\[
\bar\sigma_1=1.
\]

That theorem controls the best whole-stopband suppression available to an admissible filter.

The present countermodel shows that this information alone does not fix the physical source-resolvent ratio

\[
\Phi_a(c).
\]

Thus:

\[
\boxed{
\textbf{zero-blind variational scaling and physical source-RG scaling are distinct statements.}
}
\tag{31}
\]

To identify them, one must prove a theorem connecting the actual source capacities or scaled source spectral measures to the zero-blind extremal class.

That connection is currently open.

---

## 14. Next nonredundant gate [O]

The next task is now sharply localized:

\[
\boxed{
\textbf{derive the large-}a\textbf{ limit of }
\Phi_a(c)
=
\frac{G_{a,-}(c/N_a)}{G_{a,+}(c/N_a)}
\textbf{ directly from Suzuki's source-faithful operator.}
}
\]

Equivalent formulations are:

1. source Stieltjes ratio convergence;
2. parity source-capacity ratio convergence;
3. tightness and convergence of the critical matrix state.

If the limit exists and has a unique first crossing \(C_\tau\), then

\[
\boxed{
N_a\delta_\tau(a)\to C_\tau
}
\]

follows automatically.

---

## 15. Result

The universal source matrix of v13.956 does **not** by itself determine the critical energy scale.

An explicit positive two-atom model reproduces all known source masses and endpoint coherences while allowing

\[
N_a\delta_\tau(a)\to0,
\]

or

\[
N_a\delta_\tau(a)\to C\in(0,\infty),
\]

or

\[
N_a\delta_\tau(a)\to\infty.
\]

The correct \(N^{-1}\) scaling theorem is therefore:

\[
\boxed{
\Phi_a(c)
=
\frac{
G_{a,-}(c/N_a)
}{
G_{a,+}(c/N_a)
}
\to
\Phi(c)
}
\]

with a unique strict first crossing

\[
\Phi(C_\tau)=q_\tau.
\]

Under that hypothesis,

\[
\boxed{
N_a\delta_\tau(a)\to C_\tau.
}
\]

The selector has now been reduced to a source-RG fixed-point problem for the two parity resolvent capacities.
