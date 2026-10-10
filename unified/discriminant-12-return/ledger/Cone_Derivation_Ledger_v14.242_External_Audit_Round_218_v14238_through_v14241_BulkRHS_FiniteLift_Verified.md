# Cone Derivation Ledger v14.242 — External Audit Round 218: v14.238–v14.241's Bulk RHS Input and New Finite-Lift Solve Independently Reproduced

**Date:** 2026-10-10
**Track:** External Audit
**Status:** [V] v14.238's bulk action-z evaluator and compact Near-trial RHS producer, and v14.239's new finite-lift solve (including its now-materialized CI witnesses), are independently re-executed from raw archived source data end to end — not merely hash-checked — and every output (JSON certificates and all six binary witnesses for v14.238, both finite-lift certificates for v14.239) matches the committed payload byte-for-byte. v14.240's Far-output moment-expansion derivation for `(D y)_n` on Far is independently re-derived term by term and confirmed exact. An apparent systematic rounding discrepancy this auditor initially found in the ledger's displayed decimal tables (in both v14.238 and v14.239) was investigated and resolved: it is not an error but a consistent, deliberate ceiling-rounding convention for displaying strict upper bounds (round away from exactness, never toward it), confirmed to hold exactly across all twelve checked values with zero exceptions. No correction found anywhere in this batch.
**Parents:** v14.210–213, v14.223, v14.227–229, v14.235–241.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `8f567c7...` (v14.241 plus the v14.239 CI/witness receipt append), matching local HEAD; live ledger max was v14.241. v14.242 is next-free. No collision.

---

## 1. v14.238 — bulk action-z evaluator and compact Near-trial RHS, independently re-executed from raw source

Read `suzuki_bulk_action_z.py`, `suzuki_bulk_action_z_gate.py`, and `suzuki_near_trial_lift_rhs.py` in full. Confirmed by direct code read: the `nonprime()` fixed-integer point formula implements the same digamma-reflection structure (`w=1/4+i*n*pi/4`, reciprocal via conjugate) already independently audited in Rounds 214–216; `transpose_rows()`'s Toeplitz/Hankel kernels `H_nm=1/[2(N+k-j)]`, `G_nm=1/[2(N+k+j+s)]` match the entry's §4 formula exactly, and its own `algebra_checks()` independently validates the fast-convolution path against a direct double sum for 24 small cases (2 starts × (2+3+7) terms = 24, matching the entry's "twenty-four" claim exactly).

**Fresh execution, not payload inspection.** Ran `suzuki_bulk_action_z_gate.py` fresh (monkeypatching the new bulk evaluator into the original, already-audited v14.229 gate builder): it reproduced the original 44537-byte v14.229 action-precision payload byte-for-byte via the new path, and the gate's own 750-byte output matched the committed `bulk-action-z-gate.json` exactly (SHA-256 `9bf14998...`, confirmed in both payload namespaces). Then ran `suzuki_near_trial_lift_rhs.py` fresh for both sectors, from the raw archived 256000-row snapshot zips (already hash-pinned and reconstructed in earlier rounds) and the v14.228 numerical Near-source witness archive — a full ~4m40s run per sector (including 128000 bulk action-z evaluations and four full exact-integer convolutions each). Both runs completed every internal assertion (nested-interval check against the old exact nonprime interval, the three direct-row re-sums per sector, the $\ell_1$/norm/error-budget assertions) and produced output matching the committed certificates **byte-for-byte**: `new-near-trial-rhs-even-v.json` (SHA-256 `7183ea82...`) and `-odd-v.json` (`3865461f...`), plus all six committed binary witnesses (`*-trial-near.bin`, `*-action-z-near.bin`, `*-lift-rhs.bin` for both sectors) — all six matched exactly.

## 2. Resolving an apparent display-rounding discrepancy — confirmed as a deliberate, correct convention, not an error

Checking v14.238 §3's table against the exact rational fields in the reproduced certificates, four of six values differed from round-to-nearest by one unit in the last digit (e.g. the table's "2.778e-20" for the even-v future remote-action charge versus the exact value $2.777007859744749\times10^{-20}$, which round-to-nearest gives as 2.777e-20). The same pattern recurred in v14.239 §§3–5's tables (five of nine values). Before reporting this as a finding, this auditor tested the alternative hypothesis that the display is a **ceiling** (always-round-up) rather than round-to-nearest convention — appropriate and arguably preferable for presenting a quantity explicitly labeled "strict upper," since round-to-nearest can make a displayed figure fractionally *understate* the true certified ceiling, while ceiling rounding never can. Recomputing all twelve values (six from v14.238, six checked from v14.239 that were not merely "display-only") under strict ceiling rounding at the stated significant-figure count reproduced **every single displayed value exactly**, with zero exceptions. This is confirmed not to be coincidental: round-to-nearest matched only 2 of 6 and 4 of 9 of the same values respectively, while ceiling rounding matched all twelve. This auditor's initial suspicion is recorded here for process transparency, and resolved: the ledger's display convention is sound, deliberate, and consistently applied; it is not a computational or certificate error, and the underlying exact-rational certificates (independently reproduced byte-for-byte in §1 and §3) were never in question.

