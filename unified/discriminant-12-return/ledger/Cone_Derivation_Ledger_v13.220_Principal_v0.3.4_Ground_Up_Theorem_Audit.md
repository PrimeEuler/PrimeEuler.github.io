# Cone Derivation Ledger v13.220 — Principal v0.3.4 Ground-Up Theorem Audit

Date: 2026-09-04

Authoritative source audited:

`unified/discriminant-12-return/papers/Discriminant_12_Return_v0.3.4.tex`

Source blob at audit:

`33ca5f3d42bf7eb537bc5732a2644e46cc0bd51a`

## Purpose

This checkpoint audits the completed v0.3.4 principal manuscript from its own stated hypotheses rather than merely checking consistency with Papers A/B/C and the null-diamond bridge. Every major implication is classified as one of:

- **PROVED IN MANUSCRIPT** — follows by a displayed calculation or an explicit proof from prior results.
- **STANDARD IMPORTED FACT** — standard algebraic-number-theory / cyclotomic / finite-field input, correctly specialized.
- **NORMALIZATION / DEFINITION** — chosen convention or representative, not a consequence of the preceding theorem.
- **STRUCTURAL CORRESPONDENCE** — exact comparison across different carriers, with no claim of literal equality.
- **INTERPRETIVE / PRESENTATIONAL** — useful narrative statement that should not be read as an additional theorem.

## Executive result

**Overall theorem status: PASS, with theorem-packaging and local proof-completeness improvements recommended.**

No contradiction was found in the principal discriminant-12 chain. The core Cayley, Pell, ideal-lattice, factor-cone, cyclotomic, and finite-field statements are mutually compatible after the v0.3.4 correction separating literal residue multiplication by `lambda=2+sqrt(3)` from the transported mod-2 Pell action.

The strongest publication issue is now not a false theorem but a mismatch between the formal main theorem and the later proved claims: the XOR/field-trace identity and the n=11 Artin specialization are central conclusions of the abstract and conclusion but are not included in Theorem 2.1 or promoted to separate theorem/corollary statements.

A second local issue is that `O_K/P_2 ~= F_4` is correct and can be proved directly in two lines from the explicit cyclotomic presentation; the manuscript currently treats it mostly as a standard fact. Adding the direct quotient computation would make the finite-reduction section logically self-contained.

## Dependency audit

### A. Centered Cayley reciprocity

Let `g in SL_2(Q)`, `tau=tr(g)`,

`H = g - (tau/2) I`,

`K = (g-I)(g+I)^{-1}`.

Cayley-Hamilton gives

`g^2 - tau g + I = 0`,

hence

`H^2 = (tau^2/4 - 1) I`.

Also

`(g+I)((tau+1)I-g) = (tau+2)I`,

so, when `g+I` is invertible,

`K = 2 H/(tau+2)`

and

`KH = (tau-2)I/2`.

Classification: **PROVED IN MANUSCRIPT**.

For hyperbolic `g`, `H` is invertible. Therefore

`K=H^{-1}` iff `KH=I` iff `tau=4`.

With `tau=sigma+2`, this is

`K=H^{-1}` iff `sigma=2`.

Classification: **PROVED IN MANUSCRIPT**.

No hidden arithmetic hypothesis enters this selection.

### B. Period-[1,2] representative

The paper next imposes the positive period-[1,2] normalization

`g_12 = A_1 A_2 = [[3,1],[2,1]]`.

This is not forced by `tau=4` alone; it is an additional normalization choosing one primitive positive integral representative.

Classification: **NORMALIZATION / DEFINITION**.

The manuscript already says "impose" in the main theorem, which is the correct logical wording. Narrative phrases such as "selects this representative" should always be read as selection after the stated period/positivity normalization, not uniqueness from the Cayley condition alone.

Directly,

`det(g_12)=1`, `tr(g_12)=4`,

`chi(X)=X^2-4X+1`,

`Delta=16-4=12`,

and

`H_12 = [[1,1],[2,-1]]`, `H_12^2=3I`.

Classification: **PROVED IN MANUSCRIPT**.

### C. Ramified ideal realization

With

`f_1=2`, `f_2=sqrt(3)-1`,

`p_2=(2,sqrt(3)-1)=(1+sqrt(3))`,

the displayed identities

`sqrt(3) f_1 = f_1 + 2 f_2`,

`sqrt(3) f_2 = f_1 - f_2`

show directly that multiplication by `sqrt(3)` has matrix `H_12` in the `f` basis. Adding `2I` gives multiplication by `2+sqrt(3)` with matrix `g_12`.

