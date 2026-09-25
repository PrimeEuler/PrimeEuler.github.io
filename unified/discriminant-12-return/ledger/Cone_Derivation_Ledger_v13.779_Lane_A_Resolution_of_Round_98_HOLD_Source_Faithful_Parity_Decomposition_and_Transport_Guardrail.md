# Cone Derivation Ledger v13.779 — Lane A Resolution of Round-98 HOLD: Source-Faithful Parity Decomposition and Transport Guardrail

Date: 2026-09-25

Lane: A.

Status: [Audit/D] resolves the v13.778 HOLD by retracting the load-bearing claims of v13.776–777; [D] exact parity decomposition of Suzuki (8.5); [D] exact first- and second-derivative source identities; [N] no source-faithful \(S_Au_\pm\) equation follows from those differentiated identities without the missing domain data; [G] boundary correction must not be invented as an \(L^2\) forcing term or endpoint trace before a Green/domain theorem is supplied; [C] corrected next gate.

Parents: v13.741–743, v13.757, v13.773–778.

## 0. Synchronization and purpose

External Audit Round 98 v13.778 placed v13.776–777 on HOLD because they resurrected the already-retracted specialization
\[
u_{A,\pm}=S_A^{-1}\bar D e_{\pm i}.
\]

Live head was checked before derivation and immediately before this write: v13.778 remains head; no collision.

This entry resolves that HOLD in the negative: the claimed bypass in v13.776 and the parity-response construction in v13.777 are retracted as statements about Suzuki's actual finite deficiency vectors. The valid projective Weyl algebra using the **true** vectors from v13.742/v13.757 remains intact.

## 1. Source-faithful primitive equation [D]

For the \(+\) deficiency vector write
\[
v_A:=v_{A,+},\qquad C_A:=C_{A,+}.
\]
With
\[
I_{0,A}:=(K_Av_A)(0),
\qquad
I_{1,A}:=(K_Av_A)'(0),
\]
the corrected form of Suzuki (8.5) is
\[
\boxed{
-K_Av_A
=
C_A(e^x-1-x)-I_{1,A}x-I_{0,A}.
}
\tag{1}
\]

The kernel commutes with reflection. Decompose
\[
v_A=v_{A,e}+v_{A,o}.
\]
Since
\[
e^x-1-x=(\cosh x-1)+(\sinh x-x),
\]
equation (1) splits exactly into
\[
\boxed{
-K_A^{(+)}v_{A,e}
=
C_A(\cosh x-1)-I_{0,A},
}
\tag{E}
\]
and
\[
\boxed{
-K_A^{(-)}v_{A,o}
=
C_A(\sinh x-x)-I_{1,A}x.
}
\tag{O}
\]

Equivalently,
\[
-K_A^{(+)}v_{A,e}
=
C_A\cosh x-(C_A+I_{0,A}),
\]
\[
-K_A^{(-)}v_{A,o}
=
C_A\sinh x-(C_A+I_{1,A})x.
\]

Parity also gives
\[
\boxed{
I_{0,A}=(K_Av_{A,e})(0),
\qquad
I_{1,A}=(K_Av_{A,o})'(0).
}
\tag{2}
\]

Thus \(I_0\) belongs to the primitive-even channel and \(I_1\) to the primitive-odd channel; there is no parity mixing.

## 2. The local basepoint equations remain tautologies [D]

Evaluate (E) at \(x=0\):
\[
-I_{0,A}=-I_{0,A}.
\]

Differentiate (O) and evaluate at \(x=0\):
\[
-I_{1,A}=-I_{1,A}.
\]

Therefore parity decomposition does not create new scalar closure equations. This is the channel-wise form of the v13.773 obstruction.

## 3. Exact derivative transport of the primitive source [D]

Let
\[
D=i\partial_x,
\qquad
u_{A,e}:=Dv_{A,e},
\qquad
u_{A,o}:=Dv_{A,o}.
\]

The notation records the parity of the **primitive** component. Since differentiation reverses parity,
\[
\boxed{
u_{A,e}\ \text{is odd},
\qquad
u_{A,o}\ \text{is even}.
}
\tag{3}
\]

