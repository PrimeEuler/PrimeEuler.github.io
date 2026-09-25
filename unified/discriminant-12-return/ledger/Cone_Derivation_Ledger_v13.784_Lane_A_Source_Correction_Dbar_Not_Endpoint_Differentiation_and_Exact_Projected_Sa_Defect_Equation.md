# Cone Derivation Ledger v13.784 — Lane A Source Correction: \bar D Is Not Endpoint Differentiation on Deficiency Vectors, and the Projected S_a Defect Equation Is Exact

Date: 2026-09-25

Lane: A.

Status: [P/D] direct Suzuki-v2 source correction after External Audit Round 100; [R] partial retraction/supersession of v13.742 and v13.779; [D] exact distinction between the source-level \(T_a\) solve, the projected transported \(S_a\) solve, and the raw first-kind kernel equation (8.5); [G] endpoint reconstruction may not be imposed on actual deficiency vectors unless additional \(H_0^1\) regularity is proved.

Parents: v13.667, v13.742, v13.779–783.

## 0. Synchronization

Immediately before this write the live ledger head is v13.783 External Audit Round 100. Round 100 PASSes v13.781–782 but records a decisive operator-theoretic clarification that requires cleaning up two earlier Lane-A statements.

Primary source: Suzuki v2, Sections 6.2, 8.2, 8.3.

## 1. Source facts that control the correction [P/D]

Suzuki proves:

1. \(T_a=A_a-\lambda I\) is invertible for \(\lambda<\lambda_a\).
2. The deficiency vectors satisfy
\[
T_av_\pm=C_\pm e^{\pm x}.
\]
3. The derivative map
\[
D=i\,d/dx:H_0^1(-a,a)\to L_0^2(-a,a)
\]
extends by completion to an isometric isomorphism
\[
\boxed{
\bar D:\mathcal H(T_a)\overset{\sim}{\longrightarrow}\mathcal H(S_a).
}
\]
4. Suzuki explicitly notes
\[
\mathcal H(T_a)\hookrightarrow L^2(-a,a),
\qquad
\mathcal H(S_a)\not\subset L^2(-a,a),
\]
and, crucially,
\[
\boxed{
\bar D(\mathbf 1_{[-a,a]})\neq0.
}
\]
5. The self-adjoint transported operator satisfies
\[
\boxed{
S_a=\bar D\,T_a\,\bar D^{-1}.
}
\]
Hence, for \(u_z=\bar Dv_z\),
\[
\boxed{
S_au_z=\bar D e_z.
}
\]
At \(z=\pm i\), with the chosen deficiency normalization,
\[
\boxed{
S_au_\pm=C_\pm\bar D e_{\pm i}.
}
\tag{1}
\]

Equation (1) is exact at the abstract/projected transported-operator level.

## 2. Why the endpoint reconstruction in v13.779 is not source-faithful [R]

v13.779 §4 applied the core identity
\[
D:H_0^1(-a,a)\to L_0^2(-a,a)
\]
directly to the actual deficiency vectors and concluded
\[
v_\pm(\pm a)=0,
\qquad
v(x)=-i\int_{-a}^{x}u(t)\,dt,
\qquad
\int_{-a}^{a}u=0.
\]

This inference is not justified for the actual deficiency vectors.

The source-level deficiency vectors are
\[
v_z=T_a^{-1}e_z\in\mathfrak D(T_a)\subset\mathfrak D(A_a),
\]
while Suzuki explicitly states that
\[
\mathfrak D(A_a)\supsetneq H_0^1(-a,a)
\]
and contains constants.

Therefore one may not assume
\[
v_z\in H_0^1(-a,a)
\]
or impose Dirichlet endpoint values on \(v_z\) merely because \(D\) has that core realization.

