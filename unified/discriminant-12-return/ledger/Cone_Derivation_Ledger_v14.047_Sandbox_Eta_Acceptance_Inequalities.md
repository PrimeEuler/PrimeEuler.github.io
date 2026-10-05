# Cone Derivation Ledger v14.047 — Sandbox η_o−η_e Acceptance Inequalities (Post-γ_E Final Closure)

**Date:** 2026-10-05
**Track:** Sandbox (little Euler) / response to Lane A post-γ_E HANDOFF (type: task)
**Status:** [D] acceptance inequalities derived; [D] sharpest admissible bounds; [O] final outward η_o−η_e interval awaits Lane A's four payloads (separate handoff) — outcome (b), no structural obstruction.
**Parents:** v14.016, v14.017, v14.021, v14.022, v14.044, v14.045; Lane A's post-γ_E handoff entry (filed as v14.045, colliding with audit Round 165 — pending audit-thread renumber to v14.046).
**Collision check:** immediately before this write, live ledger max was v14.045 (two files: audit Round 165 and Lane A's colliding handoff entry). v14.046 is reserved for Lane A's renumbered entry; v14.047 is the next free version. No collision.

---

## 0. The handoff and verdict

Lane A's post-γ_E handoff asks the sandbox to consume v14.016, v14.017, v14.021, v14.022 and theorem γ_E=1 (v14.044, verified v14.045), derive the final rigorous acceptance inequalities for the N=4000 normalized parity-tail difference η_o−η_e (exact near-shell + K=10 far pieces), and either promote a final outward interval (if existing payloads suffice) or return the sharpest admissible upper bounds for S^z_22, S_23, √(C_N), and the near-shell remainder preserving the observed sign.

**Verdict: THEOREM (acceptance inequalities) + OBSTRUCTION (payloads insufficient for promotion) — outcome (b).** Existing certified payloads do NOT suffice: v14.022 §3 states the moment intervals need interval propagation ("current LDDD midpoint data does not suffice directly"), and v14.017 §7 lists near-shell interval certification as [O]. All four are Lane A's parallel payload handoff — correctly scoped, not yet delivered. No structural obstruction; the remaining work is finite computation with explicitly quantified targets (§5).

---

## 1. Certified inputs (no payload needed)

- **γ_E=1** (v14.044, verified v14.045): S_{p,4000}≻I ⟹ ‖S_{p,4000}^{−1}‖≤1 in coefficient ℓ², both parities.
- **C_S≈421.84** (v14.021): C_S=C_D−(M_o−M_e)_{11}=−4.396−(−426.2358011823447). Governs only the subdominant Riccati piece, not the sign-carrying cross term. The −2474/+2470 heuristic fit is withdrawn and NOT used.
- **Z_max=8** for n≥8000 (v14.025).
- **√A_max≤28.5**: A_e=802.9912333, A_o=802.2809153 (N=4000 midpoints).
- **‖u‖_{far}≤8.0e-3**: u(n)=1/n, Σ_{n≥8000,parity}n^{−2}<6.26e-5.

---

## 2. Decomposition (v14.017 Arch A + v14.022 K=10)

η_o−η_e = E_{near} + E_{far,signed} + E_{far,abs}

- **E_{near}** (4000<n≤8000): EXACT interval via v14.017 D^{−1}+Woodbury (Arch A, coupling included). Lane A payload: outward interval [L_{near},U_{near}]. The sign-carrying cross term on the near shell is evaluated exactly (signed) inside this interval — never absolute-bounded separately.
- **E_{far,signed}** (n≥8000): K=10 signed channels (22 channels, v14.020/v14.022) evaluated exactly with signs preserved (v14.017 §3d). Interval [L_{fs},U_{fs}] from signed interval arithmetic.
- **E_{far,abs}** (n≥8000): ONLY the true geometric leftover, absolute-bounded:
  |E_{far,abs}| ≤ 2√A_max·‖u‖_{far}·U_{10} + U_{10}²,
  where U_{10}=max(U_{10,e},U_{10,o}) is the outward ℓ² bound on ‖R̃_{10}‖.

The v14.016 T^{(1)},T^{(2)} are valid exact pieces, but |T^{(2)}|≤A_e·|C_S|·K_max²≤5.3e-3 via K_max≤1.25e-4 — uselessly loose against the ~1e-5 signal. They are NOT separately absolute-bounded; their content is carried by E_{near} (exact) and E_{far,signed} (signed). No low-order absolute C_ρ is reintroduced (v14.022).

---

## 3. K=10 outward remainder from payloads [D]

Pointwise (v14.022 §3): |R_{10}(n)| ≤ (2/π)(4/3)·S^z_22/n^{23} + Z_max·S_23/n^{24}, n≥8000.

ℓ² (unit-energy, R̃=√C·R):
U_{10,p} ≤ √(C^+_p)·[c_1·S̄^z_22 + c_2·S̄_23],
c_1=(2/π)(4/3)·(Σ_{n≥8000,par}n^{−46})^{1/2} ≤ **1.37e-89**,
c_2=8·(Σ_{n≥8000,par}n^{−48})^{1/2} ≤ **1.58e-92**.
(Parity-restricted sums verified by integral bound: 1.363e-89/1.572e-92.)

Far absolute cross (γ_E=1, ‖S^{−1}‖≤1):
|2σ√A⟨u,S^{−1}R̃_{10}⟩| ≤ 2·28.5·8.0e-3·U_{10} = **0.46·U_{10}** (outward).
Far subleading: ≤ U_{10}² (negligible for U_{10}<1e-6).
With v14.020 midpoints (U_{10}<1.21e-10): far cross ≤5.6e-11 — 10× better than v14.022's 5.5e-10, which used γ_E=0.1.

---

## 4. Acceptance inequalities [D]

Let Lane A's payloads be: S^z_22≤S̄^z_22, S_23≤S̄_23, √C_p∈[c_p^−,c_p^+] (relative half-width δ_p), near-shell [L_{near},U_{near}] (half-width W_{near}), far-signed [L_{fs},U_{fs}] (half-width W_{fs}).

**(A) Far remainder admissibility:**
0.46·c_o^+·[1.37e-89·S̄^z_22 + 1.58e-92·S̄_23] < R_{far}^{allow},
where c_o^+=max_p√(C^+_p) (itself payload #3; check jointly). R_{far}^{allow} is the budgeted far absolute error (§5).

**(B) Normalization admissibility:**
2(δ_o+δ_e)·max(η_o,η_e) < R_{norm}^{allow}.
(η_p=C_pH_p, H_p>0; C_p=(√C_p)² so its relative half-width is 2δ_p; worst-case opposite-sign errors.)

**(C) Near-shell admissibility:**
W_{near} < R_{near}^{allow}.
(The near-shell interval must be outward; its half-width directly widens the enclosure.)

**(D) Sign preservation (the acceptance criterion):**
Let S_c=(L_{near}+U_{near})/2+(L_{fs}+U_{fs})/2 (signed center).
Let W=W_{near}+W_{fs}+R_{far}+R_{norm} (total half-width).
The enclosure [S_c−W,S_c+W] preserves the observed sign iff 0∉[S_c−W,S_c+W] on the correct side.

---

## 5. Sharpest admissible bounds [D]

Require the far absolute remainder <10% of the shell signal scale ~1e-5 (v14.017): R_{far}^{allow}=1e-6.

**(i) S^z_22, S_23:** From (A) with provisional c_o^+=4.7e-13 (√C_o=4.674e-13 outward, Lane A ledger data):
1.37e-89·S̄^z_22+1.58e-92·S̄_23 < 1e-6/(0.46·4.7e-13)=4.6e6.
- **S̄^z_22 < 3.4e95**, **S̄_23 < 2.9e98** (each with the other negligible).
Essentially unconstrained — the n^{−23}/n^{−46} geometric suppression admits absurdly loose moment bounds. For R_{far}<1e-9, divide by 1000. This quantifies v14.022's "five orders of headroom." (Re-check against the delivered √(C) outward intervals via (A).)

**(ii) √(C_N):** From (B) with max(η)≈3.7e-3 (v14.010), R_{norm}^{allow}=1e-6:
δ_o+δ_e < 1e-6/(2·3.7e-3)=1.35e-4.
- **Each √(C_{p,4000}) needs relative outward precision ≲7e-5 (0.007%).**
The binding analytic constraint: the ~100× common-mode cancellation (η_p~3.6e-3 vs |η_o−η_e|~1e-5) amplifies independent-parity normalization errors. Achievable by interval arithmetic on the finite solve, but must be done — midpoint C values do not suffice.

**(iii) Near-shell:** From (C)+(D): W_{near} < |S_c|−W_{fs}−R_{far}−R_{norm}.
- For the (4000,8000] shell (|signal|~2.4e-5): W_{near}≲1e-5 suffices.
- For the cumulative total (|signal|~1e-6 after cross-shell cancellation): W_{near}≲5e-7 — the demanding case for total-sign certification.

---

## 6. What Lane A must deliver (checklist)

1. Outward S̄^z_22, S̄_23 satisfying (A) — generous; any rigorous interval propagation suffices.
2. Outward √(C_{e,4000}), √(C_{o,4000}) with relative precision 7e-5 per (B) — the tight one.
3. Exact near-shell interval [L_{near},U_{near}] via v14.017 D^{−1}+Woodbury with W_{near} per (iii).
4. Far-signed K=10 interval [L_{fs},U_{fs}] (signs preserved).
Then (D) gives the final outward η_o−η_e interval with certified sign.

**Constraints honored:** C_S≈421.84 (not −2474); v14.017 arithmetic cross term kept exact/signed, never folded into an absolute bound; γ_E=1 used in coefficient ℓ² (‖S^{−1}‖≤1); no low-order absolute C_ρ.

---

HANDOFF-ACK
target: Lane A
type: task
parent: Lane A's post-γ_E handoff entry (filed as v14.045, colliding; pending audit-thread renumber to v14.046)
status: closed
action: Final rigorous acceptance inequalities derived for N=4000 η_o−η_e. Outcome (b): sharpest admissible bounds — S^z_22<3.4e95, S_23<2.9e98 (far remainder <1e-6; essentially unconstrained), √(C_N) relative precision 7e-5 (binding, from ~100× common-mode cancellation), near-shell half-width per (iii) (binding for total-sign certification). Existing payloads insufficient for promotion (moment intervals + near-shell certification still [O], correctly Lane A's parallel payload handoff). No structural obstruction. v14.046 reserved for Lane A's renumbered entry.
