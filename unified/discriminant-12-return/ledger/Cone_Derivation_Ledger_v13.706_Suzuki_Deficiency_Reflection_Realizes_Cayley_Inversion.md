# Cone Derivation Ledger v13.706 — Suzuki Deficiency Reflection Realizes Cayley Inversion

Date: 2026-09-23

Status: exact algebraic/reflection gate following v13.705. This identifies what Suzuki's canonical reflection \(R:u_+\leftrightarrow u_-\) does to the characteristic coefficients, the \(0/\pi\) extensions, the Weyl function, and the Cayley coordinate. The result supplies the missing inversion operation, but with a convention-sensitive distinction from coefficient conjugation.

## 0. Synchronization

Immediately before this write the live head was v13.705, commit \`1151d93d646b591c7dd2dba6dbcf4bf89defc21d\`; v13.704 External Audit Round 80 had already verified the cone torus/involution algebra through v13.703. No v13.706 collision was present.

Use the exact finite-\(a\) characteristic formulas from v13.685:
\[
W_\theta(z)=A(z)+e^{i\theta}B(z),
\]
where
\[
A(z)=(z-i)F_+(z),\qquad B(z)=(z+i)F_-(z),
\]
and
\[
W_0=A+B,\qquad W_\pi=A-B.
\]
Also
\[
\boxed{
m(z)=-i\,\frac{A+B}{A-B}
}
\]
and
\[
\boxed{\frac{W_0}{W_\pi}=i\,m.}
\]

The canonical continuous-kernel reflection satisfies
\[
u_-=Ru_+,\qquad R^2=1.
\]

## 1. Algebraic reflection on the deficiency channels

The reflection exchanges the two canonical deficiency channels. At the characteristic-coefficient level define
\[
\mathscr R:(A,B)\mapsto(B,A).
\]

This is the coefficient action induced by exchanging the \(+\) and \(-\) deficiency labels; it is the correct normalization-free object to analyze. It obeys
\[
\boxed{\mathscr R^2=1.}
\]

Then
\[
W_0=A+B
\mapsto
B+A=W_0,
\]
while
\[
W_\pi=A-B
\mapsto
B-A=-W_\pi.
\]

Hence
\[
\boxed{
\mathscr R:W_0\mapsto W_0,\qquad
W_\pi\mapsto-W_\pi.
}
\]

The minus sign is characteristic gauge for the zero set of \(W_\pi\), but it is essential in the Weyl quotient.

## 2. Exact action on the Weyl function

Using
\[
m=-i\frac{A+B}{A-B},
\]
after exchange:
\[
m^{\mathscr R}
=
-i\frac{B+A}{B-A}
=
+i\frac{A+B}{A-B}
=
\boxed{-m}.
\]

Thus the canonical deficiency-channel exchange acts on the project Weyl coordinate by
\[
\boxed{
\mathscr R:m\mapsto-m.
}
\]

Equivalently,
\[
\frac{W_0}{W_\pi}=im
\mapsto
-\frac{W_0}{W_\pi}
=i(-m).
\]

This is exact and independent of common characteristic normalization.

## 3. Exact action on the Cayley variable

Use the abstract Cayley coordinate
\[
s=\frac{m-i}{m+i}.
\]
Under \(m\mapsto-m\),
\[
s^{\mathscr R}
=
\frac{-m-i}{-m+i}
=
\frac{m+i}{m-i}
=
\boxed{s^{-1}}.
\]

Therefore
\[
\boxed{
\mathscr R:s\mapsto s^{-1}.
}
\]

For a local logarithm
\[
L_s=\log s,
\]
\[
\boxed{
\mathscr R:L_s\mapsto-L_s
}
\]
modulo \(2\pi i\).

This is precisely the abstract inversion law of the cone factor-exchange involution on the boost torus:
\[
F:w\mapsto w^{-1},
\qquad
F:\ell\mapsto-\ell.
\]

Therefore the missing inversion correspondence is now exact at the primitive Cayley-coordinate level:
\[
\boxed{
s\leftrightarrow w,\qquad
\log s\leftrightarrow\ell,
\qquad
\mathscr R\leftrightarrow F
}
\]
as group-action coordinates, subject to the normalization guardrail in Section 8.

## 4. Extension phase under channel exchange

Start from
\[
W_\theta=A+e^{i\theta}B.
\]
After channel exchange,
\[
\mathscr R W_\theta
=
B+e^{i\theta}A
=
e^{i\theta}
\left(A+e^{-i\theta}B\right).
\]

Thus
\[
\boxed{
\mathscr R W_\theta
=
e^{i\theta}W_{-\theta}.
}
\]

The prefactor \(e^{i\theta}\) is independent of \(z\), so it is a harmless characteristic gauge for zeros. Therefore at the extension-family level:
\[
\boxed{
\mathscr R:\theta\mapsto-\theta
}
\]
modulo \(2\pi\).

In particular,
\[
0\mapsto0,\qquad
\pi\mapsto-\pi\equiv\pi,
\]
consistent with \(W_0\mapsto W_0\) and \(W_\pi\mapsto-W_\pi\).

Hence the boundary phase is **odd under deficiency reflection**.

## 5. Character consequences

v13.705 proved that coefficient conjugation makes the scalar extension phase \(C\)-odd:
\[
C:\theta\mapsto-\theta.
\]
The present deficiency reflection also gives
\[
\mathscr R:\theta\mapsto-\theta.
\]

If we identify
\[
\mathscr R\leftrightarrow F
\]
at the Cayley-coordinate level, then \(\theta\) has parity
\[
\boxed{(F,C)=(-,-).}
\]

This matches the cone direction
\[
\boxed{\Im\ell=\phi.}
\]

Thus the strongest current phase assignment is
\[
\boxed{
\theta\leftrightarrow\Im\ell
}
\]
at the character/parity level.

This is stronger than v13.705, where \(\theta\) could not yet be distinguished between \(\Im\tau\) and \(\Im\ell\).

## 6. Four real directions for the Cayley logarithm

Write
\[
L_s=u+iv.
\]

Under deficiency reflection:
\[
\mathscr R:L_s\mapsto-L_s,
\]
so
\[
u\mapsto-u,\qquad v\mapsto-v.
\]

Under spectral conjugation, v13.705 proved
\[
L_s(\bar\zeta)=-\overline{L_s(\zeta)},
\]
so
\[
u\mapsto-u,\qquad v\mapsto v.
\]

These are not the cone \(F,C\) actions separately. Rather:
- deficiency reflection has the cone-\(F\) law on \(\ell\);
- spectral conjugation has the cone-\(FC\) law on \(\ell\).

Their product therefore has the cone-\(C\) law:
\[
\mathscr R\circ(\zeta\mapsto\bar\zeta):
L_s
\mapsto
\overline{L_s}.
\]

Indeed,
\[
-\overline{L_s}\xrightarrow{\mathscr R}
\overline{L_s}.
\]

Thus define the induced Suzuki coefficient-conjugation action on the primitive Cayley coordinate by
\[
\boxed{
\mathscr C_s
:=
\mathscr R\circ\kappa,
\qquad
\kappa:\zeta\mapsto\bar\zeta.
}
\]
Then
\[
\boxed{
\mathscr C_s:L_s\mapsto\overline{L_s}.
}
\]

This reproduces the cone action
\[
C:\ell\mapsto\bar\ell.
\]

Therefore the Cayley log now realizes the full two-involution pattern:
\[
\boxed{
\mathscr R:L_s\mapsto-L_s,
\qquad
\mathscr C_s:L_s\mapsto\bar L_s.
}
\]

Consequently:
\[
\boxed{
\Re L_s:\ (-,+),
\qquad
\Im L_s:\ (-,-).
}
\]

These are exactly the cone characters
\[
\boxed{
\Re\ell:\ (-,+),
\qquad
\Im\ell:\ (-,-).
}
\]

So the boost pair is now completely matched at the character level:
\[
\boxed{
\Re\log s\leftrightarrow\Re\ell,
\qquad
\Im\log s\leftrightarrow\Im\ell.
}
\]

## 7. What happens to the cross-ratio

For
\[
\Delta(z;z_*)=\frac{m(z)}{m(z_*)},
\]
deficiency reflection sends both numerator and denominator to their negatives:
\[
\Delta\mapsto
\frac{-m(z)}{-m(z_*)}
=
\boxed{\Delta}.
\]

Therefore
\[
\boxed{
\mathscr R:\log\Delta\mapsto\log\Delta
}
\]
locally modulo \(2\pi i\).

This is important: the normalized \(0/\pi\) cross-ratio **forgets the deficiency-reflection sign**.

Thus it cannot carry the boost \(F\)-odd direction by itself.

This explains why v13.705 could obtain only a conjugation modulus/phase split from \(\Delta\): normalization has quotiented out precisely the \(m\mapsto-m\) datum.

## 8. Normalization guardrail

v13.647 explicitly left open the concrete identity
\[
s_A^{Suz}(z)=
\frac{m_A(\zeta)-i}{m_A(\zeta)+i}
\]
for a fully fixed ordinary boundary triple, including spectral-variable and convention factors.

The present derivation uses the project convention already stabilized in v13.684–685:
\[
\frac{W_0}{W_\pi}=im,
\]
which is enough to prove
\[
m\mapsto-m
\]
under coefficient exchange and hence the Cayley inversion law for that project Weyl coordinate.

Therefore:
\[
\boxed{
\text{the action/equivariance result is proved in the stabilized project convention;}
}
\]
but a claim of literal equality between the printed Suzuki Schur candidate and a separately normalized abstract boundary-triple Cayley function still awaits the v13.647 normalization gate.

Do not erase this distinction.

## 9. Semidirect-product consequence

At the primitive Cayley-coordinate level, the Suzuki reflection realizes
\[
s\mapsto s^{-1}.
\]

Hence the subgroup generated by nonzero Cayley scaling and deficiency reflection has the same abstract form as the cone boost normalizer:
\[
\boxed{
\mathbb C^\times_s\rtimes C_2^{\mathscr R},
\qquad
\mathscr R(s)=s^{-1}.
}
\]

Adding the induced conjugation action
\[
\mathscr C_s(s)=\bar s
\]
gives
\[
\boxed{
\mathbb C^\times_s
\rtimes
(C_2^{\mathscr R}\times C_2^{\mathscr C_s}),
}
\]
with commuting involutions
\[
\mathscr R:s\mapsto s^{-1},
\qquad
\mathscr C_s:s\mapsto\bar s.
\]

This is exactly the one-factor boost analogue of the cone semidirect product from v13.703.

It does **not** yet supply the independent scale factor \(\mathbb C^\times_{\rm scale}\).

## 10. Result

\[
\boxed{
\mathscr R:(A,B)\mapsto(B,A)
}
\]

\[
\boxed{
W_0\mapsto W_0,\qquad
W_\pi\mapsto-W_\pi
}
\]

\[
\boxed{
m\mapsto-m
}
\]

\[
\boxed{
s\mapsto s^{-1},
\qquad
\log s\mapsto-\log s
}
\]

\[
\boxed{
\theta\mapsto-\theta
\quad\text{up to a }z\text{-independent characteristic gauge}
}
\]

\[
\boxed{
\Re\log s\leftrightarrow\Re\ell\;(-,+),
\qquad
\Im\log s\leftrightarrow\Im\ell\;(-,-)
}
\]
at the exact character/equivariance level in the stabilized project convention.

\[
\boxed{
\theta\leftrightarrow\Im\ell
}
\]
is now supported at the same character-parity level.

Finally,
\[
\boxed{
\Delta_{0/\pi}=m(z)/m(z_*)
\text{ is }\mathscr R\text{-even},
}
\]
so the normalized cross-ratio cannot by itself retain the missing \(F\)-odd sign.

## 11. Next gate

The boost half of the four-character correspondence is now populated. The remaining unfilled cone directions are
\[
\Re\tau\quad(+,+),
\qquad
\Im\tau\quad(+,-).
\]

The natural candidates are the common characteristic gauge / bulk relative determinant, because they are unchanged by deficiency-channel exchange. The next gate should separate:

1. the common entire/gauge factor multiplying \(W_0,W_\pi\);
2. the same-domain bulk determinant \(\Delta^{bulk}\);

and test whether either carries an \(F\)-even complex logarithm with
\[
\Re:(+,+),\qquad
\Im:(+,-),
\]
which would complete the full four-character correspondence without conflating boundary and bulk data.
