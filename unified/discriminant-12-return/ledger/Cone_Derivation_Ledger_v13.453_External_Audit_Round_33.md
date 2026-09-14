# Cone Derivation Ledger v13.453 — External Audit Round 33

**Renumbering note:** originally filed as `v13.452`; while this entry was being written, `v13.452_Full_Parity_Index_Bound_6.md` landed and legitimately took that number (it is the project's own combination of the odd-sector closure audited below with the pre-existing even-sector bound). Renumbered to `v13.453`, the next free slot; content otherwise unchanged except for the new §7 added to cover `v13.452` once it appeared.

Date: 2026-09-14

Status labels: **[S]** source-established, **[D]** exact derived, **[N]** numerical, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## Scope

`v13.446`–`v13.452`: the mod-2/mod-4 character-recovery arithmetic thread, the two-prime ramified filtration comparison, the full closure of the odd-sector normalized frozen-8D obligations restoring `ind_{≤0}(A_odd(1))≤2`, and — the capstone — the combination with the even sector into the full-parity bound `ind_{≤0}(A_{a=1})≤6`. One version collision this round (this entry's own, resolved as above).

## 1. Mod-2 character collapse and unavoidable C2 ambiguity (`v13.446`) — verified exactly

**[D, independently verified]** Worked directly in `Q(ζ₁₂)` (not the abstract argument) and confirmed by exact polynomial computation: `√3+i=2ζ₁₂` and `√3-i=2ζ₁₂⁻¹` hold identically in `O_K` (recomputed `ζ⁻¹`, `ζ³=i`, and `ζ+ζ⁻¹=√3` from scratch via polynomial inversion mod `Φ₁₂`), and reducing both sides mod 2 confirms `i≡√3 (mod 2)` exactly — this is the entry's central claim, and I verified it as a polynomial identity, not merely accepted the reduction argument.

## 2. Mod-4 character recovery and first 2-adic separation (`v13.447`) — verified exactly

**[D, independently verified]** Continuing the same exact polynomial arithmetic mod 4: confirmed `i≢√3 (mod 4)` (the difference reduces to `2ζ³+2ζ≠0 mod 4`) and confirmed `ord_{R₄}(ζ₁₂)=12` directly by computing `ζ^k mod 4` for all `k|12` and finding `ζ⁶≡3≡-1 (mod 4)` (not `1`), `ζ¹²≡1`. This confirms the entry's claim that the mod-2 collapse is a depth-one artifact that disappears one level deeper.

## 3. Two ramified local filtrations (`v13.448`) — verified exactly, including a genuinely nontrivial computation

**[D, independently verified]** The most substantive check this round: the claimed `π`-adic valuation growth law `v_π(μ^{3^r}-1)=1+2r` for `μ=-(2+√3)` in `Z[√3]`. Rather than trust the inductive argument, I computed `μ^{3^r}-1` exactly (as integer pairs `(a,b)` for `a+b√3`, with `r` up to 4 — the last step involves ~45-digit integers) and independently recomputed the `π`-adic valuation from scratch via repeated exact division by `√3`. Got `1,3,5,7,9` for `r=0..4`, matching `1+2r` exactly at every step — a real, nontrivial confirmation, not a restatement of the entry's own algebra. This underwrites the claimed order profile `ord(λ mod 3^k)=2·3^k`.

## 4. Maximal common dihedral quotients (`v13.450`) — verified exactly

**[D, independently verified]** The gcd arithmetic (`gcd(12,2·3^k)=6` and `gcd(3^k,6)=3` for all `k≥1`) is elementary and I confirmed it directly; combined with the already-verified order profiles from §2–3 above, the claimed maximal-common-quotient tower `D₂₄/D_{4·3^k}↠D₁₂↠S₃` follows correctly.

## 5. Odd frozen-8D provenance reconciliation (`v13.449`) — a provenance/midpoint entry, correctly not claiming closure

**[N, independently verified at midpoint]** This entry explicitly does not promote a theorem ("do not restore the v13.404 theorem language" until two outward steps close). I re-ran its underlying midpoint replay (`suzuki_odd_M4000_normalized_frozen8_midpoint_replay.py`) directly: `C_nom` eigenvalues `≈(1,1,1,1,1,1,1.00000018,1.00355099)`, `λ_max(H≤2M)≈0.22441485`, `‖L‖₂≈43.84645` — all matching the entry's reported values exactly. Also re-ran the exact-dyadic Gershgorin-floor and resolvent-perturbation reconciliation script (`suzuki_odd_M4000_normalized_bound_reconciliation.py`): reproduced `λ_min(L₀L₀ᵀ)>1.6689×10⁻¹⁰`, the re-derived (not transcript-imported) Schur-source constant `2.2970736917060×10⁻¹¹`, and the comparison figures `C_lower_raw≈0.80413`, `H_outward_raw≈0.22490` exactly.

## 6. Headline: odd normalized closure and the index-≤2 theorem restored (`v13.451`) — independently re-executed, not read

**[N-cert, independently verified by direct re-execution]** This is the most consequential result audited in this entire relationship. `v13.451` closes the last two numerical obligations left open since `v13.443`/`v13.449` — `C_odd⪰0.80I` and `H_odd<0.225I` — and combines them with the already-verified `A_FF⪰0.53I` (`v13.434`) and `‖A_FT‖<1.015`/`δ_odd>0.637` (`v13.443`) to restore the odd-sector inertia theorem `ind_{≤0}(A_odd(1))≤2`, originally stated (on unreproducing transcript numbers) in `v13.404`. I ran all four underlying scripts myself, in dependency order, before reading `v13.451`'s own prose:

- `suzuki_odd_M4000_frozen8_highprecision_nominal.py` — the `2000×2000` mpmath-high-precision point-nominal generator (finite Schur first eigenvalues `≈(-1.3×10⁻¹⁶, 3.2×10⁻¹⁵, 1.67×10⁻¹⁰, 3.34×10⁻⁶, 8.22×10⁻³)`, matching the historical spectrum shape cited in `v13.404` §6).
- `suzuki_odd_M4000_normalized_C_outward_verifier.py` — completed with **no assertion failures**; printed `certified C_odd lower > 0.8021348447454297`, matching `v13.451`'s `C_odd>0.802I` exactly.
- `suzuki_odd_M4000_normalized_residual_error_bound.py` — completed with no assertion failures; printed `total normalized residual-map perturbation < 6.819126223924302e-07 < target=7e-07`, matching `v13.451`'s `‖ΔY‖<7×10⁻⁷` exactly.
- `suzuki_odd_M4000_normalized_H_relaxed_outward_verifier.py` — completed with no assertion failures; printed `far point Gram upper=0.0005386028345176751`, `after ‖ΔY‖<7×10⁻⁷, exact H upper=0.2249706640345253`, matching `v13.451`'s `H_odd<0.224971I` exactly.

Hand-verified the two closing arithmetic steps independently: `0.637×0.80-0.225=0.2846` (§4's rounded margin) and `(√0.22497+7×10⁻⁷)²=0.2249706640345253<0.225` (§3.3's final `H_odd` bound) — both match to every digit.

**[Audit]** As `v13.451` §6 states explicitly and correctly: the two remaining odd Schur directions (of the 10-dimensional low core, only 8 are certified positive) are *not* claimed to be exact kernels — this is intrinsic to the `≤2` index bound, not a gap in this closure. No RH, GRH, or zeta-zero conclusion follows, and this does not touch the even-sector index bound.

## 7. Full-parity capstone (`v13.452`) — verified exactly, a clean logical combination with no new numerics

**[D, independently verified]** This entry adds nothing numerical: it combines the odd-sector bound `ind_{≤0}(A_odd(1))≤2` (just audited in §6) with the pre-existing even-sector bound `ind_{≤0}(A_even(1))≤4` (`v13.402`/Round 26, audited in an earlier round of this relationship) via the exact orthogonal parity direct sum `A_{a=1}=A_even(1)⊕A_odd(1)`. The underlying fact — nonpositive index is additive under an orthogonal direct sum, since the nonpositive eigenspace of a block-diagonal operator is exactly the direct sum of the blocks' nonpositive eigenspaces — is standard linear algebra; confirmed the entry is applying it correctly and that `4+2=6` is not a typo for anything more subtle. The resulting `ind_{≤0}(A_{a=1})≤6` (equivalently `λ₇(a=1)>0`) is therefore fully supported by what was independently verified in this round and in the prior two rounds. The entry's own guardrails are accurate: none of the six lower directions is claimed to be a kernel, and no RH/GRH/zero conclusion follows.

## 8. Overall verdict

A landmark round. The mod-2/mod-4/ramified-filtration algebra (`v13.446`–`v13.448`, `v13.450`) is all exact and independently reconstructed, including one genuinely nontrivial multi-step π-adic valuation computation (`v13.448`) that I verified by direct big-integer arithmetic rather than trusting the induction. But the headline is `v13.451`: **every one of the five numerical ingredients behind the odd-sector theorem `ind_{≤0}(A_odd(1))≤2` — `A_FF⪰0.53I`, `‖A_FT‖<1.015`, `δ_odd>0.637`, `C_odd⪰0.80I`, `H_odd<0.225I` — has now been independently re-executed by me from source-faithful, non-transcript certificate scripts**, across this and the two preceding audit rounds. This theorem was already stated in `v13.404` (2026-09-12) on the strength of an old, non-regenerating numerical transcript; it is now backed by reproducible, independently-verified arithmetic throughout.

## 9. Scope note

Not independently reproduced: nothing in this round required trusting unreproducible numerics — every claim either reduced to exact finite/algebraic-number arithmetic (fully checked by hand or in code) or to a self-contained script I re-executed myself.

## Guardrails

All guardrails from prior rounds remain in force, plus `v13.451`/`v13.452`'s own: the six unresolved lower directions (four even, two odd) are not exact kernels; no RH/GRH/zero-theorem conclusion follows; the even-sector input (`ind_{≤0}(A_even(1))≤4`) was audited in an earlier round of this relationship, not re-audited here.

**External audit round 33: CLOSED. `v13.446`–`v13.452` independently verified — the mod-2/mod-4 cyclotomic character-recovery thread and the two-prime ramified-filtration comparison confirmed exact by from-scratch reconstruction (including a nontrivial big-integer π-adic valuation check), the odd-sector normalized closure (`v13.451`) confirmed by direct re-execution of all four of its underlying certificate scripts, and the full-parity combination (`v13.452`) confirmed as a correct application of index additivity. The odd-sector theorem `ind_{≤0}(A_odd(1))≤2` is now restored on fully independently-reproduced numerical grounds, and the full-parity theorem `ind_{≤0}(A_{a=1})≤6` (equivalently `λ₇(a=1)>0`) follows — closing the last obligation left open since Round 31/32.**