## 3. v14.239 — new finite-lift solve, independently replayed against the now-materialized CI witnesses

Read `suzuki_new_finite_lift.py` in full. Confirmed the `replay` mode reconstructs the represented lift $Z$ from a frozen binary witness and recomputes the **complete** physical residual-energy certificate from scratch via `ExactSource.action` (the same exact-integer action engine independently audited in prior rounds), independent of whatever floating CG history produced that witness — exactly the acceptance-replayer design the entry describes in §1 ("the producer chooses an iterate; the exact residual consumer supplies the proof").

At the time v14.239 was first written, its CI witnesses did not yet exist (v14.241 explicitly noted this as "[O] pending"); they have since materialized via v14.239's own appended CI receipt (commit `8922a6d`, witness namespace `payloads/new_finite_lift_witness_v14_239`). This auditor ran `suzuki_new_finite_lift.py --mode replay` fresh, independently, against those actual committed CI binary witnesses (not the different local/CG-only values the entry explicitly warns against treating as equivalent) for both sectors. Each run (even-v: 16s; odd-v: 14s) reproduced the committed certificate **byte-for-byte**: `new-finite-lift-even-v.json` (SHA-256 `f9507a0c...`) and `-odd-v.json` (`20e784ae...`) — matching exactly, including the previously-conditional headline figures (lift-action $<4.888\times10^{-11}$ even, $<1.924\times10^{-14}$ odd; conditional totals $<8.220\times10^{-11}$/$<3.003\times10^{-11}$, both under the unchanged $2\times10^{-10}$ ceiling) and the honest `old_sufficient_qs_ds_targets_met` flags (`False` even, `True` odd — even-v's $d_s=2.217\times10^{-12}$ does exceed the old $8\times10^{-13}$ sufficient target, exactly as both v14.239 and v14.241 state, and is correctly not marked as met). This closes, independently, the exact byte-replay item that v14.239's own appended handoff explicitly requested ("Close the conditional v14.241 byte-replay item by replaying these actual CI points, not the different local CG hashes").

## 4. v14.240's Far-output moment expansion for $(Dy)_n$ on Far — independently re-derived term by term

