# Cone Derivation Ledger v13.416 — F4 Reduction, Character Splitting, and Mod-2 Collapse

Date: 2026-09-14

Status labels: **[D]** exact derived, **[I]** interpretation, **[Audit]** limitation/guardrail.

## 0. Synchronization note

Two distinct files were committed concurrently under the label `v13.415` immediately before this checkpoint:

- `Cone_Derivation_Ledger_v13.415_Chi12_Tail_Residue_Profile_and_Time_Orientation.md`;
- `Cone_Derivation_Ledger_v13.415_Suzuki_Mod12_Source_Channel_Audit.md`.

This is a live numbering collision only. Their mathematical contents are separate. To avoid overwriting either thread, this checkpoint is filed as `v13.416`; the duplicate `v13.415` labels should be normalized by the next bookkeeping/audit pass.

## 1. Starting point from the audited principal paper [D]

Let

\[
K_{12}=\mathbf Q(\zeta_{12})=\mathbf Q(\sqrt3,i),
\qquad
\lambda=2+\sqrt3,
\]

and let

\[
\mathfrak P_2=\mathfrak p_2\mathcal O_{K_{12}}.
\]

The audited ramified quotient is

\[
\mathcal O_{K_{12}}/\mathfrak P_2\cong\mathbf F_4,
\]

with

\[
\omega=\bar\zeta_{12},
\qquad
\omega^2+\omega+1=0,
\qquad
\omega^3=1.
\]

Also, in this quotient,

\[
2=0,
\qquad
\sqrt3=1,
\qquad
\boxed{\lambda=2+\sqrt3\equiv1.}
\]

Thus literal residue multiplication by the Pell unit is the identity.

Separately, in the ramified-ideal coefficient basis

\[
f_1=2,
\qquad
f_2=\sqrt3-1,
\]

the mod-2 coordinate reduction of

\[
g_{12}=\begin{pmatrix}3&1\\2&1\end{pmatrix}
\]

is

\[
\bar g_{12}
=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\]

and after the audited additive identification with \(\mathbf F_4\), this transported linear action is Frobenius.

## 2. Cyclotomic Galois action on the residue field is the \(\chi_{-3}\) quotient [D]

For

\[
r\in U(12)=\{1,5,7,11\},
\qquad
\sigma_r(\zeta_{12})=\zeta_{12}^{r},
\]

reduction modulo \(\mathfrak P_2\) gives

\[
\sigma_r(\omega)=\omega^r.
\]

Since \(\omega\) has order \(3\), only \(r\bmod3\) remains:

\[
\sigma_r(\omega)=
\begin{cases}
\omega,&r\equiv1\pmod3,\\
\omega^2,&r\equiv-1\pmod3.
\end{cases}
\]

On the four unit classes,

\[
\begin{array}{c|cccc}
r&1&5&7&11\\
\hline
r\bmod3&+1&-1&+1&-1
\end{array}
\]

which is exactly the real character \(\chi_{-3}\). Therefore

\[
\boxed{
U(12)\xrightarrow{\text{residue-field action}}
\operatorname{Gal}(\mathbf F_4/\mathbf F_2)\cong C_2
}
\]

is the quotient

\[
\boxed{r\longmapsto\chi_{-3}(r).}
\]

Equivalently,

\[
\sigma_r|_{\mathbf F_4}
=
\begin{cases}
\mathrm{id},&\chi_{-3}(r)=+1,\\
\mathrm{Fr},&\chi_{-3}(r)=-1,
\end{cases}
\]

where \(\mathrm{Fr}(z)=z^2\).

## 3. Pell time orientation is a different quotient: \(\chi_{12}\) [D]

From `v13.414`,

\[
\boxed{
\sigma_r(\lambda)=\lambda^{\chi_{12}(r)}.
}
\]

Thus Pell time orientation is

\[
\boxed{r\longmapsto\chi_{12}(r),}
\]

with

\[
\chi_{12}(1)=\chi_{12}(11)=+1,
\qquad
\chi_{12}(5)=\chi_{12}(7)=-1.
\]

This differs from the residue-field quotient:

\[
\chi_{-3}(1)=\chi_{-3}(7)=+1,
\qquad
\chi_{-3}(5)=\chi_{-3}(11)=-1.
\]

Therefore the \(\chi_{12}\) Pell-time quotient does **not** survive as the Galois quotient of the ramified \(\mathbf F_4\) residue field.

The reason is exact and simple:

\[
\lambda\equiv1\pmod{\mathfrak P_2},
\]

so literal forward/backward multiplication by \(\lambda^{\pm1}\) collapses to the same identity element.

## 4. The third real character records the \(i\)-orientation [D]

For \(i=\zeta_{12}^3\),

\[
\sigma_r(i)=i^r.
\]

Hence

\[
\sigma_r(i)=
\begin{cases}
+i,&r\equiv1\pmod4,\\
-i,&r\equiv-1\pmod4.
\end{cases}
\]

This is exactly \(\chi_{-4}(r)\). Therefore

\[
\boxed{
\sigma_r(i)=\chi_{-4}(r)i.
}
\]

Likewise,

\[
\sqrt3=\zeta_{12}+\zeta_{12}^{-1}
\]

transforms by

\[
\boxed{
\sigma_r(\sqrt3)=\chi_{12}(r)\sqrt3.
}
\]

The three nontrivial real characters therefore have three clean roles:

