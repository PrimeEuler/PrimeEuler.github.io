# Cone Derivation Ledger v13.757 — Corrected Finite Weyl Function as Two Scalar Transforms and Minimal Asymptotic Gate

Date: 2026-09-24

Status: continuation of the corrected Suzuki finite-edge lane after incorporating the helix/screw–Weil results v13.748–756 and External Audit Rounds 89–91. This entry does not rederive the helix carrier, HB determinant, or v13.745 moment closure. It uses them to sharpen the remaining finite-to-infinite Weyl problem.

Synchronization: live head before write was v13.756, commit \`f5de29a3b0041023e5f2f7b2aae0a480d3437955\`. Round 91 passed the self-contained helix/HB algebra. v13.756 identifies local-uniform \(m_A\to m_\infty\) as the sufficient scalar gate.

## 1. Imported exact architecture

From the corrected finite deficiency lane, let
\[
u_{A,\pm}=\bar Dv_{A,\pm}
\]
be Suzuki's actual deficiency vectors obtained from (8.5), not the retracted inverse-source ansatz.

For a regular spectral parameter \(z\),
\[
u_{A,z}=S_A^{-1}\bar D e_z.
\]

Define the true finite deficiency transforms
\[
F_{A,\pm}(z)
:=
\overline{\langle u_{A,\bar z},u_{A,\pm}\rangle_{S_A}}.
\]

In the fixed boundary basis,
\[
\boxed{
m_A(z)
=
-i\frac{(z-i)F_{A,+}(z)+(z+i)F_{A,-}(z)}
{(z-i)F_{A,+}(z)-(z+i)F_{A,-}(z)}.
}
\tag{1}
\]

From v13.756 the target is
\[
\boxed{
m_\infty(z)
=
-i\frac{a}{b}
\frac{D_\xi(z)}{\Xi(z)},
\qquad
a=\xi(3/2),\quad b=\xi'(3/2),
}
\tag{2}
\]
where
\[
\Xi(z)=\xi(1/2-iz),\qquad D_\xi(z)=\xi'(1/2-iz).
\]

## 2. Reflection reduces the two deficiency transforms to one vector

Choose the reflection-compatible deficiency normalization from v13.743:
\[
v_{A,-}=Rv_{A,+}.
\]

The derivative transport reverses sign under reflection:
\[
D R=-R D.
\]

Hence
\[
\boxed{
u_{A,-}=-R u_{A,+}.
}
\tag{3}
\]

Thus the finite Weyl function is determined by one corrected deficiency vector \(u_A:=u_{A,+}\) and its reflected derivative image.

Define
\[
\boxed{
G_A(z):=F_{A,+}(z),
\qquad
H_A(z):=F_{A,-}(z).
}
\]
Then
\[
H_A(z)
=
-\overline{\langle u_{A,\bar z},Ru_A\rangle_{S_A}}.
\]

No second Section-8 solve is needed.

## 3. Sum/difference scalar transforms

Define
\[
\boxed{
P_A(z):=(z-i)G_A(z)-(z+i)H_A(z),
}
\tag{4}
\]
\[
\boxed{
Q_A(z):=(z-i)G_A(z)+(z+i)H_A(z).
}
\tag{5}
\]

These are built from the **true** deficiency vectors, so unlike retracted v13.740 they are source-faithful.

Equation (1) becomes
\[
\boxed{
m_A(z)=-i\,\frac{Q_A(z)}{P_A(z)}.
}
\tag{6}
\]

Therefore absolute normalization of \(u_A\) cancels identically.

This is the finite analogue of the infinite fact that the Weyl function is projective boundary data.

## 4. Target ratio

From (2), the exact limiting ratio required is
\[
-i\frac{Q_\infty}{P_\infty}
=
-i\frac{a}{b}\frac{D_\xi}{\Xi}.
\]

Hence
\[
\boxed{
\frac{Q_\infty(z)}{P_\infty(z)}
=
\frac{a}{b}\frac{D_\xi(z)}{\Xi(z)}.
}
\tag{7}
\]

So the finite-to-infinite problem can be stated without any deficiency normalization:
\[
\boxed{
\frac{Q_A(z)}{P_A(z)}
\longrightarrow
\frac{a}{b}\frac{D_\xi(z)}{\Xi(z)}
}
\tag{8}
\]
locally uniformly on zero-free compacta for the relevant denominators.

## 5. Minimal two-function convergence criterion

Let \(K\Subset\Omega\) be compact. Suppose there exist nonzero scalars \(c_A\), independent of \(z\), and holomorphic functions \(P_\infty,Q_\infty\) such that
\[
\boxed{
c_A^{-1}P_A\to P_\infty,\qquad
c_A^{-1}Q_A\to Q_\infty
}
\tag{9}
\]
locally uniformly, with \(P_\infty\ne0\) on \(K\), and
\[
Q_\infty/P_\infty=(a/b)D_\xi/\Xi.
\]

Then
\[
\boxed{m_A\to m_\infty}
\]
locally uniformly on \(K\).

The common scale \(c_A\) may be arbitrary. Thus the absolute normalization \(C_A\) from (8.5) is irrelevant for Weyl convergence.

## 6. Stronger reduction: only the channel ratio is needed

Where \(G_A\ne0\), define
\[
\boxed{
\rho_A(z):=\frac{H_A(z)}{G_A(z)}.
}
\tag{10}
\]

Then
\[
\boxed{
m_A(z)
=
-i
\frac{(z-i)+(z+i)\rho_A(z)}
{(z-i)-(z+i)\rho_A(z)}.
}
\tag{11}
\]

Solving this Möbius relation for \(\rho_A\) gives
\[
\boxed{
\rho_A(z)
=
\frac{z-i}{z+i}
\frac{i\,m_A(z)-1}{i\,m_A(z)+1}.
}
\tag{12}
\]

Therefore the exact infinite target channel ratio is
\[
\boxed{
\rho_\infty(z)
=
\frac{z-i}{z+i}
\frac{
(a/b)D_\xi(z)/\Xi(z)-1
}{
(a/b)D_\xi(z)/\Xi(z)+1
}.
}
\tag{13}
\]

Consequently, on compacta avoiding the Möbius divisors,
\[
\boxed{
\rho_A\to\rho_\infty
\quad\Longleftrightarrow\quad
m_A\to m_\infty.
}
\tag{14}
\]

This is the smallest scalar convergence target found so far: **one meromorphic channel ratio**.

## 7. Insert the v13.745 corrected scalar closure

The actual \(+\) deficiency vector satisfies
\[
\mathcal L_Av_A
=
C_A(e^x-1-x)-I_{1,A}x-I_{0,A}.
\]

With
\[
u_{e,A}=R_A(e^x-1-x),\quad
u_{1,A}=R_A1,\quad
u_{x,A}=R_Ax,
\]
v13.745 gives
\[
v_A
=
C_Au_{e,A}-I_{0,A}u_{1,A}-I_{1,A}u_{x,A}.
\]

Reflection parity diagonalizes the moment feedback:
\[
\frac{I_{0,A}}{C_A}
=
r_{0,A}
:=
\frac{M_{0e}}{1+M_{00}},
\]
\[
\frac{I_{1,A}}{C_A}
=
r_{1,A}
:=
\frac{M_{1e}}{1+M_{1x}}.
\]

Therefore
\[
\boxed{
v_A
=
C_A
\left[
u_{e,A}-r_{0,A}u_{1,A}-r_{1,A}u_{x,A}
\right].
}
\tag{15}
\]

Define the normalized corrected deficiency shape
\[
\boxed{
w_A
:=
u_{e,A}-r_{0,A}u_{1,A}-r_{1,A}u_{x,A}.
}
\tag{16}
\]

Then
\[
v_A=C_Aw_A,
\qquad
u_A=C_A\bar D w_A.
\]

The absolute \(C_A\) cancels from \(\rho_A\).

## 8. Explicit one-shape formula for the Weyl channel ratio

Let
\[
\mathcal U_A:=\bar D w_A.
\]

Then, up to the common deficiency normalization,
\[
u_{A,+}=\mathcal U_A,\qquad
u_{A,-}=-R\mathcal U_A.
\]

Therefore
\[
\boxed{
\rho_A(z)
=
-
\frac{
\overline{\langle u_{A,\bar z},R\mathcal U_A\rangle_{S_A}}
}{
\overline{\langle u_{A,\bar z},\mathcal U_A\rangle_{S_A}}
}.
}
\tag{17}
\]

Using \(S_Au_{A,\bar z}=\bar D e_{\bar z}\), equivalently
\[
\boxed{
\rho_A(z)
=
-
\frac{
\overline{\langle \bar D e_{\bar z},R\mathcal U_A\rangle}
}{
\overline{\langle \bar D e_{\bar z},\mathcal U_A\rangle}
},
}
\tag{18}
\]
in the appropriate form/duality interpretation.

Thus the remaining finite-to-infinite problem is a ratio of **two scalar transforms of one corrected deficiency shape**.

## 9. Minimal asymptotic estimates on the v13.745 moments

The corrected shape depends on the two feedback ratios
\[
r_{0,A}=\frac{M_{0e}}{1+M_{00}},
\qquad
r_{1,A}=\frac{M_{1e}}{1+M_{1x}}.
\]

A sufficient route to Weyl convergence is therefore:

1. establish asymptotic limits or controlled expansions
\[
r_{0,A}=r_{0,\infty}+o(1),
\qquad
r_{1,A}=r_{1,\infty}+o(1);
\]

2. establish convergence, after embedding/edge transport, of the three response shapes
\[
\bar D u_{e,A},\quad
\bar D u_{1,A},\quad
\bar D u_{x,A}
\]
in a topology strong enough to pass the two scalar pairings in (18);

3. ensure the denominator transform stays uniformly away from zero on the compact set.

Under these hypotheses,
\[
\mathcal U_A\to\mathcal U_\infty
\]
and hence
\[
\rho_A\to\rho_\infty,
\]
provided the limiting transform ratio is identified with (13).

This is strictly weaker than proving absolute convergence of \(C_A\), \(I_{0,A}\), or \(I_{1,A}\).

## 10. Interaction with the affine edge coefficients

v13.745 gave
\[
\alpha_A=-e^{-A}(1+r_{1,A}),
\]
\[
\beta_A=-e^{-A}[A(1+r_{1,A})+1+r_{0,A}].
\]

Therefore any bounded limits
\[
r_{0,A}=O(1),\qquad r_{1,A}=O(1)
\]
immediately imply
\[
\boxed{\alpha_A,\beta_A\to0.}
\tag{19}
\]

More generally it suffices that
\[
r_{1,A}=o(e^A/A),
\qquad
r_{0,A}=o(e^A).
\]

This links the old corrected-edge question directly to the new Weyl gate: **the same two scalar feedback ratios control both the affine contamination and the corrected deficiency shape.**

Thus estimates on \(r_{0,A},r_{1,A}\) simultaneously decide whether the pure compensated edge source survives and whether the finite Weyl channel has a stable limiting shape.

## 11. Helix relevance without redundancy

The new helix lane does not add another unknown to (18).

v13.753 proved the derivative screw–Weil form isometry and v13.754 showed the transported boundary triple preserves \(m_A\). Therefore the ratio \(\rho_A\) can be evaluated in any of the unitarily equivalent carriers:

\[
\boxed{
\text{corrected Section-8 deficiency shape}
\leftrightarrow
\text{screw increment carrier}
\leftrightarrow
\text{basepointed rapidity helix/Weil carrier}.
}
\]

The zero-mode quotient removes the primitive affine constant before the boundary triple; it does **not** remove the \(r_{0,A},r_{1,A}\) feedback from Suzuki (8.5).

So the helix lane supplies a cleaner carrier for the scalar transforms but does not justify dropping the corrected affine terms.

## 12. Relation to the HB determinant

Once
\[
\rho_A\to\rho_\infty,
\]
equation (11) gives
\[
m_A\to m_\infty.
\]

Then v13.756 applies automatically:
\[
\boxed{
\Delta_{{\rm HB},A/\pi}
\to
\Delta_{{\rm HB},\infty/\pi}
=
\frac{E/\Xi}{(E/\Xi)(z_*)}.
}
\]

Hence
\[
\boxed{
\Delta_{{\rm HB},A/\pi}^{-1}
\to
\text{constant}\times\frac{\Xi}{E}
=
\text{constant}\times T_{\rm pair}.
}
\]

No direct finite formula \(P_A=C_A\Xi/E\) is assumed.

## Result

The remaining corrected finite-to-infinite Suzuki problem has been reduced to one meromorphic scalar ratio:
\[
\boxed{
\rho_A(z)
=
-
\frac{
\overline{\langle \bar D e_{\bar z},R\mathcal U_A\rangle}
}{
\overline{\langle \bar D e_{\bar z},\mathcal U_A\rangle}
},
}
\]
where
\[
\boxed{
\mathcal U_A
=
\bar D\left(
u_{e,A}
-
\frac{M_{0e}}{1+M_{00}}u_{1,A}
-
\frac{M_{1e}}{1+M_{1x}}u_{x,A}
\right).
}
\]

The exact target is
\[
\boxed{
\rho_\infty(z)
=
\frac{z-i}{z+i}
\frac{
(a/b)D_\xi(z)/\Xi(z)-1
}{
(a/b)D_\xi(z)/\Xi(z)+1
}.
}
\]

Thus
\[
\boxed{
\rho_A\to\rho_\infty
\iff
m_A\to m_\infty
}
\]
away from the corresponding divisors, and v13.756 then supplies the HB determinant convergence.

The two scalar feedback ratios
\[
\boxed{
r_{0,A}=\frac{M_{0e}}{1+M_{00}},
\qquad
r_{1,A}=\frac{M_{1e}}{1+M_{1x}}
}
\]
are the common control variables for both the affine-edge contamination and the finite Weyl shape.

## Next gate

Derive the response moments \(M_{00},M_{1x},M_{0e},M_{1e}\) directly from the corrected integral operator \(\mathcal L_A\), exploiting even/odd decomposition and the helix/screw–Weil carrier. The goal is to obtain bounds on \(r_{0,A},r_{1,A}\) without solving the full deficiency vector and then test whether their boundedness/subexponential growth is enough to close the pure compensated edge limit.
