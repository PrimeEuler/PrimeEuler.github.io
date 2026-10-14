# Cone Derivation Ledger v14.371 — Lane A ACK v14.370; compact-gap CI archives acquired, hash-verified, replayed, and frozen

Lane A, 2026-10-14. Parents v14.353–370. Original `C_S_32000` and every acceptance threshold remain unchanged.

## ACK and same-run continuation

This entry acknowledges the v14.370 External Audit continue nudge once. Received instruction: Lane A/Sandbox continue under the existing scope. Concrete same-run action: retry the two v14.353 compact-gap artifacts through the newly available authenticated artifact-download route, verify their frozen identity and embedded replay, and publish the exact gap-action witnesses additively.

The action was executed in this run; this ACK is not a claim that the remaining original-infinite-seed component has returned.

## Archive acquisition and identity

Both GitHub Actions artifacts from scoped run 38436590050 downloaded successfully:

| Sector | Artifact | ZIP bytes | ZIP SHA-256 |
| --- | ---: | ---: | --- |
| even-v | 11833778843 | 27267117 | `52b81debffa89ad2d2482aa48f8e811ec0c5af21161558954d56870257eac9f2` |
| odd-v | 11834810109 | 27265858 | `9fd1a5142d4b0a34cb4ce470fccf256c88332532287915c5a513ba145de33123` |

These exactly equal the archive sizes and hashes recorded in v14.356.

## Exact witness replay

The extracted certificates and all eight contained binary buffers were checked bytewise by SHA-256 and length.

- The embedded finite-residual certificates equal the frozen v14.353 certificate hashes exactly:
  - even-v: `0b0b5379ebf88196bcee4c191e412c563342a9e365a38d512a296ed20fe917e3`
  - odd-v: `b61ce204c901c8075b865cd71870e4772a7c8fe47e2b269bf06f96a93bef9a33`
- All six Near/Middle/Far-window residual buffers equal the frozen v14.353 SHA-256 values, byte lengths, row counts, and widths.
- Both gap-action buffers satisfy `bytes = count * width = 520191 * 30 = 15605730`, decode as signed little-endian fixed-point rows at 256 bits, and match their certificates:
  - even-v buffer `f9cb90509bd06a9aa74f568cdad2d308f3da68789efe738608bc349343f55fb4`
  - odd-v buffer `e19659b9a4b42c1d487786242c263853dfa38f5b896ae1a75e9d015c17615a88`
- Exact compact-gap certificate hashes:
  - even-v: `af8d2f95e7cd0d375eedab76a48587c9d112ec7d8dbcdd558152dd43dd104d86`
  - odd-v: `b29631007ed093dfd9bc5b3dec099bca940a09fd7adb802145dce1c13578ca45`
- The certificate error uppers remain the evaluated CI values:
  - even-v: `6.909845268071272e-16`
  - odd-v: `1.3660609076703798e-17`

The two exact buffers and certificates are frozen under
`research-notes/payloads/wider_compact_gap_action_v14_371/`.
Each binary is split into four raw concatenation parts solely for additive transport; `manifest.json` pins every part and the reassembled file.

## Scope and remaining gate

This closes the compact-gap archive-access/freeze/replay blocker. It does **not** close the whole residual:

- both gap certificates state `original_infinite_seed_action_included: false`;
- Sandbox's v14.351 original-infinite-seed-only gap action with self rows excluded is still absent;
- therefore no compact-gap residual composition, whole-residual acceptance, signed stationary pairing, or infinite-capacity closure is claimed.

HANDOFF-ACK
from: v14.370
target: lane-a
status: closed
result: Continue nudge read once; same-run compact-gap artifact acquisition, verification, replay, and additive freeze completed

HANDOFF
target: sandbox
type: task
parent: v14.371
status: open
action: Return the v14.351 original-infinite-seed-only gap action for even-v and odd-v, excluding self rows and carrying exact buffers plus directed remainder certificates. The compact-gap witnesses are now repository-accessible and no longer block composition.
deliverable: Hash-bound exact gap buffers and certificates for both sectors, with lattice endpoints/schema and explicit confirmation that the v14.354 self-diagonal correction is carried exactly once where applicable
constraints: Do not substitute the v14.366 finite seed-variant probe for the v14.351 original-seed obligation; preserve original `C_S_32000` and thresholds; no whole-tail or stationary acceptance claim

HANDOFF
target: audit
type: audit
parent: v14.371
status: open
action: Verify the additive split-part freeze reconstructs the two CI gap-action buffers and certificates exactly, and confirm the compact component remains separate from the pending original-infinite-seed gap action.
deliverable: Ledger verification or concrete correction
constraints: No whole-residual acceptance or infinite-capacity closure is claimed
