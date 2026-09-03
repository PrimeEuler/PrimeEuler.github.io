# Cone Derivation Ledger v13.195 — Paper A v2.2 Theorem Audit

Date: 2026-09-03

Source audited: `unified/PaperA_ConicTheorem_v2.2.tex`.

## Executive verdict

The elementary geometric spine survives a beginning-to-end algebraic audit. One hypothesis/presentation issue was found and repaired in the live v2.2 source: the ellipse metric formulas were previously stated for `ab>0` while using signed `c` as a length. Since a nonempty positive-quadrant ellipse can be represented with all three coefficients negative, the line is now normalized (multiplying the equation by -1 when necessary) to `a,b,c>0` before the metric propositions. No geometric line or formula is changed by this normalization.

## 1. Coordinate map

[D]
\[
X=(x-y)/2,\qquad Y=\sqrt{xy},\qquad T=(x+y)/2
\]
implies
\[
X^2+Y^2=T^2,
\qquad x=T+X,\quad y=T-X.
\]

[D] Factor exchange is exactly `X -> -X`, with `Y,T` fixed.

## 2. General conic classification

[D] For `b != 0`, substituting `y=(c-ax)/b` gives
\[
Y^2=(c/b)x-(a/b)x^2.
\]
Hence `ab>0`, `ab=0`, `ab<0` give ellipse, parabola, hyperbola respectively on the nonempty positive-quadrant portion.

[Audit] The circle clause is stated as `a=b != 0`, in which case `x+y=c/a` is constant. This avoids silently assuming `a=b=1`.

## 3. Row/column orientation

[D] With the paper's fixed convention `X=(x-y)/2`:
\[
x=u:\quad Y^2=u^2-2uX,
\]
so its vertex/tangent endpoint is `(X,Y)=(u/2,0)`.

[D]
\[
y=u:\quad Y^2=u^2+2uX,
\]
so its vertex/tangent endpoint is `(-u/2,0)`.

[D] This matches the red/purple worked example:
\[
8x+4y=32:\ (2,4)\mapsto(X,T)=(-1,3),
\]
\[
4x+8y=32:\ (4,2)\mapsto(X,T)=(1,3).
\]

## 4. Tangent-circle theorem

[D] Both row and column parabolas are tangent to
\[
X^2+Y^2=(u/2)^2
\]
at their respective vertices. The common tangent is vertical in the `(X,Y)` projection.

[D] On the cone the two endpoints are
\[
(T,X,Y)=(u/2,\pm u/2,0),
\]
the two generator/null-ray endpoints of that fixed-`T` slice.

## 5. Ellipse metric formulas

[Audit repair] Before metric statements normalize the same geometric line to `a,b,c>0`.

[D]
\[
Y_{\max}^2=c^2/(4ab)
\]
at
\[
(x,y)=(c/(2a),c/(2b)).
\]

[D] The `Y` direction lies in the cutting plane and is orthogonal to the direction joining the two `Y=0` endpoints. Therefore
\[
b_{semi}=c/(2\sqrt{ab}),
\]
\[
a_{semi}=c\sqrt{2(a^2+b^2)}/(4ab).
\]

[D]
\[
\frac{a_{semi}^2}{b_{semi}^2}=\frac{a^2+b^2}{2ab}\ge1,
\]
so the major/minor naming is justified rather than assumed.

[D]
\[
e=|a-b|/\sqrt{a^2+b^2}.
\]

## 6. Constant product and Fermat

[D]
\[
xy=N\iff T^2-X^2=N.
\]
For odd integer `N`, integer `T,X` recover
\[
N=(T-X)(T+X).
\]
No stronger algorithmic claim is made.

## 7. Divisor summatory identity

[D] The gnomon arm at diagonal level `u` has integer length
\[
\lfloor n/u\rfloor-u.
\]
Summing the two arms plus the diagonal cell gives
\[
D(n)=\sum_{u\le\sqrt n}\left[2(\lfloor n/u\rfloor-u)+1\right]
\]
and hence the standard Dirichlet hyperbola identity
\[
D(n)=2\sum_{u\le\sqrt n}\lfloor n/u\rfloor-\lfloor\sqrt n\rfloor^2.
\]

## 8. n=11 illustration

[D]
\[
D(11)=29,\quad T_{11}=66,\quad A_{11}=37.
\]

[D]
\[
xy=11\iff Y=\sqrt{11}\iff T^2-X^2=11.
\]
The boundary meets `x+y=12` at `(1,11),(11,1)`, mapping to `(X,T)=(-5,6),(5,6)`.

[Audit] `n=11` remains explicitly illustrative, not a structural selection principle in Paper A. The displayed `11 log 11` and `11 H_11` are comparison quantities only.

## Publication guardrails retained

- Do not import discriminant-12 selection into the proof of Paper A.
- Do not identify the tangent generator rays with a particular arithmetic return without the companion-paper representation.
- Do not call `n log n` the exact area/count of the discrete divisor region.
- Do not treat the n=11 shell as causing its later cyclotomic or class-field behavior.
- Do not infer arithmetic invariance from the tangent-circle mesh relation.

## Status

[D] Core coordinate identities: clean.
[D] Conic classification: clean after explicit circle wording.
[D] Row/column signs: clean.
[D] Tangent theorem: clean.
[D] Ellipse metric formulas: clean after coefficient normalization and major-axis inequality was made explicit.
[D] Fermat restatement: clean.
[D] Divisor-summatory identity: clean.
[D] n=11 visualization arithmetic: clean.

No remaining substantive mathematical error was found in this pass. Next work is source/reference restoration, build inspection, and publication copy-editing rather than changing the theorem architecture.
