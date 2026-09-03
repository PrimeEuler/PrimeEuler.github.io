# Divisor Summatory Function, Smooth Extensions, and the V4/mod-12 Character

**A record of a real-time exploration, with every claim independently verified before being kept.**

---

## 1. The core exact identity

For the divisor summatory function $D(n) = \sum_{k=1}^n d(k)$, the classical identity

$$D(n) = n H_n - \sum_{k=1}^n \{n/k\}, \qquad H_n = \sum_{k=1}^n \frac1k,\quad \{x\} = x-\lfloor x\rfloor$$

follows directly from $\lfloor n/k \rfloor = n/k - \{n/k\}$, summed over $k$.

## 2. The "mod 0.5" construction (verified exact)

A GeoGebra construction computed, for fixed $n$,

$$v_k = \frac{n-k^2}{2k}, \qquad B(n) = 2\sum_{k=1}^n (v_k \bmod 0.5), \qquad A(n) = 2\sum_{k=1}^n v_k.$$

**Verified exactly** (via exact rational arithmetic, $n=12$):

- $v_k \bmod 0.5 = \tfrac12\{n/k\}$ exactly, since $v_k = n/(2k) - k/2$ and $k/2$ is always a multiple of $0.5$.
  Therefore $B(n) = \sum_{k=1}^n \{n/k\}$ **exactly** — this construction *is* the fractional-part sum above, algebraically disguised.
- $A(n) = nH_n - T_n$ exactly, where $T_n = n(n+1)/2$ (triangular number) — since $A(n) = \sum[n/k - k] $.
- Consequently:
  $$nH_n - B(n) = D(n), \qquad nH_n - A(n) = T_n, \qquad T_n - D(n) = A(n)\text{-related constant}.$$
  At $n=12$: $D(12)=35$, $T_{12}=78$, $T_{12}-D(12)=43$.

### OEIS confirmation

