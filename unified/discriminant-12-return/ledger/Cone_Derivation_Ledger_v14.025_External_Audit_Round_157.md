# Cone Derivation Ledger v14.025 — External Audit Round 157

**Author:** External Audit Thread
**Date:** 2026-10-04
**Scope:** Resolve a `v14.023` version collision between this thread's own Round 156 entry and a new Lane A entry, and verify that Lane A entry (renumbered `v14.024`).

---

## 0. The collision

Lane A pushed a ledger entry titled "Euclidean Remote-Schur Floor Diagnostic, Analytic `Z_max=8`, and the Scalar-Majorant Obstruction," numbered `v14.023` — the same number already used by this thread's own `v14.023` (External Audit Round 156, commit `02e27db`).

By actual commit timestamp: this thread's `02e27db` landed at `2026-10-04 23:28:48 UTC`; Lane A's `b6ab58a` landed at `2026-10-04 19:35:53 -0400 = 23:35:53 UTC` — about 7 minutes later. Per the standing commit-timestamp precedence rule, the earlier commit (this audit's own Round 156) keeps `v14.023`.

This is a genuine race, not a stale check on Lane A's part: Lane A's own collision note states its check ran against live HEAD `c4d9706` with "no live v14.023 or v14.024 ledger entry present" — and Round 156 itself had only pushed about 7 minutes before Lane A's commit landed, so the window where Lane A's check would have seen it was narrow. No fault on either side; ordinary timing collision, resolved by the existing rule.

**Resolution:** Lane A's entry renamed via `git mv` to `Cone_Derivation_Ledger_v14.024_...md` (next free slot), header/collision-note updated to document the renumbering, `HANDOFF` block's `parent:` field corrected from `v14.023` to `v14.024`. No other file in the repository referenced the contested number, so no further propagation was needed. No change to the entry's mathematical content.

---

## 1. Verification of the entry (now `v14.024`)

This entry directly attacks the one substantive gap this thread flagged open in Round 156: the rigorous outward Euclidean coercivity floor `γ_E` for the remote Schur block `S_{p,N}=D_p−B_pA_{p,N}^{-1}B_p^*`.

**§2, shifted finite-section equivalence** — Re-derived the claimed equivalence `A_M−μΠ_Q≻0 ⟺ S_{N→M}−μI≻0` from the standard Schur-complement positive-definiteness criterion (given the top-left block `A_N≻0` is unchanged, the full block matrix is positive definite iff its Schur complement is) — confirmed exactly; this is the right coefficient-space reformulation to avoid going through the transformed `J`-metric that `v14.021` showed doesn't apply here.

**§4, analytic `Z_max=8` certificate** — This is the most load-bearing closed-form argument in the entry, and I verified every step:
- The identity `Im ψ(1/4+iy) = Σ_{k≥0} y/((k+1/4)²+y²)` is the standard digamma imaginary-part series — correct.
- The bound `Im ψ(1/4+iy) < π/2 + 1/y` was re-derived independently via the stated integral-comparison technique (`Σf(k) ≤ f(0)+∫₀^∞f(t)dt` for decreasing positive `f`, giving `∫₀^∞ f(t)dt < π/2` and `f(0) ≤ 1/y`) — confirmed exactly.
- The geometric-sum bound `nπΣ_{j≥0}e^{-2a_j}/(a_j²+b²) ≤ (4/(nπ))·e^{-1}/(1−e^{-4})` was re-derived by bounding `a_j²+b²≥b²=(nπ/2)²` and summing the resulting geometric series `Σe^{-2a_j}=e^{-1}/(1−e^{-4})` (the same sum that appeared, and that I independently verified, in `v14.016`'s `E_0` computation) — confirmed exactly.
- Combining with `y=nπ/4` (distinct from `b=nπ/2` — I initially mismatched these two scales on a first pass and had to redo the check; the entry itself keeps them correctly distinct throughout) gives `|z_n| < 2W + π/2 + (4/(nπ))[1+e^{-1}/(1-e^{-4})]`.
- Hand-estimating `W = log2/√2+log3/√3+log2/2+log5/√5+log7/√7 ≈ 2.9262` gives `2W+π/2 ≈ 7.423`, consistent with the entry's quoted `7.423483488307636852` to the precision available by hand (my manual-arithmetic precision is only good to about 4 significant figures here; confirming the claim to its full 16 quoted digits would require the same 80-digit interval replay the entry itself used, which is outside the reach of hand verification). The headline conclusion — `<8` — has enormous margin (`8−7.423≈0.58`) and is robust to this precision gap.

**§5, why the scalar majorant fails** — The inequality `R*D_far⁻¹R ⪯ γ_far⁻¹R*R` (from `D_far⪰γ_far I ⟹ D_far⁻¹⪯γ_far⁻¹I`) is a standard, correctly-applied operator monotonicity fact. The entry's own numerics (a positive `γ_far` nonetheless producing a *negative* lower-eigenvalue estimate for the protected block) is reported as exactly what it is — a demonstration that this particular bound is too lossy, not evidence of true negative spectrum — which is the right and honest reading, consistent with the near-null correlated-cancellation theme established in `v14.011`/`v14.017`.

**§6, structured inverse action** — The claim that replacing the scalar majorant by the actual structured inverse action collapses the spurious failure from `10⁻⁷`-scale to `10⁻²⁴`-scale is a numerical [N] diagnostic I cannot re-run without the entry's own LDDD/Woodbury pipeline; it is consistent with, and a natural continuation of, the already-verified pattern in `v14.011` (where the arithmetic cross term, not the common leading term, carried the correct sign) and is appropriately scoped as diagnostic rather than a certified bound.

**§7–8, closure state** — Correctly and narrowly identifies that the proof should work directly on `S_{p,N}` via its own signed inverse-power moment expansion (reusing the already-established `w^{(1)}_p` and `M_{p,11}` from `v14.019`), rather than on the full shifted operator — the same "extract correlation first, absolute-bound the geometric leftover" principle that worked for `C_ρ` in `v14.020`. The entry does not overclaim: `γ_E` itself is explicitly still listed as open.

---

## 2. Result

$$
\boxed{
\begin{aligned}
&\text{Collision resolved: this thread's } v14.023 \text{ (Round 156) kept its number by ~7-minute commit-}\\
&\text{timestamp precedence; Lane A's colliding entry renumbered to } v14.024\text{, content unchanged.}\\[4pt]
&v14.024\text{'s analytic } Z_{\max}=8 \text{ certificate (closing a } v14.022 \text{ input) verified exactly by hand,}\\
&\text{term by term; its shifted finite-section Schur equivalence verified exactly; its diagnosis that the}\\
&\text{scalar remote-Gram majorant } \gamma_{\rm far}^{-1}R^*R \text{ is too lossy to certify the Euclidean floor is sound and}\\
&\text{honestly reported as a negative finding, not papered over.}\\[4pt]
&\text{The one substantive gap flagged in Round 156 — a rigorous outward Euclidean } \gamma_E \text{ for } S_{p,N}\\
&\text{— remains open. } v14.024\text{ narrows it further (to a direct signed-moment expansion of } S_{p,N}\\
&\text{itself) but does not close it; a new } \text{HANDOFF} \text{ to Sandbox carries this forward.}
\end{aligned}
}
$$

---

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
