# Sandbox Audit: v14.076 Coarse 16k→32k Operator-Radius Transport

**Task:** v14.076 HANDOFF (type: coarse-shell-operator-radius-audit).
**Date:** 2026-10-06
**Verdict:** **OUTCOME B (OBSTRUCTION)** — the θ_p premise does not transport automatically; exact missing primitive identified; max admissible θ_e^{32k} computed.
**Status:** [D] arithmetic verification; [D] transport-obstruction proof; [N] max-θ_e computation; [O] Lane A's 32k floor primitives.

---

## 1. Arithmetic verification [D]

Independently recomputed v14.076 §2 from `suzuki_M16000_M32000_coarse_shell_budget.py` formulas (80-digit Decimal):

- mid = η_o − η_e = −2.393558e-5 ✓
- W = 8.214462e-6 ✓
- Conditional interval = [−3.215004e-5, −1.572112e-5] ✓ (matches cited to all digits)
- Upper endpoint < 0 ✓ **conditional on the θ_p premise.**

The *arithmetic* is correct. The *premise* is what fails (see §3).

Producer: `~/workspace/d12/coarse_shell_audit.py`.

---

## 2. The "promoted values" discrepancy [D]

v14.076 §2 states the θ_p are "the same promoted values used in v14.052/v14.058." This is **inaccurate**:

- **v14.052** derived θ_e = 3.9e-6 as the *independent* capacity radius, then **explicitly instructed not to use it**: HANDOFF constraint "do not pay the independent 3.9e-6 even capacity source radius twice in the shell ratio." The promoted near-shell interval used *common-mode* cancellation (L_{src,e} < 5.67e-10), not independent θ_p.
- **v14.058** likewise used common-mode (R^{src}_{η,e} < 3.4e-10) with constraint "do not pay independent capacity radii."
- What was *promoted* (v14.055/56) is the **normalization** δ_{√C,e} ≤ 3e-6 (sqrt-capacity), a *weaker* bound than the computed 1.95e-6. The operator θ_e = 3.899e-6 itself was **never promoted as a theorem for independent use**; `suzuki_arch200_capacity_source_perturbation_budget.py` is a budget script, not a ledger theorem.

**Consequence:** The θ_p premise in v14.076 rests on values that (a) were computed for M=8000/N=4000, (b) were deliberately avoided in the promoted v14.052/v14.058 intervals, and (c) have no established transport even to N=16000, let alone N=32000.

---

## 3. Transport obstruction [D]

The θ_p derivation (`suzuki_arch200_capacity_source_perturbation_budget.py`) gives θ = eps/(μ − eps), where:

- **eps** = scalar representation operator radius. **Controlled at 32k** per v14.076 §4 (even max z-error 5.877e-39 < 5.88e-39 public cap). Not the obstruction.
- **μ** = global Euclidean floor for the exact shifted front, from v14.034's M=8000 graph-Schur factorization:
  - μ = min(sfloor, DELTA_Q)/(1 + kcap)²,
  - sfloor from LAMBDA_GRAPH (protected B^*SB ≥ 3.97e-30 even),
  - DELTA_Q from v14.031 complement floors (7.80e-6 even),
  - kcap from WFROB2 graph Frobenius norms (≈3.45).
  - Result: μ_e ≈ 2.0e-31, μ_o ≈ 7.3e-28.

**Why μ does not transport:**

1. The v14.034 primitives (protected six-plane P, complement floors, shear norms, λ_out bounds) are **M=8000-specific numerical objects**. The θ_source.py transfers μ to A_N only for N ≤ 8000 via principal compression ("A_N is the retained principal compression of F").
2. A_{p,16000} (16000×16000) and A_{p,32000} (32000×32000) are **not** principal submatrices of the M=8000 F. The floor implication goes the wrong way (larger section ⇒ potentially smaller floor; e.g. diagonal 1/n gives μ_N = 1/N → 0).
3. **v14.071 does not help.** It proves S_{p,N} ≽ I for the *remote* Schur complement on H_{>N}. The θ_p needs a floor for the *finite* N×N section A_{p,N}. These are different operators; remote coercivity implies nothing about the finite-section floor.

