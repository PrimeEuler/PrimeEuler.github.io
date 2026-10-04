# Cone Derivation Ledger v13.994 — Rank-One Source-Capacity Inertia Crossing and Protected-Cutoff Plateau

**Date:** 2026-10-04  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [D] exact rank-one positivity/inertia characterization of source capacity; [D] exact Schur transfer of the capacity crossing to the protected core; [N] protected bulk-subtracted source scalar extended from N=96 through N=192; [G] raw rho=0 and endpoint-shifted direct inversions are rejected as the wrong certification objects; [O] adapt the theorem-scale M3999/4000 outward inertia machinery to the rank-one source-capacity crossing.  
**Parents:** v13.798–801, v13.823–832, v13.958, v13.966, v13.971, v13.987–993.  
**New diagnostic workflow commits:** 432908655c4a1208eb5c94bba779a314c5a2bf02 and dce2a2322a77e99e6a316dce46919844b895fab0.  
**Collision check:** immediately before this write, live HEAD was dce2a2322a77e99e6a316dce46919844b895fab0; no v13.994 entry was present.

---

## 0. Purpose

v13.987 showed that certifying the absolute inverse of the corrected six-dimensional source matrix is numerically hopeless under the current perturbation budget.

v13.991–993 then showed that normalized source observables are projective and that common determinant factors can be cancelled before KKT/Feshbach elimination.

The present entry gives a second exact inverse-free formulation tailored to the project's strongest existing proof technology: inertia.

For a positive source operator, the reciprocal source energy is exactly the unique rank-one perturbation strength at which positivity is lost.

Thus the Xi scalar can be encoded by two rank-one positivity thresholds rather than two huge source inverses.

---

## 1. Source-capacity threshold theorem [D]

Let \(T>0\) be a strictly positive self-adjoint operator and let \(f\neq0\).

Define

\[
G(T,f)=\langle f,T^{-1}f\rangle
\]

and the source capacity

\[
\boxed{
\mathcal C(T,f)=\frac1{G(T,f)}.
}
\tag{1}
\]

Equivalently, as already used in v13.958,

\[
\mathcal C(T,f)
=
\inf_{\langle f,x\rangle=1}
\langle x,Tx\rangle.
\]

Set

\[
u=T^{-1/2}f.
\]

Then

\[
T-\mu ff^*
=
T^{1/2}
\left(
I-\mu uu^*
\right)
T^{1/2}.
\]

The rank-one operator \(I-\mu uu^*\) has one exceptional eigenvalue

\[
1-\mu\|u\|^2
=
1-\mu G(T,f).
\]

Therefore

\[
\boxed{
T-\mu ff^*\succeq0
\iff
0\le\mu\le\mathcal C(T,f).
}
\tag{2}
\]

At the unique threshold

\[
\mu=\mathcal C(T,f),
\]

\[
\boxed{
\ker(T-\mu ff^*)
=
\operatorname{span}\{T^{-1}f\}.
}
\tag{3}
\]

For

\[
\mu>\mathcal C(T,f),
\]

the rank-one perturbation creates exactly one negative direction:

\[
\boxed{
\operatorname{ind}_{-}(T-\mu ff^*)=1.
}
\tag{4}
\]

Hence

\[
\boxed{
\mathcal C(T,f)
=
\sup\{\mu\ge0:T-\mu ff^*\succeq0\}.
}
\tag{5}
\]

This converts the source-resolvent scalar into an inertia crossing.

---

## 2. Exact parity formula for the Xi scalar [D]

At the absolute Suzuki shift \(\lambda=0\), let

\[
G_e=\langle f_e,A_e^{-1}f_e\rangle,
\qquad
G_o=\langle f_o,A_o^{-1}f_o\rangle,
\]

and

\[
\mathcal C_e=G_e^{-1},
\qquad
\mathcal C_o=G_o^{-1}.
\]

Then the finite Xi scalar of v13.966 is

