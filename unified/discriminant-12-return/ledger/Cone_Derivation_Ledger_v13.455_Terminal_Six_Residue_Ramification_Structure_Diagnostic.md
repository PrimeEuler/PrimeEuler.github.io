# Cone Derivation Ledger v13.455 — Terminal Six Residue/Ramification Structure Diagnostic

Date: 2026-09-14

Status labels: **[D]** exact derived, **[N]** numerical diagnostic, **[I]** interpretation, **[Audit]** guardrail.

## 0. Synchronization [Audit]

A live-head check before this work found v13.453 as the newest numbered entry. During the diagnostic, v13.454 (`Intrinsic Discriminant-12 S3 Quotient`) landed. A second live-head check immediately before this write confirmed v13.454 remained newest, so v13.455 was free.

The theorem-level Suzuki status entering this checkpoint is already closed at

\[
\operatorname{ind}_{\le0}(A_{\rm even}(1))\le4,
\qquad
\operatorname{ind}_{\le0}(A_{\rm odd}(1))\le2,
\]

hence

\[
\operatorname{ind}_{\le0}(A_{a=1})\le6.
\]

The present checkpoint does **not** improve that bound. It asks what structure is visible in the six unresolved terminal directions.

## 1. Frozen complements used [D/N]

Use the exact-dyadic frozen positive subspaces already committed in

- `research-notes/suzuki_M3999_frozen_dyadic_Q_L0.py`, with a 10x6 exact-rank-six matrix on the even-v low core \(\{1,3,\ldots,19\}\);
- `research-notes/suzuki_odd_M4000_frozen_dyadic_Q8_L0.py`, with a 10x8 exact-rank-eight matrix on the odd-v low core \(\{2,4,\ldots,20\}\).

Their Euclidean orthogonal complements therefore have dimensions four and two respectively. The complements are constructed numerically only for the present structural diagnostic.

The reproducible helper is

`research-notes/suzuki_terminal_six_residue_moment_diagnostic.py`.

## 2. Low polynomial moments are almost absent [N]

For the even-v unresolved four-plane, normalized polynomial vectors \(n^p\) have unresolved fractions

\[
\begin{array}{c|c}
p&\|P_{\rm unres}n^p\|/\|n^p\|\\\hline
0&0.3163\\
1&0.003385\\
2&0.01657\\
3&0.004424\\
4&0.02234\\
5&0.03224
\end{array}
\]

For the odd-v unresolved two-plane the suppression is even stronger:

\[
\begin{array}{c|c}
p&\|P_{\rm unres}n^p\|/\|n^p\|\\\hline
0&0.03909\\
1&0.0007923\\
2&0.004653\\
3&0.001131\\
4&0.004177\\
5&0.003892
\end{array}
\]

Thus the unresolved terminal sector is not naturally described as a failure of the obvious low-order polynomial moments. The certified positive subspaces already carry essentially all of those smooth directions.

## 3. Mod-12 characters have substantial even-sector unresolved mass [N]

On the even-v core \(\{1,3,\ldots,19\}\), the real mod-12 character-like vectors have unresolved fractions approximately

\[
\boxed{
\chi_{12}:0.710,
\qquad
\chi_{-4}:0.665,
\qquad
\chi_{-3}:0.754.
}
\]

The unit indicator has unresolved fraction about \(0.376\), and the 3-divisible indicator about \(0.571\).

This is qualitatively different from the polynomial moments: residue/character content couples strongly to the unresolved even sector.

## 4. Full V4 unit-residue span: three strong directions, one weak direction [N]

Let \(V_{\rm unit}\) be the four-dimensional span of the residue indicators

\[
1_{n\equiv1},\quad1_{n\equiv5},\quad1_{n\equiv7},\quad1_{n\equiv11}
\qquad (\bmod12)
\]

restricted to the even-v low core.

The principal cosines between \(V_{\rm unit}\) and the unresolved four-plane are

\[
\boxed{
0.93574,
\quad0.71268,
\quad0.70240,
\quad0.23512.
}
\]

Therefore a pure statement that "the four unresolved even directions are the four V4 channels" is false at this cutoff.

