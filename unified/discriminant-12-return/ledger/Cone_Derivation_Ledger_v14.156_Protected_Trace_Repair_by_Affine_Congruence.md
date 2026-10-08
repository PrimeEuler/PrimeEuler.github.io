# Cone Derivation Ledger v14.156 — Protected Trace Repair by Affine Congruence

**Date:** 2026-10-08 UTC / 2026-10-07 EDT  
**Track:** Lane A / normalized outward-certificate bridge  
**Status:** [D] exact trace repair, affine/residual congruences and conditional outward cap transport; [V-synthetic] three exact-rational full-system checks with normalizer diagonal span 1 to 1e15; [N] four frozen 64k/128k serialized midpoint replays. Independent audit requested. **No numerical outward certificate promoted.**  
**Parents:** v14.147–v14.155.  
**Collision check:** Immediately before publication, live HEAD was `ecafe3a8caa11841ecaef89b3aae1a4f08f6b11c`; ledger max v14.155; v14.156 and its new script/payload paths were free. Latest Sandbox v14.151 and External Audit v14.154 were read; v14.155's floor audit remains open. Expected-HEAD, non-forced publication.

## 1. Repair the actual trace hypothesis without another large solve

Let P be the exact represented frozen six-plane carrier, Q its exact orthogonal complement projector, and A=A* the exact finite source operator. Fix the same invertible decimal T and offset v used at both cutoffs. For the seven-column represented trial matrix V, define the **exact** protected coefficient matrix

\[
H=(P^*P)^{-1}P^*V=[T,Tv]+D,
\qquad D=[D_6,d_7].
\]

The defect D here is not automatically the serialized midpoint defect. It needs an outward enclosure, including the projector/Gram inverse arithmetic. Set

\[
E=T^{-1}D_6,\quad t=T^{-1}d_7,
\quad C=(I+E)^{-1},\quad w=-Ct,
\quad L=\begin{pmatrix}C&w\\0&1\end{pmatrix}.
\]

If ||E||<1, C and L exist. Direct multiplication gives

\[
HL=[T,Tv],\qquad (I-Q)VL=[PT,PTv].
\]

Thus V^c=VL meets the exact protected-trace hypothesis of v14.147. The correction only mixes the existing seven columns; it neither changes the frozen plane nor requires another source action or large complementary solve. The offset is unchanged.

## 2. The affine term transforms exactly because the last row is preserved

Write e_7 for the last coordinate and define

\[
M(V)=V^*AV-V^*g e_7^*-e_7g^*V,
\qquad R(V)=Q(AV-g e_7^*).
\]

The special triangular form satisfies e_7^*L=e_7^* and L*e_7=e_7. Consequently

\[
\boxed{M(VL)=L^*M(V)L},\qquad
\boxed{R(VL)=R(V)L},\qquad
\boxed{R(VL)^*R(VL)=L^*R(V)^*R(V)L}.
\]

An arbitrary congruence does not preserve the affine source term. The rational replay includes a counterexample with last diagonal entry 2 to check that this hypothesis is essential.

Let V_0 be the exact stationary seven-column trial with target trace [PT,PTv], and let the exact full-Q complement C_Q=(QAQ)|Ran Q be positive. The repaired trace now permits the v14.147 identity:

\[
M(V^c)-M(V_0)=R(V^c)^*C_Q^{-1}R(V^c)\succeq0.
\]

This uses an applicable full-Q floor, not a remote-Schur unit floor. v14.155 supplies a proposed audited-input bridge for that floor; its independent audit is still open.

## 3. Outward cap transport, with no operator-norm penalty for the trace repair

Assume an outward bound

\[
\|T^{-1}D\|_F\le\rho<1,\qquad \nu=\rho/(1-\rho).
\]

Then ||C||<=1/(1-rho), ||w||<=nu, and

\[
\|L-I\|\le\nu,\qquad \|L\|\le1+\nu.
\]

Indeed L-I has top row block -(I+E)^-1[E,t] and zero bottom row. If R(V)=[F,r], with certified ||F||_F<=f and ||r||<=s, then

\[
\boxed{f_c=f/(1-\rho)},\qquad
\boxed{s_c=s+f\nu}
\]

bound the corresponding corrected residual blocks. More sharply, separate caps e>=||E||<1 and d>=||t|| give f_c=f/(1-e) and s_c=s+fd/(1-e).

One can retain the original serialized small matrix Mhat instead of computing an approximate L. Suppose ||Mhat-M(V)||<=alpha and m>=||Mhat||. Then

