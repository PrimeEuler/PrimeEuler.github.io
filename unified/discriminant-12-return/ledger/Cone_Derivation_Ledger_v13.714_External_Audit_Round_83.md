# Cone Derivation Ledger v13.714 — External Audit Round 83

Date: 2026-09-23

Auditor: independent external reviewer, verifying by direct hand re-derivation and numeric confirmation.

Scope: v13.713 (centered Xi/Zeta cone and complete V4 character correspondence) — a new, self-contained analytic-number-theory lane connecting the classical completed zeta function `\xi(s)` directly to the cone's logarithmic-torus `C_2\times C_2` character structure (v13.703, audited Round 80), independent of the Suzuki operator apparatus.

## 0. Collision/relevance check

`git fetch origin master` immediately before writing this entry shows HEAD at `2cc73e9` (v13.713), no intervening commits. Highest ledger version is v13.713; this entry claims v13.714 / Round 83.

## 1. Dirichlet-atom null-cone lift and the pairwise-cancellation identity: independently verified exactly

The construction `p_n=n^{-s/2},q_n=n^{-\bar s/2}` giving `T_n=n^{-\sigma}\cos(t\log n)`, `X_n=-in^{-\sigma}\sin(t\log n)`, `Y_n=n^{-\sigma}` and the null identity `T_n^2-X_n^2-Y_n^2=0` were independently re-derived from scratch (expanding `n^{-s}=n^{-\sigma}(\cos(t\log n)-i\sin(t\log n))` and its conjugate) and confirmed exact.

The entry's most substantive computation — the partial-sum "distance from the null cone" identity
\[
(H_N^{(\sigma)})^2-|Z_N(s)|^2=4\sum_{m<n\le N}(mn)^{-\sigma}\sin^2\!\left(\frac t2\log\frac nm\right)
\]
— was independently re-derived in full by this audit: expanding `(H_N^{(\sigma)})^2` and `|Z_N(s)|^2` as double sums, isolating the cross terms `n^{-s}m^{-\bar s}+m^{-s}n^{-\bar s}=2(mn)^{-\sigma}\cos(t\log(n/m))` for `m\ne n`, and applying `1-\cos x=2\sin^2(x/2)` gives exactly the claimed formula. This audit additionally confirmed it numerically at four independent `(N,\sigma,t)` parameter sets, agreeing with the direct evaluation of `|Z_N(s)|^2` and `(H_N^{(\sigma)})^2` to machine precision (`\le3\times10^{-15}`). This is a genuinely elegant and exact reformulation of the trivial triangle-inequality bound `|Z_N(s)|\le H_N^{(\sigma)}` as a precise "cone lightcone deficit," correctly scoped in the entry's own guardrail (§4) to the absolutely-convergent region `\Re s>1`, with an explicit warning against naive substitution on the critical strip. **PASS, exact.**

## 2. Centered functional-equation coordinate and the V4 action on Xi: independently verified exactly

The centering `\widehat\tau_n=-(\sigma-\tfrac12)r_n`, its transformation `(\widehat\tau,\ell)\mapsto(-\widehat\tau,-\ell)` under `s\mapsto1-s`, and the removal of the affine `r_n`-term in the uncentered coordinate were independently re-derived componentwise (via `\Re(w)`, `\Im(w)` for `w=s-\tfrac12`, not merely via the sum `\widehat\tau+\ell`) and confirmed exact.

The `V_4=\langle C,D\rangle` action on `\Xi(w)=\xi(\tfrac12+w)` was independently checked from the two standard classical facts `\xi(s)=\xi(1-s)` and `\xi(\bar s)=\overline{\xi(s)}`: `\Xi(-w)=\Xi(w)` and `\Xi(\bar w)=\overline{\Xi(w)}` both confirmed by direct substitution, and the resulting coordinate actions `C:(\widehat\tau,\ell)\mapsto(\widehat\tau,-\ell)`, `D:(\widehat\tau,\ell)\mapsto(-\widehat\tau,\ell)`, `R:(\widehat\tau,\ell)\mapsto(-\widehat\tau,-\ell)` were independently confirmed via direct real/imaginary-part tracking of `w\mapsto\bar w`, `w\mapsto-\bar w`, `w\mapsto-w`. `C^2=D^2=\mathrm{id}`, `CD=DC` confirmed directly, giving the genuine Klein four-group `V_4^{(\xi)}\cong C_2\times C_2`. **PASS, exact.**

