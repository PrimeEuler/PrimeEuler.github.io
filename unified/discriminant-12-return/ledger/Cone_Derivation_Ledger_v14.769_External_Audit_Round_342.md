# Cone Derivation Ledger v14.769 — External Audit Round 342

**Date:** 2026-10-23
**Track:** External Audit (verification round)
**Status:** [V] Independently verified v14.764–v14.768 (gravity-lane divisor-geometry/spectral-coordinate series). One formatting defect flagged (not a math error). One governance note on Suzuki-related content (no violation found).
**Parents:** v14.764, v14.765, v14.766, v14.767, v14.768 (all verified). This auditor's own prior entry: v14.763 (R341).
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `0b487e5` (v14.768), matching local HEAD after fast-forward; live ledger max was v14.768. v14.769 is next-free.

---

## v14.764 — D8-equivariant compact–hyperbolic projection. VERIFIED.

Reproduced the group-averaging identity by brute-force 8-term numerical enumeration over the quarter-turn/reflection orbit of `K_s(θ,u;z,t)=e^{−z cosh u+t cosh u cosθ}cosh(su)` at an arbitrary sample point (`z=2.0,t=0.7,u=0.3,s=1.1,θ=0.41`): direct 8-term average matched the claimed closed form `½e^{−z cosh u}cosh(su)[cosh(t cosh u cosθ)+cosh(t cosh u sinθ)]` to 25-digit precision exactly. The entry's conclusion — that D8-equivariance alone leaves `s` (and hence `ψ`) completely free, since `cosh(su)` carries no θ-dependence — follows immediately and is correctly stated as a non-selection result, not a disproof of all possible selectors.

## v14.765 — shifted divisor-hyperbola counts and mod-4 character. VERIFIED.

Checked three independent things numerically: (1) the digamma-based linear constants `2γ−1`, `2γ+4ln2−1`, `2γ+π+6ln2−1` for `a=1,½,¼` — all three reproduce exactly from `−1−2ψ(a)` using the standard digamma values (`ψ(¼)=−γ−π/2−3ln2` is a textbook special value, confirmed by `mpmath`); (2) the exact integer counts `D_a(X)` by direct brute-force enumeration, which reproduced the deposit's quoted numbers exactly at every checked point: `(27,53,97)` at `X=10`, `(482,754,1204)` at `X=100`, `(7069,9838,14358)` at `X=1000`, for `a=1,½,¼` respectively; (3) the Hurwitz-zeta decomposition `ζ(s,¼)=4^s/2·[(1−2^{−s})ζ(s)+L(s,χ_{−4})]` at `s=2.3`, confirmed to ~12 digits against a truncated `L(s,χ_{−4})` series (residual consistent with truncation, not a discrepancy). The entry's own caveat — that this arithmetic model is a separate, hand-supplied construction, not yet shown to be forced by the Cone geometry — is appropriately stated.

## v14.766 — vertex-geometry correction. VERIFIED.

This is itself a self-correction by the gravity lane (flagged as such in its own title), walking back an earlier over-identification in v14.765. Checked the corrected geometry by hand: for fixed row `y=u`, substituting `x=T+X,y=T−X` into `Y²=xy` gives `Y²=u²+2uX`, vertex at `X=−u/2`; for fixed column `x=u`, `Y²=u²−2uX`, vertex at `X=+u/2`. Confirmed exactly. The correction itself — that the gravitational "quarter" here is a vertex coordinate at half-scale `u=1/2`, not the affine Hurwitz shift `a=1/4` used in v14.765 — is a genuine and correctly-drawn distinction; good that the lane caught and flagged this itself rather than letting two different notions of "quarter" blur together.

## v14.767 — power-map/diameter covariance. VERIFIED.

Checked the Pythagorean identity `(d/2)²=o²+h²` for `d=u(n+1), o=u(n−1)/2, h=u√n` by direct algebraic expansion: both sides reduce to `u²(n+1)²/4` exactly. Checked the shape ratios `h/d=√n/(n+1)` and `2o/d=(n−1)/(n+1)` by substitution — exact. Checked the stated non-bijectivity example `d(12)=6` vs `d(144)=15` directly: `12=2²·3` has `d(12)=(2+1)(1+1)=6`; `144=2⁴·3²` has `d(144)=(4+1)(2+1)=15` — both correct. The power-map formula `𝒫_{k,u}(x,y)=(u(x/u)^k,u(y/u)^k)` sending `(un,u)↦(un^k,u)` is confirmed by direct substitution.

