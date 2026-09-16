# Cone Derivation Ledger v13.506 — Signed Cone-Root Algebra is exactly U(24) = V4 x C2

## Scope

Construct the induced algebra on the eight signed root states
\[
R_\pm=\{\pm1,\pm5,\pm7,\pm11\}
\]
with cone coordinates
\[
X=(r-1)/2,\qquad T=(r+1)/2.
\]
The key point is that the signed representatives are not an ad hoc eight-state enlargement: modulo 24 they are exactly all units of `Z/24Z`.

---

## 1. Exact identification with U(24) [D]

Reducing the negative representatives modulo 24 gives
\[
-11\equiv13,\quad -7\equiv17,\quad -5\equiv19,\quad -1\equiv23\pmod{24}.
\]
Therefore
\[
\boxed{
R_\pm\pmod{24}=\{1,5,7,11,13,17,19,23\}=U(24).
}
\]

Use multiplication modulo 24, followed by the canonical signed representative in `R_pm`, as the induced product. This is closed and associative because it is simply the unit-group law transported to the signed representatives.

Every element of `U(24)` squares to 1:
\[
a^2\equiv1\pmod{24}\qquad(a\in U(24)).
\]
Hence the eight-state group is elementary abelian of order 8:
\[
\boxed{R_\pm\cong U(24)\cong C_2^3\cong V_4\times C_2.}
\]
It is **not dihedral**: it is abelian and has no element of order 4.

---

## 2. Direct-product coordinates [D]

Let
\[
A=\{1,5,7,11\}\cong V_4,
\]
and let the sign bit be
\[
C_2=\{+1,-1\}.
\]
Every signed state is uniquely
\[
r=\epsilon a,\qquad \epsilon\in\{\pm1\},\ a\in A.
\]
Since `-1` is central, multiplication is componentwise:
\[
\boxed{(a,\epsilon)(b,\delta)=(ab\bmod24,\epsilon\delta).}
\]
For `a,b in A`, their product modulo 24 remains in `A`, and the sign factor is independent. Thus the exact splitting is the same algebraic `U(24)=A x B` structure already audited in v13.228/v13.501, now recovered directly from the user's signed cone-root construction.

A convenient set of three independent involutive generators is
\[
5,\quad7,\quad-1,
\]
with
\[
5^2=7^2=(-1)^2=1,
\]
and all commuting. Also `11=5*7`.

---

## 3. Transported algebra in X coordinates [D]

Because
\[
r=2X+1,
\]
the signed roots correspond modulo 12 to the eight X-states
\[
\boxed{X\in\{0,2,3,5,6,8,9,11\}\pmod{12}.}
\]
Indeed the positive sheet is `{0,2,3,5}` and the negative sheet is
\[
X(-r)=-T(r)=-X(r)-1,
\]
which gives `{11,9,8,6}` modulo 12.

Transport multiplication through `r=2X+1`. If `X,Y` represent two states, then
\[
(2X+1)(2Y+1)=2(2XY+X+Y)+1,
\]
so the exact induced operation is
\[
\boxed{X\star Y=2XY+X+Y\pmod{12}.}
\]
On the eight-state subset above this is a group law isomorphic to `C2^3`.

The sign involution (multiplication by `-1`) is
\[
\boxed{J_X(X)=-X-1\pmod{12}.}
\]
It exchanges the two four-state sheets and commutes with the transported V4 translations because the underlying group is abelian.

---

## 4. Transported algebra in T coordinates [D]

Since
\[
r=2T-1,
\]
the eight T-states modulo 12 are
\[
\boxed{T\in\{0,1,3,4,6,7,9,10\}\pmod{12}.}
\]
The positive sheet is `{1,3,4,6}` and the negative sheet is `{0,-2,-3,-5}` = `{0,10,9,7}` modulo 12.

From
\[
(2T-1)(2U-1)=2(2TU-T-U+1)-1,
\]
the transported group law is
\[
\boxed{T\diamond U=2TU-T-U+1\pmod{12}.}
\]
The sign involution is
\[
\boxed{J_T(T)=1-T\pmod{12}.}
\]
Since `T=X+1`, the X and T algebras are conjugate by the translation `X -> X+1`:
\[
(X\star Y)+1=(X+1)\diamond(Y+1).
\]

---

## 5. Cone interpretation [D]

For every signed state,
\[
T-X=1,\qquad T+X=r.
\]
Thus multiplication acts most simply on the varying null coordinate:
\[
\boxed{(T+X)_{r\cdot s}\equiv (T+X)_r(T+X)_s\pmod{24}},
\]
while the other null coordinate remains fixed at 1 by this chosen `(r,1)` section.

The sign involution is exactly
\[
r\mapsto-r,
\]
which transports to
\[
\boxed{(X,T)\mapsto(-T,-X)}
\]
as an equality on the signed representatives (before modular reduction). This exchanges
\[
X_-=-T_+,\qquad T_-=-X_+.
\]

Important guardrail: this is an algebra on the **discrete signed cone-root section** induced from multiplication modulo 24. It is not a global multiplicative symmetry of the continuous AM-GM cone.

---

## 6. Relation to the earlier mod-24 audit [Interpretation]

This result clarifies, rather than reverses, v13.502/v13.503.

- The signed cone roots themselves really are `U(24)`, so the eight-state cone-root algebra has exact `V4 x C2` content.
- The Suzuki even residue stratum `{2,10,14,22} mod 24` is still disjoint from `U(24)`. Therefore this exact signed-root algebra must **not** be identified with that Suzuki stratum.
- The common Suzuki/cone carrier remains the stripped unit core `u mod 12 in V4`; the extra signed `C2` is an exact cone/unit-group sheet coordinate whose possible relation to Pell orientation or another independently defined sign observable must be tested separately.

This distinction is potentially useful: the signed construction gives a canonical eight-state extension of the four-state cone carrier, but it does not by itself supply an eighth-state Suzuki observable.

---

## 7. Verdict

\[
\boxed{
\{\pm1,\pm5,\pm7,\pm11\}
\text{ with multiplication mod }24
\cong U(24)\cong V_4\times C_2\cong C_2^3.
}
\]

It is not dihedral-like. The cone coordinate maps transport this exact group law to the nonlinear-looking but closed formulas
\[
\boxed{X\star Y=2XY+X+Y\pmod{12}},
\qquad
\boxed{T\diamond U=2TU-T-U+1\pmod{12}},
\]
with sheet/sign involutions
\[
\boxed{J_X(X)=-X-1},\qquad \boxed{J_T(T)=1-T}.
\]

### Next exact question

The natural next audit is whether the user's proposed QR/circle double-bijection is an isomorphism/intertwiner for this transported `C2^3` algebra (or at least its V4 positive-sheet quotient), rather than merely a set-level matching. That test can be done by transporting the multiplication table through each proposed labeling and checking commutation exactly.

## Guardrail

No Suzuki, spectral, critical-line, RH, or GRH consequence is claimed. This entry is exact finite algebra plus its cone-coordinate transport.