\[
\kappa_a^\Xi
=
\frac{G_e-G_o}{G_e+G_o}.
\]

Therefore

\[
\boxed{
\frac{G_o}{G_e}
=
\frac{\mathcal C_e}{\mathcal C_o},
}
\tag{6}
\]

and

\[
\boxed{
\kappa_a^\Xi
=
\frac{\mathcal C_o-\mathcal C_e}
{\mathcal C_o+\mathcal C_e}.
}
\tag{7}
\]

Equivalently,

\[
\boxed{
q_a^\Xi
:=
\frac{\mathcal C_e}{\mathcal C_o}
=
\frac{1-\kappa_a^\Xi}{1+\kappa_a^\Xi}.
}
\tag{8}
\]

Thus the source scalar is exactly a ratio of two rank-one inertia thresholds.

No separate estimate of either \(\|A_e^{-1}\|\) or \(\|A_o^{-1}\|\) is conceptually required.

---

## 3. Schur transfer of the rank-one crossing [D]

Split one parity operator into a protected block \(P\) and a complement \(Q\):

\[
T
=
\begin{pmatrix}
A&E^*\\
E&D
\end{pmatrix},
\qquad
f=
\binom{f_P}{f_Q},
\]

with

\[
D>0.
\]

Define the ordinary Schur data

\[
\boxed{
S=A-E^*D^{-1}E,
}
\tag{9}
\]

\[
\boxed{
g=f_P-E^*D^{-1}f_Q,
}
\tag{10}
\]

and

\[
\boxed{
h=f_Q^*D^{-1}f_Q.
}
\tag{11}
\]

The standard block congruence sends

\[
T\mapsto S\oplus D
\]

and simultaneously sends the source to

\[
f\mapsto(g,f_Q)^T.
\]

Now consider

\[
T_\mu=T-\mu ff^*.
\]

If

\[
\mu h<1,
\]

then

\[
D-\mu f_Qf_Q^*>0
\]

and Sherman–Morrison gives

\[
(D-\mu f_Qf_Q^*)^{-1}
=
D^{-1}
+
\frac{\mu}{1-\mu h}
D^{-1}f_Qf_Q^*D^{-1}.
\]

Taking the Schur complement of the lower block yields exactly

\[
\boxed{
S_\mu
=
S-
\frac{\mu}{1-\mu h}
gg^*.
}
\tag{12}
\]

Therefore

\[
\boxed{
T-\mu ff^*\succeq0
\iff
\left[
\mu h<1
\ \text{and}\
S-\frac{\mu}{1-\mu h}gg^*\succeq0
\right].
}
\tag{13}
\]

The source-capacity crossing has therefore been transferred exactly to a rank-one perturbation of the protected Schur core.

---

## 4. Core threshold and source-energy decomposition [D]

Assume also

\[
S>0.
\]

Define

\[
r=g^*S^{-1}g.
\]

The ordinary block inverse identity gives

\[
\boxed{
G(T,f)=h+r.
}
\tag{14}
\]

Hence

\[
\boxed{
\mathcal C(T,f)=\frac1{h+r}.
}
\tag{15}
\]

At the capacity threshold

\[
\mu=\mathcal C(T,f),
\]

the Schur rank-one coefficient in (12) is

\[
\frac{\mu}{1-\mu h}
=
\frac1r.
\]

Therefore the exact core crossing is

\[
\boxed{
S-\frac1rgg^*\succeq0
}
\]

with one-dimensional kernel.

Equivalently,

\[
\boxed{
r^{-1}
=
\sup\{\alpha\ge0:S-\alpha gg^*\succeq0\}.
}
\tag{16}
\]

This is the load-bearing reformulation for the current project.

The large source energy is not to be certified by first bounding \(S^{-1}\). Instead, one certifies the rank-one loss-of-positivity threshold of the already protected core.

---

## 5. Why this matches the existing M3999 architecture [I]

