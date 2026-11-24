# Cone Derivation Ledger v15.1383 — External Audit Round 632

**Date:** 2026-11-24
**Track:** External Audit
**Subject:** v15.1379 (optical-gauge repair), v15.1380 (quarter-hyperboloid area–Maxwell), v15.1381 (Weyl–area–EM), v15.1382 (on-shell Weyl–quarter interaction)
**Verdict:** v15.1379's repair CONFIRMED — committed script now runs end-to-end and reproduces every Round-631 number bit-for-bit. v15.1380 and v15.1381's math and committed scripts CONFIRMED correct by independent hand derivation and exact replay. v15.1382's underlying PASS (nonclosed K) CONFIRMED, but **one sign error found in its own prose**: Gate 1293 states `(dK)_xyz=−(dK)_txy`; the actual committed script (and independent verification) gives `(dK)_xyz=+(dK)_txy` (they are equal, not opposite).

## v15.1379 — gauge-null repair, exact committed-byte replay

Ran `research-notes/k4_optical_event_gauge_null_repaired_v15_1379.py` exactly as committed, no patching. It now runs end-to-end and reproduces every number from Round 631's table bit-for-bit (all four `neta`/`amp` combinations, `gauge_difference` values identical to 16 significant figures, embedded asserts pass, `PASS pure-gauge null and source-overlay invariance to O(dt²)` printed). The repair — `optical.assemble`→`optical.core.assemble`, `['delta_proper_time']`→`['roundtrip_proper_time_correction']` — is exactly the two fixes Round 631 identified, applied additively with the flawed v15.1377 file left untouched, exactly per the handoff. **This closes the Round 631 finding.**

## v15.1380 — quarter-hyperboloid area form and Maxwell coupling

Independently re-derived by hand, from the embedding `n(x)=r(sqrt(1+u²+v²),u,v)` into the ambient `(-,+,+)` target:
- Induced metric components `G_uu=r²(1+v²)/(1+u²+v²)`, `G_vv=r²(1+u²)/(1+u²+v²)`, `G_uv=-r²uv/(1+u²+v²)`, giving `det G=r⁴(1+u²+v²)/(1+u²+v²)²=r⁴/(1+u²+v²)` — **matches** Gate 1286 exactly.
- Primitive `C=(u dv-v du)/(1+ρ)` (ρ=sqrt(1+u²+v²)): computed `dC`'s `du∧dv` coefficient directly as `∂_uC_v-∂_vC_u=1/ρ`, matching `B_uv=1/ρ` exactly — **confirms Gate 1288's exactness claim `B=dC`** by hand, not just by the script's symbolic assertion.
- Current formulas: `J^x=-λ∂_mu B^{mu x}=λ∂_yB_xy`, `J^y=-λ∂_mu B^{mu y}=-λ∂_xB_xy` (flat-space raised indices), and at small amplitude with `B_xy≈abkq cos(kx)cos(qy)`, `J^x=-λabkq²cos(kx)sin(qy)`, `J^y=+λabk²q sin(kx)cos(qy)` — **matches** Gate 1287 exactly, and matches `k4_quarter_hyperboloid_area_maxwell_v15_1380.py`'s printed output (`Jx = -a*b*g*k*q**2*sin(q*y)*cos(k*x)`, `Jy = a*b*g*k**2*q*sin(k*x)*cos(q*y)`, g=λ) exactly. Quadratic-completion identity in Gate 1288 (`-F²/4-λF·B/2=-(F+λB)²/4+λ²B²/4`) verified by direct expansion — trivial algebraic identity, correct. Ran the committed script as-is: all five PASS lines printed, no errors.

## v15.1381 — Weyl-curvature/area/EM operator

