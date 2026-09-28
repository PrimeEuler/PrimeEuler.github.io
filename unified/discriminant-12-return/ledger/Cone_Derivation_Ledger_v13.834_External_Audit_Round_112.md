# Cone Derivation Ledger v13.834 — External Audit Round 112

Date: 2026-09-28

Auditor: External audit thread (Claude, independent instance).

Scope: v13.832 — the full (infinite-tail) `ρ=0.02` endpoint inertia theorem: `ind_-(F^-_0.02)=4`, `ind_-(F^+_0.02)=2`, zero kernel at both endpoints, both parity sectors. This closes the exact gap v13.830 §10 flagged as open (certifying that the finite M3999 low-core Schur sign pattern survives the infinite remote correction), and is the strongest theorem in the current finite-tail program to date.

Verdict: **PASS. Fully verified — algebra, both scripts, and the self-disclosed bug fix.**

## 1. Proof architecture checked by hand

The entry avoids bounding `S_C^{(∞)}-S_C^{(M)}` directly (unstable, since the minus tail is indefinite) and instead uses a sandwich-by-codimension argument, which I re-derived independently rather than accepted:

- **Minus endpoint**: the certified 4-dimensional negative tail subspace (v13.821, already audited Round 107) embeds with zero low-core coordinates, giving `ind_-(F^-) ≥ 4` — standard fact: a quadratic form negative on a k-dim subspace has at least k negative eigenvalues. Separately, an explicit strict positive subspace of codimension 4 is constructed (8 positive directions of a reduced 12-core, dressed by coupling to the eliminated finite buffer and the certified remote-tail floor), giving `ind_{≤0}(F^-) ≤ 4` — the complementary standard fact: a form positive on a codim-k subspace has at most k nonpositive eigenvalues. `4 ≤ ind_- ≤ ind_{≤0} ≤ 4` forces both `ind_-=4` exactly and trivial kernel. Correct, and it's the right proof shape — no need to control the sign of a rank-4 indefinite object directly, only its complement.
- **Plus endpoint**: symmetric argument, codimension-2 version, using the already-certified positive tail (v13.821) plus an explicit compactly-supported 2-dimensional negative trial space. Same logic, correctly applied.
- Both arguments are Sylvester's-law-of-inertia congruence facts underneath the codimension bookkeeping; nothing here is hand-waved past.

## 2. Numerics: ran both cited scripts directly

`suzuki_full_endpoint_rho002_frozen_carriers.py` — PASS. Hash, exact-rational rank-8/rank-2 minor, and Cholesky-positivity checks all pass on the frozen exact-binary64-dyadic payloads.

`suzuki_full_endpoint_rho002_inertia_certificate.py` — ran to completion, reached the THEOREM printout with no `RuntimeError`. Cross-checked every boxed claim in the ledger against the run: `finite_normalized` (`0.99999931`/`0.99999817`, both ≥ the ledger's conservative floors `0.99999931`/`0.99999816`), the Gram maxima (`0.046645985671`/`0.023906652752`, exact match to displayed precision), `terminal_margin` (`3.13091`/`3.15509`, both `>` the boxed `3.1308`/`3.1550`), `normalized_post` (`0.98455`/`0.99211`, both `>` the boxed `0.9845`/`0.9920`), and the plus-endpoint restricted eigenvalues and negative margins (`0.0071917`/`0.0006166`, both `>` the boxed `0.0071916`/`0.0006165`) — all reproduce or safely exceed the theorem's own stated margins.

**Independently re-derived the §3 diagnostic from scratch** (not by re-running their code path): built the 12×12 low-core-minus-buffer Schur complement myself from `build_full12_minus`, first with a naive `ldl_solve` that omitted the rank-one pole/Sherman-Morrison correction — this gave eigenvalues visibly different from the ledger's (e.g. `0.2049` vs. the claimed `0.2468`, a ~17% miss), which I initially logged as a possible discrepancy. Redid it using the project's own pole-corrected `A.solve_full`, and got an **exact digit-for-digit match** to all 12 eigenvalues in both sectors, confirming the `4⁻+8⁺` split. The mismatch was my own omission, not theirs — recorded here so it isn't mistaken for a finding.

## 3. Minor discrepancy: descriptive figures vs. rerun (does not affect the theorem)

Two places where the ledger's "approximately" prose doesn't match numbers produced by directly running the cited script on this machine, though both remain safely inside the actual fail-closed caps that the code enforces (so no boxed claim is at risk):
- §5's stated solve residuals ("`1.17×10⁻¹⁵`, `1.00×10⁻¹⁵`") vs. what I got running `suzuki_full_endpoint_rho002_inertia_certificate.py` directly (`1.2276×10⁻¹⁵` even-v, `1.2398×10⁻¹⁵` odd-v) — both still comfortably under the caps `1.55×10⁻¹⁵`/`1.45×10⁻¹⁵`.
- §4's stated reference-defect values (`7.51×10⁻¹⁶`/`6.99×10⁻¹⁶`) vs. mine (`7.61×10⁻¹⁶`/`7.08×10⁻¹⁶`) — both under the `1.40×10⁻¹⁵` cap.

Plausibly platform/long-double-rounding sensitivity in a `np.longdouble` computation rather than a transcription error, since the gap is consistent in direction and small in absolute terms, but I can't rule out an eyeballed-rather-than-recomputed prose figure. Either way it's cosmetic: the actual fail-closed gate is the cap check, which passed on both runs.

## 4. Self-disclosed bug fix, verified

Commit `c6d95c3` ("fix full-endpoint reference envelope for 12-core dimension") replaces a call to the shared `A.reference_defect` helper — which hard-codes a 10-coordinate dot-product length inherited from an earlier theorem's dimension — with a new `reference_defect_generic` that reads `nc=C.shape[0]` dynamically. Read both old and new code paths; the fix is correct and exactly as described (a dimension-genericity fix, not a bound-weakening one). Per the ledger's own §4: this changes no displayed theorem margin, only removes a latent undercount that would have mattered had the dimension mismatch actually been exercised. Good practice — self-caught before I had to find it.

## 5. Scope

Correctly guarded. The entry explicitly does not promote the signed inertia difference (`4−2=2`) to an ordinary six-root multiplicity claim, does not assert reality/simplicity of the two low-core channels, and explicitly notes that Round 111's platform-dependent N=96 decimal eigenvalues are not used anywhere in this theorem — direct acknowledgment of last round's finding.

## Self-audit note

No error of my own found this round, beyond the transient one described in §2 (my own omitted pole correction in an independent from-scratch check), which I caught and corrected before it became a finding.

## Result

\[
\boxed{\textbf{PASS: v13.832 fully confirmed.} \operatorname{ind}_-(F^-_{0.02})=4,\ \ker F^-_{0.02}=\{0\},\ \operatorname{ind}_-(F^+_{0.02})=2,\ \ker F^+_{0.02}=\{0\} \textbf{ in both parity sectors — the full (not finite-section) infinite-tail endpoint inertia theorem, closing the gap left open by v13.830. Signed endpoint spectral flow } 4-2=2\textbf{, correctly not promoted to an ordinary multiplicity count.}}
\]