Classification: **PROVED IN MANUSCRIPT**.

The equality `(2,sqrt(3)-1)=(1+sqrt(3))` is correct because

`(1+sqrt(3))(sqrt(3)-1)=2`.

The ideal has norm 2 and is the ramified prime above 2 in `Q(sqrt(3))`.

Classification of the ramification statement: **STANDARD IMPORTED FACT**, also directly checkable from discriminant 12.

### D. Pell-Lorentz quadratic form

For

`alpha = m f_1 + n f_2 = (2m-n)+n sqrt(3)`,

`N(alpha) = (2m-n)^2 - 3 n^2 = 2 q_12(m,n)`,

where

`q_12(m,n)=2m^2-2mn-n^2`.

Thus with

`U=2m-n`, `V=sqrt(3)n`,

`2q_12=U^2-V^2`.

Since `N(2+sqrt(3))=1`, multiplication by the Pell unit preserves this norm, and the displayed boost matrix

`[[2,sqrt(3)],[sqrt(3),2]]`

follows directly.

Classification: **PROVED IN MANUSCRIPT**.

No identification with the Paper-A factor coordinates is required for this result; the manuscript correctly keeps the ideal coefficients `(m,n)` separate from factor coordinates `(x,y)`.

### E. Factor-cone realization

Separately define

`X=(x-y)/2`, `T=(x+y)/2`, `Y^2=xy`, `Y=+-sqrt(xy)`.

Then

`T^2-X^2-Y^2=0`.

The factor action

`x' = lambda x`, `y'=lambda^{-1} y`, `lambda=2+sqrt(3)`

preserves `xy`. Writing

`x=sqrt(n)e^s`, `y=sqrt(n)e^{-s}`

gives

`s' = s + log(lambda)`.

Classification: **PROVED IN MANUSCRIPT**.

For a literal 3-dimensional Lorentz action on `(T,X,Y)`, the natural choice is `Y'=Y` on each cone side. The current source specifies the factor action and invariance of `Y^2`, which is sufficient for the stated shell result, but an explicit `Y'=Y` sentence would remove any ambiguity about the signed two-sided lift.

### F. Tangency and null eigenrays

Rows and columns are

`x=u => Y^2=u^2-2uX`,

`y=u => Y^2=u^2+2uX`.

A fixed-`T` cone slice is

`X^2+Y^2=T^2`.

At the parabola vertices `Y=0`, `X=+-u/2`, tangency occurs at `T=u/2`, hence

`(T,X)=(u/2,+-u/2)`.

The `(T,X)` Pell boost has null eigendirections `X=+-T`, so these tangent endpoints lie exactly on the null eigenrays.

Classification: **PROVED IN MANUSCRIPT**.

The emphasized `u=5,6,7` figure is illustrative only and correctly not used as proof.

### G. Mod-12 unit shell

`U(12)={1,5,7,11} ~= V_4`.

For each label `r`, the factor pairs `(r,1)` and `(1,r)` give

`T=(r+1)/2`, `X=+-(r-1)/2`, `Y=+-sqrt(r)`.

Classification of coordinate placement: **PROVED IN MANUSCRIPT**.

The identification

`Gal(Q(zeta_12)/Q) ~= U(12)`

with `T_r(zeta_12)=zeta_12^r` is a **STANDARD IMPORTED FACT**.

The manuscript correctly states that geometric placement of the four labels does not itself define multiplication in `U(12)`.

### H. Cyclotomic completion

Let

`K_12=Q(zeta_12)=Q(sqrt(3),i)`,

`zeta_12=(sqrt(3)+i)/2`.

Since `H_12` acts as multiplication by `sqrt(3)`,

`Zcal=(H_12+iI)/2`

acts as multiplication by `zeta_12` after scalar extension to the cyclotomic carrier.

Classification: **PROVED IN MANUSCRIPT**, once the carrier extension is understood.

The integral carrier

`P_2=p_2 O_K`

and the basis

`{alpha, alpha zeta, alpha zeta^2, alpha zeta^3}`, `alpha=1+sqrt(3)`,

make multiplication by `zeta` integral. The displayed companion matrix follows from `Phi_12(X)=X^4-X^2+1`.

Classification: **PROVED IN MANUSCRIPT**.

`O_K=Z[zeta_12]` and

`[O_K:Z[sqrt(3),i]]=4`,

with discriminants 144 and 2304 respectively, are correct standard cyclotomic/integral-closure facts.

Classification: **STANDARD IMPORTED FACT**, with numerical consistency check `2304/144=16=4^2`.