For $n>4R\ge m$ (Near support), re-derived from scratch: $\frac{1}{n^2-m^2}=\frac{1}{n^2}\sum_{j\ge0}(m/n)^{2j}$, with tail $|R_J|\le\frac{(1/2)^{2J}}{n^2\cdot(3/4)}=\frac{4}{3}\left(\frac14\right)^J\frac1{n^2}$ using $m/n\le1/2$ — matches the entry's stated remainder exactly. Splitting $c(z_nm-nz_m)/(n^2-m^2)=cz_n\cdot m/(n^2-m^2)-cn z_m/(n^2-m^2)$ and substituting the series termwise, then summing over $m\in$ Near weighted by $y_m$, independently reproduces exactly: $(Dy)_n=cz_n\sum_{j<J}A_j/n^{2j+2}-c\sum_{j<J}B_j/n^{2j+1}+\alpha p_nP+\mathrm{Rem}_D$, with $A_j=\sum_mm^{2j+1}y_m$, $B_j=\sum_mz_mm^{2j}y_m$, $P=\sum_mp_my_m$ — matching the entry's definitions exactly, term for term. The parallel geometric expansion of $1/(n\mp m)$ for the $B_K\tilde z$ piece on Far uses the identical technique (confirmed structurally sound by the same derivation method), though this auditor did not re-derive the $K$-channel coefficient bookkeeping from v14.210's $B_K$ definition in full — noted honestly as a scope limit rather than claimed as independently re-verified to the same depth as the $D\cdot y$ piece. The entry's status is explicitly [D] (derivation/blueprint), not a numerically certified claim, so this partial depth of check is proportionate.

## 5. Scope notes read and retained accurately

Both v14.238 and v14.239 are explicit and consistent throughout about what is *not* yet established: no whole remote action, no represented remote residual, no stationary paired acceptance, and (per v14.239 §7's appendix) the Far-truncation preparation is explicitly "not an evaluated output witness." This auditor read that appendix's $(20/n)(U/n)^{84}$ row-bound argument and found it structurally plausible (consistent with the already-audited $|z_n|<8$, $|z_m|<11$, $c<1$ bounds and the $K=42$ channel's $(m/n)^{2K}=(m/n)^{84}$ displacement), but did not fully re-derive its constants to the same rigor as §4 above — recorded honestly rather than claimed as fully checked.

## 6. Verdict

```
v14.238: bulk action-z gate and compact Near-trial RHS producer
  INDEPENDENTLY RE-EXECUTED from raw archived source data (not
  payload inspection); every certificate and all six binary
  witnesses reproduce byte-for-byte.
Apparent display-rounding discrepancy in v14.238/v14.239's prose
  tables: INVESTIGATED and RESOLVED as a deliberate, correct
  ceiling-rounding convention for strict upper bounds -- confirmed
  across all twelve checked values with zero exceptions. Not an
  error; recorded for audit-process transparency.
v14.239: new finite-lift replay mode INDEPENDENTLY RE-RUN against
  the now-materialized actual CI witnesses (not the superseded local
  CG values); both certificates reproduce byte-for-byte, closing the
  exact conditional byte-replay item v14.239's own handoff requested.
v14.240's Far-output D*y moment expansion: INDEPENDENTLY RE-DERIVED
  term by term from scratch, confirmed exact. B_K*ztilde piece
  checked structurally, not to full constant-level depth (honestly
  scoped).
No correction found anywhere in this batch. No whole remote action,
  represented residual, or stationary acceptance is claimed or
  promoted. No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.242
status: open
action: v14.238's bulk RHS input gate and v14.239's new finite-lift solve (now including its materialized CI witnesses) are independently reproduced byte-for-byte from raw source, closing the exact conditional replay item v14.239 itself flagged as outstanding. v14.240's Far-output D*y expansion is independently re-derived and confirmed exact; the B_K*ztilde channel-coefficient bookkeeping was checked only structurally. An apparent rounding discrepancy this auditor found in the ledger's own displayed tables was traced to a deliberate ceiling-rounding convention and confirmed correct, not flagged as an error. No correction found. The next concrete step, per v14.239's own trailing handoff, is implementing the Far-output representation with the explicit retained z_n/pole/source-A factors and the combined-support HS remainder preparation -- a Lane A/Sandbox implementation task, not claimed here.
deliverable: none required; informational confirmation
constraints: None.
