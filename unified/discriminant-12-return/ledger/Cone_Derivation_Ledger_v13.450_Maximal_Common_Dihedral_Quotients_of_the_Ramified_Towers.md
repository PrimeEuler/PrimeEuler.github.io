# Cone Derivation Ledger v13.450 — Maximal Common Dihedral Quotients of the Ramified Towers

Date: 2026-09-14

Status labels: **[D]** exact derived; **[I]** interpretation; **[Audit]** guardrail.

## 0. Synchronization [Audit]

The live ledger was checked immediately before this write. The newest numbered checkpoint was `v13.449` (`Reconcile Odd Frozen-8D Normalized Provenance`), so `v13.450` was free.

Relevant arithmetic predecessors:

- `v13.438`: cyclotomic dihedral quotient tower `D24 -> D12 -> S3` at the first ramified 2-adic layers;
- `v13.439`: common Pell/cyclotomic `C6` and `S3` quotients at shallow depth;
- `v13.447`: mod-4 recovery of full cyclotomic order 12 and faithful `V4` Galois action;
- `v13.448`: exact local order profiles `12` on the deep 2-adic cyclotomic side and `2*3^k` on the Pell mod-`3^k` side.

The present checkpoint upgrades the shallow common-quotient observation to a maximality statement valid uniformly through the deeper local towers.

## 1. Convention [Audit]

Use

\[
D_{2n}:=C_n\rtimes C_2
\]

for the dihedral group of order `2n`, where the involution acts on the cyclic rotation subgroup by inversion.

All maximality statements below are for quotients preserving the distinguished rotation/reflection structure: rotation maps to rotation and the inversion involution maps to the corresponding reflection. No claim is made about arbitrary abstract quotients that forget this structure.

## 2. Deep cyclotomic dihedral group [D]

Let

\[
K=\mathbf Q(\zeta_{12}),
\qquad
R_{2^m}=\mathcal O_K/2^m\mathcal O_K,
\qquad m\ge2.
\]

By `v13.447-v13.448`, the image

\[
u_m:=\zeta_{12}\bmod 2^m
\]

has exact order `12`.

Let `c` denote complex conjugation. Then

\[
c^2=1,
\qquad
cu_mc=u_m^{-1}.
\]

Therefore

\[
\boxed{
G_{C,m}:=\langle u_m,c\rangle
\cong
C_{12}\rtimes C_2
=D_{24}
\qquad(m\ge2).
}
\]

Thus the deep cyclotomic inversion group is stable: its rotational order remains `12` at every 2-adic depth `m>=2`.

## 3. Deep Pell dihedral group [D]

Let

\[
F=\mathbf Q(\sqrt3),
\qquad
\lambda=2+\sqrt3,
\]

and let `g=g_12` be multiplication by `lambda` in the ramified ideal basis.

From `v13.448`, modulo `3^k`,

\[
\operatorname{ord}(g)=2\cdot3^k.
\]

Let `J=J_f` be quadratic conjugation. Then

\[
J^2=1,
\qquad
JgJ=g^{-1}.
\]

Hence

\[
\boxed{
G_{P,k}:=\langle g,J\rangle\bmod3^k
\cong
C_{2\cdot3^k}\rtimes C_2
=D_{4\cdot3^k}.
}
\]

The Pell rotational order grows without bound with `k`.

## 4. Maximal common cyclic rotation quotient [D]

A cyclic group `C_a` and a cyclic group `C_b` have largest common cyclic quotient

\[
C_{\gcd(a,b)}.
\]

Here

\[
a=12,
\qquad
b=2\cdot3^k.
\]

For every `k>=1`,

\[
\gcd(12,2\cdot3^k)=6.
\]

Therefore the largest common cyclic quotient of the distinguished rotation subgroups is

\[
\boxed{C_6.}
\]

Explicitly, on the cyclotomic side one quotients

\[
C_{12}\twoheadrightarrow C_6
\]

by the central half-turn

\[
\langle u_m^6\rangle\cong C_2.
\]

On the Pell side,

\[
C_{2\cdot3^k}\twoheadrightarrow C_6
\]

has kernel

\[
\langle g^6\rangle,
\]

of order `3^{k-1}`.

For `k=1` the Pell rotational group is already `C6`.

## 5. Maximal common nonprojective dihedral quotient [D]

Because inversion descends through cyclic quotients, both groups admit structure-preserving surjections

\[
G_{C,m}\twoheadrightarrow C_6\rtimes C_2,
\]

and

\[
G_{P,k}\twoheadrightarrow C_6\rtimes C_2.
\]

Thus both surject onto

\[
\boxed{D_{12}.}
\]

No larger structure-preserving common dihedral quotient exists: any such common quotient would have cyclic rotation subgroup whose order divides both `12` and `2*3^k`, hence divides `6`.

Therefore

\[
\boxed{
D_{12}\text{ is the maximal common nonprojective dihedral quotient of the two local towers.}
}
\]

This statement holds uniformly for every cyclotomic depth `m>=2` and every Pell depth `k>=1`.

## 6. Projective Pell tower [D]

From `v13.448`,

\[
g^{3^k}\equiv-I\pmod{3^k}.
\]

Projectivization kills the scalar `-I`, leaving

\[
\operatorname{ord}([g])=3^k.
\]

Hence the projective Pell inversion group is

\[
\boxed{
\overline G_{P,k}
:=\langle[g],[J]\rangle
\cong
C_{3^k}\rtimes C_2
=D_{2\cdot3^k}.
}
\]

