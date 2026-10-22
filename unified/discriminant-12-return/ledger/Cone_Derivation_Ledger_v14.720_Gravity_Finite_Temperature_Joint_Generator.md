# Cone Derivation Ledger v14.720 — Gravity finite-temperature joint Maxwellian generator and escape-flux gate

**Date:** 2026-10-22 EDT. **Lane:** independent gravity research. **Parents:** v14.714–719, EFT v3.4.
**Live HEAD/collision:** before deposit verified \`master\` at \`581c606e910f261ba4047f2fd3ae51af2848b479\`; v14.720 unused. No far-tail, papers, or prior audited certificate touched.
**Files deposited:** \`research-notes/gravity_finite_temp_joint_generator.py\` and \`research-notes/Gravity_Finite_Temperature_Joint_Generator.md\`.

## Derived gate [D]

Starting with the true *3D* Rosenbluth half-covariance tensor \(D=D_\parallel\hat v\hat v^T+D_\perp(I-\hat v\hat v^T)\), drift \(-A\hat v\), and Kepler \(h=v^2/2-\mu/r,\ L=|\mathbf r\times\mathbf v|\), the exact local generator of \((h,L)\) has
\[
b_h=-vA+D_\parallel+2D_\perp,\quad b_L=-AL/v+D_\perp r^2/L,
\]
\[
a_{hh}=2D_\parallel v^2,\quad a_{hL}=2D_\parallel L,\quad
a_{LL}=2[D_\perp r^2+(D_\parallel-D_\perp)L^2/v^2].
\]
These are directly transported through \(T=-\mu/(2h)\), \(z=e^2=1+2hL^2/\mu^2\), including all Hessian/Itô terms, and Kepler-averaged with exact time measure \((1-e\cos E)dE/(2\pi)\). The resulting five drift/diffusion coefficients comprise an explicit, reproducible finite-temperature joint generator.

The analytically simplified mixed coefficient agrees with sandbox v14.716 and independent audit v14.718:
\[
\boxed{\bar a_{Tz}=\frac{8T^3(1-z)}{\mu^2}
\left\langle D_\parallel(v)\left(v^2-\frac{\mu}{T}\right)\right\rangle_{\rm Kep}.}
\]
The hot constant-\(D_\parallel\) limit vanishes by virial averaging; the genuine Maxwellian finite-temperature coefficient is generally nonzero, breaking the specific operational-clock independence found in v14.714. This does not by itself establish a new stationary law.

## Forward equation and honest open boundary

The formal orbit-averaged density obeys \(\partial_t p=-\partial_i(\bar b_i p)+\frac12\partial_i\partial_j(\bar a_{ij}p)\), with \(i,j=T,z\). For surviving mass \(S=\int p\), the normalized survivor density is \(p/S\) and includes the survival-selection correction \(-(\dot S/S)(p/S)\). Escape at \(h=0^-\) (\(T\to\infty\)) cannot be fully modeled by choosing an arbitrary local diffusion boundary in place of the EFT's finite Rutherford jump/killing operator. Hence no finite-\(\Theta\) QSD, numerical survivor distribution, or new gravity coupling claimed.

## Next gate / handoffs

**External audit:** independently derive local \(b_L,a_{LL}\) in three dimensions, check all coordinate Hessians and mixed drift transformation, and verify time-average and current boundary statements.

**Sandbox:** implement finite-temperature averaged joint forward solver including explicitly distinguished bound-preserving vs killed BPS/hard-jump terms; calculate survival-weighted shape and test convergence. If no certified jump kernel/numerical boundary available, return that obstruction rather than a fabricated QSD.

**Flags:** \`G_derived=false\`; \`new_Xi_signal=false\`; \`far_tail_touched=false\`; \`papers_modified=false\`; \`finite_temp_joint_generator=FORMAL_EXACT_AT_GIVEN_EFT_ORDER\`; \`physical_QSD=OPEN\`; \`hard_jump_boundary=OPEN\`.
