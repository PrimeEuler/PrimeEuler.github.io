# Cone Derivation Ledger v13.699 — The Two Primitive Reflections Compose to the χ12 Half-Turn

Date: 2026-09-23

Status labels: **[S]** source-established, **[D]** exact derived, **[I]** interpretation.

## 1. Synchronization and target

Immediately before this write the live head was v13.698, commit \`3a5dc5335c519a80f73f43e05acc453e4daea265\`; no v13.699 collision was present.

Target: explicitly verify that the complex-conjugation reflection selected by \(7\) and the rapidity/factor-exchange reflection selected by \(5\) compose to \(11\), and compare the result with the established \(\chi_{12}\leftrightarrow R_XR_Y\) half-turn.

## 2. Rapidity reflection is the X-reflection [D]

Use null/factor coordinates
\[
x=T+X,\qquad y=T-X.
\]
The rapidity is
\[
s=\frac12\log\frac{x}{y}.
\]
Exchanging the factors,
\[
x\leftrightarrow y,
\]
gives
\[
s\mapsto-s.
\]
At the same time
\[
T=\frac{x+y}{2}\mapsto T,
\qquad
X=\frac{x-y}{2}\mapsto-X,
\]
while
\[
Y=\sqrt{xy}\mapsto Y.
\]

Therefore rapidity reversal is exactly
\[
\boxed{
R_X:(X,Y,T)\mapsto(-X,Y,T).
}
\]

In complex notation \(z=X+iY\),
\[
\boxed{
R_X:z\mapsto-\bar z.
}
\]

Under the established v13.530 intertwiner,
\[
\boxed{
5\leftrightarrow\chi_{-3}\leftrightarrow R_X.
}
\]

Thus the rapidity reflection is the carrier translation/generator \(5\).

## 3. Complex-conjugation reflection is the Y-reflection [S/D]

The compatible oriented complex structure gives
\[
z=X+iY.
\]
Complex conjugation is
\[
z\mapsto\bar z=X-iY,
\]
hence
\[
\boxed{
R_Y:(X,Y,T)\mapsto(X,-Y,T).
}
\]

The audited cyclotomic identity
\[
\sigma_r(i)=\chi_{-4}(r)i
\]
selects
\[
\boxed{
7\leftrightarrow\chi_{-4}\leftrightarrow R_Y.
}
\]

Thus the complex-conjugation reflection is the carrier generator \(7\).

## 4. Explicit composition on the cone [D]

Apply first \(R_X\), then \(R_Y\):
\[
(X,Y,T)
\xrightarrow{R_X}
(-X,Y,T)
\xrightarrow{R_Y}
(-X,-Y,T).
\]

Reversing the order gives
\[
(X,Y,T)
\xrightarrow{R_Y}
(X,-Y,T)
\xrightarrow{R_X}
(-X,-Y,T).
\]

Therefore the two reflections commute and
\[
\boxed{
R_XR_Y=R_YR_X:(X,Y,T)\mapsto(-X,-Y,T).
}
\]

In complex notation,
\[
z\xrightarrow{R_X}-\bar z
\xrightarrow{R_Y}-z,
\]
or
\[
z\xrightarrow{R_Y}\bar z
\xrightarrow{R_X}-z.
\]
Hence
\[
\boxed{
R_XR_Y:z\mapsto-z.
}
\]

This is the \(180^\circ\) rotation / half-turn of every fixed-\(T\) cone circle.

## 5. Explicit composition on the arithmetic carrier [D]

Modulo \(12\),
\[
\boxed{
5\cdot7=35\equiv11\pmod{12}.
}
\]
Modulo \(24\), the same equality holds:
\[
\boxed{
5\cdot7=35\equiv11\pmod{24}.
}
\]

Therefore
\[
\boxed{
(\times7)\circ(\times5)
=
(\times5)\circ(\times7)
=
\times11.
}
\]

On \(U(12)\), explicitly:
\[
1\to5\to11,\qquad
5\to1\to7,\qquad
7\to11\to5,\qquad
11\to7\to1,
\]
which is exactly multiplication by \(11\):
\[
1\leftrightarrow11,\qquad5\leftrightarrow7.
\]

## 6. Character product [D]

The established quadratic-character relation is
\[
\boxed{
\chi_{-3}\chi_{-4}=\chi_{12}.
}
\]

Thus the same composition is visible simultaneously in three representations:
\[
\boxed{
5\cdot7=11,
}
\]
\[
\boxed{
\chi_{-3}\chi_{-4}=\chi_{12},
}
\]
\[
\boxed{
R_XR_Y:z\mapsto-z.
}
\]

Equivalently,
\[
\boxed{
\begin{array}{ccccc}
5&\longleftrightarrow&\chi_{-3}&\longleftrightarrow&R_X\\
\times&&\times&&\circ\\
7&\longleftrightarrow&\chi_{-4}&\longleftrightarrow&R_Y\\ \hline
11&\longleftrightarrow&\chi_{12}&\longleftrightarrow&R_XR_Y.
\end{array}}
\]

## 7. C2^3 binary verification [D]

In v13.530 coordinates,
\[
5=100,\qquad7=010.
\]
Multiplication is binary addition, so
\[
\boxed{
100+010=110=11.
}
\]

On the dual side,
\[
\psi_{100}\psi_{010}=\psi_{110},
\]
i.e.
\[
\boxed{
\chi_{-3}\chi_{-4}=\chi_{12}.
}
\]

On the cone side,
\[
f_1+f_2=R_XR_Y.
\]

Therefore the composition is exactly the same \(110\) direction in carrier, dual-character, and cone-symmetry coordinates.

## 8. Pell interpretation [D/I]

The established Pell law is
\[
\sigma_r(\lambda^n)=\lambda^{\chi_{12}(r)n}.
\]

The composite carrier element is \(11\), and
\[
\chi_{12}(11)=+1.
\]
Therefore the element \(11\) itself preserves Pell time orientation:
\[
\boxed{
\sigma_{11}(\lambda^n)=\lambda^n.
}
\]

This is important: the product of the two primitive negative-\(\chi_{12}\) reflections is the \(\chi_{12}\)-labelled half-turn, but as a Galois carrier element \(11\) lies in the \(+1\) fiber of the character \(\chi_{12}\).

There is no contradiction. “\(\chi_{12}\) axis/character” and “the value \(\chi_{12}(11)\)” are different notions. The character itself is the dual vector \(110\); evaluated on the carrier vector \(110\), the binary pairing is
\[
110\cdot110=1+1=0\pmod2,
\]
hence value \(+1\).

[I] Thus two orientation-reversing primitive carrier labels compose to a fixed-sheet geometric half-turn that preserves Pell time orientation.

## 9. Result

\[
\boxed{\textbf{PASS: rapidity reversal }=\times5=R_X.}
\]

\[
\boxed{\textbf{PASS: complex-conjugation reversal }=\times7=R_Y.}
\]

\[
\boxed{\textbf{PASS: }(\times7)(\times5)=\times11\ \Longleftrightarrow\ R_XR_Y:z\mapsto-z.}
\]

\[
\boxed{\textbf{PASS: the corresponding character product is }\chi_{-3}\chi_{-4}=\chi_{12}.}
\]

This closes the reflection triangle exactly:
\[
\boxed{
(5,\chi_{-3},R_X)\,
(7,\chi_{-4},R_Y)
=
(11,\chi_{12},R_XR_Y).
}
\]

The two primitive orientation reversals are therefore complementary, not competing choices. Their product is precisely the already-established D12 \(\chi_{12}\) fixed-sheet half-turn.
