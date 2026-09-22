# Cone Derivation Ledger v13.648 — External Audit Round 69

Date: 2026-09-22

Auditor: independent external reviewer, verifying by re-derivation and direct execution wherever feasible.

Scope: the batch left open at the end of Round 68 — v13.639 (magnetic Dyson-log through g^10), v13.640 (chi_-4 source-normalization certification), v13.641 (free Friedrichs continuum obstruction), v13.642 (magnetic endpoint eps^9/eps^10), v13.644 (Dirichlet reference operator / relative Fredholm determinant) — plus the newly-landed v13.647 (Krein boundary-triple bridge). v13.645 (magnetic five-term residual certification) is a self-contained internal numerical cross-check by the source thread and is noted but not independently re-run this round.

## 0. Collision/relevance check

`git fetch origin master` immediately before writing this entry shows HEAD at `1b307c0` (v13.647), no intervening commits. Highest ledger version is v13.647; this entry claims v13.648 / Round 69.

## 1. v13.640 — chi_-4 source-normalization certification: verified by direct code inspection, PASS

Read `research-notes/suzuki_chi4_zeeman_kernel_compression.py`'s `g_chi4` function directly and compared term-by-term against the certified closed formula. Every element matches exactly: the plus-signed prime-power ramp with `chi_-4(n)Lambda(n)/sqrt(n)(T-log n)`, the linear archimedean term `-T/2[psi(3/4)+log(4/pi)]` (code: `linear = -TT/2*(digamma(a)+log(4/pi))`, `a=3/4`), the Lerch term with prefactor `-1/4`, exponent `e^{-3T/2}` (since `a=3/4` gives `e^{-2aT}=e^{-3T/2}`), and the absence of any zeta-pole term. **PASS** — the code genuinely implements the certified formula, not merely a formula that resembles it.

## 2. v13.641 — free Friedrichs continuum obstruction: independently reproduced, PASS

This entry corrects the source thread's own earlier overreach (v13.637/v13.640 had suggested an exact continuum free characteristic could simply be divided out) — a good example of the project's self-correcting discipline. Verified the core claim symbolically: differentiated `N_A(x,y)=(x^2+y^2)/(4A)-|x-y|/2+A/6` directly, confirming `-partial_x^2 N_A = -1/(2A)` away from the diagonal (matching the stated `delta(x-y)-1/(2A)` structure) and `partial_x N_A(pm A,y)=0` exactly (Neumann at both endpoints, confirmed both branches `x>y` and `x<y`), while `d/dx(cosh x+B)|_{x=A}=sinh A\neq0` for `A>0`. The range of `N_A` is confined to zero endpoint derivative but the target has nonzero endpoint derivative — a clean, genuine obstruction. **PASS, exact.**

## 3. v13.644 — Dirichlet reference operator and relative Fredholm determinant: independently reproduced, PASS

