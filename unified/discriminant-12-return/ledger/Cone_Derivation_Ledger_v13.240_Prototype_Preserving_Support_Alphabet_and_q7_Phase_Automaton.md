# Cone Derivation Ledger v13.240 — Prototype-Preserving Support Alphabet and q=7 Phase Automaton

Date: 2026-09-05
Status: EXACT FINITE OPERATOR CLASSIFICATION — continuation of v13.239; research branch remains open

## 0. Pre-write synchronization

Immediately before this write, the authoritative project README, current `master` tip, v13.236, and v13.239 were re-fetched. The tip remained

`ffd22b2e72b96af42660d6bc15e639ffff3137cb`

with v13.239 as the highest ledger checkpoint. No newer external-audit checkpoint had landed after v13.237. This entry extends the reconciled research branch and does not revise the audited principal v0.3.5 paper.

## 1. Question

v13.239 reduced all currently observed resonant support strata at each of `q=5` and `q=7` to a single decorated-fiber prototype class. The next question was whether this prototype class is preserved under adjoining a genuinely new support prime.

From v13.236, a new prime `p` acts on every crossing signal through the finite label

\[
(r,\sigma)=\bigl(p\bmod q,\chi_D(p)\bigr)
\]

and the exact operator

\[
\boxed{
(T_{r,\sigma}f)(k)
=\sum_{j=0}^{r-1}f(rk+j)-\sigma f(k).
}
\]

For a decorated fiber `\Phi(h)=f_h`, the same operator acts statewise:

\[
\boxed{(T_{r,\sigma}\Phi)(h)=T_{r,\sigma}(\Phi(h)).}
\]

Because `T_{r,\sigma}` acts on the block coordinate `k` and not on the cofactor label `h`, it commutes with multiplicative cofactor relabelling and with global sign. Therefore preservation of one prototype representative implies preservation of its entire equivalence class.

## 2. Exact finite audit method

For each prototype and every possible local label

\[
r\in\mathbf F_q^\times,\qquad \sigma\in\{\pm1\},
\]

apply `T_{r,\sigma}` to all `q-1` prototype cofactor states and test whether there exist

\[
u\in\mathbf F_q^\times,\qquad \delta\in\{\pm1\}
\]

such that

\[
\boxed{
T_{r,\sigma}\Phi(h)=\delta\Phi(uh)
\quad\text{for every }h.
}
\]

This is an exhaustive finite operator-alphabet calculation: 8 labels for `q=5` and 12 labels for `q=7`.

The calculation was independently checked by constructing actual enlarged support fibers from representative primes carrying every realizable `(r,\sigma)` label and comparing the full decorated fibers. The direct support construction and the `T_{r,\sigma}` calculation agree.

## 3. q=5 classification

Use the v13.239 prototype

\[
(D,S,q)=(8,\varnothing,5).
\]

All eight possible labels

\[
(r,\sigma),\qquad r=1,2,3,4,\quad \sigma=\pm1,
\]

were tested.

The result is

\[
\boxed{
\text{No single genuinely new support-prime label preserves the q=5 prototype class.}
}
\]

Equivalently, for every `(r,\sigma)` there are no `u,\delta` satisfying

\[
T_{r,\sigma}\Phi_5(h)=\delta\Phi_5(uh)
\quad\forall h\in\mathbf F_5^\times.
\]

This is important: the q=5 one-prototype collapse of v13.239 does **not** arise from closure of the basic `D=8` prototype under arbitrary one-prime support adjunction. The other observed q=5 prototype-equivalent strata involve different primitive discriminants, not a support-growth orbit of this fixed primitive character.

## 4. q=7 classification

Use the original discriminant-12-adjacent prototype

\[
\Phi_*:=\Phi_{-8,\{3\},7}.
\]

All twelve labels

\[
(r,\sigma),\qquad r=1,2,3,4,5,6,\quad\sigma=\pm1
\]

