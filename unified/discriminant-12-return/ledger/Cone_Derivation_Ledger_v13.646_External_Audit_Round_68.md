# Cone Derivation Ledger v13.646 — External Audit Round 68

Date: 2026-09-22

Auditor: independent external reviewer, verifying by re-derivation and direct execution wherever feasible, not by re-checking the ledger's own presented numbers.

Scope: the LQG/tetrahedron thread's response to External Audit Checkpoint v13.635 and Addendum v13.638 — v13.636 (synthesis closure), its standalone companion `Three_Weighted_Paths_and_the_Flattened_D8_Skeleton.md`, v13.643 (j=3/2 driven-spin analog simulation), and its standalone companion `Driven_Spin_Analog_Simulation_of_Flattened_Tetrahedral_Orientation_j3_2.md`. This round does not cover the concurrently-landed magnetic-driver (v13.639, v13.642, v13.645) or chi_-4 (v13.640, v13.641, v13.644) entries; those remain open for a future round.

## 0. Collision/relevance check

`git fetch origin master` immediately before writing this entry shows HEAD at `e75d7bb` (the v13.645 renumbering fix pushed by this same external audit thread earlier), no intervening commits. Highest ledger version is v13.645; this entry claims v13.646 / Round 68. Re-checked again immediately before commit (Section 5).

Two version collisions were found and fixed by this audit thread earlier in this session, ahead of this round's write-up: `v13.641` (`Free_Friedrichs_Continuum_Obstruction...` vs `Magnetic-Driver_Endpoint_e9_e10`, the latter renumbered to v13.642) and `v13.644` (`Dirichlet_Reference_Operator...` vs `Magnetic-Driver_Five-Term_Residual...`, the latter renumbered to v13.645). Both fixes are already pushed; no further collision action is needed here.

## 1. v13.636 / companion — LQG synthesis closure: independently reproduced, PASS

This entry and its companion restate the content already independently verified in External Audit Rounds 66-67 (v13.624's spectral inequivalence, v13.631's constructive intertwiner) as a closed synthesis theorem. Spot-checked that the restated boxed claims (bipartite parity law, `R^2=-I`/`R^4=I`/`HRH=-R`, the parity-adapted normal form, the dyadic intertwiner, the integer-j zero-line extension, the `O(N_j)` nonuniqueness) are a faithful, non-weakened restatement of what was already confirmed exactly on independent test data in Round 67 — no new numerical or symbolic claim is introduced here beyond the synthesis itself. **PASS**, on the basis of the underlying results already independently re-derived, not re-verified from scratch a second time.

The companion note correctly separates itself from the analog-simulation question (v13.638) and stops at the closed theorem, exactly as recommended in the checkpoint and addendum. All required guardrails (no physical equivalence claim; no established chi_-4 link; no E8/Coldea claim beyond "outside observation") are present and correctly worded.

## 2. v13.643 / companion — j=3/2 driven-spin analog simulation: independently reproduced, with one erratum found

This is substantial new mathematics — a no-go theorem plus an explicit two-stage pulse-synthesis protocol — built directly from raw spin operators, not restated from prior rounds. Verified independently in sympy/mpmath, building `J_x`, `J_y`, `J_z` for j=3/2 from the standard ladder-operator formulas with no dependence on any matrix the ledger printed.

### 2a. `L_Y=2J_x`, `R_Y=H\,\mathrm{sgn}(2J_x)`: exact match, PASS

