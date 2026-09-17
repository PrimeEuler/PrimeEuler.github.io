# Cone Derivation Ledger v13.530 — U(24), Character Dual, and Cone C2^3 Intertwiner

**Renumbering note:** originally filed as v13.528, then briefly v13.529 — both collided with concurrently-created entries (`Cone_Derivation_Ledger_v13.528_External_Audit_Round_43.md` and `Cone_Derivation_Ledger_v13.529_Ambiguity_Stabilizer_after_Chi4_and_Chi12.md` respectively). Renumbered to v13.530 during External Audit Round 44. Mathematical content is unchanged.

## Status

**Exact finite group algebra and exact cone symmetry, with one explicit basis-compatible intertwiner.**

The abstract isomorphisms proved here are exact. The assignment of all three arithmetic generators to the three displayed cone involutions is an explicit compatible choice, not yet a basis-free canonical identification. One leg has additional intrinsic justification: after choosing the cone's oriented complex coordinate compatibly with the standard cyclotomic embedding, the character `chi_-4` is exactly complex-conjugation parity and therefore exactly the `Y`-reflection parity.

This checkpoint does **not** identify the QR deck involution with arithmetic sign; those remain distinct.

---

## 1. The signed arithmetic carrier

Let

\[
G_{24}=U(24)=\{\pm1,\pm5,\pm7,\pm11\}.
\]

Use binary coordinates

\[
r(a,b,c)=5^a7^b(-1)^c\pmod{24},
\qquad (a,b,c)\in\mathbf F_2^3.
\]

Since

\[
5^2\equiv7^2\equiv(-1)^2\equiv1\pmod{24},
\]

and the three generators commute, multiplication is binary addition:

\[
r(v)r(w)=r(v+w).
\]

Hence

\[
\boxed{U(24)\cong\mathbf F_2^3\cong C_2^3.}
\]

The eight elements are

\[
\begin{array}{c|c}
(a,b,c)&r(a,b,c)\\ \hline
000&1\\
100&5\\
010&7\\
110&11\\
001&-1\equiv23\\
101&-5\equiv19\\
011&-7\equiv17\\
111&-11\equiv13
\end{array}
\]

---

## 2. Explicit self-duality and the character group

For

\[
v=(a,b,c),\qquad w=(p,q,s),
\]

define the standard binary pairing

\[
B(v,w)=ap+bq+cs\pmod2
\]

and

\[
\psi_v(w)=(-1)^{B(v,w)}.
\]

Then

\[
\mathscr D:\mathbf F_2^3\longrightarrow\widehat{\mathbf F_2^3},
\qquad v\longmapsto\psi_v
\]

is an isomorphism. Transporting through `r(a,b,c)` gives

\[
\boxed{\mathscr D:U(24)\overset\sim\longrightarrow\widehat{U(24)}.}
\]

With the established coordinate conventions,

\[
\chi_{-3}=\psi_{100},\qquad
\chi_{-4}=\psi_{010},\qquad
\sigma=\psi_{001},
\]

where

\[
\sigma(r(a,b,c))=(-1)^c.
\]

Therefore

\[
\chi_{12}=\chi_{-3}\chi_{-4}=\psi_{110}.
\]

The full dual table is

\[
\begin{array}{c|c}
000&1\\
100&\chi_{-3}\\
010&\chi_{-4}\\
110&\chi_{12}\\
001&\sigma\\
101&\sigma\chi_{-3}\\
011&\sigma\chi_{-4}\\
111&\sigma\chi_{12}
\end{array}
\]

This self-duality is exact relative to the displayed binary basis. It is not asserted to be basis-free canonical.

---

## 3. Complex form of the cone

Write

\[
z=X+iY.
\]

Then the real cone equation

\[
X^2+Y^2=T^2
\]

is equivalently

\[
\boxed{z\bar z=T^2.}
\]

Paper A already uses the conjugate pair

\[
z_\pm=X\pm i\sqrt{xy},
\qquad z_- = \overline{z_+},
\qquad z\bar z=T^2.
\]

Thus the complex coordinate is a repackaging of the existing cone geometry.

Define the three commuting involutions

\[
R_X(X,Y,T)=(-X,Y,T),
\]

\[
R_Y(X,Y,T)=(X,-Y,T),
\]

\[
S_T(X,Y,T)=(X,Y,-T).
\]

In complex notation,

\[
R_X:(z,T)\mapsto(-\bar z,T),
\]

\[
R_Y:(z,T)\mapsto(\bar z,T),
\]

\[
R_XR_Y:(z,T)\mapsto(-z,T),
\]

and

\[
S_T:(z,T)\mapsto(z,-T).
\]

All preserve `z bar(z)=T^2`, commute, and square to the identity. Therefore

