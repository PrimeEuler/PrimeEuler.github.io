# Cone Derivation Ledger v13.584 — Zeeman-Basis Ladder Ordering and Ordered-Edge Factor Dictionary

## Status

**Exact algebraic checkpoint.** This note audits the \(J_+\) versus \(J_-\) convention in the Zeeman basis and reconciles it with the Paper C / centered-half-lattice factor pair.

It builds on v13.583. No electromagnetic identification is promoted here.

## 1. Zeeman basis and ladder convention

Let

\[
J_z|j,q\rangle=q|j,q\rangle,\qquad q=-j,-j+1,\ldots,j,
\]

with \(\hbar=1\). With

\[
J_\pm=J_x\pm iJ_y,
\]

the commutators are

\[
[J_z,J_\pm]=\pm J_\pm.
\]

Hence

\[
\boxed{J_+:q\mapsto q+1},\qquad
\boxed{J_-:q\mapsto q-1}.
\]

Explicitly,

\[
J_+|j,q\rangle
=
\sqrt{(j-q)(j+q+1)}\,|j,q+1\rangle,
\]

\[
J_-|j,q\rangle
=
\sqrt{(j+q)(j-q+1)}\,|j,q-1\rangle.
\]

Define

\[
A_+^2=(j-q)(j+q+1),\qquad
A_-^2=(j+q)(j-q+1).
\]

## 2. Schwinger realization

Use

\[
J_+=a_1^\dagger a_2,\qquad
J_-=a_2^\dagger a_1,\qquad
J_z=\frac{n_1-n_2}{2},
\]

with

\[
n_1=j+q,\qquad n_2=j-q,\qquad n_1+n_2=2j.
\]

Then

\[
a_1^\dagger a_2|n_1,n_2\rangle
=
\sqrt{(n_1+1)n_2}\,
|n_1+1,n_2-1\rangle,
\]

so \(J_+\) indeed sends \(q\to q+1\).

Its squared norm is

\[
\|J_+|j,q\rangle\|^2
=
\langle j,q|J_-J_+|j,q\rangle.
\]

Using \(a_1a_1^\dagger=n_1+1\),

\[
\boxed{J_-J_+=(n_1+1)n_2}
\]

on the fixed-number basis, while

\[
\boxed{J_+J_-=n_1(n_2+1)}.
\]

Thus

\[
\boxed{
A_+^2=(n_1+1)n_2
}
\]

and

\[
\boxed{
A_-^2=n_1(n_2+1).
}
\]

The apparently reversed product order is required by the norm rule \(O^\dagger O\): the squared norm of the raising operator \(J_+\) is measured by \(J_-J_+\).

## 3. Raising-edge factor pair

For the raising edge \(q\to q+1\), define

\[
\boxed{x_+=n_1+1=j+q+1},\qquad
\boxed{y_+=n_2=j-q}.
\]

Then

\[
\boxed{x_+y_+=A_+^2}.
\]

The centered cone coordinates are

\[
X_+=\frac{x_+-y_+}{2}
=q+\frac12,
\]

\[
T=\frac{x_++y_+}{2}
=j+\frac12,
\]

and

\[
Y_+^2=x_+y_+=A_+^2.
\]

Therefore

\[
\boxed{
X_+^2+Y_+^2=T^2
}
\]

with

\[
\boxed{
(X_+,Y_+^2,T)
=
\left(q+\frac12,\,(j-q)(j+q+1),\,j+\frac12\right).
}
\]

This is the exact ordered-edge realization of the centered half-lattice identity from v13.583.

## 4. Lowering-edge factor pair

For \(J_-:q\to q-1\), define

\[
\boxed{x_-=n_1=j+q},\qquad
\boxed{y_-=n_2+1=j-q+1}.
\]

Then

\[
x_-y_-=A_-^2,
\]

\[
X_-=\frac{x_--y_-}{2}
=q-\frac12,
\]

and again

\[
T=\frac{x_-+y_-}{2}
=j+\frac12.
\]

Hence

\[
\boxed{
X_-^2+A_-^2=T^2.
}
\]

## 5. One unoriented edge, two ladder orientations

The raising description of the edge \(q\leftrightarrow q+1\) is

\[
(x_+,y_+)_q
=
(j+q+1,j-q).
\]

The lowering description from its upper endpoint is

\[
(x_-,y_-)_{q+1}
=
(j+q+1,j-q).
\]

Therefore

\[
\boxed{
(x_+,y_+)_q=(x_-,y_-)_{q+1}
}
\]

exactly, not merely at the level of the product. Likewise,

\[
\boxed{
X_+(q)=X_-(q+1)=q+\frac12
}
\]

and

\[
\boxed{
A_+^2(j,q)=A_-^2(j,q+1).
}
\]

Thus the factor/cone point is naturally an **unoriented ladder edge**, while \(J_+\) and \(J_-\) supply its two orientations.

## 6. Exact operator identities

Since

\[
J_-J_+
=
j(j+1)I-J_z(J_z+I),
\]

completion of the square gives

\[
\boxed{
\left(J_z+\frac12 I\right)^2+J_-J_+
=
\left(j+\frac12\right)^2 I.
}
\]

Similarly,

\[
\boxed{
\left(J_z-\frac12 I\right)^2+J_+J_-
=
\left(j+\frac12\right)^2 I.
}
\]

These are operator-level lifts of the centered raising/lowering cone identities.

## 7. Zeeman-energy guardrail

If an external magnetic field selects the \(z\)-axis and

\[
H_Z=-\gamma B J_z,
\]

then

\[
E_q=-\gamma B q.
\]

Therefore \(J_+\) always raises the magnetic quantum number \(q\), but it does **not** universally raise the energy. The energetic direction depends on the sign of \(\gamma B\).

Any later absorption/emission or polarization interpretation must preserve this distinction.

## 8. Promoted conclusion

The following chain is exact in the Schwinger / Paper C dictionary:

\[
\boxed{
J_+=a_1^\dagger a_2
\Longrightarrow
q\to q+1
\Longrightarrow
(x,y)=(n_1+1,n_2)
}
\]

and

\[
\boxed{
Y^2=xy=(n_1+1)n_2
=
\langle j,q|J_-J_+|j,q\rangle
=
|\langle j,q+1|J_+|j,q\rangle|^2.
}
\]

Furthermore,

\[
\boxed{
X=q+\frac12,\qquad T=j+\frac12.
}
\]

Hence the factor-pair \(+1\), the bosonic ordering identity \(aa^\dagger=n+1\), the \(SU(2)\) ladder matrix element, and the centered half-lattice shift are one coherent ordered-edge structure.

## 9. Guardrails / open bridge

1. This note does **not** identify the exploratory electromagnetic \((E,B)\) amplitudes with the external Zeeman field.
2. \(J_+\) means \(q\to q+1\), not necessarily an upward energy transition.
3. The cone point is an unoriented transition edge; \(J_\pm\) orient it.
4. The next electromagnetic question should distinguish the static field selecting \(J_z\) from a transverse driving field coupling through \(J_\pm\).
5. Any phase/polarization identification remains unpromoted until an explicit Hamiltonian-level bridge is checked.
