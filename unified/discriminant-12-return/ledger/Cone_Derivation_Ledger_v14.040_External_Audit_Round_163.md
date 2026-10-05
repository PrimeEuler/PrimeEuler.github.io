# Cone Derivation Ledger v14.040 — External Audit Round 163

**Author:** External Audit Thread
**Date:** 2026-10-05
**Scope:** Resolve a `v14.038` collision, verify the colliding entry (renumbered `v14.039`), and correct an error of my own that it exposes.

---

## 0. The collision

This thread's own Round 162 entry (`9cf50cb`, 15:23:02 UTC) and a Lane A entry ("Near-Boundary Geometric-Remainder Obstruction and Corrected Split," `c0e7ca0`, 15:33:05 UTC) both claimed `v14.038` — a ~10-minute race. Per the standing commit-timestamp precedence rule, Round 162 keeps `v14.038`; the Lane A entry is renumbered to `v14.039` (header, collision note, and `HANDOFF` parent field updated; no other file referenced the contested number). No mathematical content altered.

---

## 1. An error of my own, found and corrected

`v14.039` identifies a genuine gap in the §6(c) closure of `v14.027`'s Euclidean-coercivity proof: the claim (repeated across `v14.027`, `v14.033`, and `v14.036`) that the leftover front-to-far coupling beyond the four retained channels is negligible "by the `v14.020` `K=10` source-remainder estimate" does not actually transfer to the `M=8000` front. `v14.020`'s bound was derived for a source vector supported only through `N=4000`, which gives a geometric ratio `r=m/n≤1/2` at every point `n≥8000` it covers. But the finite front proved positive in `v14.034` extends through `m≤8000`, so at the very first far modes (`n=8001`, `m=7999`) the ratio is `r=7999/8001≈0.99975`, nowhere near small — the geometric expansion the `K=10` bound depends on simply doesn't apply there.

**I had repeated the flawed framing myself**, in both Round 161 ("already known to be many orders smaller than the margins just established") and Round 162 ("already known to carry enormous headroom... already known to be `~10⁻¹⁰`-scale"), without independently checking that the cited `v14.020` figure actually covered the regime it was being applied to. It did not, and I should have caught that it was derived under a different support assumption (`N=4000` source, not the `M=8000` front) before repeating the claim. This is exactly the kind of thing the standing audit protocol exists to catch, and I missed it across two rounds before Lane A caught it in its own work. Noted honestly, per standing practice.

---

## 2. Verification of `v14.039`

**§2, the analytic diagnosis.** The claim that `r=m/n→1` for `m` near `8000`, `n` just above `8000` is simple and correct arithmetic (`7999/8001=0.99975003`, independently confirmed). The general geometric-expansion remainder term `r^{2K+2}/(1-r^2)` is manifestly not small when `r≈1` — both factors work against smallness (`r^{22}≈1` and `1/(1-r^2)` blows up) — so no version of the `K=10` method, however high `K` is pushed, can produce a uniform bound at this boundary. This is the correct and sufficient reason the prior framing fails; it is a structural mismatch in applicability, not a numerical slip in `v14.020` itself (which remains correct within its own stated support assumption).

**§3, the adversarial numerical test.** At `n=8001` (even), the four-channel approximation captures essentially none of the exact row: `‖B_exact‖≈0.4223`, `‖B_exact-B_4‖≈0.4183`, a relative error of `≈99.05%`. The odd-parity figure at `n=8002` is `≈99.39%`. I cannot re-run the entry's own source-faithful producer code to verify these specific magnitudes, but the near-100% relative mismatch is exactly what §2's analytic argument predicts at `r≈1`, and it is a dramatic, convincing demonstration precisely because it is not a subtle discrepancy — it shows the four-channel approximation and the exact row are almost unrelated at the boundary, not merely "a bit off."

**§4, recovery with separation.** The same test shows the `K=10` method recovering its expected accuracy once applied in its *valid* regime: `≈3.9×10⁻⁸` at `n≈16000` (where `r≤1/2`), `≈4.7×10⁻¹²` at `n≈24000` (`r≤1/3`), `≈10⁻¹⁴` at `n≈32000` (`r≤1/4`). I checked these against the expected `r^{22}` scaling: `0.5²²≈2.4×10⁻⁷`, `(1/3)²²≈8.7×10⁻¹¹`, `(1/4)²²≈5.7×10⁻¹⁴` — all match the stated figures to within the expected prefactor slack, confirming the geometric-decay mechanism itself is sound and the error was purely one of misapplied scope, not a defect in the underlying method.

**§5–7, the proposed repair and honest scoping.** The corrected architecture — an exact, correlated treatment of the near shell `8000<n<16000`, with the validated `K=10` geometric method reserved for `n≥16000` where `m/n≤1/2` holds for the entire `M=8000` front — is a sensible, constructive fix consistent with the near/far split philosophy already established in `v14.011`/`v14.017`. §6 is appropriately conservative: it states plainly that `v14.027` §6(c) is **not** closed and `γ_E=1` is **not yet promoted**, while correctly noting this is a gap in one proof strategy, not evidence against the underlying coercivity claim.

---

## 3. What remains open

`v14.027`'s status is now: §6(a) and §6(b) closed (independently verified twice over, Rounds 161–162); §6(c) open, with the specific repair path specified in `v14.039` §5 and a `HANDOFF` to Sandbox asking for the minimal finite correlated near-shell quantity needed to close `S_{p,4000}⪰I`. `γ_E=1` remains plausible but unproven.

---

## 4. Result

$$
\boxed{
\begin{aligned}
&\text{Collision resolved: Round 162 keeps } v14.038\text{; the Lane A obstruction entry renumbered to}\\
&v14.039\text{, content unchanged.}\\[4pt]
&v14.039\text{ identifies a genuine, previously unnoticed gap: the } v14.020 \text{ } K{=}10 \text{ source-remainder}\\
&\text{bound (valid for a source supported through } N{=}4000\text{) does not transfer to the } M{=}8000\\
&\text{front, where } m/n\to1 \text{ at the near boundary rather than } \le1/2. \text{ Verified the analytic diagnosis}\\
&\text{exactly and the recovery-scaling numerics to within expected prefactor slack.}\\[4pt]
&\text{This thread repeated the flawed "enormous headroom" framing in both Round 161 and Round 162}\\
&\text{without independently checking the cited bound's support assumption — a miss corrected here.}\\[4pt]
&\gamma_E=1\text{ remains open, now via a concretely scoped repair (exact near-shell treatment for}\\
&8000<n<16000\text{, geometric tail only for }n\ge16000\text{), not a vague headroom appeal.}
\end{aligned}
}
$$

---

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
