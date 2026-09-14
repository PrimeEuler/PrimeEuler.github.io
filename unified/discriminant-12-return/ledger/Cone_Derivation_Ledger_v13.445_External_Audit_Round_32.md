# Cone Derivation Ledger v13.445 — External Audit Round 32

Date: 2026-09-14

Status labels: **[S]** source-established, **[D]** exact derived, **[N]** numerical, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## Scope

A large batch: `v13.436`–`v13.444` (nine entries — the V4/cyclotomic/Pell/F4 representation-theoretic thread) plus `v13.443`'s three companion Suzuki cross-block certificate scripts. No version collisions this round.

## 1. V4 Hadamard module intertwiner (`v13.436`) — verified exactly

**[D, independently verified]** Reconstructed the regular-representation matrices `L_s` for `s∈{1,5,7,11}` acting on `Q[U(12)]` from scratch and confirmed `H₄L_sH₄⁻¹=diag(1,χ₋₄(s),χ₋₃(s),χ₁₂(s))` exactly for all four `s` (standard finite Fourier duality, but checked, not assumed). Independently reordered the already-verified `v13.431` zeta-multiplication matrix into the `χ₋₃`-parity basis `(1,i√3∣i,√3)` and got the entry's boxed `2×2` block matrix `[[0,A],[B,0]]` exactly; recomputed `AB`, `BA`, and `Z³` in the parity basis and matched the entry's `Z²` and `Z³` (signed permutation) matrices exactly, plus `Z⁶=-I`, `Z¹²=I`.

## 2. Ramified F4 semilinear cyclotomic intertwiner (`v13.437`) — verified exactly

**[D, independently verified]** Confirmed `Φ₁₂(x)≡(x²+x+1)²(mod 2)` by direct polynomial arithmetic over `F2`. Built `M_ω` and `Fr` as explicit `2×2` matrices over `F2` from their defining action on the basis `(1,ω)` and got the entry's boxed matrices `[[0,1],[1,1]]` and `[[1,1],[0,1]]` exactly; confirmed `M_ω³=I`, `Fr²=I`, and the semilinear conjugation law `Fr·M_ω·Fr⁻¹=M_ω²` exactly by direct matrix computation over `GF(2)`.

## 3. Ramified order-6 lift and dihedral quotient tower (`v13.438`) — verified exactly

