# Cone Derivation Ledger v13.447 — Mod-4 Character Recovery and First 2-Adic Separation

Date: 2026-09-14

Status labels: **[D]** exact derived; **[I]** interpretation; **[Audit]** guardrail.

## 0. Synchronization [Audit]

The live ledger was checked at the start of this continuation and again immediately before this write. The newest numbered checkpoint remained `v13.446` (`Mod-2 Character Collapse and Unavoidable C2 Ambiguity`), while the unnumbered research note for the present calculation had already been committed. Therefore `v13.447` was free at creation time.

Relevant predecessors:

- `v13.442`: prime-2 tangent `V4` and `S3` automorphism bridge;
- `v13.444`: canonical `V4` self-duality and the pointed tangent/character bridge;
- `v13.446`: exact proof that `chi_-4` and `chi_12` cannot be distinguished inside the full mod-2 carrier because `i ≡ sqrt(3) (mod 2)`.

The present checkpoint tests the next 2-adic level, modulo 4.

## 1. Mod-4 carrier [D]

Let

\[
K=\mathbf Q(\zeta_{12})=\mathbf Q(\sqrt3,i),
\qquad
\mathcal O_K=\mathbf Z[\zeta_{12}],
\]

and define

\[
R_4:=\mathcal O_K/4\mathcal O_K,
\qquad
R_2:=\mathcal O_K/2\mathcal O_K.
\]

Write

\[
u:=\bar\zeta_{12}\in R_4.
\]

## 2. The two collapsed character directions separate modulo 4 [D]

The integral identities

\[
\boxed{\sqrt3+i=2\zeta_{12}}
\]

and

\[
\boxed{\sqrt3-i=2\zeta_{12}^{-1}}
\]

hold in `O_K`.

Modulo 2 both right-hand sides vanish, recovering

\[
\boxed{i\equiv\sqrt3\pmod2.}
\]

This is exactly the obstruction isolated in `v13.446`.

Modulo 4, however, `u` and `u^{-1}` are units, so

\[
2u\neq0,
\qquad
2u^{-1}\neq0
\]

in `R_4`. Hence

\[
\boxed{i\not\equiv\sqrt3\pmod4.}
\]

Thus the residual

\[
\chi_{-4}\leftrightarrow\chi_{12}
\]

ambiguity is a depth-one mod-2 phenomenon. It disappears at the first deeper 2-adic layer.

## 3. The cyclotomic generator regains exact order 12 modulo 4 [D]

Since

\[
\zeta_{12}^{12}=1,
\]

the order of `u` in `R_4^x` divides 12.

But

\[
u^6=-1,
\]

and

\[
-1\neq1\pmod4.
\]

Therefore the order does not divide 6, and hence

\[
\boxed{\operatorname{ord}_{R_4}(u)=12.}
\]

This contrasts with the already established reductions

\[
\operatorname{ord}_{R_2}(\bar\zeta_{12})=6,
\qquad
\operatorname{ord}_{\mathbf F_4}(\omega)=3.
\]

So the cyclotomic multiplication clock across the first 2-adic levels is

\[
\boxed{
12\text{ in characteristic zero}
\to
12\text{ mod }4
\to
6\text{ mod }2
\to
3\text{ in }\mathbf F_4.
}
\]

The first loss of rotational information occurs precisely at reduction mod 2, not mod 4.

## 4. Faithful recovery of the full V4 Galois action modulo 4 [D]

For

\[
r\in U(12)=\{1,5,7,11\},
\]

one has

\[
\sigma_r(u)=u^r.
\]

Because `u` has exact order 12 in `R_4`, the four exponents

\[
1,5,7,11\pmod{12}
\]

produce four distinct elements. Hence

\[
\boxed{
U(12)\hookrightarrow\operatorname{Aut}(R_4)
}
\]

is faithful.

Thus the character-information filtration at the ramified prime 2 is

\[
\boxed{
V_4\text{ in characteristic zero}
\longrightarrow
V_4\text{ mod }4
\longrightarrow
C_2\text{ mod }2
\longrightarrow
C_2\text{ on }\mathbf F_4.
}
\]

The two collapsed character bits are therefore genuinely recoverable one 2-adic level higher.

## 5. The first 2-adic correction module [D]

The reduction map

\[
R_4\twoheadrightarrow R_2
\]

