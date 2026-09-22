# Cone Derivation Ledger v13.686 — Chi4 Continuous-Kernel Cross-Ratio Implementation Gate

Date: 2026-09-22

Status: implementation committed; execution/certification still pending. No numerical PASS is claimed in this entry.

## 0. Live collision/relevance check

Immediately before this write the ledger ends at v13.685. No collision or newer audit entry.

## 1. New implementation

Added:
\[
\texttt{research-notes/suzuki_chi4_continuous_kernel_cross_ratio.py}.
\]

It builds directly on the existing
\[
\texttt{suzuki_chi4_zeeman_finite_characteristic.py}
\]
finite continuous-kernel compression.

The script implements the v13.685 formulas:
\[
W_0=(z-i)F_+ +(z+i)F_-,
\]
\[
W_\pi=(z-i)F_+ -(z+i)F_-,
\]
\[
m_a=-iW_0/W_\pi,
\]
and
\[
\Delta_{0/\pi}^{(a)}(z;z_*)
=
\frac{W_0(z)W_\pi(z_*)}{W_\pi(z)W_0(z_*)}.
\]

## 2. One-solve/reflection gate

The existing finite solver independently constructs vp and vm. The new audit additionally forms
\[
v_-^{R}=Rv_+
\]
and reports:
1. relative vector mismatch
\[
\|v_- -Rv_+\|/\|v_-\|;
\]
2. relative residual of Rv_+ in the reduced minus-source equation.

The cross-ratio is then evaluated using the reflected vector, so failure of reflection symmetry cannot silently hide behind the independently solved vm.

## 3. Three independent algebraic paths

For each complex test z and base point z_* the script computes:

A. direct A/B formula
\[
\Delta_{\rm direct}
=
\frac{A+B}{A-B}
\frac{A_*-B_*}{A_*+B_*};
\]

B. characteristic quotient
\[
\Delta_W
=
\frac{W_0(z)W_\pi(z_*)}{W_\pi(z)W_0(z_*)};
\]

C. Weyl ratio
\[
\Delta_m
=
m_a(z)/m_a(z_*).
\]

It reports relative disagreements between A/B vs W and W vs m.

## 4. Base-point cocycle

The script also checks
\[
\boxed{
\Delta(z,z_1)\Delta(z_1,z_2)=\Delta(z,z_2).
}
\]
This is an important regression check because it probes normalization cancellation across multiple base points rather than merely repeating the same two-point algebra.

## 5. Execution status

An attempted local interactive execution did not return a completed numerical run in the available execution environment. Therefore:
\[
\boxed{\text{NO NUMERICAL PASS IS CLAIMED YET.}}
\]

The implementation is committed, but its numerical outputs must be obtained from a successful repository/CI or local run before any finite-a certification is promoted.

This fail-closed status is deliberate and follows the project's audit discipline.

## 6. Next gate

Execute
\[
\texttt{suzuki_chi4_continuous_kernel_cross_ratio.py}
\]
for A=1.5,2,2.5 and record:
- reflection vector error;
- reflected-equation residual;
- direct/W/m identity errors;
- cocycle error.

If these pass near floating-point precision, next refine carrier dimension and/or move the same observable into the independent Friedrichs-Galerkin continuous discretization so the result is not tied to the Zeeman sampled carrier.
