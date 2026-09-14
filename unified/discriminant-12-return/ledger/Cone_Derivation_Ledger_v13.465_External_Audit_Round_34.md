# Cone Derivation Ledger v13.465 — External Audit Round 34

Date: 2026-09-14

Status labels: **[S]** source-established, **[D]** exact derived, **[N]** numerical, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## Scope

A large batch: `v13.454`–`v13.464` (eleven entries). Two threads: (1) the intrinsic/associated-graded refinement of the V4/S3/discriminant-12 algebra (`v13.454`, `v13.457`, `v13.458`, `v13.460`, `v13.462`), and (2) a new even-sector numerical thread investigating the structure of the six unresolved terminal directions left open by the `ind_{≤0}(A_{a=1})≤6` theorem (`v13.455`, `v13.456`, `v13.459`, `v13.461`, `v13.463`, `v13.464`). No version collisions this round.

## 1. Intrinsic discriminant-12 S3 quotient (`v13.454`) — verified exactly

**[D, independently verified]** Worked directly in `F3[ε]/(ε²)` (not the abstract argument): confirmed `(1-ε)³=1` exactly (char-3 Frobenius), that `1-ε` has order exactly 3, and — checking all three nonidentity elements of `P₃`, not just the generator — that `c(x)=x⁻¹` holds for every `x∈P₃` via direct computation. Combined with the already-verified prime-2 side (`M_ω³=I`, `Fr(ω)=ω²=ω⁻¹`, confirmed in earlier rounds), this confirms both local `S₃` constructions (`G₃=P₃⋊⟨c⟩`, `G₂=P₂⋊⟨Fr⟩`) exactly. The abstract-isomorphism argument (§8–10: both groups share the presentation `⟨r,s|r³=s²=1,srs=r⁻¹⟩`, forcing a unique generator-preserving isomorphism since both have order 6) is standard and correctly applied.

## 2. Terminal six-residue/ramification diagnostic (`v13.455`) — numerical diagnostic, re-executed and matched exactly

