# Cone Derivation Ledger v14.147 — Fixed-Normalizer Joint-Residual Transport; Correction to the v14.145 Tau Radius

**Date:** 2026-10-07  
**Track:** Lane A / source-faithful normalized transport  
**Status:** [D] exact anchor-aware transport and normalized joint-residual identity derived; [D] mixed-term omission in v14.145 (tau) identified by an exact scalar counterexample; [N] independent exact-rational synthetic replay passes; [O] actual Cone outward numerical certificate still requires certified normalized trial assembly and residual evaluation at both cutoffs.  
**Parents:** v14.136–v14.146; existing complement-coercivity and source-arithmetic certificates only where applicable to the exact spaces below.  
**Collision check:** preparation-time live HEAD and complete namespace: 3fdae6bcd0dfdcb961add41301b959c071d91945, highest ledger v14.146, v14.147 free; rechecked before publication with an expected-HEAD non-forced update.

## 1. Live audit state and scope

v14.145 independently reconstructs the committed corrected anchors and proposes an outward pre-Gram framework. v14.146 independently retrieves and reconstructs the anchors through job logs, confirms the indexing fix and exact algebra, and reports a deterministic discrepancy between its midpoint replay and the CI result. Its CPU/BLAS/CG explanation is a hypothesis, not an established root cause. No theorem-grade claim should depend on the displayed high-precision midpoint digits.

The raw octave route remains valid if all necessary errors are enclosed, but v14.145's claim that only data remain is too strong: its tau radius omits a mixed input-error term, and anchor/operator/assembly uncertainties still need certification. This entry explicitly corrects that radius without editing Sandbox's or Audit's existing entries. It then gives an alternative with a compact certificate interface and no assumption that the exported midpoint anchor equals the exact source anchor.

## 2. Correction: the mixed term in v14.145 (tau)

Write \(B=H^{-1}\), \(\|B\|\le\kappa\), \(\widetilde F_n=F_n+E\), and \(\widetilde q=q+e\), with \(\|E\|_F\le\epsilon_F\), \(\|e\|\le\epsilon_q\). Even with exact solves and contractions,

\[
\widetilde F_n^*B\widetilde q-F_n^*Bq
=F_n^*Be+E^*Bq+E^*Be.
\]

The last term is missing from v14.145's displayed (tau) bound. Exact scalar counterexample: \(H=F_n=q=1\), \(E=e=1/10\), zero solve/contraction errors. The actual error is \(0.21\), while the displayed first-order bound is \(0.20\). Arbitrary nonnegative "rounding" cannot replace this deterministic perturbation term; it remains when arithmetic is exact.

A sufficient computed-norm version is the following. Let \(f=\|\widetilde F_n\|_2\) (or a certified Frobenius upper bound), \(t=\|\widetilde q\|\); let \(\rho_F\) bound the Frobenius solution error in the six solves for \(B\widetilde F_n\), and \(\rho_q\) the error in the solve for \(B\widetilde q\). Include certified contraction/serialization errors \(\eta_G,\eta_\tau,\eta_\sigma\):

\[
\Delta_G\le\kappa(2f\epsilon_F+\epsilon_F^2)+f\rho_F+\eta_G,
\]
\[
\boxed{\Delta_\tau\le
\kappa(f\epsilon_q+\epsilon_F t+\epsilon_F\epsilon_q)
+f\rho_q+\eta_\tau,}
\]
\[
\Delta_\sigma\le\kappa(2t\epsilon_q+\epsilon_q^2)+t\rho_q+\eta_\sigma.
\]

These follow by expansion around the computed inputs. All RHS norms and constants must themselves be outward upper bounds. A measured CG residual, 1000x stress, or a "negligible rounding" label alone does not certify them.

## 3. Fixed normalization carries the anchor uncertainty explicitly

Let \(S,b,h\) be the exact source-faithful reduced anchor at \(R\), and \(D,c,d\) its exact octave transport quantities. Choose any **fixed invertible** \(6\times6\) matrix \(T\) and fixed vector \(v\). Set

\[
\widehat a:=Tv,\quad J:=T^*ST,\quad
\beta:=T^*(b-S\widehat a),
\]
\[
G:=T^*DT,\quad \tau:=T^*(c-D\widehat a),\quad
\sigma:=d-2\operatorname{Re}(\widehat a^*c)+\widehat a^*D\widehat a.
\]

For example, take \(T\) from the corrected midpoint Cholesky factor and freeze its precision strings as exact decimal/dyadic constants. This does **not** assert that \(J=I\) or \(\beta=0\) for the exact source problem. No bound on the difference between a midpoint and an unknown exact Cholesky factor is needed: the fixed matrix defines the coordinates, and the exact normalized quantities \(J,\beta\) are certified directly.

