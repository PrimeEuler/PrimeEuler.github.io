# Cone Derivation Ledger v13.224 — V4 Hadamard / Quadratic-Subfield Decomposition

Date: 2026-09-04
Status: EXACT RESEARCH RESULT — downstream of v13.223; not yet promoted into the principal paper

## 1. Parent-directory inspection

The parent `unified/` directory was inspected before deriving anything new, because it contains many legacy companion notes. No separate parent-level note devoted to the divisor-summatory / mod-12 Dirichlet-character decomposition was found. In particular, `All_Four_Means_Note.tex` and `Whole_Family_Note.tex` concern Pythagorean/power means rather than divisor characters.

The closest mathematical precursors are already inside the authoritative project scope:

- v13.171, `Fractional_Gnomons`, which proves the exact gnomon/Cone identity `g_n(u)=2X_u`;
- v13.172, `Continuous_Resolution_Modular_Refinement`, which introduces the exact phase `{2mX_u}`;
- v13.173, `Continuous_Resolution_Jump_Spectrum`, which solves the resolution jump locations exactly; and
- `research-notes/Divisor_Summatory_V4_Mod12_Findings.md`, which first identifies the `chi_12`-twisted divisor sum with the ideal-counting coefficients of `zeta(s)L(s,chi_12)`.

The active derivation below stays inside `unified/discriminant-12-return/`; parent-level files remain read-only provenance.

## 2. The V4 character table is the Hadamard transform

Order the unit classes modulo 12 as

\[
U(12)=\{1,5,7,11\}.
\]

The four real Dirichlet characters restricted to these units are

\[
\chi_0=(1,1,1,1),
\]
\[
\chi_{-4}=(1,1,-1,-1),
\]
\[
\chi_{-3}=(1,-1,1,-1),
\]
\[
\chi_{12}=\chi_{-4}\chi_{-3}=(1,-1,-1,1).
\]

Thus the character table is exactly

\[
\boxed{
H_4=
\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix}.}
\]

Direct multiplication gives

\[
\boxed{H_4^2=4I.}
\]

Therefore for any vector of data attached to the four unit classes,

\[
C=(C_1,C_5,C_7,C_{11})^T,
\]

the exact finite Fourier transform on `V4` is

\[
\boxed{\widehat C=H_4C,\qquad C=\frac14H_4\widehat C.}
\]

This is not an analogy: it is the character Fourier transform of the finite abelian group `U(12) ~= V4`.

## 3. Unit-residue divisor and fractional-part channels

Define the four floor channels

\[
S_r(n):=
\sum_{\substack{k\le n\\k\equiv r\pmod{12}}}
\left\lfloor\frac nk\right\rfloor,
\qquad r\in\{1,5,7,11\},
\]

and the four fractional-part channels

\[
F_r(n):=
\sum_{\substack{k\le n\\k\equiv r\pmod{12}}}
\left\{\frac nk\right\}.
\]

Also define the reciprocal channels

\[
R_r(n):=
\sum_{\substack{k\le n\\k\equiv r\pmod{12}}}\frac1k.
\]

For every channel separately,

\[
\boxed{F_r(n)=nR_r(n)-S_r(n).}
\]

Applying `H_4` gives, for every character `chi`,

\[
\boxed{
\widehat F_\chi(n)
=n\widehat R_\chi(n)-\widehat S_\chi(n),}
\]

where explicitly

\[
\widehat S_\chi(n)
=\sum_{k\le n}\chi(k)\left\lfloor\frac nk\right\rfloor,
\]

\[
\widehat F_\chi(n)
=\sum_{k\le n}\chi(k)\left\{\frac nk\right\},
\]

and the character is extended by zero to integers not coprime to 12.

Thus the four-character transform diagonalizes the unit-residue weighting exactly.

## 4. Dirichlet convolution and the four transformed floor channels

For any Dirichlet character `chi` modulo 12,

\[
\widehat S_\chi(n)
=\sum_{k\le n}\chi(k)\left\lfloor\frac nk\right\rfloor.
\]

