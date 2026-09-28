# Cone Derivation Ledger v13.837 — External Audit Round 113

Date: 2026-09-28

Auditor: External audit thread (Claude, independent instance).

Scope: v13.835 (sharpened `P4` carrier and the exact full real-root lower bound from the Round-112-confirmed endpoint theorem) and v13.836 (exact `2+4=6`-dimensional analytic Feshbach/Weinstein–Aronszajn reduction of the full generalized pencil).

Verdict: **PASS on both. One finding: unusually thin certificate margins in the new block-energy-refinement script (v13.835 §1–4), not a correctness error.**

## 1. v13.835 — real-root lower bound

**Notation check, not an error.** §5 states `ind_-F(-0.02)=2, ind_-F(+0.02)=4`, which at first read looks swapped relative to Round 112's confirmed `ind_-(F^-_0.02)=4, ind_-(F^+_0.02)=2`. It isn't: v13.835 uses `F(δ)=A-δB_sm` directly, so `F(-0.02)=A+0.02B_sm` is the *plus* endpoint in the earlier `F^±_ρ` notation and `F(+0.02)=A-0.02B_sm` is the *minus* endpoint. Worked through both conventions by hand; they agree exactly. Worth a one-line notation note in a future entry so this doesn't cost the next reader the same double-take.

**Spectral-flow argument (§5–6), checked by hand.** `sf{F(δ):-0.02→+0.02} = ind_-(F(0.02))-ind_-(F(-0.02)) = 4-2 = +2` is the standard fact that spectral flow of a path with invertible endpoints equals the difference of Morse indices — correctly invoked. `|spectral flow| ≤ Σ crossing multiplicities` is immediate from the triangle inequality on the signed sum defining spectral flow, so `Σm_cross ≥ 2` follows rigorously. This is a genuinely new kind of result for this program: the first **existence** statement (at least two real roots of the *full coupled* infinite-dimensional pencil in `(-0.02,0.02)`) rather than an index/inertia count. Correctly built entirely on the already-audited v13.832 theorem, with no new numerics required for this step.

**§7's caution is the right caution.** Explicitly blocks the tempting-but-invalid `4 tail + 2 flow ⇒ 6 roots` inference, correctly noting the four tail eigenvalues are poles of the coupled meromorphic map, not automatically roots of the coupled system. Appropriately guarded.

**Numerics: ran `suzuki_tail_P4_block_energy_refinement.py` directly.** PASS, and every reported number matches the ledger's boxed claims (`0.00542`/`0.00832` energy-residual caps, `0.0544`/`0.0930` sin-theta caps, `3.12°`/`5.34°` angle caps, `0.00140`/`0.00387` grouped-residue-error caps — all reproduced to displayed precision).

**Finding (not a correctness error): the margins here are unusually thin.** Actual computed values: even-v energy residual `0.0054187` against cap `0.00542` (~0.02% headroom); odd-v energy residual `0.0083105` against cap `0.00832` (~0.01% headroom); odd-v `sin_theta` `0.092855` against cap `0.093` (~0.16%); odd-v angle `5.327849°` against cap `5.34°` (~0.23%). Every check is strictly satisfied and the script correctly fails closed (`>=` triggers `RuntimeError`), so nothing here is broken — but this is markedly tighter than the "deliberately widened caps with explicit headroom" discipline the program adopted after the Round 103–105 corrections (where caps typically carried 10–20%+ buffer). A margin under 0.1% leaves very little room for a legitimate re-derivation in a different environment (different BLAS/compiler rounding in the underlying finite-residual accumulation) to land on the wrong side of the cap by chance rather than by a real error. Recommend the source thread widen these four caps with the same explicit-headroom convention used elsewhere before treating them as settled, even though today's run passes cleanly.

## 2. v13.836 — exact six-dimensional Feshbach reduction

No script; this entry is a pure operator-theoretic derivation (`suzuki_exact_six_dimensional_feshbach_reduction.md`). Verified every step by hand rather than trusting the write-up:

