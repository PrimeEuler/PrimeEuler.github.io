# Cone Derivation Ledger v13.697 — RMS/Casimir Fiber Transfer versus Pell Orientation Reversal

Date: 2026-09-23

Status labels: **[S]** source-established, **[D]** exact derived, **[N]** obstruction, **[I]** interpretation.

## 1. Synchronization and target

Immediately before this write the live head was v13.696, commit \`a8d9eeaa8391f3d7b2198c24cf8cf8e64b7d74f3\`; no v13.697 collision was present.

Established inputs:

- v13.530: \(U(24)\cong C_2^3\), \(\chi_{12}=\psi_{110}\), and the selected carrier element \(11=110\) corresponds under the explicit cone intertwiner to \(R_XR_Y\).
- audited Pell/Galois identity:
  \[
  \sigma_r(\lambda^n)=\lambda^{\chi_{12}(r)n},
  \qquad \lambda=2+\sqrt3.
  \]
  Thus \(\chi_{12}(r)=-1\) reverses Pell time \(n\mapsto-n\), while \(+1\) preserves it.
- v13.692–696: the centered \(A=3,D=1/2\) cell gives
  \[
  \{5,7\}=\chi_{12}^{-1}(-1),\qquad
  \{11,1\}=\chi_{12}^{-1}(+1),
  \]
  through the pronic and RMS/Casimir quantities.

Question: is the RMS/Casimir transfer between these fibers itself the Pell orientation reversal, multiplication by a fixed carrier element, or does it require extra structure?

## 2. First obstruction: Pell orientation is a character action, not a fiber-changing carrier map [D/N]

The Pell law is
\[
\boxed{
\sigma_r(\lambda^n)=\lambda^{\chi_{12}(r)n}.
}
\]
For a fixed carrier label \(r\), the label is not changed. Rather, \(r\) determines whether the Pell exponent is preserved or reversed:
\[
\chi_{12}(r)=+1:\ n\mapsto n,
\]
\[
\chi_{12}(r)=-1:\ n\mapsto-n.
\]

Therefore Pell orientation reversal acts on the **Pell orbit coordinate** \(n\), graded by \(\chi_{12}\); it does not intrinsically map
\[
\chi_{12}^{-1}(-1)\to\chi_{12}^{-1}(+1).
\]

Hence the RMS/Casimir fiber transfer cannot literally be the same operation as the established Pell orientation reversal.

## 3. Fixed-group-element test [D]

In \(U(12)\),
\[
\chi_{12}^{-1}(-1)=\{5,7\},
\qquad
\chi_{12}^{-1}(+1)=\{1,11\}.
\]

Multiplication by any element \(g\) with
\[
\chi_{12}(g)=-1
\]
exchanges these two cosets, because
\[
\chi_{12}(gr)=\chi_{12}(g)\chi_{12}(r)=-\chi_{12}(r).
\]

Thus either \(g=5\) or \(g=7\) gives a legitimate fiber exchange.

The two possibilities are
\[
5:\quad 5\mapsto1,\quad7\mapsto11,
\]
and
\[
7:\quad 5\mapsto11,\quad7\mapsto1.
\]

Therefore the unordered fiber transfer
\[
\boxed{
\{5,7\}\longmapsto\{1,11\}
}
\]
is exactly multiplication by either negative-\(\chi_{12}\) carrier element.

But the centered RMS/Casimir construction by itself supplies only the unordered output pair
\[
\{35,37\}\equiv\{11,1\}\pmod{12}.
\]
It does not yet canonically specify whether
\[
5\mapsto1,\ 7\mapsto11
\]
or
\[
5\mapsto11,\ 7\mapsto1.
\]

Thus:

\[
\boxed{
\text{fiber-level RMS transfer}
=
\text{a } \chi_{12}=-1\text{ coset translation},
}
\]
but
\[
\boxed{
\text{pointwise RMS transfer requires one additional binary choice.}
}
\]

## 4. The additional binary choice is already a known character/reflection axis [D/I]

The two candidate translators differ by
\[
5^{-1}7=5\cdot7=11,
\]
since every unit is self-inverse.

Thus the ambiguity between the two pointwise lifts is exactly multiplication by
\[
\boxed{11}.
\]

But v13.530 identifies
\[
11\leftrightarrow\chi_{12}\leftrightarrow R_XR_Y
\]
under the established self-dual/cone intertwiner, where
\[
R_XR_Y:(z,T)\mapsto(-z,T)
\]
is the fixed-sheet half-turn.

Therefore the two possible pointwise RMS/Casimir fiber maps differ by the already-established \(11/\chi_{12}\) half-turn:
\[
\boxed{
M_7=(\times11)\circ M_5.
}
\]

This is an exact fixed-group-element relation.

[I] Geometrically, choosing which member of the centered input pair is matched to which member of the output pair requires an orientation/order on the centered cell. Reversing that choice composes the map with the half-turn \(11\).

## 5. Oriented centered-cell calculation [D]

Take the ordered input
\[
(5,7)
\]
corresponding to the lower/upper half-step
\[
T=3-\frac12,\quad3+\frac12.
\]

The centered quadratic quantities are
\[
4G^2=35,\qquad4Q^2=37.
\]
Their residues are ordered as
\[
35\equiv11,\qquad37\equiv1\pmod{12}.
\]

Thus if the natural order is inherited from
\[
G^2=A^2-D^2
\quad\text{then}\quad
Q^2=A^2+D^2,
\]
the ordered transfer is
\[
\boxed{
(5,7)\mapsto(11,1).
}
\]

This is exactly multiplication by \(7\):
\[
7\cdot5\equiv11,\qquad
7\cdot7\equiv1\pmod{12}.
\]

Hence, once the **minus-to-plus quadratic orientation**
\[
A^2-D^2\ \to\ A^2+D^2
\]
is retained, the central RMS/Casimir cell selects
\[
\boxed{M_{\rm RMS}=\times7}
\]
on the ordered \(U(12)\) fiber.

If the centered-cell orientation is reversed, the transfer becomes
\[
(7,5)\mapsto(11,1),
\]
equivalently \(\times5\). The two differ by \(\times11\), as above.

## 6. Comparison with Pell orientation reversal [D]

The selected oriented RMS translator \(7\) satisfies
\[
\chi_{12}(7)=-1.
\]
Therefore the *same carrier label* \(7\), when used in the established Pell/Galois action, gives
\[
\boxed{
\sigma_7(\lambda^n)=\lambda^{-n}.
}
\]

This yields a precise compatibility:

- as a carrier translation, \(7\) exchanges the two \(\chi_{12}\) fibers;
- as a Galois label, \(7\) reverses Pell time orientation.

These are not the same action space:
\[
\boxed{
r\mapsto7r
\quad\text{on }U(12),
}
\]
versus
\[
\boxed{
n\mapsto-n
\quad\text{on the Pell orbit}.
}
\]

But both are controlled by the same negative character value
\[
\chi_{12}(7)=-1.
\]

Thus the relation is not equality of operations; it is a common character-controlled action carried by the same selected group element after an oriented-cell choice.

## 7. Lift to U(24) [D]

In v13.530 coordinates,
\[
5=100,\qquad7=010,\qquad11=110.
\]

Translation by \(7\) is
\[
v\mapsto v+010.
\]
It exchanges the \(\chi_{12}\) hyperplanes because
\[
\chi_{12}=\psi_{110}
\]
and
\[
B(110,010)=1.
\]

Translation by \(5\),
\[
v\mapsto v+100,
\]
does the same, since
\[
B(110,100)=1.
\]

Their difference is
\[
010+100=110,
\]
the \(11\) half-turn direction.

Therefore the entire result lifts exactly to the audited \(C_2^3\) carrier. The arithmetic-sign/sheet coordinate \(c\) is untouched by either \(5\) or \(7\), so the RMS transfer operates within each signed \(U(24)\) sheet.

## 8. Verdict [D/I]

\[
\boxed{\textbf{NOT THE SAME OPERATION.}}
\]

The RMS/Casimir transformation acts on the finite carrier; Pell orientation reversal acts on the Pell exponent/orbit.

\[
\boxed{\textbf{SAME CONTROLLING CHARACTER.}}
\]

Both are governed by a \(\chi_{12}=-1\) carrier label.

\[
\boxed{\textbf{FIXED-ELEMENT RELATION AFTER ORIENTATION.}}
\]

With the natural ordered convention
\[
A^2-D^2\to A^2+D^2,
\]
the central cell selects
\[
\boxed{M_{\rm RMS}=\times7,}
\]
and \(7\) is simultaneously a Pell-orientation-reversing Galois label.

\[
\boxed{\textbf{ONE EXTRA STRUCTURE IS REQUIRED.}}
\]

Without an orientation/order on the centered cell, the geometry determines only the coset exchange
\[
\{5,7\}\leftrightarrow\{1,11\},
\]
not whether the translator is \(5\) or \(7\). The two choices differ by the fixed \(11/\chi_{12}\) half-turn.

## 9. Next target

Test whether the oriented choice of \(7\) is independently forced by an already-existing structure rather than imposed by ordering convention. Candidates:

1. Paper A's oriented complex coordinate \(z=X+iY\) / cone orientation;
2. the \(\chi_{-4}\leftrightarrow R_Y\) leg, which v13.530 already proved intrinsically under compatible cyclotomic orientation;
3. the rapidity orientation \(s=\frac12\log(x/y)\), where \(s\mapsto-s\) exchanges the centered factor pair.

If one of these selects \(7\) rather than \(5\) without circularity, then the RMS/Pell bridge can be strengthened from “same negative-\(\chi_{12}\) class” to a canonical common carrier element.
