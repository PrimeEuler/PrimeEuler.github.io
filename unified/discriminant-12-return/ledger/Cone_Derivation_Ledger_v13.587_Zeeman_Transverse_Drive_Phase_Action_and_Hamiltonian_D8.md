# Cone Derivation Ledger v13.587 — Zeeman Transverse-Drive Phase Action and Hamiltonian D8

**Renumbering note:** originally filed as v13.586, which collided with the already-pushed `Cone_Derivation_Ledger_v13.586_External_Audit_Round_57.md`. Renumbered to v13.587 during External Audit Round 58. Mathematical content is unchanged.

## Status

**Exact algebraic / representation checkpoint.** This note extends the externally audited v13.585 ordered-edge dictionary to the transverse Zeeman interaction. It promotes only the Hamiltonian-level phase action and its discrete \(D_8\) subgroup. It does **not** identify arithmetic translations with electromagnetic operators.

## 1. Transverse Zeeman interaction

With the static field selecting the \(z\)-axis, take

\[
H_\perp=-\gamma(B_xJ_x+B_yJ_y).
\]

Define

\[
J_\pm=J_x\pm iJ_y,\qquad B_\pm=B_x\pm iB_y.
\]

Since

\[
J_x=\frac{J_++J_-}{2},\qquad
J_y=\frac{J_+-J_-}{2i},
\]

one obtains exactly

\[
\boxed{
B_xJ_x+B_yJ_y
=
\frac12(B_-J_+ + B_+J_-)
}
\]

and hence

\[
\boxed{
H_\perp
=
-\frac{\gamma}{2}(B_-J_+ + B_+J_-).
}
\]

Thus the algebraic pairing is

\[
\boxed{B_-\leftrightarrow J_+,\qquad B_+\leftrightarrow J_-}.
\]

With the v13.585 convention, \(J_+\) sends \(q\to q+1\), while \(J_-\) sends \(q\to q-1\).

## 2. Edge matrix elements

For the raising edge \(q\to q+1\),

\[
Y_q=\sqrt{(j-q)(j+q+1)}
\]

and

\[
\boxed{
\langle j,q+1|H_\perp|j,q\rangle
=
-\frac{\gamma}{2}B_-Y_q.
}
\]

For the reverse orientation,

\[
\boxed{
\langle j,q|H_\perp|j,q+1\rangle
=
-\frac{\gamma}{2}B_+Y_q.
}
\]

For a real physical transverse field,

\[
B_+=B_-^*,
\]

so the two oriented couplings are Hermitian conjugates.

Define

\[
\mathcal C_q=B_-Y_q,\qquad
\mathcal C_q^*=B_+Y_q.
\]

The intrinsic \(SU(2)\) representation fixes the radial edge magnitude \(Y_q\); the transverse drive supplies its complex amplitude and phase.

## 3. Phase-circle lift of a nonzero edge

Write

\[
B_-=B_\perp e^{-i\phi}.
\]

Define transverse phase-circle coordinates

\[
A_x=Y_q\cos\phi,\qquad
A_y=Y_q\sin\phi,
\]

so

\[
A_x-iA_y=Y_qe^{-i\phi}.
\]

Then

\[
A_x^2+A_y^2=Y_q^2.
\]

Using the audited centered-edge identity

\[
X_q=q+\frac12,\qquad
T=j+\frac12,\qquad
X_q^2+Y_q^2=T^2,
\]

the phase lift satisfies

\[
\boxed{
X_q^2+A_x^2+A_y^2=T^2.
}
\]

At a null/zero-amplitude endpoint \(Y_q=0\), the phase circle collapses.

## 4. Active transverse rotations: convention-fixed statement

For the real transverse coordinate plane, use the active vector rotation

\[
\binom{A_x'}{A_y'}
=
\begin{pmatrix}
\cos\alpha&-\sin\alpha\\
\sin\alpha&\cos\alpha
\end{pmatrix}
\binom{A_x}{A_y}.
\]

Equivalently,

\[
A_x-iA_y\mapsto e^{-i\alpha}(A_x-iA_y),
\]

so

\[
\boxed{\phi\mapsto\phi+\alpha}.
\]

The field component transforms identically as a transverse complex coordinate,

\[
\boxed{B_-\mapsto e^{-i\alpha}B_-},\qquad
\boxed{B_+\mapsto e^{+i\alpha}B_+}.
\]

For simultaneous rotation of field and matter transverse vectors, the paired edge operators carry the opposite weights,

