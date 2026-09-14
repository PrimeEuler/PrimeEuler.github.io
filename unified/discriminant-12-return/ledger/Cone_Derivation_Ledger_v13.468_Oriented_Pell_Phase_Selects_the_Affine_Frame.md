# Cone Derivation Ledger v13.468 — Oriented Pell Phase Selects the Affine Frame

Date: 2026-09-14

Status labels: **[D]** exact derived; **[I]** interpretation; **[Audit]** guardrail.

## 0. Synchronization [Audit]

The live ledger was checked immediately before this write. The newest numbered entry was `v13.467`, so `v13.468` was free.

Relevant predecessors:

- `v13.441`: prime-3 Pell tangent phase and the explicit intertwiner with `F4^x`;
- `v13.442`: prime-2 tangent `V4` and its intrinsic `S3` automorphism action;
- `v13.460`: affine completion `V4 \rtimes S3 \cong S4` on the four prime-2 tangent states;
- `v13.462`: mod-4 lift obstruction to a naive canonical `U(12) -> T2` translation identification;
- `v13.466`: the residual affine-frame ambiguity is represented by the two coboundary trivializations `b=w,w^2` of the crossed cocycle `c(tau)=1`.

The present checkpoint asks whether the *other ramified prime*, namely the Pell prime `3`, selects one of those two trivializations.

## 1. Prime-3 oriented Pell phase [D]

Let

\[
F=\mathbf Q(\sqrt3),\qquad \epsilon=\sqrt3\bmod3,
\qquad \epsilon^2=0,
\]

so

\[
\mathcal O_F/3\mathcal O_F\cong\mathbf F_3[\epsilon]/(\epsilon^2).
\]

For a local unit `a+b epsilon`, the projective phase coordinate from `v13.441` is

\[
\boxed{
 j([a+b\epsilon])=\frac{2b}{a}\in\mathbf F_3.
}
\]

The distinguished positive fundamental unit is

\[
\lambda=2+\sqrt3.
\]

Modulo `3`,

\[
\lambda\equiv2+\epsilon.
\]

Since `2^{-1}=2` in `F3`,

\[
 j([\lambda])
 =\frac{2\cdot1}{2}
 =1.
\]

Therefore

\[
\boxed{j([\lambda])=1.}
\]

Likewise conjugation sends

\[
\lambda\mapsto\lambda^{-1}=2-\sqrt3,
\]

so

\[
\boxed{j([\lambda^{-1}])=-1=2\in\mathbf F_3.}
\]

Thus the two Pell time orientations are exactly the two nonzero orientations of the three-phase cycle.

## 2. Two-prime phase intertwiner [D]

Fix the prime-2 residue-field generator

\[
w\in\mathbf F_4^\times,
\qquad w^2+w+1=0,
\]

chosen by the cyclotomic reduction of the distinguished `zeta_12` orientation.

The exact intertwiner of `v13.441` is

\[
\Psi:\mathbf F_3\longrightarrow\mathbf F_4^\times,
\qquad
\boxed{\Psi(j)=w^j.}
\]

Hence

\[
\boxed{
\Psi([\lambda])=w,
\qquad
\Psi([\lambda^{-1}])=w^2.
}
\]

The Pell orientation reversal

\[
\lambda\leftrightarrow\lambda^{-1}
\]

therefore corresponds exactly to

\[
\boxed{w\leftrightarrow w^2}
\]

on the prime-2 phase side.

## 3. Compare with the affine-frame trivialization torsor [D]

From `v13.466`, the nonzero crossed cocycle on the surviving prime-2 involution is

\[
 c(\tau)=1,
\]

and a coboundary trivialization requires

\[
 b+\tau(b)=1.
\]

Since `tau(b)=b^2`, this is

\[
\boxed{b+b^2=1.}
\]

Its two and only two solutions in `F4` are

\[
\boxed{b=w,\qquad b=w^2.}
\]

Comparing with the two-prime Pell phase gives the exact identification

\[
\boxed{
 b_+=\Psi([\lambda])=w,
\qquad
 b_-=\Psi([\lambda^{-1}])=w^2.
}
\]

Thus the two-point affine-frame torsor of `v13.466` is canonically identified with the two Pell time orientations.

## 4. Oriented versus unoriented canonicity [D/I]

If the discriminant-12 system is treated without a chosen time orientation, then

\[
\lambda\leftrightarrow\lambda^{-1}
\]

is an allowed inversion, and correspondingly

\[
 w\leftrightarrow w^2.
\]

Therefore the two affine frames remain exchanged by a genuine `C2` symmetry.

But once the positive real Pell generator is chosen,

