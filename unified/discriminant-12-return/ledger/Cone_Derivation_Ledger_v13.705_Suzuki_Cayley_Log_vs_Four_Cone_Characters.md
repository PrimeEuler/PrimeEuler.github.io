# Cone Derivation Ledger v13.705 — Suzuki Cayley/Log Variables versus the Four Cone Characters

Date: 2026-09-23

Status: exact comparison gate. This entry tests the actual finite-\(a\) Suzuki Friedrichs/Kreĭn quantities already derived in v13.647, v13.661, v13.684–685 against the four logarithmic character directions established and externally audited in v13.703–704. It records only correspondences that follow from the existing formulas.

## 0. Synchronization and audit state

Immediately before this write the live head was v13.704, External Audit Round 80, commit \`7ef91e2df0223d369ca685d84c9c642a811734cd\`. Round 80 independently verified v13.696–703, including \(\mathcal Z^3=iI\), the two distinct \(\mu_4\) torsion slices, and all v13.703 semidirect-product relations. No v13.705 collision was present.

Relevant Suzuki inputs:

- v13.647: exact abstract boundary-triple Cayley factor
  \[
  s_A(\zeta)=\frac{m_A(\zeta)-i}{m_A(\zeta)+i},
  \qquad
  b_{A,\theta}=1-e^{i\theta}s_A.
  \]
  The printed Suzuki characteristic factors identically as
  \[
  W_A(\theta;z)
  =(z-i)F_{A,+}(z)
  [1-e^{i\theta}s_A^{Suz}(z)]
  \]
  with
  \[
  s_A^{Suz}(z)=-
  \frac{(z+i)F_{A,-}(z)}
       {(z-i)F_{A,+}(z)}.
  \]
  Equality \(s_A^{Suz}=s_A\) for a concrete boundary triple remains an explicit open normalization gate.

- v13.685:
  \[
  W_0=A+B,\qquad W_\pi=A-B,
  \]
  \[
  m_a(z)=-i\frac{A+B}{A-B},
  \]
  and the normalized extension cross-ratio is
  \[
  \Delta^{(a)}_{0/\pi}(z;z_*)
  =\frac{m_a(z)}{m_a(z_*)}.
  \]

## 1. Cone character target

v13.703 gives
\[
\tau=a+i\alpha,\qquad
\ell=s+i\phi
\]
with character table
\[
\begin{array}{c|cc}
&F&C\\ \hline
a=\Re\tau&+&+\\
\alpha=\Im\tau&+&-\\
s=\Re\ell&-&+\\
\phi=\Im\ell&-&-
\end{array}.
\]

A Suzuki quantity can be assigned to one of these directions only if its transformation under the two relevant involutions is actually known. A generic complex logarithm supplies a real modulus and phase, but this alone does not determine the \(F\)-parity.

## 2. Boundary extension phase is a proved phase coordinate

The extension parameter occurs only through
\[
e^{i\theta}.
\]
Thus
\[
\theta\mapsto-\theta
\]
under coefficient conjugation of the scalar phase:
\[
\overline{e^{i\theta}}=e^{-i\theta}.
\]

Therefore \(\theta\) is a genuine \(C\)-odd phase coordinate.

It is modulus-neutral: changing \(\theta\) does not alter \(|e^{i\theta}|=1\).

Hence:
\[
\boxed{
\theta\text{ lies in a phase direction, not a real-modulus direction.}
}
\]

However, no established Suzuki operation has yet been proved to realize the cone factor-exchange involution \(F\) on the extension parameter. Therefore one cannot distinguish from existing results whether \(\theta\) should be identified with the cone's \(C\)-odd/F-even direction \(\Im\tau\) or \(C\)-odd/F-odd direction \(\Im\ell\).

Result:
\[
\boxed{
\theta:\ C\text{-odd phase is PROVED; }F\text{-parity is OPEN.}
}
\]

## 3. Cayley/Schur variable: exact modulus-phase split

For any nonzero Suzuki/abstract Schur variable \(s\), choose a local logarithm
\[
L_s=\log s=\log|s|+i\arg s.
\]

For a scalar Weyl function with the standard reality property
\[
m(\bar\zeta)=\overline{m(\zeta)},
\]
the Cayley transform
\[
s(\zeta)=\frac{m(\zeta)-i}{m(\zeta)+i}
\]
obeys
\[
\boxed{
s(\bar\zeta)=\frac{1}{\overline{s(\zeta)}}.
}
\]

Proof:
\[
s(\bar\zeta)
=
\frac{\bar m-i}{\bar m+i}
=
\frac{1}{\overline{(m-i)/(m+i)}}.
\]

Therefore, locally modulo \(2\pi i\),
\[
\boxed{
L_s(\bar\zeta)=-\overline{L_s(\zeta)}.
}
\]

Writing
\[
L_s=u+iv,
\]
gives
\[
\boxed{
u(\bar\zeta)=-u(\zeta),\qquad
v(\bar\zeta)=v(\zeta)
}
\]
modulo phase branches.

This is **not** the same transformation law as coefficient conjugation on the cone torus, which sends a generic logarithm \(u+iv\mapsto u-iv\). Spectral reflection \(\zeta\mapsto\bar\zeta\) combines conjugation with Cayley inversion.

Thus the Suzuki Cayley log naturally carries an inversion-conjugation involution:
\[
\boxed{L_s\mapsto-\bar L_s.}
\]

In the cone table, the same formal sign pattern occurs for the product involution \(FC\) acting on the boost logarithm:
\[
FC:\ell\mapsto-\bar\ell.
\]

Hence there is an exact **transformation-law match**
\[
\boxed{
L_s\ \text{under spectral conjugation}
\quad\leftrightarrow\quad
\ell\ \text{under }FC.
}
\]

This is a proved equivariance-pattern correspondence, not yet an operator intertwiner.

Under this combined involution:
- \(\Re L_s\) is odd;
- \(\Im L_s\) is even.

In the cone character table, \(FC\) has the same parity on
\[
\Re\ell=s\quad(\text{odd}),\qquad
\Im\ell=\phi\quad(\text{even}).
\]

Therefore:
\[
\boxed{
\Re\log s\leftrightarrow\Re\ell
\text{ and }
\Im\log s\leftrightarrow\Im\ell
}
\]
is proved **only at the level of the combined \(FC\) parity pattern**.

Separate \(F\) and \(C\) identification is not proved.

## 4. Boundary factor logarithm mixes extension phase and Cayley log

The exact zero-carrying boundary factor is
\[
b_\theta=1-e^{i\theta}s.
\]

Its logarithm is
\[
\boxed{
L_b=\log(1-e^{i\theta+L_s}).
}
\]

Thus the actual Kreĭn boundary determinant does not split linearly into a pure scale log plus a pure rapidity log. It is a nonlinear function of the combined complex coordinate
\[
\boxed{\eta=i\theta+L_s.}
\]

Under simultaneous scalar conjugation and spectral conjugation,
\[
e^{i\theta}s(\zeta)
\mapsto
e^{-i\theta}s(\bar\zeta)
=
\frac{e^{-i\theta}}{\overline{s(\zeta)}}.
\]

No existing cone involution has yet been proved to intertwine this full Möbius/nonlinear boundary factor. Therefore:
\[
\boxed{
L_b\text{ has no proved one-character assignment among }
\Re\tau,\Im\tau,\Re\ell,\Im\ell.
}
\]

This is a useful negative result: the determinant factor is composite; the primitive Cayley coordinate should be compared first.

## 5. W0/Wpi cross-ratio log

v13.685 gives
\[
\Delta_{0/\pi}^{(a)}(z;z_*)
=
\frac{m_a(z)}{m_a(z_*)}.
\]

Choose a local logarithm:
\[
L_\Delta
=
\log m_a(z)-\log m_a(z_*).
\]

This has the ordinary modulus/phase decomposition
\[
\boxed{
\Re L_\Delta
=
\log\frac{|m_a(z)|}{|m_a(z_*)|},
}
\]
\[
\boxed{
\Im L_\Delta
=
\arg m_a(z)-\arg m_a(z_*).
}
\]

If \(m_a(\bar z)=\overline{m_a(z)}\) and the base point is real or otherwise conjugation-fixed, then
\[
\boxed{
L_\Delta(\bar z)=\overline{L_\Delta(z)}
}
\]
locally modulo \(2\pi i\).

Therefore:
- \(\Re L_\Delta\) is conjugation-even;
- \(\Im L_\Delta\) is conjugation-odd.

This exactly matches the \(C\)-parity of either cone complex logarithm:
\[
\Re\tau,\Re\ell:\ C=+,
\qquad
\Im\tau,\Im\ell:\ C=-.
\]

But again there is no proved Suzuki realization of cone factor exchange \(F\) on this cross-ratio. Thus:
\[
\boxed{
L_\Delta:
\text{ modulus/phase }C\text{-split PROVED; }
\tau\text{ vs }\ell\text{ assignment OPEN.}
}
\]

## 6. Bulk relative determinant

v13.647 separates
\[
\Delta^{tot}
=
\Delta^{bulk}\Delta^{bdry}.
\]

For any nonzero normalized bulk determinant,
\[
L_{\rm bulk}=\log\widehat\Delta_A^{bulk}
\]
has
\[
\Re L_{\rm bulk}=\log|\widehat\Delta_A^{bulk}|,
\qquad
\Im L_{\rm bulk}=\arg\widehat\Delta_A^{bulk}.
\]

Under the standard real-operator determinant symmetry
\[
\widehat\Delta_A^{bulk}(\bar\zeta)
=
\overline{\widehat\Delta_A^{bulk}(\zeta)},
\]
one obtains
\[
L_{\rm bulk}(\bar\zeta)=\overline{L_{\rm bulk}(\zeta)}
\]
locally.

Thus the bulk determinant supplies another proved \(C\)-even modulus / \(C\)-odd phase pair.

There is currently no exact formula showing that its modulus is specifically the cone scale coordinate \(\Re\tau\), nor that its phase is specifically \(\Im\tau\). The tempting assignment
\[
L_{\rm bulk}\stackrel?{\leftrightarrow}\tau
\]
is therefore **OPEN**, not proved.

## 7. Strongest proved four-direction comparison

The current exact information is:

\[
\begin{array}{c|c|c|c}
\text{Suzuki quantity}&\text{proved transformation}&\text{cone match}&\text{status}\\ \hline
\theta&
C\text{-odd phase}&
\Im\tau\text{ or }\Im\ell&
\text{partial}\\
\Re\log s&
\text{odd under }\zeta\mapsto\bar\zeta&
\Re\ell\text{ under }FC&
\text{parity match proved}\\
\Im\log s&
\text{even under }\zeta\mapsto\bar\zeta&
\Im\ell\text{ under }FC&
\text{parity match proved}\\
\Re\log\Delta_{0/\pi}&
C\text{-even modulus}&
\Re\tau\text{ or }\Re\ell&
\text{partial}\\
\Im\log\Delta_{0/\pi}&
C\text{-odd phase}&
\Im\tau\text{ or }\Im\ell&
\text{partial}\\
\Re\log\Delta^{bulk}&
C\text{-even modulus}&
\Re\tau\text{ or }\Re\ell&
\text{partial}\\
\Im\log\Delta^{bulk}&
C\text{-odd phase}&
\Im\tau\text{ or }\Im\ell&
\text{partial}
\end{array}
\]

The only correspondence currently sharp enough to distinguish a **boost-like** logarithm is the Cayley identity
\[
\boxed{
\log s(\bar\zeta)
=
-\overline{\log s(\zeta)},
}
\]
which matches
\[
\boxed{
FC:\ell\mapsto-\bar\ell.
}
\]

This is the strongest proved export from the four-character cone table into the actual Suzuki formulas.

## 8. What is NOT proved

The following stronger identifications are not currently justified:
\[
\log\Delta^{bulk}=\tau,
\]
\[
\log s=\ell,
\]
\[
\theta=\Im\tau,
\]
\[
\theta=\Im\ell.
\]

Nor is there yet a Suzuki pair of independently defined involutions that has been shown to realize the cone \(F\) and \(C\) separately.

Thus the full four-character correspondence
\[
(\Re\tau,\Im\tau,\Re\ell,\Im\ell)
\longleftrightarrow
(\text{four Suzuki quantities})
\]
does **not** yet exist.

## 9. Structural interpretation

The actual Suzuki quantities separate into three levels:

1. **Primitive Cayley coordinate**
   \[
   s=\frac{m-i}{m+i},
   \]
   whose logarithm transforms by inversion-conjugation under spectral reflection.

2. **Extension phase**
   \[
   e^{i\theta},
   \]
   an independent unit-circle boundary parameter.

3. **Determinant/characteristic factors**
   \[
   1-e^{i\theta}s,\qquad
   \Delta^{bulk},\qquad
   \Delta_{0/\pi},
   \]
   which are nonlinear or relative composites.

This suggests that the cone's primitive logarithmic coordinates should be compared to \(s\) and \(e^{i\theta}\) before comparing them to the full determinant.

## 10. Relation to the Friedrichs-vs-Zeeman failure

External Audit Round 78 (v13.689) found the independent Friedrichs-Galerkin versus Zeeman cross-ratio gate fails stably at roughly 86–88% discrepancy.

Nothing in the present parity analysis repairs that failure.

However, the present result identifies a concrete normalization question worth testing: whether the even/odd relative normalization noted by v13.689 is effectively mixing the primitive Cayley modulus/phase directions before the cross-ratio is formed.

This is a testable diagnostic, not a diagnosis.

## 11. Result

\[
\boxed{
\textbf{PROVED: }
s(\bar\zeta)=1/\overline{s(\zeta)}
}
\]
for the abstract Weyl-Cayley transform with standard reality symmetry.

\[
\boxed{
\textbf{PROVED: }
\log s(\bar\zeta)=-\overline{\log s(\zeta)}
}
\]
locally modulo \(2\pi i\).

\[
\boxed{
\textbf{PROVED PARITY MATCH: }
\log s
\text{ has the same combined }FC\text{ transformation law as }\ell.
}
\]

\[
\boxed{
\textbf{PROVED: }
\theta\text{ is a conjugation-odd phase coordinate.}
}
\]

\[
\boxed{
\textbf{PROVED: }
\log\Delta_{0/\pi}
\text{ and }\log\Delta^{bulk}
\text{ split into conjugation-even modulus and conjugation-odd phase}
}
\]
under their standard reality hypotheses.

\[
\boxed{
\textbf{OPEN: separate }F/C\textbf{ realization on Suzuki data.}
}
\]

\[
\boxed{
\textbf{OPEN: exact assignments to all four }
(\Re\tau,\Im\tau,\Re\ell,\Im\ell).
}
\]

## 12. Next gate

Construct a candidate Suzuki factor-exchange involution from the actual deficiency pair \(u_+,u_-\) and reflection \(R:u_+\leftrightarrow u_-\). Determine its action on
\[
m_a,\quad s_a,\quad e^{i\theta},\quad W_0,\quad W_\pi.
\]

If that reflection realizes the missing \(F\), the combined data may distinguish the four character directions exactly. If it does not, record the obstruction rather than forcing the correspondence.