Applying \(D\) to the two *primitive integral identities* gives
\[
\boxed{
D(-K_Av_{A,e})=iC_A\sinh x,
}
\tag{4E}
\]
\[
\boxed{
D(-K_Av_{A,o})
=
iC_A\cosh x-i(C_A+I_{1,A}).
}
\tag{4O}
\]

These are exact identities for the derivatives of the first-kind left-hand sides.

Their information content is asymmetric:

- \(I_{0,A}\) disappears from the interior first derivative;
- \(I_{1,A}\) survives as the constant \(-iI_{1,A}\).

Applying a second derivative to the primitive right-hand sides gives
\[
\boxed{
\partial_x^2\!\left[C_A(\cosh x-1)-I_{0,A}\right]
=
C_A\cosh x,
}
\tag{5E}
\]
\[
\boxed{
\partial_x^2\!\left[C_A(\sinh x-x)-I_{1,A}x\right]
=
C_A\sinh x.
}
\tag{5O}
\]

Hence both affine integration constants are invisible to the twice-differentiated interior equation.

This is the exact mechanism behind the warning already recorded in v13.742:
\[
\boxed{
\text{the bulk twice-differentiated equation cannot determine the finite deficiency vector.}
}
\]

## 4. Endpoint reconstruction under \(D\) [D]

Suzuki's derivative map is
\[
D=i\frac d{dx}:H_0^1(-A,A)\to L_0^2(-A,A).
\]
Thus
\[
v(-A)=v(A)=0,
\qquad
u=Dv,
\]
and
\[
\boxed{
v(x)=-i\int_{-A}^{x}u(t)\,dt,
\qquad
\int_{-A}^{A}u(t)\,dt=0.
}
\tag{6}
\]

For primitive-even \(v_{A,e}\), \(u_{A,e}\) is odd, so the zero-mean condition is automatic, while
\[
v_{A,e}(0)
=
-i\int_{-A}^{0}u_{A,e}(t)\,dt.
\]

For primitive-odd \(v_{A,o}\), \(v_{A,o}(0)=0\), \(u_{A,o}\) is even, and
\[
\boxed{
v_{A,o}(x)
=
-i\int_0^x u_{A,o}(t)\,dt,
\qquad
\int_0^A u_{A,o}(t)\,dt=0.
}
\tag{7}
\]

These are exact reconstruction constraints. They show explicitly that passing to \(u=Dv\) retains nonlocal/domain information even though affine terms may disappear under differentiation.

## 5. Critical transport guardrail [Audit/N]

Equations (4E)–(4O) are **not** equations of the form
\[
S_Au_{A,e}=\cdots,
\qquad
S_Au_{A,o}=\cdots.
\]

Suzuki explicitly states that the actual deficiency equation (8.5) is different from
\[
S_Au_\pm=C_\pm\bar D e_{\pm i}.
\]

Therefore one may not identify
\[
D(-K_Av)
\]
with
\[
S_A(Dv)
\]
at the deficiency points merely by differentiating the first-kind equation.

In particular, the following tempting equations are **not established**:
\[
S_Au_{A,e}=iC_A\sinh x,
\]
\[
S_Au_{A,o}=iC_A\cosh x-i(C_A+I_{1,A}).
\]

Nor is it presently source-faithful to repair them by simply declaring
\[
S_Au=\text{bulk source}+\mathcal B_A
\]
with \(\mathcal B_A\) an ordinary \(L^2\) forcing term.

The missing object is domain/boundary information, and its functional realization must be derived from Suzuki's form/domain Green identity or boundary triple; it cannot be guessed from the differentiated interior equation.

## 6. What can be said about the missing data [D/G]

The exact hierarchy is
\[
\boxed{
\begin{array}{c}
\text{primitive equation (8.5): }I_0,I_1\text{ explicit}\\
\downarrow D\\
I_0\text{ absent from interior source},\quad
I_1\text{ survives as a constant}\\
\downarrow \partial_x\\
I_0,I_1\text{ both absent from the interior current}.
\end{array}}
\]

But disappearance from the interior source is not disappearance from the finite deficiency problem.

The data remain encoded in the requirement that the transported vector lie in the image
\[
\bar D\,\mathcal H(T_A)
\]
with the correct deficiency-domain relation inherited from (8.5).

