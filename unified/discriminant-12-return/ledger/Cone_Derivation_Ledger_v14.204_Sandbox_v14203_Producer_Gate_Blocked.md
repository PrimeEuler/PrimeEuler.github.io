# Cone Derivation Ledger v14.204 — Sandbox: v14.203 Producer Gate Audited; Cutoff Assert Blocks 256k Launch

**Date:** 2026-10-09
**Track:** Sandbox / v14.203 handoff response (source-contract audit)
**Status:** [F] Concrete defect found: the workflow passes `--cutoff 256000` but the producer asserts `k.cutoff==32000`; CI run 37960118305 failed on both parity jobs as a direct consequence. No numerical M11_256k exists. Fix required before re-launch.
**Parents:** v14.179/v14.181/v14.185–188, v14.195–203.
**Collision check:** live ledger max v14.203 at write time; v14.204 is next-free. No collision.

---

## 1. The defect

v14.203 §2 states the workflow "runs the already-audited
`suzuki_normalized_leading_source_producer.py` independently for
even-v and odd-v with cutoff 256000" and claims "this is within the
existing leading certificate's explicitly supported 8000≤R≤256000
range."

The producer at HEAD
(`research-notes/suzuki_normalized_leading_source_producer.py`,
61 lines, blob `c6aea1b468e4`) contains, line 22:

```python
assert k.cutoff==32000
```

The workflow (`.github/workflows/suzuki-remote-leading-selfenergy-256k.yml`)
invokes:

```
python suzuki_normalized_leading_source_producer.py
  --sector ${{ matrix.sector }} --cutoff 256000 ...
```

`--cutoff 256000` trips `assert k.cutoff==32000` immediately.
The "8000≤R≤256000" range cited in v14.203 belongs to the
*certificate* (`suzuki_exact_leading_source_certificate.py`),
not to this producer, which is hardcoded to the 32k
leading-source configuration it was written for (v14.179/181).

## 2. Observed consequence

GitHub Actions run 37960118305 (source `1d8efe252d2b`):
- `full (odd-v)` — completed/failure
- `full (even-v)` — completed/failure
- `paired` — completed/skipped (needs `full`)

Both producer jobs failed; the collector never ran. No M11_256k
value was produced. (Job logs could not be fetched directly —
the log-download host returns 401 in this environment — but the
assert/workflow mismatch is determinative on its own.)

## 3. What the fix requires

Option A: generalize the producer to accept 256000 (remove or
parameterize the assert; verify the 256k code path — anchor root,
mode counts, memory — actually works at that scale).

Option B: write a dedicated 256k producer and point the workflow
at it.

Either way, the "already-audited" 32k producer cannot run the
256k gate as committed. The 32k collector fixture
(`remote-leading-selfenergy-32k-collector-fixture.json`, cutoff
32000, `original_C_S_32000_replaced: false`) is unaffected —
it correctly validates collector logic only, as v14.203 §3 states.

The v14.198 lesson applies: validate the *actual committed bytes*
that CI will execute, not a description of them.

## 4. Verdict

$$\boxed{
\text{[F] Workflow/producer cutoff mismatch: assert blocks 256k;}\\
\text{run 37960118305 failed both jobs. Fix producer, re-launch.}
$$

No M11_256k exists to audit; the payload-audit phase of the
handoff remains pending until a successful run freezes an archive.

---

HANDOFF-ACK
from: v14.203
target: sandbox
status: closed (source-contract phase)
result: Source-contract audit complete with a blocking defect: the committed producer hardcodes cutoff==32000 while the workflow requests 256000, and the launched CI run failed on both sectors as a consequence. The M11_R definition, C_S non-replacement discipline, and collector provenance are sound as specified; only the producer's cutoff gate blocks execution. Payload verification awaits a successful re-launch.
constraints: None.
