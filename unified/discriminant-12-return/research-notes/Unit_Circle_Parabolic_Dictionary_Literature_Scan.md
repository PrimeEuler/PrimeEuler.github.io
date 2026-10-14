# Unit-circle / parabolic dictionary — Literature / Novelty Scan

**Date of scan:** 2026-10-14. **Method:** web-index searches (general web, arXiv-targeted, reference works, lecture notes, journal PDFs) with the mission's own search terms plus discriminators (Gudermannian, pseudorapidity, Neuman/Seiffert means, Mercator, Suzuki screw). Key pages were opened and read; the rest are index-verified. Coverage and limits are listed at the end — **absence below means "not found in this scan," not "does not exist."**

## Summary

No textbook, journal paper, arXiv paper, lecture note or reference work found in this scan states the **assembled** construction — the integer-indexed circle points $z_n$ with an AM/GM reading, the rapidity dictionary $\psi_n=\tfrac12\ln n$, the pair/chain form, and the parabolic-coordinate readout tied together. Every *ingredient* is classical and separately well documented, and two literatures come structurally very close:

1. **The Gudermannian / Mercator literature** contains the circle↔hyperbola dictionary in the *swapped* orientation: $\sin(\mathrm{gd}\,\psi)=\tanh\psi$, $\cos(\mathrm{gd}\,\psi)=\operatorname{sech}\psi$. The mission's point is $(\tanh\psi,\operatorname{sech}\psi)$, i.e. the reflection of the Gudermannian point, with polar angle $\pi/2-\mathrm{gd}\,\psi$.
2. **Pseudorapidity in particle physics** is exactly $\psi=\tfrac12\ln\frac{1+\cos\theta}{1-\cos\theta}$ with $\cos\theta=\tanh\psi$, and rapidity $y=\tfrac12\ln\frac{E+p_z}{E-p_z}$ is $\tfrac12\ln(p^+/p^-)$ in light-front variables — formally the same $\tfrac12\ln(\xi/\eta)$ shape, but never stated in parabolic coordinates $(\xi=r+z,\ \eta=r-z)$ in any source found.

The single exact scalar hit for $\tanh(\tfrac12\ln n)=(n-1)/(n+1)$ anywhere on the web is a **non-scholarly 2026 GitHub commit**, not literature (see §1/§2). The pair ratio $(a-b)/(a+b)$ with hyperbolic/trigonometric parameters *is* standard in the **Seiffert / Neuman–Sándor / Schwab–Borchardt means** literature, without rapidity language, circle points, or chains.

**Overall verdict: near-miss only for every component; the assembly as such — not found in this scan.**

---

## Findings

### Component 1 — $z_n=((n-1)+2i\sqrt n)/(n+1)$, AM/GM reading, integer "stations"

**Closest prior art**