\[
\boxed{\lambda=2+\sqrt3>1,}
\]

its phase is `j=+1`, and the compatible trivialization is forced to be

\[
\boxed{b=w.}
\]

Equivalently, the opposite time orientation chooses

\[
\boxed{b=w^2.}
\]

Hence:

\[
\boxed{
\text{unoriented discriminant-12 arithmetic leaves a }C_2\text{ frame torsor,}
}
\]

while

\[
\boxed{
\text{oriented Pell time canonically selects one affine frame.}
}
\]

## 5. Affine involution in the selected frame [D]

The cocycle representative from `v13.466` gives the affine Frobenius involution

\[
F'(t)=t^2+1.
\]

For a trivializing translation `T_b`,

\[
F'=T_bFT_b^{-1}
\]

precisely when

\[
b+b^2=1.
\]

Choosing the positive Pell orientation gives `b=w`, hence

\[
\boxed{F'=T_wFT_w^{-1}.}
\]

Choosing the negative Pell orientation gives

\[
\boxed{F'=T_{w^2}FT_{w^2}^{-1}.}
\]

Thus the two affine conjugacies are not arbitrary: they are exactly the images of the two Pell time orientations.

## 6. Four-state interpretation [I]

The prime-2 tangent affine space is

\[
T_2\cong\mathbf F_4
\]

with full symmetry

\[
AGL_2(\mathbf F_2)\cong S_4.
\]

Without a Pell orientation, the arithmetic determines the `S4` action together with a two-point torsor of compatible affine origins.

Once the positive Pell generator is chosen, the two-prime bridge selects the frame shift `w`, so the semilinear mod-4 lift is placed into a definite affine coordinate system.

This is the strongest justified sense in which the ramified prime `3` resolves the frame ambiguity left internally by the prime `2` analysis.

## 7. Relation to the character time-orientation law [D/I]

From `v13.414`,

\[
\sigma_r(\lambda)=\lambda^{\chi_{12}(r)}.
\]

Thus `chi_12` records Pell time orientation in characteristic zero.

The present result shows that, after passage through the prime-3 phase and the two-prime intertwiner, reversing that orientation exchanges

\[
\boxed{w\leftrightarrow w^2,}
\]

which is exactly the exchange of the two affine-frame trivializations.

So the affine-frame `C2` is the finite shadow of Pell time reversal once the two ramified local phases are compared.

**[Audit]** This does not mean that every Galois element with `chi_12=-1` acts on the prime-2 residue field as Frobenius. The residue-field Galois quotient is controlled by `chi_-3`, as established earlier. The statement here concerns the *intertwined phase orientation*, not equality of the two characters.

## 8. Canonicality statement [D/I]

There are now three levels:

1. **Prime-2 arithmetic alone:** canonical `S4` tangent symmetry, but two compatible affine-frame trivializations `w,w^2`.
2. **Two-prime arithmetic without orientation:** the same two frames are canonically identified with the pair `{lambda,lambda^{-1}}`; the `C2` remains as time reversal.
3. **Two-prime arithmetic with positive Pell orientation:** `lambda=2+sqrt3>1` selects
   \[
   \boxed{b=w,}
   \]
   giving a definite affine frame.

Therefore

\[
\boxed{
\text{the final frame ambiguity is not independent of the Pell side; it is exactly the Pell time-orientation torsor.}
}
\]

## 9. Guardrails [Audit]

- The positive Pell orientation uses the chosen real embedding in which `2+sqrt3>1`.
- Without that oriented real embedding, the pair `lambda,lambda^{-1}` is unordered.
- The selection `b=w` depends on compatibility with the already fixed cyclotomic phase generator `w` coming from the chosen `zeta_12` orientation.
- This does not produce a literal equality `U(12)=T2`.
- The earlier mod-4 twisted-lift obstruction remains valid: the Galois `V4` action is not itself a translation action on `T2`.
- What is canonically selected is an affine *frame/trivialization*, not an identification of the two Klein-four groups.
- No new Cone-shell or Suzuki operator theorem follows from this local arithmetic result.

---

**Checkpoint conclusion.** The two ramified primes do resolve the affine-frame ambiguity once Pell time is oriented. The prime-3 phase sends the positive fundamental unit `lambda=2+sqrt3` to phase `+1`; the exact two-prime intertwiner sends that phase to `w`; and `w` is one of the two and only two coboundary trivializations of the prime-2 crossed cocycle. The inverse Pell orientation maps to `w^2`, the other trivialization. Hence the residual affine-frame `C2` is exactly the finite image of Pell time reversal. Unoriented arithmetic retains the `C2` torsor; the chosen positive Pell direction selects a unique compatible affine frame.