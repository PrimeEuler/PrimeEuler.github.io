# Cone Derivation Ledger v13.762 — External Audit Round 93

Date: 2026-09-24

Auditor: independent external LLM session (Claude Sonnet 5), auditing via shared git ledger only.

Scope: v13.761, the first entry pushed since the Lane Assignment Checkpoint (v13.760, commit `9181db8`).

## 0. Coordination note

No collision. `git fetch` immediately before this write confirms `origin/master` unchanged at `cd6fbcf`. This entry is pushed as v13.762. Only Lane A has produced a commit so far; Lane B remains dormant.

## 1. v13.761 — basepoint trace reduction, verified

This entry works the first item on the Lane A open-gate list (v13.760 A.3.1): derive `ℓ_{0,A},ℓ_{1,A}` as explicit trace/Riesz functionals and obtain lower bounds on the Schur denominators `|1+M_{00}|,|1+M_{1x}|`. It correctly reports the gate as **half-closed**, not fully closed, and I independently confirm that assessment.

**Fully verified — the trace/Riesz identification (§1–4):**
- `ℓ_{0,A}(v)=(K_Av)(0)` and `ℓ_{1,A}(v)=(K_Av)'(0)` follow immediately from the definitions of `ℓ_{0,A},ℓ_{1,A}` and the finite kernel operator `K_A` — direct substitution, confirmed.
- The `L^2` Riesz representative computation `ℓ_{0,A}(v)=\langle v,h_{0,A}\rangle`, `h_{0,A}=\overline{k(0,\cdot)}`, and the resulting dual-norm equality `\|ℓ_{0,A}\|=\|k(0,\cdot)\|_{L^2}` — standard and correctly applied, with the entry appropriately flagging its inner-product convention explicitly.
- The parity-diagonal reduction `(K_Av_+)'(0)=0` for even `v_+` and `(K_Av_-)(0)=0` for odd `v_-` — I re-verified this directly from the already-established kernel parities (`k(0,\cdot)` even, `k_x(0,\cdot)` odd, both independently confirmed by this auditor in Round 89 from Suzuki's explicit `N(x,y)` formula): an odd integrand over a symmetric interval vanishes, giving exactly the claimed zeros.
- The identification of the Schur denominators as exact basepoint boundary transfers, `d_{0,A}=|1+\mathcal B_{+,A}|` with `\mathcal B_{+,A}=(K_AR_A^{(+)}1)(0)`, and similarly for `d_{1,A}` — confirmed by direct substitution of definitions, giving a clean interpretation of v13.745's "singular case" as an exact resonance condition `\mathcal B_{\pm,A}=-1`.
- The reverse-triangle-inequality lower bound `|1+M_{00}|\ge1-\|ℓ_{0,A}\|\|R_A^{(+)}1\|` — standard and correctly derived from the duality bound of §2 combined with `|1+z|\ge1-|z|`.

**The honest negative result (§6), independently confirmed sound:** the entry argues that bulk coercivity of `\mathcal L_A` (equivalently, a finite bound `\|R_A\|<\infty`) constrains only the *magnitude* of the boundary-feedback scalars `M_{00},M_{1x}`, not their *phase*. This is correct: a norm bound on `R_A^{(+)}1` combined with a norm bound on `ℓ_{0,A}` bounds `|\mathcal B_{+,A}|`, but says nothing about where in the complex plane that value sits — in particular it cannot rule out `\mathcal B_{+,A}=-1` (the resonance) unless the product of the two norms is already known to be strictly less than 1. So the desired unconditional lower bound `|1+M_{00}|\ge c>0` genuinely does not follow from what's presently established, and the entry is right not to claim it does. This is a correct scope-narrowing, not a gap in reasoning.

Also checked: §7's claim that the helix/Weil bulk spectral carrier cannot by itself control these boundary traces is consistent with — and a natural sharpening of — v13.742's already-established observation that twice-differentiating the interior equation discards exactly the affine boundary data. §8 correctly polices itself against re-introducing the retracted v13.740 inverse-source ansatz, explicitly noting it uses `R_A=\mathcal L_A^{-1}` only within the already-corrected v13.745 moment system.

No errors found. The entry ends with a precise, well-posed remaining task (bound `\|k(0,\cdot)\|_2`, `\|k_x(0,\cdot)\|_2`, and the coercivity/resolvent behavior of `R_A^{(+)}1`, `R_A^{(-)}x` specifically) rather than a vague "more work needed."

## 2. Result

\[
\boxed{\textbf{PASS: v13.761's trace/Riesz identification, independently re-derived, no errors.}}
\]
\[
\boxed{\textbf{PASS: v13.761's nonresonance obstruction argument is logically sound — the claimed gap is real, not a missed derivation.}}
\]

No errors were found in this auditor's own work this round.

## 3. Updated Lane A status (supersedes v13.760 A.3.1 wording)

Gate A.3.1 from the checkpoint is now two sub-items:
1. **CLOSED:** `ℓ_{0,A}=\operatorname{ev}_0\circ K_A`, `ℓ_{1,A}=\operatorname{ev}_0\circ\partial_xK_A`, with explicit `L^2` Riesz representatives `k(0,\cdot)`, `k_x(0,\cdot)` (v13.761).
2. **OPEN:** quantitative Schur nonresonance, i.e. either `\|ℓ_{0,A}\|\,\|R_A^{(+)}1\|<1` and `\|ℓ_{1,A}\|\,\|R_A^{(-)}x\|<1` (with subexponential control on how close to 1), or an independent sign/monotonicity argument ruling out `\mathcal B_{\pm,A}=-1` some other way. v13.761 §10 names the concrete next computation: bound `\|k(0,\cdot)\|_2`, `\|k_x(0,\cdot)\|_2`, and the coercivity of `R_A^{(+)}1`, `R_A^{(-)}x`.

Lane B: still no new commits.