- *Classical rational parametrization of the circle.* All rational points are classified by $x_1=\frac{1-t^2}{1+t^2},\ x_2=\frac{2t}{1+t^2}$, $t\in\mathbb Q$ — e.g. arXiv:2503.21151, eq. (24) (https://arxiv.org/pdf/2503.21151v1, index). Keith Conrad, *Pythagorean Triples* (UBC lecture notes, https://personal.math.ubc.ca/~cass/courses/m446-03/pl322/parametrization.html, index): line-through-$(1,0)$ argument giving $A=\frac{m^2-1}{m^2+1}$, $B=\frac{-2m}{m^2+1}$. Wikipedia, *Pythagorean triple* (https://en.wikipedia.org/wiki/Pythagorean_triplet, index): rational points ↔ primitive triples, $t=y/(1+x)=n/m$ is the tangent of half the angle, derived via stereographic projection.
- *Euclid's formula* is the $n=k^2$ subcase in disguise: with $t=1/\sqrt n=1/k$, the mission's point is $\big(\frac{k^2-1}{k^2+1},\frac{2k}{k^2+1}\big)$ — Euclid's $(m^2-n^2,\,2mn)/(m^2+n^2)$ at $(m,n)=(k,1)$.
- *AM/GM semicircle picture* (classical, different geometry): LibreTexts, *Arithmetic and Geometric Means* (https://math.libretexts.org/@api/deki/pages/58569/pdf/4.2%253A%2bArithmetic%2band%2bGeometric%2bMeans.pdf?stylesheet=default, index) — AM as radius/half-hypotenuse, GM as altitude on a semicircle. No unit-circle point $(\frac{n-1}{n+1},\frac{2\sqrt n}{n+1})$, no $n$-indexing.
- $n=3$ giving $(1/2,\sqrt3/2)$ is just the standard $60^\circ$ point; no source found singles it out via $n=3$ in this family.

**Gap:** No source found (i) substitutes $t=1/\sqrt n$ into the rational parametrization, (ii) indexes the resulting points by a positive integer $n$ as a sequence/stations, or (iii) reads $\operatorname{Im} z_n$ as $\mathrm{GM}/\mathrm{AM}$ or $\cosh\psi_n$ as $\mathrm{AM}/\mathrm{GM}$. A site-restricted Math StackExchange search for the formula returned no results.

**Verdict: near-miss only** (the point *set* is the classical rational parametrization at $t=1/\sqrt n$; the indexing, AM/GM reading and "station" framing were not found).

### Component 2 — Rapidity $\psi_n=\tfrac12\ln n$; $\tanh\psi_n$, $\operatorname{sech}\psi_n$, $\cosh\psi_n=\mathrm{AM}/\mathrm{GM}$, $e^{\psi_n}=\sqrt n$

**Closest prior art**

- *Rapidity itself* (Robb 1911; standard relativity): $\psi=\operatorname{artanh}(v/c)=\tfrac12\ln\frac{1+v/c}{1-v/c}$, $\gamma=\cosh\psi$ — e.g. Collins, *Foundations of Perturbative QCD*, Appendix B.3 (Cambridge University Press, https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/15E3B70439FCDA0816DADF73583798E4/9781009401838app2_595-599.pdf/lightfront_coordinates_rapidity_etc.pdf, index).
- *Gudermannian identities* (Lambert 1760s; Gudermann 1830): $\phi=\mathrm{gd}\,\psi=\int_0^\psi\operatorname{sech}t\,dt$, with $\sin\phi=\tanh\psi$, $\cos\phi=\operatorname{sech}\psi$, $\csc\phi=\coth\psi$, $\sec\phi=\cosh\psi$, and $e^{i\phi}=\operatorname{sech}\psi+i\tanh\psi$, $s=\tan\frac\phi2=\tanh\frac\psi2$ — Wikipedia, *Gudermannian function* (https://en.wikipedia.org/wiki/Gudermannian_function, **opened/verified**); Holzmann, *Gudermann function* notes, Univ. of Lethbridge (https://www.cs.uleth.ca/~holzmann/notes/gudermann.pdf, index). **Discrimination:** this is the mission's dictionary with real and imaginary parts *interchanged*. The mission's $z_n=\tanh\psi_n+i\operatorname{sech}\psi_n$ is the Gudermannian point reflected in $y=x$; its angle is $\pi/2-\mathrm{gd}\,\psi_n$ (which is why $n=3$ gives $60^\circ$, not $\mathrm{gd}\,\psi_3=30^\circ$). No Gudermannian source found makes this swap, nor sets $e^\psi=\sqrt n$.
- *Mercator / inverse Gudermannian:* $\psi=\ln\tan(\pi/4+\phi/2)=\operatorname{artanh}(\sin\phi)$ — e.g. *Catenary and Mercator projection*, arXiv:2401.12991 (https://arxiv.org/pdf/2401.12991, index). Same circle↔log bridge, in latitude language.
- *Exact scalar identity, non-scholarly:* a GitHub commit (eliottcassidy2000/math, 2026-03-15, https://github.com/eliottcassidy2000/math/commit/87c9147fc8dbd4e6d70ca1796aa8c9d3ca9e8faa, index) states, in the author's own wording, $\tanh(\ln(n)/2)=(n-1)/(n+1)$ and calls it a "Cayley address." This is a self-published code repository (no venue, no peer review, no circle point / AM–GM / parabolic content in the indexed text) — it is the **only** verbatim hit for the $n$-indexed tanh identity, and it does not antedate-establish the construction in the literature sense.
- $\cosh x\ge1$ via AM–GM on $(e^x+e^{-x})/2$ is a textbook exercise trope, but with $e^{\psi}=\sqrt n$ specifically giving $\cosh\psi_n=(n+1)/(2\sqrt n)=\mathrm{AM}/\mathrm{GM}$ — not found stated.

**Verdict: near-miss only** (Gudermannian gives the transposed dictionary for a *continuous* $\psi$; the discretization $\psi_n=\tfrac12\ln n$, $e^{\psi_n}=\sqrt n$, and the AM/GM gloss were not found in scholarly literature).

### Component 3 — Pair form $z_{n,k}$, $\psi_{n,k}=\tfrac12\ln(n/k)$, additive chains, $(n+k)/(n-k)=\coth\psi_{n,k}$

**Closest prior art**

- *Additivity of rapidity under collinear boosts is the defining textbook property:* Collins (above), eq. (B.11) $y\to y'=y+\text{const}$, derived from $\tanh(A+B)=\frac{\tanh A+\tanh B}{1+\tanh A\tanh B}$; chains of relative velocities multiply the ratios $\frac{1+v/c}{1-v/c}$ and add after taking $\tfrac12\ln$ — e.g. *Search for a Lorentz invariant velocity distribution…*, arXiv:1505.03409, eqs. (4)–(7) (http://arxiv.org/pdf/1505.03409v2, index). This is exactly the mission's chain law $\psi_{n,k}+\psi_{k,j}=\psi_{n,j}$, but parametrized by *velocities/frames*, never by a pair of integers $(n,k)$ with a circle point $z_{n,k}$ attached.
- *Means literature (the other half of the pair form, without relativity):* He, Chu, Song & Tao, *Note on certain inequalities for Neuman means*, arXiv:1405.4387 (2014) (https://export.arxiv.org/pdf/1405.4387, **opened/verified**), following Neuman: for $a>b>0$ set $v=\frac{a-b}{a+b}$ and parameters $p,q$ with $1/\cosh p=\cos q=\sqrt{1-v^2}$; $A(a,b),G(a,b),H(a,b)$ are defined alongside. Since $v=\tanh\big(\tfrac12\ln(a/b)\big)$ and $\sqrt{1-v^2}=\operatorname{sech}\big(\tfrac12\ln(a/b)\big)$, $p$ *is* the mission's $\psi_{a,b}$ — but the paper never says so, never uses the words rapidity/log-ratio, forms no circle point, and has no chain/telescoping. Neighbours: Neuman–Sándor mean $M=\frac{a-b}{2\operatorname{arcsinh} v}$; Seiffert means $P,T$ built from $\arcsin v$, $\arctan v$ and the logarithmic mean $L=\frac{a-b}{\ln a-\ln b}$ (Neuman, *On Yang means*, https://www.scik.org/index.php/aia/article/viewFile/3125/1572, index; Wikipedia, *Neuman–Sándor mean*, https://en.wikipedia.org/wiki/Neuman%E2%80%93S%C3%A1ndor_mean, index).
- $\coth\psi_{n,k}=(n+k)/(n-k)$ is $1/\tanh$ of the above; no source found states the pair coth form or attaches it to $z_{n,k}$.

**Verdict: near-miss only** (additive rapidity chains: classical for boosts; pair ratio $(a-b)/(a+b)$ with $\cosh$/$\operatorname{sech}$ parameters: classical for bivariate means; the *fusion* — integer pair $\to$ circle point $\to$ additive rapidity chain — was not found).

### Component 4 — Parabolic coordinates: $\cos\theta=\frac{\xi-\eta}{\xi+\eta}$, $\sin\theta=\frac{2\sqrt{\xi\eta}}{\xi+\eta}$, $\psi=\tfrac12\ln(\xi/\eta)$; cone row–column table of confocal parabolas

**Closest prior art**

- *Parabolic coordinates themselves* (all classical): 2-D form $x=\sigma\tau$, $y=\tfrac12(\tau^2-\sigma^2)$, $\sigma=\sqrt{r-y}$, $\tau=\sqrt{r+y}$ — i.e. $\xi,\eta$ are (up to the $z\leftrightarrow y$ axis label) $r\pm z$ — with both families of confocal parabolas as coordinate lines: Wikipedia, *Parabolic coordinates* (https://en.wikipedia.org/wiki/Parabolic_coordinates, **opened/verified**), bibliography Morse & Feshbach (1953) p. 660; Margenau & Murphy (1956); Korn & Korn (1961); Moon & Spencer (1988). 3-D paraboloidal form for hydrogen: $\xi=r+z$, $\eta=r-z$, $x=\sqrt{\xi\eta}\cos\varphi$, $z=\tfrac12(\xi-\eta)$ — e.g. *Bound states of the hydrogen atom in parabolic coordinates*, Rev. Mex. Fis. 54 (2008) 454–458 (https://rmf.smf.mx/ojs/index.php/rmf/article/download/3648/3615/6138, index); Wightman, *Group Theory and the Hydrogen Atom (I)* (https://escholarship.org/content/qt42q1m0t7/qt42q1m0t7_noSplash_1e993b4757b903425f57e4f44c2ef3b9.pdf?t=q160f5, index). From $x=\sqrt{\xi\eta}$ and $z=\tfrac12(\xi-\eta)$ the mission's $\cos\theta,\sin\theta$ readout follows in one line, but **no source found states it**, and none introduces $\tfrac12\ln(\xi/\eta)$.
- *The readout *is* pseudorapidity, in momentum language:* $\eta_{\text{ps}}=-\ln\tan\frac\theta2=\tfrac12\ln\frac{|p|+p_z}{|p|-p_z}$, $\cos\theta=\tanh\eta_{\text{ps}}$ — Buda-Lund model paper, arXiv:nucl-th/0310040 (http://arxiv.org/pdf/nucl-th/0310040, index); Collins App. B.4 (above). Since $|p|\pm p_z$ are formally $r\pm z$ for the *momentum* vector, this is the nearest statement of $\psi=\tfrac12\ln(\xi/\eta)$ in print — but it is never connected to parabolic coordinates, hydrogen, or a coordinate grid.
- *Confocal parabola nets:* Wikipedia, *Confocal conic sections* (https://en.wikipedia.org/wiki/Confocal_conic_sections, index): the plane is covered by an orthogonal net of confocal parabolas usable as a parabolic coordinate system, obtained as the image of a rectangular grid under $w=z^2$. This is the classical substance of the "row–column table." **No source found** puts this net *on a cone*, discretizes it by integer ratios $\xi/\eta=n$, or reads directions off it by rapidity. Searches coupling "parabolic coordinates" with cone/discrete/integer grids returned only unrelated results (cone/paraboloid points in geometric measure theory, arXiv:2103.01789).

**Verdict: near-miss only** (ingredients — $\xi=r+z$, $\eta=r-z$, confocal-parabola net, and separately $\cos\theta=\tanh(\text{pseudorapidity})$ — are all classical; the parabolic-coordinate angular/rapidity readout as stated, and the cone table, were not found).

### Component 5 — Logarithmic seed $\log(m/4)=2(\psi_m-\ln 2)$

This is pure algebra from Component 2: $2(\tfrac12\ln m-\ln2)=\ln m-\ln4=\log(m/4)$. Searches for the exact form and for $\log(m/4)$ in rapidity/zeta contexts returned nothing relevant (the Suzuki screw-function archimedean terms involve $\Gamma'/\Gamma(1/4)-\log\pi$ and $-\tfrac12\log2$-type constants, a different object — see §(d)). No source found names, tabulates, or uses $\log(m/4)$ as a "seed."

**Verdict: not found in this scan** (and, being a one-line rearrangement of $\psi_m=\tfrac12\ln m$, it inherits Component 2's status).

---

## Questions (a)–(e)

**(a) Specific unit-circle encoding?** **Not found** in scholarly literature. The discriminating near-miss is confirmed: the standard parametrization $\big(\frac{1-t^2}{1+t^2},\frac{2t}{1+t^2}\big)$ at $t=1/\sqrt n$ reproduces the points exactly, and the stereographic/Euclid literature (Conrad; Wikipedia *Pythagorean triple*; arXiv:2503.21151) develops $t$ as a *rational slope / half-angle tangent* — no source found makes the substitution $t=1/\sqrt n$, indexes by integers as stations, or adds the AM/GM or rapidity reading. The only verbatim $n$-indexed tanh identity is the non-scholarly GitHub commit in §2.

**(b) Pair form / rapidity-addition chain?** **Near-miss only.** Additive chains: standard for successive boosts (Collins B.3.3; arXiv:1505.03409). Pair ratio with hyperbolic parameters: standard for Seiffert/Neuman–Sándor/Schwab–Borchardt means (arXiv:1405.4387, opened). Neither literature uses the other's language, and neither attaches a unit-circle point $z_{n,k}$ or an integer chain $n\to k\to j$.

**(c) Parabolic-coordinate angular readout / rapidity-parametrized parabolic coordinates?** **Not found as stated.** $\cos\theta=\frac{\xi-\eta}{\xi+\eta}$ and $\psi=\tfrac12\ln(\xi/\eta)$ appear in no parabolic-coordinates source found (textbook-style treatments give $\sigma,\tau$ or $\xi,\eta$ via $r\pm z$ and stop there). The mathematically identical statement exists only as **pseudorapidity** for momentum directions ($\eta_{\text{ps}}=\tfrac12\ln\frac{|p|+p_z}{|p|-p_z}$, $\cos\theta=\tanh\eta_{\text{ps}}$; Collins B.4; arXiv:nucl-th/0310040), with no parabolic-coordinate framing.

**(d) Parabola meshes on a cone ↔ "screw function" (Suzuki) or helices/screws on cones?** **No connection found; the two "screw" literatures are unrelated to parabolas/cones.**
- Suzuki, *Aspects of the screw function corresponding to the Riemann zeta-function*, J. London Math. Soc. 108 (2023) 1448–1487, arXiv:2206.03682 (index; journal citation confirmed via the author's later bibliography): $g(t)$ built from $\sum_{n\le e^{|t|}}n^{-1/2}\Lambda(n)(|t|-\log n)$ plus archimedean terms; $g$ is a screw function in the Krein–Langer sense (kernel $G_g(t,u)=g(t-u)-g(t)-g(-u)+g(0)$ positive) iff RH holds.
- Suzuki, *The screw line of the Riemann zeta-function and its applications*, arXiv:2209.04658 (2022) (index): a screw line is a map $t\mapsto x(t)$ into a **Hilbert space** with translation-invariant distances, e.g. $x(t)=(e^{it\gamma}-1)/\gamma$ in $L^2(\tau)$ — not a curve on a cone or any surface.
- Suzuki, *Analytic theories around the simplest screw*, arXiv:2308.11860 (survey, index): explicitly distinguishes "screw line" (Krein–Langer/von Neumann–Schoenberg terminology) from colloquial "helix/spiral"; the simplest screw line lives in $\mathbb R^3$ as a circle-plus-drift curve. No parabolas, no cone, no foliation.
- Classical differential geometry's screw/helix is on a **cylinder**: Shifrin, *Differential Geometry* notes (https://www2.math.upenn.edu/~wziller/Math501/ShifrinDiffGeo.pdf, index): helix $(a\cos t,a\sin t,bt)$, "screwlike path … on a right circular cylinder." Conical helices exist as a separate elementary topic (parametric curve with radius growing linearly on a cone) — no source found links them to parabolic foliations, Suzuki, or zeta functions.

**Verdict (d): not found in this scan** — Suzuki's "screw" is a Hilbert-space/positive-kernel notion; nothing bridges it to parabola meshes on a cone.

**(e) Does $32/81=2^5/3^4$ appear in hydrogen dipole/parabolic matrix elements?** **Not found.** What *does* appear, repeatedly, is the mission's stated kernel:
- $\langle ez\rangle = \frac{128\sqrt2}{243}$ (in the paper's atomic-unit prefactors) computed **in paraboloidal coordinates** via $|2p,m{=}0\rangle=\frac{\sqrt2}{2}\big(|n_1{=}0,n_2{=}1\rangle-|n_1{=}1,n_2{=}0\rangle\big)$ — arXiv:1603.00899v2 (http://arxiv.org/pdf/1603.00899v2, index).
- The spherical-coordinate version $\int d^3r\,\psi_{1s}^*(-er)\psi_{2p}=-\frac{128\sqrt2}{243}\,ea_B$ as a standard Fermi-golden-rule exercise, with the $2p\to1s$ rate containing $(2/3)^8$ (https://askfilo.com/user-question-answers-smart-solutions/as-the-only-exercise-of-this-introductory-chapter-of-module-3331313633323330, index).
- Note $128\sqrt2/243$ does **not** factor through $32/81$: $243\cdot\frac{32}{81}=96\neq128\sqrt2/ \text{(any simple } \sqrt2\text{-combination found)}$. Targeted searches for `"32/81"` with hydrogen/dipole/parabolic returned no atomic-physics hit at all; general-web hits for $32/81$ are fraction-arithmetic pages and one unrelated occurrence as the volume $32\pi R^3/81$ of the largest cone inscribed in a sphere (ratio $8/27$ to the sphere) — a cone context, but not hydrogen and not a matrix element.

**Verdict (e): not found in this scan** — $32/81$ is neither named nor tabulated in the hydrogen dipole/parabolic literature found; the tabulated constant is $128\sqrt2/243$.

---

## Overall assessment of the assembly's novelty

| Component | Verdict |
|---|---|
| 1. $z_n$, AM/GM, integer stations | Near-miss only (classical rational parametrization at $t=1/\sqrt n$; indexing + AM/GM reading not found) |
| 2. $\psi_n=\tfrac12\ln n$ dictionary | Near-miss only (Gudermannian, transposed, continuous $\psi$; one non-scholarly GitHub hit for the scalar identity) |
| 3. Pair form + additive chains | Near-miss only (boost additivity ∥ means-literature $v=(a-b)/(a+b)$; fusion not found) |
| 4. Parabolic readout $\psi=\tfrac12\ln(\xi/\eta)$; cone table | Near-miss only (parabolic coords ∥ pseudorapidity, never joined; cone table not found) |
| 5. $\log(m/4)=2(\psi_m-\ln2)$ | Not found in this scan (one-line corollary of 2) |
| (d) Cone parabolas ↔ Suzuki screw | Not found in this scan |
| (e) $32/81$ in hydrogen dipoles | Not found in this scan |

**Assessment:** The assembly appears to be a *novel recombination of entirely classical parts*, with two genuinely close classical neighbours that any novelty claim must explicitly distinguish: (i) the **Gudermannian/Mercator** dictionary (same identities, coordinates swapped, continuous parameter, no integers, no AM/GM, no parabolas) and (ii) **pseudorapidity/light-front rapidity** (same $\tfrac12\ln\frac{(\cdot)+z}{(\cdot)-z}$ form, momentum setting, no parabolic coordinates, no circle stations). A third neighbour, the **Seiffert/Neuman means** literature, silently uses $v=\tanh\psi_{a,b}$ and $\operatorname{sech}\psi_{a,b}$ as parameters for means of two numbers. None of the three contains the integer station sequence, the AM/GM reading of a circle point, or the parabolic-coordinate identification — the three features that constitute the construction's claimed identity.

**Strength of the negative evidence — moderate, not conclusive.** Searched: general web index with ~35 exact-formula and discriminator queries (including the mission's suggested terms); arXiv (site-targeted and PDF-level hits); reference works (Wikipedia/Encyclopedia-of-Mathematics-style entries for parabolic coordinates, Gudermannian, Pythagorean triples, Neuman–Sándor mean); lecture notes (UBC, Harvard, Lethbridge, UPenn/GaTech, KIT, Cambridge CUP appendix); journal PDFs (JLMS via arXiv, J. Inequal. Appl./Springer, Rev. Mex. Fis.); Math StackExchange (site search, no results). **Not** searched: MathSciNet, zbMath, Scopus/Web of Science, Google Books full text, or non-English literatures — a formula stated only inside a scanned textbook (e.g. a means or special-functions monograph) could evade this scan. The one exact web hit (2026 GitHub commit) also shows the scalar identity of Component 2 circulates informally online, so "first ever written down anywhere" would be too strong a claim even for that piece.

## Could not verify

- Full texts of Suzuki JLMS 108 (2023) and arXiv:1603.00899 were read via search-index extracts, not opened PDFs (two `browser_open` fetches timed out and were not retried); their bibliographic data and the quoted formulas are corroborated by multiple independent index hits (author's later survey bibliography; the AskFilo restatement of $128\sqrt2/243$).
- Whether the 2026 GitHub repository contains more of the construction (circle points, parabolas) beyond the indexed commit text — only its indexed snippet was read; it is in any case not a literature venue.
- Textbook-only sources (MathSciNet/zbMath/Google Books) — see coverage caveat above.

## Sources

- Gudermannian function — https://en.wikipedia.org/wiki/Gudermannian_function — opened 2026-10-14. Identities $\sin/\cos(\mathrm{gd}\,\psi)=\tanh/\operatorname{sech}\,\psi$, $e^{i\phi}=\operatorname{sech}\psi+i\tanh\psi$, Lambert/Gudermann history.
- Holzmann, Gudermann function notes — https://www.cs.uleth.ca/~holzmann/notes/gudermann.pdf — index.
- Collins, *Foundations of Perturbative QCD*, App. B — https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/15E3B70439FCDA0816DADF73583798E4/9781009401838app2_595-599.pdf/lightfront_coordinates_rapidity_etc.pdf — index. Rapidity definition, additivity (B.11), pseudorapidity (B.4).
- Buda-Lund hydro model paper — http://arxiv.org/pdf/nucl-th/0310040 — index. $\eta=0.5\log\frac{|p|+p_z}{|p|-p_z}$.
- Parabolic coordinates — https://en.wikipedia.org/wiki/Parabolic_coordinates — opened 2026-10-14; bibliography Morse & Feshbach 1953, Moon & Spencer 1988.
- Rev. Mex. Fis. 54 (2008) 454–458 — https://rmf.smf.mx/ojs/index.php/rmf/article/download/3648/3615/6138 — index. Hydrogen in $(\xi,\eta,\varphi)$, $z=\tfrac12(\xi-\eta)$.
- He, Chu, Song, Tao, *Note on certain inequalities for Neuman means*, arXiv:1405.4387 — https://export.arxiv.org/pdf/1405.4387 — opened 2026-10-14. $v=(a-b)/(a+b)$, $1/\cosh p=\cos q=\sqrt{1-v^2}$.
- Neuman, *On Yang means* — https://www.scik.org/index.php/aia/article/viewFile/3125/1572 — index. Seiffert/Neuman–Sándor/Schwab–Borchardt definitions.
- Rational points classification, arXiv:2503.21151 — https://arxiv.org/pdf/2503.21151v1 — index, eq. (24).
- Conrad, *Pythagorean Triples* (UBC) — https://personal.math.ubc.ca/~cass/courses/m446-03/pl322/parametrization.html — index.
- Pythagorean triple — https://en.wikipedia.org/wiki/Pythagorean_triplet — index. Stereographic derivation, $t=n/m=\tan(\theta/2)$.
- Suzuki, *Aspects of the screw function…*, JLMS 108 (2023) 1448–1487; arXiv:2206.03682 — http://arxiv.org/pdf/2206.03682v1 — index.
- Suzuki, *The screw line of the Riemann zeta-function…*, arXiv:2209.04658 — http://arxiv.org/pdf/2209.04658 — index.
- Suzuki, *Analytic theories around the simplest screw*, arXiv:2308.11860 — https://arxiv.org/abs/2308.11860v2 — index.
- Shifrin, *Differential Geometry* notes — https://www2.math.upenn.edu/~wziller/Math501/ShifrinDiffGeo.pdf — index. Helix on cylinder; tractrix $(\cdot-\tanh t,\operatorname{sech}t)$.
- Hydrogen paraboloidal dipole, arXiv:1603.00899v2 — http://arxiv.org/pdf/1603.00899v2 — index. $\langle ez\rangle=128\sqrt2/243$ (with prefactors).
- Fermi-golden-rule exercise with $128\sqrt2/243$ — https://askfilo.com/user-question-answers-smart-solutions/as-the-only-exercise-of-this-introductory-chapter-of-module-3331313633323330 — index.
- GitHub commit, tanh identity (non-scholarly) — https://github.com/eliottcassidy2000/math/commit/87c9147fc8dbd4e6d70ca1796aa8c9d3ca9e8faa — index, dated 2026-03-15.
- Confocal conic sections — https://en.wikipedia.org/wiki/Confocal_conic_sections — index. Orthogonal net of confocal parabolas via $w=z^2$.
- *Catenary and Mercator projection*, arXiv:2401.12991 — https://arxiv.org/pdf/2401.12991 — index.
- Working notes: `notes/coverage-and-key-sources.md` (full query list).
