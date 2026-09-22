# Cone Derivation Ledger v13.688 — Independent Friedrichs-Galerkin Cross-Ratio Comparison Gate

Date: 2026-09-22

Status: implementation checkpoint. External Audit Round 77 upgraded v13.686 to numerical PASS. This entry ports the same normalization-free observable to the independently assembled Friedrichs-Galerkin discretization. No cross-discretization numerical pass is claimed until execution.

## 0. Live collision/relevance check

Immediately before this write the ledger ends at v13.687. Round 77 is directly relevant:
- v13.681-685 PASS;
- v13.686 implementation independently executed and PASS;
- reflection residuals ~1e-15;
- direct/W/Weyl cross-ratio identities ~1e-16 to 5e-16;
- cocycle ~1e-16;
- additional parameter sets also PASS.

Therefore the finite algebraic identity on the existing Zeeman continuous-kernel carrier is now closed. The next gate is discretization independence.

## 1. New implementation

Added:
\[
\texttt{research-notes/suzuki\_chi4\_friedrichs\_cross\_ratio\_comparison.py}.
\]

It imports the independently assembled endpoint-adapted Friedrichs Galerkin solver
\[
\texttt{suzuki\_chi4\_friedrichs\_independent\_galerkin.py}
\]
and the now-audited Zeeman cross-ratio implementation.

## 2. Friedrichs parity reconstruction

The independent solver produces q_e,q_o on [0,A]. Define
\[
q_+=q_e+q_o,\qquad q_-=q_e-q_o.
\]
By parity, their full-interval Fourier amplitudes are
\[
\boxed{
F_+(z)=2\int_0^A[q_e(x)\cos(zx)+i q_o(x)\sin(zx)]\,dx,
}
\]
\[
\boxed{
F_-(z)=2\int_0^A[q_e(x)\cos(zx)-i q_o(x)\sin(zx)]\,dx.
}
\]

Then exactly as in v13.685,
\[
A(z)=(z-i)F_+(z),\qquad B(z)=(z+i)F_-(z),
\]
\[
W_0=A+B,\qquad W_\pi=A-B,
\]
\[
m=-iW_0/W_\pi,
\]
and
\[
\boxed{
\Delta_{FG}(z,z_*)
=
\frac{A(z)+B(z)}{A(z)-B(z)}
\frac{A(z_*)-B(z_*)}{A(z_*)+B(z_*)}.
}
\]

Thus the observable being compared is algebraically identical; only the finite discretization/solve is independent.

## 3. Comparison protocol

For A=1.5,2,2.5:
1. freeze lambda to the existing finite generalized-spectrum rule used by the Zeeman carrier;
2. assemble independent Friedrichs systems at N=8,12,16,20;
3. report augmented-system condition numbers and solve residuals;
4. verify internally
\[
\Delta_{FG}(z,z_*)=m_{FG}(z)/m_{FG}(z_*);
\]
5. report N-refinement of Delta;
6. at the finest N, compare pointwise against the independently audited Zeeman Delta.

The complex test points and nonreal base point avoid accidental real-axis singular behavior.

## 4. Interpretation rules

A PASS requires two distinct things:
- internal FG stabilization under N/quadrature refinement;
- decreasing or acceptably small FG-vs-Zeeman discrepancy under independent refinement.

The algebraic identity Delta=m/m_* alone is NOT sufficient because it is built into both formulas.

If FG stabilizes to a value materially different from the Zeeman value, that is a discretization/model discrepancy and the gate FAILS CLOSED.

If the Zeeman discrepancy decreases only when its dimension is also increased, the next step is a two-parameter convergence table (N_FG, j_Z).

No statement about a->infinity or beta zeros is authorized at this gate.

## 5. Why this is a stronger test

The two routes use substantially different finite constructions:
- Zeeman: sampled weighted nodal compression on the SU(2) carrier;
- Friedrichs: endpoint-adapted even/odd basis with tensor Gauss-Legendre assembly and nuisance constant/linear constraints.

Agreement of the normalization-free cross-ratio under independent refinement would therefore be evidence that the observable is tied to the underlying finite Suzuki kernel problem rather than to one discretization's raw characteristic normalization.

## 6. Execution status

The implementation is committed, but this entry does not invent execution output. Await independent execution/audit or a successful runtime before assigning PASS/FAIL to the cross-discretization comparison.
