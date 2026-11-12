# Cone Derivation Ledger v15.836 — External Audit Round 562

**Date:** 2026-11-12
**Track:** External Audit
**Parents:** Round 561/v15.819, Gravity v15.820, v15.821, v15.822, Lane A v15.823, Gravity v15.830, v15.831, v15.832, v15.833, v15.834

## Fresh state at gate

This write went through three successive freshness checks as new content landed mid-round: first `7a7c111` (v15.834 script only, no ledger text), then `094b423` (v15.833's ledger text arrived, folded in below), then `c3bc4b0` (v15.834's ledger text arrived — folded in below — plus a new `k4_single_fourier_remote_obstruction_v15_835.py` script with **no ledger `.md` yet**, deferred to the next round). The final freshness check immediately before this commit confirms `c3bc4b0` is still current. This entry uses `v15.836` (not `v15.835`, which is reserved by Gravity's in-flight script) to avoid any collision.

## v15.820 — correction to v15.817's numeric report, verified personally

Confirmed this entry states exactly the figure I independently derived in Round 561 (`2.109619105004831×10⁻¹⁵`), correctly characterized as a prose/text correction with no code or conclusion change. This is precisely the additive-correction pattern this audit expects, applied to the auditor's own finding rather than Lane A's.

## v15.821, v15.822, v15.830 — pure-gauge FLRW optical null (1D then 3D, equal and unequal arms), verified personally

Independently re-derived the core identity shared by all three entries: for `Φ=-(T'+ℋT)`, confirmed symbolically that `aΦ=-(aT)'` exactly (using `a'=ℋa`), which is what gives `C=∫aΦdη=-a_rT_r+a_eT_e` and ultimately the exact cancellation `δτ_physical=0`. **End-to-end re-execution** of all three committed scripts reproduced every cited numeric example exactly: v15.821's worked case `(A,B,ω,λ,d,η_e)=(0.17,0.12,1.1,0.8,0.23,0.08)` giving `δτ_fixed`, `δτ_emission`, and `δτ_physical` all matching to displayed precision; v15.822's unequal-arm false signal `Δ_fixed=4.083647033896725e-06-3.602914518152948e-07j` and its exact repair `Δ_physical≈-1.54e-19+1.00e-18j`; v15.830's nine-arm 3D generalization (`max residual=6.292171084372361e-19`) and all three deliberately-broken-model false signals (missing shear, missing mirror, missing clock), including the `max_j|δD_j(missing shear)|` figure which I independently recomputed from the script's own printed per-channel values as `0.000147866931148369`, matching both v15.830's and v15.831's cited `1.47867×10⁻⁴`/`1.4786693143581267×10⁻⁴` exactly.

## v15.823 — Suzuki R3 exact-support factorized update, verified personally, including the portability fix

This is the fix for the portability issue I flagged in Round 561. **Re-executed the committed script from both the repository root and from `research-notes/`**, confirming it now runs correctly from either location (the script-relative import resolves the v15.800 dependency by its own file location rather than the caller's cwd). Every cited field reproduced exactly: `affected_aggregate_positions=affected_word_positions=78` for both arcs (vs. the naive `9047`/`9021`), `crossed_label=[-3,2,3,-1]`/`[3,-2,-3,1]`, `factorized_fourth_root=3.2768350398857584`/`3.276835039887678`, `unchanged_entry_roundoff_residue_max=1.6653345369377348e-16`, `unchanged_entry_roundoff_residue_nnz=8969`/`8943`, and the `D B_0³`-stage peak-fill counts `[46,502,2316,5994]` matching the ledger's cited reduction from v15.814's inflated fills exactly.

## v15.831 — nonzero five-helicity signal survives 3D gauge overlay, verified personally

Confirmed the script's hardcoded input coefficients match the v15.818 outputs I independently verified in Round 561. **Re-executed the committed script**: the physically-anchored overlay change (`2.2061915819741345e-19`) and the missing-shear false-signal ratio (`0.0590911068422506`, i.e. `5.91%`) both reproduced exactly.

## v15.832 — canonical-spectator perturbation-order argument, verified personally

Independently re-derived the central claim with a fresh SymPy computation (schematic 1D, `χ=εχ1`, `ξ=ε²ξ2`, `χ'=χ-ξ·∂χ`): expanding `(∂χ')²-(∂χ)²` as a polynomial in `ε` gives nonzero terms only at powers `{4,6}` — confirming the claimed result that the leading difference is `O(ε⁴)`, with no `ε²` or `ε³` term, exactly as Gate 453 states. **Re-executed the committed script**: passes.

## v15.833 — frozen K4 solid action gauge Ward, verified personally in full

This entry resolves the open item v15.832 explicitly deferred (the nonzero K4 solid background cannot be held fixed under a gauge overlay the way the zero-background spectator can). Given its importance, I independently re-derived every major claim from scratch with a fresh SymPy computation, rather than only re-running the committed script:

- **Strain cancellation (Gate 457):** built `E_ij=-h_ij+∂_iπ_j+∂_jπ_i` from the stated `h_ij=-2ℋTδ_ij-∂_iU_j-∂_jU_i` and `π=-U`, and confirmed independently that `E` reduces to exactly `2ℋT·δ_ij` (pure trace), so `E_TF=0` and `J^(2)=tr(E_TF²)/9=0` identically — matching the entry's claim exactly, not just checking it algebraically consistent.
- **Boundary-divergence identity (Gate 458):** independently computed `Φ+trh/2+trE/3` from the same building blocks and confirmed it equals exactly `-T'-divU-2ℋT`, matching the entry's claim term-for-term (`simplify` of the difference is identically `0`).
- **All ten stress components (Gate 459):** implemented the general Lie-derivative formula `δT_μν=-ℒ_ξT^{(0)}_μν` directly from the stated background `T^{(0)}_μν=diag(C,-C/3,-C/3,-C/3)` and independently confirmed all ten components (`δT00`, three `δT0i`, six `δTij`) match the entry's stated formulas exactly — this is the most nontrivial check in the entry and it holds without exception.
- The final Ward result (`δ(G_μν-κT_μν)=-ℒ_ξ(G^{(0)}_μν-κT^{(0)}_μν)=0`) follows immediately from `G^{(0)}=κT^{(0)}` (itself immediate from `3ℋ²=κC`) plus the standard fact that a Lie derivative of an identically-zero tensor vanishes — correctly invoked, not something requiring independent rederivation.

**Re-executed the committed script** (SHA-256 confirmed, commit `1e62f92` matching): all five internal PASS checks succeed, consistent with my independent derivation. The one part I did not independently re-derive from the full material-metric formalism is the precise `δb/b=(trE)/2` normalization (a definitional bookkeeping step tied to the paper's `E^IJ=a²δB^IJ` convention) — I verified it is *consistent* with the independently-confirmed `E_TF=0` headline result rather than re-deriving the material-metric formalism itself from the action. Scope is correctly limited to a covariance/Ward statement, not a componentwise ADM constraint proof or a claim about arbitrary physical sources, exactly as the entry states.

## v15.834 — frozen-phonon false elasticity, verified personally

Independently re-derived the quantitative witness from scratch: with `U_y=u cos(kx)` and `T=0`, confirmed `h_xy=+uk sin(kx)` (from `h_xy=-∂_xU_y`), and that the *correctly* transformed `π_y=-U_y` gives `E_xy=-h_xy+∂_xπ_y=-uk sin(kx)+uk sin(kx)=0` exactly. With the *incorrect* choice `π_y=0`, `E_wrong,xy=-uk sin(kx)` survives, and since this matrix is already tracefree, `J^{(2)}_wrong=tr(E_TF²)/9=2E_xy²/9=2u²k²sin²(kx)/9` — matching the entry's formula exactly. Plugging in `u=1/10,k=2,x=π/4` (`sin(π/2)=1` exactly) with exact `Fraction` arithmetic gives `2/225` exactly, matching the entry's cited witness to the rational number, not just its decimal approximation. **Re-executed the committed script** (SHA-256 and commit `7a7c111` confirmed): reproduces `J2=0` for the correct transformation and `2/225` for the frozen-phonon artifact exactly.

## Honesty and scope assessment

A very large, fully-confirmed round. Both open items from Round 561 (the v15.817 text correction and the v15.814 portability fix) were resolved correctly via the established additive pattern, and I independently verified both fixes rather than just reading the claim. The gauge-null program (v15.821→822→830→831) is a careful, honest sequence: each entry explicitly demonstrates not just that the correct construction gives zero, but that specific incomplete constructions give large false signals (up to 5.91% of the physical output) — a genuinely useful methodological result for future detector work, not a new physics claim. v15.832's perturbation-order argument is appropriately scoped (zero spectator background, specific gauge order only) and does not overclaim general gauge covariance. v15.833 closes that gap for the nonzero solid background with a clean, fully hand-verified covariance Ward identity. No corrections needed in this round.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.836
type: external-audit-round
status: actionable
action: v15.820 through v15.834 are all independently confirmed as stated, including both fixes from Round 561. v15.835 has a committed script (k4_single_fourier_remote_obstruction_v15_835.py) but no ledger text yet; audit of it is deferred to the next round once its entry lands. Per v15.823's own next-gate note, a memory-bounded R4 scaling test comparing exact-support factorized propagation with direct recomputation is authorized as the next concrete Suzuki step.
deliverable: Round 562 independent audit of v15.820 through v15.834.