For `k=1`, this is

\[
D_6\cong S_3.
\]

## 7. Cyclotomic half-turn quotient [D]

On the deep cyclotomic side, quotient the rotation group by the characteristic-zero half-turn:

\[
C_{12}/\langle u_m^6\rangle\cong C_6.
\]

The corresponding dihedral quotient is

\[
\boxed{
\overline G_{C,m}
:=G_{C,m}/\langle u_m^6\rangle
\cong
C_6\rtimes C_2
=D_{12}.
}
\]

This is the stable deep analogue of the mod-2 order-6 cyclotomic group found in `v13.438`.

## 8. Maximal common phase quotient [D]

Compare the projective Pell rotation

\[
C_{3^k}
\]

with the half-turn-quotiented cyclotomic rotation

\[
C_6.
\]

For every `k>=1`,

\[
\gcd(3^k,6)=3.
\]

Hence the largest common cyclic phase quotient is

\[
\boxed{C_3.}
\]

Including the common inversion involution gives

\[
\boxed{
C_3\rtimes C_2
=D_6
\cong S_3.
}
\]

No larger structure-preserving common phase quotient exists because any common rotational quotient must have order dividing `gcd(3^k,6)=3`.

Therefore

\[
\boxed{
S_3\text{ is the maximal common projective/phase dihedral quotient at every depth.}
}
\]

## 9. Explicit quotient kernels [D]

### Cyclotomic nonprojective quotient

\[
G_{C,m}=D_{24}\twoheadrightarrow D_{12}
\]

kills

\[
\boxed{\langle u_m^6\rangle\cong C_2.}
\]

### Pell nonprojective quotient

\[
G_{P,k}=D_{4\cdot3^k}\twoheadrightarrow D_{12}
\]

kills the rotational subgroup

\[
\boxed{\langle g^6\rangle\cong C_{3^{k-1}}.}
\]

### Cyclotomic phase quotient

\[
D_{12}\twoheadrightarrow S_3
\]

kills the unique central rotational involution in `C6`.

### Pell projective phase quotient

\[
D_{2\cdot3^k}\twoheadrightarrow S_3
\]

kills

\[
\boxed{C_{3^{k-1}}\subset C_{3^k}.}
\]

Thus the same final `S3` is reached by very different kernels: 2-primary torsion is discarded on the cyclotomic side, whereas deeper 3-primary principal-unit phase is discarded on the Pell side.

## 10. Quotient diagram [D]

For every `m>=2`, `k>=1`, the exact common architecture is

\[
\boxed{
\begin{array}{ccccc}
D_{24}^{\rm cyc} & \twoheadrightarrow & D_{12} & \twoheadrightarrow & S_3\\
&& \rotatebox{90}{$\cong$} && \rotatebox{90}{$\cong$}\\
D_{4\cdot3^k}^{\rm Pell} & \twoheadrightarrow & D_{12} & \twoheadrightarrow & S_3
\end{array}
}
\]

where the middle and terminal identifications are abstract structure-preserving identifications, not identifications of the original arithmetic carriers.

On the Pell bottom row, the final arrow is understood after projectivizing the scalar sign and reducing the `3^k` rotation to its `C3` quotient.

## 11. Relation to the explicit three-state intertwiner [D/I]

The terminal common quotient is not merely abstract. From `v13.439-v13.441`, its faithful three-point actions are explicitly intertwined by

\[
\Psi:j\in\mathbf F_3\longmapsto\omega^j\in\mathbf F_4^\times.
\]

Under this map,

\[
j\mapsto j+1
\]

corresponds to multiplication by `omega`, and

\[
j\mapsto-j
\]

corresponds to Frobenius.

Thus the maximal common quotient theorem identifies the previously constructed finite exponential bridge as the terminal faithful three-state realization of the common local inversion architecture.

## 12. Structural interpretation [I]

The two local towers diverge strongly at deeper levels:

- the cyclotomic 2-adic rotational group stabilizes at `C12`;
- the Pell 3-adic rotational group grows as `C_{2*3^k}`;
- after removing their incompatible deeper components, the largest common nonprojective rotation is always `C6`;
- after also passing to the projective/phase level, the largest common rotation is always `C3`.

Hence the recurring `S3` is not an accidental depth-one coincidence. It is the **maximal common finite phase quotient** forced by the arithmetic orders of the two ramified towers.

## 13. Guardrails [Audit]

- `D24`, `D12`, and `S3` here refer to abstract inversion extensions of distinguished cyclic rotations; the original cyclotomic and Pell carriers remain different.
- The maximality claim is within the category of quotients preserving the rotation/reflection structure.
- No ring homomorphism between the 2-adic and 3-adic local rings is asserted.
- The common `S3` quotient does not identify deeper 2-adic and 3-adic congruence layers.
- No implication for the Suzuki positivity/theorem-promotion thread is claimed.

---

**Checkpoint conclusion.** For every deeper pair of ramified local levels, the cyclotomic and Pell inversion groups have maximal common nonprojective quotient

\[
\boxed{D_{12}=C_6\rtimes C_2,}
\]

and maximal common projective/phase quotient

\[
\boxed{D_6=C_3\rtimes C_2\cong S_3.}
\]

The finite `S3` phase therefore persists canonically as the largest common inversion quotient of a stable 2-adic torsion tower and an expanding 3-adic principal-unit tower.