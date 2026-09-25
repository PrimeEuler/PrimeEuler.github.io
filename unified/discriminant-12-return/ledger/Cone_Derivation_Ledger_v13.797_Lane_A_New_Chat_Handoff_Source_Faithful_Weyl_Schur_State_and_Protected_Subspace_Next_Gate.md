# Cone Derivation Ledger v13.797 — Lane A New-Chat Handoff Checkpoint: Source-Faithful Weyl/Schur State, Corrections, Numerical Bottleneck, and Takeover Instructions

Date: 2026-09-25

Lane: A.

Status: [H] handoff checkpoint for a fresh chat; [P] synchronized to External Audit Round 101; [G] preserves all active corrections/guardrails; [C] gives the exact next computational/analytic gates.

Parents: v13.784–796, especially v13.790–796.

## 0. START HERE — instructions for the next chat

Before doing any mathematics:

1. Check the live ledger head and newest audit.
2. Read this handoff entry and the current audit immediately preceding it.
3. If any v13.798+ audit/checkpoint exists, read it before continuing.
4. Do not resurrect superseded endpoint/ordinary-derivative assumptions or the old raw-Fredholm Schur closure.
5. Continue Lane A from the source-level \(T_a^{-1}\) / Schur-function route described below.
6. Before any future ledger write, recheck the live head for collisions and relevant parallel-lane updates.

The current live head immediately before this write is:

- v13.796 — External Audit Round 101.

Round 101 PASSes v13.784–795 in full and independently reproduces the key numerical claims.

---

## 1. Current source-faithful operator hierarchy [D]

The three operator levels must remain separated.

### Level I — original deficiency solve

For
\[
T_{a,\lambda}:=A_a-\lambda I,\qquad \lambda<\lambda_a,
\]
Suzuki's actual deficiency vectors satisfy
\[
\boxed{
T_{a,\lambda}v_\pm=C_\pm e^{\pm x}.
}
\]

With unit source normalization,
\[
\boxed{
v_{a,+i}^{(\lambda)}=T_{a,\lambda}^{-1}e^x,
\qquad
v_{a,-i}^{(\lambda)}=T_{a,\lambda}^{-1}e^{-x}.
}
\]

Reflection commutes with \(T_{a,\lambda}\), so
\[
\boxed{
v_{a,-i}^{(\lambda)}=Rv_{a,+i}^{(\lambda)}.
}
\]

### Level II — abstract transported/projected solve

Suzuki's derivative map extends by completion to
\[
\bar D:\mathcal H(T_a)\overset{\sim}{\longrightarrow}\mathcal H(S_a),
\]
with
\[
\boxed{
S_a=\bar DT_a\bar D^{-1}.
}
\]

Thus
\[
\boxed{
S_a(\bar Dv_\pm)=C_\pm\bar D e_{\pm i}.
}
\]

This identity is exact.

### Level III — raw first-kind kernel representation

Suzuki's raw kernel equation is
\[
\boxed{
\int_{-a}^{a}k(x,y)(-v_\pm(y))\,dy
=
C_\pm e^{\pm x}+A_\pm x+B_\pm.
}
\]

This raw Fredholm operator is not literally \(S_a\). The affine terms belong to this primitive reconstruction level.

---

## 2. Critical correction: no endpoint reconstruction for actual deficiency vectors [R/G]

v13.784 corrected v13.779 §4.

The actual deficiency vectors live in the adjoint/domain completion; one may not assume
\[
v_\pm\in H_0^1(-a,a).
\]

Therefore do not impose, unless separately proved,
\[
v_\pm(\pm a)=0,
\]
\[
v(x)=-i\int_{-a}^{x}u(t)\,dt,
\]
or literal \(L^2\) zero-mean derivative conditions on
\[
u=\bar Dv.
\]

Most importantly,
\[
\boxed{
\bar Dv_\pm
\text{ must not be replaced by the ordinary derivative }iv_\pm'
}
\]
without an independent regularity theorem.

On the core,
\[
DR=-RD,
\]
and this extends abstractly:
\[
\boxed{
\bar DR=-R\bar D.
}
\]

That parity reversal survives; endpoint calculus does not.

---

## 3. Exact \(T_a^{-1}\) parity decomposition [D]

For unit source normalization,
\[
e^x=\cosh x+\sinh x.
\]

