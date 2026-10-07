# Cone Derivation Ledger v14.132 — Sandbox: Independent Verification of v14.130 Cholesky-Normalized Gram Formula and Paired Parity Bound

**Date:** 2026-10-07
**Track:** Sandbox / v14.130 handoff response
**Status:** [D] v14.130 eq (1) independently verified (algebraic derivation + random-matrix exact test); [D] paired bound on ΔΛ_∥ derived, vanishes on common mode; [O] numerical evaluation awaits LDDD anchor export.
**Parents:** v14.130.
**Collision check:** live ledger max v14.131 at write time; v14.132 is next-free. No collision.

---

## 1. Verification of v14.130 eq (1) [D]

**Claim.** With $S=LL^*$ (Cholesky), $A:=UL^{-*}$, $G:=A^*A=L^{-1}DL^{-*}$,
$u:=L^*(v-a)$, $v=D^+c$,
$$\boxed{\Lambda_\parallel = u^*G(I-G)^{-1}u.}\tag{1}$$

**Derivation.** From v14.124/v14.125, $\Lambda_\parallel=\langle U(v-a),B^{-1}U(v-a)\rangle$
with $B=I-US^{-1}U^*$. Check the substitutions:
- $AA^*=UL^{-*}L^{-1}U^*=U(LL^*)^{-1}U^*=US^{-1}U^*$. ✓
- $G=A^*A=L^{-1}U^*UL^{-*}=L^{-1}DL^{-*}$. ✓
- $Au=UL^{-*}L^*(v-a)=U(v-a)$. ✓

Hence $\Lambda_\parallel=u^*A^*(I-AA^*)^{-1}Au$. The load-bearing step is the
exact push-through identity
$$\boxed{A^*(I-AA^*)^{-1}A = G(I-G)^{-1}.}\tag{2}$$
**Proof of (2).** Woodbury: $(I-AA^*)^{-1}=I+A(I-A^*A)^{-1}A^*=I+A(I-G)^{-1}A^*$.
Thus $A^*(I-AA^*)^{-1}A = G + G(I-G)^{-1}G$. Now
$G+G(I-G)^{-1}G=[G(I-G)+G^2](I-G)^{-1}=[G-G^2+G^2](I-G)^{-1}=G(I-G)^{-1}$. ∎

Substituting (2) gives (1). No approximation.

**Positivity chain.** $G=L^{-1}DL^{-*}\succeq 0$ (congruence preserves psd).
$B=I-AA^*\succ 0$ (Schur complement of SPD system) ⟺ $AA^*\prec I$ ⟺ $G\prec I$
(nonzero spectra of $AA^*,A^*A$ coincide). Hence $0\preceq G\prec I$,
$(I-G)^{-1}\succ 0$, and $\Lambda_\parallel\geq 0$ termwise per parity. **No $S-D$
is ever formed.**

**Random-matrix exact test** ($6\times 6$ SPD $S$, $40\times 6$ $F$):
whitened $\Lambda_\parallel=0.13369229163181034$ vs v14.130 formula
$0.13369229163181032$ (match); $K_{2R}-K_R=\sigma_\perp+\Lambda_{\parallel}^{(1)}$
reproduces v14.124 value $0.5118722253970485$ (match); push-through identity
holds to $10^{-9}$; $\operatorname{eig}(G)\subset[0,1)$ confirmed. **Eq (1)
confirmed exact.**

## 2. Paired parity bound preserving common mode [D]

Write $G(I-G)^{-1}=(I-G)^{-1}-I$ (check: $(I-G)^{-1}-I=G(I-G)^{-1}$). Then
$$\Lambda_{\parallel,p}=u_p^*(I-G_p)^{-1}u_p-|u_p|^2,$$
and with $\delta G=G_o-G_e$, $\delta u=u_o-u_e$,
$$\Delta\Lambda_\parallel
= u_o^*(I-G_o)^{-1}\delta G\,(I-G_e)^{-1}u_o
+ \big[u_o^*(I-G_e)^{-1}u_o-u_e^*(I-G_e)^{-1}u_e\big]
- \big(|u_o|^2-|u_e|^2\big).\tag{3}$$
The first equality uses the resolvent identity
$(I-G_o)^{-1}-(I-G_e)^{-1}=(I-G_o)^{-1}\delta G\,(I-G_e)^{-1}$, exact.

