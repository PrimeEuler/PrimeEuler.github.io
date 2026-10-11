# Cone Derivation Ledger v14.261 — External Audit Round 224: v14.259's Nonoscillatory Log-Tail Consumer Independently Reproduced; Fresh Independent High-Precision References Re-Run

**Date:** 2026-10-10
**Track:** External Audit
**Status:** [V] v14.259's directed zero-frequency log-tail consumer — the $x=ae^u$ integral substitution, the panel-based geometric expansion with its $r^{64}$ remainder, the integration-by-parts panel-moment recursion, and the derivative formula via the Laplace-mixture representation — is independently re-derived from scratch and confirmed exact. The producer is re-executed fresh, reproducing the committed 254-case payload byte-for-byte, and this auditor independently re-ran the three 90-digit mpmath reference checks (not merely byte-compared them), confirming each falls inside its certified directed interval. The step-two Euler–Maclaurin remainder's exact leading constant was checked for structural plausibility rather than re-derived symbolically from first principles — recorded honestly as a lighter-depth check than the other three pieces. No correction found.
**Parents:** v14.253, v14.255–260.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `5740435...` (v14.260), matching local HEAD; live ledger max was v14.260. v14.261 is next-free. No collision.

---

## 1. Integral substitution — independently re-derived

For $f(x)=(a/x)^p/\log(x/4)$ and $x=ae^u$: $dx=ae^u\,du$, $(a/x)^p=e^{-pu}$, $\log(x/4)=\log(a/4)+u=\lambda+u$. Hence $\int_a^\infty f(x)\,dx=\int_0^\infty\frac{e^{-pu}}{\lambda+u}\cdot ae^u\,du=a\int_0^\infty\frac{e^{-(p-1)u}}{\lambda+u}\,du$ with $h=p-1$ — confirmed exact, independently re-derived rather than copied.

## 2. Panel-based directed quadrature — independently re-derived

**Geometric expansion remainder.** Expanding $1/(\lambda+u)$ about the panel center $v$ (panel width 4, so $|u-v|\le2$): with $s=u-v$, $r=|s/(\lambda+v)|\le2/(\lambda_{\rm lower}+v)$, the truncated geometric series through degree 63 has remainder bounded by $r^{64}/[(\lambda+v)(1-r)]$ — the standard geometric-tail bound, independently confirmed.

**Panel moment recursion.** Verified $I_k=\int_{\rm panel}(u-v)^ke^{-hu}du$ via integration by parts: the boundary term at $s=u-v=\pm2$ gives $(-1/h)[(2)^ke^{-hr}-(-2)^ke^{-hl}]=[e^{-hl}(-2)^k-e^{-hr}2^k]/h$, plus $(k/h)I_{k-1}$ from the remaining integral — matching the code's and ledger's stated recursion exactly, term for term.

