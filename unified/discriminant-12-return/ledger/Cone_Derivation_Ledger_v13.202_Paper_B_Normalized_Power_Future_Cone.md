# Cone Derivation Ledger v13.202 — Paper B Normalized Power Map and Future-Cone Audit

Status: **[D] exact refinement / [Audit] publication correction**

Date: 2026-09-03

Source audited:

`foundations/PaperB_EigenCoordinates_v2.tex`

CI status at start of this audit: the v2 source compiled successfully to a 7-page PDF, and `PaperB_EigenCoordinates_v2.pdf` is present on `master`.

---

## 1. Question left open by v13.201

The first Paper-B audit repaired the signed-sheet orbit statement and the normalization dependence of the raw power construction.  One further issue remained:

> the reconstruction proves the null-cone equation, but does it automatically land on the **future** cone rather than the past cone?

The answer is yes after the natural sign normalization of the cutting equation.  That sign normalization also exposes a cleaner projectively invariant eigen-coordinate power map.

---

## 2. [D] Factor-coordinate form of the two plane functionals

Set

\[
P=(a+b)X+(a-b)T,
\qquad
Q=(a-b)X+(a+b)T.
\]

Using

\[
x=T+X,
\qquad
y=T-X,
\]

one gets exactly

\[
\boxed{P=ax-by,\qquad Q=ax+by.}
\]

On the cut, \(Q=c\).

This identity is the simplest way to audit the sign of the reconstructed factor coordinates.

---

## 3. [D] Elliptic sign normalization and future preservation

Suppose \(ab>0\) and the line meets the positive factor quadrant.  Multiplying the equation by \(-1\) if necessary, one may and should normalize

\[
\boxed{a>0,\qquad b>0,\qquad c>0.}
\]

The remaining rescaling freedom is then only positive scaling.

On the signed future cone, \(x,y\ge0\) and \(Y=\pm\sqrt{xy}\).  The complex eigen-coordinate is

\[
\zeta=P+2i\sqrt{ab}\,Y
=ax-by+2i\sqrt{ab}\,Y.
\]

Let

\[
u=\sqrt{ax},
\qquad
v=\operatorname{sgn}(Y)\sqrt{by}.
\]

Then

\[
\boxed{\zeta=(u+iv)^2.}
\]

Also

\[
Q=ax+by=u^2+v^2=c,
\]

so

\[
|\zeta|=u^2+v^2=c.
\]

For integer \(n\ge1\), write

\[
\zeta^n=P_n+iR_n.
\]

Because

\[
|P_n|\le |\zeta^n|=c^n,
\]

the reconstruction

\[
ax_n=\frac{c^n+P_n}{2},
\qquad
by_n=\frac{c^n-P_n}{2}
\]

gives

\[
\boxed{x_n\ge0,\qquad y_n\ge0.}
\]

Therefore

\[
T_n=\frac{x_n+y_n}{2}\ge0.
\]

Since \(c>0\), the reconstructed point is not the apex, hence \(T_n>0\).

Thus:

\[
\boxed{
\text{under }a,b,c>0,
\text{ the elliptic power reconstruction preserves the signed future cone.}
}
\]

This should be stated explicitly in Paper B.

---

## 4. [D] Hyperbolic sign normalization and square factorization

Suppose \(ab<0\).  Multiplying the equation by \(-1\) if necessary, normalize

\[
\boxed{a>0>b.}
\]

Write

\[
\beta=-b>0,
\qquad
r=\sqrt{a\beta}=\sqrt{-ab}.
\]

Then

\[
P=ax-by=ax+\beta y,
\qquad
Q=ax+by=ax-\beta y=c.
\]

On the signed future cone set

\[
u=\sqrt{ax},
\qquad
v=\operatorname{sgn}(Y)\sqrt{\beta y}.
\]

The split eigen-coordinates factor exactly as

\[
\boxed{
\eta_+=(u+v)^2,
\qquad
\eta_-=(u-v)^2.
}
\]

Hence

\[
\boxed{\eta_+\ge0,\qquad \eta_-\ge0}
\]

throughout the signed future cone, and

\[
\eta_+\eta_-=c^2.
\]

For integer \(n\ge1\), define

\[
P_n=\frac{\eta_+^n+\eta_-^n}{2},
\qquad
Q_n=c^n.
\]

By AM--GM,

\[
P_n\ge\sqrt{\eta_+^n\eta_-^n}=|c|^n=|Q_n|.
\]

Therefore

\[
ax_n=\frac{P_n+Q_n}{2}\ge0,
\]

and

\[
\beta y_n=\frac{P_n-Q_n}{2}\ge0.
\]

Thus

\[
\boxed{x_n,y_n\ge0,\qquad T_n>0}
\]

for every nondegenerate hyperbolic cut \(c\ne0\), irrespective of the sign of \(c\) or the parity of \(n\).

So the hyperbolic power reconstruction also preserves the signed future cone after the natural orientation \(a>0>b\) is fixed.

---

## 5. [D] A cleaner projectively invariant normalization

The raw power map in v2 is attached to a chosen equation because

\[
(a,b,c)\mapsto(\kappa a,\kappa b,\kappa c)
\]
rescales the eigen-coordinate before powering.

After fixing the natural orientation above, only \(\kappa>0\) remains.  This positive scaling can be removed from the **shape coordinate**.

### Elliptic case

Define

