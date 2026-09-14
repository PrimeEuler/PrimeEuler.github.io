# The Divisor-Shell/Cone Identification, the n-vs-d Index Distinction, and the General Discriminant Return

**A record of a cross-session synthesis, with every claim independently re-derived before being kept.**

---

## 1. The `v_k`/`T_k` "mod-0.5" construction is exactly Paper A's cone

Recall the GeoGebra "mod 0.5" divisor-symmetry construction and its algebraic twin from `research-notes/Divisor_Summatory_V4_Mod12_Findings.md`:

$$v_k=\frac{n-k^2}{2k},\qquad T_k=\frac{n+k^2}{2k},\qquad v_k\bmod 0.5=\tfrac12\{n/k\}.$$

Paper A (`foundations/PaperA_ConicTheorem_v2.4.tex`) defines, for a factor pair $u,v$ with $uv=n$,

$$X=\frac{u-v}{2},\qquad Y=\sqrt{uv},\qquad T=\frac{u+v}2,\qquad T^2-X^2=Y^2=uv.$$

**Verified exactly (symbolic algebra):** setting $u=k,\ v=n/k$ gives $X=(k^2-n)/(2k)=-v_k$ and $T=(k^2+n)/(2k)=T_k$ identically. So the "hyperbola vertex at $k=\sqrt n$" construction explored this session is not a new object — **it is Paper A's cone, restricted to a single shell $Y=\sqrt n$, in different notation.** The vertex of that hyperbola (where $v_k=0$) is exactly the point $X=0,\ T=\sqrt n$ on the cone, i.e. the minimal-$T$ point of the shell.

**Consequence, stated plainly:** every $n$ literally has its own fixed height $Y=\sqrt n$ on Paper A's cone. This is not a loose analogy to the later discriminant-12 material — it is a directly checkable algebraic identity, confirmed above.

## 2. The index that varies with $n$ never leaves $\mathbf Q$ — this is the crucial distinction

The shell family $T^2-X^2=n$, viewed as a binary quadratic form $aT^2+bTX+cX^2$ with $a=1,b=0,c=-1$, has discriminant $b^2-4ac=4$ for **every** $n$. The asymptote slopes are always $\pm1$ — rational, for every single shell, no matter how large $n$ gets. So sweeping through all $n$ never produces an irrational ray; $n$ only indexes *which level* of one fixed rational-asymptote family you are looking at.

This was checked against a natural candidate for a "hidden" invariant — the angle at which a ray through the origin crosses the unit circle. **Result: not distinguishing.** Any line through the origin (rational slope, the quadratic-irrational slope $-1+\sqrt3$, or even a transcendental slope like $\pi$ or $e$) crosses a circle centered at the origin at the same angle to the tangent (0° to the radius), because a diameter is always perpendicular to the tangent at its endpoint. This is a generic fact of any circle centered at the origin and carries no arithmetic information; it does not distinguish the two families discussed below. Recorded here so it is not silently rediscovered and mistaken for a real connection later — this is the same "shared numeral, not shared mechanism" trap flagged repeatedly elsewhere in this ledger (e.g. the Casimir-quarter guardrail).

## 3. The discriminant-12 return already proves the real, general structure — for `d=12`

`v13.179_Return_Boost_Tangent_Rays.md` already proves (labeled `[D]`, exact) the fact that actually matters, for the specific case $d=12$:

$$g_{12}=\begin{pmatrix}3&1\\2&1\end{pmatrix},\quad\text{conjugate to}\quad B_{12}=\begin{pmatrix}2&\sqrt3\\\sqrt3&2\end{pmatrix}=\begin{pmatrix}\cosh R_{12}&\sinh R_{12}\\\sinh R_{12}&\cosh R_{12}\end{pmatrix},$$

with $\varepsilon=2+\sqrt3=e^{R_{12}}$ the fundamental unit of $\mathbf Q(\sqrt3)$. Writing $x=T+X,\ y=T-X$, the boost acts as $x'=\varepsilon x,\ y'=\varepsilon^{-1}y$, so $x'y'=xy$ **identically** — every shell $xy=n$ is preserved, for every $n$ simultaneously, not just $n=12$. In rapidity coordinates on a shell ($x=\sqrt n\,e^s,\ y=\sqrt n\,e^{-s}$), the boost is the uniform translation $s\mapsto s+R_{12}$, the same step on every shell regardless of $n$.

**Independently re-verified this session** (symbolic, not re-quoted): $x=T+X,\ y=T-X$ with $(T,X)\mapsto B_{12}(T,X)$ gives $x'y'-xy\equiv0$.

**The honest limitation, already stated in `v13.179`:** $\varepsilon=2+\sqrt3$ is irrational, so this boost does **not** map the integer divisor lattice to itself — it is a continuous symmetry of each real shell, not an arithmetic operation on actual factor pairs. It does not give a new handle on $D(n)$'s integer combinatorics by itself.

## 4. This generalizes beyond `d=12` — checked with a second, independent discriminant

**[New this session, checked, not previously in the ledger.]** Two things needed separating, since it would be easy to conflate them:

