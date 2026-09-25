# Cone Derivation Ledger v13.792 — Lane A Canonical Parity-Energy Polarization and the First Infinite Schur Parameter

Date: 2026-09-25

Lane: A.

Status: [D] exact parity-energy interpretation of the first Schur parameter; [D] exact infinite target formula from the source-fixed Weyl sign; [N] high-precision numerical evaluation for diagnostic use; [C] scalar necessary condition for finite-to-infinite convergence.

Parents: v13.782, v13.790–791.

## 0. Synchronization

Immediately before this write the live ledger head is v13.791. No collision is present.

## 1. Canonical parity decomposition [D]

Let
\[
v_+:=T_a^{-1}e^x,
\qquad
v_-:=T_a^{-1}e^{-x}=Rv_+.
\]

Define
\[
v_e:=\frac{v_++v_-}{2},
\qquad
v_o:=\frac{v_+-v_-}{2}.
\]

Because \(T_a\) commutes with reflection, the \(T_a\)-energy inner product is reflection invariant, and the even and odd sectors are orthogonal:
\[
\boxed{
\langle v_e,v_o\rangle_{T_a}=0.
}
\tag{1}
\]

Hence
\[
\boxed{
\|v_+\|_{T_a}^2
=
\|v_e\|_{T_a}^2+\|v_o\|_{T_a}^2,
}
\tag{2}
\]
while
\[
\boxed{
\langle v_+,v_-\rangle_{T_a}
=
\|v_e\|_{T_a}^2-\|v_o\|_{T_a}^2.
}
\tag{3}
\]

## 2. First Schur parameter as energy polarization [D]

From v13.791,
\[
\kappa_a
:=
h_a(i)
=
m_a'(i)
=
\frac{
\langle v_+,v_-\rangle_{T_a}
}{
\|v_+\|_{T_a}^2
}.
\]

Substituting (2)–(3),
\[
\boxed{
\kappa_a
=
\frac{
\|v_e\|_{T_a}^2-\|v_o\|_{T_a}^2
}{
\|v_e\|_{T_a}^2+\|v_o\|_{T_a}^2
}.
}
\tag{4}
\]

Thus \(\kappa_a\) is exactly the parity-energy polarization of the canonical deficiency vector.

Equivalently,
\[
\boxed{
\frac{\|v_o\|_{T_a}^2}{\|v_e\|_{T_a}^2}
=
\frac{1-\kappa_a}{1+\kappa_a},
}
\tag{5}
\]
whenever the even component is nonzero.

This gives a direct source-level numerical observable that does not use the raw first-kind endpoint closure.

## 3. Infinite target for the first Schur parameter [D]

From v13.790,
\[
h_\infty(z)
=
\frac{z+i}{z-i}
\frac{R_\xi(z)-1}{R_\xi(z)+1},
\]
where
\[
R_\xi(z)
=
\frac{\xi(3/2)}{\xi'(3/2)}
\frac{\xi'(1/2-iz)}{\xi(1/2-iz)}.
\]

Since
\[
R_\xi(i)=1,
\]
the apparent singularity at \(z=i\) is removable. By l'Hospital/Taylor expansion,
\[
\boxed{
\kappa_\infty
:=
h_\infty(i)
=
i\,R_\xi'(i).
}
\tag{6}
\]

Let
\[
L(s):=\frac{\xi'(s)}{\xi(s)}.
\]
Because
\[
R_\xi(z)
=
\frac{\xi(3/2)}{\xi'(3/2)}
L\!\left(\frac12-iz\right),
\]
\[
R_\xi'(i)
=
-i\frac{\xi(3/2)}{\xi'(3/2)}
L'(3/2).
\]

Therefore
\[
\boxed{
\kappa_\infty
=
\frac{\xi(3/2)}{\xi'(3/2)}
\left[
\frac{\xi''(3/2)}{\xi(3/2)}
-
\left(\frac{\xi'(3/2)}{\xi(3/2)}\right)^2
\right].
}
\tag{7}
\]

Equivalently,
\[
\boxed{
\kappa_\infty
=
\frac{\xi''(3/2)}{\xi'(3/2)}
-
\frac{\xi'(3/2)}{\xi(3/2)}.
}
\tag{8}
\]

This is the exact first Schur parameter predicted by the infinite \(\xi\)-target.

## 4. High-precision diagnostic [N]

Using
\[
\xi(s)
=
\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]
with 80-digit arithmetic gives
\[
\xi(3/2)
\approx
0.5087310387263239580256712366721122388745,
\]
\[
\xi'(3/2)
\approx
0.02347077860480208259883717200825312356882,
\]
\[
\xi''(3/2)
\approx
0.02447856408222121999867660404964298643670.
\]

Therefore
\[
\boxed{
\kappa_\infty
\approx
0.9968019520324009035288967047877578325738.
}
\tag{9}
\]

This lies strictly inside the finite Schur interval \((-1,1)\), providing a nontrivial consistency check on the corrected sign convention.

The corresponding target parity-energy ratio is
\[
\boxed{
\frac{1-\kappa_\infty}{1+\kappa_\infty}
\approx
0.00160158495655717571706007323750804007114.
}
\tag{10}
\]

Thus the candidate infinite canonical deficiency vector is predicted to be strongly even-dominated in the \(T\)-energy polarization at the base point \(z=i\).

## 5. Necessary scalar convergence condition [C]

If
\[
h_a\to h_\infty
\]
locally uniformly on \(\mathbb C_+\), then evaluating at \(z=i\) gives
\[
\boxed{
\kappa_a
=
\frac{
\|v_e\|_{T_a}^2-\|v_o\|_{T_a}^2
}{
\|v_e\|_{T_a}^2+\|v_o\|_{T_a}^2
}
\longrightarrow
\kappa_\infty.
}
\tag{11}
\]

Equivalently,
\[
\boxed{
\frac{\|v_o\|_{T_a}^2}{\|v_e\|_{T_a}^2}
\longrightarrow
0.0016015849565571757\ldots
}
\tag{12}
\]

This gives a very sharp scalar diagnostic for any future source-faithful Galerkin computation of \(T_a^{-1}e^x\).

Failure of (11) is enough to rule out the proposed finite-to-infinite Weyl convergence.

Success of (11) alone is not sufficient; the remaining Schur iterate or another uniqueness-set convergence criterion must still be controlled.

## 6. Result

The first Schur parameter has three exactly equivalent finite meanings:
\[
\boxed{
\kappa_a
=
h_a(i)
=
m_a'(i)
=
\frac{
\|v_e\|_{T_a}^2-\|v_o\|_{T_a}^2
}{
\|v_e\|_{T_a}^2+\|v_o\|_{T_a}^2
}.
}
\]

Its source-fixed infinite target is
\[
\boxed{
\kappa_\infty
=
\frac{\xi''(3/2)}{\xi'(3/2)}
-
\frac{\xi'(3/2)}{\xi(3/2)}
\approx0.9968019520324009.
}
\]

This is the first direct scalar parity-energy target extracted from Suzuki's finite Weyl problem.