## 3. Full four-character table for log-Xi: independently rebuilt from the classical functional equation, PASS

This is the entry's central claim and was checked most carefully. Independently re-derived `L(1-s)=-L(s)` (differentiating `\xi(s)=\xi(1-s)`) and `L(\bar s)=\overline{L(s)}` (standard reality), then independently rebuilt the full `2\times2` character table for `A=\Re L,B=\Im L` under `C,D` from these two facts alone — matching the entry's printed table exactly (`A:(C,D)=(+,-)`, `B:(C,D)=(-,+)`).

For the even sector (`\log|\xi|,\arg\xi`), this audit independently verified a subtlety the entry states but does not fully spell out: because `\Xi` is *even* (`\Xi(-w)=\Xi(w)`), the map `D=R\circ C` (since `R:w\mapsto-w` acts trivially on `G=\log\Xi` by evenness) means `D` acts on `G=U+iV` *identically* to how `C` acts on it — independently confirmed via `G(D(w))=G(-\bar w)=G(\bar w)` (using evenness to drop the sign) `=\overline{G(w)}`, the same as `G(C(w))`. This correctly explains, rather than merely asserts, why the table shows `\log|\xi|:(C,D)=(+,+)` and `\arg\xi:(C,D)=(-,-)` (both entries D-agreeing with their C-entries), populating all four `V_4` character slots exactly once across the four quantities `\{\log|\xi|,\Re L,\Im L,\arg\xi\}`. **PASS, exact — no character slot is missing or duplicated incorrectly.**

## 4. Cross-lane character correspondence with the cone table: internally consistent, appropriately hedged, PASS

Checked the claimed correspondence `\Re\tau\leftrightarrow\log|\xi|`, `\Im\tau\leftrightarrow\Re(\xi'/\xi)`, `\Re\ell\leftrightarrow\Im(\xi'/\xi)`, `\Im\ell\leftrightarrow\arg\xi` against this audit's own independently-verified Round 80 cone table (`\Re\tau,\Im\tau,\Re\ell,\Im\ell` have `(F,C_{\rm cone})=(+,+),(+,-),(-,+),(-,-)` respectively) and the freshly-rebuilt `\xi`-side table above: the identification uses a single, consistent labeling convention (cone-`F`↔`\xi`-`C`, cone-`C_{\rm cone}`↔`\xi`-`D`) applied uniformly across all four rows, not a cherry-picked match — confirmed by checking each row independently rather than trusting the stated pattern. The entry's guardrail (§9, §12, §14) that this is a **representation-theoretic character match**, not a literal equality, an operator intertwiner, or a determinant identity, is stated repeatedly and precisely, and this audit agrees this is exactly the correct scope for what has actually been shown. **PASS.**

## 5. Second-derivative consistency check: independently verified via group-theoretic argument, PASS

The claim `M=L'` satisfies `M(1-s)=M(s)` (direct differentiation of `L(1-s)=-L(s)`, confirmed) and `M(\bar s)=\overline{M(s)}` (standard reality). The entry then asserts `\Re M\in\chi_{+,+},\Im M\in\chi_{-,-}` — this audit independently derived this by solving the abelian `C_2\times C_2` consistency equation directly: since the combined action `R` (which equals `C\circ D` as a composition) acts as the *identity* on `M`'s value, and `C` acts as conjugation, the action of `D` on `M`'s value must equal the action of `C` (in an abelian group of order 4, `\mathrm{action}(D)=\mathrm{action}(C)\circ\mathrm{action}(R)=\mathrm{action}(C)\circ\mathrm{id}=\mathrm{action}(C)`), giving `\Re M:(C,D)=(+,+)`, `\Im M:(C,D)=(-,-)` exactly as claimed. This is a valid resolution of the third generator's action from two known ones in an abelian group, not an unjustified leap. The entry correctly frames this as a redundancy/consistency check (re-populating the already-covered `(+,+)` and `(-,-)` slots) rather than new information. **PASS.**

## 6. Critical-line fixed locus: independently re-derived, correctly guarded against RH overreach, PASS

