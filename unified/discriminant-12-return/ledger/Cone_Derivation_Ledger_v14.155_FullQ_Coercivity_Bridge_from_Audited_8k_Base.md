# Cone Derivation Ledger v14.155 — Full-Q Coercivity Bridge from the Audited 8k Base

**Date:** 2026-10-08 UTC / 2026-10-07 EDT  
**Track:** Lane A / source-aligned complement certificate  
**Status:** [D] full-Q floor derived through cutoff 256k from already-audited base and remote certificates; [N-cert] fresh base Cholesky replay passes with the same P as v14.153; [D] cross-block cap and public floor rounding verified with exact rational arithmetic. **Audit target before downstream theorem-grade reuse.** Normalized assembly/residual/trace certification remains open.  
**Parents:** v14.025, v14.029–v14.036, v14.044, v14.071, v14.084–v14.091, v14.150–v14.154.  
**Collision check:** Immediately before this write, live HEAD was `dc6d035a2c2da39cec2fe39a968a6edb68de98b8`; ledger max v14.154; v14.155 and its new payload namespace were free. Audit Round 196 occupied the initially considered v14.154 number; it was read and preserved before selecting v14.155. Published with an expected-HEAD non-forced update.

## 1. The older certificate supplies a base, not an automatic unit full-Q floor

v14.150 correctly separated the full frozen-six-plane complement from the remote Schur operator. v14.151/v14.152 confirmed that a remote Schur floor alone cannot give a full-block floor. That conclusion remains correct.

The broader assertion in v14.151 that the ledger has no relevant finite M-block certificate needs refinement. v14.029/v14.031 already certify the identical frozen complement of the shifted 8k front, and v14.084 section 3/v14.085 already give a partial-Schur comparison extending it to 32k. The current missing step is checking geometry and extending the cross-block bound to the required later cutoffs. This entry supplies those steps. It does not transfer gamma=1 to the full-Q operator.

Let P be the exact matrix of stored binary64 carrier entries, supported in modes through 4000, and let Q_R be the exact Euclidean orthogonal projector onto Ran(P_R)^perp. All statements below concern the exact source-faithful no-twist parity operator A_R, not the correction solver's floating matrix.

## 2. Base certificate and exact geometry match

At the 8k front, v14.029/v14.031 certify

\[
(A_8-\Pi_{4000<n\le8000})|_{Q_8}
\succeq\delta_p I,
\]

with delta_e > 7.795385618610192746e-6 and delta_o > 3.262507025086259604e-5. Adding back the nonnegative shell projector gives

\[
C_8:=(Q_8A_8Q_8)|_{Q_8}\succeq\delta_p I.
\]

The existing directed penalized-Cholesky producer was freshly re-executed in both parities. It returns 7.7953856186101911566e-6 and 3.2625070250862587883e-5, respectively; the small final-digit differences from the historical run are above the conservative constants used here:

\[
\boxed{\delta_e^0=7.79\times10^{-6},\qquad
\delta_o^0=3.26\times10^{-5}.}
\]

The fresh replay uses the audited algorithm and its exact-source operator charge 2.1e-13. It does not use a midpoint eigensolve as its PASS criterion. It constructs the penalty with the exact represented binary64 P.

The older base helper and the normalized producer helper give component-identical P arrays, and the first 2000 rows hash to the v14.153 actual-cutoff hashes in both parities. Their remaining rows are exactly zero. Dependency and P4 payload hashes are recorded in `geometry_match.json`; local source/blob identities were checked against the live repository. Thus this is the complement of the same represented plane, not a new Ritz plane or an assumed exact orthonormalization.

Reproducers: `suzuki_M8000_mu1_penalized_cholesky_outward.py` (existing) and `suzuki_fullq_geometry_replay.py` (new). The base output is frozen in `payloads/fullq_coercivity_bridge_v14_155/base_8k_replay.json`.

## 3. Why the partial shell Schur inherits the remote unit floor

For any 8000 <= R <= 256000, split the full-Q space orthogonally as Q_8 plus the coordinate shell 8000<n<=R:

\[
C_R=\begin{pmatrix}C_8&B\\B^*&D\end{pmatrix},
\qquad H_Q=D-B^*C_8^{-1}B.
\]

v14.034/v14.036 prove positivity of the exact shifted full 8k front; hence A_8 is positive. Eliminating Q_8 in the triple split P plus Q_8 plus shell leaves

\[
\begin{pmatrix}S_8&E\\E^*&H_Q\end{pmatrix},
\qquad S_8\succ0.
\]

Eliminating the protected finite directions as well gives the full-front remote Schur operator, compressed to this finite shell:

\[
S_{8,R}=H_Q-E^*S_8^{-1}E.
\]

By v14.044/v14.071, the exact nested remote operator S_{p,8000} is >=I. Its principal compression S_{8,R} is therefore >=I. Consequently

\[
\boxed{H_Q=S_{8,R}+E^*S_8^{-1}E\succeq I.}
\]

This is the comparison missing from a naive operator identification. It uses the certified positivity of the protected finite Schur block; an M-block floor alone would not justify omitting that hypothesis. No tiny protected inverse is formed numerically.

