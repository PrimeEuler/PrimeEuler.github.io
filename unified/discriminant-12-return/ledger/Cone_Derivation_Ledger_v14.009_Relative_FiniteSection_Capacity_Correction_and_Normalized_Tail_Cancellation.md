# Cone Derivation Ledger v14.009 — Relative Finite-Section Capacity Correction and Normalized Tail Cancellation

**Date:** 2026-10-04
**Track:** Lane A / no-twist Suzuki Xi scalar certification
**Status:** [D] exact finite-section source-energy correction identity; [D] finite capacities are monotone upper bounds; [D] exact parity-ratio correction depends only on the difference of normalized tail energies; [N] LDDD cutoff sweep confirms large common absolute drift but much smaller relative quotient drift; [G] no clean single power law is visible over N=192–4000; [O] certify the normalized parity-tail difference directly.
**Parents:** v14.003, v14.008, v13.997.
**Research commits:** a240b693263d4a922c0e543110cebfaa27046bb6, 5c8b15f15502ad4c7103041abe5c82339d0c9095.
**Collision check:** immediately before this write, live HEAD was 5c8b15f15502ad4c7103041abe5c82339d0c9095 and no v14.009 ledger file was present.

---

## 1. Exact finite-section correction [D]

Let T be a positive self-adjoint source operator and split the Hilbert space as V_N plus Q_N. In block form write

\[
T=
\begin{pmatrix}
A_N&B_N^*\\
B_N&D_N
\end{pmatrix},
\qquad
f=\binom{f_N}{f_Q}.
\]

Assume A_N is invertible and define the Galerkin source solution

\[
x_N=A_N^{-1}f_N,
\qquad
G_N=f_N^*A_N^{-1}f_N.
\]

The remote Galerkin residual is

\[
\boxed{
r_N=f_Q-B_NA_N^{-1}f_N.
}
\]

Define the remote Schur complement

\[
\boxed{
S_{Q,N}=D_N-B_NA_N^{-1}B_N^*.
}
\]

Then the block inverse identity gives

\[
\boxed{
G_\infty
=
f^*T^{-1}f
=
G_N+H_N,
\qquad
H_N:=r_N^*S_{Q,N}^{-1}r_N\ge0.
}
\]

This is also the exact variational defect of the finite Galerkin source solution.

---

## 2. Capacity monotonicity [D]

Let

\[
C_N=G_N^{-1},
\qquad
C_\infty=G_\infty^{-1}.
\]

Then

\[
\boxed{
C_\infty
=
\frac{C_N}{1+C_NH_N}
\le
C_N.
}
\]

Thus every finite-section source capacity is an upper bound on the full capacity.

For nested trial spaces V_N contained in V_M, the capacity variational principle gives

\[
\boxed{
C_N\ge C_M\ge C_\infty.
}
\]

Under the usual form-core density assumption, C_N decreases to C_infinity.

The exact gap formulas are

\[
C_N-C_\infty
=
\frac{C_N^2H_N}{1+C_NH_N}
=
C_NC_\infty H_N.
\]

Therefore the dimensionless quantity controlling the finite-section error is

\[
\boxed{
\eta_N:=C_NH_N
=
\frac{G_\infty-G_N}{G_N}.
}
\]

---

## 3. Exact relative parity correction [D]

Apply the preceding identity separately to even and odd parity:

\[
G_{e,\infty}=G_{e,N}+H_{e,N},
\qquad
G_{o,\infty}=G_{o,N}+H_{o,N}.
\]

Set

\[
q_N
=
\frac{C_{e,N}}{C_{o,N}}
=
\frac{G_{o,N}}{G_{e,N}},
\]

and define

\[
\eta_{e,N}=C_{e,N}H_{e,N},
\qquad
\eta_{o,N}=C_{o,N}H_{o,N}.
\]

Then

\[
\boxed{
\frac{q_\infty}{q_N}
=
\frac{1+\eta_{o,N}}{1+\eta_{e,N}}.
}
\]

Hence

\[
\boxed{
\frac{q_\infty}{q_N}-1
=
\frac{\eta_{o,N}-\eta_{e,N}}{1+\eta_{e,N}}.
}
\]

This is the key relative-tail identity.

The quotient does not require separate sharp estimates for H_e and H_o. It requires a sharp estimate for the difference of the normalized corrections

\[
\boxed{
\eta_{o,N}-\eta_{e,N}.
}
\]

In particular

\[
\left|
\frac{q_\infty}{q_N}-1
\right|
\le
|\eta_{o,N}-\eta_{e,N}|.
\]

For

\[
\kappa(q)=\frac{1-q}{1+q},
\]

the exact difference is

\[
\kappa(q_\infty)-\kappa(q_N)
=
\frac{2(q_N-q_\infty)}{(1+q_\infty)(1+q_N)}.
\]

