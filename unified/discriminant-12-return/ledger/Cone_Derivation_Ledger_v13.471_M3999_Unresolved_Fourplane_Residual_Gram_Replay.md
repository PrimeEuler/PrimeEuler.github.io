# Cone Derivation Ledger v13.471 — M3999 Unresolved Four-Plane Residual-Gram Replay

Date: 2026-09-14

Status labels: **[D]** exact derived, **[N]** numerical diagnostic, **[N-cert]** previously certified input, **[I]** interpretation, **[Audit]** guardrail.

## 0. Synchronization [Audit]

The live ledger was checked at the beginning of this continuation and again immediately before this numbered write.  During the work, concurrent entries `v13.469` and `v13.470` landed.  The newest numbered entry at the final check was therefore `v13.470` (External Audit Round 35), so `v13.471` was free.

Relevant Suzuki predecessors:

- `v13.399-v13.402`: frozen M3999 six-plane inputs and certified even-sector index bound;
- `v13.451-v13.452`: restored odd theorem and full `ind_{<=0}(A_{a=1})<=6`;
- `v13.459`: nonlinear source-channel Schur sensitivities on the unresolved even four-plane;
- `v13.463-v13.464`: high-precision cutoff stability and tiny-spectrum crossover;
- `v13.467`: signed, near-rank-one large-mode self-energy on the stabilized four-plane;
- `v13.470`: independent audit confirming the v13.467 leading moment and dominant-tail alignment.

The new reproducible helper is

`research-notes/suzuki_M3999_unresolved_fourplane_residual_gram_replay.py`.

Commit:

`e13c4cc746125a9048e61e7c0716642eb4949dae`.

## 1. Purpose

The earlier four-plane tail work used high-precision small and moderate cutoffs to identify the signed asymptotic mechanism.  The present checkpoint moves that calculation onto the **same M3999 finite split used by the certified even-sector theorem**:

\[
C=\{1,3,\ldots,19\},
\qquad
F=\{21,23,\ldots,3999\},
\qquad
T=\{4001,4003,\ldots\}.
\]

The goals are:

1. regenerate the M3999 ten-column finite solve from source-faithful formulas;
2. reproduce a known six-plane residual-Gram checkpoint as a provenance regression;
3. project the same residual machinery onto the unresolved four-plane
   \(N=\ker Q^T\);
4. estimate the resulting infinite-tail self-energy scale using the already-certified effective-tail floor.

## 2. M3999 source-faithful finite solve [N]

The helper reconstructs the canonical even source matrix from:

- cusp diagonal/off-diagonal terms;
- prime-power channels \(q=2,3,4,5,7\);
- source-faithful post-integration-by-parts archimedean rank-two term;
- full even PSD pole \(2cc^T\).

For the pole-free high block, the exact displacement-generator LDL recurrence from the earlier high-block audit is used.  The full PSD pole is then incorporated by a rank-one Woodbury update.

The resulting M3999 finite Schur spectrum begins

\[
\boxed{
\lambda(S_F)
\approx
(1.0\times10^{-15},
3.5\times10^{-15},
8.3\times10^{-15},
1.346\times10^{-12},
3.85764946\times10^{-8},
2.16204593\times10^{-4},\ldots).
}
\]

In particular,

\[
\boxed{
\lambda_5(S_F)
\approx3.85764946\times10^{-8},
}
\]

reproducing the frozen-M3999 verifier scale.

**[Audit]** The first four binary64-scale values are not interpreted as signs.  v13.461 already showed that ordinary double precision is inadequate for those levels.

## 3. Six-plane provenance regression [N]

Let \(Q\in\mathbb R^{10\times6}\) and \(L_0\in\mathbb R^{6\times6}\) be the frozen exact-dyadic inputs of v13.399.

Using the regenerated M3999 finite solve, the residual operator is accumulated:

- directly for \(4001\le n\le16001\);
- by an eight-level inverse-power expansion for \(16003\le n\le2,000,000\).

The normalized six-plane Gram is

\[
H_6
=L_0^{-1}Q^TR^*RQ\,L_0^{-T}.
\]

The replay gives

\[
\boxed{
\lambda_{\max}(H_{6,\le2M})
=0.17821051347425684.
}
\]

