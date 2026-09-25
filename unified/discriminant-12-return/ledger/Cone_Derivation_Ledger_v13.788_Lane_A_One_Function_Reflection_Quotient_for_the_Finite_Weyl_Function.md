# Cone Derivation Ledger v13.788 — Lane A One-Function Reflection Quotient for the Finite Weyl Function

Date: 2026-09-25

Lane: A.

Status: [D] exact source-level reduction of the finite Weyl function to one canonical entire transform; [D] exact reproducing-kernel interpretation; [D] exact infinite reflection-ratio target in the stabilized sign convention; [G] replaces the older two-response presentation by a smaller normalization-free observable.

Parents: v13.675, v13.754–755, v13.757, v13.782, v13.784–787.

## 0. Synchronization

Immediately before this write the live ledger head is v13.787. No collision is present.

## 1. Canonical source-level deficiency transform [D]

Let
\[
v_{a,+i}:=T_a^{-1}e^x,
\qquad
v_{a,-i}:=T_a^{-1}e^{-x}.
\]

Since \(T_a\) commutes with reflection \(R\),
\[
v_{a,-i}=Rv_{a,+i}.
\]

Define the single entire function
\[
\boxed{
F_a(z)
:=
\widehat{v_{a,+i}}(z)
=
\int_{-a}^{a}v_{a,+i}(x)e^{izx}\,dx.
}
\tag{1}
\]

Then
\[
\boxed{
\widehat{v_{a,-i}}(z)=F_a(-z).
}
\tag{2}
\]

Thus one canonical source-level resolvent vector determines both deficiency channels.

## 2. Riesz/reproducing-kernel interpretation [D]

Suzuki Section 6.3 gives
\[
\langle v,v_z\rangle_{T_a}=\widehat v(\bar z).
\]

Therefore
\[
\boxed{
F_a(z)
=
\langle v_{a,+i},v_{a,\bar z}\rangle_{T_a}.
}
\tag{3}
\]

Hence \(F_a\) is a fixed deficiency slice of the Riesz/reproducing kernel of the finite energy space.

Equation (2) is therefore a reflection identity for two kernel slices, not an arbitrary Fourier trick.

## 3. Exact finite characteristics from one function [D]

Choose the reflection-compatible deficiency basis with common scalar \(C_a\):
\[
v_+=C_av_{a,+i},
\qquad
v_-=C_av_{a,-i}.
\]

Suzuki's characteristic becomes
\[
\boxed{
W(a,\theta;z)
=
C_a\left[
(z-i)F_a(z)
+
e^{i\theta}(z+i)F_a(-z)
\right].
}
\tag{4}
\]

In particular,
\[
\boxed{
W_0(a;z)
=
C_a\left[(z-i)F_a(z)+(z+i)F_a(-z)\right],
}
\tag{5}
\]
\[
\boxed{
W_\pi(a;z)
=
C_a\left[(z-i)F_a(z)-(z+i)F_a(-z)\right].
}
\tag{6}
\]

The unknown deficiency normalization \(C_a\) cancels in every characteristic quotient.

## 4. One reflection quotient determines the Weyl function [D]

Where \(F_a(z)\neq0\), define
\[
\boxed{
\rho_a(z):=\frac{F_a(-z)}{F_a(z)}.
}
\tag{7}
\]

Using
\[
W_0/W_\pi=i\,m_a
\]
in the audited boundary convention,
\[
\boxed{
m_a(z)
=
-i
\frac{(z-i)+(z+i)\rho_a(z)}
{(z-i)-(z+i)\rho_a(z)}.
}
\tag{8}
\]

Conversely,
\[
\boxed{
\rho_a(z)
=
\frac{z-i}{z+i}
\frac{i\,m_a(z)-1}
{i\,m_a(z)+1},
}
\tag{9}
\]
away from the corresponding divisors.

Thus
\[
\boxed{
\rho_a
\Longleftrightarrow
m_a
}
\]
by an exact Möbius transformation.