### I. The residue field `F_4`

The statement

`O_K/P_2 ~= F_4`

is correct. It admits a direct proof that should preferably be inserted in the next source revision:

Because `2 in p_2`, the quotient has characteristic 2. Also `1+sqrt(3)=0` in the quotient, so `sqrt(3)=1`. Using

`sqrt(3)=zeta+zeta^{-1}`

gives

`zeta+zeta^{-1}=1`, hence

`zeta^2+zeta+1=0`.

Therefore

`O_K/P_2 ~= F_2[zeta]/(zeta^2+zeta+1) ~= F_4`,

since `X^2+X+1` is irreducible over `F_2`.

Classification: **CORRECT; currently treated as STANDARD IMPORTED FACT, but DIRECT PROOF AVAILABLE and recommended**.

This direct computation simultaneously shows that the reduced `zeta_12` is a nonzero element `omega` of order 3.

### J. Literal residue multiplication versus transported Pell action

In `O_K/P_2`,

`2=0`, `sqrt(3)=1`, hence

`lambda=2+sqrt(3)=1`.

Thus literal multiplication by the Pell unit is the identity in the cyclotomic residue field.

Classification: **PROVED IN MANUSCRIPT**.

Separately, the coordinate reduction

`gbar_12=[[1,1],[0,1]]`

acts nontrivially on `p_2/2p_2`. Under the additive `F_2`-linear map

`psi(f_1)=1`, `psi(f_2)=omega^2`,

this matrix becomes Frobenius on `F_4`.

Classification: **PROVED IN MANUSCRIPT**.

This is a transported additive action, not ring multiplication. The v0.3.4 carrier guardrail is mathematically essential and correct.

### K. Order-2/order-3 finite symmetry

Multiplication by `omega` has matrix

`[[0,1],[1,1]]`

in basis `(1,omega)` and order 3. Frobenius has order 2 and conjugates multiplication by `omega` to its inverse. Hence they generate

`GL_2(F_2) ~= S_3`.

Classification: **PROVED IN MANUSCRIPT / STANDARD FINITE-FIELD FACT**.

The further identifications

`AGL(1,4) ~= A_4`,

`A Gamma L(1,4) ~= S_4`

are correct standard small-group facts.

Classification: **STANDARD IMPORTED FACT**.

### L. Reduced quadratic parity equals field trace

Modulo 2,

`qbar_12(m,n)=n`.

The field trace on `F_4` obeys

`Tr(1)=0`, `Tr(omega)=Tr(omega^2)=1`.

Under `psi(m f_1+n f_2)=m+n omega^2`,

`Tr = n = qbar_12`.

In the principal/Boolean basis `(omega,omega^2)`, this becomes

`Tr(epsilon_1 omega+epsilon_2 omega^2)=epsilon_1 xor epsilon_2`.

Therefore

`qbar_12 = Tr_{F_4/F_2}`

under the stated additive identification.

Classification: **PROVED IN MANUSCRIPT**.

Publication note: this is one of the principal conclusions in the abstract and conclusion, but it is not formally included in Theorem 2.1. It should be promoted either to item (vii) of the main theorem or to a named corollary.

### M. The n=11 specialization

Geometrically,

`(11,1),(1,11)` lie on `xy=11`, `x+y=12`, giving

`X=+-5`, `Y=+-sqrt(11)`, `T=6`.

Classification: **PROVED IN MANUSCRIPT**.

Arithmetically,

`N(1+2sqrt(3))=-11`,

so `(1+2sqrt(3))` is a prime ideal over 11. Also

`(1+sqrt(3))(1+2sqrt(3))=7+3sqrt(3)`

is totally positive because both real embeddings are positive. Hence

`[p_11]=[p_2]`

in the narrow class group.

Classification: **PROVED IN MANUSCRIPT**.

For `F=Q(sqrt(3))`, ordinary class number is 1 and there is no norm `-1` unit, so the narrow class number is 2. The quadratic extension

`K_12=F(i)=Q(zeta_12)`

is the narrow Hilbert class field. Therefore the nontrivial narrow class has nontrivial Artin image in `Gal(K_12/F)`, and equality of narrow classes gives

`Art(p_11)=Art(p_2)=T_11`.

The identification of `T_11` with complex conjugation follows because `11=-1 mod 12` and `T_11` fixes `sqrt(3)`.

Classification: **STANDARD IMPORTED CLASS-FIELD FACT + CORRECT SPECIALIZATION**.

The manuscript's statement

`T_11 <-> J`

is explicitly only a representation correspondence.