Thus a relative-tail certificate for q transfers directly to kappa.

---

## 4. Nested-cutoff LDDD sweep [N]

The v14.008 LDDD bracket was replayed at cutoffs

\[
N=192,384,768,1536,3072,4000.
\]

The resulting midpoint capacities are:

### Even

\[
\begin{array}{c|c}
N&C_e(N)\\ \hline
192&8.73167577113433\times10^{-30}\\
384&7.87891869617289\times10^{-30}\\
768&7.81150178500978\times10^{-30}\\
1536&7.70211941132474\times10^{-30}\\
3072&7.60517660046982\times10^{-30}\\
4000&7.57730075636926\times10^{-30}
\end{array}
\]

### Odd

\[
\begin{array}{c|c}
N&C_o(N)\\ \hline
192&2.47817019662688\times10^{-25}\\
384&2.27656590591117\times10^{-25}\\
768&2.25601114835192\times10^{-25}\\
1536&2.22168649473138\times10^{-25}\\
3072&2.19248446398439\times10^{-25}\\
4000&2.18452398382966\times10^{-25}
\end{array}
\]

Both sequences decrease throughout the sweep, as predicted by the exact variational theorem.

---

## 5. No clean absolute power law [N/G]

The empirical doubling exponents extracted from the individual capacities are not stable.

For the even channel they move approximately

\[
3.66,\ -0.70,\ 0.17,
\]

and for the odd channel

\[
3.29,\ -0.74,\ 0.23.
\]

Therefore no single N^{-p} or 1/(N log N) law is promoted from this finite window.

The oscillations are consistent with arithmetic structure surviving in the remote correction.

---

## 6. Relative cancellation in the sweep [N]

The projective quotient and kappa are

\[
\begin{array}{c|c|c}
N&q_N=C_e/C_o&\kappa_N\\ \hline
192&3.52343668042626\times10^{-5}&0.9999295337492252\\
384&3.46087880685337\times10^{-5}&0.9999307848193165\\
768&3.46252800688344\times10^{-5}&0.9999307518375993\\
1536&3.46678949959408\times10^{-5}&0.9999306666136507\\
3072&3.46874822850464\times10^{-5}&0.9999306274417893\\
4000&3.46862786238931\times10^{-5}&0.9999306298489446
\end{array}
\]

From N=768 to 4000, the even capacity falls by roughly 3 percent and the odd capacity by roughly 3.2 percent, while kappa changes by only about

\[
\boxed{1.22\times10^{-7}}.
\]

For the final 3072 to 4000 step, the normalized source-energy increments are approximately

\[
\eta_e\approx3.678862\times10^{-3},
\qquad
\eta_o\approx3.644034\times10^{-3},
\]

so their difference is only

\[
\boxed{
\eta_o-\eta_e
\approx
-3.48\times10^{-5}.
}
\]

This is precisely the cancellation predicted by the relative identity.

The sign still oscillates with cutoff, so this is diagnostic evidence rather than an asymptotic theorem.

---

## 7. Consequence for the proof architecture [I/O]

The remaining remote-tail theorem should not spend its sharpness proving separate tiny intervals for C_e and C_o.

The exact consumer is the normalized difference

\[
\boxed{
\eta_{o,N}-\eta_{e,N}
=
C_{o,N}H_{o,N}-C_{e,N}H_{e,N}.
}
\]

A useful proof may allow large common upper bounds on the individual H_p provided their normalized leading terms are coupled and cancel.

This is the capacity analogue of the common-factor cancellation in the relative bordered determinant.

---

## 8. Result

The finite-section capacities satisfy the exact one-sided theorem

\[
\boxed{
C_{p,\infty}\le C_{p,N},
\qquad
C_{p,N}\downarrow C_{p,\infty}.
}
\]

and the parity quotient obeys

\[
\boxed{
\frac{q_\infty}{q_N}
=
\frac{1+\eta_{o,N}}{1+\eta_{e,N}}.
}
\]

Therefore the nonredundant remote proof target is not H_e and H_o separately but

\[
\boxed{
\eta_{o,N}-\eta_{e,N}.
}
\]

The LDDD sweep shows substantial common-mode cancellation but does not yet certify its infinite-cutoff limit.

---

HANDOFF
target: sandbox
type: task
parent: v14.009
status: open
action: Derive the leading remote asymptotic, or a rigorous enclosure, for the normalized parity-tail difference eta_o,N - eta_e,N in the exact finite-section correction identity; exploit common-mode cancellation before taking absolute values.
deliverable: theorem-or-obstruction
constraints: Keep this distinct from the active v14.008 all-mode scalar-remainder handoff; do not infer a power law from the finite sweep alone; use the known 1/n remote residual/moment machinery and couple the two parity corrections whenever possible.
