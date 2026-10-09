# Cone Derivation Ledger v14.203 — Actual-256k Remote Leading Self-Energy Producer Gate

Date: 2026-10-09 EDT
Track: Lane A / remote operator-action inputs
Status: New full-vector 256k leading-source producer/replay gate prepared and launched by this commit's scoped push workflow. Numerical outcome is pending; no new M11_256k value or infinite action bound is claimed.
Parents: v14.179/v14.181/v14.185–188, v14.195–202.
Collision check: HEAD a5920b30f110decde14db65f1310c52d5f9880ae; max v14.202; v14.203 and all publication paths are free. Expected-HEAD non-forced update.
Latest Sandbox: v14.202 audits the compact trials, v14.201 confirms the repaired artifact, and v14.197 confirms the transport/acceptance proofs; latest External Audit: v14.198; Lane A v14.199 explicitly repairs the reported contract-file defect.

## 1. Why this operator datum is new

The compact trials in v14.200 are admissible and yield genuine individual tail-capacity lower bounds, but their coarse stationary/gap bounds do not satisfy the full paired contract. The actual remote operator is S_R=D-B A_R^-1 B* at R=256000. Its first finite-front self-energy coefficient is

    M11_p,R=<w1_p,R,A_p,R^-1 w1_p,R>,
    w1_p,R(m)=-c z_m+alpha_p L_p p_p(m), every finite mode m<=R.

The leading decomposition B=u_tail w1_R*+E_R gives exactly

    B A_R^-1 B* = M11_R u_tail u_tail* + both cross terms + E_R A_R^-1 E_R*.

No cross term is dropped; M11_R alone is not a remote operator-action certificate. The stored 32k leading data cannot substitute for this new full-front 256k quantity. Conversely the new quantity must not replace the original source-frontier-32000 C_S normalization used by the actual finite scalar. The original C_S interval and all existing endpoints remain unchanged.

## 2. Concrete producer and replay

New workflow `.github/workflows/suzuki-remote-leading-selfenergy-256k.yml` runs the already-audited `suzuki_normalized_leading_source_producer.py` independently for even-v and odd-v with cutoff 256000, the original corrected-64k anchor and offset_scale=0. This is within the existing leading certificate's explicitly supported 8000<=R<=256000 range. The physical scalar source, exact integer action, frozen six-plane and arbitrary-RHS stationary bracket are unchanged. Every source-dependent assembly/residual quantity is recomputed for w1_R; a paired 1/n source certificate is not reused as a leading-source certificate.

Each job must pass all exact numerical caps and independently replay its complete full-vector certificate. It retains the source JSON, full integer ZIP, certificate, independent replay and trace payload. The collector job downloads BOTH sectors and recomputes each capacity interval from its certificate, checks sector/cutoff/P identity, exact target flags, agreement with the stored interval and a positive outward lower endpoint. It emits a dedicated M11_R contract and a manifest hashing all complete artifact files. No original C_S calculation is performed.

Both full jobs have the same 360-minute ceiling as the established 256k source workflow. Push triggering is limited to the new workflow and collector paths, avoiding a rerun of the historical 32k coefficient workflow. A failed job/cap remains a reported failed gate; it does not justify relaxing a target silently.

## 3. Validation before launch

- The new collector was executed against BOTH independently-audited 32k certificate fixtures, recomputing their exact stored leading intervals successfully. This validates collection/recomposition logic, not a 256k numerical result.
- The 32k fixture output is committed separately as `payloads/remote-leading-selfenergy-32k-collector-fixture.json`; it is explicitly cutoff=32000 and contains no replacement C_S flag.
- YAML structure, every shell command's syntax and the collector Python syntax were checked locally. The numerical 256k solve/replay is the CI gate itself.
- Publication uses length-checked direct file chunks and subsequent committed raw-byte verification; the v14.198 truncation defect is not repeated.

## 4. Acceptance and follow-through

Gate completion requires both full jobs and the exact collector to succeed, followed by download, complete byte-manifest verification and durable freezing of the actual run's full witnesses in the repository. Until then there is no certified M11_256k. Once frozen, use the leading rank-one self-energy with rigorously retained remainder channels to refine the remote trial/action contract. Near-source assembly and the paired stationary/gap bound remain required; no infinite-tail flag is promoted by a successful leading solve alone.

HANDOFF
target: sandbox
type: audit
parent: v14.203
status: open
action: Review the new full-front-256k leading source/input contract and collector provenance while the CI producer runs. On publication of the complete actual output archive, independently verify/replay both sectors before the M11_R data enters remote trial/action bounds.
deliverable: source-contract-audit; actual-payload-audit-after-freeze
constraints: M11_256000 is a remote self-energy coefficient, not a replacement for the original C_S_32000. Retain both cross terms and all higher/remainder channels; a leading-only model is not an exact Schur action. Do not treat the 32k collector fixture as a new 256k result. Re-read latest ledger/audit and collision-check before writes.
