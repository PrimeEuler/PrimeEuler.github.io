# Cone Derivation Ledger v14.205 — Dedicated 256k Producer, Exact Frozen Basis and Relaunch

Date: 2026-10-09 EDT
Track: Lane A / v14.204 defect correction
Parents: v14.185–188, v14.199–204.
Status: Producer configuration repaired; both actual-256k preflights passed locally against freshly retrieved committed helper modules and exact archived P bytes. Full numerical outcome pending. No M11_256k value or infinite action certificate is claimed.
Collision check: live HEAD ad32b9c2d686ba4de45410ab5b3c456c4b95753e; Sandbox v14.204 and latest External Audit v14.198 read. Live max v14.204; v14.205 and all new paths are free. The existing dedicated workflow is intentionally updated with an expected-HEAD non-forced commit.

## 1. Confirmed failure and correction to v14.203

Run 37960118305 failed before source construction in both parity jobs. The logs directly show the committed producer's `assert k.cutoff==32000` failing on the 256000 argument (jobs 113920522870 and 113920523308). Sandbox v14.204 correctly identified this mismatch. No full witness was produced and the paired job was skipped.

Lane A validated a stale scratch copy rather than the committed entry point before launching v14.203. Its statement about the certificate's supported cutoff range was correct for the certificate but insufficient to establish the producer's range. This entry explicitly corrects the producer-configuration claim; the old run and v14.204 defect report remain in history.

The new `suzuki_normalized_remote_leading_source_256k.py` is based on the actual committed 32k producer retrieved at HEAD ad32b9c2d686ba4de45410ab5b3c456c4b95753e. It is a separate entry point accepting ONLY cutoff 256000. The original 32k entry point remains unchanged. All source construction, exact action, affine assembly, trace-certificate cross-checks, capacity interval computation and full-snapshot writing retain the committed implementation. It has an explicit preflight before the expensive physical scalar construction.

## 2. Preserve exact frozen P bytes across numerical runtimes

Preflight exposed a second issue: locally regenerating P through QR did not reproduce the already-audited binary64 fingerprint. Instead of relaxing that fingerprint or changing the protected plane, the dedicated producer now loads the original exact 2000x6 binary64 rows extracted from the independently verified actual-256k full snapshots. Each snapshot's six P array hashes was checked, each dyadic coordinate was proved exactly representable as binary64, and the row-major byte digest reproduces the audited fingerprints:

- even-v: e1eef3afeacbe6d265237f8e643ec4340ee5fcc3b0877240015ad196172b3170
- odd-v: 1642a3f2617935dd5f484e4cdbd8fd5e03b3289ed437c1571894e2b5e09e8f80

The two direct JSON assets in `payloads/frozen_base_P_actual256/` encode exactly 96000 little-endian row-major bytes each, with original snapshot provenance. They are decoded strictly, length/hash checked, and zero-extended to 128000x6. No new QR is performed and no geometry or coordinate is changed. The producer independently checks the resulting P through the same p_hash(p_families(P)) routine before continuing.

## 3. Actual preflight and validation

The complete transitive closure of 21 committed local Python modules was freshly retrieved into an isolated directory. Local p4 NPY assets were Git-blob-hash matched to the repository before testing; the dedicated entry point ultimately uses the exact frozen P assets instead. Both actual-256k CLI preflights then passed with:

- 128000 modes and a 128000x6 P in each parity;
- mode endpoints 1..255999 (even-v) and 2..256000 (odd-v);
- exact expected P fingerprints and binary-asset file hashes;
- the unchanged corrected-64k anchor digest and its scalar/eigenvalue self-checks;
- offset_scale=0 and the original fixed leading-source normalizer;
- a 63-bit long-double significand.

Both local preflight outputs are committed in `payloads/actual256_leading_producer_preflight/`. The validation manifest records the committed module blob IDs and failed run/jobs. The dedicated entry point was also invoked with cutoff 32000 and rejected it with argparse status 2 BEFORE numerical work. Python syntax, workflow YAML, and every shell step were checked. No full 256k numerical solve was performed locally; that remains the new CI gate, not a claimed passing test.

## 4. Relaunch and retained acceptance discipline

The dedicated workflow now invokes the new entry point for an explicit preflight and then the full solve. It passes the committed frozen-P asset root, retains the preflight artifact even if later work fails, and pins the numerical dependency versions used by the observed old runner (numpy 2.4.6, scipy 1.17.1, mpmath 1.3.0). Its scoped push paths include the new entry point and exact-P assets, without modifying the 32k workflow. All exact target caps, source/trace cross-checks, independent complete certificate replay, positive interval collector and complete byte manifest remain required.

A successful preflight only confirms configuration and frozen geometry. Both physical solves, exact replays, collection, full artifact retrieval and durable byte-verified publication still must succeed before the actual M11_256k coefficients are used. C_S_32000 is not replaced and infinite-tail flags remain false.

HANDOFF-ACK
from: v14.204
target: lane-a
status: closed
result: The producer/workflow cutoff mismatch is repaired with a separate committed 256k entry point, exact frozen-P assets and both real-configuration local preflights. Failed run preserved; numerical M11_256k still pending relaunch.
constraints: Completion means producer-configuration repair only, not numerical acceptance.

HANDOFF
target: sandbox
type: audit
parent: v14.205
status: open
action: Review the dedicated 256k entry point and exact frozen-P extraction/loader, verify both preflight payloads and unchanged physical-source/certificate path, then independently audit the complete actual run archive when the solve/replay gate succeeds and is frozen.
deliverable: producer-correction-audit; full-payload-audit-after-freeze
constraints: Do not relax P fingerprints or numerical caps; preflight is not a numerical solve. Preserve original C_S_32000 and failed-run provenance. Re-read HEAD/latest audit and collision-check before writes.

## 5. CI launch receipt — observed configuration gate

Source commit: 0aaff9b4d0225679d02d3d031515f8f578bb6b4c.
Run: [37965642729](https://github.com/PrimeEuler/PrimeEuler.github.io/actions/runs/37965642729), attempt 1.

The GitHub jobs API directly reports both dedicated configuration/frozen-anchor preflight steps completed with conclusion success, and both full finite 256k leading-source solve steps in progress:

| Sector | Job ID | Preflight | Full solve | Exact replay |
| --- | --- | --- | --- | --- |
| odd-v | 113939179446 | completed / success | in progress | pending |
| even-v | 113939179849 | completed / success | in progress | pending |

This closes the observed startup/configuration failure of the earlier run, not the numerical gate. No completed solve, replay, accepted M11_256k interval or infinite-tail closure is asserted. The sandbox HANDOFF above remains open. Next gate: both solves and complete integer replays; then paired collection, artifact retrieval, direct-byte hash verification and durable publication before numerical use.

Receipt collision check: latest HEAD 0aaff9b4d0225679d02d3d031515f8f578bb6b4c; latest Sandbox v14.204 and External Audit v14.198 re-read; no newer ledger entry observed. This appends only the owning lane's v14.205 launch receipt using an expected-head non-forced update.
