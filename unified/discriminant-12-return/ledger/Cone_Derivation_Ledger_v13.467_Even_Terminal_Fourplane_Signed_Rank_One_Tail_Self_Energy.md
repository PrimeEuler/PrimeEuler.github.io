# Cone Derivation Ledger v13.467 — Even Terminal Four-Plane Signed Rank-One Tail Self-Energy

Date: 2026-09-14

Status labels: **[D]** exact derived, **[N]** numerical diagnostic, **[I]** interpretation, **[Audit]** guardrail.

## 0. Synchronization [Audit]

The live ledger was checked at the beginning of this continuation and again immediately before this numbered write.  The newest numbered entry remained `v13.466` (`Crossed Cocycle Trivialization and Affine-Frame C2`), so `v13.467` was free.

Relevant Suzuki predecessors are:

- `v13.452`: full source-faithful theorem `ind_{<=0}(A_{a=1})<=6`;
- `v13.459`: leave-one-channel nonlinear Schur sensitivity on the unresolved even four-plane;
- `v13.461`: high-precision small-cutoff even spectrum;
- `v13.463`: high-precision cutoff stability of the unresolved even four-plane;
- `v13.464`: crossover from rapid early tiny-spectrum collapse to a much slower cutoff regime;
- `v13.465`: independent external audit of the preceding numerical diagnostics.

The present checkpoint asks a more operator-directed question: **what is the sign and effective rank of the large-mode Schur self-energy acting on the stabilized unresolved even four-plane?**

The reproducible helper is

`research-notes/suzuki_even_terminal_fourplane_signed_tail_self_energy.py`.

## 1. Exact Schur sign [D]

Let

\[
C=\{1,3,\ldots,19\}
\]

be the ten-dimensional low core.  For two nested high cutoffs `M_1<M_2`, split the newly added modes into a band `G`.  Schur associativity gives

\[
\boxed{
S_{M_2}
=
S_{M_1}-R_G^*T_{G,\mathrm{eff}}^{-1}R_G.
}
\]

Whenever the effective added-band block is positive,

\[
T_{G,\mathrm{eff}}>0,
\]

the signed correction satisfies

\[
\boxed{
S_{M_2}-S_{M_1}\preceq0.
}
\]

Thus the remote high modes can only pull the low-core Schur form downward.  This is a structural Schur-complement statement, not a fitted sign from the eigenvalue ladder.

The certified even-sector high-complement positivity chain supplies the required positive-high-block setting for the source-faithful operator.  The numerical work below concerns the **size and anisotropy** of this negative correction, not its algebraic sign.

## 2. High-precision band corrections [N]

The source-faithful even matrix was rebuilt in 70-decimal-digit arithmetic, including

- cusp diagonal/off-diagonal terms;
- the five prime-power channels `q=2,3,4,5,7`;
- the source-faithful archimedean rank-two term;
- the full even PSD `cosh(1/2)` pole.

The low-core Schur complements were computed at

\[
M=39,59,79,99,119,139,159.
\]

Using the first four eigenvectors of the `M=159` low-core Schur complement as a fixed stabilized comparison basis, the successive projected correction spectra are:

\[
\boxed{
39\to59:
(-5.5851040883\!\times10^{-12},
-3.8937433814\!\times10^{-17},
-2.0837601793\!\times10^{-22},
-6.4481824619\!\times10^{-29})
}
\]

\[
\boxed{
59\to79:
(-3.5632669099\!\times10^{-13},
-2.6874097502\!\times10^{-18},
-8.3629057953\!\times10^{-25},
-1.3961592741\!\times10^{-31})
}
\]

\[
\boxed{
79\to99:
(-1.7505572683\!\times10^{-13},
-6.1944417789\!\times10^{-19},
-3.1818053412\!\times10^{-26},
-1.5469839286\!\times10^{-32})
}
\]

\[
\boxed{
99\to119:
(-1.8437385738\!\times10^{-13},
-1.6673673884\!\times10^{-19},
-6.0380617243\!\times10^{-27},
-2.0207207680\!\times10^{-33})
}
\]

and farther out,

\[
\boxed{
119\to139:
(-5.5857423648\!\times10^{-14},
-6.1061143237\!\times10^{-20},
-4.6616518617\!\times10^{-27},
-4.7021380575\!\times10^{-35})
}
\]

\[
\boxed{
139\to159:
(-2.5957082480\!\times10^{-14},
-8.9993133327\!\times10^{-20},
-8.8874978951\!\times10^{-28},
-4.5587137234\!\times10^{-35}).
}
\]

The corrections are therefore not merely negative: they are numerically **extremely close to rank one** on the stabilized four-plane.

## 3. Source-faithful leading residual channel [D/N]

For a stabilized four-plane vector, collect the low-plus-finite coefficients `w_j` after eliminating the modes through `M=159`.

The source-faithful far-tail residual has the leading expansion

\[
r_n=\frac{L}{n}+O(n^{-2}),
\]

with

