# Cone Derivation Ledger v13.929 — Sandbox: Xi Weyl-Target Herglotz/RH Equivalence and the Montel–Vitali Barrier

**Date:** 2026-10-01
**Track:** Sandbox / compression-cone + source-faithful Suzuki Weyl lane
**Status:** [D] exact equivalence theorem and convergence obstruction; [R] sign correction to v13.927 §8; [G] anti-overclaim guardrails; [O] unconditional shifted-carrier limit remains open
**Authorization:** Jeremy, 2026-10-01 ("check the ledger for new stuff and lets hit that gate")
**Parents:** v13.782/784/785/788–791/797 (source-faithful finite Weyl/Schur chain), v13.838 (Bucket-2 gap characterization), v13.925/927 (Xi operator and boundary-extension analysis), v13.928 (External Audit Round 139)
**Collision check:** v13.929 was absent immediately before this write; live head was v13.928.

---

## 0. Synchronization: what the newer ledger changes

The older v13.833 Bucket-2 checkpoint is no longer the sharpest description of the source-faithful finite problem.

The later source-faithful chain establishes:

1. **v13.782:** Suzuki's actual deficiency equation is solved at the source level by
   \[
   T_a v_{a,\pm}=C_{a,\pm}e^{\pm x},
   \qquad
   v_{a,\pm}=C_{a,\pm}T_a^{-1}e^{\pm x}.
   \]
   The primitive affine ratios are not free boundary knobs:
   \[
   r_{0,a}
   =
   \ell_{0,a}\!\left((T_a^{(+)})^{-1}\cosh\right),
   \qquad
   r_{1,a}
   =
   \ell_{1,a}\!\left((T_a^{(-)})^{-1}\sinh\right).
   \]

2. **v13.784:** the actual deficiency vectors need not lie in \(H_0^1\); no endpoint reconstruction \(v(\pm a)=0\) may be imposed. The abstract transported identity
   \[
   S_a\bar Dv_\pm=C_\pm\bar D e_{\pm i}
   \]
   is exact, while the raw first-kind Fredholm equation is a distinct primitive reconstruction.

3. **v13.785/788:** the finite Weyl function is determined by one source-faithful entire transform
   \[
   F_a(z)=\widehat{T_a^{-1}e^x}(z).
   \]

4. **v13.789–791:** the finite Cayley/Schur data are bounded holomorphic functions and form a Montel-normal family.

5. **v13.838:** the first-kind equation (8.5) alone has the two-dimensional affine ambiguity; the full distributional source equation (8.4), equivalently \(T_av=C e^{\pm x}\), is the actual selector. Smoothing the kink/distributional data destroys that selection.

Thus the structural \(I_0/I_1\) problem is already closed at the source level. The remaining \(\lambda=0\) gate is finite-to-infinite **Weyl/Schur convergence**, not discovery of two missing endpoint equations.

The present entry determines the exact logical difficulty of that convergence gate.

---

## 1. Source-fixed infinite Weyl target [D]

Use the source-fixed sign correction of v13.790.

Define

