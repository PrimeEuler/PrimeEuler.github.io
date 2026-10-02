# Cone Derivation Ledger v13.966 — Sandbox: Xi-Branch Scalar as Cayley Matrix Coefficient, Rank-One Resolvent Trace, and First de Branges–Rovnyak Jet

**Date:** 2026-10-02  
**Track:** Sandbox / no-twist Suzuki Xi scalar lane  
**Status:** [D] four exact equivalent scalar representations; [D] exact first-kernel-jet defect; [D] minimal convergence theorem for the scalar; [G] strictly weaker than full Weyl/de Branges convergence; [O] certify the one-point rank-one resolvent trace / defect-vector convergence  
**Authorization:** Jeremy, 2026-10-02 ("yep. lets hit that scalar")  
**Parents:** v13.661, v13.677, v13.682–684, v13.789–793, v13.798, v13.800, v13.962, v13.963; External Audit Round 147 confirms v13.958–963  
**Collision check:** v13.964 was absent immediately before this entry was first written, but was independently claimed by "External Audit Round 147" (commit `1283012`, pushed 2026-10-02T17:53:00Z), which this entry's own commit (`119de2a`, 2026-10-02T18:06:09Z) postdates. Per the standing collision protocol, the earlier commit keeps the contested number; this entry has therefore been renumbered v13.964→v13.966 by the external audit thread (filename and this header only — no mathematical content changed). v13.965, written after this entry under its original v13.964 label, has had its references updated to v13.966 accordingly.

---

## 0. Goal

On the no-twist Xi branch, v13.962 fixes the finite regulator exactly:

\[
\delta_\Xi(a)=\lambda_a,
\]

equivalently the absolute Suzuki shift is

\[
\lambda_{\rm abs}=0.
\]

The scalar target is

\[
\boxed{
\kappa_a^\Xi
=
h_{a,\lambda=0}(i)
=
m_{a,\lambda=0}'(i).
}
\]

The infinite Xi target is

