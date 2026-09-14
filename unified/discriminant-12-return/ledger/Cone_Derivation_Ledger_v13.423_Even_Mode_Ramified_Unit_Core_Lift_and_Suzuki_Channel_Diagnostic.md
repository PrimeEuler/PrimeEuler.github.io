# Cone Derivation Ledger v13.423 — Even-Mode Ramified/Unit-Core Lift and Suzuki Channel Diagnostic

Date: 2026-09-14

Status labels: **[D]** exact derived; **[N]** numerical midpoint diagnostic; **[Audit]** guardrail.

## 0. Synchronization

This checkpoint was assigned after checking the live ledger through v13.422.  It records a side observation motivated by the mod-12 quadratic-residue image {0,1,4,9} and tests whether even Suzuki Fourier modes can retain the unit-class labels {1,5,7,11} after removing ramified 2- and 3-parts.

The active positivity target remains the odd-sector finite-high certificate on F={22,24,...,4000}.  Nothing below promotes a new symmetry of the Suzuki operator.

## 1. Quadratic-residue layer records ramification type [D]

For any integer n,

\[
n^2\pmod{12}\in\{0,1,4,9\}.
\]

More precisely,

\[
\boxed{
\begin{array}{c|c}
n^2\bmod12 & \text{divisibility type of }n\\
\hline
1&(n,6)=1\\
4&2\mid n,\ 3\nmid n\\
9&3\mid n,\ 2\nmid n\\
0&6\mid n
\end{array}}
\]

Thus the quadratic-residue image does not distinguish the four unit classes, but it does exactly record the coarse ramified 2/3 layer.

## 2. Unit-core lift [D]

Write uniquely

\[
n=2^{a}3^{b}u,
\qquad (u,6)=1.
\]

Then

\[
\boxed{u\bmod12\in\{1,5,7,11\}.}
\]

Hence every nonzero integer carries two compatible pieces of mod-12 data:

\[
\boxed{
\text{ramification data }(v_2(n),v_3(n))
\quad+\quad
\text{unit-core label }u\bmod12.
}
\]

The direct Dirichlet characters modulo 12 vanish on ramified n, but the unit core recovers a V4 label after the ramified factors are stripped.

**[Audit]** The lifted function \(n\mapsto\chi(u(n))\) is not itself a Dirichlet character modulo 12, so this does not create an automatic character decomposition of an operator indexed by n.

## 3. Exact mod-24 lift for the first even stratum [D]

For even n with

\[
v_2(n)=1,
\qquad 3\nmid n,
\]

write n=2u with u coprime to 6.  Then the four unit classes are recovered exactly by n modulo 24:

\[
\boxed{
\begin{array}{c|cccc}
n\bmod24&2&10&14&22\\
\hline
u=n/2\bmod12&1&5&7&11
\end{array}}
\]

Thus mod 24 is the natural first lift that retains all four V4 labels on this even stratum.  In the finite-high range 22<=n<=4000, each of the four residues 2,10,14,22 mod24 occurs exactly 166 times in this stratum.

## 4. Pole-free Suzuki finite-high diagnostic [N]

Using the source-faithful midpoint pole-free matrix

\[
B=A_{FF}^{(0)}-0.53I,
\qquad F=\{22,24,\ldots,4000\},
\]

classify every mode by its unit core

\[
u(n)=\frac{n}{2^{v_2(n)}3^{v_3(n)}}\pmod{12}.
\]

The class counts are

\[
\boxed{
\#1=518,\quad \#5=499,\quad \#7=492,\quad \#11=481.
}
\]

The full shifted minimum is

\[
\lambda_{\min}(B)\approx0.002842383786.
\]

However, the four diagonal unit-core blocks are individually much more positive:

\[
\boxed{
\begin{array}{c|c}
u\bmod12 & \lambda_{\min}(B_{uu})\\
\hline
1&0.7707269294\\
5&0.2581854461\\
7&1.3469333050\\
11&0.3959374032
\end{array}}
\]

Therefore the near-loss of positivity is not internal to any one recovered unit-core channel.  It is created by inter-channel coupling.

