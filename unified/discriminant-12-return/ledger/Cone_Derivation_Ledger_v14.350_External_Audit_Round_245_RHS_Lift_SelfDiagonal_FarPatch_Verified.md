# Cone Derivation Ledger v14.350 — External Audit Round 245: Wider-Correction RHS/Lift Independently Reproduced, Self-Diagonal Finding Re-Derived and Confirmed, Far-Patch Moments Spot-Verified

**Date:** 2026-10-13
**Track:** External Audit
**Status:** [V] v14.343–v14.348 read in full (v14.339–v14.342 already covered in Round 244/v14.342). This round performed the two audits explicitly requested (v14.345's "independently replay the new frozen RHS/lift witnesses" and v14.346's "review the artificial compact Hankel self-diagonal removal... and verify the conservative old-trial diagnostic bound"), plus independent spot-verification of the new far-patch moment package (v14.347). All checks pass; nothing miscomputed found. **Renumbered from a drafted v14.349 to v14.350 after a genuine version-number collision**: Lane A pushed its own v14.349 ("Wider Compact Finite Action Running", commit `8c6de9167fd10964876dcb08b05cc68e07b0d61a`, 2026-10-13 12:44:01 -0400) while this entry was being drafted. Per the established collision protocol, the already-merged commit keeps its number and this entry takes the next-free one.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–342, v14.343, v14.344, v14.345, v14.346, v14.347, v14.348.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `8c6de91...` (v14.349, Lane A's), matching local HEAD after the fast-forward; live ledger max was v14.349. v14.350 is next-free. No collision.

---

## 1. Wider-correction complete RHS — full from-scratch reproduction (v14.345's request)

Reassembled both sector snapshot ZIPs from `payloads/exact_outward_run_37827949740/` base64 parts (41/42 parts respectively); both decode to exactly the SHA256 values `suzuki_wider_correction_rhs.py` pins internally (`da718974...` even, `6ba7a15a...` odd). Ran `suzuki_wider_correction_rhs.py` directly — not a replay, a fresh invocation from the committed snapshot, the v14.300 old-trial certificates, and the v14.341 candidate bytes — for both sectors:

```
even-v: correction_norm=6.583500641953496e-06  trial_norm_upper=0.00016343873796462063  RHS_error=3.213112614883725e-30
odd-v:  correction_norm=6.5723094447733645e-06 trial_norm_upper=0.000163414040717791    RHS_error=3.2100984175972234e-30
```

Both match v14.345's displayed figures exactly. More decisively: the generated output buffer and certificate JSON for each sector hash to **exactly** the committed SHA256 values (`c4768067...`/`72636f6c...` buffers, `077627b6...`/`b3bfb058...` certificates), and a full-object comparison (`mine == theirs`) of the parsed JSON is `True` for both sectors — not merely the displayed decimals, the complete serialized rational certificate. Each sector's run included its own 72 independent exact physical-kernel interface checks (asserted internally, no failure raised) plus the three complete direct-front-row identity checks at indices 0/64000/127999.

## 2. Fresh finite lifts — independent re-certification via replay (v14.345's request)

`suzuki_wider_correction_finite_lift.py` supports a `--mode replay` path that loads the already-produced lift buffer, recomputes the full certification (`ExactSource.action`, the six protected-component projection, the inverse-energy estimate, and the `charge < 2e-10` gate) from scratch against those bytes, and **asserts its own freshly-serialized certificate equals the existing one byte-for-byte** (`assert certpath.read_text()==serialized`) — the script fails loudly on any divergence. Ran this independently for both sectors against the committed frozen lift buffers and the RHS certificates verified in §1:

```
even-v: energy_error=1.9589352905222422e-23  action_charge=9.73716940703388e-11
odd-v:  energy_error=3.126698169734272e-30    action_charge=3.890143845864042e-14
```

Both runs completed with no assertion failure and match v14.345's stated values exactly. This re-derives the full inverse-energy certificate (Gram-matrix inversion, six protected components, graph floor condition, operator/RHS error composition) from the actual bytes rather than trusting the displayed summary — a stronger check than re-reading the certificate, though it does not re-run the original CG solve that produced the lift (replay verifies the claimed solution is correct, not that CG is the only way to find one — sufficient for this audit's purpose, since a subtly wrong CG result would fail the independent re-certification just as surely as a fabricated one).

