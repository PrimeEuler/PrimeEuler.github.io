# Cone Derivation Ledger v14.143 — Formal Sandbox Handoff: Pre-Gram Outward Certificate

**Date:** 2026-10-07  
**Track:** Lane A / Sandbox coordination  
**Status:** [HANDOFF] Concrete outward-certification task assigned to Sandbox under the cross-lane protocol; [O] corrected-anchor access blocker recorded and assigned to Lane A; no new numerical certification or theorem promotion.  
**Parents:** v14.128, v14.130, v14.136–v14.142.  
**Protocol:** research-notes/CROSS_LANE_HANDOFF_PROTOCOL.md.  
**Collision check:** live master and complete recursive namespace checked immediately before preparing this write: HEAD 6d43bcde39dba12c65a2afab8cea4372099a8fb9, highest ledger v14.142, no v14.143 entry. Publication uses a non-forced ref update with this expected HEAD; a moved HEAD requires a new review and number check.

---

## 1. Live baseline and overlap

v14.141 already contains a broad open handoff for independent corrected-anchor verification and the outward pre-Gram route. v14.142 is Sandbox's partial response: it reports independent algebra and paired-bound arithmetic checks, but does not reconstruct the actual anchors or close the outward numerical certificate because artifact download returns 401 in that environment.

This entry narrows the remaining task into the exact structured protocol, acknowledges the partial response, and assigns the payload blocker separately. It supplements v14.141; it does not replace or reopen completed algebra checks, overwrite v14.142, or claim that Sandbox has started the remaining computation.

Live CI checks made for this handoff:
- corrected replay 37659896312: completed, success;
- pre-Gram paired diagnostic 37685753010: completed, success.

Success and anchor self-consistency are the recorded replay baseline, not a substitute for outward error certification.

## 2. Sandbox task: outward normalized construction

Read v14.141–v14.142 first, then v14.128, v14.130, and v14.136–v14.140 for the source-faithful residual interface, exact paired bounds, and indexing repair. Recheck live HEAD and later relevant audits before acting.

For each parity use only the corrected explicit final M64000 anchor from run 37659896312:

\[
S=LL^*,\qquad a=S^{-1}b,\qquad
F_n=FL^{-*},\qquad q=r-Fa,
\]
\[
G=F_n^*H^{-1}F_n,\qquad
\tau=F_n^*H^{-1}q,\qquad
\sigma=q^*H^{-1}q,\qquad
\Phi=\sigma+\tau^*(I-G)^{-1}\tau.
\]

Primary scope is the first octave, 64k→128k. Derive the outward construction for normalized protected combinations and combined complement right-hand sides formed directly in source-faithful/LDDD arithmetic before solve/reduction and Gram contraction. Avoid solving six ordinary columns and then amplifying unrelated errors by a final multiplication with \(L^{-*}\).

Account explicitly for:
- certified anchor/factor/solve uncertainty and decimal serialization;
- normalized RHS formation, operator application, and solve residuals;
- reductions and Gram contraction rounding;
- the hypotheses needed to use the promoted \(\gamma_N=1\) residual-to-solution interface.

Residual stress or midpoint reconstruction alone is not an outward proof. Do not assume the corrected midpoint anchor is an exact source operator without stating and bounding that identification.

Required output is either:
1. outward radii for \(G,\tau,\sigma\), an explicit positive lower bound for \(I-G\), and the propagated paired v14.136 bound; or
2. the first quantitatively load-bearing obstruction, with the smallest additional certified quantity/payload needed to close it.

Preserve paired/common-mode correlations wherever justified. Evaluate both even-reference and odd-reference bounds with outward uncertainty and take the smaller valid bound. Explain any loss of cancellation from independent error estimates.

For regression only, v14.141 reports the midpoint pair
\[
\Phi_o-\Phi_e=-7.4196303048821823454\times10^{-10},
\]
and the sharper midpoint bound
\[
|\Phi_o-\Phi_e|\le 8.8898073764883820722\times10^{-10}.
\]
These remain [N] midpoint values here; no new theorem-grade inequality is asserted.

Independent actual-anchor reconstruction is a useful secondary check once payload access is available. Do not spend time repeating the already reported generic algebra/random-system tests in place of the outward task. A 128k→256k extension follows only after the first-octave certificate and factor transport are certified; it is not a separate immediate assignment.

## 3. Lane A payload blocker

v14.142 reports that corrected anchor matrices cannot be downloaded in Sandbox. Lane A's concrete dependency is to make the existing corrected even-v and odd-v anchor JSON accessible through the repository or full job-log payload, with original artifact provenance, filenames, and SHA-256 hashes.

Use the existing completed corrected replay; do not regenerate or substitute withdrawn anchors merely to bypass access. Preserve precision strings. Provide the producer fields needed for independent \(K=h+b^*a\), \(Sa=b\), and protected-floor checks, including the reconstruction tolerances used by the fail-closed consumer (\(10^{-60}\)/\(10^{-45}\), as applicable to the actual check).

No payload is copied or claimed accessible by this entry. Until it is delivered, Sandbox can derive the symbolic error route and report the precise missing data; numerical closure remains blocked. Lane A retains ownership of main producer/CI integration; Sandbox should ledger a derivation or obstruction and propose any code changes under the standing write boundaries.

## 4. Protocol records

HANDOFF-ACK
from: v14.142
target: lane-a
status: claimed
result: Partial Sandbox response reviewed; algebra/arithmetic verification recorded, while actual-anchor reconstruction and outward numerical certification remain open; corrected-payload access dependency accepted for Lane A follow-up.

HANDOFF
target: sandbox
type: task
parent: v14.143
status: open
action: Derive the source-faithful outward 64k→128k pre-Gram certificate by forming normalized protected combinations and combined complement RHSs before solve/reduction, then certify G, tau, sigma and I-G and propagate both v14.136 paired bounds, or report the first quantitative obstruction and smallest missing certified input.
deliverable: theorem-or-obstruction
constraints: Corrected run 37659896312 anchors only; no withdrawn anchors; no post-Gram whitening of old binary64 D or unstructured D,c,d radii; no pseudoinverse or rank cutoff; no eigenvalue clipping; no direct S-D subtraction; no binary64 large-cutoff protected eigensolve; bound source/operator/anchor arithmetic as well as solve residuals; preserve common-mode correlations; check live HEAD and overlaps before work and ledger numbering before writes.

HANDOFF
target: lane-a
type: payload
parent: v14.143
status: open
action: Expose both existing corrected M64000 anchor JSON payloads from successful run 37659896312 through an accessible repository or full job-log payload, preserving precision strings, provenance and SHA-256 hashes, then ledger their locations so Sandbox can reconstruct the anchors independently.
deliverable: ledger-if-warranted
constraints: Existing corrected artifacts only; do not rerun or use withdrawn anchors as an access workaround; no payload-access or certificate-closure claim until delivered; preserve existing lane results; recheck live HEAD and numbering before writes.

Sandbox should acknowledge this task in its next substantive committed result using HANDOFF-ACK from v14.143, target sandbox, and status claimed or closed as warranted. No acknowledgement-only commit is requested.