Classification: **STRUCTURAL CORRESPONDENCE**.

Publication note: the n=11 Artin statement is another headline conclusion in the abstract and conclusion but is not part of Theorem 2.1. It should be elevated to a named proposition/corollary if retained as a principal result.

## Main theorem coverage gap

The formal Theorem 2.1 currently ends with item (vi): the `F_4` residue, reduced `zeta` action, transported Frobenius, and generation of `GL_2(F_2)`.

However, the abstract and conclusion additionally present as principal results:

1. `qbar_12 = Tr_{F_4/F_2}` and hence Boolean XOR parity equals field trace.
2. The distinguished `n=11` narrow-class/Artin specialization ending in `T_11` and the companion correspondence `T_11 <-> J`.

Both are supported by subsequent arguments, but neither is formally contained in the main theorem package.

Recommended publication repair:

- add main theorem item **(vii)** for the trace/XOR identity under `psi`;
- add a separate named **Proposition/Corollary (n=11 specialization)** for the narrow-class and Artin statement;
- keep `T_11 <-> J` outside the literal algebraic equality and label it explicitly as representation correspondence, as v0.3.4 already does.

## Terminology guardrails

1. `H_12` is a centered operator. Calling it a "generator" is acceptable only in the project's established centered-generator terminology; it is not an infinitesimal Lie generator by default.
2. The period-[1,2] positive representative is imposed after trace 4 is selected; trace 4 alone does not uniquely determine `g_12`.
3. `p_2/2p_2` and `O_K/P_2` are different rings. `psi` is additive only.
4. Literal multiplication by `lambda` in the cyclotomic residue field is the identity. Frobenius is the transported mod-2 coordinate action.
5. `U(12)`, Boolean translations, factor exchange, `F_4^x`, affine `A_4`, and semilinear `S_4` are distinct layers.
6. The factor-cone realization and ideal-lattice Lorentz realization share the same Pell unit but are separate carriers.
7. No zeta-zero or RH statement follows from the algebraic package.

## Recommended source revision level

The audit does **not** require a conceptual rewrite or a new major version. The core theorem survives.

A narrowly scoped `v0.3.5` would be justified if desired, containing only theorem-hardening changes:

- promote the trace/XOR identity into the theorem package;
- promote the n=11 Artin result to a named proposition/corollary;
- insert the direct `O_K/P_2 ~= F_4` quotient proof;
- explicitly state `Y'=Y` for the signed 3D boost realization;
- optionally replace ambiguous "generator" prose with "centered operator" where no Lie-generator meaning is intended.

Until such a revision is made, v0.3.4 remains mathematically valid as the audited publication baseline, with the above packaging qualifications.

## Final classification of the principal chain

`K=H^{-1} <=> tau=4` — **PROVED**.

`tau=4 -> Delta=12` for the imposed period-[1,2] positive representative — **NORMALIZATION + PROVED DIRECT CALCULATION**.

`g_12 = times (2+sqrt(3)) on p_2` — **PROVED**.

`H_12 = times sqrt(3)` — **PROVED**.

Pell norm / Lorentz boost — **PROVED**.

Factor-cone shell invariance and rapidity translation — **PROVED**.

Parabola-circle tangent endpoints = null boost eigenrays — **PROVED**.

Cyclotomic completion `Zcal=times zeta_12` on `P_2` — **PROVED**.

`O_K/P_2 ~= F_4` — **CORRECT STANDARD FACT; DIRECT PROOF RECOMMENDED**.

Reduced `zeta_12` = order-3 multiplication — **PROVED / STANDARD**.

Transported mod-2 Pell action = Frobenius — **PROVED**.

Literal residue multiplication by `lambda` = identity — **PROVED**.

`qbar_12 = finite-field trace = XOR parity` under `psi` — **PROVED, BUT OUTSIDE FORMAL MAIN THEOREM**.

`n=11 -> [p_11]=[p_2] -> Artin=T_11` — **CORRECT CLASS-FIELD SPECIALIZATION, BUT OUTSIDE FORMAL MAIN THEOREM**.

`T_11 <-> J` — **STRUCTURAL REPRESENTATION CORRESPONDENCE, NOT LITERAL EQUALITY**.

## Status after audit

**Principal v0.3.4: ACTIVE / AUDITED PUBLICATION BASELINE.**

No theorem-breaking defect found.

The next strongest move is theorem hardening (optional v0.3.5) rather than another foundation repair cycle. After that, the project can return to genuinely new mathematics: the divisor-summatory / area-defect structures and the possible V4 intertwiners.