\[
\boxed{
L
= -\frac{2}{\pi}\sum_j Z_jw_j
  +\frac{8\cosh(1/2)}{\pi}\sum_j c_jw_j.
}
\]

This is the same signed leading channel used in the earlier six-plane analytic-tail work.

Evaluating this moment for the four stabilized `M=159` Schur directions gives

\[
\boxed{
L\approx
\left(
-5.4275478706\times10^{-14},
1.1010471215\times10^{-10},
7.4876778301\times10^{-8},
2.2410378496\times10^{-5}
\right).
}
\]

Hence the normalized leading channel is essentially the fourth stabilized coordinate:

\[
\boxed{
\frac{L}{\|L\|}
\approx
(-2.42\times10^{-9},
4.91\times10^{-6},
3.34\times10^{-3},
0.9999944).
}
\]

Therefore the leading `1/n` tail term is intrinsically rank one to very high accuracy on this four-plane.

## 4. Direct alignment with the signed self-energy [N]

Let `u_tail` be the most-negative eigenvector of the projected `139->159` Schur correction, expressed in the same stabilized four-plane coordinates.

The numerical overlap is

\[
\boxed{
\left|
\left\langle
u_{\mathrm{tail}},
\frac{L}{\|L\|}
\right\rangle
\right|
=0.9999997239488878.
}
\]

Thus the observed near-rank-one signed self-energy is explained directly by the source-faithful inverse-power expansion:

\[
\boxed{
\text{dominant signed tail direction}
\simeq
\text{leading }1/n\text{ residual-moment direction}.
}
\]

This is much stronger than merely observing one large singular value: it identifies the responsible source moment.

## 5. Relation to the residue/exceptional split [N/I]

The dominant tail direction is **not** the `n=3`-dominated exceptional direction found in `v13.455-v13.463`.

Across the outer bands its overlap with the frozen exceptional vector is only about

\[
0.32\text{--}0.33,
\]

while roughly

\[
\boxed{0.883}
\]

of its norm lies in the four unit-residue indicator span.

For the `99->119` dominant direction, representative character overlaps are approximately

\[
|\langle u,\chi_{12}\rangle|\approx0.417,
\]

\[
|\langle u,\chi_{-4}\rangle|\approx0.292,
\]

\[
|\langle u,\chi_{-3}\rangle|\approx0.275.
\]

**[I]** The slow large-mode self-energy therefore acts primarily on the residue-aligned part of the stabilized four-plane.  The exceptional ramified-cancellation direction is comparatively weakly exposed to the leading far-tail channel.

This does **not** make the residue characters operator eigenchannels; `v13.459` already showed strong mixing and noncommuting source sensitivities.

## 6. Consequence for the tiny-spectrum question [I]

The unresolved even four-plane now has two distinct structural scales:

1. a stable low-core four-plane already visible by small cutoff;
2. a remote self-energy whose leading asymptotic action is almost rank one.

So the four tiny eigenvalues should not be modeled as four independent copies of one cutoff law.  The large-mode tail has a preferred one-dimensional channel, with the remaining three directions receiving only higher-order inverse-power corrections at leading asymptotic order.

This gives a concrete explanation for why the four tiny levels display very different magnitudes and cutoff evolution.

## 7. What is still open [Audit]

This checkpoint does **not** determine the signs or limits of the four infinite-cutoff terminal eigenvalues.

In particular:

- the finite high-precision levels remain positive at the tested cutoffs;
- the exact Schur tail correction is downward;
- the leading downward correction is almost rank one;
- but no validated comparison yet shows whether the accumulated infinite correction exceeds or stays below any one of the tiny finite levels.

Therefore there is still no exact-kernel claim and no strengthening of

\[
\boxed{\operatorname{ind}_{\le0}(A_{a=1})\le6}.
\]

No RH or GRH conclusion follows.

## 8. Next certification target

The next useful calculation is no longer a blind cutoff extrapolation.  It is to outward-enclose, on the stabilized four-plane,

\[
\boxed{
R^*T_{\mathrm{eff}}^{-1}R
}
\]

by separating

- the explicit moderate tail;
- the rank-one leading `L/n` channel;
- the higher `n^{-2},n^{-3},\ldots` remainder channels.

Because the leading moment vector is already known to be essentially one-dimensional, this should reduce the four-plane infinite-tail problem to one dominant scalar channel plus a much smaller three-dimensional remainder.

---

**Checkpoint conclusion.** The remote even-sector Schur correction on the stabilized unresolved four-plane is signed negative and numerically almost rank one.  High-precision band replays show a single dominant negative eigenvalue with the other three suppressed by many orders of magnitude.  The source-faithful leading inverse-power moment vector `L` is itself essentially one-dimensional and aligns with the dominant signed self-energy eigenvector at `0.999999724`.  Thus the large-mode tail selects one preferred residue-heavy terminal direction, while the other three directions—including the `n=3` exceptional mode—enter only through much smaller higher-order channels.  This is a structural diagnostic, not an infinite-limit sign theorem.