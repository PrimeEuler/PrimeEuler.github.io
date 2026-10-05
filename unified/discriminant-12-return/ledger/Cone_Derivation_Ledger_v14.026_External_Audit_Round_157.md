# Cone Derivation Ledger v14.026 — External Audit Round 157

**Author:** External Audit Thread
**Date:** 2026-10-04 / 2026-10-05
**Scope:** Resolve a cascading pair of `v14.023`/`v14.024` version collisions, and verify the two Lane A entries involved plus one additional new entry.

---

## 0. The collisions

Two collisions landed in quick succession while this thread was mid-resolution:

**Collision 1 (`v14.023`).** This thread's own Round 156 entry (`02e27db`, 2026-10-04 23:28:48 UTC) and a Lane A entry ("Euclidean Remote-Schur Floor Diagnostic, Analytic `Z_max=8`, and the Scalar-Majorant Obstruction," `b6ab58a`, 23:35:53 UTC) both claimed `v14.023` — a genuine ~7-minute race, not a stale check on either side (Lane A's own collision note shows it checked live HEAD only a few minutes after Round 156 had pushed). By commit-timestamp precedence, Round 156 keeps `v14.023`; the Lane A entry was renumbered.

**Collision 2 (`v14.024`), discovered mid-resolution.** While this thread's renumbering commit (Lane A's entry → `v14.024`, plus this audit write-up → `v14.025`) was being prepared, a *second*, independent Lane A entry ("M8000 mu=1 Shifted-Front Far-Margin Diagnostic," `41778fb`, 2026-10-05 00:14:04 UTC) legitimately claimed `v14.024` on the shared remote — legitimately because, at the moment it committed, no `v14.024` file existed there yet; this thread's own renumbering commit had not yet been pushed (its first push attempt was rejected by git for being behind). This is not a case of commit-timestamp precedence overriding anything: `41778fb` simply landed in genuinely open space first. **Resolution:** the Lane A "Euclidean Schur Floor" entry is renumbered a second time, from `v14.024` to `v14.025`; this audit write-up shifts from `v14.025` to `v14.026`. The one internal cross-reference inside `41778fb`'s own text (which referred to the Euclidean Schur-floor entry as "v14.023," its very first number) was corrected to `v14.025`, along with that entry's `Parents:` field.

No other files in the repository referenced any of the contested numbers. No mathematical content was altered in either renumbering — only filenames, header metadata, collision notes, and the one cross-reference.

Final state: `v14.023` = Round 156 (unchanged); `v14.024` = "M8000 mu=1 Shifted-Front Far-Margin Diagnostic" (unchanged, only its internal cross-reference fixed); `v14.025` = "Euclidean Remote-Schur Floor Diagnostic..." (renumbered twice, content unchanged); `v14.026` = this entry.

---

## 1. Verification of `v14.025` (ex-`v14.023`/`v14.024`, "Euclidean Schur Floor Diagnostic")

Already verified in detail in the first draft of this audit round before the second collision was discovered; summary carried forward unchanged since no content changed:

- **§2's shifted finite-section Schur equivalence** (`A_M−μΠ_Q≻0 ⟺ S_{N→M}−μI≻0`) — confirmed exactly from the standard Schur-complement positive-definiteness criterion.
- **§4's analytic `Z_max=8` certificate** — every step re-derived by hand: the digamma imaginary-part series identity, the integral-comparison bound `Im ψ(1/4+iy)<π/2+1/y`, and the geometric-tail bound `nπΣe^{-2a_j}/(a_j²+b²)≤(4/(nπ))e^{-1}/(1−e^{-4})` (reusing the same `e^{-1}/(1−e^{-4})≈0.374742` sum independently verified in Round 155's check of `v14.016`'s `E_0`) — all confirmed exactly, correctly keeping the two distinct scales `y=nπ/4` and `b=nπ/2` apart. The numeric constant `2W+π/2≈7.423` was reproduced to the ~4-digit precision available by hand; the quoted 16-digit value needs the entry's own 80-digit interval replay to confirm fully, but the headline conclusion `<8` has nearly 0.6 of margin and is completely robust to that precision gap.
- **§5's diagnosis that the scalar majorant `γ_far⁻¹R*R` is too lossy** — the underlying operator-monotonicity inequality is correctly applied, and the entry's own numerics (a positive `γ_far` nonetheless yielding a *negative* lower-eigenvalue estimate) are reported honestly as a demonstration of bound looseness, not as evidence of true negative spectrum.
- **§6–8** are appropriately scoped [N]/[O] diagnostics and an honest, narrow closure state.

