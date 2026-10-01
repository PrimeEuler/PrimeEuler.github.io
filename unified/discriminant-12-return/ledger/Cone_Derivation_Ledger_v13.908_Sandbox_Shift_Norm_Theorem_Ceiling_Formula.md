# Cone Derivation Ledger v13.908 — Sandbox Shift-Norm Theorem: the 2cos(π/k) Ceiling Formula [D]

Date: 2026-10-01

Author: LIttle Euler (sandbox track). Authorization: project owner, 2026-10-01 ("ledger all three!" following the shift-norm proof report).

Predecessors: v13.904 (kink stiffness as truncated shift, contraction theorem), v13.906 (sign erratum to the δ″ identity — the corrected sign this proof depends on — and §8 open item "prove ‖KK[m]‖ = 2cos(π/k) and identify k(m,a)"). Sandbox report: `shift_norm_proof.md` (run dir `runs/20260930-divisor-tension/`).

Status: **[D]** for the continuum norm formula, the exact k(m,a), and the corollaries (proofs in full); **[N]** for the FEM↔continuum identification (7 digits, N-stable, converged from below); **[O]** for extremal-vector classification and the m=7 value 1.21 (confirmed genuinely separate). No RH/GRH claims — the argument is pure spectral theory of the truncated shift, no zero input at all. This entry closes the first [O] item of v13.906 §8.

## 1. The theorem (sharp statement) [D]

> **Theorem.** For \(0 < h := \log m < 2a\), on \(L^2(-a,a)\):
> \[ \|KK[m]\| = 2\cos\!\left(\frac{\pi}{\lceil 2a/h \rceil + 1}\right), \]
> i.e. **\(k(m,a) = \lceil 2a/\log m \rceil + 1\) exactly.**

The earlier "roughly \(2a/h + 1\)" was the exact ceiling formula all along. The integer \(k\) counts the longest shift-orbit (§3); the proof is the orbit decomposition plus the classical path-graph spectrum — no heavy machinery.

## 2. Step 1 — setup [D]

From the sign-corrected δ″ identity (v13.906 §6 — independently re-verified here by direct quadrature, ratio \(A/B = -1\) to 6 digits):
> \(KK[m] = -(T_h + T_{-h})\) on \(L^2(-a,a)\), \(h = \log m\),

where \((T_h u)(x) = u(x-h)\,\mathbf{1}_{(-a,a)}(x-h)\) and \((T_{-h}u)(x) = u(x+h)\,\mathbf{1}_{(-a,a)}(x+h)\) are the truncated shifts. \(T := T_h + T_{-h}\) is bounded self-adjoint (\(T_h^* = T_{-h}\)), \(\|T\| \le 2\).

Since \(\mathrm{spec}(T)\) is symmetric about 0 (each fiber is bipartite, §4), \(\mathrm{spec}(KK[m]) = -\mathrm{spec}(T) = \mathrm{spec}(T)\), hence
> \(\|KK[m]\| = \|T\| = \max\,\mathrm{spec}(T)\) [D].

So it suffices to compute \(\|T_h + T_{-h}\|\).

## 3. Step 2 — orbit decomposition [D]

For \(h > 0\), partition \((-a,a)\) into **shift orbits**. Every \(x \in (-a,a)\) has a unique *seed* \(x_0 = x - \lfloor (x+a)/h \rfloor \cdot h\) in the seed strip \(S := [-a, -a+h)\). The orbit of \(x_0\) is
> \(O(x_0) = \{x_0 + jh : j = 0, \dots, n(x_0)-1\},\quad n(x_0) = \lceil (a-x_0)/h \rceil,\)

the maximal \(h\)-chain in \((-a,a)\) (\(n(x_0)\) is a right-continuous step function; each value it takes is taken on an interval, hence on a set of positive measure).

