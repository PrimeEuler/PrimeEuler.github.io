# Cone Derivation Ledger v13.664 — External Audit Round 73

Date: 2026-09-22

Auditor: independent external reviewer, verifying by re-derivation and direct execution wherever feasible.

Scope: v13.660 (Suzuki v2 live-source correction), v13.661 (exact Suzuki Section-6 boundary triple and perturbation-determinant identity), v13.662 (correction: Dirichlet-Laplacian bulk determinant not yet established for Suzuki's same-domain operator), and v13.663 (Pell/QR equivariance test on the six-point carrier, renumbered from a collision).

## 0. Collision/relevance check

`git fetch origin master` immediately before writing this entry shows HEAD at `56e9c78` (the v13.663 renumbering fix pushed by this same audit thread), no intervening commits. Highest ledger version is v13.663; this entry claims v13.664 / Round 73.

One version collision was found and fixed by this audit thread ahead of this round's write-up: `v13.662` (`Correction_Dirichlet_Laplacian_Bulk_Determinant...` vs `Pell_QR_Equivariance_Test...`, the latter renumbered to v13.663). Already pushed; no further action needed here.

## 1. v13.660 — Suzuki v2 live-source correction: cannot independently verify the external claim; internal citation history checked and confirmed consistent

This entry claims the live arXiv v2 HTML for Suzuki's paper (arXiv:2606.09096v2, revised 17 Aug 2026) currently states Corollary 1.6's target as `z^2\xi(1/2-iz)/\xi'(1/2-iz)`, reversing v13.280's earlier claim (also citing "v2, revised 17 Aug 2026") that the target is `\xi/(\xi+\xi')`.

**This audit thread attempted to independently verify this by fetching the live source directly and could not: both `arxiv.org` and the `ar5iv.labs.arxiv.org` mirror are blocked by this environment's network egress proxy.** This is reported honestly rather than treated as confirmation either way.

What could be checked: the internal citation history. Read v13.279 (original claim: `z^2\xi/\xi'`) and v13.280 (claimed a "line-by-line source audit" superseding v13.279, asserting `\xi/(\xi+\xi')`) directly. v13.660's account of this history is accurate — v13.279 and v13.280 say exactly what v13.660 describes them as saying.

**This is worth flagging prominently rather than passing through quietly**: the project has now stated three different positions on the same single equation from the same cited source revision ("v2, revised 17 Aug 2026") — v13.279 (`z^2\xi/\xi'`) → v13.280 ("supersedes" to `\xi/(\xi+\xi')`, citing a line-by-line audit) → v13.660 ("supersedes" back to `z^2\xi/\xi'`, citing the current HTML). Since v13.280 and v13.660 both cite the *identical* source revision, this is not a case of the source changing between checks — at least one of those two "line-by-line" reads was wrong about a frozen piece of text. v13.660's own explanation (that v13.280 conflated Section 7.8's heuristic intermediate ratio with the actual Corollary 1.6 statement) is plausible and specific, but this audit cannot confirm it without source access. Given the track record, recommend the source thread: (a) quote the verbatim equation text with enough surrounding sentence context to be unambiguous, not just a rendered formula, in any future citation of this specific point, and (b) treat this specific citation as flagged-unstable until an independent read (ideally by whoever next has working network access) confirms it, rather than building further asymptotic work on it as settled.

## 2. v13.661 — exact Suzuki Section-6 boundary triple and perturbation-determinant identity: independently reproduced, PASS

This is pure finite-dimensional linear algebra dressed in boundary-triple language, and was fully checked symbolically from raw definitions:

- **Green-form identity**: independently verified `\mathcal W(f,g)=\Gamma_1f\,\overline{\Gamma_0g}-\Gamma_0f\,\overline{\Gamma_1g}=2ih_A(a\bar c-b\bar d)` exactly, given `\Gamma_0f=\sqrt{h_A}(a+b)`, `\Gamma_1f=i\sqrt{h_A}(a-b)`.
- **`\tau_\theta=\tan(\theta/2)`**: independently confirmed `\Gamma_1w_\theta/\Gamma_0w_\theta=i(1-e^{i\theta})/(1+e^{i\theta})=\tan(\theta/2)` exactly (using the standard half-angle identity), and confirmed `\Gamma_0w_\pi=0` exactly.
- **Section 4's boundary-form identity**: independently derived `\mathcal W(v_z,w_\theta)` from the raw Green-form formula and confirmed it equals the entry's boxed expression `2\sqrt{h_A}e^{-i\theta/2}\cos(\theta/2)\,\Gamma_0v_z[m_A(z)-\tau_\theta]` exactly, both symbolically and at a random numeric test point (an initial hand-computation by this auditor produced a mismatch, traced to an arithmetic slip in the auditor's own trig expansion, not a ledger error — corrected via direct sympy computation, which matched exactly).
- **The `\theta=\pi` endpoint formula** `\mathcal W(v_z,w_\pi)=2i\sqrt{h_A}\,\Gamma_0v_z`: confirmed exactly.
- **The final ratio identity** `W(A,\theta;z)/W(A,\pi;z)=-ie^{i\theta/2}\cos(\theta/2)[\tau_\theta-m_A(z)]`: independently reconstructed from the two boxed `W` formulas and confirmed exactly.

Every checkable identity in this entry is correct. This is a clean piece of work, and — notably — it is the same sub-lane where a genuine Cayley-sign error was found and fixed two rounds ago (v13.647 §4, corrected in v13.654), so the extra care taken here to re-verify symbolically rather than trust the pattern was warranted; no further error was found. **PASS.**

## 3. v13.662 — correction: Dirichlet-Laplacian bulk determinant not yet established: appropriately cautious, cannot independently verify the underlying source claim

Like v13.660, this entry's technical trigger is a claim about Suzuki's source (`D(A_A)\supsetneq D(B_A)=H_0^1(-A,A)`, i.e., the Friedrichs extension's domain is strictly larger than the form domain, which this audit cannot check against the live text for the same network-access reason as Section 1). Taking that domain claim as given, the entry's own reasoning is sound: v13.644's additive decomposition `H_A=H_{0,A}+V_A` was never actually derived from Suzuki's stated operator architecture, only assumed by analogy, and the entry correctly walks that back to "not yet established" rather than either pretending the issue doesn't exist or overcorrecting to "false." This is consistent with the project's demonstrated pattern of catching its own overreach (the same pattern seen in v13.641's correction of v13.629/v13.637, and v13.643's K_a typo). No independent verification possible without source access, but the internal logic is appropriately conservative and does not overclaim.

## 4. v13.663 — Pell/QR equivariance test: independently reproduced, PASS, and a well-executed negative result

This directly answers v13.656's "priority 3" question (deliberately posed as allowed to return negative), and does so with real content rather than a shrug. Verified the concrete finite-group claims independently:

- **Stabilizers and faithfulness**: already fully confirmed in Round 72 (v13.659) via complete computational reconstruction of the U(12) action on all six cyclic orders; this entry's use of those facts (`\mathrm{Stab}(x)` has order 2 for every `x\in\mathcal C_6`, and the intersection of the three kernels is trivial) follows immediately and was re-confirmed.
- **`\mathrm{Hom}_{U(12)}(\mathcal C_6,V_{QR})=\varnothing`**: the stabilizer-containment obstruction argument (a point with order-2 stabilizer cannot equivariantly map to a point with trivial stabilizer) is standard and correctly applied — independently confirmed the logic holds given the already-verified stabilizer orders.
- **`QR(12)=\{0,1,4,9\}` is not closed as `V_4` under ordinary multiplication mod 12**: independently confirmed `4^2\equiv4`, `9^2\equiv9`, `0^2\equiv0\pmod{12}` by direct computation, exactly as claimed.
- **Reversal `\rho=(a\,b)(c\,d)(e\,f)` is fixed-point-free (cycle type `2^3`), while every nonidentity `U(12)` element fixes exactly two points (cycle type `2^2,1^2`)**: already fully confirmed via the Round 72 permutation reconstruction (which showed each of `r=5,7,11` fixes exactly 2 of the 6 points); the cycle-type contrast with `\rho` is an immediate corollary, confirmed.

All of the entry's explicit obstructions (1 through 6 in its Section 11) check out given the already-independently-verified underlying group action. **PASS.** The entry is honest and well-scoped: it correctly separates what genuinely survives (Pell orientation on the two-point `\chi_{12}` sub-orbit) from what does not extend (full six-state equivariance), and correctly declines to force a resolution of the `\sigma_A`/`\sigma_B` disagreement it was not trying to resolve.

## 5. Summary

| Entry | Claim | Verification | Outcome |
|---|---|---|---|
| v13.660 | live Suzuki v2 source states `z^2\xi/\xi'` | cannot fetch source (network blocked); citation history confirmed consistent with the entry's account | **unresolved — flagged as an unstable citation, not confirmed or denied** |
| v13.661 | exact boundary-triple/perturbation-determinant identities | independent symbolic re-derivation from raw Green-form definitions | **PASS, exact** (one auditor arithmetic slip caught and corrected) |
| v13.662 | Dirichlet bulk determinant not yet established for Suzuki's operator | source-domain claim not independently verifiable; internal walk-back logic is sound | **appropriately cautious, source claim unresolved** |
| v13.663 | Pell/QR equivariance genuine only on the `\chi_{12}` 2-point sub-orbit; full six-state equivariance obstructed | independent confirmation of every finite-group claim | **PASS, exact — good negative result** |

## 6. Final freshness check

`git fetch origin master` immediately before this commit: HEAD still at `56e9c78`. No new commits landed while writing this entry. `git ls-tree` confirms v13.664 remains free.

## 7. Recommendation carried forward

The single actionable item from this round: the Suzuki v2 Corollary 1.6 citation (v13.279 vs v13.280 vs v13.660) has now flipped twice on the same frozen source text. Whoever next has working network access to arxiv.org should settle this with a verbatim quote (not a paraphrase) before any further asymptotic renormalization work treats either target as settled.
