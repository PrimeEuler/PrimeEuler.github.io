# Cone Derivation Ledger v13.501 — The U(24)/U(12) Double Cover Realized on the AM-GM Cone

## Scope

The mod-24 double cover of the mod-12 unit group,
\[
U(24)=\{1,5,7,11,13,17,19,23\}=A\times B,\qquad A=\{1,5,7,11\}\cong U(12),\quad B=\{1,13\}\cong C_2,
\]
with sheet action \(a\mapsto a\cdot13\equiv a+12\pmod{24}\), is already an exact, audited result — v13.226 (Mod-24 Boolean lift) and v13.228 §3–4 (direct-product structure, `H8=H4⊗H2` factorization, sheet-even `chi_12`). That work is entirely in Fourier/Walsh-Hadamard/DFT coordinates. No entry found there places `U(24)` on the AM-GM cone.

v13.500 realized the mod-12 unit shell `U(12)` exactly on the cone via the factor pairs `(r,1)`. This entry extends that same construction to all of `U(24)` and checks whether the already-proven double cover shows up as a clean geometric statement there. It does, and the reason is elementary — flagged explicitly in §3 so it isn't oversold.

No new algebraic theorem is claimed; v13.226/v13.228 remain the source of the double-cover fact itself. This entry only checks its coordinate realization.

---

## 1. The cone points for all of \(U(24)\)

Using the same construction as v13.500 — factor pair \((r,1)\) on \(\Pi_\pm(x,y)=\left(\frac{x-y}2,\pm\sqrt{xy},\frac{x+y}2\right)\) — for every \(r\in U(24)\):
\[
X_r=\frac{r-1}2,\qquad T_r=\frac{r+1}2,\qquad Y_r=\sqrt r.
\]

| \(r\) | sheet | \(X_r\) | \(T_r\) | \(Y_r^2\) |
|---|---|---|---|---|
| 1 | \(\varepsilon=0\) | 0 | 1 | 1 |
| 5 | \(\varepsilon=0\) | 2 | 3 | 5 |
| 7 | \(\varepsilon=0\) | 3 | 4 | 7 |
| 11 | \(\varepsilon=0\) | 5 | 6 | 11 |
| 13 | \(\varepsilon=1\) | 6 | 7 | 13 |
| 17 | \(\varepsilon=1\) | 8 | 9 | 17 |
| 19 | \(\varepsilon=1\) | 9 | 10 | 19 |
| 23 | \(\varepsilon=1\) | 11 | 12 | 23 |

Direct computation confirms the sheet-0 rows exactly reproduce v13.500's table, and the sheet-1 rows are new.

---

## 2. The sheet map is an exact uniform shift in \((X,T)\)

