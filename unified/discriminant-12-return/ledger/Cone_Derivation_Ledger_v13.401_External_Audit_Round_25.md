# Cone Derivation Ledger v13.401 — External Audit Round 25

Date: 2026-09-12

Status labels: **[S]** source-established, **[D]** exact derived, **[N]** numerical, **[N-cert]** validated computational, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## Scope

This round covers the wave landing after commit `deb3731` (Round 24's retraction push): the post-retraction reinstatement (`v13.392_Source_Faithful_High_Complement_Reinstatement`), the eleven-entry six-direction/M3999 terminal-verifier chain (`v13.390`–`v13.400`, Suzuki thread), and three V4/divisor-contact entries (`v13.382`, `v13.385`, `v13.393`).

## 1. Post-retraction reinstatement is accurate

**[Audit→confirmed]** `v13.392_Source_Faithful_High_Complement_Reinstatement` correctly restates `v13.387`'s resolution and my Round-24 confirmation, and its own arithmetic checks out: independently recomputed the Schur-tail floor
\[
\delta_T=4.673332491014484-0.994^2/0.22=0.18225976374175623,
\]
matching to every digit shown.

## 2. Six-direction/M3999 terminal-verifier chain — arithmetic independently reproduced throughout

**[D/N, independently verified]** This is a long, carefully bookkept chain (`v13.390` through `v13.400`) building a proof *contract* for `ind_{≤0}(S_10)≤4`: replace the earlier uniform ten-column residual target by an anisotropic six-dimensional residual-Gram test on the six candidate-positive low-core directions, reduce the finite block from `M=16001` to the more tractable `M=3999`, precondition by a fixed coordinate transform to avoid poorly-scaled raw pivots near the `~4×10⁻⁸` fifth eigenvalue, and finally freeze the six-dimensional basis `Q` and preconditioner `L0` as exact dyadic (hex-literal) verifier input so no eigenvector enclosure is needed.

I independently recomputed essentially every chained numeric claim in this sequence from the stated formulas, not by re-running project code:

- `v13.391`: `β_arch(16003)=1.0191055832×10⁻⁴` and `α_16003=4.673332491014484` — recomputed via `mpmath` from the stated `C_r`, `s_2(N)` formulas; matched to 13+ significant figures.
- `v13.393`: `h_hybrid=0.17910434985544155` (sum check), the margin `δ_T-h_hybrid=0.003155413886314684`.
- `v13.394`/`v13.395`: normalized slack `1.73127289399189%`, `0.995·δ_T=0.18134846492304746`, remaining budget `2.2441×10⁻³`.
- `v13.396`: the perturbation-budget chain `‖ΔS_F‖<1.37×10⁻¹⁰`, `‖ΔS_solve‖<2.52×10⁻¹¹`, combined `<1.63×10⁻¹⁰`, `η_finite<0.0043`, `C_pre≥0.9957`/`0.9958` — recomputed the exact inverse-resolvent formula and matched every bound.
- `v13.397`: `H_max=δ_T·c_low>0.18149`, raw room `>2.39×10⁻³`, `‖Y₀‖<0.424`, the `8.5×10⁻⁴` and `2.24×10⁻⁴` sub-budgets, combined `<1.08×10⁻³`, and `0.18025<H_max`.

Every one of these matched independently to the precision shown. I have never before seen this project's numerical bookkeeping checked this densely in one round and had it come back clean at every step; it did.

**[D, independently verified via a from-scratch exact-rational computation]** The most checkable single claim in this batch is `v13.400`'s exact determinant of the frozen `6×6` dyadic minor of `Q`. I wrote my own Bareiss/Fraction-based Gaussian elimination, parsed the same hexadecimal binary64 literals from `research-notes/suzuki_M3999_frozen_dyadic_Q_L0.py` via `float.fromhex(...).as_integer_ratio()`, and computed the determinant independently. My result matched the ledger's reported numerator and denominator **digit-for-digit**:
\[
\det Q_{1:6,1:6}=\frac{1795308499156921328504675698957198911069798836146299290831861630469317641019312377789718059}{143343663499379469475676305956380433799785311823017570233599302461682679755530300504376159569382855409664},
\]
confirming `rank Q=6` exactly, as claimed.

**Verdict on this chain: sound so far, and honestly scoped.** Every checkpoint in the sequence explicitly labels itself as a "proof-design/certification budget" or "verifier contract" and repeatedly states the outward/interval replay has not yet been executed and the four small directions remain unresolved. That discipline held throughout — I did not find a single place where a midpoint number was quietly promoted to a certified one.

**[O, not independently reproduced]** The two headline *computed* quantities I could not reproduce myself without redoing the full `M=3999` (1990-mode) matrix assembly and solve: `λ₅(S_F)≈3.85764945×10⁻⁸` at `M=3999`, and the solve residual `‖R_F‖₂≈5.19×10⁻¹⁶`. Both are unsurprising in scale for a well-conditioned double-precision solve of this size — nothing about them looks implausible — but I flag them as trusted-not-verified rather than confirmed, consistent with how I've treated comparable full-scale runs in prior rounds.

## 3. V4 divisor-contact thread — all verified exactly by direct computation

**[D, independently verified]** `v13.382` (squarefree orbit classification), `v13.385` (general-exponent parity attenuation), and `v13.393`'s V4 companion entry (`Uniform_Contact_Measure_Odd_Residue_Generation`) form a clean progression: squarefree contact uniformity on the generated subgroup → general-exponent attenuation/annihilation formula → the exact iff-criterion `H_odd(n)=H(n)` for when the contact measure is uniform on its own support subgroup.

Tested all three computationally against brute-force divisor enumeration:
- Squarefree orbit classification (rank-0/1/2 cases): **3000/3000** random squarefree `n` (coprime to 6) matched the predicted `C_r(n)` exactly.
- General-exponent reconstruction formula (`P_r` from `ρ_χ` via `H₄`): **3000/3000** random `n` with mixed prime-power exponents matched to `10⁻⁹`.
- Worked examples in `v13.382`/`v13.385` §6 (`p≡5 (12)`, `n=p^{2m}` and `p^{2m+1}`): matched exactly for `p∈{5,17,29}`, `m=0..3`.
- `v13.393`'s central iff-criterion (`P` uniform on `H(n)` `⟺` `H_odd(n)=H(n)`): **5000/5000** random mixed-exponent `n`, zero mismatches.

All guardrails in these three entries correctly continue to disclaim any Casimir/mixed-cell connection for their `¼`s (consistent with the discipline established since Round 22/23).

## 4. Overall verdict

No errors found this round — a genuine contrast with Round 24. The project's response to the retraction was to reinstate the source-faithful chain accurately and then spend eleven careful entries building a well-scoped, explicitly-not-yet-executed verifier contract, rather than rushing to reclaim ground. The V4 thread continues to be clean, checkable, finite arithmetic with honest guardrails. I verified more individual numeric claims by hand this round than in any prior round and found the bookkeeping fully consistent throughout.

## 5. Scope note

Not independently reproduced: the actual `M=3999` finite Schur eigendecomposition and solve residual (`v13.396`, `v13.398`) — would require rebuilding the full 1990-mode source-faithful matrix and running the displacement-rank LDL myself; the `v13.392`/`v13.393` remote-residual-Gram accumulation tables through `n=2,000,000` (trusted from the formula structure and cross-checked totals, but the raw per-band numbers were not independently re-summed from source data); `v13.399`'s floating-point Gram-orthogonality diagnostic (not load-bearing for the proof, so not checked).

## 6. Guardrails

All guardrails from prior rounds remain in force. No new guardrail needed this round.

**External audit round 25: CLOSED. Post-retraction reinstatement confirmed accurate. Six-direction/M3999 terminal-verifier chain (`v13.390`–`v13.400`) independently verified at the arithmetic level throughout, including an exact-rational reproduction of the frozen dyadic determinant; correctly scoped as an unexecuted proof contract, not a completed certificate. V4 divisor-contact entries (`v13.382`, `v13.385`, `v13.393`) verified exactly by direct computation (11,000+ combined test cases, zero mismatches).**