Therefore the safe structural statement is
\[
\boxed{
\text{bulk differentiated current}
+
\text{domain/reconstruction data}
}
\]
rather than the stronger unproved statement
\[
\text{bulk source}+\text{finite-rank }L^2\text{ boundary forcing}.
\]

## 7. Resolution of v13.776–777 [Audit]

The load-bearing claims of v13.776–777 are retracted:

### Retracted from v13.776
\[
S_Au_\pm=\bar D e_{\pm i}
\]
for Suzuki's actual deficiency vectors, and the resulting claim that finite Weyl data bypass the primitive/domain constants.

### Retracted from v13.777
The definitions
\[
u_e=(S_A^{(+)})^{-1}\bar D\cosh,
\qquad
u_o=(S_A^{(-)})^{-1}\bar D\sinh
\]
as parity components of Suzuki's actual deficiency vector, and therefore the claimed \(\eta_A=O_A/E_A\) construction as an established finite Suzuki quantity.

### Retained
The purely algebraic Möbius/projective reduction from v13.742/v13.757 using the **true** deficiency pairings
\[
F_{A,\pm}^{\rm true}(z)
=
\overline{\langle u_{A,\bar z},u_{A,\pm}\rangle_{S_A}},
\]
with
\[
u_{A,\pm}=\bar Dv_{A,\pm},
\quad
v_{A,\pm}\text{ solving Suzuki (8.5)}.
\]

Thus the valid one-channel ratio remains
\[
\boxed{
\rho_A(z)=
\frac{F_{A,-}^{\rm true}(z)}
{F_{A,+}^{\rm true}(z)},
}
\]
and
\[
\boxed{
m_A(z)
=
-i\frac{(z-i)+(z+i)\rho_A(z)}
{(z-i)-(z+i)\rho_A(z)}.
}
\tag{8}
\]

No formula for \(\rho_A\) through naive parity inverses is asserted.

## 8. Correct next gate [C]

There are now two source-faithful routes, and they must not be conflated.

### Route A — stay primitive
Solve or asymptotically control the two parity first-kind equations
\[
-K_A^{(+)}v_{A,e}
=
C_A(\cosh-1)-I_{0,A},
\]
\[
-K_A^{(-)}v_{A,o}
=
C_A(\sinh-x)-I_{1,A}x,
\]
subject to the actual deficiency normalization/domain conditions, then set
\[
u_A=D(v_{A,e}+v_{A,o})
\]
and form the true pairings.

### Route B — derive a genuine transported boundary theorem
Starting from Suzuki's form-domain identity, derive the exact Green/boundary functional that distinguishes the deficiency-point vectors from the generic regular-\(z\) solve
\[
S_Au_z=\bar D e_z.
\]
Only after that derivation may one write a transported equation of the form
\[
S_Au_\pm
=
\text{bulk source}
+
\text{boundary functional}.
\]

The next analytic gate should therefore identify the domain of the transported first-order operator and its boundary trace map from Suzuki's Section 7/8 construction, rather than attempting another formal differentiation of (8.5).

## Result

Suzuki's actual deficiency equation admits an exact parity decomposition:
\[
\boxed{
-K_A^{(+)}v_{A,e}
=
C_A(\cosh x-1)-I_{0,A},
}
\]
\[
\boxed{
-K_A^{(-)}v_{A,o}
=
C_A(\sinh x-x)-I_{1,A}x.
}
\]

Its first differentiated source identities are
\[
\boxed{
D(-K_Av_{A,e})=iC_A\sinh x,
}
\]
\[
\boxed{
D(-K_Av_{A,o})
=
iC_A\cosh x-i(C_A+I_{1,A}).
}
\]

After two derivatives both \(I_0\) and \(I_1\) disappear from the interior current, explaining exactly why the naive deficiency-point \(S_A^{-1}\) construction can reproduce the bulk equation while losing the domain data.

The Round-98 HOLD is therefore resolved by **retraction**, not reinstatement:
\[
\boxed{
\text{v13.776--777 are not valid finite-deficiency constructions.}
}
\]

The source-faithful finite Weyl lane must proceed from the actual parity equations (E),(O), or from a separately proved transported boundary/Green identity.