\[
\boxed{
G_{\rm cone}=\langle R_X,R_Y,S_T\rangle
\cong C_2^3.
}
\]

The subgroup

\[
\langle R_X,R_Y\rangle
=\{1,R_X,R_Y,R_XR_Y\}
\]

is the native geometric Klein four acting within each fixed sheet.

---

## 4. Exact assumptions for the chi_-4 / Y-reflection leg

The cone transverse plane has its distinguished real axis `X=(x-y)/2`. Equip the `(X,Y)` plane with its Euclidean metric and an orientation. The positive quarter-turn then defines

\[
J(X,Y)=(-Y,X),\qquad J^2=-I,
\]

and hence the oriented complex coordinate

\[
z=X+i_{\rm cone}Y.
\]

On the cyclotomic side choose the compatible standard embedding

\[
\zeta_{12}=e^{2\pi i/12}.
\]

Then

\[
\boxed{i_{\rm cone}=i=\zeta_{12}^3.}
\]

For `r in U(12)`,

\[
\sigma_r(i)=\sigma_r(\zeta_{12}^3)=\zeta_{12}^{3r}
=\chi_{-4}(r)i.
\]

If this Galois action is transported through the complex scalar while the real coordinates `X,Y,T` are held fixed, then

\[
X+iY\mapsto X+\chi_{-4}(r)iY.
\]

Thus

\[
\chi_{-4}(r)=+1\Rightarrow z\mapsto z,
\]

\[
\chi_{-4}(r)=-1\Rightarrow z\mapsto\bar z,
\]

so

\[
\boxed{\chi_{-4}\ \text{is exactly }R_Y\text{-parity under the compatible complex identification}.}
\]

Required assumptions:

1. `X` is retained as the distinguished real axis of the cone circle.
2. The transverse Euclidean plane is oriented.
3. `z=X+iY` is the resulting complex coordinate.
4. The cyclotomic embedding is chosen compatibly so `i=ζ_12^3`.
5. The Galois action is transported through this scalar identification while `X,Y,T` are fixed as real coordinates.

Reversing both compatible orientations sends `i` to `-i` on both sides and does not change the conjugation/reflection character. Thus the parity statement is orientation-independent once the cone complex line is identified with the quadratic subfield `Q(i)` and `X` is fixed as the real axis.

No claim is made that Paper A's real factor construction, by itself and without this complex/cyclotomic identification, already supplies the arithmetic Galois action.

---

## 5. Explicit character-to-cone intertwiner

Choose the basis-compatible map

\[
\boxed{
\chi_{-3}\mapsto R_X,
\qquad
\chi_{-4}\mapsto R_Y,
\qquad
\sigma\mapsto S_T.
}
\]

Equivalently,

\[
\mathscr G(\psi_{abc})=R_X^aR_Y^bS_T^c.
\]

This is an isomorphism

\[
\boxed{
\mathscr G:\widehat{U(24)}\overset\sim\longrightarrow G_{\rm cone}.
}
\]

The middle generator has the intrinsic complex/cyclotomic justification of Section 4. The first and third assignments are a compatible completion of the basis and are **not yet asserted to be canonically forced by arithmetic**.

Combining the carrier self-duality and cone map gives

\[
\Phi=\mathscr G\circ\mathscr D:
U(24)\overset\sim\longrightarrow G_{\rm cone},
\]

with

\[
\boxed{
\Phi(5^a7^b(-1)^c)=R_X^aR_Y^bS_T^c.
}
\]

---

## 6. Complete eight-element verification

The complete table is

\[
\begin{array}{c|c|c|c}
v&r(v)&\mathscr D(r)&\Phi(r)(X,Y,T)\\ \hline
000&1&1&(X,Y,T)\\
100&5&\chi_{-3}&(-X,Y,T)\\
010&7&\chi_{-4}&(X,-Y,T)\\
110&11&\chi_{12}&(-X,-Y,T)\\
001&-1&\sigma&(X,Y,-T)\\
101&-5&\sigma\chi_{-3}&(-X,Y,-T)\\
011&-7&\sigma\chi_{-4}&(X,-Y,-T)\\
111&-11&\sigma\chi_{12}&(-X,-Y,-T)
\end{array}
\]

In complex notation:

\[
\begin{array}{c|c}
r&\Phi(r)(z,T)\\ \hline
1&(z,T)\\
5&(-\bar z,T)\\
7&(\bar z,T)\\
11&(-z,T)\\
-1&(z,-T)\\
-5&(-\bar z,-T)\\
-7&(\bar z,-T)\\
-11&(-z,-T)
\end{array}
\]

The homomorphism law follows directly. If

