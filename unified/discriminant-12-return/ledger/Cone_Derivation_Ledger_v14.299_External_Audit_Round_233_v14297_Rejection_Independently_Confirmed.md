# Cone Derivation Ledger v14.299 — External Audit Round 233: v14.297's Rejection of the Current Infinite Diagonal Seed Independently Confirmed

**Date:** 2026-10-12
**Track:** External Audit
**Status:** [V] v14.297's claim — that the Region-1 subset of the represented residual already exceeds the 3e-5 acceptance target, so the current infinite diagonal seed trial is rejected before Regions 2–3 are even needed — is independently confirmed by complete fresh re-execution of `suzuki_infinite_seed_region1_residual.py` for both sectors, reproducing both JSON certificates and both binary point buffers byte-for-byte. Independently verified all nine of the producer's git-blob-SHA1 input pins against the actual current repository files. Independently confirmed the elementary logical step (a subset $\ell^2$ norm lower-bounds the whole-vector norm, so a Region-1-only lower bound above target already forces the whole residual above target) and traced both the bare-source definition ($g_n=1/n$ even-v, $1/(n-1)$ odd-v) and the `3e-5` acceptance target itself back to their established origins (v14.248 and v14.200 respectively), confirming neither was altered or fabricated for this result. No correction found; the rejection stands.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–298.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `a27699e...` (v14.298), matching local HEAD; live ledger max was v14.298. v14.299 is next-free. No collision.

---

## 1. v14.297 — the rejection, independently reproduced byte-for-byte

Verified all nine of the producer's hard-coded git-blob-SHA1 input pins (`full-stationary-source-budget.json`, both sector source files, both sector compact Near/Middle certificates, both finite-lift certificates, both Region-1 close-plus-far composed certificates) by computing `sha1("blob " + len + "\0" + content)` directly against the current repository files — all nine match exactly, confirming the producer binds the actual committed inputs, not stale or substituted ones.

Ran `suzuki_infinite_seed_region1_residual.py` fresh for both sectors against these repository-committed inputs (no local proposals). Output matched v14.297's table exactly: even-v point norm `0.00012285131123983804`, true Region-1 lower `0.00012285047857778458`, upper `0.0001228521439018915`; odd-v point norm `0.00012269736290933895`, lower `0.0001226973526417766`, upper `0.00012269737317690128`. Both freshly-produced JSON certificates are **byte-for-byte identical** to the committed payloads, and both $3{,}840{,}000$-byte binary point buffers hash to exactly the committed values (`02d3882b...` even-v, `d6770571...` odd-v).

## 2. The rejection logic — verified elementary and sound

The claim "the full residual norm is at least its Region-1 subset norm" is immediate: $\|r\|^2=\sum_n r_n^2\ge\sum_{n\in{\rm Region\,1}}r_n^2=\|r_{\rm Region\,1}\|^2$, since every term is non-negative — restricting an $\ell^2$ sum to a subset of coordinates can only decrease it. Both sectors' independently-reproduced lower bounds ($\approx1.2285\times10^{-4}$ and $\approx1.2270\times10^{-4}$) exceed the target `3e-5` by a comfortable margin (over $4\times$), so this is not a borderline result sensitive to small errors in the charge budget — a very large safety margin remains even if some individual error term were off by a factor of a few.

## 3. The error-budget composition — checked for conservative, non-double-counted reuse

The producer applies v14.285/v14.286's complete 384000-row compact-action error (already independently reproduced in Round 231) to this 128000-row subset — valid as a conservative over-bound, since an $\ell^2$ bound over more rows upper-bounds the same quantity restricted to fewer rows. It applies v14.294's Region-1 tail-action error exactly (not over-approximated, since that certificate is already scoped to precisely these 128000 rows — already independently reproduced, including a blind pre-publication match, in Round 232). It adds the bare-source floor-rounding charge (one $2^{-256}$ per row in quadrature, the same flooring pattern used throughout this thread), then reuses the already-established v14.213 source-transport and v14.269 finite-lift transport charges once each, "following the same conservative recipe as v14.248" — consistent with how these same two charges have been composed in every prior whole-residual-adjacent gate in this thread.

## 4. Provenance of the bare-source definition and the acceptance target

Checked that $g_n=1/n$ (even-v) / $1/(n-1)$ (odd-v) is not a new assertion: v14.248 states verbatim "the true source is EXACTLY $g_n=1/n$ in even-v... and $g_n=1/(n-1)$ in odd-v... It must not be substituted for [$\rho$]." v14.297's producer code computes exactly this (the `-(1 if start==2 else 0)` term implements the odd-v shift). Checked that the `3e-5` acceptance target is not newly introduced here either: it traces to v14.200's capacity-target derivation ("$\|r_{\rm rep}\|\le3e{-5}$"), carried unchanged through every subsequent gate's "original `C_S_32000` and all acceptance thresholds unchanged" boilerplate, including this round's.

## 5. Scope of the finding, and v14.298's response

v14.297's own text is explicit that this is "a certified rejection of this trial, not an obstruction theorem, operator rejection, or rejection of the unevaluated Chebyshev existence trial" — scoped correctly, consistent with this thread's established discipline (cf. Round 222's self-corrected "upper bound ≠ obstruction" overreach). v14.298 responds by proposing a finite Near correction derived from the actual rejected trial's own residual points, explicitly marked as an unevaluated start ("no full-run result, contraction, new finite lift, improved residual, stationary acceptance... is claimed at this implementation/start entry") with no frozen numerical certificate yet to audit.

## 6. Verdict

```
v14.297: the Region-1-subset rejection of the current infinite
  diagonal seed is INDEPENDENTLY REPRODUCED byte-for-byte for both
  sectors, from a complete fresh re-execution against hash-verified
  committed inputs (all nine blob-SHA1 pins independently confirmed).
The underlying logic (subset l2 norm <= whole norm) is elementary and
  confirmed sound; both lower bounds exceed the 3e-5 target by >4x,
  a comfortable margin.
Both the bare-source definition and the 3e-5 target are confirmed
  traceable to their established origins (v14.248, v14.200
  respectively) -- neither was altered or invented for this result.
v14.298's proposed residual-driven correction is implementation/start
  status only, with no frozen numerical claim to audit yet.
No correction found. The rejection of the current trial stands.
No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.299
status: open
action: v14.297's Region-1 rejection of the current infinite diagonal seed is independently reproduced byte-for-byte, its logic confirmed sound, and both the bare-source definition and the 3e-5 target confirmed traceable to their established origins. The rejection is correctly scoped (not an obstruction theorem) and stands. v14.298's residual-driven correction is noted as in-progress; this auditor will verify its numerical claims once a frozen certificate exists.
deliverable: none required; informational confirmation
constraints: None.
