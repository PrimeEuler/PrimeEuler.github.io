# Cone Derivation Ledger v13.930 — Sandbox: Unconditional Shifted Weyl Compactness, Canonical-System Subsequential Limits, and Large-Negative-Shift Trivialization

**Date:** 2026-10-01
**Track:** Sandbox / source-faithful Suzuki shifted branch
**Status:** [D] unconditional Schur/Herglotz compactness theorem for arbitrary admissible shifted sequences; [D] explicit large-negative-shift trivialization theorem; [C] canonical-system interpretation via the classical de Branges inverse theorem; [G] shows admissibility alone cannot select an intrinsic nontrivial infinite carrier; [O] fixed-shift/global lower-bound and shift-selection problems remain open
**Authorization:** Jeremy, 2026-10-01 ("yep. lets do it")
**Parents:** v13.274, v13.682, v13.782, v13.784, v13.788–791, v13.794, v13.872–873, v13.927, v13.929
**Collision check:** v13.930 was absent immediately before this write; live head was v13.929.

---

## 0. Synchronization and scope

The shifted branch must stay on Suzuki's actual untwisted Riemann-zeta operator

\[
A_a,
\qquad
\lambda_a:=\inf\sigma(A_a).
\]

Do **not** import the sandbox's separate \(\chi_{12}\)-twisted \(\lambda=-1\) numerics. v13.872/873 explicitly distinguishes those operators.

Suzuki's finite theory gives, for each fixed \(a>0\) and every

\[
\lambda<\lambda_a,
\]

the positive operator

\[
\boxed{
T_{a,\lambda}=A_a-\lambda I>0.
}
\tag{1}
\]

The source-faithful normalized deficiency vector is

\[
\boxed{
v_{a,+i}^{(\lambda)}
=
T_{a,\lambda}^{-1}e^x.
}
\tag{2}
\]

Define

\[
F_{a,\lambda}(z)
=
\int_{-a}^{a}
v_{a,+i}^{(\lambda)}(x)e^{izx}\,dx.
\tag{3}
\]

The canonical bounded quotient is

\[
\boxed{
h_{a,\lambda}(z)
=
\frac{F_{a,\lambda}(z)}
{F_{a,\lambda}(-z)},
}
\tag{4}
\]

with the canonical removable continuation from v13.790.

For every admissible pair \((a,\lambda)\),

\[
\boxed{
h_{a,\lambda}\in\mathcal S(\mathbb C_+),
\qquad
|h_{a,\lambda}(z)|\le1.
}
\tag{5}
\]

The corresponding Cayley data are

\[
\phi_i(z)
=
\frac{z-i}{z+i},
\tag{6}
\]

\[
\boxed{
s_{a,\lambda}(z)
=
\phi_i(z)\,h_{a,\lambda}(z),
}
\tag{7}
\]

and

\[
\boxed{
m_{a,\lambda}(z)
=
i\frac{1+s_{a,\lambda}(z)}
{1-s_{a,\lambda}(z)}.
}
\tag{8}
\]

For every finite admissible pair,

\[
\boxed{
m_{a,\lambda}(i)=i.
}
\tag{9}
\]

The present entry asks what survives **unconditionally as \(a\to\infty\)** without inserting the \(\lambda=0\) Xi target.

---

## 1. First obstruction: no uniform fixed shift is currently available [D/G]

Suzuki's theorem is pointwise in \(a\):

\[
\lambda<\lambda_a.
\]

The current ledger does **not** contain a source-faithful uniform lower bound

\[
\inf_{a>0}\lambda_a>-\infty
\]

for Suzuki's untwisted \(A_a\).

Therefore one may not simply declare

\[
\lambda=-1
\]

or any other fixed negative number and call

\[
\{T_{a,\lambda}\}_{a\to\infty}
\]

an unconditional global family.

A fixed shift \(\lambda_*\) is globally admissible only if one proves

\[
\boxed{
\lambda_*<\inf_{a>0}\lambda_a.
}
\tag{10}
\]

No such theorem is presently in the ledger.

Hence the genuinely unconditional large-\(a\) object is not a fixed-\(\lambda\) family but an arbitrary sequence of **admissible pairs**

\[
\boxed{
a_n\to\infty,
\qquad
\lambda_n<\lambda_{a_n}.
}
\tag{11}
\]

---

## 2. Unconditional Schur compactness for every admissible sequence [D]

Let \((a_n,\lambda_n)\) satisfy (11).

Set

\[
h_n:=h_{a_n,\lambda_n}.
\]

By (5),

\[
|h_n(z)|\le1
\qquad
(z\in\mathbb C_+).
\]

Therefore \(\{h_n\}\) is a Montel-normal family.

Hence there exists a subsequence, not relabeled, and a holomorphic function

