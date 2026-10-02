# Cone Derivation Ledger v13.967 — Sandbox: Phase-Window Certification for the Xi Scalar and Common-Factor Cancellation Diagnostic

**Date:** 2026-10-02  
**Track:** Sandbox / no-twist Suzuki Xi scalar lane  
**Status:** [D] exact uncertain-window phase certification theorem; [D] exact common-characteristic-zero criterion; [N] source-faithful \(a=1,\lambda=0\) finite-section root/phase diagnostics through \(N=48\); [N] direct phase-vs-source-scalar consistency check; [G] raw Ritz characteristics are not themselves certification-grade Herglotz approximants; [O] attach interval sign enclosures to a certified source solve and then move in \(a\)  
**Authorization:** Jeremy, 2026-10-02 ("swwwt. letgs do it.")  
**Parents:** v13.965, v13.966 (renumbered Cayley/trace/kernel-jet entry), v13.798, v13.800–801  
**Research artifact:** \`research-notes/suzuki_xi_scalar_phase_window_diagnostic.py\`, commit \`51f845e9f8178213bfba5f57eb73f45966246404\`  
**Collision note:** External Audit Round 147 had already occupied v13.964. The audit thread repaired the later sandbox collision by renumbering the Cayley/trace entry to v13.966. This entry was checked against the live tree and uses the next free slot v13.967.

---

## 0. Purpose

v13.965 reduced the no-twist Xi scalar to the centered sign-phase moment

\[
\boxed{
\kappa_a^\Xi
=
2\int_0^\infty
\sigma_a(t)
\frac{t}{(1+t^2)^2}\,dt,
\qquad
\sigma_a(t):=\operatorname{sgn}m_a(t),
}
\tag{1}
\]

with uniform tail bound

\[
\boxed{
\left|
\kappa_a^\Xi
-
2\int_0^T
\sigma_a(t)
\frac{t}{(1+t^2)^2}\,dt
\right|
\le
\frac1{1+T^2}.
}
\tag{2}
\]

The present gate asks how to certify the scalar when finite characteristic approximations have poorly resolved or nearly common roots.

The answer is: **do not require every root to be sharply resolved**.

Instead, certify the sign of the exact Weyl ratio away from small uncertain windows and charge the windows explicitly by their phase weight.

---

## 1. Exact finite characteristic formulas [D]

On the absolute Suzuki branch

\[
\lambda=0,
\]

let

\[
v_a=A_a^{-1}e^x,
\qquad
F_a(z)=\widehat v_a(z).
\]

For real \(t\),

\[
F_a(-t)=\overline{F_a(t)}.
\]

The two fixed extension characteristics are

\[
\boxed{
W_{a,0}(t)
=
(t-i)F_a(t)+(t+i)F_a(-t),
}
\tag{3}
\]

\[
\boxed{
W_{a,\pi}(t)
=
(t-i)F_a(t)-(t+i)F_a(-t).
}
\tag{4}
\]

Set

\[
Z_a(t):=(t-i)F_a(t).
\]

Then

\[
\boxed{
W_{a,0}(t)=2\operatorname{Re}Z_a(t),
}
\tag{5}
\]

and

\[
\boxed{
W_{a,\pi}(t)
=
2i\operatorname{Im}Z_a(t).
}
\tag{6}
\]

Because

\[
\frac{W_{a,0}(t)}{W_{a,\pi}(t)}
=
i\,m_a(t),
\]

we have, away from zeros,

\[
\boxed{
m_a(t)
=
-
\frac{
\operatorname{Re}Z_a(t)
}{
\operatorname{Im}Z_a(t)
}.
}
\tag{7}
\]

Thus the real-axis sign observable can be read directly from the two real scalar carriers

\[
\operatorname{Re}Z_a,
\qquad
\operatorname{Im}Z_a.
\]

---

## 2. Exact common-zero criterion [D]

Suppose

\[
t\in\mathbb R.
\]

Equations (5)–(6) show

\[
W_{a,0}(t)=0
\quad\text{and}\quad
W_{a,\pi}(t)=0
\]

if and only if

\[
\operatorname{Re}Z_a(t)=0
\quad\text{and}\quad
\operatorname{Im}Z_a(t)=0.
\]

Since

\[
t-i\ne0
\]

for real \(t\),

\[
Z_a(t)=0
\iff
F_a(t)=0.
\]

Hence

\[
\boxed{
W_{a,0}(t)=W_{a,\pi}(t)=0
\iff
F_a(t)=0.
}
\tag{8}
\]

A common real characteristic zero is therefore a common Fourier-transform factor.

It is **not automatically** a zero or pole of the Weyl quotient after cancellation.

For the fixed-pair spectral-shift scalar, common factors must be cancelled before interpreting interlacing.

---

## 3. Why root-by-root certification is unnecessarily strict [D/I]

The scalar only depends on

\[
\sigma_a(t)
=
\operatorname{sgn}m_a(t).
\]

Suppose a numerical or interval computation certifies the sign on a closed set

\[
C\subset[0,T],
\]

but leaves an uncertain set

\[
U=[0,T]\setminus C
\]

around poorly separated roots, common factors, or error-bound crossings.

Define the certified phase contribution

\[
\boxed{
K_C
=
2\int_C
\sigma_a(t)
\frac{t}{(1+t^2)^2}\,dt.
}
\tag{9}
\]

On the uncertain set only the trivial bound

\[
|\sigma_a(t)|\le1
\]

is needed.

Therefore

\[
\boxed{
\left|
\kappa_a^\Xi-K_C
\right|
\le
2\int_U
\frac{t}{(1+t^2)^2}\,dt
+
\frac1{1+T^2}.
}
\tag{10}
\]

This is an exact certification theorem.

---

## 4. Exact cost of an uncertain interval [D]

For one uncertain interval

\[
[u,v]\subset[0,T],
\]

\[
2\int_u^v
\frac{t}{(1+t^2)^2}\,dt
=
\frac1{1+u^2}
-
\frac1{1+v^2}.
\]

Hence

\[
\boxed{
\operatorname{cost}[u,v]
=
\frac1{1+u^2}
-
\frac1{1+v^2}.
}
\tag{11}
\]

For a finite disjoint union

\[
U=\bigcup_j[u_j,v_j],
\]

the total uncertainty budget is simply

\[
\boxed{
\mathcal E_U
=
\sum_j
\left[
\frac1{1+u_j^2}
-
\frac1{1+v_j^2}
\right].
}
\tag{12}
\]

The final scalar enclosure is

\[
\boxed{
\kappa_a^\Xi
\in
\left[
K_C-\mathcal E_U-\frac1{1+T^2},
\;
K_C+\mathcal E_U+\frac1{1+T^2}
\right].
}
\tag{13}
\]

Thus unresolved high roots are cheap.

---

## 5. Interval-sign certification criterion [D]

Suppose on an interval \(I\subset[0,T]\) we have certified enclosures

\[
\operatorname{Re}Z_a(t)
\in
R_I(t),
\]

\[
\operatorname{Im}Z_a(t)
\in
J_I(t).
\]

If

\[
0\notin R_I(t)
\quad\text{and}\quad
0\notin J_I(t)
\]

throughout \(I\), then

\[
\boxed{
\sigma_a(t)
=
-
\operatorname{sgn}
\big(
\operatorname{Re}Z_a(t)
\big)
\operatorname{sgn}
\big(
\operatorname{Im}Z_a(t)
\big)
}
\tag{14}
\]

is certified on \(I\).

Whenever either enclosure intersects zero, that subinterval may simply be moved into \(U\) and charged through (11).

This gives a fail-closed scalar algorithm.

No exact root identification is necessary.

---

## 6. Source-faithful finite-section diagnostic [N]

The committed diagnostic uses the corrected \(a=1,\lambda=0\) source-faithful form-core matrices from v13.800.

For each cutoff:

1. solve the even and odd source systems once;
2. reconstruct the single transform
   \[
   F_N(t);
   \]
3. form
   \[
   W_{0,N},W_{\pi,N};
   \]
4. scan their real roots;
5. evaluate the phase sign ratio
   \[
   -W_{0,N}/(W_{\pi,N}/i).
   \]

These are numerical finite-section diagnostics only.

A truncated transform \(F_N\) does not automatically generate an exact Herglotz Weyl function.

---

## 7. Common-factor collapse in the raw Ritz characteristics [N/G]

At \(a=1,\lambda=0\), the increasing-cutoff scans show that the two raw characteristic approximants develop nearly common roots at the first Riemann-zero ordinates.

For example:

### \(N=28\)

Both channels contain, to displayed accuracy,

\[
14.134725141735,
\quad
21.022039638772,
\quad
25.010857580146,
\quad
30.42487612586,
\quad
32.93506158777.
\]

### \(N=32\)

The same five values agree between \(W_{0,N}\) and \(W_{\pi,N}\) to approximately \(12\)–\(14\) digits.

### \(N=36\)

The displayed first five roots again coincide:

\[
\boxed{
14.134725141735,
\;
21.022039638772,
\;
25.010857580146,
\;
30.424876125860,
\;
32.935061587739.
}
\tag{15}
\]

At \(N=48\), the common pattern continues through substantially higher ordinates before floating/truncation splitting becomes visible.

This is not evidence that the exact fixed extensions share those eigenvalues.

By (8), it is evidence that the truncated one-source transforms are developing a very strong common \(\Xi\)-like factor.

Therefore:

\[
\boxed{
\textbf{raw separate root lists are the wrong numerical observable unless common factors are cancelled.}
}
\tag{16}
\]

---

## 8. Relation to the parity defect [N/I]

The finite scalar is

\[
\kappa_{0,N}
=
\frac{
E_{e,N}-E_{o,N}
}{
E_{e,N}+E_{o,N}
}.
\]

At \(N=48\), the in-session source-faithful solve gave

\[
\boxed{
\kappa_{0,48}
\approx
0.99992759462203024555,
}
\tag{17}
\]

with

\[
\boxed{
\frac{E_{o,48}}{E_{e,48}}
\approx
3.62040\times10^{-5}.
}
\tag{18}
\]

Thus the odd source channel is tiny relative to the even one.

The apparent common characteristic factor is therefore consistent with the almost-purely-even finite response.

This observation is also consistent with the later v13.801 values

\[
\kappa_{0,64}
\approx
0.9999369812174818709,
\]

\[
\boxed{
\kappa_{0,96}
\approx
0.9999287562314239928.
}
\tag{19}
\]

So the \(a=1\) scalar appears much closer to \(1\) than to the asymptotic Xi target

\[
\kappa_\Xi
\approx
0.9968019520324009035.
\]

No \(a\to\infty\) inference is made from this fixed-\(a\) calculation.

---

## 9. Finite-section phase cross-check [N/G]

For the \(N=48\) truncated characteristic, the direct numerical sign-phase integration through

\[
T=100
\]

gave

\[
\boxed{
K_{48}^{\rm phase}(100)
\approx
0.9998715285962301.
}
\tag{20}
\]

The universal exact-operator tail scale at the same height is

\[
\boxed{
\frac1{1+100^2}
\approx
9.9990001\times10^{-5}.
}
\tag{21}
\]

The direct finite-section source scalar (17) differs from the truncated phase value by only

\[
\boxed{
\approx
5.61\times10^{-5}.
}
\tag{22}
\]

This is a useful internal consistency check.

It is **not** promoted to a rigorous exact-operator enclosure because the truncated \(F_N\) is not itself certified to be a Herglotz boundary-pair characteristic.

---

## 10. Why the phase route is still superior numerically [D/I]

The direct source computation subtracts two enormous parity responses.

At \(a=1\), v13.801 reports at \(N=96\)

\[
E_e
\approx
9.6900\times10^{28},
\]

\[
E_o
\approx
3.4519\times10^{24}.
\]

The scalar information is contained in their tiny relative imbalance.

The phase formulation instead asks only:

\[
\boxed{
\text{what is the sign of the real-axis Weyl ratio?}
}
\]

The amplitude of the huge resolvent response cancels.

Thus the phase route converts an ill-conditioned amplitude problem into a bounded sign-certification problem.

---

## 11. Deterministic target heights [D]

The universal tail budget alone gives:

\[
T=32
\quad\Longrightarrow\quad
\frac1{1+T^2}
=
\frac1{1025}
\approx
9.7561\times10^{-4},
\]

\[
T=50
\quad\Longrightarrow\quad
\frac1{2501}
\approx
3.9984\times10^{-4},
\]

\[
T=100
\quad\Longrightarrow\quad
\frac1{10001}
\approx
9.9990\times10^{-5}.
\]

Therefore a first useful exact finite-\(a\) certificate needs only a bounded real window.

Any unresolved subintervals add their explicit costs from (11).

---

## 12. Correct next numerical theorem target [O]

The next certification step is now sharply defined.

For one fixed \(a\):

1. obtain a residual-certified approximation
   \[
   \widehat v_a
   \approx
   A_a^{-1}e^x
   \]
   using the protected/Feshbach machinery;

2. propagate the solve residual to uniform enclosures for
   \[
   F_a(t)-\widehat F_a(t)
   \]
   on
   \[
   0\le t\le T;
   \]

3. convert those to interval enclosures for
   \[
   \operatorname{Re}Z_a(t),
   \qquad
   \operatorname{Im}Z_a(t);
   \]

4. certify signs wherever both intervals avoid zero;

5. place all unresolved pieces into \(U\);

6. apply (13).

The output is then a rigorous scalar interval

\[
\boxed{
\kappa_a^\Xi\in[\kappa_a^-,\kappa_a^+].
}
\]

Only after fixed-\(a\) certification is stable should the same construction be moved along increasing \(a\).

---

## 13. Analytic residual-to-transform bound [D]

Let

\[
r_a
=
e^x-A_a\widehat v_a
\]

be a source residual and assume a certified inverse-action bound

\[
\boxed{
\|A_a^{-1}r_a\|_{\mathcal H}
\le
\varepsilon_v.
}
\tag{23}
\]

For any real \(t\), let

\[
\ell_t(v)
=
\int_{-a}^{a}v(x)e^{itx}\,dx.
\]

If

\[
\|\ell_t\|_{\mathcal H^*}
\le
L_T
\qquad
(|t|\le T),
\]

then

\[
\boxed{
|F_a(t)-\widehat F_a(t)|
\le
L_T\varepsilon_v
\qquad
(|t|\le T).
}
\tag{24}
\]

Consequently

\[
\boxed{
|Z_a(t)-\widehat Z_a(t)|
\le
\sqrt{1+T^2}\,
L_T\varepsilon_v.
}
\tag{25}
\]

A single uniform transform-dual norm plus the protected source-solve residual therefore suffices to generate the sign intervals required in §12.

This is the exact bridge from the existing Feshbach certification machinery to the new phase certificate.

---

## 14. Strategic consequence [D/I]

The earlier plan was:

\[
\text{compute all low roots accurately}
\longrightarrow
\text{prove interlacing}
\longrightarrow
\kappa_a^\Xi.
\]

The correct robust route is weaker:

\[
\boxed{
\text{certify the sign ratio on most of }[0,T]
\longrightarrow
\text{charge unresolved windows}
\longrightarrow
\kappa_a^\Xi.
}
\]

This survives near-common factors and avoids over-resolving roots that carry negligible phase weight.

---

## 15. Result

The scalar certification problem has become a bounded-window interval-sign problem.

For any certified sign set

\[
C\subset[0,T]
\]

and uncertainty set

\[
U=[0,T]\setminus C,
\]

\[
\boxed{
\left|
\kappa_a^\Xi
-
2\int_C
\sigma_a(t)
\frac{t\,dt}{(1+t^2)^2}
\right|
\le
\sum_{[u_j,v_j]\subset U}
\left[
\frac1{1+u_j^2}
-
\frac1{1+v_j^2}
\right]
+
\frac1{1+T^2}.
}
\]

The raw \(a=1\) Ritz scan shows strong common-factor collapse and therefore confirms that common roots must be cancelled or fenced, not interpreted as fixed-pair interlacing data.

The next gate is to attach rigorous transform-error bounds to the protected source solve and produce the first certified finite-\(a\) interval for \(\kappa_a^\Xi\).