For each \(a\in A=\{1,5,7,11\}\), compare \(a\) and \(a+12\):
\[
X_{a+12}-X_a=\frac{(a+12)-1}2-\frac{a-1}2=6,\qquad
T_{a+12}-T_a=\frac{(a+12)+1}2-\frac{a+1}2=6,
\]
confirmed for all four pairs by direct computation:
\[
(1\to13),(5\to17),(7\to19),(11\to23)\ \longmapsto\ \Delta X=\Delta T=6\text{ in every case}.
\]
So the sheet involution \(a\mapsto a\cdot13\) (v13.228's \(B\)-action) acts on the cone's \((X,T)\) coordinates of the unit shell as the single uniform translation
\[
\boxed{(X,T)\longmapsto(X+6,\,T+6).}
\]
\(Y\) does not simply shift; \(Y_a^2=a\) becomes \(Y_{a+12}^2=a+12=Y_a^2+12\).

---

## 3. Guardrail: why this shift is automatic, not a hidden cone symmetry

This is worth stating precisely so it is not mistaken for new structure. In the \((r,1)\)-pair family, \(T_r-X_r=1\) identically, for *every* \(r\), not only totatives:
\[
T_r-X_r=\frac{r+1}2-\frac{r-1}2=1.
\]
For a cone point with \(T-X=1\) fixed, shifting \(r\mapsto r+\delta\) shifts \(X,T\) by \(\delta/2\) each (since both are affine in \(r\)) and shifts \(Y^2=r\) by exactly \(\delta\) (since \(Y^2=r\) is affine in \(r\) by construction). None of this requires \(r\) to be a unit, a totative, or related to 12 or 24 in any way — it is a generic property of the row/column-1 parametrization itself. Consistency with the cone equation is automatic and not evidence of an independent symmetry of \(X^2+Y^2=T^2\):
\[
(T_r+\delta/2)^2-(X_r+\delta/2)^2=T_r^2-X_r^2+\delta(T_r-X_r)=Y_r^2+\delta=Y_r^2+\delta,
\]
using \(T_r-X_r=1\), which is exactly \(Y_{r+\delta}^2\). So the "shift by 6" is nothing but the same linear-in-\(r\) parametrization evaluated at \(r+12\) instead of \(r\); it holds for a shift of 12 along the unit group precisely because \(\delta=12\) was chosen, not because 6 or 12 are cone-distinguished numbers. The genuine content here is not the shift itself but that it lands \(U(24)\)'s second sheet exactly on integer \((X,T)\) coordinates continuing the first sheet's pattern — which follows from \(A\subset U(12)\) already consisting of odd totatives (so \((r-1)/2,(r+1)/2\in\mathbb Z\)) and \(12\) being even.

---

## 4. Where the sheets sit relative to the fixed-sum circles

Sheet 0 (\(A\)) occupies \(T\in\{1,3,4,6\}\), terminating at \(T=6\) — the fixed-\(T\) circle for the antidiagonal \(x+y=12\), already the organizing circle of v13.499 §1. Sheet 1 (\(a+12\)) occupies \(T\in\{7,9,10,12\}\), terminating at \(T=12\) — the fixed-\(T\) circle for \(x+y=24\). So:
\[
\boxed{
\text{sheet 0}\subset\{T\le6\}\ (\text{bounded by }K{=}12),\qquad
\text{sheet 1}\subset\{6<T\le12\}\ (\text{bounded by }K{=}24).
}
\]
The algebraic double cover \(U(24)\to U(12)\) (kernel \(B=\{1,13\}\), v13.228 §3) corresponds, in this cone realization, to the row/column-1 unit-shell family advancing from the \(K=12\) boundary circle to the \(K=24\) boundary circle, with the same four totative labels \(\sqrt1,\sqrt5,\sqrt7,\sqrt{11}\) reappearing as \(\sqrt{13},\sqrt{17},\sqrt{19},\sqrt{23}\) on the outer sheet.

---

## 5. Summary

| Fact | Status |
|---|---|
| \(U(24)=A\times B\), \(a\mapsto a+12\) sheet action | Already proven, v13.228 §3 |
| Sheet-even \(\chi_{12}\), \(H_8=H_4\otimes H_2\) factorization | Already proven, v13.228 §4–5 |
| Cone realization of \(U(12)\) via \((r,1)\) pairs | Already proven, published paper §"mod-12 unit shell", re-verified in v13.500 |
| Cone realization of \(U(24)\), sheet action \(=\) translation \((X,T)\mapsto(X+6,T+6)\) | **New in this entry**, verified directly |
| That translation is a generic consequence of \(T_r-X_r\equiv1\), not a special cone symmetry | Flagged explicitly, §3 |
| Sheets bounded by the \(K=12\) and \(K=24\) fixed-sum circles respectively | **New in this entry**, verified directly |

## Guardrail

This entry adds a coordinate picture to an already-proven algebraic fact; it does not strengthen, extend, or reinterpret the double-cover theorem of v13.228 itself, and it makes no claim about the Suzuki or A3 threads. Any further claim that this geometric picture is *useful* (e.g. for the Suzuki mod-24 diagnostics of v13.430/v13.432/v13.433) needs its own separate derivation.