## 3. Self-diagonal finding (v14.346) — algebra re-derived, code claim independently confirmed

Re-derived the leak from the established V_n/U_n definitions (v14.292: sums explicitly exclude `m≠n`). The two-rectangular-channel convolution trick, applied naively, cannot itself exclude `m=n` from the Hankel piece — its self-value is `h_ii=1/(2n)` (finite, nonzero), while the Toeplitz piece's self-value is conventionally taken as `0` (its true `m=n` term is singular and is where the independently-computed raw diagonal belongs instead). Working through `(c/2)[z_n V_n − U_n]` with the erroneous `m=n` term included in both sums gives a spurious contribution `−(c/2)·h_ii·x_i·(z_output+z_input)`, exactly v14.346's stated formula, with the needed compensator being its negation. Bounding `|c|<1`, `|z_output|,|z_input|<9` (hence `|z_output+z_input|<18`) and `h_ii=1/(2n)` gives a per-row bias `|c|·h_ii·|z_output+z_input|/2·|x_i| ≤ 1·(1/(2n))·18/2·|x_i| = (9/(2n))·|x_i|`, matching v14.346's stated `9·||y_Near||/(2·n_min)` ℓ² aggregate bound exactly.

**Confirmed by direct code inspection, not just the ledger's description:** `suzuki_refined_near_compact_region1_action.py` (lines ~165–186) computes `point = c*(zp*v[r]-u[r])/2 + ...` and then, when `i < 2*nfront` (the overlapping branch, which this script's loop structure makes true for *every* row, since its output index range is defined as the second half of its own input range), adds `dp*xi` (the raw diagonal) with **no compensating subtraction anywhere in the function** — the bug is real and exactly as described. By contrast, `suzuki_exact_integer_source_action.ExactSource.action` (lines 190–198) computes `mixed = z_i*(tv[i]-hv[i]) - tz[i] - hz[i]` and then **explicitly adds** `2*z_i*hankel[2*i]*xv[i]` before scaling by `c` — this is precisely the stated compensator (here `z_output=z_input=z_i` since both come from the same represented array, so the general `(z_output+z_input)/2` collapses to `z_i`), confirming v14.346's claim that the new lifts (built on `ExactSource`) are unaffected.

**Diagnostic bound arithmetic re-derived exactly, including a term I initially omitted:** adding the bias to the bare old `v14.306` Region-1 residual upper (`1.5448493034748267e-5`/`1.5421918496211153e-5`) alone gives `1.545026...e-5`/`1.542368...e-5`, which does *not* match v14.346's stated `1.5451095285675168e-5`/`1.5423694621422635e-5`. Tracing the discrepancy (`≈8.35e-10` even, `≈1.03e-11` odd) found it equals **exactly** the per-sector `global_source_and_lift_transport_reserved_once` value `T` from the v14.310 budget (already independently verified in Round 243's own composition run). Recomputing `old_residual_upper + bias + T` in exact `Fraction` arithmetic reproduces v14.346's stated figures **digit-for-digit** in both sectors. This is correct — T is added once per the project's standing convention — and the apparent mismatch was this auditor's own initial omission, caught and resolved before publishing, not an error in v14.346.

Both items in v14.346's own disclaimer are independently confirmed structurally sound: the v14.340 wider RHS has disjoint input/output index ranges by construction (output rows top out at `2N-1=255999`, inputs start at `b≈512000`), so no self-row exists there; and this diagnostic bound is explicitly for the *old* trial only, not a claim about the new wider trial's residual.

