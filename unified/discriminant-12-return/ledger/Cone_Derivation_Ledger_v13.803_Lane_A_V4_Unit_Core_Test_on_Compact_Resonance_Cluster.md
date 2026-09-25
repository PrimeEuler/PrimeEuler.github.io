# Cone Derivation Ledger v13.803 — Lane A V4 / Unit-Core Test on the Compact Resonance Cluster

Date: 2026-09-25

Lane: A with a controlled cross-check against the discriminant-12 / \(U(12)\cong V_4\) character machinery.

Status: [D] exact unit-core character operators defined; [N] \(N=96\) resonance/class diagnostics; [N] no exact or near commuting V4 symmetry found; [I] finite class-average rank-4 Schur organization remains potentially useful for certification; [G] cone-side \(U(24)\) double-cover non-bridge from v13.502–503 retained.

Parents: v13.423, v13.430, v13.433, v13.502–503, v13.801–802.

Research artifact:

- research-notes/suzuki_form_core_v4_unit_core_resonance_diagnostic.py
- commits d431f1a15ee75d8795c023c8c1b56a6ff8458837 and 0b9c67d5a58873e88c6196cc4375934c36896442.

## 0. Audit cleanup completed first

External Audit Round 102 (v13.802) found:

1. v13.798 §4 overstated the Feshbach/full-spectral relative agreement by about nine orders of magnitude;
2. v13.798–800 had systematic LaTeX escape corruption.

These were repaired before the present cross-lane test:

- f63e5f6a066290883497deb63717e1d3689eb75f — corrected v13.798 numerical figure and restored LaTeX;
- c4b553a0fdf0141818f12b9316e5d23a8e7b0cd4 — restored v13.799 LaTeX;
- 089eb93f85c2c178b63ca752f9aa4fa6d9412a0c — restored v13.800 LaTeX.

The corrected v13.798 agreement figures are
\[
9.059467616\times10^{-56}\quad\text{(even-v)},
\]
\[
9.145195157\times10^{-58}\quad\text{(odd-v)}.
\]

No v13.799–801 mathematical conclusion changes.

## 1. Exact unit-core labels and character-sign operators [D]

For every positive Dirichlet mode \(n\), define
\[
u(n)
=
\frac{n}{2^{v_2(n)}3^{v_3(n)}}\pmod{12}.
\]

Then
\[
u(n)\in U(12)=\{1,5,7,11\}\cong V_4.
\]

Use the four character rows
\[
\mathbf 1=(1,1,1,1),
\]
\[
\chi_{-4}=(1,1,-1,-1),
\]
\[
\chi_{-3}=(1,-1,1,-1),
\]
\[
\chi_{12}=(1,-1,-1,1),
\]
in class order \((1,5,7,11)\).

For each nontrivial character define the exact diagonal sign operator
\[
(M_\chi c)_n
=
\chi(u(n))c_n.
\]

The three \(M_\chi\) commute, square to identity, and generate an exact diagonal \(V_4\) representation on the coefficient space.

This gives a precise operator-level test of the tempting hypothesis
\[
\text{four Lane-A resonances}
\stackrel{?}{=}
\text{four }U(12)\text{ character channels}.
\]

## 2. The cone-side \(U(24)\) construction is not the bridge [G]

v13.502–503 already proved that the cone-side \(U(24)\), \(U(48)\), … unit-group constructions do not coincide with the Suzuki even-stratum residue carriers.

The Suzuki unit-core label is obtained by stripping the \(2\)- and \(3\)-adic factors first and then reading
\[
u(n)\bmod12.
\]

Therefore the only discriminant-12 structure tested here is the intrinsic Suzuki-side unit-core \(V_4\) label and its character table. No cone \(U(24)\) sheet action is imported.

## 3. Four-resonance subspace is not V4-invariant [N]

Use the v13.801 smooth-bulk relative resonance construction at \(N=96\), with the first two parity modes retained as the low core.

Let \(\mathcal R_4\) be the coefficient-space span of the four tail resonances closest to \(-1\).

For each character, measure
\[
\left\|
(I-P_{\mathcal R_4})M_\chi P_{\mathcal R_4}
\right\|_2.
\]

At \(N=96\):

even-v:
\[
\begin{array}{c|ccc}
\chi & \chi_{-4} & \chi_{-3} & \chi_{12}\\
\hline
\text{leakage} &
0.5651 & 0.5756 & 0.5829
\end{array}
\]

odd-v:
\[
\begin{array}{c|ccc}
\chi & \chi_{-4} & \chi_{-3} & \chi_{12}\\
\hline
\text{leakage} &
0.8549 & 0.9999 & 0.9999
\end{array}
\]

Thus the four-resonance subspace is not even approximately invariant under the character-sign representation, especially in the odd-v sector.

Therefore
\[
\boxed{
\text{the four resonances are not the four V4 characters.}
}
\]

The numerical coincidence \(4=|V_4|\) must not be promoted into a representation-theoretic identification.

## 4. The source-faithful matrices do not commute with the character signs [N]

On the \(N=96\) tail, direct coefficient-space commutator diagnostics give

even-v:
\[
\frac{\|[A,M_\chi]\|_2}{\|A\|_2}
\approx
0.47,\ 0.55,\ 0.50,
\]
\[
\frac{\|[B_{\rm sm},M_\chi]\|_2}{\|B_{\rm sm}\|_2}
\approx
0.211,\ 0.213,\ 0.211;
\]

odd-v:
\[
\frac{\|[A,M_\chi]\|_2}{\|A\|_2}
\approx
0.63,\ 0.60,\ 0.52,
\]
\[
\frac{\|[B_{\rm sm},M_\chi]\|_2}{\|B_{\rm sm}\|_2}
\approx
0.175,\ 0.188,\ 0.195.
\]