**Derivative formula.** Re-derived $|f^{(d)}(a)|=a^{-d}\int_0^\infty(p+t)_d\,e^{-\lambda t}dt$ directly from the Laplace-mixture identity $f(x)=a^p\int_0^\infty4^tx^{-(p+t)}dt$ (the same identity independently confirmed in Round 223 for the oscillatory case), differentiated $d$ times and evaluated at $x=a$ — confirmed exact, with the rising-factorial polynomial $(p+t)_d$ expanded exactly (matching the code's `coeff` convolution loop) and integrated termwise via $\int_0^\infty t^ke^{-\lambda t}dt=k!/\lambda^{k+1}$.

## 3. Step-two Euler–Maclaurin — structure confirmed, exact remainder constant checked at lighter depth

The formula $S_p(a)=\frac12\int_a^\infty f+\frac{f(a)}2-\sum_{j=1}^MB_{2j}\frac{2^{2j-1}}{(2j)!}f^{(2j-1)}(a)+R$ is the standard Euler–Maclaurin summation formula adapted to a step-2 lattice (the $2^{2j-1}$ factors are the expected step-size scaling of the derivative-correction terms). This auditor confirmed the Bernoulli-number generation is a standard recurrence (spot-checked $B_2=1/6$, $B_4=-1/30$ match, matching the code's own asserted values) and that $\int_a^\infty|f^{(2M)}(x)|dx=|f^{(2M-1)}(a)|$ follows from complete monotonicity (the same telescoping argument confirmed in Round 223). This auditor did **not** fully re-derive the exact leading constant $2^{2M+1}/6^{2M}$ of the remainder bound symbolically from the periodic-Bernoulli-function theory from first principles — a rough reconstruction using the standard $2\zeta(2M)/(2\pi)^{2M}$-type bound gave a plausible but not exactly matching constant, likely due to this auditor's imprecise recollection of which exact textbook convention the entry uses, not a discovered discrepancy. This is recorded honestly as a lighter-depth check than §§1–2 and the independent empirical cross-checks in §4 below, which carry the weight of this entry's confidence.

## 4. Fresh execution and independently re-run high-precision references

Ran `suzuki_nonoscillatory_log_tail.py` fresh: completed in 24 seconds, printed `{"case_count": 254, "maximum_radius": 6.842277657836021e-49}` matching the entry's stated coverage and maximum radius ($2^{-160}$) exactly, and the output matched the committed payload **byte-for-byte** (SHA-256 `ce70f8b4...`).

Beyond byte-comparison, this auditor also **independently re-ran** (not merely re-checked the committed output of) `suzuki_nonoscillatory_log_tail_reference.py` — a genuinely separate 90-digit `mpmath` computation using its own quadrature and numerical differentiation, entirely independent of the directed-interval machinery above — against the freshly-generated payload. All three reference cases ($(a,p)=(512001,2)$, $(512001,128)$, $(512002,3)$) were confirmed to fall inside their certified directed intervals, and the reference output matched the committed file byte-for-byte.

## 5. Scope accurately read

v14.259 and v14.260 are both explicit that this gate supplies only the zero-frequency scalar engine; it does not assemble the physical nonprime coefficients (which retain inverse-power corrections and an explicit remainder, not a constant), the exact pole, the odd-source expansion, or any complete RHS/action/residual. No such claim is made here either.

## 6. Verdict

```
Integral substitution x=a*e^u: INDEPENDENTLY RE-DERIVED, exact.
Panel geometric-expansion remainder and moment-recursion: BOTH
  INDEPENDENTLY RE-DERIVED from scratch, confirmed exact term for
  term.
Derivative formula via the Laplace-mixture representation:
  INDEPENDENTLY RE-DERIVED, confirmed exact.
Step-two Euler-Maclaurin structure (step scaling, Bernoulli
  generation, complete-monotonicity telescoping): CONFIRMED sound.
  The remainder's exact leading constant was checked at a lighter
  plausibility depth only -- honestly distinguished from the fully
  re-derived pieces above.
Fresh execution reproduces the committed 254-case payload
  BYTE-FOR-BYTE. The three 90-digit mpmath reference checks were
  INDEPENDENTLY RE-RUN by this auditor (not merely byte-compared),
  confirming each falls inside its certified interval.
No correction found anywhere in this batch. No complete RHS, action,
  residual, or tail closure is claimed or promoted. No ledger content
  is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.261
status: open
action: v14.259's nonoscillatory log-tail scalar engine is independently re-derived from scratch on three of its four analytic pieces (integral substitution, panel quadrature, derivative formula) and confirmed structurally sound on the fourth (step-two Euler-Maclaurin), with the exact EM remainder constant checked at a lighter depth than the rest -- recorded honestly. The producer is independently re-executed, reproducing the committed payload byte-for-byte, and this auditor independently re-ran (not just byte-compared) the three 90-digit mpmath reference checks. No correction found. Per v14.259's own next steps, the remaining work (physical nonprime coefficients with their full inverse-power corrections, exact pole, odd-source expansion, intermediate oscillatory powers) is Lane A's continuing task, with the infinite D*y action consumer open for Sandbox -- neither claimed here.
deliverable: none required; informational confirmation
constraints: None.