Expand the floor as a count of multiples:

\[
\left\lfloor\frac nk\right\rfloor
=\sum_{j\ge1,\,kj\le n}1.
\]

Hence

\[
\widehat S_\chi(n)
=\sum_{kj\le n}\chi(k)
=\sum_{m\le n}\sum_{k\mid m}\chi(k).
\]

Define

\[
a_\chi(m):=\sum_{d\mid m}\chi(d)=(1*\chi)(m).
\]

Then exactly

\[
\boxed{
\widehat S_\chi(n)=\sum_{m\le n}a_\chi(m).}
\]

The Dirichlet series is therefore

\[
\boxed{
\sum_{m\ge1}\frac{a_\chi(m)}{m^s}
=\zeta(s)L(s,\chi).}
\]

This proves that the four Hadamard components have standard arithmetic meanings rather than being merely four numerical linear combinations.

## 5. The three nontrivial channels are the three quadratic subfields of K_12

The three nonprincipal quadratic characters correspond to the three quadratic fields

\[
\chi_{-4}\longleftrightarrow \Q(i),
\]
\[
\chi_{-3}\longleftrightarrow \Q(\sqrt{-3}),
\]
\[
\chi_{12}\longleftrightarrow \Q(\sqrt3).
\]

For a quadratic field of fundamental discriminant `D`, the Dedekind zeta factors as

\[
\zeta_{\Q(\sqrt D)}(s)=\zeta(s)L(s,\chi_D).
\]

Consequently

\[
\boxed{
\sum_{m\ge1}\frac{a_{-4}(m)}{m^s}
=\zeta_{\Q(i)}(s),}
\]

\[
\boxed{
\sum_{m\ge1}\frac{a_{-3}(m)}{m^s}
=\zeta_{\Q(\sqrt{-3})}(s),}
\]

\[
\boxed{
\sum_{m\ge1}\frac{a_{12}(m)}{m^s}
=\zeta_{\Q(\sqrt3)}(s).}
\]

But

\[
K_{12}=\Q(\zeta_{12})=\Q(i,\sqrt3)
\]

is biquadratic, and its three quadratic subfields are precisely

\[
\boxed{
\Q(i),\quad \Q(\sqrt{-3}),\quad \Q(\sqrt3).}
\]

Therefore:

**[D] V4 quadratic-subfield decomposition.** The three nontrivial Fourier components of the unit-residue divisor floor data are exactly the ideal-counting summatory functions attached to the three quadratic subfields of the cyclotomic field `Q(zeta_12)`.

This upgrades the earlier isolated `chi_12` observation to a complete four-character picture.

## 6. The principal channel is different

The principal character modulo 12 is

\[
\chi_0(k)=1\quad\text{if }(k,12)=1,
\qquad 0\quad\text{otherwise}.
\]

Its L-function is

\[
L(s,\chi_0)
=\zeta(s)(1-2^{-s})(1-3^{-s}),
\]

so

\[
\boxed{
\zeta(s)L(s,\chi_0)
=\zeta(s)^2(1-2^{-s})(1-3^{-s}).}
\]

Thus the principal Hadamard component is the divisor channel filtered to unit denominators modulo 12. It is not the ordinary divisor summatory function `D(n)`, and it is not another quadratic-field Dedekind zeta.

This distinction is essential because the Hadamard transform acts only on the four unit residue classes; denominators divisible by 2 or 3 lie outside that four-state carrier.

## 7. Exact n=11 transform

At `n=11`, the only unit-class denominators are

\[
k=1,5,7,11.
\]

The raw floor-channel vector is

\[
\boxed{S(11)=(11,2,1,1)^T.}
\]

The raw fractional-part vector is

\[
\boxed{
F(11)=\left(0,\frac15,\frac47,0\right)^T.}
\]

The reciprocal vector is

\[
\boxed{
R(11)=\left(1,\frac15,\frac17,\frac1{11}\right)^T.}
\]

Applying the Hadamard transform gives

\[
\boxed{
\widehat S(11)=(15,11,9,9)^T,}
\]