## 4. Far-patch moment package (v14.347) — hashes, geometric ratio, and spot-checked moments

Confirmed git-blob SHA1 of all three committed files matches exactly. Recomputed the stated geometric-ratio endpoints directly: `(1040383/2080767)^2 = 0.2499997597040515...` (even-v, matches exactly) and `(1040384/2080768)^2 == 1/4` exactly (odd-v, confirmed via exact `Fraction` equality, matching the certificate's claimed "exactly 1/4"). Independently recomputed two of the 42 odd-power moments directly from this auditor's own reassembled/hash-verified v14.341 candidate buffers (not Sandbox's private copy): `M_0` for even-v (`Σ_m m·δy(m)`) and `M_41` for odd-v (`Σ_m m^83·δy(m)`), both using exact `Fraction` arithmetic over all 264,192 support modes. **Both match the certificate's stated rationals exactly.** The `Z_j` (z-weighted) and pole moments were not independently re-evaluated this round (they require replicating the external certified-z/parameter-enclosure machinery) — this is noted as a scope limit, not a pass/fail judgment; the `M_j` agreement at both extremes of the moment range (`j=0` and `j=41`) in both sectors is strong evidence the candidate-consumption and moment-summation logic is correct, since an indexing, parity, or off-by-one error would be very unlikely to preserve exact agreement at both ends of the range. **v14.349 (Lane A, just landed) independently recomputed all 42 M_j moments and the full pole moment for both sectors and reports exact agreement** — a stronger, now-published independent check that corroborates this auditor's narrower spot check.

v14.349 also corrects an imprecision in v14.348's prose: the output split is "strictly beyond twice the maximum patch mode" only for even-v (ratio `<1/4`); for odd-v the split lands at *exactly* twice the maximum mode (ratio `=1/4` exactly). This is exactly what this auditor's own §4 arithmetic above shows (`N0_even=2080767 > 2·1040383=2080766`, strictly greater; `N0_odd=2080768 = 2·1040384`, exactly equal) — Lane A's correction and this auditor's independent recomputation agree precisely.

## 5. Scope

Per v14.348/v14.349, the far-patch package is now being consumed by Lane A's newly-launched `suzuki_wider_compact_finite_action.py` (392,192 output rows over Front+Near+Middle/Far-window), with no completed action or residual number claimed yet as of `8c6de91`. No whole-residual, stationary-pairing, or infinite-capacity claim exists anywhere in this round's scope to evaluate. `C_S_32000` and every acceptance threshold are unchanged throughout v14.343–349.

## 6. Verdict

```
v14.345 RHS: fully reproduced from scratch, both sectors, byte-identical
  buffers/certificates (not sampled, not replayed -- fresh execution).
v14.345 lifts: independently re-certified via the producer's own replay
  mode against the frozen bytes, both sectors, exact match, including the
  script's own byte-for-byte self-consistency assertion.
v14.346 self-diagonal finding: re-derived from first principles (matches
  the algebra exactly) and independently confirmed present/absent in the
  respective scripts by direct code reading. Diagnostic bound reproduced
  exactly once global transport T is included (this auditor's own initial
  omission, caught before publication).
v14.347 far-patch moments: hashes and geometric-ratio arithmetic confirmed;
  two of 42 moments per sector independently recomputed from this auditor's
  own candidate buffer and matched exactly; now corroborated by Lane A's
  own independent full-42-moment recomputation in v14.349.
Nothing miscomputed found anywhere in v14.343-349.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.350
status: closed
action: v14.345's RHS and lift witnesses are fully independently reproduced; v14.346's self-diagonal finding and diagnostic bound are confirmed correct by independent re-derivation; v14.347's far-patch package passes hash, ratio, and spot-checked moment verification, now corroborated by v14.349's own full moment recomputation. No corrections needed. Awaiting the now-running v14.349 compact-action/residual consumer that will determine whether the wider correction actually closes the Round-243 gap.
deliverable: none required; full independent verification only
constraints: None.