**(a) "Preserves every shell" is a generic fact of any Lorentz boost in the $(T,X)$ plane, not a special property of $\varepsilon=2+\sqrt3$.** Verified symbolically: for *any* real $R$, the boost $\begin{pmatrix}\cosh R&\sinh R\\\sinh R&\cosh R\end{pmatrix}$ satisfies $(T')^2-(X')^2\equiv T^2-X^2$ identically, hence preserves every shell $xy=n$. This holds for every real $R$, not only $R=\log(2+\sqrt3)$.

**(b) What *is* special about $d=12$ is that $\varepsilon=2+\sqrt3$ comes from an actual integer matrix** — $g_{12}$ has integer entries, so it is a genuine arithmetic return map (a fundamental solution of a Pell-type equation of discriminant 12), not an arbitrary real boost parameter.

**The real open question from this session was: does an analogous *integer* return matrix exist for other discriminants, with the same shell-preservation property?** Checked with a second, independent example, $d=5$:

$$g_5=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad\operatorname{tr}=3,\ \det=1,\ \Delta=9-4=5,\qquad\text{eigenvalues }\frac{3\pm\sqrt5}2=\varphi^{\pm2},$$

where $\varphi=(1+\sqrt5)/2$ is the golden ratio (fundamental unit of $\mathbf Q(\sqrt5)$, up to squaring convention). Conjugating $g_5$ to its symmetric boost form $B_5$ (via diagonalization, $R_5=\log\varphi^2$) and applying the identical $x=T+X,\ y=T-X$ construction:

$$x'y'-xy\equiv0\qquad\text{(verified symbolically, for arbitrary }n\text{).}$$

So the discriminant-12 construction is **not** a one-off: it is the $d=12$ instance of a general pattern — for any non-square $d$ with an integer matrix of trace $t$, determinant $1$, and $t^2-4=d$ (a fundamental automorphism of the corresponding Pell-type form), the same argument gives a shell-preserving boost with rapidity step $R_d=\log\varepsilon_d$, $\varepsilon_d$ the relevant unit of $\mathbf Q(\sqrt d)$. This is classical Pell-equation/real-quadratic-unit theory combined with the already-established Paper-A/B cone structure — no new machinery is required to state it in general, only to verify (as done here) that nothing about the $d=12$ argument secretly depended on the specific value $12$.

Paper B's general Lorentz generator $G_{a,b}=(a+b)L+(a-b)B_Y$ (characteristic polynomial $\lambda(\lambda^2+4ab)$) is the natural home for this family: the pure-boost case $a=-b$ gives eigenvalues $0,\pm2b$, i.e. a different quadratic field $\mathbf Q(\sqrt{-ab})$ for each choice of $b$. A general treatment (stating and proving the shell-preservation and rapidity-translation facts for the whole $G_{a,b}$ family at once, rather than $d=12$ and $d=5$ as separate instances) would be the natural next step, but has not been carried out here.

## 5. What this does and does not establish

**Established, and checked independently in this session:**
- The `v_k`/`T_k` construction is exactly Paper A's cone at the shell $Y=\sqrt n$ (§1).
- The $D(n)$-shell family's discriminant is fixed at $4$ for every $n$ — it never produces an irrational ray on its own (§2).
- `v13.179`'s discriminant-12 shell-preservation and rapidity-translation facts, re-verified symbolically (§3).
- The shell-preservation property generalizes to at least one other discriminant ($d=5$), and the reason it generalizes is now identified precisely: it is a generic Lorentz-boost fact, with the *arithmetic* content living entirely in which boosts happen to come from integer (Pell) matrices (§4).

**Explicitly not established:**
- No connection between this shell-preserving symmetry and $D(n)$'s actual integer-divisor combinatorics — the boost acts on the continuous real shell, not the discrete lattice of divisor pairs, exactly as `v13.179` already cautioned.
- No connection to Suzuki's screw-function operator or RH — this entire thread is classical real/algebraic geometry on the Paper-A/B cone, independent of that separate (and separately-audited) thread.
- No general theorem covering all discriminants $d$ at once via the full $G_{a,b}$ family — only two individual instances ($d=12$, $d=5$) have been checked.

## 6. Suggested next steps

1. Prove the shell-preservation and rapidity-translation facts once, for the general $G_{a,b}$ pure-boost family, rather than per-discriminant.
2. Characterize exactly which $d$ admit an integer trace-$t$, det-$1$ matrix with $t^2-4=d$ (standard Pell theory: any $d\equiv0,1\pmod4$ that is not a perfect square, via the fundamental solution of the associated Pell equation) and connect this back to the project's own existing discriminant-12/$V_4$/QR machinery to see whether a *family* of discriminants (not just 12) intersects that machinery meaningfully.
3. If a genuine arithmetic (not just continuous) action on divisor pairs is ever wanted, the honest starting point is asking which finite set of shells a given $g_d$ *could* act on arithmetically — `v13.179` already shows the naive idea (permuting the integer tangent-circle family) fails for $d=12$; check whether this is generic or specific to 12.