**[N, independently verified]** Correctly labeled as diagnostic throughout, with explicit "no exact kernel" guardrails. Ran `suzuki_terminal_six_residue_moment_diagnostic.py` directly: every printed value (the six unresolved-fraction tables, the four principal cosines `0.93574, 0.71268, 0.70240, 0.23512`, and the exceptional direction's coordinates) matched the entry's reported numbers exactly.

## 3. Even terminal prime-channel cancellation diagnostic (`v13.456`) — re-executed and matched exactly

**[N, independently verified]** Ran `suzuki_terminal_even_prime_channel_diagnostic.py`: the raw prime Rayleigh table for the exceptional direction (`q=2:+0.5834, q=3:-0.2956, q=4:-0.1151, q=5:-0.0167, q=7:≈0`) matched exactly. The entry's own honest correction of a natural but wrong hypothesis (the exceptional direction is *not* a pure q=3 mode, despite being n=3-localized) is well-supported by its own data and correctly flagged as provisional pending the nonlinear Schur test proposed in §7.

## 4. Associated-graded ramified towers (`v13.457`) — verified exactly

**[D, independently verified]** Checked the prime-2 uniformizer claims directly in `Z[i]⊂O_K`: `σ(1+i)=(-i)(1+i)` (direct expansion), `-i≡1 (mod 𝔓₂)` (since `-i-1=-(1+i)`), `h:=ζ₁₂⁻³=-i=1-π₂`, `h²=-1` with `v_{𝔓₂}(h²-1)=v_{𝔓₂}(-2)=2` (since `2=-iπ₂²`), and `h⁴=1` — confirming the claimed torsion-depth chain `1→2→∞` exactly. The prime-3 side (`v_π(μ^{3^r}-1)=1+2r`) was already independently confirmed by direct big-integer computation in Round 33.

## 5. Mod-4 square-zero extension and derivation recovery of V4 (`v13.458`) — verified exactly

**[D, independently verified]** This is the sharpest algebraic result in the batch. Worked in `Z[x]/(Φ₁₂(x))` with genuine integer coefficients (not pre-reduced) and computed `ν⁷-ν` and `ν¹¹-ν⁵` exactly: got `-2ν` and `-2ν⁵` respectively (matching `ν(ν⁶-1)=-2ν` and `ν⁵(ν⁶-1)=-2ν⁵` exactly, using the already-confirmed `ν⁶≡-1 (mod 4)`), then divided by 2 and reduced mod 2 to get `D₇(u)=u` and `D_{11,5}(u)=u⁵` exactly, matching the entry's boxed claims to the letter. This directly confirms the two-bit reconstruction `r↦(χ₋₃(r),χ₋₄(r))` recovering the full `V₄` label from the mod-2 quotient bit plus the first-order derivation bit.

## 6. Even terminal leave-one-channel Schur sensitivity (`v13.459`) — re-executed and matched exactly

**[N, independently verified]** Ran both `suzuki_even_terminal_leave_one_prime_schur_sensitivity.py` (across the full `M=399,799,1599,3999` ladder) and `suzuki_even_terminal_grouped_component_schur_sensitivity.py`: every printed number — the nonlinear Schur-response table for the exceptional direction, the whole-four-plane operator-norm hierarchy, and the four grouped-removal (cusp/arch/pole/all-prime) eigenvalue tuples — matched the entry's reported values exactly at every cutoff. This is a genuinely informative nonlinear (not additive) sensitivity experiment, correctly distinguishing itself from the naive raw-Rayleigh picture in `v13.456`.

## 7. Affine V4-S3 completion and canonical S4 action (`v13.460`) — verified exactly

**[D, independently verified]** Hand-verified all five generator permutations directly from `F4` arithmetic (`w²=w+1`): `T₁=(0 1)(w w²)`, `T_w=(0 w)(1 w²)`, `T_{w²}=(0 w²)(1 w)`, `A=(1 w w²)` (mult. by `w`, `0` fixed), `F=(w w²)` (squaring, `0,1` fixed) — every cycle structure matched the entry's boxed claims exactly. The resulting `V₄⋊S₃≅AGL₂(F₂)≅S₄` conclusion (order 24, faithful on 4 points, hence equal to the full symmetric group on those points) is then immediate and correct.

## 8. High-precision small-cutoff even spectrum (`v13.461`) — re-executed, headline numbers confirmed, one internal assertion bug found

**[N, independently verified, with a flagged discrepancy]** Ran `suzuki_even_small_cutoff_highprecision_spectrum.py` directly: the full `M=19..69` spectrum table matched the entry's reported values exactly, confirming the four tiny finite-cutoff eigenvalues are genuine (not binary64 cancellation artifacts). **However, the script's own final precision-doubling regression assertion (`abs(a-b) < 1e-45` comparing 80-digit vs 100-digit runs at M=39) fails when actually run** — I confirmed the true 80-vs-100-digit differences are `1.03×10⁻⁴⁴, 1.22×10⁻⁴⁵, 1.99×10⁻⁴⁶, 5.00×10⁻⁴⁵` for the four eigenvalues, three of which exceed the asserted `1e-45` threshold by factors of up to ~50×. This does not undermine the entry's substantive claim — the values agree to ~44 significant digits, vastly more than needed to distinguish them from binary64 noise, and match the entry's own reported 100-digit values exactly — but the script as committed does not pass its own asserted check; the threshold appears to have been picked without being tested against the actual achievable precision-doubling agreement.

## 9. Mod-4 twisted-lift obstruction (`v13.462`) — verified exactly

**[D, independently verified]** Reduced this entry's two central claims (`D₇(u) mod η=w`, `D_{11,5}(u) mod η=w²`) to facts already exactly confirmed: `D₇(u)=u` (§5 above) reduces mod `η` to `w` by the very definition `w:=u+η`; `D_{11,5}(u)=u⁵`, and `u⁵ mod η=w²` was independently confirmed by direct computation in Round 32 (`v13.444`'s audit). Since `w≠w²`, the obstruction argument (a genuine translation cocycle would need the same correction in both quotient cosets, but the two computed corrections differ) is a correct and honest negative result, consistent with the whole thread's careful guardrailing against overclaiming a canonical `U(12)↔T₂` identification.

## 10. High-precision even terminal four-plane cutoff stability (`v13.463`) — re-executed and matched exactly