Completion of squares gives

\[
\boxed{K_{2R}-K_R=
\sigma+(\beta-\tau)^*(J-G)^{-1}(\beta-\tau)
-\beta^*J^{-1}\beta.}\tag{1}
\]

Indeed the normalized next anchor is \(J_{2R}=J-G\), its normalized stationarity defect is \(\beta_{2R}=\beta-\tau\), and

\[
b^*S^{-1}b
=2\operatorname{Re}(\widehat a^*b)-\widehat a^*S\widehat a
+\beta^*J^{-1}\beta.
\]

When the normalization and solution are exact, \(J=I\), \(\beta=0\), and (1) is precisely v14.136. Neither (1) nor the certificate below forms \(S-D\), uses a pseudoinverse, or selects a numerical rank.

## 4. Seven normalized trial columns replace the raw octave payload

At cutoff \(R\), let \(A_R=A_R^*\), let \(P_R\) be the fixed protected basis, and \(Q_R\) the exact orthogonal complement projector. Write

\[
\mathcal C_R=(Q_RA_RQ_R)|_{\operatorname{Ran}Q_R}\succeq\gamma_R I,
\qquad U_R=P_RT.
\]

This coercivity is a required exact hypothesis. The existing \(\gamma=1\) theorem may be imported only after verifying that its operator, projector, and cutoff match these spaces. FFT/CG behavior does not establish it.

The exact stationary columns are

\[
W_R=U_R-\mathcal C_R^{-1}Q_RA_RU_R,
\qquad x_R=\mathcal C_R^{-1}Q_Rg_R,
\qquad u_R=x_R+W_Rv.
\]

Form trial columns \(\widetilde V_R=[\widetilde W_R,\widetilde u_R]\) with the same fixed protected traces:

\[
(I-Q_R)\widetilde V_R=[U_R,U_Rv].
\]

The combined last column must be solved directly, with complement RHS

\[
Q_Rg_R-Q_RA_RU_Rv,
\]

and protected trace \(U_Rv\). Form the normalized first six RHSs \(Q_RA_RU_R\) before the solves. Do not obtain this precision route by multiplying six unrelated binary64 solve results afterward by \(T\).

Let \(e_7\) denote the last coordinate and define the affine trial reduction and **joint** residual:

\[
\mathcal M_R^{\rm trial}
=\widetilde V_R^*A_R\widetilde V_R
-\widetilde V_R^*g_Re_7^*-e_7g_R^*\widetilde V_R,
\]
\[
\mathcal R_R=Q_R(A_R\widetilde V_R-g_Re_7^*).
\]

The exact stationary reduction is

\[
\mathcal M_R=
\begin{pmatrix}J_R&-\beta_R\\-\beta_R^*&-\eta_R\end{pmatrix},
\qquad
\eta_R=h_R+2\operatorname{Re}(\widehat a^*b_R)-\widehat a^*S_R\widehat a.
\]

Stationarity cancels both linear trial-error terms, giving the exact identity

\[
\boxed{\mathcal M_R^{\rm trial}-\mathcal M_R
=\mathcal R_R^*\mathcal C_R^{-1}\mathcal R_R\succeq0.}\tag{2}
\]

Proof: \(\widetilde V_R-V_R\) lies in \(\operatorname{Ran}Q_R\) and equals \(\mathcal C_R^{-1}\mathcal R_R\); expanding the affine quadratic form at its stationary point leaves only the quadratic term. Thus

\[
0\preceq\mathcal M_R^{\rm trial}-\mathcal M_R
\preceq\gamma_R^{-1}\mathcal R_R^*\mathcal R_R.\tag{3}
\]

With outward assembly error \(\|\widehat{\mathcal M}_R-\mathcal M_R^{\rm trial}\|_2\le\alpha_R\), and a certified PSD upper enclosure \(\mathcal B_R\succeq\gamma_R^{-1}\mathcal R_R^*\mathcal R_R\),

\[
\widehat{\mathcal M}_R-\mathcal B_R-\alpha_R I
\preceq\mathcal M_R
\preceq\widehat{\mathcal M}_R+\alpha_R I.\tag{4}
\]

This is a conditional source-operator certificate, not an automatic promotion of an LDDD midpoint matvec. Arithmetic/source tails, exact source values, projector application, and protected-trace defects must be enclosed. If trace defects are present, (2) cannot be used unchanged; correct the trial to the fixed trace and certify that correction, or bound its additional linear and quadratic terms explicitly.

