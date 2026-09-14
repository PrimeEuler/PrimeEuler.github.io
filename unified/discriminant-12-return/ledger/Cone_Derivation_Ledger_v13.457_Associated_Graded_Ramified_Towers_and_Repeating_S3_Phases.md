# Cone Derivation Ledger v13.457 — Associated-Graded Ramified Towers and Repeating S3 Phases

Date: 2026-09-14

Status labels: **[D]** exact derived; **[I]** interpretation; **[Audit]** guardrail.

## 0. Synchronization [Audit]

The live ledger was checked before work and again immediately before this write. During the second check, `v13.456` landed on the Suzuki terminal-prime-channel thread, so this arithmetic checkpoint was moved to `v13.457` rather than colliding.

Relevant predecessors are `v13.448` (two ramified local filtrations), `v13.450` (maximal common dihedral quotients), and `v13.454` (intrinsic discriminant-12 S3 quotient).

The Suzuki theorem status has also advanced independently: `v13.451-v13.453` restore the odd bound and full-parity index theorem on independently verified certificate chains. No Suzuki theorem claim is derived here.

## 1. Prime-2 associated graded [D]

Let
\[
K=\mathbf Q(\zeta_{12}),\qquad
\mathfrak P_2=(1+i),\qquad
\kappa_2=\mathcal O_K/\mathfrak P_2\cong\mathbf F_4.
\]
For every `n>=0`,
\[
\boxed{
\operatorname{gr}_{\mathfrak P_2}^n(\mathcal O_K)
=\mathfrak P_2^n/\mathfrak P_2^{n+1}
\cong\mathbf F_4.
}
\]
If `omega=zeta_12 mod P_2`, then multiplication by `zeta_12` acts on every graded piece as multiplication by `omega`:
\[
\boxed{M_{\zeta_{12}}|_{\operatorname{gr}^n}=M_\omega.}
\]

For `r in U(12)`, the Galois action on each graded piece is exactly
\[
\boxed{
\sigma_r(a)=
\begin{cases}
a,&\chi_{-3}(r)=+1,\\
a^2,&\chi_{-3}(r)=-1,
\end{cases}}
\]
after identifying the piece with `F4`.

The uniformizer contributes no extra residue scalar: for `pi_2=1+i`, the automorphisms sending `i -> -i` satisfy
\[
\sigma(\pi_2)=( -i)\pi_2,
\qquad -i\equiv1\pmod{\mathfrak P_2}.
\]
Hence every nonzero graded shell carries
\[
\boxed{
\mathbf F_4^\times\rtimes\operatorname{Gal}(\mathbf F_4/\mathbf F_2)
\cong C_3\rtimes C_2\cong S_3.
}
\]

## 2. Prime-2 torsion depth [D]

Let
\[
w=\zeta_{12}^4
\]
be the order-3 residue/Teichmuller component and define
\[
h=\zeta_{12}w^{-1}=\zeta_{12}^{-3}=-i.
\]
With `pi_2=1+i`,
\[
\boxed{h=1-\pi_2.}
\]
Thus
\[
v_{\mathfrak P_2}(h-1)=1.
\]
Also
\[
h^2=-1,
\qquad
v_{\mathfrak P_2}(h^2-1)=v_{\mathfrak P_2}(-2)=2,
\]
and `h^4=1`. Therefore the principal-unit torsion depth under squaring is
\[
\boxed{1\to2\to\infty.}
\]
This is the graded reason the cyclotomic order stabilizes at 12 after mod 4.

## 3. Prime-3 principal-unit associated graded [D]

Let
\[
F=\mathbf Q(\sqrt3),\qquad
\pi_3=\sqrt3,\qquad
\mathfrak p_3=(\pi_3),
\]
and
\[
U_3^n=1+\mathfrak p_3^n.
\]
Then for every `n>=1`,
\[
\boxed{U_3^n/U_3^{n+1}\cong(\mathbf F_3,+).}
\]
Quadratic conjugation sends `pi_3 -> -pi_3`, hence on the nth graded piece
\[
\boxed{a\mapsto(-1)^n a.}
\]
Thus even grades have trivial conjugation and odd grades have inversion.

## 4. Pell generator visits exactly the odd grades [D]

Let
\[
\lambda=2+\sqrt3,
\qquad
\mu=-\lambda.
\]
The valuation law from `v13.448` is
\[
\boxed{v_{\pi_3}(\mu^{3^r}-1)=1+2r.}
\]
Hence
\[
\mu^{3^r}\in U_3^{1+2r}\setminus U_3^{2+2r}.
\]
So the distinguished Pell phase lands successively in
\[
\boxed{1,3,5,7,\ldots}
\]
and in each active quotient its class generates the additive `C3`. Since all active grades are odd, conjugation acts by inversion. Therefore every Pell-active grade carries
\[
\boxed{C_3\rtimes C_2\cong S_3.}
\]

## 5. Repeating graded S3 pattern [D/I]

The exact comparison is
\[
\boxed{
\text{prime 2: the same }S_3\text{ on every nonzero graded shell},
}
\]
while
\[
\boxed{
\text{prime 3: the same }S_3\text{ on every odd Pell-active graded shell}.
}
\]

Thus the common `S3` from `v13.439`, `v13.450`, and `v13.454` is not merely a terminal quotient. It recurs as an associated-graded local phase.

## 6. Why the deep towers still diverge [D/I]

The difference is inter-grade dynamics, not the phase group on an active grade.

- At prime 2, the distinguished principal-unit component is finite 4-torsion and has depth chain `1 -> 2 -> infinity`.
- At prime 3, the normalized Pell principal unit is non-torsion and repeated cubing drives it through the unbounded odd sequence `1 -> 3 -> 5 -> 7 -> ...`.

Therefore the stable 2-adic order-12 clock and the growing `2*3^k` Pell clock coexist with the same recurring local `S3` phase.

## 7. Extension-data interpretation [D/I]

Every individual prime-2 associated-graded layer sees only the `chi_-3` identity/Frobenius quotient. Hence the full `V4` Galois action recovered modulo 4 is not contained in any single graded piece. It is extension data linking successive ramified layers.

This sharpens the `v13.446-v13.447` conclusion:
\[
\boxed{
\text{mod-2 loses the extra character bit on each layer, while mod-4 recovers it in the extension between layers.}
}
\]

## 8. Guardrails [Audit]

- The two graded towers are over different residue fields and are not identified as rings.
- The repeated `S3` actions are isomorphic local phase actions, not one global operator.
- The full mod-4 `V4` recovery is extension data, not extra character information inside a single `F4` graded quotient.
- Even prime-3 principal-unit grades exist; they are simply not visited by the distinguished sequence `mu^(3^r)`.
- No Suzuki terminal direction is identified with either graded tower by this calculation.

---

**Checkpoint conclusion.** The discriminant-12 ramified towers share a repeated associated-graded `S3` phase. The prime-2 cyclotomic tower realizes it on every nonzero `F4` graded shell, while the prime-3 Pell tower realizes it on every odd principal-unit grade reached by successive cubing. Their deep arithmetic difference lies in inter-grade motion: finite torsion termination at 2 versus unbounded principal-unit penetration at 3.