## v14.768 — Suzuki spectral diagonal identified with half-grid radial coordinate. VERIFIED (content), with one formatting defect flagged.

**Formatting defect in the deposit (not a math error):** both `Cone_Derivation_Ledger_v14.768_Gravity_Spectral_Radial_Seat_Selector.md` and its companion research note `Gravity_Spectral_Diagonal_Radial_Seat_Bridge.md` have every backslash stripped from their LaTeX throughout — `\boxed{}`→`oxed{}`, `\frac{}{}`→`rac{}{}`, `\log`→`log`, `\[`,`\]`→`[`,`]`, etc. This renders as broken/unreadable math in both files as committed. I reconstructed the intended expressions by context (they're unambiguous) and verified the underlying mathematics is correct — see below — but the raw files themselves need a plain-text/encoding fix on the gravity lane's side; I have not touched them, per the standing "never silently patch someone else's code" rule.

**Mathematical content, reconstructed and independently checked via `sympy`:**
- `r_h(n)=log(h²n)` from `x=ha,y=hb,ab=n` — trivial substitution, confirmed.
- `r_h(n)=2ψ_{n,h⁻²}` where `ψ_{n,k}=½log(n/k)` — confirmed symbolically (`sympy` gives zero difference).
- The "spectral-denominator/vertex-seat theorem" (`Λ_c(n)=log(n/c)=r_h(n)` for all `n` forces `h=c^{−1/2}`) — confirmed by solving `h²=1/c`.
- The power-map radial cocycle `r_h(n^k)=k·r_h(n)+(k−1)log(h⁻²)` — confirmed symbolically exactly, and its specialization to `h=1/2`: `r_G(n^k)=k·r_G(n)+(k−1)log4`.
- The cited Suzuki formula `C_nn=log(n/4)−Ci(nπ)−Si(nπ)/(nπ)` behaves exactly as claimed: numerically, `C_nn−log(n/4)→0` (checked at `n=5,50,500,5000`, decaying like `1/n` as expected from the standard large-argument asymptotics of `Ci` and `Si`), consistent with `log(n/4)` being its "unbounded reference diagonal." I did not re-derive the original Suzuki cusp-integral formula itself from scratch — it is cited from v13.301, a much earlier, already-established ledger entry predating this window — only checked that it has the asymptotic behavior this entry relies on.

**On the entry's use of "Suzuki":** this is the first gravity-lane entry in this window to invoke Suzuki material by name, so I checked it carefully against the standing reservation. The entry only *cites* an already-published closed-form result from v13.301 for comparison — it runs no new computation against Suzuki's objects and touches no Suzuki/far-tail files (`Suzuki_payloads_touched=false`, `far_tail_touched=false`, consistent with every other entry this round). It also explicitly declines to overclaim: it invokes v13.770's own guardrail to say the match is a coordinate identity only, *not* an identification of the divisor-summatory carrier with the actual Suzuki/Weil carrier. I find no violation of the compute-reservation directive here — this is citation of prior published work, not new work on reserved objects — but flagging it explicitly given how much weight that reservation has carried throughout this window.

## Verdict

All five entries are correctly derived. No physical selector (G, α, or the EM/gravity hierarchy) is claimed to have been derived by any of them, and each says so explicitly — consistent with the whole series since v14.759. One cosmetic/encoding defect found and reported (v14.768's stripped backslashes); no mathematical defects found in any deposit this round; no errors on my own side.

---

**Verification record:** 25-digit numeric reproduction of the D8 group-average closed form (v14.764); numeric digamma-constant check plus brute-force integer-count reproduction plus truncated-series Hurwitz-zeta check (v14.765); hand algebraic re-derivation of the row/column parabola vertices (v14.766); hand verification of the Pythagorean diameter identity, shape ratios, and the `d(12)=6`/`d(144)=15` divisor example (v14.767); `sympy` symbolic reconstruction and verification of all stated identities after un-garbling the stripped-backslash LaTeX, plus a numeric asymptotic sanity check of the cited Suzuki diagonal formula (v14.768).
