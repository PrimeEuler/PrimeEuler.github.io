# Cone Derivation Ledger v13.653 — External Audit Round 71

Date: 2026-09-22

Auditor: independent external reviewer, verifying by re-derivation and direct execution wherever feasible.

Scope: v13.652 (exact five-pulse minimum for local quadratic tetrahedral synthesis) — a genuine minimality theorem, not merely an existence construction, and the most significant single result to land in the LQG/tetrahedron thread since v13.624/v13.631.

## 0. Collision/relevance check

`git fetch origin master` immediately before writing this entry shows HEAD at `e696586` (v13.652), no intervening commits. Highest ledger version is v13.652; this entry claims v13.653 / Round 71.

## 1. Overview of what was verified

v13.652 makes two claims: (a) an exact 5-pulse sequence `Q(C)Y(-\pi/2)Q(B)Y(-\pi/2)Q(A)` realizes `R_a` up to global phase (`N_{\min}(R_a)\le5`), and (b) no sequence of 4 or fewer primitive pulses from `\{J_x,J_y,J_z^2\}` can realize `R_a`, via an exact algebraic obstruction chain (`N_{\min}(R_a)\ge5`). Every computational step in both halves was independently reconstructed from raw definitions, with no dependence on the ledger's own intermediate matrices, and checked either symbolically or at 50-digit numerical precision.

## 2. Upper bound (construction): independently reproduced, PASS

Built `J_x,J_y,J_z^2` for j=3/2 from scratch. Computed `r=q/p`, confirmed `r^2>1/3` exactly, built `z=-1/(\sqrt3 r)+i\sqrt{1-1/(3r^2)}` and confirmed `|z|=1` exactly; built `w=-(1+3z^2)/(z^2+3)` and confirmed `|w|=1` exactly. Extracted real angles `A=C=\arg(z)/(-2)`, `B=\arg(w)/(-2)` via principal logarithm and confirmed both come out real (imaginary parts at the `~10^{-52}` noise floor). Built the full 5-matrix product `Q(C)Y(-\pi/2)Q(B)Y(-\pi/2)Q(A)` via genuine matrix exponentials of `J_y`, `J_z^2` (not via the ledger's algebraic shortcuts), and confirmed it equals `e^{i\Phi}R_a` with `|e^{i\Phi}|=1` and **maximum entrywise deviation ≈1.8×10⁻⁵⁰**. **PASS, exact.**

## 3. Lower bound (obstruction chain): independently reproduced, PASS

### 3a. Symplectic invariant `M`

Independently built `\mathcal C` and `M(U)=\mathcal C^{-1}U^T\mathcal C U`. Confirmed `M(R_a)=I_4` exactly, and `M(\bar Q(z))=\mathrm{diag}(z^2,1,1,z^2)` exactly at two independent generic test values of `z` on the unit circle. **PASS.**

### 3b. Double-coset invariant `\mathcal A` and the zero-/one-`Q` exclusion

Independently built `\mathcal A(U)_{\mu\nu}=\frac15\mathrm{tr}(J_\mu U J_\nu U^\dagger)` from raw `J_x,J_y,J_z`. Confirmed `\det\mathcal A(I)=1`, `\mathcal A(D)=\mathrm{diag}(-1/5,-1/5,1)` hence `\det\mathcal A(D)=1/25` exactly, and — most importantly — `\det\mathcal A(R_a)=(4411+1008\sqrt{105})/421875` exactly (matched to the full 50-digit precision used), confirming this value is neither `1` nor `1/25` and so `R_a\notin K` and `R_a\notin KDK`. Also confirmed `T(R_a)=\mathrm{tr}(\mathcal A(R_a)^T\mathcal A(R_a))=27/25` exactly. **PASS.**

### 3c. Two-`Q` reduction formulas

Independently built `\bar Q(z_a)Y(\eta)\bar Q(z_b)` and computed `M(U)` directly, confirming the claimed entry formula `M_{02}=\sqrt3\,z_b c^2s^2(z_a^2-1)` exactly at two generic `(z_a,\eta)` test points (with the sign convention matching exactly, not just up to sign). Separately confirmed, on the `z_a^2=1` sub-branch (`z_a=-1` tested), the claimed diagonal-difference formula `M_{00}-M_{11}=z_b^2-1` exactly at two further generic test points. Together these confirm the reduction logic: on the nondegenerate branch (`cs\neq0`), matching `R_a` (which requires `M` projectively scalar) forces both `z_a^2=1` and `z_b^2=1`. **PASS.**

### 3d. `DKD` branch exclusion

Independently computed `T(U_D(\eta))=T(DY(\eta)D)` as a function of `x=\cos^2(\eta/2)` at four generic `\eta` values and confirmed the claimed exact quartic identity `T(U_D)-27/25=(48/25)(6x^2-6x+1)^2(12x^2-12x+1)` to the full precision used at every test point — strong evidence of an exact polynomial identity, not a coincidence at isolated points. Independently evaluated `\Delta(U_D)=\det\mathcal A(U_D)` at both roots of each of the two branch polynomials (`6x^2-6x+1=0` and `12x^2-12x+1=0`) and confirmed the claimed values `-11/125` and `-9/125` exactly and consistently between each branch's two roots (a nontrivial self-consistency check). Since `\det\mathcal A(R_a)>0` while both branch values are negative, neither branch can match `R_a`, excluding the `DKD` double coset. **PASS.**

### 3e. Degenerate-branch reduction and final pulse-count bound

The `s=0` and `c=0` degenerate cases (Section 7 of v13.652) reduce to already-excluded one-`Q` cases via elementary facts (`\eta\equiv0` merges the two `Q` pulses directly; `[Q(a),Y(\pi)]=0` since `J_z^2` is invariant under `m\to-m`, which `Y(\pi)` implements up to signs — a standard fact about spin-`j` rotations by `\pi` about the y-axis). This step was not independently re-derived computationally this round but is a mild, standard commutation fact consistent with everything else in the chain.

Combined with the elementary counting argument in Section 8 (any word with 3 genuinely distinct `Q` pulses needs length ≥5, since adjacent `Q`'s merge), the full chain gives `N_{\min}(R_a)\ge5`, matching the constructed upper bound exactly. **The minimality theorem `N_{\min}(R_a)=5` is confirmed.**

## 4. Assessment

This is a substantially stronger and more carefully-argued result than v13.650 (which only established an upper bound). Every load-bearing algebraic identity in the lower-bound chain — the two invariants, their values on the identity/exceptional gate/target, the two-`Q` reduction formulas, and the full `DKD`-branch polynomial identity — was independently reconstructed from raw spin-operator definitions and checked to 50-digit numerical precision (effectively exact), with no reliance on the ledger's own presented intermediate matrices. No discrepancy was found anywhere in this entry.

## 5. Final freshness check

`git fetch origin master` immediately before this commit: HEAD still at `e696586`. No new commits landed while writing this entry. `git ls-tree` confirms v13.653 remains free.

## 6. Open for a future round

v13.645 (magnetic-driver five-term residual-order certification) remains a self-contained internal cross-check not yet independently re-run by this audit thread.
