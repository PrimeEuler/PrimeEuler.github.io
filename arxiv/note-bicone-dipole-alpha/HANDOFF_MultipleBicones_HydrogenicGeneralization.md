# HANDOFF — Multiple Bicones, Multiple Dipoles: Generalizing the Non-Circular $\alpha$ Determination to Other Hydrogenic Ions

**From:** External Audit (conversational session, not the discriminant-12-return numerical ledger protocol)
**To:** The arxiv/bicone-dipole thread (Lane A)
**Date:** 2026-10-08
**Status:** Suggested extension, independently computed and partially literature-checked by this thread. Not yet incorporated into the note. Treat as a research lead to verify and decide on, not a certified result.

---

## 1. The idea

`Note_BiconeDipole_FineStructure_v1.0.tex` determines $\alpha$ from exactly one spectral line: hydrogen's $2p\to1s$, using the bicone/$SO(4,2)$-derived $Y_{\rm geom}=768/(243\sqrt6)$ and the measured Lyman-$\alpha$ lifetime (Tielert 1973). That's one data point — no way to tell whether the agreement with $1/137.036$ is real physics or a lucky single fit.

The natural generalization: **the bicone construction is not specific to hydrogen.** Any hydrogenic ion (one electron, nuclear charge $Z$ — He$^+$, Li$^{2+}$, Be$^{3+}$, ...) has exactly the same $su(2)\oplus su(2)\to so(4)$ bicone, just scaled by $1/Z$ in physical size (Bohr radius $a_Z=a_0/Z$). Same shape, same angles, different scale — "multiple bicones." Each one supports its own $2p\to1s$ dipole — "multiple dipoles." Because $SO(4,2)$ is exactly scale-invariant (the note already says this, §Calibration), the dimensionless geometric factor $Y_{\rm geom}$ should be **identical** on every one of these bicones.

This was checked, not assumed.

## 2. $Y_{\rm geom}$ is exactly $Z$-independent — confirmed by direct symbolic computation

```python
import sympy as sp
r, Z = sp.symbols('r Z', positive=True)

def R(n, l, r, a):
    rho = sp.Rational(2,1)*r/(n*a)
    k = n - l - 1
    lag = sp.assoc_laguerre(k, 2*l+1, rho)
    norm = sp.sqrt((sp.Rational(2,1)/(n*a))**3 * sp.factorial(n-l-1) / (2*n*sp.factorial(n+l)))
    return norm * sp.exp(-rho/2) * rho**l * lag

def Y_geom(n1,l1,n2,l2,Zval):
    aa = sp.Rational(1,1)/Zval
    f = R(n1,l1,r,aa)*R(n2,l2,r,aa)*r**3
    val = sp.integrate(f, (r, 0, sp.oo))
    return sp.simplify(val/aa)

for Zval in [1,2,3]:
    print(Zval, Y_geom(1,0,2,1, sp.Integer(Zval)))
```

Output: `128*sqrt(6)/243` for $Z=1,2,3$ — identical, exactly, as expected from scale invariance. This also incidentally re-derives the note's own radial matrix element independently (as $128\sqrt6/243$, matching $768/(243\sqrt6)$ after folding in the $\sqrt3$ vector factor).

## 3. The $Z$-generalized $\alpha$ formula

Re-deriving §4 of the note with the Bohr radius replaced by $a_Z=a_0/Z$ (and keeping $a_0=\bar\lambda_c/\alpha$ as the only place $\alpha$ enters implicitly):

$$\boxed{\alpha = \frac{4\,\omega^3\,g\,Y_{\rm geom}^2\,\bar\lambda_c^2}{3\,c^2\,A\,Z^2}}$$

