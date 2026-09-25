# Cone Derivation Ledger v13.793 — Lane A Second Schur Parameter and the Canonical Scalar Hierarchy

Date: 2026-09-25

Lane: A.

Status: [D] exact second Schur-parameter formula; [D] exact infinite target in terms of \(\xi\)-derivatives at \(3/2\); [N] high-precision diagnostic; [C] hierarchy of necessary scalar convergence conditions and numerical-stiffness warning.

Parents: v13.790–792.

## 0. Synchronization

Immediately before this write the live ledger head is v13.792. No collision is present.

## 1. First Schur step [D]

From v13.791 define
\[
h_a^{(0)}:=h_a,
\qquad
\kappa_{0,a}:=h_a(i)=m_a'(i)\in(-1,1).
\]

Let
\[
\phi_i(z):=\frac{z-i}{z+i}.
\]

The first Schur iterate is
\[
\boxed{
h_a^{(1)}(z)
=
\frac{1}{\phi_i(z)}
\frac{h_a(z)-\kappa_{0,a}}
{1-\kappa_{0,a}h_a(z)}.
}
\tag{1}
\]

It is holomorphic and Schur on \(\mathbb C_+\).

Define the second scalar parameter
\[
\boxed{
\kappa_{1,a}:=h_a^{(1)}(i).
}
\tag{2}
\]

## 2. Exact derivative formula [D]

