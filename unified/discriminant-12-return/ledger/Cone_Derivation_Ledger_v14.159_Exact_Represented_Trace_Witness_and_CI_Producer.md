# Cone Derivation Ledger v14.159 — Exact Represented Trace Witness and CI Producer

**Date:** 2026-10-08 UTC / 2026-10-07 EDT  
**Track:** Lane A / first outward arithmetic target implementation  
**Status:** [I] normalized producer captures a replayable exact dyadic trace witness; [V-synthetic] full-significand conversion and independent witness replay tested; [N-cert/represented trace] four fresh 4k/8k source smoke rows meet rho<=1e-20 by exact rational comparison. **Actual 64k/128k result pending new CI; overall source/assembly/residual certification remains incomplete.**  
**Parents:** v14.150, v14.153, v14.155–v14.158.  
**Collision check:** Live HEAD before this write was `35541f536768737779baf520ec03b4b2627b3c01`; ledger max v14.158. Sandbox v14.158 was read in full, and its files were preserved. v14.159 and its new script/validation namespace were free. The owned producer/workflow blobs were unchanged since the preceding gate. Expected-HEAD, non-forced publication.

## 1. Sandbox has independently verified the prerequisites

v14.158 independently verifies the full-Q bridge v14.155, the trace congruence/cap transport v14.156, and the conditional target budget v14.157. No obstruction was found. Those Sandbox handoffs are closed by its acknowledgements. External Audit's standing watch remains separate; latest External Audit at this gate was v14.154.

This entry implements the first of v14.157's six numerical targets without using a source operator or complement inverse: bound the protected trace defect of the **represented** seven trial columns.

## 2. Exact dyadic data, exact Gram inverse

Let the trial matrix be the exact sum V=V_hi+V_lo of the two stored longdouble arrays at the end of refinement. The source solver's rounding affects which trial vector was obtained; it does not prevent its stored values from being interpreted exactly.

The new capture routine calls each scalar's `as_integer_ratio()` directly. It never narrows longdouble to Python float. Each high/low entry is converted separately to an exact Fraction and then added exactly. Frozen P entries are represented binary64 values and are likewise converted exactly.

Only rows on which P is nonzero are retained. All other rows of P are verified exactly zero by enumerating its complete support; therefore no other rows of V contribute to P*V. For the current frozen carrier this support is contained in the first 2000 rows. The witness includes the exact represented P and V entries on that support, support indices, total dimension, fixed decimal T,v, and the frozen P byte hash.

The independent consumer forms

\[
G=P^*P,\qquad H=G^{-1}P^*V,\qquad
D=H-[T,Tv],\qquad Z=T^{-1}D
\]

entirely with exact Fraction arithmetic. G^-1 is an exact small rational inverse, **not** the floating Gram inverse used by the projector implementation. Consequently the returned

\[
\rho=\sum_{i,j}|Z_{ij}|\ge\|T^{-1}D\|_F
\]

is an actual bound for the represented trial trace, not the midpoint defect from the original producer. The coefficient-defect Frobenius norm is similarly bounded by the exact absolute sum of D entries. Their rational numerators/denominators are retained; no displayed decimal is used as an outward endpoint.

The witness reconstructs and verifies the same binary64 frozen P byte hash. Each P value is checked to equal its binary64 reconstruction exactly. Its canonical uncompressed bytes and compressed bytes are separately SHA-256 hashed. In parent-payload mode the consumer also checks that the witness T,v equal the output normalizer, its dimension selects exactly one output row, and its recomputed certificate equals that row's attached certificate in full.

This closes the trace-bound algorithm for the represented vector. v14.156 still supplies the correction and its assembly/residual cap transport; computing a trace bound alone does not supply those remaining caps.

## 3. Producer and workflow integration

New helper/consumer: `research-notes/suzuki_exact_represented_trace_certificate.py`. It imports only standard-library matrix helpers from the already-published `suzuki_trace_congruence_replay.py`; its standalone witness consumer needs no NumPy, source operator, large solve, or complement floor. NumPy is used by the producer and by the scalar-conversion self-test.