---

## 2. Verification of `v14.024` ("M8000 mu=1 Shifted-Front Far-Margin Diagnostic")

This entry picks up directly where `v14.025` left off, and reports genuinely encouraging progress on the one gap this thread has flagged open since Round 156.

**§2, two-stage Schur equivalence.** The claim that `S_{p,4000}≻I` follows from `F≻0` (the finite `M=8000`, `μ=1`-shifted front) together with positivity of the resulting far Schur block `D_2−I−B_{2,F}F⁻¹B_{2,F}^*` is an instance of the standard nested-Schur-complement/Haynsworth inertia-additivity fact: eliminating a leading block of a larger matrix in stages gives the same positivity verdict as eliminating it all at once, provided each stage's own leading block is already positive. The logical structure is sound; I did not re-derive the precise form of the induced coupling `B_{2,F}` from the original three-block matrix, which would require the full nested-elimination bookkeeping, but the overall equivalence claimed is a standard and correctly-applied fact.

**§4, rigorous raw far floor.** `D_{e,raw}⪰3.2867753186523356094 I` and `D_{o,raw}⪰3.2869152822833307687 I` on `n>4000` are cited from a separate "N4000 raw-tail certificate" artifact (commits `217e589`/`2ee4a10`) that this entry consumes rather than re-derives; I did not independently re-verify that certificate's own derivation in this round, but the values are consistent in order of magnitude with the rest of the batch's remote-floor estimates. The claim that a coercive lower bound on the full remote subspace `n>4000` restricts to the same lower bound on the smaller subspace `n>8000` is trivial (any bound `D⪰cI` restricts to `D|_V⪰cI` on any subspace `V`) — correct.

**§6, provisional margins.** I independently reproduced both subtractions exactly: even, `2.2867753186523356094 − 1.2428000003133971099 = 1.0439753183389384995`; odd, `2.2869152822833307687 − 1.1869700135759419654 = 1.0999452687073888033` — both match the entry's boxed results digit-for-digit.

This is a substantive, encouraging result: **margins greater than 1 in both parities** before the (already-shown-to-be-small, per `v14.020`) higher-order geometric remainder is even subtracted. The entry is careful not to overclaim — §6 and §9 both explicitly state these are midpoint/residual-certified margins, not yet promoted outward margins, and the `HANDOFF` to Sandbox asks precisely for that outward promotion plus the remaining geometric-remainder bookkeeping.

---

## 3. What remains open

The `γ_E` gap flagged in Round 156 is now **much narrower** but not yet closed:

1. Outward (not midpoint) certification of the finite `M=8000`, `μ=1` shifted-front positivity `F≻0`.
2. Outward interval bounds on the four-channel far Schur budget (`Δ^mid_{e,4}`, `Δ^mid_{o,4}`), replacing the current midpoint values.
3. Explicit incorporation of `v14.020`'s high-order geometric remainder into the same shifted-front geometry (flagged by `v14.024` itself as not yet done, though expected to be small given the `>1` margins).
4. If all three close, `γ=1` becomes a certified Euclidean floor for `v14.016`'s enclosure — the last of the three original finite-data inputs.

The `v14.024` entry's own §7 correctly anticipates that the geometric remainder is unlikely to threaten closure given the size of the margins, but states this is not yet proven in the shifted-front geometry specifically.

---

## 4. Result

$$
\boxed{
\begin{aligned}
&\text{Two cascading version collisions resolved by commit-timestamp/arrival precedence; final numbering:}\\
&v14.023=\text{Round 156}, \ v14.024=\text{shifted-front far-margin diagnostic}, \ v14.025=\text{Euclidean}\\
&\text{Schur-floor diagnostic (renumbered twice)}, \ v14.026=\text{this entry. No mathematical content altered.}\\[4pt]
&\text{Both Lane A entries independently verified: } v14.025\text{'s analytic } Z_{\max}=8\text{ certificate checks out}\\
&\text{exactly term-by-term; } v14.024\text{'s two provisional coercivity margins (} 1.044 \text{ even, } 1.100 \text{ odd)}\\
&\text{reproduce exactly from its own stated inputs.}\\[4pt]
&\text{The } \gamma_E\text{ gap flagged in Round 156 is substantially narrowed — order-one midpoint margins now}\\
&\text{exist in both parities — but remains open pending outward promotion of three finite, scoped items.}
\end{aligned}
}
$$

---

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
