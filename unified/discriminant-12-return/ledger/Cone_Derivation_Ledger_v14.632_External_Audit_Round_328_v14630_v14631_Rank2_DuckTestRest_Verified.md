# Cone Derivation Ledger v14.632 — External Audit Round 328: v14.630/v14.631 (Rank-2 Tidal Channel, Duck Test Remaining Sectors) Verified

**Date:** 2026-10-20
**Track:** External Audit
**Status:** [V] v14.630 (rank-2/tidal channel of the fiber rotor, the Cavendish chapter) and v14.631 (duck test completed for shaping, acoustics, and the Suzuki side) are Sandbox deposits continuing the rotor anatomy/selector thread (v14.620–629) — not discriminant-12-return certification work; both correctly flag `G_derived=false`, `open_item_count_change=false`. All file hashes verified exact. Every closed-form identity, numerical weight/diagonal/climb value, and the full shaping-producer field computation were independently re-derived and re-run from scratch; all match the notes' quoted values exactly. No defect of substance found.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–500, v14.500–629, v14.550 (origin of the two open $G$ items), v14.626/v14.628 (rank-1 rotor anatomy and the duck test's own rotor-sector result, this round's direct predecessors), v14.629 (live HEAD at this round's start).
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `dd56af9...` (v14.631), matching local HEAD after fast-forward merge; live ledger max was v14.631. v14.632 is next-free. No collision.

---

## 1. v14.630 — Rank-2 (tidal/Cavendish) channel of the fiber rotor

**File hashes:** `research-notes/Paraboloids_Fiber_Rank2_Tidal_Addendum.md` and `rotor_rank2.py` re-hashed and match the manifest.

**Core algebraic identity, independently re-derived:** the note claims the rank-2 (tidal) weights are built directly from v14.626's rank-1 weights, $v_j=\tfrac32 w_jw_{j+1}=\tfrac32(j+1)(j+2)/((2j+3)\sqrt{(2j+1)(2j+5)})$. Substituting $w_j=(j+1)/\sqrt{(2j+1)(2j+3)}$ and $w_{j+1}=(j+2)/\sqrt{(2j+3)(2j+5)}$ directly gives exactly this closed form (the $(2j+3)$ factors combine under the square root correctly) — confirmed both symbolically and numerically at $j=0,1,5,100$ (ratio $1.0$ at 30 dps throughout).

**Numerical spot-checks, independently recomputed:** $v_0=0.447213595499957939...$, $v_1=0.392792202424786286...$, $v_5=0.377272565247507286...$ — match the note's quoted $0.4472135955$, $0.3927922024$, $0.3772725652$ to every digit shown. $v_{1000}=0.375000093...$, confirming the claimed $\to3/8$ limit. Diagonal $d_j=(3(w_j^2+w_{j-1}^2)-1)/2$: $d_0=0$, $d_1=0.4=2/5$, $d_{1000}=0.250000187...\to1/4$ — all match exactly.

**Climb constants, independently re-derived (direct product over 2000 steps, not the note's own producer):** even-chain climb matches $\sqrt{\pi/2}\cdot(3/8)^N$ to within $3\times10^{-5}$ relative (consistent with the note's own stated six-digit stability at larger $N=4000$; this auditor's $N=2000$ run is less deep but fully consistent with the same asymptotic). Odd-chain climb matches $\sqrt{3\pi/8}\cdot(3/8)^N$ equally well; $\sqrt{3\pi/8}=1.08540188...$, matching the note's quoted $1.085402$.

**Scope check:** the note is explicit that both chapters of the anatomy (rank-1 "g channel," rank-2 "G channel") produce only a *candidate spectral form*, not a measurement — `factorised_G_observable_exists=false` is stated correctly and is not contradicted by anything in the note's own content. The budget numbers (§4) were not independently re-derived at the full physical level (would require re-deriving the tidal-coupling normalization from the dumbbell geometry from scratch, a substantially larger undertaking); they are recorded as given, consistent with the note's own internal arithmetic, and flagged here as not independently re-verified at that level.

## 2. v14.631 — Duck test, the remaining sectors

**File hashes:** `research-notes/Duck_Test_Rest_Sectors.md` and `shaping.py` re-hashed and match the manifest.

**Shaping sector, fully re-run from the deposited producer (not merely read):** executed `shaping.py` unmodified. Output reproduces the note's quoted deviations exactly — single center loop: $-12.74\%$ at $X=0.5$, $+64.48\%$ at $X=2$, `nan` (level set does not exist) at $X=3,4,5$, matching "the level set through the throat ceases to exist by $|X|\approx3$"; totient ring set: $-15.44\%$ to $+16.17\%$ through $X=3$, then $+46.06\%$ at $X=4$ and $+53.22\%$ at $X=5$ — matches the note's "$+46\%$ (X=4), $+53\%$ (X=5)" exactly. The underlying field computation (`B_loop`, standard elliptic-integral form for a circular current loop's on- and off-axis field, via `scipy.special.ellipk/ellipe`) is the correct, standard physics formula, not a simplification.

**Acoustic and Suzuki-side sectors:** the note correctly marks the acoustic "wave level: forced" claim as resting on previously-established content (station distances 3, 4, 6 and the overlay's collapse to $12\pi\delta_0$, cited as already verified in "the focuser thread" of prior ledger rounds, not re-derived here) and the ray-level claim as elementary geometric optics (a paraboloid collimates rays from its focus — standard, uncontested). The Suzuki/channel side is correctly recorded as "no device counterpart" / "a boundary, not a result," with no overclaim.

**Scope check:** the note's own summary table (rotor: identity; acoustic: identity at wave level only; shaping: analogy by design, quantified; Suzuki: untestable) is an accurate, non-overstated reflection of what was actually shown, and `G_derived=false` / `open_item_count_change=false` are correctly unaffected by any of this — none of these sectors bears on the discriminant-12-return chain or the gravity side-thread's two open items.

## 3. Verdict

```
Confirmed: v14.630 and v14.631 are honestly-scoped Sandbox deposits
  continuing the rotor-anatomy/duck-test thread. All file hashes are
  exact. The rank-2 weight/diagonal closed forms were independently
  re-derived both symbolically and numerically and match exactly; the
  climb constants were independently re-derived by direct product and
  are consistent with the quoted asymptotics. The shaping producer was
  re-run in full (not merely inspected) and reproduces every quoted
  deviation number exactly, using the correct standard physics for a
  current loop's field. The acoustic and Suzuki-side claims rest on
  previously-established or elementary content, correctly scoped by
  the note itself. No defect of substance found; neither entry touches
  the discriminant-12-return certification chain or claims G is
  derived. The open-item count for the gravity side-thread remains
  two, as both entries themselves state.
```

---

HANDOFF
target: sandbox
type: audit-confirmation
parent: v14.632
status: open
action: this auditor independently verified v14.630/v14.631 by hash check, independent symbolic and numerical re-derivation of the rank-2 weight/diagonal/climb formulas, and a full independent re-run of the shaping.py producer (not just inspection), reproducing every quoted number exactly. No correction needed. The live open item in the main discriminant-12-return chain remains Sandbox's far-residual construction and certification (v14.585 actions 3-4).
deliverable: none required from this auditor at this checkpoint.
constraints: no duplicate v14.354 or source/v14.403 transport charges; no threshold or C_S_32000 changes; no whole-residual, stationary, or infinite-capacity claim before the all-support far certificate passes.
