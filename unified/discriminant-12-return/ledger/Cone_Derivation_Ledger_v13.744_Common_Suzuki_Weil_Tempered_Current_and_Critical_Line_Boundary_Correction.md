# Cone Derivation Ledger v13.744 — Common Suzuki–Weil Tempered Current and Critical-Line Boundary-Value Correction

**Date:** 2026-09-23  
**Status:** exact common distributional normalization at the source level; correction of an overstrong critical-line multiplier claim; no RH/Hilbert–Pólya promotion  
**Parents:** v13.734–739, v13.741–743  
**Synchronization:** live head before write was v13.743 (`aa0f33c8...`). Round 88 (v13.741) passed v13.739 but found a source contradiction in v13.740; v13.742–743 correct that finite-edge lane. This entry does not use the invalid v13.740 finite deficiency ansatz and does not duplicate the corrected finite-edge work.

## 1. Provenance boundary

Import without rederivation:

- [S] Suzuki's source-checked Section-2.5 distribution (-g'') from v13.735/v13.738.
- [C] centered Weil half-density normalization from v13.734.
- [C] norm-line carrier and Tate logarithmic current from v13.730–736.
- [X] Section-7 (E,T_{\rm pair}=C_\xi\Xi(-iz)) and its logarithmic split from v13.737/v13.739.

The v13.742–743 finite-edge correction is orthogonal to the present full-line distribution gate.

## 2. One common tempered distribution

With Suzuki's notation, define the full-line current
[
\boxed{\mathscr W_S(r):=-g''(r).}
]
The audited source identity is
[
\boxed{
\mathscr W_S(r)=
-\frac12\operatorname{Pf}\frac1{|r|}
-(2A+1)\delta_0
-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
[\delta(r-\log n)+\delta(r+\log n)]
-r''_{\rm arch}(r).
}
]
Here (A=\tfrac12(\log(2\pi)+\gamma-1)) in Suzuki's normalization.

The finite arithmetic term is exactly the negative of the v13.734 centered Weil prime distribution:
[
\boxed{
\mathscr W_{S,{\rm fin}}
=
-\mu^{\rm fin}_{\rm Weil}.
}
]
Thus the prime support and half-density weights are no longer merely analogous: they agree term-by-term, with the displayed sign fixed by Suzuki's (-g'') convention.

The remaining terms are the required origin finite-part/contact and archimedean completion. Equality of a differently normalized cone/Weil *full* distribution with (\mathscr W_S) is to be asserted only after those local terms are matched in the same finite-part convention.

## 3. Fourier-side symbol

Use
[
\widehat f(t)=\int_{\mathbb R}f(r)e^{itr},dr.
]
Distributional differentiation gives
[
\boxed{
\widehat{\mathscr W_S}(t)=t^2\widehat g(t).
}
]
This is the rigorous full-line Fourier symbol furnished by Suzuki. It is a tempered distribution; it is not to be replaced without proof by an ordinary scalar function.

Formally transforming the finite arithmetic train gives
[
-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\cos(t\log n),
]
but this series is not absolutely convergent on the critical half-density line. It is only a mnemonic for the regularized/distributional finite-place contribution.