Independently verified `1-s=\bar s` on `s=\tfrac12+it` (trivial algebra) and, more substantively, derived `\Re(\xi'/\xi)(\tfrac12+it)=0` cleanly from first principles: combining the universal identity `L(1-s)=-L(s)` with the critical-line identity `1-s=\bar s` gives `L(\bar s)=-L(s)` on the critical line; combined with the universal reality identity `L(\bar s)=\overline{L(s)}`, this forces `\overline{L(s)}=-L(s)`, i.e. `2\Re L(s)=0`, i.e. `\Re L(s)=0` — a clean derivation independent of the entry's own (less explicit) presentation, confirming the claim exactly. `\xi(\tfrac12+it)\in\mathbb R` was independently confirmed the same way (`\xi(s)=\xi(1-s)=\xi(\bar s)=\overline{\xi(s)}`).

Critically, this audit specifically checked whether the entry overreaches into an RH claim at this point, since "`\xi` real and `\Re(\xi'/\xi)=0` on the critical line" is exactly the kind of fact that is easy to mis-state as evidence for the Riemann Hypothesis. It does not: §11's guardrail explicitly and correctly states these are symmetry identities holding identically at every point of the critical line regardless of where the zeros actually lie, and do not imply zeros are confined there. This is the correct statement, and this audit found no place in the entry where this boundary is crossed. **PASS.**

## 7. Assessment of the user's framing versus the entry's own claim

The project owner introduced this round as "the zeta function showing up on the cone directly with the same 4 characters." Having independently verified the mathematics, this audit's assessment is: the underlying result is real, correctly derived, and a genuinely elegant piece of work — the classical completed zeta function's functional equation and reality property generate exactly the same abstract `C_2\times C_2` character structure as the cone's logarithmic torus, verified independently at every step above, including by direct numerical computation of the partial-sum identity.

However, the precise content is narrower than "the zeta function showing up on the cone": what is shown is a **shared abstract symmetry type** between two independently-constructed objects (the cone's `(\mathbb C^\times)^2` torus quotiented by its two involutions, and `\xi`'s classical `V_4=\langle s\mapsto\bar s,\,s\mapsto1-\bar s\rangle` symmetry) — a representation-theoretic coincidence of character tables, not an embedding, operator intertwiner, or determinant identity connecting the two constructions. The entry itself is explicit and consistent about this scope throughout (§1, §9 guardrail, §12, §14), including flagging as still fully open the "major bridge problem" of whether any exact identity connects the Suzuki four-coordinate package to this Xi four-coordinate package. This audit's independent verification supports the entry's own claims exactly as scoped, and no stronger claim is warranted by what has actually been proved.

## 8. Summary

| Section | Claim | Verification | Outcome |
|---|---|---|---|
| §2-3 | Dirichlet-atom null-cone lift; exact pairwise-cancellation identity for partial sums | independent re-derivation + numeric check at 4 parameter sets (agreement to `~1e-15`) | **PASS, exact** |
| §5-6 | Centered coordinate `\widehat\tau`; `V_4=\langle C,D\rangle` action on `\Xi` | independent componentwise re-derivation from `\xi(s)=\xi(1-s)`, `\xi(\bar s)=\overline{\xi(s)}` | **PASS, exact** |
| §7-8 | Full four-character table for `\log\Xi` (`\log|\xi|,\Re L,\Im L,\arg\xi`) | independently rebuilt from scratch, including the D-equals-C-on-even-sector subtlety | **PASS, exact, no slot missing** |
| §9 | Cross-lane correspondence with the cone's `(F,C_{\rm cone})` table | checked row-by-row against this audit's own Round 80 table with one consistent convention | **PASS, correctly hedged as representation-theoretic only** |
| §10 | `M=L'` second-derivative consistency check | independently resolved via abelian-group consistency argument | **PASS** |
| §11 | Critical-line fixed locus (`\widehat\tau=0`, `\Re L=0`, `\xi\in\mathbb R`) | independently re-derived cleanly; RH-overreach guardrail confirmed present and correctly stated | **PASS** |

## 9. Final freshness check

`git fetch origin master` immediately before this commit: HEAD still at `2cc73e9`. No new commits landed while writing this entry. `git ls-tree` confirms v13.714 remains free.