has kernel

\[
2R_4.
\]

Multiplication by 2 gives a canonical additive identification

\[
\boxed{
R_2\xrightarrow{\sim}2R_4,
\qquad
\bar x\longmapsto2x\pmod4.
}
\]

Under this identification, the first-order separation data are

\[
\boxed{
\sqrt3+i\longleftrightarrow u,
\qquad
\sqrt3-i\longleftrightarrow u^{-1}.
}
\]

So the correction module remembers the oriented pair

\[
\boxed{u\ \text{versus}\ u^{-1}}
\]

that becomes invisible after reducing all the way to `R_2`.

## 6. Galois action on the correction pair [D]

Inside the kernel `2R_4`, signs disappear because

\[
-2\equiv2\pmod4.
\]

Hence the action of the four Galois classes on the pair

\[
\{2u,2u^{-1}\}
\]

collapses to:

\[
\boxed{
\begin{array}{c|c}
r&\text{action on }\{2u,2u^{-1}\}\\
\hline
1,7&\text{fix}\\
5,11&\text{exchange}
\end{array}}
\]

which is again exactly the `chi_-3` quotient.

This does not contradict the faithful ambient `V4` action on `R_4`: the two-element correction pair is itself only a quotient observable.

## 7. Canonical lifts of the two characteristic-zero directions [D/I]

With the fixed primitive root `zeta_12`, the two characteristic-zero generators have the exact expressions

\[
\boxed{i=u^3}
\]

and

\[
\boxed{\sqrt3=u+u^{-1}.}
\]

They reduce to the same tangent involution in `R_2`, but remain distinct in `R_4`:

\[
\boxed{\sqrt3-i=2u^{-1}.}
\]

Therefore the pointed mod-2 bridge from `v13.444-v13.446` admits a canonical refinement once the first deeper 2-adic layer is retained: the `i` direction and the `sqrt3` direction are no longer interchangeable.

**[I]** The mod-2 residual `C2` is thus not an intrinsic ambiguity of the full 2-adic arithmetic; it is a truncation symmetry caused by throwing away the first correction module.

## 8. Relation to the two ramified-prime filtrations [I/Audit]

At the ramified prime 3 on the Pell side,

\[
\mathcal O_{\mathbf Q(\sqrt3)}/3
\cong
\mathbf F_3[\epsilon]/(\epsilon^2),
\]

and the first-order tangent coordinate carries the exact three-phase

\[
j\mapsto j+1,
\qquad
j\mapsto-j.
\]

At the ramified prime 2 on the cyclotomic side,

\[
R_2\cong\mathbf F_4[\eta]/(\eta^2)
\]

carries the tangent Klein four structure, while the next lift

\[
R_4\to R_2
\]

restores the two character directions lost at depth one.

The common principle is therefore filtration-sensitive:

\[
\boxed{
\text{ramified tangent quotients expose reduced phase symmetries,}
\quad
\text{deeper lifts recover distinctions killed at first order.}
}
\]

**[Audit]** The prime-2 and prime-3 local rings have different residue fields, different unit groups, and different ramification indices. This is a structural comparison of filtrations, not a ring identification.

## 9. Guardrails [Audit]

- `i ≡ sqrt3 (mod 2)` remains exactly true.
- Their separation mod 4 does not imply a canonical ring isomorphism between `U(12)` and the tangent `V4`.
- The pair `{2u,2u^{-1}}` still sees only the `chi_-3` quotient even though `R_4` sees the full `V4` action.
- No Cone-shell or Suzuki-sector identification is inferred from this 2-adic recovery.

## 10. Compact conclusion

The mod-2 ambiguity from `v13.446` terminates at the next 2-adic level:

\[
\boxed{
\sqrt3+i=2u,
\qquad
\sqrt3-i=2u^{-1}\pmod4,
}
\]

with

\[
\boxed{\operatorname{ord}_{R_4}(u)=12}
\]

and faithful

\[
\boxed{U(12)\cong V_4\hookrightarrow\operatorname{Aut}(R_4).}
\]

Hence the full character distinction lost in the ramified mod-2 carrier is already restored modulo 4. The remaining mod-2 `C2` swap is therefore exactly a first-order truncation symmetry, not a genuine ambiguity of the deeper 2-adic cyclotomic structure.