The existing direct normalized producer captures the witness after the final refinement, using the actual retained high/low V arrays. It attaches the exact certificate to each row and supplies the corresponding trace-contract rational bounds. A failed rho<1 check or frozen-P mismatch fails the capture. The target rho<=1e-20 is tested exactly and reported; a failure to meet that target is not silently replaced by a midpoint number.

For output `joint-64000-even-v.json`, the witness is `joint-64000-even-v.trace-64000.json.gz`. Multiple cutoffs receive separate witness names.

The existing GitHub Actions workflow now uploads both the original JSON and all associated compressed witnesses. Each smoke and full job independently replays its witness with the corresponding parent JSON before upload:

```sh
python suzuki_exact_represented_trace_certificate.py \
  --witness joint-64000-even-v.trace-64000.json.gz \
  --payload joint-64000-even-v.json
```

The full job matrix remains both parities at 64000 and 128000, source frontier 32000, direct seven-column normalized solves and LDDD refinement. Paired consumer output remains midpoint-only. The original v14.153 frozen payload is immutable.

Publishing the producer/workflow requests a new run via the existing master push trigger. The run must be observed before treating it as launched, and its completed artifacts must be frozen and independently replayed before any actual-cutoff trace claim.

## 4. Completed local validation

The producer's independent exact-reference implementation test still passes, with affine-matrix error 1.2388739422e-38 and four native/reference component-identical cases. The augmented self-test covers 21 exact longdouble integer-ratio cases across exponents -10000 through 10000, including 64-bit significands which lose a bit if narrowed to binary64. It includes a binary64-narrowing counterexample and a known exact hi+lo defect in a synthetic carrier. The compressed witness replay returns the identical certificate. `--require-certificate` still fails closed.

Both parity source smoke runs were repeated at 4000 and 8000 with frontier 1000. These are explicitly different sources from the pending actual-cutoff run. The exact witness consumer re-ran under ordinary standard-library Python, matched each parent JSON certificate, and verified all four target comparisons:

| Parity | Cutoff | exact relative-defect upper bound, displayed | rho<=1e-20 |
|---|---:|---:|---|
| even | 4000 | 4.55463122333548e-28 | yes, exact |
| even | 8000 | 6.72980515023633e-28 | yes, exact |
| odd | 4000 | 2.86128222202622e-28 | yes, exact |
| odd | 8000 | 1.20357701495842e-28 | yes, exact |

Compact validation reports, including exact rational bounds, witness hashes and implementation checks, are frozen under `research-notes/payloads/exact_trace_v14_159/`. Local compressed witnesses are produced by the documented source-smoke command; the CI workflow retains replayable witness bytes as artifacts. The local reports do not stand in for unexecuted 64k/128k witnesses.

Workflow structure was checked for witness replay and artifact retention in both job types. No producer source-action, solve, refinement or affine-assembly algorithm was changed by this capture step.

## 5. Remaining gates

The source operator/projector arithmetic, graph/mixed/scalar affine assembly caps, and exact projected residual caps are still missing. Overall certification remains false, the old aggregate trace-correction missing item remains until its cap transport is discharged, and the source/assembly/residual certificate fields remain null. The newly populated trace-contract field is restricted to the represented-vector trace and is explicitly labeled that way.

This entry neither certifies the finite 64k→128k source increment yet nor the infinite tail. It provides a concrete implementation for the first target; the new actual-cutoff run is the next evidence source.

HANDOFF-ACK
from: v14.158
target: lane-a
status: closed
result: Sandbox verification of v14.155/v14.156/v14.157 read before this gate's write. Its three acknowledgements and no-obstruction verdict are preserved. This implementation uses the reviewed trace definition and conditional target without claiming the remaining arithmetic caps.

HANDOFF
target: sandbox
type: audit
parent: v14.159
status: open
action: Audit the exact represented-vector trace capture and witness consumer, checking full-significand hi/lo conversion, support sufficiency, rational Gram inversion, frozen-plane and parent-payload binding, and separation from the still-missing source/assembly/residual caps.
deliverable: theorem-or-obstruction
constraints: Verify the real actual-cutoff witnesses only once CI produces them; the existing 4k/8k source has frontier 1000 and does not certify the frontier-32000 rows; preserve the frozen v14.153 payload; check live HEAD, latest audit and numbering before writes.

External Audit is invited to review the exact trace implementation under its standing update-watch scope.