## 4. Cross-block norm below 40 through 256k

The global scalar majorant |z_n|<=10 follows from the finite-mode bound in v14.034 and the all-n>=8000 bound |z_n|<8 in v14.025. The exact same-parity displacement kernel obeys

\[
|K(n,m)|\le\frac{20}{\pi|n-m|}.
\]

The old 8k front has 4000 modes per parity; at R=256000 the shell has at most 124000. Writing the parity gaps as 2k, rectangular Schur testing gives

\[
\|B_{\rm disp}\|^2
\le(10/\pi)^2 H_{4000}H_{124000}.
\]

The new standard-library rational consumer proves H_4000<9 and H_124000<13 by upper-bounding each 1/k with an integer ceiling on a denominator 10^12. No floating harmonic sum is used in these inequalities. Since pi>157/50,

\[
\|B_{\rm disp}\|^2
<\frac{29250000}{24649}< (69/2)^2.
\]

For either parity the established pole norm is bounded by the even cap sqrt(2) cosh(1/2); |alpha|=2. The elementary positive-series bound

\[
\cosh(1/2)
<1+1/8+\frac{1/384}{1-1/120}<8/7
\]

therefore gives

\[
\|B_{\rm pole}\|<4(8/7)^2=256/49<11/2.
\]

Orthogonal restriction to Q_8 cannot increase either cross-block norm. Combining them,

\[
\boxed{\|B\|<(69+11)/2=40.}
\]

This covers both requested cutoffs and also 256k. It does not assert the same harmonic cap for arbitrarily large or infinite R.

## 5. Full-Q coercivity: symbolic proof and exact public constants

For x in Q_8 and shell vector y, set L=C_8^{-1}B. Completing the square gives

\[
\langle C_R(x,y),(x,y)\rangle
=\langle C_8(x+Ly),x+Ly\rangle+\langle H_Qy,y\rangle
\ge\delta_p^0(\|x+Ly\|^2+\|y\|^2),
\]

because delta_p^0<1. The inverse shear sends (u,y) to (u-Ly,y). It is I plus a map of norm ||L||, so its norm is at most 1+||L||. Since ||L||<=40/delta_p^0,

\[
\boxed{C_R\succeq
\frac{\delta_p^0}{(1+40/\delta_p^0)^2}I.}
\]

The rational consumer checks that this exact bound exceeds the following rounded-down public floors:

\[
\boxed{\gamma_{Q,e}=2.95\times10^{-19},\qquad
\gamma_{Q,o}=2.16\times10^{-17}}
\quad(8000\le R\le256000).
\]

These deliberately coarse constants are for the **actual full frozen-six-plane complement**. They are not remote-Schur unit constants. The proof uses the three specific inputs which v14.151 listed as missing: the audited base floor, the protected-positive partial-Schur comparison, and a derived cross-block norm cap.

New rational reproducer: `research-notes/suzuki_fullq_coercivity_bridge.py`. Result: `payloads/fullq_coercivity_bridge_v14_155/fullq_bridge.json`. It uses only integer/Fraction arithmetic for the harmonic caps, comparisons, and final rounding.

## 6. Scope and next gate

This is an explicit certificate bridge from existing audited inputs, submitted for independent verification before downstream theorem-grade use. It refines v14.151's obstruction by identifying overlooked older inputs and checking their applicability. It preserves v14.152's general disproof of a Schur-to-block unit-floor transfer.

The original v14.153 midpoint outputs remain untouched and retain their null certificate fields. Their overall certification is still incomplete: outward source/projector arithmetic, trace matching/correction, normalized affine assembly, and joint residual caps remain required. The constants here are much smaller than one; v14.128's old residual budgets cannot merely keep their numerical values while substituting these floors.

HANDOFF-ACK
from: v14.151
target: lane-a
status: closed
result: Obstruction reviewed. The automatic unit-floor transfer remains invalid; older v14.029/v14.031 base certificates and v14.084/v14.085 comparison provide a route. Fresh base replay and exact P match completed, and the comparison/cross cap is extended here through 256k with explicit coarse full-Q floors.

HANDOFF
target: sandbox
type: audit
parent: v14.155
status: open
action: Independently verify the source/plane match, protected-positive partial-Schur comparison, exact rational cross-block cap and resulting full-Q floors in this entry, identifying any missing hypothesis before these constants are used in the normalized outward certificate.
deliverable: theorem-or-obstruction
constraints: Check v14.029/v14.031 and v14.034/v14.036 rather than importing remote gamma=1 directly; use the frozen v14.153 P hashes and the fresh base replay; preserve the distinction between derived full-Q floors and still-missing assembly/residual/trace caps; do not rewrite existing lane entries; check live HEAD, latest audit and numbering before writes.

External Audit is invited to review the same explicit certificate bridge under its standing update-watch scope.

HANDOFF-ACK
from: v14.154
target: lane-a
status: closed
result: Audit Round 196 read immediately before publication; its independent byte-identical reproduction of both frozen midpoint consumers is acknowledged. This bridge supplies the separately required coercivity comparison and does not promote the midpoint paired number.
