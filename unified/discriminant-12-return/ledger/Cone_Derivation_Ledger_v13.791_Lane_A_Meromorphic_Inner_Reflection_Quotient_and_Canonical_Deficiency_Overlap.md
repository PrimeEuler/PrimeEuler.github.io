# Cone Derivation Ledger v13.791 — Lane A Meromorphic-Inner Reflection Quotient and Canonical Deficiency Overlap Parameter

Date: 2026-09-25

Lane: A.

Status: [D] exact meromorphic-inner property of the one-function quotient; [D] exact deficiency-overlap interpretation at \(z=i\); [D] exact derivative identity \(h_a(i)=m_a'(i)\); [C] Schur-parameter convergence target.

Parents: v13.661, v13.782, v13.788–790.

## 0. Synchronization

Immediately before this write the live ledger head is v13.790. No collision is present.

## 1. The bounded reflection quotient [D]

From v13.790,
\[
F_a(z)=\widehat{T_a^{-1}e^x}(z)
\]
satisfies
\[
F_a^\sharp(z)=F_a(-z),
\]
and
\[
\boxed{
h_a(z):=\frac{F_a(z)}{F_a(-z)}
}
\tag{1}
\]
extends holomorphically to \(\mathbb C_+\) with
\[
\boxed{|h_a(z)|\le1.}
\tag{2}
\]

## 2. Unimodular real boundary values [D]

For real \(x\),
\[
F_a(-x)=\overline{F_a(x)}.
\]
Hence at every real point where the quotient is defined,
\[
\boxed{
|h_a(x)|=1.
}
\tag{3}
\]

At common real zeros the quotient is interpreted by its removable continuation where applicable. Thus \(h_a\) has unimodular nontangential boundary values almost everywhere on \(\mathbb R\).

Combining (2) and (3),
\[
\boxed{
h_a\text{ is a meromorphic inner function on }\mathbb C_+.
}
\tag{4}
\]

Equivalently,
\[
h_a^\sharp=\frac1{h_a}
\]
in the meromorphic sharp sense.

## 3. Canonical value at \(z=i\) [D]

Let
\[
v_{a,+i}:=T_a^{-1}e^x,
\qquad
v_{a,-i}:=T_a^{-1}e^{-x}=Rv_{a,+i}.
\]

Then
\[
F_a(-i)
=
\int_{-a}^{a}v_{a,+i}(x)e^x\,dx.
\]
Since
\[
T_av_{a,+i}=e^x,
\]
\[
\boxed{
F_a(-i)
=
\langle v_{a,+i},T_av_{a,+i}\rangle
=
\|v_{a,+i}\|_{T_a}^2
>0.
}
\tag{5}
\]

Likewise,
\[
F_a(i)
=
\int_{-a}^{a}v_{a,+i}(x)e^{-x}\,dx
=
\langle v_{a,+i},T_av_{a,-i}\rangle,
\]
so
\[
\boxed{
F_a(i)
=
\langle v_{a,+i},v_{a,-i}\rangle_{T_a}.
}
\tag{6}
\]

Therefore
\[
\boxed{
h_a(i)
=
\frac{
\langle v_{a,+i},v_{a,-i}\rangle_{T_a}
}{
\|v_{a,+i}\|_{T_a}^2
}.
}
\tag{7}
\]

Reflection is unitary in the \(T_a\)-energy space, so
\[
\|v_{a,-i}\|_{T_a}
=
\|v_{a,+i}\|_{T_a}.
\]
By Cauchy–Schwarz,
\[
|h_a(i)|\le1.
\]

Equality would force
\[
v_{a,-i}=c\,v_{a,+i},
\]
which after applying \(T_a\) would require
\[
e^{-x}=c\,e^x
\]
on \((-a,a)\), impossible for \(a>0\). Hence
\[
\boxed{
|h_a(i)|<1.
}
\tag{8}
\]

Because the vectors and sources can be chosen real,
\[
\boxed{
h_a(i)\in(-1,1).
}
\tag{9}
\]

Thus \(h_a(i)\) is a concrete normalized overlap of the two opposite deficiency vectors.

## 4. Exact relation to the Weyl derivative [D]

From v13.790,
\[
s_a(z)
=
\phi_i(z)h_a(z),
\qquad
\phi_i(z)=\frac{z-i}{z+i},
\]
and
\[
s_a(z)=\frac{m_a(z)-i}{m_a(z)+i}.
\]

Since
\[
m_a(i)=i,
\]
differentiate at \(z=i\).

For the Cayley transform,
\[
s_a'(i)
=
-\frac{i}{2}m_a'(i).
\]
For the Blaschke factor,
\[
\phi_i'(i)=-\frac{i}{2}.
\]
Because \(s_a(i)=\phi_i(i)=0\),
\[
s_a'(i)=\phi_i'(i)h_a(i).
\]
Therefore
\[
\boxed{
h_a(i)=m_a'(i).
}
\tag{10}
\]

Combining (7) and (10),
\[
\boxed{
m_a'(i)
=
\frac{
\langle v_{a,+i},v_{a,-i}\rangle_{T_a}
}{
\|v_{a,+i}\|_{T_a}^2
}.
}
\tag{11}
\]

This is an exact finite-\(a\) identity linking the local Weyl slope to the normalized overlap of the two deficiency directions.

## 5. First Schur parameter [D/I]

The scalar
\[
\boxed{
\kappa_a:=h_a(i)=m_a'(i)\in(-1,1)
}
\tag{12}
\]
is the first Schur parameter of the bounded quotient \(h_a\) at the canonical base point \(i\).

Define the disk automorphism
\[
\Phi_{\kappa_a}(w)
=
\frac{w-\kappa_a}{1-\kappa_a w}.
\]
Then
\[
\Phi_{\kappa_a}(h_a(i))=0.
\]

Schwarz–Pick therefore implies that
\[
\boxed{
h_a^{(1)}(z)
:=
\frac{1}{\phi_i(z)}
\frac{h_a(z)-\kappa_a}
{1-\kappa_a h_a(z)}
}
\tag{13}
\]
extends holomorphically to \(\mathbb C_+\) and satisfies
\[
\boxed{
|h_a^{(1)}(z)|\le1.
}
\tag{14}
\]

Thus the one-function finite Weyl data admit an exact Schur-algorithm decomposition
\[
h_a
\longleftrightarrow
\left(
\kappa_a,\,
h_a^{(1)}
\right).
\]

## 6. Convergence consequence [C]

To prove
\[
h_a\to h_\infty
\]
locally uniformly, one possible finer route is:

1. prove convergence of the scalar overlap
\[
\kappa_a\to\kappa_\infty;
\]
2. identify the pointwise limit of the uniformly bounded first Schur iterates
\[
h_a^{(1)}
\]
on any interior uniqueness set.

Vitali then upgrades the iterate convergence locally uniformly, and the inverse disk automorphism reconstructs \(h_a\).

This does not by itself solve the asymptotic problem, but isolates a single explicit finite scalar
\[
\kappa_a
=
\frac{\langle v_{+i},v_{-i}\rangle_{T_a}}
{\|v_{+i}\|_{T_a}^2}
\]
that can be monitored analytically or numerically without any raw first-kind endpoint assumption.

## 7. Target warning [G]

The finite \(h_a\) are meromorphic inner functions unconditionally.

A locally uniform limit in \(\mathbb C_+\) is only guaranteed to be Schur; innerness of the limit requires additional boundary control.

Therefore the project must not infer that the corrected target
\[
h_\infty(z)
=
\frac{z+i}{z-i}
\frac{R_\xi(z)-1}{R_\xi(z)+1}
\]
is inner merely from its formal expression. Its Schur property is a necessary condition for finite-to-infinite convergence; its inner boundary behavior is a stronger question.

## Result

The canonical one-function quotient has the stronger structure
\[
\boxed{
h_a(z)=\frac{F_a(z)}{F_a(-z)}
\text{ is meromorphic inner on }\mathbb C_+.
}
\]

At the canonical point,
\[
\boxed{
h_a(i)
=
m_a'(i)
=
\frac{
\langle v_{a,+i},v_{a,-i}\rangle_{T_a}
}{
\|v_{a,+i}\|_{T_a}^2
}
\in(-1,1).
}
\]

This provides the first explicit Schur parameter of the finite Suzuki problem and a new scalar observable for the asymptotic lane.