\[
\boxed{
\begin{aligned}
\chi_{-4}&:\ \text{sign of }i,\\
\chi_{-3}&:\ \text{F4 residue-field identity/Frobenius action},\\
\chi_{12}&:\ \text{sign of }\sqrt3\text{ and Pell time orientation}.
\end{aligned}}
\]

They satisfy the familiar exact relation

\[
\boxed{\chi_{12}=\chi_{-4}\chi_{-3}.}
\]

Thus the V4 character table is not merely decorative here: its three nontrivial characters resolve three distinct but compatible involutive projections of the cyclotomic structure.

## 5. Integral Pell return and real conjugation collapse to the same mod-2 additive involution [D]

In the ramified basis \((f_1,f_2)\), real quadratic conjugation is

\[
J_f=
\begin{pmatrix}
1&-1\\
0&-1
\end{pmatrix},
\]

with

\[
J_f^2=I,
\qquad
J_fg_{12}J_f=g_{12}^{-1}.
\]

But modulo \(2\),

\[
-1\equiv1,
\]

so

\[
\boxed{
\bar J_f
=
\begin{pmatrix}1&1\\0&1\end{pmatrix}
=\bar g_{12}.
}
\]

Therefore, under the same audited additive identification

\[
\psi:\mathfrak p_2/2\mathfrak p_2\to\mathbf F_4,
\]

both distinct integral operators transport to the same Frobenius involution:

\[
\boxed{
\psi\bar J_f\psi^{-1}
=
\psi\bar g_{12}\psi^{-1}
=\mathrm{Fr}.
}
\]

This is an exact quotient collapse.

Integrally,

\[
g_{12}\neq J_f,
\qquad
J_fg_{12}J_f=g_{12}^{-1},
\]

whereas modulo \(2\),

\[
\bar g_{12}=\bar J_f.
\]

## 6. Three distinct notions that must not be identified [Audit]

The following are different:

1. literal multiplication by \(\lambda\) in the residue field, which is the identity because \(\lambda\equiv1\);
2. the mod-2 coordinate reduction of the integral Pell matrix, which becomes Frobenius after additive transport;
3. the Galois action of \(U(12)\) on \(\mathbf F_4\), whose nontrivial quotient is controlled by \(\chi_{-3}\).

Their coexistence is not contradictory because they arise from different carriers and different maps.

Likewise, the \(\chi_{12}\) time-orientation quotient lives naturally before ramified reduction, on the real-quadratic/Pell unit:

\[
\lambda\leftrightarrow\lambda^{-1}.
\]

That distinction is destroyed by literal residue multiplication because both reduce to \(1\).

## 7. Structural synthesis [D/I]

The discriminant-12 V4 character structure now admits the exact decomposition

\[
U(12)\cong C_2\times C_2,
\]

with the three nontrivial characters detecting three complementary sign channels:

\[
\boxed{
\begin{array}{c|c}
\text{character}&\text{exact detected structure}\\
\hline
\chi_{-4}&i\mapsto\pm i\\
\chi_{-3}&\mathbf F_4:\ \mathrm{id}\text{ vs. Frobenius}\\
\chi_{12}&\sqrt3\mapsto\pm\sqrt3,\ \lambda\mapsto\lambda^{\pm1}
\end{array}}
\]

with

\[
\chi_{12}=\chi_{-4}\chi_{-3}.
\]

**[I]** This supplies a precise meaning for the project’s layered V4 structure: the same four cyclotomic labels project differently depending on whether one observes the complex direction, the ramified finite-field direction, or the real-quadratic/Pell-time direction.

## 8. Cross-thread relevance

The concurrent `v13.415` shell-displacement entry uses \(\chi_{12}\) as the exact signed displacement/time-orientation channel. This checkpoint explains why that same \(\chi_{12}\) should **not** be expected to appear as the residue-field Galois sign: the ramified \(\mathbf F_4\) quotient sees \(\chi_{-3}\) instead.

The concurrent Suzuki source-channel audit also finds that the active source support does not gain a positivity improvement from the \(\chi_{12}\) projection. That negative result is compatible with the present decomposition: \(\chi_{12}\) is structurally the real/Pell sign channel, not a universal sharpening character for every mod-12 carrier.

## Guardrails

- Equality \(\bar J_f=\bar g_{12}\) is a mod-2 quotient collapse, not an integral equality.
- Frobenius arising from transported Pell coordinates is not literal multiplication by \(\lambda\) in \(\mathbf F_4\).
- The residue-field Galois quotient is \(\chi_{-3}\), not \(\chi_{12}\).
- No identification is made between the four geometric Cone shells and the four Galois automorphisms.
- No positivity, RH/GRH, or divisor-error theorem is inferred from this character splitting.

---

**Checkpoint conclusion.** Ramified reduction separates the mod-12 character layers rather than merging them. The Pell-time sign \(\chi_{12}\) collapses at the level of literal residue multiplication because \(\lambda\equiv1\), while the cyclotomic residue-field action survives through the distinct quotient \(\chi_{-3}\). Meanwhile real quadratic conjugation and the integral Pell return, though opposite in their integral dynamical roles, collapse to the same transported Frobenius involution modulo 2. This yields an exact three-character decomposition: \(\chi_{-4}\) for the complex sign, \(\chi_{-3}\) for the finite-field sign, and \(\chi_{12}=\chi_{-4}\chi_{-3}\) for the real-quadratic/Pell-time sign.