\[
R_\xi(z)
:=
\frac{\xi(3/2)}{\xi'(3/2)}
\frac{\xi'(1/2-iz)}
{\xi(1/2-iz)}.
\]

Then

\[
\boxed{
m_\infty(z)=+\,iR_\xi(z).
}
\tag{1}
\]

Let

\[
\Xi(z):=\xi\!\left(\frac12-iz\right).
\]

Since

\[
\Xi'(z)
=
-i\,\xi'\!\left(\frac12-iz\right),
\]

we have

\[
\xi'\!\left(\frac12-iz\right)
=
i\Xi'(z).
\]

Put

\[
\boxed{
C_\infty
:=
\frac{\xi(3/2)}{\xi'(3/2)}
>0.
}
\]

Then (1) becomes

\[
\boxed{
m_\infty(z)
=
-C_\infty
\frac{\Xi'(z)}{\Xi(z)}.
}
\tag{2}
\]

At the canonical deficiency point,

\[
\boxed{
m_\infty(i)=i,
}
\tag{3}
\]

matching the exact finite identity \(m_a(i)=i\).

---

## 2. Main theorem: RH iff the Xi target is Herglotz [D]

### Theorem

For the source-fixed target (2),

\[
\boxed{
\mathrm{RH}
\iff
m_\infty
\text{ is a Herglotz/Nevanlinna function on }\mathbb C_+.
}
\tag{4}
\]

No simplicity assumption is required.

### 2.1 RH implies Herglotz [D]

Assume RH.

Then every zero of the even real entire function \(\Xi(z)\) is real. Pair the zeros as

\[
\pm\gamma,
\qquad
\gamma>0,
\]

with multiplicity \(m_\gamma\ge1\).

Because \(\Xi\) is even of order one, the paired Hadamard product may be written

\[
\boxed{
\Xi(z)
=
\Xi(0)
\prod_{\gamma>0}
\left(1-\frac{z^2}{\gamma^2}\right)^{m_\gamma},
}
\tag{5}
\]

with the paired logarithmic derivative converging locally uniformly off the real zeros:

\[
\frac{\Xi'(z)}{\Xi(z)}
=
\sum_{\gamma>0}
m_\gamma
\left[
\frac1{z-\gamma}
+
\frac1{z+\gamma}
\right].
\tag{6}
\]

Therefore

\[
\boxed{
-\frac{\Xi'(z)}{\Xi(z)}
=
\sum_{\gamma>0}
m_\gamma
\left[
\frac1{\gamma-z}
+
\frac1{-\gamma-z}
\right].
}
\tag{7}
\]

For \(z=x+iy\in\mathbb C_+\),

\[
\operatorname{Im}\frac1{t-z}
=
\frac{y}{(t-x)^2+y^2}
>0
\qquad(t\in\mathbb R).
\]

Thus every term in (7) has positive imaginary part. Since \(C_\infty>0\),

\[
\boxed{
\operatorname{Im}m_\infty(z)>0
\qquad(z\in\mathbb C_+).
}
\tag{8}
\]

Hence \(m_\infty\) is Herglotz.

Multiplicity only multiplies the positive contribution \(m_\gamma\); simple zeros are not needed.

### 2.2 Herglotz implies RH [D]

Conversely, suppose \(m_\infty\) is Herglotz on \(\mathbb C_+\).

A Herglotz function is holomorphic on \(\mathbb C_+\).

But every zero \(z_0\) of \(\Xi\) of multiplicity \(m\ge1\) gives

\[
\frac{\Xi'(z)}{\Xi(z)}
=
\frac{m}{z-z_0}
+
O(1),
\]

so \(m_\infty\) has a genuine simple pole at \(z_0\), irrespective of multiplicity.

Therefore \(\Xi\) has no zeros in \(\mathbb C_+\).

The map

\[
s=\frac12-iz
\]

sends

\[
\operatorname{Im}z>0
\quad\Longleftrightarrow\quad
\operatorname{Re}s>\frac12.
\]

Thus \(\xi(s)\) has no nontrivial zero with \(\Re s>1/2\).

By the functional equation \(s\mapsto1-s\), a zero with \(\Re s<1/2\) would produce one with \(\Re s>1/2\).

Hence every nontrivial zero satisfies

\[
\boxed{
\operatorname{Re}s=\frac12.
}
\]

That is RH.

This proves (4).

---

## 3. Exact Schur equivalents [D]

Define the source-fixed Cayley transform

\[
\boxed{
s_\infty(z)
=
\frac{m_\infty(z)-i}
{m_\infty(z)+i}.
}
\tag{9}
\]

Using \(m_\infty=iR_\xi\),

\[
\boxed{
s_\infty(z)
=
\frac{R_\xi(z)-1}
{R_\xi(z)+1}.
}
\tag{10}
\]

By (3),

\[
s_\infty(i)=0.
\]

Let

\[
\phi_i(z)
=
\frac{z-i}{z+i}.
\]

Define the canonically deflated target

\[
\boxed{
h_\infty(z)
=
\frac{s_\infty(z)}{\phi_i(z)}
=
\frac{z+i}{z-i}
\frac{R_\xi(z)-1}
{R_\xi(z)+1},
}
\tag{11}
\]

with the singularity at \(z=i\) understood by removable continuation when applicable.

Then

\[
\boxed{
\mathrm{RH}
\iff
m_\infty\in\mathcal N(\mathbb C_+)
\iff
s_\infty\in\mathcal S(\mathbb C_+)
\iff
h_\infty\in\mathcal S(\mathbb C_+).
}
\tag{12}
\]

Here \(\mathcal N\) denotes the Herglotz/Nevanlinna class and \(\mathcal S\) the Schur class.

### Proof of the final equivalence [D]

If \(m_\infty\) is Herglotz, its Cayley transform \(s_\infty\) is Schur.

Since \(s_\infty(i)=0\), Schwarz–Pick gives

\[
|s_\infty(z)|
\le
|\phi_i(z)|.
\]

Therefore

\[
h_\infty=s_\infty/\phi_i
\]

extends holomorphically and is Schur.

Conversely, if \(h_\infty\) extends to a Schur function, then

\[
s_\infty=\phi_i h_\infty
\]

is Schur, and the inverse Cayley transform

\[
m_\infty
=
i\frac{1+s_\infty}{1-s_\infty}
\]

is Herglotz.

Then (4) gives RH.

---

## 4. Finite functions and the exact convergence barrier [D]

For every finite admissible \(a\), v13.790 gives

\[
\boxed{
h_a(z)
=
\frac{F_a(z)}{F_a(-z)}
}
\tag{13}
\]

after canonical removable continuation, with

\[
\boxed{
|h_a(z)|\le1
\qquad(z\in\mathbb C_+).
}
\tag{14}
\]

Thus \(\{h_a\}\) is a uniformly bounded normal family.

Suppose for some sequence \(a_n\to\infty\),

\[
h_{a_n}(z)\to h_\infty(z)
\]

pointwise on a set

\[
S\subset\mathbb C_+
\]

having an accumulation point in \(\mathbb C_+\), where the meromorphic formula (11) is holomorphic on a neighborhood of that accumulation point.

By Vitali/Montel,

\[
h_{a_n}\to h_*
\]

locally uniformly on all of \(\mathbb C_+\), for a Schur function \(h_*\).

On the uniqueness set,

\[
h_*=h_\infty.
\]

The identity theorem then identifies \(h_*\) with the meromorphic target wherever the latter is initially holomorphic. Thus \(h_*\) supplies a holomorphic Schur continuation of (11) through all apparent interior poles.

By (12),

\[
\boxed{
\mathrm{RH}.
}
\tag{15}
\]

Therefore:

\[
\boxed{
\textbf{Any source-faithful proof of the }\lambda=0\textbf{ finite-to-infinite Weyl target on an interior uniqueness set proves RH.}
}
\tag{16}
\]

This is not a technical convergence lemma waiting for routine operator estimates.

It is an RH-hard gate.

---

## 5. Even a “safe” imaginary-axis interval is RH-hard [D]

There is an especially sharp consequence.

Take

\[
z=iy,
\qquad
y>\frac12.
\]

Then

\[
\frac12-i(iy)
=
\frac12+y
>1.
\]

So the target is unconditionally analytic there because \(\zeta(s)\) has no zeros for \(\Re s>1\).

Let

\[
I\subset(1/2,\infty)
\]

be any nontrivial interval.

If one proves

\[
\boxed{
h_a(iy)\longrightarrow h_\infty(iy)
\qquad
\text{for every }y\in I,
}
\tag{17}
\]

then the set \(\{iy:y\in I\}\) has accumulation points inside \(\mathbb C_+\).

Vitali therefore upgrades (17) to a Schur continuation on all of \(\mathbb C_+\), and (12) yields RH.

Thus even convergence on an interval entirely inside the classical zero-free half-plane would prove RH:

\[
\boxed{
\text{the “safe-axis uniqueness-set” strategy is already an RH route.}
}
\tag{18}
\]

This sharply reclassifies the v13.789/790 Montel–Vitali suggestion.

---

## 6. What RH would make the target spectral measure [D/I]

Under RH, (7) gives the Herglotz representation of \(m_\infty\) as a purely atomic symmetric measure.

Each real zero \(\gamma\) of multiplicity \(m_\gamma\) contributes Herglotz mass

\[
\boxed{
\mu_\infty(\{\gamma\})
=
C_\infty m_\gamma.
}
\tag{19}
\]

In paired form,

\[
m_\infty(z)
=
C_\infty
\sum_{\gamma>0}
m_\gamma
\left[
\frac1{\gamma-z}
+
\frac1{-\gamma-z}
\right].
\tag{20}
\]

Thus, conditional on RH, the source-fixed infinite Weyl target is not merely Herglotz: it has a **purely atomic spectral measure supported exactly at the zero ordinates**.

This is the cutoff-free discrete spectral type sought in v13.927.

But (20) is not a new proof of that spectral type. Its validity as a Herglotz representation is equivalent to the zeros being real.

Hence:

\[
\boxed{
\text{RH is exactly the condition under which the formal Xi Weyl target becomes a legitimate cutoff-free self-adjoint discrete spectral measure.}
}
\tag{21}
\]

This explains why the de Branges escape hatch of v13.927 is both structurally correct and RH-hard.

---

## 7. Precision correction to v13.927 §8 [R]

v13.927 inherited the older sign from the superseded v13.754 display and wrote

\[
\tau_{\rm HB}=+\frac{i}{c_\infty}.
\]

The authoritative source-fixed sign is v13.790:

\[
m_\infty=+iR_\xi,
\qquad
c_\infty=\frac{\xi'(3/2)}{\xi(3/2)}>0.
\]

Since

\[
\frac{\xi'}{\xi}
=
-i c_\infty m_\infty,
\]

the Suzuki entire function

\[
E(z)
=
\Xi(z)+i\Xi'(z)
=
\Xi(z)\left[1-i c_\infty m_\infty(z)\right]
\]

factors as

\[
\boxed{
E(z)
=
-i c_\infty
\Xi(z)
\left[
m_\infty(z)-\tau_{\rm HB}
\right],
}
\]

with

\[
\boxed{
\tau_{\rm HB}
=
-\frac{i}{c_\infty}.
}
\tag{22}
\]

Therefore v13.927 §8 should read \(-i/c_\infty\), not \(+i/c_\infty\).

The conclusion used there is unchanged:

\[
\boxed{
\tau_{\rm HB}\notin\mathbb R,
}
\]

so the \(E/\Xi\) boundary factor is non-self-adjoint (maximal dissipative/accumulative according to convention), not a real self-adjoint extension parameter.

No other v13.927 conclusion is changed by this sign correction.

---

## 8. Status of the source-faithful affine constants [D/G]

The new theorem does not reopen the primitive constants.

From v13.782:

\[
\boxed{
r_{0,a}
=
\ell_{0,a}\left((T_a^{(+)})^{-1}\cosh\right),
\qquad
r_{1,a}
=
\ell_{1,a}\left((T_a^{(-)})^{-1}\sinh\right).
}
\]

From v13.785:

\[
\boxed{
e^{-a}r_{j,a}
=
\int_0^{2a}
e^{-\xi}
\psi_{j,a}(a-\xi)\,d\xi.
}
\]

Those are exact source-faithful observables.

But the later one-function Weyl observable

\[
F_a(z)=\widehat{T_a^{-1}e^x}(z)
\]

and its quotient \(h_a\) do not require first proving that the raw affine edge contamination vanishes.

Therefore the primitive edge problem and the Weyl/Schur convergence problem remain distinct.

The present theorem concerns the latter.

---

## 9. Unconditional branch versus Xi branch [D/G]

The finite extension theory is rigorous whenever

\[
\lambda<\lambda_a.
\]

For such an admissible shifted branch, the finite Weyl function is Herglotz and the canonically deflated \(h_{a,\lambda}\) is Schur.

Hence normal-family compactness and subsequential Schur limits are unconditional.

But the \(\xi\)-target belongs specifically to

\[
\boxed{\lambda=0.}
\]

Identifying a shifted-\(\lambda\) limit with the \(\lambda=0\) Xi target is not justified.

Moreover, on the \(\lambda=0\) branch, proving the target limit on any interior uniqueness set implies RH by §4–5.

Thus the correct separation is:

\[
\boxed{
\begin{array}{ll}
\textbf{Branch U:} &
\lambda<\lambda_a,\ \text{finite Schur theory and subsequential limits unconditional;}\\[1ex]
\textbf{Branch X:} &
\lambda=0,\ \text{identification with }m_\infty=iR_\xi\text{ is RH-hard.}
\end{array}
}
\tag{23}
\]

---

## 10. What the next non-circular gate actually is [O]

The previous formulation suggested proving

\[
m_a\to m_\infty
\]

as though this were an intermediate technical theorem on the way to a Hilbert–Pólya operator.

Section 4 shows that framing is backwards: such a theorem on the \(\lambda=0\) Xi branch would itself prove RH.

The next genuinely non-circular operator gate must therefore avoid assuming or proving the full Xi target prematurely.

Two legitimate targets remain:

### A. Unconditional canonical-system limit away from the Xi identification

Construct a source-faithful infinite-volume limit of the finite \(T_{a,\lambda}\) / boundary-triple systems for an admissible shifted branch and identify its Weyl function intrinsically, without inserting \(\xi\).

Then ask what additional structural condition is needed to continue to \(\lambda=0\).

### B. Conditional RH architecture

Assume RH explicitly and derive the resulting cutoff-free canonical/de Branges system from the atomic Herglotz measure (19), then compare it with the finite Suzuki systems.

This can clarify uniqueness and geometry but must be labeled conditional; it cannot prove RH.

What is no longer honest is to label the direct \(\lambda=0\)

\[
h_a\to h_\infty
\]

identification as mere convergence plumbing.

---

## 11. Result

The finite source-faithful Suzuki Weyl family and the Xi target meet at an exact logical boundary:

\[
\boxed{
\mathrm{RH}
\iff
-C_\infty\frac{\Xi'}{\Xi}
\text{ is Herglotz on }\mathbb C_+
}
\]

and equivalently

\[
\boxed{
\mathrm{RH}
\iff
h_\infty
=
\frac{z+i}{z-i}
\frac{R_\xi-1}{R_\xi+1}
\text{ extends to a Schur function on }\mathbb C_+.
}
\]

Since every finite \(h_a\) is Schur,

\[
\boxed{
\textbf{any locally identifying finite-to-infinite }\lambda=0\textbf{ Weyl limit proves RH.}
}
\]

So the source-faithful boundary constants have been structurally resolved, but the remaining Xi Weyl-limit gate is not an ordinary asymptotic problem:

\[
\boxed{
\textbf{it is an RH-hard spectral realization problem.}
}
\]

Under RH, the target Herglotz measure becomes purely atomic at the zero ordinates, exactly yielding the cutoff-free discrete spectral type sought by the project. Without RH, the target has an interior pole and cannot be the Weyl function of a self-adjoint canonical system.

This precisely locates the remaining Hilbert–Pólya gap.