The theorem-scale endpoint program v13.806–832 already has the exact ingredients needed for this style of proof:

1. large finite buffers eliminated by structured LDL plus the exact parity rank-one pole;
2. frozen low-dimensional core coordinates;
3. outward finite-solve residual budgets;
4. exact/dyadic rank checks and Cholesky preconditioners;
5. remote residual Gram accumulation through two million;
6. analytic far-tail envelopes;
7. large certified remote positivity floors.

Those certificates were used to prove inertia statements without controlling a large indefinite inverse.

The present theorem says the source scalar can be attacked in the same language:

\[
\boxed{
\text{source energy}
\quad\longrightarrow\quad
\text{rank-one capacity crossing}
\quad\longrightarrow\quad
\text{protected-core inertia}.
}
\]

The new task is therefore not to stabilize the v13.987 six-dimensional inverse.

It is to build an outward rank-one crossing certificate in protected coordinates.

---

## 6. Direct pre-KKT inversion diagnostic fails for the right reason [N/G]

A direct full-section \(\rho=0\) structured solve was tested before any KKT elimination.

Already at the even cutoff near mode \(499\), the exact parity-pole Woodbury denominator is only about

\[
\boxed{
7.8\times10^{-16}.
}
\]

Thus the raw finite section is already sitting on the protected near-kernel geometry.

This is not a useful direct inversion route and no scalar was promoted from it.

The failure is consistent with the exact rank-four \(P_4\) resonance theorem.

---

## 7. Generalized-endpoint regularization is not the Suzuki source operator [N/G]

A second diagnostic replaced the source matrix by

\[
A+\delta B_{\rm sm}
\]

using the audited endpoint-pencil machinery.

The cutoff dependence was numerically stable, but the resulting parity quadratic forms were negative.

Therefore this regularization is not the positive Suzuki source operator \(T_a=A_a-\lambda I\) and its numerical ratios are not source-capacity values.

No \(\kappa_a^\Xi\) claim is made from that sweep.

This guardrail prevents confusing generalized endpoint flow with the absolute-\(\lambda=0\) source problem.

---

## 8. Protected bulk-subtracted source scalar through N=192 [N]

The source-faithful high-precision bulk-subtracted/Feshbach diagnostic of v13.801 was replayed unchanged at larger cutoffs.

Previously:

\[
\kappa_{0,64}
\approx
0.9999369812174818709,
\]

\[
\kappa_{0,96}
\approx
0.9999287562314239928.
\]

The new runs give

\[
\boxed{
\kappa_{0,128}
\approx
0.9999324709903608021,
}
\tag{17}
\]

\[
\boxed{
\kappa_{0,160}
\approx
0.9999311873429423731,
}
\tag{18}
\]

\[
\boxed{
\kappa_{0,192}
\approx
0.9999295337492060076.
}
\tag{19}
\]

For \(N=96,128,160,192\), the full spread is only

\[
\boxed{
3.72\times10^{-6}.
}
\tag{20}
\]

Thus the finite-\(a=1\) protected scalar is displaying a genuine \(0.99993\)-scale plateau over these cutoffs.

This is still a numerical finite-section diagnostic, not a cutoff-convergence theorem.

---

## 9. Source-energy anatomy remains four-channel dominated [N]

At \(N=128\),

\[
G_e\approx1.10110\times10^{29},
\qquad
G_o\approx3.71793\times10^{24}.
\]

At \(N=160\),

\[
G_e\approx1.11481\times10^{29},
\qquad
G_o\approx3.83579\times10^{24}.
\]

At \(N=192\),

\[
G_e\approx1.14526\times10^{29},
\qquad
G_o\approx4.03524\times10^{24}.
\]

The tail-source energy fractions carried by the first four relative resonances remain

\[
>0.99999999999999
\]

in even-v and about

\[
0.9999999999998
\]

in odd-v.

The two-dimensional low-core energy fraction remains above

\[
0.9999992
\]

