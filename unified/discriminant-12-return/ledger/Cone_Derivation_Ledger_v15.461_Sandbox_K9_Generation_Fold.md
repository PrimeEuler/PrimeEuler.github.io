# Cone Derivation Ledger v15.461 — Sandbox return: the k=9 generation fold — door II has a candidate mechanism (fiber cardinality 3 = 9/3, conditional on two named hypotheses)

Date: 2026-11-06 (America/New_York). Lane: sandbox (our Lane B), depositing the build run in the Cone dynamics side thread 2026-11-06 at Jeremy's direction ("lets do it" on the mechanism proposed in discussion; "ledger it"). Parents: v15.429 §2 (door anatomy II: the generation door measured as one unbounded positive integer); v14.818 (the AM-GM family at general k is ledgered: Hessian, signature (1, k−1), seat −k·log 2, d_k ↔ ζ^k). Live HEAD v15.460 at deposit. Status: [D] exact verified arithmetic for the fold itself; the two hypotheses it is conditional on are named in the claim and not discharged. Disclosure deposit under the ledger-everything policy: listing is disclosure, not endorsement by the other lanes.

## Claim

Door II's integer has a candidate mechanism inside the AM-GM family itself. A k-list's split phase has order k and grades a distinguished mode's occupation c by c mod k (the k=3 case is the frame's grading, v15.388). At k=9 the reduction Z9 → Z3 has fibers of size 3, and the frame's replica tower (c = τ + 3g) read at k=9 **folds to exactly three classes per τ** — distinct for g = 0, 1, 2, period-3 thereafter, so a fourth replica duplicates a class instead of extending the tower. The fine digit (g mod 3, the second base-3 digit of c mod 9) is gauge-invisible by the frame's own formulas. The claim is conditional on two hypotheses, stated here and in the build: **(H1)** the frame's third mode is a k=9 list's distinguished mode; **(H2)** some sector reads the fine digit (the mass sector is the phenomenological candidate — generations in nature differ only there — but no such coupling exists on record). If both hold, the generation count is a fiber cardinality, 3 = 9/3: the first count in this thread produced rather than assumed, with the falsifiable shape that a fourth generation would duplicate an existing class in every digit-reading sector.

## Chain of results (`k9_generation_fold.py`, exact arithmetic throughout)

1. **Split grading at general k.** Phase order k, AM coefficient 1/k from list length — the k=3 argument of the frame build rerun at k = 2, 3, 4, 6, 9, 12, 18. Only k divisible by 3 refines the frame's Z3; the fiber over Z3 has size k/3.
2. **The fold.** For all eight frame entries (L_L, Q_L, H, e_R, u_R, d_R, ν_R, W), tower classes (τ + 3g) mod 9 for g = 0..5: three distinct classes per τ for g < 3, period-3 in g thereafter. The tower has finite class structure under the k=9 reading where door anatomy II (v15.429) found only a half-line: the difference is entirely the refinement — outputs at the k=3 level are untouched.
3. **Selectivity.** Fiber sizes for k = 3, 6, 9, 12, 15, 18 are 1, 2, 3, 4, 5, 6: exactly 3 only at k = 9. The mechanism is not "any higher k" — k=6 would fold the tower to 2 classes, k=12 to 4; and k not divisible by 3 (2, 4) refines nothing.
4. **Digits and antimatter.** c mod 9 ↔ (τ, g mod 3) is a base-3 digit bijection. Conjugation is an exact involution on the nine classes: τ → −τ mod 3 (as filed at v15.388) and the digit maps g → −g − [τ>0] mod 3 — classes are paired, not digit-fixed, and antimatter stays inside the folded tower. (An early draft of this section overstated digit stability under conjugation; the exact law is what is deposited.)
5. **Charge non-leakage.** The Z6 congruence and the closed hypercharge table read only the mod-3 shadow τ = (c mod 9) mod 3, verified for all fields at g = 0, 1, 2: the refinement cannot contaminate the charge sector — the fine digit is invisible to every gauge output by construction of the frame's formulas, which is precisely the property H2 needs (a digit that ONLY a non-gauge sector can read).

## Negatives / scope limits, stated plainly

H1 and H2 are hypotheses, and this deposit does not move them: no construction on record embeds the frame's third mode into a 9-list (the frame was built at k=3; the k=9 member's existence as a family member is ledgered at v14.818, but the identification of modes across members is new and unjustified here), and no mass-sector coupling to any grading exists anywhere in the thread (door anatomy II: masses are unphraseable in-frame). The fold also does not explain why the tower is read at k=9 rather than at k=3 (which gives fiber 1 — one generation — or k=6, k=12): selectivity cuts both ways, and a selector for the reading level is the same species of open question as before, one level up. The k=9 list carries signature (1,8) on its Hessian face; no spacetime or intertwiner reading is claimed for it (the v14.818 guardrail for k=4 applies family-wide). Doors I and III are untouched by this deposit.

## Verdict

Deposited as a conditional mechanism for door II: the AM-GM family contains exactly one refinement of the frame's grading whose fiber is the observed generation count, the refinement is gauge-invisible by the frame's own arithmetic, and its antimatter structure closes exactly. Whether the frame's third mode carries that refinement, and whether anything reads its fine digit, are the two named open steps. Door II's status changes from "one unbounded integer, no candidate source" to "one integer with a candidate source, two hypotheses deep."

## Payload and snapshot note

Payload: `unified/discriminant-12-return/payloads/k9_generation_fold_v15_461/` — the full living REPORT.md (778 lines: the v15.429 snapshot's content plus the k=9 fold section) and the fold script, with `MANIFEST.sha256`. The script was re-executed from the staged copy on 2026-11-06 (exit 0). SHA-256 (generated mechanically from the manifest):

- REPORT.md `2f3ef5a05ebf0c8443a61b8df2aecffd3cbe8a70ac81df446623c631cc499ec6`
- k9_generation_fold.py `4da23b2441852cdf35078e0f8dc11e2dc19f59d7fa067e82d55a7d8fa3ed861b`

Snapshot note: this REPORT.md supersedes the v15.429 snapshot for the report as a whole. Its fold section closes with an in-text status line reading "not ledgered" — that line describes the section's state when written and is superseded by this deposit; the living file's line is being updated to name v15.461.