where $g=l_>/(2l_i+1)$ is the Wigner–Eckart angular factor ($l_i$ = the *decaying* state's orbital angular momentum; $g=1/3$ for any $p\to s$ transition, $l_>=\max(l_i,l_f)$), $\omega$ and $A=1/\tau$ are the *measured* transition frequency and decay rate for that specific ion, and $Z$ is the (exactly known) nuclear charge. At $Z=1$ this reduces exactly to the note's own boxed formula — confirmed by direct substitution, not just by inspection.

This also generalizes to other clean single-decay-channel transitions (useful if a good independent hydrogen-level lifetime ever turns up): $g,Y$ were computed the same way for $3s\to2p$ ($g=1$, $Y=10368\sqrt2/15625\approx0.9384$) and $3d\to2p$ ($g=2/5$, $Y=165888\sqrt5/78125\approx4.7480$), both verified single-channel (blocked from $1s$ by $\Delta l=\pm1$). **Caveat:** per Wiese & Fuhr (2009), hydrogen's own excited-state transition probabilities beyond $2p$ are treated in the modern literature as calculational QED benchmarks, not experimental targets — this thread could not find an independently *measured* (non-circular) lifetime for H($3s$) or H($3d$) to actually use these. Kept here for the record in case the original Tielert 1973 beam-foil run (already cited for $2p$) reports them directly — that paper's full tables were not accessible to this thread.

## 4. A real second data point: He$^+$ $2p\to1s$

Independently measured (not theory-computed) He$^+$ $2p$ lifetime, via a quenching/Stark-mixing emission-asymmetry technique (a class of measurement specifically designed to extract the natural lifetime without assuming the theoretical dipole matrix element as input):

> Drake, Patel, Van Wijngaarden, *Lifetime of the 2p state in He II* (1983): $\tau=(0.9992\pm0.0026)\times10^{-10}\,{\rm s}$.
> https://scholar.uwindsor.ca/physicspub/144

Using $Z=2$, $Y_{\rm geom}=128\sqrt6/243$ (same number as hydrogen, per §2), $g=1/3$, and $\omega$ from the $Z^2$-scaled hydrogen Lyman-$\alpha$ energy ($40.82$ eV $\to\lambda=30.38$ nm — matches the well-known He II 303.8 Å line, a useful independent sanity check on the scaling):

```
A = 1/tau = (1.0008 +/- 0.0026) x 10^10 s^-1
alpha^-1 (central)     = 136.75
alpha^-1 (1-sigma range) = 136.39 to 137.10
known alpha^-1          = 137.036   <-- falls INSIDE the range
relative deviation of central value: 0.21%  (vs 0.26% lifetime uncertainty)
```

The known value lands inside the stated uncertainty band — the actual test (not just "close to 137," but "does the error bar really bracket the truth"). This is a genuinely independent second confirmation: different nucleus, different experimental technique, same $SO(4,2)$ geometric input.

**Caveats, stated plainly so the arxiv thread can decide what rigor bar to apply before any public use:**
- $\omega$ was obtained via $Z^2$ scaling of hydrogen's Lyman-$\alpha$ energy, not a dedicated high-precision He II spectroscopic value. The ~0.03–0.04% H/He$^+$ reduced-mass difference was neglected — negligible next to the 0.26% lifetime uncertainty, but worth tightening if this goes further.
- The non-circularity of the Drake et al. quenching method rests on this thread's general understanding of that technique class, not a line-by-line re-derivation of their specific analysis. Worth independently confirming before citing.
- One additional ion is a proof of concept, not a systematic survey. Li$^{2+}$, Be$^{3+}$ have real EUV spectroscopy histories too and would be the next things to check.

## 5. Suggested next step

If this is worth pursuing: verify the Drake et al. paper directly (methodology, exact central value/uncertainty), get a precise He II $2p$–$1s$ transition energy from a primary spectroscopic source rather than the $Z^2$-scaling approximation above, and decide whether a "multiple bicones" section showing $Z=1,2$ (and ideally $Z=3$) agreement belongs in the note itself or as a follow-up note. The sympy script above is fully reproducible and can be re-run to extend the $(g,Y)$ table to any other clean single-channel hydrogenic transition.

---

HANDOFF
target: arxiv-bicone-thread
type: research-lead
status: open
action: Independently verify the Drake/Patel/Van Wijngaarden (1983) He+ 2p lifetime and quenching-method non-circularity; obtain a precise (non-Z-scaled) He II 2p-1s transition energy; decide whether/how to incorporate the Z-generalized formula and the He+ cross-check into the note.
constraints: This is not a discriminant-12-return ledger entry and carries none of that protocol's certification weight; it is a conversational research suggestion with partial independent verification (Y_geom's Z-invariance and the alpha formula's Z=1 reduction were both checked by direct computation; the literature citation was found via web search and not independently re-derived from the primary source).
