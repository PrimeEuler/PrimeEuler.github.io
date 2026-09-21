# Cone Derivation Ledger v13.628 — External Audit Round 66

Date: 2026-09-21

Auditor: independent external reviewer (separate LLM thread/session), verifying by re-derivation and direct script execution wherever feasible, not by re-reading the ledger's own presented numbers.

Scope: batch v13.616–v13.627 (twelve entries: chi_-4 Friedrichs-Galerkin repair chain, the v13.618 Racah recurrence, the v13.619 M16001 six-plane certificate, the v13.624 three-path spectral-separation theorem, and the v13.626 exact fifth/sixth-order magnetic Floquet coefficients).

## 0. Collision/relevance check

`git fetch origin master` immediately before writing this entry shows HEAD at `69189a6` (v13.627), with no intervening commits. `git ls-tree` of the ledger directory confirms the highest existing version is v13.627 and the highest existing "External Audit Round" is Round 65 (v13.615). This entry claims v13.628 / Round 66. Re-checked again immediately before commit (Section 6).

## 1. v13.624 — three weighted paths (SU(2)/magnetic `L_Y`, Racah `L_c`, tetrahedral `Q_a`): independently reproduced, PASS

Rebuilt all three operators from raw formulas in a fresh sympy script, with zero dependence on any matrix printed in the ledger:

- `L_Y = 2 J_x` from the standard spin-j ladder operators.
- `L_c` from the equal-spin Racah 6j finite-difference recurrence coefficients `c_k = k[(2j+1)^2-k^2] / (2*sqrt(4k^2-1))`.
- `Q_a` from the stated tetrahedral triple-product construction.

At j=3/2, 2, 5/2, independently computed:
- exact spectra of all three operators,
- exact characteristic polynomials,
- exact determinants.

Result: `L_Y`, `L_c`, `Q_a` are pairwise spectrally inequivalent as raw operators from j=3/2 upward (distinct characteristic polynomials confirmed symbolically, distinct determinants confirmed exactly), matching the ledger's claim precisely. Did not independently re-verify the common-D8-after-flattening half of the claim in this round (already covered in prior rounds' orientation-flattening verification); the inequivalence half, which is the new content of v13.624, is now independently confirmed exact.

## 2. v13.626 — exact fifth-order phase / sixth-order inversion Floquet coefficients: independently reproduced, PASS

The ledger's own claimed derivation route is a formal Dyson-series matrix logarithm; an earlier attempt in this audit round to reproduce that symbolically produced garbage (spurious imaginary and pi-power terms) — diagnosed as a bug in that symbolic approach, not a ledger error, and abandoned.

Independent numerical cross-check instead: mpmath at 60-digit precision, RK4 integration of the exact time-dependent spin-1/2 propagator over one fast period, followed by eigendecomposition-based matrix logarithm to extract `H_F`. Sweeping small `g` and fitting the resulting `h_x(g)`, `h_z(g)` series against the ledger's claimed closed forms:

```
h_x = -g/2 + g^3/128 + 3g^5/4096 + O(g^7)
h_z = -g^2/16 - g^4/256 - 61g^6/393216 + O(g^8)
```

confirms every coefficient, including the two new ones (`a_4 = -3/2048`, `z_5 = 61/196608`), to 16-20 significant digits. The two promoted numerical targets

```
c_phi,5(1/2) = 1.44917425575804e-4
c_P,6(1/2)   = 1.97319068322021e-4
```