The map \(\Phi: L^2(-a,a) \to \int_S^\oplus \mathbb{C}^{\,n(x_0)}\,dx_0\), \((\Phi u)(x_0) = (u(x_0+jh))_{j=0}^{n(x_0)-1}\), is unitary (orbits partition \((-a,a)\) up to null sets). Under \(\Phi\):
- \((\Phi T_h u)(x_0)_j = u(x_0+(j-1)h) = (\Phi u)(x_0)_{j-1}\) for \(j \ge 1\), and \(= 0\) for \(j = 0\) (since \(x_0 - h < -a\)) — **\(T_h\) shifts down-fiber: the subdiagonal**;
- \((\Phi T_{-h}u)(x_0)_j = u(x_0+(j+1)h) = (\Phi u)(x_0)_{j+1}\) for \(j \le n-2\), and \(= 0\) for \(j = n-1\) — **\(T_{-h}\) shifts up-fiber: the superdiagonal**.

Hence on each fiber, \(T\) acts as \(A_{n(x_0)}\), the \(n \times n\) **path-graph adjacency matrix** (ones on the first off-diagonals, zeros elsewhere):
> \(T = \int_S^\oplus A_{n(x_0)}\,dx_0\) [D].

## 4. Step 3 — spectrum and norm [D]

The \(n \times n\) path adjacency has the classical spectrum (discrete sine transform)
> \(\mathrm{spec}(A_n) = \{\,2\cos(\pi j/(n+1)) : j = 1, \dots, n\,\}\) [D, standard],

symmetric about 0 (bipartite), with largest eigenvalue \(2\cos(\pi/(n+1))\), strictly increasing in \(n\).

For a direct integral whose fiber takes finitely many values, each on a positive-measure set: \(\mathrm{spec}(T) = \bigcup_{n \in N}\mathrm{spec}(A_n)\) with \(N = \{n(x_0) : x_0 \in S\}\) (finite, hence the union is closed). Therefore
> \(\|T\| = \max_{n \in N}\, 2\cos(\pi/(n+1)) = 2\cos(\pi/(n_{\max}+1))\), \(n_{\max} := \max N\) [D].

Now \(n_{\max} = n(-a) = \lceil 2a/h \rceil\) (attained at the left endpoint; the set \(\{x_0 : n(x_0) = n_{\max}\} = [-a, \min(-a+h,\, a-h(n_{\max}-1)))\) has positive measure since \(n_{\max}-1 < 2a/h\)). Conclude:
> **\(\|KK[m]\| = 2\cos(\pi/(\lceil 2a/h \rceil + 1))\) for \(0 < h < 2a\) [D]**,

i.e. **\(k(m,a) = \lceil 2a/\log m \rceil + 1\)**.

## 5. Corollaries [D]

- **\(h > a\) (but \(< 2a\)):** \(1 < 2a/h < 2\), \(\lceil 2a/h \rceil = 2\), \(k = 3\), \(\|KK[m]\| = 2\cos(\pi/3) = \mathbf{1}\). This *explains* the contraction theorem's tightness: the longest orbit has exactly 2 points, and the bound \(\pm 1\) is attained. The "switch-on at \(m = e^a\)" is the orbit length dropping \(3 \to 2\).
- **\(h = a\):** \(\lceil 2 \rceil = 2\), norm exactly 1 — continuous with the above.
- **\(h \ge 2a\):** \(\lceil 2a/h \rceil = 1\), \(k = 2\), \(2\cos(\pi/2) = \mathbf{0}\). Indeed no pair at distance \(h\) fits in \((-a,a)\), so \(T = 0\). (Checked numerically: \(a=2\), \(m=60\) gives FEM max loading exactly 0.0 [N].)
- **\(h \to 0^+\):** \(\lceil 2a/h \rceil \to \infty\), norm \(\to 2\) — the untruncated shift sum has norm 2. Consistent.
- The top eigenspace is infinite-dimensional (one sin-profile per seed in the longest-orbit seed set) — this is why the FEM maximizer is non-unique and mesh-dependent in shape, while its *eigenvalue* is pinned.

## 6. Spot-checks and numerical confirmation