$T_n - D(n) = \sum_{i=1}^n (i - d(i))$ is exactly **[OEIS A161664](https://oeis.org/A161664)**, with $a(12)=43$ confirmed against the listed sequence. The name "prime safe periods" is a real, cited concept (Enoch Haga; G. F. Webb, *"The prime number periodical Cicada problem,"* Discr. Cont. Dyn. Syst. B, 2001) — $T(n)-D(n)$ counts non-dividing pairs $(i,j)$, $i\le j\le n$, motivated by the hypothesis that prime-length cicada life cycles minimize synchronization with shorter-cycle predators.

## 3. Real-valued smooth extension

Extending $H_n\to H(x) := \psi(x+1)+\gamma$ (digamma), the closed form

$$S(x) = x\,H(x) - (1-\gamma)x - \tfrac12$$

is smooth for all real $x>0$, matches $D(n)$ within the classical $O(\sqrt n)$ envelope at integers, and equals the classical Dirichlet asymptotic $x\log x + (2\gamma-1)x$ up to $O(1/x)$.

For a **fixed** $k$-range $1,\dots,m$ and real $x\in[m,m+1)$: $x\,H_m$ is exactly linear (genuinely smooth, no floor anywhere), while $\sum_{k=1}^m\lfloor x/k\rfloor$ is the true step function; their difference is $\sum_{k=1}^m\{x/k\}$, a sum of $m$ independent sawtooths, one per $k$, each with its own period.

## 4. The pronic/diagonal quarter-shift family

On the diagonal $y=x+k$ (constant offset $k$) of the multiplication-table cone $T^2-X^2=Y^2$:

$$X=-k/2 \ (\text{constant}), \qquad T = x+k/2, \qquad T^2 - Y^2 = (k/2)^2.$$

At $k=1$, integer $x=n$: $(n+\tfrac12)^2 = n(n+1) + \tfrac14$ — e.g. $12+0.25=12.25=3.5^2$. This is the **same universal $(\tfrac12)^2$** verified earlier in the session across the null-diamond midpoint, the $SU(2)$/$SU(1,1)$ Casimir completions, the $J_x,J_y$ ladder-operator average, and the mod-12 Boolean-cell centering — six independent, verified appearances of one constant, all from the identical "complete the square around a half-integer shift" mechanism. (This is a *different* $1/4$ from §6 below — see the note there.)

## 5. Isolating the classical open problem

$$a(n) := \sum_{k=1}^n\{n/k\} = (1-\gamma)n + \big[a(n)-(1-\gamma)n\big].$$

Numerically confirmed: $a(n)/n \to 1-\gamma \approx 0.4228$ as $n\to\infty$ (checked to $n=10^4$). So $a(n)$ is **not** bounded — it grows linearly. The genuinely bounded-looking, oscillating quantity is the *residual* after removing this trend:

$$\Delta^*(n) := a(n) - (1-\gamma)n,$$

which sits inside the classical $\pm\sqrt n$ envelope — this **is** (up to sign and lower-order constants) the famous Dirichlet divisor problem error term $\Delta(n)$, unsolved in exact order since 1849. Proven best bound: $O(n^{0.3149\ldots})$ (Huxley/Bourgain–Watt-type methods); conjectured optimal (Hardy): $O(n^{1/4+\varepsilon})$, with a matching proven **lower** bound $\Omega(n^{1/4})$.

### Where that $1/4$ actually comes from (a different mechanism from §4)

Voronoi's 1904 formula:
$$\Delta(x) = \frac{x^{1/4}}{\sqrt2\,\pi}\sum_n \frac{d(n)}{n^{3/4}}\cos\!\big(4\pi\sqrt{nx}-\tfrac\pi4\big) + \text{error}.$$
The $x^{1/4}$ exponent arises from **compounding two independent square-root decay rates**: the Bessel-function argument scales like $\sqrt x$, and Bessel functions themselves decay like (argument)$^{-1/2}$ for large argument — $(x^{1/2})^{1/2}=x^{1/4}$. This is a genuine, fully understood classical mechanism (the *open* part is only whether the conjectured exponent is tight) — structurally unrelated to the additive $(\tfrac12)^2$ from §4, despite sharing the digit.

## 6. Fourier construction of the sawtooth (the correct route to Voronoi)

Classical sawtooth series: $\{x\} = \tfrac12 - \sum_{m=1}^\infty \frac{\sin(2\pi mx)}{\pi m}$.

Applied termwise:
$$a(n) = \frac n2 - \sum_{k=1}^n\sum_{m=1}^\infty \frac{\sin(2\pi mn/k)}{\pi m}.$$

Verified numerically: truncating at $M$ harmonics per term converges to the true (jump-discontinuous) $a(n)$ as $M\to\infty$, with visible Gibbs-phenomenon overshoot near jumps — the expected, correct signature of a genuine trigonometric approximation to a discontinuous function. **This double sum is literally the historical starting point of Voronoi's derivation**: swapping the order of summation and evaluating the resulting exponential sum over $k$ via Poisson summation / stationary phase is exactly what produces the Bessel-function formula in §5.

## 7. The main result: V4/mod-12 character reduces to a *solved* classical problem

The four Dirichlet characters mod 12 form the group $(\mathbb Z/12)^\times \cong V_4$ (all real-valued, since every element has order dividing 2). $\chi_{12} = \chi_{-4}\cdot\chi_{-3}$ is the nontrivial element built from both flips — the same object identified earlier in the session as $\mathrm{Gal}(\mathbb Q(i,\sqrt3)/\mathbb Q)$.

Weighting the sawtooth sum by $\chi_{12}$:
$$\sum_{k\le n}\chi_{12}(k)\{n/k\} \;=\; \underbrace{n\sum_{k\le n}\frac{\chi_{12}(k)}k}_{\text{piece 1}} \;-\; \underbrace{\sum_{k\le n}\chi_{12}(k)\Big\lfloor\frac nk\Big\rfloor}_{\text{piece 2}}$$

**Verified numerically** (exact computation, no approximation): both pieces individually grow linearly at rate $n\cdot L(1,\chi_{12})\approx 0.760\,n$ (matching the class-number-formula value $L(1,\chi_{12}) = 2h(12)\log(2+\sqrt3)/\sqrt{12}$), and they **cancel almost completely**:

| $n$ | residual | $n^{1/3}$ | $\sqrt n$ |
|---:|---:|---:|---:|
| $10^5$ | 3.6 | 46.4 | 316 |
| $10^6$ | $-5.0$ | 100.0 | 1000 |
| $10^7$ | 32.0 | 215.4 | 3162 |

### Identification and proven bound

$\sum_{d\mid m}\chi_{12}(d)$ is exactly the Dirichlet-series coefficient of the **Dedekind zeta function** $\zeta_{\mathbb Q(\sqrt3)}(s) = \zeta(s)L(s,\chi_{12})$ — so piece 2 is literally the number of ideals of $\mathbb Z[\sqrt3]$ of norm $\le n$. This is a *classical, solved* problem (Landau 1918, refined since): for a degree-$d$ number field,
$$\#\{\mathfrak a : N(\mathfrak a) < X\} = c_K X + O\big(|\mathrm{Disc}(K)|^{1/(d+1)}X^{(d-1)/(d+1)}(\log X)^{d-1}\big).$$
For $d=2$: exponent $=(d-1)/(d+1) = \mathbf{1/3}$ — **proven**, not conjectural. The measured residuals above sit comfortably inside this bound at every tested scale.

**Why this differs from the plain divisor problem:** $D(n)$'s Dirichlet series is $\zeta(s)^2$, with a *double* pole at $s=1$ (source of the still-open $x^{1/4}$ conjecture). Twisting by the nonprincipal character $\chi_{12}$ replaces this with $\zeta(s)L(s,\chi_{12})$, a *simple* pole — and simple-pole ideal-counting problems have been fully handled by classical methods for over a century.

---

## Summary

| Object | Status |
|---|---|
| $D(n) = nH_n - \sum\{n/k\}$ | Classical identity, verified exactly |
| GeoGebra "mod 0.5" construction | Verified exactly equivalent to the above |
| $T_n - D(n) = 43$ at $n=12$ | Confirmed as OEIS A161664 (real, cited "prime safe" sequence) |
| Smooth real-variable extension $S(x)$ | Constructed and verified, tracks $D(n)$ within $O(\sqrt n)$ |
| Pronic/diagonal $(\tfrac12)^2$ identity | Verified; 6th confirmed appearance of the additive quarter-shift |
| $a(n)$ boundedness claim | **Corrected**: grows linearly at rate $1-\gamma$, not bounded |
| Residual $a(n)-(1-\gamma)n$ | This *is* the classical open $\Delta(n)$, $O(n^{1/4+\varepsilon})$ conjectured |
| Voronoi $x^{1/4}$ exponent | Verified real mechanism (Bessel asymptotics); unrelated to the additive quarter-shift |
| Fourier series of the sawtooth | Verified buildup; literal starting point of Voronoi's method |
| **$\chi_{12}$-twisted residual** | **Identified exactly as ideal-counting error for $\mathbb Q(\sqrt3)$; proven $O(n^{1/3})$ bound, confirmed numerically** |

The last row is the one substantive, mechanistically-explained connection between the project's $V_4$/mod-12 structure and the divisor-function machinery found across this whole exploration — and unlike the earlier candidate connections tested in this session (which did not hold up under direct computation), this one resolves into an actual, correct, citable theorem.
