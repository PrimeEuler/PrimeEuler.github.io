# Cone Derivation Ledger v14.170 — External Audit Round 200: v14.168's Actual 64k/128k Five Caps and Finite Paired Interval Independently Verified

**Date:** 2026-10-08
**Track:** External Audit
**Status:** [V] v14.168's actual 64k/128k five-cap witnesses and the exact finite paired capacity-increment interval are independently re-executed from the frozen namespace, byte-identical (SHA-256-matched) to the committed reference; all manifest hashes verified; all five caps on all four rows and the trace/rho bound independently decoded and cross-checked to full displayed precision; the T0 antisymmetry resolution is independently confirmed by direct inspection of the production source plus a standalone numerical test. `overall_certificate_ready` remains correctly `false` (finite-octave numerical closure only; no infinite-tail or final Cone theorem).
**Parents:** v14.155–v14.169.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `beb835d6c11dcc28f889faf992fb6180ea6ceee9` (v14.169), identical to local HEAD; live ledger max was v14.169. v14.170 is next-free. No collision.

---

## 1. Independent fresh re-execution: byte-identical, all targets pass

Ran, from scratch and read-only against the committed frozen namespace:

```
python suzuki_frozen_outward_witness_replay.py --payload-root payloads/exact_outward_run_37791856005 --output /tmp/outward_replay_audit200.json --compare-reference
```

Summary fields: `all_rows_meet_all_six_numerical_targets_exactly: true`, `all_certificates_byte_identical: true`, `reference_byte_identical: true`, `overall_certificate_ready: false` (correctly still false — pending exactly this review). This thread's full output JSON is **SHA-256-identical** to the committed `outward_replay.json` in that namespace (`41513e2377ee96bb...`, both files), confirmed by direct hash comparison, not merely a structural diff.

## 2. Manifest integrity: all 75 files hash-verified

Independently recomputed SHA-256 and byte length for every one of the 75 files listed in `artifact_manifest.json` (original JSONs, four full certificates, all base64 ZIP parts) against the manifest's recorded `sha256`/`bytes` fields: **0 mismatches, 0 missing**, across all 75 entries.

## 3. All five caps, all four rows: independently decoded and cross-checked against v14.168 §3

Extracted `bounds_display` directly from this thread's own fresh run (not the committed file) for all four rows:

```
                graph assembly        mixed assembly       scalar assembly       graph residual        source residual      target met
even/64000:  3.5913960930850545E-7  1.0493269452273822E-11  3.0659025332802595E-16  6.1927560229796172E-14  1.8080597649215486E-18   all True
even/128000: 4.6557759572539693E-7  1.3603153303794324E-11  3.9745421924398739E-16  1.0170062850148387E-13  2.9703610953627135E-18   all True
odd/64000:   1.4264616914350998E-10 4.1375269287244950E-15  1.2001113796962579E-19  4.7435455621309889E-15  1.3749638438227855E-19   all True
odd/128000:  1.8492212707238369E-10 5.3637632547232818E-15  1.5557876554955659E-19  1.4265802371414913E-14  4.1341423125130198E-19   all True
```

Every value matches v14.168 §3's table to every displayed digit. Checked against the stated targets (1e-4, 1e-9, 1e-14, 1e-11, 1e-15): all 20 cap values clear their targets with comfortable margin (worst case even/128000's graph assembly at 4.66e-7 vs 1e-4 — still four orders of margin).

## 4. Trace/rho bound: independently decoded, well inside target

Decoded `relative_trace_fro_upper_rational` (exact Fraction) to 40-digit decimal for all four rows:

```
even-v / 64000:  2.4124017071E-28  (<= 1e-20: True)
even-v / 128000: 7.8019274394E-28  (<= 1e-20: True)
odd-v  / 64000:  1.7608418313E-28  (<= 1e-20: True)
odd-v  / 128000: 3.0133255983E-28  (<= 1e-20: True)
```

All four rows meet the trace ceiling with eight orders of margin beyond the stated 1e-20 target (actual values are ~1e-28). `checks_exact['relative_trace']` is `True` on all four rows, consistent with these decoded values.

## 5. Exact finite paired interval: independently decoded, matches v14.168 §4 exactly

Decoded the exact Fraction strings from this thread's own fresh run (`sys.set_int_max_str_digits(0)` was required — the exact numerators/denominators run to ~11,000 digits, consistent with the claimed exact-rational composition rather than a truncated decimal):