Because \(T_a^{-1}\) preserves parity,
\[
\boxed{
w_{a,e}:=(T_a^{(+)})^{-1}\cosh x,
}
\]
\[
\boxed{
w_{a,o}:=(T_a^{(-)})^{-1}\sinh x.
}
\]

Then
\[
\boxed{
v_{a,+i}=w_{a,e}+w_{a,o},
\qquad
v_{a,-i}=w_{a,e}-w_{a,o}.
}
\]

Define
\[
E_a(z):=\widehat{w_{a,e}}(z),
\qquad
O_a(z):=\widehat{w_{a,o}}(z).
\]

Parity gives
\[
E_a(-z)=E_a(z),
\qquad
O_a(-z)=-O_a(z).
\]

---

## 4. Exact finite Weyl reduction [D]

For a common deficiency normalization \(C_a\),
\[
\widehat v_+=C_a(E_a+O_a),
\qquad
\widehat v_-=C_a(E_a-O_a).
\]

Suzuki's characteristic yields
\[
\boxed{
W_0(a;z)=2C_a[zE_a(z)-iO_a(z)],
}
\]
\[
\boxed{
W_\pi(a;z)=2C_a[-iE_a(z)+zO_a(z)].
}
\]

Using the audited convention
\[
\boxed{
\frac{W_0}{W_\pi}=i\,m_a,
}
\]
the finite Weyl function is
\[
\boxed{
m_a(z)
=
-i\,
\frac{zE_a(z)-iO_a(z)}
{-iE_a(z)+zO_a(z)}.
}
\]

Where \(E_a\neq0\), define
\[
\eta_a(z):=\frac{O_a(z)}{E_a(z)}.
\]

Then
\[
\boxed{
m_a(z)
=
-i\frac{z-i\eta_a(z)}
{-i+z\eta_a(z)}.
}
\]

This is the valid parity/Weyl reduction. It uses \(T_a^{-1}\), not endpoint derivatives.

---

## 5. One-function compression [D]

The current minimal source-level observable is
\[
\boxed{
F_a(z)
:=
\widehat{T_a^{-1}e^x}(z).
}
\]

Reflection gives
\[
\boxed{
\widehat{T_a^{-1}e^{-x}}(z)=F_a(-z).
}
\]

Hence
\[
F_a(z)=E_a(z)+O_a(z),
\qquad
F_a(-z)=E_a(z)-O_a(z).
\]

Define the reflection quotient
\[
\boxed{
\rho_a(z):=\frac{F_a(-z)}{F_a(z)}.
}
\]

Then
\[
\boxed{
m_a(z)
=
-i
\frac{(z-i)+(z+i)\rho_a(z)}
{(z-i)-(z+i)\rho_a(z)}.
}
\]

Conversely,
\[
\boxed{
\rho_a(z)
=
\frac{z-i}{z+i}
\frac{i\,m_a(z)-1}
{i\,m_a(z)+1}.
}
\]

No primitive affine constants or absolute deficiency normalization are needed.

---

## 6. Intrinsic Schur/Hermite–Biehler observable [D]

Because \(m_a\) is Nevanlinna,
\[
s_a(z):=\frac{m_a(z)-i}{m_a(z)+i}
\]
maps \(\mathbb C_+\) to \(\mathbb D\).

The one-function formula is
\[
\boxed{
s_a(z)
=
\frac{z-i}{z+i}
\frac{F_a(z)}{F_a(-z)}.
}
\]

The canonical calibration is
\[
\boxed{
m_a(i)=i,\qquad s_a(i)=0.
}
\]

Factor the fixed half-plane Blaschke zero
\[
\phi_i(z):=\frac{z-i}{z+i}.
\]

Define
\[
\boxed{
h_a(z)
:=
\frac{s_a(z)}{\phi_i(z)}
=
\frac{F_a(z)}{F_a(-z)}.
}
\]

Then \(h_a\) extends holomorphically through \(z=i\) and
\[
\boxed{
|h_a(z)|\le1\qquad(z\in\mathbb C_+).
}
\]

Moreover \(h_a\) is meromorphic inner, with unimodular boundary values on \(\mathbb R\) away from removable common zeros.

This is currently the cleanest bounded scalar finite observable.

---

## 7. Source-fixed infinite sign — do not regress [R/G]

v13.790 corrected a sign regression that had propagated through several earlier descendants.