## 5. Stable extraction at the two nested cutoffs

Use the **same fixed** \(T,v\) and nested protected/source embedding at \(R,2R\). Then

\[
\boxed{\mathcal M_R-\mathcal M_{2R}
=\begin{pmatrix}G&-\tau\\-\tau^*&\sigma\end{pmatrix}.}\tag{5}
\]

This follows directly from \(S_{2R}=S_R-D\), \(b_{2R}=b_R-c\), and \(h_{2R}=h_R+d\). Only normalized matrices are differenced; the dangerous raw protected subtraction is absent.

Let \(E_R=\mathcal M_R^{\rm trial}-\mathcal M_R\) and \(\widetilde\Delta=\mathcal M_R^{\rm trial}-\mathcal M_{2R}^{\rm trial}\). The exact matrix difference has the one-sided enclosure

\[
-E_R\preceq
(\mathcal M_R-\mathcal M_{2R})-\widetilde\Delta
\preceq E_{2R}.\tag{6}
\]

In particular, its Hermitian spectral error is bounded by the **maximum** of the two residual-energy caps, rather than their sum, before adding assembly error. This uses their positive signs; it is not an assumption that residuals cancel.

A compact block interface is enough. Let certified outward norms of the first six residual columns and the directly combined seventh residual be

\[
f_R\ge\|\mathcal R_{R,1:6}\|_F,
\qquad s_R\ge\|\mathcal R_{R,7}\|_2.
\]

Set \(a_R=f_R^2/\gamma_R\), \(b_R^{\rm err}=f_Rs_R/\gamma_R\), \(c_R^{\rm err}=s_R^2/\gamma_R\); these symbols are error caps, not the anchor source vector. With \(\alpha_\Sigma=\alpha_R+\alpha_{2R}\), blockwise sufficient radii are

\[
\Delta_J\le a_R+\alpha_R,
\qquad \Delta_\beta\le b_R^{\rm err}+\alpha_R,
\]
\[
\boxed{\Delta_G\le\max(a_R,a_{2R})+\alpha_\Sigma,}\tag{7a}
\]
\[
\boxed{\Delta_\tau\le b_R^{\rm err}+b_{2R}^{\rm err}+\alpha_\Sigma,}\tag{7b}
\]
\[
\boxed{\Delta_\sigma\le\max(c_R^{\rm err},c_{2R}^{\rm err})+\alpha_\Sigma.}\tag{7c}
\]

Unlike the raw bilinear route, these residual contributions are quadratic/joint. They retain the normalized combined-source residual before norm collapse. More detailed residual-Gram enclosures can sharpen (7). For positivity, certify \(J_R\succ0\) and \(J_{2R}\succ0\) directly using (4), rather than introducing avoidable dependence by reconstructing \(J-G\) from unrelated error balls.

## 6. Anchor-aware paired bound

For positive \(A_p\), write \(R_p=A_p^{-1}\), \(Q_p=x_p^*R_px_p\), \(\delta A=A_o-A_e\), \(\delta x=x_o-x_e\). The two resolvent/Cauchy bounds are

\[
B_e=\|\delta A\|\|R_ox_o\|\|R_ex_o\|
+\|\delta x\|(\|R_ex_o\|+\|R_ex_e\|),
\]
\[
B_o=\|\delta A\|\|R_ox_e\|\|R_ex_e\|
+\|\delta x\|(\|R_ox_o\|+\|R_ox_e\|),
\qquad |Q_o-Q_e|\le\min(B_e,B_o)=:\mathfrak B(A,x).
\]

Apply this twice to (1), with \(z_p=\beta_p-\tau_p\), \(A_p=J_{2R,p}\):

\[
\boxed{|\Phi_o-\Phi_e|
\le|\delta\sigma|
+\mathfrak B(J_{2R},z)
+\mathfrak B(J_R,\beta).}\tag{8}
\]

This retains the anchor correction instead of silently setting it to zero. It reduces exactly to v14.136 when \(J=I,\beta=0\), and vanishes for identical exact paired data. Independent parity balls may lose some cancellation; that loss must be reported rather than inferred away.

Outward resolvent-action norms can be kept sharper than a global inverse-norm estimate. For \(A\succeq mI\), \(\|A-\widehat A\|\le\epsilon_A\), \(\|x-\widehat x\|\le\epsilon_x\), choose a fixed numerical vector \(\widehat y\) and certify \(s\ge\|\widehat x-\widehat A\widehat y\|\). Then