**Missing primitive (exact):** A global Euclidean floor μ_{32k} > 0 for the exact 32000×32000 finite-section operator (equivalently, the M=32000 shifted front), with the associated M=32000 graph primitives:
  - protected-block outward floor (analog of LAMBDA_GRAPH),
  - complement floor (analog of DELTA_Q/v14.031),
  - graph shear norm (analog of WFROB2),
  - scalar eps_{32k} (already available per v14.076 §4).
This is a **finite numerical computation** in Lane A's domain (fixed-FFT/graph machinery at 32k), not derivable by pure analysis from M=8000 data.

---

## 4. Maximum admissible θ_e^{32k} [N]

For the coarse shell to remain strictly negative, W < |mid| = 2.393558e-5. Binary search on θ_e (θ_o fixed, negligible):

$$
\boxed{\theta_e^{\max,32k} = 1.174454 \times 10^{-5}}
$$

i.e. **3.01× headroom** over the old θ_e = 3.899e-6. Sensitivity:

| θ_e | shell interval | strictly negative? |
|---|---|---|
| 3.9e-6 (old) | [−3.215e-5, −1.572e-5] | ✓ |
| 1.0e-5 | [−4.438e-5, −3.496e-6] | ✓ |
| 1.17e-5 (max) | upper → 0⁻ | marginal |
| 2.0e-5 | [−6.441e-5, +1.654e-5] | ✗ |

**Required floor strength:** With eps_{32k} ≈ 2× eps_{8000} ≈ 1.4e-36 (even, scaling √N for pole term and log N for harmonic sum), achieving θ_e ≤ 1.17e-5 needs μ_{32k} ≥ eps/θ_max ≈ 1.2e-31 — **comparable to the M=8000 μ_e ≈ 2.0e-31**. This is a plausible target for Lane A's 32k graph computation (not orders harder than what v14.034 already did), but it must be *done*, not assumed.

---

## 5. Path forward

1. **Lane A** produces the M=32000 graph-floor package (protected floor, complement floor, shear norm) via the v14.034 methodology at 32k, yielding an explicit θ^{32k}_p. If θ^{32k}_e ≤ 1.17e-5, the v14.076 shell interval promotes.
2. **Alternatively**, Lane A runs the *common-mode* 16k→32k analysis (as in v14.052/v14.058), which avoids independent θ_p entirely but is more expensive. The large sign margin (−2.39e-5 vs W=8.2e-6) suggests common-mode would pass easily.
3. **Do not** promote the v14.076 interval on the current premise. The arithmetic is correct but the θ_p transport is unproven, and the "promoted values" citation is inaccurate.

No common-mode gradient replay was attempted (per handoff: coarse preferred, and the obstruction is in the premise, not the margin). No infinite-tail inference made.

---

## 6. Result

$$
\boxed{
\begin{aligned}
&\text{\textbf{OUTCOME B (OBSTRUCTION).} v14.076 §2 arithmetic verified exactly,}\\
&\text{but the }\theta_p\text{ premise does not transport.}\\
&\text{The }\theta_p=3.9\times10^{-6}\text{ values were derived for }M{=}8000/N{=}4000\\
&\text{and deliberately \emph{not} used independently in v14.052/v14.058}\\
&\text{(common-mode was used instead); they were never promoted for}\\
&\text{independent use, and have no established transport to 16k or 32k.}\\[4pt]
&\text{The }\mu\text{ floor is M=8000-specific (v14.034 graph primitives);}\\
&\text{A}_{p,32000}\text{ is not a principal submatrix of the M=8000 front;}\\
&\text{v14.071's remote }S_{p,N}\succeq I\text{ does not imply a finite-section floor.}\\[4pt]
&\text{\textbf{Missing primitive:} global floor }\mu_{32k}\text{ for the exact }32000\times32000\\
&\text{finite operator + M=32000 graph package (Lane A finite computation).}\\[4pt]
&\text{\textbf{Max admissible: }}\theta_e^{32k}\le1.17\times10^{-5}\ (3.01\times\text{ headroom over old }\theta_e).\\
&\text{Required }\mu_{32k}\gtrsim1.2\times10^{-31}\text{, comparable to M=8000's }2.0\times10^{-31}\\
&\text{— plausible for Lane A to produce, but must be produced.}
\end{aligned}
}
$$

**Staged files:**
- `~/workspace/d12/coarse_shell_transport_audit.md` (this report)
- `~/workspace/d12/coarse_shell_audit.py` (interval recomputation + max-θ_e binary search)