## 5. Relation to the parity ratio of v13.785 [D]

Let
\[
E_a=\widehat{(T_a^{(+)})^{-1}\cosh},
\qquad
O_a=\widehat{(T_a^{(-)})^{-1}\sinh}.
\]

Then
\[
F_a(z)=E_a(z)+O_a(z),
\qquad
F_a(-z)=E_a(z)-O_a(z).
\]

Hence
\[
\boxed{
\rho_a(z)
=
\frac{1-\eta_a(z)}
{1+\eta_a(z)},
\qquad
\eta_a:=O_a/E_a.
}
\tag{10}
\]

So the one-function reflection quotient and the v13.785 parity ratio contain exactly the same information. The reflection quotient is smaller computationally because it requires only one source solve,
\[
T_av=e^x.
\]

## 6. Stabilized infinite target [D]

Use the later audited sign convention of v13.754–755:
\[
\boxed{
m_\infty(z)
=
-i\,R_\xi(z),
}
\]
where
\[
\boxed{
R_\xi(z)
:=
\frac{\xi(3/2)}{\xi'(3/2)}
\frac{\xi'(1/2-iz)}
{\xi(1/2-iz)}.
}
\tag{11}
\]

Then
\[
i\,m_\infty=R_\xi,
\]
and (9) gives the exact target
\[
\boxed{
\rho_\infty(z)
=
\frac{z-i}{z+i}
\frac{R_\xi(z)-1}
{R_\xi(z)+1}.
}
\tag{12}
\]

This is the normalization-free finite-to-infinite scalar target.

## 7. Minimal convergence theorem [D]

On compacta avoiding zeros/poles of the Möbius factors,
\[
\boxed{
\rho_a\to\rho_\infty
\quad\Longleftrightarrow\quad
m_a\to m_\infty
}
\tag{13}
\]
locally uniformly.

Therefore the entire finite Weyl/HB convergence problem can be reduced to
\[
\boxed{
\frac{F_a(-z)}{F_a(z)}
\longrightarrow
\frac{z-i}{z+i}
\frac{R_\xi(z)-1}
{R_\xi(z)+1}.
}
\tag{14}
\]

No primitive affine constants, no raw Fredholm endpoint conditions, and no absolute deficiency normalization appear.

## 8. Reproducing-kernel slice criterion [D/C]

Let
\[
\mathscr K_a(z,w)
:=
\widehat{v_{a,w}}(z)
=
\langle v_{a,w},v_{a,\bar z}\rangle_{T_a},
\]
with \(v_{a,w}=T_a^{-1}e_w\).

Then
\[
F_a(z)=\mathscr K_a(z,i),
\qquad
F_a(-z)=\mathscr K_a(z,-i).
\]

Hence
\[
\boxed{
\rho_a(z)
=
\frac{\mathscr K_a(z,-i)}
{\mathscr K_a(z,i)}.
}
\tag{15}
\]

A sufficient convergence package is therefore any projectively common normalization under which these two kernel slices converge locally uniformly to nontrivial limits with ratio (12).

This is weaker than requiring full convergence of the finite de Branges kernels.

## 9. Computational consequence [G]

A source-faithful finite computation need only:

1. solve
\[
T_av=e^x;
\]
2. compute its entire Fourier transform \(F_a(z)\);
3. form
\[
\rho_a(z)=F_a(-z)/F_a(z);
\]
4. compare with (12).

The reflected \(-i\) deficiency vector, the common scale, and the raw affine coefficients are all unnecessary for this spectral-shape observable.

## Result

\[
\boxed{
F_a(z)=\widehat{T_a^{-1}e^x}(z)
}
\]
is a single canonical entire function whose reflection quotient
\[
\boxed{
\rho_a(z)=F_a(-z)/F_a(z)
}
\]
determines the finite Weyl function exactly by (8).

The finite-to-infinite Weyl problem is therefore reduced to the one-function projective limit (14).