\[
\boxed{
\kappa_\Xi
=
\frac{\xi''(3/2)}{\xi'(3/2)}
-
\frac{\xi'(3/2)}{\xi(3/2)}
\approx
0.9968019520324009035288967048.
}
\]

The question is whether this scalar can be attacked without proving full finite-to-infinite Weyl convergence.

It can.

---

## 1. Boundary-triple normalization at the canonical point [D]

Let

\[
H_{a,\pi}
\]

denote the \(\theta=\pi\) reference self-adjoint extension for the finite scalar boundary triple, with Weyl function \(m_a\) and gamma field \(\gamma_a\).

The source-fixed normalization gives

\[
\boxed{
m_a(i)=i.
}
\tag{1}
\]

The ordinary boundary-triple kernel identity is

\[
\boxed{
m_a(z)-\overline{m_a(w)}
=
(z-\bar w)
\langle
\gamma_a(z),
\gamma_a(w)
\rangle.
}
\tag{2}
\]

Setting

\[
w=i
\]

gives

\[
\boxed{
K_a^m(i,z)
:=
\langle
\gamma_a(z),
\gamma_a(i)
\rangle
=
\frac{m_a(z)+i}{z+i}.
}
\tag{3}
\]

At \(z=i\),

\[
\boxed{
\|\gamma_a(i)\|^2
=
K_a^m(i,i)
=
1.
}
\tag{4}
\]

Thus the canonical defect vector is already norm-normalized.

---

## 2. First gamma-kernel jet equals the Schur scalar [D]

Differentiate (3) in \(z\).

At \(z=i\),

\[
\begin{aligned}
\left.
\partial_zK_a^m(i,z)
\right|_{z=i}
&=
\frac{
m_a'(i)(2i)-2i
}{
(2i)^2
}\\
&=
\frac{i}{2}
\left[
1-m_a'(i)
\right].
\end{aligned}
\]

Since

\[
\kappa_a^\Xi=m_a'(i),
\]

we obtain

\[
\boxed{
\left.
\partial_zK_a^m(i,z)
\right|_{z=i}
=
\frac{i}{2}
(1-\kappa_a^\Xi).
}
\tag{5}
\]

Equivalently,

\[
\boxed{
\kappa_a^\Xi
=
1+
2i
\left.
\partial_zK_a^m(i,z)
\right|_{z=i}.
}
\tag{6}
\]

Thus the scalar is the **first normalized gamma-kernel jet at the canonical point**.

The diagonal kernel value itself is identically \(1\) and contains no scalar information.

---

## 3. Cayley matrix-coefficient formula [D]

The gamma-field resolvent identity at base point \(i\) is

\[
\gamma_a(z)
=
\left[
I+
(z-i)(H_{a,\pi}-z)^{-1}
\right]
\gamma_a(i).
\]

Therefore

\[
\boxed{
\gamma_a'(i)
=
(H_{a,\pi}-i)^{-1}
\gamma_a(i).
}
\tag{7}
\]

Using (5),

\[
\boxed{
\left\langle
(H_{a,\pi}-i)^{-1}
\gamma_a(i),
\gamma_a(i)
\right\rangle
=
\frac{i}{2}
(1-\kappa_a^\Xi).
}
\tag{8}
\]

Define the adjoint Cayley unitary

\[
\boxed{
U_{a,\pi}^*
:=
(H_{a,\pi}+i)(H_{a,\pi}-i)^{-1}.
}
\tag{9}
\]

Since

\[
U_{a,\pi}^*
=
I+
2i(H_{a,\pi}-i)^{-1},
\]

and \(\|\gamma_a(i)\|=1\),

\[
\boxed{
\kappa_a^\Xi
=
\langle
U_{a,\pi}^*
\gamma_a(i),
\gamma_a(i)
\rangle.
}
\tag{10}
\]

So the Xi scalar is exactly **one normalized Cayley-transform matrix coefficient**.

No full Weyl function is needed.

---

## 4. Fixed-pair rank-one resolvent-trace formula [D]

Let

\[
H_{a,0}
\]

denote the \(\theta=0\) self-adjoint extension.

Relative to \(H_{a,\pi}\), the scalar Krein formula is

\[
(H_{a,0}-z)^{-1}
-
(H_{a,\pi}-z)^{-1}
=
-
\gamma_a(z)
m_a(z)^{-1}
\gamma_a(\bar z)^*.
\]

At

\[
z=i,
\qquad
m_a(i)=i,
\]

the coefficient is

\[
-\frac1i=i.
\]

The rank-one trace is therefore

\[
\operatorname{Tr}
\left[
(H_{a,0}-i)^{-1}
-
(H_{a,\pi}-i)^{-1}
\right]
=
i\,
\langle
\gamma_a(i),
\gamma_a(-i)
\rangle.
\]

By the canonical deficiency-overlap identity of v13.791,

\[
\langle
\gamma_a(i),
\gamma_a(-i)
\rangle
=
\kappa_a^\Xi.
\]

Hence

\[
\boxed{
\kappa_a^\Xi
=
-i\,
\operatorname{Tr}
\left[
(H_{a,0}-i)^{-1}
-
(H_{a,\pi}-i)^{-1}
\right].
}
\tag{11}
\]

This is a one-point, rank-one, trace-class observable.

---

## 5. Perturbation-determinant derivative [D]

The normalized ordered-pair perturbation determinant is

\[
\boxed{
\Delta_{0/\pi}^{(a)}(z;i)
=
\frac{
m_a(z)
}{
m_a(i)
}
=
\frac{m_a(z)}i.
}
\tag{12}
\]

Therefore

\[
\left.
\partial_z
\log
\Delta_{0/\pi}^{(a)}(z;i)
\right|_{z=i}
=
\frac{
m_a'(i)
}{
m_a(i)
}
=
-i\kappa_a^\Xi.
\]

Thus

\[
\boxed{
\kappa_a^\Xi
=
i
\left.
\partial_z
\log
\Delta_{0/\pi}^{(a)}(z;i)
\right|_{z=i}.
}
\tag{13}
\]

Using the standard determinant/resolvent identity,

\[
-\partial_z\log\Delta_{0/\pi}
=
\operatorname{Tr}
[
(H_{a,0}-z)^{-1}
-
(H_{a,\pi}-z)^{-1}
],
\]

equation (13) is exactly equivalent to (11).

---

## 6. Canonical disk Schur derivative [D]

Let

\[
s_a(z)
=
\frac{
m_a(z)-i
}{
m_a(z)+i
}.
\]

Because

\[
m_a(i)=i,
\]

\[
\boxed{
s_a(i)=0.
}
\tag{14}
\]

Differentiate:

\[
s_a'(i)
=
-\frac{i}{2}
m_a'(i).
\]

Hence

\[
\boxed{
\kappa_a^\Xi
=
2i\,s_a'(i).
}
\tag{15}
\]

Now use the canonical Cayley coordinate

\[
\boxed{
z
=
i
\frac{1+\zeta}{1-\zeta},
}
\tag{16}
\]

and define

\[
\widetilde s_a(\zeta)
=
s_a
\left(
i\frac{1+\zeta}{1-\zeta}
\right).
\]

Since

\[
\frac{dz}{d\zeta}\Big|_{\zeta=0}
=
2i,
\]

we get

\[
\boxed{
\widetilde s_a(0)=0,
\qquad
\widetilde s_a'(0)
=
\kappa_a^\Xi.
}
\tag{17}
\]

Thus \(\kappa_a^\Xi\) is exactly the signed Schwarz–Pick derivative at the canonical disk origin.

For the present reflection-real normalization,

\[
\kappa_a^\Xi\in(-1,1).
\]

---

## 7. First de Branges–Rovnyak kernel-jet defect [D]

The canonical disk de Branges–Rovnyak kernel is

\[
\boxed{
\mathcal K_a(\zeta,\omega)
=
\frac{
1-
\widetilde s_a(\zeta)
\overline{
\widetilde s_a(\omega)
}
}{
1-\zeta\bar\omega
}.
}
\tag{18}
\]

Using

\[
\widetilde s_a(\zeta)
=
\kappa_a^\Xi\zeta
+
O(\zeta^2),
\]

we obtain

\[
\mathcal K_a(\zeta,\omega)
=
1+
\boxed{
\left[
1-(\kappa_a^\Xi)^2
\right]
}
\zeta\bar\omega
+
O(
|\zeta|^2|\omega|
+
|\zeta||\omega|^2
).
\tag{19}
\]

Therefore the first positive jet defect is

\[
\boxed{
\partial_\zeta
\partial_{\bar\omega}
\mathcal K_a(0,0)
=
1-(\kappa_a^\Xi)^2.
}
\tag{20}
\]

The infinite Xi target is

\[
\boxed{
1-\kappa_\Xi^2
\approx
0.00638586842439512823061433397.
}
\tag{21}
\]

This is a manifestly nonnegative, gauge-free scalar certification target.

---

## 8. Capacity ratio equivalence [D]

At absolute shift \(\lambda=0\), let

\[
G_{a,+}^{\Xi}
=
\langle
f_{+,a},
A_a^{-1}f_{+,a}
\rangle,
\]

\[
G_{a,-}^{\Xi}
=
\langle
f_{-,a},
A_a^{-1}f_{-,a}
\rangle.
\]

Then

\[
\boxed{
\kappa_a^\Xi
=
\frac{
G_{a,+}^{\Xi}
-
G_{a,-}^{\Xi}
}{
G_{a,+}^{\Xi}
+
G_{a,-}^{\Xi}
}.
}
\tag{22}
\]

Equivalently, with source capacities

\[
\mathcal C_{a,\pm}^{\Xi}
=
1/G_{a,\pm}^{\Xi},
\]

\[
\boxed{
q_a^\Xi
:=
\frac{
\mathcal C_{a,+}^{\Xi}
}{
\mathcal C_{a,-}^{\Xi}
}
=
\frac{
1-\kappa_a^\Xi
}{
1+\kappa_a^\Xi
}.
}
\tag{23}
\]

Thus

\[
\boxed{
\kappa_a^\Xi
=
\frac{
1-q_a^\Xi
}{
1+q_a^\Xi
}.
}
\tag{24}
\]

The infinite target is

\[
\boxed{
q_\Xi
\approx
0.00160158495655717571706007324.
}
\tag{25}
\]

The kernel-jet defect can also be written

\[
\boxed{
1-(\kappa_a^\Xi)^2
=
\frac{
4q_a^\Xi
}{
(1+q_a^\Xi)^2
}.
}
\tag{26}
\]

---

## 9. Minimal scalar convergence theorem [D/C]

Assume there are isometric embeddings

\[
J_a:
\mathcal H_{a,\rm simple}
\to
\mathcal H_{\infty,\rm simple}
\]

such that:

### (S1) reference-extension convergence

\[
\boxed{
J_a
(H_{a,\pi}-i)^{-1}
J_a^*
\to
(H_{\infty,\pi}-i)^{-1}
}
\tag{S1}
\]

strongly on the limiting simple space;

### (S2) one canonical defect-vector convergence

\[
\boxed{
J_a\gamma_a(i)
\to
\gamma_\infty(i)
}
\tag{S2}
\]

strongly.

Then by (10),

\[
\boxed{
\kappa_a^\Xi
\to
\kappa_\Xi.
}
\tag{27}
\]

Proof: strong resolvent convergence gives strong convergence of the bounded Cayley transforms

\[
U_{a,\pi}^*
\to
U_{\infty,\pi}^*.
\]

Combining with the strong convergence of the unit defect vectors gives convergence of the matrix coefficients.

This package is strictly weaker than local-uniform convergence of \(m_a\).

---

## 10. Even weaker rank-one trace criterion [D/C]

The scalar convergence follows if one proves directly

\[
\boxed{
\operatorname{Tr}
\left[
(H_{a,0}-i)^{-1}
-
(H_{a,\pi}-i)^{-1}
\right]
\to
\operatorname{Tr}
\left[
(H_{\infty,0}-i)^{-1}
-
(H_{\infty,\pi}-i)^{-1}
\right].
}
\tag{28}
\]

Because each difference is rank one, trace-norm convergence is sufficient but not necessary.

Only convergence of the single trace is required.

Therefore the minimal scalar target may be stated as

\[
\boxed{
\textbf{convergence of one rank-one resolvent-difference trace at }z=i.
}
\tag{29}
\]

This is much weaker than convergence of either full resolvent family.

---

## 11. Relation to the older obstruction [D/G]

v13.682 showed that strong resolvent convergence of the single reference extension does not determine the whole Weyl function because

\[
m(z)\mapsto m(z)+r
\]

leaves \(H_\pi\) unchanged.

For the present scalar branch, however,

\[
m_a(i)=i
\]

is already fixed exactly.

Moreover, \(m_a'(i)\) is invariant under additive real shifts of \(m\).

Therefore the additive-boundary-origin obstruction does not affect \(\kappa_a^\Xi\).

This explains why the scalar problem is genuinely easier than full Weyl convergence.

---

## 12. Existing finite-section evidence [N/G]

At \(a=1,\lambda=0\), v13.798 and v13.800 report source-faithful protected finite-section values including

\[
\kappa_{0,16}
\approx
0.9986559003076436730,
\]

and

\[
\kappa_{0,32}
\approx
0.9992230376149196806.
\]

The cutoff sequence through \(N=32\) is nonmonotone and not converged.

The important numerical fact is not proximity to the target.

It is that the fixed-cutoff source-resolvent scalar can be evaluated stably after protected/Feshbach reduction even when the separate inverse problems are extremely ill-conditioned.

The unresolved numerical problem is cutoff renormalization of the source-carrying near-null cluster.

---

## 13. Correct next certification target [O]

Future analytic or numerical work should target one of the equivalent objects:

\[
\boxed{
\kappa_a^\Xi
}
\]

directly;

or

\[
\boxed{
-i\,
\operatorname{Tr}
[
(H_{a,0}-i)^{-1}
-
(H_{a,\pi}-i)^{-1}
]
}
\]

directly;

or

\[
\boxed{
\partial_\zeta
\partial_{\bar\omega}
\mathcal K_a(0,0)
=
1-(\kappa_a^\Xi)^2
}
\]

directly.

There is no need to certify the huge parity source quadratic forms separately if a rank-one trace or kernel-jet computation can avoid their common divergent scale.

The decisive finite-to-infinite theorem is therefore:

\[
\boxed{
\textbf{prove convergence of the normalized first de Branges/gamma kernel jet at }i.
}
\]

---

## 14. Result

The no-twist Xi scalar has the exact equivalent representations

\[
\boxed{
\kappa_a^\Xi
=
m_a'(i)
=
2i\,s_a'(i)
=
\langle
U_{a,\pi}^*\gamma_a(i),
\gamma_a(i)
\rangle
}
\]

and

\[
\boxed{
\kappa_a^\Xi
=
-i\,
\operatorname{Tr}
\left[
(H_{a,0}-i)^{-1}
-
(H_{a,\pi}-i)^{-1}
\right].
}
\]

In canonical disk coordinates,

\[
\boxed{
\partial_\zeta
\partial_{\bar\omega}
\mathcal K_a(0,0)
=
1-(\kappa_a^\Xi)^2.
}
\]

Thus the scalar finite-to-Xi problem is only a **one-point first-jet / rank-one trace convergence problem**, strictly weaker than full Weyl-function convergence.
