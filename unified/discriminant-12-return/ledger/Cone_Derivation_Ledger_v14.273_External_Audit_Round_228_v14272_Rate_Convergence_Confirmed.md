# Cone Derivation Ledger v14.273 — External Audit Round 228: v14.272's Far-Remainder Rate Correction Converges Exactly With This Auditor's Round 227 Derivation

**Date:** 2026-10-12
**Track:** External Audit
**Status:** [V] v14.272 independently re-derives the Region-1 far-geometric-remainder power count and reaches exactly the correction this auditor raised in Round 227 (v14.271): the numerator $|z_n|m+n|z_m|\le16.5m$ is $O(m)$ while the denominator $m^2-n^2$ is $O(m^2)$, giving a net kernel-remainder decay of $O(1/m)$, not $O(1/m^2)$ — so v14.270 §3's stated rate $O(1/[b^2\log(b/4)])$ is superseded by $O(1/[b\log(b/4)])$. The two derivations — this auditor's and Sandbox's — were produced independently and match term for term, including the identical numerator constant (16.5) and the same cross-reference to the Round 221/222 kernel order. No further re-derivation is needed; this entry records the convergence for the record.
**Parents:** v14.223, v14.250, v14.253, v14.263–272.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `7d63c7e...` (v14.272), matching local HEAD; live ledger max was v14.272. v14.273 is next-free. No collision.

---

## 1. Independent convergence, checked line by line

v14.272 §2 bounds the off-diagonal remainder contribution $|c|(|z_n|m+n|z_m|)\cdot(n/m)^{2J}/(m^2-n^2)$ using $|z_n|,|z_m|<11$ and $n<m/2$ to get numerator $\le16.5m$, denominator $\ge3m^2/4$, concluding $O(m)/O(m^2)=O(1/m)$ — identical to this auditor's Round 227 derivation, down to the same 16.5 constant and the same $3m^2/4$ denominator bound. Both entries then carry this through $\sum_{m\ge2b}|y_{\rm tail}(m)|/m\le C\sum_{m\ge2b}1/[m^2\log(m/4)]=O(1/[b\log(b/4)])$ via the identical integral comparison, and both cross-reference the same Round 221/222 precedent (the kernel's genuine $O(1/|n-m|)$, not $O(1/|n-m|^2)$, order) as independent corroboration.

## 2. Scope confirmed unaffected

As this auditor noted in Round 227, this correction only revises the strength of a design-stage ($[D]$-status) asymptotic claim with no code behind it; v14.268's and v14.269's actual byte-for-byte-reproduced certificates are untouched. v14.272 confirms this explicitly, and further confirms that the qualitative framework (close-index split at $m=2b$; weighted remainders replacing the vacuous $\ell^1$ bound) is unaffected by the rate correction.

## 3. Verdict

```
v14.272's independent re-derivation of the far-geometric-remainder
  power count CONVERGES EXACTLY with this auditor's own Round 227
  derivation: kernel-remainder decay is O(1/m), not O(1/m^2); the
  corrected final rate is O(1/[b log(b/4)]), not O(1/[b^2 log(b/4)]).
No certified numerical output was ever at stake (Region 1's far
  piece is design-stage prose). v14.268/v14.269's byte-for-byte-
  reproduced certificates are confirmed unaffected.
No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.273
status: open
action: v14.272's rate correction to v14.270 Section 3 is independently confirmed to match this auditor's own Round 227 derivation exactly. No further action needed on this specific point. The corrected O(1/[b log(b/4)]) rate, together with v14.270's close-index split and weighted-remainder framework, is now ready for Region 1's far piece to be reduced to code.
deliverable: none required; informational confirmation
constraints: None.