were tested.

Exactly four preserve the prototype class:

\[
\boxed{
\mathcal A_7^{\rm pres}
=
\{(2,-1),(3,-1),(4,-1),(5,-1)\}.
}
\]

Thus the exact criterion is

\[
\boxed{
T_{r,\sigma}\Phi_*\sim\Phi_*
\iff
\sigma=-1\text{ and }r\not\equiv\pm1\pmod7.
}
\]

All labels with `\sigma=+1` fail, and the two inert labels with `r=\pm1` also fail.

For the primitive character `\chi_{-8}`, this says that a new support prime preserves the q=7 prototype precisely when

\[
\boxed{
\chi_{-8}(p)=-1,
\qquad
p\bmod7\in\{2,3,4,5\}.
}
\]

## 5. Exact induced cofactor phase

For each preserving label, the enlarged fiber is not merely equivalent abstractly; its cofactor phase is explicit.

The finite audit gives

\[
\begin{array}{c|c|c}
r&u&\delta\\
\hline
2&\pm3&-1\\
3&\pm2&-1\\
4&\pm2&-1\\
5&\pm3&-1
\end{array}
\]

where the `\pm` ambiguity is exactly the q=7 cofactor reflection

\[
\Phi_*(-h)=\Phi_*(h).
\]

Equivalently, projectively,

\[
\boxed{
u\equiv\pm r^{-1}\pmod7,
\qquad \delta=-1.
}
\]

Therefore every preserving new-support transition obeys

\[
\boxed{
T_{r,-1}\Phi_*(h)
=-\Phi_*(r^{-1}h)
}
\]

up to the harmless replacement `r^{-1}\mapsto-r^{-1}` caused by `\Phi_*(-h)=\Phi_*(h)`.

This formula was checked against all six cofactor states for all four preserving labels.

## 6. Transport of the resonance pair

The prototype resonance pair is

\[
\mathcal R_*=\{\pm1\}.
\]

If

\[
\Phi'(h)=-\Phi_*(r^{-1}h),
\]

then

\[
r^{-1}h=\pm1
\iff
h=\pm r.
\]

Hence a preserving support adjunction transports the resonance pair by the remarkably simple rule

\[
\boxed{
\mathcal R_*\longmapsto\{\pm r\}.
}
\]

Example: adjoining `p=5` has

\[
r=5,\qquad\chi_{-8}(5)=-1,
\]

so the new support stratum has resonance pair

\[
\{\pm5\}=\{2,5\},
\]

exactly reproducing the `24\to120\to240` calculation of v13.238/v13.239.

## 7. Closure under repeated preserving adjunctions

Suppose a decorated fiber already has prototype form

\[
\Phi(h)=\delta_0\Phi_*(u_0h).
\]

Because `T_{r,\sigma}` acts only on `k`,

\[
T_{r,-1}\Phi(h)
=\delta_0T_{r,-1}\Phi_*(u_0h)
=-\delta_0\Phi_*(r^{-1}u_0h).
\]

Therefore the prototype-preserving sector is closed under any sequence of preserving labels. The phase update is

\[
\boxed{
(u,\delta)\longmapsto(r^{-1}u,-\delta),
}
\]

with `u` understood modulo the reflection `u\sim-u`.

For a sequence `r_1,\dots,r_m` of preserving residues,

\[
\boxed{
u_m\equiv(r_1r_2\cdots r_m)^{-1}u_0\pmod{\pm1},
}
\]

and

\[
\boxed{
\delta_m=(-1)^m\delta_0.
}
\]

The resonance pair after the sequence is therefore

\[
\boxed{
\mathcal R_m
=u_m^{-1}\{\pm1\}.
}
\]

Starting from `u_0=1`, this is simply

\[
\boxed{
\mathcal R_m=\{\pm r_1r_2\cdots r_m\}.
}
\]