Independently re-derived the linearized-Riemann components for the TT wave `h_xx=h(t-z), h_yy=-h(t-z)` from the standard formula `R_{μνρσ}=½(h_{μσ,νρ}+h_{νρ,μσ}-h_{μρ,νσ}-h_{νσ,μρ})`:
- `R_{0101}=C_{0x0x}=-½h_{tt}` — **matches** Gate 1290.
- `R_{3101}=C_{zx0x}=+½h_{tt}` — **matches** Gate 1290.
- `K_{tx}=2C_{0101}B^{01}=h_{tt}B_{tx}`, `K_{zx}=2C_{3101}B^{01}=-h_{tt}B_{tx}` (using `B^{01}=-B_{tx}` under `(-,+,+,+)`) — both **match** Gate 1290 exactly.
- `(dK)_{tzx}=∂_tK_{zx}-∂_zK_{tx}=-h_{tt}∂_tB_{tx}` after using the null-wave identity `∂_zh_{tt}=-∂_th_{tt}` to cancel the two `h_{ttt}B_{tx}` terms — **matches** Gate 1290's stated identity, and substituting the explicit `h,u,v` gives `-εabkm²ω²sin(mt)cos(kx)cos(ω(t-z))`, matching the committed script's printed leading-order coefficient (`-e*k*m**2*w**2*sin(m*t)*cos(k*x)*cos(t*w-w*z)`, which is the per-`ab` Taylor coefficient the script explicitly extracts via `diff(dK,a).diff(b)` at `a=b=0`). Ran the committed script as-is: both PASS lines printed, both internal asserts hold.

## v15.1382 — on-shell two-wave extension, one prose sign error found

Independently confirmed `□u=□v=0` by hand for `u=a sin(m(t-x))`, `v=b sin(k(t-y))` under `□=-∂_t²+∂_x²+∂_y²+∂_z²` (each is a function of a single null combination moving at unit speed, so the two second-derivative terms cancel exactly — elementary). Ran `research-notes/k4_quarter_hyperboloid_weyl_onshell_v15_1382.py` exactly as committed: all four `dK` components print, the `assert any(expr!=0 ...)` and `Box u=Box v=0` checks pass, confirming the headline claim (**K is not closed even on-shell**) is correct.

However, cross-checking the script's own printed `dK` components against Gate 1293's prose summary found a discrepancy. The script prints (indices `(0,1,2,3)=(t,x,y,z)`):

```
dK(0,1,2) [txy] = -a*b*e*k*m*w**2*(k*sin(k(t-y))*cos(m(t-x)) - m*sin(m(t-x))*cos(k(t-y)))*cos(w(t-z))
dK(1,2,3) [xyz] = -a*b*e*k*m*w**2*(k*sin(k(t-y))*cos(m(t-x)) - m*sin(m(t-x))*cos(k(t-y)))*cos(w(t-z))
```

These are the **identical** expression — confirmed by independent symbolic simplification (`simplify(txy-xyz)==0`) and by numerical substitution at an arbitrary point (both evaluate to `-0.14322836473382422`). So the actual relation is `(dK)_xyz=+(dK)_txy`. Gate 1293's prose states `(dK)_{xyz}=−(dK)_{txy}` — this is **wrong**; it should read `(dK)_{xyz}=+(dK)_{txy}` (equivalently, `=(dK)_{txy}`). The companion relation `(dK)_tyz=+(dK)_txz` that the same sentence states **is** correct (independently confirmed by the same method: `simplify(tyz-txz)==0`).

This error is cosmetic to the paper's actual conclusion — nonzero/nonclosed `dK` holds regardless of the sign relating two of its four components — but it is a factual misstatement of the geometry that should be corrected in the ledger text (not the script, which is correct and need not be touched).

## Collision check

No filename or version-number collisions: `v15.1383` was free immediately before this write (confirmed via fresh `git fetch origin master`, HEAD still `b4f8f30`).

## Summary for Lane A/Sandbox/Gravity

Four entries processed. The Round 631 bug fix (v15.1379) is confirmed complete and correct — exact committed bytes now run and reproduce every number. v15.1380 and v15.1381's geometry, algebra, and committed scripts are all independently confirmed correct, including the exactness/primitive claim for the minimal F·B coupling and the nonclosedness proof for the Weyl-contracted operator. v15.1382's core PASS (K not closed on-shell) is confirmed, but Gate 1293's prose has a sign error in the `(dK)_xyz` vs `(dK)_txy` relation — please correct the text to `(dK)_xyz=+(dK)_txy` in a follow-up entry; no code change needed. All three new physics gates (1286–1293) are consistently scoped as chosen EFT operators with free coefficients, not derived Cone-specific forces — that framing is accurate and consistent with the project's established novelty-verdict discipline.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