The transported object is
\[
u_z=\bar Dv_z
\]
in the completion \(\mathcal H(S_a)\), not necessarily the ordinary \(L^2\) derivative \(i v_z'\).

Thus the following v13.779 statements are superseded for the actual deficiency vectors:

- \(v_\pm(\pm a)=0\);
- the endpoint integral reconstruction formula;
- the zero-mean constraint interpreted literally in \(L^2\);
- any argument that treats \(u_\pm\) as an ordinary derivative function without first proving additional regularity.

## 3. What survives from the parity differentiation in v13.779 [D/G]

The raw first-kind equation (8.5),
\[
\int_{-a}^{a}k(x,y)(-v_\pm(y))\,dy
=
C_\pm e^{\pm x}+A_\pm x+B_\pm,
\]
is an identity of ordinary functions in \(x\).

Therefore differentiating its **right-hand side** once or twice remains valid as a statement about that raw primitive equation:
\[
\partial_x(Ce^x+Ax+B)=Ce^x+A,
\]
\[
\partial_x^2(Ce^x+Ax+B)=Ce^x.
\]

What is not valid is to identify those ordinary derivatives with \(\bar Dv_\pm\) or with \(S_au_\pm\) by endpoint/core calculus.

Hence the correct guardrail is:
\[
\boxed{
\text{ordinary }x\text{-differentiation of (8.5)}
\neq
\text{application of }\bar D\text{ to the deficiency vector}.
}
\tag{2}
\]

## 4. Correction of the earlier retraction of the \(S_a\) defect identity [R/D]

v13.742 and v13.779 retracted
\[
S_au_\pm=C_\pm\bar D e_{\pm i}
\]
as though Suzuki's statement that (8.5) is different from this equation meant that the transported identity itself fails.

Round 100 rechecked the source and resolved the ambiguity.

The exact identity (1) follows from
\[
S_a=\bar DT_a\bar D^{-1}
\]
and
\[
T_av_\pm=C_\pm e_{\pm i}.
\]

Suzuki's warning instead distinguishes this rigorous projected operator equation from the **raw unprojected kernel equation**
\[
\int k(x,y)(-v_\pm(y))\,dy
=
C_\pm e^{\pm x}+A_\pm x+B_\pm.
\]

Therefore the correct statement is
\[
\boxed{
S_au_\pm=C_\pm\bar D e_{\pm i}
\quad\text{is exact},
}
\tag{3}
\]
while
\[
\boxed{
\text{the raw Fredholm operator in (8.5) is not literally }S_a.
}
\tag{4}
\]

This is the precise projected-versus-raw distinction.

## 5. What remains invalid from the old shortcut constructions [G]

Equation (3) does **not** license replacing the raw first-kind kernel in (8.5) by an ordinary \(L^2\) inverse of \(S_a\).

The abstract expression
\[
u_\pm=C_\pm S_a^{-1}\bar D e_{\pm i}
\]
is valid only when \(S_a^{-1}\) means the self-adjoint operator obtained through the unitary equivalence
\[
S_a^{-1}=\bar DT_a^{-1}\bar D^{-1}
\]
on the appropriate energy-space realization.

It must not be interpreted as:

- inversion of the raw integral operator \(f\mapsto\int k(x,y)f(y)\,dy\);
- deletion of the affine \(A_\pm x+B_\pm\) terms in (8.5);
- ordinary \(L^2\) inversion on a zero-mean function space without the completion/domain structure.

Thus the exact transported defect solve and the raw first-kind reconstruction coexist without contradiction.

## 6. Correct three-level hierarchy [D]

The source-faithful hierarchy is now:

### Level I — original deficiency solve
\[
\boxed{
T_av_\pm=C_\pm e_{\pm i},
\qquad
v_\pm=C_\pm T_a^{-1}e_{\pm i}.
}
\]

### Level II — transported projected solve
\[
\boxed{
u_\pm=\bar Dv_\pm,
\qquad
S_au_\pm=C_\pm\bar D e_{\pm i}.
}
\]

### Level III — raw first-kind primitive representation
\[
\boxed{
\int k(x,y)(-v_\pm(y))\,dy
=
C_\pm e^{\pm x}+A_\pm x+B_\pm.
}
\]

The affine constants belong only to Level III. They are global functionals of the unique Level-I solution.

## 7. Parity transport without endpoint assumptions [D]

Reflection commutes with \(T_a\) and \(S_a\). On the core,
\[
DR=-RD.
\]
Because \(R\) is bounded on the corresponding energy spaces, the relation extends by continuity:
\[
\boxed{
\bar D R=-R\bar D.
}
\tag{5}
\]

Hence \(\bar D\) reverses parity abstractly:

- an even component of \(v\) maps to an odd transported component;
- an odd component of \(v\) maps to an even transported component.

This parity reversal is valid without identifying \(\bar Dv\) with an ordinary endpoint derivative.

## 8. Dependency cleanup [G]

The following remain valid:

- v13.781 primitive-affine nonclosure theorem;
- v13.782 source-level resolvent closure
\[
r_{0,a}=\ell_{0,a}((T_a^{(+)})^{-1}\cosh),
\qquad
r_{1,a}=\ell_{1,a}((T_a^{(-)})^{-1}\sinh);
\]
- the Section-6 boundary triple and finite Weyl algebra;
- the abstract transported solve through \(S_a\).

The following are superseded:

- v13.779 §4 endpoint reconstruction for actual deficiency vectors;
- v13.779's blanket retraction of the exact \(S_a\) deficiency identity;
- any later use of literal endpoint values or ordinary zero-mean derivatives for \(u_\pm\) without a separate regularity theorem.

## 9. Result

\[
\boxed{
T_av_\pm=C_\pm e_{\pm i}
\Longleftrightarrow
S_a(\bar Dv_\pm)=C_\pm\bar D e_{\pm i}.
}
\]

At the same time,
\[
\boxed{
\text{raw (8.5) Fredholm operator}\neq S_a
}
\]
as operator realizations, and the affine terms in (8.5) remain genuine primitive reconstruction data.

Most importantly,
\[
\boxed{
\bar Dv_\pm\text{ must not be replaced by the ordinary derivative }iv_\pm'
}
\]
unless \(v_\pm\in H_0^1\) is independently proved.

The next quantitative Lane-A gates should therefore use either the source-level resolvent \(T_a^{-1}\) or the abstract projected \(S_a^{-1}\), while keeping the raw affine traces \(r_0,r_1\) as Level-III observables.