The final outward M3999 checker recorded

\[
0.17821051347430.
\]

Thus the new independent regeneration agrees at the displayed precision.

This is an important provenance check: the new four-plane calculation is not based on a different matrix branch or a reconstructed approximation inconsistent with the certified six-plane machinery.

## 4. Frozen unresolved four-plane [D/N]

The exact-dyadic frozen six-plane has

\[
\operatorname{rank}Q=6
\]

exactly.  Numerically choose an orthonormal basis

\[
N\in\mathbb R^{10\times4}
\]

for

\[
\ker Q^T.
\]

This is the unresolved even four-plane from the theorem proof.

After the M3999 finite solve, its low-plus-finite coefficient matrix is

\[
W_4=
\begin{pmatrix}
N\\
-A_{FF}^{-1}A_{FC}N
\end{pmatrix}.
\]

The tail residual Gram is then

\[
G_4=N^TR^*RN.
\]

## 5. Explicit residual Gram through two million [N]

Using direct residual rows through 16001 and the validated eight-level inverse-power architecture through two million gives

\[
\boxed{
\operatorname{spec}(G_{4,\le2M})
\approx
(0,
6.3\times10^{-30},
8.6872\times10^{-24},
1.20565193\times10^{-13}).
}
\]

The tiny negative roundoff-scale first displayed eigenvalue is symmetrization/eigensolver noise and is not interpreted.

The operator scale is

\[
\boxed{
\|G_{4,\le2M}\|_2
\approx1.20565193\times10^{-13}.
}
\]

The next genuine scale is only

\[
\boxed{8.69\times10^{-24}},
\]

so the M3999 unresolved-tail residual is numerically even more strongly rank one than the moderate-cutoff diagnostics of v13.467 suggested.

## 6. Leading M3999 residual moment [N]

The source-faithful leading far-tail vector is

\[
L
= -\frac{2}{\pi}\sum_j Z_jW_{4,j}
+\frac{8\cosh(1/2)}{\pi}\sum_j c_jW_{4,j}.
\]

The M3999 replay gives

\[
\boxed{
L
\approx
(1.45815\times10^{-6},
-1.54566\times10^{-5},
6.06568\times10^{-6},
-2.76294\times10^{-5}).
}
\]

with

\[
\boxed{
\|L\|_2\approx3.22677\times10^{-5}.
}
\]

The normalized \(L\) direction agrees with the dominant eigenvector of \(G_4\) at

\[
\boxed{
|\langle \widehat L,u_{\max}(G_4)\rangle|
>0.9999999999.
}
\]

Thus the near-rank-one residual Gram at the theorem cutoff is directly the same leading \(1/n\) moment mechanism identified at moderate cutoff in v13.467.

## 7. Analytic remainder beyond two million [N]

For \(n\ge2,000,001\), use the source-faithful remainder form

\[
\left\|r_n-\frac{L}{n}\right\|
\le
\frac{B}{n^2}+\frac{C}{n^3},
\]

with the same loose but valid far-tail envelope \(|Z_n|<8\).

Applying the componentwise moment bounds to all four columns and combining them in Euclidean norm gives

\[
\boxed{
\|G_{4,>2M}\|_2
<1.16\times10^{-15}
}
\]

at the midpoint coefficient payload.

Hence the beyond-two-million part is already below one percent of the explicit M3999 four-plane Gram scale.

## 8. Hybrid self-energy scale from the certified tail floor [N/N-cert]

The certified even-sector proof gives

\[
\boxed{
T_{\mathrm{eff}}\succeq
\delta_T I,
\qquad
\delta_T>0.18225976374175623.
}
\]

Therefore structurally

\[
R^*T_{\mathrm{eff}}^{-1}R
\preceq
\delta_T^{-1}R^*R.
\]

Combining the **certified floor** with the **midpoint regenerated four-plane Gram** gives the hybrid numerical ceiling

\[
\boxed{
\|\Sigma_{4,\mathrm{tail}}\|_2
\lesssim
\frac{1.20565193\times10^{-13}+1.16\times10^{-15}}
{0.18225976374175623}
<6.68\times10^{-13}.
}
\]