What is supported numerically is the weaker structural picture:

- roughly three unresolved directions have substantial unit-residue/V4 alignment;
- a fourth direction is qualitatively different.

## 5. The fourth even direction is concentrated at the first prime-3 core mode [N]

Choose the unit vector in the unresolved four-plane corresponding to the smallest principal cosine with the V4 unit-residue span. In the ordered even-v core

\[
(1,3,5,7,9,11,13,15,17,19),
\]

one representative has coordinates approximately

\[
(-0.0701,
\ 0.9429,
\ -0.2050,
\ -0.2260,
\ -2.7\times10^{-5},
\ -0.1049,
\ 0.0265,
\ 0.0274,
\ 0.0197,
\ -0.00276).
\]

Thus the non-V4-aligned terminal direction is overwhelmingly concentrated on the first \(n=3\) core coordinate. Its projection onto the single-coordinate vector \(e_{n=3}\) is about \(0.9462\).

Notably, the next 3-divisible core coordinate \(n=9\) is essentially absent in this representative. So this is not well described by the generic indicator \(1_{3\mid n}\).

## 6. Relation to the ramified-prime thread [I]

v13.448 and v13.454 independently establish that discriminant 12 singles out two different ramified local carriers:

- a prime-2 cyclotomic/residue branch carrying the unit/V4 and canonical local \(C_3\)/\(S_3\) phase structure;
- a prime-3 Pell/tangent branch with a distinguished ramified principal-unit direction.

The terminal diagnostic is compatible with a parallel analytic split:

\[
\boxed{
\text{three strongly residue/V4-aligned directions}
\quad+\quad
\text{one prime-3 boundary/ramified defect direction}
}
\]

inside the unresolved even four-plane.

This is presently an **interpretation**, not a derived identification. No theorem has yet connected the finite Suzuki core coordinate \(n=3\) to the local Pell tangent generator in the operator itself.

## 7. Odd-sector comparison [N/I]

The odd-v core \(\{2,4,\ldots,20\}\) has only the unit cores

\[
1,5,7
\]

at this cutoff; unit core 11 does not yet occur. Its two unresolved directions are therefore a less complete test of the four-channel V4 picture.

The same strong suppression of polynomial moments is present, so the common feature across parity sectors is that the terminal directions are oscillatory/arithmetic rather than smooth polynomial-moment modes.

## 8. Next tests [O]

The highest-value next diagnostics are:

1. isolate the three V4-aligned even terminal directions and express them in the Hadamard character basis \(1,\chi_{-4},\chi_{-3},\chi_{12}\), including the ramified 3/9 coordinates explicitly rather than zeroing them by Dirichlet-character convention;
2. test whether the exceptional \(n=3\)-dominated direction couples primarily to the q=3 source channel by decomposing its Rayleigh quotient into cusp, archimedean, prime q=2,3,4,5,7, and pole pieces;
3. perform the same source-channel decomposition for the two odd unresolved directions;
4. only if an exact source-faithful identity emerges should any terminal direction be promoted from numerical near-zero/near-defect status to an algebraic statement.

## 9. Guardrails [Audit]

- The unresolved complements here are numerical orthogonal complements of frozen exact positive subspaces; they are not frozen theorem inputs themselves.
- Principal angles and coordinate concentrations are diagnostics only.
- No exact kernel, zero eigenvalue, or sign is asserted for any of the six directions.
- The V4 character picture is only partial: the fourth even direction is demonstrably not well aligned with the unit-residue span.
- The n=3 / prime-3 interpretation is suggestive and compatible with the independent ramified-local theory, but no operator-level intertwining has yet been proved.
- No RH or GRH conclusion follows.

---

**Checkpoint conclusion.** The six unresolved Suzuki directions are not explained by ordinary low-order moments. In the even sector, three of four unresolved directions have strong mod-12 unit-residue/V4 alignment, while the fourth is sharply localized at the first n=3 core coordinate. This suggests a residue-character plus ramified-prime decomposition of the terminal obstruction and identifies source-channel Rayleigh decomposition—especially the q=3 contribution—as the next concrete test.
