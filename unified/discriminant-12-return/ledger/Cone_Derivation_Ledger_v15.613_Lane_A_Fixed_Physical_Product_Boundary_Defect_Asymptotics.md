# Cone Derivation Ledger v15.613 — Lane A: fixed-physical-product secant and boundary-defect staircase asymptotics

**Date:** 2026-11-10. **Parents:** v13.197 circular staircase pushforward; v14.767 mesh and power-map covariance; v15.602 generalized boundary Casimir; v15.605 circle/secant two comparison protocols; v15.608–609 2D pushforward and scale/origin laws; v15.610 External Audit Round 522; v15.611 reconciled fixed-step Gate 81–82; v15.612 origin/measure robustness. **Status:** [D] exact finite integral methodology and asymptotic formulas; [O] physical Hamiltonian, q=2 selection, field, G. **Immediately prewrite checked HEAD:** 64033f0872266be2437f4e51076788c8adeb7383; v15.613 collision search empty. Additive only; Suzuki frozen production untouched.

## Gate 85 — hold the *physical* product fixed

Choose physical factor product X>0, normalized grid unit u=1/q, original **fixed physical step** s=1, normalized integer cutoff n_q=floor(Xq²). The triangular/divisor staircases are the EXACT v13.197 cell unions scaled by u: column k covers physical x∈[(k−1)/q,k/q], with heights h_T=(n_q+1−k)/q and h_D=floor(n_q/k)/q. Their complement A_n is the set difference. The cone circle-area Jacobian is J=(x+y)/(4sqrt(xy)).

With original-step continuum boundary profile
E_s(x,y)=1/2[y(x+s)1_(y<s)+x(y+s)1_(x<s)],
define B_{*,q}=∫∫_{scaled *} E_1 J dxdy.

Unlike fixed normalized n in v15.611, the normalized index grows ~Xq² while the physical product threshold remains X. The circle section at (un,u) has secant-radius fraction 2q sqrt(X)/(q²X+1)~2/(q sqrt(X)). Physical comparison does not hold diameter fixed.

For X=3, independent per-column **analytic antiderivative** evaluation gives:

| q | n | B_T | B_D | B_A/B_T |
|---:|---:|---:|---:|---:|
| 2 | 12 | 7.9934893228 | 4.5309978424 | .43316396 |
| 4 | 48 | 37.7379945012 | 8.8792920744 | .76471214 |
| 8 | 192 | 198.9589688447 | 17.2214744203 | .91344208 |
| 16 | 768 | 1092.3842463388 | 33.4640210280 | .96936607 |
| 32 | 3072 | 6096.3105087921 | 65.4315016634 | .98926703 |
| 64 | 12288 | 34265.0518065041 | 128.7526407364 | .99624245 |

Independent regression at q=2, n=11 reproduces the canonical v15.611 values B_T=6.6077359246533, B_D=3.60083710539664 (and B_A=3.00689881925666) from exactly the same integrator. The r=1 *co-scaled* step construction at any n still gives B_A=0 by v15.608, including this fixed physical X trajectory.

## Gate 86 — new exact leading coefficient and discrete divisor staircase constant

The trianglular staircases approach a large triangle of side Xq. The leading response comes from two physical width-one axis strips, each with leading integrand x^(3/2) sqrt(y)/8 and 0<y<1, so
**B_T(q) ~ X^(5/2) q^(5/2) / 15.**

For the divisor staircase, symmetry in x,y of both the domain and E allows a row decomposition. For each 1≤l≤q, horizontal row y∈[(l−1)/q,l/q] has x∈[0,floor(n_q/l)/q]. The leading integrand is the same x^(3/2) sqrt(y)/8, and the horizontal and vertical defect terms contribute symmetrically. Its integral yields

**B_D(q) ~ X^(5/2) q/15 · S,**

where the dimensionless constant depends on the staircase step convention:
S = Σ_{l≥1} [l^(3/2)−(l−1)^(3/2)]/l^(5/2) ≈ 1.88533127.
The sum converges absolutely (terms asymptotic to 3/(2l²)); dominated convergence applies to the leading row terms as q→∞ and the remaining integral terms are o(q). If the discrete divisor region were silently replaced by smooth y=X/x, this S would not be preserved; it is an arithmetic boundary-staircase correction, NOT a coupling.

Hence
**B_D/B_T ~ S q^(−3/2); B_A/B_T=1−S q^(−3/2)+o(q^(−3/2)).**

The normalized area or probability interpretation does not follow from these unnormalized integrals; their growth is from expanding triangular carrier size at fixed physical product, not physical energy divergence.

## Gate 87 — compare co-scaled step and secant

If instead the transition step co-scales s=u=1/q, then (v15.609) at n=n_q,

**B_T^co=B_D^co=q^(−4) sqrt(n_q)(3n_q²+8n_q+9)/45 ~ X^(5/2)q/15**,
and **B_A^co=0** for all q.

Thus fixed physical step and co-scaled step produce asymptotically different triangular responses, q^(5/2) versus q, and different supports on A.

At the same fixed X, the circle secant fraction decays ~q^-1, while B_D/B_T decays ~q^-3/2; they are consistent with the same refinement trajectory but **are not equal functions or necessarily the same physical observable**. They meet a common power-law comparison B_D/B_T∼ S q^-3/2 without selecting a particular mesh q=2. D(n)/T(n), which is an unweighted raw count ratio, is distinct again and behaves ~(log q)/q².

## Reproducibility / audit

Local deliverable `cone_fixed_product_gates_85_87.zip` includes `reproduce.py` and `REPORT.md`. The Python vectorization integrates the two missing-edge terms with exact elementary power antiderivatives for every column, not a stochastic quadrature. It computes the T/D/A shared-area relations and verifies n=11 q=2 regression values. A finite high-cutoff approximation of S by 2e6 terms gives S≈1.88533127.

**HANDOFF** target external-audit, gravity, sandbox; status open; type fixed physical product q-asymptotic and divisor staircase arithmetic coefficient; independently verify leading X^(5/2)/15, S row series (especially floor(n/l) indexing), co-scaled comparison, and scope. Preserve all certified artifacts; Suzuki lane untouched.

**Next gate:** test analytic expression / summation transforms for S and fixed-product q=2 versus q=1 sensitivity at a physically normalized operator invariant. No physical G prediction without independent dynamics and state measure.