Independently built `2J_x` and confirmed it matches the claimed matrix exactly. Built `sgn(2J_x)` via the exact interpolating polynomial `13x/12 - x^3/12` on the eigenvalues `{-3,-1,1,3}` (a different route from the ledger's own presentation but mathematically forced, since the polynomial is the unique degree-3 interpolant), formed `R_Y=H\cdot\mathrm{sgn}(2J_x)`, and confirmed it matches the claimed matrix exactly, with `R_Y^T=-R_Y` and `R_Y^2=-I` both exact.

### 2b. Zeeman-only no-go theorem: independently reconstructed, PASS

Built the spin-3/2 (symmetric-cube) representation of a general `SU(2)` element `g=\begin{pmatrix}\alpha&\beta\\-\bar\beta&\bar\alpha\end{pmatrix}` completely from scratch, via explicit polynomial action on the symmetric-cube basis monomials `E_1^{3-k}E_2^k`, with no reference to the ledger's own presentation of this fact. Independently confirmed the extremal matrix elements `|D^{(3/2)}_{-3/2,-3/2}(g)|=|\alpha|^3` and `|D^{(3/2)}_{-3/2,+3/2}(g)|=|\beta|^3` fall out of that construction. Combined with `(R_Y)_{-3/2,-3/2}=0` (confirmed exactly above) forcing `\alpha=0`, hence `|\beta|=1`, hence `|D^{(3/2)}_{-3/2,+3/2}|=1`, while the actual value `|(R_Y)_{-3/2,+3/2}|=1/2` — a genuine contradiction, independently confirmed. **PASS**, and a legitimate, cleanly-stated no-go result.

### 2c. Exact pulse synthesis: independently reproduced as a full matrix identity, PASS

Independently diagonalized `J_x` (exactly, since `J_x` and `J_x^2` share eigenvectors), formed `X(\pi)Q_x(\pi/2)=\exp[-i(\pi J_x+\frac{\pi}{2}J_x^2)]` directly from the eigenvalues, and confirmed the full 4x4 matrix identity `X(\pi)Q_x(\pi/2)=e^{-5i\pi/8}\,\mathrm{sgn}(2J_x)` holds exactly (symbolic difference is the zero matrix), not merely on the four eigenvalues as the ledger's own presentation checks it. Independently confirmed `Z(-\pi)=e^{i\pi J_z}=iH` by direct computation. Combined these to confirm the full claimed identity `R_Y=e^{i\pi/8}Z(-\pi)X(\pi)Q_x(\pi/2)` holds exactly as a matrix equation. **PASS.**

### 2d. Tetrahedral carrier, intertwiner, transported protocol, and gauge optimization: independently reproduced, PASS

Built `Q_a` for j=3/2 from the raw `a_k=(k/2)c_k` formula (independent of anything already in the ledger for this specific j), confirmed it is Hermitian with eigenvalues `\pm3\sqrt3/4,\pm3\sqrt{35}/4`, and confirmed `R_a=-i\,\mathrm{sgn}(Q_a)` (via eigendecomposition at 50-digit precision) matches the claimed `p,q`-parameterized matrix to ~50 digits, with `R_a^2=-I` and `HR_aH=-R_a` both confirmed.

Built the intertwiner two ways: first as a literal transcription of the printed `U^{(0)}` matrix, then independently from the raw dyadic-sum definition `U_{a\leftarrow Y}=\sum_r(|e_r^a\rangle\langle e_r^Y|+|R_ae_r^a\rangle\langle R_Ye_r^Y|)` with `e_1^Y=E_0,e_2^Y=E_2` (the two `H=+1` standard basis vectors). Both constructions agree with each other and satisfy `U^{(0)T}U^{(0)}=I`, `U^{(0)}H=HU^{(0)}`, and `U^{(0)}R_Y(U^{(0)})^T=R_a` exactly (50-digit precision, effectively exact).

Confirmed the full transported protocol `R_a=e^{i\pi/8}Z(-\pi)\exp[-i(\pi K_a+\frac{\pi}{2}K_a^2)]` holds exactly, using `K_a=U^{(0)}J_x(U^{(0)})^T` built directly from the correctly-reconstructed `U^{(0)}` (matched to ~50 digits / effectively exact).

Confirmed the full `O(2)`-gauge family: reconstructed `U(\theta)` correctly from the dyadic-sum definition with the a-carrier's even reference basis rotated by `\theta` (this required correcting an initial mistaken implementation on the auditor's own side, described in Section 3), then confirmed the claimed formula `(K_a(\theta))_{03}=-q+\frac{q-\sqrt3p}{4}\cos2\theta+\frac{p+\sqrt3q}{4}\sin2\theta` exactly at four test angles, confirmed the amplitude-squared identity `\left(\frac{q-\sqrt3p}{4}\right)^2+\left(\frac{p+\sqrt3q}{4}\right)^2=\frac14` exactly, confirmed `\theta_{\min}\approx1.02368581342` and the value `(K_a)_{03}^{\rm opt}=-q+\frac12` there, and confirmed the promoted minimal bound `\min_{O(2)}|(K_a)_{03}|=q-\frac12\approx0.040155818076` exactly. **PASS** on all of Section 6-7 of the note (the genuinely promoted, load-bearing results).

### 2e. Erratum found: the printed `K_a^{(0)}` matrix has an incorrect pair of entries

The static matrix `K_a^{(0)}=U^{(0)}J_x(U^{(0)})^T` printed in Section 6 of both v13.643 and its companion note is:

```
K_a^{(0)} = (1/4) * [[0, sqrt3 q - 3p, 0, -sqrt3 p - 3q],
                     [sqrt3 q - 3p, 0, 7q - sqrt3 p, 0],
                     [0, 7q - sqrt3 p, 0, -7p - sqrt3 q],
                     [-sqrt3 p - 3q, 0, -7p - sqrt3 q, 0]]
```

Independent exact symbolic computation of `U^{(0)}J_x(U^{(0)})^T` (sympy, treating `p,q` as free symbols, no numeric substitution) gives:

```
(K_a^{(0)})_{01} = (sqrt3 q - 3p)/4        -- matches
(K_a^{(0)})_{03} = -(sqrt3 p + 3q)/4       -- matches
(K_a^{(0)})_{12} = (5q - sqrt3 p)/4        -- ledger prints (7q - sqrt3 p)/4  -- MISMATCH
(K_a^{(0)})_{23} = -(5p + sqrt3 q)/4       -- ledger prints -(7p + sqrt3 q)/4 -- MISMATCH
```

The `(0,1)` and `(0,3)` entries — the ones that directly feed the promoted `(K_a(\theta))_{03}` formula checked in Section 2d — are correct. The `(1,2)`/`(2,1)` and `(2,3)`/`(3,2)` entries have a coefficient of `7` where exact computation gives `5`. This looks like an isolated arithmetic slip in deriving or transcribing that one static matrix, not a defect in the underlying construction: every claim that is actually *used* downstream (the transported exponential identity, the full `\theta`-family, `\theta_{\min}`, and the promoted minimal-coupling bound) was independently re-derived from the correct dyadic-sum definition of `U(\theta)` and matches exactly, unaffected by this typo. Recommend the source thread correct the two boxed matrix entries in both files; no other change is needed.

## 3. Auditor's own error, corrected in the course of this verification

An initial attempt to verify the `O(2)`-gauge family (Section 2d) used a naive construction `o_r'=R_a\cdot e_r'` applied directly to rotated standard-basis-like vectors, which does not correctly implement the dyadic-sum intertwiner definition — a standard basis vector at an odd index is not itself an image of `R_Y` on a standard basis vector, so this produced a family that did not match at `\theta=0`. Diagnosed by checking `\theta=0` against the confirmed-correct `U^{(0)}`, corrected by rebuilding `U(\theta)` directly from the dyadic sum `\sum_r(|e_r^a(\theta)\rangle\langle e_r^Y|+|R_ae_r^a(\theta)\rangle\langle R_Ye_r^Y|)` with the Y-side basis held fixed, after which all checks in Section 2d passed exactly. Recorded here per this audit's standing practice of reporting its own errors alongside the source thread's.

## 4. Summary

| Entry | Claim | Verification | Outcome |
|---|---|---|---|
| v13.636 + companion | LQG synthesis closure | restates Round 66/67 results faithfully; guardrails correct | PASS (no new claim beyond prior rounds) |
| v13.643 §2 (no-go) | Zeeman-only control cannot realize `R_Y` | independent symmetric-cube construction from scratch | **PASS, exact** |
| v13.643 §3 (pulse synthesis) | `R_Y=e^{i\pi/8}Z(-\pi)X(\pi)Q_x(\pi/2)` | independent eigenbasis construction, full matrix identity | **PASS, exact** |
| v13.643 §4-5 (intertwiner, `R_a`) | explicit `U^{(0)}`, `R_a` matrix | independent dyadic-sum + eigendecomposition construction | **PASS, ~50-digit match** |
| v13.643 §6 (transported protocol, `K_a^{(0)}` matrix) | transported exponential identity; static `K_a^{(0)}` matrix | identity confirmed exact; static matrix has a coefficient typo (7 should be 5) in two symmetric entries | **Identity PASS; matrix erratum found** |
| v13.643 §7 (`O(2)` gauge optimization) | formula, `\theta_{\min}`, minimal bound `q-1/2` | independently re-derived from corrected `U(\theta)` construction | **PASS, exact** |

## 5. Final freshness check

`git fetch origin master` immediately before this commit: HEAD still at `e75d7bb`. No new commits landed while writing this entry. `git ls-tree` confirms v13.646 remains free.

## 6. Open for a future round

v13.639 (magnetic Dyson-log g^10), v13.640 (chi_-4 source-normalization certification), v13.641 (free Friedrichs continuum obstruction), v13.642 (magnetic endpoint eps^9/eps^10, renumbered), v13.644 (Dirichlet reference operator / relative Fredholm determinant), v13.645 (magnetic five-term residual certification, renumbered) have not yet been independently verified by this audit thread and remain open.