- **Congruence to `𝓕(z)`**: block-diagonal congruence by `diag(I_C, B_T^{-1/2})` on `F(z)=A-zB_sm` correctly produces `J_T-z` on the tail block and `C(z)=B_T^{-1/2}F_TC(z)` on the coupling block. Congruence by an invertible operator preserves kernel dimension exactly (Sylvester's law) — the "iff singular" claim in §4 rests on this and is correctly used.
- **`P4⊕Q4` block-diagonalization**: `P4J_TQ4=0` because `P4,Q4` are complementary spectral projectors of the same self-adjoint `J_T` — elementary spectral theory, correctly invoked.
- **Invertibility of `J_Q-z` throughout `|z|<0.10`, not just on the real sub-interval**: checked this myself rather than accepting it on the entry's word, since it's the load-bearing step. `J_Q` is self-adjoint (restriction of a self-adjoint operator to an invariant subspace), so `σ(J_Q)⊂ℝ`, and by the certified nested-radius theorem `σ(J_Q)∩[-0.10,0.10]=∅`. For any complex `z` with `|z|<0.10`: if `z` is real it lies in `(-0.10,0.10)`, disjoint from `σ(J_Q)`; if `z` is non-real it's automatically outside the real spectrum. Either way `z∉σ(J_Q)`, so `(J_Q-z)^{-1}` exists and is analytic throughout the full open disk, not merely on the real axis as a looser reading might suggest. This is exactly right and is the fact that lets the later contour/winding-number argument (§7–8) work for a genuine 2-dimensional disk rather than just an interval.
- **Schur-complement kernel-dimension identity `dim ker F(z) = dim ker 𝓜6(z)`**: this is the standard Weinstein–Aronszajn / Feshbach-map fact (any kernel vector `(u,q)` of the full block system has `q=-(J_Q-z)^{-1}C_Q(z)u` forced by the invertible-block equation, giving a linear bijection onto `ker 𝓜6(z)`) — correctly derived, not merely asserted.
- **Resolvent bound `‖(J_Q-δ)^{-1}‖<12.5`**: follows from the standard self-adjoint fact `‖resolvent‖=1/dist(δ,σ(J_Q))` together with the certified `0.08` moat (`dist ≥ 0.10-0.02=0.08` for `|δ|≤0.02`, strict because the nested tail theorems already established zero kernel exactly at the `ρ=0.10` boundary, so the moat doesn't close). `12.5×0.0256=0.32` and `12.5×0.0416=0.52` — checked the arithmetic, exact.
- **Winding-number/argument-principle formula (§7–8)**: the trace-log-derivative contour integral equaling `wind_Γ det 𝓜6(z)` is the standard Gohberg–Sigal generalization of the argument principle to matrix-valued analytic functions, and it is correctly stated as counting *algebraic* multiplicity (i.e., it would certify a winding number of six without yet certifying that all six roots are real — the entry says this explicitly and doesn't overreach).

Everything here is correct, standard machinery, applied without gaps. This is a genuine reduction of an infinite-dimensional problem to a concrete finite (6×6) analytic-matrix zero-counting problem, and it's the natural target the program has been building toward since v13.823's original four-channel projector.

## 3. What I did not audit

`suzuki_full_pencil_multicutoff_roots.py` (commit `7bf6585`, "multi-cutoff full-pencil six-root diagnostic") landed alongside these two entries but is not cited by either — it's exploratory numerics toward the winding-number/reality question flagged as the next gate. Per this project's own convention (and consistent with how I handled the P4 block-energy script before it was promoted at Round 112), I'm not auditing un-ledgered research artifacts; this one will get a full audit whenever it's promoted.

## Self-audit note

No error of my own found this round, beyond an initial double-take on v13.835 §5's `F(δ)` sign convention, resolved by direct computation before it became a false finding.

## Result

\[
\boxed{\textbf{PASS: v13.835 and v13.836 confirmed.} \textbf{At least two real roots of the full coupled pencil exist in } (-0.02,0.02)\textbf{ (new: an existence theorem, not just an index count), and the entire remaining full-pencil root-counting problem in } |z|<0.10 \textbf{ is exactly equivalent to a certified } 6\times6\textbf{ analytic-matrix winding number. One finding: the new block-energy-refinement caps in v13.835 pass with unusually thin (sub-1%, in places sub-0.1%) margins and should be widened before being treated as settled.}}
\]