\[
v=(a,b,c),\qquad w=(a',b',c'),
\]

then

\[
\Phi(r(v)r(w))
=\Phi(r(v+w))
=R_X^{a+a'}R_Y^{b+b'}S_T^{c+c'}
=\Phi(r(v))\Phi(r(w)).
\]

The kernel is trivial because

\[
R_X^aR_Y^bS_T^c=I
\]

forces

\[
a=b=c=0.
\]

Both groups have eight elements, so `Phi` is an isomorphism.

---

## 7. The 11 / chi_12 half-turn

Since

\[
11=5\cdot7,
\]

we obtain

\[
\boxed{
11\longleftrightarrow
\chi_{-3}\chi_{-4}
=\chi_{12}
\longleftrightarrow
R_XR_Y.
}
\]

On the cone,

\[
R_XR_Y:(z,T)\mapsto(-z,T),
\]

which is the half-turn of every fixed-`T` cone circle.

This matches the previously established tetrahedral standard-representation operator

\[
D_{11}=\operatorname{diag}(-1,-1,+1),
\]

which is a 180-degree rotation about the `chi_12` axis. The two statements are exact within their respective representations of the same selected `11/chi_12` label.

This compatibility does **not**, by itself, prove that the full chosen three-generator cone intertwiner is canonical.

---

## 8. Arithmetic sign versus QR deck involution

The arithmetic sign direction is

\[
S_{24}=001.
\]

Under the present explicit cone map,

\[
\boxed{001\longleftrightarrow S_T:(X,Y,T)\mapsto(X,Y,-T).}
\]

The QR deck direction remains

\[
K=111.
\]

Therefore

\[
\boxed{
111\longleftrightarrow R_XR_YS_T,
}
\]

which is the full antipodal map

\[
\boxed{(X,Y,T)\mapsto(-X,-Y,-T).}
\]

Thus the earlier distinction is preserved exactly:

\[
\boxed{
\text{arithmetic sign}=001,
\qquad
\text{QR deck}=111.
}
\]

They are not the same involution.

---

## 9. Relation to the three quadratic cyclotomic axes

The cyclotomic field decomposes over `Q` as

\[
\mathbf Q(\zeta_{12})
=\mathbf Q\,1
\oplus\mathbf Q\,i
\oplus\mathbf Q\,i\sqrt3
\oplus\mathbf Q\,\sqrt3.
\]

The nonprincipal character axes are

\[
\boxed{
\chi_{-4}\leftrightarrow i,
\qquad
\chi_{-3}\leftrightarrow i\sqrt3,
\qquad
\chi_{12}\leftrightarrow\sqrt3.
}
\]

Their multiplication relation

\[
i\cdot\sqrt3=i\sqrt3
\]

mirrors

\[
\chi_{-4}\chi_{12}=\chi_{-3}.
\]

Independently, the Pell law is

\[
\sigma_r(\lambda^n)=\lambda^{\chi_{12}(r)n},
\qquad \lambda=2+\sqrt3.
\]

Hence `chi_12` remains exactly the Pell time-orientation character while, in the chosen cone realization above, the corresponding `11` carrier element acts as the fixed-sheet half-turn `z -> -z`.

These are compatible representation-theoretic descriptions; no causal Pell-to-cone dynamical map is asserted here.

---

## 10. Guardrails and next certification target

### Exact/proved here

- `U(24) ≅ F_2^3 ≅ C_2^3`.
- `widehat{U(24)} ≅ F_2^3 ≅ C_2^3`.
- `G_cone=<R_X,R_Y,S_T> ≅ C_2^3`.
- The displayed binary pairing gives an explicit self-duality `U(24) -> widehat{U(24)}`.
- The displayed generator assignment gives an explicit isomorphism `widehat{U(24)} -> G_cone`.
- All eight elements and their real/complex cone actions are verified.
- Under the compatible oriented complex identification `i_cone=ζ_12^3`, `chi_-4` is exactly `Y`-reflection parity.
- Under the chosen full intertwiner, arithmetic sign `001` is sheet reversal and QR deck `111` is the full antipodal map.

### Not yet proved canonical

- `chi_-3 -> R_X` is not yet independently forced by arithmetic.
- `sigma -> S_T` is a natural signed-sheet convention but is not yet derived uniquely from the original positive-factor embedding.
- Therefore the full `U(24) <-> G_cone` basis assignment is explicit and compatible, but only its `chi_-4/R_Y` leg currently has the stronger cyclotomic-complex justification.
- No Pell-to-QR or Pell-to-cone dynamical map is asserted.

### Next target

Determine the stabilizer of the proven `chi_-4 <-> R_Y` leg inside `GL_3(F_2)` and impose the independently established `chi_12` Pell orientation and `11` tetrahedral half-turn. This will measure exactly how much ambiguity remains in the full three-generator intertwiner and whether the chosen assignments `chi_-3 -> R_X` and `sigma -> S_T` become forced after all existing structures are imposed.
