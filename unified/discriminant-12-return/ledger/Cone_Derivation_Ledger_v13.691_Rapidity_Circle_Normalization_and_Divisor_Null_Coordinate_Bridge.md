# Cone Derivation Ledger v13.691 — Rapidity/Circle Normalization and Divisor Null-Coordinate Bridge

Date: 2026-09-22

Status labels: **[S]** source-established, **[D]** exact derived, **[I]** interpretation, **[O]** open, **[Audit]** guardrail.

## 1. Collision and foundation check

[S] Immediately before this write, the live head of the ledger was v13.690 (commit \`9b3d54f38f420900409f06286e2f7b63a0525afc\`); no v13.691 collision was present.

[S] The active foundation chain was checked directly. The relevant established checkpoints are:

- v13.196 / \`foundations/Note_AreaDistortion_AMGM_Cone_v1.1.tex\`: product-ratio coordinates and the exact real rapidity-to-circle compactification;
- v13.202 and v13.214 / \`foundations/PaperB_EigenCoordinates_v2.1.tex\`: normalized elliptic and split eigen-coordinates, with intrinsic normal forms \`|z|=1\` and \`\xi_+\xi_-=1\`;
- v13.409 / \`research-notes/Cone_Shell_Rays_and_General_Discriminant_Return.md\`: exact identification of the old divisor-shell \`v_k,T_k\` construction with the Paper-A cone shell.

This entry does not replace those results. It reconciles them with the harmonic-mean and divisor continuation frozen in v13.690.

## 2. Fixed-product shell in the established rapidity coordinate

[D] Let
\[
xy=n>0,\qquad
s=\frac12\log\frac{x}{y}.
\]
Then
\[
x=\sqrt n\,e^s,\qquad
y=\sqrt n\,e^{-s}.
\]
In Paper-A cone coordinates
\[
T=\frac{x+y}{2},\qquad
X=\frac{x-y}{2},\qquad
Y=\sqrt{xy},
\]
this gives
\[
\boxed{
T=\sqrt n\cosh s,\qquad
X=\sqrt n\sinh s,\qquad
Y=\sqrt n.
}
\]
Hence
\[
T^2-X^2=n,\qquad T^2=X^2+Y^2.
\]

The two null coordinates are exactly
\[
\boxed{T+X=\sqrt n\,e^s=x,\qquad T-X=\sqrt n\,e^{-s}=y.}
\]

## 3. The real circle compactification and its normalized complex coordinate

[S/D] v13.196 gives the real geometric compactification
\[
X=T\sin\theta,\qquad Y=T\cos\theta,
\]
with
\[
\boxed{
\sin\theta=\tanh s,\qquad
\cos\theta=\operatorname{sech}s,\qquad
d\theta=\operatorname{sech}s\,ds.
}
\]

[D] Therefore the normalized circle point can be written as
\[
\boxed{
z_{\rm geom}(s)
:=\frac{Y+iX}{T}
=\operatorname{sech}s+i\tanh s
=e^{i\theta(s)}.
}
\]
It has unit norm identically:
\[
|z_{\rm geom}(s)|^2
=\operatorname{sech}^2s+\tanh^2s=1.
\]

[D] The half-angle formula is
\[
\boxed{\tan\frac{\theta}{2}=\tanh\frac{s}{2},}
\]
so the same map has the Cayley form
\[
\boxed{
z_{\rm geom}(s)
=
\frac{1+i\tanh(s/2)}{1-i\tanh(s/2)}.
}
\]

This is the normalized complex coordinate naturally attached to the **real** cone projection of a real rapidity shell.

## 4. Distinguish real compactification from analytic continuation

[Audit] Two mathematically valid maps must not be conflated.

### 4.1 Real geometric compactification

For real \(s\),
\[
s\longmapsto\theta(s),\qquad
\theta'(s)=\operatorname{sech}s,
\]
and
\[
z_{\rm geom}(s)=e^{i\theta(s)}
=\operatorname{sech}s+i\tanh s.
\]
This is nonlinear in \(s\) and maps
\[
\mathbb R\longrightarrow
\{\Re z>0,\ |z|=1\},
\]
with \(s\to\pm\infty\) approaching the endpoints \(\pm i\).

### 4.2 Analytic continuation / elliptic exponential

Independently, complexifying the hyperbolic parameter gives
\[
s\mapsto i\varphi,
\]
so
\[
\cosh(i\varphi)=\cos\varphi,\qquad
\sinh(i\varphi)=i\sin\varphi,
\]
and the split exponential pair
\[
(e^s,e^{-s})
\]
becomes
\[
(e^{i\varphi},e^{-i\varphi}).
\]

Paper B's normalized nonparabolic orbit coordinates realize the same compact/split dichotomy intrinsically:
\[
\boxed{|z|=1}
\qquad\text{versus}\qquad
\boxed{\xi_+\xi_-=1},
\]
with normalized flows
\[
z(t)=e^{it}z(0),
\qquad
\xi_\pm(t)=e^{\pm t}\xi_\pm(0).
\]

[Audit] The real map \(\theta=\theta(s)\) is **not** the substitution \(s=i\theta\). The former is a real compactifying change of coordinates; the latter is analytic continuation. Their common exponential/circle language is structural, not an equality of the two maps.

## 5. Pythagorean means become the real compactification coordinates

[D] On the same shell define
\[
A=\frac{x+y}{2}=T,\qquad
D=\frac{x-y}{2}=X,\qquad
G=\sqrt{xy}=Y,
\]
and harmonic mean
\[
H_{\rm harm}=\frac{2xy}{x+y}.
\]
Then
\[
A^2=D^2+G^2,\qquad
A H_{\rm harm}=G^2.
\]

Using the rapidity parameter,
\[
A=\sqrt n\cosh s,\qquad
D=\sqrt n\sinh s,\qquad
G=\sqrt n,
\]
and therefore
\[
\boxed{H_{\rm harm}=\sqrt n\,\operatorname{sech}s.}
\]

Combining with the real compactification gives the exact normalized dictionary
\[
\boxed{
\frac DA=\tanh s=\sin\theta,
\qquad
\frac GA=\operatorname{sech}s=\cos\theta,
}
\]
and
\[
\boxed{
\frac{H_{\rm harm}}G
=\frac GA
=\cos\theta,
\qquad
\frac{H_{\rm harm}}A
=\cos^2\theta.
}
\]

Thus
\[
\left(\frac DA\right)^2+\left(\frac GA\right)^2=1
\]
is literally
\[
\sin^2\theta+\cos^2\theta=1,
\]
while \(AH_{\rm harm}=G^2\) becomes the squared vertical circle coordinate.

[D] There is also an exact differential bridge:
\[
d\theta=\operatorname{sech}s\,ds
=\frac{H_{\rm harm}}{\sqrt n}\,ds,
\]
hence
\[
\boxed{H_{\rm harm}\,ds=\sqrt n\,d\theta.}
\]

## 6. Divisor boundary samples are intersections of a product shell with null-coordinate parabolas

[D] For integer \(n\ge1\) and \(k=1,\dots,n\), take the real boundary point
\[
(x_k,y_k)=\left(k,\frac nk\right)
\]
on \(xy=n\). It need not be an integer divisor pair; the floor operation will impose the lattice discretization.

Its cone coordinates are
\[
\boxed{
T_k=\frac12\left(k+\frac nk\right),\qquad
X_k=\frac12\left(k-\frac nk\right),\qquad
Y_k=\sqrt n.
}
\]
Therefore
\[
\boxed{
T_k+X_k=k,\qquad
T_k-X_k=\frac nk.
}
\]

Geometrically, the fixed-product shell \(Y^2=n\) intersects the fixed-null-coordinate row/column parabola \(T+X=k\) at precisely this point. In the \((Y,T)\) projection that parabola is
\[
Y^2=k(2T-k).
\]

## 7. Exact identification of the old GeoGebra variable with the cone odd coordinate

[D] The earlier divisor construction used
\[
v_k=\frac{n-k^2}{2k}
=\frac12\left(\frac nk-k\right).
\]
The preceding cone coordinate gives immediately
\[
\boxed{v_k=-X_k.}
\]

This is stronger than a visual correspondence: the old signed divisor variable is exactly the mirror-odd cone coordinate, up to orientation convention.

Define, to avoid collision with arithmetic mean \(A\),
\[
\mathcal A_{\rm div}(n):=2\sum_{k=1}^n v_k.
\]
Then
\[
\boxed{
\mathcal A_{\rm div}(n)
=-2\sum_{k=1}^n X_k
=nH_n-T_n,
}
\]
where
\[
H_n=\sum_{k=1}^n\frac1k,
\qquad
T_n=\frac{n(n+1)}2.
\]

Equivalently,
\[
\boxed{
nH_n=\sum_{k=1}^n(T_k-X_k),
\qquad
T_n=\sum_{k=1}^n(T_k+X_k).
}
\]
Hence
\[
\boxed{
\sum_{k=1}^nT_k=\frac{nH_n+T_n}{2},
\qquad
\sum_{k=1}^nX_k=\frac{T_n-nH_n}{2}.
}
\]

## 8. The divisor summatory function is the floored null-coordinate sum

[D] Since
\[
T_k-X_k=\frac nk,
\]
the classical identity becomes
\[
\boxed{
D(n)
=\sum_{k=1}^n\left\lfloor\frac nk\right\rfloor
=\sum_{k=1}^n\lfloor T_k-X_k\rfloor.
}
\]

Therefore
\[
\boxed{
nH_n-D(n)
=
\sum_{k=1}^n\{T_k-X_k\}.
}
\]

Because \(v_k=-X_k=n/(2k)-k/2\), and subtraction of \(k/2\) does not change a remainder modulo \(1/2\),
\[
\boxed{
2\left(v_k\bmod\frac12\right)
=\left\{\frac nk\right\}.
}
\]
Thus, with
\[
\mathcal B_{\rm div}(n)
:=2\sum_{k=1}^n\left((-X_k)\bmod\frac12\right),
\]
we obtain
\[
\boxed{
\mathcal B_{\rm div}(n)=nH_n-D(n).
}
\]

Finally,
\[
\boxed{
T_n-D(n)
=
\mathcal B_{\rm div}(n)-\mathcal A_{\rm div}(n).
}
\]
The left side is the project's previously recorded OEIS A161664 quantity.

## 9. Continuous \(n\log n\) and discrete \(nH_n\) now occupy the same rapidity/null-coordinate carrier

[D] Along \(xy=n\),
\[
y=\frac nx=\sqrt n\,e^{-s},
\qquad
dx=x\,ds,
\]
so
\[
y\,dx=n\,ds.
\]
For \(x:1\to n\), rapidity runs
\[
s:-\frac12\log n\to+\frac12\log n.
\]
Therefore
\[
\boxed{
n\log n
=
n\int_{-\frac12\log n}^{+\frac12\log n}ds.
}
\]

By contrast,
\[
\boxed{
nH_n
=
\sum_{k=1}^n(T_k-X_k)
}
\]
is the discrete sampling of the oriented null coordinate \(y=T-X=n/k\), and
\[
\boxed{
D(n)
=
\sum_{k=1}^n\lfloor T_k-X_k\rfloor
}
\]
is its lattice quantization by flooring.

[I] This gives a precise hierarchy on one fixed-product cone shell:

- \(n\log n\): continuous rapidity measure;
- \(nH_n\): discrete unrounded null-coordinate sum;
- \(D(n)\): floored/lattice null-coordinate sum;
- \(nH_n-D(n)\): total fractional remainder;
- \(T_n-D(n)\): difference between the wrapped and unwrapped odd-coordinate sums.

## 10. Mirror quotient and why the odd coordinate is still needed

[D/I] Under factor exchange,
\[
X\mapsto-X,\qquad x\leftrightarrow y.
\]
The shell quantities \(A=T\), \(G=Y\), and \(H_{\rm harm}=Y^2/T\) are mirror-even, while \(D=X\) is mirror-odd.

The real circle compactification likewise satisfies
\[
s\mapsto-s,\qquad
\theta\mapsto-\theta,\qquad
z_{\rm geom}\mapsto\overline{z_{\rm geom}}.
\]

The harmonic mean therefore descends to the mirror quotient. But the divisor-column quantity is the **oriented** null coordinate
\[
T-X=\frac nk.
\]
After forgetting the sign/orientation of \(X\), one no longer knows whether the relevant null coordinate is \(T-X\) or \(T+X\).

[I] This cleanly separates roles:

- \(H_{\rm harm}\) records the mirror-even fixed-product/circular compression;
- \(X=D\) records row-versus-column orientation;
- \(D(n)\) requires the oriented null coordinate and therefore cannot be reconstructed from \(H_{\rm harm}\) alone.

No arithmetic-character identification is asserted from this parity observation.

## 11. Publication guardrails

1. Keep harmonic number \(H_n\) and harmonic mean \(H_{\rm harm}\) typographically and conceptually distinct.
2. Do not identify the real compactification \(\theta(s)\) with analytic continuation \(s\mapsto i\theta\).
3. Do not identify Paper A's ordinary circle complex coordinate, Paper B's general elliptic eigen-coordinate, and the later discriminant-12 cyclotomic operator as the same object. They are exact related layers with different constructions.
4. The formulas for \(D(n)\), \(nH_n\), \(\mathcal A_{\rm div}\), and \(\mathcal B_{\rm div}\) are exact classical/cone identities. They do not imply that a Lorentz/Pell boost acts on the integer divisor lattice.
5. No Suzuki/RH claim follows from this checkpoint.

## 12. Controlled continuation

The next useful gates are:

1. Rewrite the existing \(n=11\) divisor-summatory three-view construction as an exact four-view dictionary: fixed-product horizontal/secant level, \(X\)-\(T\) hyperbola, fixed-null-coordinate parabolas, and 3D cone intersections.
2. Test whether the normalized real compactification coordinate
\[
z_{\rm geom}(s)=\operatorname{sech}s+i\tanh s
\]
is a special case, conjugate, or distinct normalization of Paper B's intrinsic elliptic coordinate for the relevant fixed-\(T\) cuts; record the exact transformation rather than relying on analogy.
3. Only after those checks, decide whether any foundation-paper revision is warranted. No foundation source is changed by this ledger entry.
