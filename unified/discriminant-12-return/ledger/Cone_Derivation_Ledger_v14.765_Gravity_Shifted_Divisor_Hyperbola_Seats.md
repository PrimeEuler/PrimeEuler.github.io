# Cone Derivation Ledger v14.765 — Half/quarter-seat shifted divisor-hyperbola global counts

**Date:** 2026-10-23 EDT. **Track:** gravity selector / divisor geometry. **Parents:** v13.200, v13.362, v13.691, v13.984, v14.731, v14.764. **Live HEAD pre-write:** \`50c809d4c26f82ee764ba7e0f5d99e4764f7ebdf\`, v14.765 confirmed free. **Research note:** \`research-notes/Gravity_Shifted_Divisor_Hyperbola_Seats.md\`. Suzuki sandbox untouched.

## Exact shifted global count [D]
For a>0 define
\[
D_a(X)=\#\{m,n\ge0:\ (m+a)(n+a)\le X\}.
\]
This has an exact floor-sum formula and Mellin-Dirichlet series
\[
Z_a(s)=\zeta(s,a)^2,\quad\Re s>1.
\]
At a=1 recover the summatory divisor function. At a=1/2 the scaled factors are **odd** (1 mod 2), not 2 mod 4. At a=1/4 they are both 1 mod 4. The quarter series decomposes exactly as
\[
\zeta(s,1/4)=\frac{4^s}{2}\big[(1-2^{-s})\zeta(s)+L(s,\chi_{-4})\big].
\]
This is a genuine mod-4 arithmetic-character difference between shifted hyperbolic global counts.

For fixed a, the standard hyperbola count yields
\[
D_a(X)=X\log X+(-1-2\psi(a))X+O_a(\sqrt X).
\]
For a=1,1/2,1/4 the exact linear constants are respectively \(2\gamma-1\), \(2\gamma+4\log2-1\), \(2\gamma+\pi+6\log2-1\). At X=100 the exact counts are respectively 482,754,1204. This supports the user's proposed geometry-to-global-arithmetic-count direction, with explicit limits: the local 1/4 mixed Walsh coefficient of v13.362 and the gravitational quarter monopole period of v14.731 are not **yet** proved to enforce literal factor-coordinate displacement by 1/4.

## Selector status
The arithmetic transform preserves distinguishable half/quarter offsets and introduces χ_-4 at the quarter seat, but **does not independently select the physical EM/G coupling split ψ**. Need derive the coordinate transport from actual Cone parabolic grids and a physical boundary/action law relating sector couplings and shift. No physical G or alpha prediction, no CFS minimizer, no RH claim. Next gates: shifted parabola/secant Jacobian and mod-12 residue refinements with a rigorous non-circular selector criterion.

**Flags:** \`shifted_divisor_count=EXACT\`; \`quarter_character=chi_minus4\`; \`selector=OPEN\`; \`G_derived=false\`; \`Suzuki_sandbox_reserved=true\`; \`far_tail_touched=false\`.
