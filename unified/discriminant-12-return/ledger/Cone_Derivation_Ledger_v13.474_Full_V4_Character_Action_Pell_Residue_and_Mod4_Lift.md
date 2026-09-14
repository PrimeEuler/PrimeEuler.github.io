# Cone Derivation Ledger v13.474

## Full V4 Character Action: Pell Time, Residue Frobenius, and the Mod-4 Lift Bit

### Status
Exact finite arithmetic synthesis of the character data established in v13.414, v13.416, v13.458, v13.468, and v13.469. No theorem-level Suzuki/operator claim is changed here.

---

## 1. The three quadratic characters on U(12)

Let

\[
G=U(12)=\{1,5,7,11\}\cong V_4.
\]

Use the three nontrivial quadratic characters

\[
\chi_{-4},\qquad \chi_{-3},\qquad \chi_{12}=\chi_{-4}\chi_{-3}.
\]

Their values are

\[
\begin{array}{c|ccc}
r & \chi_{12}(r) & \chi_{-3}(r) & \chi_{-4}(r)\\
\hline
1  & +1 & +1 & +1\\
5  & -1 & -1 & +1\\
7  & -1 & +1 & -1\\
11 & +1 & -1 & -1
\end{array}
\]

and therefore

\[
\boxed{\chi_{-4}(r)=\chi_{12}(r)\chi_{-3}(r).}
\]

Thus the pair

\[
\boxed{(\chi_{12},\chi_{-3})}
\]

already recovers the full element of the Klein four group.

---

## 2. First bit: Pell time orientation

Let

\[
\lambda=2+\sqrt3,
\qquad
\lambda^{-1}=2-\sqrt3.
\]

For the cyclotomic Galois element \(\sigma_r\),

\[
\sigma_r(\sqrt3)=\chi_{12}(r)\sqrt3,
\]

hence

\[
\boxed{\sigma_r(\lambda)=\lambda^{\chi_{12}(r)}.}
\]

Equivalently, for

\[
R_{12}=\log\lambda,
\]

\[
\boxed{R_{12}\mapsto \chi_{12}(r)R_{12}.}
\]

Therefore

\[
\boxed{\chi_{12}=\text{Pell time-orientation bit}.}
\]

Explicitly,

\[
\{1,11\}:\ \lambda\mapsto\lambda,
\qquad
\{5,7\}:\ \lambda\mapsto\lambda^{-1}.
\]

At the prime-3 projective tangent phase,

\[
j([\lambda])=+1,
\qquad
j([\lambda^{-1}])=-1,
\]

so

\[
\boxed{j_r=\chi_{12}(r)\in\{\pm1\}\subset\mathbf F_3.}
\]

Under the established phase intertwiner

\[
\Psi(j)=w^j,
\]

this selects the affine-frame trivialization

\[
\boxed{b_r=w^{\chi_{12}(r)}}
\]

with \(w^{-1}=w^2\). Thus

\[
\chi_{12}=+1\Rightarrow b=w,
\qquad
\chi_{12}=-1\Rightarrow b=w^2.
\]

---

## 3. Second bit: prime-2 residue-field action

At the ramified prime 2,

\[
O_{K_{12}}/\mathfrak P_2\cong\mathbf F_4.
\]

The reduced Galois action is

\[
\boxed{
\bar\sigma_r=
\begin{cases}
\mathrm{id},&\chi_{-3}(r)=+1,\\
\mathrm{Fr},&\chi_{-3}(r)=-1,
\end{cases}}
\]

where

\[
\mathrm{Fr}(x)=x^2.
\]

Therefore

\[
\boxed{\chi_{-3}=\text{prime-2 residue/Frobenius bit}.}
\]

Explicitly,

\[
\{1,7\}:\mathrm{id},
\qquad
\{5,11\}:\mathrm{Fr}.
\]

This action is independent of Pell time orientation. In particular:

\[
r=7:\quad \chi_{12}=-1,\ \chi_{-3}=+1,
\]

so 7 reverses Pell time while acting trivially on the residue field; whereas

\[
r=11:\quad \chi_{12}=+1,\ \chi_{-3}=-1,
\]

so 11 preserves Pell time while acting by Frobenius on the residue field.

---

## 4. Third bit: first-order mod-4 lift / derivation parity

The mod-2 reduction collapses

\[
\bar\sigma_1=\bar\sigma_7,
\qquad
\bar\sigma_5=\bar\sigma_{11}.
\]

The invisible distinction is recovered at first order modulo 4 by the derivation data from v13.458:

\[
D_7(\bar x)=\frac{\sigma_7(x)-x}{2}\pmod2,
\]

and

\[
D_{11,5}(\bar x)=\frac{\sigma_{11}(x)-\sigma_5(x)}2\pmod2.
\]

This is exactly the second independent binary distinction inside each mod-2 fiber. Its character is

\[
\boxed{\chi_{-4}.}
\]

Explicitly,

\[
\{1,5\}:\chi_{-4}=+1,
\qquad
\{7,11\}:\chi_{-4}=-1.
\]

Hence

\[
\boxed{\chi_{-4}=\text{first-order mod-4 lift/derivation bit}.}
\]

The key synthesis is that this bit is not independent once Pell time and residue Frobenius are known:

\[
\boxed{\chi_{-4}=\chi_{12}\chi_{-3}.}
\]

In binary language, if

\[
p(r)=\frac{1-\chi_{12}(r)}2,
\qquad
f(r)=\frac{1-\chi_{-3}(r)}2,
\]

then

\[
\ell(r)=\frac{1-\chi_{-4}(r)}2
\]

satisfies

\[
\boxed{\ell=p\oplus f.}
\]

Thus the mod-4 lift bit is the XOR of the Pell-time reversal bit and the residue-Frobenius bit.

---

## 5. Complete action table

\[
\begin{array}{c|c|c|c|c|c|c}
r & \chi_{12} & \lambda & j & b & \chi_{-3} & \mathbf F_4\text{ action}\\
\hline
1  & +1 & \lambda      & +1 & w   & +1 & \mathrm{id}\\
5  & -1 & \lambda^{-1} & -1 & w^2 & -1 & \mathrm{Fr}\\
7  & -1 & \lambda^{-1} & -1 & w^2 & +1 & \mathrm{id}\\
11 & +1 & \lambda      & +1 & w   & -1 & \mathrm{Fr}
\end{array}
\]

Appending the lift character gives

\[
\begin{array}{c|ccc|c}
r & \chi_{12} & \chi_{-3} & \chi_{-4} & (p,f,\ell)\\
\hline
1  & + & + & + & (0,0,0)\\
5  & - & - & + & (1,1,0)\\
7  & - & + & - & (1,0,1)\\
11 & + & - & - & (0,1,1)
\end{array}
\]

with

\[
\ell=p\oplus f.
\]

---

## 6. Character-theoretic reconstruction of V4

The map

\[
\boxed{
G\longrightarrow\{\pm1\}^2,
\qquad
r\longmapsto(\chi_{12}(r),\chi_{-3}(r))
}
\]

is an isomorphism onto a two-bit Klein four carrier.

The third character is the product coordinate:

\[
\boxed{
\chi_{-4}=\chi_{12}\chi_{-3}.
}
\]

Therefore the four arithmetic labels can be reconstructed from the two physically distinct actions:

1. real-quadratic/Pell orientation;
2. prime-2 residue-field Frobenius.

The mod-4 lift character is exactly their parity.

---

## 7. Guardrails

1. \(\chi_{12}\) controls the Galois action on \(\sqrt3\), hence on \(\lambda\) and Pell time.
2. \(\chi_{-3}\) controls the reduced Galois automorphism of \(\mathbf F_4\).
3. These are distinct actions; neither should be substituted for the other.
4. Direct multiplication by \(\lambda\) on the prime-2 residue field is trivial because \(\lambda\equiv1\pmod{\mathfrak P_2}\).
5. \(\chi_{-4}\) records the first-order mod-4 lift distinction recovered by the derivations; it is not an additional independent bit once \(\chi_{12}\) and \(\chi_{-3}\) are fixed.
6. The identity \(\chi_{-4}=\chi_{12}\chi_{-3}\) does not identify the Galois V4 pointwise with the tangent translation V4. The affine-frame selection remains a separate, oriented correspondence established in v13.468-v13.469.

---

## 8. Compact discriminant-12 synthesis

\[
\boxed{
\begin{aligned}
\chi_{12}&:\ \text{Pell time }\lambda\leftrightarrow\lambda^{-1},\\
\chi_{-3}&:\ \text{residue action }\mathrm{id}\leftrightarrow\mathrm{Fr},\\
\chi_{-4}&=\chi_{12}\chi_{-3}:\ \text{mod-4 lift parity}.
\end{aligned}}
\]

Equivalently, discriminant 12 supplies two independent arithmetic signs, and the third quadratic character is their product.