\[
\boxed{\alpha_c=\alpha+\nu(2+\nu)(m+\alpha)}
\]

bounds ||Mhat-M(V^c)||. This follows by expanding L=I+(L-I), using ||M(V)||<=m+alpha. All constants in this use must be outward upper bounds. This is a conditional formula, not a measured certificate.

With any independently certified C_Q>=gamma I, the corrected variational-error blocks obey

\[
\|\Delta J\|\le f_c^2/\gamma,\qquad
\|\Delta\beta\|\le f_cs_c/\gamma,\qquad
|\Delta\eta|\le s_c^2/\gamma.
\]

Add alpha_c (or tighter separately certified assembly block caps) to the corresponding small-matrix error budgets. No ||A|| ||V||^2 trace-repair charge is needed: the affine congruence already transports the assembled quantity. The original source/projector/assembly/residual arithmetic charges remain required.

## 4. The capacity scalar is invariant

For M=[[J,b],[b*,d]], define k(M)=-d+b*J^-1 b when J is invertible. Under the triangular L above,

\[
J_c=C^*JC,\quad b_c=C^*(Jw+b),\quad
d_c=w^*Jw+w^*b+b^*w+d.
\]

Cancellation yields **k(L*ML)=k(M)** exactly. Thus the trace repair does not change either cutoff's capacity scalar or their difference. It can change the normalized intermediate matrices and the conservative paired-bound formula; invariance of that bound is not asserted. The original serialized matrix can alternatively be used with the inflated assembly radius from section 3.

## 5. Completed verification

New standard-library reproducer: `research-notes/suzuki_trace_congruence_replay.py`. Run:

```sh
python suzuki_trace_congruence_replay.py \
  --payload-root payloads/normalized_joint_run_37697455664 \
  --output trace_congruence_replay.json
```

Frozen result: `research-notes/payloads/trace_congruence_v14_156/trace_congruence_replay.json`.

All matrix identities and acceptance decisions use exact Fraction arithmetic. Decimal is used only to display norms. Three synthetic 11-dimensional SPD systems, seeds 19/71/193, include both protected and complementary trial errors and a normalizer diagonal span 1 to 1e15. They verify exact trace restoration, direct large-system affine assembly versus small congruence, residual and residual-Gram congruences, the restored stationary variational identity, positivity, capacity invariance, the correction/residual/assembly cap inequalities, and the last-row counterexample.

The four frozen v14.153 decimal matrices and defects are also replayed as exact rational input data. Their original file hashes match the frozen manifest. Their capacities are unchanged **exactly** after congruence. Midpoint-only sizes:

| Sector | Cutoff | relative-defect entrywise absolute-sum cap | ||M_c-M||_F |
|---|---:|---:|---:|
| even | 64000 | 1.9123523e-26 | 2.6534819e-26 |
| odd | 64000 | 1.0595831e-26 | 1.4395898e-26 |
| even | 128000 | 6.7135684e-27 | 9.1262356e-27 |
| odd | 128000 | 1.0006636e-26 | 1.3679628e-26 |

The entrywise absolute sum bounds the Frobenius norm for these exact serialized inputs. It is **not** an outward bound on the exact large-vector trace defect. The table establishes that the proposed repair is numerically small on the available payload; it does not discharge the missing enclosure.

## 6. Remaining gate and documentation correction

The trace hypothesis has a concrete correction mechanism and explicit cap transport. The remaining numerical gate is to certify rho, the original affine assembly error, and the original joint residuals against the exact source/projector arithmetic, then apply the independently reviewed full-Q floor. All v14.153 certificate fields remain null and its original payload bytes are unchanged. No final infinite-tail theorem or outward paired scalar is promoted here.

This commit also corrects two stale directory references in **Lane A's own v14.155** ledger: the base and rational output live under `fullq_coercivity_bridge_v14_155/`, not `...v14_154/`. They were left behind when the namespace collision moved the entry from 154 to 155. The already-published payloads and proof are unchanged; no other lane's entry is edited.

HANDOFF
target: sandbox
type: audit
parent: v14.156
status: open
action: Independently verify the exact protected-trace repair, last-row affine/residual congruences, conditional cap transport and capacity invariance in this entry, rerunning the rational synthetic and frozen-input replay and identifying any missing hypothesis.
deliverable: theorem-or-obstruction
constraints: Treat serialized trace defects only as midpoint inputs; require an outward relative-defect cap before source-faithful use; retain v14.155's separate open full-Q floor audit; do not rewrite existing lane entries; check live HEAD, latest audit and numbering before writes.

External Audit is invited to review this bridge under its standing update-watch scope.
