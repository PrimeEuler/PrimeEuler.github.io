# Cone Derivation Ledger v13.902 — Sandbox Rigidity Experiment: the Λ Weights Are an Isolated Maximizer of λ₁

Date: 2026-10-01

Author: LIttle Euler (sandbox track). Authorization: project owner, 2026-10-01 ("ledger and continue!" following the rigidity verdict report).

Predecessors: v13.896 (full-A_a FEM joint experiment + prime-power ablation: the Λ knife-edge), the sandbox selector study (`selector_principle_exploration.md`, §3 multicritical pilot, §5 gate — sandbox only, not ledgered), which posed this experiment as its kill-or-confirm gate.

Status: **[N]** numerical throughout (full-A_a P1 FEM at a = 2, dense `eigh`; floor calibrated +1.8e−8, N-stable 800→3200; "breaks" = λ₁ < −1e−6, 50× the floor); **[D]** for the concavity argument; **[I]/[O]** for interpretation. No RH/GRH claim. No positivity-program transfer beyond what is stated.

## 1. The gate [D, restating the selector study §5]

Perturb the von Mangoldt weights c_n = Λ(n)/√n and map where positivity breaks:
- **Isolated/rigid:** all directions break at small ε → Λ is a rigid multicritical point → the "positivity selects" gloss gets its first real leg.
- **Flat/manifold:** some direction tolerates O(1) deformation with λ₁ ≥ 0 → mark "permitted, not selected," clean kill of the gloss.

Scripts and data: `rigidity_lib.py`, `rigidity_screen{,2}.py`, `rigidity_confirm.py`, `rigidity_vectors.py`, `rigidity_cluster.py`, `rigidity_final.py`; JSONs and `rigidity_summary.png` (sandbox run dir `runs/20260930-divisor-tension/`; ad hoc but complete and re-runnable).

## 2. Verdict: ISOLATED / RIGID [N]

110+ directions probed in weight space around the Λ point:

- **Single-kink rays — a symmetric V at every kink [N].** For each kink m, c_m → (1+ε)c_m gives λ₁(ε) = −s_m·|ε|: linear, both signs break, symmetric to 6 digits (kink 9, N=1600: −3.661941e−3 vs −3.661935e−3). Λ is a strict peak along every ray, not a smooth boundary point. Linearity holds ε = 0.002 → 1.0.
- **Exactness [N].** For all well-resolved kinks (m ≥ 8 prime powers, m ≥ 11 primes): **s_m = c_m = Λ(m)/√m, 4–6 digits.** Each kink is individually load-bearing with precisely its von Mangoldt coefficient, in both directions. Small kinks load harder (s_2/c_2 = 1.8010, s_3/c_3 = 1.6178, s_4/c_4 = 1.41415 ≈ √2, s_5/c_5 = 1.41403 ≈ √2, s_7/c_7 = 1.2110) — tower/neighborhood effects, no closed form identified [O]. Edge kinks (37–53) show slight asymmetry, flagged as domain-edge resolution effect, excluded from exactness claims.
- **Everything else breaks both ways [N].** Towers, groups, balanced pairs preserving Σw/√n, smooth n^δ deformations (δ=±0.01 → λ₁ ≈ −0.15/−0.19, violent), 80 seeded random directions (all robustly negative; least-negative 300,000× the floor), two 2D grids (origin alone at +1.8e−8, no ridge, no flat direction).
- **Mechanism of the V [N].** Q_full = Q_0 + Σ_n c_n·KK[n] with KK[n] the pure kink stiffness (assembly verified linear in g to 1.4e−5). The null space of Q_full contains directions loading on kink m with **exactly ±1** (e.g. kink 9: vᵀKK[9]v/M = −1.0000 while vᵀQ_full v ≈ 1e−7). The V is a **level crossing** between opposite-loading null directions.

## 3. The concavity promotion [D]

λ₁(w) = min_v vᵀQ(w)v/vᵀMv with Q linear in w is a minimum of linear functions, hence **concave** in the weight vector. A strict local maximizer of a concave function — if the ray-wise peak extends to a full neighborhood, which 110+ rays and two 2D grids support — is the **unique global maximizer**. The positivity cone {w : λ₁(Q_w) ≥ 0} is then numerically the **isolated point {Λ}**: no manifold of positive weights exists near Λ, and none anywhere.

## 4. What this means for the house creed [I]

The selector study's §5 gate returned the rigid outcome: the clean kill ("manifold exists → permitted, not selected") did **not** happen. The "positivity selects" gloss is promoted **[O]→[N]** — as a **variational selection of the weights**: Λ = argmax_w λ₁(Q_w), unique.

**Honest scope:** what is selected here is the *weight sequence*. The chain weights → ψ → zero ordinates runs through the explicit formula, and the analytic *why* — why the maximizer's coordinates are exactly Λ(n)/√n — remains open [O]. The creed is satisfied in the **weak form** (a shown selection principle for the weights); the **strong form** (selecting the ordinates themselves) is still the project's open question.

## 5. Secondary resolutions [N]

- **Even/odd degeneracy — genuine.** The minus_m ground state is parity-doubled to solver tolerance for the leading kinks (minus_9: gap 3.3e−7, opposite parities, N-stable 800→1600); the lifting for higher towers is likewise genuine (minus_25: 1.56e−3 gap, N-stable) — not a discretization artifact. The pilot's [O] is closed.
- **n = 4 → c₂ tower backing — characterized, naive story refuted.** |λ₁(minus_4)| = √2·c_4 = c_2 confirmed to 6 digits; minus_5 is √2 only to 4 digits (not exact — the √2 is special to m=4). Null-space anatomy: v*_4 is **even**, KK[4]-loading = √2, KK[2]-loading ≈ 0, and ⟨v*_4|v*_2⟩_M = 0 — the 2-tower does *not* share one marginal direction; the "tower backing via shared vector" story is wrong. (The 2-/3-tower *leading* kinks do share: v*_8 ≈ −v*_9, overlap −0.9916, both odd, loadings +1.000.) Analytic origin of the √2 remains [O]; leads: kink scaling k_4(t) = 2·k_2(t/2), even-sector structure.

## 6. What this is not

- **Not a proof.** Numerical [N] throughout; the concavity promotion is conditional on the neighborhood peak (strongly evidenced, not proved).
- **Not an RH result.** It selects the weights, not the zeros. No transfer to the ordinates is claimed.
- **Not connected to the twisted channel or the de Branges line.** The full D12 nonnegative-channel positivity question and the r-gate's odd-sector ill-posedness are untouched by this entry.

## Synchronization

Live ledger head checked immediately before this write: v13.901. No collision on v13.902.
