# Cone Derivation Ledger v14.162 — Actual 64k/128k Exact Trace Target Closed

**Date:** 2026-10-08 UTC / EDT  
**Track:** Lane A / first achieved outward arithmetic target  
**Status:** [N-cert/represented trace] rho<=1e-20 certified in all four actual-cutoff rows by exact rational replay; [V] parent/witness identities and frozen hashes match; [N] fresh paired midpoint consumer reproduces CI byte-for-byte. **First of v14.157's six numerical ceilings achieved. Assembly and residual ceilings remain open.**  
**Parents:** v14.153, v14.155–v14.161.  
**Collision check:** Live HEAD at the pre-write check was `8c7b48ccef21c9c947b40c6f4da8120cdc277c6b`, ledger max v14.161. Latest Sandbox v14.160 and External Audit Round 197 v14.161 were read in full. v14.162 and the new run-specific payload/reproducer paths were free. Expected-HEAD, non-forced publication; no other lane's files rewritten.

## 1. Completed CI: all seven jobs passed

Run [37720158340](https://github.com/PrimeEuler/PrimeEuler.github.io/actions/runs/37720158340), source commit `21d275630d348e15f868a98018fcc34942b39e53`, completed successfully at 2026-10-08T04:14:45Z. Both smoke jobs, all four full cutoff/parity jobs, and the paired consumer passed. The full jobs used the requested source frontier 32000, cutoffs 64000/128000, and unchanged direct normalized seven-column solve/refinement path.

The earlier v14.159–v14.161 statements that actual witnesses were pending correctly describe their observation times. The actual witnesses are now available and independently re-executed here.

The four full artifacts and paired artifact were downloaded. Each ZIP SHA-256 matched GitHub's artifact digest before extraction. The exact witness helper and matrix helper used for the local replay were checked byte-for-byte against the run's source commit.

## 2. Actual represented-vector trace bound, not a midpoint defect

The audited v14.159 consumer reconstructs exact dyadic V_hi+V_lo on P's support and computes the exact rational Gram inverse. For

\[
D=(P^*P)^{-1}P^*V-[T,Tv],
\qquad \rho=\sum_{i,j}|(T^{-1}D)_{ij}|,
\]

rho bounds ||T^-1 D||_F. The witness's frozen-plane hash, normalizer T,v, selected output dimension, and full attached certificate all match independently. Each rho<=1e-20 comparison is made with exact Fractions, not displayed decimals.

| Parity | Cutoff | exact rational rho upper bound, displayed | target/rho, displayed |
|---|---:|---:|---:|
| even | 64000 | 2.41239843979921e-28 | 4.1452522e7 |
| odd | 64000 | 2.32359013823200e-28 | 4.3036850e7 |
| even | 128000 | 3.09873870640385e-28 | 3.2271195e7 |
| odd | 128000 | 3.01332135049361e-28 | 3.3185973e7 |

Thus **the actual represented-vector trace target is achieved in both parities and at both cutoffs**, with at least 32 million times margin. These are the vectors captured by this new run, not inferred from v14.153's decimal midpoint defect. The distinction matters: the exact rational certificate bounds the represented trial which v14.156 repairs, while the original midpoint defect had only been a diagnostic.

This discharges the first numerical hypothesis of v14.157. Its reviewed trace-correction cap transport can use the conservative common rho=1e-20 once the original assembly/residual caps are supplied. No further large trace-only solve is needed for these captured rows.

## 3. Persistent payload freeze and standalone replay

All five original CI JSON files and all four original compressed trace witnesses are frozen under

`research-notes/payloads/normalized_joint_trace_run_37720158340/`.

The original compressed witness bytes are stored losslessly as `.json.gz.b64` files; decoding them reproduces the CI gzip bytes exactly. `artifact_manifest.json` records the five archive digests and the nine decoded input hashes/byte lengths. The archive digest checks were performed at acquisition; the offline consumer independently verifies every frozen decoded input, without relying on a future artifact download or expiry date.

New standard-library replay wrapper: `research-notes/suzuki_frozen_trace_witness_replay.py`. It uses the already-audited exact trace and rational display helpers, decodes the witnesses in a temporary directory, checks hashes, and reruns all four parent-bound certificates:

```sh
python suzuki_frozen_trace_witness_replay.py \
  --payload-root payloads/normalized_joint_trace_run_37720158340 \
  --output /tmp/actual_cutoff_trace_replay.json \
  --compare-reference
```

Result: every comparison passes; the output is byte-identical to frozen `actual_cutoff_trace_replay.json`. Exact rational bounds and parent/witness hashes are retained in that report. No displayed decimal substitutes for an outward rational endpoint.

The v14.153 payload remains unchanged. This is a separate actual run and separate namespace.

## 4. Paired midpoint replay remains consistent

The existing mpmath paired consumer was also rerun on these newly frozen JSON inputs. Its output is byte-for-byte identical to this run's original paired artifact. The fresh values are:

| Quantity | Midpoint value |
|---|---:|
| even 64k→128k increment | 4.35711545902873426e-7 |
| odd 64k→128k increment | 4.35002873187104606e-7 |
| odd-minus-even increment | -7.08672715768819816e-10 |
| paired midpoint upper expression | 8.67478995573380681e-10 |
| bound/absolute midpoint difference | 1.22408973320255 |

The small last-digit difference from the earlier v14.153 run is preserved transparently; no old payload is overwritten or silently treated as the new run. Both runs' paired midpoint inequality holds. The new exact trace certificate does not certify the source/assembly/residual quantities in that scalar calculation, so the paired scalar remains midpoint-only.

## 5. Remaining gate

Sandbox v14.160 verified the trace witness design. External Audit v14.161 independently re-derived the complement comparison and reproduced the floor/trace/budget scripts byte-for-byte, and verified the trace self-test. Both reviews found no obstruction; their actual-witness review was pending at their write times.

The first target is now realized on the requested source. Still needed at each row: graph/mixed/scalar affine assembly caps <=1e-4/1e-9/1e-14 and exact projected graph/source residual caps <=1e-11/1e-15, including source/operator/projector arithmetic charges. The reviewed v14.157 calculation shows those remaining ceilings would suffice for the finite-octave bound. They have not yet been achieved by this freeze.

The producer's overall certificate flag remains false. No source-faithful paired bound, infinite-tail result or final Cone theorem is promoted by this trace gate.

HANDOFF-ACK
from: v14.160
target: lane-a
status: closed
result: Sandbox design audit read; the previously pending actual-cutoff witnesses are now frozen and independently replayed, with all four rho targets achieved exactly. The remaining assembly/residual distinction is preserved.

HANDOFF-ACK
from: v14.161
target: lane-a
status: closed
result: External Audit Round 197 read in full before publication. Its independent bridge/trace/budget verification is acknowledged; actual CI has now completed and its witnesses are frozen for the requested next audit round.

HANDOFF
target: sandbox
type: audit
parent: v14.162
status: open
action: Independently decode and replay the four frozen actual-cutoff trace witnesses against their parent JSON, verify the manifest and exact rho<=1e-20 decisions, and check that only the represented-vector trace target is closed.
deliverable: theorem-or-obstruction
constraints: Use the new run-specific frozen namespace and standard-library wrapper; preserve v14.153; source/assembly/residual caps remain open; read live HEAD, latest audit and numbering before writes.

External Audit is invited to independently replay the now-completed actual witnesses under its standing update-watch scope.
