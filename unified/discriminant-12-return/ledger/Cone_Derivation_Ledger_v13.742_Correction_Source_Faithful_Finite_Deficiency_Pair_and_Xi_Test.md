# Cone Derivation Ledger v13.742 — Correction: Source-Faithful Finite Deficiency Pair and Xi Test

Date: 2026-09-23

Status: correction of v13.740 in response to External Audit Round 88 (v13.741). The finite-\(A\) deficiency pair is rebuilt from Suzuki's actual Section-8 deficiency vectors, not from the source-contradicted substitution \(u_\pm=S_A^{-1}\bar D e_{\pm i}\).

Synchronization: live head before write was v13.741, commit \`11d66482ba918a0e61d5da949d91c647206c8a4b\`. The audit verified all v13.740 algebra conditional on its definitions but correctly rejected the deficiency-source definition.

## 1. Retraction of the invalid finite source identity

v13.740 used
\[
S_Au_\pm=\bar D e_{\pm i}
\]
up to normalization.

Suzuki explicitly states that his deficiency equation (8.5) is different from
\[
S_Au_\pm=C_\pm\bar D e_{\pm i}.
\]

Therefore the following v13.740 identification is retracted:
\[
F_{A,\pm}(z)
=
\overline{\langle\bar D e_{\bar z},
S_A^{-1}\bar D e_{\pm i}\rangle}
\stackrel{\rm invalid}{=}
\text{actual deficiency pairing}.
\]

Consequently the \(P_A\), \(\mathscr R_A\), and \(\Delta_A\) of v13.740 are not established finite Suzuki quantities when built from that inverse-source formula.

The infinite-volume target from v13.739 remains unaffected.

## 2. Correct finite deficiency vectors

Let \(v_{A,\pm}\) be Suzuki's actual finite deficiency vectors in the \(T_A\)-space, with constants \(C_{A,\pm}\), characterized by the Section-8 deficiency construction and its integral equation (8.5).

The source-level equation has the form
\[
\boxed{
\mathcal L_A[v_{A,\pm}](x)
=
C_{A,\pm}e^{\pm x}
+
A_{A,\pm}x
+
B_{A,\pm},
}
\]
where \(\mathcal L_A\) denotes the left side of Suzuki's (8.5), and
\[
\boxed{
A_{A,\pm}
=
\int_{-A}^{A}k_x(0,y)(-v_{A,\pm}(y))\,dy
\mp C_{A,\pm},
}
\]
\[
\boxed{
B_{A,\pm}
=
\int_{-A}^{A}k(0,y)(-v_{A,\pm}(y))\,dy
-
C_{A,\pm}.
}
\]

The affine terms are genuine boundary/domain data and may not be discarded.

Transport the actual deficiency vectors by the unitary/isometric extension:
\[
\boxed{
u_{A,\pm}:=\bar D\,v_{A,\pm}\in H(S_A).
}
\]

This definition is source-faithful and does not require applying \(S_A^{-1}\) to \(\bar D e_{\pm i}\).

## 3. Correct generic defect vector

For a regular spectral parameter \(z\) in the regime where Suzuki states
\[
T_Av_{A,z}=e_z,
\]
the transported vector
\[
u_{A,z}:=\bar D v_{A,z}
\]
satisfies
\[
\boxed{
S_Au_{A,z}=\bar D e_z.
}
\]

Thus the generic vector may still be computed from the continuous-kernel solve:
\[
\boxed{
u_{A,z}=S_A^{-1}\bar D e_z,
}
\]
where this inverse is defined.

The correction is specifically that one must **not specialize this generic formula to the deficiency vectors** \(u_{A,\pm}\).

## 4. Source-faithful finite pairings

Define
\[
\boxed{
\mathcal F_{A,\pm}^{\rm true}(z)
:=
\overline{
\langle
u_{A,\bar z},
u_{A,\pm}
\rangle_{S_A}
}.
}
\]

Using the valid generic equation for \(u_{A,\bar z}\),
\[
\langle
u_{A,\bar z},
u_{A,\pm}
\rangle_{S_A}
=
\langle
S_Au_{A,\bar z},
u_{A,\pm}
\rangle
=
\langle
\bar D e_{\bar z},
u_{A,\pm}
\rangle
\]
in the form/duality sense appropriate to the completion.

Hence an equivalent source-faithful representation is
\[
\boxed{
\mathcal F_{A,\pm}^{\rm true}(z)
=
\overline{
\langle
\bar D e_{\bar z},
u_{A,\pm}
\rangle
},
}
\]
not
\[
\overline{
\langle
\bar D e_{\bar z},
S_A^{-1}\bar D e_{\pm i}
\rangle
}.
\]

All affine/domain information from (8.5) is retained inside \(u_{A,\pm}\).

## 5. Correct finite paired amplitude

Define
\[
\boxed{
P_A^{\rm true}(z)
:=
(z-i)\mathcal F_{A,+}^{\rm true}(z)
-
(z+i)\mathcal F_{A,-}^{\rm true}(z).
}
\]

This has exactly the same algebraic channel pairing as Suzuki's Section-7 target but uses the actual finite deficiency vectors.

If the chosen deficiency basis has constants \(C_{A,\pm}\) not already absorbed into \(u_{A,\pm}\), they must be retained:
\[
\boxed{
P_A^{\rm true}(z)
=
(z-i)\overline{\langle u_{A,\bar z},C_{A,+}u_{A,+}^{(0)}\rangle_{S_A}}
-
(z+i)\overline{\langle u_{A,\bar z},C_{A,-}u_{A,-}^{(0)}\rangle_{S_A}}.
}
\]

A common normalization may later cancel projectively; unequal \(+\)/\(-\) normalizations do not.

## 6. Correct Weyl relation

Let
\[
A_A^{\rm true}:=(z-i)\mathcal F_{A,+}^{\rm true},
\qquad
B_A^{\rm true}:=(z+i)\mathcal F_{A,-}^{\rm true}.
\]

For the same boundary basis used in Suzuki's characteristic, the algebraic Weyl relation is
\[
\boxed{
m_A(z)
=
-i\frac{A_A^{\rm true}(z)+B_A^{\rm true}(z)}
{A_A^{\rm true}(z)-B_A^{\rm true}(z)}.
}
\]

Therefore
\[
\boxed{
A_A^{\rm true}
=
\frac{1+i m_A}{2}P_A^{\rm true},
\qquad
B_A^{\rm true}
=
\frac{i m_A-1}{2}P_A^{\rm true}.
}
\]

The algebra from v13.740 survives exactly once the true pairings replace the false inverse-source pairings.

## 7. Correct normalization-free Xi test

The audited infinite-volume target is
\[
T_{\rm pair}(z)
=
C_\xi\frac{\Xi(-iz)}{E(z)}.
\]

Choose \(z_*\) away from zeros. Define
\[
\boxed{
\mathscr R_A^{\rm true}(z;z_*)
:=
\frac{P_A^{\rm true}(z)}
{P_A^{\rm true}(z_*)}
\frac{\Xi(-iz_*)E(z)}
{\Xi(-iz)E(z_*)}.
}
\]

If the actual finite deficiency amplitude obeys
\[
P_A^{\rm true}(z)
=
c_A T_{\rm pair}(z)(1+o(1))
\]
with a single \(z\)-independent common normalization \(c_A\), then
\[
\boxed{
\mathscr R_A^{\rm true}(z;z_*)\to1.
}
\]

This criterion is now source-faithful. It remains a proposed convergence test, not a proved convergence theorem.

## 8. Correct logarithmic-derivative test

Define
\[
\boxed{
\Delta_A^{\rm true}(z)
=
\frac{(P_A^{\rm true})'(z)}
{P_A^{\rm true}(z)}
-
i\frac{L'(1/2-iz)}
{1+L(1/2-iz)}.
}
\]

Then projective convergence implies
\[
\boxed{
\Delta_A^{\rm true}(z)\to0.
}
\]

Equivalently,
\[
\boxed{
\frac{d}{dz}\log[E(z)P_A^{\rm true}(z)]
\to
-iL(1/2-iz)
=
\frac{d}{dz}\log\Xi(-iz).
}
\]

Again, this is valid only with the actual Section-8 deficiency vectors from (8.5).

## 9. Where the affine terms enter after differentiation

The audit's correction also clarifies the earlier compensated-edge analysis.

Equation (8.5) contains
\[
A_{A,\pm}x+B_{A,\pm}.
\]

Differentiating once produces the constant \(A_{A,\pm}\); differentiating twice kills the affine terms in the interior. Therefore an interior twice-differentiated equation can look like the naive \(S_Au=C\bar De_{\pm i}\) equation while still missing the boundary/domain data.

This explains why the earlier formal screw/Green symbol analysis can remain useful for the **interior current**, yet cannot determine the deficiency vector without boundary conditions.

The affine coefficients are precisely integration constants/boundary data lost by the twice-differentiated reduction.

Thus:
\[
\boxed{
\text{bulk explicit-formula current}
+
\text{two boundary constants}
\quad\text{are both required.}
}
\]

## 10. Edge scaling of the affine terms

Set the right-edge coordinate
\[
x=A-\xi.
\]

Then
\[
A_{A,+}x+B_{A,+}
=
A\,A_{A,+}
+
B_{A,+}
-
A_{A,+}\xi.
\]

After the \(e^{-A}\) deficiency scaling, these terms vanish only if
\[
e^{-A}(A|A_{A,+}|+|B_{A,+}|)\to0.
\]

This is **not yet proved**.

If instead \(A_{A,+}\) or \(B_{A,+}\) grows at \(e^A\) scale, an affine edge remnant survives and changes the compensated source/edge boundary condition.

Therefore the next decisive estimate is
\[
\boxed{
e^{-A}A_{A,\pm},
\qquad
e^{-A}B_{A,\pm}.
}
\]

The previous edge source \(e^{-\xi}-\delta_0\) should now be regarded as the bulk/core contribution pending control of these affine boundary terms.

## 11. Reworked equation for the edge limit

The corrected schematic edge deficiency problem is therefore
\[
\boxed{
S_{\rm edge}q_\pm
=
\pm i(e^{-\xi}-\delta_0)
+
\mathcal B_\pm,
}
\]
where \(\mathcal B_\pm\) is the limiting boundary functional generated by the scaled affine coefficients in Suzuki (8.5).

If
\[
e^{-A}A_{A,\pm}\to0,
\qquad
e^{-A}B_{A,\pm}\to0,
\]
then
\[
\mathcal B_\pm=0
\]
and the earlier compensated edge equation is recovered.

If not, the edge equation must be augmented by the surviving trace/affine functional.

This is the correct conditional form; the boundary contribution may not be set to zero in advance.

## 12. Result

\[
\boxed{\textbf{RETRACTED: }u_{A,\pm}=S_A^{-1}\bar D e_{\pm i}.}
\]

\[
\boxed{\textbf{CORRECT: }u_{A,\pm}=\bar Dv_{A,\pm},\quad v_{A,\pm}\text{ determined by Suzuki (8.5).}}
\]

\[
\boxed{
P_A^{\rm true}(z)
=
(z-i)\overline{\langle u_{A,\bar z},u_{A,+}\rangle_{S_A}}
-
(z+i)\overline{\langle u_{A,\bar z},u_{A,-}\rangle_{S_A}}.
}
\]

The projective Xi test survives in corrected form:
\[
\boxed{
\mathscr R_A^{\rm true}(z;z_*)\to1,
}
\]
but is not yet established until \(P_A^{\rm true}\) is computed from (8.5).

Most importantly, the finite-to-edge equation must retain a possible boundary correction:
\[
\boxed{
S_{\rm edge}q_\pm
=
\pm i(e^{-\xi}-\delta_0)+\mathcal B_\pm.
}
\]

## Next gate

Compute or bound Suzuki's actual coefficients \(C_{A,\pm},A_{A,\pm},B_{A,\pm}\) from (8.5), exploiting reflection to reduce the two deficiency equations to one. Determine whether
\[
e^{-A}A_{A,\pm},\ e^{-A}B_{A,\pm}\to0.
\]

Only if those limits vanish may the pure compensated edge source from the earlier gate be promoted to the full deficiency-source limit.