## 5. Lowest-vector distribution [N]

For a normalized lowest eigenvector of B, the squared mass in the four unit-core classes is approximately

\[
\boxed{
\begin{array}{c|c}
u\bmod12 & \|P_u v_{\min}\|^2\\
\hline
1&0.0670181\\
5&0.5251509\\
7&0.1133531\\
11&0.2944779
\end{array}}
\]

Thus the dangerous direction is strongly concentrated in the 5 and 11 unit-core labels, with much less weight in 1 and 7.

This is a numerical structural fact about the current midpoint block, not an exact invariant.

## 6. Why simple block Gershgorin does not close the proof [N/Audit]

The pairwise off-block operator norms are order one:

\[
\begin{array}{c|c}
(u,v)&\|B_{uv}\|_2\\
\hline
(1,5)&1.37037\\
(1,7)&1.15652\\
(1,11)&1.13428\\
(5,7)&1.29075\\
(5,11)&1.24293\\
(7,11)&1.31569
\end{array}
\]

Therefore a crude four-block Gershgorin/triangle inequality loses far too much and cannot certify the 0.00284 global margin.

A compression onto only the four individual block ground states also has minimum about 0.2025, so the nearly critical global direction is not explained by coupling just those four ground states.  It is a more distributed inter-channel combination.

## 7. Relation to v13.420-v13.422 [D/I]

The new exact shell-displacement hierarchy establishes genuine chi12 cancellation identities and V4 projectors on their proper arithmetic/cyclotomic carriers.  The present unit-core lift complements those results on ramified integer indices:

\[
\boxed{
\text{QR class} \;\text{records ramification},
\qquad
\text{unit core} \;\text{recovers the V4 label}.
}
\]

This explains how even integer modes can retain unit-class information without contradicting the fact that the ordinary mod-12 Dirichlet characters vanish on even n.

**[Audit]** No exact intertwining between the Suzuki matrix and the cyclotomic V4 projectors has been established.  Any positivity gain must come from a proved structured coupling estimate, not from imposing character orthogonality by hand.

## 8. Positivity-certificate consequence [Audit]

The diagnostic does not replace the direct outward finite-high certificate.  Its useful conclusion is narrower:

\[
\boxed{
\text{all four recovered unit-core diagonal blocks are safely positive; the small global margin is an inter-channel phenomenon.}
}
\]

This suggests a possible future structured Schur/low-rank treatment of the inter-channel coupling, especially the 5/11-dominated dangerous direction, but the current certification path remains the parity-correct quadrature-free nominal generator plus outward source/arithmetic bounds.

## 9. Even-mode archimedean recurrence [D]

For even Fourier mode n and b=n*pi/2, sin(2b)=0 and cos(2b)=+1.  Hence

\[
I_p=\int_0^2 t^p\cos(bt)\,dt,
\qquad
J_p=\int_0^2 t^p\sin(bt)\,dt
\]

obey

\[
\boxed{I_0=J_0=0,}
\]

and for p>=1,

\[
\boxed{
I_p=-\frac{p}{b}J_{p-1},
\qquad
J_p=-\frac{2^p}{b}+\frac{p}{b}I_{p-1}.
}
\]

This is the parity-correct analogue of the archived odd-mode recurrence and allows the certified polynomial h_N to generate the even-index archimedean scalar sequence without adaptive quadrature.

The corresponding helper is stored in

`research-notes/suzuki_arch_polynomial_recurrence_even_modes.py`.

The midpoint structural diagnostic is stored in

`research-notes/suzuki_even_mode_unit_core_mod24_diagnostic.py`.

---

**Checkpoint conclusion.** The user's QR observation is mathematically productive: {0,1,4,9} supplies the ramified layer, while stripping powers of 2 and 3 recovers the unit-core V4 label; on the first even stratum this is exactly a mod-24 lift.  In the live odd-Suzuki finite-high block, every recovered unit-core diagonal block is comfortably positive and the small global gap comes entirely from inter-channel coupling.  This is genuine structural information, but not yet a sharper certified positivity bound.