# Cone Derivation Ledger v13.782 — Lane A Source Resolution: Exact Pre-Integrated Deficiency Solve and Global Scalar Closure of the Affine Ratios

Date: 2026-09-25

Lane: A.

Status: [P/D] direct Suzuki-v2 source extraction; [D] exact pre-integrated deficiency equation; [D] exact global closure of \(r_{0,A},r_{1,A}\); [G] sharpens v13.781: there are not two extra local/domain equations to discover—the source-level invertible operator already fixes the deficiency vector uniquely; [N] continuous-kernel equation (8.5) alone still does not provide an independent finite-dimensional Schur closure.

Parents: v13.742, v13.773, v13.779–781.

## 0. Synchronization and source

Immediately before this write the live ledger head is v13.781; no collision is present.

Primary source checked directly:
Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v2, Sections 6.2 and 8.3.

The decisive source statements are:

- Section 6.2: for the adjoint,
\[
T_a(\mathscr D_a^*v)=i(T_av)',
\]
and the deficiency equations \(\mathscr D_a^*v=\pm iv\) are equivalent to
\[
i(T_av)'=\pm i(T_av).
\]
Since \(\lambda<\lambda_a\), \(T_a=A_a-\lambda I\) is invertible on \(L^2(-a,a)\). Therefore
\[
\boxed{T_av_+=C_+e^x,\qquad T_av_-=C_-e^{-x}}
\tag{1}
\]
have unique solutions up to the common scalar \(C_\pm\).

- Section 8.3 rewrites (1) as
\[
\int_{-a}^{a}[-k_{xx}(x,y)]v_\pm(y)\,dy=C_\pm e^{\pm x}
\tag{2}
\]
and then *formally* twice integrates it to
\[
\int_{-a}^{a}k(x,y)(-v_\pm(y))\,dy
=
C_\pm e^{\pm x}+A_\pm x+B_\pm.
\tag{3}
\]
Suzuki explicitly warns that this argument ignores domain issues and that (3) is different from \(S_au_\pm=C_\pm\bar De_{\pm i}\).

Thus (1), not an extra pair of endpoint equations appended to (3), is the source-level deficiency characterization.

## 1. Exact pre-integrated solve [D]

Because \(T_a\) is invertible,
\[
\boxed{
v_{a,+}=C_{a,+}\,T_a^{-1}e^x,
\qquad
v_{a,-}=C_{a,-}\,T_a^{-1}e^{-x}.
}
\tag{4}
\]

This is an exact source-faithful inverse formula. It must not be confused with the retracted continuous-kernel formula
\[
u_{a,\pm}=S_a^{-1}\bar De_{\pm i}.
\]

The valid inverse in (4) is the inverse of the original distribution-kernel/self-adjoint operator
\[
T_a=A_a-\lambda I
\]
on \(L^2(-a,a)\), before derivative transport.

## 2. Reflection/parity decomposition [D]

The localized Weil operator \(A_a\), hence \(T_a\), commutes with reflection \(R\). Let
\[
T_a^{(+)}:=T_a|_{\rm even},
\qquad
T_a^{(-)}:=T_a|_{\rm odd}.
\]

Since
\[
e^x=\cosh x+\sinh x,
\]
the normalized \(+\) deficiency vector
\[
w_a:=v_{a,+}/C_{a,+}=T_a^{-1}e^x
\]
has exact parity pieces
\[
\boxed{
w_{a,e}=(T_a^{(+)})^{-1}\cosh x,
}
\tag{5E}
\]
\[
\boxed{
w_{a,o}=(T_a^{(-)})^{-1}\sinh x.
}
\tag{5O}
\]

This is the corrected parity-response construction. The crucial difference from v13.776–777 is that the inverses are those of \(T_a\), not \(S_a\), and the inputs are \(\cosh,\sinh\), not derivative-transported sources.

## 3. Exact global closure of the primitive affine ratios [D]

Let
\[
(\mathcal K_av)(x):=\int_{-a}^{a}k(x,y)v(y)\,dy,
\]
where \(k(x,y)=g(x-y)-\lambda N(x,y)\) is Suzuki's continuous kernel in Section 8.3.

Use the v13.779 convention
\[
I_{0,a}:=(\mathcal K_av_{a,e})(0),
\qquad
I_{1,a}:=(\mathcal K_av_{a,o})'(0),
\]
and
\[
r_{0,a}:=I_{0,a}/C_{a,+},
\qquad
r_{1,a}:=I_{1,a}/C_{a,+}.
\]

Substituting (5E)–(5O) gives the exact global scalar formulas
\[
\boxed{
r_{0,a}
=
\left[
\mathcal K_a (T_a^{(+)})^{-1}\cosh
\right](0),
}
\tag{6}
\]
\[
\boxed{
r_{1,a}
=
\left.
\partial_x
\left[
\mathcal K_a (T_a^{(-)})^{-1}\sinh
\right](x)
\right|_{x=0}.
}
\tag{7}
\]

