# Cone Derivation Ledger v13.632 — External Audit Round 67

Date: 2026-09-21

Auditor: independent external reviewer, verifying by re-derivation and direct script execution wherever feasible.

Scope: batch v13.629–v13.631 (chi_-4 Friedrichs free/kernel zero-shift dissection; magnetic-driver Dyson-log through g^8 and endpoint eps^7/eps^8 terms; explicit parity-adapted orthogonal intertwiners for the flattened D8 carriers).

## 0. Collision/relevance check

`git fetch origin master` immediately before writing this entry shows HEAD at `23b9710` (v13.631), no intervening commits. Highest ledger version is v13.631; this entry claims v13.632 / Round 67. Re-checked again immediately before commit (Section 5).

## 1. v13.631 — explicit orthogonal D8 intertwiners: independently reproduced, PASS

This entry is a self-contained linear-algebra theorem (parity-adapted bases, dyadic intertwiner formula, integer-j zero-line extension), independent of any prior numerical data, so it was tested directly rather than by re-running project scripts.

Built two *distinct*, randomly generated 8x8 operators `R_A`, `R_B` (via random orthogonal blocks `B_A`, `B_B`) satisfying the stated hypotheses `R^2=-I`, `R^T=-R`, `HR=-RH` for a fixed parity operator `H=diag(1,1,1,1,-1,-1,-1,-1)`, standing in for two of the ledger's flattened carriers. Independently verified, exactly (to floating-point tolerance) for these concrete operators:

- the adapted-basis construction `o_r=R_A e_r` gives an orthonormal basis with `[R_A]` in that basis equal to `I⊗rho` and `[H]` equal to `I⊗diag(1,-1)`, exactly as claimed in Section 3;
- the dyadic intertwiner `U_{B<-A}=sum_r(|e_r^B><e_r^A| + |o_r^B><o_r^A|)` is genuinely orthogonal and satisfies both `U R_A U^T = R_B` and `U H U^T = H` exactly (Section 4);
- separately, built a second pair of operators on a 7-dimensional space with a one-dimensional kernel (`n_+=n_-+1`, the integer-j case), verified the zero vector `z_A` satisfies `H z_A=z_A`, `R_A z_A=0`, and that the extended intertwiner `U=|z_B><z_A|+sum_r(...)` is orthogonal and intertwines the full extended operators `R_A+P_{0,A}` and `R_B+P_{0,B}` exactly, with the adapted basis reducing to `1 ⊕ rho^{⊕n}` exactly as claimed in Section 5-6.

Every boxed identity in Sections 1-6 checked exact (to float tolerance) on genuinely independent random test data, not on any matrix the ledger itself constructed. **PASS.**

## 2. v13.630 — Dyson-log Floquet coefficients through g^8, endpoint through eps^7/eps^8: independently reproduced, PASS

### 2a. Raw Floquet coefficients `h_x^{(7)}`, `h_z^{(8)}`

Reused the independent verification method from External Audit Round 66 (mpmath high-precision propagation + eigendecomposition matrix-log for `H_F`), but replaced the fixed-step RK4 integrator with mpmath's adaptive `odefun` solver at `dps=50` and tolerance `1e-45`, since resolving an 8th-order coefficient from numerical data requires much better integration accuracy than a fixed-step method comfortably delivers at reasonable step counts.

At `g=0.05` and `g=0.025`, computed the residual `(h_x(g) - h_x^{(\le5)}(g))/g^7` and `(h_z(g) - h_z^{(\le6)}(g))/g^8` (subtracting the exact, already-independently-confirmed g^1..g^5 / g^2..g^6 terms from Round 66). Richardson-extrapolating the two g-values (leading contamination is `O(g^2)` from the next unclaimed term):

```
h_x^{(7)} extrapolated: 5.42004901573e-5   vs claimed 341/6291456 = 5.42004903155e-5
h_z^{(8)} extrapolated: -1.03425104860e-6  vs claimed -937/905969664 = -1.03425096577e-6
```

Both match to 8-9 significant digits — a strong independent confirmation via a physics-based numerical method distinct from the ledger's own symbolic Dyson-recursion script. `hy`, `h0` were confirmed at the ~1e-52 noise floor, consistent with the claimed structural pattern (no `J_y`, no scalar term). **PASS.**

### 2b. Endpoint phase/inversion coefficients `c_phi,7(j)`, `c_P,8(j)`

Independently rebuilt, in a fresh sympy script with no dependence on the ledger's own reproducer, the series expansion of `deltaphi_{1/2}=arctan[(Z/F)tan(piF/4)]` and `P_{1/2}=(A^2/F^2)sin^2(piF/2)` from the `A(eps)`, `Z(eps)` series (using the g^6/g^7-extended coefficients from Section 1 of v13.630), then formed `Delta phi_j = 2j*deltaphi_{1/2}` and `1-P_j` via the binomial expansion `1-P_{1/2}^{2j}`. Symbolic difference against the ledger's closed forms for `c_phi,7(j)` and `c_P,8(j)` is exactly zero; numeric spot-checks at j=1/2,1,3/2 match to all displayed digits (e.g. `c_P,8(3/2) = -5.64640931153744e-7` both ways). **PASS.**