in both sectors.

Thus the old v13.801 anatomy persists:

\[
\boxed{
\text{four tail resonances}
\longrightarrow
\text{two-mode low-core amplification}.
}
\tag{21}
\]

This is exactly the anatomy later promoted basis-free in v13.823.

---

## 10. Capacity diagnostics [N]

The \(N=192\) source energies correspond nominally to

\[
\mathcal C_e
\approx
8.73\times10^{-30},
\]

\[
\mathcal C_o
\approx
2.48\times10^{-25}.
\]

Their ratio is

\[
\frac{\mathcal C_e}{\mathcal C_o}
\approx
3.52\times10^{-5},
\]

which reproduces (19) through (7).

These tiny absolute thresholds explain why ordinary entrywise perturbation of the source matrix is the wrong proof norm.

The protected-core rank-one crossing must be normalized before outward certification.

---

## 11. Relation to the infinite Xi target [G]

The infinite target is

\[
\kappa_\Xi
\approx
0.9968019520324009035.
\]

The finite \(a=1\) plateau near

\[
0.99993
\]

is not expected, by itself, to equal the \(a\to\infty\) target.

v13.962 identifies the no-twist Xi branch at each finite \(a\) with the absolute shift \(\lambda=0\), while the remaining theorem is finite-\(a\)-to-Xi convergence as \(a\to\infty\).

Therefore the present cutoff plateau is evidence that the **finite \(a=1\) scalar is numerically well-defined**, not evidence that the infinite Xi limit has already been reached.

---

## 12. Separate stable consumer at z=i [O]

v13.966 also gives the exact equivalent formula

\[
\boxed{
\kappa_a^\Xi
=
-i\,\operatorname{Tr}
\left[
(H_{a,0}-i)^{-1}
-
(H_{a,\pi}-i)^{-1}
\right].
}
\tag{22}
\]

Because \(H_{a,0}\) and \(H_{a,\pi}\) are self-adjoint,

\[
\|(H_{a,\theta}-i)^{-1}\|\le1.
\]

Thus the \(z=i\) rank-one trace remains a potentially even more stable consumer.

However the repository currently has the exact abstract boundary-triple realization, not yet a source-faithful numerical discretization of both energy-space extensions suitable for an outward trace certificate.

The capacity/inertia route is presently closer to the existing certified finite-form machinery.

---

## 13. Next proof gate [O]

Construct a theorem-scale source-capacity verifier by adapting the M3999/4000 outward architecture.

For each parity:

1. place the dangerous source-carrying modes inside a frozen protected finite block;
2. retain only the stiff \(n>4000\) remote complement;
3. include the rank-one source perturbation
   \[
   -\mu ff^*;
   \]
4. Schur-eliminate the stiff remote block using (12);
5. normalize the protected core so that the capacity crossing is \(O(1)\);
6. outward-certify two values
   \[
   \mu_-<\mathcal C<\mu_+
   \]
   by opposite inertia statements;
7. combine the even/odd capacity intervals through
   \[
   \kappa
   =
   \frac{\mathcal C_o-\mathcal C_e}
   {\mathcal C_o+\mathcal C_e}.
   \]

The aim is an interval for the projective scalar without ever proving a global bound on \(A^{-1}\).

---

## 14. Result

For every strictly positive source operator,

\[
\boxed{
\mathcal C(T,f)
=
\sup\{\mu:T-\mu ff^*\succeq0\}
=
\frac1{\langle f,T^{-1}f\rangle}.
}
\]

Under an arbitrary protected/complement split, the capacity crossing transfers exactly to

\[
\boxed{
S-
\frac{\mu}{1-\mu h}
gg^*.
}
\]

Therefore the no-twist Xi scalar is exactly a ratio of two rank-one inertia thresholds.

This formulation is compatible with the strongest source-faithful certificate machinery already present in the repository and avoids the v13.987 absolute inverse-stability obstruction.