For (\sigma>1), the absolutely convergent regulator is
[
m_\sigma(t)
:=
-\sum_{n\ge2}\Lambda(n)n^{-\sigma}
(e^{it\log n}+e^{-it\log n}),
]
hence
[
\boxed{
m_\sigma(t)
=
\frac{\zeta'}{\zeta}(\sigma-it)
+
\frac{\zeta'}{\zeta}(\sigma+it)
=
2\Re\frac{\zeta'}{\zeta}(\sigma+it).
}
]
The centered (n^{-1/2}) distribution is reached by analytic/distributional continuation, not by an absolutely convergent substitution (\sigma=1/2).

## 4. Correction: the full Weil distribution is not (2\Re L(1/2+0^++it))

A previous exploratory gate stated too strongly that the full centered Weil multiplier could be identified with
[
2\Re L(1/2+0^++it),
\qquad L=\xi'/\xi,
]
and that its singular part was the full zero measure.

That statement is **not established and is false as a general unconditional identification**.

Reason: a zero
[
\rho=\beta+i\gamma
]
produces a pole of (L(1/2+it)) on the real (t)-axis only when
[
\boxed{\beta=1/2.}
]
If (\beta\ne1/2), the corresponding pole lies off the real (t)-axis. Therefore a real-axis boundary-value delta decomposition of (L) can directly detect only critical-line zeros. Identifying it with the complete zero side of Weil's explicit formula would silently assume precisely the spectral localization that is not proved.

Hence freeze the correction:
[
\boxed{
\widehat{\mathscr W_S}=t^2\widehat g
\quad\text{is established;}
\qquad
\widehat{\mathscr W_S}\stackrel{?}{=}2\Re L(1/2+0^++it)
\quad\text{is not established.}
}
]

## 5. What remains exactly true for (L)

From the functional equation,
[
L(s)=-L(1-s).
]
For real (t), wherever (L) is regular on the critical line,
[
L(1/2-it)=\overline{L(1/2+it)}=-L(1/2+it),
]
so
[
\boxed{\Re L(1/2+it)=0}
]
away from critical-line poles.

This vanishing is a further warning that the full explicit-formula distribution cannot be represented by the ordinary function (2\Re L) on the line.

The safe logarithmic identity is instead the meromorphic centered-variable identity
[
\boxed{
L(1/2+w)=\frac{\Xi'(w)}{\Xi(w)}
}
]
for complex (w), together with the contour/test-function form of the explicit formula. All zeros, including hypothetical off-line zeros, are retained by contour displacement/residues in the complex (w)-plane.

## 6. Compatibility with the Suzuki (E/T_{\rm pair}) factorization

The cross-lane identity remains exact as a meromorphic identity:
[
E(z)T_{\rm pair}(z)=C_\xi\Xi(-iz).
]
Therefore
[
\boxed{
-iL(1/2-iz)
=
\frac{T'_{\rm pair}(z)}{T_{\rm pair}(z)}
+
\frac{E'(z)}{E(z)}.
}
]
This is not a claim that (L) itself is the Fourier transform of (-g''). Rather:

- (-g'') is the source-side Weil/screw tempered current;
- (t^2\widehat g(t)) is its exact Fourier symbol;
- (L=\Xi'/\Xi) is the meromorphic logarithmic derivative of the positive-kernel transform;
- Suzuki's (E/T_{\rm pair}) identity factorizes that meromorphic transform.

The bridge between the first two bullets and the last two is Weil's explicit formula/contour pairing, not pointwise equality of multipliers.

## 7. Exact common diagram

The source-faithful picture is therefore
[
\boxed{
\begin{array}{ccc}
\mathscr W_S=-g''
&\xrightarrow{\mathcal F}&
t^2\widehat g(t)
\\[1mm]
\Updownarrow\;\text{explicit-formula data}
&&
\text{tempered/distributional symbol}
\\[1mm]
\text{centered Weil current}
&&
\\[3mm]
\Phi
&\xrightarrow{\mathcal B}&
\Xi
\xrightarrow{\partial\log}
L=\Xi'/\Xi
\\
&&
\Xi(-iz)=C_\xi^{-1}E(z)T_{\rm pair}(z).
\end{array}
}
]
The vertical relation is an explicit-formula pairing/normalization statement, not a proved linear Fourier intertwiner (\mathscr W_S\leftrightarrow\Phi).

## 8. Updated no-rederive / open registry

**ESTABLISHED:** Suzuki and centered Weil finite prime trains coincide term-by-term up to Suzuki's overall minus sign.

**ESTABLISHED:** the exact screw/Weil source object is tempered and has Fourier symbol (t^2\widehat g).

**ESTABLISHED:** (L=\Xi'/\Xi) and the (E/T_{\rm pair}) logarithmic decomposition are meromorphic identities.

**RETRACTED AS OVERSTRONG:** full zero measure (=2\Re L(1/2+0^++it)) on the real Fourier axis.

**OPEN:** an exact formula expressing (t^2\widehat g) directly in terms of boundary values/jumps of completed logarithmic derivatives with all contour prescriptions explicit.

**OPEN:** full local normalization match between Suzuki's Pf/contact/archimedean remainder and the cone lane's anchored (W_\infty) finite-part convention.

**OPEN:** finite-(A) edge convergence remains in the corrected Suzuki lane v13.742–743.

## 9. Next nonredundant gate

Match the two archimedean/origin regularizations explicitly:

1. expand Suzuki's
[
-\frac12\operatorname{Pf}|r|^{-1}-(2A+1)\delta_0-r''_{\rm arch}(r)
]
against the cone/Tate gamma current;
2. compute their Fourier transforms under one fixed finite-part convention;
3. isolate any residual contact constant;
4. only then state a full equality of the Suzuki and cone-centered Weil distributions.

This is the shortest route to a single canonical common current without importing any finite-edge assumption.