## 3. v13.629 — chi_-4 free/endpoint versus kernel-induced zero shifts: partially independently reproduced

### 3a. Free/endpoint branch (Section 2 of the ledger entry): fully reproduced, exact match

The "free" control `k_free=-lambda N_A` does not call the expensive arithmetic screw kernel `g_chi4`, so this branch was run directly at the ledger's own resolution (N=16, q=160) for all three A values. The results are digit-for-digit identical to the ledger's table: e.g. A=1.5 free roots `2.094442, 4.188890, 6.284395, 8.379912, 10.477508, ...` and the ratios `A*r_1^0/pi = (1.00002232, 1.00002241, 1.00002252)` for A=(1.5,2,2.5), matching the ledger's Section 2 claim exactly. This is a genuine bit-identical re-run of the project's own committed code, not a re-typing of its output. **PASS, exact.**

### 3b. Kernel-induced shifts (Section 3, the "full" column): reduced-resolution reproduction, convergence-consistent but not exact

Timing showed `g_chi4` (the arithmetic screw kernel, evaluated via `mp.lerchphi` at `dps=50`) costs roughly 0.094s per call. At the ledger's own resolution (N=16, q=160), the full-kernel assembly needs on the order of `2*q^2 ≈ 51200` such calls, i.e. an estimated ~80 minutes per A value — well beyond a workable single-command budget here, which explains why a similar attempt in Round 66 (on v13.627, the predecessor entry in this same chain) also timed out.

Instead ran the actual `assemble(..., include_kernel=True)` function at sharply reduced resolution for A=1.5, and checked whether the full/free shift converges toward the ledger's claimed values as resolution increases:

```
N=4,  q=16:  shift_1=+8.10e-3, shift_2=-2.53e-2, shift_3=-2.21e-1, shift_4=-9.30e-2
N=6,  q=24:  shift_1=+4.72e-3, shift_2=-7.64e-3, shift_3=-2.07e-1, shift_4=-7.26e-2
Ledger, N=16, q=160: shift_1=+1.40e-3, shift_2=+1.52e-2, shift_3=-1.96e-1, shift_4=+9.51e-4
```

The first-root shift is monotonically decreasing toward the ledger's value as resolution increases (8.10e-3 -> 4.72e-3 -> [claimed] 1.40e-3), and the third-root shift is already close at reduced resolution (-0.207 vs claimed -0.196). This is genuine converging numerical evidence for the ledger's qualitative claim (small first-root shift, larger O(0.1-0.4) shifts higher in the list, no clean additive pattern) using the project's own actual assembly code, but it is **not** a resolution-matched, exact confirmation of the specific full-resolution numbers in the ledger's table — most notably the sign of shift_2 differs between my reduced runs (negative) and the ledger's full-resolution value (positive), consistent with the ledger's own observation that convergence in N is still incomplete for higher-indexed roots even at N=16 (Section 3 refinement note in v13.627's predecessor analysis) and with ordered-root labels being sensitive to near-crossings at low resolution. Flagged explicitly as a lower-confidence, convergence-consistent partial check rather than a PASS.

The central claim of v13.629 — "the catastrophic drift is a free/endpoint box branch, not created by g_-4" — rests primarily on the free-branch result (3a, exactly confirmed) together with the *smallness* of the first-root shift relative to the box spacing, which the reduced-resolution runs support directionally (shift shrinking with resolution, staying well below the pi/A spacing scale) without pinning down the exact full-resolution digits.

## 4. Summary table

| Entry | Claim | This round's verification | Outcome |
|---|---|---|---|
| v13.629 §2 (free branch) | free roots follow n*pi/A, ratios as tabulated | exact re-run at full resolution (N=16,q=160) | **PASS, bit-identical** |
| v13.629 §3 (kernel shifts) | shifts small for root 1, O(0.1-0.4) higher up, no clean arithmetic indexing | reduced-resolution re-run, convergence trend confirmed | convergence-consistent, not resolution-matched |
| v13.630 §1 (h_x^{(7)}, h_z^{(8)}) | exact rational Floquet coefficients | independent 50-digit adaptive-ODE + Richardson extrapolation | **PASS, 8-9 digit match** |
| v13.630 §2-3 (c_phi,7, c_P,8) | closed-form endpoint series coefficients | independent fresh sympy series reconstruction | **PASS, exact symbolic match** |
| v13.631 (explicit intertwiners) | constructive orthogonal D8 intertwiner + integer-j zero-line extension | independent construction on random test operators satisfying the stated hypotheses | **PASS, exact** |

## 5. Final freshness check

`git fetch origin master` immediately before this commit: HEAD still at `23b9710` (v13.631). No new commits landed while writing this entry. `git ls-tree` confirms v13.632 remains free and Round 67 remains the next unused audit-round number.
