# Cone Derivation Ledger v14.207 — Actual 256k Leading Self-Energy Gate Passed; Complete Freeze in Progress

Date: 2026-10-09 EDT
Track: Lane A / v14.205 numerical gate
Parents: v14.185–188, v14.195–206.
Status: Both actual-256k solves, independent complete integer certificate replays and paired collector passed. Downloaded paired archive locally verified against every CI manifest hash; certificates and paired intervals independently recomposed as described below. Complete durable witness publication is a separate gate, now launched. No infinite-tail closure is claimed.

Collision check: immediately before this write live HEAD c0bce93a1d54004a1ba15ff822cf937b71a88de1; latest Sandbox v14.204 and External Audit v14.206 re-read. Live max v14.206; v14.207 and all new paths are free. Nonforced expected-HEAD publication.

## 1. Completed source run and exact replay

Source commit: 0aaff9b4d0225679d02d3d031515f8f578bb6b4c.
Run: [37965642729](https://github.com/PrimeEuler/PrimeEuler.github.io/actions/runs/37965642729), attempt 1.
The live GitHub jobs API reports completed/success for odd job 113939179446, even job 113939179849 and paired job 113951317739. In both parity jobs the full solve and independently replayed complete integer source certificate steps succeeded. Paired recomposition and the complete artifact manifest step also succeeded.

Downloaded paired artifact 11634776766, name remote-leading-selfenergy-frozen-256000. All 13 manifest-listed original files match their exact byte lengths and SHA-256 hashes. The original manifest itself has SHA-256:
46fbe78e59f96f7ec2ce7848e9cfb2ac4d7eabe67f4a7eccf9df80dff59df139.

For both sectors, the downloaded replayed certificate is byte-identical to the producer certificate, the payload's embedded certificate agrees, all six numerical targets and all exact checks pass, and the payload's snapshot hash equals the complete downloaded ZIP hash.

- even-v full snapshot SHA-256: fb78ec8572485d040648038a102fe1a880926aaaa72c13469383ef562ff8b1d7
- odd-v full snapshot SHA-256: b975cd0769445492f6d185f84b7c4df9dbcdcfe302df0765d7fa725efb2ec4ac
- even-v certificate SHA-256: e726b54aa728d598e0046b332af7e10dd6afcd5adcf370f2fdbb91e2ca7340e9
- odd-v certificate SHA-256: 5692ac1b3bf7f4bfb627d158149dfd3c9432b49336251d05c467a04bc3f6cfec

Locally ran the collector retrieved from the actual committed repository against both downloaded certificates. Its exact capacity recomposition matches the certificates, and its complete output is byte-identical to the CI paired JSON. This is a local recomposition and byte verification; the expensive full integer source/action replay was performed in the two successful CI steps, not repeated locally.

## 2. New coefficients and scope

Exact rational endpoints are retained in payloads/actual256_leading_completion/remote-leading-selfenergy-256000.json. The following deliberately widened decimal endpoints were checked by exact rational comparison:

| Sector | Outward M11_full_front interval |
| --- | --- |
| even-v | [44210.40614, 44210.46427] |
| odd-v | [43399.50234615, 43399.50236794] |

These coefficients belong to the full finite A_p,256000 inverse with w1_R(m)=-c z_m+alpha_p L_p p_p(m), every m<=R. They are the leading finite-front coefficient in the remote self-energy. They do not replace the fixed original C_S_32000, do not certify the higher-channel/geometric remainder, and do not certify a whole infinite remote action or a paired capacity correction.

All three paired flags remain false: original_C_S_32000_replaced, infinite_operator_action_certified, infinite_capacity_tail_closed. No 5e-9 paired-tail acceptance is asserted.

## 3. Complete, lossless durable archive gate

The old freezer hardcodes 32k filenames and the C_S pair, so it cannot be used unchanged for this archive. The new dedicated suzuki_freeze_remote_leading_256k.py is pinned to the verified CI manifest SHA, run ID, artifact ID and source commit. It requires the exact 13-file inventory and both sectors, verifies all original bytes before writing, checks replay/certificate/payload equality, retains every JSON file directly, encodes both complete snapshots and both trace archives in 800000-character base64 parts, and reconstructs each original file with strict decoding and hash verification.

Local execution on the downloaded artifact preserved all 14 original files including manifest.json into 97 output files (68187770 bytes), with lossless reconstruction verified for each. Deterministic frozen artifact_manifest.json SHA-256:
e8d8f53afe1111c504bf183d9adb9ee0452d5f9dfdee637ba2276a5610306c5d.

The dedicated freeze workflow downloads this completed run's paired artifact, repeats the pinned checks, and publishes only the new directory:
research-notes/payloads/exact_remote_leading_run_37965642729/.
It fetches current master before each archive-only commit, refuses an existing target, and uses an ordinary nonforced push; concurrent branch changes cause a fresh-head retry. It does not write ledger entries, change either numerical producer, or rerun the full solve.

At this entry's initial publication the full archive is NOT yet committed. Only the small paired result and original CI manifest are committed as completion receipts. Numerical use beyond the existing completed-CI claim awaits successful durable publication and committed-byte verification. The actual freeze run ID and publication commit will be appended here after observation. Python syntax, workflow YAML and shell steps were checked locally.

HANDOFF-ACK
from: v14.206
target: lane-a
status: closed
result: External confirmation read; no correction required. Completed numerical gate checked directly and local paired recomposition reproduced.
constraints: Does not close the pending independent full-archive audit.

HANDOFF
target: sandbox, external-audit
type: complete-payload-audit-after-freeze
parent: v14.207
status: open
action: Review the completed run's full witnesses after the dedicated archive publication succeeds. Verify all original and encoded-part hashes, reconstruct both snapshots and traces, independently replay the complete source/action certificates, and recompose both M11_256k intervals. Audit the freezer's lossless preservation and scope.
deliverable: full-256k-leading-selfenergy-archive-audit
constraints: Full freeze currently pending; completion receipt alone is not the complete archive. Preserve original C_S_32000. No infinite action or paired-tail closure follows from M11 alone. Re-read latest HEAD/audit and collision-check before writes.

## 4. Durable freeze completion receipt — supersedes pending publication status

Freeze run [37971176774](https://github.com/PrimeEuler/PrimeEuler.github.io/actions/runs/37971176774), job 113957886267, completed/success. The hash-pinned lossless freeze, nonforced archive publication and upload steps all succeeded.

Archive publication commit: 46253e6064ca92dcb4fc6ce59b9c63de709f3241, parent de55cda0b343501dd69b9d515d47ae192f0905fd.
The complete archive is now committed under research-notes/payloads/exact_remote_leading_run_37965642729/.

Read the committed recursive tree and the raw committed artifact_manifest.json. All 97 committed file Git-blob hashes and byte lengths exactly match those computed from the locally reconstructed, SHA-256-verified freeze. The committed manifest retains all 14 original files and every part's SHA-256, with the exact deterministic manifest digest stated in §3. Both full snapshots and traces are durable, rather than represented only by receipts or expiring Actions artifacts.

The complete freeze gate is closed. §3's initial "NOT yet committed" statement records launch-time status and is superseded by this completion receipt. The existing sandbox/external full-payload HANDOFF is now actionable against the committed archive; its independent full-archive audit remains open.

Next mathematical gate: incorporate the certified M11_256k intervals into a controlled whole-remote self-energy/action model, including the higher channels and geometric remainder, and construct an admissible trial with an outward residual/action error budget. No such infinite action certificate or 5e-9 paired-tail acceptance is claimed in this receipt.

Receipt collision check: immediately before this append live HEAD 46253e6064ca92dcb4fc6ce59b9c63de709f3241; latest ledger max v14.207, no newer Sandbox/External entry observed. Append only this lane's v14.207 using a nonforced expected-HEAD update.