\[
h_*:\mathbb C_+\to\overline{\mathbb D}
\]

such that

\[
\boxed{
h_n\to h_*
}
\tag{12}
\]

locally uniformly on \(\mathbb C_+\).

Thus every admissible large-cutoff sequence possesses a cutoff-free Schur subsequential limit.

No RH assumption, no \(\lambda=0\) identification, no endpoint reconstruction, and no finite-section spectral convergence theorem is used.

---

## 3. The limiting Weyl function is automatically Herglotz [D]

Define

\[
s_n=\phi_i h_n.
\]

Then

\[
s_n\to s_*:=\phi_i h_*
\]

locally uniformly.

For every \(z\in\mathbb C_+\),

\[
|\phi_i(z)|<1.
\]

Since \(|h_*(z)|\le1\),

\[
\boxed{
|s_*(z)|<1
\qquad(z\in\mathbb C_+).
}
\tag{13}
\]

Therefore

\[
\boxed{
m_*(z)
:=
i\frac{1+s_*(z)}
{1-s_*(z)}
}
\tag{14}
\]

is holomorphic and Herglotz/Nevanlinna on \(\mathbb C_+\).

Moreover

\[
\phi_i(i)=0,
\]

so

\[
\boxed{
m_*(i)=i.
}
\tag{15}
\]

Because on each compact \(K\Subset\mathbb C_+\),

\[
\sup_{z\in K}|\phi_i(z)|=:q_K<1,
\]

the denominators satisfy

\[
|1-s_n(z)|\ge1-q_K.
\]

Hence the inverse Cayley map is uniformly stable on \(K\), and

\[
\boxed{
m_{a_n,\lambda_n}\to m_*
}
\tag{16}
\]

locally uniformly along the same subsequence.

So the shifted finite Weyl family is precompact directly in the canonically calibrated Herglotz class.

---

## 4. Normalized Herglotz spectral measure [D]

Every Herglotz function \(m_*\) has the representation

\[
m_*(z)
=
\alpha+\beta z
+
\int_{\mathbb R}
\left(
\frac1{t-z}
-
\frac{t}{1+t^2}
\right)
d\mu_*(t),
\tag{17}
\]

where

\[
\alpha\in\mathbb R,
\qquad
\beta\ge0,
\qquad
\mu_*\ge0,
\]

and

\[
\int_{\mathbb R}\frac{d\mu_*(t)}{1+t^2}<\infty.
\]

Evaluate (17) at \(z=i\).

Since

\[
\frac1{t-i}
-
\frac{t}{1+t^2}
=
\frac{i}{1+t^2},
\]

the calibration (15) gives

\[
\boxed{
\alpha=0,
}
\tag{18}
\]

and

\[
\boxed{
\beta
+
\int_{\mathbb R}
\frac{d\mu_*(t)}
{1+t^2}
=
1.
}
\tag{19}
\]

Thus every subsequential cutoff-free shifted limit carries a positive spectral measure with a **fixed normalized total Herglotz mass**.

This gives an unconditional spectral compactness statement.

It does **not** imply that \(\mu_*\) is discrete.

Weak limits of the finite discrete Weyl measures may acquire continuous components.

Therefore finite-\(a\) discreteness does not by itself survive the cutoff removal.

---

## 5. Canonical-system interpretation [C/D-classical]

By the classical de Branges inverse theorem for canonical systems, every Herglotz function is the Weyl coefficient of a trace-normalized canonical system, unique up to the standard null-set/reparametrization equivalence; trace normalization removes the reparametrization freedom.

Therefore every \(m_*\) produced in §3–4 admits a cutoff-free canonical-system realization

\[
\boxed{
JY'(t)=zH_*(t)Y(t),
}
\tag{20}
\]

with \(H_*(t)\ge0\) and trace normalization.

The calibration

\[
m_*(i)=i
\]

fixes the same canonical boundary-coordinate normalization used by the finite family.

Hence:

\[
\boxed{
\textbf{Every admissible shifted sequence has a subsequence converging at the Weyl level to a genuine cutoff-free canonical system.}
}
\tag{21}
\]

Important guardrail:

(21) is a **Weyl-level compactness/existence theorem**.

It does not prove coefficientwise convergence

\[
H_{a_n,\lambda_n}\to H_*
\]

of finite Hamiltonians, nor does it identify \(H_*\) with Suzuki's conjectural Xi system.

---

## 6. Admissibility alone does not select the limit [D]

The compactness theorem does not give uniqueness.

In fact the shift freedom is large enough to force a trivial limit.

Fix \(a\), and put

\[
\lambda=-L,
\qquad
L>-\lambda_a.
\]

Then

\[
T_{a,-L}=A_a+LI.
\]

By the spectral theorem for the self-adjoint lower-bounded operator \(A_a\),