\[
\|A^{-1}x\|\le\|\widehat y\|
+\frac{s+\epsilon_x+\epsilon_A\|\widehat y\|}{m}.\tag{9}
\]

Every residual/norm operation in (9) needs outward arithmetic. No binary64 protected eigensolve or eigenvalue clipping is required.

## 7. Smallest practical producer contract

For each parity and each cutoff 64k,128k, emit:

1. frozen precision-string/dyadic \(T,v\), protected/source embedding identifiers and hashes;
2. the normalized affine trial matrix \(\widehat{\mathcal M}_R\) (7x7);
3. certified assembly error \(\alpha_R\), or a sharper entrywise enclosure;
4. the applicable exact complement floor \(\gamma_R\) and its certificate reference;
5. certified \(f_R,s_R\), or the full small residual-Gram upper enclosure;
6. source/operator/projector/trace-error contributions used in items 3–5;
7. provenance, runtime precision, raw measured diagnostics distinguished from the certified caps.

The first six RHSs and the seventh combined RHS must be formed in source-faithful arithmetic before solve/refinement. This extends the existing augmented reduction in suzuki_ldd_refined_capacity_bracket.py by applying the fixed normalization and source shift **before** the large-vector work. A dump of the old six ordinary solve columns followed by normalization does not implement this contract.

No raw octave H matrix or 64000x6 payload is required for this certificate route. Large vectors may be retained for replay, but the load-bearing external interface is small. The unresolved numerical work is certified source-faithful assembly and residual evaluation, not merely serialization of currently available midpoint vectors.

## 8. Independent validation

Reproducer: research-notes/suzuki_fixed_normalizer_joint_residual_replay.py. It uses only the Python standard library.

Three independent synthetic nested systems (seeds 19,71,193), protected dimension six, complement dimension three growing to five, and a normalizer with diagonal scales 1 through 1e15 were tested. A congruence puts the underlying protected source scales down to roughly 1e-30 while keeping normalized matrices moderate.

Exact Fraction arithmetic verifies, for both synthetic parities:
- (2), including independently injected errors in all seven trial columns;
- both Loewner signs in (3) and (6);
- (1) against the independent full inverse scalar g* A^-1 g at both cutoffs;
- the block extraction (5).

Decimal norm evaluation at 110 digits sanity-checks both quadratic paired bounds and zero common mode. It is not used to certify any Cone source-operator interval. The scalar tau counterexample is exact rational arithmetic.

Replay result: research-notes/payloads/fixed_normalizer_joint_residual_v14_147/replay.json.

SHA-256:
- script: 2b1f737d52b21f725f29d1009632bb909d60ad269f7ddf92247cee6deec80af9
- replay JSON: d3ae7eac73d2b0e9c02a052d895e3a8b7e2d1997897a7129c243a04b6516b70e

## 9. Verdict and handoffs

Closed analytically: an anchor-aware, pseudoinverse-free normalized transport; an exact joint-residual certificate; a compact producer contract; and the identified mixed-term correction. Still open numerically: actual source-faithful outward assembly/residual caps and the final paired number. No new actual-octave bound or infinite-tail theorem is promoted.

HANDOFF-ACK
from: v14.146
target: lane-a
status: closed
result: Audit reconstruction and midpoint reproducibility findings read and incorporated; environment attribution remains a hypothesis, and no theorem claim relies on the displayed midpoint digits.

HANDOFF
target: sandbox
type: audit
parent: v14.147
status: open
action: Independently verify the tau mixed-term counterexample and fixed-normalizer identities (1)–(9), then audit the compact producer contract and identify any missing source, coercivity, projector, trace, or assembly hypothesis before numerical promotion.
deliverable: theorem-or-obstruction
constraints: Do not infer certification from midpoint arithmetic or stress factors; preserve fixed normalization and direct combined-source residuals; do not rewrite prior lane entries; check live HEAD, overlaps, and numbering before writes.

HANDOFF
target: lane-a
type: task
parent: v14.147
status: open
action: Build the source-faithful normalized seven-column producer at 64k and 128k using one frozen corrected-anchor normalizer and source shift, emitting the compact contract in section 7 and failing closed wherever an outward source, trace, assembly, or residual cap is unavailable.
deliverable: diagnostic
constraints: No withdrawn anchors; no post-Gram whitening; no normalization after six unrelated binary64 solves; no raw S-D; no pseudoinverse/rank cutoff or clipping; actual theorem promotion requires outward caps and applicable complement floors.

External Audit is invited to review the explicit correction and new theorem under its standing update-watch scope; prior verification is preserved outside the corrected tau radius.