Differentiate the disk automorphism in (1). Since
\[
h_a(i)=\kappa_{0,a},
\]
\[
\left.
\frac{d}{dz}
\frac{h_a(z)-\kappa_{0,a}}
{1-\kappa_{0,a}h_a(z)}
\right|_{z=i}
=
\frac{h_a'(i)}
{1-\kappa_{0,a}^2}.
\]

Also
\[
\phi_i'(i)=-\frac{i}{2}.
\]

Hence
\[
\boxed{
\kappa_{1,a}
=
\frac{2i\,h_a'(i)}
{1-\kappa_{0,a}^2}.
}
\tag{3}
\]

Using
\[
s_a=\phi_i h_a,
\qquad
s_a=\frac{m_a-i}{m_a+i},
\qquad
m_a(i)=i,
\]
a second-order expansion gives
\[
\boxed{
h_a'(i)
=
\frac12m_a''(i)
+
\frac{i}{2}
\left[
\kappa_{0,a}^2-\kappa_{0,a}
\right].
}
\tag{4}
\]

Substituting into (3),
\[
\boxed{
\kappa_{1,a}
=
\frac{
\kappa_{0,a}-\kappa_{0,a}^2
+i\,m_a''(i)
}{
1-\kappa_{0,a}^2
}.
}
\tag{5}
\]

The reflection/sharp symmetry makes the right-hand side real.

## 3. One-source moment formula [D]

Write
\[
F_a(z)=\int_{-a}^{a}v_{a,+i}(x)e^{izx}\,dx,
\qquad
H_a:=F_a(-i)>0,
\qquad
G_a:=F_a(i).
\]

Then
\[
\kappa_{0,a}=G_a/H_a.
\]

Moreover,
\[
h_a'(i)
=
\frac{
F_a'(i)H_a+G_aF_a'(-i)
}{
H_a^2
}.
\]

Define real moments
\[
M_{-,a}:=\int_{-a}^{a}x\,v_{a,+i}(x)e^{-x}\,dx,
\]
\[
M_{+,a}:=\int_{-a}^{a}x\,v_{a,+i}(x)e^{x}\,dx.
\]
Since
\[
F_a'(i)=iM_{-,a},
\qquad
F_a'(-i)=iM_{+,a},
\]
we obtain
\[
\boxed{
\kappa_{1,a}
=
-\frac{2}{
1-\kappa_{0,a}^2
}
\left[
\frac{M_{-,a}}{H_a}
+
\kappa_{0,a}\frac{M_{+,a}}{H_a}
\right].
}
\tag{6}
\]

Thus the second Schur parameter is computable from the same single source-level solve
\[
T_av=e^x
\]
using only three additional scalar moments.

## 4. Infinite second parameter [D]

Let
\[
A_\xi:=\frac{\xi(3/2)}{\xi'(3/2)},
\qquad
L(s):=\frac{\xi'(s)}{\xi(s)}.
\]

From v13.792,
\[
\boxed{
\kappa_{0,\infty}
=
A_\xi L'(3/2).
}
\tag{7}
\]

The source-fixed infinite Weyl function is
\[
m_\infty(z)
=
iA_\xi L\!\left(\frac12-iz\right).
\]

Therefore
\[
m_\infty''(i)
=
-iA_\xi L''(3/2),
\]
and
\[
i\,m_\infty''(i)
=
A_\xi L''(3/2).
\]

Equation (5) gives the exact target
\[
\boxed{
\kappa_{1,\infty}
=
\frac{
\kappa_{0,\infty}
-\kappa_{0,\infty}^2
+
A_\xi L''(3/2)
}{
1-\kappa_{0,\infty}^2
}.
}
\tag{8}
\]

Here
\[
L''(s)
=
\frac{\xi'''(s)}{\xi(s)}
-
3\frac{\xi'(s)\xi''(s)}{\xi(s)^2}
+
2\left(\frac{\xi'(s)}{\xi(s)}\right)^3.
\]

Thus the second parameter is determined by \(\xi,\xi',\xi'',\xi'''\) at the single real point \(3/2\).

## 5. High-precision diagnostic [N]

Using 80-digit arithmetic,
\[
\kappa_{0,\infty}
\approx
0.9968019520324009035288967047877578325738,
\]
and
\[
\boxed{
\kappa_{1,\infty}
\approx
-0.9954804115180577060070406508906472014061.
}
\tag{9}
\]

The corresponding Schur defects are
\[
\boxed{
1-\kappa_{0,\infty}^2
\approx
0.006385868424395128230614333972901622637,
}
\tag{10}
\]
\[
\boxed{
1-\kappa_{1,\infty}^2
\approx
0.009018750283838482536404221162064652878.
}
\tag{11}
\]

Both target parameters lie close to the unit-circle boundary, with opposite signs.

## 6. Canonical scalar hierarchy [D/C]

The construction may be iterated.

Given a Schur function \(h_a^{(n)}\), define
\[
\kappa_{n,a}:=h_a^{(n)}(i),
\]
and
\[
\boxed{
h_a^{(n+1)}(z)
=
\frac1{\phi_i(z)}
\frac{
h_a^{(n)}(z)-\kappa_{n,a}
}{
1-\overline{\kappa_{n,a}}\,h_a^{(n)}(z)
}.
}
\tag{12}
\]

For the present reflection-symmetric real normalization the \(\kappa_{n,a}\) are real as long as the symmetry is preserved.

Each
\[
|\kappa_{n,a}|\le1.
\]

If
\[
h_a\to h_\infty
\]
locally uniformly and no finite Schur denominator degenerates, then for every fixed \(n\),
\[
\boxed{
\kappa_{n,a}\to\kappa_{n,\infty}.
}
\tag{13}
\]

Thus the proposed Weyl convergence implies an infinite hierarchy of scalar necessary conditions, beginning with (7) and (8).

## 7. Numerical consequence [G/C]

Because the first two target parameters are already close to \(\pm1\), the denominators
\[
1-\kappa_{n,a}^2
\]
amplify errors in higher Schur steps.

Therefore future source-faithful Galerkin computations should not judge convergence solely from raw \(W\), \(m_a\), or first-kind residuals. They should monitor at minimum
\[
\kappa_{0,a},\qquad\kappa_{1,a}
\]
at controlled precision.

Agreement with \(\kappa_{0,\infty}\) but failure at \(\kappa_{1,\infty}\) would disprove convergence of the full finite Schur function while exposing the failure with only a few scalar moments.

## Result

The second finite Schur parameter is
\[
\boxed{
\kappa_{1,a}
=
\frac{
\kappa_{0,a}-\kappa_{0,a}^2+i\,m_a''(i)
}{
1-\kappa_{0,a}^2
},
}
\]
and the exact infinite target is
\[
\boxed{
\kappa_{1,\infty}
=
\frac{
\kappa_{0,\infty}
-\kappa_{0,\infty}^2
+
A_\xi L''(3/2)
}{
1-\kappa_{0,\infty}^2
}
\approx-0.9954804115180577.
}
\]

This initiates a canonical Schur-parameter hierarchy for Lane A, reducing increasingly fine finite-to-infinite spectral tests to scalar data at the single deficiency base point \(z=i\).
