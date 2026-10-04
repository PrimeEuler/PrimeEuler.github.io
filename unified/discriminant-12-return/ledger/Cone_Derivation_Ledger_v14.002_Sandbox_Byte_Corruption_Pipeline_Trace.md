# Cone Derivation Ledger v14.002 — Sandbox: LaTeX Byte-Corruption Pipeline Trace (v13.998 Flag)

**Date:** 2026-10-04
**Track:** Sandbox (our Lane B), infrastructure
**Status:** [D] corruption mechanism identified; [N] current pipeline verified clean (v13.995: zero control characters); [O] v13.996 repair pending Jeremy's decision.
**Parents:** v13.996, v13.998
**Authorization:** Jeremy, 2026-10-04 (v13.998 §2 flag to the sandbox)
**Collision check:** live HEAD immediately before this write was v13.999; no v14.002 entry was present.

---

## 0. Finding

External Audit Round 153 (v13.998 §2) flagged byte-level LaTeX corruption in v13.996: `\b`→backspace (0x08), `\t`→tab, `\f`→form-feed, `\r`→carriage return, turning `\boxed`→`^Hoxed`, `\frac`→`^Lrac`, etc. (36 affected lines confirmed by byte scan; the same bug had hit v13.991, which the sandbox self-repaired).

## 1. Mechanism [D]

The corruption signature is unambiguous: backslash-letter sequences interpreted as control characters. This is the classic failure of building the GitHub Contents-API JSON payload by **string interpolation** instead of `json.dumps` — JSON's `\b \f \r \t` are control characters, so an unescaped `\boxed` in an interpolated payload parses to backspace + `oxed`. Any pipeline stage that passes raw markdown through a JSON string context without escaping will mangle exactly these sequences.

## 2. Current pipeline verified clean [N]

The sandbox's current write path (file → bytes → base64 → `json.dumps`, with the base64 alphabet containing no backslashes) is immune by construction. Byte scan of the latest sandbox entry v13.995 (local staging and repo copy): **zero control characters**. The bug is in the old (pre-2026-10-04) pipeline, not a live defect.

## 3. Open item [O]

v13.996's 36 corrupted lines are mathematically reconstructable (the audit verified the entry despite them), but a repair is a repo write and is **held for Jeremy's explicit decision**. Guard added to the sandbox push script: assert no control characters (outside \n, \t) before every PUT.
