# Cone Derivation Ledger v13.665 — Addendum: v13.660 Live-Source Pull Confirmed by Project Owner

Date: 2026-09-22

Status: advisory addendum from the external audit thread, resolving the one open item flagged in Round 73 (v13.664).

## 0. Collision/relevance check

The live ledger was fetched immediately before this write. Tip is v13.664 (External Audit Round 73). v13.665 is free.

## 1. What this resolves

Round 73 (v13.664 §1, §7) flagged v13.660's claim about the live Suzuki arXiv source (arXiv:2606.09096v2, revised 17 Aug 2026 — Corollary 1.6's target being `z^2\xi(1/2-iz)/\xi'(1/2-iz)`, not `\xi/(\xi+\xi')`) as unverifiable by this audit thread: both `arxiv.org` and the `ar5iv.labs.arxiv.org` mirror are blocked by this environment's network egress proxy, so the claim could be checked only for internal consistency against the project's own prior citations (v13.279, v13.280), not against the actual source text.

The project owner has now directly confirmed that the wording in v13.660 was genuinely pulled from the live arXiv page and added to the ledger, rather than being a paraphrase or a repeat of an earlier (possibly mistaken) reading. This is exactly the kind of independent confirmation Round 73 asked for.

## 2. Updated status

`v13.660`'s restored target,
\[
\boxed{R_{\rm Suz}(z)=z^2\,\xi(1/2-iz)/\xi'(1/2-iz),}
\]
is now treated by this audit thread as **confirmed**, superseding v13.280's `\xi/(\xi+\xi')` attribution, consistent with v13.660's own account of why the project's citation history diverged (v13.280 appears to have promoted Section 7.8's heuristic intermediate de Branges ratio `\Xi/E` into the statement of Corollary 1.6, which v13.660 correctly identifies as a distinct object).

This does not retroactively verify any of the mathematics built on top of the target (that remains subject to ordinary review as it lands), only the specific external citation fact that was previously flagged as unresolved.

## 3. Standing recommendation, narrowed

Round 73's broader recommendation — quote verbatim source text with surrounding context in any future citation of this specific paper, rather than a paraphrase, given the citation's history of two prior reversals — still stands as good practice for whichever thread next touches this. It is no longer a blocking concern for v13.660 itself.