**[N, independently verified]** Ran `suzuki_even_highprecision_eigenvector_evolution.py` directly: the low-core mass fractions, the successive-cutoff principal-cosine ladder (`0.9995946, 0.9999936, 0.99999958, 0.99999990`), the `M=69`-vs-frozen-`M=3999` comparison (`[1,1,1,0.99999884]`), the unit-residue principal cosines, and the exceptional direction's `n=3` amplitude (`≈0.943`) and overlap figures all matched the entry's reported values exactly.

## 11. High-precision tiny-spectrum cutoff-law crossover (`v13.464`) — headline data independently regenerated from scratch, not merely re-run

**[N, independently verified — and this required real work]** This entry's script (`suzuki_even_highprecision_tiny_spectrum_cutoff_law.py`) does **not** regenerate its own `M=79..119` eigenvalue data — it hardcodes a `DATA` dictionary of previously-computed numbers and only derives ratios/exponents from them, so simply running the script does not constitute independent verification of its headline numbers. I therefore independently regenerated all four eigenvalues at `M=79,89,99,109,119` myself, directly from `suzuki_even_small_cutoff_highprecision_spectrum.py`'s source-faithful matrix assembly. First attempt at 50 decimal digits gave a wrong `λ₁` at `M=79` (`2.72×10⁻²⁹` vs the hardcoded `8.08×10⁻³⁰` — a factor of ~3.4 off), which turned out to be *my* insufficient working precision, not an error in the entry: re-running at 65, 80, and 100 digits converges cleanly to `8.081065355×10⁻³⁰`, matching the hardcoded table. Re-ran all five cutoffs at 80 digits and matched every one of the twenty reported eigenvalues (`M∈{79,89,99,109,119}×λ₁..λ₄`) to 9+ significant figures. The entry's qualitative conclusion (rapid early collapse crossing over to a much slower late-cutoff regime, with no stable local power-law or exponential-law exponent) is therefore on solid empirical footing, though the underlying script should be fixed to regenerate its data rather than hardcode it, for future reproducibility.

## 12. Overall verdict

A large, mixed-character round. The algebraic thread (`v13.454`, `v13.457`, `v13.458`, `v13.460`, `v13.462`) is exact and every claim independently reconstructed from raw definitions — genuinely elegant work culminating in `v13.458`'s clean two-bit character reconstruction and `v13.462`'s honest identification of exactly where a naive translation identification breaks. The numerical thread (`v13.455`, `v13.456`, `v13.459`, `v13.461`, `v13.463`, `v13.464`) is uniformly well-guardrailed (explicit "no exact kernel," "no theorem strengthening," "no RH/GRH" language throughout) and every reported number reproduced by direct re-execution — with two process notes worth fixing rather than findings against the mathematics: `v13.461`'s regression assertion has a threshold that's simply too tight for the precision it's comparing, and `v13.464`'s script hardcodes rather than regenerates its input data (I did the actual independent regeneration myself, at real computational cost, and it holds up).

## 13. Scope note

Not independently reproduced beyond what's stated above: the M=3999/M=4000 frozen-basis infrastructure used as a comparison point throughout this batch was not rebuilt from scratch (it was independently verified in earlier rounds via `v13.404`'s original construction and the certificate chain culminating in `v13.451`–`v13.453`).

## Guardrails

All guardrails from prior rounds remain in force. New process notes (not mathematical findings): `v13.461`'s precision-doubling assertion threshold should be loosened to reflect the actual ~10⁻⁴⁴ achievable agreement; `v13.464`'s cutoff-law script should regenerate its `M=79..119` data from source rather than hardcoding it, since as committed it is not self-verifying.

**External audit round 34: CLOSED. `v13.454`–`v13.464` independently verified — the intrinsic V4/S3 algebra confirmed exact by from-scratch reconstruction, and every numerical diagnostic reproduced by direct re-execution, including a full from-scratch regeneration (not just a script re-run) of `v13.464`'s extended high-precision eigenvalue ladder through M=119. No theorem-level claim is strengthened or weakened this round — the full-parity bound remains `ind_{≤0}(A_{a=1})≤6` — but the six unresolved terminal directions now have a much sharper, honestly-hedged structural picture: three residue/V4-aligned directions plus one exceptional n=3-localized, q=2-vs-q=3/4 cancellation mode in the even sector, with the positive-plateau-vs-slow-decay question for the four tiny even eigenvalues explicitly left open.**