**[D, independently verified]** Worked directly in `R=F2[x]/(x⁴+x²+1)` (not trusting the entry's abstract argument) and confirmed every claimed identity by explicit polynomial arithmetic: `η=u²+u+1` satisfies `η²=0`; `ε=(u+1)η=u³+1` satisfies `ε²=0`; `u³=1+ε≠1` and `u⁶=1`, with `u^k≠1` for `k=1..5` confirmed directly — establishing `ord_R(u)=6` exactly, not just asymptotically plausible. Also confirmed `w:=u+η` satisfies `w²+w+1=0` (the embedded coefficient-field generator) and `u⁷=u`, `u¹¹=u⁵=u⁻¹` (the claimed Galois collapse `σ₁=σ₇`, `σ₅=σ₁₁`).

## 4. Pell–cyclotomic common C6/S3 quotients (`v13.439`) — verified exactly

**[D, independently verified]** Recomputed `g⁶ mod 12 = 7I`, `g³ mod 12 = [[5,3],[6,11]]` (reducing to `[[5,3],[0,5]] mod 6`), `ord₆(g)=6`, `g³ mod 3 = -I`, `ord₃(g)=6`, and the projective action of `[g]` and `[J_f] mod 3` on `P¹(F₃)`: `[g]:∞→0→1→∞` (fixing `2`), `[J_f]:0↔1` (fixing `∞` and `2`) — all matching the entry's boxed claims exactly. Hand-verified the three-point equivariant bijection `Θ(∞)=1,Θ(0)=ω,Θ(1)=ω²` against both `M_ω` and `Fr` action tables (already independently built in §2) and confirmed `Θ∘[g]=M_ω∘Θ` and `Θ∘[J_f]=Fr∘Θ` exactly.

## 5. Mod-3 radical line / AGL₁(F₃) phase (`v13.440`) — verified exactly

**[D, independently verified]** Confirmed by direct polynomial reduction that `q̄₁₂(m,n)=2(m+n)² (mod 3)` (rank-one degeneracy), and computed `q₁₂` at all four projective points mod 3, getting `∞,0,1↦2` and `2↦0` exactly as claimed (the radical line is the unique zero). Computed the exact characteristic polynomial of `ḡ mod 3`, confirming `(X+1)²`, and verified the claimed nilpotent `N=ḡ-2I` satisfies `N²=0` and kills exactly the radical eigenvector `(2,1)`. Confirmed the phase-coordinate table `j(∞)=0,j(0)=1,j(1)=2` from the given formula `j=n/(m+n)`.

## 6. Pell mod-3 ramified tangent phase and F4 unit intertwiner (`v13.441`) — verified exactly

**[D, independently verified]** This entry's central claims are algebraic identities I checked by hand rather than by code (all elementary field arithmetic in `F₃[ε]/(ε²)`): `N(α)=2q₁₂(m,n)` (direct norm expansion), the unit/nonunit criterion `ā nonunit ⟺ m+n≡0`, the intrinsic phase formula `j=2b/a`, and the two action laws `j↦j+1` (Pell return) and `j↦-j` (conjugation) derived directly from `(1+tε)(1+2ε)=1+(t+2)ε` and `ε↦-ε`. Independently re-derived (not merely re-read) the closing intertwiner `Ψ(a+bε)=ω^{2b/a}` by combining the verified phase-shift laws with the already-confirmed `M_ω`/`Fr` action — matches the entry's boxed `Ψ∘[g]=M_ω∘Ψ`, `Ψ∘[J_f]=Fr∘Ψ` exactly.

## 7. Prime-2 tangent V4 and S3 automorphism bridge (`v13.442`) — verified exactly, after catching my own verification bug

**[D, independently verified]** Built `R₂=F₄[η]/(η²)` explicitly in Python (F4 represented as pairs over `F2` with `w²=w+1`) and confirmed `w·h=u` (with `h=1+w²η`), `h²=1`, `u³=h` exactly. Verified `T₂={1,1+η,1+wη,1+w²η}` is closed and every nonidentity element has order 2. **First attempt to verify the automorphism formula `φ_{a,σ}(x+tη)=σ(x)+aσ(t)η` used a wrong candidate map** (scaling both the residue and tangent parts by `a`, rather than only the tangent part) and got a false multiplicativity failure — caught immediately by re-reading the entry's own formula, fixed, and re-verified: `φ_{w,1}`, `φ_{1,Fr}`, and `φ_{w²,Fr}` are all confirmed exactly multiplicative (hence ring automorphisms) by brute-force checking all `16×16` products in `R₂`. Confirmed the phase action `A:τ_j↦τ_{j+1}`, `F:τ_j↦τ_{-j}` exactly for all `j∈{0,1,2}`. Flagging this as my own error, not the project's.

## 8. Odd M4000 cross-block outward closure (`v13.443`) — the headline result, independently re-executed

**[N-cert, independently verified by direct re-execution]** This is the second of the two remaining odd-sector obligations named in `v13.434` (`‖A_FT‖<1.015`), now closed. Rather than reading the printed numbers, I ran all three companion scripts myself:

- `suzuki_odd_M4000_cross_midpoint_replay.py`: completed with no assertion failures; every printed value (`near top singular value≈0.9228113143831669`, `near rank-12 residual≈0.0023073371283394`, `combined near12+remote(8 levels)≈0.9772519307552501`, `far leading≈0.0351118...`, `far Frobenius remainder≈7.5977×10⁻⁵`) matches the ledger entry's reported values to every displayed digit.
- `suzuki_odd_M4000_cross_outward_verifier.py`: completed with no assertion failures; reproduced `explicit through 2e6 outward sum=0.979564000012<0.97957`, `far outward total=0.035187847723...<0.03519`, and the final `full cross outward sum=1.01476<1.015` exactly matching the entry's §9/§11.
- `suzuki_odd_M4000_cross_lowrank_factor_certificate.py`: completed with no assertion failures; reproduced the a-posteriori Cholesky-based low-rank cap certificate (`‖W‖₂<0.977255`, shifted-Gram factor floor `>5.977965×10⁻⁶ after allowances >5.967964×10⁻⁶`) matching the entry's §6 exactly.

Hand-verified the two closing arithmetic steps directly: `0.97957+0.03519=1.01476<1.015` (§11), and `δ_odd=α_{4002}-1.015²/0.53`, recomputing `α_{4002}=2.5810511596134207` and `δ_odd=0.6372304048964401>0.637` (§12) — both match the entry's boxed values to every digit.

**[Audit]** As the entry itself states, this closes only the cross norm; the normalized frozen-8D subspace bounds (`C_odd⪰0.80I`, `H_odd<0.225I`) remain the last odd-sector obligation before theorem promotion, and no RH/GRH-adjacent claim is made.

## 9. Canonical V4 self-duality, Hadamard kernel, and tangent-character bridge (`v13.444`) — verified exactly

**[D, independently verified]** Verified the canonical alternating pairing `B(x,y)=1⟺x≠0,y≠0,x≠y` reproduces the character assignment `5↔χ₋₄, 7↔χ₋₃, 11↔χ₁₂` by hand, computing all three character sign vectors directly from `B` on an explicit basis `(e₁,e₂)` for `U(12)≅V₄` — matches the entry's table exactly, confirming this is a genuine intrinsic (canonical) labeling rather than an assumed convention. For §7's tangent Galois involution, rebuilt `σ₅(u)=u⁵` in the explicit polynomial ring and confirmed `σ₅(η)=wη` (**catching my own error first**: I initially checked against the wrong target `σ₅(η)=w` rather than `σ₅(η)=wη`, got a false mismatch, then re-read the entry and confirmed it was my mistake) and the induced involution `t↦wt²` exactly for all four `t∈F₄`, including the unique nonzero fixed point `t=w²` giving `h=u³` — matches §8's identification exactly.

## 10. Overall verdict

An exceptionally strong and dense round: nine ledger entries, essentially all pure exact algebra (finite fields, Galois theory, group theory) plus one major numerical/certificate closure, and every checkable claim across all nine independently reconstructed from raw definitions — not merely re-derived from the entries' own stated logic, but rebuilt from scratch in code or by hand and cross-checked. Two of my own verification bugs were caught and corrected before being reported as findings (§7, §9) — both were errors in my own test harness, not in the project's mathematics. The headline is `v13.443`: together with the already-audited `v13.434`, the odd-sector high-complement Schur floor is now `δ_odd>0.637` with both major numerical obstacles (`A_FF⪰0.53I` and `‖A_FT‖<1.015`) closed by independently re-executed, source-faithful certificates — leaving only the normalized frozen-8D subspace bounds before the odd-sector theorem can be promoted.

## 11. Scope note

Not independently reproduced: nothing in this round required trusting unreproducible large-matrix numerics — every claim either reduced to exact finite algebra (fully checked) or to a self-contained script I re-executed myself (`v13.443`'s three scripts).

## Guardrails

All guardrails from prior rounds remain in force, plus the ones the entries themselves state explicitly and correctly: the `U(12)↔T₂` correspondence is canonical only up to the residual `C₂` ambiguity identified in `v13.444`; no ring/geometric identification is claimed between the prime-2 and prime-3 ramified carriers (`v13.441`'s guardrail); the odd-sector index theorem is **not yet promoted** — `C_odd⪰0.80I` and `H_odd<0.225I` remain open.

**External audit round 32: CLOSED. `v13.436`–`v13.444` independently verified — the entire V4/cyclotomic/Pell/F4 representation-theoretic thread confirmed exact by from-scratch reconstruction in code and by hand, and the odd `M=4000` cross-block closure (`v13.443`) confirmed by direct re-execution of all three of its certificate scripts. Combined with the previously-audited `v13.434`, the odd-sector Schur floor now stands at `δ_odd>0.637` with both numerical obstacles closed; only the normalized frozen-8D subspace bounds remain before theorem promotion.**