\[
\boxed{z=\frac{\zeta}{c}.}
\]

Under \(a,b,c\mapsto(\kappa a,\kappa b,\kappa c)\) with \(\kappa>0\),

\[
\zeta\mapsto\kappa\zeta,
\qquad
c\mapsto\kappa c,
\]

so

\[
\boxed{z\text{ is invariant under positive equation rescaling}.}
\]

Moreover

\[
|z|=1.
\]

Thus

\[
\boxed{z\mapsto z^n}
\]

is a canonical power map of the **normalized ellipse shape coordinate**.

### Hyperbolic case

Since \(c\) may have either sign, use

\[
\boxed{\xi_\pm=\frac{\eta_\pm}{|c|}.}
\]

Then

\[
\xi_\pm\ge0,
\qquad
\boxed{\xi_+\xi_-=1},
\]

and \(\xi_\pm\) are invariant under positive equation rescaling.  Therefore

\[
\boxed{\xi_\pm\mapsto\xi_\pm^n}
\]

is the projectively normalized split power map.

This separates two logically distinct operations:

1. **shape dynamics:** \(z\mapsto z^n\) or \(\xi_\pm\mapsto\xi_\pm^n\), which is scale-invariant after orientation normalization;
2. **level assignment:** choosing the right-hand side of the target cut, e.g. \(c\mapsto c^n\), which is an additional scalar convention.

This is cleaner than calling the whole unnormalized map either canonical or noncanonical without qualification.

---

## 6. [D] Canonically normalized generator

The same refinement applies to the continuous flow.

For \(ab>0\), define

\[
\boxed{
\widehat G_{a,b}
=\frac{G_{a,b}}{2\sqrt{ab}}.
}
\]

For \(ab<0\), define

\[
\boxed{
\widehat G_{a,b}
=\frac{G_{a,b}}{2\sqrt{-ab}}.
}
\]

Under positive common scaling \((a,b)\mapsto(\kappa a,\kappa b)\), both numerator and denominator scale by \(\kappa\).  Hence

\[
\boxed{\widehat G_{\kappa a,\kappa b}=\widehat G_{a,b}.}
\]

The nonzero eigenvalues of \(\widehat G\) are then

\[
\pm i
\]

in the elliptic case and

\[
\pm1
\]

in the hyperbolic case.

Thus the oriented projective cut direction determines not merely an orbit subgroup up to time rescaling, but a natural unit-frequency/unit-rapidity generator.

This normalization fails at \(ab=0\), exactly where the parabolic degeneration occurs.

---

## 7. [D] Normalized semiconjugacy

With the normalized generator, the eigen-coordinate flow is

\[
z(t)=e^{it}z(0)
\]

in the elliptic case, while

\[
\xi_\pm(t)=e^{\pm t}\xi_\pm(0)
\]

in the hyperbolic case.

Therefore the power map obeys the scale-free semiconjugacy

\[
\boxed{
\Psi_n\circ\widehat{\operatorname{flow}}_t
=\widehat{\operatorname{flow}}_{nt}\circ\Psi_n.
}
\]

This is invariant under positive rescaling of the original line equation.

---

## 8. [Audit] recommended change to Paper B v2

Paper B v2 is mathematically much safer than the original, but the next revision should make the following distinction explicit:

- choose the natural sign orientation:
  - ellipse: \(a,b,c>0\);
  - hyperbola: \(a>0>b\), with \(c\ne0\) arbitrary;
- prove future-cone preservation using the formulas above;
- introduce normalized shape coordinates \(z=\zeta/c\) and \(\xi_\pm=\eta_\pm/|c|\);
- introduce the normalized generator \(\widehat G\);
- call the shape power map canonical for the oriented projective cut direction;
- call \(c\mapsto c^n\) a separate **level-lift convention**.

This makes the conceptual structure sharper:

\[
\boxed{
\text{projective cut direction}
\longrightarrow
\widehat G
\longrightarrow
\text{unit eigen-coordinate flow}
\longrightarrow
\text{canonical shape power }z\mapsto z^n.
}
\]

The scalar cut level is then carried separately.

---

## 9. [I] fit with the broader Cone architecture

This refinement improves the connection to the discriminant-12 paper.  The continuous Lorentz geometry naturally splits into:

- **direction / rapidity geometry**, independent of arbitrary equation scale;
- **level / shell data**, carried by a separate scalar.

The discriminant-12 return likewise has a distinguished rapidity increment

\[
R_{12}=\log(2+\sqrt3)
\]

acting on the common rapidity coordinate \(s\).

No claim is made that \(\widehat G_{a,b}\) equals the arithmetic return generator.  The point is only that both now live cleanly on the same scale-free continuous rapidity carrier.

---

## 10. Verdict

**[D] New exact results:**

\[
\zeta=(\sqrt{ax}+i\,\operatorname{sgn}(Y)\sqrt{by})^2
\quad(a,b>0),
\]

\[
\eta_\pm=(\sqrt{ax}\pm\operatorname{sgn}(Y)\sqrt{-by})^2
\quad(a>0>b),
\]

future-cone preservation of integer eigen-coordinate powers, projectively normalized eigen-coordinates, and the scale-invariant normalized generator \(\widehat G\).

**[Audit] Paper B v2 should be advanced to v2.1 before being considered stable.**

The required revision is conceptual rather than a retreat: the power map becomes stronger once its scale-invariant shape component is separated from the chosen scalar level lift.