## 8. The genuine finite q=7 phase automaton

Because q=7 reflection identifies `u` with `-u`, the multiplicative phase coordinate lies in

\[
\mathbf F_7^\times/\{\pm1\},
\]

a cyclic group of order 3. Keeping the independent global sign gives

\[
\boxed{
\left(\mathbf F_7^\times/\{\pm1\}\right)\times C_2
\cong C_3\times C_2
\cong C_6.
}
\]

The two projective transition types are

\[
r=2,5:\quad [u]\mapsto[3u],\quad\delta\mapsto-\delta,
\]

and

\[
r=3,4:\quad [u]\mapsto[2u],\quad\delta\mapsto-\delta.
\]

Since `[2]` and `[3]=[2]^{-1}` generate the order-3 projective phase group, the preserving transition alphabet generates all six signed phase states.

Thus, unlike the globally unbounded support graph corrected in v13.238, the q=7 **prototype-preserving quotient sector** really does carry a finite phase automaton:

\[
\boxed{
\text{q=7 prototype-preserving support dynamics}
\longrightarrow C_6\text{ signed phase quotient.}
}
\]

This is a quotient of decorated fibers, not a claim that the underlying support sets or carrier integers form a finite set.

## 9. Arithmetic interpretation of the preserving alphabet

For `D=-8`, the sign condition

\[
\chi_{-8}(p)=-1
\]

selects primes inert in `\mathbf Q(\sqrt{-2})`. The residue condition

\[
p\not\equiv\pm1\pmod7
\]

removes the two trivial projective directions in `\mathbf F_7^\times`.

Therefore the q=7 preserving alphabet is the intersection of:

1. the inert half of the `\chi_{-8}` quadratic splitting law; and
2. the four nontrivial/nonreflection residues modulo 7.

Because the conductor 8 and modulus 7 are coprime, CRT makes these local conditions independent. They define explicit residue classes modulo 56. No density theorem is needed for the finite operator result itself.

## 10. What fails outside the preserving alphabet

For the remaining eight q=7 labels, `T_{r,\sigma}\Phi_*` is not equivalent to `\Phi_*` under any allowed cofactor multiplication and global sign.

Thus a nonpreserving new support prime exits the one-prototype quotient sector immediately. Later support adjunctions may in principle return to it, but that is a different reachability problem and is **not** implied by this classification.

Similarly, q=5 has no one-step preserving label from its basic prototype. Therefore no analogous nontrivial one-state support-growth automaton is obtained there from this calculation.

## 11. Guardrails

1. The classification is exact for the two explicit prototypes of v13.239 and the complete finite local alphabets at q=5 and q=7.
2. The q=7 closure theorem applies to repeated adjunctions whose every local label lies in `\mathcal A_7^{pres}`.
3. It does not classify histories that leave the prototype class and later return.
4. The `C_6` object is a finite quotient of the signed cofactor phase inside the prototype-preserving sector; the global support graph remains unbounded.
5. The sign `\chi_{-8}(p)` is a quadratic splitting label, while `p mod 7` is a separate additive/cyclic residue label. Their combination is via CRT, not identification of the two structures.
6. No physical dynamical system, Hamiltonian, or energy spectrum is asserted by the word automaton.
7. The audited principal v0.3.5 theorem package is unchanged.

## 12. Next task

The next exact problem is to classify **return words**: finite sequences of local support labels that begin in the q=7 prototype class, leave it through a nonpreserving label, and later re-enter it.

Because v13.236 supplies a finite operator alphabet on `F_7` signals, this can be attacked by computing the orbit of the prototype decorated fiber under the twelve `T_{r,\sigma}` operators, quotienting at every step by cofactor rephasing and global sign. The key question is whether the full operator orbit of the prototype is finite or infinite in amplitude.

This is the appropriate next test for whether the finite `C_6` preserving sector sits inside a larger finite quotient graph or inside an infinite operator orbit.