# Cone Derivation Ledger v14.135 — External Audit Round 190: v14.134's Anchor-Export Bug Independently Rediscovered and Corroborated

**Date:** 2026-10-07
**Track:** External Audit
**Status:** [V] v14.134's diagnosis of the withdrawn 64k anchor-export artifacts is independently confirmed: this thread reconstructed `h+b^T S^{-1} b` from the *same* withdrawn JSON (retrieved via GitHub Actions job logs, since the artifacts themselves are blocked by network policy from this sandbox) and found byte-for-byte the same discrepancy Lane A reports in v14.134 §1, before reading that entry. The fix in `cf1a682` is reviewed and sound. The corrected replay (`37659896312`) is still in progress at write time; its numerical output is not yet verified.
**Parents:** v14.130, v14.132, v14.134.
**Collision check:** immediately before this write, live HEAD was `eb84da6`; live ledger max was v14.134. No collision.

---

## 1. Independent rediscovery

Prompted by a user question about the status of the LDDD-certified 64k anchor export, this thread located the (now-withdrawn) anchor artifacts for both sectors. Direct artifact download is blocked by this sandbox's network policy (`productionresultssa15.blob.core.windows.net` returns a 403 at the proxy), so the full `S,b,h,S^{-1}b` payload was instead recovered from the GitHub Actions job logs of run `37643045658`, which print the exported JSON to stdout before uploading it.

Before reading v14.134, this thread also noticed a second, separate workflow (`c9b8ba5`, run `37658776275`) had already consumed that anchor and produced `K_128k`/`K_256k` transport numbers. Cross-checking the transport script's own `anchor_K` field (defined as `h+b^T S^{-1} b`, computed directly from the committed anchor) against the independently-verified `K_total` for the same sector (already confirmed in this audit thread many rounds ago) showed a mismatch far too large for DPS=120 rounding:

```
even-v: h + b^T S^-1 b = 8.7807820378812117511e-7   vs  K_total = 8.8076337216742431370e-7   (diff -2.685168e-9)
odd-v:  h + b^T S^-1 b = 8.7980235467973339864e-7   vs  K_total = 8.8067153720271120085e-7   (diff -8.691825e-10)
```

Both numbers were obtained by an independent mpmath (DPS=120) linear solve on the exact decimal strings in the exported JSON, after first confirming `S·(S^{-1}b)_{exported} = b` to ~$10^{-88}$–$10^{-89}$ residual (ruling out a transcription error in reading the JSON). These are **exactly** the numbers v14.134 §1 reports as the symptom of the withdrawn-artifact bug (to all displayed digits). This is independent corroboration, not a re-derivation from v14.134's own text — the discrepancy was found and the job logs re-pulled before this entry's author had read v14.134.

## 2. Review of the fix (`cf1a682`)

v14.134 diagnoses the cause as a heuristic monkeypatch on `dd_matrix_to_mp` that captured the first $6\times6$/$6\times1$/$1\times1$-shaped matrices seen during the computation, rather than the specific `S,b,h,a` used in the `K=h+(b^T a)` line. The fix adds an `export_anchor=True` path to `one()` that builds the anchor dict from the *exact local variables* `S,b,h,a` already in scope at the point where `K` is computed — see the diff:

```python
protected=(b.T*a)[0]
K=h+protected
vals,_=mp.eigsy(S)
anchor=None
if export_anchor:
    anchor={"S":...,"b":...,"h":...,"Sinv_b":...,
            "K_reconstructed":mp.nstr(h+(b.T*a)[0],100),
            "protected_S_min_reconstructed":mp.nstr(vals[0],100)}
```

This is structurally the right fix: it is no longer possible for the exported anchor to refer to a different matrix than the one actually used, because it is read out of the same scope, not reconstructed by pattern-matching calls after the fact. The workflow-side self-consistency gate (`|K_reconstructed-K_total|<1e-60`, `|λ_min diff|<1e-45`, fail-closed) is a correct regression guard against this exact class of bug recurring, though by construction it cannot fail on the *current* code (both sides come from the same variables) — its value is as a tripwire if the export line and the K-computation line are ever edited out of sync in the future.

## 3. What remains open

Per v14.134 §4/HANDOFF, the preliminary transport run `37658776275` (which consumed the withdrawn anchors) is correctly marked diagnostic-invalid and must not be used. The corrected replay `37659896312` was still `in_progress` (both sectors) at the time of this write — M64000 replays have historically taken 1–2 hours per sector in this environment. This thread will verify the corrected anchor's two self-consistency checks and, once available, independently re-run the high-precision transport against it, on a future audit round.

## 4. Verdict

```
v14.134's anchor-export bug: INDEPENDENTLY CONFIRMED (same two numerical
  discrepancies reproduced from the withdrawn JSON via a separate retrieval
  path, before reading v14.134's own write-up).
Fix (cf1a682): reviewed, structurally sound.
Corrected replay 37659896312: in progress, not yet verified -- open for a
  future round.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.135
status: open
action: No correction needed to v14.134. When corrected replay 37659896312 completes, this thread will independently verify the two self-consistency checks and re-run the high-precision transport against the corrected anchor.
constraints: Do not consume the withdrawn anchor artifacts or transport run 37658776275, per v14.134.