\[
\boxed{
L(A_a+LI)^{-1}
\longrightarrow I
}
\tag{22}
\]

strongly on \(L^2(-a,a)\) as \(L\to\infty\).

Apply (22) to \(e^x\):

\[
\boxed{
L\,v_{a,+i}^{(-L)}
\to e^x
}
\tag{23}
\]

in \(L^2(-a,a)\).

For \(z\) in a fixed compact subset of \(\mathbb C\), the Fourier evaluation functional is uniformly bounded on \(L^2(-a,a)\), so

\[
\boxed{
L F_{a,-L}(z)
\to
J_a(z)
:=
\int_{-a}^{a}e^{(1+iz)x}\,dx
}
\tag{24}
\]

locally uniformly in \(z\).

Explicitly,

\[
\boxed{
J_a(z)
=
\frac{2\sinh(a(1+iz))}
{1+iz}.
}
\tag{25}
\]

For \(z\in\mathbb C_+\),

\[
J_a(-z)\neq0,
\]

because

\[
\Re(1-iz)=1+\Im z>0
\]

and the zeros of \(\sinh\) lie on the imaginary axis.

Therefore

\[
\boxed{
h_{a,-L}(z)
\longrightarrow
H_a(z)
:=
\frac{J_a(z)}
{J_a(-z)}
}
\tag{26}
\]

locally uniformly on \(\mathbb C_+\) as \(L\to\infty\).

Using (25),

\[
\boxed{
H_a(z)
=
\frac{1-iz}{1+iz}
\frac{\sinh(a(1+iz))}
{\sinh(a(1-iz))}.
}
\tag{27}
\]

This is the exact large-negative-shift free-source quotient.

---

## 7. The free-source quotient tends to zero as \(a\to\infty\) [D]

Let

\[
K\Subset\mathbb C_+.
\]

Write

\[
z=x+iy.
\]

On \(K\), there exist

\[
0<\eta\le y\le M.
\]

Now

\[
\Re(1-iz)=1+y,
\]

while

\[
|\Re(1+iz)|
=
|1-y|.
\]

Therefore the exponential growth gap is

\[
(1+y)-|1-y|
=
2\min(1,y)
\ge
2\min(1,\eta)>0.
\tag{28}
\]

The rational prefactor

\[
\frac{1-iz}{1+iz}
\]

is uniformly bounded on \(K\).

Standard bounds for \(\sinh\) in right/left half-planes therefore give constants \(C_K,c_K>0\) such that

\[
\boxed{
|H_a(z)|
\le
C_Ke^{-c_Ka}
\qquad
(z\in K).
}
\tag{29}
\]

Hence

\[
\boxed{
H_a\to0
}
\tag{30}
\]

locally uniformly on \(\mathbb C_+\).

---

## 8. Diagonal large-negative-shift trivialization theorem [D]

Take any sequence

\[
a_n\to\infty.
\]

Choose an exhaustion

\[
K_1\Subset K_2\Subset\cdots\Subset\mathbb C_+.
\]

For each \(n\), because of the fixed-\(a_n\) convergence (26), choose \(L_n\) so large that

\[
-L_n<\lambda_{a_n}
\]

and

\[
\sup_{z\in K_n}
|h_{a_n,-L_n}(z)-H_{a_n}(z)|
<
\frac1n.
\tag{31}
\]

By (30),

\[
H_{a_n}\to0
\]

locally uniformly.

Therefore the diagonal admissible sequence

\[
\lambda_n:=-L_n
\]

satisfies

\[
\boxed{
h_{a_n,\lambda_n}\to0
}
\tag{32}
\]

locally uniformly on \(\mathbb C_+\).

Consequently

\[
\boxed{
s_{a_n,\lambda_n}
=
\phi_i h_{a_n,\lambda_n}
\to0,
}
\tag{33}
\]

and

\[
\boxed{
m_{a_n,\lambda_n}\to i
}
\tag{34}
\]

locally uniformly on \(\mathbb C_+\).

Thus a perfectly source-faithful, rigorously admissible sequence of shifted Suzuki systems can converge to the constant Weyl function

\[
\boxed{
m_*(z)\equiv i.
}
\tag{35}
\]

This is the canonical trivial/free Weyl limit.

No arithmetic zero data survive this shift regime.

---

## 9. Shift-selection no-go [D/G]

Sections 2–8 prove two complementary facts.

### Compactness

For every admissible sequence,

\[
\boxed{
\text{a cutoff-free Herglotz/canonical-system subsequential limit exists.}
}
\tag{36}
\]

### Non-selection

Admissibility alone permits the trivial limit

\[
\boxed{
m_*\equiv i.
}
\tag{37}
\]

Therefore:

\[
\boxed{
\textbf{The condition }\lambda_a^{\rm shift}<\inf\sigma(A_a)\textbf{ is sufficient for finite positivity but insufficient to select a nontrivial intrinsic infinite carrier.}
}
\tag{38}
\]

This is an exact no-go against treating the auxiliary shift as harmless in the cutoff removal.

It sharpens v13.794's warning that finite data depend on \(\lambda\).

The dependence is strong enough to erase the entire arithmetic Weyl shape in the large-negative-shift regime.

---

## 10. What would be sufficient for a nontrivial intrinsic limit [C/O]

The next useful theorem cannot merely say "choose any admissible shift."

One needs an **intrinsic shift-selection law**.

Three possible forms are now sharply separated.

### A. Fixed finite shift with uniform admissibility

Prove a number \(\lambda_*<0\) such that

\[
\boxed{
\lambda_*<\inf_{a>0}\lambda_a.
}
\tag{39}
\]

Then

\[
T_{a,\lambda_*}
\]

is a single globally defined shifted family.

Only after (39) would it be meaningful to ask for uniqueness of

\[
m_{a,\lambda_*}\to m_{\infty,\lambda_*}.
\]

This uniform lower-bound problem is currently open.

### B. Stabilizing shifts

Allow

\[
\lambda_a\to\lambda_*\in\mathbb R
\]

but prove a uniform coercivity margin

\[
\boxed{
\lambda_a^{\rm bottom}-\lambda_a^{\rm shift}
\ge\delta>0.
}
\tag{40}
\]

Together with a genuine form/resolvent convergence theorem, this could prevent the large-negative-shift trivialization.

No such large-\(a\) theorem is presently established.

### C. Shift-independent geometric normalization

Construct an infinite canonical carrier directly from the localized Weil/cone geometry and then prove that all finite shifted realizations, after a prescribed renormalization, converge to that same carrier.

This would be stronger than fixed-shift convergence and would justify Suzuki's expectation that the auxiliary shift should not alter the final spectral zeros.

No such shift-removal theorem is presently proved.

---

## 11. Relation to the Xi branch [G]

v13.929 proved

\[
\mathrm{RH}
\iff
m_\infty^{\Xi}
=
-C_\infty\frac{\Xi'}{\Xi}
\text{ is Herglotz}.
\]

The present entry shows why the unconditional shifted branch does not accidentally solve that gate.

The family of admissible shifted systems is too large:

\[
\boxed{
\text{it contains sequences converging to }m\equiv i.
}
\]

Therefore no argument based only on

\[
T_{a,\lambda}>0,
\qquad
\lambda<\lambda_a,
\]

can identify the Xi target.

A nontrivial Xi identification must include additional information that selects the \(\lambda=0\) or an equivalent canonical normalization.

This is exactly where the RH-hard content re-enters.

---

## 12. Spectral-type guardrail [D/G]

Each finite Suzuki extension has discrete real spectrum.

The subsequential Herglotz limit (17) may nevertheless have

\[
\mu_*
=
\mu_{\rm pp}
+
\mu_{\rm ac}
+
\mu_{\rm sc}.
\]

Nothing in Montel compactness prevents absolutely continuous or singular-continuous mass from appearing.

Therefore:

\[
\boxed{
\textbf{finite-cutoff discreteness does not imply cutoff-free discreteness.}
}
\tag{41}
\]

To obtain a Hilbert–Pólya-type point spectrum after cutoff removal one still needs a compactness/endpoint/de Branges theorem forcing the limiting measure to be pure point.

The large-negative-shift example is already a warning that the cutoff-free limit can lose essentially all finite spectral detail.

---

## 13. Result

The unconditional shifted branch is now structurally classified.

For every admissible sequence

\[
a_n\to\infty,
\qquad
\lambda_n<\lambda_{a_n},
\]

the canonically normalized finite Weyl functions possess Herglotz subsequential limits:

\[
\boxed{
m_{a_{n_k},\lambda_{n_k}}
\to
m_*,
\qquad
m_*(i)=i.
}
\]

By the classical de Branges inverse theorem, each such \(m_*\) determines a cutoff-free trace-normalized canonical system.

So cutoff-free **existence** is not the hard part.

The hard part is **selection and spectral type**.

Indeed, admissible large-negative shifts can be chosen so that

\[
\boxed{
m_{a_n,\lambda_n}\to i.
}
\]

Therefore the finite positivity condition alone cannot select the arithmetic carrier.

The next nonredundant gate is

\[
\boxed{
\textbf{derive an intrinsic shift-selection law or a uniform fixed-shift lower bound, and then prove uniqueness of the resulting Herglotz/canonical-system limit.}
}
\]

Only after that should one ask whether the selected limit can be continued to the \(\lambda=0\) Xi branch without circularly assuming the RH-hard Herglotz property.