\[
J_+\mapsto e^{+i\alpha}J_+,\qquad
J_-\mapsto e^{-i\alpha}J_-,
\]

so each scalar product is invariant:

\[
\boxed{
B_-J_+\mapsto B_-J_+,\qquad
B_+J_-\mapsto B_+J_-.
}
\]

Therefore

\[
\boxed{H_\perp\mapsto H_\perp}.
\]

**Convention guardrail.** Conjugation formulas for operators can display the opposite sign if one switches between active vector rotation and passive/component transformation. The promoted content is the convention-consistent real-plane action above and the invariant scalar pairing.

## 5. Transverse orientation reversal

Take the reflection

\[
H:
(A_x,A_y)\mapsto(A_x,-A_y).
\]

Its matrix is

\[
\boxed{
H=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
}
\]

On the complex transverse coordinate,

\[
A_x-iA_y\mapsto A_x+iA_y,
\]

hence

\[
\boxed{\phi\mapsto-\phi}.
\]

For a real physical field this exchanges

\[
\boxed{B_-\leftrightarrow B_+}.
\]

The corresponding transverse matter reflection exchanges

\[
\boxed{J_+\leftrightarrow J_-}.
\]

Consequently

\[
B_-J_+ + B_+J_-
\mapsto
B_+J_- + B_-J_+,
\]

and therefore

\[
\boxed{H_\perp\mapsto H_\perp}.
\]

The oriented edge couplings are exchanged:

\[
\boxed{
\mathcal C_q\leftrightarrow\mathcal C_q^*.
}
\]

**Guardrail.** Complex conjugation of the scalar transverse coordinate realizes \(\phi\mapsto-\phi\), but this must not be conflated with entrywise complex conjugation of every quantum-operator matrix. The physical reflection is the transverse orientation reversal.

## 6. Quarter-turn and \(D_8\)

The quarter-turn is

\[
Q:
\phi\mapsto\phi+\frac{\pi}{2},
\]

with

\[
\boxed{
Q=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
}
\]

The reflection is

\[
H:
\phi\mapsto-\phi.
\]

They satisfy

\[
\boxed{
Q^4=I,\qquad H^2=I,\qquad HQH=Q^{-1}.
}
\]

Hence

\[
\boxed{
\langle Q,H\rangle\cong D_8
}
\]

(order \(8\), using the project's \(D_8\) convention).

This \(D_8\) is a discrete subgroup of the natural transverse \(O(2)\) action.

## 7. Exact comparison with the existing intrinsic / phase representation

The previously established intrinsic fixed-shell generators are

\[
R=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\qquad
S=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

Therefore, after the stated phase-origin and orientation convention,

\[
\boxed{Q=R,\qquad H=S}.
\]

The intertwiner between the Hamiltonian transverse-drive \(D_8\) and the existing intrinsic phase \(D_8\) is therefore

\[
\boxed{I_2}.
\]

In particular,

\[
\boxed{
Q^2=R^2=-I_2=FS.
}
\]

Using the previously certified marked correspondence,

\[
\boxed{
T_7\leftrightarrow FS,
}
\]

the safe marked chain is

\[
\boxed{
T_7
\leftrightarrow
FS
=
R^2
=
Q^2.
}
\]

This is a correspondence between marked representations, **not** an equality between the arithmetic translation \(T_7\) and an electromagnetic operator.

## 8. Promoted conclusion

The centered \(SU(2)\) transition edge carries a natural transverse phase action in the Zeeman interaction:

\[
\boxed{
Y_q
\times
B_\perp e^{-i\phi}
=
\text{complex driven-edge coupling}.
}
\]

The full continuous phase symmetry is the transverse \(O(2)\) action: rotations shift \(\phi\), while transverse orientation reversal sends \(\phi\to-\phi\).

Its quarter-turn/reflection subgroup is exactly

\[
\boxed{D_8},
\]

and in the established phase coordinates it is literally the same real two-dimensional representation as the intrinsic fixed-shell \(D_8\):

\[
\boxed{Q=R,\qquad H=S}.
\]

## 9. Open audit targets

1. Distinguish this ordinary transverse reflection from antiunitary quantum time reversal.
2. Audit the transformation of \(B_0\), \(J_z\), and \(H_Z=-\gamma B_0J_z\) under physical time reversal.
3. Determine whether time reversal normalizes, duplicates, or enlarges the transverse \(O(2)\)/\(D_8\) structure.
4. Keep polarization labels (\(\sigma^\pm\), right/left circular) convention-dependent until Fourier sign, propagation direction, and \(\gamma\) sign are fixed.