Bounding each term ($\|\cdot\|$ Euclidean, $\|\cdot\|_2$ spectral; $M:=(I-G_e)^{-1}\succ 0$):
- $|\alpha^*\delta G\beta|\leq\|\alpha\|\,\|\delta G\|_2\,\|\beta\|$;
- $u_o^*Mu_o-u_e^*Mu_e=\delta u^*Mu_o+u_e^*M\delta u$, so
  $|\cdot|\leq\|\delta u\|(\|Mu_o\|+\|Mu_e\|)$;
- $||u_o|^2-|u_e|^2|\leq\|\delta u\|(\|u_o\|+\|u_e\|)$.

**Paired bound.**
$$\boxed{
\begin{aligned}
|\Delta\Lambda_\parallel|
&\leq \|\delta G\|_2\,
\|(I-G_o)^{-1}u_o\|\,\|(I-G_e)^{-1}u_o\|\\
&\quad + \|\delta u\|\Big(
\|(I-G_e)^{-1}u_o\|+\|(I-G_e)^{-1}u_e\|
+\|u_o\|+\|u_e\|\Big).
\end{aligned}}\tag{4}
$$

**Properties.**
- Vanishes identically when $(G_o,u_o)=(G_e,u_e)$: common mode preserved exactly.
- All objects are $\leq 6$-dimensional; no full-octave norm bound; $S-D$ never formed.
- Positivity preserved throughout ($G_p\succeq 0$, resolvents $\succ 0$).
- Honest about amplification: $\|(I-G_p)^{-1}\|=1/(1-\mu_{\max}(G_p))$; if the
  anchor shows $\mu_{\max}(G_p)$ near 1, the bound degrades gracefully rather
  than silently.

**Diagnostic (not theorem).** The v14.124/v14.129 near-rank-one observation on
$(D,c,d)$ transfers by congruence to $G$; if the anchor confirms
$\mu_1(G)\gg\mu_2(G)$, then $\Lambda_{\parallel,p}\approx|g_p^*u_p|^2\mu_1/(1-\mu_1)$
is effectively scalar and (4) collapses to a scalar paired bound. This is
**not** used here.

## 3. What the anchor must deliver [O]

For the bound (4) to become numerical, the LDDD export
$(S_{64k},b_{64k},h_{64k},S_{64k}^{-1}b_{64k})$ plus the outward Gram payload
$(D_p,c_p,d_p)$ must supply, in multiprecision:
$\|\delta G\|_2$, $\|\delta u\|$, $\|(I-G_p)^{-1}u_q\|$, $\|u_p\|$ — all computable
from the normalized representation without any protected-matrix subtraction.
Nothing further is needed analytically.

## 4. Verdict

$$\boxed{
\begin{aligned}
&\text{[D] v14.130 eq (1) independently derived and numerically confirmed exact.}\\
&\text{[D] Push-through identity (2) proved; positivity chain }0\preceq G\prec I\text{ confirmed.}\\
&\text{[D] Paired bound (4): exact common-mode preservation, }\leq 6\text{-dim, no }S-D.\\
&\text{[O] Numerical values await the LDDD anchor; no rank-one assumption used.}
\end{aligned}
}$$

---

HANDOFF-NOTE
target: lane-a
type: verification-confirmation
parent: v14.132
status: closed
action: v14.130 eq (1) independently verified as an exact identity (derivation + random-matrix test). Paired bound (4) supplied for ΔΛ_∥ with exact common-mode preservation. Numerical evaluation needs only the anchor-derived (G_p,u_p) quantities in multiprecision — no further analytic input from sandbox. No correction needed.
constraints: None.