Verified from raw ODE theory, not from the ledger's presentation. Solved `u''+z^2u=0` with `u(-A)=0,u'(-A)=1` directly, confirming `u_0(x,z)=\sin(z(x+A))/z` satisfies the ODE and both initial conditions exactly. Confirmed `Delta_{0,A}(z)=u_0(A,z)=\sin(2Az)/z` and the normalized `D_{0,A}(z)=\sin(2Az)/(2Az)` with `D_{0,A}(0)=1` exactly. Confirmed the parity factorization `\sin(2Az)/(2Az)=[\sin(Az)/(Az)]\cos(Az)` exactly (trig identity). Independently reconstructed the Green kernel `R_{0,A}(z^2;x,y)` and confirmed both Dirichlet boundary conditions (`=0` at `x_<=-A` and `x_>=A`) and the correct unit jump condition on the derivative at `x=y`, all exact. **PASS**, on every checkable claim in this entry; the abstract relative-determinant identity in Section 4 (a standard resolvent-factorization fact) was not independently re-derived operator-theoretically but rests on the same correctly-verified reference characteristic.

## 4. v13.639 / v13.642 — magnetic Dyson-log through g^10 and endpoint eps^9/eps^10: independently reproduced, PASS (after resolving two false alarms, both the auditor's own)

### 4a. Raw Floquet coefficients `h_x^{(9)}`, `h_z^{(10)}`

Extended the Round 67 verification method (adaptive high-precision ODE propagation + eigendecomposition matrix-log) to 9th/10th order. An initial 2-point Richardson extrapolation (g=0.08,0.04) showed an apparent ~3e-4 relative mismatch — this was **not a ledger error**: it was insufficient extrapolation order for a 9th/10th-order signal contaminated by the next (11th/12th-order) term. Redone with 3-point Richardson (g=0.08,0.04,0.02), eliminating both the leading and next-order contamination terms:

```
h_x^{(9)}: extrapolated 3.00023842740692...e-6 vs claimed 21745/7247757312 = 3.00023842740941...e-6  (12-digit match)
h_z^{(10)}: extrapolated 4.82294114437456...e-7 vs claimed 5033593/10436770529280 = 4.82294114436877...e-7  (12-digit match)
```

**PASS**, confirmed to ~12 significant digits once the extrapolation was done correctly.

### 4b. Endpoint phase/inversion series `c_phi,9(j)`, `c_P,10(j)`

Independently rebuilt the series expansion in a fresh sympy script exactly as in Round 67. `c_phi,9(j)` matched **exactly, symbolically** (full j-dependence, zero difference). `c_P,10(j)` matched exactly at j=1/2 (symbolic). Extending to j=1 and j=3/2 numerically, an initial check showed an apparent large discrepancy at j=3/2 specifically — this was **the auditor's own bug**: the quick verification script multiplied the already-j-inclusive `c_{P,8}(j)` term by an extra factor of `j` when reconstructing "known terms through eps^8" to subtract, a double-counting invisible exactly at j=1 (where `j^2=j`) but visible at j=3/2. Diagnosed by checking that the residual scaled as `eps^8`, not `eps^{10}`, isolating the bug to the eps^8 subtraction term. After fixing, both j=1 and j=3/2 matched to ~15-16 significant digits (numerical noise floor). **PASS**, fully confirmed at all three test points.

## 5. v13.647 — Krein boundary-triple bridge: one identity confirmed exact, one identity found to have a sign error

This entry does careful, honest scope-control (explicitly separating the bulk perturbation determinant from the boundary-extension determinant, and explicitly flagging in its own Section 7 that the full identification with Suzuki's `W_A` is not yet established). Two specific algebraic identities were checked independently in sympy, treating the relevant quantities as free symbols:

**Section 5 (Suzuki Schur factoring)**: `W_A(theta;z)=(z-i)F_+(z)+e^{i theta}(z+i)F_-(z) = (z-i)F_+(z)[1-e^{i theta}s_A^{Suz}(z)]` with `s_A^{Suz}(z)=-(z+i)F_-(z)/[(z-i)F_+(z)]`. Independently verified: symbolic difference is exactly zero. **PASS, exact.**

**Section 4 (Cayley-transform factorization of `tau-m_A`)**: the entry's boxed claim is
```
tau - m_A(zeta) = -(tau+i)/(2i) * [m_A(zeta)+i] * [1 - e^{i theta} s_A(zeta)]
```
with `s_A(zeta)=(m_A(zeta)-i)/(m_A(zeta)+i)` and `e^{i theta}=(tau-i)/(tau+i)` (both as defined in the entry's own Section 4). Independently expanding the right-hand side symbolically (treating `m_A`, `tau`, `theta` as free symbols and substituting the two stated definitions) gives, exactly:
```
-(tau+i)/(2i) * (m_A+i) * [1-e^{i theta}s_A]  =  -(tau + m_A)
```
**not** `tau - m_A` as claimed — the difference between the claimed left side and the correct simplification of the right side is exactly `-2*tau`, confirmed both by direct sympy simplification and by independent hand algebra. The internally consistent corrected identity is
```
tau + m_A(zeta) = (tau+i)/(2i) * [m_A(zeta)+i] * [1 - e^{i theta} s_A(zeta)]
```
(i.e., a sign flip and `tau-m_A -> tau+m_A` relative to what is printed). This looks like an isolated algebra slip in the Cayley-transform substitution, not a defect in the surrounding framework: Krein's formula itself (Section 2, using `tau-m_A(zeta)` as the standard rank-one perturbation scalar) is the standard, correctly-stated textbook object, and Section 5's independent factoring of the printed `W_A` is unaffected by this error, since it does not depend on Section 4's specific numeric identity. Because Section 7 already flags the overall Weyl/Suzuki identification as an open next gate rather than an established result, this error does not appear to invalidate any currently-promoted conclusion, but the boxed formula in Section 4 should be corrected before further work builds on it directly.

## 6. Summary

| Entry | Claim | Verification | Outcome |
|---|---|---|---|
| v13.640 | chi_-4 source formula matches code | direct code inspection, term-by-term | **PASS, exact** |
| v13.641 | free continuum deficiency has no solution | independent symbolic differentiation | **PASS, exact** |
| v13.644 | Dirichlet reference operator, characteristic, Green kernel | independent ODE/Green-function reconstruction | **PASS, exact** (relative-determinant identity not independently re-derived) |
| v13.639 | `h_x^{(9)}`, `h_z^{(10)}` exact coefficients | independent 60-digit adaptive ODE + 3-point Richardson | **PASS, ~12-digit match** |
| v13.642 | `c_phi,9(j)`, `c_P,10(j)` endpoint series | independent sympy reconstruction, symbolic + numeric | **PASS, exact / ~15-digit match** |
| v13.647 §5 | Suzuki `W_A` Schur factoring | independent symbolic algebra | **PASS, exact** |
| v13.647 §4 | Cayley-transform factorization of `tau-m_A` | independent symbolic algebra | **Sign error found**; corrected identity derived and reported |

## 7. Auditor's own errors, corrected in the course of this round

Two false alarms were raised and resolved during this round, both due to the auditor's own verification-script bugs rather than ledger errors: (a) an initial 2-point Richardson extrapolation for `h_x^{(9)}`/`h_z^{(10)}` was insufficiently accurate for a 9th/10th-order signal and was replaced with a 3-point extrapolation; (b) a double-counted `j` factor in reconstructing the eps^8 subtraction term for the `c_P,10(j)` check produced a spurious large discrepancy at j=3/2 (invisible at j=1 where `j^2=j`), diagnosed by checking the residual's actual scaling power and fixed. Recorded per this audit's standing practice of reporting its own errors alongside genuine source-thread findings.

## 8. Final freshness check

`git fetch origin master` immediately before this commit: HEAD still at `1b307c0`. No new commits landed while writing this entry. `git ls-tree` confirms v13.648 remains free.

## 9. Open for a future round

v13.645 (magnetic-driver five-term residual-order certification) remains a self-contained internal cross-check not yet independently re-run by this audit thread.