**Spot-checks [D, formula vs. every observed value].** At \(a = 2\): \(m=2 \to 2\cos(\pi/7)\), \(m=3 \to \varphi\), \(m=4 \to \sqrt{2}\), \(m=7 \to \sqrt{2}\), \(m \ge 8 \to 1\) — all match the "anomaly" table exactly. In particular the \(m=7\) global-shift value \(\sqrt{2}\) and the \(m \ge e^a\) switch to 1 are both instances of the formula.

**FEM [N].** P1, generalized eigenvalues of \((K, M)\), \(K\) assembled from the pure-kink screw. The discrete Rayleigh quotient is a Galerkin restriction, so FEM norm \(\le\) continuum norm, converging from below. Representative results (N=400):

| \((a, m)\) | FEM | \(2\cos(\pi/k)\), \(k = \lceil 2a/h \rceil+1\) | diff |
|---|---|---|---|
| (3, 2) | 1.9021057 | 1.9021130 (k=10) | −7.3e−6 |
| (3, 3) | 1.8019342 | 1.8019377 (k=7) | −3.5e−6 |
| (3, 4) | 1.7320416 | 1.7320508 (k=6) | −9.2e−6 |
| (3, 8) | 1.4142133 | 1.4142136 (k=4) | −2.9e−7 |
| (3, 23) | 0.9999999 | 1.0000000 (k=3) | −6.8e−8 |
| (2, 2) | 1.8019360 | 1.8019377 (k=7) | −1.8e−6 |
| (1, 2) | 1.4142133 | 1.4142136 (k=4) | −2.9e−7 |
| (4, 5) | 1.7320499 | 1.7320508 (k=6) | −8.7e−7 |

All diffs negative (Galerkin from below ✓), across \(a \in \{1, 1.7, 2, 2.5, 3, 4\}\). Thin-fiber cases (\(2a/h\) just above an integer, e.g. (3,7): \(2a/h = 3.083\), (3,19): \(2a/h = 2.038\)) converge slower but monotonically, 400 → 800 → 1600 toward the target [N].

**Eigenvector check [N]:** at \((a=3, m=3)\), the top FEM eigenvector's mass concentrates on the longest-orbit seed set, as the fiber picture predicts. The single-orbit sin-profile correlation is poor, as expected: the top eigenspace is infinite-dimensional and the P1 mesh is not orbit-aligned, so the FEM maximizer mixes seeds incoherently — the *value* is pinned, the *vector* is not.

## 7. Status and what remains

| Claim | Status |
|---|---|
| \(\|KK[m]\|_{L^2(-a,a)} = 2\cos(\pi/(\lceil 2a/\log m \rceil+1))\), \(0 < \log m < 2a\) | **[D]** (§§2–4) |
| \(k(m,a) = \lceil 2a/\log m \rceil + 1\) exactly | **[D]** |
| Contraction tightness for \(h > a\) explained (longest orbit = 2 points) | **[D]** (§5) |
| \(h \ge 2a \Rightarrow KK[m] = 0\) | **[D]** (§5) |
| FEM generalized eigenvalues converge to the continuum value (7 digits, N-stable, from below) | **[N]** (§6) |
| Closed-form classification of the extremal *vectors* | **[O]** — value pinned [D]; infinite-dimensional top eigenspace, no canonical vector |
| The \(m=7\) value 1.21 | **[O]** — confirmed genuinely separate: a null-cluster-restricted maximum, not the global shift norm proved here |

**Conceptual note [I]:** the "anomaly" is now understood as orbit combinatorics — the integer \(k\) is a *count*, not a fitted parameter. Tightness of the contraction bound on the full space (\(\|KK[m]\| = 1\) for \(h > a\)) does not imply saturation on any particular subspace (e.g. the \(\lambda_1\)-eigenspace); the companion V-shape investigation keeps the two distinct.

## Synchronization

Live ledger head checked immediately before this write: v13.907 (audit thread, External Audit Round 131 — read in full; PASS on v13.906, independently confirming the sign erratum, the γ₁ frequency transition, and the two-bump construction). No collision on v13.908.