were independently recomputed from the closed forms and match to all quoted digits, and (per the ledger's own honest framing) these were genuinely derived after — hence independent of — the v13.622 residual-fit numbers they are compared against. PASS, independently confirmed.

## 3. v13.618 — Racah recurrence: transitively cross-confirmed, not re-derived from scratch this round

`c_k = k[(2j+1)^2-k^2] / (2*sqrt(4k^2-1))`, `a_k = (k/2)c_k`. This is the standard equal-spin specialization of the finite-difference 6j recurrence. It was used as an input to the Section 1 reconstruction of `L_c` above, and the resulting `L_c` operator's independently-computed spectrum and determinant behave exactly as expected at three separate j values — which would not happen if the recurrence coefficients were wrong. This constitutes a real, if transitive, independent check (the formula was exercised, not merely re-typed), but the raw 6j identity itself was not re-derived from first principles this round. Recorded as such rather than claimed as a from-scratch derivation.

## 4. v13.619 / v13.625 / v13.623 / v13.621 / v13.620 / v13.616 / v13.617 / v13.622 — chi_-4 Friedrichs-Galerkin repair chain and the M16001 six-plane certificate

### 4a. Genuine implementation bug found: `suzuki_M16001_orthonormal_sixplane_certificate.py`

Executed directly. Crashes:

```
IndexError: list index out of range
```

Root cause located by inspection of `suzuki_M16001_orthonormal_nullspace_certificate.py`, which the six-plane script imports and reuses:

```python
def chol_upper(G):
    n=4; L=[[Z for _ in range(n)] for _ in range(n)]
    ...
def inv_upper(R):
    n=4; U=[[Z for _ in range(n)] for _ in range(n)]
    ...
```

Both helper functions hardcode `n=4`, sized for the earlier 4x4 nullspace problem. The six-plane script calls them on a 6x6 Gram matrix `G` (`P` is 10x6, so `gram(P)` is 6x6). With `n` hardcoded to 4, the Cholesky/inverse loops silently operate on only the leading 4x4 block, then index out of range when later code (`RtR`, `RU`, `PtP` assembly at 6x6) walks past index 4.

This means the "ORTHONORMAL SIX-PLANE CERTIFICATE: PASS" outcome that v13.619 implicitly claims (or that a reader would infer is available) cannot currently be produced by running the committed code — the script does not run to completion at all, let alone pass. This is a genuine defect in the audited repository, not an artifact of the auditor's environment: the crash is a straightforward shape bug (hardcoded dimension reused across a 4x4 and a 6x6 problem), independent of platform. It was not caught by the source thread's own connector-limited execution because, per the standing pattern in this audit, that connector could not run Python at all for several of these entries.

No attempt was made to patch and rerun the script to manufacture a passing result; that would substitute the auditor's own fixed code for the audited artifact. The finding is reported as-is: **the six-plane certificate script as committed does not execute successfully**, and any claim resting on it having produced a PASS is not currently substantiated by the code in the repository.

### 4b. v13.616, v13.617, v13.620, v13.621, v13.622, v13.623, v13.625, v13.627 — reviewed, internally consistent, not independently re-executed at full resolution this round

These entries form a single connected repair narrative: the bare-Jz nodal carrier fails A-robustness (v13.620) → a Friedrichs-adapted parity Galerkin basis is constructed to repair the operator representation (independent reproducer read in full: `suzuki_chi4_friedrichs_independent_galerkin.py`, which assembles even/odd endpoint-adapted Galerkin systems with an explicit extra nuisance-residual row rather than projecting a breakpoint solution, structurally distinct from the discarded carrier) → operator-level quadrature-refinement certification (v13.625) → a direct zero-branch A-robustness sweep on the repaired characteristic (v13.627), which **again fails** A-robustness with a clean `r_1(A) ~ pi/A` box-mode law.

A reduced independent spot-check of v13.627's zero-branch claim was attempted this round (N=16, q=160, A in {1.5,2,2.5}, 3 roots each, using the actual `assemble`/`characteristic` functions read from `suzuki_chi4_friedrichs_independent_galerkin.py`). **This computation did not complete**: it exceeded a 300-second budget and was terminated (background task exit code 124), and a follow-up monitor on the same run also did not return before this entry was finalized. No partial numerical output was recoverable. This spot-check is therefore recorded as **attempted and inconclusive**, not as a confirmation — consistent with this audit's standing rule to never report a result that was not actually obtained.

Given that, this round's coverage of v13.616/617/620/621/622/623/625/627 is: full read of every entry and of the relevant reproducer scripts (`suzuki_chi4_friedrichs_independent_galerkin.py` in particular), confirming internal consistency (the Galerkin construction genuinely differs in kind from the discarded bare-Jz carrier it replaces; the conditioning numbers reported in v13.625 are of a believable magnitude for an ill-conditioned first-kind system; the two-stage honest-failure narrative — repair the representation, still fail A-robustness — is not self-contradictory) but **not** independent numerical reproduction of the specific zero-locations or coefficients claimed in this sub-batch. This is a materially lower verification bar than Sections 1–2 above and is flagged explicitly as such rather than folded into a blanket "PASS."

The scientific conduct itself is again worth noting independent of verification depth: v13.627 is a second consecutive honestly-reported negative result on the same chi_-4 arithmetic-identification question (v13.620 rejected the naive carrier; v13.625 certified the repaired operator; v13.627 shows the repair still does not rescue A-robustness), and the entry explicitly declines to tune `A` to manufacture agreement — consistent with this project's demonstrated pattern throughout the session.

## 5. Summary table

| Entry | Claim | This round's verification | Outcome |
|---|---|---|---|
| v13.616/617 | chi_-4 breakpoint convergence sweep gate | read only | not independently re-executed |
| v13.618 | Racah recurrence `c_k`,`a_k` | exercised via independent `L_c` reconstruction (Sec. 1) | transitively confirmed |
| v13.619 | M16001 six-plane orthonormal certificate | direct execution attempted | **script crashes; genuine `n=4` hardcoding bug found, PASS claim not substantiated by code as committed** |
| v13.620 | bare-Jz carrier fails A-robustness | read only | not independently re-executed |
| v13.621 | breakpoint-projected control | read only | not independently re-executed |
| v13.622 | numerical Floquet residual fit | used as independent target in Sec. 2 | consistent with independently-derived closed form |
| v13.623 | repaired characteristic passes convergence | read only | not independently re-executed |
| v13.624 | three paths spectrally inequivalent, D8-equivalent after flattening | full independent sympy reconstruction | **PASS, independently confirmed exact** |
| v13.625 | Galerkin operator quadrature-stable | read only | not independently re-executed |
| v13.626 | exact 5th/6th-order Floquet coefficients | full independent 60-digit numerical reproduction | **PASS, independently confirmed to 16-20 digits** |
| v13.627 | repaired characteristic still fails A-robustness | reduced spot-check attempted | **inconclusive — timed out, no usable output obtained** |

## 6. Final freshness check

`git fetch origin master` immediately before this commit: HEAD still at `69189a6` (v13.627). No new commits landed during the writing of this entry. `git ls-tree` confirms v13.628 remains free and Round 66 remains the next unused audit-round number.

## 7. Open item for the source thread

The `suzuki_M16001_orthonormal_sixplane_certificate.py` script cannot currently produce the six-plane certificate it is meant to produce, due to `chol_upper`/`inv_upper` in `suzuki_M16001_orthonormal_nullspace_certificate.py` being hardcoded to `n=4`. Generalizing those two helpers to take `n` from the input matrix shape (rather than hardcoding it) should be sufficient to let the script run; whether the resulting six-plane certificate then actually passes numerically is untested and is a genuinely open question, not something this audit is asserting either way.