Define
\[
R_\xi(z)
:=
\frac{\xi(3/2)}{\xi'(3/2)}
\frac{\xi'(1/2-iz)}
{\xi(1/2-iz)}.
\]

The source-fixed infinite Weyl function is
\[
\boxed{
m_\infty(z)=+\,iR_\xi(z).
}
\]

Check:
\[
R_\xi(i)=1
\quad\Longrightarrow\quad
m_\infty(i)=i,
\]
matching the exact finite calibration.

Do not use the superseded negative sign
\[
m_\infty=-iR_\xi.
\]

The corrected infinite Schur target is
\[
\boxed{
s_\infty(z)
=
\frac{R_\xi(z)-1}{R_\xi(z)+1}.
}
\]

The corrected bounded quotient target is
\[
\boxed{
h_\infty(z)
=
\frac{z+i}{z-i}
\frac{R_\xi(z)-1}{R_\xi(z)+1},
}
\]
with the singularity at \(z=i\) understood removably if it is the actual Schur limit.

The corrected reflection quotient is
\[
\boxed{
\rho_\infty(z)
=
\frac{z-i}{z+i}
\frac{R_\xi(z)+1}
{R_\xi(z)-1}.
}
\]

---

## 8. Montel–Vitali convergence gate [D/C]

Since
\[
|h_a|\le1
\]
on \(\mathbb C_+\), the family \(\{h_a\}\) is Montel-normal.

Therefore, to prove full local-uniform finite-to-infinite Weyl convergence, it is enough to identify
\[
h_a(z)\to h_\infty(z)
\]
on any uniqueness set in \(\mathbb C_+\) with an interior accumulation point.

A particularly useful candidate is an interval on the positive imaginary axis.

Once
\[
h_a\to h_\infty
\]
locally uniformly,
\[
s_a=\phi_i h_a\to s_\infty,
\]
and the inverse Cayley transform gives
\[
m_a\to m_\infty
\]
away from the inverse-Cayley divisor.

This is the current smallest analytic convergence gate.

---

## 9. Canonical Schur-parameter hierarchy [D]

Define
\[
\kappa_{0,a}:=h_a(i)=m_a'(i).
\]

Exact deficiency-overlap identity:
\[
\boxed{
\kappa_{0,a}
=
\frac{
\langle v_{a,+i},v_{a,-i}\rangle_{T_a}
}{
\|v_{a,+i}\|_{T_a}^2
}
\in(-1,1).
}
\]

Equivalently, using parity energies
\[
E_{e,a}:=\|w_{a,e}\|_{T_a}^2,
\qquad
E_{o,a}:=\|w_{a,o}\|_{T_a}^2,
\]
\[
\boxed{
\kappa_{0,a}
=
\frac{E_{e,a}-E_{o,a}}
{E_{e,a}+E_{o,a}}.
}
\]

The source-fixed infinite target is
\[
\boxed{
\kappa_{0,\infty}
=
\frac{\xi(3/2)}{\xi'(3/2)}
\left(\frac{\xi'}{\xi}\right)'(3/2)
\approx
0.9968019520324009035288967048.
}
\]

The second Schur parameter is
\[
\boxed{
\kappa_{1,a}
=
\frac{
\kappa_{0,a}-\kappa_{0,a}^2+i\,m_a''(i)
}{
1-\kappa_{0,a}^2
}.
}
\]

Its infinite target is
\[
\boxed{
\kappa_{1,\infty}
\approx
-0.9954804115180577060070406509.
}
\]

External Audit Round 101 independently reproduced both target values to high precision.

The Schur defects are small:
\[
1-\kappa_{0,\infty}^2\approx0.0063858684,
\]
\[
1-\kappa_{1,\infty}^2\approx0.0090187503.
\]

Higher Schur stages are therefore numerically sensitive.

---

## 10. Critical \(\lambda\)-discipline [G]

The finite theory exists unconditionally for
\[
\lambda<\lambda_a.
\]

But Suzuki's Section-7 \(\xi\)-target is specifically the
\[
\boxed{\lambda=0}
\]
branch.

Therefore distinguish:

### Branch U — unconditional finite study
Use a rigorously admissible shifted
\[
\lambda<\lambda_a.
\]
Finite Weyl/Schur theory is rigorous, but do not compare these Schur parameters directly to the \(\lambda=0\) \(\xi\)-targets.

### Branch X — \(\xi\)-target diagnostic
Use
\[
T_{a,0}=A_a.
\]
This is the relevant family for comparison with
\[
m_\infty,\ h_\infty,\ \kappa_{n,\infty}.
\]

However, positivity/invertibility of \(A_a\) uniformly in \(a\) is tied to the global Weil/RH problem. Finite successful inversions are diagnostics only, not proofs of RH.

---

## 11. Source-faithful numerical realization [D]

Use the form-core Galerkin route, not the deprecated raw-Fredholm endpoint Nyström route.

Suzuki's Friedrichs form has core
\[
H_0^1(-a,a),
\]
and a nested Galerkin sequence may solve
\[
\mathfrak t_{a,\lambda}[v_N,\varphi]
=
\langle e^x,\varphi\rangle.
\]

The current implementation uses the orthonormal Dirichlet form-core basis
\[
\psi_n(x)
=
a^{-1/2}
\sin\!\left(\frac{n\pi(x+a)}{2a}\right).
\]

For \(\lambda=0\),
\[
A_Nc_N=f_N.
\]

The source overlaps are analytic:
\[
\boxed{
\langle\psi_n,e^{\alpha x}\rangle
=
\frac{k_n}{\sqrt a}
\frac{
e^{-\alpha a}-(-1)^n e^{\alpha a}
}{
\alpha^2+k_n^2
},
\qquad
k_n=\frac{n\pi}{2a}.
}
\]

Research artifact:

research-notes/suzuki_form_core_schur_parameter_diagnostic.py

Round 101 independently executed this script and reproduced the published tables digit-for-digit.

---

## 12. Current numerical bottleneck [N]

At
\[
a=1,\qquad\lambda=0,
\]
the parity blocks become severely near-null as the Galerkin cutoff grows.

At \(N=12\),
\[
\boxed{
\lambda_{\min}^{(+)}
\approx1.82\times10^{-15}.
}
\]

The first diagnostic table is nonmonotone, and the second Schur parameter even overshoots the unit disk at one truncation:
\[
\kappa_{1,8}\approx-1.0008360669.
\]

This is interpreted as a conditioning/truncation diagnostic, not a contradiction of the exact Schur theorem.

The control run
\[
a=0.5,\ \lambda=0
\]
is much smoother and remains inside the Schur disk across the tested cutoffs.

Therefore the current obstacle is not algebraic residual accuracy. It is
\[
\boxed{
\text{accurate inversion on the near-null parity subspaces of }A_a.
}
\]

A larger naive dense inverse is not the next move.

---

## 13. Exact next gate for the new chat [C]

The next nonredundant computation is:

\[
\boxed{
\textbf{protected-subspace evaluation of the parity source resolvent quadratic forms.}
}
\]

The quantities actually needed are only
\[
\boxed{
E_{e,a}
=
f_e^T(A_a^{(+)})^{-1}f_e,
}
\]
\[
\boxed{
E_{o,a}
=
f_o^T(A_a^{(-)})^{-1}f_o,
}
\]
plus the first weighted moments needed for \(\kappa_{1,a}\).

A full inverse matrix is unnecessary.

The next chat should:

1. inspect the existing protected-subspace/Feshbach machinery before writing new code;
2. identify which existing artifacts are source-compatible with the current form-core \(A_a\) matrices;
3. freeze the exact matrix/source-vector payload before comparing methods;
4. isolate the low/near-null protected subspace in each parity block;
5. evaluate the quadratic forms through a protected/Feshbach or certified inverse action;
6. report residuals, smallest protected eigenvalues, precision dependence, and cutoff dependence;
7. compute \(\kappa_{0,a}\) first;
8. only compute/trust \(\kappa_{1,a}\) after the first-stage protected solve is stable;
9. compare \(\lambda=0\) values with the \(\xi\)-targets only as finite-\(a\) diagnostics;
10. if a shifted \(\lambda<\lambda_a\) control is used, keep its interpretation separate.

Potentially relevant existing research artifacts to inspect—not blindly reuse—include:

- research-notes/suzuki_active_core_feshbach_basis.py
- research-notes/suzuki_feshbach_buffer_anatomy.py
- research-notes/suzuki_hybrid_finite_feshbach_low_core.py
- research-notes/suzuki_rank4_streaming_inverse_residual_contract.py
- research-notes/suzuki_residual_certified_schur_solve.py
- research-notes/suzuki_two_sided_inverse_factor_bound.py
- research-notes/suzuki_rational_77x6_full_tail_protected_subspace.py

These come from earlier certification lanes and may use different matrices/targets. The next chat must check their ledger provenance and compatibility before reuse.

---

## 14. Secondary analytic gate [C]

In parallel with the protected numerical solve, the minimal convergence target remains
\[
\boxed{
h_a(z)
=
\frac{
\widehat{T_a^{-1}e^x}(z)
}{
\widehat{T_a^{-1}e^x}(-z)
}
\longrightarrow
h_\infty(z)
}
\]
on an interior uniqueness set.

The first two canonical scalar tests are
\[
\kappa_{0,a}\to\kappa_{0,\infty},
\qquad
\kappa_{1,a}\to\kappa_{1,\infty}.
\]

A stabilized protected-subspace computation of these quantities is therefore not merely numerical cleanup: it directly probes necessary consequences of the finite-to-infinite Weyl limit.

---

## 15. Primitive affine lane remains separate [G]

The raw (8.5) affine ratios remain exactly
\[
r_{0,a}
=
\ell_{0,a}((T_a^{(+)})^{-1}\cosh),
\]
\[
r_{1,a}
=
\ell_{1,a}((T_a^{(-)})^{-1}\sinh).
\]

v13.785 rewrites their edge-scaled behavior using dual resolvent responses:
\[
e^{-a}r_{j,a}
=
\int_0^{2a}e^{-\xi}\psi_{j,a}(a-\xi)\,d\xi.
\]

This primitive edge-profile problem is valid but is not a prerequisite for the Weyl/Schur lane.

Do not let the next chat drift back into trying to determine \(r_0,r_1\) by the already-failed local Schur/basepoint closures.

---

## 16. Supersession/guardrail map [G]

Do not reuse the following as active facts:

- v13.779 endpoint reconstruction for actual deficiency vectors;
- literal \(u=iv'\) for the deficiency vectors;
- the raw first-kind kernel as though it were \(S_a\);
- artificial \(1+M_{00}\), \(1+M_{1x}\) Schur denominators as a physical closure;
- the regressed infinite sign \(m_\infty=-iR_\xi\);
- arbitrary-\(\lambda\) comparison with the \(\lambda=0\) \(\xi\)-target;
- deprecated endpoint-row Fredholm/Nyström deficiency solves;
- binary64 agreement as evidence of convergence in the near-null \(a=1\) regime.

Retain:

- exact \(T_a^{-1}e^{\pm x}\) deficiency solve;
- abstract \(\bar D\) transport;
- exact finite Weyl boundary triple;
- one-function \(F_a\) reduction;
- Schur function \(h_a\);
- corrected \(+iR_\xi\) infinite target;
- Montel/Vitali normal-family gate;
- Schur-parameter hierarchy;
- form-core Galerkin route;
- protected-subspace conditioning diagnosis.

---

## 17. Recommended first prompt for the new chat

Read the live ledger starting with v13.796 and this v13.797 handoff. Check for newer audit/collision entries first. Continue Lane A from the protected-subspace numerical gate: inspect the existing Feshbach/protected inverse machinery for compatibility with the source-faithful form-core parity blocks, then compute stable protected evaluations of \(f_e^T(A_a^{(+)})^{-1}f_e\) and \(f_o^T(A_a^{(-)})^{-1}f_o\) at \(a=1,\lambda=0\), with certified residual/conditioning diagnostics. Do not use endpoint deficiency conditions, raw Fredholm inversion, the old Schur moment closure, or the superseded negative infinite Weyl sign.

---

## Result

Lane A is now in a clean state.

The active finite observable is
\[
\boxed{
h_a(z)
=
\frac{
\widehat{T_a^{-1}e^x}(z)
}{
\widehat{T_a^{-1}e^x}(-z)
},
\qquad
|h_a|\le1,
}
\]
with target
\[
\boxed{
h_\infty(z)
=
\frac{z+i}{z-i}
\frac{R_\xi(z)-1}{R_\xi(z)+1}.
}
\]

The first two scalar targets are
\[
\boxed{
\kappa_{0,\infty}\approx0.9968019520324009,
}
\]
\[
\boxed{
\kappa_{1,\infty}\approx-0.9954804115180577.
}
\]

The current computational obstacle is the near-null \(a=1,\lambda=0\) parity inverse, not the formal Weyl algebra.

\[
\boxed{
\textbf{NEXT: protected-subspace/Feshbach evaluation of the parity source resolvent quadratic forms.}
\]