Equivalently, with the exact source trace functionals
\[
\ell_{0,a}(v):=(\mathcal K_av)(0),
\qquad
\ell_{1,a}(v):=(\mathcal K_av)'(0),
\]
\[
\boxed{
r_{0,a}=\ell_{0,a}\!\left((T_a^{(+)})^{-1}\cosh\right),
\qquad
r_{1,a}=\ell_{1,a}\!\left((T_a^{(-)})^{-1}\sinh\right).
}
\tag{8}
\]

These are one independent global scalar functional per parity channel, but they are evaluated on the **source-level \(T_a^{-1}\) solutions**, not on unrestricted inverses of the first-kind continuous operator.

## 4. Affine coefficients [D]

Suzuki's equation (8.5) gives
\[
A_+=-C_+-I_{1,a},
\qquad
B_+=-C_+-I_{0,a}
\]
in the present sign convention. Therefore
\[
\boxed{
\frac{A_+}{C_+}=-(1+r_{1,a}),
\qquad
\frac{B_+}{C_+}=-(1+r_{0,a}).
}
\tag{9}
\]

Equations (6)–(9) close the primitive affine ratios exactly once the original deficiency resolvent \(T_a^{-1}\) is known.

## 5. Relation to v13.781 [G]

v13.781 correctly established that:

- basepoint substitution into (8.5) is tautological;
- the unrestricted first-kind inverse/Schur feedback collapses to \(0/0\);
- the Section-6 Green transverse traces are parity identities.

The present source extraction sharpens the final sentence of v13.781.

There are **not** two additional local boundary equations waiting to be appended to (8.5). Instead, Suzuki's original adjoint equation already fixes the whole deficiency vector through the invertible operator \(T_a\):
\[
\boxed{
\mathscr D_a^*v_+=iv_+
\iff
T_av_+=C_+e^x
\iff
v_+/C_+=T_a^{-1}e^x.
}
\tag{10}
\]

The affine constants in (8.5) are then derived global functionals of this unique solution.

Thus the correct hierarchy is
\[
\boxed{
\text{adjoint/domain equation}
\to
T_a^{-1}e^x
\to
\text{parity pieces}
\to
(r_0,r_1)
\to
(A/C,B/C).
}
\tag{11}
\]

The reverse attempt
\[
(8.5)\to\text{local traces}\to(r_0,r_1)
\]
cannot work because those traces are definitions of the affine constants.

## 6. Why this does not resurrect v13.776–777 [G]

The retracted construction used the transported continuous-kernel solve
\[
S_au_\pm=C_\pm\bar De_{\pm i}.
\]

Suzuki explicitly states that (8.5) is different from this equation.

The present valid construction is instead
\[
v_\pm=C_\pm T_a^{-1}e^{\pm x},
\qquad
u_\pm=\bar Dv_\pm.
\]

Hence
\[
\boxed{
u_{a,+}
=
C_{a,+}\bar D
\left[
(T_a^{(+)})^{-1}\cosh
+
(T_a^{(-)})^{-1}\sinh
\right],
}
\tag{12}
\]
with the analogous reflected formula for \(u_{a,-}\).

No specialization of the generic \(S_a^{-1}\bar De_z\) formula is used.

## 7. Corrected finite-dimensional theorem

**Theorem (source-level global scalar closure).**
For \(\lambda<\lambda_a\), Suzuki's \(+\) deficiency space is one-dimensional and its normalized vector is
\[
w_a=T_a^{-1}e^x.
\]
Reflection decomposes it uniquely as
\[
w_{a,e}=(T_a^{(+)})^{-1}\cosh,
\qquad
w_{a,o}=(T_a^{(-)})^{-1}\sinh.
\]
The two primitive affine ratios in the continuous-kernel Fredholm representation (8.5) are not free boundary parameters. They are the global resolvent traces
\[
r_{0,a}=\ell_{0,a}((T_a^{(+)})^{-1}\cosh),
\]
\[
r_{1,a}=\ell_{1,a}((T_a^{(-)})^{-1}\sinh).
\]
Consequently
\[
A_+/C_+=-(1+r_{1,a}),
\qquad
B_+/C_+=-(1+r_{0,a}).
\]

No independent \(2\times2\) Schur closure exists at the level of (8.5); the exact closure is inherited from the unique source-level resolvent \(T_a^{-1}\).

## 8. Next gates

The remaining problem is now quantitative rather than structural:

1. express or bound the two resolvent traces (6)–(7);
2. determine their growth as \(a\to\infty\);
3. in particular test
\[
e^{-a}(1+r_{1,a})\to0,
\qquad
e^{-a}\{a(1+r_{1,a})+1+r_{0,a}\}\to0,
\]
which is exactly the corrected affine-edge contamination gate;
4. insert the normalized shape (12) into the true Weyl channel ratio from v13.757, with all v13.773-invalid Schur formulas removed.

## Result

\[
\boxed{
r_{0,a}
=
\ell_{0,a}((T_a^{(+)})^{-1}\cosh),
\qquad
r_{1,a}
=
\ell_{1,a}((T_a^{(-)})^{-1}\sinh).
}
\]

The long-running affine-closure question is therefore resolved at the source level: the two coefficients are unique global resolvent traces of Suzuki's original deficiency solve, not extra extension parameters and not quantities recoverable from a local feedback system.
