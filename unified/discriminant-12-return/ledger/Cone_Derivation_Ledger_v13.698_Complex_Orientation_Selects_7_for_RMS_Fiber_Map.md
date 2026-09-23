# Cone Derivation Ledger v13.698 — Complex Orientation Selects 7 for the RMS Fiber Map

Date: 2026-09-23

Status labels: **[S]** source-established, **[D]** exact derived, **[N]** limitation, **[I]** interpretation.

## 1. Synchronization

Immediately before this write the live head was v13.697, commit \`973539a4c28222d929d1a6a1c28cc9713db44c98\`; no v13.698 collision was present.

Question: does the already-established oriented complex coordinate
\[
z=X+iY
\]
together with the intrinsic convention
\[
\chi_{-4}\leftrightarrow R_Y:(X,Y,T)\mapsto(X,-Y,T)
\]
independently distinguish the two negative-\(\chi_{12}\) translators \(5\) and \(7\) in the RMS/Casimir fiber map?

## 2. Existing exact identifications [S]

From v13.530 and the independently audited v13.529 stabilizer calculation:
\[
5\leftrightarrow\chi_{-3}\leftrightarrow R_X,
\qquad
7\leftrightarrow\chi_{-4}\leftrightarrow R_Y,
\]
once the already-established \(\chi_{12}/11\) cone-half-turn compatibility is imposed.

The \(\chi_{-4}\) leg has the stronger intrinsic justification:
\[
\sigma_r(i)=\chi_{-4}(r)i.
\]
With the compatible oriented complex coordinate \(z=X+iY\),
\[
\chi_{-4}(r)=-1
\quad\Longleftrightarrow\quad
z\mapsto\bar z
\quad\Longleftrightarrow\quad
Y\mapsto-Y.
\]

On the two negative-\(\chi_{12}\) labels:
\[
\chi_{-4}(5)=+1,\qquad
\chi_{-4}(7)=-1.
\]
Therefore only \(7\) is complex-conjugating / \(Y\)-reflecting.

## 3. RMS/Casimir transfer requires reversal of the signed transverse branch [D]

The centered cone quantities are
\[
G^2=A^2-D^2,\qquad
Q^2=A^2+D^2.
\]
The scalar squares depend only on \(D^2\), so by themselves they forget the sign of the centered displacement. This is exactly the twofold ambiguity found in v13.697.

To lift the scalar transfer to the oriented cone, retain the oriented transverse complex coordinate. The two oriented branches over the same scalar norm are represented by
\[
z=X+iY,\qquad \bar z=X-iY.
\]
Changing the transverse orientation while fixing the distinguished real axis \(X\) is
\[
z\leftrightarrow\bar z,
\]
i.e.
\[
R_Y.
\]

Thus the oriented lift of the RMS/Casimir scalar fiber exchange that changes the transverse branch is the \(Y\)-reflection parity, not the \(X\)-reflection parity.

By the intrinsic cyclotomic convention,
\[
R_Y\leftrightarrow\chi_{-4},
\]
and among \(\{5,7\}\) only \(7\) has \(\chi_{-4}=-1\). Hence
\[
\boxed{
M_{\rm RMS}^{\rm oriented}=\times7.
}
\]

This agrees with, but does not use, the ordering argument of v13.697:
\[
(5,7)\mapsto(11,1).
\]

## 4. Why 5 is excluded [D]

The alternative translator \(5\) has
\[
\chi_{-4}(5)=+1.
\]
Therefore it preserves the chosen complex scalar \(i\) and does not implement
\[
z\mapsto\bar z.
\]
Under the established cone intertwiner it is instead
\[
5\leftrightarrow R_X:(z,T)\mapsto(-\bar z,T).
\]

This flips the distinguished real coordinate \(X\) as well as conjugating the complex expression. It is not the pure transverse-orientation reversal selected by the \(z=X+iY\) convention.

Therefore, once the distinguished real axis \(X\) and compatible complex orientation are retained,
\[
\boxed{
7\text{ is selected and }5\text{ is excluded}.
}
\]

## 5. Independence and logical scope [D/N]

This selection is independent of the numerical ordering
\[
35<36<37
\]
and independent of declaring the input pair to be ordered as \((5,7)\). It uses instead the pre-existing complex/cyclotomic datum
\[
i=\zeta_{12}^3
\]
and the audited identity
\[
\sigma_r(i)=\chi_{-4}(r)i.
\]

However, one additional statement is required to connect the scalar RMS/Casimir transfer to this complex leg: the oriented lift is required to reverse the transverse \(Y\)-branch while keeping the distinguished \(X\)-axis fixed. The scalar identity \(Q^2=A^2+D^2\) alone does not force this lift.

Therefore the strongest exact statement is:
\[
\boxed{
\text{RMS scalar fiber exchange}
+\text{ existing oriented-cone lift }(X\text{ fixed},Y\text{ reversed})
\Longrightarrow \times7.
}
\]

[N] Without the oriented lift, the scalar RMS construction alone still determines only the unordered negative-\(\chi_{12}\) coset and leaves the \(5/7\) ambiguity.

## 6. Pell comparison [D]

The selected element satisfies
\[
\chi_{12}(7)=-1.
\]
Therefore the established Pell/Galois law gives
\[
\boxed{
\sigma_7(\lambda^n)=\lambda^{-n},
\qquad \lambda=2+\sqrt3.
}
\]

Hence the same canonical label selected by the complex orientation has the two actions:
\[
\boxed{
r\mapsto7r
\quad\text{on the finite carrier},
}
\]
and
\[
\boxed{
n\mapsto-n
\quad\text{on the Pell orbit}.
}
\]

They remain different operations on different spaces, but the previous “either 5 or 7” ambiguity is removed once the project's already-established oriented complex structure is used.

## 7. C2^3 formulation [D]

In the v13.530 coordinates
\[
5=100,\qquad7=010,\qquad11=110.
\]
The intrinsic complex axis is the second coordinate:
\[
\chi_{-4}=\psi_{010}
\leftrightarrow R_Y.
\]

Thus the selected RMS translation is
\[
\boxed{
v\mapsto v+010.
}
\]

Because
\[
B(110,010)=1,
\]
this flips the \(\chi_{12}=\psi_{110}\) fiber.

The rejected alternative
\[
v\mapsto v+100
\]
also flips \(\chi_{12}\), but acts through the \(R_X/\chi_{-3}\) axis rather than the intrinsically justified complex-conjugation axis.

## 8. Verdict

\[
\boxed{\textbf{PASS, WITH EXPLICIT LIFT CONDITION.}}
\]

The pre-existing complex orientation and \(\chi_{-4}\leftrightarrow R_Y\) convention distinguish \(7\) from \(5\) **provided the RMS/Casimir scalar transfer is lifted as pure transverse-orientation reversal with \(X\) fixed**.

This is independent of the v13.697 numerical/order convention and therefore gives a second route to the same translator:
\[
\boxed{M_{\rm RMS}=\times7.}
\]

The remaining logical guardrail is that the scalar RMS identity itself does not manufacture the complex orientation; it becomes canonical only in the already-oriented cone/cyclotomic structure of the project.

## 9. Next target

The remaining independent orientation test is rapidity:
\[
s=\frac12\log(x/y).
\]
Determine whether the centered factor exchange \(x\leftrightarrow y\), i.e.
\[
s\mapsto-s,\qquad X\mapsto-X,
\]
selects the same \(7\) or instead selects the \(5/R_X\) axis. This is important: if rapidity selects \(5\) while complex transverse orientation selects \(7\), the two are complementary reflections whose product is the already-established \(11\) half-turn, rather than two independent proofs of one canonical translator.
