# Cone Derivation Ledger v14.489 — External Audit Round 289: v14.488 Direct-Middle Residual Gate FAIL Independently Verified

**Date:** 2026-10-16
**Track:** External Audit
**Status:** [V] v14.488 is read in full. Sandbox reports that the v14.448 execution gate's acceptance condition **fails** on the direct-middle block alone, in both sectors, making the beyond-middle far block moot for this gate — a genuine negative result, reported honestly rather than suppressed or reframed. It also accepts this auditor's Round 288 finding (the even-sector endpoint-ratio display correction) verbatim and correctly. This round independently reproduces every numerical relationship the FAIL verdict rests on, checks the internal consistency of the entry's own self-verification work, and confirms the logical structure of the "far block cannot rescue this" argument — without yet being able to check raw buffer hashes, since those files remain outside this repository.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–485, v14.442, v14.444, v14.447, v14.448, v14.471, v14.473, v14.478, v14.479, v14.486, v14.487, v14.488.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `4e5b260...` (v14.488), matching local HEAD; live ledger max was v14.488. v14.489 is next-free. No collision.

---

## 1. Acceptance of the Round 288 correction — confirmed verbatim and correct

v14.488 states: "the even-sector endpoint ratio ... equals 0.24999993992596597, not '≈0.24998' as displayed in v14.486." This matches this auditor's own Round 288 finding exactly, digit for digit. The correction is accepted cleanly and the entry correctly notes the exact fraction and the `≤1/4` gate were never in question — exactly as Round 288 stated.

## 2. Core numerical relationships — independently recomputed at 50-digit precision, all exact

Using the entry's own displayed figures as inputs (point ℓ², physical upper, allowance `a`, and `q`), recomputed every derived quantity from scratch with `decimal.Decimal`:

```
even:  physical_upper - point_l2       = 1.9953349e-13   (= the seed l2 error 1.995334793914987e-13, exactly)
       physical_upper / allowance a     = 2.27299          (claimed "2.273×")
       physical_upper^2                 = 2.5580848e-09    (claimed "2.5581e-09")
       q - physical_upper^2             = -2.0629548e-09   (claimed "-2.063e-09")
       a^2                               = 4.95131e-10      (vs stated q = 4.9513e-10 -- consistent with a = sqrt(q))

odd:   physical_upper - point_l2       = 1.9846247e-13   (= the seed l2 error 1.9846246697473864e-13, exactly)
       physical_upper / allowance a     = 2.26516          (claimed "2.265×")
       physical_upper^2                 = 2.5487182e-09    (claimed "2.5487e-09")
       q - physical_upper^2             = -2.0519782e-09   (claimed "-2.052e-09")
```

Every one of these matches the entry's displayed table exactly. In particular, the gap between the entry's "physical upper" and "point ℓ²" columns is confirmed to equal precisely the seed-action's own certified ℓ² error upper (from v14.486/v14.487) — demonstrating that the physical-error combination (`compact ℓ² error + seed ℓ² error + bare floor error`) is dominated entirely by the seed term, exactly as the entry's prose describes, and that the compact (`~4e-21`/`~9e-23`) and floor (`~9e-75`) terms are correctly negligible by comparison.

## 3. Self-verification work — checked for internal consistency

- **Per-eighth block norms** (even: `2.266e-5, 2.071e-5, ..., 1.399e-5`): confirmed strictly monotonically decreasing. Recombined in quadrature (`sqrt(Σv²)`): `5.05745e-05`, matching the entry's reported total point ℓ² (`5.05775e-05`) to within the rounding implied by the four-significant-figure block values given — consistent, not merely asserted.
- **Sign-convention check:** the entry reports that of all sign combinations tried, `source − compact − seed` gives the smallest residual (`5.06e-5`) against two much larger alternatives (`7.7e-4`, `8.2e-5`), which is itself evidence against a sign-flip error being mistaken for a genuine failure — a sensible and verifiable-in-principle sanity check, reported transparently rather than omitted.
- **Independent seed re-derivation:** ten sample rows recomputed via a structurally different method (direct extended-precision bank sums over all `m≠n`, fed by *Lane A's* frozen v14.478 moments rather than Sandbox's own local ones) are reported to reproduce the v14.486 buffer to `≤7.2e-23` — i.e., Sandbox cross-checked its own seed buffer against the independently-frozen-and-audited (Round 286) T2 certificates, not only against its own pipeline. This is a meaningful internal control, not a redundant restatement.

## 4. Logical structure of "the far block is moot" — independently confirmed sound

The argument is: the beyond-gap ℓ² combines the disjoint direct-middle and far blocks in quadrature (the same disjoint-support combination rule, `‖v‖² = ‖v_direct-middle‖² + ‖v_far‖²`, this project has used throughout and that this auditor has independently verified in earlier rounds). Since `‖v_far‖² ≥ 0` always, `combined² ≥ ‖v_direct-middle‖² = physical_upper²`. Since `physical_upper² > q` already (confirmed numerically above, in both sectors), `combined² > q` regardless of the far block's value — so no possible far-block result can bring the sum back under the sufficient-condition threshold. This is a correct, minimal use of monotonicity under quadrature addition, not an unsupported leap.

## 5. Scope limit (carried forward from Round 288)

No certificate, buffer, or manifest file for this residual composition exists in this repository yet; v14.488 again states payload transfer is withheld pending explicit instruction. This round could therefore independently check the full chain of *displayed* arithmetic (and found it exact throughout) but could not yet verify the underlying buffer hashes or recompute the exact-rational residual from raw bytes. This is disclosed as a scope limit, not treated as a pass on that specific axis.

## 6. Verdict

```
v14.486 correction acceptance: confirmed verbatim-correct, matching
  Round 288's finding exactly.
FAIL-verdict arithmetic: every displayed number (physical/allowance
  ratios, both squared physical uppers, both headroom values, the
  a^2~=q consistency, and the exact seed-error attribution of the
  physical-minus-point-L2 gap) independently recomputed at 50-digit
  precision and found exact in both sectors.
Self-verification work: per-eighth block monotonicity and quadrature-
  sum consistency confirmed; the independent ten-row seed re-derivation
  against Lane A's own frozen moments (not Sandbox's) is a genuine,
  non-circular cross-check.
"Far block moot" argument: independently confirmed as a correct,
  minimal monotonicity argument under disjoint-support quadrature
  combination -- not an unsupported leap.
Scope limit: raw certificate/buffer files for this return are still
  outside the repository; hash-level and byte-level verification
  remains deferred.
No defect found in anything independently checkable this round. This
  is a genuine, well-substantiated negative result: the current
  (trial, seed) pair does not close the beyond-gap residual.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.489
status: open
action: this auditor independently reconstructed every numerical relationship underlying the FAIL verdict and found all of them exact, confirmed the internal self-checks (monotonicity, quadrature consistency, independent seed re-derivation) are genuine rather than circular, and confirmed the "far block is moot" argument is logically sound. No correction needed within the checkable scope. The next gate decision (a δ-correction of the (trial, seed) pair, per v14.488's own framing) belongs to Lane A/Jeremy, not to this audit thread.
deliverable: none required; informational confirmation
constraints: None.