**[Audit]** This is not yet an outward-certified self-energy bound because the new \(G_4\) payload has not been interval-enclosed.  Only \(\delta_T\) is currently theorem-level certified.

## 9. Comparison with the finite unresolved scale [N/I]

On the same frozen numerical complement,

\[
\operatorname{spec}(N^TS_FN)
\approx
(6.6\times10^{-16},
3.5\times10^{-15},
8.3\times10^{-15},
1.34627\times10^{-12}).
\]

Thus the largest finite unresolved level is, at the midpoint model,

\[
\boxed{
1.34627\times10^{-12}
}
\]

while the entire hybrid tail ceiling is below

\[
\boxed{6.68\times10^{-13}}.
\]

So the midpoint data exhibit more than a factor-two cushion for **one** unresolved even direction after allowing the whole infinite tail at the crude coercivity floor.

This is the first M3999-scale indication that the certified even index bound might conceivably be sharpened from four unresolved directions to three.

However, no theorem promotion is made: the existing generic exact-vs-nominal finite-Schur perturbation budget is approximately \(10^{-10}\)-scale, far larger than the \(10^{-12}\) directional margin under discussion.

## 10. What has actually improved [I]

The obstruction to a stronger even theorem is now sharply localized.

It is **not** the remote tail size: on the unresolved four-plane the tail residual Gram is only \(10^{-13}\)-scale and essentially rank one.

It is **not** uncertainty about the residual-generation branch: the same regeneration reproduces the certified six-plane residual checkpoint to the displayed digits.

The remaining bottleneck is instead the finite-side source perturbation estimate on a **single stabilized unresolved direction**.  The global finite-Schur perturbation bound used in the six-plane proof is intentionally uniform and loses roughly two orders of magnitude compared with what is now needed.

## 11. Next certification target [Audit]

Let \(v_*\in\ker Q^T\) denote the largest finite unresolved direction of the frozen M3999 midpoint Schur complement.

A theorem-level strengthening would follow if one could certify simultaneously:

1. a lower bound
   \[
   v_*^TS_{F,\mathrm{exact}}v_*
   >m_*>0,
   \]
2. an outward four-plane tail/self-energy bound
   \[
   v_*^TR^*T_{\mathrm{eff}}^{-1}Rv_*
   <m_*.
   \]

The midpoint scales suggest a target of order

\[
\boxed{m_*\sim10^{-12}}.
\]

The immediate next task is therefore **directional finite-side source sensitivity**, not another larger cutoff:

- replay the exact source-enclosure budget only on \(v_*\);
- exploit cancellation in \(A_{FC}v_*\) and the solved coefficient vector rather than the global \(\|A_{CF}\|/\mu\) bound;
- in parallel outward-enclose the already tiny rank-one residual Gram.

If the directional finite-side uncertainty can be reduced below roughly

\[
5\times10^{-13},
\]

then an even-sector index-3 certificate may become numerically plausible.

## 12. Guardrails [Audit]

- The current theorem remains
  \[
  \boxed{\operatorname{ind}_{\le0}(A_{\mathrm{even}}(1))\le4.}
  \]
- The full theorem remains
  \[
  \boxed{\operatorname{ind}_{\le0}(A_{a=1})\le6.}
  \]
- No sign is assigned theorem-level to any of the four unresolved even directions.
- No exact kernel, RH, or GRH conclusion follows.
- The apparent one-direction midpoint cushion is a certification target, not a proved positive eigenvalue.

---

**Checkpoint conclusion.** The source-faithful M3999 residual machinery has now been regenerated and projected onto the frozen unresolved even four-plane.  The same replay reproduces the established six-plane normalized residual checkpoint `0.17821051347430`, providing a strong provenance regression.  On the unresolved four-plane, the residual Gram through two million has operator norm only `1.20565193e-13` and is numerically rank one; the analytic remainder beyond two million is below `1.16e-15`.  Combining this midpoint residual payload with the certified effective-tail floor gives a hybrid self-energy scale below `6.68e-13`.  The largest frozen finite unresolved level is about `1.346e-12`, leaving a factor-two midpoint cushion for one direction.  The frontier has therefore moved: the dominant obstruction to an even index-3 theorem is now the directional finite-side source perturbation budget, not the infinite tail.