in the character order

\[
(\chi_0,\chi_{-4},\chi_{-3},\chi_{12}).
\]

For the fractional parts,

\[
\boxed{
\widehat F(11)
=\left(\frac{27}{35},-\frac{13}{35},\frac{13}{35},-\frac{27}{35}\right)^T.}
\]

For the reciprocal channels,

\[
\boxed{
\widehat R(11)
=\left(\frac{552}{385},\frac{372}{385},\frac{328}{385},\frac{288}{385}\right)^T.}
\]

Direct exact arithmetic verifies componentwise

\[
\boxed{
\widehat F(11)=11\widehat R(11)-\widehat S(11).}
\]

Two symmetries are visible:

\[
\widehat S_{-3}(11)=\widehat S_{12}(11)=9,
\]

and

\[
\widehat F_{-4}(11)=-\widehat F_{-3}(11),
\qquad
\widehat F_{12}(11)=-\widehat F_0(11).
\]

These equalities are exact at `n=11`, but at this checkpoint they are only finite-shell identities. They are not yet promoted as an exceptional arithmetic law of 11.

## 8. How this interfaces with the principal discriminant-12 theorem

The principal v0.3.5 paper singles out the real quadratic field

\[
F=\Q(\sqrt3)
\]

through the trace-4 Pell return and the discriminant-12 character. In the complete V4 Fourier decomposition above, that same arithmetic branch is exactly the `chi_12` component:

\[
\boxed{
\widehat S_{\chi_{12}}
\leftrightarrow
\zeta_{\Q(\sqrt3)}(s).}
\]

The other two nontrivial components are not noise; they are the two other quadratic subfields already contained in the same cyclotomic closure `K_12`.

Thus the four Cone labels have a rigorous dual arithmetic basis:

- group-element basis: residue labels `1,5,7,11`;
- character/Fourier basis: `chi_0, chi_{-4}, chi_{-3}, chi_12`;
- three nonprincipal channels: the three quadratic subfields of `Q(zeta_12)`.

This is presently the cleanest exact arithmetic interpretation of the four-state mod-12 shell.

## 9. Relation to the older modular-resolution ledgers

The v13.171--v13.173 results and the present V4 transform are compatible but distinct.

The older exact resolution phase is

\[
\phi_m(u)=\{2mX_u\},
\]

which describes where a particular gnomon crossing lies inside a mesh cell.

The present Hadamard transform is

\[
\widehat C(\chi)=\sum_{r\in U(12)}\chi(r)C_r,
\]

which is Fourier analysis on the finite group of unit residue classes.

**[Audit]** Do not identify `{2mX_u}` with a Dirichlet character, and do not infer the V4 multiplication law from geometric adjacency in the Cone figure. One construction is resolution phase on gnomon geometry; the other is character duality on `U(12)`.

## 10. Theorem status and next test

Exact and ready for independent audit:

1. `H_4` is the V4 character table and satisfies `H_4^2=4I`.
2. Unit-residue floor/fractional/reciprocal vectors transform exactly by `H_4`.
3. Every transformed floor channel has coefficients `1*chi` and Dirichlet series `zeta(s)L(s,chi)`.
4. The three nonprincipal channels are exactly the Dedekind-zeta channels of the three quadratic subfields of `Q(zeta_12)`.
5. The `chi_12` channel is precisely the real-quadratic `Q(sqrt(3))` channel selected independently by the principal discriminant-12 theorem.
6. The displayed `n=11` vectors and transformed values are exact.

Still open:

- whether the exact `n=11` component equalities above characterize 11 in any useful family;
- whether there is a direct ramified-ideal-coordinate formula for the `chi_12` summatory coefficients;
- how, if at all, the V4 character transform interacts with the continuous-resolution phase spectrum beyond sharing the same underlying Cone crossings;
- whether the A161664 complement `A_n=T_n-D(n)` has a natural four-character decomposition once the non-unit denominator channels are handled correctly.

Decision: keep this as a research theorem checkpoint. Do not modify the audited principal v0.3.5 source yet.