Hence neither the full form nor the smooth bulk carries an exact or numerically small \(V_4\) commutator at this cutoff.

No character block-diagonalization of the relative operator is available.

## 5. The four class-average directions are nevertheless safe [N]

Let \(U\) contain the four normalized indicator vectors of the unit-core classes on the finite \(N=96\) tail.

The generalized eigenvalues of the class-average compression
\[
U^TAU\,x
=
\delta\,U^TB_{\rm sm}U\,x
\]
are:

even-v:
\[
\boxed{
0.83546,\ 0.85425,\ 1.05730,\ 1.19667
}
\]

odd-v:
\[
\boxed{
0.82521,\ 0.93815,\ 0.99429,\ 1.10584.
}
\]

The relative resonance target is \(\delta=0\). Therefore this finite four-dimensional class-average sector is far from resonance.

For the proposed fifth-exclusion endpoint radius \(\rho=0.10\), the compressed pencil
\[
U^T(A-\rho B_{\rm sm})U
\]
still has generalized margin at least approximately
\[
0.735\quad\text{(even-v)},
\]
\[
0.725\quad\text{(odd-v)}.
\]

Thus the class-average block is an excellent candidate for a rigorously positive finite block inside the endpoint-inertia certificate.

## 6. The resonances live predominantly in within-class fluctuations [N]

Let \(P_U=UU^T\). For the four-dimensional resonance subspace, the singular values of
\[
U^TQ_4
\]
are

even-v:
\[
0.4660,\ 0.3001,\ 0.2661,\ 0.0110,
\]

odd-v:
\[
0.4486,\ 0.2012,\ 0.1453,\ 0.0503.
\]

Therefore
\[
\operatorname{tr}(P_{\mathcal R_4}P_U)
\approx0.3781
\]
in even-v and
\[
\operatorname{tr}(P_{\mathcal R_4}P_U)
\approx0.2654
\]
in odd-v.

Since \(\dim\mathcal R_4=4\), only about
\[
\boxed{9.45\%}
\]
of the total even-v resonance-subspace squared norm and
\[
\boxed{6.63\%}
\]
of the total odd-v resonance-subspace squared norm lies in the four class-average directions.

Thus the present resonance cluster is overwhelmingly a within-class fluctuation phenomenon.

This is strongly consistent with the older v13.433 conclusion:
\[
\boxed{
\text{safe class averages}
\longrightarrow
\text{rank-4 Schur feedback}
\longrightarrow
\text{dangerous fluctuation sector}.
}
\]

## 7. Hadamard character basis remains diagnostic, not exact [N]

Whiten the finite class-average compression by
\[
B_c=U^TB_{\rm sm}U
\]
and form
\[
J_c=B_c^{-1/2}U^TAU B_c^{-1/2}.
\]

Conjugating by the normalized Hadamard character table \(H_4/2\) gives a moderately structured but not nearly exact diagonal form.

At \(N=96\), the relative off-diagonal Frobenius fractions are approximately
\[
0.139\quad\text{(even-v)},
\]
\[
0.095\quad\text{(odd-v)}.
\]

These are much larger than the exceptionally sharp near-circulant balanced-stratum diagnostic of v13.430.

Therefore the character basis may be a useful coordinate system for the \(4\times4\) finite solve, but it cannot be treated as an exact decomposition.

## 8. Certification consequence [I]

The V4 machinery has a real but limited use in the proposed resonance certificate.

Do **not** use it to identify the four resonances.

Instead, after the infinite remote tail has already been controlled analytically, use the finite unit-core class-average projector \(P_U\) inside the remaining finite endpoint pencil
\[
F_\rho^\pm=A\pm\rho B_{\rm sm}.
\]

If
\[
P_UF_\rho^\pm P_U\succ0,
\]
then exact Schur complementation gives
\[
\operatorname{ind}_{-}(F_\rho^\pm)
=
\operatorname{ind}_{-}
\left(
Q_UF_\rho^\pm Q_U
-
Q_UF_\rho^\pm P_U
(P_UF_\rho^\pm P_U)^{-1}
P_UF_\rho^\pm Q_U
\right).
\]

The correction has rank at most four.

This reproduces the useful v13.433 architecture:
\[
\boxed{
\text{safe four-class block}
+
\text{explicit rank-4 feedback into fluctuations}.
}
\]

Advantages for the new certificate:

1. only four right-hand sides are needed to eliminate the class-average block;
2. the \(4\times4\) block has a large numerical positivity margin at \(\rho=0.10\);
3. its Hadamard character basis can be used as a diagnostic/preconditioning coordinate system;
4. the dangerous resonance subspace already lies mostly in the fluctuation complement.

## 9. Important infinite-dimensional guardrail [G]

The normalized constant-on-class indicators over an infinite arithmetic class are not elements of \(\ell^2\).

Therefore the rank-4 class-average projector is inherently a **finite-window / finite-buffer device**. It must not replace the v13.801 compactness argument or the analytic remote-tail certificate.

The correct order is:

\[
\boxed{
\text{analytic remote tail}
\to
\text{finite effective block}
\to
\text{V4/unit-core rank-4 class-average elimination}
\to
\text{resonance/inertia certificate}.
}
\]

## Result

The discriminant-12 / \(V_4\) concepts have genuine value here, but not in the initially tempting form.

\[
\boxed{
\textbf{No: the four Lane-A resonances are not the four }U(12)\textbf{ character channels.}
}
\]

\[
\boxed{
\textbf{Yes: the four unit-core class averages form a safe finite block whose exact Schur feedback has rank at most four and is well aligned with the fluctuation-dominated resonance problem.}
}
\]

This is a potentially useful certificate simplification and should be tested inside the endpoint-inertia architecture before building a larger generic finite Schur solve.