- Point odd-minus-even increment: `-7.08672716165404856100801210088206080234460969484872...E-10` — matches v14.168 §4's `-7.0867271616540485610080121008820608023446096948487E-10` to every displayed digit.
- Endpoint error cap sum: `6.5305944913130759233738152989491665261577067922525E-15` (field `endpoint_error_sum_display`, cross-checked numerically) — matches v14.168 §4 exactly.
- Decoded interval endpoints: `[-7.08679246759896169176724583903505029400987127191664...E-10, -7.08666185570913543024877836272907131067934811778079...E-10]` — matches v14.168 §4's stated interval to every displayed digit.
- Strictly negative (upper endpoint $<0$): independently recomputed in this thread's Decimal arithmetic as `True`, agreeing with the certificate's own `source_interval_strictly_negative_exact: True`.
- Absolute bound $\le 9\times10^{-10}$: independently recomputed as `max(|lower|,|upper|) <= 9e-10` → `True` by direct Decimal comparison, agreeing with `source_abs_bound_le_9e_minus10_exact: True`. This is not a floating-point coincidence: the comparison was done on the exact Fraction values decoded from the certificate's own rational strings, matching the certificate's claim that the decision is "true by rational comparison."

## 6. T0 antisymmetry: independently confirmed by direct source inspection and numerical test

v14.168 §1 resolves v14.167's symmetry flag by citing `ExactSource.__init__`'s construction. Located and read that constructor directly in `suzuki_exact_integer_source_action.py`:

```python
self.toeplitz = [(-1 if k < 0 else 1) * (scale // (2 * abs(k))) if k else 0
                 for k in range(-n + 1, n)]
```

This is exactly $T_0(k)=\mathrm{sign}(k)\cdot\lfloor \mathrm{scale}/(2|k|)\rfloor$ for $k\ne0$, $T_0(0)=0$, with `scale`$=2^{256}$. Hand-verification: for $k>0$, $T_0(k)=\lfloor \mathrm{scale}/(2k)\rfloor$; for $k=-m$ ($m>0$), $T_0(-m)=-1\cdot\lfloor\mathrm{scale}/(2m)\rfloor=-T_0(m)$. The `abs()` is applied *before* the floor, so this is signed-magnitude truncation toward zero, not Python's native floor-division on a negative operand (which would floor toward $-\infty$ and break exact antisymmetry). This confirms v14.168 §1's claim exactly, independent of trusting its prose description.

Also ran a standalone numerical test reconstructing this exact list comprehension in isolation (not importing the production module) for $k=-49,\dots,49$: antisymmetry $T_0(k)=-T_0(-k)$ held for every tested $k$, and $T_0(0)=0$. Also independently confirmed the Hankel sequence `scale // (2*(k+self.start))` matches $H_{0,ij}=\lfloor \mathrm{scale}/(2(i+j+a))\rfloor$ with $a=$ `self.start` $\in\{1,2\}$, consistent with v14.165 §2's stated formula. No obstruction; the v14.167 flag is correctly closed.

## 7. Scope note

This round verifies exactly what v14.168 itself describes as the open independent-audit gate: the actual 64k/128k endpoint evidence and the resulting finite paired interval, plus the T0 symmetry resolution it supplied in response to v14.167's flag. It does not extend the result beyond the finite 64k-to-128k octave, does not certify any infinite-tail claim, and does not alter `overall_certificate_ready`'s meaning — this entry's own independent confirmation is the condition v14.168 named for that flag, and is recorded here rather than by editing any prior frozen output.

---

## 8. Verdict

```
Replay of suzuki_frozen_outward_witness_replay.py against
  payloads/exact_outward_run_37791856005: INDEPENDENTLY RE-EXECUTED,
  SHA-256-identical to the committed reference output.
Manifest integrity: all 75 files hash- and length-verified, 0 mismatches.
Five caps x four rows (20 values): independently extracted from this
  thread's own fresh run, match v14.168 Sec.3 to every displayed digit,
  all clear their targets (1e-4/1e-9/1e-14/1e-11/1e-15).
Trace/rho bound: independently decoded on all four rows, ~1e-28,
  well inside the 1e-20 target.
Exact finite paired interval: independently decoded from this thread's
  own Fraction strings (~11,000-digit numerators/denominators),
  matches v14.168 Sec.4's point value, interval, strictly-negative
  decision, and <=9e-10 decision exactly, by rational comparison.
T0 antisymmetry: independently confirmed both by direct inspection of
  the production ExactSource.__init__ source and by a standalone
  numerical reconstruction; v14.167's flag is correctly closed.
No obstruction found. No ledger content is altered by this entry.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.170
status: open
action: No correction found in v14.168's actual-cutoff evidence or finite paired interval. Independently re-executed and SHA-256-matched; all manifest hashes verified; all five caps on all four rows and the trace bound independently decoded and matched to full displayed precision; the exact paired interval independently decoded and matched exactly; the T0 antisymmetry resolution independently confirmed by direct source inspection and a standalone numerical test. This satisfies the independent-audit gate v14.168 named for this specific actual-cutoff evidence and interval; `overall_certificate_ready`'s broader meaning and any further (e.g. infinite-tail) claims remain untouched by this entry.
constraints: None.
